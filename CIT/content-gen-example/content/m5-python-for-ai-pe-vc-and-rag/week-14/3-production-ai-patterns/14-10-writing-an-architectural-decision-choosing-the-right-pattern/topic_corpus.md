---
topic_id: "14.10"
title: "Writing an architectural decision — choosing the right pattern for your system"
position_in_module: 2
generated_at: "2026-06-16T00:00:00Z"
resource_count: 5
---

# 1. Writing an architectural decision — choosing the right pattern for your system — Topic Corpus

## 2. Prerequisites

This topic is the capstone of week 14. It draws directly on three earlier topics:

- **14.4** — When to use RAG (the question: "Does the answer depend on data the model was never trained on?")
- **14.7** — The decision matrix: direct call → chained calls → RAG → agent (4-tier flowchart)
- **14.9** — Production trade-offs: token cost, latency (TTFT), the cost–latency–quality triangle, and reliability patterns

All vocabulary from 14.1–14.9 (vector databases, RAG pipeline, ReAct pattern, HITL, streaming, prompt caching, circuit breaker, etc.) is available without re-definition.

## 3. Learning Objectives

By the end of this topic, you will be able to:

1. Explain what an **architectural decision record (ADR)** is and why professional teams write them.
2. Name the five standard sections of an ADR: **Title**, **Status**, **Context**, **Decision**, and **Consequences**.
3. Write the **Context** section of an AI ADR by mapping a domain problem onto the decision matrix from 14.7.
4. Write the **Decision** section by naming the chosen tier (direct call / RAG / agent) and the primary reason in plain language.
5. Write the **Consequences** section by naming the cost–latency–quality trade-off from 14.9 that the chosen tier introduces.

## 4. Introduction

You have spent all of week 14 learning what the tools do. You know what a vector database stores. You know how RAG retrieves evidence before answering. You know how an agent loops through Reason → Act → Observe until the job is done. You know when each pattern fits and what it costs in tokens, latency, and operational complexity.

That knowledge lives in your head. An ADR (Architectural Decision Record) is how professionals move that knowledge out of their heads and into a document that survives project handovers, team changes, and the passage of time [1][4].

The ADR you will write in this topic is your capstone artifact for the course. It is one paragraph — the minimum professional-grade form — that answers a single question: "Why did we choose this AI pattern for our system, and what does it cost us?" Every concept you need already lives in 14.4–14.9. This topic teaches you how to assemble those concepts into a structured, readable record.

