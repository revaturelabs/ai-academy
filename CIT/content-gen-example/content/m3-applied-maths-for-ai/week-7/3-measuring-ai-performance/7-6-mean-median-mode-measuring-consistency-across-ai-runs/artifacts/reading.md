<!-- nav:top:start -->
[⬅ Previous: 7.5 — Temperature](../../../2-how-llms-use-probability/7-5-temperature-low-picks-the-most-likely-token-high-introduces/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 7.7 — Accuracy ➡](../../7-7-accuracy-what-proportion-of-outputs-were-correct/artifacts/reading.md)
<!-- nav:top:end -->

---

# Mean, median, mode — measuring consistency across AI runs

## Overview

When you run the same prompt through an AI system multiple times, you rarely get identical results every time. The system is stochastic — its outputs vary because of how it samples from a probability distribution over possible tokens. That variability raises a practical question: across all those runs, what does the AI actually tend to do? Three simple mathematical tools — **mean**, **median**, and **mode** — give you a precise answer. Together they are called **measures of central tendency**, and they are the foundation of any honest consistency report on an AI system.

## Key Concepts

Think of mean, median, and mode as three different lenses on the same set of results. Each lens highlights something different. Using only one gives you an incomplete picture; using all three tells the full story [1].

### Mean — the overall average

**Mean** is the sum of all values divided by the number of values. It gives you the overall performance level across every run.

- Example: an AI is tested 10 times on a yes/no question, scored 1 for correct and 0 for wrong. Scores: 1, 1, 0, 1, 1, 0, 1, 0, 1, 1. Sum = 7. Mean = 7 ÷ 10 = **0.7**, meaning 70% accuracy [1].
- **Why it matters:** mean captures every data point, so a small number of very high or very low scores will pull it up or down. This sensitivity to outliers is useful — but it can also mislead you if the AI occasionally produces a wildly different result.

### Median — the middle value

**Median** is the middle value when you sort all results from smallest to largest. If there is an even number of values, average the two middle ones.

- Same 10 scores sorted: 0, 0, 0, 1, 1, 1, 1, 1, 1, 1. The two middle values (positions 5 and 6) are both 1. Median = (1 + 1) ÷ 2 = **1** [1].
- **Why it matters:** median is much less affected by outliers than mean. It answers the question "what does the AI usually do, ignoring flukes?" [2]. If a deterministic system at temperature 0 occasionally glitches into a very low score, the median stays stable while the mean dips.

### Mode — the most common answer

**Mode** is the value (or label) that appears most often. Unlike mean and median, mode works on text categories, not just numbers.

- Example (text labels): across 10 runs, the AI says "Yes" 6 times, "No" 3 times, "Partially" 1 time. Mode = **"Yes"** [1].
- **Why it matters:** mode answers "what does this AI say most often?" It is the only measure you can apply to non-numerical outputs — category labels, yes/no answers, tone classifications, and so on [2][3].

### How temperature affects all three

Recall from earlier topics that **temperature** controls how flat or sharp the probability distribution is over possible tokens. A low temperature (close to 0) makes the AI nearly deterministic — it picks the highest-probability token almost every time. A high temperature (close to 1) makes it sample more freely, producing greater variety.

That shift shows up directly in the three measures:

| Measure | Temperature near 0 | Temperature near 1 |
|---|---|---|
| Mean | High and stable across runs | More variable run to run |
| Median | Close to the mean | May differ noticeably from mean |
| Mode | Strong — one answer dominates | Weak or absent — no clear winner |

A strong mode at low temperature tells you the AI is near-deterministic on that prompt. A disappearing mode at high temperature tells you the outputs are scattered — the AI is exploring the full distribution [1][2].

### When to use which measure

| Question you are asking | Best measure |
|---|---|
| What is the overall accuracy rate? | Mean |
| What does the AI typically do, ignoring extreme results? | Median |
| What answer does the AI produce most often? | Mode |
| Is the AI consistent or scattered? | All three — compare them |

