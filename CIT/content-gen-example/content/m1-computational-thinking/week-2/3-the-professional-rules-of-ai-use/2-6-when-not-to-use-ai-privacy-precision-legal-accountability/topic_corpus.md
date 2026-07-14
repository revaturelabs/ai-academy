---
topic_id: "2.6"
title: "When NOT to use AI — privacy, precision, legal accountability"
position_in_module: 2
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. When NOT to use AI — privacy, precision, legal accountability — Topic Corpus

## 2. Prerequisites

- **2.1** — What makes a good specification: testable, bounded, observable (introduced the idea that a spec must have clear, verifiable outputs)
- **2.3** — How to identify inputs, expected outputs, and failure conditions (the six-component checklist)
- **2.5** — The 70/30 rule: human oversight, accountability split (introduced the concept that humans remain responsible for AI-assisted decisions)

## 3. Learning Objectives

- Identify at least three types of situations where using AI is inappropriate or risky.
- Explain what "sensitive data" means and give an example of why sharing it with an AI tool is a problem.
- Describe what "probabilistic output" means (introduced in topic 2.4) and explain why it is unacceptable in high-stakes precision tasks.
- Explain what "legal accountability" means and why an AI system cannot hold it.
- Apply the three-dimension framework (privacy, precision, legal accountability) to a scenario and decide whether AI use is appropriate.

## 4. Introduction

You have spent several topics learning how to write clear specifications and how AI uses patterns to produce answers. AI is genuinely useful for many tasks — drafting text, summarising long documents, suggesting ideas.

But there are tasks where using AI is the wrong choice. Not because AI is broken, but because the situation itself has constraints that AI cannot satisfy. Knowing when *not* to use a tool is just as important as knowing how to use it. A hammer is excellent for nails; using it to tighten a bolt causes damage regardless of how skilled the person swinging it is.

This topic introduces three specific reasons to say "no" to AI use:

1. **Privacy** — the data involved is sensitive or confidential.
2. **Precision** — the output must be exact, and AI's probabilistic answers are not reliable enough.
3. **Legal accountability** — the law requires a human to be responsible, and AI cannot fill that role.

You will learn to recognise each of these situations and apply a simple decision check before reaching for an AI tool. By the end of this topic you will have a framework — three questions that take under a minute to run — that you can apply to any professional task for the rest of your career.

## 5. Core Concepts

### 5.1 Privacy — when data is sensitive or confidential

**Sensitive data** is any information that could harm a person, an organisation, or a relationship if it became known to others. Examples include a patient's medical history, a client's legal case details, a student's academic record, or a company's financial plans that have not yet been made public.

When you type information into an AI tool — a chat interface, a writing assistant, a summarisation tool — that information typically leaves your device. It travels to a server run by the company that built the tool. Depending on the tool's settings and its terms of service, that information may be [1][2]:

- stored temporarily or permanently on that server,
- used to improve the AI model for future users, or
- accessible to the tool provider's staff under certain conditions.

This is the core privacy risk: **you do not control what happens to the data once it leaves your hands** [2]. The moment you press "send", you have transferred something to a third party — and you cannot take it back.

**Consumer tools versus professional tools.** Consumer AI tools (the free or low-cost tools available to anyone) are not designed to protect confidential professional data [1]. They carry the same privacy risks as typing a client's name and case details into a public discussion forum [1]. Professional-grade AI tools — sometimes called enterprise or business-tier tools — may offer stronger data-handling contracts that prevent the provider from using your input to train their models. But even a professional tool does not automatically make sensitive data safe to share; the organisation's own data-handling policy must be consulted first [2].

**A concrete scenario: the paralegal's mistake.** A paralegal (someone who assists lawyers with administrative and research tasks) is summarising a client's commercial contract to help the lead attorney prepare for a negotiation. To save time, she pastes the full contract text — including the client's name, the counterparty's identity, the financial terms, and the confidentiality clauses — into a free AI chat tool and asks it to produce a summary.

