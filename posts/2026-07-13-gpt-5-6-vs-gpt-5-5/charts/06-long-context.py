"""Chart: 06-long-context.png
Bar chart: MRCR long-context recall across GPT-5.5 and the GPT-5.6 family.

Numbers transcribed from posts/2026-07-13-gpt-5-6-vs-gpt-5-5/index.html,
alt text: "Bar chart of MRCR long-context recall: GPT-5.6 Sol 91.5 percent,
Terra 89.6 percent, GPT-5.5 74.0 percent, GPT-5.6 Luna 41.3 percent."
Body: "Sol scores 91.5% against GPT-5.5's 74.0% ... Luna scores 41.3%."

Run: python 06-long-context.py   (writes ../images/06-long-context.png)
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

# ---- data (see header) ----
MODELS = [
    ("GPT-5.6 Sol", 91.5),
    ("GPT-5.6 Terra", 89.6),
    ("GPT-5.5", 74.0),
    ("GPT-5.6 Luna", 41.3),
]
COLORS = ["#e07d2f", "#f2a35c", "#9aa2b3", "#f7c78c"]


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
    fig, ax = plt.subplots(figsize=(8, 5), dpi=200)
    fig.patch.set_facecolor("white")
    style(ax)

    labels = [m[0] for m in MODELS]
    values = [m[1] for m in MODELS]
    ax.bar(labels, values, color=COLORS, width=0.55)
    for i, v in enumerate(values):
        ax.text(i, v + 1.5, f"{v}%", ha="center", fontsize=11, fontweight="bold", color=INK)

    ax.set_ylim(0, 100)
    ax.set_ylabel("MRCR long-context recall (%)", color=MUTED, fontsize=10)
    ax.set_title("The trap inside the ladder: a cliff, not a slope",
                 fontsize=13, fontweight="bold", color=INK, pad=14)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "06-long-context.png"), bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("wrote", os.path.join(OUT, "06-long-context.png"))
