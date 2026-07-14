---
topic_id: "14.6"
title: "The ReAct pattern — Reason, Act, Observe, Repeat"
position_in_module: 2
generated_at: "2026-06-15T00:00:00Z"
resource_count: 5
---

# 1. The ReAct Pattern — Reason, Act, Observe, Repeat — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **14.5 — Agent anatomy — LLM plus memory, tools, and a planning loop.** You already know what an AI agent is, what its four components are (LLM core, memory, tools, planning loop), and how the Observe → Think → Act → Update cycle works at a high level. The ReAct pattern is a more precise specification of how that cycle should be structured.

All prior-topic vocabulary — AI agent, LLM core, short-term memory, long-term memory, tool, planning loop, Observe→Think→Act→Update cycle, RAG, embedding, vector database, hallucination, parametric memory, context window — is used freely without re-definition.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Explain what the ReAct pattern is and why it combines reasoning and acting rather than using either alone.
2. Name and describe the four stages of a ReAct cycle: Thought, Action, Observation, and Final Answer.
3. Trace through a complete multi-step ReAct example, identifying each Thought, Action, and Observation in the agent's log.
4. Explain why making the reasoning step explicit as a "Thought:" line improves debuggability.
5. Describe the two failure modes that motivated ReAct: hallucination from reasoning alone, and blind action without reasoning.

## 4. Introduction

In the last topic you saw that an AI agent has a planning loop — a cycle where the agent thinks, acts, checks the result, and repeats until the task is done. That description gives you the shape of the loop. But it leaves one important question open: *how* should the agent think? Should it just jump straight to calling a tool, or should it write out its reasoning first?

It turns out the answer matters a great deal. Researchers at Google and Princeton found that agents which only reason (produce a chain of thoughts without ever checking facts) can confidently produce wrong answers. And agents that only act (call tools without explaining why) are nearly impossible to debug — you see what the agent did, but not why [1][2].

The **ReAct pattern** — which stands for **Re**asoning + **Act**ing — is a simple solution: before every action, the agent writes out a line of explicit reasoning. This one change makes agents more accurate *and* more transparent [2][3].

You may remember a brief mention at the end of topic 14.5: "The planning loop often follows a pattern called ReAct (covered in topic 14.6)." This is that topic. Here you will learn exactly what ReAct means, how its four-stage cycle works, and why the structure matters.

## 5. Core Concepts

### 5.1 The Problem ReAct Solves

Before explaining what ReAct is, it helps to understand what it is designed to fix.

**Problem 1: Reasoning without acting (chain-of-thought alone)**

A technique called **chain-of-thought reasoning** (abbreviated CoT) asks a language model to write out its reasoning step-by-step before giving an answer. This works well for pure logic puzzles — math problems, simple deductions. But when the question depends on *real-world facts the model was not trained on* — like "What is today's top news story?" or "What is the current price of oil?" — chain-of-thought reasoning alone just produces a fluent, confident guess. The model has no way to check whether its reasoning reflects reality. The result is a form of hallucination: plausible-sounding text that may be factually wrong [2].

**Problem 2: Acting without reasoning (tool use alone)**

The opposite approach — skipping reasoning and going straight to calling tools — avoids hallucination but creates a different problem: the agent's behaviour becomes opaque. You see a sequence of tool calls in the log, but you cannot tell what the agent was trying to accomplish with each one. When something goes wrong, there is no thought trail to follow. Debugging becomes a matter of guessing [1][4].

**The ReAct solution**

ReAct interleaves reasoning and acting: before every tool call, the agent writes a brief line of explicit reasoning (called a "Thought"). Then it acts (calls a tool). Then it reads the result (the Observation). Then it reasons again before the next action. The reasoning step keeps the agent grounded in its actual findings; the acting step ensures those findings are real, not invented [2][3].

This interleaving is not a large technical change — it is primarily a **prompting strategy**: the model is instructed to produce a "Thought:" line before every action, and the agent system is built to expect and process that structure [3][5].

### 5.2 The Four Stages of a ReAct Cycle

A single iteration of the ReAct loop has four stages. The loop repeats until the task is complete [1][2].

**Stage 1 — Thought**

The **Thought** is a short line of explicit reasoning that the agent produces before taking any action. It answers the question: "What do I know, and what should I do next?"

The Thought is written as plain text, starting with the label "Thought:". For example:

```
Thought: I need to find out when the Eiffel Tower was built. I should search for that fact.
```

