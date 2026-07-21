"""Chart: 01-split-decision.png
Grouped bar chart, Claude Fable 5 vs GPT-5.6 Sol, across four benchmarks.

Every number below is transcribed from posts/2026-07-13-claude-fable-5-vs-gpt-5-6/index.html:
  - SWE-bench Pro (Fable 5 80.0, Sol 64.6) and AA Intelligence Index (Fable 5 60,
    Sol 58.9): alt text of this image ("Fable 5 leads SWE-bench Pro 80 to 64.6
    and AA Intelligence Index 60 to 58.9") and body paragraph
    ("Fable 5 dominates repo-scale coding -- 80.0% on SWE-bench Pro against
    Sol's 64.6% ... edges the overall Artificial Analysis Intelligence Index,
    60 to 58.9").
  - Agents' Last Exam (Sol 53.6, Fable 5 40.5): alt text ("GPT-5.6 Sol leads
    Agents' Last Exam 53.6 to 40.5") and body ("GPT-5.6 Sol dominates
    autonomous agents and browsing -- 53.6 to 40.5 on Agents' Last Exam").
  - BrowseComp: Sol 92.2, Fable 5 not published at all (body: "a web-agent
    benchmark where Anthropic hasn't published a Fable 5 figure at all").
  - Terminal-Bench: body states "(88.0 vs 88.8)" calling it "effectively a
    tie". NOTE: the post does not unambiguously say which of the two figures
    belongs to which model -- the parenthetical trails the paragraph about
    GPT-5.6 Sol, so this script assigns Sol=88.0, Fable 5=88.8 as the most
    natural reading of that sentence order, but this attribution is inferred
    from context, not explicitly labelled in the text. Both figures are
    verbatim from the post either way, and the post's own framing ("near-tie")
    means the assignment does not change the takeaway.

Run: python 01-split-decision.py   (writes ../images/01-split-decision.png)
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(__file__), "..", "images")
os.makedirs(OUT, exist_ok=True)

INK = "#14161c"
MUTED = "#6b7280"
FABLE = "#2f6fed"
SOL = "#e07d2f"
GRID = "#e5e7eb"

# ---- data (see header for sourcing) ----
# Each entry: (benchmark label, Fable 5 value or None, Sol value or None)
BENCHMARKS = [
    ("SWE-bench Pro", 80.0, 64.6),
    ("AA Intelligence Index", 60.0, 58.9),
    ("Agents' Last Exam", 40.5, 53.6),
    ("BrowseComp", None, 92.2),          # Fable 5: not published
    ("Terminal-Bench", 88.8, 88.0),      # attribution inferred, see header note
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
    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
    fig.patch.set_facecolor("white")
    style(ax)

    labels = [b[0] for b in BENCHMARKS]
    fable_vals = [b[1] if b[1] is not None else 0 for b in BENCHMARKS]
    sol_vals = [b[2] if b[2] is not None else 0 for b in BENCHMARKS]

    x = range(len(labels))
    w = 0.36
    bars_f = ax.bar([i - w / 2 for i in x], fable_vals, width=w, color=FABLE,
                    label="Claude Fable 5")
    bars_s = ax.bar([i + w / 2 for i in x], sol_vals, width=w, color=SOL,
                     label="GPT-5.6 Sol")

    for i, b in enumerate(BENCHMARKS):
        if b[1] is not None:
            ax.text(i - w / 2, b[1] + 1.5, f"{b[1]}", ha="center", fontsize=9,
                    color=INK, fontweight="bold")
        else:
            ax.text(i - w / 2, 2, "not\npublished", ha="center", fontsize=8,
                    color=MUTED, style="italic")
        if b[2] is not None:
            ax.text(i + w / 2, b[2] + 1.5, f"{b[2]}", ha="center", fontsize=9,
                    color=INK, fontweight="bold")

    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=9.5, color=INK)
    ax.set_ylim(0, 100)
    ax.set_ylabel("score", color=MUTED, fontsize=10)
    ax.legend(frameon=False, fontsize=10, loc="upper left")
    ax.set_title("Neither one sweeps: Fable 5 vs GPT-5.6 Sol, benchmark by benchmark",
                 fontsize=13, fontweight="bold", color=INK, pad=14)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "01-split-decision.png"), bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("wrote", os.path.join(OUT, "01-split-decision.png"))
