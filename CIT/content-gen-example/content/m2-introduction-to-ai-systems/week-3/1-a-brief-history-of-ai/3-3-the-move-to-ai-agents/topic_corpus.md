---
topic_id: "3.3"
title: "The move to AI agents"
position_in_module: 3
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. The Move to AI Agents — Topic Corpus

## 2. Prerequisites

This topic builds directly on **3.1 — The Rise of Modern AI** and **3.2 — Large Language Models Explained**. You should already be familiar with:

- **machine_learning** and **deep_learning** — how models learn patterns from data.
- **large_language_model (LLM)** — a text-generating model trained on massive corpora.
- **prompt** — the instruction or question you send to an LLM.
- **hallucination** — when an LLM produces confident but incorrect output.
- **few-shot** prompting — giving the model examples inside the prompt to guide its response.

If any of those terms feel unfamiliar, revisit topics 3.1 and 3.2 before continuing.

## 3. Learning Objectives

By the end of this topic you will be able to:

1. Define what an AI agent is and explain how it differs from a standalone LLM responding to a single prompt.
2. Identify the five core components of an agent loop — goal, planning, tool use, memory, and feedback — and describe the role of each.
3. Explain why adding planning and tool use to an LLM transforms it from a "question-answerer" into an autonomous actor.
4. Describe at least two real-world scenarios where an agent architecture is more useful than a single-prompt LLM call.
5. Recognize the current limitations of AI agents — where they tend to fail and why human oversight remains important.

## 4. Introduction

You have already met the LLM (Large Language Model). You type a question, the model reads it, and it types back an answer. That is powerful — but it is also limited. The LLM does exactly one thing: it produces the next piece of text. It cannot browse the web to check its own answer. It cannot send an email, run a calculation, or remember what you asked it yesterday. Every conversation starts fresh, from zero.

Now imagine something different. Instead of a model that answers one question, imagine a model that is given a *goal* — for example, "Research the top three competitors to our product and write a summary report." The system reads the goal, breaks it into steps, searches the web, reads the pages it finds, compares the results, and writes the report — all on its own, without you prompting it at every step. That is the idea behind an **AI agent**.

The move from LLM-as-tool to LLM-as-agent is not a replacement of what you learned in 3.2. The LLM is still the engine. But around it, engineers add extra layers — a goal to pursue, a plan for how to pursue it, tools to take action in the real world, memory to carry facts forward, and a loop that keeps going until the goal is reached. This topic explains what those layers are and why they change what AI can do.

## 5. Core Concepts

### 5.1 What is an AI agent?

An **AI agent** is a system that uses an LLM as its reasoning core and wraps it with extra capabilities so it can pursue a goal across multiple steps — taking actions, observing results, and deciding what to do next [1].

The key word is *goal*. A plain LLM responds to a prompt. An agent is given an objective and then works toward it autonomously — choosing its own next steps along the way [1].

Think of it this way:

| | LLM (standalone) | AI agent |
|---|---|---|
| Input | A prompt (single request) | A goal (desired end-state) |
| Output | One response | A sequence of actions + a final result |
| Steps | One | Many — planned and executed by the system |
| Tools | None | Web search, calculators, APIs, file access, etc. |
| Memory | None between calls | Can carry information across steps |

The word "agent" comes from the word *agency* — the ability to act on your own behalf. An AI agent has agency because it decides what actions to take, rather than waiting for a human to specify each step [2].

### 5.2 From LLM to agent — what changes

An LLM on its own is like a very knowledgeable expert locked in a room with no phone, no computer, and no notebook. They can answer your questions brilliantly, but they cannot look anything up, they cannot call anyone, and they forget the conversation the moment you leave the room.

An agent is that same expert, but now they have a phone, a computer, a notebook, and a brief they are working through. The underlying intelligence is the same LLM. What changes is what surrounds it [3].

Concretely, moving from a standalone LLM to an agent requires three things:

1. **Giving the LLM a goal** — a description of what success looks like, not just a single question.
2. **Giving the LLM tools** — ways to interact with the outside world (search, calculators, APIs, file systems).
3. **Putting the LLM in a loop** — having it take a step, observe the result, decide what to do next, take another step, and continue until the goal is achieved [2].

This loop is sometimes called the **agent loop**. The agent reasons about the current state, takes an action, receives an observation, reasons again, and so on [2].

The LLM itself does not change. It still generates text — but now that text is a *decision* ("I should search for X") or a *plan* ("Step 1: … Step 2: …"), not just an answer to a question.

### 5.3 Core components of an agent loop

Most AI agent architectures share five building blocks [1][2][3]. Each one solves a specific limitation of the plain LLM:

**1. Goal**

The starting point. The goal is a description of what the agent is supposed to accomplish — clear enough that the LLM can judge whether it has been reached. Without a goal, the agent has no way to decide when to stop or what to do next.

Example: "Find the three cheapest flights from Mumbai to London in July and return them as a table."

**2. Planning**

**Planning** is how the agent breaks a goal into smaller steps it can actually take. The LLM reads the goal and writes a plan: "First, search for flights. Then filter by price. Then format the results."

