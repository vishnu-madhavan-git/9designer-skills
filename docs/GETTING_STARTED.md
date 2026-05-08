# Getting Started

9Designer is a Codex skill suite. Install the skill folders, attach a reference image, then call `$9designer` by name.

The current source of truth is the blueprint-first workflow in [`../skills/9designer/SKILL.md`](../skills/9designer/SKILL.md).

## 1. Install The Skills

Copy these folders into your Codex skills directory:

```text
skills/9designer
skills/9image-design
skills/9design-assets
skills/9design-kit
skills/9assets-website
```

Typical destination:

```text
~/.codex/skills/
```

Project-local destination:

```text
<project>/.agents/skills/
```

## 2. Run The Primary Workflow

Attach a reference image and say:

```text
Use $9designer with this reference image.

Write the complete website blueprint first. Generate one imagegen preview from that blueprint and pause for my confirmation.

When I say GO, generate every asset from the blueprint asset list and build the complete responsive website directly from the blueprint.
```

The skill runs this sequence:

1. Analyze the reference image and any user-provided category.
2. Write the complete structured blueprint.
3. Generate an `imagegen` visual from the blueprint.
4. Pause for confirmation.
5. Generate all assets from named blueprint slots.
6. Build all pages from the blueprint.
7. Run desktop, tablet, mobile, and small-mobile QA.
8. Repair mismatches before final handoff.

## 3. Confirm Or Revise

If the preview is correct, say:

```text
GO
```

If it needs changes, describe the changes. The skill should update the blueprint first, then regenerate the preview from the updated blueprint. Do not let the preview and blueprint drift apart.

## 4. Use The Modular Helpers

Use this only when you intentionally want to split the workflow:

```text
Use $9image-design with this reference image.
```

After approving the design:

```text
Use $9design-assets with this approved design.
```

Then build:

```text
Use $9assets-website with this asset export folder.
```

## 5. What Good Output Looks Like

A good 9Designer run should produce:

- A complete blueprint with brand, colors, typography, grid, sections, pages, asset slots, interactions, and responsive behavior.
- One `imagegen` visual that is clearly derived from the blueprint.
- Clean separate assets, not one giant screenshot.
- Transparent logos, icons, dividers, and overlays where needed.
- An asset manifest that explains cleanup status and intended use.
- `tokens.css`, optional `tokens.json`, and optional `tailwind.config.js` derived from blueprint values.
- A real responsive frontend site with local assets.
- Functional buttons, forms, menus, filters, toggles, and page links when specified.
- Build results plus a visual QA ledger backed by screenshots, manual comparison, optional Playwright captures, or optional pixel diffs.

## 6. Common Mistakes

- Do not code before the blueprint and preview are confirmed.
- Do not regenerate the preview without updating the blueprint first.
- Do not pass checkerboard-backed PNGs into website implementation.
- Do not replace custom icons with generic placeholders.
- Do not use image-generated paragraph text for normal website copy.
- Do not build the final website as a pasted screenshot.
- Do not call a site deploy-ready until responsive QA and build verification are complete.
