<!-- nav:top:start -->
[⬅ Previous: 3.2 — The rise of large language models (LLMs)](../../3-2-the-rise-of-large-language-models-llms/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 3.4 — How LLMs work ➡](../../../2-how-llms-work/3-4-how-llms-work-tokens-training-and-inference/artifacts/reading.md)
<!-- nav:top:end -->

---

# The Move to AI Agents

## Overview

You have already met the LLM (Large Language Model) â€” you send it a prompt and it sends back a response. That is powerful, but it has a hard limit: one question, one answer, then it forgets everything. An **AI agent** breaks that limit by giving the LLM a *goal* to pursue across many steps, tools to act on the world, and memory to keep track of progress. Understanding agents is the bridge from "AI as a chatbot" to "AI as an autonomous assistant."

## Key Concepts

### Standalone LLM vs. AI Agent

Think of a plain LLM as a brilliant expert locked in a room with no phone, no notebook, and no internet. They answer your questions brilliantly â€” but they cannot look anything up, and they forget the conversation the moment you leave. An **AI agent** gives that same expert a phone, a notebook, a computer, and a goal to work toward [1].

The table below captures the key differences:

| | LLM (standalone) | AI agent |
|---|---|---|
| **Input** | A single prompt | A goal (desired end-state) |
| **Output** | One response | A sequence of actions + final result |
| **Steps** | One | Many â€” planned and executed by the system |
| **Tools** | None | Web search, calculators, API calls, file access |
| **Memory** | None between calls | Can carry information across steps |

The LLM is still the engine inside the agent. What changes is everything *surrounding* it [1].

### The Five Components of an Agent Loop

Most AI agent architectures share five building blocks. Each one solves a specific limitation of the plain LLM [1][2].

**1. Goal**
The **goal** is a description of what the agent is supposed to accomplish â€” specific enough that the system can judge when it is done. Without a clear goal, the agent has no way to decide when to stop.

- Example: "Find the three cheapest flights from Mumbai to London in July and return them as a table."

**2. Planning**
**Planning** is how the agent breaks a big goal into smaller steps it can actually take. The LLM reads the goal and writes a plan: "First, search for flights. Then filter by price. Then format the results." The LLM's ability to reason in language makes this possible [2]. Plans can also be revised as the agent learns new information mid-run.

**3. Tool use**
**Tool use** is the agent's ability to call external functions or services. An LLM alone can only produce text â€” tools let it take real actions [1]:

- **Web search** â€” look something up in real time
- **Calculator** â€” perform arithmetic reliably
- **API (Application Programming Interface) call** â€” talk to an external service (book a flight, send an email, read a database). An API is a standardised way for one software system to request something from another.
- **File access** â€” read or write documents
- **Code execution** â€” run a snippet of code and receive the output

The agent decides *when* to use each tool and *what to pass to it*, based on its current plan.

**4. Memory**
**Memory** lets the agent carry information across steps. Two types matter here:

- **Short-term memory** â€” everything the agent has seen so far in the current run, held in the LLM's context window. This is temporary and vanishes when the session ends.
- **Long-term memory** â€” facts written to a file or database that persist across separate sessions [2].

Without memory, an agent would forget what it found in step 1 by the time it reaches step 3.

**5. Feedback loop**
The **feedback loop** is the mechanism that keeps the agent running. After each action the agent receives an *observation* â€” the result of what it just did. That observation goes back into the LLM, which decides what to do next. This continues until the goal is reached [2][3].

Here is the loop in outline:

1. Receive goal
2. Make a plan
3. Execute next action (use a tool, write text, call an API)
4. Observe the result
5. Update the plan if needed
6. Repeat from step 3 until goal is reached

The diagram below shows how these five components connect:

![The Agent Loop](./diagram.png)
*The agent loop: Goal feeds into Planning, which drives tool-based Action, which produces an Observation that either closes the loop (goal met) or updates the Plan for the next cycle.*

### Capabilities and Limitations

Today's agents are genuinely useful â€” but they are not magic. Here is an honest picture.

**What agents do well:**
- Breaking large tasks into sub-tasks and working through them step by step [1]
- Using well-defined tools reliably when the goal is clear
- Summarising and transforming information from multiple sources
- Running long, repetitive research tasks that would take a human hours [3]

**What agents still struggle with:**
- **Hallucination propagates.** The agent's reasoning core is still an LLM, so it can still produce confident but incorrect plans â€” and then act on them [2].
- **Goal ambiguity.** A vague goal produces unpredictable behaviour. Precise goal-writing is a skill in itself.
- **Error compounding.** Each step can introduce a small mistake. Over 20 steps, small errors grow into large failures.
- **Cost.** Every step calls the LLM, which uses computing time and money [1].

Because of these limitations, most real-world agents today are **supervised** â€” a human reviews the plan or the result at key checkpoints. Fully autonomous agents are rare outside of narrow, well-tested tasks [3].

## Worked Example

