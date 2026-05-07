# Scoring Rubric

Score each category from `0` to `5`.

| Category | What to inspect | Public benchmark target |
| --- | --- | ---: |
| Reference fidelity | Composition, hierarchy, mood, palette, section order, hero placement, typography mood. | `>= 4.0` |
| Asset quality | Logo, wordmark, icons, social icons, imagery, textures, transparency, local asset usage, layering. | `>= 4.0` |
| Responsive quality | Desktop, tablet, mobile hierarchy, nav behavior, text wrapping, image cropping, no overflow. | `>= 4.0` |
| Accessibility | Semantic HTML, alt text, labels, focus states, hidden text for decorative image text, contrast. | `>= 4.0` |
| Build reliability | Install/build/dev commands, no broken images, no runtime errors, no missing local assets. | `>= 4.0` |
| Visual QA completeness | Ledger, screenshots, diff or manual notes, repair log, interaction checks, unresolved blockers. | `>= 4.0` |

## Blocking Issues

Do not mark a benchmark as public-ready when any of these remain:

- Build fails or dev server cannot run.
- Core image, logo, icon, or background is broken.
- Checkerboard, screenshot background, or unwanted matte appears behind a reusable asset.
- Mobile layout has horizontal scrolling, overlap, or unusable navigation.
- Primary nav, CTA, form, or social links are inaccessible or nonfunctional.
- The result looks like a generic redesign instead of a reconstruction of the approved design.

## Score Bands

| Score | Meaning |
| ---: | --- |
| `5` | Excellent match; only tiny differences remain. |
| `4` | Strong match; minor repairable differences remain. |
| `3` | Usable but visible drift remains. |
| `2` | Major reconstruction gaps remain. |
| `1` | Mostly generic, broken, or missing key requirements. |
| `0` | Not attempted or not reviewable. |

## Recommended Command

When a final website build has a ledger and optional diff summary:

```bash
python skills/9assets-website/scripts/score_visual_qa.py \
  --ledger docs/research/VISUAL_QA_LEDGER.md \
  --diff-summary visual-qa/diffs/visual-qa-diff-summary.json \
  --build-passed \
  --out docs/research/VISUAL_BENCHMARK_SCORE.md
```

Add manual category scores where human review is required:

```bash
python skills/9assets-website/scripts/score_visual_qa.py \
  --ledger docs/research/VISUAL_QA_LEDGER.md \
  --build-passed \
  --score fidelity=4.4 \
  --score asset_quality=4.2 \
  --score responsive_quality=4.1 \
  --score accessibility=4.0 \
  --score visual_qa_completeness=4.3 \
  --out docs/research/VISUAL_BENCHMARK_SCORE.md
```
