---
topic_id: 8.4
title: F1 score — balancing precision and recall into one metric
position_in_module: 2
generated_at: 2026-06-22T08:00:00Z
resource_count: 3
---

# 1. F1 score — balancing precision and recall into one metric — Topic Corpus

## 2. Prerequisites

This topic builds directly on **8.3 (Precision vs recall trade-off)**. From there you already know:

- **Precision** — of the cases the model flagged "yes," how many were actually right (few false alarms).
- **Recall** — of the cases that were truly "yes," how many the model caught (few misses).
- That there is a **trade-off** between them: pushing one up (by sliding the model's threshold) usually pushes the other down.
- That which one matters more depends on the **cost of each error** — a miss versus a false alarm.

You do not need to re-learn any of these. This topic takes those two numbers and asks: *can we fairly squeeze them into one?*

## 3. Learning Objectives

After this topic you will be able to:

- Explain the problem the **F1 score** solves: turning two separate numbers (precision and recall) into one.
- Describe what the F1 score is in plain words — a single balance score from 0 to 1.
- Explain why F1 uses a **harmonic mean** rather than a plain average, and what that buys you.
- State why a high F1 requires **both** precision and recall to be decent — neither can hide behind the other.
- Decide when to report one F1 number and when to report precision and recall separately.

## 4. Introduction

Picture two job candidates for a "spam catcher" role. The first catches almost every spam email but also dumps a lot of real mail in the junk folder. The second never touches a real email but lets half the spam through. Which one is better? You honestly cannot say — each is great at one half of the job and poor at the other.

This is the everyday headache from the last topic. Precision and recall are **two** numbers, and a model can look fantastic on one while quietly failing the other. Comparing models, or just answering "is this model good?", gets awkward when you have to juggle a pair of scores every time.

The **F1 score** is the fix. It combines precision and recall into **one** number between 0 and 1, built so a model only scores high when it is good at *both* halves of the job. This topic explains what that single number means and — the interesting part — why it is calculated in a slightly unusual way that refuses to be fooled by a model that is lopsided [1][2].

## 5. Core Concepts

### The problem: two numbers are hard to compare

From 8.3 you can measure a yes/no model with precision and recall. That is honest, but it is also clumsy in one common situation: when you simply want to rank models or give a quick verdict.

- Suppose Model A has precision 0.9 and recall 0.5.
- Model B has precision 0.6 and recall 0.7.
- Which is better? With two numbers, there is no obvious answer — you are comparing apples to oranges twice over [1].

What you want is a **single summary score** so you can say "this model scores 0.71, that one scores 0.65, pick the first." That single score is what the F1 score gives you [1].

### What the F1 score is

**F1 score** — one number, from 0 to 1, that summarizes how well a model balances precision and recall at the same time [1][3].

- A score near **1** means both precision and recall are high — the model rarely raises false alarms *and* rarely misses real cases.
- A score near **0** means at least one of them is poor.
- It is sometimes just called the **F1**, or the **F-score** (the "1" marks a specific, balanced version of it) [3].

The whole point of F1 is captured in one rule: **you can only get a high F1 if both precision and recall are decent.** Being brilliant at one cannot rescue a model that is weak at the other. The next section explains how the math enforces that.

### Why not just average them?

The obvious way to merge two numbers is the plain average (the **arithmetic mean**) — add them and divide by two. F1 does *not* do this, and the reason is the heart of the topic.

Watch what a plain average does to a lopsided model:

- A model with precision **1.0** and recall **0.0** (it flags one thing, gets it right, and misses everything else) is useless. Yet its plain average is (1.0 + 0.0) ÷ 2 = **0.5**. A middling-looking score for a worthless model.

The plain average lets one strong number **hide** a disastrous weak one. That is exactly the failure F1 is designed to prevent [1][3].

### The harmonic mean: pulled toward the lower number

F1 instead uses a different kind of average called the **harmonic mean**.

**Harmonic mean** — a way of averaging two numbers that sits much closer to the *smaller* of the two than a plain average does [3].

You do not need to derive it. You only need the intuition:

- A plain average sits exactly halfway between the two numbers.
- A harmonic mean leans hard toward the **lower** number — it gets "dragged down" by whichever score is worst.

Run the lopsided model through it. Precision 1.0, recall 0.0:

- Plain average: **0.5** (looks okay — misleading).
- Harmonic mean: **0** (correctly says: useless).

And when both numbers are healthy and close together — say precision 0.8 and recall 0.8 — the harmonic mean is also 0.8, almost the same as a plain average. So the harmonic mean only "punishes" you when the two numbers are far apart. When they are balanced, it behaves normally [3].

That is the single idea to keep: **the harmonic mean rewards balance and penalizes imbalance.** A high F1 means *both* precision and recall are high, because the moment one drops, the harmonic mean drops with it.

### The formula, in words

Stated once, the F1 score is:

> **F1 = 2 × (precision × recall) ÷ (precision + recall)**

In plain language: multiply the two scores together, double it, and divide by their sum. You will not be asked to compute this by hand here — that practice comes in 8.5. What matters now is reading what the formula *does*:

- If **either** precision or recall is **0**, the top of the fraction (the multiply) becomes 0, so the whole F1 is **0**. One zero kills the score. A plain average could never do that.
- If **both** are **1.0**, the formula gives **1.0** — a perfect balanced score.
- If the two are unequal, the result is dragged toward the smaller one. That dragging is the harmonic mean at work [1][3].

### A worked intuition (no arithmetic to memorize)

Go back to the two models from the start of this section:

| Model | Precision | Recall | Plain average | F1 (harmonic) |
|---|---|---|---|---|
| A | 0.9 | 0.5 | 0.70 | 0.64 |
| B | 0.6 | 0.7 | 0.65 | 0.65 |

Notice what happened. By a plain average, Model A (0.70) looks clearly better than Model B (0.65). But F1 rates them almost equal, even nudging B ahead. Why? Because Model A's weaker recall (0.5) drags its F1 down, while Model B is more *balanced*, so it keeps more of its score. F1 quietly rewards the model that is not lopsided [1].

### When to report F1, and when to report precision and recall separately

F1 is a convenience, not a replacement. Knowing when to use which is part of the skill.

| Use F1 (one number) when... | Report precision and recall separately when... |
|---|---|
| You need to **rank or compare** many models quickly | You **care more about one error type** (recall-first or precision-first, as in 8.3) |
| You want a **single headline number** for a report or leaderboard | You need to **explain** to a stakeholder *which* mistakes the model makes |
| You believe a **false alarm and a miss matter about equally** | The **cost of a miss and a false alarm are very different** |

The key caution: F1 treats precision and recall as **equally important**. If your situation says a miss is far worse than a false alarm (recall-first, like cancer screening from 8.3), then a single balanced F1 can hide the very thing you care about most. In that case, look at precision and recall directly [1][2].

So: reach for F1 when you want a quick, fair, single-number verdict; fall back to the two separate numbers the moment one error type matters more than the other.

## 7. Real-World Patterns

The F1 score shows up wherever people compare models at a glance [1][2].

- **Model leaderboards and competitions.** When dozens of models are ranked on a yes/no task, a single F1 column lets you sort them top to bottom. Two columns would make ranking ambiguous.
- **Quick project check-ins.** "Our spam classifier is at F1 = 0.88" is a clean, one-line health report for a team standup — far tidier than quoting two shifting numbers.
- **Imbalanced tasks.** When the "yes" cases are rare (most emails are *not* fraud), plain accuracy — another metric you will meet in 8.5 — can look great by ignoring the rare cases. F1 stays honest because it watches both precision and recall, which is why teams often prefer it on rare-event problems [1].

In all three, F1 earns its place by collapsing a two-number judgment into one without letting a lopsided model sneak through.

## 8. Best Practices

- **Do** use F1 when a false alarm and a miss cost roughly the same, and you want one number.
- **Do** remember a high F1 *guarantees* both precision and recall are decent — that is its whole value.
- **Don't** report F1 alone when one error type clearly matters more — show precision and recall too, as 8.3 taught.
- **Don't** confuse F1 with a plain average; the harmonic mean is the reason a lopsided model cannot fake a good score.
- **Don't** assume a single number tells the whole story — F1 is a summary, and summaries always drop detail.

## 10. Key Takeaways

- The **F1 score** packs precision and recall into **one** number from 0 to 1, so models can be compared at a glance.
- It uses the **harmonic mean**, which leans toward the **lower** of the two scores — so a high F1 demands that *both* precision and recall are decent.
- A **plain average** would let one strong score hide a weak one (precision 1.0, recall 0.0 averages to a deceptive 0.5); the harmonic mean gives that model a 0.
- The plain form is **F1 = 2 × (precision × recall) ÷ (precision + recall)** — if either input is 0, F1 is 0.
- Report **F1** for a quick single-number verdict; report **precision and recall separately** when one error type matters more than the other.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
