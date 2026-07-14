---
topic_id: "7.9"
title: "Recall — of all the things that were correct, how many did the model find"
position_in_module: 4
generated_at: "2026-06-23T00:00:00Z"
resource_count: 3
---

# 1. Recall — of all the things that were correct, how many did the model find — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **7.7 — Accuracy:** you need to understand what a classification task is, what a labelled dataset is, and why accuracy alone can be misleading when one category is much rarer than the other.
- **7.8 — Precision:** you need to understand the terms true positive and false positive, and why precision only evaluates items the model chose to flag. Topic 7.9 introduces the complementary question that precision deliberately ignores.

## 3. Learning Objectives

By the end of this topic, learners will be able to:

- Explain in plain English what recall measures for a classification model.
- Define true positive and false negative in the context of a model's predictions.
- Apply the recall formula (true positives divided by true positives plus false negatives) to a simple scenario.
- Explain why a model can have high accuracy and high precision while still having low recall.
- Identify at least one real-world situation where recall is the metric that matters most.
- Describe, without computing it, why precision and recall pull in opposite directions.

## 4. Introduction

In topic 7.8 you saw that precision answers one specific question: of all the items the model flagged, how many were genuinely correct? That is useful. But there is a second question hiding in the background — one that precision completely ignores.

Picture a disease-screening program. The program reviews 1,000 patient records and flags 5 of them as likely having the disease. All 5 flagged patients turn out to actually have the disease. That is perfect precision: every flag was correct.

But here is what you do not know from precision alone: there were 95 patients in that dataset who truly had the disease. The program found 5 of them and missed 90.

Perfect precision. Nearly complete failure. [1]

The missing question is this: **of all the cases that were genuinely positive, how many did the model actually catch?** That question has a name: recall. [1][2]

Recall and precision are two sides of the same coin. Precision asks about the quality of the model's flags. Recall asks about the coverage — did the model find the things it was supposed to find?

## 5. Core Concepts

### 5.1 The gap precision leaves behind

Precision only looks at the items the model flagged. It counts correct flags (true positives) and incorrect flags (false positives) and says nothing at all about items the model did not flag.

But some of those unflagged items may have been genuinely positive. The model failed to catch them. In the screening example above, 90 truly sick patients walked away undetected.

Recall is the metric designed to measure exactly that gap. [1][2]

### 5.2 True positive and false negative

You already know true positive from topic 7.8: a case the model flagged correctly — it said "positive" and the ground truth agreed.

The new term here is **false negative**.

A **false negative** is a case where:
- the model did NOT flag the item (it predicted "negative"), BUT
- the item was actually positive in the real world (ground truth says yes).

In plain language: the model missed it. The thing it was supposed to find was there, and the model failed to raise a flag. [1][2]

Examples:

- A spam filter that lets a phishing email pass into your inbox: the email was genuinely spam (positive), but the model called it safe (negative). That is a false negative.
- A disease-screening tool that reviews a truly sick patient's record and marks it "probably healthy": the patient was genuinely ill, but the model failed to flag it. That is a false negative.
- A fraud-detection system that processes a genuinely fraudulent transaction and approves it: real fraud (positive), no flag raised (negative). False negative. [2][3]

The practical consequence of a false negative is always the same: a real problem goes undetected.

### 5.3 The recall formula

Once you have the counts of true positives and false negatives, recall is a single calculation:

**Recall = True Positives / (True Positives + False Negatives)**

In plain English: divide the number of real positives the model correctly caught by the total number of real positives in the dataset — whether the model caught them or not. [1][2]

The denominator — true positives plus false negatives — is simply every item that was genuinely positive, regardless of what the model predicted.

- If there were 100 genuinely positive items and the model caught 90 of them: recall = 90/100 = 0.90 (90%).
- If there were 100 genuinely positive items but the model only caught 20: recall = 20/100 = 0.20 (20%).

Recall lives on a scale of 0 to 1 (or 0% to 100%). Higher is better when you care about not missing real cases. [1]

### 5.4 Recall only looks at the genuinely positive items

This is the single most important thing to understand about recall: **it ignores everything the model correctly left alone** (items that are genuinely negative and the model correctly did not flag). It is entirely focused on the group of items that were truly positive, asking how many of those the model managed to find.

This is both its strength and its limitation.

