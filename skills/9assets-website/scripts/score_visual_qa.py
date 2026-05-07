#!/usr/bin/env python3
"""Score a 9Designer website build against the visual benchmark rubric.

The script is dependency-free and supports both automated hints and manual
review scores. It is intended to make quality gates explicit without replacing
human visual judgment.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any


CATEGORIES = {
    "fidelity": "Reference fidelity",
    "asset_quality": "Asset quality",
    "responsive_quality": "Responsive quality",
    "accessibility": "Accessibility",
    "build_reliability": "Build reliability",
    "visual_qa_completeness": "Visual QA completeness",
}


def clamp_score(value: float) -> float:
    return max(0.0, min(5.0, round(value, 2)))


def parse_score(value: str) -> tuple[str, float]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("Use category=score, for example fidelity=4.5")
    key, raw_score = value.split("=", 1)
    key = key.strip().lower().replace("-", "_")
    if key not in CATEGORIES:
        allowed = ", ".join(CATEGORIES)
        raise argparse.ArgumentTypeError(f"Unknown category `{key}`. Allowed: {allowed}")
    try:
        score = float(raw_score)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Invalid score `{raw_score}`") from exc
    if score < 0 or score > 5:
        raise argparse.ArgumentTypeError("Scores must be between 0 and 5")
    return key, clamp_score(score)


def load_json(path: str) -> dict[str, Any]:
    if not path:
        return {}
    source = Path(path).expanduser().resolve()
    if not source.exists():
        raise SystemExit(f"Diff summary does not exist: {source}")
    return json.loads(source.read_text(encoding="utf-8"))


def infer_fidelity(diff_summary: dict[str, Any]) -> tuple[float | None, str]:
    comparisons = diff_summary.get("comparisons") or []
    ratios = [
        item["mismatch_ratio"]
        for item in comparisons
        if isinstance(item.get("mismatch_ratio"), (int, float))
    ]
    if not comparisons:
        return None, "No automated diff comparisons were provided."
    if any(item.get("status") == "size-mismatch" for item in comparisons):
        return 2.0, "At least one screenshot size mismatch was reported."
    if not ratios:
        return None, "Diff summary has comparisons but no numeric mismatch ratios."

    average = sum(ratios) / len(ratios)
    if average <= 0.01:
        return 4.75, f"Average mismatch ratio is {average:.2%}."
    if average <= 0.03:
        return 4.25, f"Average mismatch ratio is {average:.2%}."
    if average <= 0.06:
        return 3.5, f"Average mismatch ratio is {average:.2%}."
    if average <= 0.10:
        return 2.75, f"Average mismatch ratio is {average:.2%}."
    return 2.0, f"Average mismatch ratio is {average:.2%}."


def infer_visual_qa_completeness(ledger_path: str) -> tuple[float | None, str]:
    if not ledger_path:
        return None, "No visual QA ledger path was provided."
    path = Path(ledger_path).expanduser().resolve()
    if not path.exists():
        return None, f"Visual QA ledger does not exist: {path}"

    text = path.read_text(encoding="utf-8")
    checked = len(re.findall(r"- \[[xX]\]", text))
    unchecked = len(re.findall(r"- \[ \]", text))
    repair_rows = max(0, text.count("|") // 5)
    if checked >= 8:
        return 5.0, f"{checked} checklist items are checked."
    if checked >= 5:
        return 4.0, f"{checked} checklist items are checked."
    if checked >= 3:
        return 3.0, f"{checked} checklist items are checked."
    if unchecked or repair_rows:
        return 2.0, "Ledger exists but still needs more completed review evidence."
    return 1.0, "Ledger exists but has little structured review evidence."


def build_markdown(result: dict[str, Any]) -> str:
    rows = []
    for key, label in CATEGORIES.items():
        item = result["categories"][key]
        score = "unscored" if item["score"] is None else f"{item['score']:.2f}"
        status = item["status"]
        evidence = item["evidence"]
        rows.append(f"| {label} | {score} | {status} | {evidence} |")

    blockers = "\n".join(f"- {item}" for item in result["blockers"]) or "- None recorded."

    return f"""# Visual Benchmark Score

