---
topic_id: "3.4"
title: "How LLMs work — tokens, training, and inference"
position_in_module: 1
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. How LLMs Work — Tokens, Training, and Inference — Topic Corpus

## 2. Prerequisites

This topic builds on concepts from:

- **3.1** — Symbolic AI, machine learning, deep learning, artificial neural networks, training data
- **3.2** — Large language model (LLM), word embedding, recurrent neural network, Transformer architecture, BERT, GPT, pre-training and fine-tuning, hallucination, few-shot prompting

All terms listed above are used freely here without redefinition.

## 3. Learning Objectives

By the end of this topic, learners will be able to:

1. **Define** what a token is and explain how text is split into tokens using subword tokenisation.
2. **Describe** the next-token prediction objective and explain how a model learns by adjusting its parameters on large amounts of text.
3. **Explain** how an LLM generates text one token at a time during inference, distinguishing the prefill phase from the decode phase.
4. **Describe** the role of the attention mechanism in allowing the model to relate tokens across the context window.
5. **Identify** practical implications of tokenisation and context windows when interacting with an LLM.

## 4. Introduction

Imagine asking a friend a question and, before they answer, they have to figure out exactly what each word you said means — not just the whole sentence, but each small piece of it. An LLM (Large Language Model — a type of deep learning model trained on text) does something remarkably similar, but at a scale and speed that is hard to comprehend.

Here is the thing most people do not realise: an LLM does not "read" your text the way a human does. It never sees the raw letters you type. Before any thinking can happen, your text is broken apart into small chunks called **tokens**. Every word, punctuation mark, and space is turned into a number. That is where the magic — and the quirks — begin.

This topic opens the hood of an LLM. We will walk through three stages: how text is converted into tokens, how the model was trained (taught) to predict the next token, and how it generates an answer one token at a time when you send it a prompt. Understanding these mechanics will help you use LLMs more deliberately and avoid common mistakes.

## 5. Core Concepts

### 5.1 Tokens — The Alphabet of an LLM

A **token** is the smallest unit of text that an LLM processes. It is not the same as a word. Tokens are chunks of text — sometimes a whole word, sometimes part of a word, sometimes a punctuation mark or a space [1].

Think of it this way: the word "unhappiness" might be split into three tokens — `un`, `happiness`, and possibly a space before the next word. Short, common words like "the" or "is" are usually one token each. Rare or long words, especially technical terms, tend to be split into multiple tokens [1].

**Why not just use individual letters?** Using individual letters would make sequences extremely long and make it very hard for the model to learn meaningful patterns. **Why not use whole words?** Whole-word systems struggle with new words, names, and different languages — there are simply too many possibilities. **Subword tokenisation** — splitting words into smaller, frequently-occurring pieces — gives the best of both approaches [1].

Subword tokenisation is the technique used by most modern LLMs (including GPT and BERT). It builds a vocabulary of tens of thousands of subword pieces. When the model encounters a word it has not seen before, it can still represent it as a combination of known subword tokens rather than failing entirely [1]. The most widely used algorithm for learning these subword splits is called **Byte-Pair Encoding (BPE)** — it repeatedly merges the most frequent pairs of characters or subwords in the training text until the desired vocabulary size is reached.

**From text to numbers.** Each token is assigned a unique integer ID. The text "Hello, world!" might become the token IDs `[15496, 11, 995, 0]`. These IDs are what actually enter the model. Each ID is then looked up in an **embedding table** — a large lookup chart that converts the integer ID into a list of floating-point numbers (a vector). This vector is the model's internal numerical representation of that token's meaning [1] [2].

A practical consequence: the price you pay to use an LLM via an API is typically counted in tokens, not words. A 1,000-word document might use roughly 1,300 to 1,500 tokens. Understanding this helps you estimate cost and stay within limits [1].

### 5.2 Training — How the Model Learns

Training is the process by which an LLM learns from text. The goal is deceptively simple: **next-token prediction**. Given all the tokens seen so far, predict the most likely next token [2].

Here is a concrete example. Suppose the training text contains the sentence "The cat sat on the ___." The model sees "The cat sat on the" and has to predict "mat" (or "floor", or "chair" — any plausible next word). At the start of training, the model's predictions are essentially random. When it guesses wrong, a process called **backpropagation** nudges its internal numbers slightly in a direction that would have made the correct prediction more likely. Repeat this across billions of sentences and trillions of tokens, and the model gradually becomes very good at predicting the next token in almost any context [2].

**What are parameters?** A model's **parameters** (also called weights) are the millions or billions of numerical values stored inside the neural network. They are the product of training — the compressed representation of everything the model has learned about language, facts, reasoning patterns, and style. When a model is described as having "70 billion parameters", that means it has 70 billion individual numbers that were adjusted during training [2]. The details of how parameters are structured and updated in depth are covered in topic 3.5.

