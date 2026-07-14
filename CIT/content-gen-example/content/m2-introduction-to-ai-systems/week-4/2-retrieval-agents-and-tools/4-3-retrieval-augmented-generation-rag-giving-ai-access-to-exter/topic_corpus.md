---
topic_id: "4.3"
title: "Retrieval-Augmented Generation (RAG) — giving AI access to external knowledge at query time"
position_in_module: 1
generated_at: "2026-06-16T00:00:00Z"
resource_count: 3
---

# 1. Retrieval-Augmented Generation (RAG) — giving AI access to external knowledge at query time — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **4.1 — Foundation models — trained once at scale, usable for many tasks:** introduced the foundation model, the concept of adaptation, and the key property that a model's knowledge is frozen at the end of its training run (the knowledge cutoff). Terms such as foundation model, adaptation, generalisation from broad training, and multimodal model are used here without re-defining them.
- **4.2 — Fine-tuning — adapting a foundation model on domain-specific data:** introduced hallucination, zero-shot use, and the idea that fine-tuning is one adaptation method in a broader family. This corpus builds directly on those concepts when comparing RAG to fine-tuning.

RAG is the second named adaptation method covered in this course (after fine-tuning) and belongs to the same family — ways of extending or specialising what a foundation model can do without rebuilding it from scratch.

## 3. Learning Objectives

By the end of this topic, you should be able to:

1. Define Retrieval-Augmented Generation (RAG) in plain language and explain what problem it solves.
2. Describe the three-step RAG pipeline in sequence: retrieve, augment, generate.
3. Explain why RAG reduces hallucination compared with a foundation model used without retrieval.
4. Distinguish RAG from fine-tuning — what each method changes and when each is more appropriate.
5. Give two real-world examples of applications that benefit from RAG and explain why retrieval is the key enabler.
6. Name the advanced technical components of RAG — embeddings, vector databases, similarity search, chunking — and recognise that these are studied in Week 14.

## 4. Introduction

Imagine you are sitting an open-book exam. You are allowed to bring any books and notes you like. You do not need to have every fact memorised — you need to know how to find the right information and use it well in your answers. Now contrast that with a closed-book exam: everything you write must come entirely from memory. If a fact was not in your head before the exam started, you cannot use it.

Foundation models, as introduced in topic 4.1, work like the closed-book exam. When they are trained, they absorb an enormous amount of knowledge from their training data. But once training ends, that knowledge is frozen. The model cannot go and look something up in real time. If you ask it about an event that happened last month, or about a document your organisation published last week, it has no access to that information. It either says it does not know — or, more dangerously, it generates a confident-sounding answer that is wrong. [1]

Retrieval-Augmented Generation — universally shortened to **RAG** — is a method that gives an AI model access to external knowledge at the moment it answers a question. Instead of relying entirely on what was memorised during training, the RAG system first retrieves relevant information from a knowledge source (a document library, a company database, a set of policy files), then feeds that retrieved information to the model alongside the user's question. The model generates its answer using both its trained knowledge and the fresh material it just received. [1][2]

This is the open-book approach to AI. The model is not smarter in the sense of being retrained — it is better informed because it can read before it writes. [2]

RAG is introduced here as one of the key techniques in the 2026 AI stack. You will encounter it again in Week 14, where the full technical implementation is covered. This topic gives you the conceptual model — what problem RAG solves, how the three steps work, and why it matters — without the technical depth that Week 14 adds.

## 5. Core Concepts

### 5.1 The problem RAG solves: frozen knowledge

To understand RAG, you need to understand clearly the problem it is designed to fix.

A foundation model's knowledge comes from its training data. Once training ends, that knowledge is fixed. The model has a **knowledge cutoff**: a point in time after which it has no information. If training ended in mid-2024, the model has no knowledge of events, documents, or developments that occurred after that date. [1]

This creates two practical problems for real-world applications:

**Problem 1 — Outdated information.** The world changes. Laws are updated, products are launched, prices shift, research is published. A model trained in 2024 may give dangerously out-of-date answers about medical treatments, financial regulations, or current events when asked in 2026. [1][3]

**Problem 2 — Private or proprietary knowledge.** No foundation model was trained on your organisation's internal documents — its HR policies, product specifications, customer account records, or internal procedures — because those documents were never part of any public training dataset. A customer-support chatbot that cannot access the company's current product catalogue is not useful. [2][3]

Fine-tuning (topic 4.2) partially addresses these problems but has its own limits. Fine-tuning bakes new knowledge permanently into the model's parameters — which means every update requires a new training run, taking time and money. It also does not work well for rapidly changing information: you cannot fine-tune a model daily to keep up with a live pricing feed or a daily news cycle. [1][2]

RAG takes a different approach: instead of baking new knowledge into the model permanently, it supplies the relevant information to the model at the moment the question is asked. The model's parameters do not change at all. Only the input changes. [1]

### 5.2 The RAG pipeline — three steps

The core mechanism of RAG follows three steps: **retrieve**, **augment**, **generate**. This three-step sequence is exactly what the name describes: Retrieval-Augmented Generation. [1][2]

