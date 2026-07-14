---
topic_id: "7.2"
title: "Conditional probability — P(A given B)"
position_in_module: 2
generated_at: "2026-06-22T00:00:00Z"
resource_count: 3
---

# 1. Conditional probability — P(A given B) — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **7.1 Probability basics — likelihood, events, outcomes** — the concepts of probability (a number between 0 and 1), sample space (the complete list of all possible outcomes), event (a subset of the sample space), and complement (everything in the sample space that is not in the event) are all used here. Review topic 7.1 before continuing if any of those terms are unfamiliar.

No other formal prerequisites. No arithmetic beyond simple fractions and division is assumed.

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Explain in plain language what conditional probability means — why knowing that one thing has already happened changes the likelihood of something else.
- Identify the "reduced sample space" when a condition is given, and use it to calculate a conditional probability.
- Apply the conditional probability formula P(A|B) = P(A and B) / P(B) to a simple worked example.
- Distinguish between P(A) — the probability of A on its own — and P(A|B) — the probability of A once you know B has occurred.
- Give one real-world example of conditional probability in everyday life and one in an AI context.

## 4. Introduction

Imagine you have just looked out the window and noticed that the sky is dark and full of heavy clouds. Does that change how likely you think rain is compared to when you had not looked out the window yet?

Of course it does. Dark clouds are evidence. They narrow down what is going on. Before you looked, the probability of rain was just "the usual chance of rain on a day like today." After you looked and saw those clouds, the probability is higher — because you have new information that rules out many of the "no rain" scenarios. That shift — updating how likely an event is once you have learned something new — is exactly what conditional probability captures [1].

Conditional probability sounds technical, but the idea behind it is something you do every day. When you see someone running for a bus, you think "they probably caught it" — because you know they were running. You do not think "there is a 50/50 chance they caught it" based on nothing. You already know something about the situation. That knowledge changes your estimate [3].

This topic teaches you to make that everyday reasoning precise. You will learn the notation, the logic, and the arithmetic behind conditional probability. You will also see why this concept sits at the heart of how AI systems reason — including why an AI's confidence in its next word changes depending on the words that came before it. Bayes' theorem — a powerful rule that builds on conditional probability — is the next topic (7.3). Mastering this topic is the prerequisite for that one [2].

## 5. Core Concepts

### 5.1 What "conditional" means

The word **conditional** in mathematics means exactly what it means in plain English: "on the condition that something is true." A **conditional probability** is a probability that applies only in a specific situation — after a piece of information has been given.

Compare these two questions:

| Question | What it asks |
|---|---|
| "What is the probability it will rain today?" | Unconditional — no extra information |
| "What is the probability it will rain today, given that the sky is already dark and cloudy?" | Conditional — you know something about the current situation |

The second question is conditional. The condition is "the sky is dark and cloudy." That condition is already known to be true. Your job is to estimate the probability of rain inside that restricted situation [1].

The condition does not have to involve a sequence of events. It simply means: "assume this piece of information is already established." Before you calculate anything, you ask: "given what I already know, what is the new, narrower situation I am working in?" [3]

### 5.2 The notation P(A | B)

Mathematicians write conditional probability with a vertical bar that reads as "given":

```
P(A | B)
```

This is read aloud as "the probability of A **given** B."

- **A** is the event you are asking about — the thing you want to know the probability of.
- **B** is the condition — the information that has already been established.
- The vertical bar **|** separates them. Everything to the right of the bar is already known to be true.

Examples of reading the notation:

| Notation | Read as |
|---|---|
| P(rain \| dark clouds) | "The probability of rain, given that there are dark clouds" |
| P(late \| traffic jam) | "The probability of being late, given that there is a traffic jam" |
| P(heads \| fair coin) | "The probability of heads, given that the coin is fair" |

The order matters. P(A | B) and P(B | A) are different things. "The probability it rains given dark clouds" is not the same as "the probability of dark clouds given that it is raining." Both are conditional probabilities; they just ask different questions [1][2].

