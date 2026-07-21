"""Chart: 04-price-vs-intelligence.png
Scatter: output price vs AA Intelligence Index, GPT-5.6 family + Claude Fable 5.

Every number transcribed from posts/2026-07-13-claude-fable-5-vs-gpt-5-6/index.html,
alt text: "Scatter of price versus AA Intelligence Index. Fable 5 at $50 and
index 60; GPT-5.6 Sol at $30 and 58.9; Terra $15 and 55; Luna $6 and 51.2. A
dashed line shows plus twenty dollars per million output for plus 1.1 index
points."
The "+$20/+1.1 index points" annotation is the Sol-to-Fable-5 delta, and is
consistent with the four data points themselves: 50-30=20, 60-58.9=1.1 --
both figures come straight from the same sentence, no computation needed
beyond what the post already states.

Run: python 04-price-vs-intelligence.py   (writes ../images/04-price-vs-intelligence.png)
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
    ("Claude Fable 5", 50.0, 60.0, "#2f6fed"),
    ("GPT-5.6 Sol", 30.0, 58.9, "#e07d2f"),
    ("GPT-5.6 Terra", 15.0, 55.0, "#f2a35c"),
    ("GPT-5.6 Luna", 6.0, 51.2, "#f7c78c"),
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

    for name, price, idx, color in POINTS:
        ax.scatter([price], [idx], s=160, color=color, zorder=3, edgecolor="white", linewidth=1.2)
        ax.annotate(name, (price, idx), xytext=(8, 6), textcoords="offset points",
                    fontsize=10, color=INK, fontweight="bold")

    # Dashed line: the Sol -> Fable 5 premium the post calls out ("+$20 for +1.1 index points")
    sol = next(p for p in POINTS if p[0] == "GPT-5.6 Sol")
    fable = next(p for p in POINTS if p[0] == "Claude Fable 5")
    ax.plot([sol[1], fable[1]], [sol[2], fable[2]], linestyle="--", color=MUTED, linewidth=1.3, zorder=2)
    mid_x, mid_y = (sol[1] + fable[1]) / 2, (sol[2] + fable[2]) / 2
    ax.annotate("+$20/M output\nfor +1.1 index points", (mid_x, mid_y),
                xytext=(10, -22), textcoords="offset points", fontsize=9,
                color=MUTED, style="italic")

    ax.set_xlim(0, 58)
    ax.set_ylim(48, 63)
    ax.set_xlabel("Output price ($ per million tokens)", color=MUTED, fontsize=10)
    ax.set_ylabel("AA Intelligence Index", color=MUTED, fontsize=10)
    ax.set_title("What the premium buys at the very top",
                 fontsize=14, fontweight="bold", color=INK, pad=14)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "04-price-vs-intelligence.png"), bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("wrote", os.path.join(OUT, "04-price-vs-intelligence.png"))
