# Visual Benchmark Rubric

Use this rubric after the website builds and screenshots have been reviewed. It turns visual reconstruction quality into explicit repair targets.

## Categories

Score each category from `0` to `5`.

| Category | 5 | 3 | 1 |
| --- | --- | --- | --- |
| Reference fidelity | Layout, hierarchy, mood, palette, section order, and hero composition closely match the approved reference. | Recognizable but with several visible layout or styling drifts. | Looks like a generic redesign or misses the core composition. |
| Asset quality | Logos, icons, imagery, textures, overlays, and social icons are clean, local, matched, and correctly layered. | Some assets are acceptable but a few are blurry, generic, mislayered, or missing variants. | Placeholder, screenshot-backed, checkerboard-backed, or mismatched assets remain. |
| Responsive quality | Desktop, tablet, and mobile preserve hierarchy without overflow, overlap, or broken navigation. | One viewport has noticeable spacing, crop, or hierarchy issues. | Mobile or desktop is not usable. |
| Accessibility | Semantic structure, alt text, labels, focus states, hidden text, and contrast are intentional. | Basic semantics work, but some labels, focus states, or decorative image policies need repair. | Core controls or meaningful visuals are inaccessible. |
| Build reliability | Install/build/dev commands work and no broken images or console errors are visible. | Build works but there are minor warnings or nonblocking runtime issues. | Build fails, dev server cannot start, or core assets are broken. |
| Visual QA completeness | Ledger has at least eight concrete comparison points, viewport checks, interaction checks, and repair notes. | Ledger exists but is light or misses a viewport/interaction family. | No meaningful visual QA record exists. |

## Quality Gates

- Public benchmark target: every category `>= 4.0`, no unresolved blockers.
- Internal working-build target: overall `>= 3.5`, blockers recorded with a repair path.
- Do not average away a serious blocker. A failed build, unusable mobile layout, inaccessible primary form/nav, or checkerboard-backed core asset blocks public benchmark status.

## Repair Priority

Fix in this order:

1. Build failures, broken images, and runtime console errors.
2. Unclean assets: checkerboards, baked screenshot backgrounds, blurry logos/icons, or wrong social glyphs.
3. Major composition drift: wrong hero placement, wrong section order, wrong visual hierarchy.
4. Responsive failures: overflow, overlap, unusable nav, unreadable text, bad crops.
5. Typography and spacing drift: wrong font mood, scale, line-height, button/card dimensions, or container rhythm.
6. Color and atmosphere drift: wrong palette, missing grain/light/glow/texture, incorrect overlays.
7. Interaction gaps: buttons, links, filters, forms, mobile menu, social links, and focus/hover states.
8. Benchmark documentation gaps: missing screenshots, ledger notes, score output, source/license notes.

## Scoring Helper

When practical, run:

```bash
python <9assets-website-skill-dir>/scripts/score_visual_qa.py --ledger docs/research/VISUAL_QA_LEDGER.md --diff-summary visual-qa/diffs/visual-qa-diff-summary.json --build-passed --out docs/research/VISUAL_BENCHMARK_SCORE.md
```

Use manual `--score category=value` entries for categories that require human judgment.
