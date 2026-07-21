"""Chart: 05-long-context.png
Bar chart: MRCR long-context recall across the GPT-5.6 family and Claude Fable 5.

Every number transcribed from posts/2026-07-13-claude-fable-5-vs-gpt-5-6/index.html,
alt text: "Bar chart of MRCR long-context recall: GPT-5.6 Sol 91.5 percent,
Terra 89.6 percent, Fable 5 not published, Luna 41.3 percent."
Body confirms: "Sol scores 91.5% and Terra 89.6% ... Anthropic publishes a 1M
context window for Fable 5 but no comparable long-context recall figure ...
Luna, the cheap tier, collapses to 41.3% here."

Run: python 05-long-context.py   (writes ../images/05-long-context.png)
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

# ---- data (see header) : (label, MRCR recall % or None if not published) ----
MODELS = [
    ("GPT-5.6 Sol", 91.5),
    ("GPT-5.6 Terra", 89.6),
    ("Claude Fable 5", None),   # not published
    ("GPT-5.6 Luna", 41.3),
]
COLORS = ["#e07d2f", "#f2a35c", "#c8ccd6", "#f7c78c"]


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
    values = [m[1] if m[1] is not None else 0 for m in MODELS]
    bars = ax.bar(labels, values, color=COLORS, width=0.55)

    for i, m in enumerate(MODELS):
        if m[1] is not None:
            ax.text(i, m[1] + 1.5, f"{m[1]}%", ha="center", fontsize=11,
                    fontweight="bold", color=INK)
        else:
            ax.text(i, 3, "not\npublished", ha="center", fontsize=9,
                    color=MUTED, style="italic")

    ax.set_ylim(0, 100)
    ax.set_ylabel("MRCR long-context recall (%)", color=MUTED, fontsize=10)
    ax.set_title("Long context is GPT-5.6's home turf",
                 fontsize=14, fontweight="bold", color=INK, pad=14)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "05-long-context.png"), bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("wrote", os.path.join(OUT, "05-long-context.png"))