**The Transformer and attention.** Modern LLMs are built on the Transformer architecture (introduced in topic 3.2). At the heart of the Transformer is the **attention mechanism** — a mathematical operation that allows every token in the input to "look at" every other token and decide how much weight to give it when building its own representation [2]. For example, in the sentence "The bank by the river was flooded", the attention mechanism can link "bank" to "river" and "flooded" to figure out that "bank" means a river bank, not a financial institution. Without attention, the model would process each token in relative isolation and miss these crucial relationships. Attention is what allows Transformers to understand context — and it is a key reason LLMs outperform earlier recurrent neural networks at most language tasks.

**What the model learns beyond words.** Because next-token prediction requires understanding context, grammar, facts, and even some reasoning, the model ends up learning a great deal about the world implicitly — not because anyone told it to, but because doing so helps it predict text better [2]. This is why a well-trained LLM can answer factual questions, write code, or summarise documents, even though it was only ever given the task "predict the next token."

Training a large model requires enormous computational resources — thousands of specialised processors running for weeks or months — which is why only a handful of organisations can train frontier models from scratch [2].

### 5.3 Inference — How the Model Generates Text

**Inference** is the term for running a trained model to get an output. When you type a message into an LLM and press Enter, inference begins [3].

Inference happens in two phases [3]:

**Prefill phase.** The model processes your entire input (the prompt) at once. Every token in your prompt is converted to a number ID, looked up in the embedding table, and fed through all the layers of the Transformer simultaneously. At the end of this phase, the model has built an internal representation of your entire prompt and is ready to produce an answer. The prefill phase is relatively fast because the Transformer processes all input tokens in parallel [3].

**Decode phase — autoregressive decoding.** Now the model generates the response one token at a time. It looks at all the input tokens plus all the output tokens produced so far, and predicts the single most likely next token. That new token is appended to the sequence, and the process repeats — predict one token, append it, predict the next, and so on — until the model produces a special "end" token or reaches a length limit [3].

This token-by-token generation is called **autoregressive decoding** — "auto" because each new token feeds back in as input for the next step, "regressive" because it looks backward at previous tokens to predict the next one. If you have ever watched an LLM "type out" its answer word by word in a chat interface, you are watching autoregressive decoding in real time [3].

**Why is generation probabilistic?** At each decode step, the model produces a probability score for every token in its vocabulary — not just one answer, but a distribution of possible next tokens. It then samples from that distribution. This means the same prompt can produce slightly different outputs on different runs — the degree of randomness is controlled by temperature (covered in topic 3.6).

### 5.4 Context Window

The **context window** is the maximum number of tokens the model can "see" at one time — the input prompt plus any output generated so far, combined [3]. Think of it as the model's short-term working memory for a single conversation.

If a conversation grows longer than the context window, the oldest tokens fall off the edge and the model can no longer refer to them. This is why very long conversations can cause an LLM to "forget" something it said or was told earlier — it literally cannot see that part of the exchange anymore [3].

Modern LLMs have context windows ranging from a few thousand tokens (early models) to hundreds of thousands of tokens (recent models). A context window of 128,000 tokens can hold roughly 100,000 words — about the length of a novel. Larger context windows are useful for summarising long documents or maintaining coherent long conversations, but they also increase the computational cost of each inference step [3].

### 5.5 Capabilities and Limitations Rooted in These Mechanics

Understanding tokens, training, and inference directly explains several common LLM behaviours:

- **Strange word splits.** Because tokenisation is subword-based and not word-based, the model may handle rare proper nouns, technical jargon, or non-English words differently than common English words. A single concept expressed in a rare language might take far more tokens than the same concept in English, consuming more of the context window [1].
- **Knowledge cutoff.** Training happens on a fixed dataset collected before a certain date. Everything the model "knows" comes from that data — it has no awareness of events after the training cutoff.
- **Hallucination.** Because the model is trained to predict the next plausible token — not to retrieve verified facts — it can generate text that sounds confident and fluent but is factually wrong (hallucination, introduced in topic 3.2). Understanding that generation is probabilistic and does not involve fact-checking helps explain why this happens [2].
- **Repetition and context drift.** When the decode phase runs for many tokens, the model can drift off topic or repeat itself, partly because the growing output itself becomes part of the context and can reinforce patterns [3].

## 6. Implementation

### Working With Tokenisation

You do not need to implement a tokeniser to use an LLM, but understanding how to inspect tokenisation helps you work with models more effectively.

**Using a tokeniser library.** For models in the GPT family, the `tiktoken` library (from OpenAI) lets you see exactly how a piece of text is tokenised:

```python
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")
tokens = enc.encode("Hello, world! Tokenisation is fun.")
print(tokens)        # prints a list of integer IDs
print(len(tokens))   # prints the token count
```

