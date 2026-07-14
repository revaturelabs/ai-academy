---
topic_id: "6.9"
title: "Cosine similarity — measuring the angle between two meaning-vectors"
position_in_module: 4
generated_at: "2026-06-19T00:00:00Z"
resource_count: 5
---

# 1. Cosine similarity — measuring the angle between two meaning-vectors — Topic Corpus

## 2. Prerequisites

- **6.3 — Vectors:** a vector is an ordered list of numbers where each position represents a specific property. You need this to understand what "two vectors" means.
- **6.5 — Vectors as points in space:** vectors can be plotted as arrows from the origin; closeness in space means similarity.
- **6.6 — The dot product:** multiplying matching positions and summing the results gives a raw score that reflects how much two vectors point in the same direction. The key limitation — it is sensitive to vector length — is the problem cosine similarity solves.

---

## 3. Learning Objectives

By the end of this topic you will be able to:

1. **Define** cosine similarity and explain how it differs from the raw dot product introduced in 6.6.
2. **Explain** why cosine similarity ignores vector magnitude (length) and why that makes it a better measure for comparing word meaning-vectors.
3. **Walk through** the cosine similarity formula step by step — identifying the dot product, the two magnitudes, and the division that produces the final score.
4. **Interpret** a cosine similarity score: a score near 1 means the two vectors point in nearly the same direction (similar meaning), a score near 0 means they are perpendicular (unrelated), and a score near −1 means they point in opposite directions.
5. **Identify** where cosine similarity is used in embedding-based systems, including the nearest-word lookup you saw in 6.8.

---

## 4. Introduction

In topic 6.8 you saw that word embeddings store meaning as directions in a high-dimensional space: "king" points in roughly the same direction as "queen", "man" points in the same direction as "woman". But once you have two such arrows, how do you actually measure whether they agree on direction?

You already know one answer: the dot product from 6.6. Multiply matching positions and add up the results. If the total is large and positive, the vectors point roughly the same way. But there is a catch. Suppose you compare a short sentence to a very long document, or a compact word embedding to a longer sequence embedding. The long one will naturally produce a larger dot product just because it has bigger numbers — not because the meaning is actually closer [1][2]. That is a problem if what you care about is direction (meaning), not size.

Cosine similarity fixes this with one extra step: divide the dot product by the lengths of both vectors. That division cancels out magnitude — it removes the "loudness" of each vector and keeps only the "direction". The result is always a number between −1 and 1, and that range makes scores directly comparable no matter how long or short the original vectors were [1][3].

This one adjustment is what powers modern semantic search, recommendation systems, and the nearest-word lookups you explored in 6.8 [5].

---

## 5. Core Concepts

### 5.1 The problem with the raw dot product

Recall from 6.6 that the dot product of two vectors A and B is computed by multiplying each pair of matching numbers and summing the products:

> A · B = (A₁ × B₁) + (A₂ × B₂) + … + (Aₙ × Bₙ)

This score is high when both vectors have large numbers in the same positions, which usually means they point in the same direction. So far so good.

The problem is that the score is also high simply when the numbers themselves are large — regardless of direction. Imagine the word "the" represented as a vector with modest values like [0.1, 0.2], and the same word doubled in some way to [0.2, 0.4]. The doubled vector has the same direction (it just points twice as far along the same line), but its dot product with any third vector will be exactly twice as large [2].

In practice this matters when you compare embeddings of different lengths or intensities. A long document's embedding tends to have larger raw values than a short tweet's embedding. If you use the raw dot product to ask "which document is most similar to this query?", the long document will score higher than an equally relevant short one — simply because of its size, not its meaning [1][2].

This property is called **magnitude sensitivity** (introduced in 6.6). Cosine similarity removes it [3].

### 5.2 The angle between two vectors as a meaning measure

Every vector can be thought of as an arrow drawn from the origin (the point [0, 0] in 2D, or [0, 0, 0] in 3D) to its coordinates. When you draw two such arrows, they form an angle between them. That angle — called **theta (θ)** — is what cosine similarity actually measures [2][5].

Here is the intuition:

- If two vectors point in **exactly the same direction**, the angle between them is **0°**. The cosine of 0° is **1**.
- If two vectors are **perpendicular** (at a right angle, 90°), the angle is **90°**. The cosine of 90° is **0**.
- If two vectors point in **exactly opposite directions**, the angle is **180°**. The cosine of 180° is **−1**.

Because word meaning is stored as direction in embedding space (from 6.7), the angle between two word vectors is a direct measure of how similar their meanings are [1][5]:

| Angle θ | Cosine score | Meaning |
|---------|-------------|---------|
| 0° | 1.0 | Identical direction — very similar meaning |
| 45° | ≈ 0.71 | Similar direction — somewhat related |
| 90° | 0.0 | Perpendicular — unrelated |
| 135° | ≈ −0.71 | Mostly opposite — contrasting |
| 180° | −1.0 | Opposite direction — antonymous |

The cosine function (**cos**) is a standard maths function that converts an angle into a number between −1 and 1. You do not need to know trigonometry to use cosine similarity — the formula does all the angle work for you [2].

**Why angle and not distance?**

You met distance as a similarity measure in 6.5. Distance is also useful, but it still depends on how far from the origin the points sit. Two vectors with identical direction but different lengths are far apart in distance yet have a cosine score of exactly 1. For meaning-as-direction — which is what embeddings encode — cosine is the more natural measure [5].

### 5.3 The cosine similarity formula and a worked example

**The formula**

$$\text{cosine similarity}(A, B) = \frac{A \cdot B}{|A| \times |B|}$$

In plain words: take the dot product of the two vectors, then divide by the product of their lengths [1][2][3].

Each symbol unpacked:

- **A · B** — the dot product you already know from 6.6: multiply matching positions and sum.
- **|A|** — the **magnitude** (length) of vector A. This is the straight-line distance from the origin to the tip of arrow A. It equals the square root of the sum of each component squared: √(A₁² + A₂² + … + Aₙ²). "Magnitude" and "length" mean the same thing here.
- **|B|** — the magnitude of vector B, computed the same way.
- **|A| × |B|** — the product of the two lengths, which is the largest the dot product could possibly be if both vectors pointed in exactly the same direction. Dividing by it scales the score into the −1 to 1 range [2][4].

The division by |A| × |B| is called **normalisation** — it removes the effect of how large or small the numbers in each vector are, leaving only the directional relationship [3][5].

**Worked example — two 2D vectors**

Let A = [3, 1] and B = [2, 2].

*Step 1 — Dot product (A · B)*

(3 × 2) + (1 × 2) = 6 + 2 = **8**

*Step 2 — Magnitude of A (|A|)*

|A| = √(3² + 1²) = √(9 + 1) = √10 ≈ **3.162**

*Step 3 — Magnitude of B (|B|)*

|B| = √(2² + 2²) = √(4 + 4) = √8 ≈ **2.828**

*Step 4 — Cosine similarity*

cos(θ) = 8 / (3.162 × 2.828) = 8 / 8.944 ≈ **0.894**

A score of 0.894 is close to 1, meaning A and B point in nearly the same direction — they are quite similar [2][3].

Now compare with a vector C = [−2, −1], which is exactly A scaled by −2/3 and flipped to point the opposite way.

A · C = (3 × −2) + (1 × −1) = −6 + (−1) = −7

|C| = √(4 + 1) = √5 ≈ 2.236

cos(θ) = −7 / (3.162 × 2.236) = −7 / 7.071 ≈ **−0.990**

A score near −1 confirms A and C point in nearly opposite directions [2][5].

**The range summarised**

| Score range | Interpretation |
|-------------|----------------|
| Close to 1 | Vectors point in nearly the same direction — high similarity |
| Around 0 | Vectors are roughly perpendicular — little to no similarity |
| Close to −1 | Vectors point in nearly opposite directions — high dissimilarity |

In most text and embedding applications, scores cluster between 0 and 1 (embeddings rarely have negative components), so you will most often see cosine similarity treated as a 0-to-1 scale in practice [1][5].

### 5.4 What normalisation means for comparing word vectors

