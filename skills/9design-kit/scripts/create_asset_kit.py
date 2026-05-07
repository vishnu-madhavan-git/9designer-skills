#!/usr/bin/env python3
"""Create a website prototype asset-kit folder scaffold."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime
from pathlib import Path


FOLDERS = [
    "00-reference",
    "01-logo",
    "02-icons",
    "03-imagery",
    "04-ui-components",
    "05-fonts",
    "06-design-tokens",
    "07-export-sheets",
    "08-ready-for-build",
    "notes",
]


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "prototype-assets"


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an asset-kit scaffold.")
    parser.add_argument("--name", required=True, help="Project or prototype name.")
    parser.add_argument("--root", default=".", help="Workspace root for asset-kits/.")
    parser.add_argument(
        "--references",
        nargs="*",
        default=[],
        help="Optional reference image file paths to copy into 00-reference/.",
    )
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    kit_dir = root / "asset-kits" / f"{slugify(args.name)}-{timestamp}"
    kit_dir.mkdir(parents=True, exist_ok=False)

    for folder in FOLDERS:
        (kit_dir / folder).mkdir(parents=True, exist_ok=True)

    copied_refs = []
    for ref in args.references:
        source = Path(ref).expanduser().resolve()
        if source.exists() and source.is_file():
            dest = kit_dir / "00-reference" / source.name
            shutil.copy2(source, dest)
            copied_refs.append(str(dest))

    manifest = {
        "project": args.name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "asset_kit": str(kit_dir),
        "references": copied_refs,
        "assets": [],
        "fonts": [],
        "design_tokens": {},
        "notes": [
            "Update this manifest as assets are generated, authored, optimized, and moved into ready-for-build."
        ],
    }

    (kit_dir / "asset-manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )

    write_if_missing(
        kit_dir / "06-design-tokens" / "tokens.css",
        ":root {\n  /* Fill from extracted reference-image design system. */\n}\n",
    )
    write_if_missing(
        kit_dir / "05-fonts" / "font-notes.md",
        "# Font Notes\n\n- Exact candidate:\n- Nearest free alternative:\n- Fallback stack:\n- Confidence:\n- Source/licensing notes:\n",
    )
    write_if_missing(
        kit_dir / "notes" / "implementation-notes.md",
        "# Implementation Notes\n\n- Asset source images:\n- Visual rules:\n- Component notes:\n- Open questions:\n",
    )

    print(json.dumps({"asset_kit": str(kit_dir), "references": copied_refs}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
