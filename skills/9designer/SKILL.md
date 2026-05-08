---
name: 9designer
description: "Codex-native image-to-website pipeline. Give any reference image and 9designer writes a complete structured blueprint (brand, colors, fonts, grid, every section spec, every asset slot with exact dimensions and positions), renders that blueprint as an imagegen visual for confirmation, then builds the entire working website directly from the blueprint. The imagegen is a visual proof of the blueprint -- the blueprint drives everything."
---

# 9Designer

Give any image. 9Designer writes a precise blueprint. Renders it as a visual. You confirm. It builds the complete working website -- every page, every asset, every interaction -- exactly to spec.

The blueprint is the contract. The imagegen is the preview. The code is the output.
Nothing is guessed. Nothing is improvised.

---

## The Architecture

```
[USER] gives any reference image
       |
[STEP 1] ANALYZE
         Read the image. Extract design intent:
         brand direction, category, tone, color palette,
         layout style, imagery type, section patterns.
         (30 seconds. No output yet.)
       |
[STEP 2] WRITE THE BLUEPRINT
         Produce the complete structured specification document.
         Every value locked before imagegen runs:
         - Brand identity (name, tagline, category)
         - Exact color tokens (hex codes + roles)
         - Exact typography (font names, weights, sizes per breakpoint)
         - Grid system (columns, gaps, container width)
         - Every section with layout spec, content, dimensions
         - Every asset slot (type, ratio, position, description)
         - Every interactive element (behavior, JS pattern)
         - All pages to be built
       |
[STEP 3] GENERATE IMAGEGEN FROM BLUEPRINT
         Translate the blueprint into one imagegen prompt.
         The prompt is a visual description of the blueprint --
         nothing added, nothing invented. Every element in
         the image was already defined in the blueprint.
       |
[PAUSE] PRESENT TO USER
        Show: imagegen visual + blueprint summary card
        "Here is [BRAND]. Blueprint is locked. Say GO to build."
       |
[USER] says: go / yes / build / next / looks good / proceed
       |
[STEP 4] GENERATE ALL ASSETS FROM BLUEPRINT
         Use asset slots defined in blueprint.
         Each imagegen call uses the exact prompt, ratio,
         and style spec written in the blueprint asset list.
       |
[STEP 5] BUILD ALL PAGES FROM BLUEPRINT
         tokens.css is already written in the blueprint.
         Every section is already specced.
         Every asset is already named, sized, and positioned.
         Code is a direct translation of blueprint to HTML/CSS/JS.
         No decisions made during build -- all decisions already made.
       |
[DONE] Deploy-ready website delivered.
```

---

## Step 1 -- Analyze

Read the reference image silently. Extract:

- Visual category (SaaS / gaming / fashion / food / agency / portfolio / tech / etc.)
- Dominant tone (aggressive / minimal / luxury / editorial / playful / technical / warm)
- Color temperature (dark / light / colorful / monochrome)
- Layout style (full-bleed / split / centered / asymmetric / editorial)
- Imagery style (photography / illustration / 3D / abstract / gradient / mixed)
- Section count and types visible or implied

Do not output anything yet. Carry this into Step 2.

---

## Step 2 -- Write the Blueprint

This is the most important step. Write the complete blueprint document before anything else.
The blueprint is structured, precise, and complete. Every value is decided here.
Nothing gets decided during build.

Output the blueprint in this exact format:

