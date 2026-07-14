<!-- nav:top:start -->
[⬅ Previous: 9.8 — The Judgment Framework](../../9-8-the-judgment-framework-q2-can-i-verify-this-without-the-ai/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 9.10 — Acceptable error ➡](../../../4-defining-safe-boundaries/9-10-acceptable-error-defining-the-failure-threshold-tolerable-fo/artifacts/reading.md)
<!-- nav:top:end -->

---

# The Judgment Framework — Q3: Who is accountable if this fails?

## Overview

When an AI tool produces an output and something goes wrong, one question always surfaces: who is responsible? Q3 of the Judgment Framework asks you to answer that question *before* you act — not after. Naming the accountable person in advance is a practical safety check that keeps humans genuinely in the loop and prevents the common pattern where, after a failure, everyone points at everyone else and nothing gets fixed [2].

## Key Concepts

### Three words that sound the same but mean different things

These three terms are used interchangeably in everyday conversation, but Q3 depends on keeping them separate:

| Term | What it means | Who decides |
|---|---|---|
| **Accountability** | A named person who is expected to answer for an outcome — to explain what happened and address it | Determined before acting, by the people involved |
| **Liability** | A legal obligation to compensate for harm | Determined by courts, contracts, and statutes |
| **Blame** | A moral judgment that someone did something wrong | A social and ethical assessment |

Q3 asks only about accountability — not a legal verdict, not a moral condemnation. It is a forward-looking, practical question: *before I act, who is the named person who will be expected to answer if this goes wrong?* [2]

---

### The accountability chain

When an AI system produces an output and a human acts on it, accountability is not concentrated in one place. It is spread across four levels — what we call the **accountability chain**: the set of parties, from AI developer to end user, each of whom holds a defined portion of responsibility [1].

![Q3 accountability chain](./diagram.png)
*The four-level accountability chain, showing each party's scope of responsibility and the contrast between pre-decision naming and post-failure blame allocation.*

**Level 1 — The AI developer**

The developer is the company or team that built and trained the AI model. They are accountable for decisions baked into the model itself: what data it was trained on (relevant to the labelling bias and historical bias concepts from 9.6), what it was optimised for, what safeguards were built in, and what limitations were documented [1].

Their accountability covers the *class of outputs the model produces by design*. If the model was marketed as reliable for legal use without appropriate caveats, that scope expands. If limitations were clearly documented, that scope shrinks.

**Level 2 — The AI deployer**

The deployer is the organisation that takes the AI model and puts it into a real-world context — building a product, integrating it into a workflow, or offering it as a service. A hospital that installs an AI diagnostic assistant is the deployer. A bank that integrates a third-party AI credit-scoring model is the deployer.

The deployer's accountability covers the *appropriateness of the deployment*:
- Did they choose the right tool for the context?
- Did they set appropriate limits on what the AI can decide autonomously?
- Did they train staff?
- Did they disclose to affected parties that AI is being used?

Critically, the deployer cannot fully pass accountability to the developer by saying "we just used their model." Once an organisation deploys an AI system to affect real people, it accepts accountability for the consequences [1] [3].

**Level 3 — The operator**

The operator is the person within the deploying organisation who runs the specific task day-to-day — the paralegal using an AI document summariser, the nurse using an AI-assisted triage tool, the analyst flagging trading anomalies.

The operator's accountability covers *the specific action they took*: Did they apply appropriate judgment (Q1 and Q2 of the Judgment Framework) before acting on the output? Did they follow the organisation's procedures?

Operators are the humans in the room when a decision is made. They are the last checkpoint before the output affects the world [2].

**Level 4 — The end user**

The end user is the person who receives the AI-assisted output and acts on it — a patient following AI-generated health advice, a customer acting on an AI-generated recommendation.

End users are accountable for their own actions, but their accountability is limited by what they could reasonably have known — including whether they were even told AI was involved [3].

---

### Name accountability before acting, not after failure

