# 01-price-intelligence-frontier.png — data incomplete

Chart described (alt text): "Scatter plot of Artificial Analysis Intelligence
Index against output price on a log scale. Open-weight models (orange)
cluster in the cheap region up to index ~51; paid models (blue) extend up to
index 60 at much higher prices. GLM-5.2 sits at the same intelligence as
GPT-5.6 Luna for less money."

The post names ten models up front (Claude Opus 4.8, Claude Fable 5, OpenAI's
GPT-5.6 family [Sol/Terra/Luna], xAI's Grok 4.5, DeepSeek V4 Pro, GLM-5.2,
Kimi K2.6, Qwen3.5) but only states a full (price, index) coordinate pair for
one of them. The rest are missing one or both axes. No generator was written
because plotting the majority of points would mean inventing coordinates.

## Recoverable from the post's own text (index.html)

| Model | AA Intelligence Index | Output price ($/M) | Source |
|---|---|---|---|
| GLM-5.2 | 51.1 | ~$4.40 | body: "GLM-5.2 scores 51.1 on the index at roughly $4.40 per million output tokens" |
| Claude Fable 5 | 60 | $50 (derived) | index stated in body ("Claude Fable 5 at 60"); price derived by dividing the two numbers explicitly given elsewhere in the SAME post for Fable 5's index-points-per-dollar (60 / 1.2 = 50) — see chart 03's "Claude Fable 5 returns 1.2" — not a new invented figure, just arithmetic on two already-stated post numbers |
| GPT-5.6 Sol | 58.9 | not stated | body: "GPT-5.6 Sol at 58.9" |
| GPT-5.6 Luna | 51.2 | not stated | body: "GPT-5.6 Luna's 51.2" |
| Grok 4.5 | not stated | $6 output ($2 input) | body: "Grok 4.5 is priced at $2 input / $6 output" |
| DeepSeek V4 Pro | not stated | not stated | only "12.7 index points per dollar" given (chart 03), which needs either the index or the price to resolve into a coordinate — neither given alone in this post |

## Missing entirely (no numeric value anywhere in this post)

- Claude Opus 4.8 — named in the intro, never given an index score or price here
- GPT-5.6 Terra — never given an index score or price here
- Kimi K2.6 — never given an index score or price here
- Qwen3.5 — never given an index score or price here

## Gap for a human to fill

Pricing and/or index scores for Claude Opus 4.8, GPT-5.6 Terra, GPT-5.6 Sol,
GPT-5.6 Luna, Grok 4.5, DeepSeek V4 Pro, Kimi K2.6, and Qwen3.5 — pull from
the post's own "Sources & caveats" links (Artificial Analysis / BenchLM /
DeepInfra / Price Per Token) and re-verify against those primary sources
before hard-coding into a generator.
