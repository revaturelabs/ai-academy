---
topic_id: "3.6"
title: "Temperature and sampling — why the same question gives different answers"
position_in_module: 3
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. Temperature and Sampling — Why the Same Question Gives Different Answers — Topic Corpus

## 2. Prerequisites

This topic builds directly on two earlier topics:

- **3.2 — Large Language Models, prompts, and hallucination.** You need to know what an LLM (Large Language Model) is, what a prompt is, and what hallucination means.
- **3.4 — Tokens, tokenisation, next-token prediction, and autoregressive decoding.** This topic assumes you understand that an LLM generates text one token at a time, and that each new token is chosen based on what came before.

If either of those topics is not fresh in your mind, review them before continuing.

## 3. Learning Objectives

By the end of this topic, you should be able to:

1. **Explain** what a probability distribution over tokens is and how an LLM uses one at each generation step.
2. **Describe** what temperature is and how changing it makes an LLM's output more predictable or more varied.
3. **Distinguish** between greedy decoding, top-k sampling, and top-p (nucleus) sampling, and give one use case for each.
4. **Select** an appropriate temperature setting for a given task (factual lookup vs. creative writing vs. conversational assistant).
5. **Explain** why sending the exact same prompt twice can produce two different responses, and why that is a feature — not a bug — for many use cases.

## 4. Introduction

Have you ever noticed that asking an AI assistant the same question twice gives you slightly different answers each time? Or that one day it sounds confident and direct, and another day it sounds more exploratory? That is not a glitch. It is a deliberate design choice called **sampling**, controlled by a setting called **temperature**.

Understanding temperature and sampling is important for anyone who works with AI systems — whether you are using a chatbot, connecting to an AI through an application programming interface (API, a way for programs to talk to each other), or designing a product that uses AI. It is what separates a system that always prints the same exact response from one that can generate fresh, contextually rich replies every time.

In topic 3.4 you learned that an LLM generates text token by token, always predicting what the next token should be. But the model does not simply pick one guaranteed winner every time. Instead, it calculates a range of candidates — every token in its vocabulary gets a score — and then it samples from those candidates according to a rule you can configure. Temperature is the main dial that controls how that sampling works [1].

By the end of this topic you will be able to explain exactly why the same prompt can produce different outputs, how to make an LLM more or less predictable, and which settings suit which tasks.

## 5. Core Concepts

### 5.1 Probability Distributions Over Tokens

At each step of autoregressive decoding (generating one token at a time, as you learned in topic 3.4), an LLM does not output a single word. It outputs a **probability distribution** — a list that assigns a likelihood score to every token in its vocabulary.

Think of it like a roulette wheel. The wheel has thousands of labelled slots — one slot for "cat", one for "dog", one for "automobile", and so on for every token the model knows. The model sets the sizes of those slots based on context: the tokens that fit the conversation best get bigger slots; unlikely tokens get tiny slivers. The model then spins the wheel and lands on a token.

More precisely, the LLM first computes a raw number called a **logit** for every token. A logit is just a score — a large positive logit means "this token fits well here"; a large negative logit means "this token fits poorly." Logits are then converted into probabilities so that all scores add up to 1. You do not need to know the conversion formula; the key idea is:

- High logit → high probability → bigger slot on the wheel
- Low logit → low probability → tiny slot on the wheel

That wheel-spin is the random step. This is why two identical prompts can produce two different responses: if the wheel is spun twice, it can land on different slots [1].

**Deterministic output** — the system always returns the same answer for the same input, like a calculator. **Stochastic output** (also called probabilistic or random output) — the system may return different answers each time, like a roulette spin. LLMs, by default, are stochastic [2].

### 5.2 Temperature

**Temperature** is a single number — typically set between 0 and 2 — that controls how spread out or how concentrated the probability distribution is before the wheel is spun [1].

Think of temperature like physical heat acting on the probability wheel:

- **Low temperature** (e.g. 0.1 or 0.2) makes the wheel lopsided. The highest-scoring token gets an enormous slot, and all the other tokens get almost nothing. The model almost always picks the top candidate. The output is predictable and consistent.
- **High temperature** (e.g. 1.0 or 1.5) levels out the wheel. Tokens that were decent-but-not-top candidates get meaningfully bigger slots. The model explores a wider range of possibilities. The output is more varied and sometimes surprising.
- **Temperature = 0** is a special case. The model always picks the single highest-scoring token, making the output fully deterministic. This is called greedy decoding and is covered in §5.3.