**Step 1 — Retrieve**

When a user sends a question (also called a **query**), the RAG system does not immediately hand that question to the AI model. First, it searches a knowledge source to find documents or passages that are relevant to the question. [1]

The **knowledge source** is a pre-organised collection of documents that the system is allowed to search — it might be a company's internal policy files, a library of legal contracts, a product documentation set, a news archive, or any other body of relevant text. [2]

The retrieval step finds the passages most likely to contain information relevant to the user's question. At a conceptual level, this is an advanced, meaning-aware search: the system looks through the document library and returns the most relevant excerpts. (The technical mechanism — how "most relevant" is measured using a concept called *similarity search* over *embeddings* stored in a *vector database* — is a Week 14 topic. These terms are named here so you know they exist; they are not taught at this stage.) [2][3]

**Step 2 — Augment**

The retrieved passages are combined with the user's original question to form an enriched input. This enriched input is what gets sent to the AI model. [1]

Think of the augmented input as a message that says: "Here is some relevant context I found — [retrieved passages] — and here is the user's question: [question]. Please answer the question using this context together with your own knowledge." [2]

The model never sees the user's bare question in isolation. It always receives the question together with the retrieved supporting material. This is the key mechanical difference between a plain foundation model and a RAG system: the prompt given to the model has been **augmented** — enlarged and enriched — with retrieved information. [1]

**Step 3 — Generate**

With the augmented prompt in hand, the AI model generates its response in the normal way — drawing on both its trained general knowledge and the specific retrieved passages it was just given. [1]

Because the model now has access to accurate, current, relevant information, it can produce a more precise and grounded answer. It does not have to rely entirely on what it memorised during training. If the answer is in the retrieved passages, the model can cite and use it directly. [2][3]

This grounding in actual retrieved text is why RAG substantially reduces hallucination: the model has real material to draw on, rather than having to generate plausible-sounding content from memory alone. [1]

**The three steps together, illustrated:**

```
User question
     │
     ▼
[1] RETRIEVE ──► Search knowledge source ──► Return relevant passages
     │
     ▼
[2] AUGMENT ───► Combine: question + retrieved passages ──► Enriched prompt
     │
     ▼
[3] GENERATE ──► AI model reads enriched prompt ──► Produces grounded answer
     │
     ▼
Response delivered to user
```

[1][2][3]

### 5.3 Why RAG reduces hallucination

**Hallucination** (introduced in topic 4.2) is when an AI model produces output that sounds confident and fluent but is factually incorrect or fabricated. Hallucinations occur most often when the model is asked about information it does not have — recent events, specific documents, or specialist knowledge that was sparse in its training data.

RAG reduces hallucination because it changes what the model is working from. Without RAG, the model generating an answer is essentially drawing from memory — reconstructing what it thinks the answer might be, based on patterns absorbed during training. With RAG, the model is not primarily generating from memory: it is reading a set of provided documents and constructing an answer from material it can see in front of it. [1][2]

This does not eliminate hallucination entirely. The model can still misread or misinterpret retrieved material, and it can still generate content that goes beyond what the documents contain. But the probability of fabricated facts drops significantly when there is accurate source material grounding the response. [3]

A useful analogy: ask a colleague to explain your company's refund policy from memory. Then ask them to read the policy document first and then explain it. The second approach produces more accurate and specific answers — not because the colleague became smarter, but because they had access to the actual source. RAG applies the same principle to AI models. [1]

### 5.4 RAG vs. fine-tuning — choosing the right adaptation method

Both RAG and fine-tuning (topic 4.2) are adaptation methods. Both improve a foundation model's usefulness for specific tasks. But they work differently and suit different situations. [1][2]

| Dimension | Fine-tuning | RAG |
|---|---|---|
| What changes | The model's internal parameters are updated | Parameters stay unchanged; only the input prompt changes |
| When learning happens | Before deployment — during an explicit training step | At query time — information retrieved fresh for every question |
| How to update knowledge | Requires a new training run | Update the document library; no retraining needed |
| Best suited for | Stable domains needing specialist language and tone | Frequently updated information; private or proprietary documents |
| Data required | Labelled training examples (input-output pairs) | A document library to search; no labelled pairs needed |
| Hallucination reduction | Reduces domain hallucination by teaching correct outputs | Reduces hallucination by providing source material at answer time |

[1][2][3]

Fine-tuning and RAG are not competitors — they are often used together. A model might be fine-tuned to adopt the right tone and format for a domain, and also given a RAG pipeline so it always answers from current documents. Each method contributes something the other cannot. [1][3]

**Prefer RAG when:**
- The information changes frequently (news, prices, regulations, inventory).
- The information is private to an organisation and cannot appear in public training data.
- You want the system to cite its source documents, so answers can be verified.
- You need to add knowledge quickly, without the time and cost of retraining. [1][2]

**Prefer fine-tuning when:**
- The task requires consistent specialist language and tone across all outputs.
- The domain is stable and unlikely to change often.
- The improvement needed is in how the model reasons or responds, not just what facts it has access to. [2]

### 5.5 Named components — what Week 14 will teach

