---
topic_id: "7.3"
title: "Bayes' theorem intuition — updating belief with new evidence"
position_in_module: 3
generated_at: "2026-06-22T00:00:00Z"
resource_count: 3
---

# 1. Bayes' theorem intuition — updating belief with new evidence — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **7.1 Probability basics — likelihood, events, outcomes** — the concepts of probability (a number between 0 and 1), sample space (the complete list of all possible outcomes), and event (a subset of the sample space) are used throughout this topic.
- **7.2 Conditional probability — P(A given B)** — the notation P(A | B), the idea of a reduced sample space, and the conditional probability formula P(A | B) = P(A and B) / P(B) are the direct foundation for Bayes' theorem. Review topic 7.2 before continuing if any of those terms are unfamiliar.

No arithmetic beyond simple fractions is assumed. No prior statistics, algebra, or maths course is needed.

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Describe in plain language what Bayes' theorem does — it updates an existing belief when new evidence arrives.
- Explain the meaning of the three named pieces in Bayes' theorem: prior, likelihood, and posterior.
- Use the worked rain-and-clouds example to trace how a prior belief becomes a posterior belief after evidence is applied.
- Explain why Bayes' theorem is just conditional probability reorganised — P(A | B) expressed in terms of P(B | A).
- Give one everyday example and one AI-relevant example of Bayesian updating in action.

## 4. Introduction

You have already learned that conditional probability captures the idea of updating probability when you know something new. Suppose you know there are dark clouds outside. That information — the condition — changes how likely you think rain is. You used the formula P(rain | dark clouds) to express that updated probability precisely [1].

But now imagine a slightly different question. You are inside with no windows. You hear a rumble. You ask: "Does that sound mean it is raining?" You start with a general sense of how often it rains on a day like today. Then you ask: "If it were raining, how likely is it that I would hear a rumble?" You combine those two pieces of knowledge to update your belief. That reasoning process — starting with a prior belief, observing some evidence, and arriving at an updated belief — is exactly what Bayes' theorem captures [1][3].

Bayes' theorem is not a new formula invented from scratch. It is conditional probability reorganised. Once you understand P(A | B) from topic 7.2, Bayes' theorem is simply a way to "flip" the question — to find P(A | B) when what you actually know is P(B | A). This topic teaches you the intuition behind that flip and the names mathematicians give to each part. No derivation. No proof. Just the idea [2].

## 5. Core Concepts

### 5.1 The idea of updating a belief

Think of your brain as holding a belief meter for any claim — a number between 0 and 1 that represents how confident you are. Before you look at any evidence, that meter sits at some starting value. Mathematicians call this starting value the **prior** (short for "prior probability" or "prior belief") [1].

**Prior** — your initial estimate of how likely something is, before you have seen any new evidence. It is based on what you already know from background knowledge or past experience.

For example, if you know that it rains about 3 days out of every 10 in your city, your prior probability of rain on any given day is roughly 0.3.

Now you observe something — a piece of evidence. That evidence either makes the claim feel more likely or less likely. After you factor the evidence in, your belief meter moves to a new value. Mathematicians call this updated value the **posterior** (short for "posterior probability").

**Posterior** — your updated estimate of how likely something is, after you have taken new evidence into account. The posterior is what comes after [1][3].

The word "prior" means before. The word "posterior" means after. These two words describe the same belief at two different moments in time: before evidence and after evidence. Bayes' theorem is the rule that tells you how to move from the prior to the posterior [3].

### 5.2 The missing piece — likelihood

To move from prior to posterior, you need to know one more thing: how well does the evidence fit with the claim being true?

**Likelihood** — how probable the evidence is, assuming the claim is actually true. In notation: P(evidence | claim) — the probability of observing this evidence if the claim were the case [2].

Continuing the rain example:
- **Claim:** it is raining.
- **Evidence:** dark clouds are visible.
- **Likelihood:** P(dark clouds | rain). If rain almost always comes with dark clouds, this is high — say 0.9. If rain sometimes appears without clouds (unusual but possible), this might be lower.

