---
topic_id: "11.2"
title: "Setting up Google Colab — no installation, runs in the browser"
position_in_module: 2
generated_at: "2026-06-12T00:00:00Z"
resource_count: 5
---

# 1. Setting up Google Colab — no installation, runs in the browser — Topic Corpus

## 2. Prerequisites

This topic builds directly on **11.1 — Python's role: the orchestration layer**. Topic 11.1 named Google Colab as the browser-based environment for this course and explained Python as an interpreted language that runs line by line. That vocabulary (interpreted, REPL, syntax error, runtime error) is used freely here without re-introduction.

---

## 3. Learning Objectives

By the end of this topic, learners will be able to:

- Identify the main parts of the Google Colab interface: the notebook, code cells, text cells, the toolbar, and the runtime status indicator.
- Open a new Colab notebook and add both a code cell and a text cell.
- Run a code cell using the run button (play) and the keyboard shortcut Shift+Enter, and describe what happens in the output area.
- Explain what a "runtime" and a "session" mean in Colab, including what is lost when a session resets.
- Save a notebook to Google Drive and download it as a `.ipynb` file.
- Use at least two keyboard shortcuts (Shift+Enter, Ctrl+M B) to work more efficiently in Colab.

---

## 4. Introduction

In topic 11.1 you learned that Python is the language you will use throughout this course. You also heard that the place you will write and run that Python is called **Google Colab** [1]. But knowing *what* Colab is and knowing *how to actually open it and get something running* are two different things.

Think of it this way: knowing that a car exists does not mean you can drive it. This topic is about sitting in the driver's seat for the first time — turning the key, understanding the dashboard, and taking your first short trip.

The good news is that Colab removes almost every barrier that has historically made programming feel intimidating. There is nothing to download. There is nothing to install. There is no error message telling you that the version is wrong or that a library is missing. You open a browser tab, sign in with a Google account, and you are ready to write and run code — from any computer, anywhere [1][2].

That simplicity matters for this course in a very practical way: your Assessment 4 Portfolio (due week 13, worth 20%) consists of Colab notebooks. Every lab you complete, every piece of code you write and test, lives in Colab. Getting comfortable in this environment now is not optional — it is the foundation everything else is built on.

By the end of this topic you will know how to open Colab, navigate its interface, run your first cell, and make sure your work is saved.

---

## 5. Core Concepts

### 5.1 What Google Colab is — and why no installation is needed

**Google Colab** (short for "Google Colaboratory") is a free, cloud-based service provided by Google that lets you write and run Python code entirely inside a web browser [1]. You visit colab.research.google.com, and a full programming environment appears — no software to install on your computer.

The reason no installation is required is that the code does not actually run on your laptop or desktop. Instead, when you press the run button, your code is sent over the internet to a computer operated by Google (called a **server**). That remote computer executes the code and sends the result back to your browser as output. Your browser displays the output. The whole exchange happens in a fraction of a second [3].

This is different from installing Python locally, where the code would run directly on your machine. In Colab, your machine is just displaying the interface; the actual computing happens elsewhere. This is why Colab works on a cheap Chromebook just as well as on a high-end laptop — the hardware doing the work is Google's, not yours.

The only requirement on your side is a **Google account** (a Gmail address gives you one) and a modern web browser such as Chrome, Firefox, or Edge [1].

### 5.2 The Notebook: the fundamental unit of work

Everything in Colab is organised inside a **notebook**. A notebook is a single file that holds a mixture of code, output, and explanatory writing — all in one place [2].

Notebooks were originally invented for scientific computing because researchers wanted to show their reasoning alongside their results. The same idea applies here: instead of having code in one file and notes somewhere else, a Colab notebook lets you put a calculation, an explanation of what it means, and the result all together. This is precisely why notebooks are used for the portfolio in this course: the notebook *is* the record of your thinking.

A notebook file is stored with the extension `.ipynb`. The "ipynb" stands for **IPython Notebook**, which is the historical name for this file format — but you do not need to remember that detail. What matters is recognising `.ipynb` as the file type you will be working with [5].

### 5.3 Code cells and text cells

Inside every notebook there are two types of building block, called **cells** [3].

