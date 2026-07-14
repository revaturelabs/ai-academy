---
topic_id: "14.4"
title: "When to use RAG — use it when the answer depends on data the model was not trained on"
position_in_module: 4
generated_at: "2026-06-15T00:30:00Z"
resource_count: 3
---

# 1. When to use RAG — use it when the answer depends on data the model was not trained on — Topic Corpus

## 2. Prerequisites

- Topic 14.1 — Vector databases: you know what embeddings and vector databases are, and how similarity search works.
- Topic 14.2 — The RAG retrieval pipeline: you know what RAG (Retrieval-Augmented Generation) is and how the query → embed → retrieve → inject → generate pipeline works.
- Topic 14.3 — Why RAG reduces hallucination: you understand parametric memory, evidence-grounded generation, and the knowledge cutoff limitation.

All terms from those topics are used freely here without re-definition.

## 3. Learning Objectives

- State the core decision rule for RAG in plain language: use it when the answer lives in data the model was never trained on.
- Identify the four signals that indicate RAG is the right choice: freshness, private data, precision, and cost-benefit.
- Distinguish RAG from fine-tuning and explain which problem each one solves.
- Apply a simple decision framework to a real scenario and justify the recommendation.
- Recognise when RAG adds unnecessary complexity — and when a simpler approach is sufficient.

## 4. Introduction

You now know how RAG works from the inside — the pipeline, the retrieval, the prompt construction, and why it reduces hallucination. But knowing *how* something works is different from knowing *when* to use it.

RAG adds real cost. You need to maintain a vector database. You need to run an embedding model on every query. You need to keep your indexed documents current. For a question the model can already answer well from its training — "explain what a for-loop does" or "write a professional email declining a meeting" — adding RAG overhead just makes the system slower and more expensive with no accuracy benefit.

The decision is not "RAG or nothing." It is "does this problem actually need RAG?" The answer comes down to one core question: **does the answer live in data the model was never trained on?** [1]

If yes — the answer is in a document the model has not seen, or in information that is newer than the model's training cutoff — then RAG is the right tool. If no — the model already has reliable knowledge about this — then RAG adds cost without benefit, and you should not use it.

This topic gives you a practical framework for making that call, and it contrasts RAG with the other major approach: fine-tuning. By the end, you will be able to look at a real-world AI task and make a reasoned architectural recommendation. [1][2]

## 5. Core Concepts

### 5.1 The Core Decision Rule

The single most useful heuristic for deciding whether to use RAG comes from IBM's guidance on the topic [1]:

> **Use RAG when the answer lives in data the model was not trained on.**

That sentence is short, but it has real precision. Break it down:

- **"the answer lives in data"** — the question requires specific facts, not general reasoning ability. Specific facts can be: a policy document, a product specification, a recent news article, a private company database.
- **"the model was not trained on"** — this data is either (a) private, so it was never in the model's training corpus, or (b) created after the model's knowledge cutoff, so the model could not have seen it, or (c) so domain-specific and obscure that even if a version was in training data, the model's memory of it is unreliable.

If the question depends on those kinds of facts, RAG is appropriate. If the question depends only on general, well-represented knowledge that is stable over time — how to write a Python function, what the French Revolution was, how to structure a business letter — the model already knows this well and RAG adds no value. [1][2]

A simple test: *If you removed the LLM from the internet and locked it in a room with nothing but its training data, could it still answer this question correctly and reliably?* If yes, skip RAG. If no, RAG is the right call.

### 5.2 The Four Signals That Point Toward RAG

There are four practical situations where the core decision rule fires. Each is a different reason why the answer lies in data the model has not seen. [1][2][3]

**Signal 1 — Freshness**

The model's training has a cutoff date. Information published after that date does not exist in the model's parametric memory (the concept you learned in 14.3). If your question is about something time-sensitive — current prices, today's news, this week's policy update, the most recent version of a software library — the model cannot answer from memory. RAG over an up-to-date document store fills the gap.

Example: "What is the current interest rate set by the Reserve Bank?" A model trained in 2024 cannot know what the rate is today if it has changed since then. A RAG system indexed against the central bank's current website can answer accurately.

**Signal 2 — Private Data**

