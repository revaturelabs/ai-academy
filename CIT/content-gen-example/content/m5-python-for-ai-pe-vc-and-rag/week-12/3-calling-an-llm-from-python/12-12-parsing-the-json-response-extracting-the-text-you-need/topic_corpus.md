---
topic_id: "12.12"
title: "Parsing the JSON response — extracting the text you need"
position_in_module: 4
generated_at: "2026-06-15T00:00:00Z"
resource_count: 2
---

# 1. Parsing the JSON Response — Extracting the Text You Need — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **12.11** — Making the first API call: install the library, write the call, run in Colab (concepts: `!pip install anthropic`, `import anthropic`, `anthropic.Anthropic()`, client object, `max_tokens`, `client.messages.create()`, response object, `message.content[0].text`, content block)

All Python foundations from earlier topics (variables, data types, if/else, for loops, functions, lists with indexing, dictionaries, try/except) are assumed and used without re-definition.

---

## 3. Learning Objectives

By the end of this topic, learners will be able to:

- **Identify** the top-level fields of the Anthropic API response object (`id`, `model`, `role`, `stop_reason`, `usage`, `content`) and describe what each field contains
- **Explain** why `message.content` is a list and what each item in that list (a content block) contains
- **Extract** Claude's reply text using `message.content[0].text` for a standard single-block response
- **Write** a for-loop that safely iterates over all content blocks and collects only those with `type == "text"`
- **Use** `message.stop_reason` to detect whether Claude's reply was truncated before completion
- **Read** `message.usage.input_tokens` and `message.usage.output_tokens` to see how many tokens a call consumed

---

## 4. Introduction

In topic 12.11 you made your first live API call and used `message.content[0].text` to read Claude's reply. That single expression worked perfectly — but it felt a little like magic. You reached into an object, navigated two levels deep, and pulled out a string. What is the rest of the object? Why is `.content` a list? What happens if you need something other than the text — like how many tokens the call used, or whether Claude finished its answer?

The response object that `client.messages.create()` returns is not just a string. It is a structured data container — similar to a Python dictionary — that Anthropic's API always returns in the same shape. Understanding that shape gives you full control: you can verify the call completed normally, log how much it cost in tokens, and handle edge cases where the response contains more than one content block.

This topic is a guided walkthrough of every meaningful field in that response object. You will learn what each field is, when you need it, and how to access it safely. By the end, `message.content[0].text` will not feel like magic — it will feel like a deliberate navigation through a structure you understand completely.

---

## 5. Core Concepts

### 5.1 The Full Response Object — All Top-Level Fields

When `client.messages.create(...)` returns, the SDK gives you a `Message` object. If you print it, you see something like this [1]:

```
Message(
  id='msg_01XFDUDYJgAACzvnptvVoYEL',
  content=[ContentBlock(text='...', type='text')],
  model='claude-opus-4-5',
  role='assistant',
  stop_reason='end_turn',
  stop_sequence=None,
  type='message',
  usage=Usage(input_tokens=16, output_tokens=127)
)
```

Each part of this printout is a **field** — a named piece of data attached to the object. Here is what every field means:

| Field | Type | What it contains |
|---|---|---|
| `id` | string | A unique identifier Anthropic assigned to this specific request. Useful when you need to reference or debug a particular call. |
| `model` | string | The name of the Claude model that actually handled the request — confirms which version was used. |
| `role` | string | Always `"assistant"` on a response. Mirrors the `role` field from the `messages` array you learned in 12.10, but now from Claude's side. |
| `stop_reason` | string | Why Claude stopped generating. The two most common values are `"end_turn"` (Claude finished naturally) and `"max_tokens"` (Claude hit your `max_tokens` cap before finishing). |
| `stop_sequence` | string or None | If you passed a list of stop sequences in your call, this field shows which one triggered the stop. For most beginner calls it is `None`. |
| `type` | string | Always `"message"` for a standard response. Part of Anthropic's API versioning design. |
| `usage` | object | Contains `input_tokens` and `output_tokens` — the exact token counts for this call. |
| `content` | list | A list of one or more content blocks, each containing a piece of the reply. Covered in detail in Section 5.2. |

You access any field using dot notation, the same way you accessed `.text` in 12.11 [1]:

```python
print(message.id)           # 'msg_01XFDUDYJgAACzvnptvVoYEL'
print(message.model)        # 'claude-opus-4-5'
print(message.role)         # 'assistant'
print(message.stop_reason)  # 'end_turn'
```

### 5.2 The Content List — What It Is, Why It Is a List, What Each Block Contains

`message.content` is a Python **list**. A list, as you learned in topic 12.4, is an ordered collection of items accessed by index (`[0]`, `[1]`, etc.). In the response object, each item in that list is a **content block** — a small object that packages one piece of Claude's output [1].

**Why a list instead of a single string?**

The Anthropic API was designed to support advanced use cases where a single response can contain multiple types of output — for example, a text explanation followed by a tool result. For a standard text call (which is all you need at this level), there will almost always be exactly one content block at index `[0]`. The list structure is there for completeness and future compatibility [1].

Each content block has two fields [1]:

- **`type`** — a string that identifies what kind of content this block holds. For a normal text reply, `type` is always `"text"`.
- **`text`** — the actual string of Claude's reply. This field only exists when `type == "text"`.

You can visualize the nesting like this:

```
message
  └── content          ← a list
        └── [0]        ← content block (first and usually only item)
              ├── type = "text"
              └── text = "Machine learning is..."
```

Accessing the text follows that path exactly: `message.content[0].text` [1].

### 5.3 Extracting Text: `message.content[0].text` for Standard Calls

For the vast majority of beginner calls — one user message, one text reply — there is exactly one content block and it is at index `[0]`. The expression you already know is [1]:

```python
reply_text = message.content[0].text
print(reply_text)
```

This is the standard pattern. It is short, readable, and correct for all simple use cases.

However, it assumes two things:
1. There is at least one content block (the list is not empty).
2. The block at index `[0]` has `type == "text"`.

Both assumptions hold for all standard text calls to Claude. For the exercises and lab work in this course, you can use this expression without concern. Section 5.4 shows the safer pattern for when you want to be certain.

### 5.4 Safely Handling the Content List When You Are Not Sure How Many Blocks There Are

Instead of assuming index `[0]` holds the text, you can iterate over every content block and collect only those with `type == "text"`. This approach works regardless of how many blocks are in the response [1]:

```python
for block in message.content:
    if block.type == "text":
        print(block.text)
```

Breaking it down:

- **`for block in message.content`** — a standard Python for-loop (topic 12.5) that visits each item in the `content` list one at a time, naming each item `block`.
- **`if block.type == "text"`** — a condition check (topic 12.3) that skips any block that is not a text block. This makes the code safe: if a non-text block ever appears, it is silently ignored rather than causing an error.
- **`print(block.text)`** — accesses the text field only on confirmed text blocks.

For a single-block response, this loop runs exactly once and prints the same result as `message.content[0].text`. The difference is robustness: the loop version will not crash if the list is structured differently than you expect [1].

You can also collect all text blocks into a single string:

```python
full_text = ""
for block in message.content:
    if block.type == "text":
        full_text += block.text

print(full_text)
```

This pattern becomes the foundation for any code that needs to process Claude's reply programmatically (search it, summarize it, store it).

### 5.5 Using `stop_reason` to Detect a Truncated Reply

The `stop_reason` field tells you exactly why Claude stopped generating output [1]. There are two values you will see most often:

| `stop_reason` value | What it means |
|---|---|
| `"end_turn"` | Claude finished its response naturally. The reply is complete. |
| `"max_tokens"` | Claude hit the `max_tokens` limit before finishing. The reply is cut short. |

If you receive `"max_tokens"`, the text in `message.content[0].text` ends mid-thought. Using that text as if it were complete can lead to wrong answers, garbled output, or broken JSON if you asked Claude to return structured data.

Checking `stop_reason` before using the reply is a simple one-line guard [1]:

```python
if message.stop_reason == "max_tokens":
    print("Warning: reply was cut short. Increase max_tokens.")
else:
    print(message.content[0].text)
```

In production code this guard is often more elaborate (retry with a higher limit, alert the user, log the truncation). For this course, knowing how to detect truncation is the goal.

**When does truncation happen in practice?**