**Code cells** are where you type Python code. When you run a code cell, the code inside it is sent to Google's server, executed, and the result appears directly below the cell in a region called the **output area**. The output area can show text, numbers, tables, images, or error messages.

**Text cells** (sometimes called Markdown cells) are where you write plain English — descriptions, headings, instructions, reflections. Text cells do not run Python. They exist purely for writing. The word "Markdown" refers to a simple set of formatting rules: surrounding a word with double asterisks makes it bold, and a hash symbol at the start of a line makes a heading. You do not need to memorise Markdown rules right now; you can write plain text in a text cell and it will display just fine [2].

A practical way to think about the difference: code cells are where you *tell the computer what to do*; text cells are where you *tell the reader what is happening and why*. In your portfolio, assessors will read both.

**Adding a new cell:** In the Colab toolbar, hover near the bottom of any existing cell and two buttons appear: "+ Code" and "+ Text". Click either to insert a new cell of that type immediately below. The keyboard shortcut for inserting a code cell below the current one is **Ctrl+M B** (on Mac: Cmd+M B) [2].

### 5.4 Running a code cell

To run a code cell you have two options [2][3]:

1. **Click the play button** on the left edge of the cell.
2. **Press Shift+Enter** on your keyboard. This runs the current cell and moves the cursor to the next cell.

When you run a cell:
- A spinning circle replaces the play button while the code is executing.
- The square brackets to the left of the cell fill in with a number — for example, `[1]`. This number is the **execution count**. The first cell you run in a session gets `[1]`, the next gets `[2]`, and so on. This counter tells you the *order* in which cells were run, which matters because cells can affect each other (a value assigned in cell 1 is available in cell 2).
- The output appears in the output area directly below the cell.

A very common beginner mistake is to assume that because code appears above another cell, it has already run. **Only cells you have explicitly run are in effect.** If you write a line of code in cell 1 but never press the play button or Shift+Enter, that code has no effect on cell 2, even though cell 1 is physically above it in the notebook.

If the code has an error, the output area will show an error message in red instead of a result. This is normal — it is Colab's way of telling you what went wrong. You saw the vocabulary for this in topic 11.1: a **syntax error** means the code is written incorrectly (like a typo), and a **runtime error** means the code was written correctly but something went wrong while it was running.

### 5.5 The runtime and the session

The word **runtime** in Colab refers to the remote Google computer that is currently assigned to your notebook and executing your code [3][4]. Think of the runtime as a temporary workspace that Google sets up for you.

A **session** is the period of time during which your runtime is active and connected to your notebook. A session begins when you first run a cell (or when you click "Connect" in the top-right corner of the Colab interface). A session ends when:

- You close the browser tab and do not return for a long time (Colab disconnects idle runtimes after roughly 90 minutes of inactivity) [4].
- You explicitly choose "Runtime -> Disconnect and delete runtime" from the menu.
- You restart the runtime (via "Runtime -> Restart runtime").

**What is lost when a session ends:** Any output you computed by running code, any file you uploaded temporarily — all of that exists in the runtime's memory and is gone when the session resets. **The notebook itself — the cells and the code you typed — is saved separately and is not lost.** This distinction trips up many beginners: your *code* survives; the *results of running that code* do not persist across sessions. The next time you open the notebook you will need to re-run the cells to rebuild those results.

This is why the execution count resets to `[1]` each time you reconnect: the runtime is a fresh slate.

**Restarting the runtime** is sometimes useful: if your notebook gets into a confused state (because you ran cells out of order and outputs are not what you expected), "Runtime -> Restart and run all" wipes the slate and runs every cell from the top in order.

**Free tier limits:** On the free tier, Colab provides up to 12 hours of continuous runtime per session, but Google may reclaim the runtime sooner if demand is high. For the lab exercises in this course, that limit will never be a practical constraint [4].

### 5.6 Saving your work: Google Drive and downloading notebooks

Because Colab is cloud-based, your notebooks are saved to **Google Drive** — Google's cloud storage service [5]. When you create a new notebook in Colab, it is automatically created inside a folder called "Colab Notebooks" in the Google Drive associated with your Google account.

**Autosave:** Colab saves your notebook automatically as you work, typically every few minutes. You can also trigger a manual save with **Ctrl+S** (or Cmd+S on Mac). A small "All changes saved" message appears near the top of the screen to confirm [2].