```
========================================
BLUEPRINT: [BRAND NAME]
========================================

BRAND
  name:      [invented brand name fitting the aesthetic]
  tagline:   [1-line brand tagline]
  category:  [SaaS / gaming / clothing / food / agency / etc.]
  tone:      [one word: aggressive / minimal / luxury / editorial / technical / warm / bold]
  domain:    [brand-name.com]

----------------------------------------
COLORS
----------------------------------------
  --clr-primary:     #[hex]   [role: main brand color]
  --clr-accent:      #[hex]   [role: highlight, CTAs]
  --clr-bg:          #[hex]   [role: page background]
  --clr-surface:     #[hex]   [role: cards, panels]
  --clr-surface-2:   #[hex]   [role: elevated surface, borders]
  --clr-text:        #[hex]   [role: primary text]
  --clr-text-muted:  #[hex]   [role: secondary text, captions]
  --clr-border:      #[hex]   [role: dividers, outlines]

----------------------------------------
TYPOGRAPHY
----------------------------------------
  display-font:  [Font Name], [weight], [style]  -- Google Fonts
  heading-font:  [Font Name], [weight]            -- Google Fonts
  body-font:     [Font Name], [weight]            -- Google Fonts
  mono-font:     [Font Name], [weight]            -- Google Fonts (if numbers/code used)

  Desktop scale:
    hero-text:    [px] / line-height [ratio] / letter-spacing [em]
    h1:           [px] / line-height [ratio]
    h2:           [px] / line-height [ratio]
    h3:           [px] / line-height [ratio]
    body:         [px] / line-height [ratio]
    small:        [px]
    label:        [px] / letter-spacing [em] / uppercase [yes/no]

  Mobile scale (375px):
    hero-text:    [px]
    h1:           [px]
    h2:           [px]
    h3:           [px]
    body:         [px]

----------------------------------------
GRID
----------------------------------------
  container:      max-width [px], padding 0 [px] desktop / 0 [px] mobile
  columns:        [12 / 6 / custom]
  column-gap:     [px]
  row-gap:        [px]
  section-padding: [px] vertical desktop / [px] vertical mobile

----------------------------------------
SECTIONS
----------------------------------------

[1] NAV
  layout:         horizontal, space-between, sticky top
  height:         [px]
  bg:             [color / transparent --> blur-on-scroll]
  logo:           left, height [px], [SVG wordmark / icon + text]
  links:          center / right, [N] items, [font], [size]px, color [hex]
  cta-button:     [label], [filled/outlined], bg [hex], text [hex], h [px], padding [px px], radius [px]
  mobile:         hamburger below [px]px, menu slides in from [top/right]

[2] HERO
  layout:         [split [%/% left/right] / centered / full-bleed]
  height:         [100vh / [px]px / auto]
  bg:             [color / gradient: [from] --> [to], [angle]deg / image full-bleed]
  content-col:    [% width if split]
  image-col:      [% width if split]

  headline:
    text:         "[HEADLINE TEXT]"
    font:         [display-font], [weight], [size]px desktop / [size]px mobile
    color:        [hex]
    position:     [left-aligned / centered / bottom-left overlay]
    transform:    [uppercase / none]
    max-width:    [px]

  subtext:
    text:         "[SUBTEXT]"
    font:         [body-font], [weight], [size]px
    color:        [hex]
    max-width:    [px]
    margin-top:   [px]

  cta-primary:
    label:        "[LABEL]"
    bg:           [hex], hover: [hex]
    text:         [hex]
    height:       [px]
    padding:      [px] [px]
    border-radius:[px]
    margin-top:   [px]

  cta-secondary:
    label:        "[LABEL]"
    style:        [outlined / ghost / text-link]
    border-color: [hex]
    text:         [hex]
    margin-left:  [px]

  hero-asset:
    slot-name:    hero-illustration (or hero-bg or hero-photo)
    type:         [illustration / photograph / 3D render / abstract]
    placement:    [right-column / absolute-right / full-bleed-bg / bottom-right]
    aspect-ratio: [16/9 / 4/3 / 1/1 / 3/4]
    width:        [% of container or px]
    object-fit:   [cover / contain]
    imagegen-description: "[exact visual description for asset generation]"

[3] [SECTION NAME]
  label:          "[SECTION LABEL]" (small uppercase tag above headline)
  layout:         [full-width / 2-col [%/%] / 3-col equal / grid [cols x rows] / centered]
  bg:             [hex]
  padding:        [px] vertical
  headline:       "[TEXT]", [font], [size]px, [color]
  body:           "[TEXT]", [font], [size]px, [color]
  asset-slot:     [slot-name], [type], [ratio], [position in layout]
  components:     [list: card / stat / badge / avatar / icon-row / etc.]
  
  [For each card/component in this section:]
  card:
    width:        [px or fraction]
    bg:           [hex]
    radius:       [px]
    padding:      [px]
    border:       [px solid hex / none]
    icon:         [Lucide icon name / custom SVG slot-name]
    headline:     [size]px, [font], [weight]
    body:         [size]px, [color]
    cta:          [label / none]

[4...N] [repeat for every section]

[N] FOOTER
  layout:         [full-width, columns]
  bg:             [hex]
  padding:        [px] top / [px] bottom
  logo:           left column, height [px]
  tagline:        [size]px below logo
  columns:        [N] link columns, [label], [N] links each
  social-icons:   [platform list], [size]px, color [hex]
  legal:          copyright text, [size]px, [color]
  border-top:     [px solid hex / none]

----------------------------------------
ASSET LIST
----------------------------------------
  [Every asset that will be generated via imagegen or Lucide.]
  Format: slot-name | type | ratio | dimensions | position-in-layout | imagegen-prompt

  hero-illustration | illustration | 4/3 | 600px wide | right column, vertically centered |
    "[Detailed imagegen prompt. Style, subject, colors, mood, format.]"

  logo-main | SVG wordmark | 1/1 | 160x40px | nav top-left and footer |
    "[Logo description: style, letterforms, mark, colors, transparent bg]"

  favicon | PNG icon | 1/1 | 64x64px | browser tab |
    "[Simplified logo mark, square, bold, readable at small size]"

  [section-img-1] | [type] | [ratio] | [size] | [position] |
    "[imagegen prompt]"

  [repeat for every image asset in the design]

  Lucide icons used:
    [section] -- [icon-name]: [usage]
    [section] -- [icon-name]: [usage]

----------------------------------------
INTERACTIVE ELEMENTS
----------------------------------------
  hamburger-menu:  below [px]px, toggle .nav-open on <body>, slides from top/right
  scroll-reveal:   .reveal class, IntersectionObserver threshold 0.15, translateY 24px --> 0, 0.5s ease
  pricing-toggle:  monthly/yearly, swaps [data-monthly]/[data-yearly] attributes
  dark-mode:       [yes / no], localStorage key "theme", class "dark" on <html>
  smooth-scroll:   all nav anchor links
  form-validation: [which page], required fields, email format, loading state, success message
  [other components from visual: tabs / accordion / carousel / counter / etc.]

----------------------------------------
PAGES TO BUILD
----------------------------------------
  index.html       -- landing page (this blueprint)
  features.html    -- [brief description of page purpose]
  pricing.html     -- [brief description]
  about.html       -- [brief description]
  contact.html     -- [brief description]
  404.html         -- on-brand error page
  [additional pages if visible in reference]

========================================
BLUEPRINT COMPLETE
========================================
```

