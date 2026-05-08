---
name: 9designer
description: "Codex-native image-to-website pipeline. Give any reference image -- a Pinterest pin, screenshot, photo, anything -- and 9designer invents a brand, generates a full landing page visual for confirmation, then builds the complete website (all pages, assets, tokens) once you say go."
---

# 9Designer

Give any image. Get a complete website.

9Designer reads any reference image, invents a fitting brand and context, generates a full visual mockup of the landing page for your approval, then builds the entire site once confirmed.

---

## The Workflow

```
[USER] gives any image
       |
[STEP 1] Codex analyzes the image
         - Invents brand name, tagline, category
         - Extracts color palette, typography style, layout structure
         - Identifies tone, imagery style, section patterns
       |
[STEP 2] Codex generates ONE imagegen visual
         - Full landing page mockup: nav to footer
         - All sections visible, real content, real layout
         - Exact colors, font styles, illustration direction
       |
[PAUSE] Codex presents the visual + brief summary
        "Here is [BRAND NAME] -- a [CATEGORY] landing page.
         Say GO to build all pages."
       |
[USER] says go / yes / build / next / looks good
       |
[STEP 3] Codex generates all image assets
         - Logo (SVG + PNG)
         - Hero image / illustration
         - Section images, icons, favicons
       |
[STEP 4] Codex builds all pages
         - index.html (landing page matching the confirmed visual exactly)
         - All inner pages (features, pricing, about, contact, etc.)
         - 404.html
         - tokens.css, tokens.json, tailwind.config.js
         - sitemap.xml, robots.txt
       |
[DONE] Deploy-ready folder delivered
```

---

## Step 1 -- Analyze the Image

When the user provides any image, extract:

**Brand**
- Invent a name that fits the aesthetic and category (do not copy names from the image)
- Write a 1-line tagline
- Identify category: SaaS / gaming / clothing / food / agency / portfolio / tech / finance / health / other

**Visual System**
- Dominant colors: extract 4-6 hex codes, name each role (primary, accent, bg, text, surface, border)
- Typography style: serif editorial / bold condensed / clean sans / mono / display
- Layout type: full-bleed hero / split hero / centered / asymmetric
- Imagery style: photography / illustration / 3D render / abstract / geometric / gradient

**Sections**
- List every section visible or implied: nav, hero, social proof, features, dashboard/preview, pricing, CTA, footer
- Note layout per section: full-width / 2-col / 3-col / grid / centered

**Tone**
- Pick one: aggressive / playful / minimal / luxury / editorial / technical / warm / bold

---

## Step 2 -- Generate the Landing Page Visual

Build ONE imagegen prompt using everything from Step 1. This prompt generates the full visual confirmation the user approves before any code is written.

**Prompt structure:**
```
A full-length [CATEGORY] website landing page for a brand called [NAME].
[TAGLINE] -- [ONE LINE ON WHAT THE BRAND DOES].
Vertical scroll layout showing all sections top to bottom:

NAV: [nav description -- logo position, link style, CTA button]
HERO: [hero layout -- bg type, headline style, subtext, CTA buttons, imagery]
[SECTION 2 LABEL]: [layout + content description]
[SECTION 3 LABEL]: [layout + content description]
[SECTION N LABEL]: [layout + content description]
FOOTER: [footer layout -- logo, columns, social icons]

Aesthetic: [tone]. Brand colors: [list hex codes].
Typography: [font style description -- weight, size contrast, character].
[IMAGERY NOTE: illustration style / photography style / 3D etc].
Clean professional website mockup, full-page vertical view,
high detail, sharp, production-ready design.
```

Generate the image. Do not write any code before the user confirms.

---

## Step 3 -- PAUSE POINT

After generating the visual, present:

```
+----------------------------------------------------------+
|  DESIGN READY FOR REVIEW                                 |
+----------------------------------------------------------+
|  Brand:     [NAME]                                       |
|  Category:  [CATEGORY]                                   |
|  Tagline:   [TAGLINE]                                    |
|  Tone:      [TONE]                                       |
|  Colors:    [PRIMARY] [ACCENT] [BG] [TEXT]               |
|  Pages:     index, [list all pages], 404                 |
+----------------------------------------------------------+
|  Say GO to build. Tell me what to change if needed.     |
+----------------------------------------------------------+
```

Wait for the user. Do not proceed until confirmed.