When your `max_tokens` setting is too low for the question you asked. If you ask Claude to write a 500-word essay but set `max_tokens=100`, you will always get a truncated reply. The fix is straightforward: raise `max_tokens`. The token-count fields in `message.usage` (Section 5.6) help you calibrate this.

### 5.6 Reading Token Counts from `message.usage`

`message.usage` is a small object with exactly two fields [1]:

- **`input_tokens`** — the number of tokens in the request you sent (your system prompt, if any, plus the user message).
- **`output_tokens`** — the number of tokens in Claude's reply.

You access them with two more levels of dot notation:

```python
print(message.usage.input_tokens)   # e.g., 16
print(message.usage.output_tokens)  # e.g., 127
```

**Why do token counts matter?**

Anthropic charges per token — a small fraction of a cent per thousand tokens (the exact pricing is on Anthropic's website). For a single test call the cost is negligible. For a system that makes thousands of calls per day, token counts determine the monthly bill. Logging `input_tokens` and `output_tokens` for every call is the standard starting point for cost tracking.

Token counts also help you calibrate `max_tokens`. If you consistently see `output_tokens` close to your `max_tokens` limit and `stop_reason == "end_turn"` (meaning Claude *did* finish naturally despite being close to the cap), your limit is fine. If you see `stop_reason == "max_tokens"` and `output_tokens` equals your limit exactly, you need a higher cap.

A quick calculation:

```python
total_tokens = message.usage.input_tokens + message.usage.output_tokens
print(f"This call used {total_tokens} tokens total.")
```

---

## 6. Implementation

A step-by-step walkthrough: starting from a live response object, printing the text, checking `stop_reason`, and reading token counts.

**Step 1 — Make a call and store the full response (review from 12.11).**

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

`message` now holds the complete response object [1].

**Step 2 — Inspect all top-level fields.**

```python
print("ID:          ", message.id)
print("Model:       ", message.model)
print("Role:        ", message.role)
print("Stop reason: ", message.stop_reason)
print("Content blocks:", len(message.content))
```

Expected output:

```
ID:           msg_01AbCdEfGhIjKlMnOpQrStUv
Model:        claude-opus-4-5
Role:         assistant
Stop reason:  end_turn
Content blocks: 1
```

All five lines confirm the response is normal: one model handled it, Claude's role is `"assistant"`, it stopped naturally, and there is exactly one content block [1].

**Step 3 — Extract the text using the standard expression.**

```python
reply_text = message.content[0].text
print(reply_text)
```

Output (paraphrased):

```
A venture capitalist is an investor who provides funding to early-stage companies
in exchange for equity, aiming for high returns if those companies grow and succeed.
They also typically offer strategic guidance and industry connections to the
businesses they invest in.
```

**Step 4 — Extract the text safely using the for-loop pattern.**

```python
for block in message.content:
    if block.type == "text":
        print(block.text)
```

For this response, the output is identical to Step 3. The loop ran once, found one `"text"` block, and printed it [1].

**Step 5 — Check `stop_reason` before trusting the reply.**

```python
if message.stop_reason == "max_tokens":
    print("Reply was cut short — consider raising max_tokens.")
elif message.stop_reason == "end_turn":
    print("Reply is complete.")
    print(message.content[0].text)
```

Output:

```
Reply is complete.
A venture capitalist is an investor who provides funding...
```

**Step 6 — Read and display token counts.**

```python
print("Input tokens: ", message.usage.input_tokens)
print("Output tokens:", message.usage.output_tokens)
print("Total tokens: ", message.usage.input_tokens + message.usage.output_tokens)
```

Output (values will vary):

```
Input tokens:  18
Output tokens: 58
Total tokens:  76
```

These are the six operations that cover everything in this topic. Every more complex pattern in Section 7 is a combination of these steps [1].

---

## 7. Real-World Patterns

**Pattern 1: Check `stop_reason` before using the reply.**

Any code that does something meaningful with Claude's output — stores it in a database, passes it to another function, displays it to a user — should verify the reply is complete first [1]:

```python
message = client.messages.create(...)

if message.stop_reason != "end_turn":
    # Log the truncation, raise max_tokens, or alert the user
    raise ValueError(f"Incomplete response: stop_reason={message.stop_reason}")

reply = message.content[0].text
# Continue processing with `reply`
```

This is a lightweight guard that catches the most common failure mode before it silently corrupts downstream logic.

**Pattern 2: Log token counts for cost tracking.**

In any system that makes repeated API calls, logging token usage per call accumulates into a cost ledger. A simple version writes each call's counts to a list [1][2]:

```python
call_log = []

message = client.messages.create(...)

call_log.append({
    "id": message.id,
    "input_tokens": message.usage.input_tokens,
    "output_tokens": message.usage.output_tokens
})
```

After many calls, summing `output_tokens` across `call_log` tells you how many tokens you have consumed in a session. This feeds directly into estimating API costs.

**Pattern 3: Iterate content blocks to handle multi-block responses safely.**

Code that will be used across many different queries — like a reusable function that wraps `client.messages.create()` — should collect text from all blocks rather than assuming only one [1]:

```python
def get_reply_text(message):
    """Extract all text content from a response object."""
    parts = []
    for block in message.content:
        if block.type == "text":
            parts.append(block.text)
    return "\n".join(parts)

reply = get_reply_text(message)
print(reply)
```

This function works correctly whether `message.content` has one block or several. Wrapping this logic in a function also means you write it once and call it everywhere — a direct application of the function-reuse principle from topic 12.1.

---

## 8. Best Practices

- **Always check `stop_reason` before processing Claude's reply.** If the reply was truncated (`"max_tokens"`), using it as if it were complete will produce wrong results. A one-line check at the top of your processing code is cheap insurance [1].

- **Store the full response object before accessing any field.** Chaining `client.messages.create(...).content[0].text` in one expression works, but throws away the response object. You lose `stop_reason`, `usage`, and `id`. Always store the result in a variable first [1].

- **Use the for-loop pattern in reusable code; use `[0].text` in quick scripts.** For a one-off test or a learning exercise, `message.content[0].text` is clear and concise. For functions you will reuse or share, the for-loop pattern is more robust [1].

- **Log `input_tokens` and `output_tokens` from the start.** You will not know when your usage starts to matter financially until you are already over-spending. Adding two `print` or `log` lines after every API call in development costs nothing and builds the habit [1].

---

## 9. Hands-On Exercise

**Exercise: Inspect and parse a domain-relevant response**

This exercise extends the lab scenario from 12.11 (domain system connected to the Anthropic API).

1. Open your Colab notebook from 12.11 (or start a new one and re-run the setup cells).
2. Write a `client.messages.create()` call with a domain-relevant user message (e.g., a question about startup funding, healthcare triage, or whatever domain your lab uses). Set `max_tokens=512`.
3. After the call, print each top-level field: `message.id`, `message.model`, `message.role`, `message.stop_reason`.
4. Print `len(message.content)` — confirm there is exactly one content block.
5. Extract the text using the for-loop pattern (not `[0].text`) and print it.
6. Print `message.usage.input_tokens` and `message.usage.output_tokens`.
7. Repeat the call with `max_tokens=10` (deliberately too small). Check `message.stop_reason`. What do you see in `message.content[0].text`?

Expected outcome: For step 2–6, `stop_reason` is `"end_turn"` and the full reply is visible. For step 7, `stop_reason` is `"max_tokens"` and the text is cut mid-sentence.

---

## 10. Key Takeaways

- The response object from `client.messages.create()` contains multiple fields beyond the reply text: `id`, `model`, `role`, `stop_reason`, `usage`, and `content`. Each is accessible via dot notation [1].
- `message.content` is a list of content blocks. For standard text calls there is exactly one block at index `[0]`, which has a `type` field (`"text"`) and a `text` field holding the reply string [1].
- `message.content[0].text` is the standard expression for extracting the reply from a single-block response. The for-loop pattern (`for block in message.content: if block.type == "text"`) is the safer alternative for reusable code [1].
- `message.stop_reason` tells you whether Claude finished naturally (`"end_turn"`) or was cut short by the token cap (`"max_tokens"`). Always check this field before processing or displaying the reply [1].
- `message.usage.input_tokens` and `message.usage.output_tokens` report the exact token counts for the call. Logging these counts is the foundation of API cost tracking [1].

---

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
