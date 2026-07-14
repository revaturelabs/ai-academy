---
topic_id: 1.8
title: Flowcharts — visualising logic with standard shapes and arrows
position_in_module: 2
generated_at: 2026-06-21T00:00:00Z
resource_count: 3
---

# 1. Flowcharts — Visualising Logic with Standard Shapes and Arrows — Topic Corpus

## 2. Prerequisites

This topic builds directly on one earlier topic:

- **1.7 — Pseudocode**: introduced the three building blocks of logic — sequence, decision, and repetition — and showed how to write them out in plain English. Flowcharts express exactly those same building blocks, but using shapes and arrows instead of words.

The concepts of sequence, decision (IF/OTHERWISE), condition, and repetition are assumed known. This topic does not re-teach them — it shows you how to draw them.

## 3. Learning Objectives

By the end of this topic, you should be able to:

- Name the five standard flowchart shapes and state what each one means.
- Read a simple flowchart and describe, in plain language, the logic it represents.
- Draw a flowchart for a short, real-world process using the correct shapes and arrow conventions.
- Explain how a flowchart and a pseudocode block describe the same logic in different forms.
- Identify a decision diamond and trace both the YES and NO paths through it.

## 4. Introduction

In topic 1.7 you wrote logic out in plain English — "IF the score is 50 or above, PRINT Pass; OTHERWISE, PRINT Fail." That worked well. But imagine you are trying to explain that same logic to a team of five people in a meeting, or hand it to someone who speaks a different language. A block of written steps is harder to scan at a glance than a picture.

That is the problem flowcharts solve. A **flowchart** is a diagram that shows a process as a series of steps, connected by arrows, where each step is drawn as a specific shape. The shape tells you what kind of step it is [1].

You have almost certainly seen flowcharts without knowing the name — "Is your device plugged in? YES → continue. NO → plug it in." That is a flowchart. Customer service scripts, decision trees in troubleshooting guides, and process maps on factory walls are all flowcharts.

For computing, flowcharts matter because they make the logic of an **algorithm** — a set of step-by-step instructions for completing a task — visible. Instead of reading through lines of text, you can see the shape of the process — where it starts, where it branches, where it loops, and where it ends [2]. When the shapes are standardised — meaning every person who draws a flowchart uses the same shapes for the same things — any reader can understand the diagram immediately, without needing an explanation [3].

This topic teaches you those standard shapes, the rules for connecting them, and how to translate a pseudocode block into a flowchart (and back again).

## 5. Core Concepts

### 5.1 What a Flowchart Is

**Flowchart** — a diagram that represents a process or algorithm as a set of steps (drawn as shapes) connected by directed arrows that show the order of those steps [1].

Every flowchart has:

1. **Shapes** — each shape type has a specific meaning (defined below).
2. **Flowlines** — arrows that connect the shapes and show which step comes next.
3. **A clear start and a clear end.**

The word "standard" is important. The shapes described in this topic come from an internationally recognised convention. When you use them, anyone trained in computing can read your diagram — regardless of which tool you drew it in [3].

### 5.2 The Five Standard Shapes

There are dozens of flowchart symbols in the full standard, but five cover almost every process you will draw as a beginner. Learn these five and you can diagram any basic algorithm [1][3].

#### Shape 1 — Terminator (Oval)

**Terminator** — an oval shape that marks the start or end of a process.

Every flowchart has exactly two terminators: one labelled **START** (or BEGIN) at the top, and one labelled **END** (or STOP) at the bottom. No arrows enter the START terminator from above; no arrows leave the END terminator.

Why an oval? Convention. The rounded shape signals "this is a boundary, not an action" — visually distinct from the rectangular process boxes in the middle [1].

#### Shape 2 — Process Box (Rectangle)

**Process box** — a rectangle that represents a single action or step.

This is the most common shape. Any step that does something — a calculation, an assignment, a transformation — goes in a rectangle.

Examples:
- "Set total to 0"
- "Add item price to total"
- "Multiply length by width"

