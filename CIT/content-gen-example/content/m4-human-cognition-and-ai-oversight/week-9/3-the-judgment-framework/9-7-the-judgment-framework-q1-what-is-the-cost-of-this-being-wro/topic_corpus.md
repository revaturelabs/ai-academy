---
topic_id: "9.7"
title: "The Judgment Framework — Q1: What is the cost of this being wrong?"
position_in_module: 1
generated_at: "2026-06-13T00:00:00Z"
resource_count: 3
---

# 1. The Judgment Framework — Q1: What Is the Cost of This Being Wrong? — Topic Corpus

## 2. Prerequisites

This topic opens the Judgment Framework module. It builds directly on:

- **9.1 — System 1 Thinking**: fast, automatic processing; the brain's tendency to accept information without deliberate scrutiny
- **9.2 — System 2 Thinking**: slow, deliberate reasoning; when and why people engage careful thought
- **9.5 — Automation Bias**: the tendency to over-trust automated outputs without independent verification; calibrated trust; omission and commission errors
- **9.6 — How Human Biases Get Encoded into AI Training Data**: why AI outputs may inherit the biases of the data they were trained on

No programming or statistical background is assumed. This topic is about how a person thinks before acting on an AI recommendation — a reasoning skill, not a technical one.

---

## 3. Learning Objectives

By the end of this topic, learners will be able to:

1. State the first question of the Judgment Framework — "What is the cost of this being wrong?" — and explain what it is asking.
2. Define the three dimensions of error cost: severity, probability, and detectability.
3. Apply the three-dimension cost analysis to at least two real-world scenarios involving AI-assisted decisions.
4. Distinguish between low-cost and high-cost errors and explain why the distinction changes how much scrutiny an AI output deserves.
5. Name the other two Judgment Framework questions (covered in topics 9.8 and 9.9) and explain why Q1 must come first.

---

## 4. Introduction

You are using an AI writing assistant and it suggests rewording a sentence in your email. You accept the change without re-reading it. The worst that happens: the sentence is slightly awkward. A colleague notices. You fix it next time. Low cost.

Now imagine you are a nurse and an AI clinical-support tool suggests a drug dosage for a patient. You accept the recommendation without cross-checking it against the patient's weight and allergy record. If the suggestion is wrong, the patient could be harmed — seriously. That is a very different cost.

In both cases you did the same thing: you acted on an AI output without fully verifying it. But the consequences of being wrong were not the same. One cost is a minor embarrassment. The other could be life-changing.

This difference — the cost of being wrong — is what the first question of the Judgment Framework asks you to think about *before* you act on any AI recommendation. [1][2]

The Judgment Framework is a set of three questions. You will work through all three by the end of week 9. This topic covers Q1: **What is the cost of this being wrong?** It does not ask you to distrust AI. It asks you to be deliberate about *when* and *how much* trust is appropriate — before it is too late to change course. [2][3]

---

## 5. Core Concepts

### 5.1 The Judgment Framework — What It Is

The **Judgment Framework** is a structured set of three questions a person should ask before acting on an AI output. The framework gives you a mental pause button: it activates System 2 thinking (9.2) at the moment when System 1 (9.1) would otherwise accept the AI's output automatically.

The three questions are:

1. **Q1 — What is the cost of this being wrong?** *(this topic)*
2. Q2 — Can I verify this without the AI? *(topic 9.8)*
3. Q3 — Who is accountable if this fails? *(topic 9.9)*

You will cover Q2 and Q3 in their own topics. This topic focuses entirely on Q1.

Q1 comes first for a specific reason. Before you decide whether to verify an output (Q2) or think about accountability (Q3), you need to know whether the stakes are high enough to bother. If the cost of being wrong is negligible, you can move quickly. If the cost is serious, everything else — how hard you check, who you involve, how you document your decision — follows from that. [1][2]

### 5.2 What "Cost of Being Wrong" Actually Means

When you ask "what is the cost of this being wrong?" you are not simply asking "is this important?" You are asking a more specific question: **how bad would it be if the AI's output turned out to be incorrect, and how likely is that badness to materialise and go unnoticed?**

Researchers who study decision-making under risk break this down into three dimensions. [1]

#### Dimension 1 — Severity

