---
topic_id: 6.7
title: Embeddings — turning words into vectors that capture meaning
position_in_module: 2
generated_at: 2026-06-19T00:00:00Z
resource_count: 3
---

# 1. Embeddings — turning words into vectors that capture meaning — Topic Corpus

## 2. Prerequisites

- **6.3** Vectors — a list of numbers representing multiple properties: you need to know that a vector is an ordered list of numbers where each position maps to a specific property.
- **6.5** A vector as a point in space: you need to know that a vector can be treated as a coordinate in a multi-dimensional space, and that nearby points represent similar things.
- **6.6** Dot product as similarity: you need to know that the dot product measures how much two vectors point in the same direction, giving a similarity score.

## 3. Learning Objectives

By the end of this topic, you will be able to:

1. **Define** what a word embedding is and explain why plain text cannot be fed directly into an AI model.
2. **Explain** why one-hot encoding fails to capture meaning and how embeddings fix that problem.
3. **Describe** how a word embedding places related words close together in vector space.
4. **Identify** at least two real-world AI systems that rely on word embeddings.
5. **Interpret** a small embedding space by reading off which words are neighbours and what that neighbourhood implies about meaning.

## 4. Introduction

Imagine you want to teach a computer to understand the sentence "The cat sat on the mat." The computer does not understand words — it only understands numbers (you learned this in **6.1**). So before any AI can read text, every word has to be converted into numbers.

The simplest approach you might think of: give each word in your vocabulary a unique number. "cat" = 1, "sat" = 2, "mat" = 3, and so on. The problem? Those numbers tell the AI nothing about meaning. To the model, "cat" (1) and "kitten" (2) look almost as unrelated as "cat" (1) and "skyscraper" (500). The gap between the numbers means nothing.

Word embeddings solve this. Instead of a single number, each word is assigned a **vector** — a short list of numbers. The key insight is that these vectors are learned from enormous amounts of text, so words that appear in similar contexts end up with vectors that point in similar directions in space [1]. "Cat" and "kitten" end up close together. "Cat" and "skyscraper" end up far apart. Meaning becomes geometry.

This topic covers what embeddings are, how they are built at a high level, and why placing words as points in space is such a powerful idea. The famous arithmetic trick — "king − man + woman ≈ queen" — is a vivid demonstration of what embeddings make possible; we will name it here and explore exactly why it works in **6.8**.

## 5. Core Concepts

### 5.1 The problem: computers cannot read words

Every AI model is a mathematical function. It multiplies numbers, adds numbers, and finds patterns in numbers (see **6.1**). Text — letters, words, sentences — is not a number. Before a model can process language at all, text must be converted into vectors.

The first and most obvious conversion is called **one-hot encoding**. Imagine your vocabulary has 10,000 words. You create a vector with 10,000 positions — all zeros except for a single 1 in the slot that belongs to the word you are encoding [1]. "cat" might be a vector of 9,999 zeros with a 1 in position 42. "kitten" gets a 1 in position 1,073. Those two vectors share no structure whatsoever — they are perpendicular to each other in that 10,000-dimensional space. The dot product (from **6.6**) of any two different one-hot vectors is exactly zero, meaning "no similarity detected," even for words that are deeply related in meaning [2].

One-hot encoding has two other problems: (a) the vectors are enormous — one dimension per vocabulary word — making them expensive to store and compute with; and (b) adding new words to the vocabulary requires rebuilding the entire vector structure from scratch [3].

### 5.2 What an embedding is

An **embedding** is a dense, low-dimensional vector that represents a word (or a sentence, image, or any object) in a way that captures meaning through geometry [1].

Break that definition down:

- **Dense** means most of the numbers are non-zero. Compare this to one-hot vectors, which are almost entirely zeros.
- **Low-dimensional** means the vector might have 50, 100, or 300 numbers rather than 10,000. Each number is a learned feature — you will not be able to look at position 47 and say "this is the furriness score," but collectively the positions encode meaningful properties [1].
- **Captures meaning through geometry** means that after training, the direction and distance between embedding vectors reflect semantic relationships: synonyms cluster together, antonyms are in predictable directions, and categories form recognisable groups in space.

The result of embedding is that every word becomes a **point in a coordinate space** (from **6.5**). Words that share similar meanings land near each other. Words with opposite meanings land far apart or in opposite directions. The space itself encodes meaning.

### 5.3 How embeddings are learned (the high-level idea)

You do not hand-craft these vectors. They are learned automatically from large amounts of text [1].

The central idea, used by the landmark algorithm **Word2Vec** (published by researchers at Google in 2013), is the **distributional hypothesis**: words that appear in similar contexts tend to have similar meanings [1]. "Cat" and "dog" both appear near words like "pet," "food," "vet," and "walked." So after training, their vectors end up close together.

Training works like this at a high level:

1. A model is given a target word (say, "cat") and asked to predict the words likely to appear around it — or, in the reverse version, given surrounding words and asked to predict the centre word [1].
2. The model starts with random vectors for every word.
3. Every time it makes a prediction, it checks how wrong it was (the loss value, from **6.2**) and adjusts the vectors slightly to reduce that error.
4. After processing billions of word-context pairs, the vectors have been nudged into positions where the geometry reflects meaning [1].