One action per box. If you find yourself writing two actions separated by "then" inside one rectangle, split it into two rectangles [1][3].

#### Shape 3 — Decision Diamond

**Decision diamond** — a diamond (rhombus) shape that represents a question with exactly two outcomes.

The diamond has one arrow entering it (from above or the side) and two arrows leaving it. The two outgoing arrows are labelled **YES** and **NO** (sometimes **True/False** or **Y/N**). Each label points to a different next step [1][2].

This shape directly represents the IF/OTHERWISE building block from topic 1.7. The condition you put inside the diamond is the same condition you would write after IF in pseudocode.

Example: the diamond contains "Is score ≥ 50?" — the YES arrow leads to a "Print Pass" box, the NO arrow leads to a "Print Fail" box.

A diamond always asks a yes/no question. If your question has more than two answers, you use multiple diamonds in sequence [3].

#### Shape 4 — Input/Output Parallelogram

**Input/output parallelogram** — a slanted four-sided shape (parallelogram) that represents data coming into the process (input) or results going out of the process (output).

Use this shape when:
- The process receives something from the user or an external source ("Get the user's name").
- The process displays or delivers a result ("Print the total cost").

Why a different shape from the process box? Because reading a value from a user and calculating a value are different kinds of operations. The parallelogram signals: "data is crossing the system boundary here" [1][3].

#### Shape 5 — Flowline (Arrow)

**Flowline** — a directed arrow that connects two shapes and shows the direction of flow.

Flowlines tell you which shape comes after which. They always have an arrowhead at one end to show direction. In a simple top-to-bottom flowchart, all arrows point downward. When a decision diamond sends flow in two directions, or when a loop brings flow back upward, the arrows make those paths explicit [2][3].

Rules for flowlines:
1. Every shape except the END terminator must have at least one outgoing arrow.
2. Every shape except the START terminator must have at least one incoming arrow.
3. A decision diamond must have exactly two outgoing arrows, each labelled.
4. Arrows should not cross each other if you can avoid it — re-route to keep the diagram readable.

### 5.3 Summary Table — Standard Shapes at a Glance

| Shape | Name | What it represents | Looks like |
|---|---|---|---|
| Oval | Terminator | Start or End of the process | Rounded pill shape |
| Rectangle | Process box | An action or step | Standard rectangle |
| Diamond | Decision diamond | A yes/no question (branch) | Rotated square |
| Parallelogram | Input/Output parallelogram | Data entering or leaving | Slanted rectangle |
| Arrow | Flowline | Direction of flow | Line with arrowhead |

### 5.4 Pseudocode and Flowcharts — Same Logic, Different Medium

In topic 1.7 you learned that the three building blocks of logic are sequence, decision, and repetition. Flowcharts draw exactly those same three building blocks using shapes. The logic is identical — only the medium changes.

Here is the mapping:

| Pseudocode building block | Flowchart equivalent |
|---|---|
| Sequence — steps in order | Rectangles (and parallelograms) stacked top-to-bottom, connected by flowlines |
| Decision (IF/OTHERWISE) | A decision diamond with a YES path and a NO path diverging, then rejoining |
| Repetition | An arrow from a later box that loops back up to a decision diamond above it |

The key insight: **the choice between pseudocode and a flowchart is not about which is correct — it is about what your audience finds clearer.** A developer skimming logic alone may prefer pseudocode. A stakeholder in a meeting room may find a flowchart easier to follow at a glance [2].

Both are planning tools. Both represent the same underlying logic. You will often use both on the same project: draft the logic as pseudocode, draw it as a flowchart for communication, then code from either [1].

### 5.5 Reading a Flowchart

Reading a flowchart is a skill you practice by tracing. To trace a flowchart:

1. Find the START oval. That is where you begin.
2. Follow the first flowline to the next shape.
3. If the shape is a **process box or input/output parallelogram**, carry out the action mentally and follow the outgoing arrow.
4. If the shape is a **decision diamond**, check the condition. Follow the YES arrow if the condition is true; follow the NO arrow if it is false.
5. Continue until you reach the END oval.

