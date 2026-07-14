<!-- nav:top:start -->
[⬅ Previous: 6.10 — Using the TensorFlow Embedding Projector to explore word clusters](../../../../week-6/4-hands-on-exploration/6-10-using-the-tensorflow-embedding-projector-to-explore-word-clu/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 7.2 — Conditional probability ➡](../../7-2-conditional-probability-p-a-given-b/artifacts/reading.md)
<!-- nav:top:end -->

---

# Probability basics — likelihood, events, outcomes

## Overview

Probability is the branch of mathematics that answers the question "how likely is this?" — and turns that answer into a precise number you can reason with. You already know from topic 1.3 that some systems do not always return the same result, and from topic 1.4 that AI models give different answers to the same prompt. Probability is the mathematical language that explains both of those observations. By the end of this topic you will have the vocabulary and the basic arithmetic to talk about probability confidently — and you will understand the foundation on which every AI text-generation decision rests [1].

## Key Concepts

### What is probability?

**Probability** — a number that says how likely it is that a particular thing will happen. Probability always sits between 0 and 1.

- **0** means the thing is **impossible** — it will never happen.
- **1** means the thing is **certain** — it will always happen.
- Every value in between is a degree of likelihood.

You will also see probability written as a percentage or a fraction. They all mean the same thing:

> 0.25 = 25% = 1/4

The table below maps probability values to plain-English meaning so you can build a gut feel for the numbers [1][2]:

| Probability | Plain meaning | Everyday example |
|---|---|---|
| 0 | Impossible | Rolling a 7 on a six-sided die |
| 0.1 | Unlikely | 1 in 10 chance |
| 0.25 | Below average | 1 in 4 — one card suit from a deck |
| 0.5 | Even chance | A fair coin flip |
| 0.75 | More likely than not | 3 in 4 |
| 0.9 | Very likely | 9 in 10 — still fails once in ten tries |
| 1 | Certain | Rolling a number from 1 to 6 on a fair die |

One critical point: a "90% likely" event still fails 1 in 10 times. Over many events, that adds up. Keep that in mind whenever you read a probability number [1].

### Outcomes and the sample space

Before you can calculate any probability, you need to know the full set of things that *could* happen.

**Outcome** — one specific result of an action. When you toss a coin, "Heads" is one outcome and "Tails" is another. Each outcome is a complete, distinct result.

**Sample space** — the complete list of every possible outcome. No outcome is left out; no outcome appears twice. Why does this matter? Because the sample space is the denominator in every probability calculation — it is "everything that could happen" [2].

| Action | Sample space | Number of outcomes |
|---|---|---|
| Toss one fair coin | {Heads, Tails} | 2 |
| Roll one six-sided die | {1, 2, 3, 4, 5, 6} | 6 |
| Pick a day of the week | {Mon, Tue, Wed, Thu, Fri, Sat, Sun} | 7 |
| Flip two coins | {HH, HT, TH, TT} | 4 |

Notice that flipping two coins gives **four** outcomes, not three. You might think "both heads, one of each, both tails" — but HT and TH are different sequences. Always list every distinct sequence, or your sample space will be incomplete [2].

A common mistake: list an incomplete sample space, then get a probability larger than 1. That is your signal to go back and check step one [3].

### Events — what you are looking for

Once you have the sample space, you name the specific thing you care about.

**Event** — one or more outcomes from the sample space that you are interested in. An event is a **subset** of the sample space.

Examples using a six-sided die:

| Event | Outcomes that satisfy it | Count |
|---|---|---|
| Roll exactly a 3 | {3} | 1 |
| Roll an even number | {2, 4, 6} | 3 |
| Roll greater than 4 | {5, 6} | 2 |
| Roll less than 10 | {1, 2, 3, 4, 5, 6} — all | 6 |
| Roll a 7 | {} — impossible | 0 |

If the event covers the entire sample space, its probability is 1. If the event contains no outcomes, its probability is 0 [1].

### Calculating probability for equally-likely outcomes

When every outcome has the same chance as every other, you can calculate probability with a single division [3]:

```
P(event)  =  (number of outcomes in the event)
              ──────────────────────────────────
              (total outcomes in the sample space)
```

This is sometimes written as: **P(event) = favourable ÷ total**

The word "favourable" just means "the outcomes that count as the event."

This formula only works when every outcome is equally likely — a well-made die, a well-shuffled deck, a random number generator. Real-world situations such as weather or sports often have unequal likelihoods; you will see how probability handles those cases in later topics.

### The sum rule — all probabilities add to 1

Here is a rule that is simple and powerful: if you add up the probabilities of every outcome in the sample space, the total must equal exactly 1.

Why? Because one outcome *must* happen — the experiment always produces a result. That certainty (1) is shared among all outcomes.

- Fair coin: P(H) + P(T) = 0.5 + 0.5 = **1**
- Fair die: 6 × (1/6) = **1**

Use this as a built-in error check. Probabilities that sum to more than 1 mean you double-counted something. Probabilities that sum to less than 1 mean you left an outcome out [1].

### The complement rule

**Complement** — the complement of an event is everything in the sample space that is *not* in the event.

If an event has probability P, its complement has probability **1 − P**.

| Event | P(event) | Complement | P(complement) |
|---|---|---|---|
| Roll a 6 | 1/6 ≈ 0.167 | Roll anything except 6 | 5/6 ≈ 0.833 |
| Pick a weekend day | 2/7 ≈ 0.286 | Pick a weekday | 5/7 ≈ 0.714 |
| Pick a heart from a deck | 1/4 = 0.25 | Pick any non-heart | 3/4 = 0.75 |

