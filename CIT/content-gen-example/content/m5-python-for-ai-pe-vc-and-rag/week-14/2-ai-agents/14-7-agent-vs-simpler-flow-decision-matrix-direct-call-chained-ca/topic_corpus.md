---
topic_id: "14.7"
title: "Agent vs simpler flow — decision matrix: direct call → chained calls → RAG → agent"
position_in_module: 3
generated_at: "2026-06-15T00:00:00Z"
resource_count: 5
---

# 1. Agent vs Simpler Flow — Decision Matrix: Direct Call → Chained Calls → RAG → Agent — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **14.4 — When to use RAG.** You already know the RAG decision rule: use retrieval-augmented generation when the answer depends on data the model was not trained on — fresh data, private data, or high-precision data. RAG is one tier in the decision matrix here; it is referenced, not re-taught.
- **14.5 — Agent anatomy — LLM + memory + tools + planning loop.** You already know what an AI agent is, what its four components are, and how the planning loop works.
- **14.6 — The ReAct pattern — Reason, Act, Observe, Repeat.** You already know how an agent cycles through Thought → Action → Observation steps using tools.

All prior-topic vocabulary — RAG, vector database, embedding, hallucination, parametric memory, AI agent, LLM (Large Language Model) core, tools, planning loop, ReAct pattern, Thought step, Action step, Observation step — is used freely without re-definition.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Name and describe the four tiers of AI system complexity: direct call, chained calls, RAG, and agent.
2. State the defining criterion for each tier — what makes a task belong to that tier and not a simpler one.
3. Apply a four-question decision matrix to a new task description and identify the correct tier.
4. Explain why starting with the simplest tier that works is the right engineering default.
5. Recognize the two most common design mistakes: over-engineering (reaching for an agent when a direct call suffices) and under-engineering (skipping RAG when the model is likely to hallucinate).

## 4. Introduction

You now know that RAG exists, and you know that AI agents exist. But here is the question no one has asked yet: *when do you actually need them?*

Imagine you are building a product for your final capstone project. You could wire up an agent with tools, a vector database, a memory store, and a ReAct loop — but that is a lot of moving parts. If the same job can be done by sending a single prompt to an LLM and reading the response, adding all that complexity would be like hiring a full construction crew to hang one picture frame.

The opposite mistake is also common. Developers sometimes send every question straight to a bare LLM — no retrieval, no structure — and then wonder why the answers are confidently wrong. The model answers from its training data, which may be months or years out of date, or may never have included the private documents the user cares about.

The answer to both mistakes is the same: match the complexity of your system to the complexity of the task. This topic gives you a structured tool for doing exactly that — a **decision matrix** with four tiers, each paired with a clear criterion for when it is the right choice [3][4].

## 5. Core Concepts

### 5.1 The Four Tiers — An Overview

Think of the four tiers as a ladder. Each rung adds capability, but also adds cost, latency, and the chance that something goes wrong. The rule is: start at the bottom rung. Only climb when you have a specific reason to [3][5].

| Tier | What it does | Added complexity vs tier below |
|---|---|---|
| **Direct call** | One prompt in, one response out | — (baseline) |
| **Chained calls** | Multiple LLM calls in sequence | Prompt design, output parsing |
| **RAG** | Retrieve documents, inject into prompt, then call LLM | Vector database, embedding, retrieval pipeline |
| **Agent (ReAct loop)** | LLM + tools + multi-step loop | Tool integration, loop management, error handling |

The next four sub-sections define each tier precisely.

---

### 5.2 Tier 1 — Direct Call

**Direct call** — a single prompt sent to an LLM, followed by a single response. There is no memory between calls, no external tools, no chaining. You type a question; the model answers.

**When it works:** The task is self-contained and the correct answer already exists in the model's training data.

Examples:
- "Summarise this paragraph." (The paragraph is pasted in the prompt.)
- "Translate this sentence into French."
- "What is a for-loop?" (General programming knowledge — no private data needed.)
- "Give me five ideas for a project name."

**Why it is the default starting point:** It is the cheapest, fastest, and most predictable option. There are no moving parts to break [1][2][3].

**When it fails:** The question requires information the model was not trained on — recent events, private documents, or real-time data. The model will answer anyway, often confidently, but the answer may be wrong. That failure mode is hallucination, which you encountered in topic 14.3.

---

### 5.3 Tier 2 — Chained Calls

**Chained calls** — a sequence of two or more LLM calls where the output of one call becomes the input of the next. No external tools. No retrieval. Just LLM → LLM → LLM.

