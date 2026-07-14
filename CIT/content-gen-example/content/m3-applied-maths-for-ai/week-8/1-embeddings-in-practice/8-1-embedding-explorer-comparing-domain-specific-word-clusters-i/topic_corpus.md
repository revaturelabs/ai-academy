---
topic_id: 8.1
title: Embedding explorer — comparing domain-specific word clusters in 2D
position_in_module: 1
generated_at: 2026-06-22T06:10:00Z
resource_count: 3
---

# 1. Embedding explorer — comparing domain-specific word clusters in 2D — Topic Corpus

## 2. Prerequisites

- **6.7 Embeddings — turning words into vectors that capture meaning** — you should already know that an embedding turns a word into a list of numbers, and that words with related meanings get similar number-lists.
- **6.5 A vector as a point in space — music taste described as three numbers** — you should already picture a list of numbers as a point in space.
- **6.10 Using the TensorFlow Embedding Projector to explore word clusters** — you have already opened the Projector once and seen words drawn as dots. This topic puts that same tool to work on a focused lab task: comparing word sets from two different subject areas.

## 3. Learning Objectives

After this topic you will be able to:

- Open the TensorFlow Embedding Projector and recognize what each dot on the screen represents.
- Pick a focused set of 10 "domain-specific" words and explain why a focused set is easier to read than a random one.
- Switch the view to a flat 2D picture and describe, in plain words, what a "2D projection" is and is not.
- Identify a **cluster** (a tight group of dots) and an **outlier** (a lonely dot) by eye.
- Compare the word clusters of two different domains and say what their layout tells you about meaning.

## 4. Introduction

Imagine you tip out a box of mixed buttons on a table and start sliding the ones that look alike into little piles. Red buttons here, big metal ones there, one odd glittery button sitting on its own. You did not measure anything — you just grouped by "these belong together." That sorting instinct is exactly what this lab trains, except the "buttons" are words and the "table" is a computer screen.

You already learned that a computer stores a word as an **embedding** — a long list of numbers that captures the word's meaning. The problem is that this list is far too long to picture. A screen has two directions, left-right and up-down, but a word's number-list can have hundreds of entries. So how do you ever *look* at it?

The answer is a free web tool called the **TensorFlow Embedding Projector** [1]. It takes those long number-lists and squashes them down to a flat picture you can actually see, then draws each word as a dot. Words that mean similar things land near each other; unrelated words land far apart. In this lab you will pick 10 words from one subject area, look at how they group, and compare them against words from a different area. By the end you will be reading meaning straight off a screen.

## 5. Core Concepts

### What "domain-specific" means

A **domain** is just a subject area — a topic that words belong to. Cooking is a domain. Football is a domain. Medicine is a domain.

- **Domain-specific words** — words that clearly belong to one subject area, like *whisk*, *simmer*, and *recipe* for the cooking domain.
- **Why pick a focused set?** If you throw in random unrelated words, the picture is a confusing scatter. If you pick 10 words from one domain, the tool can show you a clean, readable shape. A focused set is the whole trick to a useful plot.

A small worked choice: for the cooking domain you might pick *recipe, oven, whisk, simmer, dough, spice, knife, plate, boil, chef*. Ten words, all clearly about one subject.

### The Embedding Projector — what the tool is

The **TensorFlow Embedding Projector** is a website that draws embeddings as dots in space so a person can look at them [1]. Google's research team released it for exactly this reason: high-dimensional data (number-lists too long to imagine) is impossible to inspect by eye, and a picture makes the hidden relationships visible [3].

- Each **dot** on the screen is one word.
- The **distance** between two dots reflects how related their meanings are: close dots mean similar meanings, far dots mean different meanings.
- You can **hover or click a dot** to see which word it is, and the tool can highlight a word's **nearest neighbors** — the handful of dots sitting closest to it [2].

### What a "2D projection" is

Here is the key idea of the whole lab. A word's embedding lives in many dimensions — many separate number-slots. You cannot draw many dimensions on a flat screen. So the tool performs a **projection**: it flattens the many-number picture down to just two directions, left-right and up-down, so it fits on screen.

- **Projection** — squashing a many-dimension picture down to a smaller number of dimensions so a person can see it. Think of a shadow: a 3D object casts a flat 2D shadow on the wall. The shadow loses some detail but keeps the overall shape.
- **2D** means two dimensions: the flat left-right and up-down picture. The tool also offers a **3D** view, but flat 2D is the easiest to read and screenshot for this lab [2].
- **What it is NOT:** the flattened picture is an approximation, not the exact truth. Two dots that look a little close in 2D might be a bit farther apart in the full number-list. Read the *overall grouping*, not the exact pixel gaps.