This document is the single source of truth. Every decision is made here. Nothing changes during build.

---

## Step 3 -- Generate Imagegen Visual FROM Blueprint

Translate the blueprint into one imagegen prompt. The visual must reflect what is written
in the blueprint -- every section, every layout, every color, every asset slot.

Build the prompt by reading the blueprint top to bottom:

```
A full-length [CATEGORY] website landing page for a brand called [BRAND NAME].
"[TAGLINE]"

Vertical scroll layout showing all sections in this exact order:

[1] NAV: [exact nav description from blueprint]
[2] HERO: [exact hero spec from blueprint -- layout %, headline text, cta positions, image slot]
[3] [SECTION NAME]: [exact section spec]
[4] [SECTION NAME]: [exact section spec]
...
[N] FOOTER: [exact footer spec]

Exact colors: primary [hex], accent [hex], bg [hex], surface [hex], text [hex].
Typography: [display-font] [weight] for headlines, [body-font] for body text.
Imagery: [imagery style description].
Tone: [tone]. Layout precision: [grid and spacing description].
Clean professional website mockup, full vertical page view,
all sections visible, high detail, sharp, pixel-perfect design reference.
```

Generate the image. Do not proceed to PAUSE until the image is generated.

---

## Step 4 -- PAUSE POINT

Present the visual and a compressed blueprint summary:

```
+----------------------------------------------------------+
|  BLUEPRINT LOCKED -- VISUAL READY FOR REVIEW             |
+----------------------------------------------------------+
|  Brand:     [NAME] -- [TAGLINE]                          |
|  Category:  [CATEGORY]  |  Tone: [TONE]                  |
|  Colors:    [PRIMARY] [ACCENT] [BG] [TEXT]               |
|  Fonts:     [DISPLAY FONT] + [BODY FONT]                 |
|  Sections:  [N] sections -- [list names]                 |
|  Assets:    [N] images to generate + [N] Lucide icons    |
|  Pages:     [list all pages]                             |
+----------------------------------------------------------+
|  The blueprint is locked. This visual is built from it.  |
|  Say GO to generate all assets and build the website.    |
|  Tell me what to change if anything looks off.           |
+----------------------------------------------------------+
```

