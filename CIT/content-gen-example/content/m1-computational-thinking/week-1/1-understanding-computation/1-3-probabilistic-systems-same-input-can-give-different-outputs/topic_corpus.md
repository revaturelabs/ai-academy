---
topic_id: "1.3"
title: "Probabilistic systems — same input can give different outputs"
position_in_module: 3
generated_at: "2026-06-19T00:00:00Z"
resource_count: 3
---

# 1. Probabilistic systems — same input can give different outputs — Topic Corpus

## 2. Prerequisites

This topic builds on **Topic 1.1 — What is computation** (the input / process / output model and the idea of defined steps) and **Topic 1.2 — Deterministic systems** (the property that the same input always gives the same output, and the concepts of predictability, reproducibility, and hidden inputs). Both are used throughout without re-explanation. The contrast with deterministic systems is the central thread.

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Define what a probabilistic system is in plain, everyday terms.
- Explain why the same input can produce different outputs in a probabilistic system without that being an error.
- Give at least three real-world examples of probabilistic systems and describe what varies in each.
- Contrast probabilistic and deterministic systems using the input / process / output model from Topic 1.1.
- Explain what probability, randomness, and uncertainty mean in the context of computational systems — at a beginner level.
- Recognise everyday situations in which a probabilistic approach is more appropriate than a deterministic one.

## 4. Introduction

In Topic 1.2, you tested determinism with one question: if you ran the same process with the same input twice, would you always get the same output? For deterministic systems, the answer is always yes.

Now imagine you type exactly the same message into an AI assistant two days in a row: "Give me an idea for a short story." On Monday you get a tale about a lighthouse keeper. On Tuesday you get a story about a lost robot. Same input. Completely different outputs. The system has not broken. It is doing exactly what it was designed to do [1].

Or think about weather forecasting. A meteorologist feeds the same temperature and pressure readings from this morning into a forecasting program. Run the program twice and you might see "70% chance of rain" — and that percentage is not a mistake or a rounding error. It is the honest answer the system can give, because the future state of the atmosphere is genuinely uncertain [2].

These are not deterministic systems. They belong to a different category — **probabilistic systems** — and understanding them is increasingly important because much of modern computing, including AI tools, is built on this idea [1][3].

This topic explains what probabilistic systems are, why they exist, and how to recognise them. It does not teach the mathematics of probability — that comes later in the course. The goal here is to build the mental model.

## 5. Core Concepts

### 5.1 What "probabilistic" means

**Probabilistic system** — a system where the output is not fully fixed by the input. Even with exactly the same input, the system can produce different outputs on different runs [1].

The word "probabilistic" comes from "probability" — the branch of mathematics that deals with how likely different outcomes are. A probabilistic system does not pick its output arbitrarily. Instead, it works with a range of possible outcomes, each with a different likelihood, and selects one. The selection can vary each time [1][2].

Here is the key distinction stated plainly:

> In a deterministic system, the input fixes the output — there is one answer and only one.
> In a probabilistic system, the input shapes the *range of possible answers* — there is a range of answers, each more or less likely, and which one is produced can differ.

The input still matters — it narrows down what kinds of outputs are likely. But it does not lock the output to a single value.

**Concrete examples:**

| System | Input | Possible outputs | Same every time? |
|---|---|---|---|
| AI story generator | "Write a short story about the sea" | Thousands of different valid stories | No — varies each run [1] |
| Weather forecast model | Today's pressure and temperature | "60% chance of rain," "70% chance of rain," varies | No — depends on how the model samples [2] |
| Spam filter (pattern-based) | A borderline email | "Spam" or "Not spam" — close calls can vary | No — probability is close to 50% [3] |
| Dice roll | Roll a fair six-sided die | 1, 2, 3, 4, 5, or 6 | No — uniformly random [1] |

In every row, the input does not disappear — it still influences what outputs are possible. But it does not lock in a single answer.

