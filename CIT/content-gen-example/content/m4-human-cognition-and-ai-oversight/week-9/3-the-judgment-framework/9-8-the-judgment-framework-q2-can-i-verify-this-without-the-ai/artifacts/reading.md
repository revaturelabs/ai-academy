<!-- nav:top:start -->
[⬅ Previous: 9.7 — The Judgment Framework](../../9-7-the-judgment-framework-q1-what-is-the-cost-of-this-being-wro/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 9.9 — The Judgment Framework ➡](../../9-9-the-judgment-framework-q3-who-is-accountable-if-this-fails/artifacts/reading.md)
<!-- nav:top:end -->

---

# The Judgment Framework — Q2: Can I verify this without the AI?

## Overview

Q1 of the Judgment Framework told you how much it matters if an AI answer is wrong. Q2 asks something different: can you actually check whether the answer is correct — without asking the AI to check itself? An AI cannot tell you whether its own output is trustworthy. Asking the same AI "are you sure?" gives you the same model's self-assessment, not an independent view. This topic explains what independent verification means, when it is possible, and what to do when it is not [1].

## Key Concepts

### Independent verification

**Independent verification** means checking an AI output against a source that is completely separate from the AI that produced it. The source cannot be the same AI, a related AI, or material that originally came from an AI.

Think of it like a rumour. If a friend tells you something and you want to know if it is true, asking that same friend again does not help. You need a second source — someone who was not part of the original conversation [3]. The same logic applies to AI output.

Independent sources include:
- A textbook, official publication, or peer-reviewed article.
- A qualified expert (doctor, lawyer, engineer) who can evaluate the claim from their own knowledge.
- A known standard, law, or regulation you can look up directly.
- A measurement or direct observation you can perform yourself.
- A second colleague who reviews the claim **before** reading the AI's answer.

### Verification is not the same as production

Students often mix up two different questions:

| Question | What it asks |
|---|---|
| **Production:** "Could I have produced this myself?" | Do I have enough expertise to generate the same output from scratch? |
| **Verification:** "Can I check whether this is correct?" | Can I test the claim against a separate source? |

These are not the same thing. You can verify without being able to produce. A patient does not know how to diagnose a disease, but they can still check that a drug dosage on a prescription matches the standard range in a reference guide. They are verifying — not producing [1]. Do not answer "no" to Q2 just because you could not have written the output yourself [2].

### The four verification methods

**1. Cross-referencing a source** — Take a specific claim from the AI and look it up in a separate, authoritative reference. Example: the AI says a drug interaction is dangerous; you check that claim in a pharmacology database written by medical professionals and updated independently of any AI [1].

**2. Using domain expertise** — Draw on your own professional knowledge to judge whether the AI's output is accurate and complete. Example: a structural engineer reads an AI-generated load calculation and spots that the safety factor is too low by professional standards. Their training is the independent source. This method only works when you have genuine expertise in the relevant domain [2].

**3. Checking against a known standard** — Compare the AI output to a rule, law, regulation, formula, or specification. Example: the AI generates a contract clause; you compare it line by line to the wording required by the legislation. The legislation removes subjectivity from the check [1].

**4. Asking a second person** — Have another human review the AI output. The second person should not have seen the AI's answer first. If they read it before forming their own view, they may be anchored to the AI's framing — a bias you studied in topic 9.4 [3].

### When is verification easy, hard, or impossible?

**Easy** when the AI's claim is factual and specific, a reliable reference exists that covers exactly that fact, and you can access it quickly. Example: the AI says the GDPR requires breach notification within 72 hours. You verify this in under two minutes by reading Article 33 of the GDPR directly [1].

**Hard** when the claim is specialised, no single authoritative reference exists, or meaningful verification would take significantly longer than the task itself. Hard does not mean skip it — it means plan for it: allow more time, find the right expert, or escalate [2].

**Impossible** when there is no external ground truth — for example, a prediction ("What will the stock price be in six months?"), frontier knowledge that no reference yet covers, or a timeline so short that no check can be done before action is required.

When verification is genuinely impossible, Q2 has a clear answer: "No, I cannot verify this." What you do next depends on what Q1 already told you.

### The Q1 × Q2 decision matrix

Q1 and Q2 work together. Your combined answers determine the right action.

![Q1 × Q2 decision matrix: four cells showing recommended action by cost-of-error level and whether verification is possible](./diagram.png)
*The Q1 × Q2 matrix: cost-of-error (from Q1) sets the stakes; verifiability (Q2) determines whether you can act or must escalate.*

