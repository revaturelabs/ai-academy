---
topic_id: "6.4"
title: "Matrices — grids of numbers and how AI uses them"
position_in_module: 3
generated_at: "2026-06-18T00:00:00Z"
resource_count: 3
---

# 1. Matrices — grids of numbers and how AI uses them — Topic Corpus

## 2. Prerequisites

This topic builds directly on:

- **6.1 – Binary, pixels and numbers as representation** — understanding that all data in a computer is stored as numbers, and that a pixel is a single numerical value.
- **6.2 – Scalars** — a scalar is a single number representing one property; it is the building block of everything in this topic.
- **6.3 – Vectors** — a vector is an ordered list of scalars; each element lives at a specific position, and a feature vector encodes one data sample as a row of numbers.

Vectors and scalars are not re-defined here; they are used freely as prior knowledge.

## 3. Learning Objectives

By the end of this topic you will be able to:

- **Describe** what a matrix is in plain language — a rectangular grid of scalars arranged in rows and columns.
- **Read** standard matrix notation, including how to state its size using rows × columns (pronounced "rows by columns").
- **Identify** a row in a matrix as a feature vector that describes one data sample.
- **Explain** how AI uses matrices to store images, representing each pixel value as one cell in a grid.
- **Recognise** the term *weight matrix* and describe, in one sentence, why neural networks use one.
- **Name** four advanced matrix operations — multiplication, transpose, determinant, eigenvalues — and state that each is covered in a later topic.

## 4. Introduction

Imagine a school register. Down the left side there is a list of students — one student per row. Across the top there are columns labelled "Maths score", "English score", "Science score". Each cell in the table holds one number: a single scalar. The whole table is a **matrix**.

That is all a matrix is: a rectangular grid of numbers, with rows going across and columns going down. You already know the individual numbers are scalars (topic 6.2), and you already know a single row of those numbers is a vector (topic 6.3). A matrix simply stacks many vectors on top of each other.

Why does this matter for AI? Because almost every piece of data an AI system touches — an image, a dataset of customer records, the learned "knowledge" inside a neural network — is stored as a matrix. Once you can see data as a grid of numbers, you can see exactly what AI is doing when it reads, learns from, or produces that data [1].

## 5. Core Concepts

### 5.1 What is a matrix?

A **matrix** (plural: *matrices*) is a rectangular arrangement of scalars, organised into rows and columns [1].

- **Row** — a single horizontal line of numbers in the grid. Row 1 is the top row, row 2 is the one beneath it, and so on.
- **Column** — a single vertical line of numbers in the grid. Column 1 is the leftmost, column 2 is the next one to the right, and so on.
- **Cell** — the individual position where one row and one column meet. Each cell holds exactly one scalar.

Think of it like a spreadsheet: rows are the horizontal bands; columns are the vertical bands; every cell is a single number [2].

### 5.2 Matrix notation — rows × columns

Mathematicians and AI engineers describe the *size* of a matrix by stating how many rows it has and how many columns it has, always in that order: **rows × columns** (read as "rows by columns") [1].

| Example | Meaning |
|---|---|
| 3 × 4 matrix | 3 rows, 4 columns, 12 cells in total |
| 100 × 5 matrix | 100 rows, 5 columns, 500 cells in total |
| 28 × 28 matrix | 28 rows, 28 columns, 784 cells in total |

The convention "rows first, columns second" is universal in maths and AI. You will see it everywhere — always read left-to-right: rows × columns [1].

Individual cells are referenced by their row number and column number. The cell in row 2, column 3 is written as position (2, 3). Nothing more complicated than that.

### 5.3 A matrix as stacked feature vectors

In topic 6.3 you learned that a **feature vector** encodes one data sample as an ordered list of numbers. For example, one house might be described by the vector: [3 bedrooms, 120 m², 2 bathrooms, 15 years old].

When you have a *dataset* — many data samples — you do not store them as separate vectors scattered around. You stack them. Put the first sample's feature vector on row 1, the second on row 2, the third on row 3, and so on. The result is a matrix where:

- **Each row is one data sample** (one feature vector from topic 6.3).
- **Each column is one feature** (one measurable property, as introduced in topic 6.3).

So a dataset of 1,000 houses, each described by 4 features, becomes a **1000 × 4 matrix** — 1,000 rows (one per house) and 4 columns (one per feature) [2].

This is how AI systems store training data. The entire dataset is a single matrix. Processing the data means working with that matrix [1].

### 5.4 Image pixel grids — matrices in every photo

In topic 6.1 you learned that a pixel is a number representing a colour or brightness. A digital image is simply a grid of pixels arranged in rows and columns — which is exactly what a matrix is [2].

A small grayscale (black-and-white) image that is 28 pixels wide and 28 pixels tall is a **28 × 28 matrix**. Each cell holds one scalar: the brightness of that pixel, typically a number between 0 (black) and 255 (white).

Here is a tiny 4 × 5 pixel image shown as its matrix of numbers:

```
Row 1:  [255, 200, 180, 160, 140]
Row 2:  [130, 120, 110, 100,  90]
Row 3:  [ 80,  70,  60,  50,  40]
Row 4:  [ 30,  20,  10,   5,   0]
```

This is a 4 × 5 matrix (4 rows, 5 columns). When an AI reads a photo, it is reading numbers from a matrix exactly like this one [1][2].

Colour images add a third dimension — one grid for red, one for green, one for blue — but that idea is covered in a later topic. For now: one grayscale image = one matrix of pixel scalars.

### 5.5 Weight matrices — the "knowledge" inside a neural network

When an AI system (such as a neural network) learns from data, the numbers it learns are stored in a **weight matrix** — a grid where each cell holds one scalar that shapes the network's output [1][3]. Weight matrices are a key reason AI engineers care about matrices; how they are used in practice (an operation called matrix multiplication) is covered in a later topic.

### 5.6 Advanced operations — named here, taught later

The following concepts involve matrices but are outside the scope of this topic. Each is named once and deferred:

- **Matrix multiplication** — an operation that combines two matrices to produce a third; covered in a later topic.
- **Transpose** — rearranging a matrix by swapping its rows and columns; covered in a later topic.
- **Determinant** — a single scalar computed from a square matrix; covered in a later topic.
- **Eigenvalues** — special scalars extracted from a matrix that reveal how it stretches or compresses data; covered in a later topic.

You do not need to understand any of these now. They are listed so you will recognise the words when you encounter them.

## 6. Implementation

The steps below show how to think about data as a matrix — no programming required.

**Step 1 — Identify your data samples.**
List the things you are describing. Example: five students.

**Step 2 — Identify your features.**
List the numbers you record per sample. Example: maths score, English score, science score (3 features).

**Step 3 — Build the grid.**
Draw a table. Put samples on rows, features on columns.

```
             Maths  English  Science
Student 1: [  72,    85,      90   ]
Student 2: [  60,    78,      55   ]
Student 3: [  88,    91,      76   ]
Student 4: [  45,    62,      70   ]
Student 5: [  95,    88,      82   ]
```

**Step 4 — State the size.**
Count rows and columns: 5 rows × 3 columns. This is a **5 × 3 matrix**.

**Step 5 — Read any cell.**
"What is Student 3's English score?" Row 3, column 2 → 91.

That is how every AI dataset is laid out internally. Rows are samples; columns are features; cells are scalars [2].

## 7. Real-World Patterns

Matrices appear in AI systems constantly. Three concrete examples:

**Handwritten digit recognition (MNIST dataset)**
The most famous beginner AI dataset — MNIST — contains 70,000 images of handwritten digits (0–9). Each image is 28 × 28 pixels, so each image is a 28 × 28 matrix. When an AI model trains on MNIST, it reads through all 70,000 of these grids one by one [1][3].

**Recommendation systems**
A streaming service that recommends films can represent its data as a matrix: rows are users, columns are films, and each cell holds a rating (or 0 if the user has not watched that film). Finding patterns in that matrix tells the system which films to suggest to which users [2].

**Neural network layers**
In a neural network, every layer is connected to the next by a weight matrix. A network with 784 inputs (one per pixel in a 28 × 28 image) connecting to 128 neurons holds a **784 × 128 weight matrix** — that is 100,352 individual weight scalars. The entire learned "knowledge" of a trained network lives inside its weight matrices [1][3].

## 8. Best Practices

**Do remember rows × columns, in that order.**
The convention is always rows first, columns second. Swapping the order is the most common beginner mistake, and it causes silent errors later when you start doing operations on matrices.

**Do think of each row as one data sample.**
This mental model carries through the entire course. Rows = samples; columns = features. Internalise it now.

**Do not confuse the size of a matrix with its total cell count.**
A 4 × 5 matrix has 4 rows and 5 columns. It has 20 cells total. The size is stated as "4 × 5", not "20".

**Do not rush into matrix operations.**
Multiplication, transpose, determinant, eigenvalues — those come later. Get the structure right first.

## 9. Hands-On Exercise

**Exercise: Build and read a matrix**

1. Open any spreadsheet tool (Google Sheets, Excel, or a plain text editor).
2. Create a small table: 5 rows of data (one row per person), 3 columns (for example: height in cm, age in years, number of siblings).
3. Fill every cell with a number.
4. Write down the size of your matrix using rows × columns notation.
5. Pick one cell and state its position as (row number, column number).
6. State in one sentence what a single row represents (answer: one data sample — one person) and what a single column represents (answer: one feature).

## 10. Key Takeaways

- A **matrix** is a rectangular grid of scalars arranged in rows and columns — nothing more, nothing less [1].
- Matrix size is always stated as **rows × columns** (rows first, columns second): a 3 × 4 matrix has 3 rows and 4 columns [1].
- Each **row in a data matrix is one feature vector** — one data sample described by all its features [2].
- AI systems use matrices for **images** (each pixel's brightness is one cell) and for **weight matrices** (each learned weight scalar is one cell) [1][3].
- Matrix multiplication, transpose, determinant, and eigenvalues are real and important — but are covered in later topics; for now, recognise the names only.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