Wait for the user. Do not generate assets or write code before confirmation.

Valid signals: go / yes / build / next / looks good / perfect / do it / proceed

If the user requests a change -- update the blueprint first, then re-generate the imagegen visual.
Never re-generate the visual without updating the blueprint. They must stay in sync.

---

## Step 5 -- Generate All Assets FROM Blueprint

Read the ASSET LIST section of the blueprint. Generate each asset in order using the
exact imagegen prompt written in the blueprint. Do not modify prompts during generation.

Generate in this order:
1. logo-main (SVG wordmark -- used in nav and footer)
2. favicon (simplified mark)
3. hero-illustration or hero-photo (largest, most important asset)
4. All section images (in section order)
5. Gallery images (in grid order: gallery-1, gallery-2, ... gallery-N)

After each generation, verify against blueprint spec:
- Correct aspect ratio
- Colors match blueprint palette
- Style consistent with other generated assets

Asset generation checklist:
```
[ ] logo-main generated: SVG, transparent bg, matches brand identity
[ ] favicon generated: simplified mark, square, bold
[ ] hero asset generated: correct ratio, correct style, dominant colors match
[ ] all section assets generated: count matches ASSET LIST
[ ] all gallery images generated: same ratio, consistent visual style
[ ] all assets visually belong to the same brand system
```

Do not proceed to Step 6 until all assets are checked.

---

## Step 6 -- Build All Pages FROM Blueprint

Build in this order. Complete each file fully before starting the next.

### 6a -- tokens.css (first file, always)

The color and typography values come directly from the blueprint COLORS and TYPOGRAPHY sections.
Do not invent values. Transcribe from blueprint.

```css
:root {
  /* From blueprint COLORS */
  --clr-primary:    [exact hex from blueprint];
  --clr-accent:     [exact hex from blueprint];
  --clr-bg:         [exact hex from blueprint];
  --clr-surface:    [exact hex from blueprint];
  --clr-surface-2:  [exact hex from blueprint];
  --clr-text:       [exact hex from blueprint];
  --clr-text-muted: [exact hex from blueprint];
  --clr-border:     [exact hex from blueprint];

  /* From blueprint TYPOGRAPHY */
  --font-display:  '[display-font]', sans-serif;
  --font-heading:  '[heading-font]', sans-serif;
  --font-body:     '[body-font]', sans-serif;
  --font-mono:     '[mono-font]', monospace;

  /* From blueprint TYPOGRAPHY desktop scale */
  --text-hero:  [px from blueprint];
  --text-h1:    [px from blueprint];
  --text-h2:    [px from blueprint];
  --text-h3:    [px from blueprint];
  --text-body:  [px from blueprint];
  --text-sm:    [px from blueprint];
  --text-label: [px from blueprint];

  /* From blueprint GRID */
  --container:     [px from blueprint];
  --section-pad-v: [px from blueprint];
  --col-gap:       [px from blueprint];

  /* Spacing (8px grid) */
  --sp-1: 8px;  --sp-2: 16px; --sp-3: 24px; --sp-4: 32px;
  --sp-6: 48px; --sp-8: 64px; --sp-12: 96px; --sp-16: 128px;

  /* Radii */
  --radius-sm: 4px; --radius-md: 8px;
  --radius-lg: 16px; --radius-full: 9999px;
}

/* Mobile scale -- from blueprint TYPOGRAPHY mobile scale */
@media (max-width: 767px) {
  :root {
    --text-hero: [mobile px from blueprint];
    --text-h1:   [mobile px from blueprint];
    --text-h2:   [mobile px from blueprint];
    --text-h3:   [mobile px from blueprint];
  }
}
```

Also write tokens.json (Style Dictionary format) and tailwind.config.js from the same values.

### 6b -- index.html

Build section by section, following blueprint SECTIONS in exact order.
For each section, read the blueprint spec and implement it directly.

**Asset placement rules (from blueprint ASSET LIST):**

