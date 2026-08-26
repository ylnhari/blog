"""Intelligence vs blended cost, open-weight vs proprietary — August 2026.

    python intelligence_vs_cost.py

Writes ../images/intelligence-vs-cost.png

DATA PROVENANCE (this is the point of committing the generator)
---------------------------------------------------------------
Two independent sources, deliberately kept apart:

* INTELLIGENCE  — Artificial Analysis Intelligence Index v4.1.1, fetched
  2026-08-26. Independent measurement, not a vendor's claim about itself.
  AA publishes no last-updated date; the version string is the only provenance.

* PRICE         — each VENDOR'S OWN pricing page, fetched 2026-08-26. Not AA's
  price column: AA's leaderboard listing disagrees with AA's own model pages
  (it showed Opus 5 at $2.34 against $3.85 on the model page), so its prices are
  not used here at all.

BLENDED PRICE FORMULA
---------------------
AA blends a single $/M figure as 0.7*cached_input + 0.2*input + 0.1*output.
That is not documented as a formula on their site — it is DERIVED here and
verified to reproduce three of their published model-page figures exactly:

    Sol      0.7(0.40) + 0.2(4)  + 0.1(20) = 3.08   (AA prints 3.08)
    Opus 5   0.7(0.50) + 0.2(5)  + 0.1(25) = 3.85   (AA prints 3.85)
    Kimi K3  0.7(0.30) + 0.2(3)  + 0.1(15) = 2.31   (AA prints 2.31)

Because it reproduces AA exactly, the same formula is applied to VENDOR prices
for models whose AA price column could not be trusted or verified. Every such
row is marked `derived=True` below and is drawn with a hollow marker.

CAVEATS CARRIED INTO THE CHART
------------------------------
* Gemini 3.7 Flash is on PROMOTIONAL pricing through 2026-12-31, reverting to
  exactly 2x on 2027-01-01. Both points are plotted; the promo one is annotated.
* GPT-5.6 Sol's price is also promotional ("at least through 2026-11-21");
  OpenAI does not publish the reversion price, so no reverted point is drawn.
* Anthropic's 4.7-and-later models emit ~30% more tokens for the same text, so
  the Claude points understate real per-task cost. Noted on the chart, not
  silently baked into the numbers.
* Claude Fable 5's AA index is listed as "(max, Opus 4.8 fallback)" — lower
  confidence than the others; marked with a hatched marker.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "images", "intelligence-vs-cost.png")


def blended(cached, inp, out):
    """AA's blend, derived and verified against three of their model pages."""
    return 0.7 * cached + 0.2 * inp + 0.1 * out


# name, index, cached, input, output, class, derived, note
ROWS = [
    # --- proprietary -----------------------------------------------------
    ("Claude Fable 5",   62, 1.00, 10.00, 50.00, "prop", True,  "fallback"),
    ("Claude Opus 5",    63, 0.50,  5.00, 25.00, "prop", False, ""),
    ("GPT-5.6 Sol",      61, 0.40,  4.00, 20.00, "prop", False, "promo"),
    ("Grok 4.6",         61, 0.50,  2.00,  6.00, "prop", True,  ""),
    ("GPT-5.6 Terra",    57, 0.20,  2.00, 12.00, "prop", True,  ""),
    ("Gemini 3.7 Flash", 56, 0.075, 0.75,  3.75, "prop", True,  "promo"),
    ("Claude Sonnet 5",  55, 0.20,  2.00, 10.00, "prop", True,  ""),
    ("GPT-5.6 Luna",     52, 0.02,  0.20,  1.20, "prop", True,  ""),
    # --- weights downloadable, but licence carries a revenue trigger -----
    ("Kimi K3",          60, 0.30,  3.00, 15.00, "gated", False, "$20M trigger"),
    # --- genuinely open source, permissive licence -----------------------
    ("DeepSeek V4-Pro",  53, 0.044, 1.32,  3.96, "open", False, "MIT"),
    ("DeepSeek V4-Flash", 52, 0.014, 0.44, 1.32, "open", False, "MIT"),
]

# Gemini 3.7 Flash after the promo expires (exactly 2x on both sides)
REVERT = ("Gemini 3.7 Flash\n(from Jan 2027)", 56,
          blended(0.15, 1.50, 7.50), "prop")

C_PROP = "#c2410c"   # proprietary
C_OPEN = "#1d4ed8"   # open source, permissive licence (MIT / Apache-2.0)
C_GATE = "#7c3aed"   # weights downloadable, but licence has a revenue trigger

fig, ax = plt.subplots(figsize=(11, 7.2))

