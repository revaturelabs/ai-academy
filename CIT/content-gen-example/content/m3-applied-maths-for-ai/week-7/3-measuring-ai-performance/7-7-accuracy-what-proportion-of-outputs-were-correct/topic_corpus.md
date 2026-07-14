---
topic_id: "7.7"
title: "Accuracy — what proportion of outputs were correct"
position_in_module: 2
generated_at: "2026-06-23T00:00:00Z"
resource_count: 3
---

# 1. Accuracy — what proportion of outputs were correct — Topic Corpus

## 2. Prerequisites

- **7.1 — Probability basics, likelihood, events, outcomes:** this topic uses the idea of counting outcomes (correct vs incorrect) in the same way you counted favourable outcomes in a sample space.
- **7.6 — Mean, median, mode:** descriptive statistics vocabulary (counting, averaging) carries directly into accuracy as a summary measure.

## 3. Learning Objectives

By the end of this topic, learners will be able to:

- Define accuracy in plain English as the proportion of predictions that were correct.
- Apply the accuracy formula (correct predictions ÷ total predictions) to a small labelled dataset.
- Explain why a high accuracy score does not always mean a model is useful.
- Identify the types of AI tasks (classification tasks) where accuracy is a meaningful metric.
- Recognise that accuracy is one of several metrics and that precision and recall exist to fill gaps accuracy leaves behind (without defining them here).

## 4. Introduction

Imagine you ask an AI assistant ten yes-or-no questions: "Is this email spam?" or "Is this image a cat?". The AI answers all ten. At the end you check: how many did it get right? If it got seven correct and three wrong, it was right 70% of the time. That percentage — seven out of ten — is **accuracy** [1].

That single number is the most natural way to start measuring how well any AI model is doing. It is easy to explain, easy to compute, and easy to understand even if you have never written a line of code. It is the "gut check" metric: before diving into anything more specialised, accuracy tells you whether the model's answers are roughly landing in the right place.

This topic focuses exclusively on accuracy. Two other measures — precision and recall — address cases where accuracy alone is not enough. Those come in topics 7.8 and 7.9. For now, the goal is to understand what accuracy means, how to calculate it, and — crucially — when to trust it and when to be suspicious of it.

## 5. Core Concepts

### 5.1 What is a classification task?

Accuracy is most useful when an AI is doing a **classification task**: a task where the model must assign each input to one of a fixed set of categories [1]. Common examples:

- Deciding whether an email is **spam** or **not spam** (two categories).
- Recognising whether a photo contains a **cat**, a **dog**, or a **rabbit** (three categories).
- Predicting whether a customer review is **positive**, **neutral**, or **negative**.

In every case, the model picks one label from a list. A human expert (or a reliable automated process) checks each answer against the correct label. That checking process produces two raw counts:

- **Correct predictions** — the model's label matched the true label.
- **Incorrect predictions** — the model's label did not match the true label.

Everything in accuracy is built from those two numbers.

### 5.2 The accuracy formula

Accuracy is defined as [1][2]:

> **Accuracy = correct predictions ÷ total predictions**

Or, equivalently:

> **Accuracy = number of times the model was right ÷ total number of questions asked**

The result is a number between 0 and 1 (or 0% and 100% if you multiply by 100). An accuracy of 1.0 means the model was right every single time. An accuracy of 0.0 means it was wrong every single time.

**Worked example — spam filter:**

Suppose you have 100 emails. You already know the correct label for each one (this is called a **labelled dataset** or **test set**). You run a spam filter on all 100:

| What actually happened | How many |
|---|---|
| Real spam, correctly flagged as spam | 40 |
| Real spam, incorrectly passed through as "not spam" | 10 |
| Real "not spam", correctly passed through | 45 |
| Real "not spam", incorrectly flagged as spam | 5 |

Total correct = 40 + 45 = **85**
Total predictions = 100

Accuracy = 85 ÷ 100 = **0.85 (85%)** [1]

The filter got 85 out of 100 right. That is the accuracy. Nothing more complicated is needed to compute it.

### 5.3 Correct predictions and incorrect predictions — the two building blocks

When you compare a model's output to the known correct answer, every single prediction lands in one of two buckets:

