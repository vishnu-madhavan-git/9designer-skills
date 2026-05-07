# Fast Development Mode

Use this reference when the user asks to speed up the image-to-website process. Fast mode removes duplicated work; it does not lower fidelity.

## Principles

- Lock the visual target once, then build against it. Repeated redesign is the main source of delay.
- Build the website shell early: routes, layout, tokens, asset loading, header, footer, mobile nav.
- Keep text, controls, and layout code-native. Use generated images for the visual world, not for every button or paragraph.
- Reuse approved assets and tokens. Regenerate only assets that are missing, unclean, blurry, or visibly mismatched.
- Repair the smallest failing unit: token, breakpoint, component, section, or asset.
- Run targeted QA during repair and full QA at the end.

## Fast Path

1. Create `RECONSTRUCTION_CONTRACT.md`.
2. Create `FAST_TRACK_PLAN.md`.
3. Validate the asset manifest and copy `06-ready-for-builder/` into `public/assets/`.
4. Scaffold the app and routes.
5. Create tokens before styling sections.
6. Implement the landing page first.
7. Extract landing-page primitives into shared components.
8. Implement remaining pages with shared primitives and page-specific sections.
9. Run the build after the landing page and after each major route group.
10. Capture targeted screenshots for changed sections, then full desktop/iPad/tablet/mobile screenshots before final handoff.
11. Write the QA ledger, benchmark score, and production-readiness result.

## What To Skip In Fast Mode

Skip only when the final site does not need it:

- Extra design boards after the visual system is already approved.
- Regenerating clean assets that are already good enough.
- Image exports for normal HTML text, buttons, simple cards, and forms when CSS can match them.
- Rewriting the entire CSS system when one token or breakpoint is wrong.
- Full-site screenshots after every small change; use targeted screenshots during repair.

Do not skip:

- First landing-page approval.
- Asset cleanup for reusable image assets.
- Reconstruction contract.
- Section specs.
- Production build.
- Desktop, iPad/tablet, mobile, and small-mobile QA.
- Interaction QA.
- Visual QA ledger and readiness validation.

## Coding Pattern

- Create shared `tokens.css` first.
- Create `Button`, `Link`, `MediaFrame`, `Section`, `Header`, `MobileNav`, and `Footer` primitives early.
- Implement page sections in separate components.
- Use page data arrays for repeated gallery/cards/timeline items.
- Keep responsive behavior in the component stylesheet next to the section or in predictable shared CSS.
- Avoid one giant `App` and one giant CSS file when the site has multiple visual systems.

## Repair Loop

1. Identify mismatch category: layout, spacing, typography, color, asset, icon, interaction, or responsive behavior.
2. Locate the smallest owner: token, component, section, route, asset, or breakpoint.
3. Patch only that owner.
4. Rebuild if code changed.
5. Recapture only the affected viewport or section.
6. Log the repair.
7. Run full QA once the repair queue is empty.
