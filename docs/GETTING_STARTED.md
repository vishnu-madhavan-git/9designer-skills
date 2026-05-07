# Getting Started

9Designer is a Codex skill suite. Install the skill folders, then call the skill by name in Codex with a reference image.

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

## 2. Use The All-In-One Skill

Attach a reference image and say:

```text
Use $9designer with this reference image.
Create the first landing-page prototype, wait for approval, then export production assets and build the working website.
```

The skill runs three stages:

1. `Design Prototype`
2. `Production Asset Export`
3. `Working Website Build`

The first landing page is approval-gated by default. Approve it before the skill continues into deeper pages, assets, or website implementation.

## 3. Use The Modular Pipeline

Use this when you want more control:

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

## 4. What Good Output Looks Like

A good 9Designer run should produce:

- A landing-page prototype faithful to the reference image.
- Clean separate assets, not one giant screenshot.
- Transparent logos, icons, dividers, and overlays where needed.
- An asset manifest that explains cleanup status and intended use.
- Manifest validation that catches missing roles, responsive variants, accessibility notes, icon policy, token dependencies, and QA notes before website build.
- A real responsive frontend site with local assets.
- Build results plus a visual QA ledger backed by manual screenshots, optional Playwright captures, or optional pixel diffs.

## 5. Common Mistakes

- Do not skip the first landing-page approval.
- Do not pass checkerboard-backed PNGs into website implementation.
- Do not replace custom icons with generic placeholders.
- Do not use image-generated paragraph text for normal website copy.
- Do not build the final website as a pasted screenshot.
