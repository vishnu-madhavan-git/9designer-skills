#!/usr/bin/env python3
"""Create a reconstruction contract for exact image-to-website builds.

The contract makes the approved reference, target viewports, page map,
interaction expectations, and pass/fail gates explicit before coding starts.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


DEFAULT_VIEWPORTS = [
    ("desktop", 1440, 1100, "Primary desktop reconstruction target."),
    ("laptop", 1280, 900, "Common laptop sanity check."),
    ("ipad-pro", 1024, 1366, "iPad portrait target."),
    ("tablet", 768, 1024, "Tablet portrait target."),
    ("mobile", 390, 844, "Primary mobile target."),
    ("small-mobile", 360, 800, "Small mobile overflow target."),
]

DEFAULT_INTERACTIONS = [
    "desktop navigation links",
    "mobile menu open/close",
    "primary CTA",
    "secondary CTA",
    "footer links",
    "social/community links",
    "form input and submit state when present",
    "tabs, filters, carousel controls, accordions, or menus when present",
    "hover, focus, active, selected, disabled, and reduced-motion states when present",
]


def parse_page(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("Use route=reference, for example /=landing.png")
    route, reference = value.split("=", 1)
    route = route.strip() or "/"
    reference = reference.strip()
    if not reference:
        raise argparse.ArgumentTypeError("Reference path cannot be empty")
    return route, reference


def parse_viewport(value: str) -> tuple[str, int, int, str]:
    parts = value.split(":", 1)
    if len(parts) != 2 or "x" not in parts[1]:
        raise argparse.ArgumentTypeError("Use name:widthxheight")
    name = parts[0].strip()
    width, height = parts[1].split("x", 1)
    return name, int(width), int(height), "Custom viewport."


def markdown(args: argparse.Namespace, pages: list[tuple[str, str]], viewports: list[tuple[str, int, int, str]]) -> str:
    generated = datetime.now().isoformat(timespec="seconds")
    page_rows = "\n".join(
        f"| `{route}` | `{reference}` | pending | pending |" for route, reference in pages
    ) or "| `/` | `pending-reference` | pending | pending |"
    viewport_rows = "\n".join(
        f"| {name} | {width} x {height} | {purpose} | pending |"
        for name, width, height, purpose in viewports
    )
    interaction_rows = "\n".join(
        f"| {item} | pending | pending |" for item in DEFAULT_INTERACTIONS
    )
    gates = [
        "Production build passes.",
        "Preview build or deploy preview was used for final visual QA when practical.",
        "Every reference page has a rendered screenshot at the locked viewports.",
        "Desktop, iPad/tablet, mobile, and small-mobile layouts have no horizontal scroll, overlap, unreadable text, or broken navigation.",
        "All visible buttons, links, forms, menus, filters, tabs, carousel controls, and social links work or have explicit safe placeholder destinations.",
        "No core logo, icon, UI component, overlay, or divider contains a checkerboard, screenshot background, or unwanted matte.",
        "No placeholder text, placeholder gray boxes, unrelated stock imagery, or generic icon substitutions remain.",
        "Visual QA ledger and benchmark score exist and unresolved blockers are recorded.",
    ]
    gate_rows = "\n".join(f"- [ ] {gate}" for gate in gates)
    return f"""# Reconstruction Contract

Project: {args.project}
Generated: {generated}

This contract locks the approved visual references before implementation. Do not reinterpret the design, change the visual system, or replace reference-specific assets with generic alternatives.

## Source Of Truth

- Asset export: `{args.asset_export or "not recorded"}`
- Prototype/reference folder: `{args.reference_root or "not recorded"}`
- Target stack: `{args.target_stack}`
- Final QA target: production build or deploy preview when practical.

## Page Reference Map

| Route | Approved reference | Section specs complete | Final QA complete |
| --- | --- | --- | --- |
{page_rows}

## Required Viewports

| Viewport | Size | Purpose | Screenshot reviewed |
| --- | ---: | --- | --- |
{viewport_rows}

## Interaction Matrix

| Interaction | Implemented | QA result |
| --- | --- | --- |
{interaction_rows}

## Section Contract

For every major section, create `docs/research/components/<section>.spec.md` before coding. Each spec must record:

- Source reference screenshot or board.
- Exact visible copy and code-native/decorative text policy.
- Asset mapping and layering order.
- Typography, spacing, color, radius, shadow, border, mask, and background treatment.
- Desktop, laptop, iPad/tablet, mobile, and small-mobile layout behavior.
- Interaction, hover, focus, active, selected, open/closed, and reduced-motion states.
- Known risks, missing assets, or font uncertainty.

## Pass/Fail Gates

{gate_rows}

## Repair Rule

The first rendered site is a draft. After every screenshot review, repair the specific component, token, asset, or layout rule that caused the drift, rebuild, and recapture the affected viewport.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a 9Designer reconstruction contract.")
    parser.add_argument("--project", default="", help="Project name.")
    parser.add_argument("--website-root", default=".", help="Website project root.")
    parser.add_argument("--asset-export", default="", help="Asset export folder.")
    parser.add_argument("--reference-root", default="", help="Prototype/reference folder.")
    parser.add_argument("--target-stack", default="React + TypeScript + Vite", help="Implementation stack.")
    parser.add_argument("--page", action="append", default=[], type=parse_page, help="Route/reference pair, e.g. /=landing.png")
    parser.add_argument("--viewport", action="append", default=[], type=parse_viewport, help="Viewport, e.g. ipad:1024x1366")
    parser.add_argument("--out", default="docs/research/RECONSTRUCTION_CONTRACT.md", help="Output Markdown path.")
    args = parser.parse_args()

    website_root = Path(args.website_root).expanduser().resolve()
    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = website_root / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)

    args.project = args.project or website_root.name
    viewports = args.viewport or DEFAULT_VIEWPORTS
    out_path.write_text(markdown(args, args.page, viewports), encoding="utf-8")

    summary = {
        "valid": True,
        "contract": str(out_path),
        "pages": len(args.page) or 1,
        "viewports": [{"name": name, "width": width, "height": height} for name, width, height, _ in viewports],
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
