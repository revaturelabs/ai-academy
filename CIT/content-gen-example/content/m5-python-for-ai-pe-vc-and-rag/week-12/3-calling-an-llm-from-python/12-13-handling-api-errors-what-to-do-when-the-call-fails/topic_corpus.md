---
topic_id: "12.13"
title: "Handling API errors — what to do when the call fails"
position_in_module: 5
generated_at: "2026-06-15T00:00:00Z"
resource_count: 2
---

# 1. Handling API Errors — What to Do When the Call Fails — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **12.8** — Exception handling: reading errors without crashing (try, except, raise, the concept of an exception as an object Python raises when something goes wrong)
- **12.11** — Making the first API call: `client.messages.create()`, the response object, `message.content[0].text`, `message.stop_reason`, `message.usage`

Additional concepts used without re-definition: variables, if/else, for loops, functions, lists, dicts, file I/O, specific exception catching, API, client, server, JSON, status code, API key, Messages API, `AnthropicClient`, `max_tokens`.

---

## 3. Learning Objectives

By the end of this topic, learners will be able to:

1. **List** the four main categories of API failure (network, authentication, rate-limit, server) and describe what causes each one.
2. **Describe** the Anthropic SDK exception hierarchy — how `AnthropicError`, `APIError`, and the specific error classes relate to one another.
3. **Wrap** a `client.messages.create()` call in a `try/except` block that catches at least two specific Anthropic exception classes.
4. **Distinguish** the correct response for each exception type: fix credentials for `AuthenticationError`, wait and retry for `RateLimitError`, inspect the request for `BadRequestError`, check connectivity for `APIConnectionError`.
5. **Implement** a basic retry loop for `RateLimitError` using `time.sleep()`.
6. **Explain** why catching the most-specific exception class first leads to clearer, safer error-handling code.

---

## 4. Introduction

You have already written a working `client.messages.create()` call. Most of the time it runs, returns a response, and you extract `message.content[0].text`. But not every time. API calls travel across the internet to Anthropic's servers and back. A lot can go wrong along the way — your internet connection might drop, your API key might be wrong, you might be sending requests too fast, or Anthropic's servers might be temporarily busy. When any of those things happens, the SDK does not silently return `None`. It raises an **exception** — the same mechanism you studied in topic 12.8.

Here is a concrete scenario: you write a script that loops through fifty customer questions and sends each one to Claude. You run it. Forty-seven calls succeed. On call forty-eight, you hit a rate limit — Anthropic's servers tell your code "you have sent too many requests too quickly, please slow down." If you have no error handling, your script crashes and you lose the results of the first forty-seven calls. With error handling, the script catches the rate-limit signal, waits a few seconds, retries the same question, and keeps going.

This topic teaches you exactly what error types the Anthropic SDK raises, what each one means, how to catch them with `try/except`, and what to do once you have caught one. The patterns are short — usually five to ten lines — but they are the difference between a script that works reliably and one that fails unpredictably in production.

---

## 5. Core Concepts

### 5.1 Why API Calls Can Fail

Every call to `client.messages.create()` involves several steps: your code prepares the request, the Anthropic SDK serializes it, your operating system opens a network connection, the request travels to Anthropic's servers, the servers process it and run Claude, the response travels back, and the SDK deserializes it into a Python object. Any of those steps can fail. The four main failure categories are:

**1. Network failures**
Your computer cannot reach Anthropic's servers at all. This can happen because your internet connection dropped, a firewall blocked the connection, or a DNS lookup failed. The SDK reports these as `APIConnectionError` [1][2].

**2. Authentication failures**
Your API key is missing, wrong, or has been revoked. Anthropic's servers receive your request, inspect your credentials, and reject the request before doing any AI work. The HTTP status code in this case is 401 (Unauthorized). The SDK raises `AuthenticationError` [1][2].

**3. Rate-limit failures**
You are sending requests faster than your account tier allows. Rate limits exist to ensure fair use across all Anthropic customers. When you exceed your limit, Anthropic's servers respond with HTTP status 429 (Too Many Requests). The SDK raises `RateLimitError` [1][2].