**Severity** is how bad the harm would be *if* the error occurred. Think of it as the size of the damage.

Severity spans a spectrum:

| Severity level | What it means | Example in AI context |
|---|---|---|
| Very low | Trivially reversible, no lasting harm | AI suggests a slightly odd word choice in a casual message |
| Low | Noticeable but easily corrected | AI autocompletes a date field incorrectly; you catch it before submitting |
| Medium | Some cost to fix; real but bounded harm | AI mis-categorises a customer complaint; support team has to re-open a case |
| High | Significant harm; difficult or impossible to fully reverse | AI flags the wrong patient record; a clinician acts on it before checking |
| Critical | Catastrophic or irreversible | AI misjudges brake-failure risk in an autonomous vehicle; crash results |

Severity alone is not enough to assess cost. A critical-severity outcome that cannot possibly happen still costs nothing. That is why you also need probability.

#### Dimension 2 — Probability

**Probability** is the likelihood that this specific AI output is actually wrong in this specific situation.

Some factors that raise probability of error: [1][3]

- The task is outside the type of data the AI was trained on (recall from 9.6: AI learns from training data; tasks it has not seen reliably perform worse).
- The AI has given confident-sounding answers on similar questions before that turned out to be wrong.
- The output cannot be explained or traced — it is just a recommendation with no visible reasoning.
- The situation is high-variation: human lives, specific individuals, unusual circumstances.

Some factors that lower probability of error:

- The task is narrowly defined, repetitive, and well within the AI's documented capabilities.
- The AI's outputs in this category have been verified many times before and found reliable.
- The output can be independently checked quickly and cheaply.

A useful mental move: separate what the AI *says* from how confident you are that it is *right*. AI systems do not always signal uncertainty accurately. Overconfident outputs are common. [2][3]

#### Dimension 3 — Detectability

**Detectability** is how easily you or someone else would catch the error *before it causes harm*.

This is the dimension most people forget. An error that is severe and probable still has low real-world cost if it is caught before it matters. An error that is moderate in severity but completely invisible — no one would know until damage is done — has a much higher effective cost. [1]

Think of detectability in three bands:

- **High detectability**: the error would be obvious quickly — it is factually checkable, immediately visible, or triggers a known alert.
- **Medium detectability**: someone would likely catch it, but only if they were looking carefully and had background knowledge.
- **Low detectability**: the error blends in; no obvious flag; discovery might only happen after harm has occurred.

Low detectability dramatically raises the effective cost of an error, even when severity and probability are moderate on their own.

### 5.3 Combining the Three Dimensions

The three dimensions work together. A useful shorthand from risk analysis is: [1]

> **Decision consequence = Severity x Probability x (1 / Detectability)**

You do not need to calculate a number. The point is directional thinking: when any one of the three is high, the overall cost of error rises. When detectability is low, it amplifies the contribution of both severity and probability.

Use the three dimensions as a quick triage checklist before acting on any AI output:

1. **How bad if wrong?** (severity)
2. **How likely to be wrong in this situation?** (probability)
3. **Would I know before it causes harm?** (detectability)

If all three answers point toward high cost, you need to apply deliberate scrutiny — System 2 thinking (9.2) — before acting. If all three are low, you can move faster. Most real situations fall somewhere in between, which is exactly why Q1 is a question, not a rule. [2]

### 5.4 High-Stakes Domains Where Q1 Almost Always Points to High Cost

Some domains have structural features that push Q1 toward high cost almost by default. In these areas, the cost of acting uncritically on an AI output is rarely negligible. [1][2][3]

**Medical decisions**
Severity: physical harm to a person. Probability: medical AI operates on incomplete patient data and is frequently used outside the narrow population it was trained on. Detectability: clinical errors often only surface after harm has occurred, sometimes many steps removed from the original decision.

**Legal judgments**
Severity: legal consequences can restrict a person's freedom, finances, or rights — difficult to reverse once enacted. Probability: legal reasoning is context-specific; AI trained on general legal text may not have seen the jurisdiction, statute combination, or factual pattern in front of you. Detectability: legal documents are complex; an AI error in a contract clause may not be spotted until the clause is triggered.

