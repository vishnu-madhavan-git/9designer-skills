# Examples

This page shows how a completed 9Designer run is organized.

## Dreaming Example

The Dreaming example started from a visual reference with atmospheric, editorial, surreal styling. The output demonstrates the intended flow:

1. Full landing page prototype.
2. Inner page and design-system boards.
3. Production asset export.
4. Website-ready asset folder.

## Prototype Outputs

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

Build the first landing-page prototype only. Preserve the image mood, typography, color, lighting, composition, and motifs. Wait for my approval before generating the remaining pages, production assets, or working website.
```

After approval:

```text
Continue the 9Designer pipeline. Export clean separate assets, run background cleanup where needed, write the asset manifest, then build the working responsive website from those assets.
```

## Example Acceptance Criteria

- The design feels native to the original image.
- The hero composition follows the image focal point.
- Icons and social icons match the design world.
- Logos and foreground motifs have clean transparency.
- Normal site copy is real HTML/CSS text.
- The final website passes build verification.
- Desktop, tablet, and mobile screenshots are checked.
