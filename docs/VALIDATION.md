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

## Optional Future Checks

These checks are useful when the corresponding optional tooling exists, but they are not required for normal skill validation:

- Run Playwright screenshot capture for desktop, tablet, and mobile website renders.
- Compare screenshots with pixelmatch or SSIM-style tools and save diffs.
- Validate `asset-export-manifest.json` for asset roles, responsive variants, accessibility notes, token dependencies, icon policy, and QA notes.
- Smoke test optional background cleanup tools such as `rembg` only when they are installed.
- Optimize traced SVGs with SVGO only when SVG assets are intentionally part of the handoff.
