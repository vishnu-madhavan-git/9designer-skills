#!/usr/bin/env python3
"""Validate deploy-readiness evidence for a 9Designer website build.

This does not replace a real build or browser test. It checks that the project
has the files and QA artifacts a final image-to-website handoff should include.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


REQUIRED_DOCS = [
    "docs/research/RECONSTRUCTION_CONTRACT.md",
    "docs/research/VISUAL_QA_LEDGER.md",
    "docs/research/VISUAL_BENCHMARK_SCORE.md",
]

REQUIRED_SCREENSHOTS = [
    "desktop.png",
    "ipad-pro.png",
    "tablet.png",
    "mobile.png",
    "small-mobile.png",
]

PLACEHOLDER_PATTERNS = [
    r"\blorem ipsum\b",
    r"\btodo\b",
    r"\bplaceholder\b",
    r"\bcoming soon\b",
    r"\bgray box\b",
    r"\bimage here\b",
]


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def add(target: list[dict[str, str]], code: str, message: str) -> None:
    target.append({"code": code, "message": message})


def package_checks(root: Path, errors: list[dict[str, str]], warnings: list[dict[str, str]]) -> None:
    package = root / "package.json"
    if not package.exists():
        add(warnings, "package_json_missing", "No package.json found. Static HTML builds may be valid, but document the run/deploy command.")
        return

    data = read_json(package)
    scripts = data.get("scripts") or {}
    if "build" not in scripts:
        add(errors, "build_script_missing", "package.json is missing a build script.")
    if "dev" not in scripts and "preview" not in scripts:
        add(warnings, "serve_script_missing", "package.json has no dev or preview script for local review.")


def asset_checks(root: Path, errors: list[dict[str, str]], warnings: list[dict[str, str]]) -> None:
    assets = root / "public" / "assets"
    if not assets.exists():
        add(errors, "public_assets_missing", "public/assets does not exist.")
        return
    files = [path for path in assets.rglob("*") if path.is_file()]
    if not files:
        add(errors, "public_assets_empty", "public/assets exists but contains no files.")
    if not any(path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".svg", ".avif"} for path in files):
        add(warnings, "no_image_assets", "public/assets does not contain common image asset formats.")


def qa_doc_checks(root: Path, errors: list[dict[str, str]], warnings: list[dict[str, str]], strict: bool) -> None:
    for rel in REQUIRED_DOCS:
        path = root / rel
        if path.exists():
            continue
        if strict or rel.endswith("RECONSTRUCTION_CONTRACT.md"):
            add(errors, "qa_doc_missing", f"Missing required QA document: {rel}")
        else:
            add(warnings, "qa_doc_missing", f"Missing QA document: {rel}")


def screenshot_checks(root: Path, errors: list[dict[str, str]], warnings: list[dict[str, str]], strict: bool) -> None:
    screenshots = root / "visual-qa" / "screenshots"
    if not screenshots.exists():
        add(errors if strict else warnings, "screenshots_missing", "visual-qa/screenshots does not exist.")
        return
    for name in REQUIRED_SCREENSHOTS:
        if not (screenshots / name).exists():
            add(errors if strict else warnings, "screenshot_missing", f"Missing screenshot: visual-qa/screenshots/{name}")


def text_scan(root: Path, errors: list[dict[str, str]], warnings: list[dict[str, str]]) -> None:
    candidates = []
    for folder in ["src", "app", "pages", "components", "styles"]:
        path = root / folder
        if path.exists():
            candidates.extend(
                item for item in path.rglob("*") if item.suffix.lower() in {".ts", ".tsx", ".js", ".jsx", ".css", ".scss", ".html"}
            )
    for name in ["index.html", "README.md"]:
        path = root / name
        if path.exists():
            candidates.append(path)

    for path in candidates:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        rel = path.relative_to(root).as_posix()
        for pattern in PLACEHOLDER_PATTERNS:
            if re.search(pattern, text, re.IGNORECASE):
                add(warnings, "placeholder_text", f"Possible placeholder text in {rel}: {pattern}")
                break
        if re.search(r"<img[^>]+src=[\"']https?://", text, re.IGNORECASE):
            add(warnings, "remote_image", f"Remote image URL found in {rel}. Prefer local exported assets.")


def score_checks(root: Path, warnings: list[dict[str, str]]) -> None:
    score = root / "docs" / "research" / "VISUAL_BENCHMARK_SCORE.md"
    if not score.exists():
        return
    text = score.read_text(encoding="utf-8", errors="ignore")
    if "unscored" in text.lower() or "needs-review" in text.lower() or "needs-repair" in text.lower():
        add(warnings, "benchmark_not_passed", "Visual benchmark score still contains unscored or needs-review items.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate 9Designer production readiness evidence.")
    parser.add_argument("--website-root", default=".", help="Website project root.")
    parser.add_argument("--strict", action="store_true", help="Treat screenshot/doc gaps as deploy blockers.")
    args = parser.parse_args()

    root = Path(args.website_root).expanduser().resolve()
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []

    if not root.exists():
        raise SystemExit(f"Website root does not exist: {root}")

    package_checks(root, errors, warnings)
    asset_checks(root, errors, warnings)
    qa_doc_checks(root, errors, warnings, args.strict)
    screenshot_checks(root, errors, warnings, args.strict)
    text_scan(root, errors, warnings)
    score_checks(root, warnings)

    result = {
        "valid": not errors,
        "strict": args.strict,
        "website_root": str(root),
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
