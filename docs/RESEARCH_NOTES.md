# Research Notes

This document tracks public design-to-code patterns that should influence 9Designer.

## Repositories Reviewed

| Project | Public signal | Useful pattern for 9Designer |
| --- | ---: | --- |
| [`abi/screenshot-to-code`](https://github.com/abi/screenshot-to-code) | 72.5k stars, 8.9k forks as of 2026-05-07 | Clear supported stacks, examples, setup commands, troubleshooting, and video/screen-recording input experiments. |
| [`onlook-dev/onlook`](https://github.com/onlook-dev/onlook) | 25.7k stars, 2.0k forks as of 2026-05-07 | Visual-first editing, brand assets, tokens, pages, project images, real-time preview, code mapping, and checkpointed iteration. |
| [`firecrawl/open-lovable`](https://github.com/firecrawl/open-lovable) | 26.2k stars, 5.0k forks as of 2026-05-07 | Strong “clone/recreate website as React app” positioning and fast onboarding. |
| [`tldraw/make-real`](https://github.com/tldraw/make-real) | 5.4k stars as of 2026-05-07 | Sketch/reference-to-working-output workflow with a simple mental model. |
| [`BuilderIO/figma-html`](https://github.com/BuilderIO/figma-html) | 3.6k stars as of 2026-05-07 | HTML-to-Figma direction shows the value of editable design artifacts, not only code output. |
| [`Nutlope/llamacoder`](https://github.com/Nutlope/llamacoder) | 6.9k stars as of 2026-05-07 | Example-driven README, fast local setup, and sandboxed preview expectations. |

## Source Findings

- `screenshot-to-code` advertises explicit output stacks such as HTML/Tailwind, React/Tailwind, Vue/Tailwind, Bootstrap, Ionic/Tailwind, and SVG, plus examples and setup commands. 9Designer should keep its default stack clear while allowing explicit target-stack requests.
- Onlook’s public README highlights design-tool behaviors: importing from text/image/Figma/GitHub, managing brand assets and tokens, pages, project images, components, branches, real-time preview, and code mapping. 9Designer should mirror this as written inventories and section specs.
- Vitest’s browser visual regression docs recommend stable screenshot baselines, specific element screenshots, fixed viewport sizes, disabled animations, and mismatch thresholds. 9Designer should use these as QA guidance even when it performs manual screenshot comparison instead of adding a test runner.
- The VisRefiner paper argues that screenshot-to-code quality improves when systems learn from rendered visual differences versus the target design. 9Designer should operationalize this as a render-compare-repair loop.

## Improvements Added To 9Designer

- Added a research-backed operating model to `$9designer`.
- Added a mandatory visual refinement loop after the first successful website build.
- Added `docs/research/VISUAL_QA_LEDGER.md` as the expected mismatch ledger path for website builds.
- Added guidance to classify mismatches as layout, spacing, typography, color, asset, icon, interaction, or responsive behavior.
- Added stable screenshot guidance: fixed viewports, wait for fonts/images, and disable nonessential animations during QA where practical.

## Manus Phase 1 Findings Integrated

The downloaded Manus plan at `C:\Users\mrvis\Downloads\9Designer Skill Suite Improvement Plan` recommended deeper automation and tool integration. Phase 1 intentionally integrates the low-risk parts as skill and documentation guidance only:

- Optional target stacks beyond the default React + TypeScript + Vite: Next.js + Tailwind, static HTML/CSS, Vue + Tailwind, Astro, or existing repo stack.
- Optional visual QA accelerators: Playwright screenshot capture, pixelmatch, and SSIM-style comparison.
- Optional asset cleanup accelerators: rembg, Segment Anything/SAM, Pillow, ImageMagick, Sharp, and SVGO.
- Expanded asset manifest guidance with asset roles, responsive variants, accessibility notes, token dependencies, icon policy, and QA notes.
- Stronger font matching workflow with ranked candidates, confidence levels, fallback stacks, and typography tuning values.

All of these remain optional or roadmap items. They are not required dependencies for a normal 9Designer run.

## Future Improvements

- Add an optional `target_stack` decision in prompts: React/Vite default, Next/Tailwind, static HTML/CSS, Vue/Tailwind, or existing repo stack.
- Add a tiny validation helper that checks for required asset manifest fields and missing media files.
- Add a sample visual QA ledger from a completed website build.
- Add optional benchmark examples with before/reference/render/diff images.
- Add a repo-level gallery index for community-submitted examples.
