---
topic_id: "4.5"
title: "Tool use — AI calling search, calculator, and code runner"
position_in_module: 3
generated_at: "2026-06-17T00:00:00Z"
resource_count: 3
---

# 1. Tool Use — AI Calling Search, Calculator, and Code Runner — Topic Corpus

## 2. Prerequisites

This topic builds directly on **4.4 — Agents, planning loops, and the observe-think-act cycle**. In that topic you learned what an agent is, what a tool is (at the definition level), and how the LLM (Large Language Model) sits at the centre of an agent as its reasoning engine. Here in 4.5 we go much deeper into the tool side: how calling a tool actually works, which tools are most common, and what difference they make to what an AI can do.

Topics 4.1–4.3 (foundation models, fine-tuning, RAG) are background that enriches this topic but are not required entry gates.

## 3. Learning Objectives

By the end of this topic you will be able to:

- Explain, in plain language, what it means for an AI to "call a tool" and why an LLM alone cannot perform that action.
- Describe the four-step tool-use cycle (request → route → execute → return) without prompting.
- Give a concrete example of each of the three core tool types: search, calculator, and code runner.
- Distinguish what each tool type fixes — information freshness, mathematical accuracy, and code execution — compared with an LLM working alone.
- Identify one real-world AI product feature that relies on tool use.
- Recognise that tool use is what turns a standalone language model into a genuinely capable AI assistant.

## 4. Introduction

Imagine you ask a knowledgeable friend a question: "What is the exchange rate between euros and dollars right now?" Your friend is very smart, but if they have been asleep for a year, they cannot tell you the current rate. They have to pick up their phone and look it up. The looking-up is a tool use.

LLMs face exactly this problem. They are trained on a fixed snapshot of the internet. After that training is done, they know nothing new [1]. They cannot browse the web. They cannot do precise arithmetic reliably. They cannot run a piece of code and tell you the output. When you ask an LLM "What did the FTSE close at today?" or "What is 2,847 × 1,293?" or "Does this Python script produce an error?", the model has to guess — and guessing goes wrong.

Tool use is the solution. A tool is an external capability — a search engine, a calculator, a code execution environment — that the AI can call out to when it needs information or computation it cannot produce from memory alone [1][2]. The LLM decides it needs help, asks for it, receives the answer, and folds that answer into its response. The user sees one clean answer; the fact that the AI made a side trip to look something up is mostly invisible.

This is not magic. It is a very specific, structured handshake — a protocol — between the LLM and an external system. Understanding that protocol is what this topic is about.

## 5. Core Concepts

### 5.1 Why an LLM needs tools at all

An LLM is essentially a very sophisticated pattern-matching system. During training it read enormous amounts of text and learned to predict what words come next [1]. That training gave it a broad, general understanding of language, facts, and reasoning. But three things are permanently outside what it can do on its own:

| Gap | Why it exists | What it means in practice |
|---|---|---|
| **Knowledge cutoff** | Training ended at a specific date; nothing after that date is in the model | The model does not know about news, prices, or events after its cutoff |
| **Precise arithmetic** | The model works with tokens (chunks of text), not numbers; it approximates rather than calculates | Multi-step maths is unreliable — it can give a plausible-looking wrong answer |
| **Code execution** | The model has read lots of code but cannot actually run any | It cannot tell you whether a piece of code works without testing |

Tools patch each of these gaps directly [2]. A search tool supplies current information. A calculator supplies exact arithmetic. A code runner actually executes code and returns the real output. Together they transform the LLM from a brilliant-but-limited text predictor into something that can act reliably in the world [1].

### 5.2 The four-step tool-use cycle

Tool calling follows a fixed four-step pattern. Every major AI system that supports tools — ChatGPT's plugins, Google Gemini, Anthropic's Claude — uses a version of this cycle [1][2].

**Step 1 — Decide.** The LLM reads the user's message and decides whether it can answer from its training alone or whether it needs to call a tool. This decision is made internally by the model; the user does not see it. Example: the user asks "What time is it in Tokyo right now?" — the model recognises it does not know the current time and flags that a search or clock tool is needed.

**Step 2 — Request.** The model forms a structured request — a precisely formatted message saying which tool it wants to call and what inputs to give it. This request is not sent to the user; it goes to a layer of software sitting between the model and the outside world [2]. Think of it as the model writing a note that says: "Please call the search tool with the query: current time in Tokyo."

**Step 3 — Execute.** The routing software receives the request, calls the actual external system (the real search engine, the real calculator, the real code execution environment), and collects the result. The LLM is paused and waiting during this step — it is not involved [1].

**Step 4 — Return.** The result comes back to the LLM. The model reads it and uses it to compose the final reply to the user. From the user's perspective, the whole cycle usually takes a second or two and looks like the AI simply "knew" the answer.

This cycle can run more than once in a single conversation. If the model decides it needs two different tools — say, a search and then a calculator — it can chain the calls: call the first tool, get the result, call the second tool, get that result, then write the final answer [2].

