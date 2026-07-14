---
topic_id: "3.2"
title: "The rise of large language models (LLMs)"
position_in_module: 2
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. The Rise of Large Language Models (LLMs) — Topic Corpus

## 2. Prerequisites

This topic builds directly on **Topic 3.1 — From Symbolic AI to Machine Learning**, which introduced:

- machine learning, deep learning, and artificial neural networks
- the concept of training data and learned parameters
- the role of GPUs in accelerating neural-network training
- the ImageNet / AlexNet milestone (2012) as the turning point for deep learning

It also draws on concepts from Topics 1.1–2.9: algorithm, abstraction, and pattern recognition.

If you have not yet read Topic 3.1, do that first. Every term defined there is used freely here.

## 3. Learning Objectives

By the end of this topic you should be able to:

- Define what a Large Language Model (LLM) is in plain language.
- Describe the sequence of milestones — from early neural-network language work through word embeddings, sequence models, and the Transformer — that made LLMs possible.
- Explain what makes LLMs different from the earlier AI approaches covered in Topic 3.1.
- Identify at least three capabilities that LLMs demonstrate and two limitations they carry today.
- Recognise the names of landmark LLMs (BERT, GPT series) and place them on a rough timeline.

## 4. Introduction

Imagine asking a computer to finish this sentence: "The best way to learn something new is to…"

For most of computing history, a machine would either fail completely or return a stilted, robotic answer by looking up pre-written phrase templates. Then, starting roughly in 2018, something changed. A new kind of AI model — trained on enormous amounts of text from the internet, books, and other sources — began producing answers that sound fluent, relevant, and sometimes surprisingly insightful.

These are **Large Language Models**, or **LLMs**. They are the technology behind tools like ChatGPT, Google Gemini, and Claude (the AI you may be using right now). Understanding where LLMs came from, what they actually are, and what they can and cannot do is one of the most important skills for anyone working in or around technology today.

This topic tells that story — from the early attempts to make machines understand words, through a series of research breakthroughs, to the LLMs that have become a practical tool across industries worldwide. It will not go deep into how LLMs work internally (that comes later); its job is to give you the big picture so that later topics make sense. [1]

## 5. Core Concepts

### 5.1 What is a Large Language Model?

A **Large Language Model (LLM)** is a type of deep-learning model — the kind introduced in Topic 3.1 — that has been trained on vast quantities of text. After training, it can generate, translate, summarise, and answer questions in natural language (everyday human language). [1]

Break that definition into its three parts:

| Part | What it means |
|---|---|
| **Large** | The model has billions of learned parameters — numerical values adjusted during training so the model captures patterns in language. |
| **Language** | Its input and output are text: sentences, paragraphs, code, questions, or answers. |
| **Model** | It is a mathematical pattern-matcher built from an artificial neural network, not a lookup table or a set of hand-written rules. |

The word "large" matters. Earlier language models existed, but they were small enough that their vocabulary and reasoning were limited. The jump to billions of parameters — made possible by more data and far more powerful hardware — is what makes these models qualitatively different from what came before. [1][2]

### 5.2 The road to LLMs: a milestone timeline

LLMs did not appear from nowhere. They sit at the end of a chain of research steps, each one solving a problem the previous approach could not handle. Understanding those steps is what makes the LLM story make sense.

**Step 1 — Early neural-network language work (1980s–2000s)**

Researchers noticed early on that artificial neural networks could in theory learn patterns in sequences of words, not just patterns in images or numbers. The challenge was that language is sequential: the word "bank" means something different in "river bank" and "bank account." A model has to track context across many words to understand meaning.

Early neural-network language models existed but were tiny by today's standards. They could handle short phrases but struggled with long sentences. They were also slow to train on the hardware available at the time. [2]

**Step 2 — Word embeddings: giving words a location in space (2013)**

A major practical breakthrough came with **word embeddings** — a technique for turning each word into a list of numbers (a vector) in such a way that words with similar meanings end up numerically close together.

