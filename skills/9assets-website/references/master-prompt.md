# Master Prompt

Use this prompt when you want Codex to build the final working website from a prepared asset export folder.

```text
Use $9assets-website.

Build the complete working website from the provided asset export kit.

The asset kit is the production source of truth. Do not redesign the brand, replace assets with stock imagery, or invent generic sections. Use the exported images, logos, icons, backgrounds, UI elements, tokens, and manifest to build the real site.

First read the kit:
- asset-export-manifest.json
- asset-manifest.json if present
- notes/builder-handoff.md
- notes/asset-plan.md
- notes/font-and-token-notes.md
- design token files
- 06-ready-for-builder/
- logo, icon, UI, background, and page asset folders

Create an implementation map:
- Pages/routes supported by the kit
- Components needed
- Which exported asset is used by each component
- Tokens, fonts, colors, spacing, radii, shadows, borders, overlays, and textures
- Missing assets or assumptions

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

Verification:
- Run npm install if dependencies are missing.
- Run npm run build.
- Start the dev server.
- Test desktop and mobile views with browser testing or screenshots.
- Fix broken images, console errors, text overflow, layout overlap, and mobile nav issues.
- If graphify instructions apply after code edits, run graphify update .

After implementation, briefly report:
1. Pages and routes built.
2. Asset kit folder used.
3. Major assets copied into public/assets/.
4. Verification commands and results.
5. How to run the website locally.
6. Any remaining risks such as missing exact fonts or incomplete assets.
```
