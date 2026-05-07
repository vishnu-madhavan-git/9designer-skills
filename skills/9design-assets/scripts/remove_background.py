#!/usr/bin/env python3
"""Remove generated asset backgrounds and verify alpha transparency.

This utility is intended for imagegen outputs used as implementation assets.
It prefers existing transparency, optionally uses rembg when installed, and
falls back to edge-connected flat/checkerboard cleanup for common generated
PNG artifacts.
"""

from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path


def load_pillow():
    try:
        from PIL import Image
    except ImportError as exc:
        raise SystemExit(
            "Pillow is required for background cleanup. Install with: pip install pillow"
        ) from exc
    return Image


def color_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def top_border_colors(pixels, width: int, height: int, quant: int = 16) -> list[tuple[int, int, int]]:
    counts: dict[tuple[int, int, int], int] = {}
    coords = []
    for x in range(width):
        coords.append((x, 0))
        coords.append((x, height - 1))
    for y in range(height):
        coords.append((0, y))
        coords.append((width - 1, y))

    for x, y in coords:
        r, g, b, _ = pixels[x, y]
        key = (
            min(255, round(r / quant) * quant),
            min(255, round(g / quant) * quant),
            min(255, round(b / quant) * quant),
        )
        counts[key] = counts.get(key, 0) + 1

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [color for color, _ in ranked[:4]]


def has_meaningful_alpha(image) -> bool:
    if image.mode != "RGBA":
        return False
    alpha = image.getchannel("A")
    extrema = alpha.getextrema()
    return bool(extrema and extrema[0] < 250)


def try_rembg(input_path: Path, output_path: Path) -> bool:
    try:
        from rembg import remove
    except ImportError:
        return False

    data = input_path.read_bytes()
    output_path.write_bytes(remove(data))
    return True


def edge_connected_cleanup(image, tolerance: int):
    image = image.convert("RGBA")
    pixels = image.load()
    width, height = image.size
    bg_colors = top_border_colors(pixels, width, height)

    visited = set()
    queue: deque[tuple[int, int]] = deque()

    for x in range(width):
        queue.append((x, 0))
        queue.append((x, height - 1))
    for y in range(height):
        queue.append((0, y))
        queue.append((width - 1, y))

    removed = 0

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited or x < 0 or y < 0 or x >= width or y >= height:
            continue
        visited.add((x, y))

        r, g, b, a = pixels[x, y]
        if a == 0:
            should_remove = True
        else:
            should_remove = any(color_distance((r, g, b), bg) <= tolerance for bg in bg_colors)

        if not should_remove:
            continue

        if a != 0:
            pixels[x, y] = (r, g, b, 0)
            removed += 1

        queue.append((x + 1, y))
        queue.append((x - 1, y))
        queue.append((x, y + 1))
        queue.append((x, y - 1))

    return image, removed, bg_colors


def alpha_stats(image) -> dict:
    image = image.convert("RGBA")
    alpha = image.getchannel("A")
    extrema = alpha.getextrema()
    transparent = 0
    opaque = 0
    for value in alpha.tobytes():
        if value == 0:
            transparent += 1
        if value == 255:
            opaque += 1
    total = image.size[0] * image.size[1]
    return {
        "alpha_min": extrema[0],
        "alpha_max": extrema[1],
        "transparent_pixels": transparent,
        "opaque_pixels": opaque,
        "transparent_ratio": round(transparent / total, 4) if total else 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Remove an asset background and save RGBA PNG.")
    parser.add_argument("--input", required=True, help="Input image path.")
    parser.add_argument("--output", required=True, help="Output PNG path.")
    parser.add_argument(
        "--mode",
        default="auto",
        choices=["auto", "edge", "rembg"],
        help="Cleanup mode. auto tries existing alpha, rembg if available, then edge cleanup.",
    )
    parser.add_argument("--tolerance", type=int, default=54, help="RGB edge cleanup tolerance.")
    args = parser.parse_args()

    Image = load_pillow()
    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    image = Image.open(input_path).convert("RGBA")
    method = "existing-alpha"
    removed = 0
    bg_colors: list[tuple[int, int, int]] = []

    if has_meaningful_alpha(image):
        image.save(output_path)
    elif args.mode in {"auto", "rembg"} and try_rembg(input_path, output_path):
        method = "rembg"
        image = Image.open(output_path).convert("RGBA")
    else:
        method = "edge-connected"
        image, removed, bg_colors = edge_connected_cleanup(image, args.tolerance)
        image.save(output_path)

    stats = alpha_stats(image)
    result = {
        "input": str(input_path),
        "output": str(output_path),
        "method": method,
        "removed_pixels": removed,
        "background_colors": bg_colors,
        "alpha_verified": stats["alpha_min"] == 0 and stats["transparent_pixels"] > 0,
        **stats,
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
