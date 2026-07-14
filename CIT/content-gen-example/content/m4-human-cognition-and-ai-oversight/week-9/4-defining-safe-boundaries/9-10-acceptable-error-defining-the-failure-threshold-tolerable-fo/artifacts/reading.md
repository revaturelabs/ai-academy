<!-- nav:top:start -->
[⬅ Previous: 9.9 — The Judgment Framework](../../../3-the-judgment-framework/9-9-the-judgment-framework-q3-who-is-accountable-if-this-fails/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 9.11 — High-stakes domains where AI must not have the final word ➡](../../9-11-high-stakes-domains-where-ai-must-not-have-the-final-word-me/artifacts/reading.md)
<!-- nav:top:end -->

---

# Acceptable error — defining the failure threshold tolerable for a use case

## Overview

Every AI system makes mistakes. The question is not how to eliminate errors entirely — no production system achieves that. The real question is: which errors are tolerable, which are not, and at what rate does the line get crossed?

**Acceptable error** is the deliberate decision about where that line sits: the maximum rate of specific failure types that a use case can absorb before the cost of using the AI exceeds its benefit. This is not a licence to be sloppy — it is a design decision that forces you to confront exactly what "wrong" looks like for your situation and how much of it you can sustain [3].

This topic builds directly on Judgment Framework Q1 (9.7): "What is the cost of this being wrong?" Q1 asks that question for a single decision. Acceptable error asks it for a whole system operating repeatedly over time — and translates the answer into a threshold that governs when the AI's output is safe to act on and when it must be escalated or reviewed.

## Key Concepts

Every AI classification system produces two kinds of errors:

| Error type | What happens | Example |
|---|---|---|
| **False positive (FP)** | AI says "yes" when the correct answer is "no" | Spam filter marks a legitimate email as spam |
| **False negative (FN)** | AI says "no" when the correct answer is "yes" | Medical screening tool clears a patient who has the condition |

These two error types almost never cost the same. In most real-world use cases, one is far more harmful than the other. This is **asymmetric error cost** — and it is the most important thing to understand before setting any threshold. A single combined accuracy figure (e.g., "94% accurate") hides which error type is occurring and at what rate, making it a poor guide for safety-critical decisions.

![Acceptable error threshold-setting process](./diagram.png)
*The four-step process for setting an acceptable error threshold, with contrasting examples of FP-heavy versus FN-heavy use cases.*

The diagram above shows the **four-step threshold-setting process**:

**Step 1 — Identify error types.** In plain language, define what a false positive and a false negative each mean for your specific use case. "The AI flags a legitimate transaction as fraud" is a false positive. "The AI misses a fraudulent transaction" is a false negative. Vague definitions produce vague thresholds — and vague thresholds fail silently in production.

**Step 2 — Cost each error type.** What happens when each type occurs? Who is affected, and how severely? This step forces you to decide which type is more harmful. If both are roughly equally costly, combined accuracy is a useful single metric. If the costs are asymmetric — the normal case in real-world deployments — you need separate thresholds for each type [2].

**Step 3 — Set the threshold ceiling.** The threshold is not a target — it is a ceiling the system must stay below. Set it conservatively: build in margin for the difference between test conditions and real-world production (distribution shift, adversarial inputs, edge cases). A threshold calibrated tight to test-set performance will often be exceeded once the system meets the full range of production data [2].

**Step 4 — Compare to the human baseline.** What error rate does a human practitioner achieve on the same task? Research found that radiology staff held AI to a stricter standard than human clinicians — an average acceptable AI error rate of 6.8%, compared to 11.3% for humans performing the same task [1]. The human baseline is a calibration reference: if the AI's error rate on the high-cost type exceeds the human baseline for that type, the case for deploying the AI rather than a human becomes harder to defend on quality grounds.

A useful decision-level tool is the **confidence threshold**: the minimum confidence score below which the AI's output is routed to human review rather than acted on automatically. Raising this threshold reduces the AI's autonomous error rate but increases human workload — the right calibration depends on the cost structure established in step 2 [3].

## Worked Example

A team is deploying an AI tool to screen job applications at a recruitment agency. They apply the four steps:

**Step 1.** False positive: AI shortlists a candidate who is not qualified. False negative: AI rejects a candidate who is qualified.

