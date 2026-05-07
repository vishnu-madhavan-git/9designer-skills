# Contributing to 9Designer Skills

Thanks for helping improve 9Designer. This repo is an installable Codex skill pack, so the best contributions make the workflow clearer, stricter, easier to validate, or better demonstrated.

## What To Contribute

Useful contributions include:

- Skill prompt improvements that increase visual fidelity.
- Better asset-generation, cleanup, or manifest instructions.
- More precise frontend reconstruction and QA rules.
- New examples from different reference-image styles.
- Documentation fixes, install notes, and workflow diagrams.
- Validation scripts or tests that catch broken skill metadata.

Avoid broad rewrites unless an issue or discussion has agreed on the direction.

## Repository Structure

```text
skills/                  Installable Codex skills
docs/                    User and contributor documentation
docs/media/              README and example images
.github/                 Issue and PR templates
```

## Local Validation

Run the skill validator before opening a PR:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/9image-design
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/9design-assets
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/9design-kit
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/9assets-website
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/9designer
```

On Windows, replace `~/.codex/skills` with your local Codex skills path, such as:

```text
C:\Users\<you>\.codex\skills
```

Also run:

```bash
git diff --check
```

When changing asset export behavior, run the manifest validator against a generated or fixture export:

```bash
python skills/9design-assets/scripts/validate_asset_manifest.py asset-exports/<project> --check-files --strict
```

## Pull Request Checklist

Before submitting:

- Keep changes scoped to one improvement.
- Update README or docs when behavior changes.
- Add example images only when they are directly useful.
- Do not commit generated website builds, `asset-exports/`, `asset-kits/`, `node_modules/`, or secrets.
- Include validation results in the PR description.

## Skill Quality Bar

Skill changes should preserve these principles:

- The reference image is the source of truth.
- The first landing page is approval-gated.
- Assets are generated separately and cleaned before website build.
- Normal website text stays code-native.
- Icons and social icons must match the approved design.
- Working websites must be verified against screenshots and interactions.

## Review Process

Maintainers should check:

- Skill metadata is valid.
- Instructions are specific, not vague.
- New rules do not contradict existing stage boundaries.
- Docs and examples match the current skill names.
- Validation commands pass.
