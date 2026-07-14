---
topic_id: "7.6"
title: "Mean, median, mode — measuring consistency across AI runs"
position_in_module: 1
generated_at: "2026-06-23T00:00:00Z"
resource_count: 3
---

# 1. Mean, Median, Mode — Measuring Consistency Across AI Runs — Topic Corpus

## 2. Prerequisites

This topic builds on concepts from earlier in Week 7:

- **7.4** — Why LLMs output a probability distribution, not a single fixed answer (stochastic system, sampling, temperature)
- **7.5** — Temperature — low picks the most likely token, high introduces variation (sharp distribution, flat distribution, reliability vs variety trade-off)

You should be comfortable with the idea that an AI can give different answers to the same question depending on its temperature setting before continuing here.

## 3. Learning Objectives

By the end of this topic, you will be able to:

- Define mean, median, and mode in plain language and calculate each from a small set of numbers.
- Explain what each measure tells you about a set of AI outputs collected across multiple runs.
- Choose the right measure (mean, median, or mode) for a given consistency question about AI behaviour.
- Describe how temperature affects the mean, median, and mode of a set of AI responses.
- Identify when a single measure is misleading and why using all three together gives a fuller picture.

## 4. Introduction

Imagine you ask an AI assistant the same yes/no question ten times in a row. Sometimes it says "Yes." Sometimes it says "No." Occasionally it says "I'm not sure." You now have ten answers — but what do you actually know about this AI's behaviour?

Answering that question is the job of **descriptive statistics**. Descriptive statistics are simple mathematical tools that summarise a group of numbers (or responses) into a few key facts. You do not need to study every single answer individually; instead, you compute one or two summary numbers and those numbers tell the story.

In this topic, you will learn three of the most important summary tools: **mean**, **median**, and **mode**. These three are often called **measures of central tendency** — they each describe, in a slightly different way, what a "typical" result looks like across a collection of results. You will then see how to use them to measure how consistent an AI system is across multiple runs of the same prompt [1][2].

Why does this matter right now? You already know from topics 7.4 and 7.5 that AI models are **stochastic systems** — they do not always produce the same output for the same input. Measuring that variation is the first step toward trusting (or not trusting) an AI for a particular job.

## 5. Core Concepts

### 5.1 What is the mean?

**Mean** — the average of a group of numbers, found by adding them all up and dividing by how many there are.

Example: Suppose you ask an AI a factual question ten times and score each answer as 1 (correct) or 0 (wrong). Your scores are:

```
1, 1, 0, 1, 1, 0, 1, 0, 1, 1
```

Add them up: 1+1+0+1+1+0+1+0+1+1 = **7**
Divide by the count: 7 ÷ 10 = **0.7**

The mean score is 0.7, which you can also read as 70%. That is the AI's accuracy rate across ten runs [1].

**What the mean tells you about AI consistency:** The mean summarises the overall level of performance. A mean accuracy of 0.9 (90%) means the AI was right most of the time. A mean of 0.5 means it was right about as often as a coin flip. The mean is your first number to look at when evaluating reliability [2].

**One caution about the mean:** The mean is sensitive to extreme values (called **outliers** — single results that are very different from the rest). If nine answers score 1 and one answer scores 0, the mean is 0.9 — which feels right. But if nine answers score 0 and one unusual run scores 10 (imagine a scoring system where partial credit goes up to 10), the mean could be inflated by that one exceptional run. When you suspect outliers, also check the median [2].

### 5.2 What is the median?

**Median** — the middle value when you sort all the results from smallest to largest.

Using the same ten scores (1, 1, 0, 1, 1, 0, 1, 0, 1, 1), sort them:

```
0, 0, 0, 1, 1, 1, 1, 1, 1, 1
```

With ten values (an even count), there is no single middle item. Take the two middle values — position 5 and position 6 — which are both 1. The median is (1+1) ÷ 2 = **1**.

That result tells you that for more than half of the runs, the AI got the answer right [1].

**Odd vs even counts:** When you have an odd number of results, the median is simply the single middle value after sorting. For example, five scores of 0, 0, 1, 1, 1 have a median of 1 (the third value).

