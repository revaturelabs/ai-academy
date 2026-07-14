<!-- nav:top:start -->
[⬅ Previous: 7.1 — Probability basics](../../7-1-probability-basics-likelihood-events-outcomes/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 7.3 — Bayes' theorem intuition ➡](../../7-3-bayes-theorem-intuition-updating-belief-with-new-evidence/artifacts/reading.md)
<!-- nav:top:end -->

---

# Conditional probability — P(A given B)

## Overview

Imagine you are about to roll a die, and someone tells you the result is already known to be greater than 3. Does that change how you would guess the result? It does — because you have new information, and that information rules out some outcomes. **Conditional probability** is the branch of probability that captures exactly this: how the likelihood of one event changes once you know something else has already happened [1].

This topic builds on the probability basics from 7.1 — sample space, event, outcome, and complement. You will learn the notation P(A | B), the logic of the reduced sample space, and the formula that makes conditional probability calculable even when you cannot list every outcome. By the end, you will be able to apply this reasoning to everyday situations and see why it is the engine behind AI language generation.

## Key Concepts

### What "conditional" means

The word **conditional** in plain English means "on the condition that something is already true." A **conditional probability** is a probability that is calculated only inside a specific, restricted situation — after a piece of information has been given.

Compare these two questions:

| Question | Type |
|---|---|
| "What is the probability it will rain today?" | Unconditional — no extra information |
| "What is the probability it will rain today, given the sky is already dark and cloudy?" | Conditional — a piece of information is already known |

The second question is conditional. The condition — "sky is dark and cloudy" — is already known to be true. You are estimating the probability of rain *inside* that restricted situation [1].

### The notation P(A | B)

Mathematicians write conditional probability like this:

```
P(A | B)
```

Read it aloud as "the probability of A **given** B."

- **A** — the event you want to know the probability of.
- **B** — the condition that has already been established as true.
- **|** — the vertical bar means "given." Everything to the right of the bar is already known.

Examples:

| Notation | Read as |
|---|---|
| P(rain \| dark clouds) | "Probability of rain, given dark clouds" |
| P(late \| traffic jam) | "Probability of being late, given a traffic jam" |

One important point: P(A | B) and P(B | A) are **different questions**. "Probability of rain given clouds" is not the same as "probability of clouds given rain." The order of the two sides of the bar always matters [1][2].

### The reduced sample space

The key insight of conditional probability is what happens to the **sample space** — the complete list of all possible outcomes — when a condition is introduced.

- **Without a condition:** the sample space is the full picture, every possible outcome.
- **With a condition:** you immediately discard every outcome that contradicts the condition. You are left with a smaller, **reduced sample space** containing only the outcomes consistent with what you know [1].

You then ask: within this reduced sample space, how many outcomes also satisfy event A?

The diagram below shows this for a standard six-sided die. The left panel shows the full sample space {1–6}. The right panel shows what happens after condition B ("die > 3") is applied — the space shrinks to {4, 5, 6}.

![Conditional probability: full sample space vs reduced sample space after condition B is applied](artifacts/diagram.png)
*Left: full sample space {1–6}, event A = even numbers {2, 4, 6}. Right: after condition B (die > 3), the reduced space is {4, 5, 6}; event A inside B = {4, 6}, giving P(A|B) = 2/3.*

### The conditional probability formula

The reduced-sample-space method works well when you can list every outcome. When you already have probabilities — rather than raw counts — you use the **conditional probability formula**:

```
P(A | B)  =  P(A and B)
             ───────────
               P(B)
```

Breaking it down:

- **P(A and B)** — the probability that both A and B happen at the same time. This is sometimes called the **joint probability** of A and B — "both things are true at once." You will study joint probability in more depth in later topics; for now, think of it as "the probability of the overlap."
- **P(B)** — the probability of the condition alone.
- The division "rescales" the probabilities so they add up to 1 within the B-only world [1][2].

### P(A) versus P(A | B) — spotting the difference

A common mistake is treating these as the same thing. They almost never are.

| | P(A) | P(A \| B) |
|---|---|---|
| What it is | Probability of A, no extra information | Probability of A once you know B is true |
| Sample space used | Full sample space | Reduced sample space — only outcomes where B holds |

A concrete contrast: across all job applicants, the probability of being hired might be 5%. But the probability of being hired given you passed the technical test might be 60%. The condition completely changes the picture [3].

## Worked Example

**Scenario:** You roll a standard six-sided die. Event A = "the result is an even number." Condition B = "the result is greater than 3."

**Method 1 — Reduced sample space (counting):**

1. **Identify condition B.** The die is greater than 3.
2. **Reduce the sample space.** Discard {1, 2, 3}. Remaining outcomes: {4, 5, 6}.
3. **Find event A within the reduced space.** Even numbers in {4, 5, 6}: {4, 6} — 2 outcomes.
4. **Divide.** P(A | B) = 2 / 3 ≈ 0.67.
5. **Verify.** 0.67 is between 0 and 1. Intuitively, half the numbers above 3 are even, so 2/3 is reasonable.

| Step | Action | Result |
|---|---|---|
| 1. Start | Full sample space | {1, 2, 3, 4, 5, 6} — 6 outcomes |
| 2. Apply condition | Keep only outcomes where die > 3 | {4, 5, 6} — 3 outcomes |
| 3. Find event A | Which remaining outcomes are even? | {4, 6} — 2 outcomes |
| 4. Calculate | 2 ÷ 3 | P(even given >3) = 2/3 ≈ 0.67 |

**Method 2 — The formula (using known probabilities):**

- P(even AND greater than 3) = 2/6 ≈ 0.33 (outcomes that are both even and >3: {4, 6})
- P(greater than 3) = 3/6 = 0.5

```
P(even | greater than 3)  =  P(even AND >3)  =  2/6  =  2  = 0.67
                              ──────────────     ───    ─
                               P(greater than 3)  3/6    3
```

Both methods give the same answer. The formula is more general — use it when you have probabilities but cannot list every outcome [2].

**Compare to unconditional:** Without any condition, P(even) = 3/6 = 0.5. Knowing the die landed above 3 raises the probability of an even result from 0.5 to 0.67. The condition is doing the work.

## In Practice

**Weather forecasting.** Every percentage on a weather app is a conditional probability. The model asks: "Given current cloud cover, pressure, and temperature readings, what is P(rain in the next 6 hours)?" New observations arrive, the condition updates, and the probability updates with it [3].

**Medical diagnosis.** A doctor does not ask P(has condition X) for a random person. The relevant question is P(has condition X | tested positive). The test result is the condition. A positive result raises the conditional probability — but does not always make it certain. Confusing P(disease) with P(disease | positive test) is a real reasoning error with serious consequences [2][3].

**AI language models.** Every word an LLM (Large Language Model) generates is selected based on a conditional probability. The model asks: "Given all the tokens — a **token** is a chunk of text the model processes, roughly a word — in this conversation so far, what is the probability of each possible next token?" The preceding text is the condition. Without it, the model would produce incoherent output. Conditional probability is what makes language generation coherent and context-aware [1][2].

**Spam filtering.** An email filter estimates: "Given that this message contains the word 'urgent' and came from an unknown sender, what is the probability it is unwanted?" The words and sender details form the condition. This is conditional probability reasoning applied at scale [3].

## Key Takeaways

- **Conditional probability measures how likely A is once you know B has already happened.** It is written P(A | B) and read "the probability of A given B." The vertical bar means "given."
- **A condition shrinks the sample space.** When you learn B is true, you discard every outcome inconsistent with B and calculate within that smaller, reduced sample space.
- **The formula is P(A | B) = P(A and B) / P(B).** The numerator is the probability of both events happening together; the denominator rescales everything to the B-only world.
- **P(A) and P(A | B) are not the same.** Unconditional probability uses the full picture; conditional probability uses a restricted picture. The difference can be enormous.
- **P(A | B) and P(B | A) are different questions.** Swapping the sides of the bar changes the meaning completely — a common mistake in medical, legal, and statistical reasoning.
- **Conditional probability underpins AI language generation.** Every next-token choice an LLM makes is a conditional probability conditioned on everything written so far.

## References

1. Yale Statistics 101 — Conditional Probability. <http://www.stat.yale.edu/Courses/1997-98/101/condprob.htm>
2. probabilitycourse.com — Chapter 1.4: Conditional Probability. <https://www.probabilitycourse.com/chapter1/1_4_0_conditional_probability.php>
3. setosa.io — Conditional Probability (interactive visual). <https://setosa.io/ev/conditional-probability/>

---
<!-- nav:bottom:start -->
[⬅ Previous: 7.1 — Probability basics](../../7-1-probability-basics-likelihood-events-outcomes/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 7.3 — Bayes' theorem intuition ➡](../../7-3-bayes-theorem-intuition-updating-belief-with-new-evidence/artifacts/reading.md)
<!-- nav:bottom:end -->
