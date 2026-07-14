---
topic_id: 3.3
title: Modules, Packaging & Professional Tooling
position_in_module: 3
generated_at: 2026-07-14T00:00:00Z
resource_count: 5
---

# 1. Modules, Packaging & Professional Tooling — Topic Corpus

## 2. Prerequisites

- **3.1 Functions** — modules are, in practice, files full of the functions (and docstrings) you already know how to write; you are about to learn how to reuse them across files instead of retyping them.
- **2.2 Loops** — the worked examples below (rolling dice, timing a countdown) use `for` loops you already know to exercise the standard library.
- **1.1 The Python Environment** — this topic assumes you know that Python code runs as `.py` files through an interpreter; virtual environments and package tools are extensions of that same environment.

## 3. Learning Objectives

- Import a module three ways (`import`, `from ... import`, `import ... as`) and explain how each changes what name you use to reach the imported code.
- Use the standard library modules `random`, `math`, and `datetime` to solve small, concrete problems.
- Explain what `pip` does and how installing a third-party package differs from importing a standard-library module.
- Explain why an isolated virtual environment (`venv`) matters for a real project, and describe the create → activate → install → deactivate workflow.
- Describe, at a conceptual level, what `poetry new` scaffolds and how Poetry manages a project's dependencies.
- Write a first Pytest test function and explain how Pytest discovers and reports on it.

## 4. Introduction

Every program you have written so far has lived in a single file, and every tool you have used to write it — `def`, loops, `*args`, decorators — came built into Python itself. Real software does not stay that way for long. The moment a project grows past a page or two, you split it across files so it stays readable. The moment you need something Python does not ship with — talking to a web API, reading a spreadsheet, running a machine learning model — you reach for code someone else already wrote and published. And the moment more than one person (or more than one project) touches your machine, you need a way to keep each project's dependencies from stepping on the others.

