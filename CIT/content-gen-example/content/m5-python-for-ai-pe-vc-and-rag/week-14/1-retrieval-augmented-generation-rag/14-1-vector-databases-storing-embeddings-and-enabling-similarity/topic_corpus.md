---
topic_id: "14.1"
title: "Vector databases — storing embeddings and enabling similarity search at scale"
position_in_module: 1
generated_at: "2026-06-13T00:10:00Z"
resource_count: 4
---

# 1. Vector databases — storing embeddings and enabling similarity search at scale — Topic Corpus

## 2. Prerequisites

- Topic 12.x — Calling an LLM via the API: you have sent text to a language model and received a response. You do not need any mathematics beyond what you learned in secondary school; all new concepts are introduced from scratch.

## 3. Learning Objectives

- Define an **embedding** and explain in plain language what it represents
- Describe why keyword (exact-match) search fails for meaning-based queries, and how a vector database addresses this
- Explain the three-step query process: embed the query → measure distance → return top-k results
- Define **approximate nearest neighbour (ANN) search** and explain why it is necessary at scale
- State what HNSW is and why it is used (conceptual level only — no implementation required)
- Identify at least two real-world scenarios where a vector database is the correct choice

## 4. Introduction

Imagine a company stores ten thousand customer support tickets. A manager types "problems with the payment not going through." A traditional search scans for those exact words. It finds tickets containing "payment" and "through" — but misses the ticket that says "my card kept getting declined at checkout" and the one that says "the transaction failed every time I tried." Different words, same problem.

This is the limitation of keyword search: it matches text, not meaning. The same limitation applies everywhere — searching a research paper library, a product catalogue, a legal database. The words people use to describe a problem rarely match the words used to record the solution.

**A vector database is designed to solve this.** Instead of comparing words, it compares *meaning*. It does this by converting text into numbers in a way that preserves meaning — close meanings produce close numbers. You can then search for "the most similar meaning to my query" instead of "the most exact match to my words."

You have already seen one half of this picture: in weeks 12 and 13 you called a language model through an API. Under the hood, the model converts every word into numbers before doing anything else. A vector database is the storage and search infrastructure built specifically for those numbers. It is a core component of almost every production AI application you will encounter. Understanding it conceptually prepares you to understand the RAG pipeline (topic 14.2) and to make architectural decisions (topic 14.10) with confidence.

## 5. Core Concepts

### 5.1 What is an embedding?

An **embedding** is a list of numbers that represents the *meaning* of a piece of content [1][3]. The list is produced by a specialised machine learning model called an **embedding model**. You give the model a sentence, a paragraph, or even an image, and it outputs a list of numbers — typically 384, 768, or 1536 numbers long. That list is the embedding, and each embedding is also called a **vector**.

Here is a simplified example. Suppose the embedding model outputs only 3 numbers (real models use hundreds or thousands, but 3 is easier to visualise):

| Input text | Embedding (simplified, 3D) |
|---|---|
| "the battery dies too quickly" | [0.91, -0.43, 0.12] |
| "my phone barely lasts through the afternoon" | [0.89, -0.41, 0.14] |
| "chocolate cake recipe with buttercream" | [-0.67, 0.88, -0.54] |

The first two sentences have similar numbers because they express similar meanings (short battery life). The third sentence has very different numbers because its meaning is completely different.

This is the fundamental property of embeddings: **similar meanings produce similar vectors**. The embedding model learns this during training by reading enormous amounts of text and learning which sentences tend to appear in similar contexts. A user complaint about battery life appears near other battery-life complaints; a recipe appears near other recipes.

**High-dimensional space.** Mathematically, a vector with 768 numbers is a point in 768-dimensional space [1]. "Close" means the points are near each other in that space, measured by a distance formula. You cannot visualise 768 dimensions, but the maths works exactly the same way as measuring the distance between two cities on a flat map — just with more coordinates.

**Embedding models are separate from the language model you call for chat.** When you call GPT-4 or Claude to generate text, you are using a *generative* model. When you want to convert text to a vector, you call a separate *embedding* model — for example, OpenAI's `text-embedding-3-small` or Cohere's `embed-v3`. The embedding model outputs a vector, not a text response [3].

### 5.2 What is a vector database?

A **vector database** is a purpose-built database for storing, organising, and searching over large collections of embeddings (vectors) [1]. Think of it as a filing cabinet that is specially designed for lists of numbers — one that can instantly answer the question "which stored items are most similar in meaning to this query?"

A regular SQL database stores rows of text, dates, and numbers. It finds records by matching exact values: `WHERE status = 'pending'` or `WHERE user_id = 42`. This works perfectly for structured, categorical data.

A vector database stores vectors and finds records by *distance*: "which stored vectors are geometrically closest to this query vector in high-dimensional space?" The result is a ranked list of the most semantically similar items, regardless of exact word choice.