**Word embedding** — a representation of a word as a list of numbers, where words with similar meanings have similar lists. Think of it as giving each word a coordinate on a map: words that mean similar things land near each other.

The landmark tool was **Word2Vec** (2013, Google). After training on a large text corpus, Word2Vec learned that "king" and "queen" are close in its numerical space, and that the relationship "king minus man plus woman" points toward "queen." The model had captured something about meaning without being told what meaning was. [2]

Word embeddings became a building block that later, larger models would reuse and extend.

**Step 3 — Sequence models: reading text in order (2014–2017)**

Even with good word embeddings, a model needs to read words in order and remember what it read earlier. This is the sequence problem.

**Recurrent Neural Network (RNN)** — a type of neural network that processes inputs one step at a time and passes a summary of earlier steps forward, so later steps know something about earlier ones.

RNNs and a refinement called **LSTMs (Long Short-Term Memory networks)** were designed to do exactly this. They read a sentence word by word, carrying a running "memory" of what they had seen. [2]

RNNs and LSTMs powered the first serious neural machine-translation systems (for example, early versions of Google Translate). They were a genuine improvement over older phrase-based systems. But they had a weakness: the further back in a sentence a word appeared, the harder it was for the model to remember it. A 100-word sentence caused the model to effectively "forget" the opening clause by the time it reached the end. [2]

**Step 4 — The Transformer: the architecture that changed everything (2017)**

In 2017, a team at Google published a research paper titled "Attention Is All You Need." It introduced the **Transformer architecture** — the design that every major LLM today is built on. [1][2]

**Transformer** — an artificial neural network architecture that can process all words in a text simultaneously and connect words to each other regardless of their distance in the sentence. [1]

The key innovation is a mechanism called attention (covered in detail in topic 3.4). The result: **the Transformer solved the long-range memory problem** that held back earlier sequence models, and it opened the door to training much larger models on much more data. [1][2]

**Step 5 — BERT and GPT: the first large Transformer models (2018–2019)**

With the Transformer in place, two landmark models arrived in 2018–2019:

**BERT (Bidirectional Encoder Representations from Transformers)**, released by Google in 2018, was trained to read text in both directions simultaneously (left-to-right and right-to-left). This made it excellent at understanding the meaning of a passage — useful for search, question answering, and text classification. [2]

**GPT (Generative Pre-trained Transformer)**, released by OpenAI in 2018, was trained to predict the next word in a sequence. This made it excellent at generating text — completing sentences, writing paragraphs, answering prompts. Later versions — GPT-2 (2019), GPT-3 (2020), GPT-4 (2023) — scaled up massively in size and capability. [1][2]

| Model | Organisation | Year | Primary strength |
|---|---|---|---|
| BERT | Google | 2018 | Understanding text (search, question answering) |
| GPT-1 | OpenAI | 2018 | Generating text (completions, answers) |
| GPT-2 | OpenAI | 2019 | Larger; fluent multi-paragraph text |
| GPT-3 | OpenAI | 2020 | 175 billion parameters; few-shot task performance |
| GPT-4 | OpenAI | 2023 | Multimodal; near-human on many benchmarks |

**Few-shot** — the ability to perform a new task after seeing only a handful of examples, without any retraining. GPT-3 demonstrated this at scale for the first time. [1]

**Step 6 — Scale and the "pre-train then fine-tune" pattern**

What makes a language model "large" is the combination of three things:

1. A massive training dataset — hundreds of billions of words drawn from the web, books, code repositories, and other sources.
2. A very large number of parameters — GPT-3 has 175 billion; some 2024–2025 models exceed a trillion.
3. Enormous compute — thousands of specialised GPUs running for weeks or months.

The **pre-train then fine-tune** pattern emerged as the standard approach: [1][3]

**Pre-training** — the initial training phase where an LLM learns general language patterns from a very large text corpus. This is expensive and slow.

**Fine-tuning** — a follow-on training phase where a pre-trained model is adapted to a specific task or domain using a smaller, focused dataset. This is relatively cheap compared to pre-training.