Using only one measure can mislead you. A high mean can hide a single run that skewed the average upward. A stable median can hide the fact that there is no dominant answer at all [2][3].

## Worked Example

Suppose an AI rates the quality of a paragraph on a 1–5 scale, and you run the same paragraph through it 10 times. The scores are:

**4, 5, 4, 4, 5, 4, 3, 4, 4, 5**

Here is how to compute all three measures step by step.

**Step 1 — Mean**
1. Add all scores: 4 + 5 + 4 + 4 + 5 + 4 + 3 + 4 + 4 + 5 = 42
2. Divide by the count: 42 ÷ 10 = **4.2 out of 5** (84% accuracy)

**Step 2 — Median**
1. Sort the scores: 3, 4, 4, 4, 4, 4, 4, 5, 5, 5
2. Even number of values — average the two middle ones (positions 5 and 6): (4 + 4) ÷ 2 = **4 out of 5** (80%)

**Step 3 — Mode**
1. Count each value: 3 appears once, 4 appears six times, 5 appears three times
2. The most frequent value is **4 out of 5**

**Step 4 — Interpret**

All three measures cluster tightly: mean ≈ 4.2, median = 4, mode = 4. This is a sign of a consistent AI — the runs are not wildly scattered, no outliers are pulling the mean away from the median. If instead the mean were 4.2 but the median were 2, you would know that a few high scores are inflating the average and the typical result is actually much lower [1][3].

## In Practice

Teams that test AI systems for quality use these three measures regularly. Here is how they apply in real situations:

- **Setting a quality standard:** a development team runs a prompt 20 times and reports the mean accuracy. If the mean falls below a target (say, 80%), the prompt or the system needs revision [2].
- **Detecting temperature sensitivity:** if the mode is strong at temperature 0 but disappears at temperature 1, the AI's output is highly sensitive to sampling settings — a flag worth noting before deploying [1].
- **Writing a complete evaluation report:** reporting only the mean is a common shortcut that hides problems. A complete report includes mean, median, and mode so readers can see whether the average is being skewed by unusual cases [2][3].

**Do:**
- Run at least 10 trials before drawing conclusions — a single run tells you nothing about consistency.
- Report all three measures together.
- Use mode when your outputs are text labels or categories; use mean and median when outputs are numbers.
- Note the temperature setting alongside your results.

**Do not:**
- Report only the mean and call it done.
- Compute a mean or median on text labels — those operations are meaningless on non-numbers.
- Assume a high mean means the AI is consistent — it might just have a few excellent runs hiding many poor ones.

## Key Takeaways

- **Mean** = the sum of all values divided by the count. Sensitive to outliers; best for overall accuracy rate.
- **Median** = the middle value when sorted. Outlier-robust; best for "what does the AI typically do?"
- **Mode** = the most frequent value or label. Works on text categories; best for "what does the AI say most often?"
- All three together reveal consistency more honestly than any one alone — compare them to spot outliers, skew, and scattered behaviour.
- Temperature near 0 produces a strong mode and mean close to median; temperature near 1 weakens the mode and can open a gap between mean and median.

## References

1. Khan Academy, "Mean, median, and mode review." <https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/a/mean-median-and-mode-review>
2. Laerd Statistics, "Measures of Central Tendency." <https://statistics.laerd.com/statistical-guides/measures-central-tendency-mean-mode-median.php>
3. Statistics How To, "Mean, Median, Mode." <https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/mean-median-mode/>

---
<!-- nav:bottom:start -->
[⬅ Previous: 7.5 — Temperature](../../../2-how-llms-use-probability/7-5-temperature-low-picks-the-most-likely-token-high-introduces/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 7.7 — Accuracy ➡](../../7-7-accuracy-what-proportion-of-outputs-were-correct/artifacts/reading.md)
<!-- nav:bottom:end -->
