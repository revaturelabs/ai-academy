---
topic_id: 8.2
title: Similarity scoring — computing cosine similarity between sentence pairs
position_in_module: 2
generated_at: 2026-06-22T06:25:00Z
resource_count: 3
---

# 1. Similarity scoring — computing cosine similarity between sentence pairs — Topic Corpus

## 2. Prerequisites

- **6.7 Embeddings — turning words into vectors that capture meaning** — you should already know that an embedding turns a word into a list of numbers, and that words with related meanings get similar number-lists. In this topic the same idea applies to a whole sentence, not just one word.
- **6.5 A vector as a point in space** — you should already picture a list of numbers as an arrow pointing somewhere in space.
- **6.6 Dot product as similarity — vectors pointing the same direction score high** — you already met the idea that two arrows pointing the same way count as similar.
- **6.9 Cosine similarity — measuring the angle between two meaning-vectors** — you have already seen the name "cosine similarity" and the idea of an angle between two meaning-arrows. This topic turns that idea into an actual score you compute for sentence pairs.
- **8.1 Embedding explorer — comparing word clusters in 2D** — you have already read closeness *by eye* in the Projector (clusters, outliers, nearest neighbors). This topic puts an actual **number** on "how close," instead of just eyeballing it.

## 3. Learning Objectives

After this topic you will be able to:

- Explain what a **sentence embedding** is, reusing what you know about word embeddings.
- Describe **cosine similarity** as the angle between two arrows, and read its score from a simple scale.
- State what a high score and a low score mean about two sentences' meaning.
- Walk through scoring five sentence pairs using **pre-computed vectors** the lab hands you.
- Tell the difference between "same words" and "same meaning" when you read a similarity score.

## 4. Introduction

You text a friend "Where are you?" and they reply "I'm running late." Different words, but you instantly feel the two messages are *related* — they are about the same thing. Now imagine a computer trying to do the same: decide whether two sentences are about the same thing, using only numbers. How close is "close"?

In the last topic you read closeness with your eyes. You opened the Embedding Projector, saw words as dots, and noticed which dots clustered together. That worked, but "those two look near each other" is a feeling, not a measurement. To compare many sentence pairs, or to let a program do it, you need a single number that says *how* similar.

That number is **cosine similarity** [1]. In this lab you will take five pairs of sentences whose vectors have already been worked out for you, and read off a similarity score for each. By the end you will be able to look at a score and say, in plain words, "these two sentences mean nearly the same thing" or "these two are unrelated."

## 5. Core Concepts

### From word vectors to sentence vectors

You already know an **embedding** turns a word into a list of numbers that captures its meaning [1]. The same trick works on a whole sentence.

- **Sentence embedding** — a single list of numbers that captures the meaning of an entire sentence, not just one word. The sentence "The cat sat on the mat" becomes one number-list; "A feline rested on the rug" becomes another.
- Just like word embeddings, sentences with **similar meaning** get **similar number-lists**, even when the actual words are different [2].

Why does this matter? Because once a sentence is a list of numbers — an arrow pointing somewhere in space — you can compare two sentences the same way you compared two words.

### Pre-computed vectors — the lab hands them to you

A real model produces these sentence vectors, and that step is not what this lab is about. For this exercise the vectors are **pre-computed**.

- **Pre-computed vectors** — the number-lists for each sentence are worked out ahead of time and given to you ready-made. You do **not** build the embeddings yourself.
- Your job is only the next step: take two ready-made vectors and score how similar they are. *How* a model turns text into those vectors was covered earlier and is not repeated here.

### Cosine similarity — the angle between two arrows

Here is the heart of the topic. Picture each sentence as an **arrow** starting from the same point and pointing off into space. Two sentences that mean nearly the same thing point in nearly the **same direction**. Two unrelated sentences point in **different directions** [1].

**Cosine similarity** — a score that measures the **angle** between two arrows. A small angle (arrows pointing the same way) gives a high score; a wide angle (arrows pointing apart) gives a low score [1].

- The key insight: cosine similarity cares about **direction, not length**. A short arrow and a long arrow pointing the same way still count as a perfect match. This is why it works well for sentences of different lengths [1].
- A common one-line way people describe how it is worked out: it is the **dot product of the two vectors divided by their lengths (magnitudes)** [3]. You do not need to compute that by hand — the lab tool does it. Just hold on to the picture: *smaller angle means more similar.*