The Thought is *not* a tool call. It is not sent anywhere external. It is reasoning, written out loud, that becomes part of the conversation log. This is what makes the agent's decision-making visible [2][3].

**Stage 2 — Action**

The **Action** is the concrete step the agent takes based on its Thought. Usually this means calling a tool — a web search, a calculator, a database query. The action is written as a structured output, starting with the label "Action:".

```
Action: search("When was the Eiffel Tower built?")
```

The agent system reads this output, extracts the tool name and input, calls the actual tool, and waits for the result [1][4].

**Stage 3 — Observation**

The **Observation** is the result that comes back from the tool call. It is added to the conversation log by the system (not generated by the LLM core), starting with the label "Observation:".

```
Observation: The Eiffel Tower was built between 1887 and 1889 and was completed in March 1889.
```

This is a real fact from the external world, not a guess from the model. The agent can now reason about a verified piece of information [2][5].

**Stage 4 — Repeat or Final Answer**

After receiving the Observation, the agent loops back to Stage 1 and writes another Thought. It continues looping — Thought → Action → Observation → Thought → Action → Observation → … — until it has enough information to answer the original question.

When the agent has enough information, instead of producing another Action, it produces a **Final Answer**:

```
Final Answer: The Eiffel Tower was completed in 1889, which is 137 years ago (as of 2026).
```

The loop ends. The final answer is returned to the user [2][3].

### 5.3 Why "Thought:" Lines Are Part of the Prompt

A detail that beginners sometimes miss: the Thought lines are not internal to the model. They are written *into the conversation context* — into the same text stream that becomes the next prompt [3].

Here is what this means in practice. When the agent starts the second cycle, the prompt fed to the LLM core includes not just the original question and the Observation from the tool, but *also the Thought from the previous cycle*. The Thought is literally in the text. This does three things:

1. **It keeps the agent on track.** The LLM core can see what it was trying to do in the previous step and why.
2. **It creates a traceable log.** Every Thought is recorded. If the agent makes a wrong turn, a developer can read the log and pinpoint exactly where the reasoning went astray.
3. **It helps the model reason better.** Writing reasoning out loud (even as text in a prompt) has been shown to improve language model accuracy on multi-step tasks compared to asking for an answer directly [2][4].

This is why ReAct is described as a *prompting strategy*: the pattern is enforced through the structure of the prompt and the agent's system instructions, not through special model architecture. Any capable instruction-following language model can run ReAct [3][5].

### 5.4 ReAct vs. the Generic Planning Loop from Topic 14.5

In topic 14.5 you learned the Observe → Think → Act → Update cycle. ReAct is a specific, named instantiation of that same idea with three important refinements [1][2]:

| Aspect | Generic loop (14.5) | ReAct |
|---|---|---|
| Reasoning step | "Think" — the model reasons internally | "Thought:" — explicit text, written into the prompt |
| Visibility | Internal to the model; not logged | Every Thought is in the conversation log |
| Debugging | Hard — no trace of why actions were chosen | Easy — every decision has a corresponding Thought |
| Failure mode addressed | Not specified | Explicitly addresses hallucination (via grounding) and opacity (via Thought logs) |

The key difference is **explicitness**. The generic loop says "the agent should think before acting." ReAct specifies *exactly how*: write a "Thought:" line, make it part of the prompt, and log it permanently [2][3].

In the field, when people say "ReAct agent" they mean an agent whose planning loop is structured this way — alternating Thought, Action, and Observation until a Final Answer is reached [1][4].

### 5.5 A Worked ReAct Trace

The best way to make ReAct concrete is to see a full trace. Here is a three-step example.

**Task:** "What year was the Eiffel Tower built, and how many years ago was that from 2026?"

---

```
Question: What year was the Eiffel Tower built, and how many years ago was that from 2026?

Thought: I need to find out when the Eiffel Tower was built. I do not know this from memory
         with certainty, so I should search for it.
Action: search("Eiffel Tower construction year")
Observation: The Eiffel Tower was built between 1887 and 1889. It was completed and opened
             in March 1889.

Thought: The Eiffel Tower was completed in 1889. Now I need to calculate how many years ago
         1889 was, relative to 2026. That is 2026 minus 1889.
Action: calculator("2026 - 1889")
Observation: 137

Thought: I now have both pieces of information: the Eiffel Tower was completed in 1889, and
         that was 137 years ago from 2026. I have enough to answer the question.
Final Answer: The Eiffel Tower was completed in 1889. That is 137 years ago from 2026.
```

---

