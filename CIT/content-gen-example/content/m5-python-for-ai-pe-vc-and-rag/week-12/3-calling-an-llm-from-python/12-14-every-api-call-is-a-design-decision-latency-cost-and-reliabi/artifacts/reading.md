<!-- nav:top:start -->
[⬅ Previous: 12.13 — Handling API errors](../../12-13-handling-api-errors-what-to-do-when-the-call-fails/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 13.1 — System prompt vs user prompt ➡](../../../../week-13/1-prompt-engineering-fundamentals/13-1-system-prompt-vs-user-prompt-context-setting-vs-the-live-req/artifacts/reading.md)
<!-- nav:top:end -->

---

# Every API Call Is a Design Decision — Latency, Cost, and Reliability Considered Upfront

## Overview

Every time your Python code calls `client.messages.create()`, three things happen: time passes, money is spent, and something can go wrong. Most beginners focus only on getting a reply — but professional developers ask three questions *before* they write the call: Does this task need an API call at all? How many calls will it make? Which model tier fits the job? This topic teaches you to ask those questions and to quantify the answers.

## Key Concepts

### Latency — How Long You Wait

**Latency** is the time between sending a request and receiving the first part of the reply. Three things control it:

- **Network transit time** — milliseconds for your request to travel to Anthropic's servers and back.
- **Queue time** — if many users are sending requests simultaneously, yours is held briefly before processing.
- **Model processing time** — larger, more capable models generate each token more slowly.

Independent benchmarking shows Claude Haiku achieves roughly 3–4× lower latency than Opus on the same prompt [1]. A short Haiku call can return in under one second; a long Opus call can take fifteen seconds or more [1].

### Cost — Tokens In, Tokens Out

Every call is billed on **tokens** — the small chunks Anthropic uses to measure text. One token is roughly four characters of English. You already know where token counts live: `message.usage.input_tokens` and `message.usage.output_tokens` from topic 12.11.

The cost formula is:

**Cost = (input tokens × input price) + (output tokens × output price)**

Approximate prices per million tokens across the three model tiers [1][2]:

| Model tier | Input (per 1M tokens) | Output (per 1M tokens) |
|---|---|---|
| Claude Haiku | ~$0.25 | ~$1.25 |
| Claude Sonnet | ~$3.00 | ~$15.00 |
| Claude Opus | ~$15.00 | ~$75.00 |

> Always verify against the official Anthropic pricing page — rates change.

Scaling is where cost bites: a feature costing $2.50/day on Haiku costs $150/day on Opus — same code, same output, sixty times the bill [1][2].

### Reliability — Designing for Failure

You already have the toolkit from topic 12.13: `try/except`, retry logic with `time.sleep()`, and fail-loudly discipline. The new idea here is to ask the reliability question *before* you write the call. **Rate limits** are per-account caps on requests and tokens per minute [1][2]. Hitting one is not a bug — it is a signal your call volume exceeds your account tier. Decide upfront whether to slow down, upgrade, or redesign.

### Model Selection — Haiku, Sonnet, Opus

Anthropic's three tiers reflect increasing capability and cost [1][2]:

- **Claude Haiku** — fastest and cheapest. Best for classification, short-answer extraction, one-sentence outputs. Latency typically under one second [1].
- **Claude Sonnet** — balanced middle tier. Best for multi-step reasoning, medium-length summaries, most general-purpose tasks. Latency a few seconds [1].
- **Claude Opus** — most capable, most expensive. Best for long-document analysis and complex reasoning where quality is the primary constraint. Latency can exceed ten seconds [1].

**Rule of thumb:** Start on Haiku. Step up to Sonnet only if quality fails. Reserve Opus for tasks where Sonnet has been tested and found insufficient [1]. Defaulting to Opus "just to be safe" is the most common beginner mistake — it depletes free credit fast.

### The Three Questions Before Every Call

