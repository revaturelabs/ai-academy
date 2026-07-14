---
topic_id: "14.2"
title: "The RAG retrieval pipeline — query → embed → similarity search → top-k → inject into prompt"
position_in_module: 2
generated_at: "2026-06-15T00:10:00Z"
resource_count: 4
---

# 1. The RAG retrieval pipeline — query → embed → similarity search → top-k → inject into prompt — Topic Corpus

## 2. Prerequisites

- Topic 14.1 — Vector databases: you understand embeddings (lists of numbers representing meaning), vector databases, similarity search, and top-k results.
- Topic 12.x — Calling an LLM via the API: you have sent a prompt to a language model and received a response.

## 3. Learning Objectives

- Define **Retrieval-Augmented Generation (RAG)** in one sentence and explain what problem it solves
- Trace each step of the RAG retrieval pipeline in order: receive query → embed query → similarity search → top-k retrieval → inject into prompt → LLM generation
- Explain what **prompt injection** means in the RAG context (injecting retrieved context into the prompt)
- Describe what the LLM receives as input in a RAG system and how that differs from a standard LLM call
- Identify common failure points at each stage of the pipeline

## 4. Introduction

When you call a language model directly, it answers from its training data — everything it learned before its knowledge cutoff. Ask it "what did our company announce last Tuesday?" and it cannot answer. Its training stopped months or years ago; last Tuesday simply does not exist in its memory.

**RAG — Retrieval-Augmented Generation — solves this by giving the model something to read right before it answers [1].** Instead of asking the model to answer from memory, you first find the most relevant documents from your knowledge base, then hand those documents to the model as part of the prompt. The model reads what you give it and bases its answer on that — not on training data alone.

Think of it like asking a friend a question cold versus handing them the relevant page of a manual first. The friend's general knowledge still helps (how to read, how to reason), but the answer comes from the page you gave them. RAG gives the LLM the right page before asking the question.

You already know two of the building blocks from topic 14.1: embeddings and vector databases. This topic connects those pieces into the full pipeline — showing exactly what happens between a user typing a question and the model producing a grounded answer [2]. Once you can trace the five steps, you can debug where a RAG system goes wrong and understand what to build when you encounter it in a production system.

## 5. Core Concepts

### 5.1 What RAG is — one-sentence definition

**Retrieval-Augmented Generation (RAG)** is a pattern where a language model's input prompt is augmented with relevant documents retrieved from an external knowledge base before the model generates its response [1][3].

Breaking that down:
- **Retrieval** — finding relevant documents from a knowledge base using the vector database from topic 14.1
- **Augmented** — adding those documents to the model's input (the prompt)
- **Generation** — the model producing its response using the retrieved documents and its own reasoning ability

RAG is a *system design pattern*, not a model feature. You apply it to any LLM by wiring up a retrieval step before the generation step. The model itself does not know it is in a RAG system — it only sees the prompt you hand it [3]. This is important: you can add RAG to any existing LLM API call without changing the model. You are changing what goes into the prompt, not the model itself.

The problem RAG solves is simple: LLMs are frozen at their training cutoff. They cannot answer questions about events after that date, about private documents they never saw, or about an organisation's internal knowledge. RAG bypasses this limitation without retraining the model — you just give it the right information at query time.

### 5.2 The five-step RAG retrieval pipeline

The pipeline executes every time a user submits a query [2][4]. Each step has a specific purpose, and each has its own failure mode — knowing both is what lets you debug RAG systems in practice.

**Step 1 — Receive the query.**
The user types a question or request. This is the entry point. Example: "What are the refund terms for annual subscriptions?" The query's phrasing matters: a vague query ("refunds?") will produce a vague embedding and may retrieve irrelevant documents. Most RAG systems pass the user's query through to the embedding step exactly as typed, though some systems add preprocessing such as spell-correction or rewriting ambiguous queries before embedding. Failure mode: query too vague → embedding too general → retrieved chunks are broad and loosely relevant [2].

