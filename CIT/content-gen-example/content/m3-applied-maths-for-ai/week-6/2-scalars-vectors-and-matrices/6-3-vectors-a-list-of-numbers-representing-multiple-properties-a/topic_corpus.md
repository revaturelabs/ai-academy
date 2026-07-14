---
topic_id: 6.3
title: "Vectors — a list of numbers representing multiple properties at once"
position_in_module: 2
generated_at: 2026-06-18T00:00:00Z
resource_count: 3
---

# 1. Vectors — a list of numbers representing multiple properties at once — Topic Corpus

## 2. Prerequisites

- **6.1 — Binary representation and data as numbers:** Establishes that all data — images, text, sound — is converted into numbers so a computer can process it, and that finding patterns through arithmetic on those numbers is what AI does.
- **6.2 — Scalars — a single number representing one property:** Defines a scalar (a single number capturing one quantity such as brightness, loss value, or learning rate). Topic 6.3 builds directly on this: a vector is what you get when you collect several scalars and hold them together as one unit.

## 3. Learning Objectives

By the end of this topic you should be able to:

1. **Define** a vector as an ordered list of scalars, where each position captures a different property of the same thing.
2. **Explain** why grouping multiple properties into one vector is more useful than keeping them as separate, unrelated numbers.
3. **Construct** a simple feature vector for a familiar object by deciding which properties to include and assigning a number to each.
4. **Describe** how AI systems use feature vectors to represent real-world things — people, words, images, products — so that patterns can be found through arithmetic.
5. **Identify** the number of elements in a vector (its dimension) and explain why the same position must always mean the same property across all vectors being compared.

## 4. Introduction

Think about how you would describe a song to a friend. You might say it is loud, fast, and happy. That is three separate facts about one song. Now imagine writing those facts as numbers: loudness = 0.8, tempo = 0.6, mood = 0.3. You have just built a **vector** — a compact bundle that represents the song using three numbers in a fixed order [1].

A single number — a scalar, which you met in topic 6.2 — can only capture one fact at a time. Pixel brightness is 142. Loss value is 0.07. Those are clean, but they are incomplete. A real thing — a song, a customer, a medical patient — has many properties at once. A scalar can hold one of them. A vector holds all of them together, in one neat package, ready for arithmetic [1][2].

This is why vectors are one of the most important ideas in applied mathematics for AI. Almost everything an AI model "sees" arrives as a vector: a product description, an image patch, a user's history, a sentence. Once you have a vector, you can feed it to algorithms that detect patterns, measure similarity, and make predictions. None of that is possible if your facts are scattered as separate, unrelated scalars [2][3].

In this topic you will learn exactly what a vector is, how to build one for any real-world thing, and how AI systems use vectors to represent meaning numerically. Operations on vectors — such as comparing two vectors or computing their similarity — come in later topics.

## 5. Core Concepts

### 5.1 What a vector is

A **vector** is an ordered list of numbers, where each number is a scalar and each position in the list represents a specific, named property [1].

The key word is *ordered*. The list `[0.8, 0.6, 0.3]` is not the same as `[0.3, 0.8, 0.6]` even though the three numbers are identical, because position carries meaning. If position 1 means "energy" and position 2 means "tempo" and position 3 means "mood," then the order must be consistent every time you build a vector for a new song [1][2].

A clean way to write a vector is with square brackets:

```
song_vector = [energy, tempo, mood]
            = [0.8,    0.6,   0.3]
```

- **energy** at position 1 = 0.8 (on a 0-to-1 scale, 0.8 is high energy)
- **tempo** at position 2 = 0.6 (moderately fast)
- **mood** at position 3 = 0.3 (fairly calm or serious)

You can read this vector out loud: "This song is high-energy, moderately fast, and calm." The vector compresses that sentence into three numbers in a fixed order [1].

### 5.2 Scalars inside a vector

Each number inside a vector is a scalar — a single magnitude. You already know what scalars are from topic 6.2. In a vector, scalars play a specific role: each one occupies a named slot and contributes one piece of information to the overall description [1].

