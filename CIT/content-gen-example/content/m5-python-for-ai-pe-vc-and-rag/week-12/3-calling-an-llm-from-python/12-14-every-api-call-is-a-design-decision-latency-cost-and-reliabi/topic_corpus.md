---
topic_id: "12.14"
title: "Every API call is a design decision — latency, cost, and reliability considered upfront"
position_in_module: 6
generated_at: "2026-06-15T00:00:00Z"
resource_count: 2
---

# 1. Every API Call Is a Design Decision — Latency, Cost, and Reliability Considered Upfront — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **12.11** — Making the first API call: `client.messages.create()`, the response object, `message.usage` (token counts), `model` parameter
- **12.13** — Handling API errors: retries, `RateLimitError`, `APIConnectionError`, the concept of transient vs. permanent failure

Additional concepts used without re-definition: variables, functions, for loops, `print()`, `time.sleep()`, `try/except`, API, client, server, request, response, tokens, `max_tokens`, `AnthropicClient`.

---

## 3. Learning Objectives

By the end of this topic, learners will be able to:

1. **Define** latency in the context of an API call and explain what controls it.
2. **Calculate** the approximate cost of a single API call given input and output token counts and per-token prices.
3. **Describe** three dimensions of reliability — retries, error handling, and rate limits — and explain how they connect to topics already covered (12.13).
4. **Compare** the Haiku, Sonnet, and Opus model tiers on speed, cost, and capability, and select the appropriate tier for a given task.
5. **Apply** the three-question design checklist before writing an API call.
6. **Write** a cost-and-latency note suitable for a lab submission (Assessment A4).

---

## 4. Introduction

You have now written a working API call, parsed the response, and added error handling. Every one of those calls to `client.messages.create()` costs money, takes time, and might fail. So far you have been making those calls to learn the mechanics. From this point forward, every call you write is a decision.

Imagine you are building a tool that helps a doctor summarise patient notes. The tool needs to respond before the doctor finishes reaching for the keyboard — roughly two seconds. It also needs to handle hundreds of patients per day without running up a bill that makes the whole project uneconomical. And it needs to keep working even when Anthropic's servers are momentarily slow.

None of those requirements come from the code you already know. They come from asking three questions before you write a single line:

1. Does this task actually need an API call, or can I use a simpler approach?
2. How many calls will this feature make, and under what conditions?
3. Which model — and which model tier — is the right fit for this task?

This topic teaches you to ask those questions and to quantify the answers. It also teaches you how to document your choices in the cost-and-latency note required for your A4 portfolio submission.

---

## 5. Core Concepts

### 5.1 Latency — Time from Call to First Reply Token

**Latency** is the amount of time that passes between when your code sends a request and when the first part of the response arrives. For a `client.messages.create()` call, latency includes:

- **Network transit time** — the milliseconds it takes your request to travel to Anthropic's servers and the response to travel back. This depends on your internet connection and how close Anthropic's data center is to you.
- **Queue time** — if many users are sending requests simultaneously, Anthropic's servers may need to queue yours for a moment before processing it.
- **Model processing time** — the time Claude takes to generate the response. Larger models (more parameters, more capability) take longer per token. Smaller models are faster.

Independent benchmarking data shows that Claude Haiku (the smallest/fastest model tier) achieves roughly 3–4× lower latency than Opus (the largest/slowest tier) on the same prompt [1]. In practice, a Haiku call on a short prompt can return in under one second; an Opus call on a long prompt can take fifteen seconds or more [1].

**Why latency matters for your code:** A script that processes one question interactively must feel fast to the user. A batch job that processes ten thousand questions overnight can tolerate high per-call latency. Knowing your latency tolerance before you choose a model is essential.

**Measuring latency in Python:** The simplest measurement uses `time.time()` — a function that returns the current time as a decimal number of seconds since a fixed reference point.

```python
import time

start = time.time()
message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=256,
    messages=[{"role": "user", "content": "Summarise this in one sentence: ..."}]
)
elapsed = time.time() - start
print(f"Latency: {elapsed:.2f} seconds")
```

`elapsed` is how many seconds the call took. You will use this pattern in the lab note in §6.

---

### 5.2 Cost — Input Tokens × Price + Output Tokens × Price

Every Claude API call has a cost made up of two components:

**Cost = (input_tokens × input_price) + (output_tokens × output_price)**

**Tokens** are the units Anthropic uses to measure text. Roughly speaking, one token is four characters of English text, or about three-quarters of a word. A sentence like "What is the capital of France?" is approximately nine tokens. A 500-word document is roughly 700 tokens [2].

