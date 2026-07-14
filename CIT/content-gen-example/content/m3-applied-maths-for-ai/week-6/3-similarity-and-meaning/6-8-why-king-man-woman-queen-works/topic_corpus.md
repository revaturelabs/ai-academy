---
topic_id: 6.8
title: Why 'king − man + woman ≈ queen' works
position_in_module: 3
generated_at: 2026-06-19T00:00:00Z
resource_count: 3
---

# 1. Why 'king − man + woman ≈ queen' works — Topic Corpus

## 2. Prerequisites

- **6.3** Vectors — a list of numbers representing multiple properties: you need to know that a vector is an ordered list of numbers where each position maps to a specific property.
- **6.5** A vector as a point in space: you need to know that a vector is a coordinate in a multi-dimensional space, and that nearby points represent similar things.
- **6.6** Dot product as similarity: you need to know that the dot product measures how much two vectors point in the same direction, producing a similarity score.
- **6.7** Embeddings — turning words into vectors that capture meaning: you need to know that word embeddings are dense learned vectors, that similar words land near each other in the embedding space, and that the distributional hypothesis underlies why this works.

## 3. Learning Objectives

By the end of this topic, you will be able to:

1. **Define** what a direction in embedding space means and give an example of a direction that encodes a real-world relationship.
2. **Explain** how the analogy "king − man + woman ≈ queen" can be described as a sequence of vector arithmetic steps.
3. **Describe** why the result of the arithmetic is approximate rather than exact, and what "nearest word" means in that context.
4. **Identify** at least two other analogies that follow the same vector arithmetic pattern.
5. **Interpret** a simple 2D diagram showing words as points with arrows, identifying which arrow represents a shared direction.

## 4. Introduction

Here is a fact that stops most people in their tracks the first time they hear it: if you take the vector for the word "king," subtract the vector for "man," and then add the vector for "woman," the result lands very close to the vector for "queen" [1].

You can write it like this:

> king − man + woman ≈ queen

The "≈" symbol means approximately equal. This is not exact arithmetic — it is a discovery about the structure of an embedding space. It is surprising because nobody programmed the computer to know anything about royalty or gender. The model learned it purely from reading enormous amounts of text [1].

Why does this happen? The answer lies in geometry. Once you understand that words are points in space (from **6.7**), you can ask: what does it mean to move in a particular direction through that space? The answer turns out to be: moving in a direction can correspond to changing a specific property — like gender — while keeping everything else the same.

This topic explains the geometry behind that insight and shows why the arithmetic works the way it does.

## 5. Core Concepts

### 5.1 Meaning becomes geometry: quick recap

In **6.7** you learned that a word embedding places every word as a point in a high-dimensional coordinate space (from **6.5**). Words that appear in similar contexts end up close together. Words with different meanings end up far apart.

This means the space has structure. "Cat," "dog," and "kitten" cluster in one region. "King," "queen," "prince," and "princess" cluster in another. "Paris," "London," and "Berlin" cluster in yet another. The model does not know these are categories. It just discovers that these words appear near the same other words, so it places them near each other [1].

Once words are points in space, you can do geometry with them. You can measure distance. You can measure the angle between vectors using the dot product from **6.6**. And — crucially — you can talk about **direction**.

### 5.2 What "direction" means in embedding space

A **direction** in embedding space is the path you travel when you move from one word's point to another word's point.

Here is the key example. Consider two pairs of words:

- "man" and "woman"
- "king" and "queen"

If you draw an arrow from "man" to "woman," that arrow points in some direction through the space. Now draw an arrow from "king" to "queen." Here is the remarkable finding: those two arrows point in almost exactly the same direction [1][2].

This is not a coincidence. Both arrows encode the same underlying relationship: one is the female version of the other, and everything else about the two words is roughly the same. The direction from the male word to the female word captures the concept of gender. Researchers call this a **gender direction** in the embedding space.

The same pattern appears for other relationships:

- Arrow from "actor" to "actress" points in nearly the same direction as the arrow from "man" to "woman."
- Arrow from "France" to "Paris" points in nearly the same direction as the arrow from "Germany" to "Berlin" — this captures the "country to capital city" direction [1][3].

The embedding space has encoded real-world relationships as geometric directions, purely from learning which words appear near which other words.

### 5.3 The analogy as vector arithmetic

Now you can see exactly why the arithmetic works.

**The goal:** find the word that stands to "woman" the same way "king" stands to "man." In everyday language: the female equivalent of a king.

**The vector arithmetic steps:**

