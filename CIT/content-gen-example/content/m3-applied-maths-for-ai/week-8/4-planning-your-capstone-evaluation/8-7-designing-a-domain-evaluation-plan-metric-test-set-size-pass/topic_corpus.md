---
topic_id: 8.7
title: Designing a domain evaluation plan — metric, test set size, pass/fail threshold
position_in_module: 1
generated_at: 2026-06-22T08:05:00Z
resource_count: 3
---

# 1. Designing a Domain Evaluation Plan — Metric, Test Set Size, Pass/Fail Threshold — Topic Corpus

## 2. Prerequisites

This is the capstone synthesis topic for the week. It does not teach new measures — it teaches you how to **choose** among the ones you already know and write them into a plan. You should already have these earlier topics in hand:

- **8.3 — Precision vs recall trade-off.** Precision, recall, false positives, false negatives, and the idea that the *cost of a mistake* decides which one you care about.
- **8.4 — F1 score.** A single balanced number that combines precision and recall.
- **8.5 — Accuracy and the confusion matrix.** Accuracy, the 2x2 grid of true/false positives and negatives, and when accuracy is misleading.
- **8.6 — Calibration.** Whether a model's stated confidence matches its real accuracy.
- **8.1 / 8.2 — Embeddings and cosine similarity.** Used here only as an example of a *similarity-based* task you might be evaluating.

If any of those four metrics still feel fuzzy, revisit that topic first — this topic assumes you can already explain each one in a sentence.

## 3. Learning Objectives

After this topic you should be able to:

- **Choose** an evaluation metric for your own system by matching it to the cost of errors in your domain.
- **Justify** that choice in one plain sentence (why this metric and not the others you know).
- **Decide** how many labeled test examples you need so the score is trustworthy, not noise.
- **Set** a pass/fail threshold *in advance* — the score that means "good enough to ship."
- **Assemble** these three decisions into a one-page evaluation plan for your Capstone system.

## 4. Introduction

Imagine you have built something — a tool that sorts support tickets, a question-answering helper for one company's documents, a filter that flags risky messages. It seems to work when you try it. But "seems to work" is not an answer you can defend. How do you *prove* it is good enough to put in front of real users?

That is what an **evaluation plan** is for. It is a short, written decision made *before* you judge your system, so you cannot fool yourself afterward. A good plan answers three questions: **What will I measure? On how many examples? And what score counts as a pass?** [2]

You already met the measuring tools across this week — precision, recall, F1, accuracy, calibration. This topic is the part where you stop learning new tools and start *choosing* the right ones for your own project. The skill here is judgment, not arithmetic. There is no new formula to memorize. [1]

## 5. Core Concepts

An evaluation plan rests on three decisions. We take them one at a time, then put them together. Think of them as a short pipeline: **pick the metric → size the test set → set the threshold**, and the plan tells you the pass-or-fail verdict at the end.

### 5.1 What an evaluation plan is

**Evaluation plan** — a short, written description of how you will judge whether your system is good enough, decided in advance. It names the measure, the test data, and the bar to clear. [2]

Why write it down in advance? Because if you wait until after you see the results, it is too easy to move the goalposts — to say "well, 70% is fine actually" only because that is the number you happened to get. Deciding first keeps you honest. [3] A plan you can put on one page is the goal; a plan that needs ten pages is usually a sign the task has not been pinned down.

### 5.2 Decision 1 — Metric choice

A **metric** is the single measure you use to score your system. The whole game is: **match the metric to what a mistake actually costs in your domain.** You already know the candidates, so this is a matching exercise, not new learning.

Here is how to choose among the measures you have:

| If your situation is... | Reach for... | Because... |
|---|---|---|
| Missing a real case is expensive (a missed fraud, a missed disease flag) | **Recall** (from 8.3) | Recall punishes false negatives — the cases you let slip through. |
| A false alarm is expensive (wrongly blocking a good user) | **Precision** (from 8.3) | Precision punishes false positives — the wrong alarms. |
| Both kinds of mistake hurt and you want one number | **F1** (from 8.4) | F1 balances precision and recall and stays low if either is bad. |
| Your classes are roughly balanced and all mistakes cost about the same | **Accuracy** (from 8.5) | Accuracy is the simplest fair summary only when classes are even. |
| You will *show users a confidence score* and want them to trust it | Also check **calibration** (from 8.6) | A confident-but-wrong model is dangerous even if accuracy looks fine. |

Two warnings carried over from the week:

- **Accuracy can lie when classes are imbalanced.** If 99 of every 100 emails are not spam, a model that says "never spam" scores 99% accuracy and catches zero spam. That is why you learned precision, recall, and F1 in the first place. [1]
- **Calibration is a second question, not a replacement.** A model can be accurate but overconfident. If your system *displays* a confidence number that a person will act on, add a calibration check alongside your main metric. [1]

The point of having choices is that **different domains care about different mistakes.** Choosing well means you can finish the sentence: *"I will use ___ because in my domain a ___ mistake is the costly one."*

### 5.3 Decision 2 — Test set size

A **test set** is a collection of labeled examples — inputs where you already know the right answer — that you run your system against to compute the metric. **Labeled** just means a human has written down the correct answer for each one.

The decision here is: **how many examples do you need before the score is trustworthy?**

The intuition is simple. A metric computed on 5 examples is almost meaningless — one lucky or unlucky case swings it wildly. If you test on 5 tickets and get 4 right, your accuracy is 80%; get one more right or wrong, and it jumps to 100% or 60%. The number is **noise**. The more examples you test on, the more one or two odd cases stop mattering, and the steadier and more trustworthy the score becomes. [2]

A practical way to size it without any formula: **pick enough examples that one or two individual cases cannot swing the result.** A few dozen is far better than a handful; a couple hundred is steadier still. For a beginner Capstone, a test set of roughly 30–100 carefully labeled examples is a reasonable starting point — enough to be meaningful, small enough to label by hand.

Two qualities matter as much as the count:

- **Held-out** — the test examples must be ones your system has never been tuned on. Testing on examples you already adjusted the system to handle is like grading your own homework with the answer key open. [2]
- **Representative** — the test examples should look like the real inputs your system will face. If real users ask messy, varied questions, a test set of only tidy textbook questions will give a falsely rosy score. [1][2]

> The deeper question of *exactly* how big a test set must be — using confidence intervals or other statistical reasoning, and the formal practice of splitting data into separate training, validation, and test portions — belongs to a later, more advanced treatment. For your Capstone plan, the intuition above ("enough that a stray case won't swing it, held-out, representative") is what you need.

### 5.4 Decision 3 — Pass/fail threshold

A **pass/fail threshold** is the score you decide *in advance* counts as "good enough to ship." Above it, the system passes; below it, it fails and goes back for more work. [3]

The key word is *in advance*. Set the bar before you see the result, so the result cannot quietly lower the bar for you. [3]

How high should the bar be? **Tie it to the stakes of the task.** [3]

| Stakes of the task | Threshold attitude | Example |
|---|---|---|
| Low — a wrong answer is a minor annoyance | A modest bar can be fine | A movie-suggestion helper; 80% might ship |
| High — a wrong answer causes real harm or cost | The bar must be strict | A tool flagging unsafe content; you might demand 95%+ recall |

There is no universal "good" number. A threshold is a *decision about acceptable risk*, written as a score on the metric you chose. Sometimes you set more than one bar — for example, "recall must be at least 0.90 **and** precision at least 0.70" — when the task genuinely has two costs you cannot ignore.

> Setting a threshold *rigorously* — with Z-scores or confidence intervals to account for test-set randomness — and validating it with K-fold cross-validation are more advanced techniques you will meet later. For this planning topic, a threshold is a stake-based judgment call you write down and defend in one sentence.

### 5.5 Putting the three together

A finished plan is just the three decisions in order, each with a one-line reason:

1. **Metric:** I will measure with **___**, because in my domain a **___** mistake is the costly one.
2. **Test set:** I will test on about **___** labeled, held-out, representative examples, because that is enough that no single case swings the score.
3. **Threshold:** I will count **___** as a pass, because the stakes of this task are **___**.

That is the whole one page. The verdict — ship or rework — falls straight out of comparing the measured score to the threshold.

## 6. Implementation

A step-by-step way to write your own plan:

1. **Name the task in one sentence.** "My system sorts incoming support tickets into 'billing', 'technical', or 'other'." Be concrete about the input and the output.
2. **Name the costly mistake.** Ask: when this system is wrong, which kind of wrong hurts most — a miss (false negative) or a false alarm (false positive), or both equally? This single question drives the metric.
3. **Pick the metric** from the table in 5.2 that matches that costly mistake. Add a calibration check only if you will surface confidence scores to users.
4. **Size the test set.** Decide a number of labeled examples large enough that one stray case won't move the result, and confirm they are held-out and representative.
5. **Set the threshold.** Write the pass score, tied to the stakes. Decide it now, before you run anything.
6. **Write the one-pager.** Three sentences (metric, test set, threshold), each ending in "because...". If you can defend all three reasons out loud, your plan is done.

## 7. Real-World Patterns

Teams that build machine-learning systems professionally write this kind of plan before they trust a system in production — a written test-and-evaluation design with named metrics, a held-out test suite, and explicit pass criteria agreed in advance. [2] The same discipline scales down cleanly to a Capstone: the plan is shorter, but the three decisions are identical.

Two worked sketches:

- **Support-ticket classifier.** Task: route tickets to a team. Costly mistake: sending an urgent ticket to the wrong queue (a miss), so **recall on the urgent class** matters most. Test set: 60 real, labeled past tickets, held out from anything used to build it. Threshold: recall on urgent tickets must be at least 0.90 to ship — because a missed urgent ticket means a customer waits days. [1][2]

- **Domain question-answering helper.** Task: answer staff questions from one company's handbook. This is a similarity-flavored task — like the cosine-similarity matching from 8.1 and 8.2, answers are judged on whether they mean the right thing, not on exact words. Costly mistake: a confident wrong answer, so the team tracks **accuracy plus a calibration check** (from 8.6) so a confidently-wrong answer is caught. Test set: 50 real questions with known correct answers. Threshold: at least 0.85 accuracy *and* no overconfident wrong answers above the displayed-confidence bar. [1]

## 8. Best Practices

**Do:**

- **Decide the threshold before you see results.** This is the single most important habit. [3]
- **Match the metric to the cost of errors**, not to whichever number looks highest. [1]
- **Keep the test set held-out and representative** of real use. [2]
- **Write one defensible sentence per decision.** If you cannot say "because...", the decision is not made yet.

**Don't:**

- **Don't trust a metric on a tiny test set.** Five or ten examples is a vibe, not evidence.
- **Don't report accuracy alone on imbalanced classes** — it hides the failures that matter (recall on the rare class). [1]
- **Don't move the goalposts** after seeing a disappointing score.
- **Don't show users a confidence number without a calibration check.** Confident-but-wrong erodes trust fast. [1]

## 9. Hands-On Exercise

Write the one-page evaluation plan for your own Capstone system. Pick the task, then fill in three "because" sentences: the metric and why, the test-set size and why, and the pass threshold and why. Read it aloud — if every "because" holds up, your plan is sound.

## 10. Key Takeaways

- An **evaluation plan** is three decisions written in advance: which metric, how many test examples, and what score counts as a pass.
- **Metric choice** is a matching exercise — pick the measure (recall, precision, F1, accuracy, plus a calibration check) that punishes the mistake your domain most wants to avoid.
- **Test set size** is about trust: enough labeled, held-out, representative examples that one or two stray cases cannot swing the score.
- **The pass/fail threshold is set in advance and tied to the stakes** — strict for high-harm tasks, modest for low-stakes ones — so the result cannot quietly lower the bar.
- Every decision should come with a one-sentence "because" you can defend out loud.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
