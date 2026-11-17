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
    pg = locator.page
    pg.evaluate("document.querySelectorAll('.controls, .chips').forEach(e => e.style.display = 'none')")
    locator.screenshot(path="/tmp/_fig.png")
    pg.evaluate("document.querySelectorAll('.controls, .chips').forEach(e => e.style.display = '')")
    im = Image.open("/tmp/_fig.png").convert("RGB")
    im = im.resize((1400, int(im.height * 1400 / im.width)), Image.LANCZOS)
    im.save(OUT + name + ".jpg", quality=88, optimize=True)

with sync_playwright() as p:
    b = p.chromium.launch(**CHROME)
    # 1240px wide keeps the page in its single-column layout, so each figure spans the full width
    pg = b.new_page(viewport={"width": 1240, "height": 900}, device_scale_factor=2, color_scheme="light")
    pg.emulate_media(reduced_motion="reduce")            # skip entry animations: final frame only
    pg.goto(SRC); pg.wait_for_timeout(1000)
    # save() hides the buttons and chips for each shot: they do nothing in a static image
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
    save(pg.locator("#batching .fig").first, "07-batching")
    pg.click('#pg-seg button:text-is("Paged (8-token blocks)")')
    save(pg.locator("#paged .fig").first, "08-paged-attention")
    pg.click('#at-seg button:text-is("GQA · 2 KV")')
    save(pg.locator("#attention .fig").first, "09-gqa")
    pg.click('#fa-seg button:text-is("FlashAttention")'); pg.wait_for_timeout(300)
    save(pg.locator("#flash .fig").first, "10-flash-attention")
    save(pg.locator("#quant .fig").first, "11-quantization")
    pg.click('#sp-seg button:text-is("Prune 2:4")')
    save(pg.locator("#sparsity .fig").first, "12-sparsity")
    save(pg.locator("#distill .fig").first, "13-distillation")
    for _ in range(3): pg.click("#sd-next"); pg.wait_for_timeout(400)
    save(pg.locator("#spec .fig").first, "14-speculative-decoding")
    save(pg.locator("#par-why .fig"), "15-gpus-needed")
    save(pg.locator("#par-dp .fig"), "16-data-parallel")
    pg.click('#pp-m button:text-is("4")')
    save(pg.locator("#par-pp .fig").first, "17-pipeline-parallel")
    save(pg.locator("#par-tpc .fig"), "18-tp-matmul-trick")
    pg.click('#cube-seg button:text-is("TP · at LayerNorm (copied)")')
    save(pg.locator("#par-sp .fig").first, "19-tp-copies")
    pg.click('#cube-seg button:text-is("TP + SP · at LayerNorm (split s)")')
    save(pg.locator("#par-sp .fig").first, "20-sequence-split")
    save(pg.locator("#par-combo .fig").first, "21-combined-parallelism")
    pg.click('#md-seg button:text-is("Mixture of Experts")'); pg.wait_for_timeout(400)
    save(pg.locator("#modern .fig").first, "23-mixture-of-experts")
    for _ in range(6): pg.click("#bw-next")                # backward pass: memory stage
    save(pg.locator("#backward .fig"), "22-training-memory")
    b.close()
