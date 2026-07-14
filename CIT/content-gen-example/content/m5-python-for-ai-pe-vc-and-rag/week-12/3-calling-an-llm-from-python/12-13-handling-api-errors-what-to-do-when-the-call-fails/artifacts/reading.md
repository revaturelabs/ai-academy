<!-- nav:top:start -->
[⬅ Previous: 12.12 — Parsing the JSON response](../../12-12-parsing-the-json-response-extracting-the-text-you-need/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 12.14 — Every API call is a design decision ➡](../../12-14-every-api-call-is-a-design-decision-latency-cost-and-reliabi/artifacts/reading.md)
<!-- nav:top:end -->

---

# Handling API errors — what to do when the call fails

## Overview

You have already written a working `client.messages.create()` call that sends a message to Claude and gets a reply back. Most of the time that works perfectly. But API calls travel across the internet to Anthropic's servers and back — and a lot can go wrong along the way. When something does go wrong, the Anthropic SDK raises an **exception** — the same error-signalling mechanism you studied in topic 12.8 — and your script crashes unless you are ready to catch it. This reading shows you exactly which exception types the SDK raises, what each one means, how to catch them, and what to do once you have caught one.

## Key Concepts

### Why API calls can fail

Every call to `client.messages.create()` travels from your code, across the internet, to Anthropic's servers, and back. Any part of that journey can break. The four main failure categories are:

- **Network problem** — your computer cannot reach Anthropic's servers at all. Maybe your internet dropped, a firewall blocked the connection, or a DNS lookup failed. The SDK raises `APIConnectionError` [1][2].
- **Bad credentials** — your API key is missing, wrong, or has been revoked. Anthropic's servers receive your request, check your key, and reject it before doing any AI work. This is HTTP status 401 (Unauthorized). The SDK raises `AuthenticationError` [1][2].
- **Too many requests** — you are sending requests faster than your account tier allows. Anthropic's servers reply with HTTP status 429 (Too Many Requests). The SDK raises `RateLimitError` [1][2].
- **Bad request** — your request is malformed. For example, you passed a model name that does not exist, or left the `messages` list empty. This is HTTP status 400. The SDK raises `BadRequestError` [1][2]. This kind of error is a bug in your code, not a temporary network hiccup.

### The Anthropic SDK exception hierarchy

In Python, exceptions are organized as a **hierarchy** — a tree where more-general classes sit above more-specific ones. Topic 12.8 introduced this idea with built-in Python exceptions like `ValueError`. The Anthropic SDK defines its own hierarchy on top of Python's standard `Exception` class [1][2].

Here is the hierarchy, from most-general to most-specific:

```
Exception
└── AnthropicError          ← root of every Anthropic exception
    ├── APIConnectionError  ← no HTTP response received (network failure)
    └── APIError            ← HTTP response arrived, but it was an error
        ├── AuthenticationError   (HTTP 401)
        ├── RateLimitError        (HTTP 429)
        ├── BadRequestError       (HTTP 400 / 422)
        └── APIStatusError        (other non-2xx codes, e.g. 500)
```

Key points:

- **`AnthropicError`** is the base class for every exception the SDK raises. Catching it captures everything — useful as a last-resort fallback.
- **`APIError`** covers cases where Anthropic's servers replied but with an error code. All the status-specific classes inherit from it.
- **`APIConnectionError`** is separate because no HTTP response arrived at all — the connection itself failed before reaching Anthropic.
- After `import anthropic`, you refer to these classes as `anthropic.AuthenticationError`, `anthropic.RateLimitError`, and so on [2].

### Catch specific exceptions first, general ones last

Python checks `except` clauses in order, top to bottom, and stops at the first match. If you put `anthropic.AnthropicError` at the top, it matches everything and none of your specific handlers ever run. The rule is: **most-specific class first, most-general class last** [1][2].

| Exception class | HTTP status | Correct response |
|---|---|---|
| `AuthenticationError` | 401 | Fix your API key — do not retry |
| `RateLimitError` | 429 | Wait, then retry |
| `BadRequestError` | 400/422 | Fix the code — do not retry |
| `APIConnectionError` | none | Check connectivity — single retry is ok |
| `APIError` (fallback) | other non-2xx | Inspect status code; may retry for 5xx |

## Worked Example

The following function wraps a single `client.messages.create()` call and handles all four common failure types. Read through it step by step.

```python
import anthropic
import time

client = anthropic.Anthropic()

def safe_call(prompt):
    """
    Call the Anthropic API and handle common errors.
    Returns Claude's reply text, or None if the call failed.
    """
    try:
        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text

    except anthropic.AuthenticationError as e:
        # API key is wrong or missing — fix the key, do not retry.
        print(f"Authentication error: {e}")
        return None

    except anthropic.RateLimitError as e:
        # Too many requests — wait 10 seconds, then let the caller retry.
        print(f"Rate limit hit: {e}. Waiting 10 seconds...")
        time.sleep(10)
        return None

    except anthropic.BadRequestError as e:
        # Malformed request — this is a code bug, not a transient failure.
        print(f"Bad request (check your parameters): {e}")
        return None

    except anthropic.APIConnectionError as e:
        # Network problem — check your internet connection.
        print(f"Connection error: {e}")
        return None

    except anthropic.APIError as e:
        # Any other API-level error (e.g. server-side 500).
        print(f"API error (status {e.status_code}): {e}")
        return None

    except anthropic.AnthropicError as e:
        # Final fallback — any SDK error not caught above.
        print(f"Unexpected SDK error: {e}")
        return None


# Usage

<!-- nav:top:start -->
[⬅ Previous: 12.12 — Parsing the JSON response](../../12-12-parsing-the-json-response-extracting-the-text-you-need/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 12.14 — Every API call is a design decision ➡](../../12-14-every-api-call-is-a-design-decision-latency-cost-and-reliabi/artifacts/reading.md)
<!-- nav:top:end -->

---
reply = safe_call("What is machine learning in one sentence?")
if reply is not None:
    print(reply)
else:
    print("The call did not succeed. See error messages above.")
```