The summary is excellent. The problem is that she has just shared her client's confidential business terms with a third-party server [1][2]. She no longer controls where that data goes or how it is used. That is a breach of professional confidentiality — even though the AI worked perfectly and even though she kept the summary entirely internal. The harm is in the act of sharing, not in what was done with the output.

This example illustrates a principle that applies well beyond legal work: **the quality of the AI's output does not affect whether sharing the data was appropriate**. A perfect summary of confidential data is still a confidentiality breach.

**The rule of thumb.** Before using any AI tool, ask: "Would I be comfortable if this data were visible to a stranger?" If no, do not paste it into the tool [2].

Data protection laws regulate what "comfortable" means in specific industries. **HIPAA** (Health Insurance Portability and Accountability Act, pronounced "HIP-ah") is a United States law that sets rules for how health information may be stored, shared, and handled. Equivalent regulations exist in other jurisdictions — for example, GDPR (General Data Protection Regulation) in Europe. You will study these regulations in later topics. For now, the principle is straightforward: health information is sensitive data, and you need explicit permission and a data-compliant platform before using any AI tool with it [3].

---

### 5.2 Precision — when probabilistic output is too uncertain for the stakes

You learned in topic 2.4 that AI produces **probabilistic output** — an answer that represents the most likely response based on patterns, not a guaranteed correct answer. AI can be wrong, and the same question asked twice may produce slightly different answers.

For many tasks, a "usually right" answer is fine. If an AI helps you brainstorm five project name ideas and three are good, the stakes are low. If it suggests three ways to phrase an email and one lands awkwardly, you edit it and move on. The cost of a wrong answer is trivial.

But some tasks require **exact precision** — an answer that is either completely correct or must not be acted upon. In those situations, AI's probabilistic nature is a disqualifying problem, because "usually right" is not the same as "always right", and the task demands the latter.

**What counts as high-precision-required?**

| Task type | Why exactness matters |
|---|---|
| Drug dosage calculation | A wrong dose — too high or too low — directly harms the patient. |
| Financial audit figures | A rounding error or incorrect figure carries legal and financial consequences. |
| Navigation coordinates for aviation | A small error in latitude or longitude means a dangerous course deviation. |
| Legal contract clause interpretation | Misreading a clause can create binding obligations the client never agreed to. |
| Medical diagnosis | An incorrect diagnosis leads to the wrong treatment, which can cause harm. |
| Structural load calculations | An error in engineering figures can make a building or bridge unsafe. |

In each case, the cost of a wrong answer is not "mildly inconvenient" — it is potentially catastrophic. What makes AI specifically dangerous here is that it produces its wrong answers **confidently** [3]. An AI does not say "I am not sure"; it says "The dosage is 500mg" in the same tone whether it is correct or not. This is called **hallucination** — a term you will encounter more in later topics — where an AI produces a plausible-sounding but factually incorrect output without signalling any uncertainty.

This connects directly to the verification loop from topic 2.5: when precision is required, the human verification step is not optional — it is what prevents a confident-but-wrong AI answer from causing harm. Skipping verification in a precision-required task is not a minor shortcut; it is the step that turns AI from a useful assistant into a liability.

**A concrete scenario: the dosage calculation.** A nurse is preparing medication for a patient and asks an AI tool to cross-check the calculated dosage against the patient's weight and the prescribed concentration. The AI returns a figure. The figure is wrong by a factor of ten because the AI conflated two different unit conventions in its training data. The nurse does not double-check against a validated calculator because the AI answered so quickly and confidently. The patient receives a dangerous dose [3].

The failure here is not that the nurse used AI. The failure is that the task required exact precision and the output was acted on directly without verification.

**The rule of thumb.** Ask: "If the AI's answer is 5% wrong, would that cause serious harm?" If yes, do not use AI as the source of the final answer. A human expert must verify it against a reliable, auditable source.

---

### 5.3 Legal accountability — when a human must be legally responsible

**Legal accountability** means that a specific person or organisation is formally responsible — in the eyes of the law — for a decision and its consequences. If the decision causes harm, that responsible person can face legal action: a fine, a lawsuit, or professional sanction such as losing their licence to practise.