**Accessing your notebooks later:** Go to colab.research.google.com and you will see a list of your recent notebooks. You can also find them at drive.google.com inside the "Colab Notebooks" folder.

**Downloading a notebook:** For submission purposes (including portfolio work for Assessment 4), you may need to download the notebook as a file. Go to **File -> Download -> Download .ipynb**. This saves the notebook to your computer as a `.ipynb` file, which preserves both the code cells and the text cells exactly as they appeared in Colab [5].

You can also download a notebook as a `.py` file (pure Python script), but for this course the `.ipynb` format is what you will submit — it keeps the text cell explanations alongside the code, which is part of what assessors read.

### 5.7 The Colab interface: a quick map

When you open a Colab notebook, the screen is divided into a few key areas [2][3]:

| Area | Where it is | What it does |
|---|---|---|
| **Menu bar** | Very top of the page | File, Edit, View, Insert, Runtime, Tools menus |
| **Toolbar** | Below the menu bar | Quick-access buttons: + Code, + Text, and others |
| **Cell area** | Centre of the page | The cells themselves, in order from top to bottom |
| **Output area** | Below each code cell | Where results appear after you run the cell |
| **Runtime status** | Top-right corner | Shows whether you are connected (green dot) or disconnected (grey dot) |

The **runtime status indicator** in the top-right corner is the first thing to check when you open a notebook. If it shows "Disconnected", click the "Connect" button to allocate a runtime before you start running cells.

### 5.8 Keyboard shortcuts worth learning immediately

Using keyboard shortcuts makes working in Colab noticeably faster. Two shortcuts that pay off from day one [2]:

| Shortcut | What it does |
|---|---|
| **Shift+Enter** | Run the current cell and move to the next cell |
| **Ctrl+M B** (Cmd+M B on Mac) | Insert a new code cell below the current one |

A few more shortcuts you will discover quickly (no need to memorise them now):

| Shortcut | What it does |
|---|---|
| Ctrl+S | Save the notebook |
| Ctrl+M A | Insert a code cell above the current one |
| Ctrl+M Y | Convert the current cell to a code cell |
| Ctrl+M M | Convert the current cell to a text cell |

All available shortcuts are listed under **Tools -> Keyboard shortcuts** inside Colab [2].

---

## 6. Implementation

The following is a step-by-step walkthrough for opening your first notebook and running your first cell. This is the procedure you will repeat at the start of every lab.

**Step 1 — Open Colab.**
Navigate to colab.research.google.com in your browser [1]. If you are not signed in to a Google account, sign in now. You will see a dialog showing recent notebooks or the option to create a new one.

**Step 2 — Create a new notebook.**
Click "+ New notebook" (or go to File -> New notebook). A blank notebook opens with one empty code cell already in place.

**Step 3 — Check the runtime status.**
Look at the top-right corner. If it shows "Disconnected", click "Connect". Wait for a green dot or RAM/Disk usage bar to appear — this means a runtime is active and ready.

**Step 4 — Type something in the code cell.**
Click inside the code cell (the box with a `[ ]` on its left). Type:

    2 + 2

**Step 5 — Run the cell.**
Press Shift+Enter or click the play button. After a brief moment, the number `4` appears below the cell in the output area. The `[ ]` becomes `[1]`.

**Step 6 — Add a text cell.**
Click "+ Text" in the toolbar. A text cell appears below. Click inside it and type: `This is my first Colab notebook.` Click outside the cell (or press Shift+Enter) to render it.

**Step 7 — Save the notebook.**
Press Ctrl+S. Confirm that "All changes saved" appears at the top.

You have just created a notebook, run code, added a text cell, and saved your work. Every future lab in this course follows this same basic pattern.

---

## 7. Real-World Patterns

**Data science and AI teams use notebooks as living documents.** A Colab notebook is not just a scratchpad — it is a self-contained record of an analysis or experiment. Teams at research labs and companies share notebooks where the text cells explain the reasoning, the code cells show the implementation, and the output cells display the results. This is sometimes called a "computational essay." Your portfolio follows exactly this format: an assessor should be able to read your notebook and understand what you were trying to do, how you did it, and what happened [2].

