"""Side-by-side of the SVG each model drew for the same prompt.

Prompt (identical to both, first answer taken):
  "Generate an SVG of an auto-rickshaw towing a server rack up a steep hill,
   monsoon rain falling. Return only the SVG in one code block."

Source renders live in the private bench kit; this script composites the two
into one image for the post.
"""
import os
from pathlib import Path
from PIL import Image, ImageDraw

default_bench = Path(__file__).resolve().parents[4] / "signaldesk" / "experiments" / "model-bench" / "results"
MB = Path(os.environ.get("MODEL_BENCH_RESULTS", default_bench)).expanduser().resolve()
if not MB.is_dir():
    raise SystemExit("Set MODEL_BENCH_RESULTS to the private benchmark results directory.")
OUT = Path(__file__).resolve().parent.parent / "images"
OUT.mkdir(parents=True, exist_ok=True)

CLAUDE = (47, 111, 237)
GROK = (224, 125, 47)


def load(p, h=560):
    im = Image.open(p).convert("RGB")
    w = int(im.width * h / im.height)
    return im.resize((w, h), Image.LANCZOS)


a = load(MB / "claude-sonnet-5" / "2026-07-18" / "x1-render.png")
b = load(MB / "grok-4.5" / "2026-07-18" / "x1-render.png")

pad, top = 24, 54
W = a.width + b.width + pad * 3
H = a.height + top + pad
canvas = Image.new("RGB", (W, H), "white")
canvas.paste(a, (pad, top))
canvas.paste(b, (pad * 2 + a.width, top))

d = ImageDraw.Draw(canvas)
d.text((pad + 8, 20), "Claude Sonnet 5", fill=CLAUDE)
d.text((pad * 2 + a.width + 8, 20), "Grok 4.5", fill=GROK)

output = OUT / "03-svg-side-by-side.png"
canvas.save(output)
print("wrote", output)