Project: {result["project"]}
Generated: {result["generated_at"]}

Overall score: {result["overall_score_text"]}
Status: {result["status"]}

## Category Scores

| Category | Score | Status | Evidence |
| --- | ---: | --- | --- |
{chr(10).join(rows)}

## Blockers

{blockers}

## Notes

- Scores are 0-5.
- Public benchmark target: every category at least 4.0 and no blockers.
- Internal working-build target: overall at least 3.5 with blockers recorded and repairable.
- Automated screenshot diffs are evidence, not final approval.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Score a 9Designer visual QA run.")
    parser.add_argument("--project", default="", help="Project name.")
    parser.add_argument("--ledger", default="", help="Path to VISUAL_QA_LEDGER.md.")
    parser.add_argument("--diff-summary", default="", help="Optional visual-qa-diff-summary.json.")
    parser.add_argument("--score", action="append", default=[], type=parse_score, help="Manual category score, e.g. fidelity=4.5.")
    parser.add_argument("--build-passed", action="store_true", help="Set build reliability to 5 unless manually scored.")
    parser.add_argument("--build-failed", action="store_true", help="Set build reliability to 1 unless manually scored.")
    parser.add_argument("--minimum", type=float, default=4.0, help="Minimum category score target.")
    parser.add_argument("--strict", action="store_true", help="Exit nonzero when unscored categories or blockers remain.")
    parser.add_argument("--out", default="", help="Optional markdown output path.")
    args = parser.parse_args()

    if args.build_passed and args.build_failed:
        raise SystemExit("Use only one of --build-passed or --build-failed.")

    manual_scores = dict(args.score)
    diff_summary = load_json(args.diff_summary)
    generated_at = datetime.now().isoformat(timespec="seconds")
    project = args.project or Path.cwd().name

    categories: dict[str, dict[str, Any]] = {}
    blockers: list[str] = []

    fidelity, fidelity_evidence = infer_fidelity(diff_summary)
    visual_qa, visual_qa_evidence = infer_visual_qa_completeness(args.ledger)

    inferred = {
        "fidelity": (fidelity, fidelity_evidence),
        "visual_qa_completeness": (visual_qa, visual_qa_evidence),
    }
    if args.build_passed:
        inferred["build_reliability"] = (5.0, "Build command passed.")
    elif args.build_failed:
        inferred["build_reliability"] = (1.0, "Build command failed.")

    for key, label in CATEGORIES.items():
        if key in manual_scores:
            score = manual_scores[key]
            evidence = "Manual review score supplied."
        else:
            score, evidence = inferred.get(key, (None, "Manual score required."))

        if score is None:
            status = "unscored"
            blockers.append(f"{label} is unscored.")
        elif score < args.minimum:
            status = "needs-repair"
            blockers.append(f"{label} scored {score:.2f}, below target {args.minimum:.2f}.")
        else:
            status = "pass"

        categories[key] = {
            "label": label,
            "score": score,
            "status": status,
            "evidence": evidence,
        }

    scored = [item["score"] for item in categories.values() if item["score"] is not None]
    overall_score = clamp_score(sum(scored) / len(scored)) if scored else None
    overall_score_text = "unscored" if overall_score is None else f"{overall_score:.2f}/5"
    status = "pass" if not blockers and overall_score is not None else "needs-review"

    result = {
        "valid": status == "pass",
        "project": project,
        "generated_at": generated_at,
        "minimum": args.minimum,
        "status": status,
        "overall_score": overall_score,
        "overall_score_text": overall_score_text,
        "categories": categories,
        "blockers": blockers,
        "inputs": {
            "ledger": args.ledger,
            "diff_summary": args.diff_summary,
        },
    }

    if args.out:
        out_path = Path(args.out).expanduser().resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(build_markdown(result), encoding="utf-8")
        result["markdown"] = str(out_path)

    print(json.dumps(result, indent=2))
    if args.strict and status != "pass":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
