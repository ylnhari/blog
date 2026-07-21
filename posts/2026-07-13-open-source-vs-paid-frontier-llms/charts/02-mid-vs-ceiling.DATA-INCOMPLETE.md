# 02-mid-vs-ceiling.png — data incomplete

Chart described (alt text): "Horizontal bar chart of AA Intelligence Index
for all ten models, colored by open versus paid. Open weights top out around
index 51 while paid models extend to 60."

The post's ten models are: Claude Opus 4.8, Claude Fable 5, GPT-5.6 Sol,
GPT-5.6 Terra, GPT-5.6 Luna, Grok 4.5, DeepSeek V4 Pro, GLM-5.2, Kimi K2.6,
Qwen3.5. Only four of the ten get an exact index score in this post's text;
three more are placed in a named band without an exact number; three have no
number or band at all. No generator was written because a ten-bar chart with
six bars missing or approximate would misrepresent the post's own numbers.

## Recoverable exact scores (index.html body)

| Model | AA Intelligence Index |
|---|---|
| Claude Fable 5 | 60 |
| GPT-5.6 Sol | 58.9 |
| GPT-5.6 Luna | 51.2 |
| GLM-5.2 | 51.1 |

## Recoverable only as a band (post names the range, not the exact score)

- "There is a band from roughly index 51 to 55 — GPT-5.6 Luna, GLM-5.2, Grok
  4.5, GPT-5.6 Terra — where open and paid models are genuinely
  interchangeable." → Grok 4.5 and GPT-5.6 Terra are placed in [51, 55] but
  given no exact figure.
- "Above that band, from 56 to 60 ... Claude Opus 4.8, GPT-5.6 Sol, and
  Claude Fable 5." → Claude Opus 4.8 is placed in [56, 60] but given no exact
  figure.

## Missing entirely (no number or band given)

- DeepSeek V4 Pro (only its SWE-bench Verified score, ~80.6%, appears
  elsewhere in the post — a different benchmark, not the Intelligence Index)
- Kimi K2.6
- Qwen3.5

## Gap for a human to fill

Exact Intelligence Index scores for Claude Opus 4.8, GPT-5.6 Terra, Grok 4.5,
DeepSeek V4 Pro, Kimi K2.6, and Qwen3.5 — from the post's own cited source,
BenchLM's Artificial Analysis Intelligence Index leaderboard.