Try this with the student-pass example:

- START
- Parallelogram: "Get student score" → you receive the value 45
- Diamond: "Is score ≥ 50?" → 45 is NOT ≥ 50, so follow NO
- Rectangle: "Print Fail"
- END

Now trace again with score = 72:

- START
- Parallelogram: "Get student score" → you receive 72
- Diamond: "Is score ≥ 50?" → 72 IS ≥ 50, so follow YES
- Rectangle: "Print Pass"
- END

The diagram is the same both times. The path through it changes depending on the input. That is what makes flowcharts useful: you can see every possible path through a process in one picture [2][3].

### 5.6 Loops in Flowcharts

A **loop** in a flowchart is a path where one or more arrows point backwards (upward) to a shape that was already visited. Loops represent the repetition building block from topic 1.7.

A typical loop looks like this:

1. A decision diamond checks a condition.
2. If the condition is true (YES), the flowline moves forward to one or more process boxes.
3. After the last process box in the loop body, a flowline curves back up to the decision diamond.
4. When the condition becomes false (NO), the flowline exits the loop and moves on to the next step.

Example — adding up items in a shopping cart:

- Diamond: "Are there more items?" → YES leads to a process box ("Add item price to total"), which loops back to the diamond. NO leads to a process box ("Print total"), then END.

The decision diamond always stays in the same position in the diagram. The looping flowline is the only visual sign that repetition is happening [1][2].

## 6. Implementation

### Drawing a Flowchart — A Step-by-Step Method

You can apply this process every time you need to turn a process description (or a pseudocode block) into a flowchart [1][2][3]:

1. **State the process in one sentence.** What does it do? Example: "Check whether a user's age allows them to register."

2. **Identify the start and end.** Draw an oval at the top (START) and one at the bottom (END) first — they anchor the diagram.

3. **List the steps in order.** Work through the process as if you were writing pseudocode: what happens first? What is the first decision? What loops?

4. **Choose a shape for each step:**
   - Is it an action or calculation? → Rectangle (process box).
   - Does data come in or go out? → Parallelogram (input/output).
   - Is it a yes/no question? → Diamond (decision diamond).

5. **Connect the shapes with flowlines.** Label both exits from every decision diamond (YES / NO).

6. **Check loop backs.** If any step repeats, draw the return arrow back to the appropriate decision diamond. Make sure the arrow direction is clear.

7. **Verify completeness.** Every shape except END has an outgoing flowline. Every shape except START has an incoming flowline. Every decision diamond has exactly two labelled exits.

8. **Trace through it with a test example.** Pick a real input value and follow the flowchart from START to END. Does it produce the right outcome?

### Worked Example — "Check Whether a User May Register"

Process: a user types in their age. If the age is 18 or above, registration proceeds. If not, an error message appears.

**Pseudocode (using the building blocks from topic 1.7):**
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

**Equivalent flowchart (described in text — see diagram artifact for the visual):**

1. Oval: START
2. Parallelogram: "Get user age" (input)
3. Decision diamond: "Is user age ≥ 18?"
   - YES path → Rectangle: "Print Registration approved" → Oval: END
   - NO path → Rectangle: "Print You must be 18 or older" → Oval: END

Both the pseudocode and the flowchart contain exactly the same logic. The flowchart makes the two paths visually obvious at a glance. The pseudocode is faster to type. You choose the representation to fit the context [1][2].

## 7. Real-World Patterns

### Where Flowcharts Appear in Practice

Flowcharts are one of the most widely used communication tools in computing and business [1][2][3]:

**Troubleshooting guides.** "Is the device powered on? YES → proceed. NO → plug it in." Technical support documentation is almost always a flowchart, whether drawn explicitly or not.

**Customer service scripts.** Call centre agents follow flowcharts — often without realising that is what they are — to handle different customer scenarios. The decision diamonds are the branching questions.

**Software design reviews.** Before a team writes code for a new feature, they often draw a flowchart to show the logic to non-technical stakeholders. The shapes convey the structure of the process without requiring anyone to read code.

