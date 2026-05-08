# Dreaming Benchmark Seed

Dreaming is the first public example set for 9Designer. It demonstrates the intended visual direction for an atmospheric, editorial, surreal image-to-website pipeline.

This is a seed benchmark from the earlier visual-output flow. It remains useful as public demo material, but new benchmark submissions should include the current blueprint-first `$9designer` artifacts.

Status: **seed benchmark**

Current coverage: design prototype boards, brand kit board, UI component board, responsive preview board, and asset overview.

Pending for complete benchmark status: rendered working website screenshots and final build QA ledger.

## Preview

| Landing page | Brand kit |
| --- | --- |
| ![Dreaming landing page](../../media/demo-landing.png) | ![Dreaming brand kit](../../media/demo-brand-kit.png) |

| UI components | Responsive preview |
| --- | --- |
| ![Dreaming UI component board](../../media/demo-ui-components.png) | ![Dreaming responsive preview](../../media/demo-responsive.png) |

![Dreaming asset overview](../../media/demo-asset-overview.png)

## What This Example Tests

- Surreal image-led hero composition.
- Atmospheric color and lighting preservation.
- Decorative typography and brand-kit extraction.
- UI component system consistency.
- Responsive preview expectations.
- Asset overview readability for implementation handoff.

## Pipeline Notes

The current standard 9Designer flow is:

1. `$9designer`: analyze the reference and write the complete blueprint.
2. `$9designer`: generate one `imagegen` preview from the blueprint.
3. User confirmation: approve the preview or request blueprint changes.
4. `$9designer`: generate individual logos, icons, UI elements, textures, backgrounds, and page assets from blueprint slots.
5. `$9designer`: build the real website from the same blueprint and local assets.
6. Visual QA: capture screenshots, compare against references, write ledger, score benchmark.

The public media currently shows the design/prototype side of the older pipeline. A complete benchmark should add the blueprint, generated preview, rendered website screenshots, and a final QA score once a deployable site is generated from this kit.

## Current Score

See [visual-benchmark-score.md](visual-benchmark-score.md).

This score is intentionally marked as provisional because the rendered website QA artifacts are not yet included.

## Public Safety

The images linked here are existing generated demo assets from this repository. Do not add private reference images or client screenshots to this folder.