**Normalisation** (from 5.3 above) is the act of dividing a vector by its own magnitude, producing a new vector with length 1 that preserves only direction. When you normalise before computing the dot product, you are performing cosine similarity [3][4].

Libraries like scikit-learn offer a `cosine_similarity` function that does steps 1–4 automatically [3]. Keras uses a `CosineSimilarity` loss for training models where you want two output vectors to point in the same direction [4].

The practical benefit: once you normalise all your word vectors once, comparing any pair becomes just a dot product — which is very fast, making cosine similarity efficient even in databases with millions of stored embeddings [5].

---

## 6. Step-by-Step Plain-English Walkthrough — "cat" and "kitten"

There is no code in this topic. Instead, here is a full manual walkthrough using two toy 2D word vectors to show exactly how cosine similarity works from start to finish.

**Setup**

Imagine a simple 2D embedding space with two dimensions:
- Dimension 1: "small animal" (higher = more associated with small animals)
- Dimension 2: "domestic" (higher = more associated with things found in homes)

After training, the word vectors are:

- **"cat"** = [4, 3] (fairly associated with small animals, fairly domestic)
- **"kitten"** = [3, 4] (similar, slightly more domestic)
- **"car"** = [0, 2] (not really a small animal, somewhat domestic/household)

**Comparing "cat" and "kitten"**

*Step 1 — Dot product of "cat" and "kitten"*

(4 × 3) + (3 × 4) = 12 + 12 = **24**

*Step 2 — Magnitude of "cat"*

|cat| = √(4² + 3²) = √(16 + 9) = √25 = **5**

*Step 3 — Magnitude of "kitten"*

|kitten| = √(3² + 4²) = √(9 + 16) = √25 = **5**

*Step 4 — Cosine similarity*

cos(θ) = 24 / (5 × 5) = 24 / 25 = **0.96**

A score of 0.96 is very close to 1 — "cat" and "kitten" point in almost exactly the same direction. They are highly similar. This matches our everyday knowledge that kittens are young cats [1][2].

**Comparing "cat" and "car"**

*Step 1 — Dot product of "cat" and "car"*

(4 × 0) + (3 × 2) = 0 + 6 = **6**

*Step 2 — Magnitude of "cat" (already computed)*

|cat| = 5

*Step 3 — Magnitude of "car"*

|car| = √(0² + 2²) = √4 = **2**

*Step 4 — Cosine similarity*

cos(θ) = 6 / (5 × 2) = 6 / 10 = **0.60**

A score of 0.60 is moderate. "Cat" and "car" share the domestic dimension a little but are otherwise quite different — the formula captures this correctly [2][5].

**Interpretation**

| Pair | Cosine similarity | What it says |
|------|-------------------|--------------|
| "cat" and "kitten" | 0.96 | Very similar meaning — nearly same direction |
| "cat" and "car" | 0.60 | Partial overlap — somewhat different direction |

Notice that the raw dot products were 24 and 6 respectively — a ratio of 4:1. The cosine similarity scores are 0.96 and 0.60 — a much smaller contrast because normalisation removed the size advantage. The relative ranking is the same (cat/kitten are more similar than cat/car) but the scores now reflect only direction, not magnitude [2][3].

---

## 7. Real-World Patterns

**Nearest-word lookup in embedding space**

In 6.8 you used vector arithmetic to compute "king − man + woman" and then found the nearest word to the result. The "nearest" step is cosine similarity: compute the cosine score between the result vector and every word in the vocabulary, then return the highest scorer. That is exactly the nearest-neighbour search you used to get "queen" [1][5].

**Semantic search engines**

A semantic search engine converts your query into an embedding vector. It then computes cosine similarity between that query vector and the embeddings of every document in the database. Documents whose embeddings point in a similar direction to the query — same topics, same intent — score near 1 and are returned at the top of the results, even if the exact words differ [1][5].

This is fundamentally different from keyword search (which just counts word matches). Cosine similarity lets the search understand meaning rather than just vocabulary [1].

**Recommendation systems**

A user's taste can be represented as a vector (as you saw with the music taste example in 6.5). Cosine similarity computes which items in a catalogue point in the most similar direction to the user's taste vector. Items with cosine scores near 1 are recommended [5].

