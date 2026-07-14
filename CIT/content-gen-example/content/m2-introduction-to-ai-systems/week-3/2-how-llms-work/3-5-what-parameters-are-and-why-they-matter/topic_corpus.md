---
topic_id: "3.5"
title: "What parameters are and why they matter"
position_in_module: 2
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. What Parameters Are and Why They Matter — Topic Corpus

## 2. Prerequisites

This topic builds directly on prior topics in this sequence:

- **3.1** — machine learning, deep learning, artificial neural networks, training data
- **3.2** — large language model (LLM), Transformer architecture, pre-training and fine-tuning, hallucination, prompt
- **3.4** — token, tokenisation, next-token prediction, backpropagation, attention mechanism, inference, context window, parameters (model weights) — introduced briefly; this topic is the deep dive

## 3. Learning Objectives

By the end of this topic, you will be able to:

1. **Define** what a parameter (weight) is in a neural network, using a plain-language explanation that a non-technical person could follow.
2. **Explain** how parameters encode knowledge — describing what gets compressed into weights during training.
3. **Describe** why parameter count (scale) matters for capability, with reference to the concept of scaling laws.
4. **Explain** what quantisation is and why the same model can appear at different file sizes without changing its parameter count.
5. **Apply** an understanding of parameter count to practical model-selection decisions, such as trading capability for speed or cost.

## 4. Introduction

When you ask an LLM a question and it gives you a fluent, accurate answer, where did that answer come from? The model was not given a textbook to look up. It was not following a hard-coded rule book. The answer came from billions of tiny numbers — called **parameters** — baked into the model during training.

You already met the word "parameters" in topic 3.4, where we described them as the numerical values the model learns during training. That was a one-sentence introduction. This topic is the deep dive. By the end you will understand what those numbers actually are, how they store knowledge, why more of them generally means a more capable model, and why the file size of a model on your hard drive is not the same thing as its parameter count.

Think of parameters as the "settings" that were tuned — billions of times — until the model got good at predicting text. Understanding parameters is the key to understanding why GPT-4 behaves differently from a smaller model, why running a large model costs more, and how engineers make trade-offs when choosing a model for a real project.

## 5. Core Concepts

### §5.1 What a Parameter Is

A **parameter** — also called a **weight** — is a single number inside a neural network. It is stored as a decimal value, such as `0.347` or `-1.82` [1].

To understand what that means, picture a neural network as a web of connected nodes (the "neurons" from topic 3.1). Every connection between two nodes has a number attached to it — its weight. That weight controls how strongly one node's signal influences the next node. A high positive weight amplifies the signal. A weight near zero ignores it. A negative weight suppresses it [1].

A large language model is made of layers of these connections. Each layer is a grid of numbers called a **weight matrix** — a table of weights that transforms one representation of text into another [3]. Stack dozens of these layers, each with its own weight matrix, and you get a Transformer (from topic 3.2).

**Bias** is a related concept. Every neuron also has a **bias** value — a small extra number that shifts the neuron's output up or down, independent of its inputs [1]. You can think of a bias as a baseline: it lets the neuron fire even when all its incoming signals are zero. Biases are also parameters — they are learned during training just like weights.

So when someone says "GPT-3 has 175 billion parameters," they mean: GPT-3 has 175 billion individual numbers (weights and biases) spread across its weight matrices and layers [1].

> **Key definition recap:**
> - **Parameter (weight)** — a single number on a connection between neurons; controls signal strength.
> - **Weight matrix** — a grid of weights that transforms one layer's output into the next layer's input.
> - **Bias** — a per-neuron offset number; also a parameter.

### §5.2 How Parameters Encode Knowledge

Parameters do not store knowledge as text or as facts. There is no row in the model that says "Paris is the capital of France." Instead, knowledge is distributed across millions of weights working together [2].

Here is how that happens. During training (pre-training, from topic 3.2), the model sees vast amounts of text. For each piece of text, it makes a prediction — "what word comes next?" — and checks whether it was right. When it was wrong, backpropagation (from topic 3.4) traced the error backward through the network and adjusted the weights slightly: push this weight up a little, nudge that one down [2]. This happened billions of times across billions of text examples.

After enough adjustments, the weight values settled into a pattern where — collectively — they cause the model to predict plausible next tokens very well [2]. The "knowledge" that Paris is the capital of France is not stored in any one weight. It is encoded in the combined behaviour of many weights across many layers. When the model sees the tokens "The capital of France is," the weights collectively produce a very high probability for the token "Paris" [3].

This is why parameters are sometimes described as **compressed world knowledge**: the entire distribution of human-written text — facts, grammar, reasoning patterns, conversational styles — has been compressed into billions of floating-point numbers [1].

It is also why models can hallucinate (topic 3.2). Weights encode patterns, not verified facts. If a pattern in the training data was wrong, or if a question triggers a pattern that does not actually apply, the model will confidently produce the wrong answer — because the weights say that answer is plausible [1].

### §5.3 Why Scale Matters — Scaling Laws

If a single weight is just one decimal number, why do we need billions of them?

