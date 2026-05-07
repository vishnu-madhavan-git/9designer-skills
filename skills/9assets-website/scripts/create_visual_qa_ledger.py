#!/usr/bin/env python3
"""Create or update a 9Designer visual QA ledger.

This script is dependency-free. It can consume screenshot capture summaries or
pixel diff summaries, but it also works as a manual QA ledger template.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any


CATEGORIES = [
    "layout",
    "spacing",
    "typography",
    "color",
    "asset",
    "icon",
    "interaction",
    "responsive behavior",
]

CHECKPOINTS = [
    ("copy", "Visible copy matches the approved prototype and no placeholder text remains."),
    ("layout", "Section order, hierarchy, and major composition match the approved prototype."),
    ("typography", "Font family/fallback, weight, size, line-height, and tracking match the design intent."),
    ("color", "Backgrounds, surfaces, text, accents, gradients, and overlays match exported tokens."),
    ("asset", "Logos, hero art, cards, textures, and overlays use the cleaned local assets."),
    ("icon", "Core icons and social/community icons match source glyphs, weight, padding, and state."),
    ("spacing", "Container width, section rhythm, gaps, padding, and alignment match the reference."),
    ("responsive behavior", "Desktop, tablet, and mobile preserve hierarchy without overflow or overlap."),
    ("interaction", "Navigation, menu, links, buttons, forms, filters, and hover/focus states work."),
    ("motion", "Motion supports the design and respects reduced-motion behavior."),
]


def load_json(path: Path | None) -> dict[str, Any]:
    if not path:
        return {}
    path = path.expanduser().resolve()
    if not path.exists():
        raise SystemExit(f"Summary JSON does not exist: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: str | Path | None, base: Path) -> str:
    if not path:
        return ""
    value = Path(path)
    if not value.is_absolute():
        return str(value).replace("\\", "/")
    try:
        return str(value.relative_to(base)).replace("\\", "/")
    except ValueError:
        return str(value).replace("\\", "/")


def comparison_rows(summary: dict[str, Any], base: Path) -> list[str]:
    rows = []

    if summary.get("comparisons"):
        for item in summary["comparisons"]:
            ratio = item.get("mismatch_ratio")
            ratio_text = "n/a" if ratio is None else f"{ratio:.4%}"
            categories = ", ".join(item.get("category_suggestions") or [])
            rows.append(
                "| {viewport} | {status} | {ratio} | {diff} | {categories} |".format(
                    viewport=item.get("file", ""),
                    status=item.get("status", "needs-manual-review"),
                    ratio=ratio_text,
                    diff=rel(item.get("diff_file"), base),
                    categories=categories or "manual review",
                )
            )
        return rows

    if summary.get("screenshots"):
        for item in summary["screenshots"]:
            rows.append(
                "| {viewport} | captured | n/a | {file} | manual review |".format(
                    viewport=item.get("name", ""),
                    file=rel(item.get("file"), base),
                )
            )
    return rows


def build_markdown(args: argparse.Namespace, summary: dict[str, Any], out_path: Path) -> str:
    base = out_path.parent
    generated_at = datetime.now().isoformat(timespec="seconds")
    rows = comparison_rows(summary, base)
    if not rows:
        rows = [
            "| desktop | pending | n/a |  | manual review |",
            "| tablet | pending | n/a |  | manual review |",
            "| mobile | pending | n/a |  | manual review |",
        ]

    category_lines = "\n".join(f"- `{category}`: " for category in CATEGORIES)
    checkpoint_lines = "\n".join(
        f"- [ ] `{category}` - {description}" for category, description in CHECKPOINTS
    )

    capture_summary = rel(summary.get("output_dir"), base)
    reference_dir = rel(args.reference_dir, base)
    actual_dir = rel(args.actual_dir or summary.get("actual_dir"), base)
    diff_dir = rel(args.diff_dir or summary.get("output_dir"), base)

    return f"""# Visual QA Ledger

Project: {args.project}
Generated: {generated_at}

Manual visual review remains required. Automated screenshots and diffs are helpers, not final approval.

## Inputs

- Website root: `{rel(args.website_root, base) or "."}`
- Asset export: `{rel(args.asset_export, base) or "not recorded"}`
- Reference screenshot directory: `{reference_dir or "not recorded"}`
- Actual screenshot directory: `{actual_dir or "not recorded"}`
- Diff directory: `{diff_dir or "not recorded"}`
- Summary source: `{rel(args.summary, base) or "none"}`
- Capture/diff output: `{capture_summary or "not recorded"}`

## Automated Artifacts

| Viewport/File | Status | Mismatch ratio | Artifact | Suggested categories |
| --- | --- | ---: | --- | --- |
{chr(10).join(rows)}

## Mismatch Categories

Use these categories for every issue found:

{category_lines}

## Manual Comparison Checklist

{checkpoint_lines}

## Repair Log

| Date | Category | Issue | Fix | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  | pending |

## Unresolved Blockers

- None recorded yet.

## Final Review Notes

- Desktop target: around 1440px wide unless the approved reference uses another size.
- Tablet target: around 768px wide.
- Mobile target: around 390px wide.
- Record any viewport that cannot be matched exactly and explain the nearest practical comparison.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a 9Designer visual QA ledger.")
    parser.add_argument("--project", default="", help="Project name for the ledger.")
    parser.add_argument("--website-root", default=".", help="Website project root.")
    parser.add_argument("--asset-export", default="", help="Asset export folder used by the website.")
    parser.add_argument("--summary", default="", help="Optional capture or diff summary JSON.")
    parser.add_argument("--reference-dir", default="", help="Approved reference screenshot directory.")
    parser.add_argument("--actual-dir", default="", help="Rendered screenshot directory.")
    parser.add_argument("--diff-dir", default="", help="Diff artifact directory.")
    parser.add_argument(
        "--out",
        default="docs/research/VISUAL_QA_LEDGER.md",
        help="Output markdown path.",
    )
    args = parser.parse_args()

    website_root = Path(args.website_root).expanduser().resolve()
    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = website_root / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not args.project:
        args.project = website_root.name
    args.website_root = str(website_root)

    summary = load_json(Path(args.summary) if args.summary else None)
    markdown = build_markdown(args, summary, out_path)
    out_path.write_text(markdown, encoding="utf-8")

    print(json.dumps({"valid": True, "ledger": str(out_path)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
