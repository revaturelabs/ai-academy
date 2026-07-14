<!-- nav:top:start -->
[⬅ Previous: 3.4 — How LLMs work](../../3-4-how-llms-work-tokens-training-and-inference/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 3.6 — Temperature and sampling ➡](../../3-6-temperature-and-sampling-why-the-same-question-gives-differe/artifacts/reading.md)
<!-- nav:top:end -->

---

# What Parameters Are and Why They Matter

## Overview

When an LLM (Large Language Model) gives you a fluent, accurate answer, that answer does not come from a hard-coded rulebook or a textbook lookup. It comes from billions of tiny numbers — called **parameters** — that were tuned into the model during training. Understanding what those numbers are, how they store knowledge, and why their count matters will help you make smarter decisions about which model to use and why larger models behave differently from smaller ones [1].

## Key Concepts

### Parameters and Weights

A **parameter** — also called a **weight** — is a single number stored inside a neural network, typically a decimal value such as `0.347` or `-1.82` [1]. Think of a neural network as a web of connected nodes. Every connection between two nodes has a number attached to it — its weight. That weight controls how strongly one node's signal influences the next:

- A high positive weight **amplifies** the signal.
- A weight near zero **ignores** it.
- A negative weight **suppresses** it.

A **weight matrix** is a grid (table) of weights that transforms one layer's output into the next layer's input [3]. A Transformer (from topic 3.2) is built by stacking dozens of these layers, each with its own weight matrix.

Every neuron also has a **bias** — a small extra number that shifts the neuron's output up or down, independent of its inputs [1]. A bias lets a neuron produce a signal even when all incoming signals are zero. Biases are learned during training just like weights, so they count as parameters too.

When someone says "GPT-3 has 175 billion parameters," they mean GPT-3 contains 175 billion individual numbers (weights and biases) spread across its layers [1].

### How Parameters Encode Knowledge

Parameters do not store facts as text. There is no single weight that holds the sentence "Paris is the capital of France." Instead, knowledge is **distributed** across millions of weights working together [2].

Here is how that works:

1. During pre-training (topic 3.2), the model reads vast amounts of text.
2. For each piece of text it makes a prediction — "what token comes next?"
3. When wrong, backpropagation (topic 3.4) traces the error backward and nudges each weight slightly up or down [2].
4. After billions of adjustments, the weights settle into a pattern where, collectively, they produce accurate next-token predictions.

The result is sometimes called **compressed world knowledge**: facts, grammar, reasoning patterns, and conversational styles from human-written text — all compressed into billions of floating-point numbers [1]. When the model sees the tokens "The capital of France is," the weights across many layers collectively assign a very high probability to the token "Paris" [3].

This also explains hallucination (topic 3.2). Weights encode **patterns**, not verified facts. If a pattern in the training data was wrong, or a question triggers a pattern that does not actually apply, the model will confidently produce the wrong answer — because the weights say that answer is plausible [1].

### Scaling Laws

If a single weight is just one decimal number, why do we need billions?

More parameters give the model more capacity to store more patterns. Researchers have found a predictable relationship between parameter count, training data volume, and model quality. This relationship is called **scaling laws** [1].

Scaling laws say: double the parameters (and scale up training data and compute proportionally) and you get a reliably better model — predictably, before you even run the training. The practical implications:

- GPT-3 (175 billion parameters) was qualitatively more capable than GPT-2 (1.5 billion) — not just "a bit better," but able to perform entirely new task types [1].
- LLaMA models from Meta range from 7 billion to 70+ billion parameters, letting developers choose their own capability-vs-cost balance [1].

**Emergent capability** describes a specific phenomenon: certain abilities — solving multi-step logic puzzles, writing working code — appear **suddenly** as a model crosses a size threshold, rather than improving gradually [1]. A 7-billion-parameter model may fail completely at a task that a 70-billion-parameter model handles with ease. Scale is not just quantitative; at some thresholds it is qualitative.

> **Why this matters for you:** You cannot make a small model behave like a large model through clever prompting alone. If an ability only emerges above a certain scale, the capacity for it simply is not there in a smaller model.

### Quantisation

If a 7-billion-parameter model has 7 billion weights, why does it sometimes appear as a 4 GB file and sometimes as a 14 GB file?

The answer is **quantisation** — a technique for reducing the number of bits used to store each weight [1].

By default, each weight is stored as a **fp16** (16-bit floating-point, also called "half precision") number. Each weight takes 2 bytes, so:

- 7 billion parameters × 2 bytes = approximately 14 GB

Quantisation stores each weight with less precision, saving space:

| Precision | Bits per weight | Approx. size of a 7B model | Quality trade-off |
|---|---|---|---|
| fp16 (16-bit) | 16 bits | ~14 GB | Full quality |
| int8 (8-bit) | 8 bits | ~7 GB | Tiny quality loss |
| int4 (4-bit) | 4 bits | ~4 GB | Small quality loss |

Think of quantisation as rounding: instead of storing `0.3471823`, you store `0.35`. You lose a little information but save a lot of space [1].

**Important:** quantisation does not change the parameter count. A 7B model at int4 precision still has 7 billion parameters — only how precisely each one is stored changes. A quantised small model does not become as capable as a large model [1].