**Step 2 — Embed the query.**
The query is passed through the embedding model — the *same* embedding model used when the knowledge base was indexed (critical: see §8.1). The model converts the query text into a vector that captures its meaning as a list of numbers. This takes milliseconds [1][3]. The key property is that embedding captures *semantic* meaning, not just keywords: "refund policy for yearly plan" and "money back for an annual subscription" produce very similar vectors, so they retrieve the same documents even though the words differ. This semantic matching is the advantage of embedding-based search over keyword search. Failure mode: using a different embedding model than the one used at index time produces a vector in a different mathematical space — similarity scores will be meaningless and retrieval will silently return the wrong documents (this failure has no error message, which makes it dangerous) [1][3].

**Step 3 — Similarity search over the vector database.**
The query vector is sent to the vector database. Using ANN search (topic 14.1), the database finds stored vectors that are closest in meaning to the query vector. This is fast — milliseconds even over millions of stored documents [2]. The database is not searching for matching words; it is finding documents whose meaning is geometrically close to the query meaning in high-dimensional vector space. Documents about "subscription cancellation" and "money-back guarantee" will rank highly for a refund query even if they never use the word "refund." Failure mode: if the knowledge base does not contain any documents about refund policies, the ANN search returns whatever is least-wrong — often marginally related documents that look plausible but do not contain the answer.

**Step 4 — Top-k retrieval.**
The database returns the top-k most similar document chunks. "k" is chosen by the developer — typically 3 to 10. Each returned item contains three things: the original chunk text, a similarity score (e.g. 0.92), and metadata such as the source URL, the document date, or the section title [4]. The similarity score is useful context for the prompt: a score of 0.92 means the chunk is very likely relevant; a score of 0.50 may be coincidental overlap with no meaningful connection. Failure mode: if k is set too small, the most relevant chunk may be missed because the answer happened to be ranked 4th; if k is set too large, the prompt fills with marginally-relevant content that dilutes focus and increases token cost [4].

**Step 5 — Inject into the prompt and generate.**
The retrieved document texts are formatted and inserted into the LLM prompt alongside the original query. The LLM reads the assembled prompt and generates a response grounded in those documents rather than training memory alone [1][3][4]. The prompt template (§5.4) controls exactly how the context is formatted and what instructions the model receives. This is where the RAG system's quality lives: if the template is well-designed, the model answers from the retrieved context; if it is poorly designed, the model blends retrieved facts with its own training knowledge, reintroducing the hallucination risk RAG was meant to prevent. Failure mode: a prompt template that does not clearly instruct the model to answer from context only — see §5.4 for what that instruction must say.

### 5.3 What the LLM actually receives

In a **standard (non-RAG) call**, the LLM receives:

```
User: What are the refund terms for annual subscriptions?
```

In a **RAG call**, the LLM receives:

```
You are a helpful assistant. Answer the user's question using ONLY the context below.
If the context does not contain the answer, say "I don't know."

Context:
[Document 1, score 0.92]
Annual subscriptions may be refunded within 14 days of purchase. After 14 days,
no refund is available. Contact support@example.com to initiate.

[Document 2, score 0.87]
For subscription changes and cancellations, see help.example.com/subscriptions.
Downgrades take effect at the next billing cycle.

User question: What are the refund terms for annual subscriptions?
```

The LLM reads the context, sees that Document 1 answers the question directly, and responds citing that information. The model's training still shapes *how* it writes the answer — the phrasing, the structure, the tone — but the *facts* come from the retrieved documents [1].

This is the key distinction: **the model's training provides reasoning ability; retrieved context provides the facts**.

The three structural choices in the prompt template above each serve a specific purpose. The system instruction ("Answer using ONLY the context below") is the most important element: without it, the LLM freely mixes retrieved facts with its training knowledge, which sounds authoritative but may contradict or dilute the retrieved documents. The fallback instruction ("say I don't know") is equally critical: without it, the model will hallucinate a plausible-sounding answer when no relevant context was retrieved — exactly the failure mode RAG was designed to prevent. Labelling each document block with its similarity score lets the model weight higher-confidence retrievals, though not all implementations include this detail. Most production failures in RAG systems trace to one of these three elements being missing or ambiguous in the template [2][3].

### 5.4 Prompt templates in RAG

A **prompt template** is the structured wrapper around the retrieved context and the user query [2]. It typically includes:

- A system instruction: "Answer using ONLY the context below"
- A "Context:" block where retrieved documents are inserted
- The user's original question
- A fallback instruction: "If the context does not contain the answer, say 'I don't know'"

Prompt templates are written by the developer and stay fixed across queries. The retrieved content changes with every query; the template structure stays the same. The template is what converts a raw pile of retrieved text into a well-structured LLM input. Why the exact wording of the template instruction matters — and when RAG still fails despite a well-designed template — is covered in topic 14.3.

### 5.5 The two phases of a RAG system

A RAG system operates in two distinct time phases [4]:

**Index phase (done once, or periodically):**
- Documents are split into chunks → each chunk embedded → vectors stored in vector database → HNSW index built
- Can take minutes to hours depending on corpus size
- Users never experience this phase directly
- The index phase can be re-run when new documents are added (overnight batch update is common)

**Query phase (runs on every user query, typically under 1 second end-to-end):**
- User query → embed query → ANN search → top-k retrieved → prompt assembled → LLM call → response returned
- This is what users experience as "the AI answered my question"
- The LLM call is typically the slowest step; embedding + ANN search together are usually under 100ms [4]

The separation of phases matters for system design: the index phase can run in the background without interrupting users, while the query phase must be fast enough to feel responsive. Most production RAG systems keep the embedding model loaded in memory and the HNSW index on fast storage to hit sub-second latency on the query phase. The LLM is only involved in the query phase, and only at the final generation step — not at any point in retrieval.

## 6. Implementation (conceptual — no build required)

The query-phase execution order in application code:

1. User sends query string to the application
2. Application calls embedding model API → returns query vector
3. Application calls vector database: `search(query_vector, top_k=5)` → returns list of `(text, score, metadata)` tuples
4. Application builds prompt string: system instruction + formatted context blocks (each labelled with score + source) + user query
5. Application calls LLM API with the full prompt → LLM returns generated text
6. Application returns the response to the user (optionally with source citations extracted from metadata)

**The LLM never directly accesses the vector database.** The application code orchestrates retrieval; the LLM only sees the assembled prompt [3]. This is the most common misconception — learners sometimes assume the LLM is "browsing" the knowledge base in real time. It is not. It only reads the prompt the application hands it.

**Chunking at index time.** Long documents must be split into chunks before embedding because embedding models have a maximum input length (typically 512 or 8,192 tokens depending on the model). A 20-page document might become 60 chunks of ~200 words. Chunk size involves real trade-offs: chunks that are too small lose surrounding context and retrieve incomplete answers; chunks that are too large bring in too much irrelevant content per chunk, diluting the relevant signal. The optimal chunking strategy — overlapping chunks, sentence-boundary splitting, document-structure-aware splitting — is a Semester 2 implementation topic [2][4].

**Common failure points by step:**
- **Step 1 — Query too vague:** broad query embedding → irrelevant chunks retrieved with high scores
- **Step 2 — Mismatched embedding model:** silent failure, no error; similarity scores are meaningless
- **Step 3 — Missing content in knowledge base:** ANN returns least-wrong chunks, model answers from them confidently
- **Step 4 — k too small or too large:** missed answer, or diluted context overwhelming the relevant chunk
- **Step 5 — Poorly worded prompt template:** model ignores context, mixes training knowledge with retrieved facts

When a RAG system produces a wrong answer, this list is the debugging checklist [2][4].

## 7. Real-World Patterns

RAG is the most widely deployed pattern for production AI applications that need accurate, up-to-date, or private-domain answers [1][3]:

**Customer support automation [1][3].** Help centre articles, policy documents, and product guides are indexed. When a customer asks a question, the top 3–5 most relevant articles are retrieved and handed to the LLM. The LLM produces a specific, accurate answer grounded in the retrieved policy — not a generic paraphrase of what it learned during training. Reduces support ticket volume and agent escalation rates. This is one of the most common first RAG deployments organisations build.

**Internal knowledge search [1][2].** Contract libraries, HR policy documents, engineering wikis, and meeting notes are indexed. An employee asks a question ("What is the parental leave policy for remote employees?") and receives a grounded answer with a source link to the original document. Eliminates manual keyword searching through hundreds of documents and surfaces answers from documents the employee did not know existed.

