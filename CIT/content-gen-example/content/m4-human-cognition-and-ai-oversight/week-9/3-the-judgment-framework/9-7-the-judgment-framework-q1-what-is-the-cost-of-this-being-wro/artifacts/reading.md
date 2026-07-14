<!-- nav:top:start -->
[⬅ Previous: 9.6 — How human biases get encoded into AI training data](../../../2-cognitive-biases-and-ai/9-6-how-human-biases-get-encoded-into-ai-training-data/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 9.8 — The Judgment Framework ➡](../../9-8-the-judgment-framework-q2-can-i-verify-this-without-the-ai/artifacts/reading.md)
<!-- nav:top:end -->

---

# The Judgment Framework — Q1: What is the cost of this being wrong?

## Overview

When you accept an AI output and act on it, you are making a decision. Some decisions barely matter if the AI was wrong — you send an email with an awkward sentence and nobody is harmed. Others can cause serious harm if the AI was wrong — a nurse follows an incorrect drug dosage and a patient is put at risk. Q1 of the Judgment Framework asks you to stop and think about this difference *before* you act: **What is the cost of this being wrong?** Asking that question is what switches your thinking from automatic acceptance to deliberate judgment [1][2].

## Key Concepts

The **Judgment Framework** is a set of three questions you ask before acting on any AI output. This topic covers Q1 only. Q2 and Q3 are introduced in topics 9.8 and 9.9.

Q1 works by breaking "cost of being wrong" into three dimensions. You assess all three, then decide how much scrutiny the output deserves.

![Q1 triage flow: three dimensions (severity, probability, detectability) combine into a cost signal, leading to a high/low cost verdict with two outcomes](./diagram.png)
*Three dimensions — severity, probability, and detectability — combine into a single cost signal that determines how much scrutiny an AI output deserves.*

### Dimension 1: Severity

**Severity** — how bad the harm would be if the error actually occurs.

Think of severity as a spectrum. At one end: trivially reversible (you delete a wrong word and retype it). At the other end: catastrophic and irreversible (a patient receives the wrong medication). Before acting on any AI output, ask yourself: *What is the worst plausible consequence if this is wrong?* Be concrete — name the actual harm, not a vague "something bad."

### Dimension 2: Probability

**Probability** — how likely it is that this specific output is wrong in this specific situation.

Probability is not fixed for an AI system overall. It goes up when:
- The task is unusual or outside the AI's training data.
- The AI has been wrong on similar tasks before.
- The output cannot be explained or seems surprising.
- The situation is highly variable (many edge cases).

Probability goes down when:
- The task is narrow and well-documented.
- The AI's reliability on this task type is known and high.
- The output can be quickly checked against a reliable source.

### Dimension 3: Detectability

**Detectability** — how easily you (or someone else) would catch the error *before* harm occurs.

This dimension has three rough bands:
- **High detectability:** The error is obvious and surfaces quickly (e.g., a number that is clearly impossible).
- **Medium detectability:** The error is catchable if you look carefully (e.g., a clause in a contract that reads oddly).
- **Low detectability:** The error blends in and is only discovered after harm has already happened (e.g., a missed cancer flag in a radiology scan).

Low detectability amplifies the cost even when severity and probability are individually moderate [1].

### Combining the three dimensions

The relationship is directional, not a precise formula: **Decision consequence = Severity × Probability × (1 / Detectability)** [1]. In practice, this is a quick triage, not a calculation:

1. How bad if wrong? (severity)
2. How likely is it wrong here? (probability)
3. Would I know before harm hits? (detectability)

If all three point high — apply scrutiny before acting. If all three point low — you can move faster. The habit of asking all three is what matters [2].

## Worked Example

Here is a step-by-step Q1 walkthrough using a real scenario: a nurse using an AI clinical assistant that suggests a drug dosage.

**Step 1 — Identify the AI output.**
The AI has recommended a dosage of 400 mg for a patient.

**Step 2 — Assess severity.**
Worst plausible consequence: too high a dose causes an adverse reaction; too low a dose leaves the condition untreated. Both are serious. Severity: **high**.

**Step 3 — Assess probability.**
The patient has an unusual combination of conditions the AI may not have encountered in training. The recommendation has no cited source. Probability of error: **meaningful**.

