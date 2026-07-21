"""Chart: 08-ultra-mode.png
Scatter: cost per task vs Terminal-Bench score, single-agent Sol vs Sol Ultra.

Numbers transcribed from posts/2026-07-13-gpt-5-6-vs-gpt-5-5/index.html,
alt text: "Scatter plot: single-agent Sol at $1.70 per task scoring 88.8
percent on Terminal-Bench, Sol Ultra with four agents at $5.00 scoring 91.9
percent. Three times the cost for 3.1 points."
Body: "Ultra lifts Terminal-Bench 2.1 from 88.8% to 91.9% ... roughly 3x the
cost per task, for a 3.1-point gain."

Run: python 08-ultra-mode.py   (writes ../images/08-ultra-mode.png)
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

# ---- data (see header) : (label, cost per task $, Terminal-Bench %, color) ----
POINTS = [
    ("Sol (single agent)", 1.70, 88.8, "#e07d2f"),
    ("Sol Ultra (4 agents)", 5.00, 91.9, "#a8471f"),
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
    fig, ax = plt.subplots(figsize=(7.5, 5.5), dpi=200)
    fig.patch.set_facecolor("white")
    style(ax)

    xs = [p[1] for p in POINTS]
    ys = [p[2] for p in POINTS]
    ax.plot(xs, ys, linestyle="--", color=MUTED, linewidth=1.2, zorder=1)
    for name, cost, score, color in POINTS:
        ax.scatter([cost], [score], s=180, color=color, zorder=3, edgecolor="white", linewidth=1.2)
        ax.annotate(name, (cost, score), xytext=(8, -4), textcoords="offset points",
                    fontsize=10, color=INK, fontweight="bold")

    ax.set_xlim(0, 6.5)
    ax.set_ylim(85, 94)
    ax.set_xlabel("Cost per task ($)", color=MUTED, fontsize=10)
    ax.set_ylabel("Terminal-Bench 2.1 (%)", color=MUTED, fontsize=10)
    ax.set_title("Ultra mode: 3x the cost for 3.1 points",
                 fontsize=13, fontweight="bold", color=INK, pad=14)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "08-ultra-mode.png"), bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("wrote", os.path.join(OUT, "08-ultra-mode.png"))