| Q1 — cost of being wrong | Q2 — can I verify? | Recommended action |
|---|---|---|
| Low | Yes | Act, then verify when convenient. |
| Low | No | Act with awareness that error is undetected; review later. |
| High | Yes | Verify before acting. Do not act until the check passes. |
| **High** | **No** | **Stop. Do not act on AI output alone. Escalate, seek expert input, or use a different approach.** |

The bottom-right cell is the most important. When cost is high and verification is impossible, acting on the AI output without further steps is a failure of judgment — regardless of how confident the AI sounds [1][2].

## Worked Example

Here is Q2 applied step by step. A nurse receives an AI clinical decision support recommendation for a drug dosage.

**Step 1 — List the specific claims.**
Break the output into individual facts. In this case: drug name, recommended dose, unit, frequency, and any listed contraindications.

**Step 2 — Classify each claim.**
Each item is a factual medical statement. That points toward cross-referencing a published reference and using domain expertise.

**Step 3 — Identify a verification source.**
"I'll check online" is not a source. A specific source is: the hospital's formulary — an approved list of drugs and doses maintained by clinical pharmacists.

**Step 4 — Perform the check.**
Look up the drug in the formulary. Record what it says. Does the AI-recommended dose match the formulary entry? Does the patient's weight, kidney function, or other medications affect the safe range?

**Step 5 — Record the Q2 answer.**
State clearly: "I can verify this via the hospital formulary and clinical judgment — the recommended dose matches / does not match the formulary entry." This written record is the evidence trail if the decision is later questioned [1][3].

If the formulary is unavailable and the clinical expert cannot be reached in time, the answer to Q2 is "No — I cannot verify independently." Combined with the high cost-of-error from Q1, the correct next step is not to proceed on the AI output alone: escalate to a senior clinician.

## In Practice

These three patterns show Q2 applied in different fields:

**Legal — AI-generated contract clauses [1]**
Before any AI-drafted clause enters a final contract, a qualified lawyer checks it against the relevant legislation and the firm's precedent library — clause by clause. The lawyer is not re-drafting from scratch; they are verifying. If the AI clause deviates from the statutory requirement, it is corrected before the contract is signed.

**Medical — AI-suggested drug dosage [2]**
A prescribing doctor checks an AI dosage recommendation against the hospital formulary and applies their own clinical judgment about the specific patient. Two independent checks run in parallel. The AI recommendation is a starting point, not the final word.

**Financial — AI market analysis [2][3]**
An analyst cross-references AI-generated earnings figures against the company's actual regulatory filing before sharing the summary with clients. Numbers in public regulatory filings are independently verifiable. The AI may have misread a table or made an arithmetic error — the check is fast and covers the highest-risk element.

**Three common mistakes to avoid:**

- **Asking the AI again is not verification.** Two outputs from the same model can both be wrong in the same way. Consistency is not correctness [2].
- **"I'm not an expert" does not mean you can't verify.** Cross-referencing a claim against a published standard does not require expertise — it requires knowing where to look [3].
- **"I can't produce this" does not mean "I can't verify this."** A non-chemist can still check a molecular weight against a published chemistry database — that is verification, not production [1].

## Key Takeaways

- **Independent verification** means checking against a source completely separate from the AI — not the same AI, not a second prompt to the same AI.
- **Verification and production are different.** You can check a claim without being able to generate it yourself.
- **Four methods:** cross-referencing a source, applying domain expertise, checking against a known standard, and asking a second person (who has not seen the AI output first).
- **Q1 sets the stakes for Q2.** When cost-of-error is low, incomplete verification may be acceptable. When cost-of-error is high, Q2 becomes a gate — do not act before it passes.
- **High cost + cannot verify = stop and escalate.** Do not act on AI output alone. Seek expert input, a different source, or an explicit decision by an accountable person. (Who that accountable person is, and what accountability means, is the subject of topic 9.9.)

## References

1. Clio, "Verifying Legal AI Output — Checklist." <https://www.clio.com/resources/ai-for-lawyers/verify-legal-ai-output/>
2. VerifyWise, "AI Output Validation — Methods Catalog." <https://verifywise.ai/lexicon/ai-output-validation>
3. CSUN Library, "Evaluating AI-Generated Output." <https://libguides.csun.edu/c.php?g=1377855&p=11076059>

---
<!-- nav:bottom:start -->
[⬅ Previous: 9.7 — The Judgment Framework](../../9-7-the-judgment-framework-q1-what-is-the-cost-of-this-being-wro/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 9.9 — The Judgment Framework ➡](../../9-9-the-judgment-framework-q3-who-is-accountable-if-this-fails/artifacts/reading.md)
<!-- nav:bottom:end -->
