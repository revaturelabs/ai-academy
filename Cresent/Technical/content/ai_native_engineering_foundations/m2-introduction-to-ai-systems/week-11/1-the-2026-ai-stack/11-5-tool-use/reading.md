<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Cresent view of 11.5 — Tool Use.
     Source of truth: CIT 4.5.
     Regenerate: python Cresent/Technical/tools/generate_shared_readings.py -->
<!-- nav:top:start -->
Previous: [⬅ 11.4 — Agents (Concept)](../11-4-agents-concept/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../README.md#part-b)&emsp;·&emsp;[11.6 — Multimodal AI ➡](../11-6-multimodal-ai/reading.md)
<!-- nav:top:end -->

---

# Tool use â€” AI calling search, calculator, and code runner

## Overview

An LLM (Large Language Model) is trained on a fixed snapshot of the world â€” after training ends, it cannot look anything up, do reliable arithmetic, or run code. Tool use is the mechanism that closes those gaps: the AI calls an external capability, gets a real result back, and folds it into its answer. Understanding how that calling process works explains why modern AI assistants can answer time-sensitive questions, compute accurate figures, and test code â€” things a language model alone cannot do. [1]

This topic traces that process step by step. You will see what the three core tool types are, what problem each one solves, and how the structured handshake between the model and an external system turns a text generator into a genuinely capable assistant.

## Key Concepts

### Why an LLM needs tools

Think of a brilliant friend who has been off the grid for a year. They know a huge amount, but they cannot tell you today's exchange rate â€” they would have to pick up their phone and look it up. LLMs face the same constraint, plus two others.

| Gap | What it means |
|---|---|
| **Knowledge cutoff** | Training ended on a specific date; nothing after that date is in the model's memory [1] |
| **Precise arithmetic** | The model works with text patterns, not numbers â€” it approximates and can give a plausible-looking wrong answer |
| **Code execution** | The model has read lots of code but cannot actually run any â€” it can only predict the output |

Each gap can cause a real failure: stale facts, wrong calculations, or a "this works" verdict on code that actually crashes. Tools patch each gap directly [2].

### The four-step tool-use cycle

Every major AI system that supports tools â€” including ChatGPT, Google Gemini, and Anthropic's Claude â€” uses the same four-step pattern [1][2].

![Tool-use cycle â€” four-step flow](../../../../../../../../CIT/content-gen-example/content/m2-introduction-to-ai-systems/week-4/2-retrieval-agents-and-tools/4-5-tool-use-ai-calling-search-calculator-and-code-runner/artifacts/diagram.png)
*The four-step cycle: the LLM decides a tool is needed, forms a structured request, routing software executes the external tool, and the result returns to the LLM before the final answer reaches the user.*

1. **Decide.** The LLM reads the user's message and decides whether it can answer from training alone or whether a tool is needed. The user does not see this decision.

2. **Request.** The model forms a structured request â€” a precisely formatted message naming which tool to call and what input to give it. This goes to a routing software layer, not to the user. Think of it like filling in a library request slip: *Section: Reference, Query: current time in Tokyo*. The form is precise so the software can act immediately, without guessing [2].

3. **Execute.** The routing software calls the actual external system â€” the real search engine, the real arithmetic engine, the real code environment. The LLM is paused and waiting; it plays no part in this step [1].

4. **Return.** The result comes back to the LLM. The model reads it and composes the final reply. From the user's side, the whole cycle usually takes one to two seconds and feels like the AI simply knew the answer.

The cycle can run more than once. If the model needs two tools â€” say, a search followed by a calculator â€” it chains the calls: finish step 4 for the first tool, then restart at step 1 for the second [2].

### The three core tool types

#### Search tool

**Search tool** â€” an integration that lets the LLM send a query to a live search engine or knowledge base and receive current results back.

- **What it fixes:** the knowledge-cutoff problem. Instead of a stale training snapshot, the model gets information from right now [1][3].
- **Example:** A user asks "Who won the Champions League final last week?" Without a search tool, the model may give last year's result or admit it does not know. With a search tool, it queries a live engine and returns the correct, current answer.
- **Why it matters:** A large share of questions people ask AI assistants are time-sensitive â€” news, prices, sports results, weather. Search is what makes those questions answerable [3].

#### Calculator tool

**Calculator tool** â€” an integration that sends a mathematical expression to a dedicated arithmetic engine and receives the exact numerical result.

- **What it fixes:** the precise-arithmetic problem. LLMs handle simple sums well, but as numbers grow or problems grow more complex, errors creep in â€” the model produces a plausible-sounding figure that is actually wrong [2].
- **Example:** "If I invest Â£5,000 at 4.75% annual interest compounded monthly for 8 years, what do I end up with?" An LLM without a calculator will often give a slightly (or significantly) wrong figure. With a calculator tool, the expression goes to a genuine arithmetic engine and the exact answer returns.
- **Why it matters:** In contexts involving money, measurements, or science, wrong arithmetic is a serious problem. A dedicated calculator tool eliminates that entire class of error [1].

#### Code runner

**Code runner** (also called a code execution tool or interpreter tool) â€” an integration that takes a piece of code, runs it in a sandboxed environment (an isolated, safe area that cannot affect the rest of the computer), and returns the real output.

- **What it fixes:** the inability to actually test code. An LLM can read and write code, but it cannot run it â€” it can only predict what the output should be, and predicting is not the same as running [2][3].
- **Example:** A user pastes a short program and asks "Does this produce an error?" Without a code runner, the model inspects the code and makes a best guess â€” which can be wrong. With a code runner, the code is actually executed and the real output or error message comes back.
- **Why it matters even for non-coders:** AI assistants increasingly do small computational tasks on your behalf â€” converting data, cleaning up a spreadsheet, doing a lookup. The code runner is what makes those tasks reliable rather than guesswork.

### What changes when tools are available

| User question | LLM alone | LLM with tools |
|---|---|---|
| "What is Bitcoin trading at right now?" | Gives a price from training data â€” possibly months out of date | Calls search â†’ returns today's price |
| "What is 17,432 Ã— 298?" | Often correct for simple cases, increasingly error-prone for large numbers | Calls calculator â†’ returns 5,194,736 (exact) |
| "Does this code snippet crash?" | Reads the code and guesses | Calls code runner â†’ returns actual error or output |
| "Explain what photosynthesis is" | Answers directly from training â€” no tool needed | Does not call a tool; answers directly |

The last row matters: tools are not called for every question. The model decides, per question, whether its training knowledge is sufficient [1][2]. For stable, evergreen knowledge it answers directly; for time-sensitive, computational, or execution tasks it routes to a tool.

### Tools in the context of agents

In topic 4.4 you learned that an agent uses a planning loop to observe, think, and act. Tools are what make the *act* step concrete â€” without them, an agent can only observe and think. It cannot reach outside the conversation to do something in the world [1].

A single tool call is not an agent. An agent is a system that chains tool calls across a multi-step plan. But every individual call in that plan follows the four-step cycle above â€” making the cycle the foundation for understanding how agents operate.

This is why tool use matters beyond any single conversation. Once you understand that tools are what bridge reasoning and action â€” and that this bridge follows a structured four-step protocol â€” you have the mental model to make sense of every AI assistant that can search, calculate, or test code on your behalf. The same cycle runs inside coding assistants, research tools, and customer service bots. It is the mechanism that turns language understanding into real-world capability. [1][2]

## Worked Example

**Scenario:** A user asks an AI assistant equipped with a search tool: "What was the closing price of Apple shares yesterday?"

1. **Decide.** The model reads the question. Stock prices are time-sensitive and not in its training data. Decision: a search tool call is needed.

2. **Request.** The model generates a structured request â€” something like: *Tool: web_search | Query: "Apple AAPL closing price [yesterday's date]"*. This is passed to the routing software layer; the user does not see it.

3. **Execute.** The routing software calls the actual search engine. The search engine returns a result. The routing software extracts the relevant number and passes it back to the model.

4. **Return.** The model reads the returned price and composes its reply: "Apple (AAPL) closed at $213.42 yesterday, according to market data." The user receives a plain, confident answer.

**Total time for steps 2â€“4:** typically under two seconds. The user experiences it as the model simply knowing the answer.

**What if the tool fails?** If the external system is unavailable or returns an error, the routing software passes that error back to the model in step 4. The model then decides: try again, try a different tool, or tell the user it could not complete the request. The four-step pattern still governs the exchange â€” only the outcome changes.

## In Practice

Tool use is already deployed in products you may have encountered.

- **ChatGPT with web browsing.** When enabled, the model routes time-sensitive queries through a live search rather than relying on training data. A small note tells users the model "searched the web" before answering [3].
- **Code interpreter / advanced data analysis.** Several AI products let users paste data or ask computation questions; behind the scenes, the model writes code, runs it via a code runner, and returns the actual output â€” not a prediction [2][3].
- **Calculator integrations in financial tools.** AI-powered customer service and financial assistants use a dedicated calculator for anything involving money â€” a deliberate design choice that eliminates a class of errors that could cause real harm [1].
- **Search-augmented enterprise chatbots.** Internal IT helpdesks and HR assistants often combine an LLM with a search tool pointed at company documents. The LLM handles conversation; the search tool fetches the right policy or procedure. This is closely related to the RAG (Retrieval-Augmented Generation) pattern from topic 4.3, where retrieval is implemented as a tool call [1].

**Two design principles worth knowing:**

- **Call tools only when needed.** Unnecessary tool calls slow responses and add complexity. A well-designed system answers from knowledge when it can, and reaches for a tool only when it genuinely improves the answer [2].
- **Be transparent when a tool shaped the answer.** When a search result significantly influences a reply â€” especially one a user might want to verify â€” good practice is to surface that a search was performed and, where possible, to show the source [3].
- **Scope is defined at session start.** The model can only call tools it has been told about. A tool must be explicitly described to the model before the session begins â€” the LLM cannot invent new tools spontaneously [1].

## Key Takeaways

- **An LLM alone has three fixed gaps:** it cannot access information after its training cutoff, it cannot perform precise arithmetic reliably, and it cannot execute code. Tools patch exactly these three gaps.
- **Tool use follows a four-step cycle:** the model decides a tool is needed â†’ forms a structured request â†’ routing software executes the external call â†’ the result returns to the model to inform its final answer.
- **The three core tool types are search, calculator, and code runner** â€” each closing one specific gap: freshness, arithmetic accuracy, and real execution.
- **Not every question triggers a tool call.** The model decides per question whether its training knowledge is sufficient; for stable knowledge it answers directly.
- **Tool use is what turns a language model into a capable assistant.** Without tools, the model is brilliant but limited. With tools, it can act reliably in a world that changes every day.

## References

[1] IBM. "Tool Calling." *IBM Think*. https://www.ibm.com/think/topics/tool-calling

[2] Fowler, M. "Function Calling with LLMs." *martinfowler.com*. https://www.martinfowler.com/articles/function-call-LLM.html

[3] Claburn, T. "AI LLM Tool Calling." *The Register*, 26 Aug 2024. https://www.theregister.com/2024/08/26/ai_llm_tool_calling/

---
<!-- nav:bottom:start -->
Previous: [⬅ 11.4 — Agents (Concept)](../11-4-agents-concept/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../README.md#part-b)&emsp;·&emsp;[11.6 — Multimodal AI ➡](../11-6-multimodal-ai/reading.md)
<!-- nav:bottom:end -->
