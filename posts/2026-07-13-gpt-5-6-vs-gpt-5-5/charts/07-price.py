"""Chart: 07-price.png
Grouped bar chart: input/output prices, GPT-5.6 family + GPT-5.5 + GPT-5.5 Pro.

Numbers transcribed from posts/2026-07-13-gpt-5-6-vs-gpt-5-5/index.html,
alt text: "Grouped bar chart of input and output prices: GPT-5.6 Luna $1/$6,
Terra $2.50/$15, Sol $5/$30, GPT-5.5 $5/$30, GPT-5.5 Pro $30/$180."
Body: "Sol costs $5 input / $30 output per million tokens, identical to
GPT-5.5" and "GPT-5.5 Pro was ... $30 / $180."

Run: python 07-price.py   (writes ../images/07-price.png)
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(__file__), "..", "images")
os.makedirs(OUT, exist_ok=True)

INK = "#14161c"
MUTED = "#6b7280"
GRID = "#e5e7eb"

# ---- data (see header) : (label, input $/M, output $/M) ----
MODELS = [
    ("GPT-5.6\nLuna", 1.0, 6.0),
    ("GPT-5.6\nTerra", 2.5, 15.0),
    ("GPT-5.6\nSol", 5.0, 30.0),
    ("GPT-5.5", 5.0, 30.0),
    ("GPT-5.5\nPro", 30.0, 180.0),
]
INPUT_COLOR = "#93b4f7"
OUTPUT_COLOR = "#2f6fed"


def style(ax):
    ax.set_facecolor("white")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=MUTED, labelsize=10)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def main():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=200)
    fig.patch.set_facecolor("white")
    style(ax)

    labels = [m[0] for m in MODELS]
    inputs = [m[1] for m in MODELS]
    outputs = [m[2] for m in MODELS]
    x = range(len(labels))
    w = 0.36

    ax.bar([i - w / 2 for i in x], inputs, width=w, color=INPUT_COLOR, label="Input $/M")
    ax.bar([i + w / 2 for i in x], outputs, width=w, color=OUTPUT_COLOR, label="Output $/M")

    for i, (_, inp, out) in enumerate(MODELS):
        ax.text(i - w / 2, inp + 3, f"${inp:g}", ha="center", fontsize=9, color=INK)
        ax.text(i + w / 2, out + 3, f"${out:g}", ha="center", fontsize=9, color=INK)

    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=9.5, color=INK)
    ax.set_ylim(0, 200)
    ax.set_ylabel("$ per million tokens", color=MUTED, fontsize=10)
    ax.legend(frameon=False, fontsize=10, loc="upper left")
    ax.set_title("The quiet casualty: GPT-5.5 Pro",
                 fontsize=14, fontweight="bold", color=INK, pad=14)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "07-price.png"), bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("wrote", os.path.join(OUT, "07-price.png"))
