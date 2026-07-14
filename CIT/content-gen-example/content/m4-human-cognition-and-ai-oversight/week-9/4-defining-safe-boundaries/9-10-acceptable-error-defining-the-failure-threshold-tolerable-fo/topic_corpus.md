## 1. Topic Metadata

- **Topic ID:** 9.10
- **Title:** Acceptable error — defining the failure threshold tolerable for a use case
- **Module:** 4 — Defining Safe Boundaries
- **Course:** M4 — Human Cognition and AI Oversight
- **Week:** 9
- **Depth Profile:** standard
- **Resources:** PMC (pmc.ncbi.nlm.nih.gov/articles/PMC10301708/), AppSignal (appsignal.com/learning-center/what-are-good-and-acceptable-error-rates), LlamaIndex (llamaindex.ai/glossary/what-is-confidence-threshold)

---

## 2. Prerequisites

- **9.7 — The Judgment Framework Q1: What is the cost of this being wrong?** introduces severity of error, probability of error, detectability, and cost-of-error triage. Acceptable error formalises that Q1 triage into a concrete threshold that governs repeated decisions.
- **9.5 — Automation bias** introduces alert fatigue and calibrated trust. Setting thresholds too conservatively (too many false alarms) is the direct cause of alert fatigue.

---

## 3. Learning Objectives

By the end of this topic, learners will be able to:

1. Define "acceptable error" as a deliberate threshold decision — not zero errors, but a bounded tolerance for specific types of failure within a defined use case.
2. Distinguish false positives (Type I errors) from false negatives (Type II errors) and explain why their costs typically differ.
3. Explain why the same error rate can be acceptable in one context and unacceptable in another, using at least two contrasting examples.
4. Apply a four-step process to define a failure threshold for a given AI use case.
5. Describe the "human baseline" and explain why it is a useful — but insufficient on its own — reference point for setting AI error thresholds.

---

## 4. Introduction

When an AI system gets something wrong, the natural first reaction is: "How do we stop this from happening again?" That is the wrong question. The right question is: "How often can we afford for this to happen — and in which direction?"

No AI system operates at perfect accuracy. Every classifier has a false positive rate. Every language model occasionally produces incorrect output. Every recommendation engine sometimes surfaces the wrong item. The question is not whether errors will occur — they will — but whether the errors that do occur fall within the bounds that the use case can tolerate.

**Acceptable error** is the deliberate definition of those bounds: the maximum rate or type of failure that a use case can absorb before the cost of using the AI exceeds the benefit. Setting this threshold is a design decision, not a measurement. It requires asking: what kinds of wrong are tolerable, what kinds are catastrophic, and at what rate does each type cross from manageable to unacceptable?

This topic builds directly on Judgment Framework Q1 (9.7: cost-of-error triage). Q1 asks "what is the cost of this being wrong?" at the level of a single decision. Acceptable error formalises that question into a threshold that governs repeated decisions — a standing policy that defines when AI output is safe to act on and when it must be escalated or rejected [3].

---

## 5. Core Concepts

### 5.1 What "acceptable error" means — and what it does not

**Acceptable error** does not mean "errors are fine." It means: given this specific use case, this specific type of failure, and this specific cost structure, a rate below threshold X is within the bounds we can operate within safely and responsibly.

An acceptable error threshold has three components:

1. **A type** — which kind of failure is being tolerated (false positives, false negatives, or both separately)
2. **A rate** — what proportion of decisions this failure type may represent
3. **A condition** — the use case context in which this rate applies

A threshold without a type is meaningless. "We can tolerate a 5% error rate" says nothing useful until you specify: 5% of what — false alarms that waste time, or missed detections that cause harm? The same 5% figure can be completely safe in one context and catastrophically permissive in another.

### 5.2 False positives and false negatives

Every AI classification system produces two kinds of errors:

