# ylnhari's Blog

> AI-assisted technical blog — posts are written by AI agents and published to Medium via GitHub Pages.

**Live blog:** https://ylnhari.github.io/blog  
**Medium profile:** https://medium.com/@ylnhari  
**GitHub:** https://github.com/ylnhari/blog

---

## How This Works

```
AI Agent (Claude / OpenClaw / DeepSeek)
    ↓  generates post as static HTML
GitHub repo  (this repo)
    ↓  GitHub Pages auto-deploys in ~90 seconds
https://ylnhari.github.io/blog/posts/{slug}/
    ↓  paste URL into medium.com/p/import
Medium draft  →  review  →  publish
```

No paid APIs. No Medium API token. Just static HTML + GitHub Pages + Medium's import feature.

---

## For AI Agents — Read This First

**Full rules and standards are in [`STANDARDS.md`](./STANDARDS.md). Read it before creating any post.**

Quick checklist to add a post:

1. Create folder `posts/YYYY-MM-DD-your-slug/`
2. Copy `templates/post.html` → `posts/YYYY-MM-DD-your-slug/index.html` — fill all `POST_*` placeholders
3. Copy `templates/meta.json` → `posts/YYYY-MM-DD-your-slug/meta.json` — fill all fields
4. Prepend entry to `posts/index.json` (newest first)
5. Commit all 3 files to `main`
6. Wait ~90 seconds for GitHub Pages to build
7. Go to `https://medium.com/p/import`, paste `https://ylnhari.github.io/blog/posts/YYYY-MM-DD-your-slug/`
8. Review the imported draft on Medium, then publish

---

## For Humans

### Clone and set up
```bash
gh repo clone ylnhari/blog
cd blog
```

### Add a new post manually
Copy the template and edit it:
```bash
cp -r templates/ posts/2026-07-01-my-new-post/
# rename and edit index.html and meta.json
# update posts/index.json
git add -A && git commit -m "feat: add my-new-post" && git push
```

### Publish to Medium
1. Wait ~90s after pushing
2. Go to https://medium.com/p/import
3. Paste: `https://ylnhari.github.io/blog/posts/2026-07-01-my-new-post/`
4. Review and click Publish

---

## Repo Structure

```
blog/
├── README.md                          ← you are here
├── STANDARDS.md                       ← full agent rules and HTML spec
├── index.html                         ← blog homepage (reads posts/index.json)
├── assets/
│   └── style.css                      ← shared stylesheet — do not edit per post
├── templates/
│   ├── post.html                      ← copy this for every new post
│   └── meta.json                      ← copy this for every new post
└── posts/
    ├── index.json                     ← master post registry (update on every add)
    └── 2026-06-22-ai-assisted-blogging/
        ├── index.html                 ← post content
        └── meta.json                  ← post metadata
```

---

## What Medium Import Supports

| Works ✅ | Doesn't work ❌ |
|---------|----------------|
| H1, H2, H3 headings | Tables |
| Bold, italic, inline code | `<iframe>` / embeds |
| Code blocks (`<pre><code>`) | JavaScript |
| Images (absolute HTTPS URLs) | Inline CSS / `<style>` |
| Blockquotes, lists, links | H4–H6 |
| Horizontal rules | Relative image URLs |

For YouTube: put the bare URL in a `<p>` tag — after import, click it in Medium's editor to auto-embed.

---

## Adding an Agent

Any agent that can read `STANDARDS.md` and commit files to this repo can write blog posts. Supported workflows:

- **Claude (Cowork):** Can read the standards, generate HTML, and commit via gh CLI or GitHub web UI
- **OpenClaw:** Can read the standards, generate HTML, commit to this repo, then use Medium's import URL — avoids the editor automation entirely
- **DeepSeek / any LLM with tool use:** Same pattern — generate HTML per the template, commit, import URL to Medium

The entire spec an agent needs is in `STANDARDS.md`. Point any agent at that file.
