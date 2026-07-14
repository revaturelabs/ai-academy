---
topic_id: "14.5"
title: "Agent anatomy — LLM plus memory, tools, and a planning loop"
position_in_module: 1
generated_at: "2026-06-15T00:00:00Z"
resource_count: 3
---

# 1. Agent Anatomy — LLM Plus Memory, Tools, and a Planning Loop — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **14.1 — Vector databases: storing embeddings and enabling similarity search at scale.** You already know what embeddings are and how a vector database stores and retrieves them by similarity.
- **14.2 — The RAG retrieval pipeline: query → embed → similarity search → top-k → inject.** You already know what RAG is and how retrieved context is injected into a prompt.
- **14.3 — Why RAG reduces hallucination.** You already know the difference between parametric memory and retrieved evidence.
- **14.4 — When to use RAG.** You already know the decision signals — freshness, private data, precision — that distinguish RAG from simpler approaches.

All terms introduced in those four topics are used freely here without re-definition. You may also use freely the earlier M5 concepts: LLM (Large Language Model), prompt, temperature, API, Python, token, system prompt, user prompt.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Name the four components of an AI agent and describe in plain language what each one does.
2. Explain why an LLM on its own is not an agent, and what the other three components add.
3. Describe what an agent's planning loop does and why it is necessary for multi-step tasks.
4. Distinguish between short-term memory and long-term memory in the context of an agent.
5. Explain what a tool is in the agent context and give two concrete examples.
6. Identify the kinds of tasks where an agent is the right choice, versus tasks where a simpler approach is better.

## 4. Introduction

Imagine you ask a helpful assistant to "book me the cheapest flight to London next week, then email my manager the travel details, and then add the trip to my calendar." No single action completes that request. The assistant must search for flights, pick the best one, draft an email, send it, and create a calendar event — all in sequence, with each step depending on the result of the previous one.

A plain language model — the kind you have been using throughout this course — cannot do this on its own. You send it a prompt, it sends back a response, and that is the end of the interaction. It has no way to search the web, send an email, or update a calendar. It also does not remember what it figured out in step 2 when it is working on step 3.

An **AI agent** is a system built around a language model that adds exactly the pieces needed to carry out multi-step tasks. Those pieces are: **memory** (so the agent can remember things across steps), **tools** (so the agent can take actions in the world), and a **planning loop** (so the agent can figure out what to do next, do it, observe the result, and keep going until the task is done) [1].

This topic gives you a clear picture of what each piece is and what it contributes. Building agents is a Semester 2 topic — here the goal is to understand the anatomy, the way you might understand what an engine, a gearbox, and wheels do before learning to repair a car [2].

## 5. Core Concepts

### 5.1 What an AI Agent Is

An **AI agent** (sometimes called an "LLM agent" or "autonomous agent") is a software system in which a language model acts as a decision-making core, surrounded by additional components that let it pursue a goal across multiple steps [1][3].

The key word is *autonomous*: unlike a single prompt-and-response exchange, an agent can take a sequence of actions — including calling tools, reading results, and deciding what to do next — without a human directing each individual step. The human sets the goal; the agent works out how to achieve it [2].

Three things an agent can do that a plain LLM cannot:

1. **Take actions in the outside world** — for example, search the web, read a file, call an API, write to a database.
2. **Remember information across steps** — so that what was discovered in step 1 is available when making the decision in step 3.
3. **Decide what to do next** based on what just happened — rather than requiring the human to guide each step.

An agent without all three of these properties is not really an agent — it is a pipeline or a single LLM call [1].

### 5.2 The Four Components of an Agent

Every AI agent, regardless of how it is implemented, has four identifiable components working together [1][2][3]. Think of them as roles inside a small team.

**Component 1 — The LLM Core**

The **LLM core** is the language model itself — the GPT-style, instruction-following AI that you have been working with throughout M5. It is the "brain" of the agent. Its job is to read everything put in front of it (the goal, the current situation, any retrieved memory, any tool results) and produce a decision: what should be done next?

