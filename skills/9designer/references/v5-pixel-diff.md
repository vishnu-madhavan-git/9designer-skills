# v5.0 Pixel Diff Reference

## When to Use

Use pixel diff when Playwright MCP (`browser_evaluate`) is available in the session. Fall back to manual visual comparison when Playwright is not available. Never make the skill fail for lack of this tool.

## Pixelmatch Injection Pattern

After capturing a Playwright screenshot of the built site, compare it to the reference image using pixel data:

```javascript
// Inject via mcp__playwright__browser_evaluate
const result = await page.evaluate(async (referenceDataUrl) => {
  const refCanvas = document.createElement('canvas');
  const refCtx = refCanvas.getContext('2d');
  const refImg = new Image();
  await new Promise(resolve => { refImg.onload = resolve; refImg.src = referenceDataUrl; });
  refCanvas.width = refImg.width;
  refCanvas.height = refImg.height;
  refCtx.drawImage(refImg, 0, 0);
  const refData = refCtx.getImageData(0, 0, refCanvas.width, refCanvas.height);

  // Count mismatched pixels with 10% per-pixel tolerance
  const threshold = 0.1;
  let mismatched = 0;
  const total = refData.data.length / 4;
  // Full pixelmatch impl is ~100 lines — include inline or use bundled copy
  return {
    total,
    mismatched,
    similarity: ((total - mismatched) / total * 100).toFixed(1) + '%'
  };
}, referenceImageDataUrl);
```

## Quadrant Analysis

Divide the viewport into four quadrants and report which has the most pixel difference:

| Quadrant | Covers | Common issues |
|----------|--------|---------------|
| Top-left | Nav logo, hamburger | Logo size, menu alignment |
| Top-right | Nav CTA, search | Button styling, spacing |
| Center-top | Hero headline, CTA button | Font weight, button shadow |
| Center/bottom | Features, footer | Card layout, color drift |

Report: `Similarity: 94.2% | Diff concentrated: top-center (hero CTA button)`

## Thresholds

| Score | Status | Action |
|-------|--------|--------|
| ≥ 90% | ✅ Pass | Deliver |
| 80–89% | ⚠️ Warn | Fix top diff quadrant, re-check |
| < 80% | ❌ Fail | Continue fix loop, max 5 iterations |

## 4-Breakpoint Test Matrix

| Breakpoint | Width | Height | Key checks |
|------------|-------|--------|------------|
| Mobile S   | 375px | 812px  | Hamburger menu, single-col, tap targets ≥44px |
| Tablet     | 768px | 1024px | 2-col layouts, hybrid nav |
| Laptop     | 1024px| 768px  | Full nav, 3-col grids |
| Desktop    | 1440px| 900px  | Full wide layout, centered container |

Horizontal scroll = critical bug. Check: `body.scrollWidth > window.innerWidth`.