- **Correct prediction (also called a "hit"):** The model said X, and the true answer was X.
- **Incorrect prediction (also called a "miss"):** The model said X, but the true answer was Y.

For a two-category task (like spam vs not-spam), incorrect predictions can happen in two ways — the model can miss a real case or raise a false alarm — but accuracy treats all misses equally. It just counts them all as wrong and moves on [2].

This "lumping all misses together" is what makes accuracy so simple — and also what makes it incomplete in some situations, as you will see in 5.4 below.

### 5.4 When accuracy is a useful metric

Accuracy works well when:

1. **The categories are roughly balanced.** If about half your emails are spam and half are not, a model that gets 90% accuracy has genuinely learned something useful [1][2].

2. **All mistakes are roughly equally bad.** In a low-stakes quiz app, getting a question wrong is about as bad as getting another one wrong — no mistake is dramatically worse than any other.

3. **You need a quick, readable summary number.** Accuracy is the one metric almost everyone immediately understands. For a first pass at "is this model any good?", it is hard to beat.

### 5.5 When accuracy can be misleading — the high-accuracy failure case

This is the most important idea in this topic, and it takes one example to see clearly.

**The broken spam filter problem [2][3]:**

Suppose only 5 out of every 100 emails in your inbox are actually spam (the rest are legitimate). You build the laziest possible filter: it marks every single email as "not spam" without looking at anything. What is its accuracy?

- Correct predictions: 95 (all the legitimate emails it correctly left alone)
- Incorrect predictions: 5 (all the spam it missed)
- Accuracy = 95 ÷ 100 = **95%**

A 95% accuracy score — and the filter does absolutely nothing useful. Every piece of spam sails straight through.

This happens because the two categories are **imbalanced**: one category (not spam) makes up 95% of the data, so a model that always guesses the dominant category will score 95% without ever catching any spam.

This is the fundamental limitation of accuracy: when one category vastly outnumbers the other, a high accuracy number can hide a completely broken model [1][2][3].

**The practical takeaway:** When you see a high accuracy number, the first question to ask is: "What would I get if I just guessed the most common category every time?" If the answer is close to the reported accuracy, the metric is not very informative.

### 5.6 Accuracy in the context of AI outputs you have seen this week

In topic 7.4 you saw that an LLM outputs a probability distribution over its vocabulary and samples a token from it. In topic 7.5 you saw that temperature controls how peaked or flat that distribution is. Accuracy enters the picture when you evaluate the results of that process.

In the lab activity this week [lab seed], you run the same five yes/no questions ten times each. To measure accuracy, you would:

1. Decide, in advance, what the correct answer to each question is.
2. Run the AI ten times per question.
3. Count how many times it gave the correct answer.
4. Divide by the total number of attempts (10 questions × 10 runs = 100 attempts).

That calculation — correct answers ÷ total attempts — is accuracy [1].

At temperature 0, the model always picks the highest-probability token (topic 7.5), so you would expect high consistency. At temperature 1, answers vary. Accuracy measures whether that variation drifts away from the correct answer, not just whether the answers vary.

### 5.7 Accuracy vs other metrics — naming precision and recall (without teaching them)

Accuracy is the starting point, not the finish line. Two metrics that address the gaps accuracy leaves are precision (topic 7.8) and recall (topic 7.9). Do not worry about their definitions now; just know that when accuracy is misleading — as in the broken spam filter example — those two metrics restore meaningful measurement [2][3].

## 6. Implementation

**Step-by-step: computing accuracy by hand on a small test set**

This procedure works for any two-category classification task with a small labelled dataset.

1. **Collect your test set.** You need inputs (e.g., emails, images, questions) where you already know the correct label for each one. This is the "ground truth".

2. **Run the model on every item.** Record the model's output label for each input. Do not adjust or cherry-pick.

3. **Compare model output to ground truth, item by item.** For each item, mark it C (correct) if they match, or W (wrong) if they do not.

4. **Count C and W.** Let C = number of correct predictions, W = number of wrong predictions. Total = C + W.

5. **Apply the formula.** Accuracy = C ÷ (C + W).

