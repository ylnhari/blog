"""Chart: 06-decision.png
Decision table -- which model for which job.

All four rows transcribed verbatim from the alt text of this image in
posts/2026-07-13-claude-fable-5-vs-gpt-5-6/index.html:
  "Decision table. Repo-scale coding and low-hallucination work: Claude
  Fable 5. Autonomous agents and web browsing: GPT-5.6 Sol. Long documents:
  GPT-5.6 Sol or Terra. Cost-sensitive high-volume work: GPT-5.6 Terra or
  Luna."
This mirrors (in slightly condensed form) the numbered decision list in the
post body under "So which one" -- items 1+2 of that list ("Repo-scale coding
and autonomous debugging" / "Anything where a confident wrong answer causes
harm") are combined into row 1 here, matching the alt text's own wording.

Run: python 06-decision.py   (writes ../images/06-decision.png)
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
FABLE = "#2f6fed"
SOL = "#e07d2f"

# ---- data (verbatim from alt text) : (job, recommendation) ----
ROWS = [
    ("Repo-scale coding and\nlow-hallucination work", "Claude Fable 5"),
    ("Autonomous agents and\nweb browsing", "GPT-5.6 Sol"),
    ("Long documents", "GPT-5.6 Sol or Terra"),
    ("Cost-sensitive,\nhigh-volume work", "GPT-5.6 Terra or Luna"),
]


def main():
    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=200)
    fig.patch.set_facecolor("white")
    ax.axis("off")
    ax.set_title("So which one", fontsize=15, fontweight="bold", color=INK, pad=16)

    n = len(ROWS)
    row_h = 0.8 / n
    for i, (job, rec) in enumerate(ROWS):
        y = 0.85 - i * row_h
        ax.add_patch(plt.Rectangle((0.02, y - row_h * 0.42), 0.96, row_h * 0.84,
                                    transform=ax.transAxes, facecolor="#f6f7fb",
                                    edgecolor=GRID, linewidth=1))
        ax.text(0.06, y, job, ha="left", va="center", fontsize=10.5, color=INK,
                transform=ax.transAxes)
        color = FABLE if "Fable" in rec and "or" not in rec else SOL
        ax.text(0.94, y, rec, ha="right", va="center", fontsize=11,
                fontweight="bold", color=color, transform=ax.transAxes)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "06-decision.png"), bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("wrote", os.path.join(OUT, "06-decision.png"))