**What the median tells you about AI consistency:** The median is less influenced by outliers than the mean. If one run produced a wildly wrong answer and all others were correct, the median would still be 1 (correct), reflecting what the AI does in the typical case. This makes the median useful when you want to know: "What does the AI usually do, ignoring the occasional fluke?" [2]

### 5.3 What is the mode?

**Mode** — the value (or answer) that appears most often in your results.

Example with text responses: You ask an AI "Is this sentence grammatically correct?" ten times and get:

| Response | Count |
|---|---|
| "Yes" | 6 |
| "No" | 3 |
| "Partially" | 1 |

The mode is **"Yes"** — it appeared six out of ten times [1].

**What the mode tells you about AI consistency:** The mode is particularly useful when your results are not numbers but **categories** — like text labels, yes/no answers, or classification labels. The mean and median only work cleanly with numbers, but the mode works with anything you can count [2][3].

The mode answers the question: "What does this AI say most often?" That is a natural consistency question. If the mode is "Yes" and it appears 9 out of 10 times, you can be fairly confident the AI will say "Yes" next time. If the mode appears only 3 out of 10 times and three other responses each appear 2–3 times, there is no strong mode — that is a signal of high inconsistency.

**When there is no clear mode:** If every response appears the same number of times, the data has no mode. If two responses tie for most common, there are two modes. Neither situation is an error — it is information. No clear mode means the AI's outputs are scattered, which is itself a finding [3].

### 5.4 Putting all three together: a worked example

Suppose you run a yes/no factual quiz with five questions, ten times each (temperature 0), and score each run out of 5. Your ten run scores are:

```
4, 5, 4, 4, 5, 4, 3, 4, 4, 5
```

**Step 1 — Mean:**
Add: 4+5+4+4+5+4+3+4+4+5 = 42
Divide: 42 ÷ 10 = **4.2 out of 5** (84%)

**Step 2 — Median:**
Sort: 3, 4, 4, 4, 4, 4, 4, 5, 5, 5
Middle two values (positions 5 and 6): both are 4.
Median = (4+4) ÷ 2 = **4 out of 5** (80%)

**Step 3 — Mode:**
Count: 3 appears once, 4 appears six times, 5 appears three times.
Mode = **4 out of 5**

**Reading the three together:** Mean (4.2), median (4), and mode (4) are all close together. That cluster signals a consistent, reliable system — the AI reliably scores around 4 out of 5. If the mean were 4.2 but the median were 2, that gap would tell you a few very high scores are pulling the mean up, while most runs actually perform much worse [1][3].

### 5.5 How temperature changes the picture

You already know from topic 7.5 that **temperature** controls how varied the AI's outputs are:

- **Temperature 0** produces near-deterministic outputs — the model almost always picks the highest-probability token. Across ten runs, responses are nearly identical.
- **Temperature 1** produces varied outputs — the model samples from the full probability distribution and responses differ more from run to run.

Here is what that means for mean, median, and mode:

| Measure | Temperature 0 | Temperature 1 |
|---|---|---|
| Mean | High and stable — most runs score similarly | More variable — a few low-scoring runs can pull the mean down |
| Median | Very close to the mean — little spread | May differ noticeably from the mean if some runs are outliers |
| Mode | Strong — one answer dominates nearly all runs | Weak or absent — responses are spread across more options |

A **strong mode** (one answer appearing 8 or 9 times out of 10) at temperature 0 is a sign the AI is effectively behaving like a deterministic system for that particular prompt. A **weak or absent mode** at temperature 1 is expected — variation is built in by design [1][2].

### 5.6 Why these three measures, not just one?

Each measure shows you a different slice of the same data:

| Question you want to answer | Best measure to use |
|---|---|
| "What is the AI's overall accuracy rate?" | Mean |
| "What does the AI do in the typical case, ignoring flukes?" | Median |
| "What answer does the AI give most often?" | Mode |
| "Is the AI consistent or scattered?" | All three — compare them |

Using only one measure can mislead you. A high mean can hide a few catastrophic failures. A strong mode can hide the fact that the other 30% of runs are wildly inconsistent. Looking at all three together gives you a fuller, more honest picture of AI reliability [2][3].

## 6. Implementation

How to compute mean, median, and mode by hand for a small AI evaluation [1][2]:

1. **Collect your data.** Run the same prompt N times (e.g., 10 runs) and record a result for each run. This could be a score, a label, or a yes/no answer.

2. **Compute the mean** (for numerical data only) [1]:
   - Add all values together.
   - Divide by N (the number of runs).

3. **Compute the median** (for numerical data only) [1]:
   - Write all values in order from smallest to largest.
   - If N is odd: the median is the value at position (N+1) ÷ 2.
   - If N is even: the median is the average of the values at positions N÷2 and (N÷2)+1.

4. **Compute the mode** (works for numbers OR text labels) [1][3]:
   - Count how many times each value or response appears.
   - The mode is the value with the highest count.
   - If two values tie, there are two modes. If all values appear equally, there is no mode.

5. **Interpret by comparing** [2][3]:
   - Mean ≈ Median ≈ Mode → the AI is consistent; results cluster tightly.
   - Mean much higher than Median → a few very high scores are pulling the mean up; most runs score lower.
   - No clear Mode → responses are scattered; the AI is behaving unpredictably for this prompt.

## 7. Real-World Patterns

**Evaluating chatbot consistency:** Development teams routinely run the same test prompts dozens of times to generate statistics. They compute mean accuracy across runs to set a quality bar ("this model must average at least 85% on our benchmark") [2].

**Detecting temperature-sensitivity:** A model that shows a stable mode at temperature 0 but no clear mode at temperature 1 is highly temperature-sensitive. Teams use this comparison to decide which temperature setting is appropriate for a production task — customer support chatbots usually need temperature 0 or close to it, while creative writing tools benefit from temperature 1 [1].

**Red-teaming and worst-case analysis:** The median is used when teams want to characterise typical performance while being robust to adversarial outliers — one very unusual prompt should not make the overall system look better or worse than it actually is [2][3].

**A3 Lab Report context:** The lab activity for this week asks you to run the same prompt ten times at each temperature setting, tally unique responses, and measure variation. Reporting the mean accuracy, the median score, and the mode of responses is exactly what a short evaluation report requires — the three measures together tell the examiner that you understood consistency, not just the single best result.

## 8. Best Practices

**Do:**
- Run at least 10 trials before computing any of these measures. Fewer trials make the statistics unreliable — a single outlier can dominate.
- Report all three measures together when writing an AI evaluation. Each adds information the others miss.
- Match the measure to the data type: use mean and median for numerical scores; use mode for categorical responses (text labels, yes/no).
- Note the temperature used when reporting statistics — a mean of 90% at temperature 0 is very different from 90% at temperature 1.

**Avoid:**
- Reporting only the mean and calling it "accuracy." The mean alone hides how spread out the results are.
- Computing a mean or median on text labels (e.g., averaging "Yes" and "No" makes no sense). Use mode for text.
- Drawing conclusions from a single run. One correct answer does not make an AI reliable.
- Confusing a high mean with consistency. A mean of 0.8 could come from ten runs scoring 0.8 each (consistent) or five runs scoring 1.0 and five scoring 0.6 (inconsistent). The median and mode reveal the difference.

## 9. Hands-On Exercise

Run the same yes/no factual question five times at temperature 0 and five times at temperature 1 (ten runs total). Record whether the AI answered correctly (1) or incorrectly (0) each time.

1. Calculate the mean score separately for the temperature 0 group and the temperature 1 group.
2. Find the median for each group.
3. Identify the mode of the responses (consider using the raw text response, not just the score).
4. Write two sentences: What does the mean tell you? What does the mode tell you that the mean does not?

This is the foundation of the full lab activity for this week (Assessment A3).

## 10. Key Takeaways

- **Mean** is the average of all results. It gives the overall performance level but is sensitive to extreme values (outliers).
- **Median** is the middle value after sorting. It reflects typical performance and is more robust than the mean when outliers are present.
- **Mode** is the most frequent result. It is the only measure that works directly on text labels and category answers, making it essential for AI output analysis.
- All three measures together give a fuller picture of AI consistency than any one measure alone.
- Temperature affects all three: temperature 0 produces a strong mode and a mean close to the median; temperature 1 weakens the mode and introduces gaps between the mean and median.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