Trace the structure:

- **Cycle 1:** Thought (I need to search) → Action (search tool) → Observation (real result from search).
- **Cycle 2:** Thought (I need to calculate) → Action (calculator tool) → Observation (real result from calculation).
- **Cycle 3:** Thought (I have everything I need) → Final Answer (no more tools needed).

Notice that each Thought explains *why* the next action makes sense. If the search had returned an unexpected result — for example, a clearly wrong date — the Thought trail would make it immediately obvious where the error entered. Without the Thought lines, you would just see two tool calls and an answer, with no explanation [2][3].

This trace also illustrates why two separate tools are used. The language model could probably estimate "137 years" without a calculator, but using the calculator tool produces a *verified* number — not a model estimate. ReAct grounds every step in real tool results rather than model memory [1][5].

### 5.6 Why ReAct Reduces Hallucination

You already know from topic 14.3 that hallucination happens when a model generates text from its parametric memory without checking whether that text is true. ReAct addresses this in a direct way: every fact-dependent step is grounded in an Observation from a real tool call [2][5].

In the Eiffel Tower example, the agent did not write "Thought: The Eiffel Tower was built in 1889, I remember this" and skip the search. It searched first, received a verified Observation, and *then* reasoned about it. The Thought step directs what to do next; the tool call provides the evidence; the Observation contains only real data.

This is structurally similar to how RAG reduces hallucination in a simple question-answering system (topic 14.3) — both approaches substitute retrieved evidence for model memory. The difference is that ReAct does this *inside a loop*, across multiple steps, for tasks that require more than one piece of evidence [1][2].

A clean way to remember the relationship: RAG grounds a single answer in retrieved documents. ReAct grounds each step of a multi-step reasoning chain in tool observations.

### 5.7 Why ReAct Improves Debuggability

When an agent built with a plain Observe → Think → Act → Update loop produces a wrong answer, debugging requires guessing. You know what tools were called; you do not know why.

When a ReAct agent produces a wrong answer, the full Thought trail is in the log. A developer can read each Thought and find the exact step where the reasoning broke down:

- Did the agent misinterpret the Observation from step 1?
- Did it choose the wrong tool?
- Did it rely on its parametric memory in a Thought instead of verifying with a tool?
- Did it stop too early, before gathering all needed information?

Each of these failure modes leaves a distinct fingerprint in the Thought log. Fixing it becomes a matter of reading the trace, not guessing [3][4].

This debugging transparency is one of the main reasons ReAct became a standard pattern in production agent frameworks. When something goes wrong with an agent in a real application, the cost of debugging blind is high. Thought logs reduce that cost significantly [1][4].

## 6. Implementation — ReAct as Pseudocode

This section makes the ReAct loop concrete with pseudocode. Building a full agent is a Semester 2 skill; here you are learning to read and trace the structure.

```
REACT LOOP:

Given: question, available_tools, conversation_log (starts empty)

Add question to conversation_log

Repeat:
  1. Send conversation_log to LLM core → receive response

  2. If response contains "Final Answer:":
       Extract the answer text
       Return answer to user
       Stop loop

  3. If response contains "Thought:" and "Action:":
       Extract Thought text → append to conversation_log
       Extract Action (tool_name, inputs)
       Call tool_name(inputs) → get result
       Append "Observation: <result>" to conversation_log
       Continue loop
```

Key point: `conversation_log` is the short-term memory. Every Thought and every Observation is appended to it. On the next cycle, the LLM core sees the full history — question, prior Thoughts, prior Actions, and prior Observations — before writing its next Thought. This is how context accumulates across cycles [2][3].

The loop runs until one of three things happens:

1. The LLM core produces a Final Answer (task complete).
2. The LLM core produces a "cannot answer" signal (graceful failure).
3. A safety limit — a maximum number of cycles — is reached and the system stops automatically [1][5].

The safety limit is the same mechanism described for the generic planning loop in 14.5, applied here to the ReAct structure specifically.

## 7. Real-World Patterns

### 7.1 ReAct in Modern Agent Frameworks

ReAct is not a theoretical curiosity — it is the default loop structure in widely used agent frameworks [4][5].

LangChain, one of the most popular Python frameworks for building LLM-powered applications, implements a "ReAct agent" as a first-class component. When you create a LangChain agent and give it a set of tools, the default behaviour is a ReAct loop: the framework instructs the LLM to produce Thought + Action pairs, calls the specified tool, appends the Observation, and repeats [4]. Developers building with LangChain see the Thought lines in their logs by default — they do not have to add tracing manually.