The retrieval step of RAG depends on several technical components. This course names them here so you are aware they exist; you will study each in full in Week 14: *embeddings*, *vector databases*, *similarity search*, and *chunking*. You do not need to understand how any of these work at this stage — knowing their names and that they power the retrieval step is sufficient for now. [2][3]

## 6. Implementation

_No coding is required in this course. The conceptual flow of a RAG system is fully described in Section 5.2._

One operationally important fact: setting up a RAG system does not require retraining or modifying the AI model at all. The knowledge source is built and maintained completely separately from the model. This means an organisation can update the document library — add new documents, remove outdated ones, reflect policy changes — without touching the AI model itself. Updates take effect immediately at query time, for all users, with no deployment of a new model version. [1][2]

## 7. Real-World Patterns

RAG is one of the most widely deployed AI patterns in enterprise settings as of 2025–2026. Its core advantages — no retraining required, easy knowledge updates, source-grounded answers — make it the default choice for many organisations deploying AI on internal or frequently changing knowledge. [1][3]

**Enterprise document Q&A**
The most common RAG deployment: an organisation uploads its internal documents — HR policies, product manuals, compliance guidelines, financial reports — into a document library. Employees ask questions in natural language and receive answers grounded in those specific documents, with references to the source passages. Without RAG, a general foundation model would have no access to proprietary internal knowledge. [1][2]

**Customer support chatbots**
A support chatbot powered by RAG can access the current product catalogue, updated pricing, and the latest FAQs at the moment each customer asks a question. If a product is discontinued or a price changes, the document library is updated and the chatbot immediately reflects the change — no retraining needed. [1][3]

**Legal and compliance**
Law firms and compliance teams use RAG to query large libraries of legislation, regulation, and case law. The model retrieves the relevant legal text and constructs an answer grounded in it, rather than relying on training-data recall that may be outdated or incomplete for specialist jurisdictions. [3]

**Healthcare reference**
Hospitals and health-technology companies deploy RAG systems that allow clinicians to query current clinical guidelines, drug interaction databases, and recent research. The knowledge source is updated as guidelines change, keeping the system current without retraining. [2][3]

**News and current events**
Media organisations and research tools use RAG to allow users to ask questions about recent events, connecting a general-purpose large language model (LLM) to a continuously updated article database. This directly addresses the knowledge-cutoff limitation of foundation models. [1][3]

**India-specific context**
Government agencies and large enterprises in India are deploying RAG-based systems to give staff and citizens access to up-to-date policy documents, scheme guidelines, and regulatory information across multiple languages — updating the knowledge source as policy changes, without retraining the underlying model. [2]

## 8. Best Practices

**Keep the knowledge source current.**
RAG's main advantage — access to current information — only holds if the document library is actively maintained. Outdated or poorly curated documents produce answers no better than the model's training data alone. Treat the document library as a living resource that needs the same ongoing care as any organisational knowledge base. [1]

**Document quality matters as much as model quality.**
The quality of retrieval is only as good as the quality of the source documents. Poorly structured, inconsistently written, or internally contradictory documents produce poor retrieval and confused answers. Preparing the knowledge source carefully is a prerequisite for RAG quality. [2]

**Build in attribution.**
One of RAG's strengths is that the retrieved passages are visible in the pipeline — the system knows which documents informed an answer. Building attribution into the user interface (showing which source passages were used) increases trust and allows errors to be traced and corrected. [1][3]

**Combine RAG with fine-tuning when both are needed.**
RAG handles factual grounding; fine-tuning handles tone, format, and domain reasoning style. For demanding enterprise applications, both are often deployed together. [1][3]

**Design queries to be specific.**
Vague questions produce vague retrieval. Educating users to ask precise questions improves the quality of retrieved passages and, consequently, the quality of answers. [2]

## 9. Hands-On Exercise

The week 4 lab includes a live demonstration comparing the same question answered with and without RAG. Before attending the lab, prepare two versions of a question you would want an AI system to answer about a topic that changes frequently — for example, a question about a recent event, a product released in the last year, or an organisation's current policy. Think about what a foundation model relying only on its training knowledge might say, versus what it could say if it had access to a document published this week. Bring your comparison to the lab discussion; this preparation will sharpen what you observe in the live demonstration.

## 10. Key Takeaways

- **RAG (Retrieval-Augmented Generation)** gives an AI model access to external knowledge at query time — it does not change the model's parameters; it changes what the model is given to read before it generates its answer. [1]
- The three-step pipeline is: **retrieve** relevant passages from a knowledge source, **augment** the user's question with those passages to form an enriched prompt, then **generate** a grounded answer from that enriched input. [1][2]
- RAG reduces hallucination because the model generates its answer from actual retrieved source material, rather than relying entirely on patterns memorised during training. [1][3]
- RAG and fine-tuning solve different problems and are often used together: fine-tuning changes how the model behaves by updating its parameters; RAG changes what the model knows at the moment it answers, without touching the model. [2][3]
- Advanced RAG components — embeddings, vector databases, similarity search, chunking — power the retrieval step and are taught fully in Week 14. [2]

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
