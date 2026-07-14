---
topic_id: "7.4"
title: "Why LLMs output a probability distribution, not a single fixed answer"
position_in_module: 1
generated_at: "2026-06-22T00:00:00Z"
resource_count: 3
---

# 1. Why LLMs output a probability distribution, not a single fixed answer — Topic Corpus

## 2. Prerequisites

This topic builds on:

- **7.1 Probability basics — likelihood, events, outcomes** — the idea that probability is a number between 0 and 1, that a sample space is the complete list of all possible outcomes, and that an event is a subset of those outcomes. All three concepts are used directly here.
- **7.2 Conditional probability — P(A given B)** — the idea that the probability of something changes depending on what you already know. LLM token prediction is a direct application of this idea.
- **7.3 Bayes' theorem intuition — updating belief with new evidence** — the idea that a prior belief is updated by evidence into a posterior belief. LLM generation is a sequential version of this updating process.

From week 6 of this course: **vectors** and **embeddings** are used briefly when explaining how input text is converted to a form the model can process. No new maths from week 6 is required — those terms are used as vocabulary only.

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Explain in plain language what a probability distribution over a vocabulary is and why an LLM produces one at each step.
- Describe what a token is and why LLMs work on tokens rather than whole words or whole sentences.
- Trace the three-stage loop — take in context, compute a distribution, pick a token — and explain what happens at each stage.
- Explain the difference between a deterministic system (always gives the same answer) and a stochastic system (can give different answers), and identify which category LLMs belong to.
- Give one everyday analogy and one LLM-specific example that illustrate why the same prompt can produce different outputs on different runs.

## 4. Introduction

You have probably noticed that asking an AI chatbot the same question twice does not always give you the same answer. Sometimes the wording changes. Sometimes entirely different information appears. This is not a bug. It is a direct consequence of how LLMs (Large Language Models) work at a mathematical level [1].

A calculator is a **deterministic** system — it always gives the same answer to the same input. Type `2 + 2` and you always get `4`. No variation. No surprises. An LLM is different. It is a **stochastic** system — a system that involves randomness. Feed it the same prompt and it can, in principle, produce a different response every time [3].

Why? Because an LLM does not look up a fixed answer in a table. Instead, at each moment of generating a response, it computes a **probability distribution** — a list of every possible next word (actually, every possible next token) together with a score for how likely each one is. Then it picks one. That picking step involves randomness, which is why two runs of the same prompt can produce two different responses [1][2].

This topic explains that process in detail — what a probability distribution over a vocabulary is, how the model computes it, and why the element of chance is baked in by design, not by accident. The question of how much randomness is injected is controlled by a setting called *temperature*, which you will explore in topic 7.5.

## 5. Core Concepts

### 5.1 What is a token?

Before anything else, you need to understand what an LLM actually reads and writes, because it is not whole words or whole sentences — it is **tokens**.

**Token** — a chunk of text that the model processes as a single unit. In English, a token is roughly a word or part of a word. The word "running" might be one token. The word "unbelievable" might be split into two tokens: "un" and "believable". Common short words like "the" or "a" are typically one token each. Punctuation marks and spaces are also tokens [1][2].

Why tokens and not whole words? Because a fixed list of every possible word in every possible language would be enormous and hard to manage. Tokens are a practical compromise: a vocabulary of roughly 50,000 to 100,000 tokens can cover virtually any text in English (and many other languages) by combining parts [2].

**Vocabulary** — the complete, fixed list of all tokens the model knows about. Every token that can ever appear in the model's output is somewhere in this list. Think of it as the model's alphabet, but instead of 26 letters it has tens of thousands of entries [1].

The vocabulary is fixed at training time. The model cannot invent a token that was not in its training vocabulary.

### 5.2 What is a probability distribution over the vocabulary?

At every step of generating a response, the LLM assigns a probability to every single token in its vocabulary. The result is a **probability distribution over the vocabulary** — a list where:

- each entry is one token, and
- each entry has a number between 0 and 1 that represents how likely that token is to come next, and
- all the numbers add up to exactly 1.0 [1][2].

This is a probability distribution in exactly the sense you studied in topic 7.1: a complete set of outcomes (all tokens in the vocabulary) each with a probability, and the probabilities sum to 1.

Here is a tiny made-up example. Suppose the model has just seen the text "The sky is" and is about to generate the next token. The distribution might look something like this (using a very small vocabulary for illustration):

| Next token | Probability |
|---|---|
| "blue" | 0.55 |
| "clear" | 0.18 |
| "dark" | 0.12 |
| "grey" | 0.08 |
| "falling" | 0.04 |
| (all other tokens) | 0.03 combined |

Every token in the full vocabulary has a score. "Blue" has the highest score here — but the others are not zero. "Clear" has an 18% chance, "dark" has a 12% chance, and so on [1].

Key point: the model does not simply select the highest-probability token automatically. It has a list of many possible next tokens, each with a weight. What happens next is a picking step — covered in section 5.4.