1. **Start at "king."** You have the vector for the word "king" — a point in the embedding space.
2. **Subtract the "man" vector.** Subtracting a vector is the reverse of moving in its direction. This step removes the "male" component from "king," leaving you at a point that represents something like "royalty without gender" [1][2].
3. **Add the "woman" vector.** Adding a vector moves you in the direction of that word. This step adds the "female" component in, pointing you toward the female version of royalty [1][2].
4. **Arrive near "queen."** The point you land on is not exactly the "queen" vector, but it is very close to it. The nearest word in the vocabulary to that landing point is "queen."

You can write this as:

> king − man + woman ≈ queen

Or, reading it as a direction: "the direction from man to woman, applied starting from king, leads you to queen" [1].

The same logic gives you:

- actor − man + woman ≈ actress
- Paris − France + Germany ≈ Berlin
- uncle − man + woman ≈ aunt [3]

In every case, the arithmetic strips out one property (gender, country) and replaces it with another, by travelling the same direction through the embedding space [1][3].

### 5.4 Why it is approximate, not exact

The "≈" in "king − man + woman ≈ queen" is doing important work. The result is not exactly the vector for "queen." Here is why [2][3]:

**The space is high-dimensional and noisy.** A typical Word2Vec embedding has 300 dimensions. The gender direction is not a perfectly clean axis through all 300 dimensions. There is noise — the vectors were learned from statistics, not designed by hand.

**"King" carries more than gender.** The word "king" appears near words like "throne," "crown," "rule," and "monarch" — but also near words like "chess" and "chess piece." Its embedding reflects all of those contexts. Some of those contexts do not apply to "queen." So the arithmetic does not produce a perfect cancellation [2].

**The model never saw an explicit rule.** Nothing told the model "gender is a direction." The model learned it implicitly from patterns in text. Implicit learning is powerful but not exact [1].

So what does "≈" mean in practice? After computing king − man + woman, you get a point in space. You then find the word in the vocabulary whose vector is **nearest** to that point. "Queen" is the nearest word — closer than "princess," closer than "duchess," closer than any other word [2]. That is what it means for the arithmetic to work: not that the result is exactly queen's vector, but that queen's vector is the closest point in the space to the result.

**Vector arithmetic in embedding space is always approximate, and the answer is always the nearest neighbour in the vocabulary** [2][3].

### 5.5 Why it works at all: the distributional hypothesis at scale

The arithmetic works because of the **distributional hypothesis** you met in **6.7**: words that appear in similar contexts end up with similar vectors.

Now think about "king" and "queen." Both words appear near terms like "throne," "crown," "reign," "castle," and "royal court." They differ systematically in exactly one way: "king" appears near male-specific words ("he," "his," "prince," "lord") while "queen" appears near female-specific words ("she," "her," "princess," "lady") [1][3].

Because the model sees thousands of such pairs — man/woman, actor/actress, uncle/aunt, king/queen, prince/princess — it sees a consistent pattern across all of them. There is a set of contexts that co-vary with gender. The model's vectors encode that pattern as a consistent direction [1].

The more word pairs that follow the same pattern, the cleaner and more consistent the direction becomes. This is why the analogy arithmetic works better for common, well-documented relationships (gender, country-capital) than for rare or irregular ones [3].

No one built the gender direction deliberately. The model discovered it by learning from billions of sentences where gendered words appeared in consistent patterns [1].

## 6. Implementation

There is no coding this week — understanding only. Here is the step-by-step plain-English walkthrough of the vector arithmetic.

**Setting:** You have a pre-trained embedding where every word is a 300-dimensional vector. You want to verify that king − man + woman ≈ queen.

**Step 1 — Look up the vectors.**
Find the 300-number vector for "king," the vector for "man," and the vector for "woman" in the embedding table. Each is a row in the weight matrix from **6.4**.

**Step 2 — Subtract the "man" vector from the "king" vector.**
For each of the 300 positions, subtract the "man" number from the "king" number. This gives you a new 300-number vector. Call it the "de-gendered royalty" vector. It is not a real word — it is a point in the space between words.

**Step 3 — Add the "woman" vector.**
For each of the 300 positions, add the "woman" number to your result from Step 2. This gives you another 300-number vector. Call it your result vector. It is still not a real word — it is a landing point in the space.

**Step 4 — Find the nearest word.**
Go through every word in the vocabulary. For each word, compare its vector to your result vector using the dot product from **6.6**. The word with the highest similarity score is your answer. In this case, the nearest word is "queen" [1][2]. The precise tool for this comparison is cosine similarity — you will see the formula in **6.9**.

**Step 5 — Check the margin.**
A useful check: how much closer is "queen" than the next-nearest words? If "queen" scores clearly higher than "princess" or "duchess," the analogy is working cleanly. If the margin is small, the analogy is weak in this particular embedding space [2][3].

