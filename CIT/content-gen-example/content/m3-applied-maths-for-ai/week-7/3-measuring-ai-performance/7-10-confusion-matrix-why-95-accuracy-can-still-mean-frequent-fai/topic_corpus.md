---
topic_id: "7.10"
title: "Confusion matrix — why 95% accuracy can still mean frequent failure"
position_in_module: 5
generated_at: "2026-06-23T00:00:00Z"
resource_count: 1
---

# 1. Confusion matrix — why 95% accuracy can still mean frequent failure — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **7.7 — Accuracy:** you need to understand the classification task, the labelled test set, and the core insight that high accuracy can hide failure when one class is rare.
- **7.8 — Precision:** you need the definitions of true positive and false positive, and the precision formula.
- **7.9 — Recall:** you need the definition of false negative and the recall formula.

Topic 7.10 is a unification topic. The confusion matrix is the single table that puts all four prediction outcomes — true positive, false positive, false negative, and true negative — in one view, and shows how precision, recall, and accuracy each read off that same table.

## 3. Learning Objectives

By the end of this topic, learners will be able to:

- Name and describe all four cells of a confusion matrix (TP, FP, FN, TN) in plain language.
- Construct a simple confusion matrix from a worked scenario and read off counts from it.
- Explain why a model can report 95% accuracy while still failing badly on the cases that matter most.
- Identify which cells of the confusion matrix feed the precision formula and which feed the recall formula.
- Describe at least one real-world situation where the confusion matrix reveals a problem that accuracy hides.

## 4. Introduction

You have now met three metrics for measuring how well a classification model performs: accuracy (topic 7.7), precision (topic 7.8), and recall (topic 7.9). Each one answers a different question about the model's behaviour. Accuracy asks whether predictions were right overall. Precision asks whether the positive flags were trustworthy. Recall asks whether the model actually found all the real positives.

But those three metrics are not separate, unrelated ideas. They all flow from the same underlying set of counts — four numbers that describe every possible outcome of a classification decision. The confusion matrix is the tool that puts those four numbers in one place, in a simple table, so you can see the full picture at a glance. [1]

Here is the motivating problem. Suppose someone tells you: "Our disease-screening AI has 95% accuracy." Should you be impressed?

Not necessarily. If 95 out of every 100 patients in the test set were healthy, a model that labels every single patient "healthy" — without doing any real screening at all — achieves 95% accuracy automatically. It misses every single sick patient. Its recall for the disease is 0%. Its confusion matrix would make this failure immediately obvious. [1]

The confusion matrix is not a more complicated metric. It is a clearer view — a 2×2 table that shows you exactly how many predictions landed in each of the four possible buckets, so that no failure mode can hide behind a single headline number.

## 5. Core Concepts

### 5.1 The four possible outcomes of a classification prediction

When a model makes a prediction about a single item, exactly one of four things happens. The model either says "positive" or "negative," and the truth is either positive or negative. That gives four combinations. [1]

Before naming those combinations, two terms need plain-language definitions used throughout this topic:

**Positive class** — the category the model is trained to detect. If you are building a spam filter, "spam" is the positive class. If you are screening for a disease, "has the disease" is the positive class. Everything that is not the positive class is the **negative class** — the default, unremarkable outcome the model is trying to separate from. [1]

**Ground truth** — the actual correct label for each item in the dataset, determined by a human expert or a reliable reference before the model is run. Ground truth is what the model's prediction is compared against to decide whether it was right or wrong. [1]

You already know three of the four prediction outcomes from topics 7.8 and 7.9. The fourth is new here.

**True Positive (TP)**
The model predicted positive AND the item really is positive (matches ground truth).
The model was right to flag it. It caught a real case.
Example: the spam filter marks an email as spam, and that email genuinely is spam. [1]

**False Positive (FP)**
The model predicted positive BUT the item is actually negative (does not match ground truth).
The model raised a false alarm.
Example: the spam filter marks a legitimate email from your bank as spam. [1]

**False Negative (FN)**
The model predicted negative BUT the item is actually positive (does not match ground truth).
The model missed it — a real positive slipped through.
Example: the spam filter lets a genuine phishing email through to your inbox. [1]

**True Negative (TN)**
The model predicted negative AND the item really is negative (matches ground truth).
The model was right to leave it alone. It correctly identified a non-case.
Example: the spam filter looks at a legitimate newsletter and correctly decides it is not spam. [1]