Here is a concrete example. Suppose the model is completing the phrase "The sky is ___" and the top candidates are:

| Token     | Raw score | Probability at temp 0.2 | Probability at temp 1.0 |
|-----------|-----------|-------------------------|-------------------------|
| "blue"    | highest   | ~95%                    | ~55%                    |
| "clear"   | second    | ~4%                     | ~25%                    |
| "grey"    | third     | ~1%                     | ~15%                    |
| anything else | very low | <0.1%               | ~5%                     |

At temperature 0.2, "blue" wins almost every time. At temperature 1.0, "clear" and "grey" both have a real chance. At temperature 1.5, even rarer tokens might appear [2].

Why does this matter? Because the right level of predictability depends on what you are trying to do. A medical summarisation tool should always say the same thing; a creative-writing assistant should say something new each time.

Temperature works by scaling all logits before converting them to probabilities. Dividing logits by a small number (low temp) makes the gaps between scores larger — the winner dominates. Dividing by a large number (high temp) compresses the gaps — candidates are more equal [1][2]. You do not need to compute this; you just need to understand the directional effect.

### 5.3 Sampling Strategies: Greedy Decoding, Top-k, and Top-p

Even after temperature adjusts the probability distribution, there is still the question of how to pick from it. This is where sampling strategies come in [3].

**Greedy decoding**

**Greedy decoding** means always picking the single highest-probability token at every step — no randomness at all. It is the simplest possible approach.

- Equivalent to setting temperature = 0.
- Produces fully **deterministic** output: the same prompt always gives the same response.
- Advantage: predictable, fast, good for structured outputs (code, data extraction, yes/no answers).
- Disadvantage: tends to be repetitive and safe — the model can get "stuck" repeating the same words or phrases when the top token at each step keeps being the same word [2].

**Top-k sampling**

**Top-k sampling** keeps only the top k highest-probability tokens and sets all others to zero probability before spinning the wheel.

- Example: if k = 50, only the 50 best candidates are eligible; the other tens of thousands of tokens are excluded.
- This prevents the model from accidentally picking a very low-probability, strange token, while still allowing variety among the plausible candidates.
- The limitation: k is a fixed number. If the model is very confident (one token dominates), k = 50 still forces some unnecessary variety. If the model is uncertain (many plausible tokens), k = 50 might be too restrictive [2][3].

**Top-p sampling (nucleus sampling)**

**Top-p sampling** — also called **nucleus sampling** — solves top-k's limitation by selecting candidates dynamically based on cumulative probability.

- You set p as a fraction between 0 and 1 (e.g. p = 0.9).
- The model sorts tokens from highest to lowest probability and adds them up until the cumulative total reaches p.
- Only tokens in that "nucleus" are eligible for selection.
- Why this is smarter than top-k: when the model is confident, the nucleus is small (maybe just 5 tokens reach 90% cumulative probability); when the model is uncertain, the nucleus is large (maybe 200 tokens are needed to reach 90%). The method adapts automatically [2][3].

A practical comparison:

| Strategy        | Randomness | Key control | Best for |
|-----------------|------------|-------------|----------|
| Greedy decoding | None (deterministic) | — | Structured outputs, factual extraction |
| Top-k sampling  | Moderate   | k (integer) | General chat, moderate variety |
| Top-p (nucleus) | Adaptive   | p (0–1)     | Creative tasks, nuanced chat |

In real-world APIs — such as the OpenAI API, Anthropic API, or Ollama (a tool for running LLMs locally) — you can usually set both temperature and top-p as separate parameters. A common convention: if you want to control randomness via top-p, keep temperature at 1.0 and adjust p; if you want to control it via temperature, keep p at 1.0 and adjust temperature [3].

### 5.4 Practical Settings

How do you choose temperature in the real world? The rule of thumb is: match your temperature to how much creativity the task requires [1][2][3].

**Low temperature (0.0 – 0.3) — use when accuracy matters most**

- Factual question answering ("What is the capital of France?")
- Code generation — you want working, predictable logic
- Data extraction — pulling structured information from a document
- Medical, legal, or financial summarisation — accuracy and reproducibility are critical
- Customer support bots that need to give the same correct answer each time

At temperature 0, the model behaves nearly like a look-up table for well-memorised facts. Important caveat: it can still hallucinate (as you learned in topic 3.2) — low temperature reduces variety but does not eliminate errors [2].

