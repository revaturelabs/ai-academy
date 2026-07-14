<!-- nav:top:start -->
[⬅ Previous: 1.7 — Pseudocode](../../1-7-pseudocode-writing-logic-in-plain-english-before-writing-cod/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 1.9 — Algorithmic thinking ➡](../../../4-algorithmic-thinking/1-9-algorithmic-thinking-what-makes-a-set-of-steps-an-algorithm/artifacts/reading.md)
<!-- nav:top:end -->

---

# Flowcharts — Visualising Logic with Standard Shapes and Arrows

## Overview

In topic 1.7 you wrote logic out in plain English using pseudocode. A flowchart shows the exact same logic as a picture. Each step is drawn as a specific shape, and arrows connect the shapes to show what happens next. Flowcharts make it easy to see every possible path through a process at a glance — including branches and loops — before a single line of code is written [1].

## Key Concepts

### What a flowchart is

**Flowchart** — a diagram that represents a process as a set of steps drawn as shapes, connected by directed arrows [1].

Every flowchart has three things:

1. **Shapes** — each shape type has one fixed meaning.
2. **Flowlines** — arrows that show which step comes next.
3. **A clear start and a clear end.**

The shapes described below follow an internationally recognised convention. When you use them, anyone trained in computing can read your diagram straight away — no explanation needed [3].

### The five standard shapes

There are dozens of flowchart symbols in the full standard. These five cover almost every process you will draw as a beginner [1][3].

**Shape 1 — Terminator (oval)**

**Terminator** — an oval that marks the start or end of a process.

Every flowchart has exactly two: one labelled **START** at the top and one labelled **END** at the bottom. No arrows enter START from above; no arrows leave END.

**Shape 2 — Process box (rectangle)**

**Process box** — a rectangle that represents a single action or step.

This is the most common shape. Any step that does something — a calculation, an assignment — goes in a rectangle. Examples: "Set total to 0", "Multiply length by width".

One rule: one action per box. If you find yourself writing two actions separated by "then", split into two rectangles [1][3].

**Shape 3 — Decision diamond**

**Decision diamond** — a diamond shape that represents a yes/no question.

The diamond has one arrow entering it and two arrows leaving it. The two outgoing arrows are labelled **YES** and **NO**. Each label points to a different next step [1][2].

This shape is the visual form of the IF/OTHERWISE building block from topic 1.7. Example: the diamond contains "Is score ≥ 50?" — the YES arrow leads to a "Print Pass" box; the NO arrow leads to a "Print Fail" box.

**Shape 4 — Input/output parallelogram**

**Input/output parallelogram** — a slanted four-sided shape that represents data coming into the process (input) or results going out (output).

Use it when the process receives something from the user ("Get the user's name") or delivers a result ("Print the total cost"). It is a different shape from the rectangle because reading a value and calculating a value are different kinds of operations [1][3].

**Shape 5 — Flowline (arrow)**

**Flowline** — a directed arrow that connects two shapes and shows the direction of flow [2][3].

Rules for flowlines:

1. Every shape except END must have at least one outgoing arrow.
2. Every shape except START must have at least one incoming arrow.
3. A decision diamond must have exactly two outgoing arrows, each labelled.
4. Avoid crossing arrows — re-route to keep the diagram readable.

### Shapes at a glance

| Shape | Name | What it represents |
|---|---|---|
| Oval | Terminator | Start or End of the process |
| Rectangle | Process box | An action or step |
| Diamond | Decision diamond | A yes/no question (branch) |
| Parallelogram | Input/output parallelogram | Data entering or leaving |
| Arrow | Flowline | Direction of flow |

### The diagram below shows all five shapes labelled in a worked flowchart

![Five Standard Flowchart Shapes — User Age Check](./diagram.png)
*The user age check flowchart with each standard shape labelled: terminator (oval), input parallelogram, decision diamond, process boxes (rectangles), and flowlines (arrows).*

### Pseudocode and flowcharts — same logic, different medium

The three building blocks you learned in topic 1.7 — sequence, decision, and repetition — map directly onto flowchart shapes:

| Pseudocode building block | Flowchart equivalent |
|---|---|
| Sequence — steps in order | Rectangles and parallelograms stacked top-to-bottom, connected by flowlines |
| Decision (IF/OTHERWISE) | A decision diamond with a YES path and a NO path diverging, then rejoining |
| Repetition | A flowline pointing back up to a decision diamond already visited |

The logic is identical in both forms. The choice between them depends on your audience. A developer skimming logic alone may prefer pseudocode. A stakeholder in a meeting may find a flowchart easier to follow at a glance [2].

### How to read (trace) a flowchart

Tracing is how you verify a flowchart is correct. Follow these steps:

1. Find the START oval — that is where you begin.
2. Follow the first flowline to the next shape.
3. If the shape is a **process box or parallelogram**, carry out the action mentally, then follow the outgoing arrow.
4. If the shape is a **decision diamond**, check the condition. Follow YES if the condition is true; follow NO if it is false.
5. Continue until you reach the END oval.

Try it with the student-pass example, score = 45:

- START → "Get student score" (parallelogram, value = 45)
- "Is score ≥ 50?" (diamond) → 45 is NOT ≥ 50, follow NO
- "Print Fail" (rectangle) → END