Popular vector databases available as of 2025 include **Pinecone**, **Weaviate**, **Qdrant**, **Chroma**, and **pgvector** (an extension for the PostgreSQL database you may already know) [1]. You will not build a vector database in this course. The goal is to understand what they do so you can use them confidently when you encounter them in demos, job descriptions, and production system designs.

### 5.3 Similarity search and distance metrics

When you submit a query to a vector database, the process works as follows:

1. Your query text is passed through the same embedding model used to index the data.
2. The embedding model returns a query vector — a list of numbers representing the meaning of your query.
3. The vector database compares that query vector against every stored vector using a **distance metric** — a formula that measures how far apart two vectors are.
4. The database returns the **top-k** results: the k stored vectors whose distance to the query vector is smallest (i.e., most similar).

**Distance metrics.** Three are commonly used [2]:

| Metric | What it measures | When to use it |
|---|---|---|
| **Cosine similarity** | The angle between two vectors — 1.0 means identical direction (most similar), 0 means perpendicular, −1 means opposite | Default for text embeddings; ignores the length of the vector, only direction matters |
| **Euclidean distance** | Straight-line distance between two points in high-dimensional space | When both the direction and magnitude of the vector matter |
| **Dot product** (inner product) | A combined score of direction and magnitude | Some embedding models are specifically trained to use this metric |

For most text-based AI applications, **cosine similarity is the recommended default** [2]. Which metric to use is determined by the embedding model you chose — the model's documentation specifies which metric it was trained for, and using the wrong one gives bad results.

**Top-k.** The "k" in top-k is a number you choose at search time. Asking for top-5 returns the 5 most similar stored items. Asking for top-20 returns 20. The results come back ranked from most similar to least similar, along with a similarity score so you can judge how close the match is.

### 5.4 Why not compare every vector? The scale problem

If your database holds 100 vectors, comparing your query against all 100 takes a fraction of a millisecond. Easy.

But production AI systems routinely hold millions or hundreds of millions of vectors — every paragraph in a company's entire document library, every product in an e-commerce catalogue, every support ticket from the past five years [3]. Comparing one query vector against 100 million stored vectors, one by one, would take seconds to minutes per search. That is called **exact nearest neighbour search** (also written k-NN), and it does not scale to production workloads.

The solution is **approximate nearest neighbour (ANN) search** — a family of algorithms that skip most of the comparisons and still return results that are correct (or very close to correct) 90–99% of the time, in milliseconds [3]. The trade-off is clear: you might occasionally miss the single best match. For almost all AI applications, "the five most relevant results, found in 10 milliseconds" is far more valuable than "the five perfect results, found in 45 seconds." ANN search is the standard in every production vector database.

### 5.5 How ANN works — HNSW

The dominant ANN algorithm in production vector databases is **HNSW — Hierarchical Navigable Small World** [4]. You do not need to implement HNSW; understanding what it does conceptually is enough to make sense of how vector databases perform at scale.

HNSW builds a multi-layered graph structure over the stored vectors when data is loaded. Think of it like a geographical navigation system:

- **Top layer** — a sparse "highway" network connecting distant landmarks. Very few nodes; each node is connected to its approximate global neighbours.
- **Middle layers** — progressively denser networks, adding regional detail.
- **Bottom layer** — the full, dense neighbourhood graph connecting every vector to its actual nearest neighbours.

When you submit a query vector, the search starts at the top layer: "roughly, which region of the space is this query in?" It finds a good entry point quickly because there are few nodes to check. It then descends through the layers, narrowing down to the specific neighbourhood at the bottom [4].

This is similar to navigating a city: you first look at the country map to find the right city, then the city map to find the right neighbourhood, then the street map to find the right building. At no point do you scan every street in the country. HNSW does exactly this in high-dimensional space.

**Why it matters.** HNSW is the index structure that makes vector databases fast enough to use in real applications. The database builds the index once when you load your data (or incrementally as data arrives) and reuses it for every search query. Without it, similarity search at scale would be impractical [4].

### 5.6 What a vector database actually stores per item

Each record in a vector database has three parts [1][2]:

1. **The vector** — the embedding itself (the list of numbers produced by the embedding model)
2. **A unique ID** — a reference back to the original document, row, or object in your main data store
3. **Metadata** — optional extra fields (document title, author, creation date, product category, etc.) that you can use to filter results before or after the similarity search

The metadata filter is important in practice. You might search for "payment failure" but only want results from tickets created in the last 30 days, or only from a specific product line. The vector database can filter on metadata at query time, combining keyword-style filters with semantic similarity in a single query.

After the search, your application uses the returned IDs to fetch the full document content from wherever you actually store it — a SQL database, a file store, an object store. The vector database answers "which items are most similar?" Your main data store answers "what is the full content of those items?" The two systems work together; neither replaces the other [1].

## 6. Implementation (conceptual walkthrough — no build required)

Understanding the workflow helps you follow live demos and read documentation confidently. You will not write this code in this course; Week 14 is concept and demo only.