The model was trained on publicly available text. Your company's internal documents — employee handbook, contracts, project wikis, support tickets, product roadmaps — were never in that training data. The model has no knowledge of them. If an answer depends on private organisational knowledge, RAG over a private vector database is the only way to make that knowledge accessible to the model at query time. [1][2]

Example: "What is the on-call rotation policy for the infrastructure team?" This information exists only inside the company. The model cannot answer from training. A RAG system over the internal HR wiki answers immediately.

**Signal 3 — Precision**

Some answers require exact facts: exact dollar amounts, exact legal clause wording, exact product specifications. Language models are good at understanding and reasoning, but they are not reliable fact stores for specific, low-frequency details. Parametric memory is fuzzy — trained on many documents, the model often returns a plausible approximation rather than the precise fact. [1][3]

RAG retrieves the actual document and puts the exact text in front of the model before it generates. The model then reads and reports the precise fact rather than approximating it from memory.

Example: "What is the exact warranty period for the Model 7 industrial pump?" The precise warranty terms live in a product specification document. A model answering from memory might say "typically one to two years" based on similar products it has seen. A RAG system retrieves the spec sheet and reports the actual number.

**Signal 4 — Cost-Benefit**

RAG is not free. It adds:
- Latency: an extra embedding call and a database search before every LLM call
- Infrastructure cost: a vector database to host, maintain, and keep current
- Operational complexity: you must keep the indexed documents up to date

These costs are worth it when the accuracy benefit is large — when the model's unassisted answer would be wrong or unreliable. They are not worth it when the model's unassisted answer would be correct anyway. [2]

The cost-benefit signal is a check on the other three. If the question is about current data but the data changes only once a year, the freshness problem may be small enough that an occasional outdated answer is acceptable. If the question requires precision but the exact fact is stable and prominent in training data (for example, the boiling point of water), the precision problem does not apply. Always weigh the actual accuracy gap against the actual infrastructure cost. [2][3]

### 5.3 When NOT to Use RAG

It is just as important to know when to skip RAG. Use the model's parametric knowledge directly when:

- **The question is conceptual or procedural.** "Explain how a for-loop works." "How do I write a professional email?" These are general knowledge questions the model answers reliably from training.
- **The answer is stable, well-represented, and publicly known.** Historical facts, established scientific knowledge, widely used programming patterns — if these have been stable for years and are in millions of training documents, the model's memory is reliable.
- **You are generating content, not retrieving facts.** Writing a draft, brainstorming ideas, rephrasing text — these tasks use the model's language capability, not its fact recall. RAG does not improve creative or generative tasks.
- **Latency is critical and the accuracy gain is marginal.** If a real-time system needs sub-100 ms responses and the model's unassisted accuracy is already high, the retrieval step may not be worth the added latency.

Adding RAG to a system that does not need it is a form of over-engineering. It increases cost and introduces new failure modes without improving outcomes. [1][2]

### 5.4 RAG vs. Fine-Tuning — Two Different Problems

The most common confusion among practitioners new to RAG is conflating it with **fine-tuning** — a different technique that is sometimes described as an alternative. They are not alternatives for the same problem. They solve fundamentally different problems. [1][2][3]

**Fine-tuning** means continuing to train a language model on a new, specific dataset. This updates the model's parametric memory — the knowledge baked into its weights. Fine-tuning teaches the model new *behaviour*: how to respond in a particular style, how to follow a particular format, how to reason in a specific domain the way domain experts reason.

**RAG** does not change the model at all. It changes what information is placed in front of the model at query time. The model's weights are unchanged; you are expanding what the model can see right before it answers.

| | RAG | Fine-tuning |
|---|---|---|
| What it changes | The prompt at query time (adds retrieved documents) | The model's weights (adds new knowledge and patterns) |
| Best for | Questions that need current or private facts | Teaching new style, format, or reasoning patterns |
| Data stays fresh? | Yes — update the vector database; model unchanged | No — model must be retrained when knowledge changes |
| Cost structure | Per-query retrieval cost; vector database infrastructure | One-time training cost (can be significant); model storage |
| Solves knowledge cutoff? | Yes | No — the fine-tuned model has its own cutoff |
| Private data problem? | Yes — private documents indexed in vector database | Partially — data is baked into model weights; harder to audit or remove |
| Requires retraining the model? | No | Yes |
| When wrong, how to fix? | Update or add documents in the vector database | Retrain or fine-tune again |

