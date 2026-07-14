<!-- nav:top:start -->
[⬅ Previous: 7.7 — Accuracy](../../7-7-accuracy-what-proportion-of-outputs-were-correct/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 7.9 — Recall ➡](../../7-9-recall-of-all-the-things-that-were-correct-how-many-did-the/artifacts/reading.md)
<!-- nav:top:end -->

---

# Precision — of the things the model flagged, how many were actually correct

## Overview

In topic 7.7 you saw that accuracy — the share of all predictions a model gets right — can be misleading when one outcome is far rarer than the other. Precision answers a sharper question: of all the items the model chose to flag as positive, how many were actually correct? [1] This matters any time a false alarm has a real cost — a blocked bank card, an anxious patient, a legitimate email buried in spam.

## Key Concepts

### The model's positive prediction — "flagged"

Every classification model looks at each item and outputs one of two labels: **positive** (the thing it is trained to detect is present) or **negative** (it is not). A positive prediction is often called a **flag** — the model raises its hand on that item. [1]

Examples of what "positive" means in different tasks:

- Spam filter → "this email is spam"
- Fraud detector → "this transaction is suspicious"
- Medical screener → "this patient likely has the disease"
- Content moderator → "this post is harmful"

### True positive (TP)

A **true positive** is a flagged item that is genuinely positive — the model was right to raise its hand. [1][2]

> Example: the spam filter marks an email as spam, and that email really is spam. That is a true positive.

### False positive (FP)

A **false positive** is a flagged item that is actually negative — the model raised a false alarm. [1][2][3]

> Example: the spam filter marks a legitimate email from your bank as spam. Nothing was wrong with that email. That is a false positive.

### The precision formula

Precision is a single calculation over the items the model flagged:

**Precision = True Positives ÷ (True Positives + False Positives)**

In plain English: divide the number of correct flags by the total number of flags. [1][2]

The denominator — true positives plus false positives — is simply every item the model flagged, whether the flag was correct or not.

| Flags raised | True positives | False positives | Precision |
|---|---|---|---|
| 100 | 90 | 10 | 90 / 100 = **0.90** |
| 100 | 30 | 70 | 30 / 100 = **0.30** |

Precision runs from 0 to 1 (or 0% to 100%). Higher means the model's alerts are more reliable. [1]

### Precision only looks at what the model flagged

This is the most important thing to understand: **precision ignores items the model did not flag**. It evaluates only the group the model called positive. [2][3]

That gives it both a strength and a limitation:

- **Strength:** it directly answers "can I trust this model's alerts?" A precision of 0.95 means 95 out of every 100 flags are correct.
- **Limitation:** a model can achieve perfect precision of 1.0 by flagging only the single most obvious case in the entire dataset. It misses everything else, but precision alone does not penalise it for that.

This is why precision is discussed alongside another metric — recall — which is covered in topic 7.9.

### How precision and accuracy tell different stories

Recall the spam filter from topic 7.7 that labelled every email "not spam."

- Its **accuracy** was high, because most emails genuinely are not spam.
- Its **precision** is undefined — it never flagged anything, so the denominator is zero.

Now flip it: a filter that flags every single email as spam.

- **Accuracy:** low — it gets all the legitimate emails wrong.
- **Precision:** equal to the real spam rate — perhaps 2%. It flagged 1,000 emails; 20 were real spam; precision = 20 / 1,000 = 2%. [1][3]

Neither extreme is useful. Precision and accuracy each illuminate a different part of a model's behaviour.

## Worked Example

A disease-screening algorithm processes 500 patient records and flags 40 as likely having the disease.

**Step 1 — Identify the positive class.** "Has the disease" is positive.

**Step 2 — Count true positives.** Medical review finds 32 of the 40 flagged patients genuinely have the disease. True positives = 32.

**Step 3 — Count false positives.** The remaining 8 flagged patients do not have the disease. False positives = 8.

**Step 4 — Apply the formula.**

```
Precision = 32 / (32 + 8) = 32 / 40 = 0.80
```

**Step 5 — Interpret.** A precision of 0.80 means 8 out of every 10 patients this algorithm flags for further tests genuinely need attention. 2 out of every 10 are false alarms.

Whether 80% is acceptable depends on the cost of those false alarms and on what happens to patients who were never flagged — a question precision alone cannot answer. [2]

## In Practice

**Spam filtering.** Email providers tune precision carefully. A filter with low precision buries legitimate email in the spam folder. High-precision filters only flag mail they are confident about, even if some real spam slips through. [1][3]

**Fraud detection.** Flagging a legitimate transaction as fraudulent (false positive) blocks a customer's card. High precision keeps customer experience smooth; lower precision means more manual reviews. [2]

**Medical screening.** Screening tests for rare diseases often run at lower precision by design — a missed positive can be life-threatening, so the algorithm accepts more false alarms to catch every real case. Precision is kept in view alongside recall when making that design choice. [3]

**Content moderation.** Human review teams can only handle a limited volume of flagged content. High precision means the flags that reach reviewers are mostly genuine cases, so reviewers spend their time on real problems rather than false alarms. [1][2]

**Two rules of thumb:**

- Do report precision alongside accuracy — a model with 95% accuracy but 40% precision is failing badly at its primary job. [1]
- Do not optimise precision in isolation — a model can game precision by flagging almost nothing. Precision is meaningful only as part of a broader picture that includes recall (topic 7.9). [3]

## Key Takeaways

- **Precision answers one question:** of all the items the model flagged as positive, what fraction were genuinely positive?
- **Precision = True Positives ÷ (True Positives + False Positives).** The denominator is the total number of flags raised.
- **A false positive is a false alarm** — the model flagged something it should not have.
- **Precision and accuracy measure different things.** High accuracy does not guarantee high precision; the two can diverge dramatically on imbalanced datasets.
- **Precision ignores what the model did not flag.** That is both its strength (laser-focused on alert reliability) and its limitation (a stingy model can look great on precision while missing most real cases).

## References

1. Google ML Crash Course — Classification: Accuracy, Precision, and Recall. https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall
2. EvidentlyAI — Accuracy, Precision, Recall. https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall
3. BuiltIn — Precision and Recall. https://builtin.com/data-science/precision-and-recall

---
<!-- nav:bottom:start -->
[⬅ Previous: 7.7 — Accuracy](../../7-7-accuracy-what-proportion-of-outputs-were-correct/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 7.9 — Recall ➡](../../7-9-recall-of-all-the-things-that-were-correct-how-many-did-the/artifacts/reading.md)
<!-- nav:bottom:end -->
