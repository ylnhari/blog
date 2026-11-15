"""Regenerate this post's figures from the interactive page (headless Chrome via Playwright).
Usage: python make_screens.py [page_url_or_path]
Default source: the published page in ml-scratchpad.
Figures ship as 1400px JPEGs: Medium's importer silently drops very large PNGs."""
import os, sys
from PIL import Image
from playwright.sync_api import sync_playwright

SRC = sys.argv[1] if len(sys.argv) > 1 else "https://ylnhari.github.io/ml-scratchpad/llm-inference-visualized/"
OUT = __file__.rsplit("/charts/", 1)[0] + "/images/"
os.makedirs(OUT, exist_ok=True)
CHROME = {"executable_path": "/usr/bin/google-chrome", "args": ["--no-sandbox"]} if os.path.exists("/usr/bin/google-chrome") else {}

def save(locator, name):
    locator.screenshot(path="/tmp/_fig.png")
    im = Image.open("/tmp/_fig.png").convert("RGB")
    im = im.resize((1400, int(im.height * 1400 / im.width)), Image.LANCZOS)
    im.save(OUT + name + ".jpg", quality=88, optimize=True)

with sync_playwright() as p:
    b = p.chromium.launch(**CHROME)
    # 1240px wide keeps the page in its single-column layout, so each figure spans the full width
    pg = b.new_page(viewport={"width": 1240, "height": 900}, device_scale_factor=2, color_scheme="light")
    pg.emulate_media(reduced_motion="reduce")            # skip entry animations: final frame only
    pg.goto(SRC); pg.wait_for_timeout(1000)
    for _ in range(4): pg.click("#ar-next")                # architecture: attention highlighted
    save(pg.locator("#architecture .fig"), "01-architecture")
    save(pg.locator("#attention-explained .fig"), "02-attention")
    for _ in range(4): pg.click("#an-next")                # forward pass stage 5: split heads
    save(pg.locator("#anatomy .fig"), "03-tensor-shapes")
    pg.click("#pd-next"); pg.click("#pd-skip")             # prefill, full picture
    save(pg.locator("#phases .fig"), "04-prefill")
    for _ in range(2): pg.click("#pd-next")
    pg.click("#pd-skip")                                    # first decode step, full picture
    save(pg.locator("#phases .fig"), "05-decode")
    save(pg.locator("#kv .fig"), "06-kv-cache")
    save(pg.locator("#par-why .fig"), "07-gpus-needed")
    save(pg.locator("#par-dp .fig"), "08-data-parallel")
    save(pg.locator("#par-tpc .fig"), "09-tp-matmul-trick")
    pg.click('#cube-seg button:text-is("TP · LayerNorm (copied)")')
    save(pg.locator("#par-sp .fig").first, "10-tp-copies")
    pg.click('#cube-seg button:text-is("SP · split s")')
    save(pg.locator("#par-sp .fig").first, "11-sequence-split")
    for _ in range(6): pg.click("#bw-next")                # backward pass: memory stage
    save(pg.locator("#backward .fig"), "12-training-memory")
    b.close()
