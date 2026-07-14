<!-- nav:top:start -->
[⬅ Previous: 3.5 — What parameters are and why they matter](../../3-5-what-parameters-are-and-why-they-matter/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 3.7 — AI in India today ➡](../../../3-ai-in-context/3-7-ai-in-india-today-healthcare-agriculture-vernacular-translat/artifacts/reading.md)
<!-- nav:top:end -->

---

# Temperature and Sampling — Why the Same Question Gives Different Answers

## Overview

You may have noticed that asking a chatbot the same question twice can produce two different answers. This is not a bug — it is a deliberate design choice controlled by a setting called **temperature**. Understanding temperature helps you predict when an AI model will be consistent and when it will be creative, and lets you tune that behaviour for your own tasks [1].

## Key Concepts

### From Words to Numbers: Logits and Probability Distributions

When an LLM finishes reading your prompt, it does not immediately "pick" the next word. Instead, the model runs a forward pass through its network and produces a raw score for every token in its vocabulary. These raw scores are called **logits** — one number per possible next token, representing how strongly the model "votes" for each choice.

Those logits are then converted into a **probability distribution over tokens** — a list of percentages that must all add up to 100%. Think of it like a roulette wheel where each slot is labelled with a token: a larger slot means a higher chance of landing there [1].

For example, after the prompt "The sky is ___", the distribution might look like:

| Token | Probability |
|-------|-------------|
| "blue" | 55% |
| "clear" | 25% |
| "dark" | 12% |
| everything else | 8% |

**Deterministic output** means the model always picks the single highest-probability token — the result is the same every time. **Stochastic output** means the model samples randomly from the distribution — the result can vary on every run.

### The Temperature Dial

**Temperature** is a number you pass to the model that reshapes the probability distribution before sampling happens [2].

- **Low temperature (0.1–0.3):** The high-probability tokens get even more of the weight. The distribution becomes "spikier." The model will almost always pick the same token, producing consistent, predictable output.
- **High temperature (1.0–1.5):** The probabilities are spread more evenly across tokens. The distribution becomes "flatter." The model is more likely to pick a lower-probability, surprising token, producing varied and sometimes unexpected output.
- **Temperature = 0 (greedy decoding):** A special case. The model always picks the single highest-probability token and ignores all others. This is called **greedy decoding** — "greedy" because it takes the best option at every step without looking ahead [1].

Here is how temperature changes the picture for "The sky is ___":

| Temperature | "blue" | "clear" | "dark" | "crimson" |
|-------------|--------|---------|--------|-----------|
| 0 (greedy)  | 100%\* | 0%      | 0%     | 0%        |
| 0.2         | 88%    | 10%     | 2%     | ~0%       |
| 1.0         | 55%    | 25%     | 12%    | 8%        |
| 1.5         | 38%    | 28%     | 18%    | 16%       |

\*At temperature 0, only the top token is ever chosen.

### Three Sampling Strategies

Temperature controls the shape of the distribution. Sampling strategies control which tokens are even considered before sampling [3].

1. **Greedy decoding** — Always pick the top-1 token. Fast and deterministic, but can get stuck in repetitive loops.

2. **Top-k sampling** — Before sampling, keep only the top *k* tokens by probability (e.g. the top 40). Tokens ranked lower than *k* are zeroed out. This caps the "roulette wheel" to a fixed number of slots.

3. **Top-p sampling (nucleus sampling)** — Instead of a fixed count, keep the smallest set of tokens whose cumulative probability reaches a threshold *p* (e.g. 0.9 = 90%). If the model is very confident, that might be just 2–3 tokens. If it is uncertain, it might include 50+ tokens. The set adapts to the model's confidence [2][3].

| Strategy | What it cuts | Best for |
|----------|-------------|----------|
| Greedy | Everything except rank 1 | Exact recall tasks |
| Top-k | Tokens below rank k | Balanced creativity |
| Top-p | Tokens past cumulative p | Adaptive, most widely used |

