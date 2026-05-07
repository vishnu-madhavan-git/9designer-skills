# Dreaming Visual Benchmark Score

Status: provisional seed benchmark.

This score evaluates the public design/prototype assets currently stored in `docs/media/`. It does not claim that a final rendered website has already passed QA.

| Category | Score | Status | Evidence |
| --- | ---: | --- | --- |
| Reference fidelity | `4.2` | pass | The landing page, brand kit, UI board, and responsive board preserve the atmospheric editorial direction. |
| Asset quality | `4.0` | pass | The asset overview is strong enough for handoff, but individual cleaned implementation files are not shown in this public example folder. |
| Responsive quality | `3.8` | needs final website QA | Responsive preview exists, but rendered desktop/tablet/mobile website screenshots are not included yet. |
| Accessibility | `3.2` | needs final website QA | The design boards imply code-native text, but final semantic HTML, labels, focus states, and contrast need website verification. |
| Build reliability | unscored | pending | No final website build artifact is included in this example folder. |
| Visual QA completeness | `3.0` | pending | Prototype screenshots exist, but final QA ledger and repair log are still required. |

Overall: provisional only.

To promote Dreaming to a complete public benchmark, add:

- Rendered website screenshots at desktop, tablet, and mobile.
- `VISUAL_QA_LEDGER.md` with at least eight comparison points.
- `VISUAL_BENCHMARK_SCORE.md` generated or updated after the build passes.
- Notes for any unresolved font, asset, or responsive differences.
