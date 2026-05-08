# v5.0 Token Export Reference

## tokens.json — Style Dictionary Format

Write alongside `tokens.css`. Enables cross-platform portability: iOS (Swift), Android (XML), Tailwind config, SCSS maps, documentation sites.

```json
{
  "color": {
    "primary": { "value": "#e94560", "type": "color", "description": "Main brand CTA color" },
    "primary-9": { "value": "#e94560", "type": "color" },
    "primary-11": { "value": "#8c1a2a", "type": "color", "description": "Accessible text on light bg" },
    "accent": { "value": "#...", "type": "color" },
    "bg": { "value": "#f8f8f8", "type": "color" },
    "surface": { "value": "#ffffff", "type": "color" },
    "text": { "value": "#111111", "type": "color" },
    "text-muted": { "value": "#666666", "type": "color" },
    "border": { "value": "#e0e0e0", "type": "color" }
  },
  "typography": {
    "display": { "value": "Outfit", "type": "fontFamily" },
    "body": { "value": "Inter", "type": "fontFamily" },
    "scale-ratio": { "value": "1.333", "type": "other", "description": "Perfect Fourth" },
    "base-size": { "value": "1rem", "type": "dimension" }
  },
  "fontSize": {
    "xs":   { "value": "0.563rem", "type": "dimension" },
    "sm":   { "value": "0.75rem",  "type": "dimension" },
    "base": { "value": "1rem",     "type": "dimension" },
    "lg":   { "value": "1.333rem", "type": "dimension" },
    "xl":   { "value": "1.777rem", "type": "dimension" },
    "2xl":  { "value": "2.369rem", "type": "dimension" },
    "3xl":  { "value": "3.157rem", "type": "dimension" },
    "4xl":  { "value": "4.209rem", "type": "dimension" }
  },
  "spacing": {
    "1":  { "value": "0.25rem", "type": "spacing" },
    "2":  { "value": "0.5rem",  "type": "spacing" },
    "4":  { "value": "1rem",    "type": "spacing" },
    "6":  { "value": "1.5rem",  "type": "spacing" },
    "8":  { "value": "2rem",    "type": "spacing" },
    "12": { "value": "3rem",    "type": "spacing" },
    "16": { "value": "4rem",    "type": "spacing" },
    "24": { "value": "6rem",    "type": "spacing" },
    "32": { "value": "8rem",    "type": "spacing" }
  },
  "borderRadius": {
    "sm":   { "value": "4px",    "type": "borderRadius" },
    "md":   { "value": "8px",    "type": "borderRadius" },
    "lg":   { "value": "16px",   "type": "borderRadius" },
    "xl":   { "value": "24px",   "type": "borderRadius" },
    "full": { "value": "9999px", "type": "borderRadius" }
  },
  "boxShadow": {
    "sm": { "value": "0 1px 3px rgba(0,0,0,0.06)",  "type": "boxShadow" },
    "md": { "value": "0 4px 16px rgba(0,0,0,0.08)", "type": "boxShadow" },
    "lg": { "value": "0 8px 32px rgba(0,0,0,0.12)", "type": "boxShadow" }
  }
}
```

## tailwind.config.js — Token Mapping

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./**/*.html', './**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#e94560',
          1: 'hsl(350,80%,98%)',
          2: 'hsl(350,75%,95%)',
          // ... steps 3-8
          9:  '#e94560',
          10: 'hsl(350,75%,45%)',
          11: 'hsl(350,70%,35%)',
          12: 'hsl(350,65%,18%)',
        },
        accent: { DEFAULT: '#...' },
        bg:      '#f8f8f8',
        surface: '#ffffff',
      },
      fontFamily: {
        display: ['Outfit', 'sans-serif'],
        body:    ['Inter', 'sans-serif'],
      },
      fontSize: {
        xs:   ['clamp(0.563rem,1vw,0.75rem)',  { lineHeight: '1.4' }],
        sm:   ['clamp(0.75rem,1.5vw,0.875rem)',{ lineHeight: '1.5' }],
        base: ['clamp(1rem,2vw,1.125rem)',      { lineHeight: '1.6' }],
        lg:   ['clamp(1.333rem,2.5vw,1.5rem)', { lineHeight: '1.5' }],
        xl:   ['clamp(1.777rem,3vw,2rem)',      { lineHeight: '1.4' }],
        '2xl':['clamp(2.369rem,4vw,2.667rem)', { lineHeight: '1.3' }],
        '3xl':['clamp(3.157rem,5vw,3.556rem)', { lineHeight: '1.2' }],
        '4xl':['clamp(4.209rem,6vw,4.741rem)', { lineHeight: '1.1' }],
      },
      borderRadius: {
        sm: '4px', md: '8px', lg: '16px', xl: '24px',
      },
      boxShadow: {
        sm: '0 1px 3px rgba(0,0,0,0.06)',
        md: '0 4px 16px rgba(0,0,0,0.08)',
        lg: '0 8px 32px rgba(0,0,0,0.12)',
      },
    },
  },
  plugins: [],
}
```

## content.json — Content Layer

```json
{
  "brand": {
    "name": "[Brand Name]",
    "tagline": "[Tagline]",
    "description": "[Meta description, 150-160 chars]",
    "email": "[contact@brand.com]",
    "phone": "[+1 (555) 000-0000]"
  },
  "nav": {
    "links": [{ "label": "Home", "href": "#home" }],
    "cta": { "label": "Get Started", "href": "#signup" }
  },
  "hero": {
    "headline": "[OCR-extracted or generated]",
    "subheadline": "[OCR-extracted or generated]",
    "cta_primary": { "label": "[CTA text]", "href": "#" }
  },
  "features": [
    { "icon": "[emoji]", "title": "[name]", "description": "[desc]" }
  ],
  "testimonials": [
    { "quote": "[text]", "name": "[Name]", "role": "[Role, Company]" }
  ],
  "pricing": [
    { "tier": "[Name]", "price": "[price]", "period": "/month",
      "features": ["[f1]", "[f2]"], "cta": "[Buy Now]", "highlighted": false }
  ],
  "faq": [{ "question": "[q]", "answer": "[a]" }],
  "footer": {
    "legal": "[© 2026 Brand Name. All rights reserved.]",
    "social": [{ "platform": "twitter", "href": "#" }]
  }
}
```