**Algorithm description in textbooks.** Most introductory computing textbooks teach search and sort algorithms using flowcharts. You will encounter these later in the course.

**Business process documentation.** Organisations document procedures — how an expense is approved, how a complaint is escalated — as flowcharts so new staff can follow them without needing to ask. More complex process diagrams build on basic flowcharting as a foundation.

The common thread: a flowchart communicates process logic to a mixed audience — some technical, some not — faster than a block of text or code [3].

## 8. Best Practices

### Do

- **Use the standard shapes.** Do not invent your own. A diamond that means "process" to you means "decision" to every other reader [3].
- **One action per process box.** If a box contains "Get the input AND validate it", split it into two boxes.
- **Label both exits from every decision diamond.** Unlabelled arrows on a diamond are ambiguous — always write YES and NO (or True/False) [1].
- **Draw top-to-bottom, left-to-right.** This is the conventional reading direction. Readers expect it.
- **Keep diagrams readable.** If your flowchart is too large to read on one page, it is a signal to break the process into smaller parts.
- **Trace through with at least two test cases** — one that takes the YES path and one that takes the NO path at each decision diamond. Verify you reach END in both cases.

### Avoid

| Avoid | Reason |
|---|---|
| Using a rectangle for a decision | Misleads every reader expecting a YES/NO branch |
| Leaving a decision diamond with one exit | A question with no NO path is not a decision — use a rectangle instead |
| Arrows that loop with no exit condition | The process can never reach END — an infinite loop |
| Cramming multiple actions into one process box | Hides detail; makes tracing impossible |
| Drawing flowcharts without tracing them | An untraced flowchart is an unverified plan |

## 9. Hands-On Exercise

**Exercise: Flowchart for a real-world task**

This connects directly to the week's lab activity — drawing flowcharts for real-world tasks and swapping with a partner to verify they can follow them exactly.

1. Choose a simple everyday task — deciding what to wear based on the weather, checking whether a parcel has arrived, deciding whether to take an umbrella.
2. Write 3–5 lines of pseudocode for it using the building blocks from topic 1.7 (sequence, decision, and repetition where needed).
3. Translate your pseudocode into a flowchart: one shape per step, a decision diamond for every IF, flowlines connecting everything, START and END ovals at the top and bottom.
4. Hand your flowchart to a partner. Ask them to trace it with a real input value. Do they reach END? Do they reach the outcome you intended?
5. If they got stuck or went the wrong way, identify which shape or arrow was unclear. Fix it.

The goal is to see that a flowchart only works if every path leads somewhere and every decision diamond has two labelled exits [1][2].

## 10. Key Takeaways

- **A flowchart is a visual diagram** that represents a process using standard shapes connected by directed arrows — it is the same logic as pseudocode, drawn instead of written.
- **The five standard shapes are:** terminator (oval) for START/END, process box (rectangle) for actions, decision diamond for yes/no questions, input/output parallelogram for data crossing the system boundary, and flowline (arrow) for direction of flow.
- **Decision diamonds always have two labelled exits: YES and NO.** This is the visual form of the IF/OTHERWISE building block from topic 1.7.
- **Loops are shown by a flowline pointing back up to a decision diamond.** When the condition is false, the flowline exits the loop — without this exit, the process never ends.
- **Pseudocode and flowcharts are interchangeable representations of the same logic.** Choose the form that best communicates to your audience.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._

---
concepts_introduced:
  - flowchart
  - terminator (oval)
  - process box (rectangle)
  - decision diamond
  - input/output parallelogram
  - flowline (arrow)
  - loop (in a flowchart)
depth_profile_suggestion: standard
depth_profile_signals: "Concrete visual notation with 5 standard shapes; explicit bridge from 1.7 pseudocode; hands-on drawing task in lab; five shapes plus loop concept fits standard depth without padding."
requires_diagram: true
diagram_intent: "Side-by-side: pseudocode snippet (left) and equivalent flowchart (right), with each standard shape labelled by name"
scope_flags: []
prerequisites:
  - "1.7"
cross_refs: []
---
