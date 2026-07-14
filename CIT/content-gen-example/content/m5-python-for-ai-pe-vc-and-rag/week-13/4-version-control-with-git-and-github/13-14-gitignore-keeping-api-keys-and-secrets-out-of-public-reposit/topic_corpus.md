---
topic_id: "13.14"
title: ".gitignore — keeping API keys and secrets out of public repositories"
position_in_module: 5
generated_at: "2026-06-15T00:00:00Z"
resource_count: 3
---

# 1. .gitignore — keeping API keys and secrets out of public repositories — Topic Corpus

## 2. Prerequisites

This topic builds directly on 13.13 (Folder structure and README), which introduced the `.gitignore` file and the term **API key** as concepts. It also assumes the learner completed 13.12 (GitHub workflow — clone, add, commit, push), which established the git add → commit → push sequence, and 13.11 (Git fundamentals), which introduced repositories, commits, and commit history.

The current topic does NOT re-teach those mechanics. It uses them as a foundation to explain WHY `.gitignore` is a security requirement — not just a housekeeping convenience.

## 3. Learning Objectives

By the end of this topic, you should be able to:

- Explain what can happen when an API key is accidentally committed to a public GitHub repository.
- Describe the `.env` file + `.gitignore` pattern and why it keeps secrets out of version control.
- Write the correct entries in a `.gitignore` file to prevent `.env` from being tracked.
- Use `os.getenv()` in Python to load a secret from a `.env` file at runtime without hardcoding it.
- State the critical ordering rule: `.gitignore` must include `.env` before running `git add`.
- Identify the first action to take if a secret is accidentally committed (rotate the key immediately).

## 4. Introduction

In topic 13.13 you learned that a `.gitignore` file tells Git which files to ignore. You also saw that API keys should never be committed. This topic explains why that rule exists with hard consequences — and gives you the exact, practical workflow to follow so you never make that mistake.

Here is the scenario that plays out hundreds of times every day across GitHub:

A developer writes a Python script. To call an AI service they paste their API key directly into the code — something like `api_key = "sk-abc123..."`. They run `git add .`, `git commit`, `git push`. Within minutes, automated bots scan the new commit. The key is found, used to run thousands of API calls, and the developer's billing account is charged hundreds of dollars before they notice.

This is not a rare edge case. It is a common, documented incident [1]. The good news: one file — `.gitignore`, used correctly — prevents it entirely.

You already know `.gitignore` exists. This topic shows you how to use it as a security barrier, not just a file-cleanup tool.

## 5. Core Concepts

### 5.1 What a "secret" is in this context

A **secret** is any piece of information that grants access to a resource — and that should be known only to you (or your application), not to anyone reading your code.

Common secrets in Python AI projects:

| Secret type | Example (fictional) | What it unlocks |
|---|---|---|
| API key | `sk-abc123XYZ` | Calls to an AI service (billed to your account) |
| Password | `db_pass_xyz` | Access to a database |
| Token | `ghp_abc123` | GitHub Personal Access Token (account actions) |
| Connection string | `postgres://user:pass@host/db` | Direct database access |

In this course, the secret you are most likely to handle is an **API key** — the token that authenticates your requests to an LLM service like OpenAI or Anthropic. You were introduced to this term in topic 13.13. The key identifies your account. Anyone who has it can make requests that are billed to you [2].

### 5.2 Why committing a secret to GitHub is dangerous

When you run `git push`, your commit history — including every file tracked by Git — goes to GitHub. If your repository is **public** (visible to everyone on the internet), the commit is instantly readable by:

- **Human users** browsing your repository.
- **Automated scanners** — bots purpose-built to scan every new GitHub commit within seconds of it being pushed, looking for patterns that match API keys, passwords, and tokens [1].

Even a private repository carries risk: if it ever becomes public, or if your GitHub account is compromised, the secret travels with it.

**Deletion does not help.** This is the most important thing to understand. If you commit a secret and then delete the file in a later commit, the secret is still in your commit history. Anyone can view old commits using `git log` and recover the original file. Deleting from your working directory and committing the deletion does NOT remove a secret from history [1].

**The only safe assumption once a secret is committed:** treat it as fully public and compromised, even if you deleted it immediately after.