**Where the token counts come from:** The response object returned by `client.messages.create()` carries usage data. You already saw `message.usage` in topic 12.11. It exposes:

- `message.usage.input_tokens` — tokens in your system prompt plus user messages
- `message.usage.output_tokens` — tokens in Claude's reply

**Current pricing across model tiers** (always verify against official Anthropic documentation — prices change):

| Model tier | Input price (per 1M tokens) | Output price (per 1M tokens) |
|---|---|---|
| Claude Haiku | ~$0.25 | ~$1.25 |
| Claude Sonnet | ~$3.00 | ~$15.00 |
| Claude Opus | ~$15.00 | ~$75.00 |

These figures are approximate and sourced from published pricing data [2]. Output tokens cost more than input tokens because generating text is computationally heavier than reading it.

**A worked example:** Suppose your lab sends a 200-token system prompt plus a 50-token user message (250 input tokens total) and Claude replies with 150 output tokens.

- Haiku cost: (250 × $0.25/1M) + (150 × $1.25/1M) = $0.0000625 + $0.0001875 = **$0.00025** per call
- Sonnet cost: (250 × $3.00/1M) + (150 × $15.00/1M) = $0.00075 + $0.00225 = **$0.003** per call
- Opus cost: (250 × $15.00/1M) + (150 × $75.00/1M) = $0.00375 + $0.01125 = **$0.015** per call

At these token counts, Opus is sixty times more expensive per call than Haiku [1][2].

**Scaling matters:** If your lab calls the API five times (as the lab asks), the absolute cost is tiny for any tier. But a production feature that calls the API ten thousand times per day scales those per-call costs by 10,000. A feature that costs $2.50/day on Haiku would cost $150/day on Opus — the same code, the same output, but sixty times the bill [1][2].

**Two features that reduce cost (names only — beyond this topic):** Anthropic offers a batch API for non-real-time workloads (lower per-token prices) and a prompt caching feature (discounts repeated context). These are mentioned here so you know they exist; they are not in scope for this module.

---

### 5.3 Reliability — Retries, Error Handling, and Rate Limits

Reliability means your code keeps working correctly over many calls, not just the first one.

You already have the full toolkit from topic 12.13:

- **Error handling with `try/except`** — catching `AuthenticationError`, `RateLimitError`, `BadRequestError`, `APIConnectionError`
- **Retry logic with `time.sleep()`** — waiting before re-attempting a `RateLimitError`
- **Fail-loudly discipline** — re-raising exceptions you cannot handle rather than silently returning `None`

Reliability in the design-decision sense means asking, before you write the call, *how often will this fail and what should my code do about it?*

For a lab script that runs five calls interactively, a `RateLimitError` is unlikely and a simple `try/except` that prints a message is sufficient. For a production loop that runs thousands of calls, you need the full retry loop from 12.13 and you need to monitor failure rates over time [1].

**Rate limits** are per-account caps on requests per minute (RPM) and tokens per minute (TPM) [1][2]. Free-tier accounts have lower limits than paid accounts. Hitting a rate limit is not a bug — it is a signal that your call volume exceeds your account tier. The design decision is whether to slow down the caller, upgrade the account tier, or redesign the feature to use fewer calls.

This section is deliberately brief — topic 12.13 covers the mechanics. The new idea here is that reliability is a *design question you ask before you build*, not just a bug-fix you add after a crash [1].

---

### 5.4 Model Selection — Haiku, Sonnet, and Opus

Anthropic publishes three main model tiers, named after literary forms, reflecting increasing capability and cost [1][2].

**Claude Haiku** — the smallest, fastest, and cheapest tier.
- Best for: classification, short-answer extraction, simple Q&A, tasks where the output is a few sentences.
- Typical latency: under one second on short prompts [1].
- Cost: approximately $0.25 / $1.25 per million input/output tokens [2].
- Trade-off: lower performance on tasks requiring complex reasoning, nuanced writing, or long-form synthesis.

**Claude Sonnet** — the balanced middle tier.
- Best for: multi-step reasoning, summaries of medium-length documents, coding assistance, most general-purpose tasks.
- Typical latency: a few seconds on medium prompts [1].
- Cost: approximately $3 / $15 per million input/output tokens [2].
- Trade-off: noticeably more capable than Haiku for complex tasks; noticeably cheaper than Opus; the right default for most applications.