A useful way to think about this:

| Slot (position) | Property name | Example value | What it means |
|---|---|---|---|
| 1 | energy | 0.8 | High energy |
| 2 | tempo | 0.6 | Medium-fast |
| 3 | mood | 0.3 | Calm / serious |

Every row in that table is one scalar. Together, the three rows form a vector that describes one song. Alone, each scalar is an incomplete description. Together, they form a richer picture [2].

### 5.3 Dimension — how many properties the vector holds

The **dimension** of a vector is the count of how many numbers it contains [1].

- `[0.8, 0.6, 0.3]` is a **3-dimensional** vector.
- `[height, weight, age, income]` would be a **4-dimensional** vector.
- A word represented in a large AI language model might use a **768-dimensional** vector — 768 separate numbers, each capturing a different nuance of that word's meaning.

Dimension matters because every vector you want to compare must have the **same number of dimensions**. You cannot compare a 3-dimensional song vector to a 4-dimensional one — the slot structures do not match [1][3].

### 5.4 The rule of consistent positions

The most important discipline when building vectors is: **position N must always mean the same property across every vector in a dataset** [2].

Imagine you describe three songs:

```
song_A = [0.8, 0.6, 0.3]   energy=0.8, tempo=0.6, mood=0.3
song_B = [0.4, 0.9, 0.7]   energy=0.4, tempo=0.9, mood=0.7
song_C = [0.6, 0.5, 0.5]   energy=0.6, tempo=0.5, mood=0.5
```

Position 1 is energy in every row. Position 2 is tempo in every row. Position 3 is mood in every row. That consistency is what makes arithmetic between these vectors meaningful [2].

If you accidentally put tempo in position 1 for song_C, the numbers are now incompatible. Any calculation you do later would compare energy against tempo — which is nonsense. AI systems depend on this discipline completely. The data pipeline must guarantee consistent position-to-property mapping before any learning happens [2][3].

### 5.5 Feature vectors — the standard name in AI

In AI and machine learning, a vector used to describe a real-world thing is called a **feature vector** [3].

- **Feature** — a single measurable property of the thing you are describing. Energy, tempo, and mood are features of a song.
- **Feature vector** — the complete collection of all chosen features for one item, packed into an ordered list [3].

The word "feature" just means "one property we decided to measure." When an AI team says "we represent each customer as a feature vector," they mean: we picked a set of properties (age, number of purchases, average spend, days since last visit), measured those properties for every customer, and stored each customer as an ordered list of those measurements [2][3].

Feature vectors appear across many AI applications:

- **Spam detection:** each email is a feature vector — count of capital letters, count of exclamation marks, presence of certain words, sender reputation score.
- **House price prediction:** each house is a feature vector — square footage, number of bedrooms, distance from a school, year built.
- **Recommendation systems:** each user is a feature vector — age group, genres watched, average session length.

The pattern is always the same: pick properties, measure them, line them up in a fixed order, and you have a feature vector [2][3].

### 5.6 Why grouping properties into a vector is powerful

You might wonder: why not just keep the individual scalars separate? Why do we need the bundle? There are three strong reasons [1][2].

**Reason 1: A vector is one thing, not many.**
When energy, tempo, and mood are bundled into `[0.8, 0.6, 0.3]`, you can pass that single object to an algorithm. The algorithm receives everything it needs about the song in one move. If you kept them separate, you would need to pass three separate values and keep them synchronised — more complexity, more room for error.

**Reason 2: Arithmetic on vectors compares whole descriptions at once.**
When AI looks for songs similar to one you liked, it compares the full description of every song to your song in a single calculation. That comparison uses the whole vector — all properties simultaneously. How this similarity calculation works is covered in topic 6.6. The key point here is: you need the bundle to do the comparison; scattered scalars cannot be compared this way.