The IBM framework summarises the distinction clearly: **use RAG when the answer is a matter of facts the model does not have; use fine-tuning when the task is a matter of skills or style the model does not have.** [1]

Concrete examples:

- You want the model to answer questions about your company's internal policy documents that change every quarter. → **RAG.** The model needs access to current, private facts. Fine-tuning would bake in the policy as of training time and would require retraining every quarter.
- You want the model to respond in your company's brand voice — short sentences, specific terminology, a particular tone. → **Fine-tuning.** This is a style and behaviour change, not a facts-access problem. RAG cannot teach the model a new style.
- You want the model to answer questions about documents published this week. → **RAG.** Fine-tuning cannot solve the freshness problem because a fine-tuned model has its own training cutoff.
- You want the model to specialise in a narrow technical domain like radiology reporting. → **Fine-tuning.** The model needs to have internalised the reasoning patterns of the domain, not just access to documents.

In many production systems, RAG and fine-tuning are used together: fine-tuning shapes how the model behaves, RAG ensures it has access to the right facts. But when you can only choose one, the table above is your guide. [1][2]

### 5.5 A Practical Decision Framework

Apply these questions in order when you need to decide whether a system should use RAG [1][2][3]:

**Question 1 — Is the answer in documents the model has never seen?**
If yes (private docs, post-cutoff data) → proceed to Question 2.
If no (stable, public, well-known) → skip RAG.

**Question 2 — Does precision matter?**
If yes (exact legal wording, exact prices, specific procedures) → RAG becomes strongly indicated.
If no (approximate, general-purpose answer is fine) → weigh Question 3 carefully.

**Question 3 — Does the data change over time?**
If yes (weekly updates, policy changes, new products) → RAG is almost certainly right. Fine-tuning cannot keep up with rapid change without constant retraining.
If no (stable facts) → fine-tuning is a candidate, but ask whether training costs justify it.

**Question 4 — Is the need about facts or about behaviour?**
If facts → RAG.
If behaviour (style, tone, reasoning pattern, domain expertise) → fine-tuning.

**Question 5 — Is the accuracy gain worth the retrieval overhead?**
Estimate the accuracy gap: how often would the model give a wrong or outdated answer without RAG? If the gap is large, RAG pays for itself. If the gap is small, simpler approaches may suffice.

After working through all five questions, most real-world cases land clearly in one category. The hard cases — usually ones where both style and facts are important — are the cases where RAG and fine-tuning are combined, which is a Semester 2 implementation topic. [1]

## 6. Implementation (conceptual walkthrough — no build required)

The decision framework is the implementation for this topic. Here is how to apply it to a real scenario.

**Scenario: A retail company wants an AI assistant for customer enquiries.**

Step 1 — Write down the specific questions the system will answer:
- "What is your return policy for electronics?" → private, specific, changes seasonally.
- "Is my order #45231 delivered?" → real-time order data from a transactional database.
- "Write a polite response to an angry customer email." → generative task, general capability.
- "Respond in a friendly, casual tone that matches our brand." → style requirement.

Step 2 — Apply the decision framework to each question:
1. Return policy → private data signal + freshness signal + precision signal → **RAG.**
2. Order status → private + real-time data signal → **RAG** (or a direct database lookup, depending on architecture).
3. Drafting a reply → generative task; model's language capability is sufficient → **No RAG.**
4. Brand tone → style/behaviour requirement → **Fine-tuning** (or prompt engineering for simpler cases).

Step 3 — Assess cost-benefit for the RAG use cases:
- Customer enquiries happen thousands of times per day. Wrong answers about return policies damage trust. The accuracy benefit is high. The infrastructure cost is justified. → **Build with RAG.**

This is the decision process in practice. The framework is not a formula — it is a checklist that forces you to think through each signal before committing to an architecture. [2][3]

## 7. Real-World Patterns