**Strength:** recall directly answers the question "is the model actually finding the things it is supposed to find?" If recall is 0.95, the model is catching 95 out of every 100 real cases — very few slip through.

**Limitation:** a model can achieve perfect recall of 1.0 by being extremely aggressive — flagging every single item in the dataset as positive. It will catch every genuine positive, but it will also flag everything else. Recall alone does not penalise that behaviour. A 1.0 recall score on its own tells you almost nothing about whether the flags are any good. [1][2][3]

This is why recall is discussed alongside precision, and why the two metrics matter together.

### 5.5 A concrete worked example

An AI content-moderation system reviews 1,000 social-media posts. Of those 1,000 posts, 100 are genuinely harmful content (ground truth = positive). The remaining 900 are ordinary posts.

The model flags 60 posts as potentially harmful.

- 50 of those 60 flagged posts are genuinely harmful (true positives = 50).
- 10 of those 60 flagged posts are ordinary posts incorrectly flagged (false positives = 10, which affects precision).
- 50 of the 100 genuinely harmful posts were NOT flagged by the model (false negatives = 50).
- 850 ordinary posts were correctly left alone (true negatives, which do not affect recall).

**Recall = 50 / (50 + 50) = 50 / 100 = 0.50 (50%)**

The model only caught half of the genuinely harmful posts. One in every two harmful posts went undetected. [1][2]

For comparison:

**Precision = 50 / (50 + 10) = 50 / 60 ≈ 0.83 (83%)**

So of the posts the model flagged, 83% were genuinely harmful — the flags are fairly reliable. But the model is only reaching 50% of the real harmful content. Whether that trade-off is acceptable depends on the context.

### 5.6 Why a model can have high accuracy but low recall

This mirrors the lesson from topic 7.7 (accuracy) and topic 7.8 (precision), applied to recall.

Return to the disease-screening example. Suppose:
- 1,000 patients are reviewed.
- 20 of them genuinely have the disease.
- The model flags 0 patients — it marks everyone "healthy."

Accuracy: 980 correct predictions out of 1,000 = **98%**. The model seems excellent.
Precision: undefined (no positive predictions, so the denominator is zero).
Recall: 0 / (0 + 20) = **0%**. The model caught none of the sick patients.

Perfect recall failure, hidden by a high accuracy number. [1][3]

The model with 98% accuracy and 0% recall is worse than useless for screening — it provides a false sense of security. Every genuinely sick patient walks away undetected.

This is exactly why accuracy alone is not enough (7.7), why precision fills one gap (7.8), and why recall fills the other (7.9).

### 5.7 The precision–recall relationship

Precision and recall often pull in opposite directions. Understanding why this happens does not require maths — the logic is intuitive.

Imagine a model is trying to catch fraud. It has a dial that controls how cautious it is:

- **Very cautious (flags almost nothing):** it only flags a transaction when it is extremely certain. Most flags are correct — high precision. But it misses most genuine fraud — low recall.
- **Very aggressive (flags almost everything):** it catches nearly every fraudulent transaction — high recall. But it also flags large numbers of legitimate transactions — low precision.

Moving the dial in one direction tends to improve one metric and hurt the other. This is the precision–recall trade-off. [1][2][3]

The right balance depends on the context. In a situation where missing a real positive is catastrophic (catching a rare but life-threatening illness, detecting a critical security breach), recall is prioritised even at the cost of more false alarms. In a situation where false alarms are expensive (customer complaints, blocked transactions, wasted review capacity), precision is prioritised even if some real cases slip through.

Neither precision nor recall is universally "more important." The context decides. Metrics that try to balance the two exist but are covered in a later topic.

## 6. Implementation

### Working through a recall calculation step by step

**Step 1: Identify the positive class.** Decide what counts as "positive" in your task — spam, fraud, harmful content, a disease diagnosis.

**Step 2: Find every genuinely positive item.** Go through your labelled test set and count all items where the ground truth label is positive. Call this the total positive count.

**Step 3: Count true positives.** Of all genuinely positive items, count how many the model flagged correctly (model said positive AND ground truth is positive).

**Step 4: Count false negatives.** From all genuinely positive items, count how many the model did NOT flag (model said negative BUT ground truth is positive). Note: true positives + false negatives = total positive count from step 2.

**Step 5: Apply the formula.**