Now trace with score = 72:

- START → "Get student score" (parallelogram, value = 72)
- "Is score ≥ 50?" (diamond) → 72 IS ≥ 50, follow YES
- "Print Pass" (rectangle) → END

The diagram is identical both times. The path through it changes with the input. That is what makes flowcharts useful: one picture shows every possible outcome [2][3].

### Loops in flowcharts

A **loop** in a flowchart is a path where one or more arrows point back up to a shape already visited. Loops represent the repetition building block [1][2].

A typical loop works like this:

1. A decision diamond checks a condition.
2. If YES, flowlines move forward through one or more process boxes.
3. After the last box in the loop body, a flowline curves back up to the same decision diamond.
4. When the condition becomes NO, the flowline exits the loop and moves on.

Example — adding up items in a shopping cart: "Are there more items?" → YES leads to "Add item price to total", which loops back to the diamond. NO leads to "Print total", then END.

The decision diamond does not move. The looping flowline is the only visual sign that repetition is happening [1][2].

## Worked Example

**Process:** a user types in their age. If the age is 18 or above, registration proceeds. If not, an error message appears.

**Pseudocode (building blocks from topic 1.7):**

```
START
  GET user_age
  IF user_age >= 18
    PRINT "Registration approved"
  OTHERWISE
    PRINT "You must be 18 or older"
  END IF
END
```

**Equivalent flowchart — step by step:**

1. Oval: START
2. Parallelogram: "Get user age" (input)
3. Decision diamond: "Is user age ≥ 18?"
   - YES path → Rectangle: "Print Registration approved" → Oval: END
   - NO path → Rectangle: "Print You must be 18 or older" → Oval: END

Both forms contain exactly the same logic. The flowchart makes the two paths visually obvious. The pseudocode is faster to type. You choose the form that fits the context [1][2].

To verify the flowchart, trace it twice — once with age = 20, once with age = 15. You should reach END both times, through different boxes.

## In Practice

Flowcharts appear across computing and business wherever a process needs to be communicated to a mixed audience [1][2][3]:

- **Troubleshooting guides** — "Is the device powered on? YES → proceed. NO → plug it in." Technical support documentation follows this pattern.
- **Customer service scripts** — call centre agents follow flowcharts (often without knowing that is what they are) to handle different customer scenarios.
- **Software design reviews** — teams draw a flowchart to explain feature logic to non-technical stakeholders before writing any code.
- **Business process documentation** — organisations document approval workflows as flowcharts so new staff can follow them without asking.

The common thread: a flowchart communicates process logic faster than a block of text or code to a mixed audience [3].

**Key rules to follow every time:**

- Use standard shapes only — do not invent your own. A diamond means decision to every reader [3].
- One action per process box — if a box contains two actions separated by "and", split it.
- Label both exits from every decision diamond — an unlabelled arrow on a diamond is ambiguous [1].
- Every loop must have an exit condition — a loop with no NO path can never reach END.
- Trace with at least two test cases before calling a flowchart done.

**Common mistakes to avoid:**

| Mistake | Why it matters |
|---|---|
| Using a rectangle for a decision | Misleads every reader expecting a YES/NO branch |
| Leaving a decision diamond with one exit | A question with no NO path is not a decision |
| A loop with no exit condition | The process can never reach END — an infinite loop |
| Multiple actions in one process box | Hides detail; makes tracing unreliable |

## Key Takeaways

- **A flowchart is a visual diagram** — the same logic as pseudocode, drawn as shapes and arrows instead of written steps [1].
- **The five standard shapes are:** terminator (oval) for START/END, process box (rectangle) for actions, decision diamond for yes/no questions, input/output parallelogram for data crossing the system boundary, and flowline (arrow) for direction of flow [1][3].
- **Decision diamonds always have two labelled exits: YES and NO.** This is the visual form of the IF/OTHERWISE building block from topic 1.7 [2].
- **Loops are shown by a flowline pointing back up to a decision diamond.** When the condition is false, the flow exits — without this exit, the process never ends [1][2].
- **Pseudocode and flowcharts are interchangeable.** Choose the form that best communicates to your audience [2].

## References

1. Visual Paradigm, "Flowchart Tutorial." <https://www.visual-paradigm.com/tutorials/flowchart-tutorial/>
2. GeeksforGeeks, "An Introduction to Flowcharts." <https://www.geeksforgeeks.org/dsa/an-introduction-to-flowcharts/>
3. SmartDraw, "Flowchart Symbols." <https://www.smartdraw.com/flowchart/flowchart-symbols.htm>

---
<!-- nav:bottom:start -->
[⬅ Previous: 1.7 — Pseudocode](../../1-7-pseudocode-writing-logic-in-plain-english-before-writing-cod/artifacts/reading.md)&emsp;·&emsp;[⬆ Table of Contents](../../../../../../../README.md#curriculum-topic-index)&emsp;·&emsp;[Next: 1.9 — Algorithmic thinking ➡](../../../4-algorithmic-thinking/1-9-algorithmic-thinking-what-makes-a-set-of-steps-an-algorithm/artifacts/reading.md)
<!-- nav:bottom:end -->