### 5.3 The three core tool types

#### Search

**Search tool** — an integration that lets the LLM send a query to a live search engine or a curated knowledge base and receive back the top results.

What it fixes: the knowledge-cutoff problem. Instead of relying on training data from months or years ago, the model can retrieve up-to-date information right now [1][3].

Concrete example: A user asks an AI assistant "Who won the Champions League final last week?" Without a search tool, the model might give the winner from a year ago or admit it does not know. With a search tool, it queries a search engine, receives the current answer, and replies accurately.

Why this matters: A large share of the questions people actually ask AI assistants are time-sensitive — news, prices, sports results, weather, stock movements. Search is the tool that makes those questions answerable [3].

#### Calculator

**Calculator tool** — an integration that sends a mathematical expression to a reliable arithmetic engine and returns the exact numerical result.

What it fixes: the precise-arithmetic problem. LLMs are not built to be calculators. They can do simple arithmetic in their heads much of the time, but as numbers grow larger or problems grow more complex they start making errors — producing answers that look reasonable but are wrong [2].

Concrete example: A user asks "If I invest £5,000 at 4.75% annual interest compounded monthly for 8 years, what do I end up with?" This is not trivially simple. An LLM without a calculator will often produce a plausible-sounding figure that is slightly (or significantly) wrong. With a calculator tool, the expression is sent to a genuine arithmetic engine and the exact result comes back.

Why this matters: In any context involving money, measurements, dates, statistics, or science, wrong arithmetic is a serious problem. A calculator tool eliminates that class of error entirely [1].

#### Code runner

**Code runner** (also called a code execution tool or interpreter tool) — an integration that takes a piece of code, runs it in a sandboxed environment, and returns the output.

What it fixes: the inability to actually test or execute code. An LLM can read and write code — it has processed enormous quantities of it during training — but it cannot run code. It can only predict what the output should be. Predicting and running are not the same thing [2][3].

Concrete example: A user pastes a short program and asks "Does this code produce an error?" Without a code runner, the model inspects the code visually and makes a guess — which can be wrong. With a code runner, the code is actually executed, and the real output (or error message) comes back. The model then reports what actually happened, not what it predicted would happen.

Why this matters for a non-technical audience: even if you never write code yourself, AI assistants increasingly do small computational tasks on your behalf — converting data between formats, doing lookups, cleaning up a spreadsheet. The code runner is what makes those tasks reliable rather than guesswork.

### 5.4 What tools enable — a before-and-after view

It helps to see explicitly what changes when tools are available.

| User question | LLM alone | LLM with tools |
|---|---|---|
| "What is Bitcoin trading at right now?" | Gives a price from its training data — possibly months out of date | Calls search → returns today's price |
| "What is 17,432 × 298, to the nearest whole number?" | Often correct for simple cases, but increasingly error-prone for large numbers | Calls calculator → returns 5,194,736 (exact) |
| "Does this code snippet crash?" | Reads the code and guesses | Calls code runner → returns actual error or output |
| "Summarise this article for me" | Can do this from training knowledge alone — no tool needed | Does not call a tool; answers directly |

The last row is important: tools are not called for every question. The model decides, per question, whether a tool is needed. If the model can answer reliably from its training — for example, "Explain what photosynthesis is" — it does so directly, without any tool call [1][2].

### 5.5 The handshake in plain language

The technical detail behind Step 2 (the request) is worth understanding at one level up from implementation.

When the LLM wants to call a tool, it does not simply type a message to the tool in plain English. It produces a structured description: which tool to call, and what input to give it. This structured description follows a specific format that the routing software can reliably parse and act on [2].

Think of it like filling in a form. If you want a librarian to look something up, you write on the request slip: **Section: Reference, Query: population of Brazil 2025**. You do not write a free-form essay. The structured form means the librarian knows exactly what you want and can act immediately. The LLM's tool request works the same way — it is a precise, machine-readable instruction, not a vague wish [2].

The routing software then acts as the intermediary: it receives the form, performs the look-up, and hands the result back. The LLM was never talking directly to the search engine or the calculator — there is always a software layer in between that handles the actual connection [1][2].

This matters for scope: the exact format of the request, the way tools are defined so the model knows they exist, and the frameworks that manage multi-tool conversations are all advanced topics you will encounter later. For now, the key idea is that the handshake is structured and deliberate, not ad-hoc.

### 5.6 Tools in the context of agents (building on 4.4)

In 4.4 you learned that an agent is an AI system that can plan and take actions over multiple steps, using tools as one of its core capabilities. Tool use is what makes the "act" part of the observe-think-act cycle concrete.

Without tools, an agent can only observe (read the conversation) and think (reason about it). Tools are what give the agent the ability to *act* — to reach outside the conversation and do something in the world [1].

A single tool call is not an agent. An agent is a system that can call tools as part of a multi-step plan. But each individual tool call follows the four-step cycle described in Section 5.2. Understanding the cycle is therefore the foundation for understanding everything agents do.

