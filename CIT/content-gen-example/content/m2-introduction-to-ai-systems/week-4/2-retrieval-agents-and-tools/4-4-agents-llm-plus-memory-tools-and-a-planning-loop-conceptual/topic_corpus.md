---
topic_id: "4.4"
title: "Agents — LLM plus memory, tools, and a planning loop (conceptual introduction)"
position_in_module: 2
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. Agents — LLM plus memory, tools, and a planning loop (conceptual introduction) — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **4.1 — Foundation models — trained once at scale, usable for many tasks:** introduced the foundation model, the idea that a model is trained once on broad data and can generalise to many tasks, and the concept of adaptation. These terms are used here without re-definition.
- **4.2 — Fine-tuning — adapting a foundation model on domain-specific data:** introduced hallucination and the baseline expectation that a model responds to a single question and produces a single answer.
- **4.3 — Retrieval-Augmented Generation (RAG):** introduced the retrieve-augment-generate pipeline, the idea of supplementing an LLM with an external knowledge source at query time, and prompt augmentation. RAG is referenced here as one specific tool an agent may use.

Together, topics 4.1–4.3 have built the picture of an LLM as a powerful but essentially passive system: given a question, it produces an answer. Topic 4.4 asks: what if we put an LLM at the centre of something that can act, remember, and plan?

## 3. Learning Objectives

By the end of this topic, you should be able to:

1. Define an AI agent in plain language and explain how it differs from a standalone large language model (LLM).
2. Identify and describe the four core components of an agent: the LLM core, memory, tools, and the planning loop.
3. Explain the observe-think-act cycle and trace how a simple task moves through it step by step.
4. Distinguish short-term memory from long-term memory in the context of an agent and give an example of each.
5. Give two examples of tools an agent might use and explain what a tool enables that an LLM alone cannot do.
6. Recognise what an agentic workflow is and identify two real-world systems that rely on one.

## 4. Introduction

Think about the difference between reading a recipe and actually cooking a meal. Reading the recipe is a single act of generating text — useful, but passive. Cooking involves a sequence of steps: checking the oven, adjusting seasoning, looking at the time, going back to the recipe when you forget a step. It requires memory, tools (pots, timers, a thermometer), and a loop of observing, deciding, and acting.

Until recently, AI systems worked like the recipe reader: given a question, produce a response; one turn, one answer, done. The foundation models introduced in topic 4.1 are extraordinarily capable at that one-turn task — summarising, translating, explaining, drafting. But there is a large class of real-world jobs that cannot be done in a single response. Planning a research project. Booking travel across multiple websites. Monitoring a system and responding when something goes wrong. Debugging a business process. These jobs require a system that can take a sequence of actions, use external tools, remember what has happened so far, and keep going until the task is complete. [1]

That is what an **AI agent** is. An agent puts a foundation model at the centre of an active, multi-step process. The model is no longer just answering questions — it is deciding what to do next, choosing which tool to use, observing the result, and continuing until the task is finished. [1][2]

This topic introduces agents at a conceptual level. You will see the four components that every agent needs and understand the basic cycle that connects them. The detailed design of agents — how to build them, how to coordinate multiple agents working together, how to evaluate their behaviour — is covered in Week 14 and in Year 2 of this programme. This topic gives you the vocabulary and mental model to recognise agents when you encounter them in the 2026 AI landscape. [1]

## 5. Core Concepts

### 5.1 What makes something an agent?

The word "agent" in everyday English means something that acts on behalf of someone else — a travel agent books your flights, a real estate agent finds your home, a sports agent negotiates your contract. In AI, the word means something similar: a system that acts on behalf of a user, in the world, to get a task done. [1][2]

Three properties separate an AI agent from a plain LLM:

**1. It takes actions, not just produces text.**
A standalone LLM generates a response and stops. An agent can do things: search the web, send an email, read a file, book an appointment, write to a database. These actions have effects beyond the conversation window. [1]

**2. It runs multiple steps in a loop.**
A standalone LLM responds once per prompt. An agent continues working — deciding what to do next, doing it, checking the result, deciding again — until the task is complete or it runs into a situation where it needs human input. [2]

**3. It has memory.**
A standalone LLM, by default, knows only what is in its current context window (the block of text the model can see at any given moment). An agent maintains memory across steps and, in more sophisticated designs, across separate sessions. It can refer back to earlier parts of its work without having everything re-stated each time. [1][2]

An agent that has all three of these properties — action, looping, memory — can carry out multi-step, open-ended tasks that no single LLM prompt could complete. [1]

### 5.2 The four components