Other frameworks — including AutoGen, LlamaIndex, and OpenAI's Assistants API — implement similar structured loops, many directly inspired by the original ReAct paper [1][2].

### 7.2 Multi-Hop Question Answering

One of the original applications demonstrated in the ReAct paper is multi-hop question answering: questions that require gathering evidence from more than one source and combining it [2].

For example: "In what country is the headquarters of the company that makes the most-used web browser?" Answering this requires:

- Step 1: Find the most-used web browser (search → Chrome).
- Step 2: Find the company that makes Chrome (search → Google).
- Step 3: Find the country where Google is headquartered (search → United States).

A chain-of-thought answer risks hallucinating any of these facts. A direct tool-call approach without ReAct would have no thought trail. A ReAct agent discovers the chain dynamically — each Thought determines what to look up next, and each Observation provides a verified fact [2][5].

### 7.3 Customer Support Agents

In a customer support deployment, an agent might need to: look up a customer's order (database tool), check the shipping carrier's tracking API (API tool), and decide whether to offer a refund based on a policy document (retrieval tool). Each step depends on the previous result.

With a ReAct loop, the agent's Thought log records why it called each tool and what it concluded from each result. A support team supervisor can audit a resolved case by reading the Thought trail — exactly as they would read a case note [3][4].

## 8. Best Practices

**Keep Thought lines concise and specific.** A good Thought names the next step and its reason in one or two sentences. Verbose Thoughts inflate the context window and make the log harder to read. "I need the product price; I will call the pricing API" is better than a paragraph of hedged reasoning [3][5].

**Treat the Observation as the authoritative fact — not the model's memory.** If the Observation says the price is $42.00, the next Thought should use $42.00, not whatever the model "remembers" from training. The entire point of the Observation step is to replace model memory with verified data [2].

**Log every Thought–Action–Observation triple for debugging.** In development, store the full ReAct trace somewhere readable. When the agent gives a wrong answer, reading the trace from the beginning is almost always the fastest path to finding the bug [1][4].

**Set a maximum cycle count.** An unconstrained ReAct loop can run indefinitely if the agent keeps deciding it needs more information. A hard limit of 10–15 cycles is standard; adjust based on the complexity of the tasks you expect [1][5].

**Do not let the agent substitute Thoughts for Observations.** If an agent writes "Thought: I recall that the population is 3 million, so I don't need to search" for a fact that could be wrong or outdated — that is a prompt-design problem. A well-instructed ReAct agent defaults to verifying facts via tools rather than relying on its parametric memory for specific claims [2][5].

## 9. Hands-On Exercise

This exercise does not require writing code — it is a tracing exercise.

**Task:** Write out a full ReAct trace (Thought → Action → Observation, repeated at least twice, then Final Answer) for this question: "Who is the current Prime Minister of Canada, and in what year did they take office?"

Use the following tools (write the Action lines yourself, and make up plausible Observations as if you were the tool returning a result):

- `search(query)` — returns a text snippet from a web search.
- `extract_year(text)` — extracts a four-digit year from a sentence.

After writing the trace, answer these two questions in a short paragraph:

1. Which Thought was most important for keeping the agent on track?
2. If the search had returned an obviously wrong result (e.g., the name of a historical figure), what would the agent's next Thought need to say?

This exercise builds the habit of thinking in ReAct terms — writing explicit reasoning before every action — which is the core mental model you need before building agents in Semester 2.

## 10. Key Takeaways

- **ReAct** (Reasoning + Acting) is a prompting strategy and loop structure for AI agents that interleaves explicit reasoning ("Thought:") with tool calls ("Action:") and observed results ("Observation:") before reaching a Final Answer [1][2].
- The **four stages of a ReAct cycle** are: **Thought** (write reasoning), **Action** (call a tool), **Observation** (read the real result), and **repeat** — until the agent produces a **Final Answer** [2][3].
- ReAct differs from the generic planning loop in topic 14.5 in one critical way: the **Thought step is explicit, written into the prompt, and logged** — making every decision traceable and every mistake findable [3][4].
- ReAct addresses two failure modes: **hallucination from chain-of-thought-only reasoning** (fixed by grounding each step in a real Observation) and **opacity from action-only loops** (fixed by logging every Thought) [2][5].
- In practice, ReAct is the **default loop structure in major agent frameworks** such as LangChain and is the natural choice whenever an agent must work through multiple, sequentially dependent steps [4].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