**When it works:** The task has decomposable sub-steps that the model can handle individually, but trying to do everything in one massive prompt produces low-quality results.

A simple example: you want to (1) extract the key claims from a long document, then (2) fact-check each claim for logical consistency, then (3) write a critique. You could try to do all three in one prompt, but each step is better when it is isolated. Chained calls let you separate the steps without involving any external data source [3].

Another example: a multi-stage writing pipeline. Step 1: ask the LLM to create an outline. Step 2: pass the outline back to the LLM and ask it to draft each section. Step 3: pass the draft back and ask for a revision pass.

**The key signal:** Ask yourself — "Are all the facts the model needs already in its training data or in the prompts I am sending it?" If yes, chaining may be enough. If the model needs to look something up outside itself, you need at least Tier 3.

**Why not use an agent here?** Because the steps are known in advance and can be scripted. You do not need a loop that decides its own next move. Agents (Tier 4) are for tasks where the steps cannot be fully planned ahead of time [5].

---

### 5.4 Tier 3 — RAG

**RAG (Retrieval-Augmented Generation)** is the pattern covered in topics 14.1–14.4. A quick reference: the user's question is embedded (turned into a vector), the vector is used to search a database for relevant documents, and those documents are injected into the LLM's prompt before the model generates its answer.

This topic does not re-teach RAG internals. It positions RAG within the decision matrix.

**When it works:** The answer depends on data the model was not trained on. Three signals from topic 14.4 apply:

1. **Freshness signal** — the answer changes over time (news, prices, policies).
2. **Private data signal** — the answer lives in documents the model has never seen (company HR policy, product manuals, legal contracts).
3. **Precision signal** — the answer must cite a specific source, not a plausible-sounding paraphrase.

When any of those three signals is present, a bare LLM (Tier 1 or 2) will hallucinate. RAG gives the model real documents to read, which grounds its answer in evidence [1][4].

**The key distinction from Tier 4 (agent):** RAG is still a one-shot or low-step retrieval. The model retrieves, reads, and answers. It does not loop, does not call multiple heterogeneous tools, and does not plan. If you need multiple retrievals interleaved with other tool calls, that is an agent task [5].

---

### 5.5 Tier 4 — Agent (ReAct Loop)

An **agent** (covered in topics 14.5 and 14.6) is an LLM that can use tools and loop: it reasons about what to do next, calls a tool, reads the result, reasons again, and repeats until the task is done. The ReAct pattern is the most common structure for this loop.

**When it works:** One or more of the following is true:

- **Real-time data is needed across multiple steps.** The agent must look up a live stock price, then check a news headline, then do a calculation — three different tool calls, order determined by what it finds.
- **Multiple heterogeneous tools are required.** The task requires combining a search engine, a code interpreter, a database query, and an email sender — tools of completely different types.
- **Steps cannot be scripted in advance.** You do not know how many steps the task will take or which tools will be called in what order. The agent decides as it goes.
- **The model needs to recover from errors.** If a tool call fails, the agent can reason about why and try an alternative approach [1][2][3][5].

**Why not use an agent for everything?** Because every added step is a place where something can go wrong. Agents are slower, more expensive per call, harder to debug, and less predictable than a direct call or even RAG. The ReAct loop you learned in topic 14.6 is powerful — but power is only useful when the task actually requires it [3][4].

---

### 5.6 The Decision Matrix

The decision matrix is a set of four yes/no questions. Answer them in order. Stop at the first "yes" and use that tier.

**Question 1:** Is the answer in the model's training data, and does it not need to be pinned to a specific external source?
- **Yes → Direct call (Tier 1).**
- No → continue to Question 2.

**Question 2:** Is the task decomposable into sequential LLM sub-steps, with all facts already available in training data or in the prompts?
- **Yes → Chained calls (Tier 2).**
- No → continue to Question 3.

**Question 3:** Does the task require grounding in external documents or data that the model was not trained on — private data, fresh data, or high-precision citations?
- **Yes → RAG (Tier 3).**
- No → continue to Question 4.

**Question 4:** Does the task require multiple heterogeneous tools, real-time data across several steps, or a dynamic number of steps that cannot be scripted?
- **Yes → Agent (Tier 4).**
- No → reconsider whether an LLM-based system is even the right solution.

A visual summary of the four questions and their branching outcomes is in the diagram for this topic.

---

### 5.7 Worked Examples — Applying the Matrix

**Scenario A:** A user asks, "What is the capital of France?"

- Question 1: Is the answer in training data? Yes. Paris is general knowledge.
- **Result: Direct call.** One prompt, one answer.