**Key point:** Steps 2 and 3 are ordinary addition and subtraction applied position-by-position to the vectors. The only special step is Step 4 — finding the nearest word. Everything else is the basic vector arithmetic you already know.

## 7. Real-World Patterns

### Analogy-based search

The same vector arithmetic that gives you king − man + woman ≈ queen can be used in search and question-answering systems. A system can represent a query like "What is the capital of Spain?" as vector arithmetic: Spain + (France → Paris direction) ≈ Madrid. The system does not need the answer stored as a fact — it computes it geometrically [1][3].

### Detecting and auditing bias in embeddings

Because the embedding space encodes direction as meaning, you can audit it for unintended bias. If you compute doctor − man + woman and the nearest word is "nurse" rather than "doctor," that reveals a gender stereotype absorbed from the training text [2]. Researchers use exactly this technique — applying analogy arithmetic and inspecting the results — to measure and document bias in pre-trained embeddings. This is a direct practical application of analogy arithmetic in responsible AI work [1][2].

### Cross-lingual word alignment

Some multilingual embedding systems train vectors for words from multiple languages in the same space. The analogy idea extends across languages: if you learn the direction from English words to their French equivalents, you can apply that direction to new English words to find approximate French translations — without a dictionary [3]. This is the same arithmetic, applied across a language boundary rather than a gender boundary.

## 8. Best Practices

| Do | Why |
|---|---|
| Check analogies from your embedding to detect bias | The direction structure reveals what the model has learned about gender, race, and other attributes [1][2] |
| Treat the result as the nearest neighbour, not an exact vector | The arithmetic gives a landing point; the answer is whichever real word is closest to that point [2] |
| Try analogies from multiple semantic categories | One working analogy does not prove the whole embedding is good; several categories give a fairer picture [3] |

| Don't | Why |
|---|---|
| Treat the arithmetic as exact | The "≈" is essential — the result is always an approximation [2][3] |
| Assume every analogy will work | The arithmetic is strongest for frequent, consistent relationships; rare ones produce weaker results [3] |
| Use biased analogy results as facts | If an analogy returns a biased result, that is a finding about the training data, not a truth about the world [1][2] |

## 9. Hands-On Exercise

**Paper exercise — draw the direction arrows**

You are given four words placed on a simplified 2D coordinate plane (this is a compressed view of a real 300-dimensional space):

| Word | Axis 1 (horizontal) | Axis 2 (vertical) |
|---|---|---|
| man | 1.0 | 0.5 |
| woman | 1.0 | 2.5 |
| king | 3.0 | 0.5 |
| queen | 3.0 | 2.5 |

**Step 1:** Plot the four points on paper.

**Step 2:** Draw an arrow from "man" to "woman." Note its direction: straight upward (Axis 2 goes from 0.5 to 2.5; Axis 1 stays at 1.0).

**Step 3:** Draw an arrow from "king" to "queen." Note its direction.

**Step 4:** Compare the two arrows. They should be parallel — same direction, same length. This is the gender direction.

**Step 5:** Compute king − man + woman by hand:
- Axis 1: 3.0 − 1.0 + 1.0 = 3.0
- Axis 2: 0.5 − 0.5 + 2.5 = 2.5

The result is (3.0, 2.5) — exactly the "queen" point in this simplified space.

**Reflection:** In a real 300-dimensional embedding the result would land near queen, not exactly on it. Why? Because the real embedding was learned from messy text statistics, not laid out on a clean grid.

## 10. Key Takeaways

- A **direction** in embedding space is the path from one word's point to another. When many word pairs share the same direction — man→woman, king→queen, actor→actress — that direction encodes a real-world relationship such as gender [1].
- **Analogy arithmetic** works by subtracting the source-property vector and adding the target-property vector. king − man + woman applies the gender direction starting from "king" and lands near "queen" [1][2].
- The result is always **approximate**. The arithmetic produces a landing point in the space; the answer is the nearest real word to that point. Nobody programmed this — the geometry emerges from training [1][2].
- The arithmetic works because of the **distributional hypothesis**: words like "king" and "queen" appear near identical contexts except for systematic gender differences. The model picks up that pattern as a consistent geometric direction across thousands of word pairs [1][3].
- Analogy arithmetic has practical uses: analogy-based search, cross-lingual alignment, and — importantly — **bias auditing**, where the direction structure reveals unintended associations the model absorbed from its training data [2][3].

## 11. Next Steps

_Next topic: **6.9 — Cosine similarity: measuring the angle between two meaning vectors** — introduces the cosine similarity formula, the standard tool for finding the nearest word in embedding space after performing vector arithmetic._