Valid signals to continue: go / yes / build / next / looks good / perfect / do it / proceed

---

## Step 3b -- Visual Map (extract from confirmed visual)

Before generating any asset or writing any code, read the confirmed imagegen visual
and document the exact element map. This map is the contract everything is built against.

```
VISUAL MAP
----------
Sections (in order):
  1. nav
  2. hero
  3. [section name]
  ...
  N. footer

Asset slots:
  hero-bg:          [full-bleed / right-col / floating] -- [description]
  feature-img-1:    [position in section] -- [description]
  gallery-1 to N:   [grid position] -- [description]
  logo:             [nav top-left / centered]

Text overlays:
  hero-headline:    [position: centered / bottom-left / top-left]
  hero-sub:         [position relative to headline]

Buttons / CTAs:
  primary-cta:      [label] [position in hero]
  secondary-cta:    [label] [position]
  nav-cta:          [label] [style: filled / outlined]

Toggles detected:
  pricing-toggle:   [yes / no]
  dark-mode:        [yes / no]
  tabs/accordion:   [yes / no -- which section]

Interactive components:
  [list every interactive element visible in the confirmed visual]
```

Do not skip this step. Every asset slot must be named before any imagegen call is made.

---

## Step 4 -- Generate All Assets (after GO)

Before writing a single line of HTML, generate all image assets via imagegen.

Generate in this order:

1. **Logo** -- brand mark + wordmark, on transparent background, vector clean
2. **Favicon** -- simplified logo mark, 32x32 appropriate
3. **Hero image / illustration** -- matches hero section from confirmed visual
4. **Section images** -- any photography, illustrations, or background images used in sections
5. **Icons** -- if custom icons needed beyond Lucide/standard libraries

Each imagegen prompt must reference the confirmed visual's exact style, colors, and tone. Assets must look like they belong to the same brand.

**Asset generation checklist -- verify before writing any HTML:**
```
[ ] Logo generated: SVG + PNG, transparent background
[ ] Favicon generated: simplified mark, square crop
[ ] Hero image/illustration generated: matches hero slot in visual map
[ ] All section images generated: count matches visual map asset slots
[ ] Gallery images generated: all same aspect ratio, consistent style
[ ] All assets visually match brand tone and color palette
```

Do not proceed to Step 5 until all boxes are checked.

---

## Step 5 -- Build All Pages

Build in this order. Complete each file fully before moving to the next.

### Design Tokens First

Generate `tokens.css` before any HTML:

```css
:root {
  /* Colors */
  --clr-primary:    [hex];
  --clr-accent:     [hex];
  --clr-bg:         [hex];
  --clr-surface:    [hex];
  --clr-text:       [hex];
  --clr-text-muted: [hex];
  --clr-border:     [hex];

  /* Typography */
  --font-display: '[Font Name]', sans-serif;
  --font-body:    '[Font Name]', sans-serif;

  /* Typescale (Perfect Fourth 1.333) */
  --text-xs:   0.75rem;
  --text-sm:   1rem;
  --text-base: 1.333rem;
  --text-lg:   1.777rem;
  --text-xl:   2.369rem;
  --text-2xl:  3.157rem;
  --text-3xl:  4.209rem;
  --text-4xl:  5.61rem;

  /* Spacing (8px grid) */
  --space-1:  8px;
  --space-2:  16px;
  --space-3:  24px;
  --space-4:  32px;
  --space-6:  48px;
  --space-8:  64px;
  --space-12: 96px;
  --space-16: 128px;

  /* Radii */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
  --radius-full: 9999px;
}
```

Also generate `tokens.json` (Style Dictionary format) and `tailwind.config.js`.

### Pages

Build each page as a complete standalone HTML file:

**index.html** -- landing page, exact match to confirmed visual
- Nav with all links, CTA button
- Every section in the confirmed order
- All generated assets embedded
- Scroll animations (IntersectionObserver, CSS transitions)
- Mobile hamburger menu

**[feature/product].html** -- expanded features or product detail
**pricing.html** -- pricing tiers, toggle monthly/yearly
**about.html** -- brand story, team if applicable
**contact.html** -- contact form, locations if applicable
**404.html** -- on-brand error page

### Asset placement rules (from visual map)

Hero image:
- Full-bleed bg: `background-image` on section, `background-size: cover`, `background-position: center`
- Right-col illustration: CSS grid column 2, `max-width: 100%`, `height: auto`
- Floating/layered: `position: absolute` inside `position: relative` hero, `z-index` layered

