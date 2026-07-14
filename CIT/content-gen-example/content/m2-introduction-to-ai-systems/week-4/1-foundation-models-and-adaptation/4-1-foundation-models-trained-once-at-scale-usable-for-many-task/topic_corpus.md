---
topic_id: "4.1"
title: "Foundation models — trained once at scale, usable for many tasks"
position_in_module: 1
generated_at: "2026-06-16T00:00:00Z"
resource_count: 3
---

# 1. Foundation models — trained once at scale, usable for many tasks — Topic Corpus

## 2. Prerequisites

This topic builds directly on the following earlier topics in this sequence:

- **3.2 — The rise of large language models (LLMs):** introduced the idea of a model trained on large amounts of text to predict and generate language.
- **3.4 — How LLMs work — tokens, training, and inference:** introduced tokens, the training process (feeding data, adjusting parameters), and inference (running the model to get a response).
- **3.5 — What parameters are and why they matter:** introduced parameters as the numerical settings learned during training that shape a model's behaviour.

These three topics provide the vocabulary used throughout this corpus. Terms such as LLM (Large Language Model), token, training, inference, and parameters are used here without re-defining them.

## 3. Learning Objectives

By the end of this topic, you should be able to:

1. Define what a foundation model is and explain how it differs from the narrow, task-specific AI systems that came before it.
2. Explain what "trained once at scale" means and why the scale of training matters.
3. Describe what "usable for many tasks" means, and give two examples of different tasks the same foundation model can perform.
4. Identify at least three real-world foundation models by name and describe the type of input each one handles.
5. Explain the general idea of adaptation — that a foundation model can be adjusted or guided for a specific use — without confusing adaptation with the original training process.

## 4. Introduction

Think about a human expert who has read millions of books, articles, research papers, and websites. They have absorbed an enormous breadth of knowledge. When you ask them a question, they draw on all that reading. When you ask them to help write a letter, they do that too. They do not have to go back to school each time you give them a new kind of task. They apply what they already know.

Foundation models work in a similar way. A foundation model is an AI system trained on a massive amount of data — text, images, code, or a mix — in one large, expensive training run. After that training is complete, the same model can be used for many different tasks: answering questions, summarising documents, translating languages, writing code, describing images, and more.

This is a significant shift from how AI worked before. Earlier AI systems were narrow — one model recognised faces, a different model translated sentences, another model detected spam. Each model was built and trained for exactly one job. Foundation models broke that pattern. A single trained model became a starting point for dozens of applications. [1]

This topic explains what a foundation model is, what "trained once at scale" really means, and why the same model can be useful for so many different things. Topics 4.2 and 4.3 will cover how foundation models are adapted for specific tasks; this topic establishes the foundation that makes those adaptations possible.

## 5. Core Concepts

### 5.1 What is a foundation model?

**Foundation model** — a large AI model trained on broad, diverse data at massive scale, which can then be adapted or directly applied to a wide range of tasks. [1]

The word "foundation" is deliberate. Just as a building's foundation is not the finished structure but the base everything else stands on, a foundation model is not the finished application — it is the base layer. Developers, businesses, and researchers build on top of it. [2]

A few things distinguish a foundation model from earlier AI:

- **Breadth of training data.** Earlier AI models were trained on narrow, task-specific datasets — for example, thousands of labelled images of cats and dogs to build an image classifier. Foundation models are trained on enormous, general datasets: billions of web pages, books, scientific papers, code repositories, images, and more. [1]
- **Size.** Foundation models contain billions — sometimes hundreds of billions — of parameters (the learned numerical settings introduced in topic 3.5). That size is what allows them to encode so much knowledge. [1]
- **General capability.** Because the training data is so broad, the resulting model develops a general-purpose understanding of language, concepts, and even images. It is not locked into one task. [2]

One important clarification: **LLM (Large Language Model)** and **foundation model** are related but not identical terms. An LLM is a type of foundation model — specifically, one trained primarily on text. But foundation models can also be trained on images, audio, video, or combinations of these. So every LLM is a foundation model, but not every foundation model is an LLM. [3]

