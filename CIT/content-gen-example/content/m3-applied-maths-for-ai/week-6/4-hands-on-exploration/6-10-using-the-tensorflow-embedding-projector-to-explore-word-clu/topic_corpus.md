---
topic_id: "6.10"
title: "Using the TensorFlow Embedding Projector to explore word clusters"
position_in_module: 1
generated_at: "2026-06-19T00:00:00Z"
resource_count: 3
---

# 1. Using the TensorFlow Embedding Projector to Explore Word Clusters — Topic Corpus

## 2. Prerequisites

This is the hands-on capstone of the week. It does not teach new theory — it gives you a place to *see* everything you already learned. It builds directly on these earlier topics in this sequence:

- **6.3 — Vector:** an ordered list of numbers, where each position holds one feature. A word can be turned into such a list.
- **6.5 — A vector as a point in space:** a vector with several numbers can be read as a single point — an address — in space. Points that sit close together represent things that are similar.
- **6.6 — Dot product as similarity:** a single score that is high when two vectors point the same way.
- **6.7 — Embedding:** turning a word into a vector of numbers so that words with related meanings end up with similar vectors.
- **6.8 — "king − man + woman ≈ queen":** doing arithmetic on word-vectors lands you near another meaningful word.
- **6.9 — Cosine similarity:** measuring how similar two meaning-vectors are by the angle between them, ignoring their length.

All of those terms are available vocabulary here and will not be re-defined — only used.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Describe what the **TensorFlow Embedding Projector** is and what it shows on screen.
2. Explain why high-dimensional embeddings have to be *squashed* down to 2D or 3D before you can see them.
3. Read a cluster of points on the Projector and say, in plain language, why those words sit together.
4. Use the Projector's search-and-highlight feature to find the **nearest neighbours** of a chosen word.
5. Rank a small set of word- or sentence-vectors by similarity by hand, then check your ranking against the tool.

## 4. Introduction

For the last nine topics you have been building one big idea: meaning can be written as numbers. A word becomes a **vector** (a list of numbers). Similar words get **similar vectors** — that is what an **embedding** is. You measured that similarity with the **dot product** (6.6) and with **cosine similarity** (6.9), and you even did arithmetic on word-vectors in 6.8.

But there is a catch you have been living with the whole time: these vectors are *long*. A real word embedding often has 100, 300, or more numbers in it. You can hold a 2-number vector in your head as a dot on a page (6.5). You cannot picture a 300-number vector at all. So far you have trusted the maths without ever *seeing* the space.

This week's lab fixes that. There is a free web tool — the **TensorFlow Embedding Projector** — that takes those long vectors and draws them as dots you can spin around in 3D in your browser. Words that mean similar things show up as a **cluster**: a clump of dots sitting near each other [1]. There is no coding this week. You open a website, look, search, and notice patterns. The goal is understanding, not programming.

## 5. Core Concepts

### 5.1 What the Embedding Projector is

The **TensorFlow Embedding Projector** is a free, browser-based tool for *looking at* embeddings. (TensorFlow is the name of a software toolkit built by Google for machine learning; you do not need to know anything about it to use the Projector.) You point your browser at **projector.tensorflow.org** and it shows you a cloud of dots floating in space. Each dot is one item — for word embeddings, each dot is one word. The position of each dot comes straight from that word's embedding vector [1][3].

The whole point of the tool is this: it turns the abstract idea of "a word is a point in space" (6.5) into something you can literally see and rotate with your mouse. It loads with an example dataset already in it, so you can explore on day one without preparing anything [3].

### 5.2 The squashing problem (why we only ever see 2D or 3D)

Here is the honest difficulty. A word embedding might have 200 numbers. By 6.5 that means the word is a point in a 200-**dimension** space. Your screen is flat. Your eyes work in 3D at most. So 200 dimensions cannot be drawn directly — there is no way to show 200 separate directions on a screen.

The Projector solves this by **squashing** the high-dimensional points down to 2 or 3 dimensions so they fit on screen, while trying hard to keep points that were close in the original space still close in the picture [1]. Think of it like photographing a 3D sculpture: the photo is flat, but a good photo still shows you which parts of the sculpture are near each other. The Projector is doing the same trick, just from many more dimensions down to a viewable few.

You do not control the squashing by hand. You pick one of a couple of built-in methods from a menu — they have the labels **PCA** and **t-SNE** in the tool [1][3]. For this week, treat those two as *named buttons that do the squashing*. How PCA and t-SNE actually work is its own topic and is covered later in the curriculum — do not worry about the internals now. What matters for the lab:

- The picture you see is an *approximation*. It is a flattened shadow of a much larger space.
- Because it is a shadow, exact distances on screen can be slightly distorted. Trust the *big picture* — which words clump together — more than tiny pixel-level gaps.
- Switching from one squashing button to the other rearranges the dots. The clusters usually survive the switch; their exact shape and spacing changes. That is expected, not a bug.

### 5.3 Reading a cluster

A **cluster** is a clump of dots sitting close together [1]. By everything you learned this week, closeness means similarity: dots near each other are words whose embeddings are similar, which means the words tend to mean related things or get used in related ways.

So reading the Projector is mostly one move: *find the clumps, then ask what the words in each clump have in common.* You might find a clump of country names, a clump of numbers, or a clump of polite words. The tool did not label these clusters — the embedding put related words near each other, and your eye spots the grouping. This is the visual payoff of topics 6.5 through 6.9: similarity-as-closeness, made literal.

