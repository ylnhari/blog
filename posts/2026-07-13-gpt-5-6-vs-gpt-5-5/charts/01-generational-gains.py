"""Chart: 01-generational-gains.png
Grouped bar chart: point gains, GPT-5.6 Sol vs GPT-5.5, per benchmark.

Numbers transcribed from posts/2026-07-13-gpt-5-6-vs-gpt-5-5/index.html,
alt text: "Grouped bar chart of GPT-5.6 Sol versus GPT-5.5: ExploitBench
+25.6, DeepSWE +5.7, SWE-bench Pro +5.2, Terminal-Bench 2.1 +3.2, AA Coding
Agent Index +3.6."
Body corroborates the ExploitBench figure with absolute numbers: "from
47.9% to 73.5%" (delta 25.6, matching the alt text exactly).

Run: python 01-generational-gains.py   (writes ../images/01-generational-gains.png)
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
SOL = "#e07d2f"

# ---- data (see header) : (benchmark, point gain of Sol over GPT-5.5) ----
GAINS = [
    ("ExploitBench", 25.6),
    ("DeepSWE", 5.7),
    ("SWE-bench Pro", 5.2),
    ("Terminal-Bench 2.1", 3.2),
    ("AA Coding Agent Index", 3.6),
]


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
    fig, ax = plt.subplots(figsize=(9.5, 5), dpi=200)
    fig.patch.set_facecolor("white")
    style(ax)

    labels = [g[0] for g in GAINS]
    values = [g[1] for g in GAINS]
    ax.bar(labels, values, color=SOL, width=0.55)
    for i, v in enumerate(values):
        ax.text(i, v + 0.6, f"+{v}", ha="center", fontsize=11, fontweight="bold", color=INK)

    ax.set_ylim(0, 30)
    ax.set_ylabel("point gain (Sol over GPT-5.5)", color=MUTED, fontsize=10)
    ax.set_xticklabels(labels, fontsize=9.5, color=INK, rotation=12, ha="right")
    ax.set_title("Every agentic and coding measure moved up, same flagship price",
                 fontsize=13, fontweight="bold", color=INK, pad=14)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "01-generational-gains.png"), bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("wrote", os.path.join(OUT, "01-generational-gains.png"))
