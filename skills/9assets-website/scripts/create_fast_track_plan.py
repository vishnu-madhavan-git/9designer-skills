#!/usr/bin/env python3
"""Create a fast-track implementation plan for 9Designer website builds."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


DEFAULT_PAGES = [
    ("/", "Home / landing page"),
    ("/about", "About / story page when supported"),
    ("/gallery", "World / gallery page when supported"),
    ("/experience", "Feature / experience page when supported"),
    ("/detail", "Detail page when supported"),
    ("/contact", "Contact / signup page when supported"),
]


def parse_page(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("Use route=label, for example /=Home")
    route, label = value.split("=", 1)
    return route.strip() or "/", label.strip() or route.strip() or "/"


def markdown(args: argparse.Namespace, pages: list[tuple[str, str]]) -> str:
    page_rows = "\n".join(
        f"| `{route}` | {label} | pending | pending | pending |" for route, label in pages
    )
    generated = datetime.now().isoformat(timespec="seconds")
    return f"""# Fast Track Plan

Project: {args.project}
Generated: {generated}

Fast mode means fewer wasted passes, not lower fidelity. Do not skip the reconstruction contract, production build, responsive QA, interaction QA, visual QA ledger, benchmark score, or production-readiness validation.

## Critical Path

1. Lock references with `RECONSTRUCTION_CONTRACT.md`.
2. Inventory routes, visible copy, tokens, asset roles, and missing blockers.
3. Scaffold the app, routes, shared layout, tokens, and asset loader immediately.
4. Implement the landing page first because it defines the visual system.
5. Implement remaining pages by reusing landing primitives and section variants.
6. Run build early, then keep it green after every major page.
7. Capture only changed viewport/section screenshots during repair, then full desktop/iPad/tablet/mobile QA before final handoff.

## Page Queue

| Route | Page | Shell | First pass | Final QA |
| --- | --- | --- | --- | --- |
{page_rows}

## Parallel Work Queues

| Queue | Work | Rule |
| --- | --- | --- |
| Assets | Copy ready assets, validate manifest, flag missing blockers. | Do not regenerate assets that are already clean and visually accepted. |
| Tokens | Create CSS variables, font stack, spacing, radii, shadows, overlays. | Use tokens before section styling to avoid repeated CSS churn. |
| Structure | Create routes, layout, header, footer, mobile nav, shared primitives. | Keep shells lightweight but buildable. |
| Sections | Implement section specs one by one. | Reuse primitives; do not create one-off CSS unless the design demands it. |
| QA | Build, screenshots, interaction checks, ledger, score, readiness validation. | Use targeted checks during repair, full checks at the end. |

## Speed-Safe Shortcuts

- Use real HTML/CSS for buttons, nav, forms, cards, tags, and footer text unless the element is decorative bitmap art.
- Use CSS gradients, borders, masks, shadows, and overlays when they match the prototype better and faster than generated UI chrome.
- Use exported image assets for visual-world elements: logo, wordmark, hero art, scene art, icons, social glyphs, textures, overlays, dividers, and decorative motifs.
- Prefer existing clean assets over regeneration. Regenerate only missing, unclean, blurry, or visibly mismatched assets.
- Create section specs in compact form; include only the decisions needed to code accurately.
- Use component variants instead of duplicate section implementations.
- Repair the exact failing token, component, asset, or breakpoint instead of rewriting whole sections.

## Non-Negotiable Gates

- Production build passes.
- Desktop, iPad/tablet, mobile, and small-mobile views are reviewed.
- Mobile menu and all visible interactions work.
- No placeholder copy, gray boxes, broken images, remote replacement assets, or checkerboard-backed assets remain.
- `VISUAL_QA_LEDGER.md`, `VISUAL_BENCHMARK_SCORE.md`, and production-readiness validation exist before final handoff.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a 9Designer fast-track implementation plan.")
    parser.add_argument("--project", default="", help="Project name.")
    parser.add_argument("--website-root", default=".", help="Website project root.")
    parser.add_argument("--page", action="append", default=[], type=parse_page, help="Route/label pair, e.g. /=Home")
    parser.add_argument("--out", default="docs/research/FAST_TRACK_PLAN.md", help="Output Markdown path.")
    args = parser.parse_args()

    website_root = Path(args.website_root).expanduser().resolve()
    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = website_root / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)

    args.project = args.project or website_root.name
    pages = args.page or DEFAULT_PAGES
    out_path.write_text(markdown(args, pages), encoding="utf-8")

    print(json.dumps({"valid": True, "fast_track_plan": str(out_path), "pages": len(pages)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
