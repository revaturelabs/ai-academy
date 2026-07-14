---
topic_id: "7.5"
title: "Temperature — low picks the most likely token, high introduces variation"
position_in_module: 2
generated_at: "2026-06-23T00:00:00Z"
resource_count: 3
---

# 1. Temperature — low picks the most likely token, high introduces variation — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **7.4 Why LLMs output a probability distribution, not a single fixed answer** — the generation loop, the probability distribution over the vocabulary, softmax, and the sampling step. Temperature is a control knob on that sampling step. Without 7.4, this topic has no foundation.
- **7.1 Probability basics — likelihood, events, outcomes** — probability as a number between 0 and 1, sample space, and the idea that probabilities across all outcomes sum to 1. These are used when explaining what "flattening" or "sharpening" a distribution means.

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Explain what temperature is in the context of an LLM (Large Language Model) and what it controls.
- Describe what happens to the probability distribution over the vocabulary when temperature is set low versus high.
- Predict whether a low or high temperature setting is more appropriate for a given task.
- Explain in plain language why temperature 0 makes an LLM behave like a deterministic system.
- Give one real-world example where low temperature is preferable and one where high temperature is preferable.

## 4. Introduction

You have just learned that an LLM does not produce a single fixed answer — it produces a probability distribution over all possible next tokens, then samples from that distribution. A token with a probability of 0.55 is chosen most of the time, but not always [1].

Now imagine you had a dial. Turn the dial down toward zero and the model becomes more cautious — it almost always picks the single most likely token. Turn the dial up and the model becomes more adventurous — it spreads its choices across a wider range of tokens, including ones it would not normally pick [1][3].

That dial is called **temperature**. It is one of the most important settings you can adjust when working with an LLM. Understanding it helps you make sense of when to trust an AI's output, when to expect variation, and why "asking the same question twice" gives different results at some settings and identical results at others [1][2].

This topic explains exactly what temperature does, how it reshapes the probability distribution, and when each setting is useful.

## 5. Core Concepts

### 5.1 What temperature is

**Temperature** — a number you can set (usually between 0 and 2, with some systems going higher) that controls how spread out the probability distribution is before the model samples a token [1][3].

Temperature does not change which words the model knows or what the model has learned. It changes how the model chooses from what it knows. Think of it as adjusting the confidence with which the model commits to its top choice [1].

The name "temperature" comes from physics — in thermodynamics, higher temperature means more energy and more random movement of particles. In the LLM context, the analogy holds: higher temperature means more randomness in the choices the model makes [3].

Here is the key rule:

- **Low temperature (close to 0):** the model becomes more confident and picks the most likely token almost every time.
- **High temperature (close to 1 or above):** the model becomes less confident and spreads probability more evenly, making less likely tokens a real possibility.

### 5.2 How temperature reshapes the distribution

To understand what temperature does mechanically, recall from topic 7.4 that the model produces raw scores (one per token), then applies softmax to turn those scores into probabilities. Temperature is applied before softmax: every raw score is divided by the temperature value [1][3].

You do not need to memorise the maths. The intuition is:

- **Dividing by a small number (low temperature, e.g. 0.2)** makes the raw scores more spread apart — the gap between the highest score and the others grows. When softmax then runs on those more-spread scores, it assigns an even higher probability to the top token and drives the others closer to zero. The distribution becomes **sharp** — most of the probability mass sits on one or two tokens.
- **Dividing by a large number (high temperature, e.g. 1.5)** makes the raw scores closer together — the gap between the highest and the rest shrinks. When softmax runs on those compressed scores, it distributes probability more evenly. The distribution becomes **flat** — many tokens have meaningful probability, not just the top one [1][3].

A concrete illustration. Suppose after "The sky is," the model's raw distribution (before temperature adjustment) looks like this:

| Next token | Probability at temperature 1.0 |
|---|---|
| "blue" | 0.55 |
| "clear" | 0.18 |
| "dark" | 0.12 |
| "grey" | 0.08 |
| "falling" | 0.04 |
| (all others) | 0.03 combined |

Now watch what happens at different temperature settings:

| Next token | Temp 0.2 (low) | Temp 1.0 (neutral) | Temp 1.5 (high) |
|---|---|---|---|
| "blue" | ~0.97 | 0.55 | ~0.36 |
| "clear" | ~0.02 | 0.18 | ~0.20 |
| "dark" | ~0.01 | 0.12 | ~0.17 |
| "grey" | ~0.00 | 0.08 | ~0.14 |
| "falling" | ~0.00 | 0.04 | ~0.09 |
| (others) | ~0.00 | 0.03 | ~0.04 |

At temperature 0.2, "blue" dominates — the model will almost certainly pick it. At temperature 1.5, "blue" is still the most likely single token, but the others are competitive. "Clear," "dark," and "grey" all have meaningful probability [1][3].

### 5.3 The special case: temperature 0

Temperature 0 is a special setting. Dividing any number by 0 is mathematically undefined, so systems that offer temperature 0 do not literally divide by zero. Instead, they apply a rule: always pick the token with the highest probability, no matter what [1][3].

**Temperature 0 = always pick the top token.**

This turns the LLM from a stochastic system back into a deterministic system (both terms from topic 7.4). Give it the same prompt twice and it gives the same response both times. There is no sampling — the model simply commits to its single most likely choice at every step [1].

When is this useful? When you need reliability and repeatability — for example, when you are testing whether the model gives a factually correct answer and you want that answer to be consistent, not randomly different each time you check [2].

When is it limiting? When you need variety, creativity, or when you want to explore different valid phrasings. Temperature 0 locks in one path and never explores alternatives [1].

### 5.4 Low temperature versus high temperature — what each is for