## 6. Implementation

This section shows the four-step cycle as a numbered procedure, so you can trace any real-world tool call against it.

**Trace the cycle — a worked example.**

Scenario: A user asks an AI assistant equipped with a search tool: "What was the closing price of Apple shares yesterday?"

1. **Decide.** The model reads the question. It knows stock prices are time-sensitive and not in its training data. Decision: a tool call is needed. Tool type: search.

2. **Request.** The model generates a structured request — something like: _Tool: web_search | Query: "Apple AAPL closing price [yesterday's date]"_. This request is passed to the routing software layer; the user does not see it.

3. **Execute.** The routing software calls the actual search engine. The search engine returns a result page. The routing software extracts the relevant number and passes it back to the model.

4. **Return.** The model reads the returned price. It composes a reply: "Apple (AAPL) closed at $213.42 yesterday, according to market data." The user receives this as a plain, confident answer.

Total elapsed time for Steps 2–4: typically under two seconds. The user experiences it as the model simply knowing the answer.

**What happens when a tool fails?**

If the external system is unavailable or returns an error, the routing software passes that error back to the model in Step 4. The model then has to decide: try again, try a different tool, or tell the user it could not complete the request. Handling failures gracefully is part of robust tool-use design — but the mechanics follow the same four-step pattern.

## 7. Real-World Patterns

Tool use is not a theoretical concept. It is already deployed in products you may have encountered.

**ChatGPT with web browsing enabled.** OpenAI's ChatGPT can be given access to a web search tool. When enabled, the model routes time-sensitive queries through a live search rather than relying on training data. Users see a small note indicating that the model "searched the web" before answering [3].

**AI assistants with code interpreters.** Several AI products offer what they call a "code interpreter" or "advanced data analysis" feature. Behind the scenes this is a code runner tool. The user can paste data or ask a computation question; the model writes code, runs it via the tool, and returns the result — not a prediction of the result, but the actual output [2][3].

**Calculator integrations.** Many AI-powered customer service tools and financial assistants use a calculator tool for anything involving money. This is a deliberate design choice: using a dedicated arithmetic tool instead of the model's in-built prediction eliminates a class of errors that could otherwise cause real harm in financial contexts [1].

**Search-augmented chatbots.** Enterprise search tools — internal knowledge bases, HR assistants, IT helpdesks — often combine an LLM with a search tool pointed at the company's own documents. The LLM handles the conversation; the search tool fetches the right policy document or procedure. This is a pattern closely related to RAG (Retrieval-Augmented Generation, covered in topic 4.3), where the retrieval step is implemented as a tool call [1].

## 8. Best Practices

These are principles that guide how tool use is designed — relevant for understanding why AI systems are built the way they are, even if you are not building one yourself.

**Tools are called only when needed.** A well-designed system does not call a tool for every message. The model should answer directly from its knowledge when it can, and reach for a tool only when a tool genuinely improves the answer. Unnecessary tool calls slow responses and add complexity [2].

**Results should be verified, not blindly trusted.** A tool returns a result, but that result can itself be wrong — a search engine can return an outdated cached page, for example. Responsible AI design includes awareness that tools are not infallible [1].

**Tool calls should be transparent to users when they matter.** When a tool significantly shapes an answer — especially a search result that a user might want to verify — good practice is to indicate that a search was performed and, where possible, to show the source [3].

**Scope is defined in advance.** The model can only call tools it has been told about. A model is given a list of available tools at the start of a session. It cannot spontaneously invent new ones or call tools that have not been described to it [1][2].

## 9. Hands-On Exercise

This exercise connects to the lab activity for this session.

**Compare: with tools vs. without tools.**

Pick two questions — one time-sensitive (e.g. "What is the current price of gold?") and one evergreen (e.g. "What is the boiling point of water?").

1. Ask both questions to an AI assistant that clearly states it has no internet access (or turn off any browsing feature if one exists).
2. Ask the same questions to an AI assistant with a live web-search tool enabled.
3. For the time-sensitive question: how do the answers differ? Which is more reliable and why?
4. For the evergreen question: do the answers differ at all? What does this tell you about when tool use adds value versus when it is unnecessary?

This mirrors the "same question with and without" structure in the session lab activity.

## 10. Key Takeaways

- **An LLM alone has three fixed gaps:** it cannot access information after its training cutoff, it cannot perform precise arithmetic reliably, and it cannot execute code. Tools patch exactly these three gaps.
- **Tool use follows a four-step cycle:** the model decides a tool is needed, forms a structured request, the request is routed to an external system that executes it, and the result returns to the model to inform its final answer.
- **The three core tool types are search, calculator, and code runner** — each closing one specific gap.
- **Not every question triggers a tool call.** The model decides per question whether its training knowledge is sufficient. For evergreen questions it answers directly; for time-sensitive, computational, or execution questions it routes to a tool.
- **Tool use is what turns a language model into a capable assistant.** Without tools, the model is brilliant but limited. With tools, it can act reliably in the real world.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