**Code documentation assistant [2][3].** API documentation, SDK reference guides, and code examples are indexed. A developer asks "how do I authenticate with the payment gateway?" and receives accurate, version-specific instructions from the retrieved documentation — not a generic answer hallucinated from the LLM's training data about a different payment API.

**Research and legal summarisation [3][4].** Published papers, case law, regulatory filings, or financial reports are indexed. An analyst or lawyer asks a question and receives a summary with citations to the retrieved passages. The citations make the answer auditable: the user can click through to the exact source passage that grounded the LLM's response.

**Medical Q&A (retrieval over clinical guidelines) [1][4].** Clinical guidelines, drug interaction databases, and formularies are indexed. A clinician queries "what is the recommended first-line treatment for type 2 hypertension in a patient with CKD?" and receives an answer grounded in the specific retrieved guideline, with the guideline version and section cited. The model does not invent a treatment from training data alone.

The shared structure across all five: **user query → retrieve relevant documents from a specialised knowledge base → model answers from those documents, not from training memory**.

## 8. Best Practices

### 8.1 Use the same embedding model at index time and query time [1][3]

This is the single most critical rule. If documents were embedded with model A but queries are embedded with model B, the vectors exist in different mathematical spaces. Similarity scores will be meaningless, and retrieval will silently fail — the wrong documents will be returned with high confidence scores. No error message is thrown. The only symptom is that the RAG system gives confident, plausible-sounding wrong answers.

### 8.2 Choose top-k thoughtfully [4]

- **Too small (k=1–2):** risk missing the most relevant chunk if the answer was ranked 3rd
- **Too large (k=20+):** prompts grow long, model may lose focus on the most relevant chunk, latency and cost increase
- **Practical starting range:** k=3 to k=7 for most applications; tune experimentally against real queries

### 8.3 Structure your prompt template clearly [2]

- Tell the model explicitly to answer from context only
- Label each context block with its source identifier (file name, URL, section) — enables citations in the response
- Put context *before* the question (models attend more to content placed earlier in the prompt)
- Include a "say I don't know" fallback for queries where the knowledge base has no relevant answer
- Keep the system instruction short and unambiguous — long, hedged instructions produce inconsistent behaviour

### 8.4 Use metadata filtering to sharpen retrieval [3]

Filter by date, department, or product line before the similarity search: "only search documents updated in the last 6 months." This prevents retrieving a highly similar but outdated document — for example, last year's refund policy when the question is about current terms. All major vector databases support metadata filtering at query time, applied before the ANN search runs.

### 8.5 Set a minimum similarity threshold [2][4]

If all top-k results have low similarity scores (e.g., all below 0.60), the knowledge base probably does not contain a relevant answer to the query. Injecting low-confidence chunks into the prompt and asking the LLM to answer from them produces hallucinated-sounding responses that mix poor retrievals with training knowledge. A common pattern: check the top-1 similarity score before assembling the prompt; if it falls below a threshold (tune per system), respond with "I don't have information on that" rather than injecting weak context. This is a simple gate that eliminates a large class of confident-but-wrong RAG responses [4].

## 9. Hands-On Exercise

During today's live RAG demo:
1. Read the retrieved top-k chunks shown on screen before the LLM responds. Predict: does the answer to the user's question appear in these chunks?
2. Observe whether the LLM's response matches what was in the retrieved chunks, or whether it added information from outside those chunks.
3. Note when the demo shows a query where the knowledge base does not contain the answer. What does the system do? Is the similarity score low for all retrieved chunks?

## 10. Key Takeaways

- **RAG** is a system design pattern: retrieve relevant documents from a knowledge base, inject them into the LLM prompt, let the model answer from retrieved context rather than training memory alone.
- The five-step pipeline: receive query → embed query (same model as index time) → similarity search → top-k retrieval → inject into prompt + generate.
- The **LLM only sees the assembled prompt** — the application code orchestrates retrieval; the model handles generation. The LLM does not browse the knowledge base.
- A **prompt template** wraps retrieved context and the user query with a system instruction to answer from context only and a "say I don't know" fallback — both are required to prevent hallucination.
- Each step has a failure mode: wrong embedding model, k too small, missing content, weak template. This list is the debugging checklist when a RAG system produces wrong answers.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