The likelihood is the bridge between the prior and the posterior. Without it, you would have no way to know how much the evidence should shift your belief. A piece of evidence with a very high likelihood under the claim is strong evidence — it should push the posterior much higher than the prior. Weak or ambiguous evidence barely moves the posterior [2][3].

### 5.3 Bayes' theorem — the rule as a named equation

With the three pieces named, here is Bayes' theorem expressed as a named equation. You will see this written out; you are not expected to derive it or prove it:

```
Posterior  =  Likelihood × Prior
              ───────────────────
                   Evidence
```

Or, using the standard probability notation for a claim A and evidence B:

```
P(A | B)  =  P(B | A) × P(A)
             ─────────────────
                  P(B)
```

Each piece has a plain-English name:

| Symbol | Name | Plain meaning |
|---|---|---|
| P(A \| B) | **Posterior** | Your updated belief in A after seeing B |
| P(B \| A) | **Likelihood** | How probable B is if A were true |
| P(A) | **Prior** | Your belief in A before seeing B |
| P(B) | **Evidence** (marginal probability of B) | How probable B is overall, regardless of A |

Why does this look like conditional probability from topic 7.2? Because it is. Recall the conditional probability formula: P(A | B) = P(A and B) / P(B). Bayes' theorem uses the fact that P(A and B) can be rewritten as P(B | A) × P(A). That substitution is the only algebra involved. The result is still a conditional probability — just written in terms of the reverse conditional P(B | A) and the prior P(A) [2].

You do not need to memorise the algebra. What matters is the meaning: Bayes' theorem lets you find the probability of a cause given an effect (P(A | B)), when you know the probability of the effect given the cause (P(B | A)). That "flip" is the useful move [1][2].

### 5.4 Worked example — the rain and clouds story

Let's trace through the numbers using the same scenario that has run through topics 7.1 and 7.2.

**Setup:**

- On any given day, the probability of rain is 0.3. This is the **prior**: P(rain) = 0.3.
- On days when it rains, the probability of seeing dark clouds is 0.9. This is the **likelihood**: P(dark clouds | rain) = 0.9.
- On days when it does not rain, the probability of seeing dark clouds is 0.2. This captures the case where clouds appear but lead to nothing.

**Question:** You look outside and see dark clouds. What is the updated probability of rain? That is: what is the **posterior** P(rain | dark clouds)?

**Step 1 — prior:** P(rain) = 0.3. Before you look outside, your best estimate is a 30% chance of rain.

**Step 2 — likelihood:** P(dark clouds | rain) = 0.9. If it were raining, you would see dark clouds 90% of the time.

**Step 3 — compute P(dark clouds) overall:**

You need P(dark clouds) — the probability of seeing dark clouds regardless of whether it rains. You sum over both possibilities:

```
P(dark clouds)  =  P(dark clouds | rain) × P(rain)
                 + P(dark clouds | no rain) × P(no rain)

                =  0.9 × 0.3  +  0.2 × 0.7

                =  0.27 + 0.14  =  0.41
```

Dark clouds appear about 41% of the time overall.

**Step 4 — apply Bayes' theorem:**

```
P(rain | dark clouds)  =  P(dark clouds | rain) × P(rain)
                          ─────────────────────────────────
                                   P(dark clouds)

                       =  0.9 × 0.3
                          ─────────
                             0.41

                       =  0.27 / 0.41  ≈  0.66
```

**Result:** The posterior probability is about 0.66. Seeing dark clouds updates your belief in rain from 30% (your prior) to roughly 66% (your posterior). The evidence moved the belief upward significantly, because dark clouds are a strong signal of rain [1][3].

**Summary of the update:**

| Moment | Belief in rain | What changed |
|---|---|---|
| Before looking outside | 0.30 (prior) | Background knowledge only |
| After seeing dark clouds | 0.66 (posterior) | Dark clouds applied as evidence |

The posterior becomes the new starting point. If you then hear thunder, you would run Bayes' theorem again — the previous posterior (0.66) becomes the new prior [1].

### 5.5 Why it is conditional probability reorganised

You already know from topic 7.2 that P(A | B) = P(A and B) / P(B). Bayes' theorem does not change what a conditional probability is. It changes how you compute it [2].

