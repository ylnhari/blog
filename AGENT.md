# Agent Instructions — End-to-End Blog Post Workflow

This file tells any AI agent (Claude, OpenClaw, DeepSeek, etc.) exactly how to take a topic and produce a Medium draft ready for Hari to review and publish.

**Read [`STANDARDS.md`](./STANDARDS.md) for the full HTML spec before writing any post.**

---

## What You Are Doing

Given a topic or title from Hari, you will:
1. Generate a complete blog post as a static HTML file
2. Create the required metadata files
3. Commit everything to this GitHub repo
4. Wait for GitHub Pages to deploy (~90 seconds)
5. Import the post into Medium using the import URL
6. Confirm the Medium draft is ready for Hari to review and publish

You do NOT publish to Medium yourself. Leave it as a draft.

---

## Step-by-Step Workflow

### Step 1 — Gather requirements

Before writing, confirm:
- **Topic / Title**: What is the post about? (required)
- **Audience**: Technical? General? Beginner?
- **Tone**: Casual? Formal? Tutorial-style?
- **Length**: do NOT ask for or assume a word count. Length is set by the topic —
  write what the subject needs and stop (STANDARDS.md § "Length is set by the
  topic, never by a target"). Only honour a length if Hari volunteers one.
- **Key points to cover**: Anything Hari specifically wants included?

If Hari gave a brief prompt (e.g. "write about vLLM quantization"), proceed with sensible defaults and note your assumptions.

---

### Step 2 — Generate the post content

Write the full blog post per **STANDARDS.md § Writing Craft** (house style —
read it first). Quality baseline:
- Analytical post ⇒ insight-first opening; tutorial ⇒ numbered steps
- 1–3 blockquote pull-quotes compressing the thesis
- Charts as pre-rendered PNGs in `posts/{SLUG}/images/` with the generator
  script + data committed in `posts/{SLUG}/charts/`; interactive versions are
  a standalone `interactive.html` LINKED (never embedded) with a static PNG
  in the body
- Every `<pre><code>` block labeled: **Run this:** / **Output:** / **Example
  (illustrative):**
- 3–6 sections with H2 headings; comparison posts end with a numbered
  decision framework; series posts cross-link siblings

### Step 2b — Fact-check pass (MANDATORY before Step 3)

Go through the draft claim by claim:
1. Every third-party number/date/price/benchmark has an inline source link
   you fetched THIS session. Unfetchable ⇒ cut the claim or mark it as an
   estimate with a confidence marker.
2. Third-party data ⇒ closing **"Sources & caveats"** section (source list +
   methodology notes: snapshot date, which aggregator, vendor-only figures).
3. Claims about things WE built/ran ⇒ anchored to the repo/tool or a pasted
   **Output:** block instead of a link.
4. Self-audit: scan the draft for every numeral; each one must be traceable
   via rules 1–3. A draft that fails this pass does not reach Hari.

---

### Step 3 — Prepare files

**Slug**: Create from the title — lowercase, hyphens only, max 60 chars.
Example: "AI-Assisted Blogging in 2026" → `ai-assisted-blogging-2026`

**Date**: Today's date in `YYYY-MM-DD` format.

**Folder**: `posts/YYYY-MM-DD-slug/`

#### File 1: `posts/YYYY-MM-DD-slug/index.html`

Copy the structure from `templates/post.html`. Replace ALL placeholders:

| Placeholder | Replace with |
|-------------|-------------|
| `POST_TITLE` | Full post title |
| `POST_DESCRIPTION` | 1–2 sentence summary (max 200 chars) |
| `POST_DATE` | Human-readable date (e.g. "June 22, 2026") |
| `POST_TAGS` | Comma-separated tags (2–5) |
| `COVER_IMAGE_URL` | Absolute HTTPS image URL (Unsplash preferred) |

Content rules (from STANDARDS.md):
- Only use: h1, h2, h3, p, strong, em, a, img, blockquote, pre/code, ul/ol/li, hr
- NEVER use: script, style, iframe, table, div, span, h4-h6, relative image URLs
- All `<img src>` must be absolute HTTPS URLs
- One `<h1>` only, at the top

#### File 2: `posts/YYYY-MM-DD-slug/meta.json`

```json
{
  "title": "FULL TITLE",
  "date": "YYYY-MM-DD",
  "author": "ylnhari",
  "description": "DESCRIPTION (max 200 chars)",
  "tags": ["tag1", "tag2"],
  "status": "draft",
  "medium_url": null,
  "cover_image": "https://images.unsplash.com/..."
}
```

#### File 3: Update `posts/index.json`

Prepend the new entry at the top of the array (newest first):

```json
{
  "slug": "YYYY-MM-DD-slug",
  "title": "FULL TITLE",
  "date": "YYYY-MM-DD",
  "description": "DESCRIPTION",
  "tags": ["tag1", "tag2"],
  "cover_image": "https://...",
  "status": "draft",
  "medium_url": null
}
```

---

### Step 4 — Commit to GitHub

Use `gh` CLI (preferred) or `git`:

```bash
cd C:\Users\ylnha\projects\blog

git add posts/YYYY-MM-DD-slug/
git add posts/index.json
git commit -m "feat(posts): add \"POST TITLE\" [YYYY-MM-DD]"
git push origin main
```

Verify push succeeded before continuing.

---

### Step 5 — Wait for GitHub Pages

After pushing, wait **90 seconds** for the build to complete.

To verify the page is live, check:
```
https://ylnhari.github.io/blog/posts/YYYY-MM-DD-slug/
```

If it returns 404, check the Actions tab:
```
https://github.com/ylnhari/blog/actions
```

Wait for the "pages build and deployment" workflow to show a green checkmark, then verify the URL again.

Do not proceed to Step 6 until the URL is live.

---

### Step 6 — Import to Medium

Navigate to: `https://medium.com/p/import`

In the input field, paste:
```
https://ylnhari.github.io/blog/posts/YYYY-MM-DD-slug/
```

Click the **Import** button.

Medium will show a confirmation screen: "Imported the story — TITLE from https://ylnhari.github.io"

Click **"See your story"** to open the draft editor.

Do NOT click Publish. Leave it as a draft.

---

### Step 7 — Confirm and report to Hari

Report back with:
- ✅ Post title and slug
- ✅ GitHub Pages URL: `https://ylnhari.github.io/blog/posts/YYYY-MM-DD-slug/`
- ✅ Medium draft URL: `https://medium.com/p/{draft-id}/edit`
- Any notes on content decisions or assumptions made
- Prompt Hari: "The draft is ready for your review. Open the Medium draft, make any edits, then click Publish when ready."

---

## Error Handling

| Error | Action |
|-------|--------|
| `git push` fails (auth) | Run `gh auth login` first |
| GitHub Pages still 404 after 3 min | Check `github.com/ylnhari/blog/actions` for build errors |
| Medium import fails ("could not import") | Verify the GitHub Pages URL loads correctly in a browser first |
| Medium "not saved properly" error during editor automation | Refresh the page — Medium restores last saved state. Do NOT manipulate innerHTML or use execCommand('insertParagraph'). Use the import method instead of editor automation. |
| Commit has nothing to add | Check files were created in correct paths |

---

## Tools Required

| Task | Tool |
|------|------|
| Clone / push repo | `gh` CLI or `git` |
| Check GitHub Pages build | Browser or `curl` |
| Import to Medium | Browser (navigate to medium.com/p/import) |
| Wait for deploy | `sleep 90` or manual wait |

---

## Quick Command Reference

```bash
# Check gh auth
gh auth status

# Clone repo (first time)
gh repo clone ylnhari/blog C:\Users\ylnha\projects\blog

# Push a new post
cd C:\Users\ylnha\projects\blog
git add posts/YYYY-MM-DD-slug/ posts/index.json
git commit -m "feat(posts): add \"TITLE\""
git push origin main

# Verify Pages is live
curl -I https://ylnhari.github.io/blog/posts/YYYY-MM-DD-slug/
# Should return HTTP 200
```

---

## One-Line Summary

> Read STANDARDS.md → write HTML post → create meta.json → update posts/index.json → git push → wait 90s → medium.com/p/import → leave as draft → report back.