| Setting | Behaviour | Best for | Watch out for |
|---|---|---|---|
| Low (0 to ~0.5) | Predictable, consistent, picks most likely tokens | Factual Q&A, classification, yes/no tasks | Can produce repetitive or generic text; less creative |
| Medium (~0.7–1.0) | Balanced — some consistency, some variety | General conversation, summarisation, explanation | Output still varies; not fully repeatable |
| High (above 1.0) | Adventurous, varied, explores less likely tokens | Creative writing, brainstorming, generating many options | Can produce incoherent or off-topic text; less reliable |

The right setting depends on what you need the model to do. There is no universally "best" temperature — it is a trade-off between reliability and creativity [1][2].

### 5.5 Temperature and trust — what this means for you

Temperature directly affects how much you can predict and trust an AI's output.

At **low temperature**, the model's output is more predictable. Run the same prompt ten times and you get nearly the same result each time. This makes it easier to evaluate accuracy — you can check whether the model's consistent answer is correct [2].

At **high temperature**, the model's output varies. Run the same prompt ten times and you get ten different responses. This is useful for generating ideas, but it makes accuracy harder to measure — each run is a different draw from a broader part of the distribution [2].

A key insight: changing the temperature does not make the model smarter or more knowledgeable. It only changes how confidently the model commits to its most likely choices. A model at temperature 0 gives you its single best guess — but that best guess can still be wrong [1][2].

This matters for your A3 Maths and Cognition Lab Report: understanding temperature is part of understanding when and how much to trust AI outputs.

## 6. Implementation

There is no code in this topic — but the mechanism can be traced as a clear sequence of steps.

**How temperature is applied during generation — step by step:**

1. **The model produces raw scores.** After reading the context (your prompt plus any tokens already generated), the model computes one raw score for every token in the vocabulary.
2. **Divide each raw score by the temperature value.** If temperature is 0.5, every raw score gap is amplified (distribution sharpens). If temperature is 2.0, every raw score gap is compressed (distribution flattens).
3. **Apply softmax.** The adjusted scores are converted into probabilities that sum to 1 — the sharpened or flattened distribution.
4. **Sample one token.** The model picks one token from the adjusted distribution. At temperature 0, this step is replaced by simply picking the token with the highest probability.
5. **Append the token and continue.** The generation loop continues with the newly chosen token added to the context.

Steps 1–5 repeat for every token in the output. The temperature setting stays constant throughout a single generation run [1][3].

## 7. Real-World Patterns

**Customer service chatbots (low temperature).** Systems that answer questions about order status, opening hours, or return policies use low temperature. The same question should give the same answer — consistency and accuracy matter more than variety [1].

**Creative writing assistants (high temperature).** Tools designed to help with fiction, poetry, or brainstorming use higher temperature. Users want varied suggestions; the model explores less obvious word choices and phrasings [1][3].

**API access and developer settings.** When developers integrate LLM APIs (Application Programming Interfaces — connection points that let software talk to an LLM service) into products, temperature is typically one of the first parameters they configure. A factual knowledge-base tool might default to 0.2; a creative idea generator might default to 1.2 [3].

**Research on LLM reliability.** Studies have found that temperature directly affects how often LLMs give correct answers on structured tasks. At very low temperatures, models are more consistent but may repeat the same mistake every time. At higher temperatures, errors vary more — which can sometimes be measured and corrected by running many samples and taking the most common answer [2].

## 8. Best Practices

**Do:**

- Set temperature low (0–0.5) when accuracy and consistency matter — factual questions, structured tasks, yes/no answers.
- Set temperature higher (0.8–1.2) when variety matters — creative tasks, generating multiple options to choose from.
- Run the same prompt multiple times at your chosen temperature to get a sense of how much the output varies — this tells you how much to trust a single response.
- Remember that temperature 0 does not guarantee a correct answer — it guarantees a consistent answer.

**Don't:**

- Assume that higher temperature means better or more intelligent output. It means more variety, not more accuracy.
- Use high temperature for tasks where wrong answers are harmful — a model producing plausible-sounding but incorrect responses happens more readily at high temperature.
- Treat a consistent low-temperature response as automatically trustworthy — consistency and correctness are different things.

## 9. Hands-On Exercise

This exercise matches the lab activity for week 7 and feeds directly into your A3 Maths and Cognition Lab Report.

1. Access any AI chat tool that lets you adjust temperature (or use any tool and frame your requests as "give me only your single best answer" vs "give me a varied, creative response" to simulate low and high temperature).
2. Pick five yes/no factual questions — for example: "Is the capital of France Paris?" Run each question at temperature 0 (or the lowest available setting) ten times. Record the answers in a table.
3. Run the same five questions at temperature 1 (or the highest available setting) ten times each. Record the answers.
4. Tally: how many unique responses did you get at low temperature versus high temperature? How often was each setting correct?
5. Write a 200-word interpretation — what do the results tell you about trusting AI outputs at different temperature settings?

## 10. Key Takeaways

- **Temperature controls how spread out the probability distribution is before sampling.** Low temperature sharpens the distribution so the top token dominates; high temperature flattens it so many tokens are competitive.
- **Temperature 0 makes an LLM deterministic.** The model always picks its single most likely token — the same prompt gives the same response every time.
- **Low temperature is better for reliability; high temperature is better for variety.** Neither is universally correct — the right choice depends on what you need.
- **Changing temperature does not change the model's knowledge.** It only changes how confidently the model commits to its top choices. A low-temperature response is consistent, not necessarily correct.
- **Temperature is a key factor in trusting AI output.** Understanding what temperature does helps you interpret when AI responses are predictable, when they vary, and how that affects the value of any single response.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