**Enterprise customer support** is the most common first RAG deployment [1][2]. A company's support team answers the same questions about products, policies, and procedures hundreds of times per day. The model cannot answer from training (private, specific, changing). RAG over the support knowledge base solves this cleanly.

**Legal and compliance Q&A** [3]. Regulation changes frequently. Exact wording matters — the precision signal is high. The relevant documents are authoritative but lengthy. RAG retrieves the specific clause or regulation section rather than asking a model to recall legislation from training, where it may have seen an outdated version or no version at all.

**Medical knowledge assistants** [1]. Clinical guidelines, drug databases, and treatment protocols are updated regularly and require exact facts. Parametric memory is unreliable for exact dosages and interaction details. RAG over current clinical reference databases provides grounded answers.

**Internal IT and HR knowledge bases** [2]. Employees ask questions about internal tools, security procedures, and HR policies. This is private data — definitionally not in the model's training corpus. RAG over the company's internal documentation is the standard solution.

**When practitioners chose fine-tuning instead — and regretted it** [1][3]. Early adopters sometimes fine-tuned models on company documents hoping to "teach" the model the company's knowledge. The problem: the knowledge was then baked into the model weights as of training time. When policies changed, the model confidently gave outdated answers. Updating required another expensive training run. RAG avoids this by separating the knowledge store from the model — the database updates; the model stays fixed.

## 8. Best Practices

**Start with the question, not the tool.** Before deciding to use RAG, write down the specific questions your system will answer. Then apply the decision framework to those questions — not to the general category of application [1].

**Do not use RAG as a default.** RAG is not "the right way to build AI applications." It is the right way to build AI applications that need current or private facts. Overusing it adds cost and new failure modes without improving outcomes [2].

**If you choose RAG, commit to corpus maintenance.** The most common failure mode after deploying RAG is a stale vector database. Policies change, products are discontinued, prices update. Build a process for keeping indexed documents current before you build the retrieval system [3].

**Prefer RAG over fine-tuning for private data.** Fine-tuning on private data bakes that data into the model weights. This creates auditing risks — it is harder to verify exactly what the model "knows," and harder to remove a piece of information if it later becomes sensitive. RAG keeps private data in the vector database, where it can be versioned, audited, and deleted independently of the model [1][2].

**When in doubt about RAG vs. fine-tuning, ask: does the answer change over time?** If yes, lean toward RAG. Fine-tuning on data that changes requires retraining every time the data changes — which is expensive and slow [1][3].

## 9. Hands-On Exercise

This is a written reflection exercise, not a coding task.

**Journal Entry #9 — Architectural Decision:**

Your course lab activity asks you to write a one-paragraph architectural decision for your capstone domain system: does it need RAG, fine-tuning, both, or neither?

Work through these steps:
1. Write down three to five questions your domain system will need to answer.
2. For each question, apply the five-question decision framework from section 5.5. Note which signals fire.
3. Based on that analysis, write a one-paragraph recommendation with your reasoning.
4. Identify what documents or data would go into the vector database if you chose RAG — and how often those documents would need to be updated.

The goal is not a single correct answer — different domains will land differently. The goal is a reasoned argument that uses the framework vocabulary: freshness, private data, precision, cost-benefit, RAG vs. fine-tuning.

## 10. Key Takeaways

- The core RAG decision rule: **use RAG when the answer lives in data the model was never trained on** — private documents, post-cutoff information, or precise domain-specific facts that parametric memory cannot reliably recall.
- Four signals point toward RAG: **freshness** (data changes after the model's cutoff), **private data** (documents the model never saw), **precision** (exact facts matter), and a favourable **cost-benefit** ratio (accuracy gain justifies retrieval overhead).
- **RAG and fine-tuning solve different problems.** RAG provides access to current and private facts at query time without changing the model. Fine-tuning changes how the model behaves — its style, tone, and domain reasoning patterns. If the answer changes over time, RAG is almost always the right choice.
- When an AI task requires only general, stable, public knowledge — or when it is purely generative — RAG adds cost without benefit. Simpler is better.
- A five-question decision framework: (1) Is the answer in unseen documents? (2) Does precision matter? (3) Does the data change? (4) Is the need about facts or behaviour? (5) Does accuracy gain justify retrieval overhead? These questions cover the vast majority of real cases.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