The LLM core does not act by itself. It can only generate text. Every action in the world is taken by calling a tool. Every piece of information it needs from the past comes from memory. The LLM core is the reasoner; the other components are its hands, legs, and filing cabinet [2].

The LLM core is exactly the same kind of model you already know — a large language model that takes a prompt and produces a response. What makes it an agent is the system built around it [1].

**Component 2 — Memory**

**Memory** is how the agent holds onto information across multiple steps. Without memory, each step would start with a blank slate — the agent would forget everything it had done and learned so far. There are two kinds of memory an agent can use [1][3].

- **Short-term memory** (also called working memory or context): Information kept in the current prompt — the conversation history, the goal, the results of recent tool calls. This is the agent's "desk": whatever is on the desk right now. It is fast and immediately available, but it is limited by the model's context window (the maximum amount of text the model can process at once). When a task has many steps, the desk can fill up.

- **Long-term memory**: Information stored outside the prompt in an external system — often a vector database of the kind you studied in 14.1 — and retrieved when needed. This is the agent's "filing cabinet": vast capacity, but the agent must look something up to get it. Long-term memory allows agents to remember facts from much earlier in a session, or even across separate sessions [2][3].

A simple way to remember the distinction: short-term memory is *in the prompt right now*; long-term memory is *stored outside and fetched when needed* [1].

**Component 3 — Tools**

**Tools** are functions that give the agent the ability to act in the world or retrieve information from outside itself [1][2]. The LLM core cannot do anything by itself except generate text. Tools are what turn that text into real-world actions.

A tool is typically a piece of code that the agent can call by name, with specific inputs, and that returns a result. Common examples:

| Tool | What it does |
|---|---|
| Web search | Queries a search engine and returns a summary of results |
| Calculator | Evaluates a mathematical expression and returns the answer |
| File reader | Opens and reads a file, returns its contents |
| API caller | Sends a request to an external service (e.g. a weather API) |
| Database query | Looks up a record in a database |
| Email sender | Composes and sends an email |
| Code interpreter | Runs a snippet of code and returns the output |

When the LLM core decides that a tool is needed, it produces a structured output naming the tool and providing the inputs. The agent system then calls that tool, gets the result, and feeds the result back into the LLM core's next prompt. The model itself never directly calls code — it only says "I want to call this tool with these arguments" [3].

This is an important point: the LLM core is *not* running Python code or accessing the internet. The tools are separate programs. The LLM core is the planner; the tools are the executors [1].

**Component 4 — The Planning Loop**

The **planning loop** (sometimes called the agent loop or reasoning loop) is the repeating cycle that coordinates the other three components. Without it, the LLM core would produce a single response and stop. With it, the agent can work through a multi-step task by repeating the same cycle until the task is done [1][2][3].

The basic loop works in four stages:

1. **Observe** — the agent looks at the current situation: the goal, the conversation so far, the results of the last tool call (if any).
2. **Think** — the LLM core reasons about what to do next. Should it call a tool? Which one? With what inputs? Or is the task complete?
3. **Act** — if a tool is needed, the agent calls it and receives the result. If the task is complete, the agent produces a final answer for the user.
4. **Update** — the result of the action (or the final answer) is added to memory, and the loop begins again from step 1.

The loop repeats until the agent reaches a stopping condition — either the task is done, or the agent determines it cannot complete the task [2].

This cycle — Observe → Think → Act → Update → repeat — is what separates an agent from a simpler system. A simpler system runs once. An agent runs until it is finished [1][3].

### 5.3 The Planning Loop in Depth — Why It Matters and How It Decides to Stop

The planning loop is the component that turns the LLM core from a one-shot text generator into a system that can work through a complex, multi-step task. Understanding how it works — and, crucially, how it knows when to stop — is central to understanding agent anatomy.

**What the planning loop does on each cycle**

