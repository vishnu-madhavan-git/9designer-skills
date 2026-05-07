# 9Designer Skills

9Designer is an image-to-working-website skill pipeline for Codex.

## Skills

Required modular pipeline:

```text
$9image-design
image -> design

$9design-assets
design -> assets

$9assets-website
assets -> website
```

Optional expanded kit:

```text
$9design-kit
design -> expanded brand/UI kit
```

All-in-one:

```text
$9designer
image -> design -> assets -> website
```

## Folder Layout

```text
skills/
  9designer/
  9image-design/
  9design-assets/
  9design-kit/
  9assets-website/
```

## Install

Copy the folders under `skills/` into your Codex skills folder.

Typical user skills folder:

```text
~/.codex/skills/
```

For a project-local skill folder, copy them into:

```text
<project>/.agents/skills/
```

## Recommended Use

For the full pipeline from one image:

```text
Use $9designer with this reference image.
```

For modular control:

```text
Use $9image-design with this reference image.
Use $9design-assets with this approved design.
Use $9assets-website with this asset export folder.
```

## Notes

- `$9image-design` waits for approval after the first landing page unless explicitly overridden.
- `$9image-design` now uses a frontend design bar: visual thesis, content plan, interaction thesis, image-led composition, no generic card grids, and section/detail concepts when the full-page design is too compressed to implement.
- `$9design-assets` generates clean separate image assets, runs background cleanup for reusable non-background assets, and avoids baked-in screenshot/checkerboard backgrounds for logos, icons, and UI elements.
- `$9assets-website` builds the working responsive website from the exported assets, then uses implementation inventories, responsive checks, and screenshot comparison against the approved template to tighten the visual clone.

## Background Cleanup

`$9design-assets` includes:

```text
skills/9design-assets/scripts/remove_background.py
```

Use it after image generation for logos, icons, overlays, dividers, and reusable UI assets:

```text
python skills/9design-assets/scripts/remove_background.py --input generated.png --output cleaned.png --mode auto
```

The exporter manifest tracks:

```text
background_cleanup_required
background_cleaned
alpha_verified
background_removal_needed
```

Do not pass checkerboard-backed or screenshot-backed reusable assets into `$9assets-website`.
