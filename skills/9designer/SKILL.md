---
name: 9designer
description: "Complete image-to-working-website pipeline. Use when the user provides a single reference image and wants the full process handled as one skill: design prototype, production asset export, and working website build. This skill must execute the three stages clearly, wait for approval after the first landing-page prototype unless explicitly overridden, generate clean separate image assets, then build and verify a real responsive website."
---

# 9Designer

9Designer turns one reference image into a complete working website through three required stages:

1. **Design Prototype**
2. **Production Asset Export**
3. **Working Website Build**

Do not collapse these into one vague step. Each stage must produce its own outputs before the next stage starts.

## Stage 1: Design Prototype

Goal: create the approved visual direction from the single reference image.

Use the reference image as the creative source of truth. Internally analyze:

- Main subject, focal point, empty space, movement, horizon, and depth
- Lighting, mood, color palette, texture, atmosphere, and visual style
- Existing logo, wordmark, lettering, typography, symbols, motifs, objects, and patterns
- Best hero text placement based on the image composition

Required behavior:

1. Generate only the first full landing-page prototype image first.
2. The first landing page must include navigation, hero, intro/story, highlight, features, visual showcase, CTA, and footer.
3. Keep the artwork as the dominant visual and avoid generic SaaS/corporate templates.
4. Stop after Image 1 and wait for user approval or requested changes, unless the user explicitly overrides this approval gate.
5. If changes are requested, revise Image 1 before continuing.
6. After approval, generate the remaining prototype pages and boards needed for the website.

Default prototype set after approval:

- Landing page
- About/story page
- World/gallery page
- Feature/experience page
- Detail page
- Contact/signup page
- Brand kit/design system board
- UI component library board
- Copy/content system board
- Responsive website preview board

Stage 1 output:

- Approved prototype image direction
- Prototype/reference images for the site
- Stable brand decisions: name, logo direction, palette, typography mood, icon style, copy tone, section rhythm, and visual motifs

## Stage 2: Production Asset Export

Goal: turn the approved prototype images into clean separate image assets for implementation.

Create an output folder in the workspace:

```text
asset-exports/<project-slug>-YYYYMMDD-HHMM/
```

Required structure:

```text
00-source-kit/
01-logos/
02-icons/
03-ui-elements/
04-backgrounds/
05-page-assets/
06-ready-for-builder/
notes/
asset-export-manifest.json
```

Required behavior:

1. Use image generation for every visual asset.
2. Generate each asset separately. Do not create one giant sheet as the only output.
3. Save every generated image into the correct folder.
4. Copy final implementation assets into `06-ready-for-builder/`.
5. Write or update `asset-export-manifest.json` so the website build can consume the folder without guessing.

Default exported assets:

- `logo-primary`
- `logo-wordmark`
- `logo-mark`
- `favicon`
- Exactly 5 core icons by default
- `button-primary`
- `button-secondary`
- `nav-desktop`
- `nav-mobile`
- `card-default`
- `form-input`
- `cta-banner`
- `footer-module`
- `hero-background`
- `section-texture`
- `decorative-divider`

Background policy:

- Logos, icons, overlays, dividers, and decorative elements: transparent preferred.
- If transparency is not reliable, use a perfectly flat neutral background and mark `background-removal-needed` in the manifest.
- Buttons, nav, cards, forms, and reusable UI elements: isolated component only, no screenshot/page background.
- CTA and footer modules may include their internal component background, but not the full page screenshot background.
- Only true background assets such as `hero-background`, `section-texture`, or background patterns may be full-bleed.

Stage 2 output:

- Clean implementation-ready asset folder
- Separate generated image assets
- `asset-export-manifest.json`
- `notes/asset-plan.md`
- `notes/generation-prompts.md`
- `notes/font-and-token-notes.md`
- `notes/builder-handoff.md`

## Stage 3: Working Website Build

Goal: build the real responsive website from the exported assets.

Use the existing repository stack if one exists. If no stack exists or the workspace is empty, use React + TypeScript + Vite.

Required behavior:

1. Read `asset-export-manifest.json`, `06-ready-for-builder/`, and the notes from Stage 2.
2. Copy final assets into the website project under `public/assets/`.
3. Build a real website, not a screenshot background.
4. Implement responsive pages, navigation, sections, cards, forms, CTAs, footer, and visual styling using HTML/CSS/React components.
5. Use CSS variables for colors, typography, spacing, radii, borders, shadows, overlays, and textures.
6. Preserve the approved brand direction and avoid redesigning.

Default files for a new Vite app:

```text
package.json
index.html
src/main.tsx
src/App.tsx
src/pages/*
src/components/*
src/styles/*
public/assets/*
README.md
```

Default pages when supported by the prototype:

- Home
- About/story
- Gallery/world
- Feature/experience
- Detail
- Contact/signup

Verification requirements:

- Run the smallest meaningful verification for the stack.
- For a Vite app, run `npm install` if needed and `npm run build`.
- Start the dev server and provide the local URL.
- Use browser testing or screenshots for desktop and mobile when available.
- Fix broken images, console errors, text overflow, layout overlap, and mobile navigation issues.
- If the workspace has graphify instructions and code files changed, run `graphify update .`.

Stage 3 output:

- Complete working website project
- Local assets copied into `public/assets/`
- Verified build
- Dev server URL or run command

## Execution Checkpoints

Use these checkpoint labels in progress updates and final summaries:

- `Stage 1 Complete: Design Prototype`
- `Stage 2 Complete: Production Asset Export`
- `Stage 3 Complete: Working Website Build`

Do not mark a stage complete until its required output exists.

## Relationship To Smaller Skills

This skill combines the optimized flow of the existing smaller skills. When useful, follow their behavior:

- Stage 1 follows `9image-design`.
- Stage 2 follows `9design-assets`.
- Stage 3 follows `9assets-website`.

`9design-kit` remains optional for expanded brand-system boards, but it is not required in the normal 9Designer pipeline.

## Final Response

Keep the final concise and include:

- Stages completed
- Prototype images generated or approval status
- Asset export folder path
- Website folder or key files changed
- Verification commands and results
- Dev URL or run command
- Any missing assets, uncertain fonts, or remaining risks