This is where the LLM's language ability becomes genuinely useful — it can reason in language about what needs to happen next [2]. Planning does not have to be perfect on the first try; the agent can revise its plan as it receives new information.

**3. Tool use**

**Tool use** refers to the agent's ability to call external functions or services. An LLM alone can only produce text. Tools let it take real actions in the world [1]:

- **Web search** — look something up in real time
- **Calculator** — perform arithmetic without relying on the LLM's error-prone mental math
- **API calls** — talk to external services (book a flight, send an email, read a database)
- **File access** — read or write documents
- **Code execution** — run a snippet of code and get the output

The agent decides *when* to use a tool and *what to pass to it*, based on its plan. The result comes back as text, which the agent reads and uses to plan its next step [1].

**4. Memory**

**Memory** lets the agent carry information across steps. There are two types relevant at this level:

- **Short-term memory (context window)** — everything the agent has seen so far in the current run, held in the LLM's working space (the context window you met in 3.2). This is temporary; it vanishes when the session ends.
- **Long-term memory (external storage)** — facts written to a file or database that the agent can retrieve later, even across separate sessions [2].

Without memory, an agent would forget what it found in step 1 by the time it reaches step 3. Memory is what allows multi-step work to stay coherent.

**5. Feedback loop**

The **feedback loop** is the mechanism that keeps the agent running. After each action, the agent receives an *observation* — the result of what it just did. It feeds that observation back into the LLM, which then decides what to do next. This continues until the goal is reached — or until the agent decides it cannot proceed and asks for help [2][3].

The loop is what distinguishes an agent from a simple chain of pre-set instructions. The agent can adapt: if a tool call fails, it tries another approach; if it discovers new information, it updates its plan.

Here is the loop in outline form:

1. Receive goal
2. Make a plan
3. Execute next action (use a tool, write text, call an API)
4. Observe the result
5. Update the plan if needed
6. Repeat from step 3 until goal is reached

### 5.4 Capabilities and limitations of today's agents

AI agents are genuinely impressive — but beginners often over- or underestimate them. Here is an honest picture.

**What today's agents do well:**

- Breaking a large task into smaller sub-tasks and working through them step by step [1]
- Using tools reliably when the tools are well-defined and the goal is clear
- Summarising, extracting, and transforming information from multiple sources
- Drafting documents or code that a human then reviews and finalises
- Running long, repetitive research tasks that would take a human hours [3]

**What today's agents struggle with:**

- **Hallucination propagates.** Because the LLM is the reasoning core, the agent can still produce confident but incorrect plans or conclusions — and it will act on them unless a human or another check catches the error [2].
- **Goal ambiguity.** If the goal is unclear, the agent will often guess — sometimes sensibly, sometimes badly. Precise goal-setting is a skill.
- **Long chains amplify errors.** Each step can introduce a small mistake. Over 20 steps, small errors compound into large failures.
- **Tool errors.** If a tool returns bad data, the agent may not recognise the problem and will continue with faulty information.
- **Cost.** Every step in the loop calls the LLM, which uses computing resources and time. Complex agents can be expensive to run [1].

Because of these limitations, most real-world agents today are **supervised** — a human reviews the plan before execution, or reviews the result at checkpoints. Fully autonomous, unsupervised agents are rare outside of narrow, well-tested tasks [3].

## 6. Implementation

This section describes, at a conceptual level, how a practitioner would wire up a basic agent. No programming knowledge is required — the goal is to understand the shape of the thing so that the agent loop in §5.3 feels concrete.

Imagine you want to build a simple agent whose job is: "Given a company name, find its current stock price and write a one-paragraph summary of recent news about it."

Here is how a practitioner would approach it:

**Step 1 — Define the goal clearly.**
The goal must be specific enough that the agent can judge when it is done. Vague goals ("tell me about Company X") produce unpredictable behaviour. A precise goal ("find the current stock price of Company X and summarise 3 recent news headlines about it") gives the agent a clear finish condition.

**Step 2 — Choose the tools the agent will have access to.**
For this goal, the agent needs at minimum:
- A web-search tool (to find current news)
- A stock-price API tool (to retrieve live price data)

The practitioner connects these tools to the agent framework. The agent does not use them automatically — it decides *when* to call them as it executes its plan [1][2].

**Step 3 — Write a system prompt that sets the agent's behaviour.**
The agent is still an LLM at its core. The system prompt (a set of instructions the LLM receives before anything else) tells it its role, what tools it has, what format it should output in, and any constraints (for example: "do not make up information — only report what the tools return") [3].

**Step 4 — Run the agent loop.**
The practitioner starts the agent with the goal. The agent:
- Plans: "I need to search for stock price, then search for recent news."
- Calls the stock-price tool and receives a number.
- Calls the web-search tool with the company name and "recent news" and receives headlines.
- Drafts a summary paragraph using what the tools returned.
- Decides the goal is met and returns the output.

**Step 5 — Review the output.**
A human checks the result. Are the facts correct? Is the summary accurate? If the agent made an error — used the wrong ticker symbol, summarised old news — the human corrects the goal specification or the tools and runs again.