True negative is the new term introduced in this topic. It is the "correct non-flag" — the model looked at something that was not the positive class, and correctly left it alone. [1]

Notice the naming pattern: "True" means the model's prediction matched the ground truth. "False" means the model's prediction did not match the ground truth. "Positive" means the model predicted the item belonged to the positive class. "Negative" means the model predicted the item did not. [1]

### 5.2 The confusion matrix — all four outcomes in one table

A confusion matrix is a 2×2 table that arranges these four outcomes in a consistent layout. One axis shows what the model predicted; the other axis shows what was actually true — the ground truth. [1]

```
                        ACTUAL: Positive    ACTUAL: Negative
PREDICTED: Positive     True Positive (TP)  False Positive (FP)
PREDICTED: Negative     False Negative (FN) True Negative (TN)
```

Every single prediction the model made lands in exactly one of these four cells. Add up all four cells and you get the total number of predictions made. [1]

The matrix gets its name — "confusion" — because it shows where the model gets confused: the FP cell is where it confused a negative for a positive, and the FN cell is where it confused a positive for a negative. [1]

Reading the matrix is straightforward once you remember the layout: [1]
- The top row is everything the model called positive (all flags the model raised).
- The bottom row is everything the model called negative (all items the model left alone).
- The left column is everything that was actually positive in the real world — the ground truth positives.
- The right column is everything that was actually negative in the real world — the ground truth negatives.

The two cells on the diagonal (top-left and bottom-right) are the model's correct predictions. The two cells off the diagonal are the model's mistakes. [1]

### 5.3 A concrete worked example

A disease-screening model is tested on 1,000 patient records. Of those 1,000 patients, 100 genuinely have the disease (ground truth: positive) and 900 do not (ground truth: negative). [1]

The model produces predictions. After checking every prediction against the ground truth:

- 70 patients who truly had the disease were correctly flagged by the model → **TP = 70**
- 30 patients who truly had the disease were not flagged — the model missed them → **FN = 30**
- 50 healthy patients were incorrectly flagged as having the disease → **FP = 50**
- 850 healthy patients were correctly left alone → **TN = 850**

The confusion matrix for this model is:

```
                        ACTUAL: Disease     ACTUAL: Healthy
PREDICTED: Disease      TP = 70             FP = 50
PREDICTED: Healthy      FN = 30             TN = 850
```

Total predictions: 70 + 50 + 30 + 850 = 1,000. Every prediction accounted for. [1]

Now read off the headline numbers:

**Accuracy** = correct predictions / total predictions = (TP + TN) / all = (70 + 850) / 1000 = 920 / 1000 = **92%** [1]

**Precision** = TP / (TP + FP) = 70 / (70 + 50) = 70 / 120 ≈ **58%** [1]

**Recall** = TP / (TP + FN) = 70 / (70 + 30) = 70 / 100 = **70%** [1]

The accuracy number (92%) looks respectable. But the confusion matrix shows what is really happening: the model misses 30 out of every 100 genuinely sick patients, and raises false alarms on 50 healthy patients for every 70 real cases it catches. The precision of 58% means fewer than 6 in 10 of its positive flags are correct. A clinician following every flag from this model would be sending a large number of healthy patients for unnecessary follow-up. [1]

The matrix does not add new information on top of TP, FP, FN, and TN — it simply presents those four numbers together so none of them can be hidden. [1]

### 5.4 Why 95% accuracy can still mean frequent failure

The confusion matrix makes the "accuracy paradox" easy to see. Return to the extreme example from the Introduction. [1]

Suppose a model is screening 1,000 patients. 50 genuinely have a rare condition (ground truth: positive). 950 are healthy (ground truth: negative). The model is a lazy model: it labels every single patient "healthy" — it never flags anyone.

```
                        ACTUAL: Condition   ACTUAL: Healthy
PREDICTED: Condition    TP = 0              FP = 0
PREDICTED: Healthy      FN = 50             TN = 950
```

- Accuracy = (0 + 950) / 1000 = **95%** [1]
- Precision = 0 / 0 = undefined (the model flagged no one)
- Recall = 0 / (0 + 50) = **0%** [1]

The accuracy looks excellent. The confusion matrix reveals the truth: the model has never correctly identified a single sick patient. Every genuinely positive patient is in the FN cell. The bottom-right cell (TN = 950) is inflating accuracy because there are many healthy patients and the model happens to get all of them right by simply doing nothing. [1]

This is the scenario the topic title names: 95% accuracy meaning frequent failure. The failure is invisible when you look at accuracy alone, but the confusion matrix makes it concrete — TP = 0 says everything. [1]

