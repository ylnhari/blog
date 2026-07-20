# Blog Standards & Agent Guide

This repository is the canonical source for Hari's blog posts.  
Any AI agent (Claude, OpenClaw, DeepSeek, or any other) can create, edit, and publish posts by following this document exactly.

---

## Quick Start (for agents)

1. Create folder `posts/YYYY-MM-DD-slug/`
2. Copy `templates/post.html` → `posts/YYYY-MM-DD-slug/index.html`, fill placeholders
3. Copy `templates/meta.json` → `posts/YYYY-MM-DD-slug/meta.json`, fill all fields
4. Prepend entry to `posts/index.json` (newest first)
5. Commit all three files to `main` in one commit
6. Wait ~90 seconds for GitHub Pages to deploy
7. Import into Medium: paste `https://ylnhari.github.io/blog/posts/YYYY-MM-DD-slug/` at `https://medium.com/p/import`
8. After publishing, update `meta.json` → set `status: "published"` and `medium_url`

---

## Folder Structure

```
blog/
├── STANDARDS.md                        ← this file (do not modify)
├── index.html                          ← blog homepage (auto-generated from posts/index.json)
├── assets/
│   └── style.css                       ← shared stylesheet (do not modify per-post)
├── templates/
│   ├── post.html                       ← copy for every new post
│   └── meta.json                       ← copy for every new post
└── posts/
    ├── index.json                      ← master registry (update for every post)
    └── YYYY-MM-DD-slug/
        ├── index.html                  ← post HTML content
        └── meta.json                   ← post metadata
```

---

## Naming Convention

| Item | Format | Example |
|------|--------|---------|
| Folder | `posts/YYYY-MM-DD-slug/` | `posts/2026-06-22-ai-assisted-blogging/` |
| Date | ISO 8601 (`YYYY-MM-DD`) | `2026-06-22` |
| Slug | lowercase, hyphens only, no special chars, max 60 chars | `ai-assisted-blogging` |
| HTML file | always `index.html` | fixed — never vary |
| Meta file | always `meta.json` | fixed — never vary |

---

## meta.json Schema

```json
{
  "title": "Human-readable post title",
  "date": "YYYY-MM-DD",
  "author": "ylnhari",
  "description": "1–2 sentence summary for SEO and blog index card. Max 200 chars.",
  "tags": ["tag1", "tag2"],
  "status": "draft",
  "medium_url": null,
  "cover_image": "https://images.unsplash.com/photo-XXXXXXX?w=1200&q=80"
}
```

Field rules:
- `status`: must be `"draft"` or `"published"` — no other values
- `medium_url`: `null` until published; then the full `https://medium.com/...` URL
- `cover_image`: must be an absolute HTTPS URL; cannot be a relative path
- `tags`: 2–5 tags, lowercase preferred

---

## posts/index.json Schema

Maintain as a JSON array, newest post first:

```json
[
  {
    "slug": "2026-06-22-ai-assisted-blogging",
    "title": "AI-Assisted Blogging: A Technical Deep Dive",
    "date": "2026-06-22",
    "description": "How to automate blog creation with AI agents and GitHub Pages.",
    "tags": ["AI", "automation", "blogging"],
    "cover_image": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1200&q=80",
    "status": "published",
    "medium_url": null
  }
]
```

When adding a new post, prepend its entry. Do not re-sort existing entries.

---

## HTML Post Structure

Every `index.html` MUST follow this exact outer structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="author" content="ylnhari">
  <meta name="description" content="POST_DESCRIPTION">
  <meta property="og:title" content="POST_TITLE">
  <meta property="og:description" content="POST_DESCRIPTION">
  <meta property="og:image" content="COVER_IMAGE_URL">
  <title>POST_TITLE</title>
  <link rel="stylesheet" href="../../assets/style.css">
</head>
<body>
<article>

<h1>POST_TITLE</h1>
<p class="byline">By ylnhari · POST_DATE · POST_TAGS</p>

<!-- === POST CONTENT STARTS HERE === -->



<!-- === POST CONTENT ENDS HERE === -->

<hr>
<p class="footer-note"><em>Published via automated pipeline · <a href="https://ylnhari.github.io/blog">ylnhari.github.io/blog</a></em></p>

