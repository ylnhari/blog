# Skill: Create Blog Post

## Trigger

Use this skill when Hari says any of:
- "write a blog post about X"
- "create a post on X"
- "new blog post: X"
- "draft a Medium post about X"
- "add a post to the blog"
- "blog about X"

## What This Skill Does

Takes a topic from Hari, generates a complete blog post, commits it to `github.com/ylnhari/blog`, imports it to Medium, and leaves a draft for Hari to review and publish. Hari only needs to click Publish.

## Before You Start

1. Read `AGENT.md` in the blog repo root — it has the full step-by-step workflow.
2. Read `STANDARDS.md` in the blog repo root — it defines every HTML rule.
3. The repo is cloned at `C:\Users\ylnha\projects\blog`

## Step Summary

```
1. Confirm topic, audience, length with Hari (1 message exchange)
2. Generate complete blog post content
3. Create posts/YYYY-MM-DD-slug/index.html  (from templates/post.html)
4. Create posts/YYYY-MM-DD-slug/meta.json   (from templates/meta.json)
5. Update posts/index.json                  (prepend new entry)
6. git add + commit + push via gh CLI
7. Wait 90s, verify https://ylnhari.github.io/blog/posts/YYYY-MM-DD-slug/
8. Navigate to https://medium.com/p/import
9. Paste GitHub Pages URL, click Import
10. Report Medium draft URL to Hari
```

## Output to Hari

Always finish with:
```
✅ Post created: "[TITLE]"
📄 GitHub Pages: https://ylnhari.github.io/blog/posts/YYYY-MM-DD-slug/
📝 Medium draft: https://medium.com/p/{id}/edit

The draft is ready for your review. Open the Medium link, make any edits, and click Publish when you're happy with it.
```

## Key Rules

- Generate REAL, accurate content — no filler or hallucinated facts
- Cover image MUST be an absolute HTTPS URL (use Unsplash: `https://images.unsplash.com/photo-{id}?w=1200&q=80`)
- NEVER use: `<script>`, `<style>`, `<iframe>`, `<table>`, `<div>`, `<span>`, inline CSS, relative image URLs
- NEVER click Publish on Medium — leave as draft
- If git push fails: run `gh auth login` first
- If Medium import fails: verify the GitHub Pages URL loads in a browser (HTTP 200) before retrying