---

**Scenario B:** A user pastes a 5,000-word article and asks: "Summarise this, identify the three strongest arguments, then draft an email to my professor about it."

- Question 1: In training data? The article is the input — but no external lookup is needed.
- Question 2: Decomposable LLM sub-steps with all facts in the prompts? Yes — summarise → identify arguments → draft email.
- **Result: Chained calls.** Three prompts in sequence. No retrieval, no tools.

---

**Scenario C:** A customer support chatbot answers questions about a company's 500-page internal product documentation — PDFs the LLM was never trained on.

- Question 1: In training data? No — specific product details are private.
- Question 2: Fixed LLM sub-steps? Not the bottleneck — the model lacks the content.
- Question 3: Needs external documents the model wasn't trained on? Yes.
- **Result: RAG (Tier 3).** Embed the PDFs, store in a vector database, retrieve on each query, inject into prompt.

---

**Scenario D:** A research assistant that takes a question, searches the web for recent papers, checks citation counts, runs a sentiment analysis on abstracts, and compiles a structured report — with the number of papers and tools varying by query.

- Question 1: In training data? No — live papers needed.
- Question 2: Fixed LLM sub-steps? No — steps vary by query.
- Question 3: Static document retrieval? No — the web is live.
- Question 4: Multiple heterogeneous tools, dynamic steps, real-time data? Yes.
- **Result: Agent (Tier 4).**

## 6. Implementation

Apply the decision matrix as a checklist before you start building. Walk through the four questions in order and stop as soon as you reach a "Yes."

**Decision matrix checklist**

1. **Training data sufficient?**
   - Ask: "Can a well-prompted LLM answer this correctly, without looking anything up, at least 95% of the time?"
   - Yes → use a **direct call**. Stop.
   - No → go to step 2.

2. **Fixed, scriptable LLM sub-steps?**
   - Ask: "Can I write out every step in advance, where each step is just prompting the LLM and passing the result forward — with no external data lookups?"
   - Yes → use **chained calls**. Stop.
   - No → go to step 3.

3. **External data needed (private, fresh, or precision)?**
   - Ask: "Does the answer depend on documents the model was never trained on, or data that changes frequently, or a specific source that must be cited?"
   - Yes → use **RAG**. Stop.
   - No → go to step 4.

4. **Multiple heterogeneous tools or dynamic steps?**
   - Ask: "Does the task require combining different kinds of tools in an order I cannot predict in advance?"
   - Yes → use an **agent**. Stop.
   - No → reconsider whether the task is well-defined enough for an LLM at all.

**After picking a tier, write a one-paragraph justification.** State which question stopped the walk, what the evidence was, and why the tier above is unnecessary. This is the form of the lab activity for this week.

Note: building RAG pipelines and coding agents are Semester 2 topics. This matrix tells you *which* tier to choose; the build skills come later [1][2].

## 7. Real-World Patterns

Real products use each tier, and the tier chosen reflects a deliberate decision, not a default [3][4][5].

**FAQ chatbot — Direct call**

A company publishes a static FAQ page with 40 questions and answers that rarely change. The developer embeds the entire FAQ in the system prompt and lets users ask questions. The LLM reads the FAQ from the prompt and answers. No vector database, no tools, no loop. Direct call is correct.

If the FAQ grew to 10,000 questions — too large for a single prompt — the architecture would graduate to RAG. But for 40 items, a direct call is simpler and cheaper.

---

**Internal knowledge base assistant — RAG**

A mid-size company has five years of internal policy documents, meeting notes, and engineering runbooks — thousands of PDFs that the LLM has never seen. Employees want to ask natural-language questions and get accurate, sourced answers. The answer depends entirely on private documents. RAG is the correct tier: embed the documents, store vectors, retrieve on query, inject into prompt, answer with citations [1][4].

Building an agent here would add latency and complexity for no benefit — the task is retrieval plus one LLM call, not multi-tool orchestration.

---

**Multi-step writing pipeline — Chained calls**

A content team uses an LLM to help produce blog posts. The pipeline is: (1) prompt the LLM with a topic to generate an outline, (2) prompt it again with the outline to write each section, (3) prompt it with the draft for a polishing pass. All facts needed are in the model's training data or in the prompts. No external documents, no tools, no dynamic branching. Chained calls are right. An agent would be wasteful [3].

---

**Automated order-fulfillment coordinator — Agent**

