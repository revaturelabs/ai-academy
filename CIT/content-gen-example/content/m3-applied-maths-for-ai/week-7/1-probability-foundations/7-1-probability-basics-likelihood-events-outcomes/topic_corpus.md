---
topic_id: "7.1"
title: "Probability basics — likelihood, events, outcomes"
position_in_module: 1
generated_at: "2026-06-22T00:00:00Z"
resource_count: 3
---

# 1. Probability basics — likelihood, events, outcomes — Topic Corpus

## 2. Prerequisites

This topic builds lightly on:

- **1.3 Probabilistic systems** — the idea that some systems do not always return the same result. That concept introduced the word "probabilistic" without defining the underlying maths. This topic fills that gap.
- **1.4 Why AI gives different answers to the same question** — the observation that AI outputs vary each time you run the same prompt. This topic gives you the mathematical vocabulary that explains why.
- **3.4 How LLMs work — tokens, training, inference** — the concept of a token (a small chunk of text the model reads and writes) is referenced in section 7 when probability is connected to AI behaviour. No deep knowledge of that topic is needed here.

No arithmetic beyond simple fractions and division is assumed. No prior statistics, probability, or maths course is needed.

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Define probability in plain language and express it as a number between 0 and 1.
- Identify the **sample space**, an **event**, and an **outcome** for a given everyday scenario.
- Distinguish between impossible, unlikely, even-chance, likely, and certain events using probability values on a 0-to-1 scale.
- Calculate the probability of a simple event when all outcomes are equally likely (count of favourable outcomes ÷ count of total outcomes).
- Explain the complement rule — how the probability of an event *not* happening relates to the probability that it does.
- Recognise that AI systems assign a probability to every possible next word, and name this as something you will explore more deeply in later topics.

## 4. Introduction

Think about the last time you checked the weather before leaving home. You did not know for certain whether it would rain. You looked at the sky, maybe checked an app, and made a judgement — "it probably won't rain" or "I should take an umbrella just in case." That judgement is probability thinking.

Probability is the branch of mathematics that takes the question "how likely is this?" and turns it into a precise number. Why does that matter? Because a number can be compared, added, multiplied, and reasoned about in ways that a vague feeling cannot. Engineers use probability numbers to design reliable bridges. Doctors use them to interpret medical tests. Game designers use them to balance difficulty. And AI researchers use them at the very core of how a language model decides what to say next [1].

When a Large Language Model (LLM) — a type of AI system trained on vast amounts of text — generates a sentence, it is not picking words randomly and it is not following a fixed script. At every single step, it computes a probability for each possible next word or token, and then makes a choice based on those numbers. The specific way it uses those probabilities — and how a setting called temperature controls the choice — is a later topic in this week. But you cannot understand any of that without first understanding what a probability is, how it is expressed, and how it relates to outcomes and events [1].

That is what this topic covers. By the end, you will have the vocabulary and the basic arithmetic to talk about probability confidently. Every concept in the rest of this week's session — conditional probability, Bayes' theorem intuition, temperature, mean, median, precision, recall — is built on top of the foundation you will lay here.

## 5. Core Concepts

### 5.1 What is probability?

**Probability** — a number that expresses how likely it is that a particular thing will happen. Probability always sits between 0 and 1, inclusive.

- **0** means the thing is **impossible** — it will never happen under any circumstances.
- **1** means the thing is **certain** — it will always happen without exception.
- Every value in between is a degree of likelihood.

| Probability value | Plain-English meaning | Everyday example |
|---|---|---|
| 0 | Impossible | Rolling a 7 on a standard six-sided die |
| 0.1 | Very unlikely | Drawing the one joker from a 10-card pile |
| 0.25 | Unlikely | Picking the one defective item from a batch of 4 |
| 0.5 | Even chance | A fair coin landing heads |
| 0.75 | Likely | Rain when 3 out of 4 weather models predict it |
| 0.9 | Very likely | A bus arriving within 10 minutes when 9 in 10 do |
| 1 | Certain | Rolling a number between 1 and 6 on a standard die |

You will also see probability written as a **percentage** or as a **fraction**. They all mean the same thing:

- 0.25 = 25% = 1/4

Choose whichever form suits the situation. Fractions make arithmetic easy; percentages communicate quickly to non-specialists [2].

Imagine probability as a position on a straight line. The left end of the line is labelled "impossible" (0). The right end is labelled "certain" (1). The midpoint is "50/50" (0.5). Every event you can think of sits somewhere on that line. The closer it is to the right, the more likely it is. This visual is exactly what you see when you open an interactive probability tool like the one at Brown University's Seeing Theory [1].

### 5.2 Outcomes and the sample space

Before you can calculate a probability, you need to know the full set of things that *could* happen. This set has a name.