After a failure, naming an accountable person becomes blame allocation — a political and often legal exercise that rarely produces learning. Before a decision, naming an accountable person is a safety check: it forces everyone to ask whether the right human has reviewed and authorised the action [2].

The practice is straightforward. Before acting on any AI output, ask: "Who is the person who has reviewed this and is prepared to answer for it if it is wrong?" If you can name that person — and they have been informed — you have established accountability. If you cannot, pause.

---

### Three criteria for a valid accountable person

Not just anyone can fill this role. For accountability to be real — not just a name on a form — three criteria must all be met [1] [2]:

1. **Authority to approve** — The person must have actual authority to say yes or no to the action. A junior employee who was told to forward an AI-generated report has not meaningfully approved it. The person who directed them is the authority.

2. **Knowledge of the risk** — The person must know that AI was involved and understand the key risks. They do not need to understand the AI's architecture, but they must know: this output came from an AI system, these are its known limitations, and here is what could go wrong. Accountability without knowledge is accountability in name only.

3. **Nameability** — The person must be identifiable after the fact. In automated systems where no human explicitly reviewed a specific decision, this still has an answer: the person who *authorised the deployment* of the automated pipeline is accountable for every output it produces [1].

---

### When no accountable person exists: escalate

What if you apply Q3 and cannot name a valid accountable person? The correct response is **escalation** — pausing the action and surfacing it to someone with the required authority and knowledge.

Escalation is not failure. It is the Judgment Framework working correctly. The steps are:

1. Stop the action.
2. Identify who in the organisation has the authority to approve it.
3. Brief that person: explain the AI output, its limitations, and what action is being proposed.
4. Get an explicit approval — not an implicit one.
5. Document that you escalated and why.

Acting without a named accountable person — because escalating is inconvenient — is precisely how large-scale AI failures occur. When everyone assumes someone else is responsible, no one is [2] [3].

---

### Accountability in fully automated systems

A frequent question: what if no human was involved in a specific decision at all? In automated pipelines — a fraud detection model that automatically freezes accounts, an AI scheduler that books appointments — Q3 still has an answer.

The accountable person for each automated decision is **the person who authorised the deployment of the pipeline** [1]. This is called **design-time accountability** — the accountability is assigned at the point when a human chose to let the system run autonomously.

This means that before an automated AI pipeline goes live, the organisation must explicitly record: who is authorising it, what its scope is, and what failure modes have been accepted. If that record does not exist, the pipeline should not be deployed.

---

### Three misconceptions to avoid

| Misconception | Why it is wrong |
|---|---|
| "The AI is responsible" | AI is not a legal person. It cannot be sued, disciplined, or learn from accountability. A tool produced the output; a human chose to act on it [1] [3]. |
| "Whoever clicked submit is responsible" | Accountability follows authority and knowledge, not mechanical action. The person with the power to approve — not the person who pressed the button — is accountable [2]. |
| "No one is responsible if it was automated" | Every automated system was authorised by a human at deployment. Automation compresses accountability into the design decision — it does not eliminate it [1] [3]. |

The third misconception is the most dangerous at scale. Automation bias (9.5) makes it feel natural: if the system ran on its own, surely it owns the outcome. But the accountability did not disappear — it was assigned when the deployment was approved.

## Worked Example

**Scenario:** A law firm deploys an AI legal research tool that drafts summaries of precedents. A junior associate uses the tool to produce a summary and sends it to a client without reviewing it. The summary incorrectly characterises a key ruling. The client makes a decision based on the incorrect summary.

**Applying Q3 step by step:**

1. **State the action explicitly** — "I am about to send a contract summary to a client based on AI-generated text."

2. **Who has authority to approve this action?** — A senior associate or partner, whose name appears on client communications for this matter.

3. **Does that person know AI was involved?** — In this case, no. The junior associate did not brief anyone. The approval was not meaningful.

4. **Check the three criteria:**
   - Authority: the partner has it, but was not consulted.
   - Knowledge: the partner was not told AI produced the summary.
   - Nameability: no one explicitly approved this output.