An e-commerce company wants a system that (1) receives a customer complaint email, (2) looks up the order in a database, (3) checks the carrier's live tracking API, (4) decides whether to issue a refund or escalate, and (5) sends a reply. The steps depend on what the lookup and tracking return — sometimes two tool calls, sometimes six. The order of steps is not scriptable in advance.

This is an agent task. The LLM needs multiple heterogeneous tools (email parser, database query, carrier API, decision logic, email sender) and the step count varies by case [2][3][5]. Using only RAG would not work — the task requires live API calls, not document retrieval.

## 8. Best Practices

**Start at the simplest tier. Move up only when criteria are met.**

The most common engineering mistake is reaching for agents or RAG because they seem more impressive, not because the task requires them. An agent that does what a direct call could do is slower, costs more per query, and has more failure modes [3][4]. Prototype as a direct call first. If output quality is acceptable, ship it. If the model hallucinates because it lacks current data, add RAG. If RAG is not enough because the task requires multi-tool orchestration, add an agent.

**Measure before upgrading tiers.**

Before deciding that a task needs RAG, test whether the model's training data is actually insufficient. Run 20 representative queries and check the outputs. If the error rate is low and the answers are grounded, a direct call may be enough. Evidence beats intuition.

**One tier change at a time.**

When something breaks, changing the entire architecture at once makes it hard to isolate the cause. Add one component at a time — a retrieval step, then a second tool, then a loop — so you can identify what each change contributes.

**Do not confuse "complex prompt" with "chained calls."**

A single prompt with many instructions and examples is still a direct call — one prompt, one response. Chained calls means multiple separate LLM invocations, each with its own context, where results are passed forward. This distinction matters because chained calls require output parsing and error handling that a single prompt does not.

**Understand cost and latency before committing.**

A direct call typically completes in under a second. A RAG pipeline adds retrieval latency (often 100–500 ms). An agent with five tool calls may take 5–15 seconds per query. For a real-time chat product, that latency difference affects user experience. Choose the tier your users can tolerate, not just the tier with the most capable output [3][5].

**High-stakes, irreversible actions require a different consideration.**

When an agent might take an action that cannot be undone — sending an email, placing an order, deleting a file — a human checkpoint may be needed before the action executes. That concern is the topic of 14.8, immediately after this one. This matrix tells you when to reach for an agent; 14.8 tells you when to pause before the agent acts.

## 9. Hands-On Exercise

This exercise is the lab activity for the week. It connects the decision matrix to your capstone project domain.

**Step 1.** Describe one core user interaction your capstone domain system must support. Write it as a plain sentence: "A user asks ___ and the system should ___."

**Step 2.** Walk through the four decision matrix questions in order. For each question, write one sentence: your answer (Yes/No) and your reasoning.

**Step 3.** Identify which tier the matrix points to (direct call, chained calls, RAG, or agent).

**Step 4.** Write a one-paragraph architectural decision. Include: (a) the tier you chose, (b) which decision matrix question stopped the walk, (c) one sentence on why the tier above is unnecessary, and (d) one sentence acknowledging any risk or limitation of your choice.

Example format (write for your own domain — do not copy this content):

> "For the student FAQ feature, the decision matrix points to RAG. The walk stopped at question 3: the answers depend on internal university documents (course catalogs, academic policies) that the model was never trained on. An agent is unnecessary because the task is single-turn retrieval, not multi-tool orchestration. The main risk is that newly published policies may not be indexed in time if the vector database is not refreshed regularly."

## 10. Key Takeaways

- **There are four tiers of AI system complexity**: direct call, chained calls, RAG, and agent. Each tier adds capability and adds complexity.
- **The decision matrix points you to the correct tier** by walking four questions: Is the answer in training data? Are the steps fixed and LLM-only? Does the task need external documents? Does it need multiple tools across dynamic steps?
- **The cardinal rule: use the simplest tier that works.** An agent that does what a direct call could do is slower, costlier, and harder to debug.
- **Over-engineering and under-engineering are both defects.** Reaching for an agent when a direct call suffices is over-engineering. Sending every question to a bare LLM when the model lacks the relevant data is under-engineering.
- **RAG and agents are tools for specific problems, not defaults.** RAG solves the private/fresh/precision data problem. Agents solve the multi-tool, dynamic-step problem. Neither is needed unless the criteria are met.

## 11. Next Steps

Topic 14.8 covers when NOT to use agents — specifically, when an agent might take a high-stakes, irreversible action and why a human checkpoint is required. The decision matrix in this topic tells you when to reach for an agent; 14.8 tells you when to pause before that agent acts.

_System-derived from the next entry in curriculum/sequence.md._