**Outcome** — one specific result of an action or experiment. When you toss a coin, "Heads" is one outcome and "Tails" is another outcome. Each outcome is distinct and describes one complete result.

**Sample space** — the complete, exhaustive list of every possible outcome. No outcome is left out. No outcome is listed twice. The sample space covers everything that could happen.

Why is the sample space so important? Because it is the denominator in every probability calculation. You are asking "out of everything that could happen, how often does this particular thing happen?" The sample space is the "everything that could happen" part [2].

Here are some clear examples:

| Action | Sample space | Number of outcomes |
|---|---|---|
| Toss one fair coin | {Heads, Tails} | 2 |
| Roll one standard six-sided die | {1, 2, 3, 4, 5, 6} | 6 |
| Pick a day of the week at random | {Mon, Tue, Wed, Thu, Fri, Sat, Sun} | 7 |
| Flip two coins | {HH, HT, TH, TT} | 4 |
| Pick a letter from {A, B, C} | {A, B, C} | 3 |

Notice that flipping two coins gives four outcomes, not three. You might be tempted to say "both heads, one of each, both tails" — that is only three possibilities if you do not distinguish the order. In probability, the standard approach is to list every distinct sequence, which gives four. Getting the sample space right is the first skill you build [2].

A common mistake is to list an incomplete sample space and then get a probability that is larger than 1. For example, if you roll a die and only write {1, 2, 3} as your sample space, you will calculate P(rolling a 1) = 1/3, which is wrong — it should be 1/6. Always check that your sample space really contains every possible outcome [3].

### 5.3 Events — what you are looking for

Once you have the sample space, you identify the specific thing you are interested in. That is called an event.

**Event** — one or more outcomes from the sample space that you care about. An event is a **subset** of the sample space — it can contain one outcome, several outcomes, or (in extreme cases) all of them or none of them.

Here are some examples using a six-sided die:

| Event | Outcomes that satisfy it | Count |
|---|---|---|
| Roll exactly a 3 | {3} | 1 |
| Roll an even number | {2, 4, 6} | 3 |
| Roll a number greater than 4 | {5, 6} | 2 |
| Roll a number less than 10 | {1, 2, 3, 4, 5, 6} | 6 (all outcomes) |
| Roll a 7 | {} (empty — impossible) | 0 |

The last two rows illustrate the extremes. If the event covers the entire sample space, its probability is 1 (it always happens). If the event contains no outcomes, its probability is 0 (it never happens) [1].

One subtle point: the event "roll an even number" and the event "roll a 2" are different events, even though rolling a 2 *is* rolling an even number. The first event groups three outcomes together; the second isolates one. In everyday speech, people are often loose about this distinction. In probability, the difference matters when you start calculating [2].

### 5.4 Calculating probability for equally-likely outcomes

When every outcome in the sample space has the same chance as every other outcome — meaning the system is fair and unbiased — you can calculate the probability with a simple division [3]:

```
Probability of an event  =  (number of outcomes in the event)
                             ─────────────────────────────────
                             (total number of outcomes in the sample space)
```

This is sometimes written as P(event) = favourable / total, where "favourable" just means "the outcomes that count as the event."

**Worked example 1 — rolling a die:**

- Action: roll one fair six-sided die.
- Sample space: {1, 2, 3, 4, 5, 6} — six equally likely outcomes.
- Event: rolling a number greater than 4.
- Outcomes in the event: {5, 6} — two outcomes.
- P(greater than 4) = 2 / 6 = 1/3 ≈ 0.33 (about 33%).

**Worked example 2 — picking a day of the week:**

- Action: randomly select one day of the week.
- Sample space: {Mon, Tue, Wed, Thu, Fri, Sat, Sun} — seven equally likely outcomes.
- Event: picking a weekend day.
- Outcomes in the event: {Sat, Sun} — two outcomes.
- P(weekend) = 2 / 7 ≈ 0.286 (about 29%).

**Worked example 3 — picking a card:**

- Action: pick one card at random from a standard 52-card deck.
- Sample space: all 52 cards — 52 equally likely outcomes.
- Event: picking a heart.
- Outcomes in the event: 13 cards (all hearts in the deck).
- P(heart) = 13 / 52 = 1/4 = 0.25 (exactly 25%) [2].

The phrase "equally likely" is crucial. This formula only works when no outcome is more likely than any other. A well-made die, a well-shuffled deck, a random number generator — these qualify. Real-world scenarios — weather, sports outcomes, AI responses — often do not have equally likely outcomes. You will see how probability is handled in those situations in later topics in this module [3].

### 5.5 The sum rule — all probabilities add up to 1

Here is a fact that is both simple and powerful: if you assign a probability to every outcome in the sample space and add those probabilities up, the total must always equal exactly 1.