At the start of each cycle, the loop assembles everything the agent knows right now: the original goal, the conversation history, the results of any tool calls from previous cycles, and the list of available tools with their descriptions. This assembled context is packaged into a prompt and sent to the LLM core. The LLM core then produces one of two kinds of output: a tool call (specifying which tool to invoke and with what inputs), or a final answer (signalling that the task is complete) [1][2].

If the output is a tool call, the planning loop executes that call, collects the result, writes the result into short-term memory, and immediately starts the next cycle with the richer context. If the output is a final answer, the loop stops and returns the answer to the user.

**Why the planning loop is necessary**

Without the loop, the LLM core would receive the user's goal, produce a single response, and halt — regardless of whether the task needed five more steps. The planning loop is the mechanism that keeps the agent engaged with the task across as many cycles as the task requires. It also provides a consistent structure: every cycle follows the same Observe → Think → Act → Update pattern, which makes agent behaviour predictable and auditable [3].

**How the loop decides when to stop**

An agent does not loop forever. Real agent systems use two stopping conditions working together. The first is the LLM core itself: the model is instructed to produce a special "final answer" signal when it judges the task to be complete, based on everything in its context. The second is a hard safety limit — a maximum number of cycles (for example, 15) configured by the developer. If the agent has not produced a final answer within that limit, the system stops the loop automatically and returns whatever partial result it has, along with a note that the limit was reached. This prevents runaway loops from consuming unlimited API calls and time [1][3].

The planning loop often follows the ReAct pattern (covered in topic 14.6).

Taken together, the planning loop is the "executive function" of the agent: it keeps the other three components — LLM core, memory, and tools — working in coordination, cycle after cycle, until the job is done [2].

### 5.4 How the Four Components Work Together — A Walkthrough

To make the anatomy concrete, trace through a simple two-step agent task: "What is the population of the capital city of France, and is that number bigger than 5 million?"

**Step 0 — Setup:** The agent receives the goal. Short-term memory contains the goal and any system instructions.

**Planning loop, cycle 1:**
- *Observe:* The agent has the goal but no information yet.
- *Think (LLM core):* "I need to know the population of Paris, the capital of France. I will search for it."
- *Act:* The agent calls the `web_search` tool with query "population of Paris, France."
- *Update:* The tool returns: "The population of Paris is approximately 2.1 million in the city proper; the greater metropolitan area is about 12 million." This result is added to short-term memory.

**Planning loop, cycle 2:**
- *Observe:* The goal plus the tool result from cycle 1.
- *Think (LLM core):* "I have the population figures. The city proper is 2.1 million; the metro area is 12 million. I need to compare both to 5 million. I have enough information to answer."
- *Act:* No tool call needed. The agent produces its final answer: "The capital of France is Paris. The city proper has about 2.1 million people — smaller than 5 million. The greater metropolitan area has about 12 million — larger than 5 million."
- *Loop ends.*

Notice the roles:
- The **LLM core** did all the reasoning — "what do I need?", "what do the numbers mean?", "am I done?"
- **Memory** (short-term) carried the tool result from cycle 1 into cycle 2.
- The **tool** (web search) fetched real information from outside the model.
- The **planning loop** ran twice and stopped when the task was complete [1][2][3].

### 5.5 How the Four Components Interact as a System

Understanding each component separately is valuable. Understanding how they interact within a single agent turn is what makes the anatomy click.

Here is what happens inside one complete agent turn — from the moment a user sends a goal to the moment the agent returns an answer:

1. **The planning loop starts.** It assembles the current state: the user's goal, any prior conversation, and the list of available tools. This assembled context becomes a prompt.
2. **The prompt is sent to the LLM core.** The LLM core reads everything — goal, history, tool descriptions — and decides what to do next. It may decide to call a tool, or it may decide it already has enough information to answer.
3. **If a tool call is needed,** the planning loop extracts the tool name and inputs from the LLM core's output and calls that tool. The tool runs (it might query a database, call an API, run a calculation) and returns a result.
4. **The result is written to short-term memory.** Short-term memory now includes the original goal, any prior steps, and this new tool result. The planning loop feeds this richer context back into step 1 and starts the next cycle.
5. **If a final answer is produced,** the planning loop stops. The answer is returned to the user. Key facts from the completed task may be archived to long-term memory for use in future sessions.