More parameters give the model more capacity to encode more patterns. A model with 7 billion parameters can hold more nuance, more facts, and more complex relationships than a model with 1 billion parameters — roughly speaking. Researchers have found that, across a wide range of model sizes, there is a predictable relationship between parameter count, the amount of training data, and the quality of the model's predictions. This relationship is called **scaling laws** [1].

Scaling laws say: if you double the number of parameters (and also scale up your training data and compute), you get a reliably better model. This was a major discovery because it meant engineers could predict in advance how much better a bigger model would be — they did not have to train it first to find out.

The implications are significant:

- GPT-3 (175 billion parameters) was dramatically more capable than GPT-2 (1.5 billion) — not just "a bit better," but qualitatively different in what tasks it could do [1].
- GPT-4 is estimated to be larger still, though its exact parameter count has not been publicly confirmed.
- LLaMA models (a family of open-weight models from Meta) come in sizes from 7 billion to 70+ billion parameters, letting developers trade capability for cost [1].

**Emergent capability** is what researchers call the phenomenon where certain abilities — like solving multi-step logic puzzles or writing working code — appear suddenly as models cross a size threshold, rather than improving gradually [1]. A 7-billion-parameter model may fail completely at a task that a 70-billion-parameter model handles easily. This makes scale not just quantitative but qualitative.

> **Why does this matter for you as a practitioner?** Bigger models cost more to run (more compute, more memory, higher API cost) and respond more slowly. Smaller models are cheaper and faster. Scaling laws tell you that you cannot get a small model to behave like a large model just by prompting it cleverly — at some point, the capacity simply is not there.

### §5.4 Quantisation

Here is a question that often confuses beginners: if GPT-3 has 175 billion parameters, and a 7-billion-parameter model takes up around 14 GB on disk, why does a 7B model sometimes appear as a 4 GB file?

The answer is **quantisation** — a technique for reducing the number of bits used to store each weight [1].

By default, a weight is stored as a 16-bit floating-point number (called "fp16" or "half precision"). That means each weight takes 2 bytes of disk space. So:

- 7 billion parameters x 2 bytes = approximately 14 GB (at 16-bit precision)

Quantisation reduces how precisely each weight is stored:

| Precision | Bits per weight | Approximate size of a 7B model | Quality trade-off |
|---|---|---|---|
| 16-bit (fp16) | 16 bits | ~14 GB | Full quality |
| 8-bit (int8) | 8 bits | ~7 GB | Tiny quality loss |
| 4-bit (int4) | 4 bits | ~4 GB | Small quality loss |

When you see a model listed as "7B Q4" (for example, in Ollama — a tool for running models locally on your laptop), the "Q4" means it has been quantised to 4 bits per weight [1]. The model still has 7 billion parameters — the parameter count does not change. What changes is the precision with which each parameter is stored. Think of it like rounding: instead of storing `0.3471823`, you store `0.35`. You lose a little information, but you save a lot of space.

**Why does quantisation matter?**

- It lets you run large models on consumer hardware (a laptop with 8–16 GB of RAM) that would otherwise require expensive server GPUs.
- It reduces latency (faster responses) because less data has to move through memory.
- The quality drop for 8-bit quantisation is usually small enough to be acceptable for most tasks. For 4-bit, quality loss is noticeable on complex reasoning tasks but acceptable for many everyday uses [1].

**What quantisation does NOT do:** it does not make a small model as capable as a large one. A 7B model quantised to 4-bit is still a 7B model — it will not suddenly perform like a 70B model.

### §5.5 Capabilities and Limitations Tied to Parameter Count

Understanding parameters clarifies several practical realities:

**Larger models, broader capability.** A model with more parameters can handle more task types — creative writing, factual recall, logical reasoning, code generation — simultaneously. Smaller models often excel at one or two tasks but fall apart on others [1].

**Smaller models, lower cost and latency.** Running a 70B model requires large amounts of GPU memory (often 40 GB or more). A 7B model can run on a laptop. For many production applications — a customer-service chatbot handling simple queries — a smaller model is the right choice [1].

**Parameter count is not the only factor.** Training data quality, fine-tuning (updating parameters on a specific task — covered in a later topic), and the attention mechanism (topic 3.4) all affect capability. A well-trained 7B model can outperform a poorly trained 13B model on certain tasks.

**Hallucination risk is not purely a parameter-count issue.** Bigger models hallucinate less often on well-represented topics, but they can still confidently produce wrong answers on obscure topics or on events after their training cutoff. More parameters compress more knowledge, but they cannot compress knowledge that was never in the training data [2].

## 6. Implementation

### Checking a Model's Parameter Count and Size Before Choosing It

When you are choosing a model for a task, you will often compare options by their parameter count and quantisation. Here is a practical approach:

**Step 1: Find the parameter count.**
Model cards (published by the model creators on platforms like Hugging Face or in official documentation) state the parameter count directly. Look for phrases like "7B parameters" or "70B parameters."

**Step 2: Estimate the memory you need.**
Use the rough rule: multiply the parameter count (in billions) by 2 to get the approximate size in GB at 16-bit precision. For 8-bit, multiply by 1. For 4-bit, multiply by 0.5.