Why? Because one of the outcomes in the sample space *must* happen — the experiment always produces a result. So the total likelihood of "something happens" is 1 (certain). That total is shared among all the outcomes.

- Fair coin: P(Heads) + P(Tails) = 0.5 + 0.5 = 1.
- Fair die: P(1) + P(2) + P(3) + P(4) + P(5) + P(6) = 6 × (1/6) = 1.
- Three equally likely letters {A, B, C}: P(A) + P(B) + P(C) = 1/3 + 1/3 + 1/3 = 1.

Use this as a built-in error check. If your probabilities sum to more than 1, you have double-counted something. If they sum to less than 1, you have left out an outcome. Either way, something in your sample space is wrong [1].

This rule also means that the probability of an event and its complement always sum to 1 — which leads directly to the next concept.

### 5.6 The complement of an event

**Complement** — the complement of an event is everything in the sample space that is *not* in the event.

If an event has probability P, then its complement has probability 1 − P.

| Event | P(event) | Complement | P(complement) |
|---|---|---|---|
| Roll a 6 on a fair die | 1/6 ≈ 0.167 | Roll anything other than 6 | 5/6 ≈ 0.833 |
| Pick a weekend day | 2/7 ≈ 0.286 | Pick a weekday | 5/7 ≈ 0.714 |
| Pick a heart from a deck | 1/4 = 0.25 | Pick any non-heart | 3/4 = 0.75 |

The complement rule is useful whenever it is easier to count "what does not happen" than "what does happen." For example: what is the probability that at least one head appears when you toss a coin three times? Counting all the outcomes with at least one head is tedious. But the complement is simple — the only way to get no heads is {TTT}, probability 1/8. So the probability of at least one head = 1 − 1/8 = 7/8 [3].

You will use the complement frequently in later topics, especially when working with conditional probability and AI reliability metrics (which belong to later topics in this week).

### 5.7 Reading probability values — developing intuition

One skill that takes a little practice is developing a gut feel for what a probability number actually means in context. Here is a reference table to build that intuition:

| Probability | Words | Practical feel |
|---|---|---|
| 0.01 or less | Almost impossible | Less than 1 in 100 — a rare edge case |
| 0.05 | Very unlikely | 1 in 20 — worth planning for in critical systems |
| 0.1 | Unlikely | 1 in 10 — happens regularly over many trials |
| 0.25 | Below average chance | 1 in 4 — the chance of picking one card suit |
| 0.5 | Even chance | 1 in 2 — a coin flip |
| 0.75 | Better than average | 3 in 4 — more often than not |
| 0.9 | Very likely | 9 in 10 — expect it most of the time |
| 0.99 or above | Almost certain | Rare to see a failure, but failures do occur |

Notice that "90% likely" (0.9) still fails 1 in 10 times. Over hundreds of events, that adds up. An AI model that gives a correct answer 90% of the time is wrong about 10% of the time — which might be acceptable in casual use but unacceptable in a medical context. Reading probability values critically is a skill you will use throughout this module [1][2].

### 5.8 Probability in AI — naming the connection

You encountered the observation in topic 1.4 that AI models give different answers to the same question. Now you can be more precise about why.

When an LLM generates text, it builds the response one token at a time. At each step, it assigns a probability to every token that could come next — and that is a sample space with tens of thousands of outcomes. The model then picks one based on those probabilities. The token with probability 0.4 is more likely to be chosen than the one with probability 0.05, but neither is guaranteed.

How the model uses those probabilities when making the final choice — whether it always picks the most likely token or sometimes picks a less likely one — is controlled by a setting called temperature. Temperature is a later topic in this week. For now, just note that probability is the foundation: every AI text generation decision is a probability calculation over an enormous sample space [1].

## 6. Implementation

There is no code to write at this stage. But the counting method from section 5.4 can be applied to any equally-likely situation in a consistent set of steps:

1. **Define the experiment.** What action are you performing? (Toss a coin, roll a die, pick a card, select a day.)
2. **List the sample space.** Write down every possible outcome. Count them — call this number N.
3. **Define your event.** What outcome or set of outcomes counts as "the event you care about"?
4. **Count the favourable outcomes.** How many outcomes in the sample space satisfy your event? Call this number k.
5. **Divide.** P(event) = k / N.
6. **Verify the range.** Is your answer between 0 and 1? If not, you made an arithmetic error.
7. **Verify the sum.** Do all outcome probabilities for the full sample space add to 1? If not, revisit step 2.

Apply this process to two or three examples until it feels mechanical. That automaticity will serve you in every probability topic that follows [3].

## 7. Real-World Patterns