The four components are not independent — they are continuously passing information around this cycle. The LLM core is the decision-maker, but it cannot decide well without memory giving it context and tools giving it real-world data. Memory is the connective tissue; tools are the hands; the planning loop is the coordinator that keeps them all in sync [1][2][3].

When to use an agent versus simpler approaches — such as a direct LLM call or a fixed chain of calls — is covered in topic 14.7.

## 6. Implementation — The Planning Loop as Pseudocode

This section makes the planning loop concrete with pseudocode. Building a real agent is a Semester 2 skill; here you are learning to read and reason about the structure, not to code it.

```
AGENT LOOP:

Given: goal, available_tools, memory

Repeat:
  1. Build a prompt containing:
       - The goal
       - Contents of short-term memory (recent history, tool results)
       - List of available tools and their descriptions
  2. Send prompt to LLM core → receive response

  3. If response is FINAL ANSWER:
       Return answer to user
       Stop loop

  4. If response is TOOL CALL (tool_name, inputs):
       Call tool_name(inputs) → get result
       Add result to short-term memory
       If needed: also write result to long-term memory (vector database)
       Continue loop
```

The loop runs until one of three things happens:

1. The LLM core produces a final answer (success).
2. The LLM core decides it cannot complete the task (graceful failure).
3. A safety limit is reached — for example, the loop has run more than 10 times — and the system stops automatically to prevent an infinite loop [1][3].

Each time the loop runs, the prompt grows slightly: it includes more memory (tool results, thoughts from earlier cycles). This is why memory management — deciding what to keep in short-term memory and what to store in long-term memory — matters in real agent systems [2].

## 7. Real-World Patterns

### 7.1 Agents in Customer Service Automation

A common real-world agent deployment is in customer service. A user asks: "Where is my order, and can I change the delivery address?" Answering this requires: looking up the order by ID (tool: database query), checking the delivery status (tool: logistics API), and — if the package has not yet shipped — updating the address (tool: database write). Each step's result determines whether the next step is needed. A fixed chain cannot handle this — whether the address update is possible depends on the status result [1][3].

The agent pattern handles this naturally. The LLM core decides what to do next based on what it finds out. The tools do the real work. Memory carries the order ID and status across steps [2].

### 7.2 Research and Summarisation Agents

Another common pattern is a research agent: given a topic, the agent searches the web, reads several pages, extracts key facts, and writes a summary. The number of searches needed is not known in advance — it depends on what is found. This is a canonical agent use-case: multi-step, decision-dependent, requiring both retrieval tools and text-generation [1][2].

### 7.3 Personal Productivity Assistants

A personal productivity assistant is a practical example of all four agent components working together in everyday use. Consider an email drafting agent built for a busy professional. The agent holds the user's communication preferences — tone, sign-off style, common phrases — in long-term memory. When asked to "draft a reply to Alice's meeting request and check whether my calendar is free that afternoon," the planning loop kicks off: it first calls a calendar tool to check availability, stores the result in short-term memory, then calls a drafting function that reads the availability result alongside the user's stored preferences to produce a personalised reply. The LLM core coordinates each step, deciding when to call a tool and when it has enough information to produce the draft. The user reviews the output, and the loop ends. This pattern illustrates why all four components are necessary: preferences in long-term memory, availability data from a tool, step coordination from the planning loop, and reasoning from the LLM core [2][3].

### 7.4 The Live Demo You Will See in Lab

In the lab for Week 14, you will watch a live demo of an agent completing a multi-step task in real time. Pay attention to:
- Which tool the agent calls at each step, and why.
- How the agent's thinking changes when it receives a tool result.
- The moment the agent decides it has enough information and stops the loop.