**Medium temperature (0.5 – 0.8) — use for balanced tasks**

- Conversational assistants — some variety keeps dialogue feeling natural
- Email drafting — similar structure, slightly different phrasing each time
- Summarisation where a consistent style is wanted but verbatim repetition is undesirable

**High temperature (1.0 – 1.5+) — use when creativity or diversity is the goal**

- Creative writing, poetry, brainstorming
- Generating multiple distinct options for A/B testing (comparing version A to version B)
- Personas or storytelling bots where uniqueness is a feature

Above approximately 1.5, outputs tend to become incoherent — the probability distribution becomes so flat that very unlikely tokens start winning the roulette spin regularly. This is generally not useful [2].

Quick reference table:

| Temperature | Behaviour | Typical use case |
|-------------|-----------|------------------|
| 0           | Fully deterministic (greedy) | Code, data extraction, factual Q&A |
| 0.2 – 0.4   | Very predictable, minor variation | Medical notes, structured summarisation |
| 0.5 – 0.8   | Balanced | Conversational AI, email drafts |
| 1.0         | Default for many systems — noticeable variety | General purpose chat |
| 1.2 – 1.5   | High variety | Creative writing, brainstorming |
| > 1.5       | Often incoherent | Rarely useful |

### 5.5 Limitations and Misconceptions

Even with a solid understanding of temperature and sampling, several important limitations apply.

**Low temperature does not mean high accuracy.** A model set to temperature 0 will always give the same answer — but if that answer is wrong, it will be consistently wrong. Temperature controls consistency, not correctness [2].

**Temperature does not change what the model knows.** Adjusting temperature reshapes how probabilities are sampled; it does not add new knowledge or fix gaps in training data. A model that does not know something at temperature 1.0 also does not know it at temperature 0.

**Sampling randomness is not the same as unpredictability everywhere.** Some variation in LLM outputs comes from sources other than temperature: differences in hardware, batching of requests on a server, or system-level settings. Setting temperature to 0 eliminates sampling randomness but may not eliminate all sources of variation on every platform [1].

**Top-p and temperature can interact in unexpected ways.** Using a high temperature and a high top-p at the same time amplifies variety. Using a low temperature with a narrow top-p aggressively restricts choices. Most practical guidance recommends adjusting one at a time [3].

## 6. Implementation

This section walks through what actually happens inside an LLM at each generation step — not as mathematics, but as a clear sequence of events you can reason about.

**Step-by-step: one token generation cycle**

1. **Context is assembled.** The model reads all previous tokens in the conversation — your prompt plus anything it has already generated. This is the context window you learned about in topic 3.4.
2. **Logits are computed.** The model's parameters (weights from topic 3.5) process the context and produce one raw score (logit) per token in the vocabulary.
3. **Temperature is applied.** Every logit is divided by the temperature value. A small temperature makes the largest logits relatively larger and the smallest ones relatively smaller. A large temperature compresses the differences.
4. **Probabilities are computed.** The adjusted logits are converted into a probability distribution — all values become positive numbers that sum to 1.
5. **Sampling strategy is applied.**
   - Greedy: pick the token with the highest probability. Done.
   - Top-k: zero out every token outside the top k; then sample from the remainder.
   - Top-p: zero out every token not in the cumulative nucleus up to p; then sample from the nucleus.
6. **A token is selected.** The probability-weighted random draw produces one token.
7. **The token is appended.** The chosen token joins the context, and the cycle repeats from step 1 for the next token.

This cycle continues until the model generates a special end-of-sequence token or hits the maximum output length configured.

**Pseudocode (plain language)**

```
given: prompt, temperature, strategy (greedy / top-k / top-p), max_tokens

tokens_generated = []

repeat up to max_tokens times:
    logits = model.forward(prompt + tokens_generated)   # one score per vocab item
    logits = logits / temperature                       # reshape distribution
    probabilities = convert_to_probabilities(logits)    # all values sum to 1

    if strategy == greedy:
        next_token = highest_probability_token          # always pick the top one
    elif strategy == top_k:
        keep only top-k entries; re-normalise; pick randomly
    elif strategy == top_p:
        sort descending; accumulate until sum >= p; re-normalise; pick randomly

    tokens_generated.append(next_token)

    if next_token == END_OF_SEQUENCE:
        break

return decode(tokens_generated)
```

## 7. Real-World Patterns