### 5.3 Why a condition changes probability — the reduced sample space

The key to understanding conditional probability is understanding what happens to the **sample space** (from topic 7.1) when a condition is introduced.

**Without any condition:** The sample space includes every possible outcome — the full picture.

**With a condition:** You immediately discard every outcome that contradicts the condition. The condition tells you certain outcomes did not happen. You are left with a smaller, reduced sample space that contains only the outcomes consistent with what you know [1].

Then, within that reduced sample space, you ask: how many of the remaining outcomes also satisfy event A?

Here is a concrete example. You roll a standard six-sided die. The full sample space is {1, 2, 3, 4, 5, 6}.

- **P(even number)** — no condition. Even numbers in the full sample space: {2, 4, 6}. P(even) = 3/6 = 0.5.

Now add a condition: you are told the roll was **greater than 3**.

- **P(even | greater than 3)** — the condition "greater than 3" reduces the sample space to {4, 5, 6}. Within that reduced sample space, even numbers are {4, 6}. P(even | greater than 3) = 2/3 ≈ 0.67.

The same event (rolling an even number) has a different probability once you know the die landed above 3. The condition eliminated {1, 2, 3} from consideration. That is the entire logic of conditional probability [1][3].

| Step | Action | Result |
|---|---|---|
| 1. Start | Full sample space | {1, 2, 3, 4, 5, 6} — 6 outcomes |
| 2. Apply condition | Keep only outcomes where die > 3 | {4, 5, 6} — 3 outcomes |
| 3. Find the event | Which of the remaining outcomes are even? | {4, 6} — 2 outcomes |
| 4. Calculate | 2 divided by 3 | P(even given >3) = 2/3 ≈ 0.67 |

### 5.4 The conditional probability formula

The reduced-sample-space approach works well when you can list every outcome. But sometimes the sample space has too many outcomes to list — or you already know probabilities rather than raw counts. In those cases, you use the **conditional probability formula**.

Here it is:

```
P(A | B)  =  P(A and B)
             ───────────
               P(B)
```

Let's unpack each piece:

- **P(A and B)** — the probability that both A and B happen at the same time. This is sometimes called the **joint probability** of A and B. Think of it as "the probability of the overlap between A and B." You will study joint probability in more depth in later topics; for now, the phrase means "both things are true at once."
- **P(B)** — the probability that the condition B is true on its own.
- **P(A | B)** — the result: the probability of A, once you have restricted the world to cases where B is true [2].

Why does dividing by P(B) make sense? Because you are zooming in on the portion of the sample space where B occurred. Dividing by P(B) "rescales" the probabilities so they add up to 1 within the B-only world [1][2].

**Worked example — the die, using the formula:**

Return to the die example. Use these known probabilities:
- P(even number) = 3/6 = 0.5
- P(greater than 3) = 3/6 = 0.5
- P(even AND greater than 3) = 2/6 ≈ 0.33 (outcomes that are both even and >3: {4, 6})

Applying the formula:

```
P(even | greater than 3)  =  P(even AND greater than 3)  =  2/6  =  2/3 ≈ 0.67
                              ────────────────────────────   ───
                                   P(greater than 3)         3/6
```

This matches the result from the reduced-sample-space method — as it should. Both methods give the same answer; the formula is just more general [2].

**Second worked example — weather:**

Imagine a dataset of 100 days:
- 30 days had dark clouds.
- Of those 30 cloudy days, it rained on 24 of them.

What is P(rain | dark clouds)?

- P(dark clouds) = 30/100 = 0.30
- P(rain AND dark clouds) = 24/100 = 0.24

```
P(rain | dark clouds)  =  0.24 / 0.30  =  0.80
```

Given dark clouds, the probability of rain is 0.80 (80%). In the full 100-day dataset, rain might have occurred on only 35 of those 100 days, giving P(rain) = 0.35. The condition "dark clouds" raises the probability from 0.35 to 0.80. That is conditional probability at work [1][3].