**Safety-critical engineering**
Severity: structural failures, equipment failures, or software failures in safety systems can injure or kill. Probability: engineering AI is often applied in novel configurations the training data did not include. Detectability: safety-critical systems often fail silently until a triggering event exposes the failure.

**Financial decisions affecting third parties**
Severity: decisions that affect other people's money, housing, or credit are hard to reverse once actioned. Probability: financial AI is heavily dependent on historical data, which (as noted in 9.6) encodes historical inequalities. Detectability: biased financial AI outputs may not be detectable without systematic auditing that most organisations do not perform by default.

Note: the lesson is not "never use AI in these domains." It is that in these domains, Q1 reliably returns "high cost" — and that finding should shape how carefully you treat the AI's output. [1][2]

### 5.5 Low-Cost Errors — and Why They Still Deserve a Moment's Thought

Low-cost situations exist, and recognising them is part of using the Judgment Framework well. If you treat every AI output as life-or-death, you will burn out and start applying System 1 anyway. [3]

Low-cost situations typically look like:

- The AI is helping with something you could do yourself without difficulty.
- The output is easily reversible — you can undo, re-send, or correct with minimal effort.
- No one except you is affected.
- The output will be reviewed again before any final action is taken.

Even in genuinely low-cost situations, Q1 still earns its keep. Asking the question — even briefly — is the habit. The habit is what protects you in high-cost situations, where the temptation to skip the question is highest because you are busy, confident, or under time pressure. [2][3]

---

## 6. Implementation

Applying Q1 is a brief structured pause, not a lengthy analysis. Here is how to run through it in practice. [1][2]

**Step 1 — Identify the output you are about to act on.**
Name the specific AI output. Example: "The AI has suggested a drug interaction is safe for this patient."

**Step 2 — Assess severity.**
Ask: if this output is wrong, what is the worst plausible consequence? Be concrete. Avoid vague answers like "it could cause problems." Say what the problem would actually be.

**Step 3 — Assess probability.**
Ask: how likely is this output to be wrong *in this specific context*? Consider: Is this task within the AI's documented reliability range? Is this situation typical or unusual? Has the AI been wrong on similar tasks before?

**Step 4 — Assess detectability.**
Ask: if this output is wrong, how would I know? Would the error be visible before any harm occurs? Who else would see this output before it is actioned?

**Step 5 — Make a deliberate decision about scrutiny.**
If severity x probability x (1 / detectability) is high, invest time in verification before acting. The specific methods of verification are the subject of Q2 (topic 9.8). Right now, Q1 is telling you whether verification is warranted at all.

**Step 6 — Document your reasoning in high-stakes situations.**
In professional contexts — clinical, legal, financial, engineering — write down what Q1 told you and what you decided to do about it. This matters for accountability, which is Q3 (topic 9.9). Acceptable error thresholds are covered in topic 9.10.

---

## 7. Real-World Patterns

### Pattern 1 — Medical: AI-Assisted Diagnosis

A radiology department has deployed an AI tool that flags potential abnormalities in chest X-rays. The tool has an 87% sensitivity rate on the population it was tested on — meaning it correctly identifies 87 in every 100 true abnormalities. [1][3]

Before a radiologist acts on the AI's flag (or absence of a flag), Q1 analysis:

- **Severity**: high — a missed cancer or an unnecessary biopsy both carry serious patient consequences.
- **Probability**: meaningful — 13% of true abnormalities are missed; and the test population may not represent this patient's demographics (recall selection bias from 9.6).
- **Detectability**: low — a missed flag produces an absent signal, not a visible error; the patient is discharged and only re-presents if symptoms worsen.

Q1 verdict: high cost. The radiologist should not treat the AI's output as the final word. Independent review of the imaging — especially for unflagged areas — is warranted. This is not distrust; it is calibrated engagement. [1]

### Pattern 2 — Legal: AI Contract Review

A law firm uses an AI document-review tool to scan commercial contracts for non-standard clauses. A junior associate is reviewing a lease agreement. The AI marks it as "standard — no issues flagged." [1][2]

Q1 analysis:

- **Severity**: medium-to-high — a missed non-standard clause could expose the client to financial liability or limit their rights under the lease.
- **Probability**: meaningful — commercial leases contain jurisdiction-specific and landlord-specific language; the AI was trained on a general corpus; the specific clause in question may be unusual enough to be under-represented in training data.
- **Detectability**: medium — a problematic clause is visible in the text if read; but the AI's "clean" report anchors the reviewer's attention away from re-reading (anchoring bias, 9.4).