# Label offsets are in POINTS, never data units — the x axis is logarithmic,
# so a fixed data offset would shift labels wildly across the range.
# (dx_pt, dy_pt, horizontal alignment)
OFFSET = {
    "Claude Fable 5":    (-14, 10, "right"),
    "Claude Opus 5":     (-14,  8, "right"),
    "GPT-5.6 Sol":       (  2, 14, "center"),
    "Grok 4.6":          (  0, 14, "center"),
    "GPT-5.6 Terra":     (-14,  6, "right"),
    "Gemini 3.7 Flash":  (-12, 10, "right"),
    "Claude Sonnet 5":   ( 14, -4, "left"),
    "GPT-5.6 Luna":      (  0, -21, "center"),
    "Kimi K3":           (  0, -22, "center"),
    "DeepSeek V4-Pro":   (  0,  15, "center"),
    "DeepSeek V4-Flash": ( 15,  6, "left"),
}

COLOR = {"prop": C_PROP, "open": C_OPEN, "gated": C_GATE}

for name, idx, cached, inp, out, cls, derived, note in ROWS:
    x = blended(cached, inp, out)
    color = COLOR[cls]
    ax.scatter(x, idx, s=210,
               facecolors="none" if derived else color,
               edgecolors=color, linewidths=2.2, zorder=3,
               hatch="///" if note == "fallback" else None)
    label = name
    if note in ("MIT", "$20M trigger", "promo"):
        label = f"{name} ({note})"
    dx, dy, ha = OFFSET.get(name, (12, 8, "left"))
    ax.annotate(label, (x, idx), xytext=(dx, dy),
                textcoords="offset points", ha=ha,
                fontsize=10.5, color="#111", zorder=4,
                fontweight="bold" if cls != "prop" else "normal")

# the promo-expiry ghost point
ridx = REVERT[1]
rx = REVERT[2]
gx = blended(0.075, 0.75, 3.75)
ax.scatter(rx, ridx, s=210, facecolors="none", edgecolors=C_PROP,
           linewidths=1.4, linestyle=":", zorder=3)
ax.annotate("", xy=(rx, ridx), xytext=(gx, ridx),
            arrowprops=dict(arrowstyle="->", color=C_PROP, ls=":", lw=1.4))
ax.annotate("2x on 1 Jan 2027", (rx, ridx), xytext=(6, -14),
            textcoords="offset points", fontsize=9.5, color=C_PROP,
            style="italic")

ax.set_xscale("log")
ax.set_xlim(0.12, 12)
ax.set_ylim(49.5, 65.5)
ax.set_xticks([0.2, 0.5, 1, 2, 5, 10])
ax.set_xticklabels(["$0.20", "$0.50", "$1", "$2", "$5", "$10"])
ax.set_xlabel("Blended cost per 1M tokens  (log scale)  —  vendor pricing, "
              "26 Aug 2026", fontsize=11)
ax.set_ylabel("Artificial Analysis Intelligence Index v4.1.1", fontsize=11)
ax.set_title("More intelligence is cheap. The top of the range is not.\n"
             "The nearest thing to a frontier open model carries a licence "
             "condition;\nthe unconditionally free ones are a tier down.",
             fontsize=13.5, loc="left", pad=14)

ax.grid(True, which="both", alpha=0.18, linewidth=0.7)
ax.set_axisbelow(True)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)

handles = [
    plt.Line2D([], [], marker="o", ls="", markersize=11,
               markerfacecolor=C_PROP, markeredgecolor=C_PROP,
               label="Proprietary"),
    plt.Line2D([], [], marker="o", ls="", markersize=11,
               markerfacecolor=C_GATE, markeredgecolor=C_GATE,
               label="Weights downloadable, licence has a revenue trigger"),
    plt.Line2D([], [], marker="o", ls="", markersize=11,
               markerfacecolor=C_OPEN, markeredgecolor=C_OPEN,
               label="Open source (MIT / Apache-2.0)"),
    plt.Line2D([], [], marker="o", ls="", markersize=11,
               markerfacecolor="none", markeredgecolor="#555",
               label="Blended price derived from vendor rates"),
]
ax.legend(handles=handles, loc="lower right", frameon=False, fontsize=9.6)

fig.text(0.008, 0.012,
         "Index: Artificial Analysis Intelligence Index v4.1.1, fetched 26 Aug 2026 "
         "(no last-updated date published).  Price: each vendor's own pricing page, same date.\n"
         "Blended = 0.7x cached + 0.2x input + 0.1x output — derived here, and verified to "
         "reproduce AA's own published figures for Sol, Opus 5 and Kimi K3 exactly.\n"
         "Claude 4.7+ models emit ~30% more tokens for the same text, so the Claude points "
         "understate real per-task cost. Hatched marker = lower-confidence index.",
         fontsize=8.2, color="#555", linespacing=1.5)

fig.tight_layout(rect=(0, 0.085, 1, 1))
fig.savefig(OUT, dpi=170)
print("wrote", os.path.normpath(OUT))

CLASS_LABEL = {"prop": "proprietary",
               "gated": "open weights, revenue trigger",
               "open": "open source"}

print("\nblended price check (vendor rates):")
for name, idx, cached, inp, out, cls, derived, note in ROWS:
    print(f"  {name:22} index {idx}   ${blended(cached, inp, out):6.3f}"
          f"   {CLASS_LABEL[cls]}")