The lab activity (Journal Entry #9) asks you to make this decision for your own domain system and write it down. This corpus gives you the template, the rules, and a worked example to copy from.

## 5. Core Concepts

### 5.1 What is an ADR?

An **ADR (Architectural Decision Record)** is a short, plain-text document that records one significant technical decision: what was decided, why, and what the consequences are [4].

The format was introduced by Michael Nygard in 2011 [4]. The core insight is simple: **code shows you what a system does, but it rarely shows you why it was designed that way**. When a new engineer joins the team six months later and asks "why are we using RAG here instead of just asking the model directly?", the ADR answers that question in two minutes instead of requiring a meeting.

Key properties of an ADR:

- **One decision per record.** Each ADR covers exactly one design choice. This keeps records short and searchable.
- **Plain text.** ADRs live in a folder in your source-code repository (typically a folder called `docs/decisions/`). They are version-controlled alongside the code.
- **Append-only.** You do not edit an old ADR when the decision changes. You write a new ADR that supersedes the old one. This preserves the history of why decisions evolved.
- **Lightweight.** The Nygard format fits on one page. It is not a formal specification document — it is a decision log [1].

The ADR format has been adopted widely. AWS recommends it for any system component maintained by more than one engineer [2]. Teams at data-intensive companies keep entire ADR libraries on GitHub [1].

### 5.2 The five-section ADR template

Every ADR has five sections [1][4]:

| Section | What it contains |
|---|---|
| **Title** | A short noun phrase naming the decision. Example: "Use RAG for university FAQ chatbot." |
| **Status** | One word: `Proposed`, `Accepted`, `Deprecated`, or `Superseded`. Most ADRs you write start as `Accepted`. |
| **Context** | The problem you were facing. Why did a decision need to be made at all? What constraints existed? |
| **Decision** | What you chose to do, stated clearly. "We decided to…" — past tense, one or two sentences. |
| **Consequences** | What changes as a result of this decision. What gets better? What gets harder? What will you need to monitor? |

The five sections always appear in this order. Keeping the structure consistent means any teammate can scan any ADR in the same way, every time.

### 5.3 Writing the Context section for AI systems

The **Context** section is where you describe the problem your system is solving and the constraints that shaped the decision [3][5].

For an AI system, the Context section should answer three questions drawn from the decision matrix (14.7):

1. **What is the domain problem?** State it in one sentence. Example: "Students ask questions about university policies, deadlines, and procedures."
2. **Is the answer in data the model was never trained on?** If yes, RAG is a candidate. If no, a direct call might be enough.
3. **Does answering require multi-step reasoning, tool use, or taking actions?** If yes, an agent is a candidate.

You are not yet saying what you decided. You are describing the situation that made a decision necessary.

A weak Context section says: "We needed to pick an AI pattern." A strong Context section says: "The system must answer questions about our company's internal HR policies, which change quarterly and are not part of any public dataset. The system must not take actions — it only provides answers."

The second version makes the decision almost obvious to a future reader before they even get to the Decision section.

### 5.4 Writing the Decision section

The **Decision** section names the tier you chose and gives the primary reason [3].

Structure it as:

> "We decided to use **[tier name]** because **[primary reason in one sentence]**."

For an AI system, also state:
- **If RAG:** the retrieval scope (what corpus you are searching) and the approximate model tier (e.g., a mid-tier model for generation).
- **If an agent:** the planning pattern (e.g., ReAct loop) and the toolset.
- **If a direct call:** why the simpler pattern was sufficient.

Rules for the Decision section:
- Use past tense ("We decided to…"). ADRs record completed decisions, not proposals in progress.
- Give **one primary reason**. If you list five reasons, the reader cannot tell which one was decisive. Pick the most important.
- Do not justify the decision only by listing benefits. A decision with only upsides is a decision that wasn't thought through carefully [5].

### 5.5 Writing the Consequences section

The **Consequences** section is where you name the trade-offs [2][3].

For an AI system, use the cost–latency–quality triangle from 14.9 as your frame. Every tier creates a specific profile:

| Tier | What typically gets better | What typically gets harder |
|---|---|---|
| Direct call | Low cost, low latency, simple stack | No access to private or current data; answers limited to trained knowledge |
| RAG | Grounded answers, reduced hallucination | Higher cost per request (embedding + retrieval + generation), longer latency |
| Agent | Can complete multi-step tasks | Highest cost, highest latency, unpredictable loop count, harder to test |

Your Consequences section should name:
1. **What gets better** as a result of this choice.
2. **What gets harder or more expensive** as a result of this choice.
3. **What reliability pattern you will need** — for example: streaming to reduce perceived latency, prompt caching to reduce cost, circuit breaker to handle provider outages, or human-in-the-loop review for irreversible actions.

A Consequences section that only lists benefits is incomplete. The discipline of listing what gets harder is what makes an ADR valuable — it forces honest thinking before the system is built.

## 6. Implementation

### Complete worked example: University FAQ Chatbot ADR

Below is a complete five-section ADR for a fictional university chatbot. Read it as a template you can adapt.

---

**ADR-001: Use RAG for university FAQ chatbot**

**Status:** Accepted

**Context:**
Students ask questions about university policies, admissions deadlines, course registration, and financial aid. These policies change each semester. The answers are not part of any publicly available training dataset. The system only needs to retrieve and present information — it does not take any actions on behalf of the student. Response time under 3 seconds is a requirement. The cost per question must stay below $0.01 to fit the department budget.

**Decision:**
We decided to use a RAG (Retrieval-Augmented Generation) pipeline backed by a vector database of university policy documents, with a mid-tier language model for generation. RAG was chosen because the answers depend on internal documents that no model has been trained on, and the system does not need multi-step reasoning or tool use.

**Consequences:**
Answers will be grounded in the actual policy documents, which reduces hallucination compared to a direct call to the model. Each request will cost more than a direct call because it requires an embedding step and a similarity search before generation. To keep latency within the 3-second target, we will use streaming for the generation step. We will need to monitor retrieval quality (are the top-k chunks actually relevant?) and set up re-indexing when policy documents are updated.

---

### Side-by-side skeleton comparison

The template structure is the same for all three tiers. Only the content of Context, Decision, and Consequences changes.

| Section | Direct call | RAG | Agent |
|---|---|---|---|
| **Title** | "Use direct LLM call for …" | "Use RAG for …" | "Use ReAct agent for …" |
| **Status** | Accepted | Accepted | Accepted |
| **Context** | Answer is in the model's trained knowledge; no private data; no actions needed. | Answer depends on un-trained private data; retrieval is the bottleneck. | Task requires multi-step reasoning, tool calls, or taking actions. |
| **Decision** | "We decided to use a direct call because the model already knows the domain and no retrieval is needed." | "We decided to use RAG because the answers depend on internal documents the model was never trained on." | "We decided to use a ReAct agent because completing the task requires calling external tools in sequence." |
| **Consequences** | Lowest cost and latency; risk of stale answers if the domain changes. | Grounded answers; higher cost; must monitor retrieval quality and re-index when documents change. | Most capable; highest cost and latency; must cap loop iterations; consider HITL for irreversible actions. |

## 7. Real-World Patterns

**ADR libraries on GitHub.** Engineering teams at data-intensive companies maintain folders of ADRs in their source repositories, following the Nygard template [1]. Searching GitHub for `docs/decisions` or `adr` turns up hundreds of real examples. The `adr.github.io` site provides a command-line tool to scaffold new ADRs from a template [1].

**AI-specific ADR fields.** The original Nygard format was written for general software systems [4]. Teams building AI systems have started adding two fields not in the original template: a **"model tier"** field (which model family was chosen) and an **"estimated cost per request"** field. These additions reflect the fact that AI systems have a cost structure that traditional software does not [3].

**AWS production mandate.** AWS prescriptive guidance recommends ADRs as mandatory for any system component that will be maintained by more than one engineer [2]. The reasoning: the cost of a poorly understood decision compounds over time. An ADR written in 30 minutes today can save hours of archaeology next year.

## 8. Best Practices

- **One decision per ADR.** Do not bundle "we use RAG AND we use streaming" in a single record. These are separate decisions with separate consequences. Write two ADRs [1][4].

- **Write for the future teammate who wasn't in the room.** Assume zero context. A reader who wasn't in the original discussion should be able to read your ADR and understand not just what was decided but why the alternatives were rejected [5].

- **Use past tense in the Decision section.** "We decided to…" — not "We will use…" or "The system should…" Past tense signals that the decision is final, not still under discussion [4].

- **State trade-offs explicitly.** Avoid writing a Consequences section that only lists benefits. If the choice has no downsides, you haven't thought about it hard enough. An ADR that lists only upsides is an ADR that will mislead the next engineer [5].

- **Date and status every ADR.** Every record needs a date (when the decision was made) and a status (`Proposed`, `Accepted`, `Deprecated`, or `Superseded`). Without these, a reader cannot tell if the ADR is current or years out of date [1][2].

- **Do not delete superseded ADRs.** When a decision changes, write a new ADR and mark the old one as `Superseded by ADR-00N`. The history of why decisions evolved is often as valuable as the decisions themselves.

## 9. Hands-On Exercise

This exercise IS the lab activity (Journal Entry #9). Complete all five steps. Your final written ADR should be 80–120 words.

**Your task:** Write a complete ADR for the domain system you have been designing this week.

**Steps:**

1. **Context (2–3 sentences):** Describe the problem your system solves. Name the data source the answers must come from. State whether the system takes any actions or only provides information.

2. **Pick a tier from the decision matrix (14.7):** Work through the flowchart. Does the answer depend on data the model was never trained on? Does the task require multi-step reasoning or tool calls? Write down which tier the matrix points to.

3. **Decision (1 sentence):** "We decided to use [tier] because [one primary reason]."

4. **One trade-off from 14.9:** Name one thing that gets harder or more expensive because of your choice (e.g., higher cost per request for RAG, unpredictable loop count for an agent).

5. **One reliability pattern:** Name one production pattern from 14.9 you will need (e.g., streaming, prompt caching, circuit breaker, HITL).

When you are done, you will have a complete ADR — the same artifact professional engineers write before they build.

## 10. Key Takeaways

- An **ADR (Architectural Decision Record)** is a short plain-text document that records one design decision — what was chosen, why, and what it costs. It survives team rotation and answers "why was this built this way?" for future teammates.

- Every ADR has five sections in order: **Title**, **Status**, **Context**, **Decision**, **Consequences**. Keeping the structure consistent makes ADRs scannable across a codebase.

- The **Context** section for an AI ADR maps the domain problem onto the decision matrix from 14.7: Is the answer in un-trained data? Does the task need multi-step reasoning or actions?

- The **Decision** section names the tier (direct call / RAG / agent) in one sentence using past tense ("We decided to…") and gives a single primary reason.

- The **Consequences** section must name both what gets better and what gets harder. Use the cost–latency–quality triangle from 14.9 as the frame, and name one reliability pattern you will need.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