**Multimodal model** — a foundation model that can process and generate more than one type of data (for example, both text and images). [2]

### 5.2 Trained once at scale — what this means

The phrase "trained once at scale" has two parts, both important.

**"At scale"** refers to the size and cost of the training process. Training a foundation model requires:

- Enormous datasets — trillions of words and/or millions of images.
- Massive computing power — hundreds or thousands of specialised processors running continuously for weeks or months.
- Significant financial investment — training a leading foundation model can cost tens of millions of dollars. [1]

This scale is why only a small number of organisations — large technology companies and well-funded research labs — have trained foundation models from scratch. Most teams and businesses use models that were already trained by others. [2]

**"Trained once"** means the expensive, large-scale training happens one time (or occasionally, in periodic updates). The resulting model — with all its billions of parameters — is then saved and distributed. Every time someone uses the model to answer a question or generate an image, they are using that single trained result. The model is not retrained from scratch for each new use. [1]

This is the key economic insight: the enormous upfront cost of training is shared across all the uses that follow. A model trained once can serve millions of users and thousands of different tasks. [2]

Why does scale matter for capability? During training, the model adjusts its parameters to get better at predicting patterns in its training data (as explained in topic 3.4). The more data and the more parameters, the more subtle and complex the patterns the model can learn. A small model trained on a small dataset learns basic associations. A large model trained on a vast, diverse dataset learns something that looks much closer to general understanding. [3]

### 5.3 Usable for many tasks — why one model generalises

The most surprising thing about foundation models, when they first emerged, was that a model trained to do one thing (typically: predict the next word in a sequence of text) turned out to be useful for dozens of other things.

Why? Because the patterns that a model learns from enormous, diverse data are not narrow rules. They are deep representations of meaning, structure, and relationships. When a model has processed billions of sentences across every topic imaginable, it does not just learn surface associations. It develops an understanding of how arguments are structured, how technical language differs from casual conversation, how concepts relate across domains, and much more. [1]

This general capability means the same model can handle all of the following:

- Answer a factual question ("What is the capital of France?")
- Write a formal email
- Summarise a long document into three bullet points
- Translate a sentence from English to Hindi
- Generate a short piece of code
- Describe what is happening in an image (for multimodal models)

None of these are separate trained skills. They are all expressions of the same underlying learned representations. [1]

The contrast with earlier, narrow AI is worth making explicit:

| Earlier narrow AI | Foundation model |
|---|---|
| One model per task | One model, many tasks |
| Trained on task-specific labelled data | Trained on broad, diverse data |
| Fixed capability — only does what it was trained for | Flexible — can be prompted or adapted for new tasks |
| Cheap to train (small dataset, small model) | Expensive to train (massive dataset, massive model) |
| Full training cost paid for one use case | Large training cost amortised across many use cases |

[1][2]

### 5.4 The role of adaptation — introduction only

A foundation model is capable out of the box, but it is often not perfectly suited to a specific application without some form of adjustment. That is where adaptation comes in.

There are several ways to adapt a foundation model. You do not need to understand their mechanics yet — each has its own dedicated topic coming up. But it is worth knowing they exist as a category:

- **Prompting** — giving the model written instructions (a "prompt") that guide its behaviour for a specific task, without changing the model itself. You have done this whenever you have typed a question or instruction into an AI chat interface.
- Fine-tuning — continuing the training process on a smaller, domain-specific dataset to specialise the model (covered in topic 4.2).
- RAG (Retrieval-Augmented Generation) — giving the model access to external documents at the moment it answers a question (covered in topic 4.3).

These adaptation methods are what allow a single foundation model to become a customer-service chatbot for one organisation, a medical-records summariser for another, and a legal-document reviewer for a third. [1]

The key point for this topic: adaptation does not replace the foundation model. It sits on top of it. The expensive trained base stays the same; only the layer on top changes.

## 6. Implementation

