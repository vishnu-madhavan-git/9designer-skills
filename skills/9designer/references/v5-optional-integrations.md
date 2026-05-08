# v5.0 Optional Integrations Reference

All tools in this file are optional accelerators. Never fail a 9Designer run because these are unavailable.

## Generative Backgrounds (p5.js)

Activate only when `🟡 GENERATIVE BACKGROUND DETECTED` was flagged in Stage 1.

```html
<!-- In <head> -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js" defer></script>

<!-- In hero section -->
<canvas id="hero-canvas" aria-hidden="true"></canvas>
```

```css
#hero-canvas {
  position: absolute; inset: 0; width: 100%; height: 100%;
  z-index: 0; opacity: 0.6; pointer-events: none;
}
.hero { position: relative; overflow: hidden; }
.hero-content { position: relative; z-index: 1; }
```

Choose system based on reference aesthetic:
- **Particle field** (organic, flowing): `new p5(sketch, document.getElementById('hero-canvas'))`
- **Flow field** (noise-based, mesmerizing): use `p5.noise()` to drive angle fields
- **Noise mesh** (texture, depth): grid of points displaced by Perlin noise

Performance: max 200 particles, `requestAnimationFrame` via p5. Add `document.addEventListener('visibilitychange', ...)` to pause when tab hidden.

## 3D Assets (Three.js + Sketchfab)

Activate only when `🟡 3D OPPORTUNITY DETECTED` was flagged and user confirms.

```html
<script type="importmap">
  { "imports": { "three": "https://cdn.jsdelivr.net/npm/three@0.160/build/three.module.js",
                 "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.160/examples/jsm/" } }
</script>
<script type="module">
  import * as THREE from 'three';
  import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 100);
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setSize(container.clientWidth, container.clientHeight);
  container.appendChild(renderer.domElement);

  const loader = new GLTFLoader();
  loader.load('model.glb', gltf => {
    scene.add(gltf.scene);
    animate();
  });

  function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
  }
</script>
```

Sketchfab sourcing: search `https://sketchfab.com/search?q=[keyword]&type=models&sort_by=-likeCount&license=cc-attribution` for CC-licensed models. Download GLB format. Record attribution in `notes/builder-handoff.md`.

Performance budget: < 200K triangles. Mobile fallback: `<img>` static render inside the same container with CSS `display:none` at desktop widths.

## Figma MCP Integration

Available when `mcp__figma__*` tools appear in the session tool list.

1. Export color tokens → Figma Color Variables (organize into collections: Colors, Typography, Spacing)
2. Export typography → Figma Text Styles
3. Create frames per major section (nav, hero, features, footer) as Figma components
4. Enable bidirectional loop: designer edits Figma → exports updated tokens → 9Designer regenerates

Skip gracefully when Figma MCP is not configured. Mention availability in final report.

## Penpot MCP Integration

Available when `mcp__penpot__*` tools appear in the session tool list. Privacy-first, self-hosted alternative to Figma.

1. Export all color tokens → Penpot color library
2. Export typography → Penpot text styles
3. Create component definitions per section
4. All data stays local — no cloud upload

## Design System Map (D3)

Generate `design-system-map.html` — a standalone interactive knowledge graph.

```javascript
// Build relationship data
const nodes = [
  { id: 'home', type: 'page', label: 'Home' },
  { id: 'hero', type: 'section', label: 'Hero Section' },
  { id: 'btn-primary', type: 'component', label: 'PrimaryButton' },
  { id: 'clr-primary', type: 'token', label: '--clr-primary' },
];
const links = [
  { source: 'home', target: 'hero', rel: 'contains' },
  { source: 'hero', target: 'btn-primary', rel: 'uses' },
  { source: 'btn-primary', target: 'clr-primary', rel: 'references' },
];
```

Render with D3 force-directed layout (`https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js` via CDN). Color-code nodes: pages (blue), sections (green), components (orange), tokens (purple). Click to highlight all connections. No server required.