Walk through what happens for each failure:

1. If the API key is wrong, Python matches `AuthenticationError`, prints a message, and returns `None`. The more specific `AuthenticationError` clause fires instead of the generic `APIError` clause lower down.
2. If you hit a rate limit, `RateLimitError` is caught, the script pauses for 10 seconds with `time.sleep(10)`, and returns `None` so the caller can decide whether to try again.
3. If your request was malformed, `BadRequestError` is caught and you get a message telling you to inspect your code — retrying would just fail again.
4. If the network is down, `APIConnectionError` is caught and you are told to check connectivity.
5. Any other API-level error (such as a temporary server problem) falls through to the `APIError` clause, which prints the HTTP status code.
6. The final `AnthropicError` clause is a safety net for anything the SDK raises that none of the above caught.

### Adding a retry loop for rate limits

When a `RateLimitError` hits, the error is **transient** — it goes away on its own once a moment passes. That makes it worth retrying automatically. Here is a small helper that retries up to three times [1][2]:

```python
import anthropic
import time

client = anthropic.Anthropic()

def call_with_retry(prompt, max_retries=3, wait_seconds=10):
    for attempt in range(1, max_retries + 1):
        try:
            message = client.messages.create(
                model="claude-opus-4-5",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text

        except anthropic.RateLimitError:
            if attempt < max_retries:
                print(f"Rate limit. Waiting {wait_seconds}s (attempt {attempt}/{max_retries})...")
                time.sleep(wait_seconds)
            else:
                print("All retries exhausted.")
                raise   # re-raise so the caller knows it genuinely failed
```

How it works:

1. `range(1, max_retries + 1)` — loop up to `max_retries` times, tracking an attempt counter.
2. On success, `return` exits immediately with the text.
3. On `RateLimitError` with retries remaining, `time.sleep(wait_seconds)` pauses the script, then the loop tries again.
4. When all retries are exhausted, `raise` (with no argument) re-raises the same exception. This tells the caller that the call genuinely failed rather than silently swallowing the problem.

**Why `raise` and not just return `None`?** Silently returning `None` after all retries hides the failure. The rest of your program may then crash later with a confusing error like `NoneType has no attribute 'split'`. Re-raising makes the failure visible at the right moment.

## In Practice

- **Never retry `AuthenticationError` or `BadRequestError`.** These errors will produce the same result on every attempt — no amount of waiting will fix a wrong API key or a malformed request. Fix the code or the key first [1].
- **Keep the retry count small.** Three retries with a 10-second wait is a reasonable ceiling for beginner scripts. Hundreds of retries with no cap can exhaust your daily API quota and make a stuck script look like it is still running.
- **Order `except` clauses from most-specific to most-general.** If `AnthropicError` appears before `RateLimitError`, the rate-limit handler becomes unreachable dead code [1][2].
- **Log before returning or re-raising.** At minimum, print the attempt number and the first part of the error message. This leaves a trail in the terminal output that makes debugging much easier.
- **Do not use bare `except` or `except Exception`.** Those catch everything — including programming mistakes like `NameError` — and hide real bugs in your code [2].

## Key Takeaways

- API calls can fail for four main reasons: network problems (`APIConnectionError`), wrong credentials (`AuthenticationError`), too many requests (`RateLimitError`), and malformed requests (`BadRequestError`). Each requires a different response [1].
- The Anthropic SDK exception hierarchy flows from `AnthropicError` → `APIError` → specific classes. Catching a parent catches all its children; catching a specific class is cleaner and more intentional [1][2].
- Always list `except` clauses from most-specific to most-general — Python stops at the first match, so the general fallback must come last.
- `RateLimitError` is the only common exception worth retrying automatically. Use `time.sleep(n)` before the retry and cap the number of attempts [1][2].
- `AuthenticationError` and `BadRequestError` indicate a problem in your configuration or code — fix the cause, do not retry [1].

## References

1. Anthropic, "API errors reference." <https://docs.anthropic.com/en/api/errors>
2. Anthropic, "anthropic-sdk-python." <https://github.com/anthropics/anthropic-sdk-python>

---
<!-- nav:bottom:start -->
[⬅ Previous: 12.12 — Parsing the JSON response](../../12-12-parsing-the-json-response-extracting-the-text-you-need/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 12.14 — Every API call is a design decision ➡](../../12-14-every-api-call-is-a-design-decision-latency-cost-and-reliabi/artifacts/reading.md)
<!-- nav:bottom:end -->
