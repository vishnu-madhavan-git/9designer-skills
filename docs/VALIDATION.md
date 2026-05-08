# Validation

Run these checks before opening a pull request.

## Skill Metadata Validation

From the repo root:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/9image-design
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/9design-assets
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/9design-kit
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/9assets-website
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/9designer
```

On Windows, use the full local path:

```powershell
python C:\Users\<you>\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\9designer
```

## Whitespace Check

```bash
git diff --check
```

## Background Cleanup Smoke Test

If you changed `remove_background.py`, run it against a non-private test image:

```bash
python skills/9design-assets/scripts/remove_background.py --input generated.png --output cleaned.png --mode auto
```

Expected result:

- Output file exists.
- Alpha transparency is present when cleanup is required.
- No checkerboard is baked into the final asset.

## Asset Manifest Validation

Validate a generated export folder before handing it to `9assets-website`:

```bash
python skills/9design-assets/scripts/validate_asset_manifest.py asset-exports/<project> --check-files
```

For new Phase 2 exports, use strict mode:

```bash
python skills/9design-assets/scripts/validate_asset_manifest.py asset-exports/<project> --check-files --strict
```

Expected result:

- The script prints JSON with `valid: true`.
- Older manifests may produce warnings without failing unless `--strict` is used.
- New exports should include asset roles, responsive variants, accessibility notes, token dependencies, icon policy, and QA notes.

## Visual QA Helper Smoke Tests

These commands must work without installing optional Playwright or pixel diff dependencies:

```bash
node skills/9assets-website/scripts/capture_visual_qa.mjs --help
node skills/9assets-website/scripts/compare_visual_qa.mjs --help
python skills/9assets-website/scripts/create_fast_track_plan.py --website-root . --out visual-qa/test-fast-track.md
python skills/9assets-website/scripts/create_reconstruction_contract.py --website-root . --out visual-qa/test-contract.md
python skills/9assets-website/scripts/create_visual_qa_ledger.py --website-root . --out visual-qa/test-ledger.md
python skills/9assets-website/scripts/score_visual_qa.py --ledger visual-qa/test-ledger.md --build-passed --score fidelity=4 --score asset_quality=4 --score responsive_quality=4 --score accessibility=4 --score visual_qa_completeness=4 --out visual-qa/test-score.md
python skills/9assets-website/scripts/validate_production_readiness.py --website-root .
```

Expected result:

- The Node scripts print help text.
- The fast-track script creates an implementation plan template.
- The reconstruction contract script creates a contract template.
- The Python script creates a ledger template.
- The score script prints JSON and creates a score Markdown file.
- The production-readiness script prints JSON. It may report missing website artifacts in the repo root because it is meant to run against generated website projects.
- No Playwright, pixelmatch, or pngjs dependency is required for these smoke tests.

When optional tooling is installed in a website project, run:

```bash
node skills/9assets-website/scripts/capture_visual_qa.mjs --url http://localhost:5173 --out visual-qa/screenshots
node skills/9assets-website/scripts/compare_visual_qa.mjs --reference-dir visual-qa/reference --actual-dir visual-qa/screenshots --out visual-qa/diffs
python skills/9assets-website/scripts/create_visual_qa_ledger.py --website-root . --summary visual-qa/diffs/visual-qa-diff-summary.json
python skills/9assets-website/scripts/score_visual_qa.py --ledger docs/research/VISUAL_QA_LEDGER.md --diff-summary visual-qa/diffs/visual-qa-diff-summary.json --build-passed --out docs/research/VISUAL_BENCHMARK_SCORE.md
python skills/9assets-website/scripts/validate_production_readiness.py --website-root . --strict
```

## README Media Check

Confirm README image paths exist:

```bash
ls docs/media/demo-landing.png
ls docs/media/demo-brand-kit.png
ls docs/media/demo-ui-components.png
ls docs/media/demo-responsive.png
ls docs/media/demo-asset-overview.png
ls docs/media/social-preview.png
```

## Community File Check

Confirm these files exist:

```text
README.md
LICENSE
CONTRIBUTING.md
CODE_OF_CONDUCT.md
SECURITY.md
CHANGELOG.md
.github/ISSUE_TEMPLATE/bug_report.yml
.github/ISSUE_TEMPLATE/skill_improvement.yml
.github/ISSUE_TEMPLATE/example_submission.yml
.github/PULL_REQUEST_TEMPLATE.md
.github/CODEOWNERS
```

## v5.0 Marker Check

Confirm v5.0 content was merged correctly into the 9designer skill and references:

```powershell
# Windows
Select-String -Path "skills\9designer\SKILL.md" -Pattern "Two-Turn Workflow|v5.0|PAUSE POINT|tokens.json|tailwind.config|pixel diff|shadcn"
Select-String -Path "skills\9designer\references\v5-workflow.md" -Pattern "PAUSE POINT|Subagent Dispatch"
Select-String -Path "skills\9designer\references\v5-image-analysis.md" -Pattern "Radix|typescale|Perfect Fourth"
Select-String -Path "skills\9designer\references\v5-token-exports.md" -Pattern "Style Dictionary|tailwind.config"
Select-String -Path "skills\9designer\references\v5-pixel-diff.md" -Pattern "pixelmatch|quadrant|similarity"
Select-String -Path "skills\9designer\references\v5-optional-integrations.md" -Pattern "p5.js|Three.js|Figma MCP|Penpot"
```

```bash
# macOS/Linux
grep -n "Two-Turn Workflow\|v5.0\|PAUSE POINT\|tokens.json\|tailwind.config\|pixel diff\|shadcn" skills/9designer/SKILL.md
ls skills/9designer/references/
```

Expected: all patterns match, and four reference files exist in `skills/9designer/references/`.

## Optional Future Checks

These checks are useful when the corresponding optional tooling exists, but they are not required for normal skill validation:

- Smoke test optional background cleanup tools such as `rembg` only when they are installed.
- Optimize traced SVGs with SVGO only when SVG assets are intentionally part of the handoff.
