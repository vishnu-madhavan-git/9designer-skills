# Contributor Workflow

Use this workflow for changes to skills, docs, examples, and helper scripts.

## 1. Choose A Small Scope

Good scopes:

- Improve one skill stage.
- Add one example.
- Fix one documentation gap.
- Add one validation helper.

Avoid combining unrelated prompt edits, docs rewrites, and examples in one pull request.

## 2. Create A Branch

```bash
git checkout -b improve/<short-topic>
```

Examples:

```bash
git checkout -b improve/icon-inventory-rules
git checkout -b docs/getting-started-clarity
```

## 3. Edit And Validate

Validate every changed skill folder:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/9designer
```

If your change touches multiple skills, validate all five. See `docs/VALIDATION.md`.

## 4. Commit

Use concise commit messages:

```bash
git add .
git commit -m "Clarify asset cleanup workflow"
```

## 5. Open A Pull Request

In the PR:

- Explain what changed.
- Include validation commands and results.
- Include screenshots or example outputs for visual docs changes.
- Link the issue if one exists.

## 6. Review Expectations

Maintainers should verify:

- Skill metadata is valid.
- Instructions remain stage-based and decision-complete.
- New rules do not conflict with existing rules.
- Public docs match current skill names and folder paths.
- Example images are useful and not private.
