# Examples

This page shows how 9Designer examples should be organized.

For benchmark scoring and public-safe submissions, see the [benchmark gallery](examples/README.md).

## Dreaming Example

The Dreaming example started from a visual reference with atmospheric, editorial, surreal styling. It predates the current blueprint-first wording, but it remains the public visual benchmark seed for the repo.

Future examples should include the current source-of-truth flow:

1. Reference image.
2. Complete blueprint.
3. `imagegen` preview generated from the blueprint.
4. User confirmation.
5. Production asset export from named blueprint slots.
6. Working website build from the same blueprint.
7. Visual QA ledger and benchmark score.

## Visual Outputs

| Output | Preview |
| --- | --- |
| Landing page | ![Dreaming landing page](media/demo-landing.png) |
| Brand kit | ![Dreaming brand kit](media/demo-brand-kit.png) |
| UI components | ![Dreaming UI components](media/demo-ui-components.png) |
| Responsive preview | ![Dreaming responsive preview](media/demo-responsive.png) |

## Asset Overview

![Dreaming asset overview](media/demo-asset-overview.png)

## Example Prompt

```text
Use $9designer with this reference image.

Write the complete website blueprint first. Include brand direction, exact color tokens, typography, grid, every section, every page, every asset slot, and every interactive behavior.

Then generate one imagegen preview from that blueprint and pause. Do not build the website until I say GO.
```

After approval:

```text
GO
```

Expected continuation:

```text
Generate every asset from the blueprint asset list, clean transparent assets where needed, write the asset manifest, then build the complete responsive website directly from the blueprint.
```

## Example Acceptance Criteria

- The blueprint exists before any generated preview or code.
- The design feels native to the original image.
- The hero composition follows the image focal point.
- Colors, fonts, layout, and section rhythm match the blueprint.
- Icons and social icons match the design world or use verified official marks.
- Logos and foreground motifs have clean transparency.
- Normal site copy is real HTML/CSS text.
- Every specified interaction works.
- The final website passes build verification.
- Desktop, tablet, mobile, and small-mobile screenshots are checked.
