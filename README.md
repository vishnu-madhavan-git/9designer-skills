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
- `$9design-assets` generates clean separate image assets and avoids baked-in screenshot backgrounds for logos, icons, and UI elements.
- `$9assets-website` builds the working responsive website from the exported assets.
