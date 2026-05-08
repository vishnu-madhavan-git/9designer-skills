# v5.0 Workflow Reference

## PAUSE POINT — Design Brief Template

After completing Stage 1 analysis, present this design brief to the user and wait for confirmation before writing any code or generating final assets.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎨 9DESIGNER — DESIGN BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BRAND: [Name] | INDUSTRY: [Type] | STYLE: [Aesthetic direction]

COLORS
  Primary: #[hex] | Accent: #[hex] | BG: #[hex] | Text: #[hex]
  12-step scale: generated for primary and accent ✓

TYPOGRAPHY
  Display: [Font] | Body: [Font] | Scale ratio: [name, e.g. Perfect Fourth 1.333]
  Size range: [smallest] → [largest]

EXTRACTED TEXT (OCR)
  Hero: "[exact headline if visible]"
  Nav: [list of nav labels]
  CTA: "[button text]"
  [other key copy]

PAGES
  [Numbered list of all pages planned]

SECTIONS (homepage, in order)
  [Numbered list of all sections]

ASSETS TO GENERATE (Stage 2)
  🖼️  Logo: [description]
  🖼️  Favicon: [emoji or icon concept]
  🖼️  Hero image: [description]
  🖼️  Feature icons: [count and style]
  🖼️  Section images: [list]

COMPLEXITY PATH
  [✅ Vanilla HTML/CSS/JS] or [✅ React + Tailwind + shadcn/ui]
  [Reason if React path chosen — 3+ complex components]

OPTIONAL FLAGS
  [🟡 GENERATIVE BACKGROUND — p5.js canvas if confirmed]
  [🟡 3D OPPORTUNITY — Three.js if confirmed]
  [Subagent dispatch: YES/NO]

ESTIMATED OUTPUT
  [n files, ~n lines of code]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ready to build? Say "go", "yes", "build", or "next" to proceed.
Anything to adjust? Tell me now before code generation starts.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Subagent Dispatch Mode

Activate when the site has 5+ pages OR 8+ major sections. Dispatch parallel subagents:

```
Main Agent (orchestrator):
  ├── Subagent A: OCR + Stage 1 analysis → outputs design-brief.json
  ├── Subagent B: HTML structure for all sections (semantic, IDs, ARIA)
  ├── Subagent C: CSS (tokens, responsive, animations, dark mode)
  ├── Subagent D: JavaScript (menu, scroll, forms, carousels, cookie banner)
  └── Subagent E: Playwright QA (4-breakpoint + pixel diff + Lighthouse + WCAG)

Main Agent merges all outputs, reviews, delivers.
```

Each subagent receives `design-brief.json` as context. Two-stage review per output: spec compliance → code quality.

## Confirmation Signals

Any of these trigger Turn 2 (build phase):
"go", "yes", "next", "build", "looks good", "proceed", "do it", "fire", "let's go", "start", "continue", "ship it", or any clearly positive forward signal.
