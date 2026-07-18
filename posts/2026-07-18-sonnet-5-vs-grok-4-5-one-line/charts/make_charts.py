"""Charts for "Claude Sonnet 5 vs Grok 4.5".

Data sources (all fetched 2026-07-18):
  - Artificial Analysis Intelligence Index via BenchLM mirror:
      https://benchlm.ai/benchmarks/artificialAnalysis
      Grok 4.5 = 53.8, Claude Sonnet 5 = 53.4
  - Pricing + per-benchmark + token efficiency: https://x.ai/news/grok-4-5
      Grok 4.5 $2/M in, $6/M out. Competitor figures on that page are drawn
      from each lab's own published cards.
  - Claude Sonnet pricing ($3/M in, $15/M out) via
      https://simonwillison.net/2026/Jul/16/kimi-k3

Run:  python make_charts.py     (writes ../images/*.png)
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(__file__), "..", "images")
os.makedirs(OUT, exist_ok=True)

INK = "#14161c"
MUTED = "#6b7280"
CLAUDE = "#2f6fed"
GROK = "#e07d2f"
OTHER = "#9aa2b3"
GRID = "#e5e7eb"


def style(ax):
    ax.set_facecolor("white")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=MUTED, labelsize=10)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def chart_intelligence_vs_price():
    """The headline: near-identical intelligence, 2.5x apart on output price."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), dpi=200)
    fig.patch.set_facecolor("white")
    models = ["Claude\nSonnet 5", "Grok 4.5"]
    colors = [CLAUDE, GROK]

    ax = axes[0]
    style(ax)
    scores = [53.4, 53.8]
    ax.bar(models, scores, color=colors, width=0.5)
    for i, v in enumerate(scores):
        ax.text(i, v + 0.6, f"{v}", ha="center", fontsize=13, fontweight="bold", color=INK)
    ax.set_ylim(0, 62)
    ax.set_title("Intelligence Index\n(Artificial Analysis)", fontsize=12,
                 fontweight="bold", color=INK, pad=12)
    ax.text(0.5, -0.22, "0.4 points apart", transform=ax.transAxes, ha="center",
            fontsize=11, color=MUTED, style="italic")

    ax = axes[1]
    style(ax)
    price = [15, 6]
    ax.bar(models, price, color=colors, width=0.5)
    for i, v in enumerate(price):
        ax.text(i, v + 0.5, f"${v}", ha="center", fontsize=13, fontweight="bold", color=INK)
    ax.set_ylim(0, 19)
    ax.set_title("Price per million\noutput tokens", fontsize=12,
                 fontweight="bold", color=INK, pad=12)
    ax.text(0.5, -0.22, "2.5x apart", transform=ax.transAxes, ha="center",
            fontsize=11, color=MUTED, style="italic")

    fig.suptitle("Same intelligence. Very different price.", fontsize=15,
                 fontweight="bold", color=INK, y=1.02)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "01-intelligence-vs-price.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


def chart_where_each_wins():
    """Per-benchmark split — the shape the aggregate score hides."""
    fig, ax = plt.subplots(figsize=(9, 4.4), dpi=200)
    fig.patch.set_facecolor("white")
    style(ax)

    labels = ["SWE Marathon\n(long-horizon agentic)", "Terminal Bench 2.1",
              "SWE Bench Pro\n(repo-scale fixes)"]
    grok = [29.0, 83.3, 64.7]
    best_claude = [24.0, 84.3, 80.4]  # Fable 5 = strongest Claude on each

    x = range(len(labels))
    w = 0.36
    ax.bar([i - w / 2 for i in x], grok, width=w, color=GROK, label="Grok 4.5")
    ax.bar([i + w / 2 for i in x], best_claude, width=w, color=CLAUDE,
           label="Best Claude (Fable 5)")

    for i, (g, c) in enumerate(zip(grok, best_claude)):
        ax.text(i - w / 2, g + 1.5, f"{g}%", ha="center", fontsize=10, color=INK)
        ax.text(i + w / 2, c + 1.5, f"{c}%", ha="center", fontsize=10, color=INK)

    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=10, color=INK)
    ax.set_ylim(0, 95)
    ax.set_ylabel("score (%)", color=MUTED, fontsize=10)
    ax.legend(frameon=False, fontsize=10, loc="upper left")
    ax.set_title("Grok runs long; Claude lands the hard change",
                 fontsize=14, fontweight="bold", color=INK, pad=14)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "02-where-each-wins.png"),
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    chart_intelligence_vs_price()
    chart_where_each_wins()
    print("wrote charts to", os.path.abspath(OUT))
