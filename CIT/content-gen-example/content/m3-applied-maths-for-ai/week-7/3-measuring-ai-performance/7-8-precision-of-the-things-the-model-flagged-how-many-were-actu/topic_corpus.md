---
topic_id: "7.8"
title: "Precision — of the things the model flagged, how many were actually correct"
position_in_module: 3
generated_at: "2026-06-23T00:00:00Z"
resource_count: 3
---

# 1. Precision — of the things the model flagged, how many were actually correct — Topic Corpus

## 2. Prerequisites

This topic builds directly on topic 7.7 (Accuracy, correct prediction, incorrect prediction, accuracy formula, classification task, labelled dataset, test set, ground truth, accuracy limitations, imbalanced dataset, dummy baseline). You must understand what a classification task is and why accuracy alone can be misleading before this topic will make full sense.

## 3. Learning Objectives

- Explain in plain English what precision means for a classification model.
- Define **true positive** and **false positive** in the context of a model's flagged predictions.
- Apply the precision formula (true positives divided by true positives plus false positives) to a simple scenario.
- Explain why a model can have high accuracy but low precision.
- Identify at least one real-world situation where precision is the metric that matters most.

## 4. Introduction

In topic 7.7 you saw that accuracy — the share of all predictions the model got right — can be dangerously misleading when one outcome is much rarer than the other. A spam filter that labels every single email as "not spam" gets 98% accuracy and catches zero spam. That is clearly useless, yet accuracy does not tell you so.

So here is the natural follow-up question: **when the model does raise its hand and say "yes, this one is positive," how often is it actually right?**

That question has a name: **precision**. [1]

Think of a doctor ordering a medical test. The test flags ten patients as likely having a disease. Precision asks: of those ten flagged patients, how many truly have the disease? If nine of ten actually do, precision is high — great, the test is reliable. If only two of ten actually do, precision is low — most of the alerts are false alarms, which wastes resources, causes anxiety, and erodes trust.

The same logic applies to any AI classifier: a content-moderation system flagging harmful posts, a fraud-detection model alerting on suspicious transactions, or an email filter marking messages as spam. In every case, precision is the metric that tells you how trustworthy the model's positive flag is. [1][2]

## 5. Core Concepts

### 5.1 What "flagged" means — the model's positive prediction

When a classification model runs, it looks at each item and makes a decision: **positive** (the thing it is trained to detect is present) or **negative** (it is not). The positive label is whatever the model is designed to find: spam, fraud, a disease, a harmful image.

"Flagged" is everyday language for a positive prediction — the model raised its hand on that item. [1]

### 5.2 True positive (TP)

A **true positive** is a case where:
- the model flagged the item as positive, AND
- the item really is positive in the real world (ground truth says yes).

In other words: the model was right to flag it. It caught a real instance of the thing it is looking for.

Example: the spam filter marks an email as spam, and that email genuinely is spam. That is a true positive. [1][2]

### 5.3 False positive (FP)

A **false positive** is a case where:
- the model flagged the item as positive, BUT
- the item is actually negative in the real world (ground truth says no).

In other words: the model raised a false alarm. It flagged something that should not have been flagged.

Example: the spam filter marks a legitimate email from your bank as spam. Nothing was wrong with that email — the model was wrong to flag it. That is a false positive. [1][2][3]

### 5.4 The precision formula

Once you have those two counts, precision is a single calculation:

**Precision = True Positives / (True Positives + False Positives)**

In plain English: divide the number of correct flags by the total number of flags. [1][2]

The denominator — true positives plus false positives — is simply every item the model flagged, regardless of whether the flag was correct or not.

- If the model flagged 100 items and 90 of those were genuinely positive: precision = 90/100 = 0.90 (or 90%).
- If the model flagged 100 items but only 30 were genuinely positive: precision = 30/100 = 0.30 (or 30%).

Precision lives on a scale of 0 to 1 (or 0% to 100%). Higher is better when you care about the reliability of positive flags. [1]

### 5.5 Precision only looks at what the model flagged

This is the single most important thing to understand about precision: **it ignores items the model did not flag**. It is entirely focused on the group of items the model chose to call positive.

This is both its strength and its limitation.

**Strength:** it directly answers the question "can I trust the model's alerts?" If precision is 0.95, you can be quite confident that when the model raises a flag, it is right 95% of the time.

**Limitation:** a model can achieve perfect precision of 1.0 by being extremely stingy — flagging only the single most obvious case in the entire dataset and getting that one right. That model misses everything else, but precision alone does not penalise it for that. [2][3]

This is why precision is often discussed alongside another metric called recall, covered in topic 7.9.

### 5.6 Why precision and accuracy tell different stories

Recall the spam filter from topic 7.7 that labelled every email "not spam." Its accuracy was high because most emails genuinely are not spam. But its precision is undefined — it never flagged anything, so there are zero positives in the denominator.

Now consider the opposite extreme: a spam filter that flags every single email as spam.

- Accuracy: low (it gets all the legitimate emails wrong).
- Precision: equal to the proportion of emails that truly are spam — maybe 2%. It flagged 1000 emails; 20 were really spam; precision = 20/1000 = 2%.

Neither extreme is useful. Precision and accuracy each illuminate a different part of the model's behaviour. [1][3]

A more realistic example to make the numbers concrete:

> An AI content-moderation system reviews 1,000 social-media posts. It flags 80 posts as potentially harmful. Of those 80 flagged posts, 64 are genuinely harmful and 16 are harmless posts that were flagged by mistake.
>
> - True positives = 64
> - False positives = 16
> - Precision = 64 / (64 + 16) = 64 / 80 = 0.80 (80%)
>
> For every 10 posts the system flags for human review, 8 really do need attention and 2 are false alarms. [1][2]

