<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Cresent view of 10.2 — How LLMs Work.
     Source of truth: CIT 3.4, CIT 3.5.
     Regenerate: python Cresent/Technical/tools/generate_shared_readings.py -->
<!-- nav:top:start -->
Previous: [⬅ 10.1 — History of AI](../10-1-history-of-ai/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../README.md#part-b)&emsp;·&emsp;[10.3 — The Jagged Frontier ➡](../10-3-the-jagged-frontier/reading.md)
<!-- nav:top:end -->

---

# How LLMs Work — Tokens, Training, and Inference

## Overview

You type a message into an LLM (Large Language Model) and a response appears — but what actually happens between your keystroke and that first word on screen? This topic opens the hood on three interconnected mechanics: how your text is broken into pieces the model can process, how the model was taught to understand language, and how it generates a reply one step at a time. Understanding these mechanics will help you use LLMs more deliberately and explain behaviours that otherwise seem mysterious.

![From Raw Text to Generated Token — LLM Inference Pipeline](../../../../../../../../CIT/content-gen-example/content/m2-introduction-to-ai-systems/week-3/2-how-llms-work/3-4-how-llms-work-tokens-training-and-inference/artifacts/diagram.png)
*From Raw Text to Generated Token — LLM Inference Pipeline*

## Key Concepts

### 1. Tokens — The Smallest Unit an LLM Sees

An LLM never reads your raw text. Before any processing can happen, your text is broken into **tokens** — the smallest chunks that an LLM processes. A token is not the same as a word: it can be a whole word, part of a word, a punctuation mark, or even a space [1].

Examples:
- "the" → one token
- "unhappiness" → might split into `un`, `happiness` (two tokens)
- "Hello, world!" → roughly four tokens: `Hello`, `,`, ` world`, `!`

**Why not individual letters?** Sequences would become extremely long, making it hard for the model to learn patterns.  
**Why not whole words?** Whole-word systems break on new words, names, and other languages — the vocabulary would be unmanageably large.

The solution is **subword tokenisation** — splitting words into smaller, frequently occurring pieces. This approach handles known and unknown words gracefully, because even an unfamiliar word can be represented as a combination of familiar subword tokens [1].

The most widely used algorithm is **Byte-Pair Encoding (BPE)** — a method that repeatedly merges the most frequent pairs of characters or subwords in training text until the desired vocabulary size is reached.

**From text to numbers.** Each token is assigned a unique integer ID. "Hello, world!" might become `[15496, 11, 995, 0]`. Each ID is then looked up in an **embedding table** — a large lookup chart that converts the integer ID into a list of numbers that encodes the token's meaning. These numbers are what the model actually computes with [1].

![LLM Inference Pipeline](../../../../../../../../CIT/content-gen-example/content/m2-introduction-to-ai-systems/week-3/2-how-llms-work/3-4-how-llms-work-tokens-training-and-inference/artifacts/diagram.mmd)
*The full pipeline from raw text through tokenisation, embedding, Transformer layers, and autoregressive decode — showing the prefill and decode phases.*

**Practical note on cost.** LLM APIs typically charge per token, not per word. A 1,000-word document uses roughly 1,300–1,500 tokens. Knowing this helps you estimate costs and avoid running into context limits [1].

---

### 2. Training — How the Model Learns

Training is the process of teaching the model by having it make predictions over enormous amounts of text. The task sounds simple: **next-token prediction** — given all the tokens seen so far, predict the most likely next token [2].

Here is how it works step by step:

1. The model sees a partial sentence, e.g. "The cat sat on the ___."
2. It predicts a next token — at the start, essentially at random.
3. The correct token ("mat") is revealed.
4. A process called **backpropagation** calculates how wrong the prediction was and nudges the model's internal numbers slightly toward a better answer.
5. This repeats across billions of sentences and trillions of tokens.

After enough repetitions the model becomes very good at predicting the next token in almost any context [2].

**What are parameters?** A model's **parameters** (also called weights) are the millions or billions of numbers stored inside the neural network. They are the product of training — the compressed record of everything the model learned about language, facts, and reasoning patterns. When a model is described as "70 billion parameters," that means 70 billion individual numbers were adjusted during training [2].

**The attention mechanism.** Modern LLMs are built on the Transformer architecture (introduced in topic 3.2). At its core is the **attention mechanism** — a mathematical operation that lets every token in the input "look at" every other token and decide how much weight to give it [2].

For example, in "The bank by the river was flooded":
- Without attention, "bank" is processed in relative isolation.
- With attention, the model links "bank" to "river" and "flooded" and concludes this is a riverbank, not a financial institution.

Attention is the key reason Transformers outperform earlier architectures at most language tasks.

**What the model learns.** Because predicting the next token well requires understanding grammar, facts, and reasoning, the model implicitly learns a great deal about the world — not because anyone labelled it, but because it helps prediction [2]. This is why a trained LLM can answer questions and summarise documents even though it was only ever given one task.

Training at this scale requires thousands of specialised processors running for weeks or months, which is why only a small number of organisations train frontier models from scratch [2].

---

### 3. Inference — How the Model Generates Text

**Inference** is the term for running a trained model to produce an output. When you send a prompt to an LLM and press Enter, inference begins [3].

Inference runs in two distinct phases:

**Phase 1 — Prefill.** The model processes your entire prompt at once. Every token in your input is converted to a number ID, looked up in the embedding table, and passed through all Transformer layers simultaneously. At the end, the model holds an internal representation of your full prompt and is ready to generate. The prefill phase is relatively fast because all input tokens are processed in parallel [3].

**Phase 2 — Decode (autoregressive decoding).** The model generates one token at a time:

1. Look at all input tokens plus all output tokens generated so far.
2. Predict the single most likely next token.
3. Append that token to the sequence.
4. Repeat from step 1 — until the model produces a special "end" token or reaches a length limit.

This loop is called **autoregressive decoding** — "auto" because each new token feeds back in as input for the next step, and "regressive" because it always looks backward at prior tokens. When you watch an LLM type out its answer word by word in a chat interface, you are watching autoregressive decoding in real time [3].

**Why outputs vary.** At each decode step the model produces a probability score for every token in its vocabulary — a distribution of possible next tokens — and samples from it. This is why the same prompt can produce slightly different outputs on different runs. The degree of randomness is controlled by a setting called temperature, which is covered in topic 3.6.

---

### 4. Context Window

The **context window** is the maximum number of tokens the model can "see" at one time — your prompt plus any output generated so far, combined [3]. Think of it as the model's working memory for a single conversation.

| Context window size | Roughly equivalent to |
|---|---|
| 4,000 tokens | A few pages of text |
| 32,000 tokens | A short novel chapter |
| 128,000 tokens | About 100,000 words — a full novel |

If a conversation grows longer than the context window, the oldest tokens fall off the edge and the model can no longer refer to them. This is why LLMs can "forget" something said earlier in a very long conversation — they literally cannot see that part of the exchange anymore [3].

Larger context windows are useful for summarising long documents, but they also increase the computational cost of each inference step [3].

## Worked Example

**Watching tokenisation in action.** The `tiktoken` library (for GPT-family models) lets you inspect exactly how text is tokenised:

```python
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")
tokens = enc.encode("Hello, world! Tokenisation is fun.")
print(tokens)        # a list of integer IDs
print(len(tokens))   # the token count
```

Try this with:
1. A sentence in English.
2. The same sentence translated into Hindi, Tamil, or Arabic.

You will likely see the non-English version produce three to five times as many tokens as the English version [1]. This happens because most LLM tokenisers are optimised for English vocabulary — a consequence of training data composition. The non-English sentence uses more of the context window and costs more per API call.

This single experiment builds strong intuition about two things at once: the subword nature of tokens, and why tokenisation choices have real consequences for multilingual applications.

## In Practice

**Do test tokenisation when results are unexpected.** If a model misreads a name, a code snippet, or an uncommon technical term, check how that string is tokenised. An awkward split at a word boundary can confuse the model's predictions [1].

**Do not assume one word equals one token.** Technical terms, code, URLs, and non-English text are significantly more token-expensive than plain English. Build in a buffer — roughly 1.3 tokens per word — when estimating costs or context window usage [1].

**Keep prompts purposeful.** Every token in your prompt counts against the context window limit and affects what the model attends to. Unnecessary padding dilutes attention on the parts that matter [3].

**Design explicit handling for context window overflow.** Applications that silently truncate input when the limit is exceeded can produce responses that miss critical information — with no warning to the user [3].

**Match model size to task.** A smaller model may be fast and cheap enough for simple summarisation; a larger one may be needed for complex reasoning. The inference mechanics are identical — the difference is the depth of what was learned during training [2].

**Multilingual applications need extra token budget.** Teams building for non-English languages should account for the higher token-per-sentence ratio and consider language-specific models where cost or latency is critical [1].

## Key Takeaways

- A **token** is the smallest unit an LLM processes — a subword chunk, not a full word. Text is converted to integer IDs, then to embedding vectors, before any computation begins [1].
- An LLM is trained by repeatedly predicting the next token across billions of examples; every wrong prediction nudges the model's **parameters** toward a better answer via backpropagation [2].
- The **attention mechanism** inside the Transformer lets each token relate to every other token in the context — enabling the model to resolve meaning that depends on relationships between words [2].
- **Inference** runs in two phases: **prefill** (the full prompt is processed in parallel) followed by **decode** (one token is generated at a time, autoregressively). The sequential decode step is why generation is not instantaneous [3].
- The **context window** is the hard limit on how many tokens the model can see at once; text beyond it is invisible during that call, which explains certain "forgetting" behaviours in long conversations [3].

## References

1. "What Is an LLM Token? A Beginner-Friendly Guide for Developers." *The New Stack*. https://thenewstack.io/what-is-an-llm-token-beginner-friendly-guide-for-developers/
2. Deudney. "How an LLM Actually Learns: A Hilariously Simple Guide to Training, Tokens, and Transformers." *Medium*. https://medium.com/@deudney/how-an-llm-actually-learns-a-hilariously-simple-guide-to-training-tokens-and-transformers-29e062427109
3. "How Does LLM Inference Work?" *BentoML*. https://bentoml.com/llm/llm-inference-basics/how-does-llm-inference-work

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
Previous: [⬅ 10.1 — History of AI](../10-1-history-of-ai/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../README.md#part-b)&emsp;·&emsp;[10.3 — The Jagged Frontier ➡](../10-3-the-jagged-frontier/reading.md)
<!-- nav:bottom:end -->