The complement is useful when counting "what does not happen" is easier than counting "what does happen." Example: what is the probability that at least one head appears in three coin tosses? The only way to get *no* heads is {TTT}, probability 1/8. So P(at least one head) = 1 − 1/8 = **7/8** [3].

### Probability in AI — naming the connection

You know from topic 1.4 that AI models give different answers to the same prompt. Now you can be precise about why.

When an LLM (Large Language Model — from topic 3.4) generates text, it builds the response one token at a time. A **token** is a chunk of text the model reads and writes — roughly a word or part of a word. At each step, the model assigns a probability to every token that could come next. That is a sample space with tens of thousands of outcomes — and all those probabilities must sum to 1.

The token with probability 0.4 is more likely to be chosen than the token with probability 0.05, but neither is guaranteed. How the model uses those probabilities to make the final choice is covered in later topics this week [1].

## Worked Example

Apply the seven-step counting method to any equally-likely scenario:

**Scenario:** roll one fair six-sided die. What is the probability of rolling a number greater than 4?

1. **Define the experiment.** Roll one fair six-sided die.
2. **List the sample space.** {1, 2, 3, 4, 5, 6} — six outcomes total (N = 6).
3. **Define the event.** Rolling a number greater than 4.
4. **Count the favourable outcomes.** {5, 6} — two outcomes (k = 2).
5. **Divide.** P(greater than 4) = 2 / 6 = 1/3 ≈ **0.33** (about 33%).
6. **Verify the range.** Is 0.33 between 0 and 1? Yes.
7. **Verify the sum.** P(1) + P(2) + P(3) + P(4) + P(5) + P(6) = 6 × (1/6) = 1. Correct.

**Try another:** what is the probability of picking a weekend day at random from a week?

- Sample space: {Mon, Tue, Wed, Thu, Fri, Sat, Sun} — N = 7
- Event: {Sat, Sun} — k = 2
- P(weekend) = 2/7 ≈ **0.286** (about 29%) [2]

Apply these same steps until the process feels automatic. That automaticity carries you through every probability topic that follows [3].

## In Practice

**Weather forecasts.** When a forecast says "40% chance of rain," a meteorologist has assigned probability 0.4 to the event "measurable rain falls here today." A 40% chance is genuinely uncertain — not low, not high. The number 0.4 is expressed exactly the way you practised here [3].

**Quality control.** A factory tests 200 light bulbs and finds 6 defective. P(defective) = 6/200 = 0.03, or 3%. That single number guides decisions about the production line — and whether 3% is acceptable depends entirely on what the bulbs are used for [2].

**Card and board games.** Every card game and dice game is built on probability. A 1-in-4 chance of drawing a heart, a 1-in-6 chance of rolling the number you need — these numbers help players make better decisions and help designers balance difficulty [3].

**AI content generation.** Every time an LLM generates a response, it assigns a probability to each possible next token — a sample space with tens of thousands of entries that all sum to 1. You will meet probability distributions in topic 7.4. How the model uses those probabilities to make the final word choice is covered in later topics this week [1].

**Email triage tools.** Some tools estimate the likelihood that a message is unwanted based on simple counts — how many flagged words appear, or how many similar messages users marked as junk. If the probability score exceeds a threshold, the message is flagged. The core of that decision is exactly the favourable-count-divided-by-total-count formula you have practised [2].

**Do / Don't summary:**

| Do | Don't |
|---|---|
| Write out the sample space before calculating | Skip the sample space step |
| Check that all probabilities sum to 1 | Assume equally likely outcomes without checking |
| Try the complement when counting directly is hard | Confuse "high probability" with "certainty" |
| Use fractions, decimals, or percentages interchangeably | Apply k/N to situations with unequal likelihoods |

## Key Takeaways

- **Probability is a number between 0 and 1.** Zero means impossible; 1 means certain. Percentages and fractions are equivalent ways to say the same thing.
- **The sample space is the complete list of every possible outcome.** It is the denominator for every probability calculation. An incomplete sample space gives wrong answers.
- **An event is a subset of the sample space** — one or more outcomes you care about. A single outcome ("roll a 3") is a valid event; so is a group ("roll an even number").
- **For equally-likely outcomes:** P(event) = outcomes in event ÷ total outcomes. This formula only works when every outcome has the same chance.
- **All outcome probabilities in a sample space must sum to 1.** This is a built-in correctness check.
- **The complement rule:** P(not event) = 1 − P(event). Often the easiest path to a probability is to calculate the complement instead.
- **AI systems assign a probability to every possible next token.** The vocabulary here — outcome, event, sample space, probability — is the language used to describe what an LLM does at every generation step. The specifics of how those probabilities drive output belong to later topics this week.

## References

[1] Seeing Theory — Brown University interactive probability visualizer. https://seeing-theory.brown.edu/basic-probability/index.html

[2] LibreTexts — Basic Probability Concepts. https://math.libretexts.org/Courses/Fullerton_College/Math_100:_Liberal_Arts_Math_(Claassen_and_Ikeda)/06:_Probability/6.01:_Basic_Probability_Concepts

[3] Math is Fun — Probability. https://www.mathsisfun.com/data/probability.html

---
<!-- nav:bottom:start -->
[⬅ Previous: 6.10 — Using the TensorFlow Embedding Projector to explore word clusters](../../../../week-6/4-hands-on-exploration/6-10-using-the-tensorflow-embedding-projector-to-explore-word-clu/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 7.2 — Conditional probability ➡](../../7-2-conditional-probability-p-a-given-b/artifacts/reading.md)
<!-- nav:bottom:end -->
