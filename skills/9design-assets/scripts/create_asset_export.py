#!/usr/bin/env python3
"""Create a separated image asset export scaffold for website builds."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime
from pathlib import Path


FOLDERS = [
    "00-source-kit",
    "01-logos",
    "02-icons",
    "03-ui-elements",
    "04-backgrounds",
    "05-page-assets",
    "06-ready-for-builder",
    "notes",
]


DEFAULT_ASSETS = [
    ("logo-primary", "logo", "01-logos", "Primary logo image", "transparent-preferred"),
    ("logo-wordmark", "logo", "01-logos", "Wordmark image", "transparent-preferred"),
    ("logo-mark", "logo", "01-logos", "Icon mark image", "transparent-preferred"),
    ("favicon", "logo", "01-logos", "Favicon/app icon image", "transparent-preferred"),
    ("icon-01-primary", "icon", "02-icons", "Core icon 1", "transparent-preferred"),
    ("icon-02-secondary", "icon", "02-icons", "Core icon 2", "transparent-preferred"),
    ("icon-03-action", "icon", "02-icons", "Core icon 3", "transparent-preferred"),
    ("icon-04-navigation", "icon", "02-icons", "Core icon 4", "transparent-preferred"),
    ("icon-05-accent", "icon", "02-icons", "Core icon 5", "transparent-preferred"),
    ("social-icon-set", "icon", "02-icons", "Matched social/community icon treatment", "transparent-preferred"),
    ("button-primary", "ui-element", "03-ui-elements", "Primary button image", "isolated-component"),
    ("button-secondary", "ui-element", "03-ui-elements", "Secondary button image", "isolated-component"),
    ("nav-desktop", "ui-element", "03-ui-elements", "Desktop navigation image", "isolated-component"),
    ("nav-mobile", "ui-element", "03-ui-elements", "Mobile navigation image", "isolated-component"),
    ("card-default", "ui-element", "03-ui-elements", "Card component image", "isolated-component"),
    ("form-input", "ui-element", "03-ui-elements", "Form input image", "isolated-component"),
    ("cta-banner", "ui-element", "03-ui-elements", "CTA banner image", "component-internal-background"),
    ("footer-module", "ui-element", "03-ui-elements", "Footer module image", "component-internal-background"),
    ("hero-background", "background", "04-backgrounds", "Hero background image", "full-bleed-background"),
    ("section-texture", "texture", "04-backgrounds", "Section texture image", "full-bleed-background"),
    ("decorative-divider", "overlay", "04-backgrounds", "Decorative divider image", "transparent-preferred"),
]


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "asset-export"


def asset_role(asset_type: str, background_policy: str) -> str:
    if asset_type == "logo":
        return "logo"
    if asset_type == "icon":
        return "icon"
    if asset_type == "background":
        return "background"
    if asset_type == "texture":
        return "texture"
    if asset_type == "overlay":
        return "transparent-overlay"
    if background_policy in {"isolated-component", "component-internal-background"}:
        return "ui-chrome"
    return "foreground-object"


def responsive_variants(asset_type: str, asset_id: str) -> list[str]:
    if asset_type in {"background", "texture"}:
        return ["desktop", "tablet", "mobile"]
    if asset_id in {"nav-desktop", "nav-mobile", "cta-banner", "footer-module", "card-default"}:
        return ["desktop", "tablet", "mobile"]
    if asset_type == "logo":
        return ["desktop", "mobile"]
    return ["not-applicable"]


def accessibility_notes(asset_type: str, asset_id: str) -> dict:
    if asset_type == "logo":
        return {
            "alt_text": "Fill with brand name from the approved design.",
            "decorative": False,
            "aria_label": "",
            "hidden_text_required": asset_id == "logo-wordmark",
        }
    if asset_type == "icon":
        return {
            "alt_text": "",
            "decorative": False,
            "aria_label": "Fill with the icon meaning or platform name.",
            "hidden_text_required": False,
        }
    if asset_type in {"background", "texture", "overlay"}:
        return {
            "alt_text": "",
            "decorative": True,
            "aria_label": "",
            "hidden_text_required": False,
        }
    return {
        "alt_text": "",
        "decorative": True,
        "aria_label": "",
        "hidden_text_required": False,
    }


def token_dependencies(asset_type: str, asset_id: str) -> list[str]:
    dependencies = ["colors"]
    if asset_type in {"logo", "icon"}:
        dependencies.extend(["icon-size", "optical-padding"])
    if asset_type == "ui-element" or asset_id in {"cta-banner", "footer-module"}:
        dependencies.extend(["typography", "radius", "shadow", "spacing"])
    if asset_type in {"background", "texture", "overlay"}:
        dependencies.extend(["gradient", "texture", "opacity"])
    return dependencies


def icon_policy(asset_type: str, asset_id: str) -> str:
    if asset_id == "social-icon-set":
        return "generated-transparent-png"
    if asset_type == "icon":
        return "generated-transparent-png"
    return "not-an-icon"


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def copy_source_kit(source: Path, dest: Path) -> str | None:
    if not source.exists():
        return None

    if source.is_file():
        target = dest / source.name
        shutil.copy2(source, target)
        return str(target)

    summary = dest / "source-kit-path.txt"
    summary.write_text(str(source), encoding="utf-8")

    manifest = source / "asset-manifest.json"
    export_manifest = source / "asset-export-manifest.json"
    for candidate in [manifest, export_manifest]:
        if candidate.exists():
            shutil.copy2(candidate, dest / candidate.name)

    for folder_name in ["00-reference", "07-export-sheets", "01-logo", "02-icons"]:
        folder = source / folder_name
        if folder.exists() and folder.is_dir():
            target = dest / folder_name
            shutil.copytree(folder, target, dirs_exist_ok=True)

    return str(source)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create separated image asset export scaffold.")
    parser.add_argument("--name", required=True, help="Project or export name.")
    parser.add_argument("--root", default=".", help="Workspace root for asset-exports/.")
    parser.add_argument("--source-kit", default="", help="Optional reference asset kit path.")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    export_dir = root / "asset-exports" / f"{slugify(args.name)}-{timestamp}"
    export_dir.mkdir(parents=True, exist_ok=False)

    for folder in FOLDERS:
        (export_dir / folder).mkdir(parents=True, exist_ok=True)

    source_record = None
    if args.source_kit:
        source_record = copy_source_kit(Path(args.source_kit).expanduser().resolve(), export_dir / "00-source-kit")

    assets = []
    for asset_id, asset_type, folder, description, background_policy in DEFAULT_ASSETS:
        alpha_required = background_policy in {
            "transparent-preferred",
            "isolated-component",
            "component-internal-background",
        }
        assets.append(
            {
                "id": asset_id,
                "type": asset_type,
                "folder": folder,
                "path": f"{folder}/{asset_id}.png",
                "expected_file": f"{asset_id}.png",
                "clean_file": f"{asset_id}.png",
                "ready_file": f"06-ready-for-builder/{asset_id}.png",
                "status": "pending-imagegen",
                "use": description,
                "asset_role": asset_role(asset_type, background_policy),
                "responsive_variants": responsive_variants(asset_type, asset_id),
                "accessibility": accessibility_notes(asset_type, asset_id),
                "token_dependencies": token_dependencies(asset_type, asset_id),
                "icon_policy": icon_policy(asset_type, asset_id),
                "background_policy": background_policy,
                "alpha_required": alpha_required,
                "background_cleanup_required": alpha_required,
                "background_cleaned": False,
                "alpha_verified": False,
                "background_removal_needed": False,
                "background_removal_method": "",
                "source_reference": source_record,
                "prompt_summary": "",
                "text_policy": "no-text",
                "accessible_text": "",
                "interaction_state": "not-applicable",
                "qa_notes": [],
                "notes": "",
            }
        )

    manifest = {
        "manifest_schema_version": "2.0",
        "project": args.name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "export_dir": str(export_dir),
        "source_kit": source_record,
        "process": [
            "reference-kit",
            "asset-plan",
            "scaffold-folder",
            "generate-each-image-with-imagegen",
            "package-for-builder",
        ],
        "assets": assets,
    }

    (export_dir / "asset-export-manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )

    write_if_missing(
        export_dir / "notes" / "asset-plan.md",
        "# Asset Plan\n\nGenerate each listed asset as its own imagegen output. For every asset with `background_cleanup_required: true`, run `remove_background.py` and verify `alpha_verified: true` before copying it into `06-ready-for-builder/`. Update `asset-export-manifest.json` after each asset is saved and cleaned. Run `validate_asset_manifest.py` before website handoff so missing roles, responsive variants, accessibility notes, token dependencies, icon policy, and QA notes are visible.\n",
    )
    write_if_missing(
        export_dir / "notes" / "generation-prompts.md",
        "# Generation Prompts\n\nRecord the prompt summary for each generated image asset.\n",
    )
    write_if_missing(
        export_dir / "notes" / "font-and-token-notes.md",
        "# Font And Token Notes\n\nReference the source kit tokens and fonts. Do not guess exact fonts without evidence.\n",
    )
    write_if_missing(
        export_dir / "notes" / "builder-handoff.md",
        "# Builder Handoff\n\nUse `06-ready-for-builder/` and `asset-export-manifest.json` as input for the website-building skill.\n",
    )
    write_if_missing(
        export_dir / "notes" / "icon-inventory.md",
        "# Icon Inventory\n\nRecord each core icon, its meaning, source reference, optical size, stroke/fill treatment, color, background cleanup status, and implementation notes.\n",
    )
    write_if_missing(
        export_dir / "notes" / "social-icons.md",
        "# Social Icons\n\nRecord each platform/community icon, source glyph or generated asset, container treatment, hover/active state, accessible label, and whether it is `official-vector`, `generated-transparent-png`, `custom-svg`, or `code-native`.\n",
    )

    print(json.dumps({"asset_export": str(export_dir), "source_kit": source_record}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
