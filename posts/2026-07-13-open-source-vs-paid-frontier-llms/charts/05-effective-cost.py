"""Chart: 05-effective-cost.png
Bar chart: effective cost per task, Claude Opus 4.8 (baseline) vs Grok 4.5.

Numbers transcribed from
posts/2026-07-13-open-source-vs-paid-frontier-llms/index.html,
alt text: "Bar chart comparing effective cost per task. Claude Opus 4.8 is
the baseline at 1.0; Grok 4.5 completes the same task at roughly 0.06 of the
cost, being both cheaper per token and far more token-efficient."
Body: "Grok 4.5 is priced at $2 input / $6 output ... roughly 4.2x fewer
tokens than Opus 4.8. Multiply the two effects together and a finished task
can cost a small fraction of the Opus equivalent." (The supporting $2/$6 and
4.2x figures are included below as annotations only -- the chart's own two
plotted values, 1.0 and ~0.06, are the numbers explicitly given for this
image.)

Run: python 05-effective-cost.py   (writes ../images/05-effective-cost.png)
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
MODELS = [("Claude Opus 4.8\n(baseline)", 1.0), ("Grok 4.5", 0.06)]
COLORS = ["#2f6fed", "#e07d2f"]


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
    fig, ax = plt.subplots(figsize=(7, 5.2), dpi=200)
    fig.patch.set_facecolor("white")
    style(ax)

    labels = [m[0] for m in MODELS]
    values = [m[1] for m in MODELS]
    ax.bar(labels, values, color=COLORS, width=0.45)
    for i, v in enumerate(values):
        ax.text(i, v + 0.03, f"{v:.2f}x", ha="center", fontsize=13, fontweight="bold", color=INK)

    ax.set_ylim(0, 1.2)
    ax.set_ylabel("effective cost per task (Opus 4.8 = 1.0)", color=MUTED, fontsize=9.5)
    ax.set_title("Sticker price isn't task price",
                 fontsize=13, fontweight="bold", color=INK, pad=14)
    ax.text(0.5, -0.16,
            "Grok 4.5: $2/M input, $6/M output, ~4.2x fewer tokens than Opus 4.8",
            transform=ax.transAxes, ha="center", fontsize=9, color=MUTED, style="italic")

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "05-effective-cost.png"), bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("wrote", os.path.join(OUT, "05-effective-cost.png"))