6. **Sanity check: what would a "dummy" model score?** Count how many items belong to the most common category. Divide by total. If your model's accuracy is not meaningfully higher than this baseline, the score is not telling you much.

**Example trace (five-question yes/no task, 10 runs each):**

```
Question 1: correct answer = YES
  Run results: YES YES YES NO YES YES YES YES YES YES
  Correct count: 9   Wrong count: 1

Question 2: correct answer = NO
  Run results: NO NO NO NO NO YES NO NO NO NO
  Correct count: 9   Wrong count: 1

(... and so on for questions 3–5)

Total correct across all runs: 44
Total attempts: 50

Accuracy = 44 ÷ 50 = 0.88 (88%)
```

## 7. Real-World Patterns

**Email spam filters** are the canonical accuracy example [2][3]. Providers measure accuracy across millions of messages. However, because spam volume is a small fraction of total email, engineers almost always supplement accuracy with additional metrics — exactly the situation from section 5.5.

**Medical screening tests** are the domain where accuracy limitations become highest-stakes. A test that screens for a rare disease affecting 1 in 1,000 people will score 99.9% accuracy by labelling everyone as disease-free. No one would call that a good test. This is why real-world medical AI evaluation never reports accuracy alone [2].

**AI quiz or tutoring systems** are a setting where accuracy is more trustworthy. If a system grades student answers as correct or incorrect, and the distribution of correct vs incorrect answers is roughly 50/50, accuracy gives a fair picture of grading quality.

**The pattern:** accuracy is most trustworthy when both categories appear with roughly similar frequency. It becomes deceptive when one category dominates.

## 8. Best Practices

**Do:**
- Always compute the "dummy baseline" (what score would you get by always predicting the most common category?) before trusting an accuracy number.
- Report accuracy alongside the size of your test set. Accuracy of 90% on 10 examples is far less reliable than 90% on 1,000 examples.
- State clearly which categories you are measuring. "90% accuracy" is ambiguous; "90% accuracy on a 50/50 spam / not-spam test set of 200 emails" is precise.

**Do not:**
- Treat accuracy as the only metric when category sizes are very different. In imbalanced datasets, accuracy can be actively misleading.
- Measure accuracy on the same data the model was trained on. That is like grading yourself on the exam questions you already saw — it overstates real performance.
- Report accuracy to many decimal places as if it were exact. A difference of 0.1% on a 100-item test set is meaningless noise.

## 9. Hands-On Exercise

In the lab this week, after running the same prompt 10 times at temperature 0 and 10 times at temperature 1:

1. Pick five of the yes/no questions from your run. Decide the correct answer for each before you look at the outputs.
2. For each temperature setting separately, count how many outputs matched the correct answer.
3. Compute accuracy for temperature 0 and accuracy for temperature 1 using the formula: correct ÷ total.
4. Compare the two numbers. Does lower temperature reliably produce higher accuracy, or does it depend on the question?

Write two sentences interpreting what the accuracy difference (if any) tells you about how useful temperature 0 vs temperature 1 is for factual yes/no tasks.

## 10. Key Takeaways

- **Accuracy = correct predictions ÷ total predictions.** It is the simplest summary of how often a model gets things right.
- **Accuracy is most meaningful when categories are balanced.** When one category is much more common than the other, a high accuracy score can hide a model that is essentially useless.
- **The "dummy baseline" is a quick sanity check.** If your model's accuracy is not much better than "always guess the most common answer", the number is not informative.
- **Accuracy measures outcomes, not confidence.** A model can be very confident and very wrong. Accuracy only scores the final answer against the correct label.
- **Precision and recall exist because accuracy is incomplete.** When accuracy misleads, those two metrics (topics 7.8 and 7.9) fill the gaps — but you do not need them yet.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._

---

**Quiz builder guidance (section 11 addendum):**

Recurring length bias: correct-answer options tend to attract explanatory prose while distractors are left short. For this topic, trim correct-answer stems to the same word count as their distractors before generation. All four options for each question should be roughly the same length. Key concepts to test: the accuracy formula, the dummy-baseline insight, the imbalanced-dataset failure case, and the difference between accuracy and the named-but-deferred precision/recall. Do not write quiz items that require the learner to define precision or recall — those are tested in 7.8 and 7.9.