This topic covers the four things that make that possible: **modules** (splitting and reusing code across files), the **standard library** (the toolbox that ships with Python for free), **pip and virtual environments** (installing and isolating other people's code), and two tools professional Python developers reach for constantly, **Poetry** and **Pytest** (project scaffolding and testing). None of this is exotic — it is the plumbing every real Python project sits on top of, and it is what turns "a script that runs on my machine" into "a project someone else can clone, install, and trust."

## 5. Core Concepts

### 5.1 Modules and imports

A **module** is just a `.py` file, treated as a self-contained bundle of names — functions, variables, whatever it defines — that other files can borrow from [1]. If you have a file `geometry.py` containing a function `area_of_circle`, any other file in the same project can use it by importing `geometry`.

The plain `import` statement brings in the whole module as a single name, and you reach everything inside it with dot notation:

```python
import geometry

geometry.area_of_circle(3)
```

`from ... import` pulls specific names out of a module directly into your file, so you use them without the module prefix:

```python
from geometry import area_of_circle

area_of_circle(3)
```

`import ... as` gives an imported module (or name) a different local name, most often to shorten a long module name or avoid clashing with something you already have:

```python
import geometry as geo

geo.area_of_circle(3)
```

The dot-notation requirement (`geometry.area_of_circle` rather than a bare `area_of_circle`) is called **namespacing**: every module keeps its own set of names separate from every other module's, so two different files can each define a function called `area_of_circle` without colliding [1]. `import geometry` keeps that separation intact; `from geometry import area_of_circle` deliberately breaks it by copying one name into your current file, which is convenient but means you lose the reminder of where that name came from — worth keeping in mind once a file has a dozen imports. A **package** extends the same idea to a directory: a folder containing multiple related modules (plus a special file marking it importable) that you can import as a single unit, the same way the standard library itself is organized into packages of modules [1].

### 5.2 The Python Standard Library

Python ships with a large collection of modules that are always available, with no separate installation step — this is the **standard library** [3]. Three modules from it come up constantly:

- **`random`** generates pseudo-random values: `random.random()` returns a float between 0 and 1, `random.randint(1, 6)` returns a random whole number in that inclusive range (handy for simulating a die), and `random.choice(["rock", "paper", "scissors"])` picks one item at random from a sequence [3].
- **`math`** provides mathematical functions and constants beyond the built-in operators: `math.sqrt(16)` returns `4.0`, `math.floor(3.7)` rounds down to `3`, and `math.pi` gives you the constant `3.14159...` [3].
- **`datetime`** works with dates and times: `datetime.date.today()` returns today's date, `datetime.datetime.now()` returns the current date and time, and subtracting two `datetime` objects gives you a `timedelta` representing the difference between them [3].

```python
import random
import math
from datetime import date

roll = random.randint(1, 6)
radius_area = math.pi * math.pow(3, 2)
today = date.today()
```

The point of the standard library is not that these three modules are special — it is that *hundreds* of modules like them ship with every Python install, covering everything from file paths to networking, and none of them require installing anything. Before reaching for an outside package, it is worth checking whether the standard library already solves the problem.

### 5.3 Package management with pip

The standard library is large, but it cannot cover everything — it does not ship libraries for, say, building a web server framework or talking to a specific cloud API. Code like that is published by other developers as **packages** on the **Python Package Index (PyPI)**, and **pip** is the tool that downloads and installs them into your Python environment [2]. `pip install requests`, for example, downloads the popular `requests` package and makes `import requests` work afterward — something that fails with a `ModuleNotFoundError` before installation, because `requests` is not part of the standard library.

Installed packages are typically recorded in a `requirements.txt` file (one package, often with a version, per line) so that anyone else can recreate the exact same set of installed packages with a single `pip install -r requirements.txt` [2]. This distinction matters: `import` only ever *loads* code that is already present somewhere Python can find it; `pip install` is the separate step that *puts* third-party code there in the first place.

### 5.4 Virtual environments (venv): why isolation matters

Installing a package with plain `pip install` puts it into your machine's one global Python installation — which becomes a problem the moment you have two projects that need different versions of the same package. Project A might depend on `requests` version 2.10, while Project B needs version 2.31; installing one globally breaks the other. A **virtual environment**, created with Python's built-in `venv` module, solves this by giving each project its own private, isolated copy of the Python interpreter and its own separate set of installed packages [2].

The conceptual workflow — described here rather than run live, since it depends on a real terminal — is:

1. **Create** an environment for a project: `python -m venv env` creates a folder (commonly named `env` or `.venv`) holding an isolated Python and package set.
2. **Activate** it: running the environment's activation script (`source env/bin/activate` on macOS/Linux, `env\Scripts\activate` on Windows) makes that isolated Python the one your terminal uses until you deactivate.
3. **Install** packages as normal with `pip install <package>` — they land inside `env`, not the global Python install.
4. **Deactivate** when done, returning your terminal to the system-wide Python [2].

Every serious Python project gets its own virtual environment. This is the single habit that prevents "it works on my machine" — because "my machine" and "the isolated environment for this project" are deliberately kept separate.

### 5.5 Poetry: initializing a project (concept)

**Poetry** is a project and dependency management tool that wraps the ideas in 5.3 and 5.4 into one workflow: it creates the virtual environment, tracks dependencies, and scaffolds a project's folder structure, all through one command-line tool [4]. Running `poetry new my_project` generates a starting directory structure — a package folder named `my_project`, an empty `tests` folder, and a `pyproject.toml` file that records the project's name, dependencies, and metadata in one place, replacing the separate `requirements.txt` file from plain pip [4].

From there, `poetry add <package>` installs a dependency and automatically records it (and its exact version) in `pyproject.toml`; `poetry install` reads that file and recreates the exact environment on any machine; and `poetry run <command>` runs a command inside the project's managed virtual environment without you needing to activate it by hand [4]. At the concept level this topic asks you to hold onto: Poetry does not replace `venv` and `pip` conceptually — it automates the same create-isolate-install pattern from 5.3–5.4 behind a single, project-aware tool.

### 5.6 Pytest: writing and running a first test (concept)

**Pytest** is a testing framework: a tool that runs small functions you write specifically to check that your code behaves the way you expect, and reports which ones passed or failed [5]. A Pytest test is an ordinary function whose name starts with `test_`, living in a file whose name also starts with `test_` (or ends with `_test.py`) — that naming convention is how Pytest *discovers* which functions to run without you having to list them anywhere [5]. Inside a test function, you use Python's built-in `assert` statement to state something that must be true; if it is not, the test fails and Pytest shows you exactly what was expected versus what happened.

```python
# test_geometry.py
from geometry import area_of_circle

def test_area_of_circle():
    assert area_of_circle(0) == 0
    assert round(area_of_circle(2), 2) == 12.57
```

Running `pytest` from the terminal (with no arguments) scans the current directory for files and functions matching that naming pattern, runs each one, and prints a summary — a dot for every passing test, an `F` for every failing one, followed by a detailed traceback for any failure [5]. At the concept level, the workflow to hold onto is: write a small function that asserts what correct behavior looks like, name it so Pytest can find it, and let the tool run and report instead of eyeballing output yourself.

## 6. Implementation

Setting up a new project the professional way, end to end (conceptual walkthrough):

1. Create the project scaffold: `poetry new my_project` (or manually: a folder, a `venv`, and a `requirements.txt`).
2. Activate the project's isolated environment (Poetry does this automatically when you use `poetry run`; with plain `venv` you activate it yourself).
3. Add dependencies as you need them: `poetry add requests` (or `pip install requests` inside an activated `venv`).
4. Write your code, splitting it into modules as it grows, importing between files with `import`, `from ... import`, or `import ... as`.
5. Add a `tests/test_<module>.py` file per module, with `test_`-prefixed functions asserting expected behavior.
6. Run `pytest` (or `poetry run pytest`) before every commit to confirm nothing broke.

## 7. Real-World Patterns

Splitting a growing script into modules — one file for data loading, one for calculations, one for output formatting — is the first packaging decision every real project makes, well before anyone thinks about publishing anything [1]. Once a project needs outside code, `pip install <package>` plus a committed `requirements.txt` (or Poetry's `pyproject.toml`) is how a team makes sure everyone, and every deployment server, ends up with the identical set of dependencies [2][4]. A dedicated virtual environment per project is standard practice specifically because most working developers have more than one Python project on the same machine at once, each with its own, sometimes conflicting, dependency needs [2]. And automated tests run through `pytest` — often on every push to a shared repository — are how teams catch a broken function before it reaches anyone else's machine, rather than relying on someone remembering to test by hand [5].

## 8. Best Practices

- **Prefer `import module` or `from module import specific_name`** over `from module import *` — the wildcard form pulls in every name the module defines, silently, making it hard to tell later where a given name came from.
- **Check the standard library before installing anything.** `random`, `math`, and `datetime` (and hundreds of others) are already there — no `pip install` needed.
- **Never install a third-party package into the global Python.** Create a virtual environment (or a Poetry project) per project, every time, even for a small script — the habit costs seconds and saves hours of dependency conflicts later.
- **Commit `requirements.txt` or `pyproject.toml` to your project, never the `venv`/environment folder itself.** The environment is regenerated from that file; it should never be something you hand someone else directly.
- **Name test files and functions with the `test_` convention** so Pytest's automatic discovery finds them without extra configuration, and keep each test function checking one specific behavior.

## 9. Hands-On Exercise

Write a `dice.py` module containing a function `roll(sides=6)` that returns `random.randint(1, sides)`. In a second file, `import dice` and print the result of five calls to `dice.roll()`. Then sketch (on paper, or as a comment block — no live terminal required) the four `venv` commands you would run to isolate this mini-project, and write one `test_dice.py` function using `assert` to check that `dice.roll(6)` always returns a value between `1` and `6` inclusive.

## 10. Key Takeaways

- A module is a `.py` file whose names you can reuse elsewhere via `import`, `from ... import`, or `import ... as` — each form changes how you reach the imported names, not what they do.
- The standard library (including `random`, `math`, and `datetime`) ships with Python and needs no installation; `pip` is the separate tool for installing third-party packages from PyPI.
- A virtual environment gives each project its own isolated interpreter and package set, which is what prevents one project's dependencies from breaking another's.
- Poetry automates the create-environment-and-track-dependencies workflow through `poetry new`, `poetry add`, and `pyproject.toml`, rather than replacing the underlying `venv`/pip concepts.
- A Pytest test is a `test_`-named function using `assert` to check expected behavior; naming it correctly is what lets Pytest discover and run it automatically.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