AI tools cannot be held legally accountable. An AI system is software [1]. It does not hold a professional licence. It cannot appear before a court. It cannot be fined, imprisoned, or struck off a professional register (removed from the official list of people licensed to practise their profession). Because it cannot be held responsible, it cannot, by itself, fulfil the role that law and professional regulation have created for licensed humans [1].

This matters because some professions exist inside a framework of legal responsibility. A licensed doctor is accountable for clinical decisions. A licensed solicitor (lawyer) is accountable for the legal advice they give a client. A certified financial adviser is accountable for investment recommendations. The licence exists precisely because the stakes are high enough that society requires a specific, identifiable, responsible human.

When someone uses AI to produce an output and presents that output as their own professional advice, the legal responsibility still falls on the human [1]. There is no way for a professional to transfer their accountability to a piece of software. But here is the deeper problem: **if the AI's output is wrong and a human relied on it without verifying it, the harm has already occurred** — and the human professional is the one who faces the consequences [1][3]. The AI cannot be sanctioned. Only the human can.

This creates a subtler risk: using AI in a way that quietly undermines the verification step from topic 2.5. If a doctor copies an AI-generated clinical note into a patient record without reading it, the doctor is still legally accountable for that note — but has skipped the quality check that their accountability is meant to guarantee [3]. The accountability has not gone away; it has been disconnected from the review that justifies it.

**A concrete scenario: the fabricated case citation.** A junior lawyer is preparing a legal brief. She asks an AI tool to research relevant court precedents — past rulings that could support her client's argument. The AI returns a list of cases with confident summaries. She incorporates three of them into the brief without individually checking whether the cases exist.