1. **Does this task need a call at all?** Counting words or formatting a date are free in Python. Reserve AI for tasks that genuinely require language understanding — summarisation, reasoning, fuzzy classification [1].
2. **How many calls will this make — and under what conditions?** Count them before building the loop. Calculate the cost at Haiku prices. If the count is unbounded, plan for rate limits and cost ceilings [1][2].
3. **Which model tier fits?** Brief factual answer → Haiku. Reasoning over several paragraphs → Sonnet. Long-document analysis where quality dominates → Opus [1][2].

## Worked Example

The function below measures latency and calculates cost for every call.

```python
import anthropic, time

client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"                     # one variable, easy to swap

INPUT_PRICE_PER_TOKEN  = 0.25 / 1_000_000      # $0.25 per million — update when rates change
OUTPUT_PRICE_PER_TOKEN = 1.25 / 1_000_000      # $1.25 per million

def call_and_measure(prompt):
    start   = time.time()
    message = client.messages.create(
        model=MODEL, max_tokens=256,
        messages=[{"role": "user", "content": prompt}]
    )
    elapsed = time.time() - start

    inp  = message.usage.input_tokens
    out  = message.usage.output_tokens
    cost = (inp * INPUT_PRICE_PER_TOKEN) + (out * OUTPUT_PRICE_PER_TOKEN)

    print(f"Model: {MODEL} | Latency: {elapsed:.2f}s | "
          f"Tokens in/out: {inp}/{out} | Cost: ${cost:.6f}")
    return message.content[0].text
```

Step by step:

1. `time.time()` records the clock the moment the request leaves your code.
2. `client.messages.create()` sends the request and waits for a reply.
3. `time.time() - start` gives elapsed seconds — your latency measurement.
4. `message.usage` provides the exact token counts the API recorded.
5. The cost formula multiplies each count by its per-token price and sums them.

Run this on five test inputs and paste the printed output into your lab notebook. Add one sentence explaining your model choice — for example: *"I chose Haiku because each task requires a short classification where speed and cost efficiency dominate."*

## In Practice

- **Test on the cheapest model first.** Prototype on Haiku; promote to Sonnet only when a quality gap appears in testing [1].
- **Count calls before building loops.** Before writing any loop, answer: "If this runs on the full dataset, how many calls is that?" Calculate the cost at Haiku prices. The habit matters when the dataset is fifty thousand rows [1][2].
- **Set `max_tokens` deliberately.** A large ceiling on a task that needs three sentences invites padding and raises cost [2].
- **Put the model name in a variable.** One constant at the top of the file means one edit to switch tiers across the whole script [1].
- **Log token counts and latency during development.** `message.usage` is always available — even a `print()` is better than guessing [1].

## Key Takeaways

- Every `client.messages.create()` call has three measurable properties: **latency**, **cost**, and **reliability** — all three should be considered before writing the call [1][2].
- The three model tiers — Haiku, Sonnet, Opus — differ by roughly 10–60× in cost. Choosing the wrong tier is the largest source of avoidable cost in beginner AI projects [1][2].
- Ask the **three questions** before every call: Does this need a call? How many calls at scale? Which model tier fits? [1]
- **Start cheap, escalate on evidence:** Haiku first, Sonnet if quality fails, Opus only when Sonnet is proven insufficient [1][2].
- A cost-and-latency note — model chosen, token counts, measured latency, and your reasoning — is a standard professional deliverable.

## References

[1] Artificial Analysis. "Anthropic Provider — Latency, Throughput & Cost Data." *Artificial Analysis*. https://artificialanalysis.ai/providers/anthropic

[2] Finout. "Anthropic API Pricing Breakdown." *Finout Blog*. https://www.finout.io/blog/anthropic-api-pricing

---
<!-- nav:bottom:start -->
[⬅ Previous: 12.13 — Handling API errors](../../12-13-handling-api-errors-what-to-do-when-the-call-fails/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 13.1 — System prompt vs user prompt ➡](../../../../week-13/1-prompt-engineering-fundamentals/13-1-system-prompt-vs-user-prompt-context-setting-vs-the-live-req/artifacts/reading.md)
<!-- nav:bottom:end -->