### 5.3 The consequences of an exposed API key

The consequences are concrete and fast [1][2]:

1. **Unauthorized charges.** The most common outcome for AI API keys. Bots find the key and make thousands of requests. You receive a large bill.
2. **Account suspension.** The API provider detects unusual usage and suspends your account — locking you out of the service.
3. **Data exposure.** If the key grants access to private data (a database, file storage), that data can be read or deleted.
4. **Key revocation.** The provider may revoke your key without warning, breaking your application until you generate a new one.

None of these outcomes require malicious intent from a person. Automated tools do this in minutes [1].

### 5.4 The correct prevention pattern: `.env` + `.gitignore`

The standard solution used by professional developers has two parts working together [2][3]:

**Part 1: Store the secret in a `.env` file.**

A `.env` file (the name starts with a dot; it has no file extension beyond the dot itself) is a plain text file that holds key-value pairs:

```
OPENAI_API_KEY=sk-abc123XYZ
DATABASE_URL=postgres://user:pass@host/db
```

Each line is `VARIABLE_NAME=value`. This file lives in your project folder but is **never added to Git**.

**Part 2: Add `.env` to `.gitignore`.**

You already know from topic 13.13 that `.gitignore` lists files and patterns Git should ignore. Add this line to your `.gitignore`:

```
.env
```

Once that line is in `.gitignore`, Git will not track the `.env` file. Running `git add .` will skip it. Running `git status` will not show it. It will never appear in a commit [3].

A more defensive pattern — useful when you might have multiple environment files — is:

```
.env
.env.*
*.env
```

This covers variations like `.env.local`, `.env.production`, and `secrets.env`.

### 5.5 The critical ordering rule

**`.gitignore` must include `.env` BEFORE you run `git add` for the first time.**

If you create `.env`, run `git add .` before updating `.gitignore`, and then update `.gitignore`, it is too late. Git has already started tracking `.env`. The `.gitignore` rule only prevents **untracked** files from being tracked; it does not un-track files that Git is already watching [3].

The safe sequence every time you start a project:

1. Create your project folder.
2. Run `git init` (or clone the repo).
3. Create `.gitignore` and add `.env` to it — before writing any other files.
4. Create `.env` and add your secrets.
5. Now run `git add .` — Git ignores `.env` automatically.

If you already ran `git add .` on a `.env` file by mistake, the file is staged. You must un-stage it with `git rm --cached .env` before committing. This tells Git to stop tracking it without deleting it from your disk.

### 5.6 Loading the secret in Python with `os.getenv()`

Having a `.env` file solves the storage problem. Your Python code still needs to read the secret at runtime. The correct way is to load it as an **environment variable** — a named value stored in your operating system's memory for the current session, not hardcoded in your source code [2].

**environment variable** — a key-value pair the operating system holds in memory. Programs can read these values at runtime without the values being written into source code files.

Two steps:

**Step 1: Load the `.env` file using `python-dotenv`.**

`python-dotenv` is a Python library (a reusable package of code you install) that reads your `.env` file and puts its values into the environment. Install it once:

```
pip install python-dotenv
```

Then at the top of your Python script:

```python
from dotenv import load_dotenv
load_dotenv()
```

`load_dotenv()` reads `.env` and makes each key available as an environment variable.

**Step 2: Read the value with `os.getenv()`.**

```python
import os
api_key = os.getenv("OPENAI_API_KEY")
```

`os.getenv("OPENAI_API_KEY")` returns the value of that variable from the environment — not from your source code. The key never appears in your `.py` file [2].

**Why this is safe:** your `.py` file contains no secret. It contains only the variable name `"OPENAI_API_KEY"`. Someone reading your code on GitHub sees the name, not the value.

### 5.7 The `.env.example` pattern for teams

When working with teammates, there is a related problem: how does a teammate know which environment variables the project needs, if `.env` is gitignored and never committed?

The solution is a `.env.example` file [2][3]:

```
# .env.example — copy this to .env and fill in your values
OPENAI_API_KEY=your_key_here
DATABASE_URL=your_database_url_here
```

This file contains the variable **names** and placeholder values — no real secrets. It IS committed to Git. A teammate clones the repo, copies `.env.example` to `.env`, fills in their own real values, and the project works.

