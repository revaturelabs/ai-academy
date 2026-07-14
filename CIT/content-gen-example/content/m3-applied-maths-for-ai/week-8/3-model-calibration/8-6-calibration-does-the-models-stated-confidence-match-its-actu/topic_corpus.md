---
topic_id: 8.6
title: Calibration — does the model's stated confidence match its actual accuracy?
position_in_module: 1
generated_at: 2026-06-22T00:00:00Z
resource_count: 3
---

# 1. Calibration — does the model's stated confidence match its actual accuracy? — Topic Corpus

## 2. Prerequisites

- **8.5 — Computing accuracy, precision, recall, and F1 by hand from a confusion matrix.** You should already know that **accuracy** means the fraction of predictions the model got right [3].
- **8.3 — Precision vs recall trade-off.** You should be comfortable with the everyday idea that a model makes predictions and is sometimes right and sometimes wrong.

## 3. Learning Objectives

After this topic you will be able to:

- Explain in plain words what it means for a model to be **well-calibrated**.
- Describe how a model can attach a **confidence** number to a prediction.
- Read a **reliability diagram** and say whether a model is over- or under-confident.
- Tell the difference between a model being **accurate** and a model being **calibrated** — they are not the same thing.
- Explain why a confidence score is only useful for decisions when the model is calibrated.

## 4. Introduction

Imagine your weather app says "70% chance of rain" every day for a month. On the days it said 70%, did it actually rain about 70% of the time? If yes, the app's confidence matches reality — you can trust the number and decide whether to carry an umbrella. If it rained only 40% of those days, the app was *too sure of itself*, and its "70%" means nothing useful.

AI models do the same thing. When a model makes a prediction, it can also report **how confident it is** — a number like "I'm 90% sure this email is spam." **Calibration** asks one question about those confidence numbers: *do they match how often the model is actually right?* [1]

This matters because in 8.5 you learned to measure **accuracy** — how often the model is right overall. But accuracy alone does not tell you whether to trust any *single* prediction. Calibration is the missing piece: it tells you whether the confidence attached to a prediction can be believed [1].

## 5. Core Concepts

### 5.1 Confidence — the model's own bet on each prediction

When a model makes a prediction, many models also output a **confidence**: a number between 0 and 1 (or 0% to 100%) saying how sure the model is about that single prediction.

- **Confidence** — the model's stated belief that *this particular* prediction is correct. Example: "spam, confidence 0.95" means the model is betting 95% that this email is spam.
- A high confidence (0.95) is the model saying "I'm almost certain." A low confidence (0.55) is the model saying "I'm barely leaning this way."

Confidence is a *claim the model makes about itself*. The whole point of this topic is to check whether that claim is honest.

### 5.2 Calibration — does the claim match reality?

**Calibration** — a model is **well-calibrated** when its stated confidence matches its actual accuracy over many predictions [1].

Here is the plain-words test. It is the single most important idea in this topic:

> If you gather every prediction the model made with about **70% confidence**, then about **70% of them** should turn out correct. If you gather all the **90% confidence** predictions, about **90%** should be correct. And so on, at every confidence level.

Notice this is a statement about *groups* of predictions, not one prediction. You cannot check calibration from a single guess. You check it by collecting many predictions at the same confidence level and seeing what fraction were actually right [1][3].

A quick contrast keeps this straight:

| Question | What it measures |
|---|---|
| **Accuracy** (8.5) | Of all predictions, how many were correct? |
| **Calibration** (this topic) | When the model says "X% sure," is it right about X% of the time? |

A model can be accurate but badly calibrated, and a model can be calibrated but not very accurate. They answer different questions.

### 5.3 Grouping predictions by confidence level (bucketing)

To check calibration you cannot compare each confidence to a single right/wrong outcome — one prediction is either fully right or fully wrong, never "70% right." So you **group** predictions by confidence level first.

- Sort every prediction into **buckets** by its confidence. For example: a bucket for predictions around 0.6 confidence, another around 0.7, another around 0.8, and so on.
- For each bucket, compute two numbers:
  1. The **average stated confidence** of the predictions in that bucket (e.g. 0.70).
  2. The **observed accuracy** in that bucket — what fraction of those predictions actually turned out correct (e.g. 0.55) [2][3].
- If those two numbers match in every bucket, the model is well-calibrated. If they drift apart, it is not.

That is the entire mechanism. We are not doing any heavy math — just *group, then compare the model's confidence to the truth* in each group.

### 5.4 The reliability diagram — a picture of calibration

A **reliability diagram** is a plot that shows calibration at a glance [2]. It is the visual heart of this topic.

- The **x-axis (across)** is the model's **stated confidence** for each bucket.
- The **y-axis (up)** is the **observed accuracy** — how often the model was actually right in that bucket.
- Each bucket from 5.3 becomes one point on the plot.