### 5.2 Probability and uncertainty — the two ideas underneath probabilistic systems

You do not need to know the mathematics of probability to understand this topic. But two underlying ideas are worth naming clearly.

**Probability** is a way of expressing how likely something is, on a scale from 0 (impossible) to 1 (certain). A probability of 0.7 means the event happens roughly 70% of the time over many trials. In a probabilistic system, different possible outputs have different probabilities attached to them [1].

**Uncertainty** is the reason probabilistic systems exist. Some problems involve situations where the correct answer is not known in advance — because the world is incomplete, ambiguous, or genuinely variable. A probabilistic system is designed to work honestly in the presence of that uncertainty, rather than pretending a single fixed answer exists [2][3].

Together: a probabilistic system accepts that uncertainty is real, uses probability to represent how likely different answers are, and produces outputs that reflect that range rather than forcing a false certainty.

### 5.3 Randomness as a tool — not as chaos

In everyday language, "random" often implies chaos or arbitrariness. In computing and in probabilistic systems, randomness is a *design tool* — something deliberately introduced to make the system behave usefully [1][2].

**Randomness** means the system uses a source of unpredictability when choosing among possible outputs. The choice varies from run to run even when the input is the same — because an unpredictable element is built into the process. This is deliberate, not accidental [1].

Examples of deliberate randomness in computing:

- **Shuffling a playlist.** A music app that shuffles songs uses randomness intentionally. The same playlist, shuffled twice, gives different orders — and that variability is the point [1].
- **Generating a security token.** A system that creates a random one-time code exploits randomness so the code is unpredictable to an attacker [2].
- **Recommender systems.** When a video platform offers recommendations, some randomness is often injected so that users with the same viewing history do not all see an identical list [3].

In all of these, randomness is not a flaw — it is an intentional feature of the design.

### 5.4 How probabilistic systems differ from deterministic systems — a direct comparison

The input / process / output model from Topic 1.1 applies to both deterministic and probabilistic systems, but the relationship between input and output is different.

**Deterministic flow:**

```
Input ──► Fixed process ──► Single fixed output
(same input always produces this exact output)
```

**Probabilistic flow:**

```
Input ──► Process that includes randomness ──► One of several possible outputs
(same input can produce different outputs on different runs)
```

The process in a probabilistic system includes something the deterministic process does not: a source of randomness. The system uses randomness to choose among the plausible outputs that the input has made possible.

A key step in that choice is called **sampling** — picking one answer from a range of possible answers. Think of it like reaching into a bag of labelled cards and pulling one out: the input determines which cards are in the bag and how many of each kind, and the sampling step is the act of drawing a card. The input still matters — it shapes which outputs are plausible and how likely each is. But the same input fed in twice can still produce two different answers [1][2].

### 5.5 The range of outputs — what varies and what does not

When the same input goes into a probabilistic system many times, the outputs it produces do not appear in completely unpredictable patterns. They follow a pattern — some outputs appear more often than others [1][2].

Think of asking an AI assistant to complete the sentence "The cat sat on the ___." Possible completions might include:

- "mat" — very likely
- "chair" — somewhat likely
- "roof" — less likely
- "quantum accelerator" — extremely unlikely

The input sentence strongly shapes which outputs are probable. "Mat" might appear 60% of the time, "chair" 25%, "roof" 10%, and everything else 5% combined. But "mat" is not guaranteed on any single run [1].

This is why probabilistic systems are not simply random noise. They are constrained by the input — they just cannot be pinned to a single, fixed answer. The variation is bounded and shaped, not arbitrary.

### 5.6 When a probabilistic system is the right tool

Deterministic systems are essential when you need the answer to be exactly the same every time — in arithmetic, financial calculations, and sorting (Topic 1.2). But some problems are genuinely better served by a probabilistic approach [1][2][3].

**Situations where probabilistic is the right tool:**