**Reason 3: Patterns emerge across many properties together.**
A song with energy=0.8 alone could mean anything. But energy=0.8 AND tempo=0.9 AND mood=0.2 is a very specific signature — probably an aggressive, fast, dark track. The combination is informative in a way that no single scalar is. AI finds these multi-property signatures in data, and it can only do that if the properties are grouped [3].

### 5.7 Choosing which properties to include

Building a useful feature vector always starts with a design question: which properties should I measure? [2][3]

The answer depends on what you want the AI to do. For a music recommendation system, energy, tempo, and mood are sensible choices because they reflect how a song feels to a listener. Measuring the audio file size in bytes would not help — file size does not predict whether someone will enjoy the song.

A few practical principles:

- **Include properties that vary between items.** If every song in your dataset has the same record label, "record label" carries no information and should not be a feature.
- **Include properties that are measurable consistently.** Every item in the dataset must be measured the same way. If you measure tempo in beats-per-minute for some songs and in "fast/slow" categories for others, the positions become inconsistent.
- **Include properties that are relevant to the task.** This is the hardest part and is called feature engineering — a topic for later in the curriculum. For now, the important point is that the choice of what to include shapes everything an AI learns from the data [3].

### 5.8 How AI systems use feature vectors

Once every item in a dataset is represented as a feature vector with the same dimension, an AI system can treat the entire dataset as a large table of numbers [1][2].

Imagine a music dataset with 10,000 songs, each described by a 3-dimensional feature vector:

```
song_1:     [0.8, 0.6, 0.3]
song_2:     [0.4, 0.9, 0.7]
song_3:     [0.7, 0.5, 0.4]
...
song_10000: [0.5, 0.5, 0.6]
```

That table has 10,000 rows and 3 columns. Each row is one vector. The table is now pure arithmetic — no text, no ambiguity, no subjective meaning. An algorithm can scan every row, compute relationships between rows, and find clusters of similar songs, all through basic number operations [1][3].

This is the bridge from raw data (words, sounds, images) to AI computation. Topic 6.1 established that AI converts everything to numbers. Topic 6.2 showed that a single number (scalar) is too limited to capture a complex thing. Topic 6.3 shows how grouping scalars into a vector gives you a complete, machine-readable description of one thing — and how that unlocks pattern-finding at scale [2].

How AI then stacks many vectors into a grid, multiplies them, or uses them in neural networks is covered in later topics — matrices in 6.4, the geometric view in 6.5, and the dot product in 6.6. What matters here is the foundation: **one vector = one thing described by multiple numbers in a fixed order** [1].

## 6. Implementation

### Building a feature vector step by step

You do not need code to build a feature vector. Here is the process for any real-world item [2]:

1. **Choose the thing you want to describe.** Example: a coffee drink.

2. **Decide which properties matter for your goal.** If the goal is to recommend coffees based on taste, useful properties are: bitterness, sweetness, strength.

3. **Define the scale for each property.** Use 0.0 (none) to 1.0 (maximum) for each. Be consistent — every coffee must use the same scale.

4. **Measure each property for your item and record the number.**
   - Espresso: bitterness = 0.9, sweetness = 0.1, strength = 1.0

5. **Line the numbers up in a fixed, named order.**
   ```
   espresso_vector = [bitterness, sweetness, strength]
                   = [0.9,        0.1,       1.0]
   ```

6. **Repeat for every other item, using the same order and scale.**
   ```
   latte_vector      = [0.4, 0.5, 0.6]
   cappuccino_vector = [0.5, 0.4, 0.7]
   ```

7. **Check consistency: position 1 is always bitterness, position 2 is always sweetness, position 3 is always strength, for every coffee.** Any row that violates this makes the dataset broken.

You now have a collection of feature vectors that an algorithm could use to group similar coffees or recommend one based on what a customer already likes [2][3].

## 7. Real-World Patterns

### Vectors in production AI systems

Feature vectors are the standard input format for virtually every machine learning algorithm in use today [3].