The rule: `.env.example` is committed (it has no secrets). `.env` is never committed (it has real secrets).

## 6. Implementation

Setting up the secure pattern for a Python AI project, step by step:

1. Open your project folder in your terminal.
2. If the repository does not already have a `.gitignore` file, create one now — before any `git add`.
3. Open `.gitignore` and add these lines:
   ```
   .env
   .env.*
   __pycache__/
   *.pyc
   ```
4. Create a file named `.env` in your project root. Add your API key:
   ```
   OPENAI_API_KEY=your_real_key_here
   ```
5. Create a file named `.env.example`. Add placeholder lines:
   ```
   OPENAI_API_KEY=your_key_here
   ```
6. Install `python-dotenv` if not already installed:
   ```
   pip install python-dotenv
   ```
7. In your Python script, load the environment at the top:
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()
   api_key = os.getenv("OPENAI_API_KEY")
   ```
8. Run `git status` and confirm `.env` does NOT appear in the "Changes to be staged" or "Untracked files" list. If it appears, recheck step 3.
9. Add, commit, and push normally:
   ```
   git add .
   git commit -m "Add project structure with secure env loading"
   git push
   ```
10. Verify on GitHub: browse the repository files. You should see `.gitignore` and `.env.example` — but NOT `.env`.

## 7. Real-World Patterns

Professional development teams use the `.env` + `.gitignore` pattern as the baseline for all projects [2][3]. In larger organizations, additional tools extend this foundation:

- Secret scanning services such as GitGuardian run automatically on repositories and alert teams when a secret pattern is detected in a commit [1].
- GitHub Actions secrets is a built-in GitHub feature that stores secrets for automated workflows — you will encounter this in later courses.

For your current projects in this course, the `.env` + `.gitignore` + `os.getenv()` pattern is exactly what professional developers use in production Python applications. It is not a beginner shortcut — it is the standard approach [2].

## 8. Best Practices

**Do / Don't:**

| Do | Don't |
|---|---|
| Store secrets in `.env` | Paste secrets directly in `.py` files |
| Add `.env` to `.gitignore` before `git add` | Add the rule after already staging the file |
| Use `os.getenv()` to read secrets in code | Use `print()` to debug-print a secret (it may appear in logs) |
| Commit `.env.example` with placeholder values | Put real values into `.env.example` by mistake |
| Rotate a key immediately if it leaks | Assume deleting the file from the repo is enough |

**The rotation rule:** If you suspect a key has been committed and pushed — even for a moment — rotate it immediately. Rotation means: log in to the API provider's dashboard, generate a new key, update your `.env` with the new key, and revoke the old one. The old key becomes worthless even if it still exists in commit history [1].

**What if you already committed a secret?**

1. Rotate the key first — assume it is already compromised.
2. Remove the file from tracking: `git rm --cached .env`, then add, commit, and push.
3. The secret still exists in commit history. Removing it from history requires tools like `git filter-branch` or BFG Repo Cleaner — these are advanced techniques covered in later courses. Rotating the key makes the leaked value worthless even if it remains in history.

## 9. Hands-On Exercise

1. Create a new folder called `secure-test` and run `git init` inside it.
2. Create `.gitignore` with `.env` listed — before creating any other file.
3. Create `.env` with `MY_KEY=hello123`.
4. Run `git status` and confirm `.env` is not listed as an untracked file.
5. Create `app.py` that calls `load_dotenv()` and prints `os.getenv("MY_KEY")`. Run it and confirm it prints `hello123` — without `MY_KEY` ever appearing in the script as a literal value.

## 10. Key Takeaways

- An API key committed to a public GitHub repository can be stolen by automated bots within minutes, resulting in unauthorized charges or account suspension.
- Deleting a file after committing it does NOT remove the secret from commit history — the only safe response to a committed secret is to rotate (replace) the key immediately.
- The correct pattern is: store secrets in a `.env` file, list `.env` in `.gitignore`, and read values in Python using `os.getenv()` — no secret ever appears in your source code.
- `.gitignore` must include `.env` before the first `git add` — adding the rule after staging a file does not un-track it.
- The `.env.example` file (committed, with placeholder values only) tells teammates which variables they need without exposing any actual secrets.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
