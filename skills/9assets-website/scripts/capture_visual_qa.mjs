#!/usr/bin/env node
/**
 * Capture stable desktop/tablet/mobile screenshots for 9Designer website QA.
 *
 * Playwright is optional. This script only requires it when actual capture runs.
 */

import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";

const DEFAULT_VIEWPORTS = [
  { name: "desktop", width: 1440, height: 1100 },
  { name: "tablet", width: 768, height: 1024 },
  { name: "mobile", width: 390, height: 844 },
];

function usage() {
  console.log(`Usage:
  node capture_visual_qa.mjs --url <local-url> [options]

Options:
  --url <url>                Website URL to capture. Required.
  --out <dir>                Output directory. Default: visual-qa/screenshots
  --viewport <n:wxh>         Add/replace a viewport, e.g. desktop:1440x1100
  --wait <ms>                Extra wait after fonts/images settle. Default: 600
  --viewport-only            Capture only the visible viewport instead of full page
  --keep-animations          Do not inject reduced-motion CSS
  --help                     Show this help

Optional dependency:
  npm i -D playwright
  npx playwright install chromium`);
}

function parseArgs(argv) {
  const args = {
    url: "",
    out: "visual-qa/screenshots",
    viewports: [],
    wait: 600,
    fullPage: true,
    reduceMotion: true,
    help: false,
  };

  for (let index = 2; index < argv.length; index += 1) {
    const value = argv[index];
    if (value === "--help" || value === "-h") {
      args.help = true;
    } else if (value === "--url") {
      args.url = argv[++index] || "";
    } else if (value === "--out") {
      args.out = argv[++index] || args.out;
    } else if (value === "--viewport") {
      args.viewports.push(argv[++index] || "");
    } else if (value === "--wait") {
      args.wait = Number(argv[++index] || args.wait);
    } else if (value === "--viewport-only") {
      args.fullPage = false;
    } else if (value === "--keep-animations") {
      args.reduceMotion = false;
    } else {
      throw new Error(`Unknown argument: ${value}`);
    }
  }

  return args;
}

function parseViewport(value) {
  const match = /^([a-z0-9_-]+):(\d+)x(\d+)$/i.exec(value);
  if (!match) {
    throw new Error(`Invalid viewport "${value}". Use name:widthxheight.`);
  }
  return {
    name: match[1].toLowerCase(),
    width: Number(match[2]),
    height: Number(match[3]),
  };
}

function mergeViewports(values) {
  if (!values.length) {
    return DEFAULT_VIEWPORTS;
  }

  const byName = new Map(DEFAULT_VIEWPORTS.map((viewport) => [viewport.name, viewport]));
  for (const value of values) {
    const viewport = parseViewport(value);
    byName.set(viewport.name, viewport);
  }
  return Array.from(byName.values());
}

async function loadPlaywright() {
  try {
    return await import("playwright");
  } catch (error) {
    const result = {
      valid: false,
      optional_dependency_missing: "playwright",
      message: "Playwright is optional and is not installed in this project.",
      install: ["npm i -D playwright", "npx playwright install chromium"],
      error: error?.message || String(error),
    };
    console.error(JSON.stringify(result, null, 2));
    process.exit(2);
  }
}

async function waitForStablePage(page, waitMs) {
  await page.waitForLoadState("domcontentloaded");
  await page.waitForLoadState("networkidle").catch(() => {});
  await page.evaluate(async () => {
    if (document.fonts?.ready) {
      await document.fonts.ready;
    }
    await Promise.all(
      Array.from(document.images)
        .filter((image) => !image.complete)
        .map(
          (image) =>
            new Promise((resolve) => {
              image.addEventListener("load", resolve, { once: true });
              image.addEventListener("error", resolve, { once: true });
            }),
        ),
    );
  });
  if (waitMs > 0) {
    await page.waitForTimeout(waitMs);
  }
}

async function main() {
  const args = parseArgs(process.argv);
  if (args.help) {
    usage();
    return;
  }
  if (!args.url) {
    usage();
    process.exit(1);
  }

  const { chromium } = await loadPlaywright();
  const outDir = path.resolve(args.out);
  await mkdir(outDir, { recursive: true });

  const browser = await chromium.launch({ headless: true });
  const screenshots = [];
  const consoleMessages = [];

  try {
    const viewports = mergeViewports(args.viewports);
    const results = await Promise.all(
      viewports.map(async (viewport) => {
        const page = await browser.newPage({
          viewport: { width: viewport.width, height: viewport.height },
          deviceScaleFactor: 1,
        });
        const messages = [];
        page.on("console", (message) => {
          if (["error", "warning"].includes(message.type())) {
            messages.push({
              viewport: viewport.name,
              type: message.type(),
              text: message.text(),
            });
          }
        });

        await page.goto(args.url, { waitUntil: "domcontentloaded" });
        if (args.reduceMotion) {
          await page.addStyleTag({
            content: `
              *, *::before, *::after {
                animation-delay: 0s !important;
                animation-duration: 0.001s !important;
                animation-iteration-count: 1 !important;
                scroll-behavior: auto !important;
                transition-delay: 0s !important;
                transition-duration: 0s !important;
              }
            `,
          });
        }
        await waitForStablePage(page, args.wait);

        const file = path.join(outDir, `${viewport.name}.png`);
        await page.screenshot({ path: file, fullPage: args.fullPage });
        await page.close();

        return {
          screenshot: { ...viewport, file },
          messages,
        };
      })
    );

    for (const result of results) {
      screenshots.push(result.screenshot);
      consoleMessages.push(...result.messages);
    }
  } finally {
    await browser.close();
  }

  const summary = {
    valid: true,
    tool: "capture_visual_qa",
    url: args.url,
    output_dir: outDir,
    full_page: args.fullPage,
    reduce_motion: args.reduceMotion,
    screenshots,
    console_messages: consoleMessages,
  };
  await writeFile(path.join(outDir, "visual-qa-capture-summary.json"), JSON.stringify(summary, null, 2));
  console.log(JSON.stringify(summary, null, 2));
}

main().catch((error) => {
  console.error(JSON.stringify({ valid: false, error: error?.message || String(error) }, null, 2));
  process.exit(1);
});