The learning process is not guided by human definitions. No one tells the model "cat and kitten are related." The model discovers that relationship purely from which words appear near which other words in text.

This is also why embeddings are called **learned representations** — the vectors are not assigned by a rule; they emerge from the training process [2].

### 5.4 The embedding space

Once training is complete, every word in the vocabulary has a vector. Taken together, these vectors define an **embedding space** — a coordinate space (from **6.5**) where meaning has a geometric shape [1].

A few properties of this space worth knowing:

**Similarity is distance.** Words with similar meanings have vectors that are close together in the space. You can measure how close two words are by computing the distance between their points, or by using the dot product (from **6.6**) as a similarity score. This is the same "distance as similarity" idea you met in **6.5** with the taste-space example [1].

**Categories form clusters.** If you could look at the embedding space — which tools like the TensorFlow Embedding Projector let you do — you would see groups: animals cluster together, capital cities cluster together, cooking verbs cluster together [2]. The model learned these groupings without being told what categories exist.

**Relationships have directions.** Word embeddings can encode analogy relationships — for example, "king is to man as queen is to woman" — through vector arithmetic. These analogy relationships, called vector arithmetic, are named here and explored fully in **6.8** [1].

**Embeddings exist for more than words.** The same idea extends to sentences, paragraphs, images, and products. Any object that can be compared for similarity can be given an embedding [2]. A recommendation system, for example, might embed both users and products into the same space so that nearby user-product pairs indicate a strong match.

### 5.5 Dimension count and what it means

A common question: how many dimensions should an embedding have?

In one-hot encoding, the number of dimensions equals the size of the vocabulary — potentially hundreds of thousands. In a typical word embedding, the number of dimensions is a **hyperparameter** (from **6.2**) that you choose before training: 50, 100, and 300 are common choices [3].

More dimensions allow the model to encode more subtle distinctions, but they also require more data to learn well and more computation to use. Fewer dimensions are faster and easier to visualise, but may not capture fine-grained meaning differences.

The TensorFlow Embedding Projector (a free browser tool you will use in the lab) takes high-dimensional embeddings and projects them down to 2D or 3D so you can see the clusters and relationships visually. The 2D picture is a simplified projection, but the clusters and neighbourhoods it reveals are real [2].

### 5.6 One-hot encoding vs. embeddings: the key contrast

| Property | One-hot encoding | Embedding |
|---|---|---|
| Vector size | One dimension per vocabulary word (very large) | Fixed small number (e.g., 300) |
| Most values | Zero | Non-zero |
| Captures meaning | No — all distinct words are equally dissimilar | Yes — similar words are geometrically close |
| Needs training | No | Yes — learned from text data |
| Can do arithmetic on meaning | No | Yes (explored in 6.8) |

[1][3]

## 6. Implementation

There is no programming this week — understanding only. Here is the step-by-step procedure that produces word embeddings, written as a plain-language walkthrough.

**Step 1 — Collect a large corpus of text.**
You need text from which the model can learn context. This might be millions of articles, books, or web pages. The bigger and more diverse the corpus, the richer the resulting embedding space [1].

**Step 2 — Build a vocabulary list.**
List every unique word in the corpus and assign each word an index number. This is your vocabulary. A typical vocabulary might be 50,000 to 1,000,000 words [3].

**Step 3 — Initialise random vectors.**
For each word in the vocabulary, create a vector of your chosen dimension (say, 300 numbers) filled with small random values. These are your starting embeddings — meaningless at first [1].

**Step 4 — Train on context.**
Walk through the corpus. For each word, look at the words nearby (in a window of, say, five words on each side). Feed the model a task: "given the surrounding words, predict the centre word" (or the reverse). The model scores its prediction against the actual word [1][2].

**Step 5 — Update vectors based on error.**
If the model predicted wrongly, adjust the vectors. Words that should appear together get nudged slightly closer in the embedding space; words that should not appear together get nudged slightly apart. The size of each nudge is controlled by the learning rate — a scalar (from **6.2**) [1].

**Step 6 — Repeat for billions of examples.**
After enough repetitions, the vectors have settled into positions that reflect the distributional structure of language. The model has never been told what "similar" means — it learned it from co-occurrence patterns [1][2].

**Step 7 — Store the final weight matrix.**
The final set of vectors is stored as a weight matrix (from **6.4**): rows correspond to words, columns correspond to embedding dimensions. To look up the embedding for any word, you find its row in the matrix [1].

**Using a pre-trained embedding:**
In practice, most projects do not train embeddings from scratch. They download a pre-trained set (such as GloVe, Word2Vec, or FastText) and use those vectors directly. Pre-trained embeddings encode knowledge from billions of words of text that you do not need to gather yourself [2][3].

## 7. Real-World Patterns

### Google Search

