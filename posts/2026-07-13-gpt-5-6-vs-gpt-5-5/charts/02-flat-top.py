"""Chart: 02-flat-top.png
Bar chart: AA Intelligence Index, GPT-5.5 vs GPT-5.6 Sol (both max reasoning).

Numbers transcribed from posts/2026-07-13-gpt-5-6-vs-gpt-5-5/index.html:
  alt text: "Bar chart: GPT-5.5 scores 60 on the Artificial Analysis
  Intelligence Index, GPT-5.6 Sol scores 59. The new flagship is one point
  lower."
  body: "Sixty versus fifty-nine. One point, in the wrong direction."

Run: python 02-flat-top.py   (writes ../images/02-flat-top.png)
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
MODELS = [("GPT-5.5", 60), ("GPT-5.6 Sol", 59)]
COLORS = ["#9aa2b3", "#e07d2f"]


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
    fig, ax = plt.subplots(figsize=(6, 5), dpi=200)
    fig.patch.set_facecolor("white")
    style(ax)

    labels = [m[0] for m in MODELS]
    values = [m[1] for m in MODELS]
    ax.bar(labels, values, color=COLORS, width=0.5)
    for i, v in enumerate(values):
        ax.text(i, v + 1, f"{v}", ha="center", fontsize=14, fontweight="bold", color=INK)

    ax.set_ylim(0, 68)
    ax.set_ylabel("AA Intelligence Index", color=MUTED, fontsize=10)
    ax.set_title("Raw intelligence at the top: flat",
                 fontsize=13, fontweight="bold", color=INK, pad=14)
    ax.text(0.5, -0.14, "One point lower, in the wrong direction",
            transform=ax.transAxes, ha="center", fontsize=10, color=MUTED, style="italic")

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "02-flat-top.png"), bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("wrote", os.path.join(OUT, "02-flat-top.png"))
