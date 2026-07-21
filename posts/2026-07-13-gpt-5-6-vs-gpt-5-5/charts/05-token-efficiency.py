"""Chart: 05-token-efficiency.png
Bar chart: output tokens per Intelligence Index task, GPT-5.5 vs GPT-5.6 Sol.

Numbers transcribed from posts/2026-07-13-gpt-5-6-vs-gpt-5-5/index.html,
alt text: "Bar chart: GPT-5.5 uses 16,000 output tokens per Intelligence
Index task, GPT-5.6 Sol uses 15,000."
Body: "Roughly 6% fewer output tokens on this particular measure, with OpenAI
claiming 10-15% in general." (16000 -> 15000 is ~6.25%, consistent with the
post's own "roughly 6%" framing.)

Run: python 05-token-efficiency.py   (writes ../images/05-token-efficiency.png)
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
MODELS = [("GPT-5.5", 16000), ("GPT-5.6 Sol", 15000)]
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
        ax.text(i, v + 300, f"{v:,}", ha="center", fontsize=12, fontweight="bold", color=INK)

    ax.set_ylim(0, 18500)
    ax.set_ylabel("output tokens per Intelligence Index task", color=MUTED, fontsize=9.5)
    ax.set_title("Same intelligence, fewer tokens to get there",
                 fontsize=13, fontweight="bold", color=INK, pad=14)
    ax.text(0.5, -0.14, "~6% fewer output tokens per task",
            transform=ax.transAxes, ha="center", fontsize=10, color=MUTED, style="italic")

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "05-token-efficiency.png"), bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("wrote", os.path.join(OUT, "05-token-efficiency.png"))