**Step 2.** A false positive wastes one recruiter's time (roughly one hour reviewing an unqualified application). A false negative loses a potentially strong hire and damages the agency's reputation with its client. False negatives are more costly.

**Step 3.** The agency sets its threshold: no more than 5% of qualified candidates may be incorrectly rejected. They calibrate conservatively, actually targeting 3%, to account for the fact that the AI was trained on historical hiring data that may not fully represent the current candidate pool. The threshold is a ceiling — not the acceptable rate to aim for.

**Step 4.** A human recruiter scanning CVs at speed incorrectly rejects approximately 8% of qualified candidates. The AI's measured false negative rate in testing is 3.2% — well below both the threshold (5%) and the human baseline (8%). The threshold is cleared.

The team also sets a confidence threshold at 75%: any application where the AI's score is below this level goes to a human reviewer, regardless of whether the tentative decision is accept or reject. This gives human judgment a foothold on borderline cases without routing every decision manually.

## In Practice

**Spam filtering: minimise false positives.**
Most spam filters accept a higher false negative rate (some spam lands in the inbox) in order to keep the false positive rate very low (legitimate email rarely blocked). Blocking a real email — especially from a financial institution or government agency — can cause material harm, while delivering an occasional spam message is a manageable nuisance. Enterprise filters often apply **threshold segmentation**: near-zero false positive tolerance for high-priority sender categories, higher tolerance for unknown senders.

**Medical screening: minimise false negatives.**
In cancer screening, missing a tumour (false negative) is far more costly than flagging a benign finding for follow-up (false positive). Screening protocols are calibrated for very high sensitivity, accepting a higher false positive rate because an unnecessary follow-up examination costs far less than a missed diagnosis [1]. Regulatory standards for medical AI devices often specify maximum false negative rates rather than overall accuracy.

**Fraud detection: tiered thresholds.**
Fraud detection applies the threshold-setting process twice: one threshold for "block automatically" (high-confidence fraud) and one for "route to manual review" (medium-confidence). Below both thresholds, transactions pass with enhanced monitoring. This three-tier structure manages both error types explicitly — rather than burying one inside a combined accuracy figure [2].

**Alert fatigue: the cost of thresholds set too strictly.**
Setting a threshold too conservatively generates excessive false alarms. This causes **alert fatigue** — introduced in 9.5 — where reviewers stop taking alerts seriously because so many turn out to be false positives. Paradoxically, a threshold that is too strict can increase overall error rates by degrading the human vigilance that is supposed to catch genuine misses [2].

## Key Takeaways

- **Acceptable error is a deliberate threshold decision:** the maximum rate of specific failure types a use case can absorb before AI cost exceeds benefit. Not zero errors — bounded tolerance within defined conditions.
- **False positives and false negatives carry asymmetric costs** in almost every real-world use case. Set separate thresholds per error type when costs are unequal — overall accuracy hides the distribution.
- **The four-step process:** identify error types in plain language → cost each separately → set threshold ceiling conservatively → compare to human baseline as a calibration reference.
- **The human baseline** shows that stakeholders hold AI to stricter standards than humans (6.8% vs 11.3% in radiology) [1] — account for this asymmetry when communicating threshold decisions.
- **Alert fatigue** (9.5) is the direct consequence of thresholds set too strictly — excessive false alarms erode human vigilance and can raise overall error rates [2].

## References

1. "Should artificial intelligence have lower acceptable error rates than humans?" — PMC / National Library of Medicine. https://pmc.ncbi.nlm.nih.gov/articles/PMC10301708/
2. "What are good and acceptable error rates?" — AppSignal Learning Center. https://www.appsignal.com/learning-center/what-are-good-and-acceptable-error-rates
3. "Understanding Confidence Threshold in AI Systems" — LlamaIndex Glossary. https://www.llamaindex.ai/glossary/what-is-confidence-threshold

---
<!-- nav:bottom:start -->
[⬅ Previous: 9.9 — The Judgment Framework](../../../3-the-judgment-framework/9-9-the-judgment-framework-q3-who-is-accountable-if-this-fails/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 9.11 — High-stakes domains where AI must not have the final word ➡](../../9-11-high-stakes-domains-where-ai-must-not-have-the-final-word-me/artifacts/reading.md)
<!-- nav:bottom:end -->
