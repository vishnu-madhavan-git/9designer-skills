# Master Prompt

Use this prompt when you want Codex to build the final working website from a prepared asset export folder.

```text
Use $9assets-website.

Build the complete working website from the provided asset export kit.

The asset kit is the production source of truth. Do not redesign the brand, replace assets with stock imagery, or invent generic sections. Use the exported images, logos, icons, backgrounds, UI elements, tokens, and manifest to build the real site.

Strictly clone the approved template/prototype. Do not make an inspired redesign. Match the reference layout, spacing, typography scale, image placement, colors, component shapes, shadows, borders, and responsive behavior as closely as possible.

First read the kit:
- asset-export-manifest.json
- asset-manifest.json if present
- notes/builder-handoff.md
- notes/asset-plan.md
- notes/font-and-token-notes.md
- notes/icon-inventory.md
- notes/social-icons.md
- design token files
- 06-ready-for-builder/
- logo, icon, UI, background, and page asset folders

Create an implementation map:
- Pages/routes supported by the kit
- Components needed
- Which exported asset is used by each component
- Tokens, fonts, colors, spacing, radii, shadows, borders, overlays, and textures
- Reference screenshot/template for each page
- Asset cleanup status for every logo, icon, overlay, divider, and UI image
- Exact visible copy, typography system, icon inventory, component families, container model, and hero/media treatment
- Text policy: real HTML/CSS text versus decorative image text that needs hidden accessible text
- Social icon mapping: exact platform/community glyph, source asset, container treatment, accessible label, href placeholder, and hover/active state
- Missing assets or assumptions

Before coding, create `docs/research/RECONSTRUCTION_CONTRACT.md`. Lock the approved reference pages, desktop, iPad/tablet, mobile, and small-mobile viewports, required interactions, and final pass/fail gates. Do not start implementation until this contract exists.

Before building:
- Reject any reusable asset that has a checkerboard background baked in.
- Reject any logo, icon, or UI element with a screenshot/page background behind it.
- Require manifest fields such as background_cleaned and alpha_verified to be true for reusable assets that need transparency.
- Only true background assets may be full-bleed.

Build the full website. Unless I specify a different stack or an existing app already exists, use React + TypeScript + Vite.

Create or update:
- package.json
- index.html
- src/main.tsx
- src/App.tsx
- src/pages/*
- src/components/*
- src/styles/*
- public/assets/*
- README.md

Website requirements:
- Home / landing page
- Any additional pages represented by the kit, such as About, Gallery, Feature, Detail, and Contact
- Responsive desktop, tablet, and mobile layouts
- Real navigation and mobile navigation
- Real HTML/CSS buttons, cards, forms, CTA, and footer
- Local copied assets under public/assets/
- CSS variables for design tokens
- Faithful use of logo, icons, imagery, textures, backgrounds, and UI references
- No placeholder gray boxes
- No broken images
- No remote assets when local kit assets exist
- No generic SaaS styling unless the asset kit clearly uses that style
- No invented hero eyebrows, badges, pills, sections, forms, dashboards, carousels, or visible above-the-fold copy unless present in the approved design or explicitly requested
- Code-native interactive controls with deliberate typography, accessible labels/states, and shared component variants
- Real HTML/CSS text for nav, headings, paragraphs, buttons, cards, CTA, forms, and footer whenever possible
- Hidden accessible text for decorative logo/wordmark/hand-lettered image text
- Exact matched social icon assets or official/vector-quality glyphs; no generic social placeholders or text labels unless shown in the approved design
- Working behavior for every visible button, link, nav item, social link, form control, tab/filter, carousel control, and mobile menu
- Reusable components such as Header, Hero, StorySection, FeatureSection, ShowcaseSection, GallerySection, CTASection, Footer, Button, and Card when those sections exist
- README with install, dev, build, and asset-source notes

Verification:
- Run npm install if dependencies are missing.
- Confirm npm run dev starts for new Vite projects when practical.
- Run npm run build.
- Start the dev server and, when practical, the production preview server.
- Test desktop and mobile views with browser testing or screenshots.
- Use the optional 9assets-website visual QA helper scripts when available: Playwright screenshot capture, pixel diff comparison, and visual QA ledger generation.
- Compare desktop and mobile screenshots against the approved reference/template at matching viewport sizes.
- Check iPad/tablet viewports around 1024px x 1366px and 768px x 1024px, plus mobile around 390px and small mobile around 360px.
- Iterate until the website closely matches the approved template.
- Fix broken images, console errors, text overflow, layout overlap, mobile nav issues, visual drift, wrong spacing, wrong font scale, wrong component sizing, and incorrect background layering.
- Keep a visual QA ledger with at least eight comparison points across copy, layout, typography, palette, asset treatment, icon/social icon fidelity, spacing/container model, responsive behavior, interactions, or motion.
- Create a visual benchmark score when final quality matters, scoring reference fidelity, asset quality, responsive quality, accessibility, build reliability, and visual QA completeness.
- Run production-readiness validation when the helper exists. Fix errors before final handoff and explain remaining warnings.
- Check 1440px desktop, 768px tablet, and 390px mobile when practical.
- If graphify instructions apply after code edits, run graphify update .

After implementation, briefly report:
1. Pages and routes built.
2. Asset kit folder used.
3. Major assets copied into public/assets/.
4. Verification commands and results.
5. Visual QA ledger, visual benchmark score summary, and production-readiness validator result.
6. How to run the website locally or preview the production build.
7. Any remaining risks such as missing exact fonts or incomplete assets.
```
