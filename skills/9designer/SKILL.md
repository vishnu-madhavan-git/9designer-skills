---
name: 9designer
description: "Complete image-to-working-website pipeline. Use when the user provides a single reference image and wants the full process handled as one skill: design prototype, production asset export, and working website build. This skill must execute the three stages clearly, wait for approval after the first landing-page prototype unless explicitly overridden, generate clean separate image assets, then build and verify a real responsive website."
---

# 9Designer

9Designer turns one reference image into a complete working website through three required stages:

1. **Design Prototype**
2. **Production Asset Export**
3. **Working Website Build**

Do not collapse these into one vague step. Each stage must produce its own outputs before the next stage starts. Inside each stage, work section-by-section and asset-by-asset so Codex has time to identify every essential element instead of producing a generic approximation.

## Core Fidelity Principle

The reference image, approved prototype, and exported asset kit are the source of truth. The final website must feel like a careful reconstruction of that design system, not a redesign inspired by it.

Use this priority order whenever there is a conflict:

1. Approved visual reference and prototype.
2. Extracted asset manifest, design tokens, and section specs.
3. Existing project stack and component conventions.
4. General frontend best practices.

General best practices never justify changing the visible design.

## Research-Backed Operating Model

9Designer should combine the strongest patterns from public design-to-code tools:

- From screenshot-to-code tools: keep explicit supported output targets, examples, troubleshooting, and repeatable setup/verification commands.
- From visual-first editors: manage brand assets, tokens, pages, images, components, and code side by side instead of treating the website as one screenshot.
- From visual-difference research: render the implementation, compare it to the approved design, classify visible differences, then repair the code/assets and repeat.

Do not treat the first generated website as final. The final quality comes from the visual refinement loop.

## Stage 1: Design Prototype

Goal: create the approved visual direction from the single reference image.

Use the reference image as the creative source of truth. Internally analyze:

- Main subject, focal point, empty space, movement, horizon, and depth
- Lighting, mood, color palette, texture, atmosphere, and visual style
- Existing logo, wordmark, lettering, typography, symbols, motifs, objects, and patterns
- Best hero text placement based on the image composition
- Which visual elements need transparent backgrounds
- Which text should be HTML/CSS and which text is decorative image-based typography

Before generating, define internally:

- Visual thesis: mood, material, and energy.
- Content plan: hero, support/story, detail/showcase, final CTA.
- Interaction thesis: 2-3 motion or interaction cues for the eventual website.

Required behavior:

1. Generate only the first full landing-page prototype image first.
2. The first landing page must include navigation, hero, intro/story, highlight, features, visual showcase, CTA, and footer.
3. Keep the artwork as the dominant visual and avoid generic SaaS/corporate templates.
4. Stop after Image 1 and wait for user approval or requested changes, unless the user explicitly overrides this approval gate.
5. If changes are requested, revise Image 1 before continuing.
6. After approval, generate the remaining prototype pages and boards needed for the website.
7. Generate section/detail concepts when a full-page prototype is too compressed to implement precisely.

Stage 1 design quality rules:

- Start with composition, not component count.
- Prefer image-led/full-bleed heroes and cardless section layouts unless the reference demands otherwise.
- Keep brand/product name dominant in the first viewport.
- Keep copy short, specific, and scannable.
- Avoid hero cards, generic card grids, stat strips, logo clouds, decorative pill clutter, and unrequested hero eyebrows/kickers/badges.
- Make concepts readable enough to extract typography, spacing, button details, colors, and component shapes.
- Do not use generic social icons, utility icons, arrows, or feature icons. Their metaphor, fill/outline mode, optical weight, corner style, color, size, and container treatment must match the reference world.
- If a prototype image becomes too compressed to read, generate standalone section/detail concepts before implementation. Do not guess from tiny text or miniature icons.

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
4. Run background cleanup for every reusable non-background asset.
5. Copy only cleaned and verified final implementation assets into `06-ready-for-builder/`.
6. Write or update `asset-export-manifest.json` so the website build can consume the folder without guessing.

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
- `social-icon-set`

Also export reference-driven assets when present: decorative wordmarks, hero objects/characters, section illustrations, custom feature icons, gallery cards, CTA artwork, footer visuals, social media/community icons, navigation glyphs, carousel arrows, form icons, and background motifs such as clouds, waves, leaves, stars, magic effects, mountains, animals, dividers, textures, or masks.

Asset discovery protocol:

1. Create an asset inventory before generating files.
2. List every visible logo, wordmark, favicon, social icon, nav icon, CTA icon, card icon, decorative glyph, divider, texture, image frame, section illustration, button treatment, form treatment, and footer element.
3. For each asset, record its intended use: background, foreground object, transparent overlay, icon, logo, UI chrome, decorative image text, or code-native text.
4. For each icon, record metaphor, platform if any, filled vs. outline, stroke width, corner style, bounding box, padding, color, hover/active state, and whether it should be SVG, transparent PNG, or code-native.
5. For social icons, use the exact platform glyphs visible in the approved design where legally and technically practical, then match the design's container, color, radius, shadow, and spacing. Do not substitute generic lucide/social placeholders.
6. If a social icon is stylized by the brand illustration style, generate it as a transparent PNG. If it is a standard platform mark, use a clean official/vector-quality glyph and style the surrounding UI to match the prototype.

Background policy:

- Logos, icons, overlays, dividers, and decorative elements: transparent preferred.
- If transparency is not reliable, use a perfectly flat neutral background, run background cleanup, and verify alpha before handoff.
- Buttons, nav, cards, forms, and reusable UI elements: isolated component only, no screenshot/page background.
- CTA and footer modules may include their internal component background, but not the full page screenshot background.
- Only true background assets such as `hero-background`, `section-texture`, or background patterns may be full-bleed.

Background cleanup requirements:

- Use the `9design-assets` cleanup behavior for all logos, wordmarks, favicons, icons, overlays, dividers, buttons, nav, cards, forms, CTA modules, and footer modules.
- Never accept a baked-in checkerboard pattern as transparency.
- Manifest entries for reusable assets must include `background_cleaned: true`, `alpha_verified: true`, and `background_removal_needed: false` before Stage 3 starts.
- If cleanup fails, regenerate the asset on a flat neutral background and clean it again.

Stage 2 output:

- Clean implementation-ready asset folder
- Separate generated image assets
- `asset-export-manifest.json`
- `notes/asset-plan.md`
- `notes/generation-prompts.md`
- `notes/font-and-token-notes.md`
- `notes/builder-handoff.md`

Stage 2 fidelity rules:

- Match icon metaphor, stroke/fill, optical weight, radius, color, padding, and alignment from the approved design.
- Match actual colors; do not warm, cool, mute, or "improve" the palette.
- Preserve hero/media treatment. Do not add overlays or tints that are not in the approved design.
- Keep interactive UI text and controls code-native for Stage 3 unless the text belongs inside a decorative image asset.
- For decorative image-text assets, record the exact accessible hidden text required in Stage 3.
- Find the closest practical web font by comparing visual traits: serif/sans/display/script, x-height, contrast, terminals, width, weight, tracking, numerals, and distinctive letterforms. Record the chosen font, fallback stack, confidence level, and visual differences in `notes/font-and-token-notes.md`.
- When the exact font cannot be confirmed, choose the closest available web font and adjust CSS size, weight, line-height, and letter spacing to match the prototype instead of pretending the font is exact.

Stage 2 notes must include:

```text
notes/asset-plan.md
notes/asset-inventory.md
notes/icon-inventory.md
notes/social-icons.md
notes/generation-prompts.md
notes/font-and-token-notes.md
notes/builder-handoff.md
```

## Stage 3: Working Website Build

Goal: build the real responsive website from the exported assets.

Use the existing repository stack if one exists. If no stack exists or the workspace is empty, use React + TypeScript + Vite.

Required behavior:

1. Read `asset-export-manifest.json`, `06-ready-for-builder/`, and the notes from Stage 2.
2. Verify reusable assets are cleaned: no checkerboards, no screenshot backgrounds, and alpha verified where required.
3. Copy final assets into the website project under `public/assets/`.
4. Build a real website, not a screenshot background.
5. Implement responsive pages, navigation, sections, cards, forms, CTAs, footer, and visual styling using HTML/CSS/React components.
6. Use CSS variables for colors, typography, spacing, radii, borders, shadows, overlays, and textures.
7. Preserve the approved brand direction and avoid redesigning.
8. Strictly clone the approved template layout instead of creating an inspired redesign.
9. Use real HTML/CSS text for navigation, headings, paragraphs, buttons, cards, CTA, forms, and footer whenever possible.
10. Use accessible hidden text for decorative image-based logos, wordmarks, or hand-lettered titles.

Before coding, create an implementation inventory:

- Exact visible copy, nav items, CTA labels, headings, labels, captions, and footer text.
- Design tokens for color, type, spacing, radii, borders, shadows, overlays, and motion.
- Typography system, icon inventory, component families, container model, and hero/media treatment.
- Asset-to-component mapping and cleanup status.
- Reference screenshot/template for each page.

Then create section specs before implementation. For every major visible section, write a spec in:

```text
docs/research/components/<section-name>.spec.md
```

Each spec must include:

- Target component file.
- Source prototype/reference image.
- DOM/content structure.
- Exact visible copy.
- Assets used, including layered foreground/background assets.
- Colors, typography, spacing, radii, borders, shadows, overlays, and image treatment.
- Icon requirements, including social icon source/style.
- Interaction model: static, click-driven, hover-driven, scroll-driven, time-driven, or mixed.
- Hover, active, selected, focus, open, closed, and mobile states when applicable.
- Desktop, tablet, and mobile layout behavior.

Do not start coding a section until its spec exists.

Frontend implementation rules:

- Use existing repo stack when present; otherwise default to React + TypeScript + Vite.
- Build small focused components, shared primitives, page sections, and shared tokens/styles.
- Implement repeated elements through shared components or variants.
- Keep interactive controls code-native, accessible, and deliberately typed.
- Preserve the container model; do not add cards, wrappers, borders, glows, or panels where the concept uses open space or full-bleed composition.
- Use exported icons/assets only when clean, and use SVG/icon components only when they faithfully match the approved icon style.
- Use semantic HTML, accessible alt text, reusable components, and modern CSS layout. Do not hardcode everything with absolute positioning unless needed for faithful visual layering.
- Implement all buttons, links, nav items, tabs, filters, accordions, forms, carousels, mobile menus, and social links as working UI. If a destination is unknown, use a safe local placeholder such as `#` with an accessible label and preserve the visual behavior.
- Social links must use the matched social icon assets from Stage 2. Do not use text labels or generic icons unless the prototype explicitly shows them.
- Use official/vector-quality SVG icons for simple UI controls when they match the approved design; otherwise use the exported transparent assets. Every icon must pass an optical review for size, baseline, padding, color, and hover/active state.
- Keep the app componentized enough that each major section can be repaired independently. Avoid one giant `App` component or one giant CSS block when the page has multiple visual systems.

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

Default reusable components for a landing-page build:

```text
Header
Hero
StorySection
FeatureSection
ShowcaseSection
GallerySection
CTASection
Footer
Button
Card
```

Use only the components supported by the approved design.

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
- Confirm `npm run dev` starts successfully for new Vite projects when practical.
- Start the dev server and provide the local URL.
- Use browser testing or screenshots for desktop and mobile when available.
- Compare desktop and mobile screenshots against the approved prototype/template at matching viewport sizes.
- Iterate on CSS/components/assets until the website closely matches the reference layout, typography scale, spacing, colors, and section rhythm.
- Fix broken images, console errors, text overflow, layout overlap, and mobile navigation issues.
- Fix visual drift such as wrong background layering, checkerboard-backed assets, wrong card ratios, wrong button heights, or incorrect font weight/size.
- Keep a visual QA ledger with at least eight comparison points covering copy, layout, typography, palette, asset treatment, icon/social icon fidelity, spacing/container model, responsive behavior, interactions, or motion.
- Check desktop around 1440px, tablet around 768px, and mobile around 390px when practical.
- Click or trigger every visible button, link, nav item, tab, filter, form, carousel control, mobile menu, and social icon. Record behavior in the QA ledger.
- If a screenshot comparison shows a mismatch, fix the component or regenerate the relevant asset. Do not explain away fixable drift.
- Run a visual refinement loop after the first successful build:
  1. Capture reference and rendered screenshots at matching desktop and mobile viewports.
  2. Compare the images and write `docs/research/VISUAL_QA_LEDGER.md`.
  3. Classify every visible mismatch as layout, spacing, typography, color, asset, icon, interaction, or responsive behavior.
  4. Repair the specific component, token, or asset that caused the mismatch.
  5. Rebuild and recapture screenshots.
  6. Repeat until remaining differences are minor, intentional, or blocked by missing assets/fonts.
- Prefer element or section screenshots for debugging when a full-page screenshot makes differences hard to isolate.
- Keep screenshots stable by using fixed viewports, waiting for fonts/images, and disabling nonessential animations during visual QA when practical.
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
- Sections recreated, assets generated/used, and main design decisions
- Verification commands and results
- Visual QA ledger location and the main mismatches fixed
- Dev URL or run command
- Any missing assets, uncertain fonts, or remaining risks
