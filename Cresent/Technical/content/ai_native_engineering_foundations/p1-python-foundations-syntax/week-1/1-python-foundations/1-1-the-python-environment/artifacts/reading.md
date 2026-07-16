# The Python Environment

<sub>[Go back to TOC](../../../../../../../README.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Next: 1.2 Variables, Identifiers, Types &#8594;](../../../../../../../content/ai_native_engineering_foundations/p1-python-foundations-syntax/week-1/1-python-foundations/1-2-variables-identifiers-types/artifacts/reading.md)</sub>

---

## Overview

This is the very first topic in the program, and it assumes you have never written a line of code. That is exactly the right place to start. Before you can build anything with AI, you need a place to write instructions for the computer and a way to run them. In this program that place is **Python** (a programming language) and the tool you run it in is **Google Colab**. Think of Python as the language you speak to the computer, and Colab as the room where the conversation happens. We keep the scope small on purpose: what Python is, how it runs your code, where you will write it, and how to run your first line. By the end you will have run a real program and seen it print a message back to you. _This contributes to A1 — Python Core Skills Checkpoint (due W3)._

## Key Concepts

<strong><u>Why Python for AI work.</u></strong> A **programming language** is a set of words and rules for writing instructions a computer can follow. There are many such languages. For artificial intelligence (AI) and machine learning (ML) work, Python is the one almost everyone uses. Two reasons stand out:

- **Readable** — Python's code looks close to plain English and has low "syntax overhead," meaning you write fewer confusing symbols to get something done. That lets you focus on the idea instead of fighting the language.
- **Richest ecosystem for AI** — an *ecosystem* here means the large collection of ready-made, shareable code packages (for math, data, and training models) that other people have already built and you can reuse. Because almost every AI tool is written for Python first, choosing Python means the whole AI world works with you rather than against you.

In an AI-native workflow — one where you build and use AI systems every day — Python is the layer where you connect the pieces: loading data, calling models, and reading results. It is the glue and the workbench at the same time.

<strong><u>The interpreter and interactive mode.</u></strong> When you write Python, something has to turn your instructions into actions. That something is the **Python interpreter**: a program that reads your code and carries it out. This is worth a moment. Languages generally run in one of two ways:

- **Compiled** — translated all at once, ahead of time, into a separate file the machine runs later.
- **Interpreted** — read and executed directly, line by line, as it runs. Python is interpreted, so you do not compile it first; the interpreter just does what each line says, in order.

The practical benefit for a beginner is speed of feedback: you write a line, run it, and see the result immediately. That immediate back-and-forth has a name: **interactive mode**, also called the **REPL** (Read-Eval-Print Loop). The interpreter **R**eads what you type, **E**valuates (runs) it, **P**rints the result, and **L**oops back to wait for more. You type an instruction, you get an answer, you type the next one. Colab gives you this same read-run-see rhythm, one cell at a time.

<strong><u>Google Colab as the standard environment.</u></strong> **Google Colab** (short for Colaboratory) is a free tool from Google for writing and running Python in your web browser. It is a **hosted Jupyter notebook** environment, which means the code runs on Google's computers, not yours, and there is nothing to install or set up on your machine [1]. You open a web page and you are ready to write Python. A Colab document is called a **notebook**, and a notebook is made of **cells** — a cell is a box you type code into. You run one cell at a time, and each cell shows its output right underneath it [1]. This gives you the same read-run-see loop as the REPL, but saved and organized on a page you can return to.

<strong><u>Run order matters.</u></strong> Cells do not run by themselves and they do not have to run top to bottom — they run when you tell them to, in the order you run them [2]. Because of this, code in an earlier cell affects later cells only after you have actually run it. Running cells out of order is a common source of confusion, so a good habit is to run cells from top to bottom.

<strong><u>The runtime.</u></strong> Behind your notebook is the **runtime**: the live Python session on Google's computer that remembers everything you have run so far in this session [1][3]. Sometimes you want a clean slate — for example, if something gets into a confused state. You can **restart the runtime**, which wipes that memory and starts the Python session fresh; after a restart you must run your setup cells again [3]. (Colab runtimes can also be given extra hardware such as a GPU for heavier AI work, but you do not need that yet [1].) Your work is not lost when you close the tab: Colab **saves notebooks to Google Drive**, your Google storage, so you can reopen them later from any browser [1].

<strong><u>Running your first program.</u></strong> The `print()` function is how a program shows text to you. A **function** is a named, reusable instruction; you use it by writing its name followed by parentheses. Whatever you put inside the parentheses of `print()` gets displayed as output. Text you want printed literally goes inside quotation marks and is called a **string** — a piece of text data.

## Worked Example

Here is your first program. You type it into a cell and run it:

```python
print("Hello, world!")
```

Output:

```
Hello, world!
```

That is a complete program. When you run several cells in sequence, each one's output appears below its own cell, in the order you ran them [2]. Reading that output — checking that what appeared matches what you expected — is a core part of programming from day one.

Step by step in Colab:

1. Go to `colab.research.google.com` in your browser and sign in with a Google account.
2. Create a new notebook (File -> New notebook). It saves to your Google Drive automatically [1].
3. Click the empty code cell to place your cursor in it.
4. Type `print("Hello, world!")`.
5. Run the cell — click the run button on its left, or press Shift+Enter.
6. Read the output that appears directly below the cell.

If you ever want a fresh start, use Runtime -> Restart runtime, then run your cells again from the top [3].

## In Practice

- **Run cells top to bottom.** Because run order controls what the runtime remembers, running out of order causes confusing errors [2].
- **When in doubt, restart and rerun.** A restart clears the runtime's memory; rerunning from the top rebuilds a clean, predictable state [3].
- **Read every output.** The value under a cell is the program talking back to you. Confirm it matches what you expected before moving on.
- **Save is automatic, but check.** Colab saves to Drive, but glance at the save indicator so you know your work is stored [1].

## Key Takeaways

- Python is the standard language for AI work because it is readable and has the largest ecosystem of AI tools.
- Python is interpreted: the interpreter runs your code line by line, giving fast feedback — the same read-run-see idea as the REPL.
- Google Colab runs Python in your browser with no setup; you write code in cells, and the runtime remembers what you have run this session [1].
- Run order matters, restarting the runtime clears its memory, and notebooks save to Google Drive [1][2][3].
- `print()` displays output, and reading that output is how you confirm your program did what you meant.

Coming next: the building blocks of the language itself — storing values and doing math.

## References

1. Google Colab — Welcome / Overview. https://developers.google.com/colab
2. QuantEcon, Getting Started with Colab notebooks. https://colab.research.google.com/github/QuantEcon/lecture-py-notebooks/blob/master/getting_started.ipynb
3. Real Python — Jupyter Notebook: An Introduction. https://realpython.com/jupyter-notebook-introduction/

---

<sub>[Go back to TOC](../../../../../../../README.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Next: 1.2 Variables, Identifiers, Types &#8594;](../../../../../../../content/ai_native_engineering_foundations/p1-python-foundations-syntax/week-1/1-python-foundations/1-2-variables-identifiers-types/artifacts/reading.md)</sub>