### 5.3 How the model computes the distribution — softmax in plain language

The model does not start with a list of probabilities. It starts with a list of raw scores — one number per token. These raw scores come from the model's internal calculations (the details of those calculations involve the neural network architecture and are beyond this topic's scope).

The raw scores can be any numbers — positive, negative, very large, very small. They are not yet probabilities because they do not sum to 1. To convert them into a proper probability distribution, the model applies a mathematical function called **softmax**.

**Softmax** — a function that takes a list of raw scores and converts them into probabilities that sum to 1. Tokens with higher raw scores get higher probabilities; tokens with lower scores get lower probabilities. The function ensures every probability is between 0 and 1 and all of them add up to exactly 1 [2].

You do not need to memorise the softmax formula. The key intuition is:

1. Tokens that the model "favours" based on the context get high raw scores.
2. Softmax converts those scores into a fair competition — everyone gets a probability, nothing is forced to zero.
3. The result is a proper probability distribution over the vocabulary [1][2].

Softmax is the step that turns the model's internal judgements into the kind of probability distribution you studied in topic 7.1.

### 5.4 The picking step — why the same prompt gives different answers

Once the model has a probability distribution, it needs to choose one token. How does it do that?

It uses **sampling** — a process of randomly choosing one outcome from a probability distribution, where the probability of choosing each outcome equals its weight in the distribution [3].

**Sampling** — picking one item from a list at random, where items with higher probability are more likely to be picked but are not guaranteed to be picked every time.

Think of it like a weighted lottery. In topic 7.1 you studied the idea that equally likely outcomes each have a probability of 1 divided by the total number of outcomes. Sampling from a probability distribution is the generalised version of that idea: outcomes are not equally likely, but the probability of picking each one matches its assigned probability weight.

Returning to the example from section 5.2. If the model samples from:

| Next token | Probability |
|---|---|
| "blue" | 0.55 |
| "clear" | 0.18 |
| "dark" | 0.12 |
| "grey" | 0.08 |
| "falling" | 0.04 |

then about 55% of the time, the model will pick "blue." But 45% of the time it will pick something else. If you run the same prompt twice, you might get "The sky is blue" once and "The sky is clear" the next time [3].

This is why LLMs are stochastic. The randomness is not noise or malfunction — it is a deliberate feature of the sampling step. Each run is a fresh draw from the distribution [1][3].

**Deterministic vs stochastic — a direct comparison:**

| Property | Deterministic system | Stochastic system |
|---|---|---|
| Definition | Same input always gives same output | Same input can give different outputs |
| Example | A calculator computing 2 + 2 | An LLM generating a response |
| Source of variation | None | Randomness in the sampling step |
| Predictability | Fully predictable | Probabilistic — high-probability outcomes are more likely but not certain |

### 5.5 The generation loop — one token at a time

An LLM does not write a complete response all at once. It generates text one token at a time, in a loop. Each pass through the loop produces one token, which is then added to the context, and the loop runs again [1][2].

The loop has three steps at each iteration:

1. **Take in the context.** The model reads all the tokens so far — your original prompt plus every token the model has already generated in earlier iterations of this loop.
2. **Compute a probability distribution.** Using that full context, the model computes a fresh distribution over all tokens in the vocabulary. The context directly shapes this distribution — which is why the model's output is coherent rather than random nonsense. This is conditional probability in action: the probability of the next token depends on all the previous tokens [1][2].
3. **Sample one token.** The model picks one token from the distribution using the sampling process described in section 5.4. That token is appended to the growing output.

The loop continues until the model samples a special end-of-sequence token (a signal that the response is complete) or until a maximum length is reached.

**Example trace — generating "The sky is blue today":**

| Iteration | Context fed to model | Distribution peak | Token sampled |
|---|---|---|---|
| 1 | "The sky is" | "blue" (0.55) | "blue" |
| 2 | "The sky is blue" | "today" (0.42) | "today" |
| 3 | "The sky is blue today" | [END] (0.81) | [END] — stop |

At iteration 1, if the sampling had landed on "clear" instead of "blue," the entire rest of the response would have developed differently — because the context fed into iteration 2 would have been "The sky is clear" instead [3].

This is the cascade effect. A single different choice early in the loop ripples forward through every subsequent step. It is why two runs of the same prompt can diverge substantially after just a few tokens [3].

### 5.6 Why a distribution rather than just the top answer?

A natural question: why not just always pick the highest-probability token? That would make LLMs deterministic — the same prompt would always give the same answer.

There are two reasons the designers chose to use a distribution and a sampling step rather than always picking the top entry [1][3]:

**Reason 1 — Quality and diversity.** Always picking the top token can lead to repetitive, generic text. The model locks into common patterns and produces the most statistically average response. Using the full distribution allows the model to occasionally pick a less-common but perfectly valid word, producing more varied and natural-sounding language.

**Reason 2 — Avoiding dead ends.** Sometimes the highest-probability token leads the sentence into a grammatical or semantic corner that forces worse tokens in later steps. Sampling from the distribution gives the model a chance to avoid those traps by occasionally choosing a slightly less obvious path that works better in the long run.