When the opposing counsel and the judge review the brief, they discover that one of the cases the AI cited does not exist. The AI **hallucinated** it — constructed a plausible-sounding case name, court, date, and ruling from patterns in its training data. The lawyer — not the AI — faces professional discipline. She may be reprimanded by the bar association (the professional body that regulates lawyers). She may face a costs order (a court ruling requiring one party to pay the other's legal costs). In a serious instance, she could face suspension [1].

The AI produced the error. The human owns the consequence.

**The rule of thumb.** Ask: "Could I — or my organisation — face legal consequences if this AI output is wrong?" If yes, a qualified human must review and own the final decision. The AI can assist with drafting or research, but the human must be the accountable last step.

---

### 5.4 Putting the three dimensions together

You can use all three checks as a quick pre-use checklist before applying AI to any task.

**The three-question check:**

1. **Privacy check** — Does this task involve sensitive or confidential data? If yes, do not use a consumer AI tool without explicit organisational approval and a data-compliant platform (a tool that meets the data-privacy rules for your profession).

2. **Precision check** — Does this task require an exact, verified answer where a plausible-but-wrong answer would cause serious harm? If yes, do not rely on AI as the final source of truth; a human expert must verify the output against an authoritative, auditable source.

3. **Legal accountability check** — Does this task require a person to be legally responsible for the output? If yes, a qualified human must own and sign off on the final decision; AI can assist in drafting and research only.

If the answer to any of the three questions is "yes", that is a signal to either (a) not use AI, or (b) use AI only as a drafting aid with a mandatory human verification step [1][2][3].

Notice that the three dimensions can overlap. A clinical diagnosis involves all three: the data is sensitive (patient health information), the output requires precision (the wrong diagnosis causes harm), and a licensed physician must be legally accountable for the diagnosis. When two or more dimensions apply simultaneously, the constraint on AI use is even stronger.

## 6. Implementation

**Applying the three-question check to a task — step by step**

Use this procedure when deciding whether AI is appropriate for a given task. Run it before you open any AI tool for a work-related activity.

**Step 1 — Write down the task clearly.**

Before you can evaluate a task, you need to understand it. What is the output you need? A piece of text? A number? A recommendation? Who will use that output, and what will they do with it? A summary read only by you internally carries different stakes than advice delivered to a client.

Writing the task down also connects to the specification skills from topics 2.1–2.3: if you cannot state the task clearly, you are not ready to evaluate whether AI is appropriate for it.

**Step 2 — Run the privacy check.**

Ask yourself:
- Does the task require you to paste in names, health records, financial details, legal documents, or anything marked "confidential" or "for internal use only"?
- Would you be comfortable if this data appeared in a public search result?

If yes to either: identify whether your organisation has an approved, data-compliant AI platform — one that meets your profession's data-privacy rules. If there is no such platform available, stop. Do not use AI for this task. If there is an approved platform, proceed with it and not with a consumer tool [1][2].

**Step 3 — Run the precision check.**

Ask yourself:
- Is the output going to be acted on directly, without a human expert reviewing it first?
- Could a 5–10% error in the output cause physical harm, financial loss, or legal exposure for anyone?
- Is the task one that normally requires a qualification — such as a pharmacy technician calculating doses, or an engineer calculating loads — because the error tolerance is near zero?

If yes to any of these: mark the AI output explicitly as "draft for review only" and assign a qualified human to verify it against a validated, auditable source before it is acted on. Do not present an unverified AI output to an end user as a final answer [3].

**Step 4 — Run the legal accountability check.**

Ask yourself:
- Is the final output something that a licensed professional — a doctor, lawyer, financial adviser, engineer — must own under their professional registration?
- Would the output, if wrong, expose your organisation or a colleague to a regulatory investigation or lawsuit?

If yes: the licensed professional must actively review the AI's output and formally sign off on the final version with their name attached. It is not enough for them to glance at it; they must engage with it enough to take genuine ownership. The AI can assist with drafting, research, or summarising background material, but the human must be the accountable last step [1].

**Step 5 — Make the decision.**

| Outcome of checks | Decision |
|---|---|
| All three checks are "no" | AI use is likely appropriate. Proceed with a clear specification (topics 2.1–2.3). |
| Privacy check is "yes", others are "no" | Use only an approved data-compliant platform, or do not use AI. |
| Precision check is "yes", others are "no" | Use AI as a draft aid only; mandate expert human verification before acting on the output. |
| Legal accountability check is "yes" | Qualified human must own the final output. AI can assist; human must sign off. |
| Two or more checks are "yes" | Apply all relevant constraints simultaneously. Consider whether AI involvement helps at all. |

## 7. Real-World Patterns

**Healthcare.** Hospitals and clinics are beginning to explore AI tools for administrative tasks like appointment scheduling, medical note summarisation, and discharge letter drafting. Research into AI use in healthcare settings shows that data-privacy compliance remains a central challenge: tools used in a clinical environment must comply with HIPAA or equivalent national regulations, and any AI-generated clinical content requires physician review before it becomes part of a patient's record [3]. Studies examining AI adoption in healthcare settings have found that AI-generated clinical recommendations can appear plausible while containing factual errors that a trained clinician would catch — making the human review step non-negotiable [3]. The combination of sensitive health data, precision requirements, and mandatory physician accountability means all three checks simultaneously apply in most clinical AI use cases.

**Legal practice.** Law firms have begun adopting AI tools for searching large document repositories and drafting initial contract clauses. Professional associations — including the American Bar Association — have issued formal guidance warning lawyers that using standard consumer AI tools with client information creates real privacy and confidentiality risks [1][2]. The ABA's guidance makes clear that a lawyer's professional duty of confidentiality extends to third-party tools: pasting client data into a consumer AI tool may itself constitute a breach of that duty, regardless of what the AI does with the output [2]. Beyond privacy, law firms have experienced widely-reported incidents where AI tools fabricated court citations that were then submitted in legal filings — exposing the filing lawyers to judicial sanctions [1]. The lawyer remains responsible for the accuracy of every document filed; AI assistance does not transfer or reduce that responsibility [1][2].

**Financial services.** Automated tools assist financial analysts and advisers with tasks like risk modelling, portfolio summarisation, and regulatory report drafting. However, regulatory frameworks in most jurisdictions require that any investment recommendation given to a retail client be reviewed and approved by a qualified, licensed human adviser. An AI-generated portfolio recommendation cannot be handed directly to a client as professional advice — it must pass through a human adviser's review, and that adviser is accountable for the recommendation they ultimately deliver [1]. Financial data — account balances, transaction histories, personal financial circumstances — is also sensitive data under privacy regulations, so the privacy check applies alongside the accountability check.

**Software and engineering.** Even in a technology context, the three checks arise. A software team using AI to auto-generate code for a safety-critical system (such as medical device firmware or aviation control software) must have a qualified engineer review every line, because a precision error in safety-critical code can be catastrophic. An AI-generated error in a load-bearing structural calculation, if acted on without expert verification, poses risks that no disclaimer in an AI tool's terms of service would mitigate.

These four domains — healthcare, law, finance, and safety-critical engineering — consistently exhibit one or more of the three "do not use AI without constraint" signals. Recognising which signal applies in a given situation is the professional skill this topic is building.

## 8. Best Practices

**Do this:**

- Before using any AI tool professionally, run the three-question check (section 5.4).
- Use AI for drafting, brainstorming, and summarising low-stakes, non-confidential content.
- When AI assists on a task that touches precision or accountability, document that a human verified the output and name that person.
- Check your organisation's AI use policy before using any tool for work-related tasks.
- When in doubt about whether data is "sensitive", treat it as sensitive until you have confirmed otherwise with your manager or compliance team.

**Avoid this:**

- Pasting names, case details, medical records, or financial data into a consumer AI chat tool without approval.
- Presenting AI-generated professional advice — medical, legal, financial — to an end user without human review.
- Treating AI's confident-sounding output as automatically correct in high-stakes contexts.
- Assuming the AI tool "won't remember" your data — whether or not data is retained depends on the specific tool and its settings, not on your assumption [2].
- Using the quality of AI's output as justification for skipping the privacy check ("the summary was so good, it's fine") — the output quality is irrelevant to the data-sharing decision.

| Situation | Appropriate AI use? |
|---|---|
| Drafting an internal memo with no client names | Yes — low privacy risk, low stakes |
| Summarising a client's confidential contract | No — privacy risk [1][2] |
| Generating a rough estimate for a non-critical budget | Yes, if treated as a draft for review |
| Calculating a medication dosage for a patient | No — precision and accountability risk [3] |
| Brainstorming ideas for a marketing campaign | Yes — no sensitive data, low stakes |
| Writing a legal opinion for a client | No — accountability; needs licensed human review [1] |

## 9. Hands-On Exercise

Choose any two of the following scenarios — or substitute a task from your own work or study:

**Scenario A (health):** A practice assistant wants to use an AI tool to draft appointment-reminder letters. Each letter will include the patient's name, date of birth, and the name of the upcoming test.

**Scenario B (finance):** A junior analyst wants to use an AI tool to calculate a key revenue figure from raw data and include it in a client report that will be filed with a regulator.

**Scenario C (general):** A student wants to use an AI tool to brainstorm five essay-title ideas for a history assignment on the Industrial Revolution.

For each scenario you choose:

1. Run the three-question check from section 5.4.
2. Write your verdict: "AI use is appropriate" or "AI use requires constraint X" (state the constraint).
3. For any scenario that triggers a check, rewrite the task description so the AI's role is limited to drafting and the human verification step is explicit.

Compare your verdicts with a peer and discuss any case where you disagreed.

## 10. Key Takeaways

- AI is inappropriate when the task involves **sensitive or confidential data** — sharing that data with a consumer tool removes your control over it [1][2].
- AI is inappropriate when the task demands **exact precision** and a plausible-but-wrong answer would cause serious harm — AI's probabilistic output does not guarantee correctness [3].
- AI is inappropriate as the final decision-maker when the task requires **legal accountability** — only a licensed human professional can own that responsibility [1].
- The three-question check (privacy, precision, legal accountability) gives you a quick, repeatable way to decide whether AI is appropriate for any given task.
- Saying "no" to AI for certain tasks is not a failure — it is the professional judgment your specifications and verification skills are designed to support.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