Every AI agent, regardless of its specific design, consists of four fundamental components: the **LLM core**, **memory**, **tools**, and the **planning loop**. [1][2][3]

Think of the LLM core as the brain, memory as the notepad, tools as the hands, and the planning loop as the rhythm that keeps everything moving.

#### 5.2.1 The LLM core — the reasoning engine

The **LLM core** is a foundation model (as introduced in topic 4.1). Its role inside an agent is to reason and decide. At each step, the LLM core receives a description of the current situation — the task, the memory of what has happened so far, what the last action returned — and produces a decision: what should happen next? [1][3]

The LLM core does not perform actions itself. It reasons about actions, chooses them, and generates instructions for the rest of the system to carry out. This division is important: the model contributes intelligence and language; the tools and loop contribute capability and persistence. [1]

Because the LLM core is a foundation model, it brings everything a foundation model can do: it can read, summarise, draft, translate, classify, reason about what it has been shown, and generate structured instructions for the next step. The agent structure does not replace the LLM — it gives the LLM a stage on which to act. [2]

#### 5.2.2 Memory — what the agent remembers

**Memory** is how an agent retains information across steps and time. Without memory, each step of the planning loop would start from scratch, as if nothing had happened before. Memory is what allows an agent to say: "I already checked the inventory; I do not need to do that again." [2]

There are two broad kinds of memory in an agent:

**Short-term memory** — sometimes called working memory or in-context memory — holds everything the agent is currently working with: the original task, the steps taken so far, the results of those steps, any relevant retrieved documents. Short-term memory lives in the model's context window. It is temporary: when the session ends, it is gone. A useful analogy is a notepad you keep beside you while working — you write things down while you need them, and you can discard the notepad once the task is done. [1][2]

**Long-term memory** — sometimes called external memory — persists beyond any single session. It is stored outside the model itself, in an external database or file, and retrieved as needed. An agent with long-term memory can remember a preference you stated three weeks ago, recall a decision made in a previous session, or build up knowledge about a project over many interactions. This is not the same as retraining the model — the model's internal configuration does not change. Long-term memory is external storage that the agent can read from and write to. [1][3]

RAG (introduced in topic 4.3) is a specific way of pulling long-term memory into the context window at the moment it is needed. An agent may use RAG as part of its memory system — one example of how prior topics in this week connect naturally at this level. [1]

#### 5.2.3 Tools — what the agent can do

A **tool** is any external capability the agent can invoke. The LLM core generates a decision; the tool carries out an action that has a real-world effect or retrieves new information. Tools are what turn reasoning into doing. [1][2]

Common examples of tools:

- **Web search** — the agent issues a query and receives current search results. This extends the agent beyond its training knowledge, similar to how RAG extends a model with a private document library.
- **A code executor** — the agent generates a computation, and a separate executor runs it and returns the result. The agent can then reason about that result.
- **A calendar or booking system** — the agent can check availability and make reservations on behalf of the user.
- **A file reader or writer** — the agent can read a document, extract information, write a new document, or update an existing one.
- **An API call** — the agent can communicate with an external software service: checking a weather forecast, sending an email, querying a database, posting to a system. [1][2][3]

The LLM core does not directly call these external services. It knows that these tools exist and what they return, and it generates instructions that the surrounding system uses to invoke the right tool. The result comes back to the LLM core, which incorporates it into its next reasoning step. [1][2]

Tools dramatically expand what an agent can do. A standalone LLM can only generate text from what it already knows. An agent with web search, a calculator, and a database connector can act on live information, perform precise computations, and interact with real organisational systems. [2][3]

#### 5.2.4 The planning loop — how everything connects

The **planning loop** (also described as the **observe-think-act cycle**) is the repeating sequence that drives the agent from the start of a task to its completion. [1][2]

The cycle has three phases:

**Observe.** The agent receives information about the current state of the world and the task. At the start, this is the user's request. At later stages, it also includes the results of previous actions — what a tool returned, what a document contained, what an error message said. The LLM core assembles this information from its current short-term memory. [1]

**Think.** The LLM core reasons about what has been observed and decides what to do next. This is the pure reasoning step: analysing the situation, selecting which tool (if any) to invoke, deciding whether the task is complete, or identifying that human input is needed. The output of the think phase is a decision — often expressed as a structured instruction to the system. [1][2]

**Act.** The agent executes the decision made in the think phase. This might mean invoking a tool, writing to memory, returning a response to the user, or pausing to ask a clarifying question. The result of the action feeds back into the next observe phase. [1]

The cycle repeats — observe, think, act; observe, think, act — until one of three things happens: the task is complete, the agent determines it cannot proceed and returns a result with an explanation, or the agent encounters a situation requiring a human decision and pauses to ask. [2][3]

