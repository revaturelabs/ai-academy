---
topic_id: "12.11"
title: "Making the first API call — install the library, write the call, run in Colab"
position_in_module: 3
generated_at: "2026-06-15T00:00:00Z"
resource_count: 3
---

# 1. Making the First API Call — Install the Library, Write the Call, Run in Colab — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **12.9** — What is an API and how does an API call work (API, client, server, request-response cycle, endpoint, HTTP method, JSON, API key)
- **12.10** — The Anthropic API structure: Messages array, model parameter, and authentication (Messages API, `messages` array, `role`, `content`, system prompt, user prompt, `AnthropicClient`, authentication)

All Python foundations from topics 11.1 through 12.8 (variables, functions, dictionaries, error handling, etc.) are assumed and used without re-definition.

---

## 3. Learning Objectives

By the end of this topic, learners will be able to:

- **Install** the `anthropic` Python library in a Google Colab notebook using `!pip install anthropic`
- **Import** the `anthropic` module and create an `AnthropicClient` object that connects to the Anthropic API
- **Explain** what the `max_tokens` parameter controls and why it must be included in every `client.messages.create()` call
- **Write** a complete `client.messages.create()` call with all four required elements: `model`, `max_tokens`, the `messages` list, and at least one message dict
- **Run** the call inside a Colab cell and identify where Claude's reply text appears in the response object
- **Access** Claude's reply text using the expression `message.content[0].text`

---

## 4. Introduction

Think about ordering food through a delivery app. You open the app (that is the client), you tap "send order" (that is the request), and a few seconds later your meal arrives (that is the response). The app does not grow a kitchen — it talks to an existing restaurant through a well-defined channel. In the same way, your Python code does not run Claude. It talks to Anthropic's servers through a well-defined channel called the **Messages API**. Topic 12.10 introduced that channel — you learned what the messages array looks like, what the model parameter does, and how authentication works with an API key. Everything you need conceptually is already in your head.

This topic is about sending the first real message. Three practical steps stand between you and Claude's first reply: install the library that gives Python the vocabulary to talk to the API, import it and create the connection object, and then write the actual call. Each step is one or two lines of code. By the end of this topic you will have run each of those lines in a Google Colab notebook and seen Claude respond.

Google Colab is a free, browser-based Python environment. You do not need to install anything on your own computer. Every cell you run in Colab is executed on a cloud machine, which means `!pip install` commands (explained below) work the same way they would on any fresh Linux machine — Colab just adds the `!` prefix to let Python cells run shell commands. Anthropic's official learning materials are built around Colab notebooks for exactly this reason: it removes all setup friction and lets you focus on the API itself [1].

One small concept is being introduced here that was deliberately deferred from 12.10: **`max_tokens`**. This parameter is required on every call. Without it, the SDK raises an error before the request even leaves your computer. It is covered fully in Section 5.3.

---

## 5. Core Concepts

### 5.1 Installing the `anthropic` Library in Colab

Before Python can talk to the Anthropic API, the Python process running in your Colab session needs the `anthropic` package. A **package** (also called a **library**) is a bundle of pre-written code someone else has published so that you can use it without writing everything from scratch. The `anthropic` package is the official Python SDK (Software Development Kit — a toolkit for a specific service) that Anthropic publishes and maintains [2].