You will also write a one-paragraph architectural decision for your domain system: does it need RAG, an agent, or something simpler? The decision signals for that choice are covered in topic 14.7.

## 8. Best Practices

**Use the simplest approach that works.** A direct LLM call is faster, cheaper, and easier to debug than an agent. Reach for the agent pattern only when the task genuinely requires dynamic, multi-step decision-making [2][1].

**Give each tool only the access it needs — not more.** Every additional capability you grant a tool is a potential source of unintended behaviour. An agent that has the ability to delete files can cause irreversible damage if it misunderstands its goal. Keep each tool's permissions narrow and specific to what the agent's task actually requires [3].

**Set a maximum loop count.** Without a limit, a confused agent can run in circles, burning API credits and time. All production agent systems enforce a maximum number of planning loop cycles [1][3].

**Do not give agents irreversible actions without a human checkpoint.** For actions that cannot be undone — sending messages, making payments, deleting data — build in a confirmation step. The agent asks "I am about to do X. Shall I proceed?" and waits for a human answer before acting [2].

**Keep short-term memory focused.** As the planning loop runs, short-term memory grows with each tool result and reasoning step. A very long memory context slows the model down, increases cost, and can push earlier important facts out of the effective context window. Prune low-relevance items from short-term memory as the task progresses and archive them to long-term storage when they may be needed later [1][2].

**Log every tool call for debugging.** When an agent produces an unexpected result, the most useful diagnostic is a record of exactly which tools were called, with what inputs, and what they returned at each cycle. Logging tool calls and their results during development makes it far easier to identify where the agent's reasoning went wrong [3].

**Understand what you are delegating.** Before using an agent to do something on your behalf, be clear about: what tools it has, what memory it can access, and what stopping conditions exist. An agent that can do more than you intended, or run longer than you expected, is a risk [3].

## 9. Hands-On Exercise

This is an observation and planning exercise, not a coding task.

**Part 1 — Trace an agent task:**
Pick a real-world task that would require three or more steps — for example, "Find the cheapest hotel near the conference venue on the 15th, and check whether breakfast is included." Write out:
- What information is needed at each step?
- What tool would provide that information?
- What would short-term memory need to carry from one step to the next?

You do not need to build anything. This is practice at reading an agent's anatomy — understanding what each component does before you build with it.

**Part 2 — Map the four components to your domain system:**
For a domain system of your choice, write one sentence for each of the four agent components:
- **LLM core:** What reasoning task would the LLM core perform in your system?
- **Short-term memory:** Name one piece of information your agent would need to carry from one step to the next.
- **Tools:** Name two tools your agent would need, and describe in one sentence what each one does.
- **Planning loop:** What would the stopping condition be — how would the agent know the task is complete?

You do not need to build anything. This exercise practices mapping the four-component anatomy to a concrete use case before the next topics cover when to choose agents and how to plan their interactions.

## 10. Key Takeaways

- An **AI agent** is a system built around an LLM core plus three additional components: **memory** (to hold information across steps), **tools** (to act in the world), and a **planning loop** (to decide what to do next, repeatedly, until the task is done).
- The **LLM core** is the reasoner — it reads the current situation and decides what action to take next. It cannot act directly; it calls tools through the planning loop.
- **Memory** comes in two forms: **short-term** (in the current prompt context) and **long-term** (stored externally, often in a vector database, and retrieved when needed).
- **Tools** are functions the agent can call — web search, database query, API caller, calculator — that let the agent interact with the outside world.
- The **planning loop** repeats Observe → Think → Act → Update until the task is complete. ReAct pattern (covered in topic 14.6) is introduced in the next topic.
- Use the simplest approach that works: direct call → chained calls → agent. Agents are powerful but add cost and complexity; they are right only when tasks require dynamic, multi-step decisions based on intermediate results.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