Section images:
- Match exact grid position from visual map
- Set `aspect-ratio` CSS to prevent layout shift: `aspect-ratio: 16/9` or `4/3` or `1/1`
- All below-fold images: `loading="lazy"`

Gallery images:
- CSS grid with explicit column count: `grid-template-columns: repeat(N, 1fr)`
- Responsive: 1-col mobile, 2-col tablet, N-col desktop
- Consistent aspect-ratio across all cells

Logo:
- Nav: `height: 36px; width: auto`
- Footer: `height: 28px; width: auto; opacity: 0.85`

### Required in every page

- `<link rel="canonical">` and full Open Graph meta tags
- Skip-to-main link for accessibility
- Dark mode support via `prefers-color-scheme`
- Responsive: 375px / 768px / 1024px / 1440px
- No horizontal scroll at any breakpoint
- All images have descriptive `alt` text

### Interactive elements (must be functional, not decorative)

**Hamburger menu:**
```javascript
const burger = document.querySelector('.burger');
const nav = document.querySelector('.nav-menu');
burger.addEventListener('click', () => {
  nav.classList.toggle('open');
  burger.setAttribute('aria-expanded', nav.classList.contains('open'));
});
```
```css
.nav-menu { display: none; }
.nav-menu.open { display: flex; flex-direction: column; }
@media (min-width: 768px) { .nav-menu { display: flex; } .burger { display: none; } }
```

**Pricing toggle (monthly/yearly):**
```javascript
const toggle = document.querySelector('.pricing-toggle');
const prices = document.querySelectorAll('[data-monthly][data-yearly]');
toggle.addEventListener('change', () => {
  const isYearly = toggle.checked;
  prices.forEach(el => {
    el.textContent = isYearly ? el.dataset.yearly : el.dataset.monthly;
  });
});
```

**Dark mode:**
```javascript
const root = document.documentElement;
const saved = localStorage.getItem('theme');
if (saved) root.classList.add(saved);
document.querySelector('.theme-toggle')?.addEventListener('click', () => {
  root.classList.toggle('dark');
  localStorage.setItem('theme', root.classList.contains('dark') ? 'dark' : 'light');
});
```

**Form validation:**
```javascript
document.querySelector('form')?.addEventListener('submit', (e) => {
  e.preventDefault();
  const email = e.target.querySelector('[type="email"]');
  if (!email.value.includes('@')) {
    email.setCustomValidity('Enter a valid email');
    email.reportValidity();
    return;
  }
  e.target.querySelector('[type="submit"]').textContent = 'Sending...';
  setTimeout(() => {
    e.target.innerHTML = '<p class="success">You\'re in. Check your inbox.</p>';
  }, 1200);
});
```

**index.html build checklist -- verify before moving to next page:**
```
[ ] All sections present in order matching visual map
[ ] All assets placed in correct slots (no placeholder divs)
[ ] All alt="" attributes filled with descriptive text
[ ] Nav: all links present, CTA button styled
[ ] Hamburger: JS toggle works, menu opens/closes
[ ] Smooth scroll: anchor links scroll correctly
[ ] All CTA buttons have valid href or onclick
[ ] Pricing toggle: swaps prices correctly (if present)
[ ] Dark mode: persists on reload via localStorage (if present)
[ ] Forms: validation + loading + success state
[ ] Scroll reveal: IntersectionObserver applied to .reveal elements
[ ] No hardcoded hex -- all colors via tokens.css variables
[ ] Google Fonts CDN loaded in <head>
[ ] Open Graph meta tags complete
[ ] canonical link present
```

**Responsive checklist -- run mentally for every page:**
```
375px mobile:
[ ] Hamburger visible, desktop nav hidden
[ ] Hero single column, headline readable (min 28px)
[ ] All sections stack vertically
[ ] No element overflows horizontally
[ ] Buttons/links min 44px tall
[ ] Font sizes min 14px

768px tablet:
[ ] Nav hamburger or compact links
[ ] 2-col grids active where appropriate
[ ] Hero image visible alongside text
[ ] Feature/pricing cards in 2-col grid

1024px laptop:
[ ] Full horizontal nav
[ ] 3-col grids active
[ ] Containers properly bounded

1440px desktop:
[ ] Max-width container (1200px or 1280px) centered
[ ] No content edge-to-edge without padding
[ ] Layout matches confirmed visual proportions
```