**Why quantisation matters:**

- It lets you run large models on consumer hardware (a laptop with 8–16 GB of RAM) that would otherwise require expensive server GPUs.
- It reduces latency because less data moves through memory during inference.
- int8 quality loss is usually acceptable for most tasks; int4 loss is noticeable on complex reasoning but fine for many everyday uses [1].

### Model Size, Capability, and Cost

Parameter count directly shapes the practical trade-offs you will face as a practitioner:

- **Larger models, broader capability.** More parameters means more capacity for creative writing, factual recall, logical reasoning, and code generation simultaneously [1].
- **Smaller models, lower cost and latency.** A 70B model may require 40 GB of GPU memory. A 7B model can run on a laptop. For a customer-service chatbot handling simple queries, a smaller model is often the right choice [1].
- **Parameter count is not the only factor.** Training data quality, fine-tuning (covered in a later topic), and the attention mechanism (topic 3.4) all affect capability. A well-trained 7B model can outperform a poorly trained 13B model on specific tasks.
- **Hallucination is not purely a scale issue.** Bigger models hallucinate less often on well-represented topics, but they can still produce wrong answers on obscure topics or on events after their training cutoff — more parameters cannot compress knowledge that was never in the training data [2].

How to estimate what you need:

1. Multiply the parameter count (in billions) by **2** for fp16 size in GB.
2. Multiply by **1** for int8, or **0.5** for int4.
3. Match that number to your available RAM or API budget.

## Worked Example

Suppose you want to run a model locally on a laptop with 8 GB of RAM and you are comparing two options in Ollama.

**Option A — Llama-3 7B at Q4 (int4)**
- Parameters: 7 billion
- Estimated size: 7B × 0.5 bytes = ~3.5–4 GB
- Fits comfortably in 8 GB RAM with room for the operating system.

**Option B — Llama-3 13B at Q4 (int4)**
- Parameters: 13 billion
- Estimated size: 13B × 0.5 bytes = ~6.5–7 GB
- Tight fit in 8 GB RAM; may cause slowdowns or swapping.

You choose Option A for daily drafting tasks, and you verify by checking Ollama's model card, which confirms the label "Q4" next to the download. Later, for a multi-step reasoning task where quality matters, you switch to a cloud API that runs the full fp16 version — paying a higher per-token cost for the higher precision. This is the capability-vs-cost trade-off that scaling laws make predictable [3].

## In Practice

**Match model size to task complexity.**

| Task type | Suggested model size | Why |
|---|---|---|
| Simple Q&A, summarisation | 7B–13B | Fast, cheap, sufficient |
| Multi-step reasoning, coding | 30B–70B+ | Needs the capacity |
| Local / offline use | 7B Q4 or Q8 | Fits consumer hardware |

**Do:**
- Read the model card before deploying — parameter count, training data details, and known limitations are all there.
- Test the model on your actual task type before committing; parameter count gives an estimate, direct testing confirms fit.
- Prefer Q8 (int8) over Q4 (int4) when task quality matters (legal analysis, technical writing), if your hardware allows.

**Don't:**
- Confuse file size with parameter count — a Q4 and Q8 version of the same model have identical parameter counts; only precision differs [1].
- Expect clever prompting to unlock emergent capabilities that only exist above a certain scale.
- Assume bigger is always better — a fine-tuned 7B model can outperform a generic 70B model on a narrow domain task (fine-tuning is covered in a later topic).

One note on temperature: this is another model setting that affects output behaviour and will be covered in topic 3.6.

## Key Takeaways

- A **parameter** (weight) is a single number on a connection between neurons. A large language model holds billions of these numbers, and they collectively encode the patterns learned from training data [1].
- Parameters do not store facts as text. Knowledge is distributed across many weights working together — this is why models can be fluent and wrong at the same time; the weights encode plausible patterns, not verified truths [2].
- **Scaling laws** describe a predictable relationship: more parameters (with proportional training data and compute) produce more capable models. Some capabilities only appear above certain scale thresholds — this is called **emergent capability** [1].
- **Quantisation** (fp16 → int8 → int4) reduces the bits used to store each weight, shrinking file size without changing parameter count. It trades a small amount of quality for large reductions in memory and cost [1].
- Choosing a model means choosing between capability, cost, and latency. Larger parameter counts give more capability but cost more to run; quantisation lets you run larger models on smaller hardware [3].

## References

1. Towards AI. "What Are LLM Parameters? A Simple Explanation of Weights, Biases, and Scale." https://towardsai.net/p/machine-learning/what-are-llm-parameters-a-simple-explanation-of-weights-biases-and-scale
2. Trott, S. "How a Model Got Its Weights." *Sean Trott's Substack.* https://seantrott.substack.com/p/how-a-model-got-its-weights
3. Webopedia. "LLM Tokens, Weights, and Parameters." https://www.webopedia.com/technology/llm-tokens-weights-parameters/

---
<!-- nav:bottom:start -->
[⬅ Previous: 3.4 — How LLMs work](../../3-4-how-llms-work-tokens-training-and-inference/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 3.6 — Temperature and sampling ➡](../../3-6-temperature-and-sampling-why-the-same-question-gives-differe/artifacts/reading.md)
<!-- nav:bottom:end -->