| Placement type | CSS implementation |
|---|---|
| full-bleed-bg | background-image: url(); background-size: cover; background-position: center |
| right-column | grid column 2; width 100%; height auto; object-fit: contain |
| absolute-right | position: absolute; right: 0; top: 50%; transform: translateY(-50%) |
| inline-card | width 100%; aspect-ratio: [from blueprint]; object-fit: cover |
| gallery-grid | CSS grid; grid-template-columns: repeat([N], 1fr); aspect-ratio: [from blueprint] |

All images get:
- `alt="[descriptive text matching imagegen description]"` -- never blank
- `loading="lazy"` on all below-fold images
- `width` and `height` attributes matching blueprint dimensions (prevents layout shift)

**Interactive elements -- all from blueprint INTERACTIVE ELEMENTS section:**

Hamburger:
```javascript
const burger = document.querySelector('[data-burger]');
const menu = document.querySelector('[data-nav-menu]');
burger.addEventListener('click', () => {
  const open = menu.classList.toggle('is-open');
  burger.setAttribute('aria-expanded', open);
  document.body.style.overflow = open ? 'hidden' : '';
});
```

Scroll reveal:
```javascript
const io = new IntersectionObserver(
  entries => entries.forEach(e => e.isIntersecting && e.target.classList.add('revealed')),
  { threshold: 0.15 }
);
document.querySelectorAll('.reveal').forEach(el => io.observe(el));
```
```css
.reveal { opacity: 0; transform: translateY(24px); transition: opacity .5s ease, transform .5s ease; }
.reveal.revealed { opacity: 1; transform: none; }
```

Pricing toggle (if in blueprint):
```javascript
const toggle = document.querySelector('[data-pricing-toggle]');
document.querySelectorAll('[data-monthly]').forEach(el => {
  toggle.addEventListener('change', () => {
    el.textContent = toggle.checked ? el.dataset.yearly : el.dataset.monthly;
  });
});
```

Dark mode (if in blueprint):
```javascript
const root = document.documentElement;
const saved = localStorage.getItem('theme') || 'light';
root.classList.add(saved);
document.querySelector('[data-theme-toggle]')?.addEventListener('click', () => {
  root.classList.toggle('dark');
  localStorage.setItem('theme', root.classList.contains('dark') ? 'dark' : 'light');
});
```

Form (if in blueprint):
```javascript
document.querySelector('[data-form]')?.addEventListener('submit', e => {
  e.preventDefault();
  const btn = e.target.querySelector('[type=submit]');
  const email = e.target.querySelector('[type=email]');
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
    email.setCustomValidity('Enter a valid email'); email.reportValidity(); return;
  }
  btn.textContent = 'Sending...'; btn.disabled = true;
  setTimeout(() => {
    e.target.innerHTML = '<p class="form-success">You\'re in. Check your inbox.</p>';
  }, 1200);
});
```

**index.html build checklist -- verify before moving to next page:**
```
[ ] All sections present in blueprint order
[ ] All asset slots filled with generated images (no placeholder divs)
[ ] All alt attributes: descriptive, not blank
[ ] All colors from tokens.css variables (zero hardcoded hex)
[ ] Google Fonts CDN in <head> for all fonts in blueprint
[ ] Nav: all links, CTA button, hamburger trigger
[ ] Hamburger: JS implemented, aria-expanded, body scroll lock
[ ] Smooth scroll: all anchor links have scroll-behavior
[ ] All CTA buttons: valid href or data attribute
[ ] Pricing toggle: JS implemented if in blueprint
[ ] Dark mode: JS + CSS if in blueprint
[ ] Form: validation + loading + success if in blueprint
[ ] Scroll reveal: .reveal on all content elements
[ ] Open Graph meta tags: title, description, image, url
[ ] canonical <link> in <head>
[ ] viewport meta tag present
[ ] No horizontal scroll (check all section widths)
```

**Responsive checklist -- verify for every page:**
```
375px mobile:
  [ ] Hamburger visible, desktop nav hidden
  [ ] Hero: single column, font >= blueprint mobile scale
  [ ] All grids: collapsed to 1 column
  [ ] No element wider than viewport
  [ ] All buttons and links: min-height 44px (tap targets)
  [ ] No font smaller than 14px

768px tablet:
  [ ] Nav: hamburger or compact
  [ ] 2-col grids active where blueprint specifies
  [ ] Hero image visible alongside text
  [ ] Cards: 2-per-row

1024px laptop:
  [ ] Full nav visible
  [ ] 3-col grids active where blueprint specifies
  [ ] Container bounded, not full-bleed

1440px desktop:
  [ ] Container max-width from blueprint enforced
  [ ] No content stretching beyond container
  [ ] Layout matches blueprint section specs
```

