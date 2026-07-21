"""Chart: 04-cost-per-task.png
Bar chart: cost to run one Intelligence Index task, across the GPT-5.6 family.

Numbers transcribed from posts/2026-07-13-gpt-5-6-vs-gpt-5-5/index.html,
alt text: "Bar chart of cost to run one Intelligence Index task: GPT-5.6
Luna $0.21, Terra $0.55, Sol $1.04."
Body: "Luna runs the same evaluation for $0.21 that Sol runs for $1.04."

Run: python 04-cost-per-task.py   (writes ../images/04-cost-per-task.png)
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
MODELS = [("GPT-5.6 Luna", 0.21), ("GPT-5.6 Terra", 0.55), ("GPT-5.6 Sol", 1.04)]
COLORS = ["#f7c78c", "#f2a35c", "#e07d2f"]


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
    fig, ax = plt.subplots(figsize=(7, 5), dpi=200)
    fig.patch.set_facecolor("white")
    style(ax)

    labels = [m[0] for m in MODELS]
    values = [m[1] for m in MODELS]
    ax.bar(labels, values, color=COLORS, width=0.5)
    for i, v in enumerate(values):
        ax.text(i, v + 0.03, f"${v:.2f}", ha="center", fontsize=12, fontweight="bold", color=INK)

    ax.set_ylim(0, 1.25)
    ax.set_ylabel("cost per Intelligence Index task ($)", color=MUTED, fontsize=10)
    ax.set_title("Roughly 5x cheaper, same benchmark",
                 fontsize=13, fontweight="bold", color=INK, pad=14)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "04-cost-per-task.png"), bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("wrote", os.path.join(OUT, "04-cost-per-task.png"))