### 5.4 Searching for nearest neighbours

The single most useful button in the Projector is **search**. You type a word — say `apple` — and the tool highlights that word's dot and lights up its **nearest neighbours**: the handful of words whose vectors are most similar to it [1][3]. *Nearest neighbour* is vocabulary you already met (6.5 and 6.8): the closest point to a given point.

When you search, the tool shows a side panel listing those neighbours, often with a similarity number next to each. That number is typically a **cosine similarity** (6.9) — higher means more similar in meaning, ignoring vector length. So the panel is just an automatic, ranked version of the by-hand comparisons you did earlier in the week. You search `apple` and might see `apples`, `fruit`, and `banana` near the top — and, depending on the dataset, maybe `iphone`, because embeddings learn from how words are *used*.

### 5.5 What the Projector is NOT for (scope boundary)

To keep this lab focused, three things are deliberately out of bounds:

- **It does not teach you how embeddings are trained.** The Projector *displays* finished embeddings; it does not make them. How a word gets its vector in the first place is covered later — for now you are a viewer, not a trainer.
- **You will not study the squashing maths.** PCA and t-SNE are named buttons here; their inner workings come later.
- **No coding.** This week is browser-only. You are reading clusters, not writing programs.

## 6. Implementation

You do not write code, but the lab is still a procedure. Follow these steps in order — this is the spine of the hands-on activity [3]:

1. **Open the tool.** Go to **projector.tensorflow.org** in your browser. A 3D cloud of dots loads automatically from a built-in word-embedding dataset.
2. **Look and rotate.** Click and drag to spin the cloud. Scroll to zoom. Spend a minute just noticing that the dots are not spread evenly — some areas are denser. Those dense areas are your **clusters**.
3. **Toggle the squashing method.** Find the panel that lets you switch between **PCA** and **t-SNE**. Click between them and watch the dots rearrange. Note that the clumps mostly stay clumped even as the overall shape changes.
4. **Search a word.** Use the search box. Type a common word (`king`, `apple`, `paris`). The tool highlights that word and its **nearest neighbours**, and shows a side list of the closest words with a similarity score [1][3].
5. **Read the neighbours.** Look at the listed neighbours and ask: do these make sense as "similar in meaning"? Write down what you see.
6. **Repeat with a contrast word.** Search a clearly different word and confirm its neighbours sit in a different cluster.

Keep this to roughly 15 minutes of clicking. The thinking — *why* the clusters look like they do — is the real assignment.

## 7. Real-World Patterns

The Projector is not a toy demo; it is a working diagnostic tool used by real machine-learning teams [1]. The everyday pattern is: *before trusting an embedding, look at it.* If words that should be similar are not clustering, the embedding is suspect.

The same closeness-means-similarity idea you are seeing on screen is exactly what powers products you already use:

- **Search.** A search engine turns your query into a vector and finds documents whose vectors are nearest neighbours of it.
- **Recommendations.** "Customers who liked this also liked…" is nearest-neighbour lookup in an embedding space.
- **Grouping similar items.** Photo apps and support tools group similar items the same way the Projector groups words [1].

The Projector lets you *see* the geometry that all of those systems run on without ever showing it to the everyday user.

## 8. Best Practices

A short do/don't list for getting honest readings out of the tool:

| Do | Don't |
|---|---|
| Trust the big clusters — which words clump together. | Read deep meaning into tiny pixel gaps; the squashing distorts fine distances. |
| Toggle PCA and t-SNE and compare; trust patterns that survive both. | Assume one squashed view is "the truth"; it is one shadow of many. |
| Use search to confirm a hunch about a word's neighbours. | Expect every neighbour to make obvious sense — embeddings learn from usage, so some surprises are real. |
| Treat the similarity numbers as cosine similarity (6.9): higher = more similar. | Treat on-screen distance as an exact measurement. |

## 9. Hands-On Exercise

This is **Journal Entry #3** for the week, and it pairs by-hand work with the tool:

1. Your instructor gives you 5 short pre-computed sentence vectors and one query vector.
2. **By hand first:** using cosine similarity intuition from 6.9 (smaller angle = more similar), rank the 5 vectors from most to least similar to the query. Write your ranking down.
3. **Then verify in the browser:** load the same vectors into the Projector, search the query, and read off the tool's nearest-neighbour ranking.
4. In your journal, note where your by-hand ranking matched the tool and where it differed — and write one sentence on *why* the differences might have happened (hint: squashing, and length-vs-angle).

(Assessment 2 is due this week; this journal entry is part of your evidence for it.)

## 10. Key Takeaways

- The **TensorFlow Embedding Projector** is a free browser tool that draws word embeddings as dots you can rotate, turning "a word is a point in space" into something you can actually see.
- High-dimensional vectors must be **squashed** to 2D or 3D to fit on screen; PCA and t-SNE are the named buttons that do this, and the on-screen view is an approximate shadow of the real space.
- A **cluster** is a clump of nearby dots; nearness means similar embeddings, which means related words — this is similarity-as-closeness made literal.
- **Search** highlights a word's **nearest neighbours** and lists them by similarity (typically cosine similarity), automating the by-hand comparisons from earlier in the week.
- The lab is understanding-only: look, search, notice patterns — no coding, and no studying how embeddings are trained or how the squashing maths works.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