This example shows the five components in action for a concrete task: "Given a company name, find its current stock price and write a one-paragraph summary of recent news about it."

**Step 1 â€” Define the goal clearly.**
The goal must be specific enough that the agent can recognise when it is done. "Find the current stock price of Company X and summarise 3 recent news headlines about it" gives the agent a clear finish condition. Vague goals produce unpredictable results.

**Step 2 â€” Equip the agent with tools.**
For this task, the agent needs:
- A stock-price API tool (to retrieve live price data)
- A web-search tool (to find current news)

The practitioner connects these tools to the agent. The agent does not use them automatically â€” it calls them when its plan requires it [1][2].

**Step 3 â€” Write a system prompt.**
The **system prompt** is a set of instructions the LLM receives before the user's goal. It tells the agent its role, which tools it has, what format to output in, and any constraints â€” for example: "Only report what the tools return; do not make up information" [3].

**Step 4 â€” Run the agent loop.**
The agent:
1. Plans: "I need the stock price, then recent news."
2. Calls the stock-price tool â€” receives a number.
3. Calls the web-search tool with the company name â€” receives headlines.
4. Drafts a summary paragraph from the tool results.
5. Decides the goal is met and returns the output.

**Step 5 â€” A human reviews the result.**
Is the stock price correct? Does the summary match the actual headlines? If the agent used the wrong ticker symbol or cited stale news, the practitioner refines the goal or the tools and runs again.

This five-step pattern â€” define, equip, instruct, loop, review â€” is the core of most agent deployments in use today [1].

## In Practice

AI agents are already at work across industries. The common thread is always the same: the agent handles repetitive, multi-step information work so a human can focus on judgement and decision-making.

**Customer support** â€” Many companies use agents to handle queries end-to-end: the agent reads the complaint, checks account data via an API call, drafts a response, and sends it (or routes it to a human with a summary already written if it is not confident) [1].

**Research and reporting** â€” Financial analysts use agents to gather data from regulatory filings and news sources, synthesise findings, and draft a first-version report. The analyst reviews and edits rather than starting from scratch [3].

**Software development** â€” Developer tools now include agent-mode features: given a task description, the agent reads relevant code files, writes new code, runs it, reads error output, fixes mistakes, and repeats â€” without hand-holding at each step [2].

**Best practices for using agents safely:**

- **Be precise about the goal.** Write it as if briefing a new employee â€” include what success looks like, required output format, and hard constraints [1].
- **Give the agent only the tools it needs.** Every extra tool is an extra way the agent can take an unintended action [2].
- **Keep humans in the loop for irreversible actions.** If the agent can send emails, move money, or delete files, build in a human-approval checkpoint before those actions execute [1][3].
- **Log everything.** Record what the agent planned, what tool it called, what the tool returned, and what it concluded. Without logs, debugging a failure in a 20-step chain is nearly impossible.

## Key Takeaways

- An **AI agent** uses an LLM as its reasoning core and surrounds it with a goal, planning, tools, memory, and a feedback loop â€” enabling it to pursue multi-step objectives autonomously rather than responding to a single prompt [1][2].
- The five core components of an agent loop are: **goal** (what to achieve), **planning** (how to get there), **tool use** (taking real-world actions via APIs and other services), **memory** (carrying information across steps), and the **feedback loop** (observe, reason, act â€” then repeat) [2][3].
- The move from LLM to agent does not change the underlying model â€” it changes what surrounds it. The LLM becomes a decision-maker inside a larger system rather than a one-shot responder [3].
- Today's agents are powerful for multi-step information tasks but are still prone to hallucination, goal ambiguity, and compounding errors over long chains â€” making human oversight essential in most real-world settings [1][2].
- The core practitioner pattern is: define a precise goal, equip the agent with the minimum necessary tools, instruct it via a system prompt, run the loop, and review the output before acting on it [1].
- This topic introduced the agent loop in action — the five components as they run. Topic 4.4 builds on this foundation with the architectural view: how goal, LLM core, memory, tools, and planning layer are structured inside a production agent system.

## References

1. Apideck. "AI Agents Explained: Everything You Need to Know in 2025." https://www.apideck.com/blog/ai-agents-explained-everything-you-need-to-know-in-2025
2. Data Science Dojo. "Agentic LLM in 2025." https://datasciencedojo.com/blog/agentic-llm-in-2025/
3. Proactive Management. "2025: The Year of the Agent â€” Building on the Foundation of LLMs." https://proactivemgmt.com/blog/2025/01/22/2025-the-year-of-the-agent-building-on-the-foundation-of-llms/

---
<!-- nav:bottom:start -->
[⬅ Previous: 3.2 — The rise of large language models (LLMs)](../../3-2-the-rise-of-large-language-models-llms/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 3.4 — How LLMs work ➡](../../../2-how-llms-work/3-4-how-llms-work-tokens-training-and-inference/artifacts/reading.md)
<!-- nav:bottom:end -->