The balance between following the top answer and using the full distribution — how much randomness is injected — is controlled by a setting called *temperature*, which you will explore in topic 7.5.

## 6. Implementation

There is no code at this stage. The token-by-token generation loop follows a clear procedure you can trace manually.

**The LLM generation procedure — step by step:**

1. **Receive the prompt.** The user's input is split into tokens using the model's vocabulary. The result is a sequence of tokens representing the input text.
2. **Pass the token sequence to the model.** The model processes the entire sequence, using its internal representations (embeddings and related mechanisms) to build a picture of the context.
3. **Produce raw scores.** The model outputs one raw score for every token in the vocabulary. A higher score means the model considers that token a better continuation given the context.
4. **Apply softmax.** Convert the raw scores to probabilities. The result is a probability distribution — a list of (token, probability) pairs that sum to 1.
5. **Sample one token.** Use the distribution to randomly select one token. Tokens with higher probability are more likely to be chosen but are not guaranteed to be chosen.
6. **Append the sampled token to the context.** The output grows by one token.
7. **Check for a stopping condition.** If the sampled token is the end-of-sequence token, or if the maximum output length has been reached, stop. Otherwise, return to step 3 with the updated context.

Steps 3 through 7 repeat for every token in the output. A 100-token response means the loop ran 100 times [1][2].

## 7. Real-World Patterns

**Chat assistants.** When you ask a chat assistant a question, the model runs the generation loop until it produces a complete response. The probability distribution shifts at every token based on what came before. A small random draw early in the loop can send the response in a noticeably different direction — which is why asking the same question twice sometimes yields a different emphasis or structure [1][3].

**Autocomplete on a phone keyboard.** Phone keyboards show you the three most likely next words. That shortlist is produced by a small model doing exactly what is described here: taking your last few words as context, computing a distribution over possible next words, and displaying the top entries. The model does not show you the full distribution — only the top few — but the distribution is what the model computes [2].

**Writing assistance tools.** AI writing tools that "continue" a paragraph are running the generation loop until a paragraph boundary is reached. Because sampling introduces randomness, clicking "regenerate" can produce a noticeably different continuation from the same starting text. This is the stochastic property in direct action [3].

**Medical and legal language generation (cautionary pattern).** Because LLMs sample from a distribution rather than look up verified facts, the model can and does sample low-probability but syntactically plausible tokens — including incorrect claims that happen to fit the context well in terms of language patterns. This is one reason human review remains important in high-stakes settings. The model's output reflects language-pattern probability, not verified truth [1][3].

## 8. Best Practices

**Do:**

- Expect variation. When you run the same prompt twice and get slightly different answers, that is the stochastic sampling working as designed — not an error.
- Use multiple runs when accuracy matters. If the question has one correct answer, running the prompt several times and looking for consistency across runs is a practical way to assess reliability.
- Remember that a high-probability output is not necessarily correct. A token being likely means it fits the language patterns in the training data — it does not mean it is factually accurate.

**Don't:**

- Assume the model "knows" the answer and is just choosing how to phrase it. The model assigns probabilities based on patterns in training data. A confident-sounding output and a correct output are not the same thing.
- Treat two different responses to the same prompt as a sign that the system is broken. Variation is a property of stochastic systems — it is expected.
- Confuse the probability distribution with certainty. A token with probability 0.90 is chosen 90% of the time — but 10% of the time something else is chosen. Even high-probability outputs can be wrong.

## 9. Hands-On Exercise

No special equipment needed — just a browser and access to any AI chat tool.

**Scenario:** You want to observe stochastic behaviour directly.

1. Pick one short, open-ended prompt — for example: "Describe the colour blue in one sentence."
2. Send the prompt five times in a row (refresh or start a new chat each time if the system caches answers).
3. Record each response word-for-word in a table.
4. Identify which words or phrases are the same across most or all runs (high-probability tokens) and which vary (lower-probability tokens that got sampled on some runs but not others).
5. Write two sentences connecting what you observe to the generation loop described in section 5.5.

_Note: if you set temperature to 0 in a system that allows it, the model will always pick the top token — making it deterministic. You will study temperature in topic 7.5._

## 10. Key Takeaways

- **An LLM produces a probability distribution at every step, not a fixed answer.** At each point in the generation loop, the model assigns a probability to every token in its vocabulary. The probabilities sum to 1.
- **The generation loop runs one token at a time.** Each iteration takes the full context, computes a fresh distribution via softmax, and samples one token. The loop repeats until the response is complete.
- **Sampling introduces randomness.** The model does not always pick the highest-probability token. It picks from the distribution, so the same prompt can produce different outputs on different runs.
- **LLMs are stochastic systems, not deterministic ones.** This is by design — sampling from the distribution produces more varied, natural language than always picking the top token would.
- **Probability reflects language patterns, not verified truth.** A high-probability output fits the model's training data well. That is not the same as being factually correct.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