</article>
</body>
</html>
```

Placeholders to replace:
- `POST_TITLE` — exact title string, no HTML entities needed for basic ASCII
- `POST_DESCRIPTION` — same as `meta.json` description field
- `POST_DATE` — human-readable date, e.g. `June 22, 2026`
- `POST_TAGS` — comma-separated, e.g. `AI, automation`
- `COVER_IMAGE_URL` — same as `meta.json` cover_image field

---

## Supported HTML Elements

| Tag | Medium mapping | Usage |
|-----|---------------|-------|
| `<h1>` | Title | Once only, at the top |
| `<h2>` | Section heading | Major sections |
| `<h3>` | Sub-heading | Sub-sections, use sparingly |
| `<p>` | Paragraph | All body text |
| `<strong>` | **Bold** | Key terms, emphasis |
| `<em>` | *Italic* | Titles, foreign words, soft emphasis |
| `<a href="...">` | Hyperlink | Must be absolute URLs |
| `<img src="..." alt="...">` | Image | Must be absolute HTTPS URL |
| `<blockquote>` | Pull quote | Quotes, important callouts |
| `<pre><code>` | Code block | Multi-line code |
| `<code>` | Inline code | Short code references in text |
| `<ul><li>` | Bullet list | Unordered list |
| `<ol><li>` | Numbered list | Ordered list |
| `<hr>` | Separator (· · ·) | Section dividers, use max 2 per post |

---

## NEVER Use (breaks Medium import or causes save errors)

- `<script>` or any JavaScript
- `<style>` tags or `style="..."` inline attributes
- `<iframe>` (stripped by Medium)
- `<table>`, `<tr>`, `<td>` (Medium has no table support)
- `<video>`, `<audio>` (not supported)
- `<div>`, `<span>` with styling
- H4, H5, H6 (Medium only supports H1–H3)
- Relative image URLs (Medium's importer cannot resolve them)
- Self-referencing anchor links (`<a href="#section">`)

---

## Images

Must be absolute HTTPS URLs. Recommended free sources:

```html
<!-- Unsplash (free, high quality) -->
<img src="https://images.unsplash.com/photo-{PHOTO_ID}?w=1200&q=80" alt="Description">

<!-- Wikimedia Commons -->
<img src="https://upload.wikimedia.org/wikipedia/commons/path/to/file.jpg" alt="Description">

<!-- Your own assets in this repo (raw GitHub URL) -->
<img src="https://raw.githubusercontent.com/ylnhari/blog/main/posts/{SLUG}/images/filename.png" alt="Description">
```

To store images in the repo: place them in `posts/YYYY-MM-DD-slug/images/`.

---

## Writing Craft (the house style — distilled from the shipped posts)

### Length is set by the topic, never by a target
There is no house word count, no "keep it tight" default, and no upper bound.
**The right length is whatever the subject and the reader's need require** — a
narrow correction may be 400 words; a comparison that has to carry benchmarks,
pricing and a decision framework may be 2,500. Say everything the topic needs
said, in the way that expresses it best, and stop there.

- Never cut substance to hit a size. If material earns its place, it stays.
- Never pad to reach a size either — length is an outcome, not a goal.
- If Hari specifies a length or scope for a given post, that instruction wins.
- **Sources, caveats, and methodology notes do not count toward length** and must
  never be trimmed, dropped or "compressed" to make a post feel shorter. They are
  supplementary apparatus, not body copy. Judge the post's length by its argument.

### Structure
- **Analytical/comparison posts open insight-first**: state the counter-intuitive
  conclusion (or what's wrong with the conventional take) in the first two
  paragraphs, then spend the body proving it. **Tutorial posts** may instead
  build up step-by-step (numbered "Step 1…N") after a short personal cold-open.
- **1–3 `<blockquote>` pull-quotes** per post: one aphoristic sentence that
  compresses the thesis, used as mid-article punctuation — never decoration.
- **Comparison posts end with a numbered decision framework** ("So which one?
  Three cases: …") — a closing that tells the reader what to DO, not a summary.
- **Series posts cross-link each other** in the body ("companion to …") — every
  post on adjacent ground published within a week links its siblings.

### Data & charts — ONE convention
- Charts are **pre-rendered PNGs** in `posts/{SLUG}/images/`, referenced by
  absolute raw.githubusercontent URL, with a **descriptive `alt` that states the
  chart's takeaway** (it doubles as the caption Medium keeps).
- **Commit the generator with the chart**: the script + data that produced each
  PNG live in `posts/{SLUG}/charts/` (any tooling; matplotlib fine). A chart
  whose numbers can't be regenerated is a claim that can't be checked.
- Small numeric walkthroughs (a memory budget, a cost breakdown) may be an
  indented list instead of a chart — show the arithmetic line by line.
- **Interactive visualizations are standalone pages, never embedded**: build
  `posts/{SLUG}/interactive.html` (self-contained Canvas/SVG+JS, its own
  `<style>`) and LINK to it from the post body. Medium strips `<script>`,
  `<style>`, and `<canvas>` — an embedded interactive collapses to nothing.
  The post body must still carry a static PNG of the same view, so Medium
  readers lose interactivity, not information.

### Model comparisons — link the standing bench page, never re-argue it
There is ONE canonical, first-hand model comparison:
**https://ylnhari.github.io/ai-signal/bench.html**. It carries the full results
table (coding / long-document reading / drawing), the exact prompts, every
model's raw output, the scoring method, and each model's drawings — all measured
first-hand, and it grows as new models are tested.

- Any post that compares models, or leans on a claim about one model being
  better/worse at coding, reading, or instruction-following, **links to it**
  instead of restating the numbers. One link, in the sentence making the claim.
- **Never re-derive or re-argue model differences per post**, and never paste the
  results table into a post — it goes stale the moment a new model is added,
  and two copies of the numbers will drift apart.
- Post-specific measurements are still welcome — but if the claim is "model X
  handles Y better than model Z", that belongs on the bench page first, then the
  post links it.
- When a new model is tested, the bench page and the interactive chart at
  `posts/2026-07-13-open-source-vs-paid-frontier-llms/interactive.html` are both
  updated; past posts are not retro-edited.

### Code blocks — label the purpose
Every `<pre><code>` block gets a one-line bold lead-in immediately above it,
one of: **Run this:** (commands the reader executes) · **Output:** (verified
program output, pasted not paraphrased) · **Example (illustrative):** (API
usage/sketch, not guaranteed runnable). Never make the reader infer which.

### Fact discipline (the gate a draft must pass before Hari sees it)
- **Every third-party number, date, price, or benchmark score carries an
  inline link to its source, fetched during the writing session.** No source
  found ⇒ the claim is cut or explicitly marked as estimate. Never write
  "every number is sourced" as prose — make each number BE sourced.
- **Prefer sourcing inline.** A hyperlink on the number itself, in the sentence
  that uses it, is the default — it reads better and keeps the claim next to its
  evidence. A closing **"Sources & caveats"** section is *optional*: add one when
  there is genuine methodology to disclose (which aggregator, snapshot date, where
  vendors disagree, what's vendor-only or unverified, sample size), and skip it
  when inline links already carry everything. Include sources whenever relevant —
  just never let their presence or absence drive the post's length.
- **A vendor's own facts come from the vendor.** Pricing, release dates, context
  windows and model specs cite the vendor's page (Anthropic / platform.claude.com,
  x.ai, OpenAI, Moonshot…), never a blogger, newsletter or aggregator who reported
  them. Secondary sources are for analysis and independent measurement only.
  Vendor pages carry qualifiers summaries drop — introductory pricing windows,
  effective dates, tokenizer changes — and those often change the conclusion.
- Where a claim comes from something WE built or ran, anchor it to the
  reproducible artifact instead: the repo, the tool, or a pasted **Output:**
  block (measured beats cited).
- Numbers that are estimates get a confidence marker (°, †, ‡ with a one-line
  glossary) — the vllm-model-chooser pattern.

---

## YouTube / Video Embeds

Medium doesn't support `<video>` or `<iframe>`. Workaround for YouTube:

```html
<!-- Put the YouTube URL as plain text in a paragraph -->
<p>https://www.youtube.com/watch?v=VIDEO_ID</p>
```

After importing to Medium, click the URL in the editor → Medium auto-converts it to a video embed.

---

## GitHub Pages URL Pattern

```
https://ylnhari.github.io/blog/posts/{YYYY-MM-DD-slug}/
```

This is the URL to paste into `https://medium.com/p/import`.

