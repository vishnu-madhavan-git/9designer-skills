#!/usr/bin/env python3
"""Validate 9Designer asset manifests without requiring optional tooling.

The validator is intentionally lightweight. It accepts older manifests, reports
Phase 2 fields as warnings by default, and turns warnings into failures only
when `--strict` is used.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ASSET_ROLES = {
    "background",
    "foreground-object",
    "transparent-overlay",
    "icon",
    "logo",
    "ui-chrome",
    "decorative-image-text",
    "code-native-reference",
    "texture",
}

ICON_POLICIES = {
    "official-vector",
    "generated-transparent-png",
    "custom-svg",
    "code-native",
    "not-an-icon",
}

TEXT_POLICIES = {
    "code-native-text",
    "decorative-image-text",
    "no-text",
}

PHASE2_ASSET_FIELDS = [
    "asset_role",
    "responsive_variants",
    "accessibility",
    "token_dependencies",
    "icon_policy",
    "qa_notes",
]


def resolve_manifest(path: Path) -> Path:
    path = path.expanduser().resolve()
    if path.is_file():
        return path

    for name in ["asset-export-manifest.json", "asset-manifest.json"]:
        candidate = path / name
        if candidate.exists():
            return candidate

    raise SystemExit(f"No asset manifest found at: {path}")


def note_missing(
    errors: list[str],
    warnings: list[str],
    strict: bool,
    message: str,
) -> None:
    if strict:
        errors.append(message)
    else:
        warnings.append(message)


def require_type(
    errors: list[str],
    value: Any,
    expected: type | tuple[type, ...],
    field: str,
    asset_id: str | None = None,
) -> None:
    if not isinstance(value, expected):
        prefix = f"asset `{asset_id}` " if asset_id else ""
        if isinstance(expected, tuple):
            expected_name = " or ".join(t.__name__ for t in expected)
        else:
            expected_name = expected.__name__
        errors.append(f"{prefix}`{field}` must be {expected_name}.")


def validate_asset(
    asset: dict[str, Any],
    index: int,
    manifest_dir: Path,
    check_files: bool,
    strict: bool,
    errors: list[str],
    warnings: list[str],
) -> None:
    asset_id = str(asset.get("id") or f"asset-{index}")

    for field in ["id", "type", "folder", "status"]:
        if field not in asset:
            note_missing(errors, warnings, strict, f"asset `{asset_id}` is missing `{field}`.")

    for field in PHASE2_ASSET_FIELDS:
        if field not in asset:
            note_missing(errors, warnings, strict, f"asset `{asset_id}` is missing Phase 2 field `{field}`.")

    if "asset_role" in asset and asset["asset_role"] not in ASSET_ROLES:
        errors.append(
            f"asset `{asset_id}` has unsupported asset_role `{asset['asset_role']}`."
        )

    if "responsive_variants" in asset:
        require_type(errors, asset["responsive_variants"], list, "responsive_variants", asset_id)

    if "accessibility" in asset:
        require_type(errors, asset["accessibility"], dict, "accessibility", asset_id)

    if "token_dependencies" in asset:
        require_type(errors, asset["token_dependencies"], (list, dict), "token_dependencies", asset_id)

    if "icon_policy" in asset and asset["icon_policy"] not in ICON_POLICIES:
        errors.append(
            f"asset `{asset_id}` has unsupported icon_policy `{asset['icon_policy']}`."
        )

    if "text_policy" in asset and asset["text_policy"] not in TEXT_POLICIES:
        errors.append(
            f"asset `{asset_id}` has unsupported text_policy `{asset['text_policy']}`."
        )

    if "qa_notes" in asset:
        require_type(errors, asset["qa_notes"], (list, str), "qa_notes", asset_id)

    if check_files:
        for path_field in ["path", "ready_file"]:
            rel_path = asset.get(path_field)
            if not rel_path:
                continue
            candidate = manifest_dir / str(rel_path)
            if not candidate.exists() and asset.get("status") != "pending-imagegen":
                warnings.append(f"asset `{asset_id}` references missing `{path_field}`: {rel_path}")


def validate_manifest(path: Path, check_files: bool, strict: bool) -> dict[str, Any]:
    manifest_path = resolve_manifest(path)
    manifest_dir = manifest_path.parent
    errors: list[str] = []
    warnings: list[str] = []

    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {
            "manifest": str(manifest_path),
            "valid": False,
            "errors": [f"Invalid JSON: {exc}"],
            "warnings": [],
        }

    require_type(errors, data, dict, "manifest root")

    for field in ["project", "created_at"]:
        if isinstance(data, dict) and field not in data:
            note_missing(errors, warnings, strict, f"manifest is missing `{field}`.")

    assets = data.get("assets", []) if isinstance(data, dict) else []
    require_type(errors, assets, list, "assets")

    if isinstance(assets, list):
        for index, asset in enumerate(assets):
            if not isinstance(asset, dict):
                errors.append(f"asset at index {index} must be an object.")
                continue
            validate_asset(asset, index, manifest_dir, check_files, strict, errors, warnings)

    kind = "asset-export" if manifest_path.name == "asset-export-manifest.json" else "asset-kit"
    if kind == "asset-export" and isinstance(data, dict) and "process" not in data:
        note_missing(errors, warnings, strict, "asset export manifest is missing `process`.")

    valid = not errors and not (strict and warnings)
    return {
        "manifest": str(manifest_path),
        "kind": kind,
        "valid": valid,
        "assets_checked": len(assets) if isinstance(assets, list) else 0,
        "strict": strict,
        "check_files": check_files,
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a 9Designer asset manifest.")
    parser.add_argument("path", help="Manifest file or folder containing an asset manifest.")
    parser.add_argument(
        "--check-files",
        action="store_true",
        help="Warn when non-pending assets reference files that do not exist.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat missing Phase 2 fields and other warnings as failures.",
    )
    args = parser.parse_args()

    result = validate_manifest(Path(args.path), args.check_files, args.strict)
    print(json.dumps(result, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
