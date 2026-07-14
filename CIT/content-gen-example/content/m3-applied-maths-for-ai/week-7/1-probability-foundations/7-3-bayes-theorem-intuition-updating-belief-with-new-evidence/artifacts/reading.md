<!-- nav:top:start -->
[⬅ Previous: 7.2 — Conditional probability](../../7-2-conditional-probability-p-a-given-b/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 7.4 — Why LLMs output a probability distribution, not a single fixed answer ➡](../../../2-how-llms-use-probability/7-4-why-llms-output-a-probability-distribution-not-a-single-fixe/artifacts/reading.md)
<!-- nav:top:end -->

---

# Bayes' theorem intuition — updating belief with new evidence

## Overview

You already know from topic 7.2 that conditional probability lets you update a probability when you learn something new. Bayes' theorem takes that same idea one step further: it gives you a rule for doing that update when the information you have is "backwards" from what you need. You know how probable the evidence is if the claim is true — but you want to know how probable the claim is now that you have seen the evidence. That flip is what Bayes' theorem is for, and it is one of the most useful tools in both everyday reasoning and modern AI [1].

## Key Concepts

### Prior, posterior, and the belief update

Think of your confidence in any claim as a number between 0 and 1 — a probability. Before you look at any new evidence, that number sits at a starting value. This starting value is called the **prior** — your initial estimate of how likely something is, based on background knowledge or past experience, before any new evidence arrives [1].

For example: you know it rains roughly 3 days out of 10 in your city. Your prior probability of rain today is 0.3.

When you observe something new, your confidence shifts. After you factor the evidence in, the number moves to a new value called the **posterior** — your updated estimate of how likely the claim is, after taking new evidence into account [1][3].

- **Prior** = belief *before* evidence. Example: P(rain) = 0.3.
- **Posterior** = belief *after* evidence. Example: P(rain | dark clouds) = ?

The word "prior" means before; "posterior" means after. Bayes' theorem is the rule that moves you from one to the other.

### Likelihood — the bridge

To move from prior to posterior you need one more piece: how well does the evidence fit with the claim being true?

**Likelihood** — the probability of seeing this evidence assuming the claim is true. Written as P(evidence | claim) [2].

- **Claim:** it is raining.
- **Evidence:** dark clouds outside.
- **Likelihood:** P(dark clouds | rain). If rain almost always comes with dark clouds, this is high — say 0.9.

The likelihood is the bridge. Strong evidence (a high likelihood under the claim) pushes the posterior well above the prior. Weak or ambiguous evidence barely moves it [2][3].

### Bayes' theorem — the named equation

With the three pieces named, here is Bayes' theorem. You are not expected to derive or prove it — just read it as a named relationship:

```
P(A | B)  =  P(B | A) × P(A)
             ─────────────────
                  P(B)
```

Each symbol has a plain-English name:

| Symbol | Name | Plain meaning |
|---|---|---|
| P(A \| B) | **Posterior** | Updated belief in A after seeing B |
| P(B \| A) | **Likelihood** | How probable B is if A were true |
| P(A) | **Prior** | Belief in A before seeing B |
| P(B) | **Evidence** | Overall probability of B, regardless of A |

Why does this look like conditional probability from topic 7.2? Because it is. Recall P(A | B) = P(A and B) / P(B). Bayes' theorem simply rewrites P(A and B) as P(B | A) × P(A). That substitution is the only algebra involved — the result is still a conditional probability, just written in terms you can actually measure [2].

The useful move is the "flip": you start with P(effect | cause) — which is often what you can observe — and arrive at P(cause | effect) — which is what you actually want to know [1][2].

![Bayesian belief updating: prior → observe evidence → Bayes update → posterior → cycle repeats](artifacts/diagram.png)
*The Bayesian update cycle: a prior belief absorbs new evidence through Bayes' theorem to produce a posterior, which becomes the prior for the next round.*

### Bayesian updating — repeating the cycle

The rule stays the same every time. The numbers change as new evidence arrives.

**Bayesian updating** — the process of repeatedly applying Bayes' theorem as evidence accumulates, each time using the previous posterior as the new prior [3].

| What stays the same | What changes each round |
|---|---|
| The formula structure | The prior (it becomes the last posterior) |
| The meaning of prior, likelihood, posterior | The piece of evidence observed |
| The mathematical relationship | The resulting posterior |

Each new piece of evidence turns the current posterior into the next prior. Over many rounds, beliefs converge toward the truth — strong evidence eventually overwhelms even a poor starting guess [1][3].

## Worked Example

Let's trace the rain-and-clouds scenario step by step.

**Setup:**
- P(rain) = 0.3 — it rains about 3 days in 10. This is the **prior**.
- P(dark clouds | rain) = 0.9 — when it rains, dark clouds appear 90% of the time. This is the **likelihood**.
- P(dark clouds | no rain) = 0.2 — clouds sometimes appear even on dry days.

