<!-- nav:top:start -->
[⬅ Previous: 12.11 — Making the first API call](../../12-11-making-the-first-api-call-install-the-library-write-the-call/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 12.13 — Handling API errors ➡](../../12-13-handling-api-errors-what-to-do-when-the-call-fails/artifacts/reading.md)
<!-- nav:top:end -->

---

# Parsing the JSON response — extracting the text you need

## Overview

When you call the Anthropic API, you get back more than just a reply string. The SDK returns a structured **response object** — a container with named fields holding the reply text, the model that answered, why Claude stopped, and how many tokens the call used. Understanding that structure gives you full control: you can verify the reply is complete, track cost, and extract text safely every time.

## Key Concepts

### The response object and its fields

`client.messages.create()` returns a `Message` object. Think of it like a Python dictionary with named slots — each slot is a **field** accessible with dot notation (`message.field_name`). The full schema is documented in the Anthropic SDK API reference [1]:

| Field | Type | What it contains |
|---|---|---|
| `id` | string | A unique ID Anthropic assigned to this specific request — useful for debugging. |
| `model` | string | The Claude model version that handled the request. |
| `role` | string | Always `"assistant"` on a response. |
| `stop_reason` | string | Why Claude stopped generating (`"end_turn"` or `"max_tokens"`). |
| `usage` | object | Contains `input_tokens` and `output_tokens` — the token counts for the call. |
| `content` | list | A list of one or more **content blocks**, each packaging a piece of the reply. |

You access any field the same way you accessed `.text` in topic 12.11:

```python
print(message.id)           # 'msg_01XFDUDYJgAACzvnptvVoYEL'
print(message.model)        # 'claude-opus-4-5'
print(message.stop_reason)  # 'end_turn'
```

### The content list and content blocks

`message.content` is a Python **list** — an ordered collection you index with `[0]`, `[1]`, and so on (topic 12.4). Each item in that list is a **content block**: a small object with exactly two fields [1]:

- **`type`** — a string identifying what kind of content the block holds. For a normal text reply, this is always `"text"`.
- **`text`** — the actual reply string. This field only exists when `type == "text"`.

The nesting looks like this:

```
message
  └── content          ← a list
        └── [0]        ← content block (first and usually only item)
              ├── type = "text"
              └── text = "Machine learning is..."
```

**Why is `content` a list instead of a plain string?** The API was designed to support future use cases where a single response might contain multiple output types. For all standard text calls — which covers everything in this course — there is exactly one block at `[0]`.

### Extracting the text

For a standard single-block response, the expression from topic 12.11 is correct and concise [1]:

```python
reply_text = message.content[0].text
print(reply_text)
```

For reusable code — functions you will call from many places — a **for-loop** is safer. It works regardless of how many blocks are in the response:

```python
for block in message.content:
    if block.type == "text":
        print(block.text)
```

- `for block in message.content` visits each item in the list (topic 12.5).
- `if block.type == "text"` skips any non-text block silently (topic 12.3).
- `print(block.text)` only runs on confirmed text blocks.

For a standard response, both approaches produce the same result. The loop version just does not crash if the list is ever structured differently than expected [1].

### Detecting truncation with `stop_reason`

`stop_reason` tells you exactly why Claude stopped [1]. The two values you will see most often:

| `stop_reason` | What it means |
|---|---|
| `"end_turn"` | Claude finished its response naturally — the reply is complete. |
| `"max_tokens"` | Claude hit your `max_tokens` cap before finishing — the reply is cut short. |

If you receive `"max_tokens"`, the text in `message.content[0].text` ends mid-thought. Using a truncated reply as if it were complete can corrupt downstream logic — especially if you asked Claude to return structured data.

### Reading token counts from `message.usage`

`message.usage` has exactly two fields [1]:

- **`input_tokens`** — tokens in your request (system prompt + user message).
- **`output_tokens`** — tokens in Claude's reply.

```python
print(message.usage.input_tokens)   # e.g., 16
print(message.usage.output_tokens)  # e.g., 127
```