### Scroll animations (standard pattern)

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) e.target.classList.add('visible');
  });
}, { threshold: 0.15 });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

```css
.reveal { opacity: 0; transform: translateY(24px); transition: opacity 0.5s ease, transform 0.5s ease; }
.reveal.visible { opacity: 1; transform: none; }
```

---

## Step 5b -- Inner Pages (imagegen-first for every page)

When the user asks for inner pages after confirming the landing page, OR when building
all pages automatically after GO -- every inner page follows the same visual-first process.

For EACH inner page:

**1. Generate imagegen prompt for that page:**

Use the same brand name, colors, nav style, and typography from the confirmed landing page.
Describe the page-specific content and layout. Example templates:

features.html:
```
Full features/product page for [BRAND], [TAGLINE].
Same nav as landing page. Page-specific sections:
HERO: page hero with headline "[Feature headline]", subtext, muted bg
FEATURES GRID: alternating dark/light rows, feature cards with icons left and text right
COMPARISON TABLE: feature matrix vs competitors, checkmarks/crosses
DEMO PREVIEW: screenshot or UI mockup with caption
CTA: full-width CTA banner matching landing page style
FOOTER: identical to landing page footer
Brand colors: [palette]. Typography: [style]. Same aesthetic as confirmed landing page.
Clean professional website page mockup, full-page vertical view.
```

pricing.html:
```
Pricing page for [BRAND], [TAGLINE].
Same nav as landing page. Sections:
HEADER: "Choose Your Plan" headline, monthly/yearly toggle
PRICING CARDS: 3 tiers side by side -- [Free/Starter], [Pro highlighted], [Enterprise]
Each card: price, billing period, feature list with checkmarks, CTA button
FAQ ACCORDION: 5-6 common pricing questions, expandable
CTA BANNER: bottom full-width CTA
FOOTER: identical to landing page
Brand colors: [palette]. Highlighted card uses accent color.
```

about.html:
```
About page for [BRAND], [TAGLINE].
Same nav as landing page. Sections:
MISSION HERO: bold statement headline, muted full-width bg
STORY SECTION: 2-col -- paragraph text left, brand image right
VALUES GRID: 3-col icon + title + text cards
TEAM GRID: 3-4 team member cards with photo, name, role
TIMELINE: horizontal or vertical milestone list
FOOTER: identical to landing page
Brand colors: [palette]. Warm, human tone.
```

contact.html:
```
Contact page for [BRAND].
Same nav as landing page. Sections:
CONTACT HERO: minimal headline, subtext
SPLIT LAYOUT: form left (name, email, message, submit), contact info right (email, address, hours)
MAP PLACEHOLDER: full-width map area (dark surface color bg with map icon)
SOCIAL LINKS: row of social icons
FOOTER: identical to landing page
Brand colors: [palette].
```

404.html:
```
On-brand 404 error page for [BRAND].
Centered layout, full viewport height.
Large "404" display text in brand font.
Short friendly message: "Page not found. Let's get you back."
"Go Home" CTA button in brand primary color.
Subtle background using brand colors (gradient or texture).
Brand colors: [palette].
```

**2. Generate the page visual**
**3. Extract element map for that page (same format as Step 3b)**
**4. Build HTML to exactly match the generated visual**
**5. Run the index.html checklist adapted for that page**
**6. Run the responsive checklist**

---

## Step 6 -- File Delivery

```
[brand-name]/
  index.html
  [all inner pages].html
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
    [all generated images]
  icons/
    [any custom SVG icons]
```

---

## Quality Rules

- Every color comes from tokens.css -- no hardcoded hex in HTML
- Every font comes from Google Fonts CDN -- no system font guessing
- Every icon comes from Lucide CDN or is a generated SVG -- no emoji as icons
- Every image is either generated by imagegen or sourced with a real URL -- no placeholder divs
- Spacing uses only the 8px grid values from tokens.css
- All interactive elements have :hover and :focus states
- Lighthouse score target: Performance 90+, Accessibility 90+, SEO 100

---

## What This Skill Does NOT Do

- Backend, auth, databases -- static only
- Custom CMS -- use content.json as the data layer
- E-commerce checkout -- layout only, no payment processing
- Pixel-perfect clone of the reference image -- the confirmed imagegen visual is the spec, not the original image