### 5.5 P(A) versus P(A | B) — spotting the difference

A common confusion is treating P(A) and P(A | B) as the same thing. They are almost never the same, and conflating them leads to serious reasoning errors.

| | P(A) | P(A \| B) |
|---|---|---|
| What it is | Probability of A with no extra information | Probability of A once you know B is true |
| Sample space | Full sample space | Reduced sample space — only outcomes where B holds |
| Changes when you learn B? | Ignored — uses the full picture | Yes — defined relative to B |

The difference matters in everyday decision-making:

- **Job application:** "What is the probability of being hired?" might be 5% across all applicants. But "What is the probability of being hired, given you passed the technical test?" might be 60%. The condition radically changes the picture [3].
- **Medical test:** "What is the probability this person has the disease?" might be 1% in the general population. But "What is the probability this person has the disease, given the test came back positive?" might be 90%. Confusing these two is a real error — you will study it in later topics.

### 5.6 An everyday anchor — P(rain | dark clouds)

The narrative seed for this week uses one specific example: **P(rain | dark clouds)**. It is worth unpacking it fully because it is the kind of conditional probability that appears constantly in AI systems.

Think about a weather app. It does not just say "there is a 30% chance of rain today, forever, regardless of what you see outside." It takes in current conditions — temperature, pressure, cloud cover — and gives you a probability conditional on those observations. Every time new information arrives, the sample space is updated. Old outcomes that are no longer consistent are discarded [3].

This is also exactly how an AI language model works when generating text. At every step, it asks: "Given the words I have already written, what is the probability of each possible next word?" The words already written are the condition. They narrow the sample space of plausible next words from tens of thousands down to a smaller, more relevant set. The probability of the word "umbrella" is much higher after "it might rain, so grab your" than after "the recipe says to add" [1][2].

Conditional probability is not just a maths concept. It is the operating principle of any reasoning system — human or artificial — that updates its beliefs as new information arrives.

## 6. Implementation

There is no code at this stage. But the logic of conditional probability follows a consistent set of steps you can apply to any problem.

**Step-by-step procedure — counting method (when outcomes can be listed):**

1. **Identify the condition B.** What information is already known to be true? Write it down explicitly.
2. **Reduce the sample space.** Discard every outcome inconsistent with B. You are left with only outcomes where B is true.
3. **Count the event within the reduced space.** How many of the remaining outcomes satisfy A?
4. **Divide.** P(A | B) = count of A-outcomes in reduced space / total outcomes in reduced space.
5. **Verify.** Is the result between 0 and 1? Does the direction make intuitive sense?

**Step-by-step procedure — formula method (when you have probabilities, not raw counts):**

1. **Identify P(B).** What is the probability of the condition alone?
2. **Identify P(A and B).** What is the probability of both A and B occurring together?
3. **Divide.** P(A | B) = P(A and B) / P(B).
4. **Verify.** Same checks as above.

**Practice example — cards:**

A standard deck has 52 cards. You pick one at random, but before looking a friend tells you it is a face card (Jack, Queen, or King). There are 12 face cards in a standard deck.

- Reduced sample space: 12 face cards.
- Event A: the card is a King. There are 4 Kings.
- P(King | face card) = 4 / 12 = 1/3 ≈ 0.33.

Without the condition, P(King) = 4/52 ≈ 0.077. Knowing the card is a face card more than quadruples the probability of it being a King. The condition is doing all the work [1][2].

## 7. Real-World Patterns

**Weather forecasting.** Modern weather models produce conditional probabilities: "Given current atmospheric pressure, cloud cover, and humidity readings, what is P(rain in the next 6 hours)?" Every percentage you see on a weather app is a conditional probability, conditioned on measurements taken at a specific time [3].

**Medical diagnosis.** The relevant probability is not P(has condition X) for a random person. It is P(has condition X | tested positive). The test result is the condition. Understanding this distinction is why doctors order follow-up tests: a positive result raises the conditional probability but does not always make it certain [2][3].