**4. Server-side errors**
Anthropic's servers encountered an internal problem. The HTTP status code is 500 (Internal Server Error) or similar 5xx codes. These are transient — they usually resolve on their own within seconds or minutes. The SDK raises `APIStatusError` (or more specifically `InternalServerError`) [1].

**5. Bad-request errors**
Your request is malformed — for example, you passed an invalid `model` name, omitted a required field, or provided a `messages` array that violates the API's rules. The HTTP status code is 400 (Bad Request) or 422 (Unprocessable Entity). The SDK raises `BadRequestError` [1][2]. These are bugs in your code, not transient failures.

---

### 5.2 The Anthropic SDK Exception Hierarchy

In Python, exceptions are organized as a **hierarchy** — a tree where more-general exception classes sit above more-specific ones. When you use `except SomeClass`, you catch that class and every class below it in the tree. Topic 12.8 introduced this idea with built-in Python exceptions like `ValueError` and `TypeError`. The Anthropic SDK defines its own parallel hierarchy [1][2].

Here is the hierarchy, from most-general to most-specific:

```
BaseException
└── Exception
    └── AnthropicError          ← the root of all Anthropic exceptions
        └── APIError            ← any error that came back as an HTTP response
            ├── AuthenticationError   (HTTP 401)
            ├── PermissionDeniedError (HTTP 403)
            ├── NotFoundError         (HTTP 404)
            ├── RateLimitError        (HTTP 429)
            ├── BadRequestError       (HTTP 400 / 422)
            ├── InternalServerError   (HTTP 500)
            └── APIStatusError        (any other non-2xx HTTP status)
        └── APIConnectionError  ← no HTTP response was received at all
```

Key observations:

- **`AnthropicError`** is the base class for every exception the SDK raises. If you write `except anthropic.AnthropicError`, you catch everything the SDK can raise — useful as a last-resort fallback.
- **`APIError`** covers any situation where Anthropic's servers replied but the reply was an error (a non-2xx HTTP status code). All the status-code-specific classes inherit from `APIError`.
- **`APIConnectionError`** is separate from `APIError` because no HTTP response arrived at all — the connection itself failed.
- **Specific classes** let you handle each failure in the most appropriate way. Always catch the specific class you intend to handle, not the generic parent [1][2].

The SDK makes all these exception classes available directly on the `anthropic` module. After `import anthropic`, you refer to them as `anthropic.AuthenticationError`, `anthropic.RateLimitError`, and so on [2].

---

### 5.3 Catching `AuthenticationError`

`AuthenticationError` means your API key is wrong or missing. The HTTP status code is 401.

**What to do:** There is nothing to retry. The key is either correct or it is not. Fix the key, not the code.

```python
import anthropic

client = anthropic.Anthropic()

try:
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": "Hello"}]
    )
    print(message.content[0].text)

except anthropic.AuthenticationError as e:
    print("Authentication failed. Check your ANTHROPIC_API_KEY.")
    print("Details:", e)
```

When `AuthenticationError` is caught, `e` is the exception object. Printing `e` (or `str(e)`) shows the SDK's error message, which often includes the HTTP status code and a short description from Anthropic's API [1][2].

**Common causes:**

- The environment variable `ANTHROPIC_API_KEY` is not set.
- The key was typed or copied incorrectly.
- The key has been revoked in the Anthropic console.

---

### 5.4 Catching `RateLimitError` and Implementing a Simple Retry

`RateLimitError` means you sent requests too quickly. The HTTP status code is 429. Unlike `AuthenticationError`, this error is **transient** — it resolves itself once you wait a moment. That makes it the most important error class to handle with a retry loop.

**The `time` module** is a Python standard library module (no install needed) that provides time-related utilities. The function `time.sleep(n)` pauses execution for `n` seconds. This is exactly what you need between retries [1][2].

A basic retry pattern:

```python
import anthropic
import time

client = anthropic.Anthropic()

def call_with_retry(prompt, max_retries=3, wait_seconds=10):
    """Call the API, retrying on rate-limit errors."""
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
                print(f"Rate limit hit. Waiting {wait_seconds}s before retry {attempt}/{max_retries}...")
                time.sleep(wait_seconds)
            else:
                print("Rate limit hit and all retries exhausted.")
                raise   # re-raise so the caller knows it failed
```

How it works step by step:

1. `for attempt in range(1, max_retries + 1)` — loop up to `max_retries` times, keeping a counter.
2. Inside the loop, wrap the API call in `try/except anthropic.RateLimitError`.
3. If the call succeeds, `return` exits the function immediately with the text.
4. If `RateLimitError` is caught and there are retries left, `time.sleep(wait_seconds)` pauses the loop, then the loop iterates again (attempts the call again).
5. If all retries are exhausted, `raise` (with no argument) re-raises the same exception, letting the caller decide what to do next [1][2].

**Why `raise` instead of just printing?** Silently swallowing an exception that you cannot handle hides the failure from the rest of the program. Re-raising lets the caller see the problem and handle it at the right level.

---

### 5.5 Catching `BadRequestError` and `APIConnectionError`

**`BadRequestError` (HTTP 400 / 422)**

This exception means your request violated the API's rules. Examples include passing a `model` name that does not exist, providing an empty `messages` list, or including parameters that conflict with each other [1][2].

```python
except anthropic.BadRequestError as e:
    print("The request was invalid. This is a bug in the code.")
    print("Details:", e)
    # Do NOT retry. Inspect the request and fix the code.
```

`BadRequestError` is a **code bug**, not a transient network issue. Retrying the same bad request will always fail. The correct action is to inspect the `e` message, find the invalid parameter, and fix the code.

**`APIConnectionError`**

This exception means the SDK could not establish or maintain a network connection to Anthropic's servers [1][2]. Examples: your internet is down, your VPN blocked the connection, or a firewall rule rejected outbound HTTPS.

```python
except anthropic.APIConnectionError as e:
    print("Could not reach Anthropic's API. Check your internet connection.")
    print("Details:", e)
    # May retry after checking connectivity, but not in a tight loop.
```

Unlike `RateLimitError`, connection errors do not benefit from a tight retry loop — if the internet is down, retrying ten times in three seconds will not help. A single retry after a short pause is reasonable; more complex network resilience is beyond this topic.

---

## 6. Implementation

A complete `try/except` block that handles all four error categories in one place.

```python
import anthropic
import time

client = anthropic.Anthropic()

def safe_call(prompt):
    """
    Call the Anthropic API and handle the most common error types.
    Returns Claude's reply text, or None if the call could not be completed.
    """
    try:
        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text

    except anthropic.AuthenticationError as e:
        # API key is missing or wrong — fix the key, do not retry.
        print(f"Authentication error: {e}")
        return None

    except anthropic.RateLimitError as e:
        # Too many requests — wait and give the caller a chance to retry.
        print(f"Rate limit hit: {e}. Waiting 10 seconds...")
        time.sleep(10)
        return None   # caller can retry if needed

    except anthropic.BadRequestError as e:
        # Invalid request — this is a code bug, not a transient failure.
        print(f"Bad request (check your parameters): {e}")
        return None

    except anthropic.APIConnectionError as e:
        # Network problem — check connectivity.
        print(f"Connection error: {e}")
        return None

    except anthropic.APIError as e:
        # Any other API-level error (e.g. InternalServerError, PermissionDeniedError).
        print(f"API error (status {e.status_code}): {e}")
        return None

    except anthropic.AnthropicError as e:
        # Fallback: any SDK error not caught above.
        print(f"Unexpected Anthropic SDK error: {e}")
        return None


# --- Usage ---
reply = safe_call("What is machine learning in one sentence?")
if reply is not None:
    print(reply)
else:
    print("The call did not succeed. Check the error messages above.")
```

**Why list `AnthropicError` last?** Python matches `except` clauses in order, top to bottom. The most-specific class must come first. If you put `AnthropicError` first, it would match every exception from the SDK and none of the specific handlers would ever run. The rule is: **most-specific first, most-general last** [1][2].

**Why return `None` instead of raising?** This is a design choice for a beginner function. Returning `None` lets the caller check `if reply is not None` and handle the failure gracefully without a nested `try/except`. In more advanced code you would re-raise; for this topic, returning `None` keeps the logic easy to follow.

---

## 7. Real-World Patterns

**Pattern 1: Separate retry logic from business logic.**
In real applications, the retry loop lives in a helper function (like `call_with_retry` in Section 5.4), and the main business logic calls that helper without knowing about retries. This separation keeps both pieces of code easier to read and test [2].