**Weather forecasts.** When a forecast says "40% chance of rain," a meteorologist has assigned probability 0.4 to the event "measurable rain falls at this location today." The sample space is not simply {rain, no rain}; modern forecasts use many continuous variables. But the way the number 0.4 is communicated — as a probability between 0 and 1 — is exactly the language you have learned here. A 40% chance is not a low chance and not a high chance; it is genuinely uncertain [3].

**Quality control in manufacturing.** A factory produces light bulbs. A sample of 200 bulbs is tested and 6 are found defective. The estimated probability of a randomly selected bulb being defective is 6/200 = 0.03, or 3%. This single number guides decisions about the production line. Is 3% acceptable? It depends on the application — a 3% failure rate in a consumer bulb may be acceptable; in a medical device, it would not be. Probability gives managers a precise number to debate [2].

**Card games and board games.** Every card game, dice game, and board game is built on probability. Knowing that you have a 1 in 4 chance of drawing a heart, or a 1 in 6 chance of rolling the exact number you need, helps players make better decisions. Game designers use these numbers to balance difficulty and ensure the game is neither trivially easy nor frustratingly impossible [3].

**AI content generation.** Every time an LLM generates a response, it assigns a probability to each possible next token — a sample space with tens of thousands of entries that all sum to 1. You will meet probability distributions, which describe how those probabilities are spread across the full sample space, in topic 7.4. How the model uses those probabilities to make the final word choice is covered in later topics this week [1].

**Email triage tools.** Some email tools estimate the likelihood that a message is unwanted based on simple counts — for example, how many flagged words appear, or how many of 20 similar messages were marked as junk by users. If that count-based likelihood score exceeds a threshold, the message is flagged. The core of that decision is a plain probability number of the kind you have practised in this topic: favourable count divided by total count. How a system combines evidence from multiple features at once is a technique you will encounter in a later topic [2].

## 8. Best Practices

**Do:**

- Always write out the sample space before calculating. Skipping this step is the most common source of errors in probability problems.
- Check that your probabilities sum to 1 across all outcomes — treat this as a mandatory self-check, not an optional step.
- Use fractions, decimals, and percentages interchangeably based on what communicates clearly; just stay consistent within a single calculation.
- When a problem feels hard, check the complement first — it is often easier to count what does *not* happen.
- Develop a feel for what probability numbers mean in context. "Very likely" is not the same as "certain." 0.9 fails 10% of the time.

**Don't:**

- Assume all outcomes are equally likely without checking. A coin is equally likely; a biased die is not; a sports match is definitely not.
- Confuse "high probability" with "certainty." Even a 99% probability means the event sometimes does not happen.
- List an incomplete sample space. Missing outcomes inflate your calculated probabilities above their true values.
- Mix up the *event* and the *outcome*. An outcome is one specific result; an event is the set of outcomes you care about — it can be larger than one.
- Apply the counting formula (k/N) to situations with unequal likelihoods without adjustment. The formula only works when the sample space is uniform.

## 9. Hands-On Exercise

You will need: one standard six-sided die (or a virtual one — search "roll a die" in any browser).

**Part A — build the sample space:**
1. Write out the full sample space for one roll.
2. Confirm it has 6 outcomes and that each has probability 1/6.
3. Add all six probabilities and confirm the total is 1.

**Part B — calculate events:**

For each event below, list the outcomes that satisfy it, count them, and calculate the probability:
- Rolling an odd number.
- Rolling a number less than 3.
- Rolling a number that is a multiple of 3.
- Rolling a number that is neither 1 nor 6.

**Part C — use the complement:**

Pick one of your events from Part B. Calculate its probability directly. Then calculate the probability of its complement. Confirm they sum to 1.

**Part D — reflect:**

Which of these events surprised you? Was any probability higher or lower than your intuition suggested? Write one sentence explaining why your intuition was off (or on target).

## 10. Key Takeaways

- **Probability is a number between 0 and 1.** Zero means impossible; 1 means certain; values in between express degrees of likelihood. Percentages and fractions are equivalent ways to express the same thing.
- **The sample space is the complete list of every possible outcome.** It is the denominator for every probability calculation. An incomplete sample space gives wrong answers.
- **An event is a subset of the sample space** — one or more outcomes that you care about. A single outcome ("roll a 3") is a valid event; so is a larger group ("roll an even number").
- **For equally-likely outcomes:** P(event) = (outcomes in event) ÷ (total outcomes in sample space). This formula only works when every outcome has the same chance.
- **All outcome probabilities in a sample space must sum to 1.** This is a built-in correctness check; if your numbers do not sum to 1, revisit your sample space.
- **The complement rule:** P(not event) = 1 − P(event). Often the easiest path to a probability is to calculate the complement instead.
- **AI systems assign a probability to every possible next word.** The vocabulary in this topic — outcome, event, sample space, probability — is the language used to describe what a language model is doing at every generation step. The specifics of how those probabilities drive output belong to later topics in this week.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