Each individual loop is simple. The complexity of the task is handled by running the loop many times, with different tool calls and different observations at each step. [1]

**The observe-think-act cycle, illustrated:**

```
User task arrives
        |
        v
+-------------------------------------------+
|              OBSERVE                      |
|  LLM core reads: task + memory +          |
|  last action result                       |
+-------------------------------------------+
        |
        v
+-------------------------------------------+
|              THINK                        |
|  LLM core reasons -> decides next action  |
|  or determines task is complete           |
+-------------------------------------------+
        |
        v
+-------------------------------------------+
|              ACT                          |
|  Invoke tool / write memory /             |
|  respond to user / ask for input          |
+-------------------------------------------+
        |
        +--- task complete? ---+
        |                      |
       YES                     NO
        |                      |
        v               loop back to OBSERVE
  Deliver result
```

[1][2][3]

### 5.3 What is an agentic workflow?

An **agentic workflow** is any real-world process structured around an agent's planning loop rather than a single prompt-response exchange. In an agentic workflow, the AI system is given a goal, not a single question, and it sequences its own actions to reach that goal. [1][2]

The key characteristics of an agentic workflow:
- The task is specified at a goal level ("research this topic and produce a summary report") rather than at a step level ("here is the text; summarise it").
- The sequence of steps is determined by the agent at runtime, not pre-programmed.
- Tools are called dynamically, based on what the agent decides it needs.
- Memory accumulates across the steps of a single task.

Agentic workflows are the dominant design pattern for ambitious AI applications in 2026: coding assistants that write, test, and debug in a loop; research assistants that search, read, and synthesise; customer service systems that look up accounts, apply policies, and process requests end to end. [1][3]

A note on scale: multiple agents can work in concert — you will explore multi-agent systems in Week 14. [1]

### 5.4 How agents relate to RAG, fine-tuning, and foundation models

It is worth pausing to see how topic 4.4 fits with topics 4.1–4.3 — because an agent is not a replacement for those concepts; it is a structure that builds on them.

**Foundation model (4.1):** The LLM core of an agent is a foundation model. Everything a foundation model can do — generalise, reason, generate — is what gives the agent its intelligence. Without a capable foundation model, an agent has no useful reasoning engine. [1]

**Fine-tuning (4.2):** The foundation model at the centre of an agent may itself have been fine-tuned for a particular domain or task style. Fine-tuning and the agent structure operate at different levels: fine-tuning shapes what the model knows and how it behaves; the agent structure determines how the model is deployed and what it can reach. [2]

**RAG (4.3):** RAG is one example of a tool an agent can use. An agent might invoke a RAG pipeline as its document retrieval tool — retrieving relevant passages and feeding them into the next observe phase. RAG handles the retrieval problem; the agent structure handles the multi-step planning problem. [1][3]

The four topics of week 4 form a layered picture of the 2026 AI stack: foundation models are the base layer; fine-tuning and RAG are adaptation methods that make the base layer more useful for specific contexts; agents are the operational layer that puts the model to work on complex, multi-step tasks.

## 6. Implementation

_No coding is required in this course. The conceptual flow of the observe-think-act cycle is fully described in Section 5.2.4._

One operational point is worth noting. When a user assigns a task to an agent, they do not specify each step. They state a goal. The agent decomposes that goal into steps during its planning loop — deciding which tools to call, in what order, and when to stop. This division between goal-specification (user) and step-planning (agent) is what makes agents practically useful for complex tasks. [1][2]

Agents also differ from fully automated scripts in that they can pause and ask for human input when they encounter uncertainty or a decision that requires human judgement. Rather than proceeding through an ambiguous situation on its own, a well-designed agent surfaces the ambiguity to the human. This is one of the key safety properties of the design. [2][3]

## 7. Real-World Patterns

As of 2026, agent-based AI systems are moving from research settings into mainstream production deployment across many domains. The following examples illustrate how the four components manifest in real applications. [1][3]

**Coding assistants**
Software development tools operate as agents: given a task description ("fix this bug" or "add this feature"), the system reads existing code files (tool: file reader), reasons about the change needed (LLM core), writes a proposed change (tool: file writer), runs tests (tool: code executor), reads the test output (observe), and iterates until tests pass. The multi-step loop and tool use are what separate this from a simple code-completion suggestion. [1][3]

**Research assistants**
An AI research agent can accept a question like "Summarise the current state of evidence on X" and proceed to search the web, retrieve and read relevant documents, synthesise findings, identify gaps or contradictions, and produce a structured report — all without a human directing each step. Each search and each document read is a tool call; the synthesised understanding accumulates in memory across the loop. [1][2]

