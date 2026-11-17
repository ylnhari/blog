"""Regenerate this post's figures from interactive.html (headless Chromium via Playwright).
Usage: python make_figures.py
Figures ship as 1400px JPEGs: Medium's importer silently drops very large PNGs."""
import os
from PIL import Image
from playwright.sync_api import sync_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "file://" + os.path.join(HERE, "..", "interactive.html")
OUT = os.path.join(HERE, "..", "images") + "/"
FIGS = [("ladder", "01-autonomy-ladder"), ("loop", "02-agent-loop"), ("patterns", "03-pattern-gallery"),
        ("rosetta", "04-pattern-names"), ("readwrite", "05-read-vs-write"), ("context", "06-context-budget"),
        ("harness", "07-long-running-harness"), ("safety", "08-safety"), ("protocols", "09-mcp-a2a"),
        ("evals", "10-pass-at-k"), ("chooser", "11-decision-tree"), ("examples", "12-example-support")]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1100, "height": 900}, device_scale_factor=2, color_scheme="light")
    pg.emulate_media(reduced_motion="reduce")
    pg.goto(SRC); pg.wait_for_timeout(600)
    pg.evaluate("document.querySelectorAll('.controls .spd').forEach(e=>e.style.display='none')")
    def save(sel, name, hide=""):
        if hide: pg.evaluate(f"document.querySelectorAll('{hide}').forEach(e=>e.style.display='none')")
        pg.locator(sel).screenshot(path="/tmp/_fig.png")
        if hide: pg.evaluate(f"document.querySelectorAll('{hide}').forEach(e=>e.style.display='')")
        im = Image.open("/tmp/_fig.png").convert("RGB")
        im = im.resize((1400, int(im.height * 1400 / im.width)), Image.LANCZOS)
        im.save(OUT + name + ".jpg", quality=88, optimize=True)
    for sid, name in FIGS:
        if sid == "chooser":
            save("#sv-tree", name); continue
        if sid == "context":   # show the engineered state: every technique on
            for c in pg.locator("#cx-chips .chip").all(): c.click()
        save(f"#{sid} .fig", name, hide={"loop": "#lp-play,#lp-note", "examples": "#ex-seg", "context": "#cx-chips"}.get(sid, ""))
        if sid == "examples":
            for v, n in (("Deep research", "13-example-research"), ("Coding agent", "14-example-coding")):
                pg.evaluate("v=>[...document.querySelectorAll('#ex-seg button')].find(b=>b.textContent===v).click()", v); save("#examples .fig", n, hide="#ex-seg")
    b.close()