**Question:** You look outside and see dark clouds. What is the updated probability of rain — the **posterior** P(rain | dark clouds)?

**Step 1 — state the prior:**
P(rain) = 0.3. Before looking outside, your best estimate is a 30% chance of rain.

**Step 2 — state the likelihood:**
P(dark clouds | rain) = 0.9. If it were raining, you would see dark clouds 90% of the time.

**Step 3 — compute P(dark clouds) overall:**
You need the overall probability of seeing dark clouds — how often they appear regardless of whether it rains. Sum over both cases:

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

                       =  0.9 × 0.3  /  0.41

                       =  0.27 / 0.41  ≈  0.66
```

**Result:** The posterior is about 0.66. Seeing dark clouds updates your belief in rain from 30% to roughly 66% [1][3].

| Moment | Belief in rain | What happened |
|---|---|---|
| Before looking outside | 0.30 (prior) | Background knowledge only |
| After seeing dark clouds | 0.66 (posterior) | Dark clouds applied as evidence |

The evidence moved the belief upward because dark clouds are a strong signal of rain. If you then heard thunder, you would run the update again — the posterior 0.66 becomes the new prior, and the cycle continues [1].

## In Practice

Bayesian updating appears across medicine, software, and AI wherever a system must reason from evidence to causes.

**Medical testing.** A doctor tests a patient for a condition. Before the test, the doctor has a prior estimate based on the patient's symptoms and demographics — say, 5% chance. The test comes back positive. The likelihood of a positive test given the condition might be 95%. Bayes' theorem gives the posterior: the updated probability the patient actually has the condition. Crucially, this posterior is not automatically high — it depends on how common the condition is. A rare condition with a 5% prior can still yield a surprisingly low posterior even after a positive test, because most positive tests come from the large pool of healthy people [3].

**Spam filters.** An email filter starts with a prior that any incoming message is unwanted. It then observes evidence — specific words, sender patterns, formatting. For each piece of evidence, it assesses a likelihood: "If this message were spam, how probable is this word?" The posterior after all evidence is processed becomes the filter's confidence score. Bayesian spam filtering was one of the first commercially successful applications of this reasoning [2][3].

**LLM (Large Language Model) generation.** When an LLM generates text, it assigns a probability to each possible next word based on all the words that came before. The probabilistic reasoning behind how the model estimates which word fits the context draws on the same underlying principles as Bayes' theorem. You will explore how LLMs use probability distributions in topic 7.4 [1].

One important caution: skipping the prior and relying only on the likelihood is a reasoning error. It leads to over-confidence in results when the claim is rare to begin with. You will study this pattern — called the base rate fallacy — by name in a later topic in this course.

## Key Takeaways

- **Bayes' theorem updates a prior belief into a posterior belief when new evidence arrives.** Prior = before evidence; posterior = after evidence; the evidence shifts the number between them.
- **The three named inputs are prior, likelihood, and overall probability of the evidence.** Prior = P(A). Likelihood = P(B | A). Evidence = P(B). Together they produce the posterior P(A | B).
- **Bayes' theorem is conditional probability reorganised.** It lets you "flip the conditional" — computing P(cause | effect) when you know P(effect | cause). That flip is the useful move [2].
- **Bayesian updating is a repeatable cycle.** Each new piece of evidence turns the current posterior into the next prior. Beliefs accumulate and sharpen as more evidence arrives [3].
- **The prior is never ignored.** Strong evidence can overcome a poor prior, but the prior is always part of the calculation. Omitting it is a reasoning error you will encounter by name later in this course.
- **P(A | B) and P(B | A) are not the same.** Confusing the two is the most common error when reasoning with conditional probabilities — Bayes' theorem exists precisely to navigate that difference [1][2].

## References

1. BetterExplained. "An Intuitive (and Short) Explanation of Bayes' Theorem." <https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/>
2. Piech, C. "Bayes' Theorem." Stanford CS Probability for Computer Scientists. <https://chrispiech.github.io/probabilityForComputerScientists/en/part1/bayes_theorem/>
3. Bhatt, P. "Bayesian Updating Simply Explained." Towards Data Science. <https://towardsdatascience.com/bayesian-updating-simply-explained-c2ed3e563588/>

---
<!-- nav:bottom:start -->
[⬅ Previous: 7.2 — Conditional probability](../../7-2-conditional-probability-p-a-given-b/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 7.4 — Why LLMs output a probability distribution, not a single fixed answer ➡](../../../2-how-llms-use-probability/7-4-why-llms-output-a-probability-distribution-not-a-single-fixe/artifacts/reading.md)
<!-- nav:bottom:end -->