This pattern is why the same base model (for example, GPT-3) can be adapted into a coding assistant, a medical-information chatbot, or a language-translation tool without starting from scratch each time. [3]

### 5.3 What LLMs can and cannot do

LLMs are genuinely impressive at some tasks. They are unreliable at others. Knowing the difference is a core skill for responsible AI use.

**What LLMs are good at:**

- **Fluent text generation** — writing emails, summaries, explanations, stories, and code drafts that read naturally. [1]
- **Multilingual tasks** — translating between languages, including languages with limited prior tool support. [3]
- **Summarisation** — condensing a long document into a short paragraph while keeping the main points.
- **Question answering** — answering factual questions from a passage, or drawing on knowledge learned during training.
- **Few-shot adaptation** — doing new tasks from just a few examples in the prompt, without any retraining.

**What LLMs struggle with:**

| Weakness | What it looks like |
|---|---|
| **Hallucination** | The model generates a fluent, confident-sounding answer that is factually wrong or entirely invented. |
| **Arithmetic and precise reasoning** | LLMs were not built as calculators; they often make errors in multi-step maths. |
| **Up-to-date knowledge** | Training data has a cut-off date. The model does not know about events after that date unless given them in the prompt. |
| **Consistency** | Asking the same question twice may produce different answers. |
| **Verification** | The model cannot check whether its answer is true; it generates what looks plausible given its training, not what is factually verified. |

**Hallucination** — when an LLM generates text that sounds correct and fluent but is factually wrong, invented, or misleading. The word is used because the model produces something that is not there, just as a visual hallucination produces something that is not seen. [1][3]

LLM performance is uneven across task types; the shape and structure of that unevenness is examined in topic 3.8. You will begin to observe it firsthand in this week's lab activity. [3]

### 5.4 How LLMs differ from earlier AI approaches

Topic 3.1 covered two earlier paradigms. It is worth placing LLMs clearly in relation to them.

| Approach | How knowledge is encoded | Who does the work |
|---|---|---|
| **Symbolic AI / Expert systems** (1950s–1980s) | Explicit rules written by humans ("IF symptom = fever AND symptom = rash THEN …") | Human experts encode all knowledge as rules |
| **Classic machine learning** (1980s–2010s) | Statistical patterns in structured data; humans engineer the relevant features | Humans choose features; algorithm learns weights |
| **Deep learning** (2012–2017) | Patterns learned from raw data via many-layer neural networks | Architecture chosen by humans; patterns learned from data |
| **LLMs** (2018–present) | Language patterns learned from internet-scale text; fine-tuned for specific tasks | Pre-trained by large organisations; adapted by practitioners |

The critical shift with LLMs is **scale and generality**. Earlier approaches were built for one task: a chess engine plays chess; a spam filter detects spam. LLMs are general-purpose language reasoners — the same pre-trained model can write an essay, translate a sentence, explain a recipe, and sketch a business plan. [1][2]

## 6. Implementation

This topic does not involve implementing an LLM (that is beyond this course). However, the conceptual workflow of using a pre-trained LLM is worth knowing, because it is the practical starting point for all LLM-based applications:

1. A large organisation (OpenAI, Google, Anthropic, Meta, etc.) pre-trains a base LLM on internet-scale text. This costs millions of dollars and takes months. [1]
2. The base model may be fine-tuned on a task-specific dataset by the same or a different organisation. [1]
3. The fine-tuned model is deployed behind an API (a service interface) so applications can send text to it and receive text back. [1]
4. A practitioner accesses the model via that API, writes a **prompt** (the input text), and receives the model's **response**. [1]

**Prompt** — the text you send to an LLM to get a response. It can be a question, an instruction, a partial sentence, or a detailed description of what you want. How prompts are written affects the quality of responses; this is covered in a later topic.

The key insight: from a practitioner's perspective, using an LLM means writing good text input (a prompt) and reading text output (a response). The billions of parameters and terabytes of training data are managed by the provider behind the API. [1]