### 6c -- Inner Pages (same blueprint-first process)

For each inner page in the blueprint PAGES list:

**1. Write the inner page blueprint:**

Extend the main blueprint with page-specific sections. Same brand, same tokens, same nav.
Add the page-specific content spec:

features.html blueprint addition:
```
PAGE: features.html
Sections:
  PAGE-HERO: headline "[Features headline]", subtext, muted bg matching --clr-surface
  FEATURES-ALTERNATING: rows alternating dark/light bg, image left + text right then flip
    each row: asset-slot | [ratio] | description
  COMPARISON-TABLE: columns [Brand], [Comp A], [Comp B]; rows = feature list; checkmarks/X
  DEMO-PREVIEW: full-width screenshot or UI mockup, caption below, border radius [px]
  PAGE-CTA: same full-width CTA banner as landing page
```

pricing.html blueprint addition:
```
PAGE: pricing.html
Sections:
  PAGE-HERO: "Choose Your [X]" headline, monthly/yearly toggle above cards
  PRICING-CARDS: 3-col, card specs:
    tier-1: [name], $[price]/mo, [N] features, [CTA label], bg --clr-surface
    tier-2: [name HIGHLIGHTED], $[price]/mo, [N] features, [CTA label], bg --clr-primary
    tier-3: [name], $[price]/mo, [N] features, [CTA label], bg --clr-surface
  FAQ: accordion, [N] questions, one open at a time
  PAGE-CTA: same CTA banner
```

about.html blueprint addition:
```
PAGE: about.html
Sections:
  PAGE-HERO: mission statement headline, full-bleed or muted bg
  STORY: 2-col 50/50, text left, image right, asset-slot: about-photo | 4/3
  VALUES: 3-col cards, icon + headline + body each
  TEAM: grid [N]-col, each card: photo (asset-slot: team-[N] | 1/1) + name + role
  TIMELINE: [horizontal/vertical], [N] milestones
```

contact.html blueprint addition:
```
PAGE: contact.html
Sections:
  PAGE-HERO: minimal, "Get in Touch" headline
  CONTACT-SPLIT: 2-col 55/45
    left: form (name, email, message, submit)
    right: contact details, address, hours, social links
  MAP: full-width, 400px height, --clr-surface bg, map icon centered
```

404.html blueprint addition:
```
PAGE: 404.html
  centered, 100vh
  "404" display text [display-font], [large size]px, --clr-primary
  headline: "Page not found."
  subtext: "[friendly brand-voice message]"
  cta: "Back to Home" --> index.html, filled primary button
  bg: --clr-bg or brand gradient
```

**2. Generate imagegen visual for that page FROM its blueprint**
**3. Build HTML from page blueprint**
**4. Run build checklist and responsive checklist**

---

## Step 7 -- File Delivery

```
[brand-name]/
  index.html
  features.html
  pricing.html
  about.html
  contact.html
  404.html
  tokens.css
  tokens.json
  tailwind.config.js
  sitemap.xml
  robots.txt
  assets/
    logo.svg
    logo.png
    favicon.png
    hero.[ext]
    [all generated images named by slot-name from blueprint]
  icons/
    [any custom SVG icons not covered by Lucide]
```

---

## Rules That Cannot Be Broken

1. Blueprint is written BEFORE imagegen is called. No exceptions.
2. Imagegen is called BEFORE any HTML is written. No exceptions.
3. All code values come from the blueprint. If a value is not in the blueprint, add it to the blueprint first, then use it.
4. No hardcoded hex in HTML or CSS -- always use tokens.css variables.
5. No placeholder divs -- every image slot is filled with a generated asset.
6. No blank alt attributes on visible images.
7. No emoji or decorative characters used as icons -- Lucide or generated SVG only.
8. Every interactive element in the blueprint must be functionally implemented -- not mocked.
9. Every inner page gets its own imagegen visual generated before its HTML is written.
10. Blueprint and imagegen visual must always be in sync -- if visual changes, blueprint changes first.