Now the key reading rule:

- A **perfectly calibrated** model sits exactly on the **diagonal line** (the 45-degree line from bottom-left to top-right). On the diagonal, stated confidence *equals* observed accuracy — exactly what "well-calibrated" means [1][2].
- A point **below the diagonal** means the model is **overconfident**: it stated high confidence but was right less often. Example: it said 0.90 but was only correct 0.70 of the time [1].
- A point **above the diagonal** means the model is **underconfident**: it was right more often than it claimed. Example: it said 0.60 but was actually correct 0.80 of the time [1].

| Where the point sits | What it means | Plain example |
|---|---|---|
| On the diagonal | Well-calibrated | Says 0.70, right 70% of the time |
| Below the diagonal | Overconfident | Says 0.90, right only 70% of the time |
| Above the diagonal | Underconfident | Says 0.60, right 80% of the time |

Overconfidence is the more dangerous failure: the model sounds sure but is wrong more than it claims, so you trust it more than you should [1].

### 5.5 Why calibration matters

A confidence score is only worth something if it is calibrated [1]. Confidence numbers exist so people (or other systems) can make decisions: "if the model is over 90% sure, accept it automatically; otherwise send it to a human."

- If the model is **well-calibrated**, that rule is safe — a 0.90 really does mean right 9 times out of 10.
- If the model is **overconfident**, the same rule quietly lets many wrong answers through, because "0.90" actually means "right 7 times out of 10."

So calibration turns a confidence number from a vague vibe into something you can build a decision on. An accurate-but-overconfident model can be more dangerous than a less accurate but honest one, because it hides its own mistakes behind a high number.

> **Beyond this topic:** the gap between stated confidence and observed accuracy can be squeezed into a single summary number called Expected Calibration Error (ECE) — covered beyond this topic. Techniques that adjust a model's confidence to fix poor calibration are also covered later, not here.

## 6. Implementation

A by-hand procedure to check calibration on a set of predictions — no formulas beyond counting and dividing:

1. **Collect** every prediction together with (a) the model's stated confidence and (b) whether it was actually correct.
2. **Bucket** the predictions by confidence — for example, group everything near 0.6, near 0.7, near 0.8, and so on.
3. For each bucket, find the **average stated confidence** (the model's claim).
4. For each bucket, find the **observed accuracy** — count how many in the bucket were correct, divide by how many are in the bucket [3].
5. **Compare** the two numbers in each bucket. Close = calibrated for that bucket; confidence higher than accuracy = overconfident; lower = underconfident.
6. **Plot** each bucket as a point (stated confidence across, observed accuracy up) and see where it falls relative to the diagonal [2].

## 7. Real-World Patterns

- **Decision thresholds.** Spam filters, fraud flags, and medical triage tools often "auto-act above 0.9, escalate to a human below it." That rule only holds if the model's 0.9 is calibrated [1].
- **Reliability diagrams in tooling.** Practitioners plot reliability diagrams to inspect a model's confidence behaviour before trusting its scores in production [2].
- **Spotting overconfidence.** A model that scores well on accuracy can still be overconfident — its high confidence numbers leak more errors than the score suggests, which the reliability diagram exposes [1][2].

## 8. Best Practices

- **Do** judge a confidence score only after checking calibration — never assume "0.95" means "right 95% of the time."
- **Do** use many predictions grouped into buckets; calibration is a property of groups, not single predictions.
- **Don't** confuse accuracy with calibration — a model can be one without the other.
- **Don't** trust an automatic accept/reject threshold on an uncalibrated model; overconfidence will quietly pass wrong answers through.

## 9. Hands-On Exercise

Run a 10-question quiz with an AI assistant. For each question, write down two things: the model's **stated confidence** and whether its answer was **actually correct**. Then group the questions by confidence level (e.g. the ones it was ~70% sure about, the ones it was ~90% sure about) and, for each group, compute the fraction it actually got right. Compare that fraction to the stated confidence: where it matches, the model is calibrated; where confidence is higher than the fraction correct, it is overconfident. Optionally plot each group as a point against the diagonal to make your own reliability diagram.

## 10. Key Takeaways

- **Calibration** asks whether a model's stated **confidence** matches its **actual accuracy** over many predictions.
- A model is **well-calibrated** when, among all its ~70%-confidence predictions, about 70% turn out correct — and likewise at every confidence level.
- On a **reliability diagram**, a perfectly calibrated model sits on the diagonal; points **below** it are **overconfident**, points **above** it are **underconfident**.
- **Accuracy** and **calibration** are different questions — a model can be accurate yet overconfident.
- A confidence score is only trustworthy for decisions when the model is calibrated.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