_Not applicable. This topic is conceptual — there is no procedure or algorithm to demonstrate at this level. No coding is required in this course._

## 7. Real-World Patterns

Foundation models are now a core layer in the AI products and services encountered every day. Here are concrete examples from 2023–2026:

**Text-based foundation models (LLMs)**

- **GPT-4 and GPT-4o (OpenAI)** — the models behind ChatGPT. Trained on a vast corpus of text and code; used for conversation, writing assistance, coding help, and more. [2]
- **Gemini (Google DeepMind)** — Google's family of foundation models, integrated into Google Search, Workspace (Docs, Gmail), and Google Cloud products. [1]
- **Claude (Anthropic)** — a foundation model designed with a focus on safety and helpfulness; the model powering this course's AI interface. [3]
- **Llama (Meta AI)** — an open-weights family of foundation models that organisations can download and run on their own infrastructure. [3]

**Multimodal foundation models**

- **DALL-E, Stable Diffusion, Midjourney** — foundation models trained on text-image pairs; they can generate an image from a text description. [3]
- **Whisper (OpenAI)** — trained on audio; it transcribes speech to text across dozens of languages. [3]
- **GPT-4o** — handles text, images, and audio within a single model.

**In India specifically**

- **Krutrim (Ola)** — India's first publicly announced foundation model, designed to handle Indian languages including Hindi, Tamil, Telugu, Bengali, and others. [3]
- Government and research institutions are actively exploring foundation models adapted for vernacular languages and agriculture — continuing the India AI context from topic 3.7.

The pattern across all these examples is the same: one large model trained once, then deployed or adapted for many specific applications. [1][2]

## 8. Best Practices

When working with foundation models — whether as a user, a student, or someone evaluating which model to use — a few principles are worth keeping in mind:

**Understand what the model was trained on.**
A foundation model's strengths and weaknesses come from its training data. A model trained primarily on English text will perform better in English than in other languages. A model trained on general web data will know less about a specialist medical domain than a model that was subsequently fine-tuned on medical literature.

**Do not assume bigger always means better for your task.**
Larger models are not always better for every application. A smaller, well-adapted model can outperform a larger general model on a specific, narrow task. Size matters most for general breadth; adaptation matters most for task-specific depth. [2]

**Recognise the knowledge cutoff.**
A foundation model's knowledge is frozen at the end of its training run. It does not know about events that happened after that date. It cannot look things up in real time unless it has been given specific tools to do so. This is a direct consequence of the "trained once" property.

**Treat the base model as a starting point, not a finished product.**
Deploying a raw foundation model directly to end users without any adaptation or safety constraints is rarely appropriate. Real products layer instructions, constraints, and often fine-tuning on top of the base model before it reaches users. [1]

## 9. Hands-On Exercise

_The lab activity for week 4 uses a live demonstration comparing results with and without RAG — that exercise is most meaningful after topics 4.2 and 4.3 establish what fine-tuning and RAG are. If you want to explore the concept of "usable for many tasks" right now: visit any publicly available foundation model interface (such as ChatGPT, Gemini, or Claude), and try three very different requests — a factual question, a creative writing task, and a translation. Notice that the same model handles all three without you retraining it. That is "usable for many tasks" in action._

## 10. Key Takeaways

- A **foundation model** is a large AI model trained once on massive, diverse data, which can then be applied to many different tasks — it is a base layer, not a finished application. [1]
- "Trained at scale" means a large, expensive, one-time training process using vast datasets and enormous computing power — a cost shared across all the subsequent uses. [1][2]
- Foundation models generalise across many tasks because broad training produces deep, general-purpose internal representations — not narrow rules for a single job. [1][3]
- **LLMs** are the most common type of foundation model (trained primarily on text), but **multimodal models** extend this to images, audio, video, or combinations. [2][3]
- Foundation models are almost always adapted for specific applications through methods such as prompting, fine-tuning, or RAG — the mechanics of each are covered in the topics that follow (4.2 and 4.3).

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
