<!-- nav:top:start -->
[⬅ Previous: 13.7 — The 5-role context framework](../../../2-the-5-role-context-framework/13-7-the-5-role-context-framework-authority-exemplar-constraint-r/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 13.9 — Retry logic ➡](../../13-9-retry-logic-what-to-do-when-validation-fails/artifacts/reading.md)
<!-- nav:top:end -->

---

# Output validation — checking the AI's response meets the required format

## Overview

When you send a prompt to an AI model, the model returns text. That text may or may not follow the format you asked for. **Output validation** is the step where your Python code checks the response against your format rules — after the response arrives. It is not about whether the answer is correct; it is about whether the answer has the right shape for your program to use it [1]. Without this check, a misformatted response can silently break the rest of your code.

## Key Concepts

### What output validation is

Think of ordering a form to be filled in. When it comes back, you scan it before submitting: is every required box filled? Is the date in DD/MM/YYYY, not "June 14th"? That scan is output validation.

The AI is confident — it does not warn you when it breaks your rules. It just returns text. Your job is to inspect what came back [1].

Two things to keep in mind:

- **Validation checks structure, not meaning.** You are not judging whether the recipe is good. You are checking whether the response has the right keys, types, and length.
- **Validation is automatic.** You write a Python function once. Every time a response comes back, you call it — faster and more reliable than reading every response by eye.

### The validation function

A **validation function** is a Python function that takes one input — the AI's response — and returns a pass or fail result [1][2]. The simplest version returns `True` (pass) or `False` (fail). A more useful version returns both the result and a reason:

```python
def validate_response(response):
    if <condition is not met>:
        return False, "reason the check failed"
    return True, "all checks passed"
```

The reason string is essential. "Validation failed" tells you nothing. "Missing keys: {'cooking_time'}" tells you exactly what to fix.

### Where the checklist comes from

The checklist is not something you invent. It comes directly from the **Rubric role** you wrote in your prompt (introduced in topic 13.7). Every rule in the Rubric becomes one `if` check in your validator [1][3].

**Prompt Rubric → Validation checklist → Validation function.** That is the chain [1].

Your prompt and your validator must agree. If the Rubric says "return JSON with three keys" but your validator only checks for two, you will miss errors.

### Common things to check

The most frequent checks map directly to common Rubric rules [1][3]:

**1. Is it valid JSON?**

**JSON (JavaScript Object Notation)** is a standard text format for structured data that looks like a Python dictionary. If your prompt asks for JSON and the response is plain text, no further processing will work.

```python
import json

try:
    data = json.loads(response_text)
except json.JSONDecodeError:
    return False, "response is not valid JSON"
```

**2. Does it have the required keys?**

```python
required_keys = {"dish_name", "steps", "cooking_time"}
if not required_keys.issubset(data.keys()):
    return False, "missing required keys"
```

**3. Does it match a length constraint?**

```python
if len(data["steps"]) < 2:
    return False, "steps list is too short"
```

**4. Is it the right data type?**

```python
if not isinstance(data["cooking_time"], (int, float)):
    return False, "cooking_time must be a number"
```

A **schema check** means checking structure all at once — types, required keys, and constraints together [1][3]. A **validation error** is what happens when a response fails a check — the response did not match one of your rules [1].

## Worked Example

Here is a complete validator for a recipe prompt that asks for JSON with three keys: `dish_name`, `steps`, and `cooking_time`.

**Step 1 — Read your Rubric role and list every constraint.**

Open your prompt and find the Rubric role. Write out each rule as a bullet:

- Response must be valid JSON.
- Must contain the key `dish_name` (string).
- Must contain the key `steps` (list of strings, minimum 2 items).
- Must contain the key `cooking_time` (integer, minutes).

**Step 2 — Write one `if` check per constraint.**

```python
import json

def validate_recipe_response(response_text):
    # Check 1: valid JSON
    try:
        data = json.loads(response_text)
    except json.JSONDecodeError:
        return False, "response is not valid JSON"

    # Check 2: required keys present
    required = {"dish_name", "steps", "cooking_time"}
    missing = required - data.keys()
    if missing:
        return False, f"missing keys: {missing}"

    # Check 3: steps is a list with at least 2 items
    if not isinstance(data["steps"], list) or len(data["steps"]) < 2:
        return False, "steps must be a list with at least 2 items"

    # Check 4: cooking_time is an integer
    if not isinstance(data["cooking_time"], int):
        return False, "cooking_time must be an integer"

    return True, "all checks passed"
```

**Step 3 — Call the validator after every AI response.**

Using the Anthropic SDK (already introduced in this course), get a response and immediately pass it to the validator:

```python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": your_prompt}]
)

response_text = message.content[0].text
passed, reason = validate_recipe_response(response_text)

if passed:
    data = json.loads(response_text)
    print("Valid response:", data)
else:
    print("Validation failed:", reason)
    # topic 13.9 covers what to do next (retry)
```

**Step 4 — Use the result.**

If `passed` is `True`, continue with the response. If `passed` is `False`, log the `reason` string. When validation fails, you can retry — that is covered in topic 13.9.

## In Practice

Output validation is standard in real AI systems, not just learning exercises [2][3].

- **Automated pipelines.** When an AI feeds data into a database, a validation layer sits between the model and the database. A malformed response is caught before it corrupts data or causes a crash.
- **Customer-facing tools.** If a chatbot response is supposed to populate a web form with JSON, missing keys produce a broken form. Validation catches this before the user sees an error.
- **Prompt improvement during development.** Running a validator on every test response tells you how often the model follows your format. If validation fails 20% of the time, your Rubric role needs more specificity.

Key do's and don'ts:

- **Do** test your validator with bad inputs — plain text when you expect JSON, a response with missing keys, an empty string [1].
- **Do** return a reason, not just `True` or `False`. Context makes debugging fast.
- **Do** keep the validator as its own function, separate from your prompt-building code.
- **Don't** let your Rubric and your validator fall out of sync. Add a new Rubric rule? Add the matching check [3].
- **Don't** catch errors silently and return `True` anyway. Every failed check must surface as `False` with a reason.

## Key Takeaways

- **Output validation** means checking an AI's response against your format rules after the response is returned — not before, and not during generation.
- The **validation function** returns `True` (pass) or `False` plus a reason (fail). Always include the reason.
- The **checklist comes from the Rubric role** in your prompt. Every Rubric rule becomes one check in the validator [1].
- Common checks: valid JSON, required keys present, correct data types, length constraints.
- A **validation error** means the response broke one of your rules. Knowing which rule broke is essential for debugging and for deciding whether to retry (topic 13.9).

## References

1. Machine Learning Mastery — The Complete Guide to Using Pydantic for Validating LLM Outputs. https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs/
2. Cohere LLMU — Validating LLM Outputs. https://cohere.com/llmu/validating-llm-outputs
3. Xebia — Enforce and Validate LLM Output with Pydantic. https://xebia.com/blog/enforce-and-validate-llm-output-with-pydantic/

---
<!-- nav:bottom:start -->
[⬅ Previous: 13.7 — The 5-role context framework](../../../2-the-5-role-context-framework/13-7-the-5-role-context-framework-authority-exemplar-constraint-r/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 13.9 — Retry logic ➡](../../13-9-retry-logic-what-to-do-when-validation-fails/artifacts/reading.md)
<!-- nav:bottom:end -->