```
recall = true_positives / (true_positives + false_negatives)
```

**Step 6: Interpret.** A recall of 0.70 means 70 out of every 100 genuinely positive cases were caught. 30 out of every 100 were missed.

### Worked example

A spam filter is tested on 200 emails. 40 of those emails are genuinely spam (positive). The remaining 160 are legitimate.

The filter flags 30 emails as spam:
- 28 of those 30 are genuinely spam (true positives = 28).
- 2 of those 30 are legitimate emails wrongly flagged (false positives = 2, affects precision).
- 12 of the 40 genuine spam emails were not flagged (false negatives = 12).

Recall = 28 / (28 + 12) = 28 / 40 = **0.70 (70%)**

The filter catches 70% of real spam. One in three genuine spam emails slips through to the inbox. Whether that is acceptable depends on how much the user cares about missing spam vs having legitimate email falsely flagged.

## 7. Real-World Patterns

**Medical screening.** In cancer screening and other disease detection applications, missing a real case (false negative) can be life-threatening. Recall is a primary metric in these settings — engineers accept a higher rate of false positives (lower precision) in order to ensure that most genuine cases are caught. [1][3]

**Security and fraud detection.** A bank's fraud system that misses 30% of real fraud events is failing its customers even if the flags it does raise are highly reliable. In high-stakes security contexts, teams typically set minimum recall thresholds before optimising anything else. [2]

**Content moderation at scale.** Platforms dealing with harmful content face a recall challenge: the volume of content is so large that a model with 70% recall still lets large numbers of harmful posts through undetected. Engineering teams at these organisations tune recall and precision simultaneously, accepting that no single threshold is perfect. [2][3]

**AI assistants answering factual questions.** In a setting like the lab this week — running yes/no questions through an AI — recall applies if you treat the correct-answer category as "positive." Of all the questions where "yes" was the right answer, how many did the model answer correctly with "yes"? That is recall for that category. [1]

## 8. Best Practices

**Do: pair recall with the question "what is the cost of a missed case?"** Before setting targets for recall, understand what happens when the model fails to flag a genuinely positive item. High-cost misses (undetected illness, undetected fraud, undetected security breach) push you toward needing higher recall. [1][2]

**Do: report recall alongside precision, not instead of it.** A model with recall of 1.0 that flags everything is useless. Recall alone can be gamed trivially by flagging all items. It is only meaningful alongside precision or a similar complementary measure. [1][3]

**Do: know your positive class before computing anything.** Recall is defined relative to what counts as "positive." Be explicit about this definition before running numbers.

**Don't: optimise recall alone.** A model that flags every item achieves perfect recall and zero useful information. Always consider what happens to precision when you push recall up.

**Don't: confuse false negatives with false positives.** A false negative is a miss — the model failed to flag something real. A false positive is a false alarm — the model flagged something that was not real. They are opposite errors with different costs in most real situations. [1][2]

## 9. Hands-On Exercise

Using the lab scenario from this week's session (a 5-question yes/no task run 10 times at temperature 0 and 10 times at temperature 1):

1. Decide which answer is "positive" for each question (for example, "yes" is the positive label).
2. Count the total number of times the correct answer for a question was "yes" — those are your genuinely positive instances.
3. Of those genuinely positive instances, count how many times the model actually answered "yes" (true positives) and how many times it said "no" instead (false negatives).
4. Compute recall = true positives / (true positives + false negatives) for each temperature setting.
5. Compare recall with the precision figure you computed in topic 7.8 (if you did that exercise). Write one sentence describing how the two numbers together give a more complete picture than either one alone.

## 10. Key Takeaways

- Recall answers one specific question: of all the items that were genuinely positive, what fraction did the model actually find?
- **Recall = True Positives / (True Positives + False Negatives).** The denominator is the total count of genuinely positive items in the dataset.
- A **false negative** is a miss — the model failed to flag something that was genuinely positive.
- Recall ignores everything the model correctly left alone. It only evaluates coverage of the real positives — which is both its strength and its limitation.
- Precision and recall pull in opposite directions: pushing one up tends to push the other down. The right balance depends on the cost of false alarms versus the cost of missed cases in the specific context.
- High accuracy does not guarantee high recall. A model can score 98% accuracy while catching 0% of the genuinely positive cases.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
