<!-- nav:top:start -->
[⬅ Previous: 7.6 — Mean, median, mode](../../7-6-mean-median-mode-measuring-consistency-across-ai-runs/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 7.8 — Precision ➡](../../7-8-precision-of-the-things-the-model-flagged-how-many-were-actu/artifacts/reading.md)
<!-- nav:top:end -->

---

# Accuracy — what proportion of outputs were correct

## Overview

When an AI model answers a set of questions, the most natural thing to ask is: how many did it get right? **Accuracy** answers exactly that — it is the proportion of predictions that matched the correct answer [1]. It is the starting point for measuring any AI model's performance: easy to compute, easy to explain, and useful as a quick gut check before looking at anything more specialised.

## Key Concepts

### Classification tasks

Accuracy is most meaningful on a **classification task** — a task where the model must assign each input to one of a fixed set of categories [1]. Examples:

- Is this email **spam** or **not spam**? (two categories)
- Does this photo show a **cat**, **dog**, or **rabbit**? (three categories)
- Is this review **positive**, **neutral**, or **negative**?

In every case the model picks one label. A human expert or reliable process checks each answer against the **ground truth** — the known-correct label you compare the model's answer against. That check produces two raw counts:

- **Correct predictions** — the model's label matched the ground truth label.
- **Incorrect predictions** — the model's label did not match the ground truth label.

### The accuracy formula

Accuracy is defined as [1][2]:

> **Accuracy = correct predictions ÷ total predictions**

The result is a number between 0 and 1 (or 0 %–100 %). Accuracy of 1.0 means right every time; 0.0 means wrong every time.

### When accuracy is useful

Accuracy gives a fair picture when [1][2]:

1. The categories appear with roughly equal frequency in your test data.
2. All types of mistake cost about the same (a low-stakes quiz app, for example).
3. You need a single, readable summary number to compare models quickly.

### When accuracy can mislead — the imbalanced-dataset problem

Consider a spam filter tested on 100 emails where only 5 are actually spam. A filter that labels every single email "not spam" — without ever looking at the content — scores 95 % accuracy [2][3]. It misses every piece of spam.

This happens because the dataset is **imbalanced**: one category (not-spam, 95 %) dominates. The model exploits that imbalance by always predicting the majority class [1][2].

**The dummy baseline** is the quick sanity check: what accuracy would you get by always predicting the most common category? If your model's score is close to that number, the score is not informative — the model may be doing nothing useful at all.

| Situation | Accuracy reliable? |
|---|---|
| Balanced categories (roughly 50 / 50) | Yes |
| Heavily imbalanced categories | No — check the dummy baseline |
| All mistakes cost the same | Yes |
| Some mistakes far more costly than others | Needs extra metrics |

### Accuracy and LLM outputs

Earlier in this week (topics 7.4 and 7.5) you saw that an LLM outputs a probability distribution over its vocabulary and samples a token — with temperature controlling how peaked or flat that distribution is. Accuracy evaluates the downstream results of that process: how often do the generated answers land on correct ones, regardless of how confident or varied the outputs were [1]?

### Precision and recall — named and deferred

When accuracy misleads, two other metrics step in: precision (topic 7.8) and recall (topic 7.9). These are named here only — their definitions and calculations come in the next two topics [2][3].

## Worked Example

**Scenario:** a spam filter is tested on 100 emails with known labels [1].

| What happened | Count |
|---|---|
| Real spam, correctly flagged as spam | 40 |
| Real spam, incorrectly passed through as "not spam" | 10 |
| Real "not spam", correctly passed through | 45 |
| Real "not spam", incorrectly flagged as spam | 5 |

**Step-by-step calculation:**

1. Collect the test set — 100 emails, each with a known ground truth label (spam or not spam).
2. Run the filter on every email and record its output label.
3. Compare each output to the ground truth — mark C (correct) or W (wrong).
4. Count: correct = 40 + 45 = **85**; incorrect = 10 + 5 = **15**; total = 100.
5. Apply the formula: Accuracy = 85 ÷ 100 = **0.85 (85 %)**.
6. Sanity check: the dummy baseline is 50 % (roughly equal spam / not-spam split here), so 85 % is meaningfully higher — the score is informative.

**Key observation:** accuracy treats all mistakes equally. The 10 spam emails that slipped through and the 5 legitimate emails that were wrongly flagged each count as one wrong answer. Whether that equal weighting is acceptable depends on the use case.

## In Practice

**Where accuracy shows up:**

- **Email spam filters** — the canonical first example in almost every ML course [2][3]. Engineers quickly move beyond accuracy here because spam is a small fraction of total email.
- **Medical screening** — a disease that affects 1 in 1,000 people means labelling everyone disease-free gives 99.9 % accuracy. No clinician calls that useful [2].
- **AI quiz and tutoring apps** — when roughly half of attempts are correct and half incorrect, accuracy gives a fair, readable summary.

**Do:**

- Compute the dummy baseline before reporting any accuracy figure.
- Report the test-set size alongside the accuracy number (85 % on 10 items means far less than 85 % on 10,000).
- State the categories clearly so readers know what "correct" means.

**Don't:**

- Use accuracy as the only metric on imbalanced data.
- Measure accuracy on the training data — use a held-out test set.
- Report accuracy to many decimal places on small test sets; the noise swamps the signal.

## Key Takeaways

- **Accuracy = correct predictions ÷ total predictions** — the proportion of outputs the model got right [1].
- It is most trustworthy when categories appear with similar frequency in the test data.
- Always compute the **dummy baseline** first: if your model barely beats "always predict the majority class", the score is not informative.
- Accuracy treats all mistakes equally and measures outcomes, not confidence.
- When accuracy misleads, precision (topic 7.8) and recall (topic 7.9) fill the gaps [2][3].

## References

1. Google ML Crash Course — Classification: Accuracy, Precision, Recall. https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall
2. EvidentlyAI — Accuracy, Precision, Recall for Classification. https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall
3. BuiltIn — Precision and Recall. https://builtin.com/data-science/precision-and-recall

---
<!-- nav:bottom:start -->
[⬅ Previous: 7.6 — Mean, median, mode](../../7-6-mean-median-mode-measuring-consistency-across-ai-runs/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 7.8 — Precision ➡](../../7-8-precision-of-the-things-the-model-flagged-how-many-were-actu/artifacts/reading.md)
<!-- nav:bottom:end -->