5. **Result:** No valid accountable person exists. The action should have been paused and escalated for explicit sign-off.

**Who is primarily accountable for the failure?**

The law firm as deployer — for putting the AI tool into a client-facing context without establishing a mandatory verification and approval step [1] [3]. The associate's accountability is real but secondary — they operated inside a system that did not require them to obtain approval. The developer's accountability is limited if the tool's limitations were clearly documented.

The lesson: deployers cannot outsource accountability to the AI developer. The moment an organisation puts an AI tool into a workflow that affects others, it accepts accountability for how that workflow was designed.

## In Practice

**Common patterns and the Q3 response:**

- **Medical discharge decisions** — An AI risk-scoring tool flags a patient as low-risk and the nursing team initiates discharge based on the flag. Q3: the accountable person is the named responsible clinician — the consultant or attending physician who examined the patient, reviewed the AI flag, and explicitly authorised discharge. The AI flag is a data point, not a decision. If the clinician was not consulted, accountability is diffuse and disputed [2].

- **Automated credit decisions** — A bank deploys an AI that automatically approves or declines credit applications with no human review. The model declines applications from a particular demographic at a higher rate — a feedback loop rooted in historical bias (9.6). Q3: no human was in the loop on each specific decision. The accountable parties are the risk officer and product lead who authorised the autonomous pipeline. Their accountability does not require that they intended the discriminatory outcome — they chose to deploy a system that made consequential decisions without human oversight [1].

**Practical checklist for applying Q3:**

- Before acting on any AI output, name the accountable person out loud or in writing.
- Confirm all three criteria: authority, knowledge, nameability.
- If any criterion is missing, escalate — do not proceed.
- For consequential decisions, make a brief record: who approved, when, on what basis, and with what known limitations acknowledged. Without a record, pre-decision accountability reverts to post-failure blame allocation [2].

**Watch for these failure modes:**

- Accountability pushed downward to the person with the least power and least context — the person who clicked the button.
- Accountability assumed to be the developer's problem because "it's their AI."
- Accountability skipped entirely in automated pipelines because "no human decided this."

## Key Takeaways

- **Accountability means answerability, not blame.** The accountable person is the named individual expected to explain and address an outcome. They need not have been at fault, but they must be identifiable and reachable.
- **The accountability chain has four levels** — developer, deployer, operator, end user — each with a different scope. Deployers cannot fully transfer their accountability to developers; operators cannot transfer theirs to deployers.
- **Name accountability before acting, not after failure.** After a failure, assigning accountability is blame allocation. Before acting, it is a safety check.
- **A valid accountable person must have authority to approve, knowledge of the risk, and the ability to be named.** If any of these is missing, escalate rather than proceed.
- **In automated systems, accountability attaches to the deployment decision.** When no human was in the loop on a specific output, the person who authorised the pipeline to run autonomously is accountable for its outputs.
- **When applying the Judgment Framework to an AI component you are analysing** — for any AI system you evaluate, you should be able to name who sits at each level of the accountability chain and who would be the valid accountable person for a given decision.

## References

1. HFW, "Legal liability for AI-driven decisions: when AI gets it wrong, who can you turn to?" <https://www.hfw.com/insights/legal-liability-for-ai-driven-decisions-when-ai-gets-it-wrong-who-can-you-turn-to/>
2. Salesforce, "AI Accountability." <https://www.salesforce.com/blog/ai-accountability/>
3. Stephen Rimmer, "Artificial Intelligence: Who is Accountable for Getting it Wrong?" <https://www.stephenrimmer.com/news/artificial-intelligence-who-is-accountable-for-getting-it-wrong/>

---
<!-- nav:bottom:start -->
[⬅ Previous: 9.8 — The Judgment Framework](../../9-8-the-judgment-framework-q2-can-i-verify-this-without-the-ai/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 9.10 — Acceptable error ➡](../../../4-defining-safe-boundaries/9-10-acceptable-error-defining-the-failure-threshold-tolerable-fo/artifacts/reading.md)
<!-- nav:bottom:end -->
