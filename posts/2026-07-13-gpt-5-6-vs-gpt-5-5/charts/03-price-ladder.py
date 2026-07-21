"""Chart: 03-price-ladder.png
Scatter: AA Intelligence Index vs output price, GPT-5.5 and the GPT-5.6 family.

Numbers transcribed from posts/2026-07-13-gpt-5-6-vs-gpt-5-5/index.html,
alt text: "Scatter plot of Intelligence Index against output price. GPT-5.5
and GPT-5.6 Sol both at $30, scoring 60 and 59. GPT-5.6 Terra at $15 scoring
55, GPT-5.6 Luna at $6 scoring 51, forming a dashed price ladder."

Run: python 03-price-ladder.py   (writes ../images/03-price-ladder.png)
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

# ---- data (see header) : (label, output $/M, AA Intelligence Index, color) ----
POINTS = [
    ("GPT-5.5", 30.0, 60.0, "#9aa2b3"),
    ("GPT-5.6 Sol", 30.0, 59.0, "#e07d2f"),
    ("GPT-5.6 Terra", 15.0, 55.0, "#f2a35c"),
    ("GPT-5.6 Luna", 6.0, 51.0, "#f7c78c"),
]


def style(ax):
    ax.set_facecolor("white")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=MUTED, labelsize=10)
    ax.grid(color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def main():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=200)
    fig.patch.set_facecolor("white")
    style(ax)

    # dashed ladder line through the three GPT-5.6 tiers
    ladder = [p for p in POINTS if "5.6" in p[0]]
    ax.plot([p[1] for p in ladder], [p[2] for p in ladder], linestyle="--",
            color=MUTED, linewidth=1.2, zorder=1)

    for name, price, idx, color in POINTS:
        ax.scatter([price], [idx], s=160, color=color, zorder=3, edgecolor="white", linewidth=1.2)
        ax.annotate(name, (price, idx), xytext=(8, 6), textcoords="offset points",
                    fontsize=10, color=INK, fontweight="bold")

    ax.set_xlim(0, 35)
    ax.set_ylim(45, 65)
    ax.set_xlabel("Output price ($ per million tokens)", color=MUTED, fontsize=10)
    ax.set_ylabel("AA Intelligence Index", color=MUTED, fontsize=10)
    ax.set_title("GPT-5.5 was one model, GPT-5.6 is a price ladder",
                 fontsize=13, fontweight="bold", color=INK, pad=14)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "03-price-ladder.png"), bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("wrote", os.path.join(OUT, "03-price-ladder.png"))