Anthropic charges per token. For a single test call the cost is negligible; for a system making thousands of calls a day, these counts determine the monthly bill. Token counts also help you calibrate `max_tokens`: if `stop_reason == "max_tokens"` and `output_tokens` exactly equals your cap, you need a higher limit [2].

## Worked Example

Starting from a live API call, here is a complete walkthrough of all six operations.

**Step 1 — Make the call and store the full response object.**

```python
import anthropic

client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY from environment

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain what a venture capitalist does in two sentences."}
    ]
)
```

`message` now holds the complete response object. Always store the result in a variable — chaining straight to `.content[0].text` in one expression throws away `stop_reason`, `usage`, and `id` [1].

**Step 2 — Inspect the top-level fields.**

```python
print("ID:          ", message.id)
print("Model:       ", message.model)
print("Stop reason: ", message.stop_reason)
print("Content blocks:", len(message.content))
```

Expected output:

```
ID:           msg_01AbCdEfGhIjKlMnOpQrStUv
Model:        claude-opus-4-5
Stop reason:  end_turn
Content blocks: 1
```

**Step 3 — Check `stop_reason` before using the reply.**

```python
if message.stop_reason == "max_tokens":
    print("Reply was cut short — consider raising max_tokens.")
elif message.stop_reason == "end_turn":
    print("Reply is complete.")
```

**Step 4 — Extract the text with the for-loop pattern.**

```python
for block in message.content:
    if block.type == "text":
        print(block.text)
```

Output (paraphrased):

```
A venture capitalist is an investor who provides funding to early-stage companies
in exchange for equity, aiming for high returns if those companies grow and succeed.
```

**Step 5 — Read the token counts.**

```python
print("Input tokens: ", message.usage.input_tokens)
print("Output tokens:", message.usage.output_tokens)
print("Total:        ", message.usage.input_tokens + message.usage.output_tokens)
```

Output (values will vary):

```
Input tokens:  18
Output tokens: 58
Total:         76
```

## In Practice

- **Always check `stop_reason` before processing the reply.** Code that stores, displays, or passes Claude's output to another function should verify it is complete first. A `"max_tokens"` reply used as-is will silently produce wrong results [1].

- **Store the full response object in a variable first.** Writing `client.messages.create(...).content[0].text` in one line works but loses all the other fields. Assign to `message`, then extract what you need [1].

- **Use `[0].text` in quick scripts; use the for-loop in reusable functions.** For a one-off test, `message.content[0].text` is clear and concise. For any function you will call repeatedly or share with teammates, the for-loop pattern is more robust [1].

- **Log `input_tokens` and `output_tokens` from the start.** You will not notice growing API costs until they are already significant. Two log lines per call during development builds the habit at zero cost [1].

## Key Takeaways

- The response object has multiple fields beyond the reply text — `id`, `model`, `role`, `stop_reason`, `usage`, and `content` — all accessible via dot notation [1].
- `message.content` is a list of **content blocks**. Each block has a `type` field and, when `type == "text"`, a `text` field holding the reply string.
- `message.content[0].text` is the standard extraction expression for simple calls; the for-loop pattern (`for block in message.content: if block.type == "text"`) is the safer form for reusable code.
- `message.stop_reason` tells you whether Claude finished naturally (`"end_turn"`) or was cut short by the token cap (`"max_tokens"`). Always check it before using the reply.
- `message.usage.input_tokens` and `message.usage.output_tokens` report exact token counts — the foundation of API cost tracking.

## References

1. Anthropic SDK Python — API response schema reference. https://github.com/anthropics/anthropic-sdk-python/blob/main/api.md
2. Anthropic SDK Python — SDK source. https://github.com/anthropics/anthropic-sdk-python

---
<!-- nav:bottom:start -->
[⬅ Previous: 12.11 — Making the first API call](../../12-11-making-the-first-api-call-install-the-library-write-the-call/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 12.13 — Handling API errors ➡](../../12-13-handling-api-errors-what-to-do-when-the-call-fails/artifacts/reading.md)
<!-- nav:bottom:end -->
