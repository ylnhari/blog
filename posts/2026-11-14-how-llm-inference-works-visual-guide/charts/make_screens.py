"""Regenerate this post's PNGs from the interactive page (headless Chrome via Playwright).
Usage: python make_screens.py [page_url_or_path]
Default source: the published page in ml-scratchpad."""
import sys
from playwright.sync_api import sync_playwright
SRC = sys.argv[1] if len(sys.argv) > 1 else "https://ylnhari.github.io/ml-scratchpad/llm-inference-visualized/"
OUT = __file__.rsplit("/charts/", 1)[0] + "/images/"
with sync_playwright() as p:
    b = p.chromium.launch(**({"executable_path": "/usr/bin/google-chrome", "args": ["--no-sandbox"]} if __import__("os").path.exists("/usr/bin/google-chrome") else {}))
    pg = b.new_page(viewport={"width": 1300, "height": 900}, device_scale_factor=2)
    pg.emulate_media(reduced_motion="reduce")          # skip entry animations: final frame only
    pg.goto(SRC); pg.wait_for_timeout(800)
    for _ in range(4): pg.click("#an-next")              # anatomy stage 5: split heads
    pg.locator("#anatomy .fig").screenshot(path="/tmp/_01.png")
    from PIL import Image  # Medium's importer drops the full-size PNG; ship a 1400px JPEG
    im = Image.open("/tmp/_01.png").convert("RGB"); im = im.resize((1400, int(im.height * 1400 / im.width)))
    im.save(OUT + "01-forward-pass.jpg", quality=88, optimize=True)
    pg.locator("#par-sp .fig").first.screenshot(path=OUT + "02-tensor-split-h.png")
    pg.click('#cube-seg button:text-is("SP · split s")')
    pg.locator("#par-sp .fig").first.screenshot(path=OUT + "03-sequence-split-s.png")
    pg.locator("#par-why .fig").screenshot(path=OUT + "07-gpus-needed.png")
    pg.locator("#par-tpc .fig").screenshot(path=OUT + "08-tp-matmul-trick.png")
    for _ in range(3): pg.click("#tp-next")              # TP layer walk: out-proj All-Reduce
    pg.locator("#par-tp").screenshot(path=OUT + "04-tp-layer-allreduce.png")
    pg.locator("#kv .fig").screenshot(path=OUT + "05-kv-cache-calculator.png")
    for _ in range(6): pg.click("#bw-next")              # backward: memory stage
    pg.locator("#backward .fig").screenshot(path=OUT + "06-training-vs-inference-memory.png")
    b.close()