The tool offers a few different methods for doing this flattening — you will see buttons labelled **PCA**, **t-SNE**, and **UMAP** [1]. For this lab you only need to know they are different ways to squash the picture; you do not need the math behind them. Pick one (PCA is the quickest), look at the shape, and if it is messy, try another. *How* each method works is a more advanced topic you can explore later.

### Clusters and outliers — what you are looking for

Once the dots are drawn, two shapes matter:

- **Cluster** — a tight group of dots sitting close together. A cluster means those words share related meaning. Your 10 cooking words should mostly bunch into one cooking cluster.
- **Outlier** — a single dot sitting off on its own, away from the groups. An outlier is a word whose meaning does not fit neatly with the others. For example, the word *plate* might drift away from the cooking actions because a plate is also a plain dinnerware object, not a cooking step.

| Shape | What it looks like | What it means |
|---|---|---|
| Cluster | Several dots bunched together | Those words share related meaning |
| Outlier | One dot alone, far from any group | That word's meaning does not fit the rest |

### Comparing two domains

The headline of this topic is *comparing* clusters across domains. The move is simple: load words from two subject areas at once — say cooking and football — and look at the picture.

- You should see **two separate clusters**: a cooking blob and a football blob, sitting apart from each other.
- The **gap between the two clusters** is itself information: a wide gap means the two domains share little meaning; a small gap or some overlap means they share something. A word like *coach* might sit between cooking and football, since a coach trains people in many domains.

Comparison turns a single picture into a story: same-domain words pull together, different-domain words push apart, and the in-between words tell you where domains touch.

## 6. Implementation

You do not write any code for this lab — the Projector is a website you click through [2]. Here is the end-to-end flow.

1. **Pick your words.** Choose 10 words from one domain (e.g. cooking). For a comparison, also pick 10 from a second domain (e.g. football). Write them down first.
2. **Open the tool.** Go to the TensorFlow Embedding Projector website [1]. It opens with a sample word dataset already loaded, so you see dots immediately.
3. **Find your words.** Use the search box on the side to type one of your words. The tool highlights that word's dot and its nearest neighbors [2]. Repeat for each of your 10 words, noting where each lands.
4. **Switch to 2D.** Choose a projection method (PCA is the simplest) and select the **2D** view rather than 3D, so the picture is flat and easy to read [1][2].
5. **Read the groups.** Look for clusters (tight bunches) and outliers (lonely dots). Hover a dot to confirm which word it is.
6. **Compare.** With both domains in view, check that each domain forms its own cluster and note the gap between them, plus any word that sits in between.
7. **Capture it.** Take a screenshot of the 2D view so you can describe the clusters and outliers in your lab notes.

## 7. Real-World Patterns

This same "flatten it and look" move is how working teams sanity-check the meaning a model has learned [3].

- **Spotting bad data.** If a team expects two topics to separate but the dots all blur into one cluster, that is a signal the model has not learned to tell them apart yet.
- **Catching surprises.** An outlier that should not be one — a clearly on-topic word sitting alone — often points to a typo, a rare word, or a labelling mistake in the data.
- **Explaining a model to non-experts.** A picture of dots grouping sensibly is far more convincing to a manager or client than a wall of numbers — which is exactly the gap the Projector was built to close [3].

## 8. Best Practices

- **Do** keep your word set small and focused — 10 words from one domain reads far cleaner than 30 random ones.
- **Do** start with PCA, then try t-SNE or UMAP only if the picture looks tangled. Switching methods is one click.
- **Do** read the *overall grouping*, not exact distances — a 2D picture is an approximation, not the exact truth.
- **Don't** over-interpret a single close pair of dots; trust the big clusters and the obvious outliers.
- **Don't** mix in throwaway words "to see what happens" before you have read the clean focused picture first.

## 9. Hands-On Exercise

Pick two domains you know well — for example cooking and football. List 10 words for each. Open the Projector [1], search for your words, switch to the 2D PCA view, and study the result. Then answer in your own words: Which words formed a cluster? Which one word is the clearest outlier, and why might its meaning sit apart? How big is the gap between your two domain clusters, and is any single word stuck in between?

## 10. Key Takeaways

- An embedding is a long number-list per word; the Embedding Projector flattens it into a flat 2D picture so you can actually look at it.
- A **2D projection** trades exact detail for a readable shape — read the overall grouping, not the exact pixel distances.
- A **cluster** is a tight group of related-meaning words; an **outlier** is a lonely dot whose meaning does not fit the group.
- Picking a focused set of domain-specific words is the trick that turns a confusing scatter into a clean, readable plot.
- Comparing two domains shows two separate clusters; the gap between them, and any word in between, tells you how the domains' meanings relate.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