| Error type | Also called | What happens | Example |
|---|---|---|---|
| **False positive** (FP) | Type I error | AI says "yes" when the correct answer is "no" | Spam filter marks a legitimate email as spam |
| **False negative** (FN) | Type II error | AI says "no" when the correct answer is "yes" | Medical screening tool clears a patient who has the condition |

These two error types are not symmetrical. In most real-world use cases, they carry different costs:

- A **false positive** in spam filtering means a user misses an email. Annoying, but recoverable.
- A **false negative** in cancer screening means a patient's tumour is missed. Potentially fatal.

The same asymmetry runs in the opposite direction for other domains: in fraud detection, a false positive (flagging a legitimate transaction) costs the bank a customer relationship and a support call; a false negative (missing a fraudulent transaction) costs the bank the full transaction value and potentially regulatory penalties.

**The core insight:** before setting any threshold, identify which error type is more costly for your use case — and set the threshold to minimise that type, even at the expense of increasing the other.

### 5.3 Asymmetric error cost

**Asymmetric error cost** describes the condition where false positives and false negatives carry materially different consequences. This is the normal case in real-world AI deployments, not the exception.

When costs are asymmetric, a single accuracy figure (e.g., "94% accurate") is misleading. A classifier that is 94% accurate but misses 40% of positive cases (high FN rate) may be dangerous in a medical screening context, even though its headline accuracy looks high. Accuracy hides the error type distribution.

For this reason, professional and regulatory standards in high-risk domains typically specify error tolerances separately for each error type rather than using a combined accuracy measure. A medical imaging device might be required to achieve ≤2% false negative rate (sensitivity ≥98%) even if this means accepting a higher false positive rate — because the cost of missing a positive case is far greater than the cost of an unnecessary follow-up examination [1].

### 5.4 The threshold-setting process

Setting an acceptable error threshold for an AI use case involves four steps:

**Step 1: Identify what "wrong" looks like.**
Define, in plain language, what a false positive and a false negative each mean for your specific use case. Be concrete. "The AI approves a loan application that should be rejected" is a false positive. "The AI rejects a loan application that should be approved" is a false negative. Vague definitions produce vague thresholds.

**Step 2: Cost each error type.**
What happens when each error type occurs? What is the impact on the user, the organisation, third parties, and compliance obligations? Be explicit about which is more costly. If the costs are roughly equal, combined accuracy is a useful metric. If they are asymmetric, you need separate thresholds per error type.

**Step 3: Set the threshold below the point where costs exceed benefits.**
The threshold is not a target — it is a ceiling. The AI's actual error rate must stay below this ceiling for the system to be safe to operate. Set it conservatively: build in margin for real-world conditions that differ from the testing environment (distribution shift, edge cases, adversarial inputs). A threshold set tight against test-set performance will be breached in production [2].

**Step 4: Compare to the human baseline.**
What error rate does a human professional achieve on the same task? This does not determine your threshold, but it provides a calibration reference. If the AI's error rate on the high-cost error type is materially higher than the human baseline for that same type, the case for deploying the AI rather than the human is harder to make on quality grounds.

### 5.5 The human baseline

Research comparing AI and human error rates in real-world settings reveals an important asymmetry in how people perceive acceptable error. A survey of radiology department staff found that they held AI to a stricter standard than human radiologists: the average acceptable AI error rate was 6.8%, compared to 11.3% for humans performing the same task [1].

This finding reflects something important: social tolerance for error is not just a function of the error rate itself, but of who or what produced the error. AI systems are perceived as having less social capital than human colleagues — there is less "forgiveness" available for a machine that gets something wrong. Whether this asymmetry is justified is a separate debate; the practical implication is that AI systems may need to demonstrate lower error rates than humans before stakeholders will accept them.

For threshold-setting, the human baseline is useful in two ways:

1. **Floor check:** if the AI's error rate on the high-cost error type exceeds the human baseline for that type, the case for deploying the AI — rather than the human — becomes harder to make on quality grounds.
2. **Calibration reference:** if the AI's error rate is substantially lower than the human baseline across all error types, a tighter threshold may be appropriate and defensible, because the AI is outperforming human practitioners.

The human baseline is a reference point, not a pass/fail gate. Some use cases have no meaningful human baseline because the task is too large, too fast, or too complex for a human to perform. In those cases, the threshold must be derived entirely from first principles using steps 1–3 above.

---

## 6. Implementation

### 6.1 Practical threshold levels

In practice, acceptable error thresholds operate at two distinct levels:

**System-level threshold:** the maximum tolerable error rate at which the AI system is allowed to operate overall. If production monitoring shows the system's error rate crossing this threshold, the system is taken offline, reduced to an advisory role, or routed entirely to human review.

**Decision-level threshold (confidence threshold):** the minimum confidence score at which the AI's output is acted upon directly. Outputs below this confidence level are flagged for human review rather than acted on automatically. This is the **confidence threshold** in AI system design — a tunable parameter that controls the balance between AI autonomy and human oversight [3].

These two thresholds interact: raising the decision-level threshold (requiring higher AI confidence before acting automatically) reduces the AI's autonomous error rate but increases the human review workload. The right calibration depends on the cost structure from §5.4.

### 6.2 Common pitfalls

**Too strict (threshold too low):** Setting the threshold too conservatively means the system generates too many false alarms or escalates too many decisions to human review. This causes **alert fatigue** (introduced in 9.5) — reviewers stop taking alerts seriously because the false alarm rate is so high. Paradoxically, a threshold set too strictly can increase overall error rates by degrading the human vigilance that is supposed to catch the AI's misses [2].

**Too permissive (threshold too high):** Setting the threshold too generously means harmful errors pass through without escalation. This is particularly dangerous when test-set performance differs from production conditions — a threshold calibrated to test data may already be embedded in downstream processes before the higher production error rate becomes apparent.

**Conflating accuracy with safety:** Overall accuracy hides the distribution across error types. A system that is "95% accurate" but has a 30% false negative rate on the high-cost error type is less safe than a system that is "88% accurate" with a 5% false negative rate on that same type. Never use overall accuracy as the sole indicator of acceptable performance in domains with asymmetric error costs.

---

## 7. Real-World Patterns

### 7.1 Spam filtering — asymmetric FP tolerance

A spam filter produces two error types: false positives (legitimate email marked as spam) and false negatives (spam delivered to inbox). Most spam filter designs accept a higher false negative rate in order to keep the false positive rate very low — because delivering unwanted email is an inconvenience, while blocking a legitimate communication (especially from a financial institution or a government agency) can cause material harm.

Enterprise spam filters often segment thresholds by sender type: near-zero false positive tolerance for high-priority sender categories, higher tolerance for unknown or low-reputation senders. This is **threshold segmentation** — different thresholds applied to different sub-populations within the same system.

### 7.2 Medical screening — asymmetric FN tolerance

In cancer screening (e.g., mammography AI), the asymmetry runs the other way. A false negative — missing a tumour that is present — is far more costly than a false positive — flagging a benign finding for further examination. Screening protocols are therefore calibrated for very high sensitivity (low FN rate), accepting a higher false positive rate because the cost of a follow-up examination is much lower than the cost of a missed diagnosis.

The PMC research cited here [1] shows that in radiology, stakeholders apply a more stringent standard to AI on the false negative dimension specifically — they tolerate less AI "miss" error than human "miss" error, even when the AI produces fewer total errors than human clinicians.

### 7.3 Fraud detection — tiered thresholds for both error types

Fraud detection sits in a space where both error types carry material costs: false positives (blocking legitimate transactions) cost customer relationships and operational overhead; false negatives (missing fraud) cost direct financial loss and regulatory exposure. In practice, fraud detection systems use a tiered decision structure: high-confidence fraud triggers automatic blocking; medium-confidence triggers manual review; low-confidence passes with enhanced monitoring [2].