This five-step pattern — define, equip, instruct, loop, review — is the core of most agent deployments today. Frameworks like LangChain, AutoGen, and CrewAI (covered in later topics) automate much of steps 2–4, but the conceptual shape is the same [1].

## 7. Real-World Patterns

AI agents are already at work in a range of industries. Here are patterns that span India-based and global contexts.

**Customer support automation (global and India)**
Many large companies — including Indian e-commerce platforms and banks — now use agents to handle customer queries end-to-end. The agent reads the customer's complaint, searches internal databases for account information, calls an API to check order status, drafts a response, and — if it is confident — sends it. If it is not confident, it routes the ticket to a human agent with a summary already written [1].

**Research and report generation**
Financial analysts at investment firms use agents to gather data: the agent searches regulatory filings, news sources, and market databases; synthesises the findings; and drafts a first-version report. The analyst reviews and edits rather than starting from scratch [3]. This pattern is increasingly common in India's growing financial-technology sector.

**Software development assistance**
Developer tools now offer agent-mode features. Given a task description, the agent reads the relevant code files, writes new code, runs the code to check for errors, reads the error output, fixes the code, and repeats — without requiring the developer to hand-hold each step [2]. Junior developers at Indian tech firms and global product companies both use these tools to accelerate repetitive coding tasks.

**Personal productivity**
Individuals use agents wired to their calendars, email, and documents to summarise long email threads, draft replies, schedule meetings, and extract action items — all from a single high-level instruction [1].

**Healthcare data processing**
Hospitals and health-tech companies are experimenting with agents that can read patient records, flag abnormal values, search medical literature, and draft a preliminary report for a clinician to review. The agent handles the information-gathering burden; the clinician makes the clinical judgement [3].

In every pattern above, the agent's role is to handle the *repetitive, multi-step information work* so a human can focus on the *judgement and decision* work. Agents augment humans — they do not replace the need for human oversight.

## 8. Best Practices

**Be precise about the goal.**
An agent is only as good as the goal you give it. Vague goals produce unpredictable plans. Write the goal as if you were briefing a new employee: include what success looks like, what format the output should be in, and any hard constraints [1].

**Give the agent only the tools it needs.**
Every tool you add is a way the agent can take an unintended action. Start with the minimum set and add tools as you confirm the agent handles them correctly [2].

**Expect to iterate.**
The first run of a new agent almost always produces something imperfect. Treat the first run as a diagnostic — examine the plan the agent made and where it went wrong — then refine the goal or the tools [3].

**Keep humans in the loop for high-stakes actions.**
If the agent can send emails, move money, delete files, or take other irreversible actions, build in a human-approval checkpoint before those actions execute. Autonomous action is a tool; irreversible autonomous action is a risk [1][3].

**Watch for hallucination in multi-step chains.**
A single hallucinated fact in step 2 can corrupt every downstream step. Build in checks: have the agent cite the source for every factual claim it makes, or verify critical outputs before the loop continues [2].

**Log everything.**
Each step in the agent loop should be recorded — what the agent planned, what tool it called, what the tool returned, what the agent concluded. Without logs, debugging a failure in a 20-step chain is nearly impossible.

## 9. Hands-On Exercise

This exercise connects to the week's **Capability Probe lab**.

In the Capability Probe, you will test an AI assistant (such as Claude) across five task types: creative, factual, logical, ethical, and coding. For this topic's extension, add a sixth dimension to your probe:

**Agent-mode simulation.** Give the assistant a *goal* instead of a *question*. Example: "I want to compare three free online tools for making presentation slides. Research your options and give me a comparison table with pros and cons."

Observe and document:
1. Does the assistant break the goal into steps on its own, or does it produce a single flat answer?
2. Does it acknowledge what it cannot do (for example, it cannot browse the web in real time)?
3. Does it ask a clarifying question before starting, or does it guess?
4. Where does the response feel like it came from a single-step LLM, and where does it feel like multi-step reasoning?

Compare this to your other five task-type probes. Record what worked, what failed, and whether the assistant hallucinated any specific facts in its comparison.

This exercise gives you a concrete first feel for the gap between a standalone LLM response and agent-like behaviour — even before you work with a real agent framework.

## 10. Key Takeaways

- An **AI agent** uses an LLM as its reasoning core but surrounds it with a goal, a plan, tools, memory, and a feedback loop — allowing it to pursue multi-step objectives autonomously rather than responding to a single prompt [1][2].
- The five core components of an agent loop are: **goal** (what to achieve), **planning** (how to get there), **tool use** (taking real-world actions), **memory** (carrying information across steps), and the **feedback loop** (observe, reason, act — then repeat) [2][3].
- The transition from LLM to agent does not change the underlying model — it changes what surrounds it: the LLM becomes a decision-maker inside a larger system rather than a one-shot responder [3].
- Today's agents are powerful for multi-step information tasks but still prone to hallucination, goal ambiguity, and compounding errors over long chains — making human oversight essential in most production settings [1][2].
- The core practitioner pattern is: define a precise goal, equip the agent with the minimum necessary tools, instruct it via a system prompt, run the loop, and review the output before acting on it [1].

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