**Claude Opus** — the largest and most capable tier.
- Best for: difficult reasoning, nuanced analysis, long documents requiring deep comprehension, tasks where quality matters more than speed or cost.
- Typical latency: can exceed ten seconds on long prompts [1].
- Cost: approximately $15 / $75 per million input/output tokens [2].
- Trade-off: genuinely better on hard tasks but sixty times more expensive than Haiku. Defaulting to Opus "just to be safe" is a common beginner mistake that rapidly depletes free credit.

**The model selection rule of thumb:** Start with the cheapest model that is likely to produce an acceptable answer for your task. Test on Haiku. If the output quality is not good enough, step up to Sonnet. Reserve Opus for tasks where you have tested that Sonnet cannot handle the complexity [1].

This is not a performance claim — it is an economic principle. Using Opus for a task Haiku can do equally well is pure waste. Using Haiku for a task that genuinely requires Opus produces poor output. Neither outcome is acceptable in a professional system.

---

### 5.5 The Three Questions Before Every Call

Every time you write a `client.messages.create()` call, ask these three questions before you commit the code.

**Question 1: Does this task need an API call at all?**

An API call is not always the right tool. If you need to count words, Python's `len()` and `.split()` are free and instant. If you need to check whether a string contains a number, a regular expression is free and instant. AI models are powerful but they cost money, take time, and can produce wrong answers. Reserve them for tasks that genuinely require language understanding — summarisation, reasoning, generation, classification where the categories are fuzzy [1].

**Question 2: How many calls will this feature make — and under what conditions?**

"My script loops over a list of inputs" can mean five inputs in a lab or fifty thousand inputs in production. Before you build the loop, count the calls. If the count is bounded (your lab has exactly five test inputs), a simple loop is fine. If the count is unbounded (process every row in a growing database), you need to think about rate limits, batching, and cost ceilings before writing the loop [1][2].

**Question 3: Which model tier fits this task?**

Use the Haiku/Sonnet/Opus framework from §5.4. Concretely:
- Can a brief, factual answer satisfy the user? → Haiku
- Does the task require reasoning over several paragraphs or generating multiple coherent sentences? → Sonnet
- Is the task long-document analysis or complex multi-step reasoning where quality is the primary constraint? → Opus

Document your choice in your code comment or lab note (see §6). "I chose Haiku because the output is a one-sentence classification and latency is the dominant constraint" is a professional engineering note [1][2].

---

## 6. Implementation

### Adding a Cost-and-Latency Note to Your Lab Code

The lab for this week asks you to write a cost-and-latency note alongside your API calls. Here is the pattern.

**Step 1: Measure latency with `time.time()`**

```python
import anthropic
import time

client = anthropic.Anthropic()

def call_and_measure(prompt, model="claude-haiku-4-5"):
    """
    Call the API, return the reply text, and print latency + cost.
    """
    start = time.time()

    message = client.messages.create(
        model=model,
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}]
    )

    elapsed = time.time() - start
    reply_text = message.content[0].text

    # Token counts from the response object (covered in 12.11)
    input_tokens = message.usage.input_tokens
    output_tokens = message.usage.output_tokens

    # Approximate prices for claude-haiku ($ per token)
    # Source: Anthropic pricing page — verify before use
    INPUT_PRICE_PER_TOKEN  = 0.25 / 1_000_000   # $0.25 per million
    OUTPUT_PRICE_PER_TOKEN = 1.25 / 1_000_000   # $1.25 per million

    cost = (input_tokens * INPUT_PRICE_PER_TOKEN) + (output_tokens * OUTPUT_PRICE_PER_TOKEN)

    print(f"--- Cost & Latency Note ---")
    print(f"Model:          {model}")
    print(f"Latency:        {elapsed:.2f}s")
    print(f"Input tokens:   {input_tokens}")
    print(f"Output tokens:  {output_tokens}")
    print(f"Estimated cost: ${cost:.6f}")
    print(f"--------------------------")

    return reply_text
```

**Step 2: Call it on your five domain-relevant inputs**

```python
test_inputs = [
    "Classify this claim as fact or opinion: 'Python is the most popular AI language.'",
    "Summarise this sentence in five words: 'Machine learning finds patterns in data.'",
    "Is this question answerable from the text? Question: 'What year was Python created?'",
    "Translate this phrase to plain English: 'stochastic gradient descent'",
    "Rate the complexity of this prompt from 1-5: 'Explain neural networks to a 10-year-old.'"
]

for prompt in test_inputs:
    reply = call_and_measure(prompt)
    print(f"Reply: {reply}\n")
```

**Step 3: Write the note in your lab submission**

After running the calls, copy the printed output into a Markdown cell in your Colab notebook. Then add one sentence explaining your model choice:

> "I chose claude-haiku-4-5 for all five test calls because each task requires a short classification or one-sentence reply where Haiku's speed and cost efficiency dominate. Total estimated cost for five calls: $0.000XX. Average latency: X.XXs."

That is the cost-and-latency note format expected in A4.

---

## 7. Real-World Patterns

**Pattern 1: Test with the cheapest model first.**

In professional AI development teams, new features are prototyped on the cheapest model available and promoted to a more capable model only if quality testing reveals a gap [1]. The cheapest model almost always produces acceptable results for simple extraction or classification tasks. Testing on Opus first and then trying to cut costs later is backward — you may have already shaped your prompts around Opus's capabilities and find that Haiku fails for reasons unrelated to model tier.

The lab exercise deliberately asks you to run five test inputs and observe the output. That observation is the quality gate. If the output is correct and coherent, you have evidence that the cheaper model is sufficient.

**Pattern 2: Count calls before you build.**

A common beginner mistake is to build a loop, run it, and then discover the cost. Before writing any loop that calls the API, answer: "If this runs on the full dataset, how many calls is that?" Write down the number. Calculate the cost at Haiku prices. If that number is already large, think about whether you can batch, cache, or filter inputs to reduce it [1][2].

For your lab, the dataset is five inputs and the cost is negligible. The habit of counting still matters — you are forming the instinct you will need when the dataset is fifty thousand rows.

---

## 8. Best Practices

- **Never default to Opus.** Unless you have tested that Haiku and Sonnet produce unacceptably poor output for your task, Opus is the wrong starting point. Start cheap, escalate only when quality evidence demands it [1][2].

- **Log token counts and latency on every call during development.** You cannot optimise what you cannot measure. The `message.usage` object is always available — use it. Even a `print()` statement is better than guessing [1].

- **Set `max_tokens` deliberately, not arbitrarily.** A `max_tokens=1024` ceiling on a task that needs a three-sentence answer wastes nothing, but a `max_tokens=4096` ceiling on the same task invites the model to pad its answer. Shorter output means lower cost and lower latency [2].

- **Put the model name in a variable, not a string literal.** If the model name appears in twenty places in your code, changing it requires twenty edits. Use `MODEL = "claude-haiku-4-5"` at the top of the file and reference `MODEL` everywhere. When you want to test Sonnet, one line changes [1].

- **Never embed per-token prices as magic numbers.** Prices change. Put them in named constants (`INPUT_PRICE_PER_TOKEN = 0.25 / 1_000_000`) with a comment linking to the source. When prices change, one update covers all your calculations [2].

- **Reliability is not optional for production.** A script that crashes on the first rate-limit error is a prototype, not a product. The error-handling patterns from 12.13 are a prerequisite, not an advanced feature.

---

## 9. Hands-On Exercise

**Exercise: Run five domain-relevant inputs and write the cost-and-latency note**

1. Copy the `call_and_measure()` function from §6 into a new Colab notebook cell.
2. Replace the `test_inputs` list with five prompts relevant to your chosen domain (for example, healthcare, education, or finance — any domain you used earlier in the lab).
3. Run all five calls with `model="claude-haiku-4-5"`.
4. Copy the printed output into a Markdown cell.
5. Add a sentence explaining why you chose Haiku for these tasks.
6. (Optional) Re-run the same five inputs with `model="claude-sonnet-4-5"` and compare the latency and cost printout. Note whether the output quality is meaningfully different.

Expected outcome: a Colab notebook with code, printed cost-and-latency data, and a two-to-three sentence written note — exactly what Assessment A4 requires.

---

## 10. Key Takeaways

- Every API call has three measurable properties: **latency** (time to first reply), **cost** (input tokens × price + output tokens × price), and **reliability** (how often it succeeds and what happens when it does not). All three should be considered before writing the call [1][2].
- The three model tiers — **Haiku** (fast/cheap), **Sonnet** (balanced), **Opus** (capable/expensive) — differ by roughly 10–60× in cost. Choosing the wrong tier is the single largest source of avoidable cost in beginner AI projects [1][2].
- The **three questions** before every call: (1) Does this need a call at all? (2) How many calls will this make at scale? (3) Which model tier fits the task? Asking them upfront prevents expensive surprises [1].
- A **cost-and-latency note** documents the model chosen, the token counts, the measured latency, and the reasoning. It is a standard professional deliverable and is required in Assessment A4.
- **Start cheap, escalate on evidence.** Test on Haiku, step up to Sonnet only if quality fails, and reserve Opus for tasks where you have proven that Sonnet is insufficient [1][2].

---

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