- **Creative generation.** When the goal is to produce varied, useful content — writing, images, music — you want the system to explore a range of valid outputs, not always produce the same one. Determinism would make every story identical [1].
- **Working with incomplete information.** A medical diagnostic tool that uses patient symptoms to suggest likely conditions cannot give a single deterministic answer because the same symptoms can have different causes. A probabilistic approach gives a ranked list of possibilities with likelihoods — which is more honest and more useful [2].
- **Modelling real-world uncertainty.** A weather model cannot say with certainty what tomorrow holds. Probabilistic forecasting gives a percentage likelihood — more honest than false certainty [2][3].
- **Personalisation at scale.** A recommendation system serving millions of users needs to explore a range of options. Controlled randomness prevents every user from seeing exactly the same recommendations and allows the system to learn what less-obvious options users enjoy [3].

**Situations where deterministic is still required:**

- You need the same input to produce the exact same answer every time — for audit, legal, or safety reasons.
- The correct answer is uniquely defined — arithmetic, sorting, looking up a value in a fixed table.
- Reproducibility is essential — for testing, debugging, or regulatory compliance.

Neither type is universally superior. The right choice depends on what the problem requires [1][2].

### 5.7 Probabilistic systems and temperature — a designed control on randomness

AI systems like language models are probabilistic — we will explore exactly how they work in later topics. But one concept that belongs here is the idea of a **temperature** setting: a control that tells the system how much variation to introduce when sampling [1].

A lower temperature makes the system more predictable — it tends to choose the most likely output almost every time. A higher temperature makes the system more varied — it samples more freely from a wider range of possible outputs, producing more surprising or creative results [1][2].

Temperature is mentioned here because it is a concrete example of a design choice that directly controls the core property of probabilistic systems: how much the output can vary from run to run. You do not need to know the internal mechanics to understand the principle — the setting turns the "dial" on randomness up or down.

### 5.8 Predictability in probabilistic systems

If the output can vary, can you predict anything about a probabilistic system? Yes — and this is important. Probabilistic systems are not unpredictable in a total sense [1][2].

**What you can predict:**

- Which outputs are possible. The input still constrains the output space. A story generator asked about "the sea" will not generate answers about quantum mechanics.
- Which outputs are most likely. Some answers are far more probable than others.
- Long-run behaviour. Over many runs with the same input, you can observe roughly how often each category of answer appears.

**What you cannot predict with certainty:**

- The exact output of any single run. That is what makes the system probabilistic.

This distinction — predictable range and likelihoods, unpredictable single outcome — is what separates a well-designed probabilistic system from pure chaos [1][2].

**Output variation** is the name for this property: the fact that the same input can yield different specific results across runs, even though the shape and distribution of those results remains stable. Understanding output variation is central to working with any probabilistic system [1].

## 6. Implementation

No programming is required for this topic. But here is a thought experiment that makes the concept concrete.

**Simulating a probabilistic system with a physical process:**

Imagine a bag containing ten cards. Seven are labelled "Option A," two are labelled "Option B," and one is labelled "Option C." The input to this system is: "draw a card from the bag." The process is: reach in without looking and pick one. The output is whichever card you drew.

- Run it once: you get "Option A."
- Run it again with the same input: you might get "Option A," "Option B," or "Option C."
- The input is identical both times. The output can vary.
- But "Option A" appears far more often than "Option C" — the range is shaped by the contents of the bag.

This is exactly the structure of a probabilistic system. The "bag" in an AI language model holds a range of possible next words with associated likelihoods; the "card draw" is the sampling step that picks one of them [1][2].

**Applying the three-step determinism test from Topic 1.2 to identify a probabilistic system:**

1. Identify all inputs — including hidden ones.
2. Run the process twice with exactly the same input.
3. Ask: is there any way the output could differ?

For a probabilistic system, step 3 answers yes — and the reason is not a missing hidden input or a mistake. The process itself includes a designed source of variation. That is the signal that you are dealing with a probabilistic system rather than a deterministic one with a hidden input you have not yet found [1].

