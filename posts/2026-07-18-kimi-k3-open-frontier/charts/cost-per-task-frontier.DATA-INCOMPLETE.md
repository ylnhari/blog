# cost-per-task-frontier.jpg — data incomplete

Chart described (alt text): "Scatter of 19 frontier models by intelligence
index versus cost per Intelligence Index task. Kimi K3 (open weight) sits on
the efficient frontier at index 57.1 and $0.94 per task, between GPT-5.6
Terra and GPT-5.6 Sol. Cheap open models like DeepSeek V4 Pro, GLM-5.2 and
Kimi K2.6 cluster at the low-cost left; the paid flagships Fable 5, Sol and
Opus 4.8 hold the top right."

The post (posts/2026-07-18-kimi-k3-open-frontier/index.html) names or implies
19 models on this chart but states a full (index, cost-per-task) coordinate
pair, in its own text, for only three of them, plus one more derivable by
simple subtraction. No generator was written for the 19-point scatter because
the other ~15 points have no numbers in this post at all and would have to be
invented.

## Recoverable as full (index, cost) pairs from the post's own text

| Model | AA Intelligence Index | Cost per Intelligence Index task | Source |
|---|---|---|---|
| Kimi K3 | 57.1 | $0.94 | body: "Kimi K3 scores 57.1"; "K3 comes in at $0.94 per task" |
| GPT-5.6 Sol | 58.9 | $1.04 | body: "behind only Claude Fable 5 (59.9) and GPT-5.6 Sol (58.9)"; sources list: "$1.04 Sol" |
| Claude Opus 4.8 | 55.7 | $1.80 | body: "It sits above Claude Opus 4.8 (55.7)"; sources list: "$1.80 Opus 4.8" |
| Kimi K2.6 | 44.1 (derived) | $0.33 | cost stated directly in sources list ("$0.33 K2.6"); index derived as K3's 57.1 minus the post's own stated "13-point gain over Kimi K2.6" (57.1 − 13 = 44.1) — arithmetic on two numbers already in this post, not a new invented figure |

## Recoverable as a single value only (the other axis is not stated in this post)

- Claude Fable 5 — index 59.9 given ("behind only Claude Fable 5 (59.9)"); no
  cost-per-task figure for Fable 5 anywhere in this post (the sources list
  gives costs only for K3, Opus 4.8, Sol, K2.6, and Grok 4.5)
- Grok 4.5 — cost $0.31 given (sources list: "$0.31 Grok 4.5"); no index
  score for Grok 4.5 in this post
- GPT-5.6 Terra — mentioned only as the point K3 sits next to ("wedged
  between GPT-5.6 Terra and Sol"); no index or cost number given

## Missing entirely (named only as part of a cluster, no numbers)

DeepSeek V4 Pro, GLM-5.2, MiniMax-M3, and roughly a dozen further unnamed
models implied by "19 frontier models" — the post describes them only
collectively ("cheap open models ... cluster at the low-cost left") with no
per-model figures.

## Note on a possible source for the rest

The post's own Sources section says the map's "data and the chart code live
in" `posts/2026-07-13-open-source-vs-paid-frontier-llms/interactive.html`.
That file does contain a full 19-model dataset (a `MODELS` array with `idx`
and `task` per model) which would plot this exact chart. It was deliberately
NOT copied into a generator here: per this backfill's rule ("use only
numbers that already appear in the post's own HTML"), the interactive.html
values were authored/updated for that companion post and don't all match
this post's own stated figures one-for-one (e.g. that file's Claude Fable 5
index is 59.9, matching this post's 59.9 — but this post gives no cost
figure for Fable 5 at all, and other pairings would need independent
verification against this post's own text before being trusted here). A
human filling this gap should pull from that array but re-verify each value
against a primary source first, per the same primary-source rule.