### 5.7 What happens when precision is low?

Low precision means the model produces many false positives — many false alarms. Depending on the context, that has real costs:

- A fraud-detection system that flags legitimate transactions causes customers to have their cards blocked unnecessarily. Loss of trust, wasted review time, customer complaints. [2]
- A medical screening tool that flags many healthy patients as likely ill causes unnecessary follow-up tests, anxiety, and cost. [3]
- A spam filter with low precision puts legitimate emails in your spam folder. You miss important messages.

The cost of a false positive varies enormously by domain. In some settings (e.g., catching a rare but catastrophic failure) you accept low precision because missing a real positive is far worse. That trade-off involves recall, covered in topic 7.9.

### 5.8 Precision in the context of AI systems

When an AI system is used as a **classifier** — for example, a model that reads job applications and flags them as "relevant" or "not relevant" — precision directly applies. Of the applications it flags as relevant, how many genuinely are? [2]

For retrieval systems (where a model retrieves documents to answer a question), precision at a given number of results measures how many of the retrieved documents are actually relevant. The formula is identical. [3]

The core intuition is the same regardless of the system: precision is the reliability score for the model's positive outputs.

## 6. Implementation

### Working through a precision calculation step by step

Follow these steps whenever you need to compute precision from raw results:

**Step 1: Identify the positive class.** Decide what counts as "positive" in your task — spam, fraud, relevant, harmful, etc.

**Step 2: Count true positives.** Go through every item the model flagged as positive. Count how many were genuinely positive (ground truth = positive).

**Step 3: Count false positives.** From the same flagged set, count how many were actually negative (ground truth = negative).

**Step 4: Apply the formula.**

```
precision = true_positives / (true_positives + false_positives)
```

**Step 5: Interpret.** A precision of 0.75 means 75 out of every 100 flags the model raises are correct. 25 out of every 100 are false alarms.

### Worked example

A disease-screening algorithm processes 500 patient records. It flags 40 patients as likely having the disease.

- Medical review finds that 32 of the 40 flagged patients genuinely have the disease (true positives = 32).
- The remaining 8 flagged patients do not have the disease (false positives = 8).

Precision = 32 / (32 + 8) = 32 / 40 = **0.80 (80%)**

Eight out of every 100 patients the algorithm flags will be false alarms. Whether 80% is good enough depends on the consequences of those false alarms and on what happens to patients who were not flagged — a question precision alone cannot answer.

## 7. Real-World Patterns

**Spam filtering.** Email providers tune precision carefully. A filter with low precision annoys users by burying legitimate email in the spam folder. High precision filters only flag mail they are confident about, even if that means some actual spam slips through. [1][3]

**Fraud detection.** Banks face a sharp precision trade-off. Flagging a legitimate transaction as fraudulent (false positive) means blocking a customer's card mid-purchase. High precision keeps customer experience smooth; lower precision means more manual reviews but fewer missed frauds. [2]

**Medical screening.** Screening tests for rare diseases often run at relatively lower precision by design. A false positive (telling a healthy person they might be ill) leads to further testing. A missed positive (telling a sick person they are fine) could be life-threatening. Precision is kept in view alongside recall when making that design choice. [3]

**Content moderation.** Platforms moderating harmful content at scale use precision as a key metric. Human review teams can only handle a certain volume of flagged content. High precision means the flags that reach human reviewers are mostly genuine cases — reviewers spend their time on real problems rather than false alarms. [1][2]

## 8. Best Practices

**Do: pair precision with the question "what is the cost of a false alarm?"** Before optimising for precision, understand what happens when the model raises an incorrect flag. High-cost false alarms (blocking a patient's surgery, freezing a business account) push you toward needing higher precision. [2]

**Do: report precision alongside accuracy.** Accuracy alone hides precision problems. A model with 95% accuracy but 40% precision is failing badly at its most important job — correctly identifying the things it flags. [1]

**Do: understand your positive class clearly.** Precision only makes sense once you have decided what "positive" means. Be explicit about this before computing or reporting the metric. [1][2]

**Don't: optimise precision in isolation.** A model that flags nothing has undefined precision (division by zero) or trivially high precision by flagging only the one case it is most certain about. Both extremes are useless. Precision is meaningful as part of a broader picture that includes recall (topic 7.9). [3]

**Don't: confuse precision with accuracy.** Accuracy counts across all predictions. Precision only looks at the positive predictions. They measure different things and can diverge dramatically. [1]

## 9. Hands-On Exercise

Using the lab scenario from this week's session (a 5-question yes/no task run 10 times at temperature 0 and 10 times at temperature 1):

1. Decide which answer is "positive" for each question (for example, "yes" is the positive label).
2. For each temperature setting, count how many times the model said "yes."
3. Of those "yes" answers, count how many were actually correct (true positives) and how many were wrong (false positives).
4. Compute precision for each temperature.
5. Write one sentence comparing precision at temperature 0 vs temperature 1. Does higher temperature help or hurt precision in your results?

This exercise connects the precision formula directly to the lab data you already collected.

## 10. Key Takeaways

- **Precision answers one specific question:** of all the items the model flagged as positive, what fraction were genuinely positive?
- **Precision = True Positives / (True Positives + False Positives).** The denominator is the total number of flags the model raised.
- **A false positive is a false alarm** — the model flagged something it should not have.
- **Precision and accuracy measure different things.** High accuracy does not guarantee high precision, and a model can have any combination of the two.
- **Precision ignores what the model did not flag.** It only evaluates the reliability of the positive predictions the model did make — which is both its strength and its limitation.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