## 7. Real-World Patterns

### AI content generation

Every time you use a modern AI writing assistant, a probabilistic system is at work. The same prompt can produce different essays, summaries, or code snippets on different runs. This is not randomness for its own sake — it is the system drawing from a range of plausible, coherent outputs. A single "correct" response does not exist for open-ended creative tasks [1][2].

### Spam and fraud detection

Email providers run every incoming message through a system that estimates a spam likelihood. Rather than returning a simple yes or no from a fixed lookup, the system computes a likelihood score based on patterns, then uses that score to decide. Messages near the boundary between spam and not-spam may be handled differently depending on how that score falls [3].

### Medical diagnosis support

Software that assists doctors with diagnosis does not return "this patient definitely has condition X." It returns a ranked list of likely conditions. The same set of symptoms re-entered might yield a slightly different ranking, reflecting the genuine ambiguity of medical evidence. This probabilistic output is considered more trustworthy than a false-certainty binary answer [2][3].

### Personalised recommendation

Streaming and e-commerce platforms use probabilistic approaches to recommend content. Controlled randomness prevents every user with similar history from seeing an identical list and allows the platform to discover which less-obvious options users enjoy [3].

### Forecasting and simulation

Weather forecasting, financial risk modelling, and epidemic spread modelling all use probabilistic simulations. Running the same model many times and aggregating results gives a range of possible futures — far more useful for planning than a single deterministic projection that pretends to know the future exactly [2].

## 8. Best Practices

- **Do not assume variation means error.** If a system produces different outputs for the same input, check whether it is designed to be probabilistic before concluding something is broken. Variability in an AI assistant or a recommendation engine is usually intentional [1].

- **Match the tool to the problem.** Use a deterministic approach when the correct answer is uniquely defined and must be reproducible. Use a probabilistic approach when the problem involves genuine uncertainty, creativity, or ambiguity [1][2].

- **Look for the source of variation.** When a system is probabilistic, ask: where does the randomness enter? Is the system sampling from a weighted set of options? Is there a temperature-like control you can adjust? That understanding helps you reason about how to control the behaviour [1][2].

- **Distinguish "most likely" from "certain."** Probabilistic systems give you information about likelihoods. High-stakes decisions — medical, legal, financial — should treat probabilistic outputs as inputs to human judgement, not as final verdicts [2][3].

## 9. Hands-On Exercise

This exercise connects to the AI Decision Journal activity in the lab session.

1. Open an AI chatbot (any one you have access to) and type the same prompt three times: "Describe computation in one sentence." Copy each response.
2. Compare the three responses. Are they identical? Slightly different? Very different? Write down one word that describes the variation you see.
3. Now run the same experiment with a calculator: type the same arithmetic expression three times. Do the responses vary?
4. In your AI Decision Journal (Entry #1), write one sentence explaining why the chatbot varied but the calculator did not. Use the words "deterministic" and "probabilistic."

The goal is to make the contrast tangible through direct observation, not just through reading.

## 10. Key Takeaways

- **A probabilistic system can produce different outputs from the same input.** This is a designed feature, not a malfunction — the system intentionally includes a source of randomness or uncertainty [1].
- **The input still shapes what outputs are possible and likely** — some outputs are far more probable than others. Probabilistic is not the same as arbitrary [1][2].
- **Sampling is the step where the system picks one answer from a range of plausible answers.** The same input leads to the same range but does not fix which item from that range is selected [1][2].
- **Randomness and uncertainty are design tools.** When a problem involves creativity, ambiguity, or incomplete information, a probabilistic system is often more honest and more useful than a deterministic one [2][3].
- **The contrast with deterministic systems is the key mental model.** Both types process input to produce output; the difference is whether the same input always locks in the same output (deterministic) or leaves room for output variation (probabilistic) [1].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