This three-tier structure is the threshold-setting process in §5.4 applied twice — once for the "block automatically" threshold and once for the "escalate for review" threshold. Decisions between the two thresholds go to humans; decisions above the upper threshold go to automated action; decisions below the lower threshold pass without intervention.

---

## 8. Common Misconceptions

**"Zero errors is the right target."**
No production AI system achieves zero errors. Designing for zero errors typically produces extremely high false positive rates, alert fatigue, and systems that operators learn to route around. The right target is a calibrated threshold appropriate to the use case.

**"The same error threshold applies everywhere."**
Error tolerance is use-case specific. A threshold appropriate for a creative writing tool (where errors are a minor inconvenience) is catastrophically permissive for a medical diagnosis tool. Applying thresholds across contexts without recalibrating is a design failure.

**"If the AI is more accurate than humans overall, no threshold is needed."**
Even AI systems that outperform humans on average accuracy produce failure modes that differ systematically from human failures — concentrated in specific subpopulations, specific input distributions, or adversarially crafted inputs. A threshold is still needed, and it may need to be set differently from the human baseline because the AI's error distribution is different, not just smaller.

**"A confidence score equals an error threshold."**
Confidence scores reported by AI systems are not calibrated probabilities unless the system has been explicitly calibrated [3]. A model that reports "95% confidence" may be wrong 20% of the time on out-of-distribution inputs. Confidence thresholds are useful routing rules but do not substitute for measuring the actual error rate on real production data.

---

## 9. Key Takeaways

- **Acceptable error** is a deliberate threshold decision: the maximum rate of specific failure types a use case can absorb before the cost of using the AI exceeds its benefit. It is not an absence of errors — it is a bounded tolerance within defined conditions.
- **False positives and false negatives carry asymmetric costs** in most real-world applications. Setting a threshold requires identifying which error type is more costly and calibrating separately for each, not just measuring overall accuracy.
- **The four-step process:** (1) identify what "wrong" looks like in plain language, (2) cost each error type separately, (3) set the threshold below the point where costs exceed benefits, (4) compare to the human baseline as a calibration reference.
- **The human baseline** is a reference point, not a pass/fail test. Research shows that stakeholders hold AI to stricter standards than human practitioners — an asymmetry worth accounting for when communicating threshold decisions to stakeholders [1].
- **Alert fatigue** (introduced in 9.5) is the direct consequence of thresholds set too strictly — excessive false alarms degrade human vigilance and can raise overall error rates [2].
- Some domains have such severe asymmetric costs that no AI error rate is truly acceptable for autonomous decision-making — that territory is covered in topic 9.11.

---

## 10. Discussion Prompts

1. A hospital wants to deploy an AI screening tool for a rare but treatable condition. The AI has a 3% false negative rate and a 15% false positive rate. A human radiologist has a 5% false negative rate and a 6% false positive rate. Is the AI's error profile acceptable? What additional information would you need before deciding?
2. You are setting a confidence threshold for an AI that auto-approves expense reports. Claims above the threshold are approved automatically; below it go to a human reviewer. What factors should drive where you set this threshold?
3. A colleague argues that if the AI makes 40% fewer total errors than a human, no further threshold analysis is needed. Using the concepts from this topic, explain what is missing from this argument.

---

## 11. Further Reading

- [1] "Should artificial intelligence have lower acceptable error rates than humans?" — PMC / National Library of Medicine. https://pmc.ncbi.nlm.nih.gov/articles/PMC10301708/
- [2] "What are good and acceptable error rates?" — AppSignal Learning Center. https://www.appsignal.com/learning-center/what-are-good-and-acceptable-error-rates
- [3] "Understanding Confidence Threshold in AI Systems" — LlamaIndex Glossary. https://www.llamaindex.ai/glossary/what-is-confidence-threshold
