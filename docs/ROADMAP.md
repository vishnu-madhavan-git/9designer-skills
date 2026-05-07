# Roadmap

This roadmap keeps 9Designer practical for current Codex use while leaving a clear path toward deeper automation. New tools remain optional until they are validated in real runs.

## Phase 1: Skill And Docs Upgrades

- Strengthen prompt rules for reference analysis, asset export, font matching, stack selection, and visual QA.
- Mark Playwright, pixelmatch, SSIM, rembg, SAM, SVGO, Sharp, Pillow, and ImageMagick as optional accelerators.
- Expand documentation for research findings, validation, and future tooling.

Acceptance:

- All five skills validate.
- No new required dependencies are introduced.
- README and docs links resolve.

## Phase 2: Manifest And Script Upgrades

- Add an optional manifest validation helper.
- Extend generated manifests with asset roles, responsive variants, accessibility notes, token dependencies, icon policy, and QA notes.
- Add optional `rembg` support to background cleanup without replacing the bundled fallback behavior.

Status:

- Implemented with a dependency-free manifest validator, richer scaffolded manifests, and clearer optional `rembg` fallback reporting.

Acceptance:

- Existing manifests remain readable.
- Missing optional tools produce clear fallback guidance.
- Background cleanup smoke tests still pass.

## Phase 3: Automated Visual QA Tooling

- Add optional Playwright screenshot capture commands for desktop, tablet, and mobile.
- Add optional pixelmatch or SSIM-style diff generation.
- Generate or update `docs/research/VISUAL_QA_LEDGER.md` from comparison outputs when practical.

Status:

- Implemented with optional Playwright screenshot capture, optional pixelmatch/pngjs diffs, and a dependency-free visual QA ledger generator.

Acceptance:

- Manual visual QA remains supported.
- Automated QA outputs stable screenshots and useful mismatch categories.
- Visual diff artifacts are easy to inspect and do not replace human review.

## Phase 4: Benchmark Gallery

- Add `docs/examples/` with public-safe example sets.
- Store reference, prototype, asset overview, rendered website screenshots, and visual QA ledger summaries.
- Define a scoring rubric for fidelity, asset quality, responsiveness, accessibility, and build reliability.

Status:

- Implemented with a public benchmark gallery, Dreaming seed example, scoring rubric, and a reusable visual benchmark scoring helper.

Acceptance:

- Examples do not include private or unlicensed assets.
- Contributors can submit examples through the existing issue template.
- README links to the gallery once at least one complete benchmark exists.

## Phase 5: Deployment And Public Showcase

- Add deployment notes for Vercel, Netlify, and static hosting.
- Add public showcase links when example websites are deployed.
- Consider GitHub Pages or a small documentation site only after the skill pack remains stable.

Acceptance:

- Deployment docs do not change the core install flow.
- Public examples have clear source, asset, and license notes.
- The repo remains focused on installable Codex skills.