Q1 verdict: the associate should not file the document based solely on the AI's clean flag. A focused independent read of high-risk clause categories is warranted. [1][2]

### Pattern 3 — Content Moderation at Scale

A social media platform uses an AI to decide which posts to remove for policy violations. The AI is fast — it processes millions of posts daily — and has a published precision (7.8) rate of 94% on flagged content, meaning 94 in every 100 posts it removes actually violated the policy. [3]

Individual moderation decision, Q1 analysis:

- **Severity**: variable — wrongly removing a post (false positive) suppresses legitimate speech; wrongly leaving a post up (false negative) allows potential harm to propagate.
- **Probability**: 6% of removals are wrong at a 94% precision rate; across millions of posts, that is hundreds of thousands of erroneous decisions daily.
- **Detectability**: low for false negatives (harmful posts that slipped through are not automatically surfaced for review); medium for false positives (users can appeal removals).

Q1 verdict: individual high-stakes cases — accounts with large reach, politically sensitive content, first-time offences — warrant human review even when the AI has already made a call. The AI's scale makes its aggregate error rate large enough to require systematic human oversight on the margin. [3]

---

## 8. Best Practices

**Do this before acting on any AI output:**

| Situation | Q1 signal | Appropriate response |
|---|---|---|
| All three dimensions (severity, probability, detectability) are low | Low cost | Act on the AI's output; note that Q1 was considered |
| Severity is high even if probability seems low | High cost | Probability estimates can be wrong; apply verification |
| Detectability is low even if severity is medium | High cost | Low visibility amplifies harm; do not skip review |
| You are in a medical, legal, safety, or financial domain | Almost always high cost | Apply Q2 and Q3 as well before acting |
| The AI output is confidently stated but you cannot trace the reasoning | Probability is uncertain | Treat uncertainty as elevated probability; apply scrutiny |

**Avoid these patterns:**

- Treating Q1 as a box to check rather than a question to genuinely answer. The pause is the point.
- Confusing the AI's confidence level with accuracy. AI systems routinely express high confidence on wrong answers. [2][3]
- Applying Q1 only when you already have doubts. The whole purpose of the framework is to catch cases where System 1 would otherwise wave you through without doubt arising at all. [2]
- Skipping Q1 under time pressure. Time pressure is precisely the condition under which System 1 dominates and cost-of-error thinking is most needed.

---

## 9. Hands-On Exercise

**Q1 Triage on Three AI Outputs**

Below are three AI-generated outputs. For each one, apply the three-dimension Q1 triage (severity, probability, detectability) and write:

1. A one-sentence assessment of each dimension.
2. A one-sentence overall cost verdict (low / medium / high).
3. One sentence on what you would do before acting.

**Output A:** An AI email-writing tool suggests a subject line for a routine internal update.

**Output B:** An AI legal research tool summarises the applicable employment law for a redundancy decision affecting 40 employees.

**Output C:** An AI customer service chatbot provides a refund amount to a customer whose claim involves a product defect.

No background knowledge is required to answer — this is a reasoning exercise using the Q1 framework only. Compare your answers with a peer and discuss where you disagreed on severity or detectability.

---

## 10. Key Takeaways

- **Q1 asks one thing**: before you act on an AI output, how bad would it be if that output is wrong — taking into account how serious the harm would be (severity), how likely the error is in this context (probability), and how quickly it would be spotted before causing harm (detectability). [1]
- **The three dimensions work together.** Any one of them being high raises the effective cost of error. Low detectability amplifies both severity and probability. [1]
- **High-stakes domains — medical, legal, safety-critical, financial — almost always return "high cost" from Q1.** In these domains, AI output is useful input, not the final word. [1][2]
- **Low-cost situations are real and worth recognising.** Not every AI output warrants deep scrutiny. The framework helps you spend scrutiny where it actually matters. [3]
- **The habit of asking Q1 is the protection.** The question most needs to be asked when time pressure, confidence, and cognitive fatigue (9.2) conspire to skip it — which is the situation where errors are most likely. [2][3]

---

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