**`pip`** is the standard Python package installer. When you run `pip install <name>`, it downloads the named package from the internet and makes it available to your Python environment. On a normal laptop you would open a terminal and type `pip install anthropic`. In Colab you are inside a Python cell, so Python would normally interpret `pip install anthropic` as Python code — which it is not. The **`!` prefix** tells Colab to send the rest of the line to the underlying shell (the operating system's command runner) instead of running it as Python [1].

The exact command to run in a Colab cell is:

```python
!pip install anthropic
```

You will see output like:

```
Collecting anthropic
  Downloading anthropic-0.x.x-py3-none-any.whl ...
Successfully installed anthropic-0.x.x ...
```

The version number changes as Anthropic releases updates, but the install command stays the same [2]. Once the cell finishes, the package is available for the rest of that Colab session. If you close the session and reopen it, you must run the install cell again — Colab sessions are temporary.

**Key point:** `!pip install anthropic` only needs to run once per Colab session. Conventionally it goes in the very first cell of your notebook so it is always ready.

### 5.2 Importing the Library and Creating a Client Object

After installation, the next step is to bring the library into your Python code. The **`import` statement** is how Python loads a module (a named unit of code) into your current script so you can use the names it defines.

```python
import anthropic
```

This one line gives your script access to everything in the `anthropic` package [3].

The most important name inside that package is `Anthropic` — it is a **class** (a blueprint for an object). You create an instance of it by calling `anthropic.Anthropic()`. In Python, calling a class like a function produces an **object** — a value that bundles data and behavior together. This object is your **client**. A client, as established in 12.9, is the piece of software that sits on your side of the API conversation and knows how to format and send requests.

```python
client = anthropic.Anthropic()
```

**Where does the API key go?** By default, the Anthropic SDK looks for an environment variable (a named value stored in the operating system, separate from your code) called `ANTHROPIC_API_KEY`. If that variable is set, `anthropic.Anthropic()` reads it automatically — you do not need to paste your key into the code. You can also pass the key explicitly:

```python
client = anthropic.Anthropic(api_key="sk-ant-...")
```

However, pasting a real key directly in a notebook is a security risk (it is easy to accidentally share the notebook). The Best Practices section (Section 8) covers the safer pattern. For now, understand that the client object needs your key to authenticate requests, and the SDK retrieves it automatically if `ANTHROPIC_API_KEY` is set in the environment [1][3].

Once `client` exists, you have a live connection object ready to send requests. No data has been sent yet — creating the client just prepares the channel.

### 5.3 The `max_tokens` Parameter — What It Controls and Why Every Call Needs It

**Tokens** are the unit Claude uses internally to process text. A token is roughly three to four characters, or about three-quarters of an average English word. When you send a message to Claude, it reads your message (input tokens) and generates a reply (output tokens). The total output tokens produced determine a large part of the cost and time of every call.

**`max_tokens`** is a required integer parameter that caps how many output tokens Claude will generate in its reply. If you ask Claude a question that could be answered in 500 tokens but you set `max_tokens=100`, Claude stops at 100 tokens — the reply will be cut short. If you set `max_tokens=1024`, Claude will generate up to 1024 output tokens and stop there, even if its answer is shorter [1][3].

Why is it required? The parameter is mandatory because without an explicit upper limit, a single API call could generate an enormous response — very expensive and possibly running for many seconds. The SDK enforces the requirement at the call site so the error is caught before any network traffic happens [1].

Practical guidance for beginners:

| Goal | Suggested `max_tokens` |
|---|---|
| Short factual answer | 256 – 512 |
| Paragraph-length reply | 512 – 1024 |
| Multi-paragraph or structured output | 1024 – 2048 |

For your first test call, `max_tokens=1024` is a safe default that is large enough for most answers and not wasteful.

### 5.4 Writing the `messages.create()` Call with All Required Parameters

The object `client` that you created in Section 5.2 has a property called `messages`, which in turn has a method called `create`. A **method** is a function that belongs to an object — you call it with dot notation: `client.messages.create(...)`.

This is the line that actually sends your request to the Anthropic API [1][3]:

```python
message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude! What is machine learning?"}
    ]
)
```

Four things to notice:

1. **`model`** — a string that tells the API which Claude model to use. `"claude-opus-4-5"` is one current model name. Model names are listed in Anthropic's documentation and change as new versions release [1].

2. **`max_tokens`** — the cap you learned in Section 5.3. It is required. Omitting it raises a `TypeError` before the request leaves your machine.

3. **`messages`** — a Python list containing one or more dictionaries. Each dictionary has two keys: `"role"` and `"content"`. As established in 12.10, `"role"` is either `"user"` (your message) or `"assistant"` (Claude's reply in a multi-turn conversation). `"content"` is the actual text.

4. **The return value** is stored in `message` (singular). The SDK does not just return a string — it returns a structured **response object** that wraps the full API response, including metadata. Section 5.5 explains what this object looks like.

The entire call is synchronous by default: Python pauses at this line, waits for the network round-trip to complete (typically one to three seconds for a short reply), and then continues. During the wait, the Colab cell spinner shows it is still running — this is normal [1].

### 5.5 Running the Call and Reading the Raw Response Object

When `client.messages.create(...)` returns, the variable `message` holds a response object. If you just print it, you see something like:

```
Message(id='msg_01XFDUDYJgAACzvnptvVoYEL', content=[ContentBlock(text='Machine learning is a field of artificial intelligence...', type='text')], model='claude-opus-4-5', role='assistant', stop_reason='end_turn', stop_sequence=None, type='message', usage=Usage(input_tokens=16, output_tokens=127))
```

This looks intimidating at first. It is a Python object whose fields map directly to the JSON the API returned. Here are the key fields a beginner needs to know right now:

- **`message.id`** — a unique identifier Anthropic assigns to this specific request. Useful for debugging.
- **`message.model`** — confirms which model actually handled the request.
- **`message.role`** — always `"assistant"` (Claude's role) in a response object.
- **`message.stop_reason`** — `"end_turn"` means Claude finished its response naturally. `"max_tokens"` means it hit the token cap before finishing.
- **`message.usage`** — an object with `input_tokens` and `output_tokens`, showing exactly how many tokens were consumed. Useful for understanding cost.
- **`message.content`** — a list of **content blocks**. Each block has a `type` (usually `"text"`) and the actual text. In most calls there is exactly one block [1][3].

The reply text itself is one level deeper, inside that `content` list. The next section shows how to get it.

### 5.6 Accessing the Reply Text with `message.content[0].text`

The full Python expression to get Claude's reply as a plain string is:

```python
reply_text = message.content[0].text
print(reply_text)
```

Breaking it down piece by piece:

- **`message`** — the response object from the call.
- **`.content`** — the list of content blocks (usually just one for a simple call).
- **`[0]`** — list indexing, introduced in topic 12.4. Index `0` is the first (and usually only) block. In a standard call with one text response, there is always a block at index 0.
- **`.text`** — the string attribute of that content block holding the actual reply text [1][3].

After `print(reply_text)`, the Colab cell output will show Claude's words directly — just plain text, no object wrapper.

Why not just `message.content`? Because `.content` is a list object, not a string. `message.content[0]` is a content block object, not a string. `.text` is the string. Each step navigates one level deeper into the object structure until you reach the data you actually want.

This three-part expression `message.content[0].text` is the single most-used line in all beginner Anthropic Python code. Memorize it or write it down.

---

## 6. Implementation

A numbered walkthrough from a blank Colab notebook to Claude's first reply.

**Step 1 — Open a new Google Colab notebook.**

Go to [colab.research.google.com](https://colab.research.google.com), sign in with a Google account, and click "New notebook". You will see an empty cell ready for input.

**Step 2 — Install the SDK (Cell 1).**

In the first cell, type and run:

```python
!pip install anthropic
```

Click the play button or press `Shift+Enter`. Wait for "Successfully installed anthropic-..." to appear in the output. This may take 10–20 seconds [2].

**Step 3 — Set your API key (Cell 2).**

In a new cell, set your API key as an environment variable using `os.environ`:

```python
import os
os.environ["ANTHROPIC_API_KEY"] = "sk-ant-YOUR-KEY-HERE"
```

Replace `"sk-ant-YOUR-KEY-HERE"` with your actual key from the Anthropic console. Do not share or publish this cell. See the Best Practices section for a safer approach.

**Step 4 — Import and create the client (Cell 3).**

```python
import anthropic
client = anthropic.Anthropic()
```

Run the cell. If no error appears, the client is ready. The SDK automatically read the `ANTHROPIC_API_KEY` environment variable you set in Step 3 [1].

**Step 5 — Write and run the call (Cell 4).**

```python
message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is machine learning in one sentence?"}
    ]
)
print(message.content[0].text)
```

Run the cell. After one to three seconds, Claude's reply will appear directly below the cell [1]. A typical output:

```
Machine learning is a branch of artificial intelligence where systems learn patterns
from data to make predictions or decisions without being explicitly programmed for
each task.
```

**Step 6 — Inspect the full response object (Cell 5, optional but recommended).**

```python
print(message)
print("---")
print("Stop reason:", message.stop_reason)
print("Tokens used:", message.usage.input_tokens, "in,", message.usage.output_tokens, "out")
```

The stop reason should be `end_turn`, confirming Claude finished naturally. The token counts tell you how much of the request was consumed [1].

---

## 7. Real-World Patterns

**Pattern 1: Install in its own cell at the top of the notebook.**
Notebooks shared on GitHub or Colab typically have a single "Setup" cell at the top that runs `!pip install ...` for all dependencies. This makes it clear what the notebook needs and lets a new user run setup once before anything else [1].

**Pattern 2: Keep the client creation outside loops.**
A common beginner mistake is creating a new `anthropic.Anthropic()` client object inside a loop that makes multiple calls. Creating the client has a small overhead (reading the key, setting up the HTTP connection pool). Create it once before the loop, then call `client.messages.create()` many times:

```python
client = anthropic.Anthropic()            # once, outside the loop
for question in questions:
    msg = client.messages.create(...)     # many times, inside
    print(msg.content[0].text)
```

**Pattern 3: Always store the full response before accessing `.text`.**
Some beginners chain everything into one line: `print(client.messages.create(...).content[0].text)`. This works but throws away the response object, so you lose `stop_reason`, `usage`, and `id`. Store the response in a variable first, then access `.text` [3].

**Pattern 4: Verify `stop_reason` for completeness.**
If `message.stop_reason == "max_tokens"`, the reply was cut short. For any use case where a complete answer matters (structured output, summaries, code), always check this field after the call [1].

---

## 8. Best Practices

- **Never hardcode your API key in a shared notebook.** In Colab, use the Secrets panel (the key icon in the left sidebar) to store `ANTHROPIC_API_KEY`, then access it with `from google.colab import userdata; os.environ["ANTHROPIC_API_KEY"] = userdata.get("ANTHROPIC_API_KEY")`. This way the key is never in the cell text and cannot be accidentally published [1].

- **Choose `max_tokens` intentionally.** Start with `1024` for general testing. Once you know the shape of your expected responses (e.g., "a JSON object with five fields"), set `max_tokens` to roughly twice the expected output length. Too low and you get truncated replies; unnecessarily high wastes money and slows tests [1][3].

- **Run the install cell every new session.** Colab environments reset when a session closes. Always put `!pip install anthropic` in Cell 1 so the package is ready whenever you reopen the notebook [2].

- **Confirm the response before parsing.** After your first call, print `message` and `message.stop_reason` before writing any code that processes the text. This confirms the call succeeded and shows you what the raw object looks like — valuable before you build more complex logic on top of it [1].

- **Use a lightweight model for testing.** When iterating on your code, use `"claude-haiku-3-5"` (Anthropic's fastest, lowest-cost model). Switch to a more capable model like `"claude-opus-4-5"` once the code structure is confirmed. This keeps testing costs near zero [1].

---

## 9. Hands-On Exercise

**Exercise: Your domain's first question to Claude**

This exercise connects the steps above to the lab domain (the domain system from Lab Part 2).

1. Open a new Colab notebook.
2. In Cell 1, install the SDK: `!pip install anthropic`
3. In Cell 2, set your API key using `os.environ["ANTHROPIC_API_KEY"] = "sk-ant-..."`.
4. In Cell 3, import `anthropic` and create `client = anthropic.Anthropic()`.
5. In Cell 4, write a `client.messages.create()` call where the user message is a question relevant to your lab domain — for example: `"What are three key risks in early-stage startup investing?"` (adjust to your domain).
6. Set `max_tokens=512`.
7. Print `message.content[0].text`.
8. Run the cell and read Claude's reply.
9. Then print `message.stop_reason` and `message.usage.output_tokens`. Did Claude finish naturally? How many output tokens did it use?

Expected outcome: Claude returns a coherent answer to your domain question, `stop_reason` is `"end_turn"`, and `output_tokens` is less than 512.

---

## 10. Key Takeaways

- **`!pip install anthropic`** installs the Anthropic SDK into the current Colab session. The `!` prefix routes the command to the shell, not Python's interpreter. The install is temporary and must be repeated each new session [2].
- **`anthropic.Anthropic()`** creates a client object that authenticates to the Anthropic API using the `ANTHROPIC_API_KEY` environment variable. Create it once per script, before any calls [1][3].
- **`max_tokens`** is a required parameter that caps Claude's output length in tokens. Omitting it raises an error before any network request is sent. `1024` is a safe default for initial testing [1].
- **`client.messages.create(model=..., max_tokens=..., messages=[...])`** is the single line that sends your request and returns a response object containing Claude's reply and metadata [1][3].
- **`message.content[0].text`** is the expression that extracts Claude's reply as a plain Python string from the response object. Each part — `.content`, `[0]`, `.text` — navigates one level deeper into the structured response [1].

---

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
