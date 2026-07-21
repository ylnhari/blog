"""Chart: 02-who-wins-what.png
Categorical "who wins each category" map -- Claude Fable 5 vs GPT-5.6.

All category/winner assignments are transcribed verbatim from the alt text of
this image in posts/2026-07-13-claude-fable-5-vs-gpt-5-6/index.html:
  "Fable 5 wins repo-scale coding, trustworthiness, and the raw intelligence
   ceiling; GPT-5.6 wins autonomous agents, web browsing, and long-context
   recall."

The one numeric figure on this chart -- the hallucination rate -- is
transcribed from the body paragraph immediately below the image:
  "On AA-Omniscience, which measures how often a model answers confidently
   and wrongly, Fable 5 hallucinates 36.2% of the time. OpenAI hasn't
   published Sol's number, but its predecessor GPT-5.5 sat above 85% on the
   same test."
Note: the >85% figure is explicitly GPT-5.5 (Sol's predecessor), NOT Sol
itself -- the post is explicit that Sol's own number was never published.
That distinction is preserved below; it is not attributed to Sol.

Run: python 02-who-wins-what.py   (writes ../images/02-who-wins-what.png)
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

# ---- data (verbatim from alt text) ----
FABLE_WINS = ["Repo-scale coding", "Trustworthiness", "Raw intelligence ceiling"]
SOL_WINS = ["Autonomous agents", "Web browsing", "Long-context recall"]

# Supplementary numeric fact from the body paragraph right after this image.
HALLUCINATION_FABLE5 = 36.2       # AA-Omniscience hallucination rate, Fable 5
HALLUCINATION_GPT55 = 85.0        # "above 85%" -- this is GPT-5.5 (predecessor), not Sol
SOL_HALLUCINATION_PUBLISHED = False  # post states Sol's own figure was never published


def main():
    fig, ax = plt.subplots(figsize=(9, 5), dpi=200)
    fig.patch.set_facecolor("white")
    ax.axis("off")

    ax.set_title("Who wins what", fontsize=15, fontweight="bold", color=INK, pad=18)

    ax.text(0.25, 0.88, "Claude Fable 5 wins", ha="center", fontsize=13,
            fontweight="bold", color=FABLE, transform=ax.transAxes)
    for i, cat in enumerate(FABLE_WINS):
        ax.text(0.25, 0.75 - i * 0.12, cat, ha="center", fontsize=11.5,
                color=INK, transform=ax.transAxes)

    ax.text(0.75, 0.88, "GPT-5.6 Sol wins", ha="center", fontsize=13,
            fontweight="bold", color=SOL, transform=ax.transAxes)
    for i, cat in enumerate(SOL_WINS):
        ax.text(0.75, 0.75 - i * 0.12, cat, ha="center", fontsize=11.5,
                color=INK, transform=ax.transAxes)

    ax.axvline(0.5, ymin=0.25, ymax=0.92, color="#e5e7eb", linewidth=1.2,
               transform=ax.transAxes)

    note = (f"AA-Omniscience hallucination rate: Fable 5 = {HALLUCINATION_FABLE5}%.\n"
            f"Sol's own figure not published; predecessor GPT-5.5 was above {HALLUCINATION_GPT55:.0f}%.")
    ax.text(0.5, 0.10, note, ha="center", fontsize=9.5, color=MUTED,
            style="italic", transform=ax.transAxes)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "02-who-wins-what.png"), bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
    print("wrote", os.path.join(OUT, "02-who-wins-what.png"))