When you type a query into Google Search, the system needs to match your words to web pages that may use different words to express the same idea. Google uses embeddings — specifically, large-scale neural embeddings — to convert both your query and indexed documents into vectors in the same embedding space [2]. Pages whose vectors are close to your query vector rank higher, even if they do not share exact keywords. This is why searching "broken leg" can return results about "fractured tibia" — the embeddings know these phrases are close in meaning.

### Spotify and Netflix Recommendation Engines

Recommendation systems face a challenge: how do you decide that a user who loved one song might love another, even if the two songs share no artists, genre tags, or explicit features? Both Spotify and Netflix have published approaches that treat items (songs, shows, movies) as embeddings [2][3]. A user's history of interactions is used to build a "user vector." Items with vectors close to that user vector are recommended. The geometry of the embedding space encodes taste in a way that raw category labels cannot.

### Spam Filters and Sentiment Analysis

Email spam filters and sentiment analysis tools — which decide whether a product review is positive or negative — use word embeddings to understand meaning in context [2][3]. A spam filter trained on embeddings knows that "free money transfer" and "no-cost wire payment" are semantically close, even though the words are different, because both phrases live in similar regions of the embedding space. Without embeddings, the filter would only catch vocabulary it had explicitly seen before in spam.

## 8. Best Practices

**Do: use pre-trained embeddings as your starting point.**
Training embeddings from scratch requires enormous data and computation. Pre-trained embeddings (Word2Vec, GloVe, FastText) were trained on billions of words and capture a rich set of relationships. For most beginner projects, starting from a pre-trained embedding is both cheaper and more accurate [2][3].

**Do: choose an embedding dimension appropriate to your data.**
Larger is not always better. For small datasets or simple tasks, 50–100 dimensions often performs as well as 300 and trains much faster. Treat the dimension count as a hyperparameter to experiment with [3].

**Do: check your embedding space for bias.**
Because embeddings are learned from human-written text, they absorb the biases present in that text. An embedding trained on old news articles may associate certain job titles with one gender. Before deploying a model, inspect the embedding space for unintended associations [1][2].

**Don't: assume one-hot encoding is enough for any language task.**
One-hot encoding is simple but strips out all semantic information. Any task where word meaning matters — translation, search, sentiment analysis, summarisation — requires embeddings or a more powerful representation [1].

**Don't: confuse the embedding vector with a definition.**
An embedding is not a dictionary definition. It is a geometric position that captures patterns of use. A word used ambiguously (like "bank," which can mean a river bank or a financial institution) will have one averaged vector that mixes both senses. Context-sensitive embeddings used in modern language models handle this better — but that is a topic for a later module.

**Don't: skip the visualisation step when learning.**
The TensorFlow Embedding Projector lets you see clustering and neighbourhood structure in 2D. For a beginner, actually looking at how "cat," "dog," "kitten," and "puppy" cluster together — and how they sit far from "skyscraper" — makes the geometry of meaning concrete in a way no written explanation fully can [2].

## 9. Hands-On Exercise

**Paper exercise — mapping a tiny embedding space**

You are given five pre-computed 2-dimensional embedding vectors (simplified for illustration):

| Word | Dimension 1 | Dimension 2 |
|---|---|---|
| cat | 0.9 | 0.8 |
| kitten | 0.85 | 0.75 |
| dog | 0.88 | 0.6 |
| car | −0.7 | 0.3 |
| skyscraper | −0.8 | −0.6 |

**Step 1:** Plot the five points on a piece of paper (Dimension 1 on the horizontal axis, Dimension 2 on the vertical axis).

**Step 2:** Without measuring, rank the five words from "most similar to cat" to "least similar to cat" based on visual distance from the "cat" point.

**Step 3:** Using the dot product formula from **6.6** (multiply matching dimensions, then sum), compute the dot product of "cat" and "kitten," and the dot product of "cat" and "skyscraper." Which is higher?

**Step 4:** Visit the TensorFlow Embedding Projector at `projector.tensorflow.org`, load the default Word2Vec dataset, search for "cat," and check whether the nearest neighbours you see there match your intuition from the paper exercise.

**Reflection question:** Why does a word like "car" land far from "cat" even though both are common nouns? What does that tell you about how embeddings learn similarity?

## 10. Key Takeaways

- An **embedding** converts a word (or any object) into a dense, low-dimensional vector so that meaning is encoded as geometry: words with similar meanings have vectors that are close together in the embedding space [1].
- **One-hot encoding** assigns every word a unique single-1 vector, but has no way to represent meaning — any two distinct words look equally dissimilar to a model that uses it [1][2].
- Embeddings are **learned from context**: a model trained on large text corpora discovers that words appearing in similar surroundings should have similar vectors, without being given any explicit definitions [1].
- The **embedding space** is a coordinate space where categories cluster, relationships have directions, and similarity is measurable using the distance and dot-product tools you have already learned (topics 6.5 and 6.6) [1][2].
- Word embeddings power real-world AI systems including search engines, recommendation systems, and spam filters by allowing those systems to handle meaning rather than just exact keyword matches [2][3].

## 11. Next Steps

_Next topic: **6.8 — Why 'king − man + woman ≈ queen' works** — explores the geometric arithmetic that makes analogical reasoning possible in embedding spaces._