**Duplicate and near-duplicate detection**

In content moderation and plagiarism detection, two pieces of text that are paraphrases of each other will have embeddings that point in nearly the same direction — high cosine similarity — even if they share few literal words [2][5].

**Similarity in Keras training**

Keras provides `CosineSimilarity` as a loss function. When training a model to produce embeddings for similar items (images, sentences), the loss pushes the embeddings of matching pairs towards cosine score 1 and diverging pairs towards lower scores [4].

---

## 8. Best Practices

**Use cosine similarity when meaning is direction.**
If your vectors represent meaning, style, topic, or preference encoded as a direction in space, cosine similarity is the right choice. If you are measuring actual geometric distance (e.g. physical location coordinates), Euclidean distance from 6.5 is more appropriate [5].

**Normalise once, compare many times.**
If you will compare one query against thousands of stored embeddings, normalise all stored embeddings once up front (divide each by its magnitude). After that, cosine similarity between the query and any stored vector is just a dot product — the cheapest possible operation. This is how large-scale vector databases are made fast [3][5].

**Scores near 0 do not mean "opposite" — they mean "unrelated".**
A common misreading: "these two things scored 0 so they are opposed." No — perpendicular vectors have no directional relationship (neither similar nor opposite). A score of −1 means opposite. A score of 0 means orthogonal/unrelated [2][5].

**Beware of embeddings with all-positive components.**
Most modern embedding models produce vectors where all values are zero or positive. In that case, the cosine score can only range from 0 to 1 (negative values are impossible). The theoretical −1 to 1 range applies to the full formula; your practical range depends on your specific embedding model [1][2].

**Do not use cosine similarity as a raw distance for clustering.**
Some clustering algorithms expect a true distance metric (e.g. satisfying the triangle inequality). Cosine similarity is not a distance metric. Convert it first: cosine distance = 1 − cosine similarity [3][5].

---

## 9. Hands-On Exercise

**Paper exercise: rank three vector pairs by similarity**

Work through the following steps without a calculator — rough estimates are fine.

You have three vectors:
- P = [1, 0]
- Q = [1, 1]
- R = [0, 1]
- S = [−1, 0]

**Task:** Compute the cosine similarity for each of the three pairs below, then rank them from most similar to least similar.

1. **Pair A — P and Q**
   - Dot product: (1 × 1) + (0 × 1) = ?
   - |P| = √(1² + 0²) = ?
   - |Q| = √(1² + 1²) = ?
   - cos(θ) = dot product / (|P| × |Q|) = ?

2. **Pair B — P and R**
   - Dot product: (1 × 0) + (0 × 1) = ?
   - |P| = 1, |R| = 1
   - cos(θ) = ?

3. **Pair C — P and S**
   - Dot product: (1 × −1) + (0 × 0) = ?
   - |P| = 1, |S| = 1
   - cos(θ) = ?

**Expected answers:** Pair A ≈ 0.707, Pair B = 0.0, Pair C = −1.0. Ranking from most to least similar: Pair A > Pair B > Pair C.

**Reflection question:** Pair B scored 0 — does that mean P and R are opposite? What does a score of 0 actually mean? [2][5]

---

## 10. Key Takeaways

- **Cosine similarity measures the angle between two vectors**, not the distance between their endpoints. Angle captures direction (meaning); distance is affected by how large the numbers are.
- **The formula is: cos(θ) = (A · B) / (|A| × |B|)**. The numerator is the dot product from 6.6; the denominator normalises by the product of both magnitudes, removing size sensitivity.
- **The score always falls between −1 and 1**: near 1 means very similar direction, near 0 means perpendicular/unrelated, near −1 means opposite direction.
- **Normalisation makes comparisons fair**: two vectors with the same direction but different lengths receive a cosine score of 1, regardless of how big or small their numbers are.
- **Cosine similarity powers nearest-word search, semantic search, and recommendation systems** — wherever meaning is stored as direction in an embedding space, this formula is the standard tool for measuring similarity [1][3][5].

---

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