For models hosted on Hugging Face (an open-source model hosting platform), the `transformers` library provides tokenisers for each model:

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokens = tokenizer("Hello, world!")
print(tokens["input_ids"])
```

Running code like this on your own text is one of the most effective ways to build intuition about how the model sees your prompts [1].

**Counting tokens before sending.** Most LLM APIs charge per token and enforce context window limits. Estimating token count before sending a large prompt prevents unexpected errors or costs. A rough rule of thumb: 1 English word is approximately 1.3 tokens on average [1].

### Managing the Context Window

The context window is a finite resource. Practical strategies:

1. **Keep system prompts concise.** Every token in your system prompt (the standing instructions you give the model at the start of a conversation) counts against the limit.
2. **Summarise long histories.** In a multi-turn application, summarise earlier conversation turns instead of keeping them verbatim.
3. **Chunk long documents.** If you are asking the model to analyse a document longer than the context window, break it into overlapping segments and process each one separately, then aggregate the results.

### Inference Latency

The two-phase nature of inference (prefill then decode) means:

- **Time to first token** depends mainly on the length of your prompt (prefill cost). A very long prompt takes longer before you see the first word of the response [3].
- **Time to generate the full response** depends on how many tokens the model generates (decode cost). Requesting a short answer is faster than requesting a detailed essay.

Understanding these factors helps you design applications with appropriate timeouts and user-experience expectations.

## 7. Real-World Patterns

### Tokenisation Asymmetries Across Languages

Because LLMs are predominantly trained on English-language text, their tokenisers are optimised for English vocabulary. A sentence in Hindi, Tamil, or Arabic may require three to five times as many tokens as the equivalent sentence in English [1]. This has two practical consequences for teams building multilingual applications:

1. **Higher cost and slower generation** for non-English content, because more tokens are needed per sentence.
2. **Reduced effective context window** for the same amount of information expressed in a non-English language.

This is one reason why localised or language-specific models (trained predominantly on a target language) can outperform generic English-dominant models for vernacular tasks — a pattern increasingly relevant for India's multilingual AI ecosystem.

### Inference Infrastructure at Scale

Large LLMs are deployed on specialised hardware — GPUs (Graphics Processing Units) or TPUs (Tensor Processing Units), types of processors optimised for parallel computation. The autoregressive decode phase is the performance bottleneck in production: generating each token requires a forward pass (one complete run of the input through all model layers to produce an output) through all the model's layers, and this must happen sequentially [3]. This is why LLM inference services invest in techniques like batching (processing multiple users' decode steps together in parallel) to improve throughput.

For practitioners, this means that the choice between a small model and a large model is not just about output quality — it is also about latency, cost, and infrastructure requirements [3].

### Training Data Scale

The scale of training required for a frontier LLM is difficult to overstate. GPT-3, released in 2020, was trained on roughly 300 billion tokens from internet text, books, and code [2]. More recent models use trillions of tokens. The quality and diversity of this training data directly affect what the model knows, what biases it may have absorbed, and how well it handles rare topics or under-represented languages.

## 8. Best Practices

**Do test tokenisation when prompt results are unexpected.** If a model seems to misread a name, a code snippet, or an uncommon word, check how it tokenises that string. A split at an awkward boundary can confuse the model [1].

**Do not assume every word costs one token.** Technical terms, code, URLs, and non-English text can be significantly more token-expensive than plain English prose. Build in a buffer when estimating costs or context window usage [1].

**Do keep prompts purposeful.** Padding a prompt with unnecessary text wastes context window space and can dilute the model's attention on the parts that matter.

**Do not ignore the context window limit.** Applications that silently truncate input when the context window is exceeded can produce responses that miss critical information with no warning to the user. Design explicit handling for this case [3].

**Do match model size to task.** A smaller model may be fast and cheap enough for simple summarisation tasks, while a larger model may be warranted for complex reasoning. The inference mechanics are the same — the difference is the depth of what was learned during training.

## 9. Hands-On Exercise

**Capability Probe — Tokenisation and Context**

1. Go to the OpenAI tokeniser playground (platform.openai.com/tokenizer) or use the `tiktoken` library locally.
2. Paste the same sentence in English and then in a non-English language of your choice (for example, Hindi, Tamil, or Arabic). Compare the token counts — note the ratio.
3. Send a prompt to an LLM asking it to complete the sentence "The most important thing about artificial intelligence is ___." Run it three times without changing the prompt. Note whether the output is identical or varies — and why (hint: generation is probabilistic).
4. Try a very short prompt (five words) and a long prompt (200+ words). Observe the difference in how quickly you see the first response token appear. Reflect on what this tells you about the prefill phase.

Record your observations in Journal Entry #2.

## 10. Key Takeaways

- A **token** is the smallest unit an LLM processes — a subword chunk, not a full word. Text is converted to integer IDs, then to embedding vectors, before any computation happens [1].
- An LLM is trained by repeatedly predicting the next token across billions of examples; every wrong prediction nudges the model's **parameters** (weights) toward a better answer via backpropagation [2].
- The **attention mechanism** inside the Transformer lets each token relate to every other token in the context, enabling the model to understand meaning that depends on relationships between words — such as disambiguating which "bank" is meant in a sentence [2].
- **Inference** runs in two phases: **prefill** (processing your full prompt in parallel) and **decode** (generating output one token at a time, autoregressively). The sequential decode step is why generation is not instantaneous [3].
- The **context window** is the hard limit on how many tokens the model can "see" at once; text beyond this window is invisible to the model during that call, which explains certain "forgetting" behaviours in long conversations [3].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