- 7B at 16-bit = approximately 14 GB
- 7B at 8-bit = approximately 7 GB
- 7B at 4-bit = approximately 4 GB

**Step 3: Match to your hardware or budget.**
If you are running locally using Ollama, check your laptop's RAM. If you are calling an API (such as Claude or OpenAI), check the provider's pricing page — larger models cost more per token.

**Step 4: Check the quantisation label.**
In Ollama's model library, models are listed with their quantisation level (Q4, Q8, etc.). For tasks where quality matters most (legal analysis, technical writing), prefer Q8 or fp16 if hardware allows. For casual or draft tasks, Q4 is usually fine.

**Step 5: Run a quick capability probe.**
Before committing to a model, test it on the types of tasks you plan to use it for. Parameter count gives you a starting estimate; direct testing tells you whether the model is right for your specific use case. The lab exercise in this module does exactly this.

## 7. Real-World Patterns

**GPT-3 and the scaling breakthrough.** When OpenAI released GPT-3 in 2020 with 175 billion parameters, it demonstrated capabilities — coherent long-form writing, few-shot reasoning, basic coding — that its smaller predecessors could not reliably perform [1]. This was one of the first public demonstrations of emergent capability at scale, and it shifted the field's attention toward scaling as a primary lever for improving AI systems.

**LLaMA and accessible large models.** Meta's LLaMA family makes it practical for individuals and smaller companies to run capable models locally, without paying API fees [1]. By releasing models at multiple sizes (7B, 13B, 34B, 70B+), Meta gave practitioners a direct way to experience the capability-cost trade-off. LLaMA models are widely used in tools like Ollama.

**Quantisation in practice with Ollama.** When you run a model download command in Ollama on a consumer laptop, Ollama automatically downloads a 4-bit quantised version of the model [1]. This is why a 7-billion-parameter model fits in approximately 4 GB rather than 14 GB. Understanding this helps you know when to reach for a larger, less-compressed model when quality is critical.

**API pricing as a proxy for model size.** When you compare different tiers of a commercial API — faster/cheaper vs more capable/more expensive — the pricing differences reflect in part the difference in model size and the compute required to run it [3]. Choosing an API model involves the same trade-off as choosing a local model by parameter count: capability vs cost vs latency.

## 8. Best Practices

**Match model size to task complexity.**

| Task type | Suggested model size | Reason |
|---|---|---|
| Simple Q&A, summarisation | 7B–13B | Fast, cheap, sufficient |
| Multi-step reasoning, coding | 30B–70B+ | Needs the capacity |
| Long-document analysis | Any + large context window | Window size matters as much as scale |
| Local/offline use | 7B Q4 or Q8 | Fits consumer hardware |

**Do** read the model card before deploying. Parameter count is stated there, along with training data details and known limitations.

**Don't** assume bigger is always better for your use case. A 7B model fine-tuned on your specific domain can outperform a generic 70B model on domain-specific tasks. Fine-tuning is covered in a later topic.

**Don't** confuse file size with parameter count. A Q4 model and a Q8 model of the same architecture have the same number of parameters — only the precision differs. Comparing capabilities requires comparing parameter counts, not file sizes [1].

**Don't** expect a small model to reach large-model capability through prompting alone. If a task requires emergent capabilities that only appear at a certain scale, clever prompting cannot compensate for missing parameters [1].

## 9. Hands-On Exercise

This exercise connects directly to the lab in this module: the Capability Probe (test an LLM across 5 task types — creative, factual, logical, ethical, coding).

**Extension: Parameter-aware comparison**

1. Pick one task from your Capability Probe (for example, a multi-step logic puzzle).
2. If you have access to two models of different sizes (for example, a small API tier vs a large tier, or two Ollama models of different sizes), run the same task through both.
3. Note: Does the larger model give a more complete or accurate answer? Does it handle nuance the smaller model misses?
4. Check the quantisation level of any local model you use. Record it in your notes.
5. Add one sentence to Journal Entry #2 describing what the parameter-count difference seemed to produce in practice.

This exercise builds the intuition that parameter count is a real, observable lever — not just an abstract specification number.

## 10. Key Takeaways

- A **parameter** (weight) is a single number on a connection between neurons. A large language model contains billions of these numbers, and they collectively encode the patterns the model learned from training data [1].
- Parameters do not store facts as text. Knowledge is distributed across many weights working together. This is why models can be fluent and wrong simultaneously — the weights encode plausible patterns, not verified truths [2].
- **Scaling laws** describe a predictable relationship: more parameters (with proportional training data and compute) produce more capable models. Some capabilities only appear above certain scale thresholds — this is called emergent capability [1].
- **Quantisation** reduces the number of bits used to store each weight (16-bit to 8-bit to 4-bit), shrinking file size without changing parameter count. It trades a small amount of quality for large reductions in memory and cost [1].
- Choosing a model means choosing between capability, cost, and latency. Larger parameter counts give more capability but cost more to run. Quantisation gives you a way to run larger models on smaller hardware [3].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