## 7. Real-World Patterns

**Global language tools.** LLMs now power translation and transcription services that work across hundreds of languages, including languages that older automated tools handled poorly due to limited training data. [3]

**Vernacular and regional language processing in India.** India has 22 scheduled languages and hundreds of dialects. LLMs — particularly models fine-tuned on Indian-language corpora — have opened practical translation, transcription, and content-generation capabilities for Kannada, Tamil, Telugu, Hindi, Marathi, and others at scale. Earlier rule-based and statistical systems required enormous manual effort per language pair; LLMs reduce that barrier substantially. [3]

**Healthcare documentation.** Hospitals and clinics use LLM-based tools to convert spoken or typed notes from clinicians into structured medical records — reducing paperwork time and improving consistency. [1][3]

**Agriculture advisory systems.** In India and other agriculture-heavy economies, LLM-powered tools deliver crop advice, weather alerts, and market pricing information to farmers via simple text or voice interfaces in local languages. [3]

**Software development assistance.** Developers worldwide use LLM-based code-completion and code-review tools (for example, GitHub Copilot, built on GPT-series models) to accelerate writing and debugging code. [1]

**Search and information retrieval.** Major search engines now incorporate LLM capabilities to provide direct answers to natural-language queries rather than only returning a list of links. [1]

## 8. Best Practices

When working with or evaluating LLMs, these heuristics apply:

**Do:**
- Verify important factual claims independently. LLMs hallucinate; trust but check.
- Treat LLM output as a first draft, not a final product. It is a capable collaborator, not an infallible authority.
- Be specific in prompts. A vague instruction produces a vague answer; a detailed, well-framed prompt produces a more useful response.
- Note the training data cut-off date when asking about recent events. If the event is after the cut-off, the model may not know about it.

**Avoid:**
- Using LLM output uncritically for high-stakes decisions (medical diagnoses, legal advice, financial plans) without expert review.
- Assuming the model understood your intent. It is predicting plausible text, not reasoning about your goals.
- Confusing fluency with correctness. A confident, well-written sentence can still be factually wrong.

The unevenness pattern from Section 5.3 is the most important practical reminder here: test the model on your specific task before relying on it, because LLM performance varies in ways that are not always predictable. [3]

## 9. Hands-On Exercise

This links directly to the week's lab activity — the **Capability Probe**.

Try the following with any publicly accessible LLM (ChatGPT, Gemini, Claude, or similar):

1. Give it a creative task (e.g. "Write a short poem about monsoon season in Mumbai").
2. Give it a factual task (e.g. "What is the capital of Karnataka?").
3. Give it a logical task (e.g. "If all cats are mammals and Felix is a cat, is Felix a mammal? Explain your reasoning.").
4. Give it an arithmetic task (e.g. "What is 17 multiplied by 23?").
5. Give it an ethical task (e.g. "Should a hospital use AI to decide which patients are treated first? Give reasons for and against.").

For each task: did the model succeed? Did it give a wrong answer confidently? Did it refuse to answer? Record your observations. You will use these notes for Journal Entry 2 and they feed into Assessment 1.

## 10. Key Takeaways

- A **Large Language Model (LLM)** is a deep-learning model trained on vast quantities of text; it can generate, summarise, translate, and answer in natural language.
- LLMs emerged from a chain of milestones: word embeddings (2013) → sequence models / RNNs (2014–2017) → the **Transformer architecture** (2017) → BERT and GPT (2018–2019) → massive scaling (2020–present).
- The **Transformer** was the key enabling breakthrough: it can process all words at once and connect words regardless of how far apart they are, solving the long-range memory problem of earlier sequence models.
- LLMs are general-purpose: the same pre-trained model can be fine-tuned for many different tasks — a major shift from the one-task AI systems of earlier eras.
- LLMs have real limitations: they **hallucinate** (produce fluent but false text), they have a training data cut-off date, and their performance is uneven — excellent at some tasks, surprisingly poor at others (covered in topic 3.8).

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