The key insight: accuracy is computed from all four cells equally. When the negative class is much larger than the positive class, the TN cell dominates the numerator of the accuracy formula. A model that does nothing but predict negative will have high accuracy while having zero TP, and its failure will be buried. [1]

### 5.5 How precision and recall connect to the confusion matrix

Precision and recall — introduced as standalone metrics in topics 7.8 and 7.9 — are both derived directly from the confusion matrix. The matrix unifies them. [1]

**Precision uses the top row of the confusion matrix.**

```
Precision = TP / (TP + FP)
```

TP and FP are both in the top row (everything the model predicted as the positive class). Precision asks: of all the items the model flagged, what share were real? It reads across the top row and compares the correct flags (TP) to the total flags (TP + FP). [1]

**Recall uses the left column of the confusion matrix.**

```
Recall = TP / (TP + FN)
```

TP and FN are both in the left column (everything that was actually the positive class — the ground truth positives). Recall asks: of all the items that were truly positive, what share did the model find? It reads down the left column and compares what the model caught (TP) to everything that was real (TP + FN). [1]

**Accuracy uses all four cells.**

```
Accuracy = (TP + TN) / (TP + FP + FN + TN)
```

The diagonal cells (TP and TN) are the correct predictions. The total of all four cells is the total number of predictions. [1]

So the confusion matrix is not a separate metric alongside precision and recall — it is the common foundation that all three metrics read from. Having the matrix means you can compute all three with arithmetic; having only a single metric means you cannot recover the others. [1]

### 5.6 True negatives — the fourth cell

True negative (TN) is the outcome that precision and recall both ignore. Precision ignores TN entirely; recall also ignores TN entirely. Both metrics are defined only over the items that were positive in some sense — either predicted positive or actually positive (ground truth positive). [1]

Why does TN matter, then? Because TN is what inflates accuracy in imbalanced datasets (as shown in section 5.4). When TN is large — when there are many genuine negatives and the model correctly identifies all of them — accuracy climbs even if the model is completely failing on the positive class.

True negative is not a failure. It is a correct prediction: the model looked at a genuinely negative item and correctly said "negative." In a spam filter, every legitimate email that passes through without a flag is a true negative. In a disease screener, every healthy patient correctly cleared is a true negative. These are good outcomes. [1]

The issue is that a dataset with many items in the negative class will generate a large TN count, which then props up accuracy. The confusion matrix makes this visible: if you see a very large TN alongside a very small TP, you know accuracy is being driven by the negative class, and you need to look at precision and recall to understand whether the model is actually doing its job. [1]

## 6. Implementation

### Reading a confusion matrix step by step

**Step 1: Identify the positive class.** Decide what the model is trained to detect — that is the positive class. Everything else is the negative class. [1]

**Step 2: Build the table.** For every prediction the model made, compare the model's output to the ground truth — the actual correct label. Increment the count in the matching cell: [1]
- Model said positive, ground truth positive → TP
- Model said positive, ground truth negative → FP
- Model said negative, ground truth positive → FN
- Model said negative, ground truth negative → TN

**Step 3: Verify the total.** TP + FP + FN + TN should equal the total number of predictions. [1]

**Step 4: Read the metrics you care about.**
- Top-row sum (TP + FP) = total flags raised by the model.
- Left-column sum (TP + FN) = total genuinely positive items in the test set (ground truth positives).
- Diagonal sum (TP + TN) = total correct predictions.
- Compute precision, recall, or accuracy from the relevant cells. [1]

**Step 5: Look at the off-diagonal cells.** FP and FN are where the failures are. Large FP means many false alarms. Large FN means many misses. The context of the task tells you which failure is more costly. [1]

### Worked example

An email spam filter is tested on 200 emails. 40 are genuine spam (ground truth: positive class); 160 are legitimate (ground truth: negative class). [1]

The filter's results:

- Correctly flagged spam: 30 (TP = 30)
- Legitimate email wrongly flagged: 8 (FP = 8)
- Spam that slipped through: 10 (FN = 10)
- Legitimate email correctly cleared: 152 (TN = 152)

Confusion matrix:

```
                        ACTUAL: Spam        ACTUAL: Legitimate
PREDICTED: Spam         TP = 30             FP = 8
PREDICTED: Not spam     FN = 10             TN = 152
```

