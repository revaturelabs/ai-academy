<!-- nav:top:start -->
[⬅ Previous: 12.10 — The Anthropic API](../../12-10-the-anthropic-api-model-messages-array-system-prompt-user-pr/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 12.12 — Parsing the JSON response ➡](../../12-12-parsing-the-json-response-extracting-the-text-you-need/artifacts/reading.md)
<!-- nav:top:end -->

---

# Making the first API call — install the library, write the call, run in Colab

## Overview

Topic 12.10 introduced the Anthropic Messages API: what the messages array looks like, how the model parameter works, and how your API key authenticates each request. This topic puts that knowledge to work. Three short steps stand between you and Claude's first reply: install the Python library that lets your code talk to the API, import it and create a connection object, then write and run the actual call. By the end, you will have run all three steps inside a Google Colab notebook and seen Claude respond in plain text [1].

## Key Concepts

**Google Colab** is a free, browser-based Python environment. Every cell you run executes on a cloud machine — no local installation required. Anthropic's official learning materials are built around Colab because it removes all setup friction [1].

**Installing the `anthropic` library**

A **library** (also called a **package**) is a bundle of pre-written code you can reuse without writing it yourself. The `anthropic` package is the official Python **SDK** (Software Development Kit — a ready-made toolkit for a specific service) published by Anthropic [2].

**`pip`** is Python's standard package installer. In Colab you are inside a Python cell, so you prefix the install command with `!` to send it to the shell (the operating-system command runner) instead of the Python interpreter [1]:

```python
!pip install anthropic
```

**Importing and creating the client**

After installation, bring the library into your code and create a **client** — the object on your side of the API conversation that formats and sends requests:

```python
import anthropic
client = anthropic.Anthropic()
```

By default, `anthropic.Anthropic()` reads your key from an **environment variable** (a named value stored in the OS, outside your code) called `ANTHROPIC_API_KEY`. No key in the code means no accidental sharing [1][3].

**`max_tokens` — the required output cap**

**Tokens** are the unit Claude uses to process text — roughly three to four characters each. **`max_tokens`** is a required integer that caps how many output tokens Claude generates. Without it, the SDK raises an error before any network request is sent. `1024` is a safe default for initial testing [1].

**`client.messages.create()` — the call itself**

A **method** is a function that belongs to an object. `client.messages.create(...)` is the line that actually sends your request. It needs four things:

| Parameter | What it does |
|---|---|
| `model` | Which Claude model to use (e.g. `"claude-opus-4-5"`) |
| `max_tokens` | Output token cap — required |
| `messages` | A list of dicts, each with `"role"` and `"content"` keys |
| return value | A **response object** wrapping the full API reply |

**Reading the response — `message.content[0].text`**

The response object is not a plain string. Claude's reply lives inside it, three levels deep:

- **`.content`** — a list of content blocks
- **`[0]`** — the first (and usually only) block
- **`.text`** — the actual reply string [1][3]

## Worked Example

A complete five-cell Colab sequence from blank notebook to printed reply.

1. **Cell 1 — Install the SDK.**

   ```python
   !pip install anthropic
   ```

   Wait for `Successfully installed anthropic-...` in the output. Takes 10–20 seconds [2].

2. **Cell 2 — Set your API key.**

   ```python
   import os
   os.environ["ANTHROPIC_API_KEY"] = "sk-ant-YOUR-KEY-HERE"
   ```

   Replace the placeholder with your real key from the Anthropic console. Do not share or publish this cell.

3. **Cell 3 — Import and create the client.**

   ```python
   import anthropic
   client = anthropic.Anthropic()
   ```

   No error means the client is ready. The SDK silently read `ANTHROPIC_API_KEY` from the environment [1].

4. **Cell 4 — Write and run the call.**

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

   After one to three seconds, the output appears directly below the cell [1]:

   ```
   Machine learning is a branch of artificial intelligence where systems learn
   patterns from data to make predictions or decisions without being explicitly
   programmed for each task.
   ```

5. **Cell 5 — Inspect the response metadata (recommended).**

   ```python
   print("Stop reason:", message.stop_reason)
   print("Tokens used:", message.usage.input_tokens, "in,", message.usage.output_tokens, "out")
   ```

   `stop_reason: end_turn` confirms Claude finished naturally. `stop_reason: max_tokens` means the reply was cut short by the token cap [1].

## In Practice

- **Run the install cell every new session.** Colab environments reset when a session closes. Keep `!pip install anthropic` in Cell 1 so the package is always available when you reopen the notebook [2].
- **Create the client once, outside any loop.** Creating `anthropic.Anthropic()` inside a loop that makes many calls adds unnecessary overhead. Create it once before the loop, then call `client.messages.create(...)` inside [3].
- **Store the full response before accessing `.text`.** Chaining everything into one line — `print(client.messages.create(...).content[0].text)` — throws away the response object. Store it in a variable first so `stop_reason`, `usage`, and `id` are still available for debugging [3].
- **Check `stop_reason` when completeness matters.** If your call returns structured output, a summary, or code, verify `message.stop_reason == "end_turn"` before using the text. `"max_tokens"` means the reply was truncated [1].

## Key Takeaways

- `!pip install anthropic` installs the Anthropic SDK for the current Colab session. The `!` prefix routes the line to the shell. The install is temporary — repeat it each new session.
- `anthropic.Anthropic()` creates a client object that authenticates using the `ANTHROPIC_API_KEY` environment variable. Create it once per script, outside any loops.
- `max_tokens` is required on every `messages.create()` call. Omitting it raises an error before any request is sent. `1024` is a safe starting value.
- `client.messages.create(model=..., max_tokens=..., messages=[...])` is the single line that sends your request and returns a structured response object.
- `message.content[0].text` extracts Claude's reply as a plain Python string. Each step — `.content`, `[0]`, `.text` — navigates one level deeper into the response structure.

## References

1. Anthropic. *Getting Started with the Anthropic API* (official Colab notebook). [https://colab.research.google.com/github/anthropics/courses/blob/master/anthropic_api_fundamentals/01_getting_started.ipynb](https://colab.research.google.com/github/anthropics/courses/blob/master/anthropic_api_fundamentals/01_getting_started.ipynb)
2. Anthropic. *anthropic · PyPI* (official install page). [https://pypi.org/project/anthropic/](https://pypi.org/project/anthropic/)
3. Anthropic. *anthropic-sdk-python* (official SDK source). [https://github.com/anthropics/anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python)

---
<!-- nav:bottom:start -->
[⬅ Previous: 12.10 — The Anthropic API](../../12-10-the-anthropic-api-model-messages-array-system-prompt-user-pr/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 12.12 — Parsing the JSON response ➡](../../12-12-parsing-the-json-response-extracting-the-text-you-need/artifacts/reading.md)
<!-- nav:bottom:end -->
