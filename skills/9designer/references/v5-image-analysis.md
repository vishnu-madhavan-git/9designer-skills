# v5.0 Image Analysis Reference

## Radix-Style 12-Step Color Scale

For each extracted brand color, generate a 12-step accessible scale. Convert hex → HSL, keep hue constant, vary lightness from ~98% (step 1) to ~15% (step 12) with slight saturation adjustments.

```css
/* Example for primary color #e94560 (H=350, S=80%) */
--clr-primary-1:  hsl(350, 80%, 98%);   /* App background tint */
--clr-primary-2:  hsl(350, 75%, 95%);   /* Subtle background */
--clr-primary-3:  hsl(350, 72%, 90%);   /* UI element background */
--clr-primary-4:  hsl(350, 70%, 84%);   /* Hovered UI element */
--clr-primary-5:  hsl(350, 68%, 77%);   /* Active / selected */
--clr-primary-6:  hsl(350, 65%, 69%);   /* Subtle border */
--clr-primary-7:  hsl(350, 63%, 59%);   /* UI element border */
--clr-primary-8:  hsl(350, 75%, 47%);   /* Hovered border */
--clr-primary-9:  #e94560;              /* Solid CTA background (exact brand hex) */
--clr-primary-10: hsl(350, 75%, 45%);   /* Hovered solid */
--clr-primary-11: hsl(350, 70%, 35%);   /* Accessible text on light bg */
--clr-primary-12: hsl(350, 65%, 18%);   /* High-contrast text */

/* Alpha variants */
--clr-primary-a3: rgba(233, 69, 96, 0.12);
--clr-primary-a9: rgba(233, 69, 96, 0.90);
```

**Verify WCAG AA (4.5:1 contrast) at steps 11 and 12 against white. Adjust lightness if needed.**

Apply the same process for the accent color.

## Mathematical Typescale

Detect the approximate ratio between heading sizes in the reference, then match to a named scale:

| Ratio | Name | Ratio value | Best for |
|-------|------|-------------|----------|
| Tight | Minor Third | 1.200 | Editorial, dense content |
| Balanced | Major Third | 1.250 | Clean landing pages |
| Classic | Perfect Fourth | 1.333 | Most web sites |
| Dramatic | Golden Ratio | 1.618 | Hero-driven, expressive |

Compute semantic scale from detected base size (body text ≈ 1rem / 16px):

```
step n = base × ratio^n
```

Output as CSS custom properties:

```css
/* Mobile scale (base = 1rem, ratio = 1.333 Perfect Fourth) */
--text-xs:   0.563rem;   /* base × 1.333^-2 */
--text-sm:   0.75rem;    /* base × 1.333^-1 */
--text-base: 1rem;       /* base */
--text-lg:   1.333rem;   /* base × 1.333^1 */
--text-xl:   1.777rem;   /* base × 1.333^2 */
--text-2xl:  2.369rem;   /* base × 1.333^3 */
--text-3xl:  3.157rem;   /* base × 1.333^4 */
--text-4xl:  4.209rem;   /* base × 1.333^5 */

/* Desktop scale: multiply mobile values by 1.10–1.15 for larger sizes */
--text-3xl-lg: 3.473rem;
--text-4xl-lg: 4.630rem;
```

Use `clamp(mobile, fluid-vw, desktop)` for each step:

```css
--text-3xl: clamp(2.369rem, 5vw, 3.157rem);
--text-4xl: clamp(3.157rem, 6vw, 4.209rem);
```

## 3D Detection Flag

Set `🟡 3D OPPORTUNITY DETECTED` when the reference shows:
- Rotating or floating 3D product renders
- Depth-based animations or parallax with 3D elements
- WebGL-style visual effects or immersive environments
- Physical product mockups that clearly benefit from interactive 3D

Do NOT flag for: flat product photography, 2D illustrations that mimic depth, or CSS perspective effects.

## Generative Background Detection

Set `🟡 GENERATIVE BACKGROUND DETECTED` when the reference shows:
- Particle fields or dot systems in motion
- Flow fields or stream-line organic patterns
- Animated gradient meshes or aurora-style backgrounds
- Noise-based texture animations
- Biological/organic morphing shapes

Do NOT flag for: static gradients, simple CSS animations, or video backgrounds.