**Step 4 — Assess detectability.**
If the dosage is wrong, there is no immediate visible signal — the nurse administers it, and the patient deteriorates hours later. No other clinician will double-check the AI's work before administration. Detectability: **low**.

**Step 5 — Decide on scrutiny.**
High severity + meaningful probability + low detectability = high cost of being wrong. The nurse must verify the dosage against the pharmacopeia and the prescribing physician's notes before acting. Q2 (topic 9.8) covers exactly how to verify.

**Step 6 — Document reasoning (in professional contexts).**
In a clinical setting, note that the AI recommendation was reviewed and cross-checked. This creates an audit trail and reinforces the habit of deliberate judgment [1][2].

Compare this to a low-cost situation: an AI suggests a subject line for a marketing email. Severity: low (a weak subject line is annoying, not harmful). Probability: moderate. Detectability: high (you re-read it yourself before sending). Cost of being wrong: low — you can move faster and spend scrutiny elsewhere.

## In Practice

Three real-world patterns show how Q1 plays out across different domains [1][2][3].

**Medical — Radiology AI (87% sensitivity)**
- Severity: high — a missed diagnosis causes delayed treatment.
- Probability: meaningful — a 13% miss rate, and demographic mismatches from historical training data (see topic 9.6) can raise it further.
- Detectability: low — a missed flag is an *absent* signal; nothing visibly alerts the radiologist.
- Verdict: the AI flag is a starting point, never a final word.

**Legal — Contract Review AI**
- Severity: medium-high — an overlooked clause can affect rights, finances, or liability.
- Detectability: medium — anchoring bias (topic 9.4) pulls your attention toward what the AI highlighted, making it easy to skip the clauses it did not flag.
- Verdict: an independent read of high-risk clauses is warranted even when the AI reports clean.

**Content Moderation AI (94% precision)**
- At millions of posts per day, 6% error = hundreds of thousands of wrong decisions daily.
- Detectability: low for false negatives (missed harmful content), medium for false positives (wrongly removed content).
- Verdict: individual high-stakes cases need human review regardless of what the AI flags [3].

**Do / Don't checklist**

| Do | Don't |
|---|---|
| Ask all three dimensions every time | Skip Q1 when time pressure is high — that is exactly when it matters most |
| Be concrete about worst-case harm | Keep severity vague ("something bad could happen") |
| Factor in who else will catch an error | Assume someone downstream will check |
| Recognise genuinely low-cost situations | Treat every AI output as equally risky |
| Document reasoning in high-stakes contexts | Act first and justify later |

Recognising low-cost situations is part of using Q1 well. The framework is not about distrust — it is about spending scrutiny where it counts. The habit of asking is what protects you in high-cost situations, where time pressure makes skipping tempting [2][3].

## Key Takeaways

- Q1 asks one question before you act on AI output: **How bad would it be if this is wrong?** It does so by weighing three dimensions — severity, probability, and detectability.
- The three dimensions work together. Low detectability amplifies cost even when severity and probability are moderate on their own.
- High-stakes domains — medical, legal, safety-critical engineering, financial decisions affecting others — almost always return a high cost of being wrong.
- Low-cost situations are real; recognising them lets you spend scrutiny where it matters instead of everywhere equally.
- The habit of asking Q1 is the protection. It is most needed exactly when time pressure conspires to make you skip it [2][3].

## References

1. AI Competence, "Risk-Aware Decision Framework for Complex AI Systems." <https://aicompetence.org/risk-aware-decision-framework-complex-ai-systems/>
2. Acharya et al., "Think First, Verify Always" (arXiv 2508.03714). <https://arxiv.org/pdf/2508.03714>
3. Corporate Finance Institute, "How AI Affects Decision Making." <https://corporatefinanceinstitute.com/resources/strategy/how-ai-affects-decision-making/>

---
<!-- nav:bottom:start -->
[⬅ Previous: 9.6 — How human biases get encoded into AI training data](../../../2-cognitive-biases-and-ai/9-6-how-human-biases-get-encoded-into-ai-training-data/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 9.8 — The Judgment Framework ➡](../../9-8-the-judgment-framework-q2-can-i-verify-this-without-the-ai/artifacts/reading.md)
<!-- nav:bottom:end -->