Build time after a commit: typically 60–120 seconds. Check build status at:
`https://github.com/ylnhari/blog/actions`

---

## Agent Checklist (copy this when creating a post)

```
[ ] Folder created:       posts/YYYY-MM-DD-slug/
[ ] index.html created:   copied from templates/post.html, all placeholders replaced
[ ] meta.json created:    all fields filled, cover_image is absolute HTTPS URL
[ ] posts/index.json:     new entry prepended (newest first)
[ ] No JavaScript in HTML
[ ] No inline CSS in HTML
[ ] No relative image URLs
[ ] All <img src="..."> use absolute HTTPS URLs
[ ] Every third-party number has an inline source link (fetched this session)
[ ] "Sources & caveats" section present if the post carries third-party data
[ ] Any model-vs-model claim links bench.html (see "Model comparisons") —
    numbers NOT restated in the post
[ ] Charts: PNGs in images/ + generator committed in charts/
[ ] Interactive (if any): standalone interactive.html, linked not embedded,
    static PNG fallback in body
[ ] Code blocks labeled (Run this: / Output: / Example:)
[ ] Committed to main branch
[ ] GitHub Actions build passed (check /actions)
[ ] Medium import tested at medium.com/p/import
[ ] (After publish) meta.json status → "published", medium_url filled
```

---

## Error Recovery

If Medium shows "not saved properly" during browser automation:
1. Refresh the page — Medium auto-restores the last saved state
2. Resume from the last successfully saved element
3. Do NOT use: `execCommand('insertParagraph')`, `innerHTML =`, `execCommand('selectAll')`
4. DO use: `document.execCommand('insertText', false, text)` for typing; CDP `Input.dispatchKeyEvent` for Enter key

---

## Commit Message Convention

```
feat(posts): add "POST_TITLE" [YYYY-MM-DD]
fix(posts): update "POST_TITLE" meta/content
chore: update posts/index.json
```