The standard conditional probability formula asks: "I know P(A and B) and P(B) — compute P(A | B)."

Bayes' theorem is useful when you know P(B | A) and P(A) instead — which is often what you actually have. In the rain example, you knew P(dark clouds | rain) = 0.9 (how clouds behave when it rains) rather than P(rain and dark clouds) directly. Bayes' theorem is the algebraic bridge from one form to the other.

This "flipping the conditional" is the core move. You start with P(effect | cause) and arrive at P(cause | effect). In the rain example:

- You know: P(dark clouds | rain) — the effect given the cause.
- You want: P(rain | dark clouds) — the cause given the effect.

Bayes' theorem lets you make that flip. That is why it is so useful in diagnosis, detection, and AI — you often observe an effect (a symptom, a signal, a word) and want to infer the cause (a disease, an event, an intent) [2][3].

### 5.6 What changes and what stays constant — Bayesian updating

A common question is: does Bayes' theorem change every time you apply it? The rule stays the same. The numbers change each time you get new evidence.

| What stays the same | What changes |
|---|---|
| The formula structure | The prior (updated after each round) |
| The meaning of prior, likelihood, posterior | The evidence you observe |
| The mathematical relationship | The resulting posterior |

Each time you get new evidence, the most recent posterior becomes the new prior. Then you apply the rule again. This process — repeatedly updating a belief as evidence accumulates — is called **Bayesian updating** [3].

**Bayesian updating** — the process of repeatedly applying Bayes' theorem as new pieces of evidence arrive, each time using the previous posterior as the new prior. Belief shifts gradually and systematically as evidence accumulates.

This is not an arbitrary process. The mathematics guarantees that if you keep collecting good evidence, your posterior will converge toward the truth. The more evidence you have, the less the starting prior matters — strong evidence eventually overwhelms even a very wrong initial guess [1][3].

## 6. Implementation

There is no code at this stage. The Bayesian updating process follows a consistent set of named steps you can apply to any scenario.

**Bayesian belief-update procedure:**

1. **Name the claim (A).** What are you trying to assess the probability of? State it clearly. Example: "It is raining."
2. **Set the prior P(A).** What is your best estimate before any new evidence? Use background knowledge or historical data. Example: P(rain) = 0.3.
3. **Name the evidence (B).** What new observation have you made? Example: "Dark clouds are visible."
4. **Assess the likelihood P(B | A).** If the claim were true, how probable is this evidence? Example: P(dark clouds | rain) = 0.9.
5. **Compute P(B) overall.** How probable is the evidence regardless of the claim? This requires considering both the "A is true" and "A is false" cases and summing them. Example: P(dark clouds) = 0.41.
6. **Apply Bayes' theorem.** Posterior = Likelihood × Prior / P(B). Example: 0.9 × 0.3 / 0.41 ≈ 0.66.
7. **Interpret the posterior.** Did the evidence raise or lower your belief? By how much? Is the shift proportionate to how strong the evidence was?
8. **Repeat if new evidence arrives.** The posterior from step 6 becomes the new prior. Return to step 3.

This procedure applies whether you are reasoning about weather, medical tests, spam detection, or AI confidence scores [1][2][3].

## 7. Real-World Patterns

**Medical testing.** A doctor tests a patient for a condition. Before the test, the doctor has a prior estimate based on the patient's symptoms and demographics — say, a 5% chance the patient has the condition. The test comes back positive. The likelihood of a positive result given the condition is, say, 95%. Bayes' theorem gives the posterior: the updated probability of the condition given the positive test result. Crucially, this posterior is not automatically very high — it depends strongly on how common the condition is in the first place. This is a practical medical reasoning problem, and Bayes' theorem is the tool that makes it precise [3].

**Search engines and spam filters.** An email filter starts with a prior probability that any incoming message is unwanted. It then observes evidence — specific words, sender patterns, formatting. For each piece of evidence, it applies a likelihood: "If this message were unwanted, how probable would it be to contain the word 'urgent'?" The posterior after processing all the evidence becomes the filter's confidence score. Bayesian spam filtering was one of the first commercially successful applications of this reasoning style [2][3].