Most APIs — including OpenAI, Anthropic, and Ollama — expose temperature, top-k, and top-p as separate parameters. The general rule: adjust one at a time and test [3].

## Worked Example

**Scenario:** A student types "Give me an example of a metaphor." into an LLM-powered study tool.

**At temperature = 0 (greedy decoding):**
Every time the student submits this prompt, the model returns exactly the same answer — for instance, "Life is a journey." Here is why: the forward pass always produces the same logits for the same input. At temperature 0, the model always picks the highest-probability token at every step, so the sequence of tokens is completely fixed. The output is deterministic.

**At temperature = 1.0:**
The first run might return "Time is a thief." The next run might return "The classroom was a zoo." A third run might produce "Her voice was honey." Here is why: the distribution is not collapsed to one token. At each step the model samples from the full spread of probabilities, so a different token "wins the roulette spin" each time, steering the sentence in a new direction.

**What changed?** Nothing about the model's knowledge changed. The same weights, the same vocabulary, the same probability scores were computed. The only difference is whether the sampling step picks greedily or probabilistically. Temperature does not inject new facts — it unlocks tokens that were already assigned nonzero probability.

## In Practice

**Choosing a temperature by task type [1][2]:**

| Task | Recommended temperature | Why |
|------|------------------------|-----|
| Factual Q&A, code generation | 0–0.3 | Consistency matters more than variety |
| Summarisation, classification | 0.3–0.6 | Moderate control, low randomness |
| Conversational assistants | 0.6–0.9 | Natural-feeling variation without going off-rail |
| Creative writing, brainstorming | 1.0–1.5 | Diversity of output is the goal |

**How to set it in practice:**
- OpenAI API: pass `temperature` in the request body (0.0–2.0 range).
- Anthropic API: pass `temperature` in the messages request (0.0–1.0 range).
- Ollama (local models): pass `temperature` in the model options block.

**The key anti-pattern to avoid:**

> "If I set temperature to 0, the model will give me the correct answer."

This is a common and dangerous misconception. Low temperature makes the model *consistent* — it will return the same answer every time. But if the model's top-probability token happens to be wrong (a hallucination, a stale fact, a misread prompt), temperature = 0 will reproduce that wrong answer reliably, every single run [1][2]. Temperature controls the sampling randomness — it does not control the accuracy of the model's knowledge. A confidently wrong model at temperature 0 is worse than an uncertain model, because you lose the diversity that might have surfaced the correct answer.

## Key Takeaways

- **Temperature reshapes the probability distribution** before the model picks the next token — low values make the model more consistent; high values make it more varied.
- **Greedy decoding (temperature = 0)** always picks the single most likely token, producing fully deterministic output.
- **Top-k and top-p (nucleus) sampling** narrow which tokens the model can choose from before the random draw; top-p adapts the pool size to the model's confidence.
- **Match temperature to the task:** factual and code tasks want low temperature; creative tasks want high temperature.
- **Low temperature does not mean accurate.** Temperature controls randomness, not the correctness of the model's underlying knowledge.

## References

1. Hopsworks. "LLM Temperature." *Hopsworks AI Dictionary*. https://www.hopsworks.ai/dictionary/llm-temperature
2. Thinking Sand. "The Definitive Guide to LLM Temperatures." *Medium*. https://medium.com/thinking-sand/the-definitive-guide-to-llm-temperatures-abab311260a6
3. Vellum AI. "Temperature." *LLM Parameters Reference*. https://www.vellum.ai/llm-parameters/temperature

---
<!-- nav:bottom:start -->
[⬅ Previous: 3.5 — What parameters are and why they matter](../../3-5-what-parameters-are-and-why-they-matter/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 3.7 — AI in India today ➡](../../../3-ai-in-context/3-7-ai-in-india-today-healthcare-agriculture-vernacular-translat/artifacts/reading.md)
<!-- nav:bottom:end -->