- Accuracy = (30 + 152) / 200 = 182 / 200 = **91%** [1]
- Precision = 30 / (30 + 8) = 30 / 38 ≈ **79%** [1]
- Recall = 30 / (30 + 10) = 30 / 40 = **75%** [1]

The matrix shows 10 spam emails slipping through (FN) and 8 legitimate emails wrongly blocked (FP). Whether the 91% accuracy headline is good depends entirely on how much those 10 misses and 8 false alarms matter to users. [1]

## 7. Real-World Patterns

**Medical screening.** Confusion matrices are standard reporting for diagnostic models in healthcare. Regulators and clinicians expect to see all four cells, not just accuracy. A cancer-screening model's TP and FN counts directly translate to detected and missed cancers — the stakes are immediate. [1]

**Fraud detection.** Banks building fraud classifiers use the confusion matrix to assess both false alarms (FP: legitimate transactions blocked, causing customer friction) and misses (FN: real fraud approved, causing financial loss). The two failure types have different costs, and the matrix separates them clearly. [1]

**Spam and content filtering.** Email providers adjust how cautious the model is set to be — requiring more or less confidence before it flags an item — using precision and recall read directly off the confusion matrix. Making the model more cautious reduces FP but increases FN. Making it less cautious does the opposite. The matrix makes this trade-off visible. [1]

**AI confidence in the lab setting.** In this week's lab exercise — running yes/no questions at different temperatures — you can build a small confusion matrix. For each question, treat the correct answer as the positive class. Count TP, FP, FN, TN across your 10 runs. You will see that accuracy at temperature 0 may look clean, but the confusion matrix shows whether any particular answer type is systematically missed. [1]

## 8. Best Practices

**Do: report all four cells, not just accuracy.** A headline accuracy figure is incomplete. The confusion matrix shows which failure mode is driving inaccuracy — or concealing it. Anyone evaluating a classification model should ask for the full matrix. [1]

**Do: check whether a large TN is inflating accuracy.** When your dataset has many more items in the negative class than in the positive class, compute recall before trusting accuracy. A large TN with a small TP is the signature of the accuracy paradox. [1]

**Do: identify which failure costs more before reading the matrix.** In the context of the task, ask: is a false positive (false alarm) more costly, or is a false negative (a miss) more costly? That answer tells you which off-diagonal cell to prioritise minimising.

**Don't: optimise a single metric in isolation.** Precision, recall, and accuracy all read from the same underlying confusion matrix. Gaming one in isolation (for example, always predicting positive to maximise recall) produces pathological results visible immediately in the other cells. [1]

**Don't: confuse FP and FN.** These are opposite errors with different costs. A false positive is a false alarm — the model flagged something it should not have. A false negative is a miss — the model failed to flag something real. Mixing them up leads to solving the wrong problem.

## 9. Hands-On Exercise

Using the yes/no task from this week's lab (5 questions, run 10 times at temperature 0 and 10 times at temperature 1):

1. Pick one question where the correct answer is "yes" — treat "yes" as the positive class label and "no" as the negative class label.
2. Across all 10 runs at temperature 0, count TP (model said yes, ground truth was yes), FP (model said yes, ground truth was no), FN (model said no, ground truth was yes), TN (model said no, ground truth was no).
3. Build the 2×2 confusion matrix and fill in all four cells.
4. Compute accuracy, precision, and recall from the matrix.
5. Repeat for temperature 1. Compare the two matrices side by side. Does the distribution across the four cells change? Does that match your intuition from topics 7.5 and 7.7?

## 10. Key Takeaways

- A confusion matrix is a 2×2 table that records every prediction a model made, split into four outcome types: true positive (TP), false positive (FP), false negative (FN), and true negative (TN). [1]
- The positive class is what the model is trained to detect; the negative class is everything else. Ground truth is the actual correct label each item carries — what the model's prediction is compared against.
- True negative (TN) is the correct non-flag: the model predicted negative, and the item genuinely was negative (ground truth: negative). It is a good outcome, but a large TN in an imbalanced dataset inflates accuracy and can hide poor performance on the positive class. [1]
- Accuracy is computed from all four cells: (TP + TN) / total. When TN dominates, a model that catches nothing in the positive class can still score 95% accuracy — the accuracy paradox. [1]
- Precision reads from the top row of the confusion matrix: TP / (TP + FP). Recall reads from the left column: TP / (TP + FN). The matrix is the common foundation for both. [1]
- The off-diagonal cells — FP and FN — are the failure modes. The confusion matrix keeps them visible so no single headline number can hide them. [1]

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