**AI language models and next-token probability.** When an LLM (Large Language Model) generates text, it assigns a probability to each possible next token based on all the tokens that came before. This is a form of conditional probability — covered in topic 7.2. The probabilistic reasoning behind how models estimate which word is most probable given context draws on the same underlying principles as Bayes' theorem. You will explore how LLMs use probability distributions in topic 7.4 [1].

**Navigation systems.** A car's navigation system starts with a prior about where the car is (its last known position). As new sensor readings arrive — GPS, camera, proximity sensors — each is treated as evidence. The system applies Bayesian updating to move from a noisy prior to a sharper posterior about the car's true position. Both humans and machines use this same pattern: start with a belief, observe evidence, update the belief [3].

## 8. Best Practices

**Do:**

- Always name the prior, the likelihood, and the evidence explicitly before applying the formula. Skipping the naming step is the most common source of errors — it becomes unclear what is being updated and what is doing the updating.
- Check whether your posterior makes intuitive sense. Bayesian results that contradict your intuition are worth re-examining — sometimes intuition is wrong, but sometimes a component (prior or likelihood) has been set incorrectly.
- Remember that the posterior can go up or down. Evidence that contradicts the claim will lower the posterior, not raise it. A piece of evidence that is very unlikely if the claim were true is a reason to reduce belief, not increase it.
- Use the posterior as the new prior when more evidence arrives. Each update is incremental — you never discard what you have already learned.

**Don't:**

- Confuse P(A | B) and P(B | A). The whole point of Bayes' theorem is that these are not the same. "The probability of rain given dark clouds" is not the same as "the probability of dark clouds given rain."
- Assume the posterior equals the likelihood. The likelihood P(B | A) is an input to the calculation, not the answer. The answer is P(A | B), and it depends on the prior and P(B) as well.
- Set the prior to 0 or 1. A prior of 0 means you consider something completely impossible — no amount of evidence can update a belief if the prior is 0. A prior of 1 means you are completely certain before looking — evidence is irrelevant. In practice, neither extreme is appropriate unless you are truly certain before any evidence.
- Skip the prior and rely only on the likelihood. Ignoring how common the claim is to begin with is a reasoning error — you will encounter it by name in a later topic in this course.

## 9. Hands-On Exercise

No equipment required — paper and a calculator (or a smartphone calculator) are enough.

**Scenario:** A hospital uses a screening test for a rare infection. The infection affects 2% of people who come in for a general check-up — so P(infected) = 0.02 (this is the prior). The test is sensitive: if you are infected, the test is positive 95% of the time — P(positive | infected) = 0.95 (this is the likelihood). But the test also produces false positives: if you are not infected, the test is still positive 10% of the time — P(positive | not infected) = 0.10.

**Part A — compute P(positive test) overall:**

Use the same two-case summing approach from the worked example. Compute P(positive) by considering both the "infected" and "not infected" cases.

**Part B — apply Bayes' theorem:**

Given that a patient's test came back positive, what is the posterior probability that they are actually infected? Compute P(infected | positive test).

**Part C — interpret:**

Write two sentences explaining why the posterior might be lower than you expected, given that the test sensitivity is 95%.

_Hint: the prior of 2% (the infection is rare) interacts with the evidence. When a condition is rare, even a good test produces many false positives in a large population._

## 10. Key Takeaways

- **Bayes' theorem updates a prior belief into a posterior belief when new evidence arrives.** The prior is what you believed before; the posterior is what you believe after; the evidence is what changed your mind.
- **The three named inputs are prior, likelihood, and evidence.** Prior = P(A). Likelihood = P(B | A). Evidence = P(B). Together they produce the posterior P(A | B).
- **Bayes' theorem is conditional probability reorganised.** It lets you "flip the conditional" — to compute P(cause | effect) when you know P(effect | cause). That flip is the useful move.
- **Bayesian updating is a repeatable process.** Each new piece of evidence turns the current posterior into the next prior. Beliefs accumulate evidence step by step.
- **The prior matters — it is never ignored.** Strong evidence can overcome a weak prior, but the prior is always part of the calculation. Skipping it entirely is a reasoning error that you will study in a later topic.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