**Step 1 — Choose an embedding model.**
Select a model that converts your documents into vectors. The choice depends on the language and domain of your data. Common options: OpenAI `text-embedding-3-small` (general English text, 1536-dimensional vectors), Cohere `embed-v3` (multilingual option), or open-source models from the `sentence-transformers` library. Check the model's documentation for which distance metric to use [3].

**Step 2 — Embed your documents (index time).**
Pass every document (or document chunk) through the embedding model. This produces one vector per document. For a knowledge base of 50,000 paragraphs, you call the embedding model 50,000 times. This step is done once, then repeated only when the knowledge base is updated.

**Step 3 — Load into the vector database.**
Store each (id, vector, metadata) record in the database. The database builds (or updates) the HNSW index. This index build is the expensive one-time cost; searches after that are fast.

**Step 4 — At query time: embed the query.**
When a user asks a question, pass it through the same embedding model used in Step 2. This is critical: query and documents must use the same model. Output is a single query vector.

**Step 5 — Search.**
Send the query vector to the database along with your top-k value and any metadata filters. The database runs ANN search (using the HNSW index) and returns k results with their similarity scores and IDs.

**Step 6 — Use the results.**
Your application retrieves the original document content for those IDs. In a RAG application (topic 14.2), you inject those documents as context into the LLM prompt. In a recommendation system, you display those items to the user.

## 7. Real-World Patterns

Vector databases appear in every AI application that needs to find relevant information quickly [1][2]:

**Semantic document search.** A law firm stores thousands of contracts as embeddings. A lawyer searches "clauses about liability for delayed delivery." Results include clauses worded a dozen different ways — none of which would have been found by keyword search.

**Customer support automation.** A support chatbot embeds the company's FAQ and documentation. Customer question → embedding → top-3 FAQ matches → inject into LLM prompt → accurate, grounded answer. This is the RAG pattern you will learn in topic 14.2.

**Product recommendations.** An e-commerce platform embeds every product description. When a user buys a product, the system finds the 10 nearest products in embedding space and surfaces them as "you might also like." Recommendations are based on semantic similarity, not just purchase history.

**Duplicate detection and deduplication.** A content platform embeds every article. Near-duplicate articles (same story, different wording) cluster together and can be automatically flagged for editorial review.

**Code search.** A development tool embeds every function in a codebase. A developer types a plain-English description of what they want ("a function that sorts a list of dictionaries by a date field") and gets back the most relevant existing functions.

The shared pattern across all of these: **the core question is "what is most similar to this?" and "similar" means semantically similar, not textually identical.**

## 8. Best Practices

**Use the same embedding model at index time and query time [3].** If you embed your documents with model A and your queries with model B, the vectors will be in different mathematical spaces and your results will be random. This is the single most common mistake when first setting up a vector database.

**Store meaningful metadata with every vector [2].** Raw vectors with no labels are hard to debug and hard to filter. Always store at least: (1) the original text or a summary, (2) the source document ID, (3) the date or version. Metadata also enables hybrid search — semantic similarity plus exact filters — which is almost always what production applications need.

**Chunk long documents before embedding.** Embedding models have a maximum input length (typically 512 or 8192 tokens). Long documents must be split into paragraphs or sections before embedding. Choosing the right chunk size and overlap is a practical decision you will encounter in Semester 2 implementation work.

**Vector databases complement, not replace, regular databases [1].** They answer "what is similar?" Regular SQL or NoSQL databases answer "what is exactly this record?" or "what happened between these dates?" Almost all production systems use both, with the vector database sitting in front as the semantic routing layer.

**Approximate is almost always good enough.** For semantic search, returning the 4th most relevant result instead of the 3rd is usually invisible to users. The speed gain from ANN over exact k-NN search is enormous. Default ANN accuracy settings (90–99% recall) are appropriate for nearly every application.

## 9. Hands-On Exercise

After watching today's live RAG demo:
1. In the embedding visualisation, identify two sentences that appear close together. Write down why you think the model placed them near each other.
2. Observe how changing one word in the demo query shifts the top-k results. Which word change made the biggest difference?
3. In your journal (Entry #9), write: "In my capstone domain (\_\_\_\_), a vector database would be useful for \_\_\_\_ because \_\_\_\_." Use the decision-matrix language from topic 14.7 once you reach it.

## 10. Key Takeaways

- An **embedding** is a list of numbers that captures the meaning of text; similar meanings produce numerically close vectors. It is produced by an embedding model, not a chat LLM.
- A **vector database** stores embeddings and finds the most semantically similar ones to a query — not by matching words, but by measuring distance (typically cosine similarity) in high-dimensional space.
- The query process is: embed the query → measure distance against stored vectors → return top-k ranked results.
- **ANN (approximate nearest neighbour) search** makes this fast at scale by skipping most comparisons. **HNSW** is the dominant ANN index algorithm; it works by navigating a multi-layer graph from coarse to fine.
- Each database record contains: the vector, a unique ID linking back to the original content, and optional metadata for filtering. Vector databases work alongside regular databases, not instead of them.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
