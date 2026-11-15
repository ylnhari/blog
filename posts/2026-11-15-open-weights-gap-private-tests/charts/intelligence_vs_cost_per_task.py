"""Intelligence vs cost per task, open weights vs proprietary: November 2026.

    python intelligence_vs_cost_per_task.py

Writes ../images/intelligence-vs-cost-per-task.jpg (1400px JPEG: Medium's importer
drops very large PNGs).

DATA PROVENANCE
---------------
One source for both axes, one index version, so nothing is mixed across vintages:

* INTELLIGENCE: Artificial Analysis Intelligence Index v5.0.1
  (https://artificialanalysis.ai/leaderboards/models), fetched 2026-11-15.
  v5 launched 2026-10-27 with 60% of the index on private or held-out test sets.
  Scores are NOT comparable with v4.x (the August draft of this post used v4.1.1).

* COST: Artificial Analysis "cost per Intelligence Index task" (USD) from the same
  page and fetch. It is measured, not list price: it includes how many tokens each
  model actually spends at the effort setting shown.

* OPENNESS: from each model's own licence or release, checked 2026-11-15:
  - Kimi K3.1 Pro: weights on Hugging Face 2026-11-04 under the custom "Kimi K3.1-Pro
    License" (separate agreement for model-as-a-service businesses over $20M revenue
    in 12 months; branding above 100M MAU or $20M monthly revenue).
  - GLM-5.3: weights 2026-08-28 under a custom "GLM-5.3 License" (security review for
    MaaS operators over $10B revenue). GLM-5.3-Flash: plain MIT.
  - DeepSeek V4.1 Flash 1017 and V4 Pro 0813: MIT.
  Only models whose openness was checked are plotted. Proprietary = no downloadable weights.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "images", "intelligence-vs-cost-per-task.jpg")

# name, index (v5.0.1), cost per task USD, class
ROWS = [
    ("Claude Fable 5.2",     65, 26.54, "prop"),
    ("Gemini 4 Carbon",      60,  5.48, "prop"),
    ("Claude Opus 5.5",      59, 10.04, "prop"),
    ("GPT-6 Astra",          57,  6.24, "prop"),
    ("GPT-6.1 Sol",          55,  1.27, "prop"),
    ("Claude Sonnet 5.5",    55, 10.02, "prop"),
    ("Gemini 4 Hydrogen",    54,  3.16, "prop"),
    ("GPT-6.1 Terra",        51,  0.96, "prop"),
    ("Gemini 4 Argon",       50,  4.97, "prop"),
    ("Claude Haiku 5.5",     36,  0.41, "prop"),
    ("GPT-6 Luna",           28,  0.15, "prop"),
    ("Kimi K3.1 Pro",        46,  3.68, "gated"),
    ("GLM-5.3",              32,  5.01, "gated"),
    ("DeepSeek V4.1 Flash",  33,  0.60, "open"),
    ("GLM-5.3-Flash",        28,  0.58, "open"),
    ("DeepSeek V4 Pro",      23,  1.77, "open"),
]
C = {"prop": "#e07a5f", "gated": "#9b7fe0", "open": "#3fa37f"}
LABEL = {"prop": "Proprietary (no weights)", "gated": "Open weights, custom licence with conditions", "open": "Open weights, MIT licence"}
OFF = {  # label offsets in points (log x axis, so never data units)
    "Claude Fable 5.2": (-10, 6, "right"), "Gemini 4 Carbon": (0, 11, "center"), "Claude Opus 5.5": (10, 4, "left"),
    "GPT-6 Astra": (0, -17, "center"), "GPT-6.1 Sol": (-10, 6, "right"), "Claude Sonnet 5.5": (10, -12, "left"),
    "Gemini 4 Hydrogen": (-10, -12, "right"), "GPT-6.1 Terra": (-10, -10, "right"), "Gemini 4 Argon": (10, -10, "left"),
    "Claude Haiku 5.5": (10, 2, "left"), "GPT-6 Luna": (0, 11, "center"), "Kimi K3.1 Pro": (10, 4, "left"),
    "GLM-5.3": (10, 2, "left"), "DeepSeek V4.1 Flash": (10, 4, "left"), "GLM-5.3-Flash": (8, -13, "left"),
    "DeepSeek V4 Pro": (10, -4, "left"),
}
fig, ax = plt.subplots(figsize=(11.5, 7.4), dpi=150)
fig.patch.set_facecolor("#fbfaf7"); ax.set_facecolor("#fbfaf7")
for cls in ("prop", "gated", "open"):
    xs = [r[2] for r in ROWS if r[3] == cls]; ys = [r[1] for r in ROWS if r[3] == cls]
    ax.scatter(xs, ys, s=170, color=C[cls], edgecolor="#1c1a2b", linewidth=0.8, zorder=3, label=LABEL[cls])
for name, idx, cost, cls in ROWS:
    dx, dy, ha = OFF[name]
    ax.annotate(name, (cost, idx), xytext=(dx, dy), textcoords="offset points", ha=ha, fontsize=10,
                fontweight="bold" if cls != "prop" else "normal", color="#1c1a2b", zorder=4)
ax.annotate("", xy=(3.68, 64.6), xytext=(3.68, 46.6), arrowprops=dict(arrowstyle="<->", color="#1c1a2b", lw=1.2, ls="--"))
ax.text(3.45, 61.5, "19-point gap:\nbest open weights\nvs best overall", fontsize=10, color="#1c1a2b", va="center", ha="right")
ax.set_xscale("log"); ax.set_xlim(0.1, 40); ax.set_ylim(18, 69)
ax.set_xticks([0.1, 0.3, 1, 3, 10, 30]); ax.set_xticklabels(["$0.10", "$0.30", "$1", "$3", "$10", "$30"])
ax.set_xlabel("Measured cost per Intelligence Index task (USD, log scale)", fontsize=11)
ax.set_ylabel("Artificial Analysis Intelligence Index v5.0.1", fontsize=11)
ax.set_title("On the new private-test index, open weights sit well below the frontier.\nSome of the cheapest strong models are proprietary.", fontsize=13.5, loc="left", pad=12, color="#1c1a2b")
ax.grid(True, which="both", alpha=0.2, lw=0.7); ax.set_axisbelow(True)
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.legend(loc="lower right", frameon=False, fontsize=10)
fig.text(0.01, 0.01, "Source: Artificial Analysis leaderboard, Intelligence Index v5.0.1 and cost per task, fetched 15 Nov 2026. Openness from each model's licence.", fontsize=8.5, color="#66637d")
fig.tight_layout(rect=(0, 0.03, 1, 1))
tmp = os.path.join(HERE, "_chart.png"); fig.savefig(tmp, facecolor=fig.get_facecolor())
im = Image.open(tmp).convert("RGB"); im = im.resize((1400, int(im.height * 1400 / im.width)), Image.LANCZOS)
im.save(OUT, quality=88, optimize=True); os.remove(tmp)
print("wrote", OUT, im.size)