**Notebooks travel well.** Because a `.ipynb` file contains both code and text, it can be shared, opened in Colab by anyone with a Google account, and re-run from scratch. This makes reproducibility straightforward — a quality valued highly in responsible AI work, where you need to be able to explain and replicate your results. You explored the idea of accountability and explainability in M4; notebooks are one practical tool for achieving it.

**Colab is also used outside education.** The official Colab intro notebook [2] and the features overview [3] are maintained by Google's research teams. Researchers publish entire paper implementations as Colab notebooks so that others can read and reproduce the work without any setup. When you encounter such notebooks in future work, you will already know how to navigate them.

---

## 8. Best Practices

**Run cells in order, from top to bottom.** Code cells in a notebook can affect each other — results computed in one cell are available in cells that run after it (you will learn exactly how this works through variables in topic 11.3). If you run cells out of order, you can create hard-to-debug situations where outputs are not what you expect. The safest habit is to write your notebook so it runs cleanly from the first cell to the last in a single pass. Use "Runtime -> Restart and run all" to verify this at any time [3].

**Name your notebook immediately.** When you create a new notebook it is called "Untitled0.ipynb". Click the name at the top of the page and give it a meaningful name (for example, `week11-lab-gradecalculator`). Colab notebooks saved to Drive accumulate quickly; a clear naming convention saves time later, especially when you are assembling your portfolio.

**Do not close the browser tab mid-execution.** If a long-running cell is executing and you close the tab, the runtime may lose the result. The cell will still exist in the notebook, but you will need to re-run it after reopening.

**Understand what autosave does — and does not — save.** Autosave preserves the cells and their last outputs as they appeared when the save triggered. It does not preserve the live computational state in memory. After reopening a notebook, always re-run the cells to restore that live state [4].

**Treat disconnects as normal, not as errors.** Colab's free tier will disconnect idle runtimes. This is expected behaviour, not a bug. When it happens, click "Reconnect" and re-run your cells from the top [4].

---

## 9. Hands-On Exercise

Before the next session:

1. Open Colab (colab.research.google.com) and create a new notebook. Name it `11-2-colab-orientation`.
2. In the first code cell, type `10 + 5` and run it with Shift+Enter.
3. Add a text cell below it. Write one sentence explaining in your own words what the output area shows.
4. Add a second code cell. Type `1 + 1` and run it. Note the output.
5. Save the notebook (Ctrl+S). Then download it as a `.ipynb` file (File -> Download -> Download .ipynb) and keep it somewhere you can find it.
6. Close the browser tab, wait 30 seconds, reopen Colab, and find your notebook in the recent list. Re-run all cells to confirm everything still works.

This exercise covers the full loop: create, write, run, save, retrieve, re-run. You will repeat this loop in every lab.

---

## 10. Key Takeaways

- **Google Colab runs entirely in the browser** — no software installation is needed because your code executes on Google's servers, not your local machine. The only requirement is a Google account [1].
- **A notebook is made of cells.** Code cells run Python; text cells hold explanatory writing. Both types live together in a single `.ipynb` file [2][3].
- **Running a cell sends its code to the runtime.** The result appears in the output area below the cell. Use the play button or Shift+Enter. The execution count (`[1]`, `[2]`, ...) shows the order cells were run [2].
- **A session is temporary.** When the runtime disconnects, computed results in memory are lost — but the code in your cells is saved to Google Drive and survives. Always re-run cells from the top when you reconnect [4].
- **Saving is automatic but confirming it is your responsibility.** Look for "All changes saved" or press Ctrl+S. For submission, download the `.ipynb` file [5].

---

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._

<!-- Downstream topics: 11.3 covers variables and data types (string, int, float, bool). Once the environment is set up, you will start writing actual Python code in topic 11.3. -->

---

## References

[1] Google Colab homepage — https://colab.research.google.com/

[2] Official Colab intro notebook — https://colab.research.google.com/notebooks/intro.ipynb

[3] Colab features overview notebook — https://colab.research.google.com/notebooks/basic_features_overview.ipynb

[4] Official Colab FAQ — https://research.google.com/colaboratory/faq.html

[5] Colab I/O notebook — https://colab.research.google.com/notebooks/io.ipynb