**Search engines and recommendations.** When you type a query, a search engine ranks results using conditional probability thinking: "Given this query, what is the probability this page is what the user wants?" The same web page has a different relevance probability depending on what you typed [3].

**AI language models.** Every token an LLM generates is chosen based on a conditional probability. The model asks: "Given all the tokens in this conversation so far, what is the probability of each possible next token?" Without that condition — if the model chose words with no context — output would be incoherent. Conditional probability is what makes language generation make sense [1][2].

**Spam filtering.** An email filter estimates: "Given that this message contains these specific words and came from this sender, what is the probability it is unwanted?" The words and sender details are the condition. This type of filtering relies directly on conditional probability reasoning [3].

## 8. Best Practices

**Do:**

- Always name the condition B explicitly before calculating. Leaving B implicit is the most common source of errors — you lose track of which sample space you are working in.
- Double-check whether the question is asking for P(A) or P(A | B). In real-world problems, the condition is often buried in the phrasing. Phrases like "given that," "assuming," "knowing that," and "having seen" all signal a conditional probability.
- Use the reduced-sample-space method when you can list all outcomes — it is the easiest to verify by inspection.
- Use the formula P(A | B) = P(A and B) / P(B) when working with overall probabilities rather than raw counts.
- After calculating, sanity-check the direction: does the condition make A more likely or less likely? Does your answer reflect that?

**Don't:**

- Confuse P(A | B) with P(B | A). "The probability of rain given clouds" is not the same as "the probability of clouds given rain." They are both valid conditional probabilities, but they answer entirely different questions.
- Assume that conditioning on B always raises P(A). A condition can also lower a probability. If you know the die landed on an odd number, the probability of rolling a 6 drops to zero.
- Forget to check that P(B) is not zero before dividing. If the condition B is impossible — its probability is zero — the conditional probability P(A | B) is undefined. You cannot condition on something that can never happen [2].
- Treat P(A | B) as the same thing as P(A). They almost never are. The whole point of conditional probability is that new information changes things.

## 9. Hands-On Exercise

You need: a standard deck of playing cards (or a virtual one — search "virtual card deck" in any browser).

**Part A — reduced sample space practice:**

1. Shuffle the deck. Draw one card face-down.
2. A friend peeks and tells you: "The card is red."
3. List the reduced sample space (all red cards). How many outcomes are there?
4. Within that reduced sample space, calculate the probability the card is a Heart.
5. Compare to P(Heart) with no condition. Is it higher, lower, or the same? Why?

**Part B — formula practice:**

Use the following facts about a dataset of 200 emails:
- 60 emails contained the word "urgent" in the subject line.
- 45 of those 60 "urgent" emails turned out to be unwanted.

Calculate P(unwanted | contains "urgent") using the formula. Show each step.

**Part C — reflect:**

Write two sentences: (1) state what the condition changed in Part A, and (2) explain in plain English why a spam filter would care about the result from Part B.

## 10. Key Takeaways

- **Conditional probability measures how likely A is once you know B has already happened.** It is written P(A | B) and read "the probability of A given B." The vertical bar means "given."
- **A condition shrinks the sample space.** When you learn B is true, you discard every outcome inconsistent with B. You then calculate within that smaller, reduced sample space.
- **The formula is P(A | B) = P(A and B) / P(B).** The numerator is the probability of both events happening together; the denominator rescales everything to the B-only world.
- **P(A) and P(A | B) are not the same.** Unconditional probability uses the full picture; conditional probability uses a restricted picture. The difference can be enormous.
- **P(A | B) and P(B | A) are different questions.** Swapping the two sides of the bar changes the meaning completely — a mistake that causes real errors in medical, legal, and statistical reasoning.
- **Conditional probability underpins AI language generation.** Every next-token choice an LLM makes is a conditional probability over tens of thousands of possible tokens, conditioned on everything written so far.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
