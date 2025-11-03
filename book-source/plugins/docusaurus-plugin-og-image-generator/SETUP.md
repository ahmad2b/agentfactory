# Docusaurus OG Image Generator Plugin - Setup Guide

## Problem

Your OG images are being generated but not showing in production because Docusaurus doesn't automatically use them.

## Solution

Follow these steps to enable page-specific OG images:

### Step 1: Generate OG Images

Build your site to generate the images:

```bash
npm run build
```

This creates images in `static/img/og/` like:

- `preface-agent-native.png`
- `01-Introducing-AI-Driven-Development-README.png`
- etc.

### Step 2: Add Image Paths to Frontmatter

Run the helper script to add `image` fields to your markdown files:

```bash
node scripts/add-og-images-to-frontmatter.js
```

This updates each file's frontmatter from:

```yaml
---
title: "Preface: Welcome to the AI-Native Era"
description: "Introduction to AI-native software development"
---
```

To:

```yaml
---
title: "Preface: Welcome to the AI-Native Era"
description: "Introduction to AI-native software development"
image: "/img/og/preface-agent-native.png"
---
```

### Step 3: Rebuild

Build again to apply the changes:

```bash
npm run build
```

### Step 4: Deploy

Deploy your updated build directory to production.

## Verification

Test OG images using:

- [Open Graph Debugger](https://www.opengraph.xyz/)
- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
- [Twitter Card Validator](https://cards-dev.twitter.com/validator)

## Manual Alternative

You can also manually add the `image` field to any markdown file's frontmatter:

```yaml
---
title: "My Page"
image: "/img/og/[slug].png"
---
```

Where `[slug]` is the file path with `/` replaced by `-` and without the `.md` extension.

Example:

- File: `docs/01-Introduction/README.md`
- Slug: `01-Introduction-README`
- Image: `/img/og/01-Introduction-README.png`