**Customer-facing chatbots.** Services like customer support bots typically run at temperature 0.2 – 0.5. The goal is consistent, accurate answers. A bot that gives a different refund policy each time it is asked would erode user trust [1].

**Code assistants.** AI-powered coding tools typically use low temperature (0.0 – 0.3) or even pure greedy decoding for code completion. Code is either syntactically correct or it is not; creativity is not an asset here [2].

**Creative writing tools.** Applications designed for storytelling, poetry, or game dialogue generation use high temperature (1.0 – 1.5) combined with top-p sampling. The model's varied word choices are the product, not a defect.

**Bulk content generation and A/B testing.** When a product team needs 20 different variations of marketing copy, they run the same prompt multiple times at temperature 1.0 – 1.2 and keep the best outputs. Temperature is intentionally used to produce diversity [3].

**APIs and developer settings.** If you connect to an LLM through the OpenAI API, Anthropic API, or Ollama, temperature is one of the first parameters you set. The default in many systems is 1.0. Developers often tune it down toward 0.2 for production factual workloads and leave it higher for experimental or creative features [1][3].

**Reproducibility in research.** AI researchers who need to replicate results set temperature to 0 and fix the random seed so every run produces identical output. This makes experiments comparable across different machines or dates.

## 8. Best Practices

| Do | Don't |
|----|-------|
| Start at temperature 0.7 and adjust from there based on the task | Assume temperature = 0 means the model is always correct |
| Use greedy / low temperature for factual, structured, or code tasks | Use high temperature for tasks where accuracy is critical |
| Use top-p (nucleus) sampling for creative tasks — it adapts better than top-k | Set both temperature and top-p to extreme values at the same time without testing |
| Test your chosen temperature with at least 5 prompt runs before locking it in | Assume the same temperature setting works for all models |
| Document your temperature setting alongside the prompt when sharing AI outputs | Forget that low temperature makes errors consistent, not absent |

**Anti-patterns to avoid**

- **"Temperature 0 means truthful."** Low temperature means consistent — a model can confidently hallucinate the same wrong answer every time at temperature 0.
- **"Higher temperature = smarter answers."** High temperature means more variety, not deeper understanding. The model's underlying knowledge does not change.
- **Setting temperature above 1.5 for production use.** Outputs reliably become incoherent. Reserve very high temperatures only for experimental contexts [2].
- **Ignoring top-p when using temperature.** If the platform supports both, they interact. Read the documentation for the specific API or tool you are using [3].

## 9. Hands-On Exercise

**Capability Probe — Temperature in Action** (connects to this week's Lab Activity)

This exercise supports the week's Capability Probe, where you are exploring what Claude can and cannot do across different task types.

1. **Pick a factual question** that has one clearly correct answer (e.g. "What is the capital of Japan?" or "What year did the first iPhone launch?"). Run it three times and note whether the answer changes. If your tool allows it, set temperature to 0 and run it three more times. Record your observations.
2. **Pick a creative prompt** (e.g. "Write the opening sentence of a mystery novel set in a lighthouse."). Run it five times. Notice how different each response is. This is sampling at work.
3. **Document your findings** for Journal Entry #2: What changed across runs? Did you notice any hallucinations in the factual question? Did the creative prompt produce anything surprising or incoherent? What does this tell you about how temperature affects reliability vs. creativity?

No code or API access is needed — you can do this directly in a chat interface like Claude.ai. If your course environment provides API access, try setting the temperature parameter explicitly for each step.

## 10. Key Takeaways

- **An LLM produces a probability distribution at every generation step** — not a single guaranteed answer. Each token is chosen by sampling from that distribution, which is why the same prompt can yield different outputs.
- **Temperature is the main dial controlling how concentrated or spread out that distribution is.** Low temperature (close to 0) makes the model predictable and consistent; high temperature (close to 1.5) makes it varied and creative.
- **Three main sampling strategies exist:** greedy decoding (always pick the top token — deterministic), top-k sampling (pick from the top k candidates), and top-p / nucleus sampling (pick from the smallest group of tokens whose probabilities sum to p — adaptive and generally preferred for creative tasks).
- **Match temperature to the task:** use low temperature for factual, code, or structured work; use medium-to-high temperature for conversation, creative writing, or generating diverse options.
- **Low temperature does not mean the model is correct — it means the model is consistent.** A confidently wrong answer at temperature 0 is still wrong. Temperature controls randomness, not accuracy.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