**Customer service automation**
Large-scale customer service platforms are deploying agents that can handle multi-step service requests: look up a customer account (tool: database query), check order status (tool: API call), apply a refund policy (reasoning from retrieved policy document via RAG), and initiate a refund (tool: transaction system call). A task that previously required a human to navigate multiple screens and systems can be completed by the agent in a single agentic workflow. [2][3]

**Autonomous scheduling and coordination**
Agents are deployed to manage complex scheduling tasks: checking multiple participants' calendars (tool: calendar API), finding optimal meeting times, sending invitations, rescheduling when conflicts arise, and following up. The multi-step, tool-using, memory-maintaining structure of an agent is exactly what this task requires. [1]

**India-specific context**
Public services and banking institutions in India are exploring agent-based systems to handle multi-step citizen or customer service requests — verifying identity, retrieving account status, applying eligibility rules, and generating responses — in regional languages, with human review gates built into the workflow for high-stakes decisions. [2][3]

## 8. Best Practices

These are conceptual-level principles that inform how agents are designed, not implementation instructions.

**Define the task at the goal level, not the step level.**
Agents are most useful when given a goal to pursue. Providing a step-by-step script reduces the agent to following instructions rather than reasoning through unexpected situations. Agents plan their own steps; they do not need humans to pre-specify every action. [1]

**Build in human-in-the-loop stops for high-stakes decisions.**
An agent that can act in the world — send emails, book resources, process payments — must have explicit checkpoints where it pauses and asks for human confirmation before taking irreversible actions. Fully autonomous action without human gates is appropriate only for low-stakes, easily reversible steps. [2][3]

**Match memory to task timescale.**
Short-term memory is right for within-session, within-task information. Long-term memory is right for information that must persist across sessions or inform many future tasks. Storing everything in long-term memory creates noise; storing nothing forces the user to re-state context they have already provided. [1][2]

**Choose tools with clear, narrow purposes.**
The best agent tools do one thing well and return reliable, structured output. A tool that does too many things is hard for the LLM core to reason about. A tool that returns poorly structured results injects noise into the observe phase of the loop. [1][3]

**Design for transparency.**
Users and organisations deploying agents need to understand what an agent did and why — which tools it called, what results it received, what decisions it made at each step. Logging the planning loop is as important as the outcome it produces. [2]

## 9. Hands-On Exercise

Before the week 4 lab, choose a task you actually need to do — something with at least three steps (for example: find out the opening hours of a specific venue, check whether a date is available, and draft an email to confirm attendance). Write down each step as if you were giving instructions to an assistant who has access to a web browser, an email client, and a calendar. Notice which steps require looking something up (a tool call), which require remembering what the previous step produced (memory), and which require making a judgment call (LLM core reasoning). Bring this breakdown to the lab; you will use it to compare how a human completes the task versus how an AI agent would structure the same work.

## 10. Key Takeaways

- An **AI agent** is a system that puts a foundation model (the LLM core) at the centre of an active, multi-step process, giving it **memory**, **tools**, and a **planning loop** so it can pursue goals that no single prompt could accomplish. [1]
- The **observe-think-act cycle** is the repeating engine of every agent: observe the current state, think about what to do next, act by invoking a tool or producing output — then repeat until the task is complete. [1][2]
- **Memory** comes in two forms: short-term memory (what the agent holds in its current context window) and long-term memory (external storage that persists across sessions). RAG is one specific way of pulling long-term memory into the agent's context at the moment it is needed. [1][3]
- **Tools** are the agent's hands — they give the LLM core the ability to act in the world: searching the web, reading files, calling APIs, executing computations, writing data. Without tools, the agent can only reason; tools let it do. [2]
- An **agentic workflow** is a real-world process structured around an agent's planning loop rather than a single exchange — the dominant pattern for ambitious AI applications in 2026, from coding assistants to autonomous customer service. [1][3]

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._

---CORPUS-META---
concepts_introduced: ["agent", "LLM core (the reasoning engine)", "memory (short-term and long-term)", "tool", "planning loop", "observe-think-act cycle", "agentic workflow"]
prerequisites: ["4.1", "4.2", "4.3"]
cross_refs: []
depth_profile: deep
depth_profile_source: hitl_override_budget_driven
depth_signals: conceptual introduction, four distinct components, multi-section Core Concepts, no derivations — standard fits
requires_diagram: true
diagram_intent: Four-component agent architecture — LLM core linked to memory, tools, planning loop in cyclic observe-think-act flow
scope_flags: []
---END-META---
