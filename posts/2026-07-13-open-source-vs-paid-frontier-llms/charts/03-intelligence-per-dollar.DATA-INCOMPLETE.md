# 03-intelligence-per-dollar.png — data incomplete

Chart described (alt text): "Horizontal bar chart of intelligence index
divided by output price. DeepSeek V4 Pro leads at 12.7, Claude Fable 5 trails
at 1.2 — roughly a tenfold spread."

This is presented as a chart of all (or most of) the post's ten models, but
the post's text only gives an index-points-per-dollar value, directly or by
computation, for three of them. No generator was written for the full
ranking because seven of the ten values would have to be invented.

## Recoverable from the post's own text (index.html)

| Model | Index points per $ (output) | Source |
|---|---|---|
| DeepSeek V4 Pro | 12.7 | body: "DeepSeek V4 Pro returns about 12.7 index points per dollar" (stated directly) |
| Claude Fable 5 | 1.2 | body: "Claude Fable 5 returns 1.2" (stated directly) |
| GLM-5.2 | ~11.6 (derived) | computed as index / price = 51.1 / 4.40, using two numbers both explicitly stated elsewhere in this same post ("GLM-5.2 scores 51.1 ... at roughly $4.40 per million output tokens") — not a new invented figure, just the same division the chart's own alt text describes |

## Missing entirely (would require a number not stated in this post)

- GPT-5.6 Sol, GPT-5.6 Terra, GPT-5.6 Luna — index scores are given elsewhere
  in the post (58.9 / not given / 51.2) but none of the three has an output
  price stated in this post, so the ratio can't be computed without guessing
- Claude Opus 4.8 — neither index nor price given in this post
- Grok 4.5 — price given ($6 output) but index not given in this post
- Kimi K2.6, Qwen3.5 — neither index nor price given in this post

## Gap for a human to fill

Output price and/or index score for GPT-5.6 Sol, GPT-5.6 Terra, GPT-5.6
Luna, Claude Opus 4.8, Grok 4.5, Kimi K2.6, and Qwen3.5 — from the post's own
cited sources (Artificial Analysis, BenchLM, DeepInfra, Price Per Token).