### Reading the score

Cosine similarity produces a number on a fixed scale, so every pair is judged the same way [1][3].

| Score | Angle between arrows | What it means |
|---|---|---|
| about 1 | none — same direction | Sentences mean nearly the same thing |
| about 0.5 | partway apart | Sentences are somewhat related |
| about 0 | square corner — unrelated directions | Sentences are unrelated |
| below 0 | pointing opposite ways | Sentences pull in opposite directions (rare for normal sentence pairs) |

- For sentence embeddings the score usually lands between **0 and 1**, where **1 = same meaning** and **0 = unrelated** [1].
- The full scale runs from **-1 to 1**, but everyday sentence pairs rarely go negative, so in this lab treat **0 as "unrelated" and 1 as "identical in meaning."**

### Same words vs same meaning

The reason similarity scoring is useful — and not just word-counting — is that it follows **meaning**, not spelling.

- "How do I reset my password?" and "I forgot my login details" share almost no words, yet score **high**, because they mean the same thing [2].
- "I love this movie" and "I love this pizza" share most of their words, yet score **lower**, because they are about different things.

A high cosine similarity says *these mean the same*, even when the words differ — that is the whole point.

## 6. Implementation

You do not write embedding code in this lab — the sentence vectors are pre-computed and handed to you. Here is the end-to-end flow for scoring one pair, repeated across five pairs.

1. **Read the pair.** Look at the two sentences and make a quick guess: same meaning, somewhat related, or unrelated?
2. **Take the two pre-computed vectors.** Each sentence already has its ready-made number-list. You do not build these.
3. **Score them.** Feed the two vectors into the cosine-similarity step the lab gives you. Out comes one number, somewhere between 0 and 1.
4. **Read the number.** Use the score table: near 1 means same meaning, near 0 means unrelated.
5. **Check it against your guess.** Did the number match your gut feeling from step 1? Note any surprise — a low score for a pair you thought was similar is worth a second look.
6. **Repeat for all five pairs**, then line the scores up and rank the pairs from most to least similar.

## 7. Real-World Patterns

This exact "score how similar two pieces of text are" move runs quietly inside tools you already use [2][3].

- **Search that understands meaning.** When a search box returns a good result even though you did not type the exact words on the page, a similarity score between your query and each page is doing the work [3].
- **Grouping similar messages.** Support teams group near-duplicate tickets ("can't log in" vs "login not working") by scoring how similar their sentences are, so one answer can cover many [2].
- **Catching paraphrases.** Detecting that two sentences say the same thing in different words — for de-duplication or plagiarism checks — is a similarity-score job [3].

## 8. Best Practices

- **Do** trust the score over the shared words. A high score on differently-worded sentences is the feature, not a bug.
- **Do** read the score as a *band* (high / medium / low), not an exact truth — 0.81 vs 0.83 is not a meaningful gap.
- **Do** sanity-check a surprising score by re-reading the two sentences; a strange score sometimes flags an odd or ambiguous sentence.
- **Don't** treat cosine similarity as a length comparison — it ignores how long the arrows are and only reads their direction.
- **Don't** expect a hard cutoff for "similar." Where you draw the line (say, above 0.7) depends on the task; pick a threshold and stay consistent.

## 9. Hands-On Exercise

Take the five sentence pairs your lab provides, each with its pre-computed vectors. Before scoring, rank the five pairs yourself from "most alike" to "least alike" just by reading them. Then run each pair through the cosine-similarity step and write down the five scores. Compare your eyeball ranking to the number ranking: where did they agree, and which pair surprised you? In one sentence, explain why a pair with few shared words can still score high.

## 10. Key Takeaways

- A **sentence embedding** is one number-list capturing a whole sentence's meaning — the same idea as a word embedding, scaled up.
- **Cosine similarity** scores the **angle** between two meaning-arrows: same direction scores near 1, unrelated directions score near 0.
- It reads **direction, not length**, so sentences of different sizes still compare fairly.
- In this lab the vectors are **pre-computed** — you score similarity, you do not build the embeddings.
- A high score means **same meaning even with different words** — similarity follows meaning, not spelling.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