**Pattern 2: Log the exception before returning or re-raising.**
In a script that processes many items, print at minimum the attempt number, the exception class name, and the first 80 characters of the error message before any retry. This gives you a breadcrumb trail in the terminal output that makes debugging far easier [1].

**Pattern 3: Use the exception's `status_code` attribute for fine-grained decisions.**
`APIError` (and all its subclasses) exposes a `.status_code` integer attribute. If you want to treat HTTP 429 differently from HTTP 500 without separate `except` clauses, you can catch `anthropic.APIError` and branch on `e.status_code` [1][2]:

```python
except anthropic.APIError as e:
    if e.status_code == 429:
        time.sleep(10)
    elif e.status_code >= 500:
        print("Server error — try again later.")
    else:
        raise
```

**Pattern 4: Do not catch errors you cannot handle.**
A common beginner mistake is wrapping everything in `except Exception` and printing "something went wrong." This hides bugs. Catch only the exceptions you know how to respond to; let the rest propagate so the program fails visibly and you can fix the real problem [2].

---

## 8. Best Practices

- **Always catch specific exception classes, not bare `except` or `except Exception`.** `except anthropic.RateLimitError` is clear about intent; `except Exception` catches everything including programming errors like `NameError` and hides bugs [2].

- **Order `except` clauses from most-specific to most-general.** Python stops at the first matching clause. If `AnthropicError` comes before `RateLimitError`, the rate-limit handler is unreachable dead code [1][2].

- **`AuthenticationError` should never be retried.** If the key is wrong, every retry will produce the same 401 response and cost you nothing except wasted time. Fix the key [1].

- **Use `time.sleep()` before a rate-limit retry, not after.** Sleeping after the failure, before the next attempt, gives Anthropic's servers time to replenish your quota. Sleeping after the next attempt (if it succeeds) wastes time unnecessarily [1][2].

- **Keep the retry count small.** Three retries with a 10-second wait is a reasonable ceiling for beginner scripts. Dozens of retries with no ceiling can make a misbehaving script look "stuck" and can exhaust your daily API quota [1].

- **Re-raise when you are out of retries.** Silently returning `None` after all retries are exhausted can cause confusing downstream failures (e.g., `NoneType has no attribute 'split'`). At minimum, print a clear message and consider re-raising so the caller knows the call genuinely failed [2].

---

## 9. Hands-On Exercise

**Exercise: Add error handling to your API script from topic 12.11**

1. Open the Colab notebook you built in topic 12.11 that calls `client.messages.create()`.
2. Wrap the existing call in a `try/except` block that catches `anthropic.AuthenticationError`, `anthropic.RateLimitError`, and `anthropic.APIConnectionError` separately.
3. For `AuthenticationError`: print "Check your API key" and return `None`.
4. For `RateLimitError`: print "Rate limited — waiting 5 seconds…", call `time.sleep(5)`, and return `None`.
5. For `APIConnectionError`: print "No connection to Anthropic servers" and return `None`.
6. **Test `AuthenticationError`**: temporarily change your API key to `"bad-key"`, run the call, confirm you see your custom message. Then restore the real key.
7. **Test the successful path** again to confirm the error handling did not break the normal flow.

Expected outcome: the wrong-key test prints your authentication message and does not crash; the correct-key test prints Claude's reply as before.

---

## 10. Key Takeaways

- API calls can fail for four main reasons: network problems (`APIConnectionError`), bad credentials (`AuthenticationError`), too-many-requests (`RateLimitError`), and server errors (`APIStatusError` / `InternalServerError`). Each requires a different response [1].
- The Anthropic SDK exception hierarchy flows from `AnthropicError` → `APIError` → specific classes. Catching a parent class catches all its children; catching a specific class is cleaner and more intentional [1][2].
- Wrap `client.messages.create()` in `try/except` and list the most-specific exception class first. Always place the most-general fallback (`AnthropicError` or `APIError`) last [1][2].
- `RateLimitError` is the only common exception worth retrying automatically. Use `time.sleep(n)` before the retry and cap the number of attempts [1][2].
- `AuthenticationError` and `BadRequestError` indicate problems in your configuration or code — fix the cause, do not retry [1].

---

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