**Text and language:** A word or sentence is converted into a high-dimensional vector before being processed. A word might be represented by 300 numbers, each capturing a different facet of its meaning — how formal it is, whether it relates to emotions, whether it often appears near scientific terms. These high-dimensional vectors applied to words are introduced in a later module [3].

**Images:** A photograph is converted into a feature vector by measuring properties of pixel patches — colour intensities, edge sharpness, texture patterns — resulting in vectors with hundreds or thousands of dimensions [1]. The internal layers of image-processing AI models produce feature vectors that capture "what the image looks like" as a bundle of numbers.

**User profiles in recommendation systems:** Streaming platforms represent each user as a feature vector encoding viewing history, genre preferences, time-of-day patterns, and device type. When recommending a new film, the system looks for films whose vectors are close to films the user has already enjoyed. That closeness calculation is only possible because both the user and the films are described as vectors [2][3].

**Medical data:** Each patient record can become a feature vector — age, blood pressure, cholesterol level, blood glucose, body mass index. An AI trained on thousands of such vectors can learn to predict disease risk. The vector format makes patient comparisons mathematically rigorous [2].

In every case the pattern is the same: choose meaningful properties, measure them consistently, bundle them into a vector, repeat for every item. Once that is done, arithmetic takes over [3].

## 8. Best Practices

**Do**

- **Decide what each position means before collecting any data.** Write it down: position 1 = X, position 2 = Y, and so on. Changing this later breaks everything.
- **Use the same measurement scale across all items.** If bitterness runs from 0 to 1 for the espresso, it must run from 0 to 1 for every other coffee too.
- **Include only properties that genuinely vary across your items and matter for the task.** More dimensions is not always better — irrelevant properties can add noise without adding useful signal.
- **Treat the vector as a single object.** When passing it to an algorithm or storing it, keep all the numbers together and in order.

**Do not**

- **Do not mix up the property order between items.** This is the most common beginner mistake. It makes vectors incompatible and corrupts all downstream arithmetic.
- **Do not assume more features are always better.** Adding properties that do not relate to the task adds noise.
- **Do not confuse a vector with a matrix.** A vector is a single ordered list — one row or one column. A matrix is a grid of numbers — multiple vectors stacked together. That distinction is covered in topic 6.4.
- **Do not try to compare vectors of different dimensions.** A 3-dimensional vector and a 4-dimensional vector cannot be compared until they share the same structure.

## 9. Hands-On Exercise

### Build a feature vector by hand — then observe clusters in the Embedding Projector

This exercise requires no coding and mirrors the week's lab activity.

**Step 1.** Choose five songs you know well.

**Step 2.** Pick three properties to measure: energy (0–1), tempo (0–1), mood (0–1). Write your own 0-to-1 scores for each song based on how you hear it.

**Step 3.** Write out each song as a vector:
```
song_A = [energy, tempo, mood] = [?, ?, ?]
song_B = [energy, tempo, mood] = [?, ?, ?]
...
```

**Step 4.** By eye — looking only at the numbers — rank the five songs from most similar to least similar to song_A. Do this before any calculation, using your intuition about which songs have the closest numbers.

**Step 5.** Open the TensorFlow Embedding Projector (projector.tensorflow.org) and load the pre-computed demo vectors. Observe how items that feel similar cluster close together in the 2D view. This is the same principle at work — things with similar vectors end up near each other. The formal similarity calculation that makes this precise is covered in topic 6.6.

## 10. Key Takeaways

- A **vector** is an ordered list of scalars. Each scalar occupies a fixed position that always represents the same property across every item in the dataset.
- Grouping multiple properties into one vector lets AI treat a complex thing — a song, a patient, a user — as a single mathematical object that can be fed to algorithms.
- The **dimension** of a vector is the number of scalars it contains. All vectors being compared must have the same dimension.
- **Feature vectors** are the standard way AI systems represent real-world items numerically — from words to images to user profiles to medical records.
- **Consistent position-to-property mapping** is the foundational discipline: if position 1 means energy for song A, it must mean energy for every other song in the dataset.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
