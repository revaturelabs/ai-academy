# Object-Oriented Foundations

## Overview

Every program you've written so far keeps data and the logic that acts on it as two separate things: a variable here, a statement over there. That works for one task, but it falls apart once you're tracking several related values about the same thing — a task's name, priority, and done status — alongside logic that needs all three at once. Object-oriented programming (OOP) fixes this by packaging state (data) and behavior (the logic that acts on it) into a single unit called an object. This topic gives you the vocabulary and mechanics — classes, objects, `__init__`, `self`, instance and class attributes, methods — that every later refinement in this course (inheritance, encapsulation, operator overloading, dataclasses) builds on top of. _This contributes to A3 — Python Foundations Diagnostic (due W8), by giving you the class-and-object vocabulary the diagnostic will test directly._

## Key Concepts

**Abstract data types.** An **abstract data type (ADT)** describes a "thing" by what it *is* and what it *can do*, without worrying about implementation. A `Task` is an ADT if you can say: it has a name, a priority, and a done status (state), and it can be marked complete (behavior). Before classes, you'd model this with loose variables and a function:

```python
task_name = "Write topic corpus"
task_priority = "normal"
task_done = False

def mark_complete(done):
    return True

task_done = mark_complete(task_done)
```

This works for one task, but nothing ties `task_name` to `task_priority` to `task_done` — they're just variables sitting near each other. Nothing stops you from passing the wrong one into a function by mistake. The official Python tutorial frames the class mechanism as exactly the fix: a way to bundle data and the functions that operate on it so the association is enforced by the language, not by memory [1]. A class is really two things wearing one name — a *contract* (what attributes and methods any instance can be relied on to have) and an *implementation* (how those are stored and written) — and that separation is the entire reason ADT thinking is worth the shift.

**Class vs. object.** A **class** is a blueprint: it defines what attributes and methods every object built from it will have, but a class alone isn't a usable "thing" — it's the plan. An **object**, or **instance**, is a specific thing created from that blueprint with its own actual values. You can create as many instances as you like, and each holds independent state:

```python
class Task:
    pass

first_task = Task()
second_task = Task()

print(type(first_task))            # <class '__main__.Task'>
print(first_task is second_task)   # False -- two separate objects
```

`type(first_task)` reports the class an object was built from, the same way `type()` reported `float` or `str` back in 1.2 [1]. `first_task is second_task` is `False` because `is` compares object identity: two calls to `Task()` allocate two distinct objects in memory, even from the identical blueprint. By convention, class names use `PascalCase` (`Task`, `Person`), while instance names follow the `snake_case` rule from 1.2 — not enforced by Python, but followed by every professional codebase so a name alone signals blueprint vs. thing-built-from-it [2].

**The constructor, and instance vs. class attributes.** An empty class isn't useful. The **constructor**, `__init__`, is a special method Python calls automatically on every new instance to set up its starting state:

```python
class Task:
    category = "general"      # class attribute -- shared by every Task

    def __init__(self, name, priority):
        self.name = name          # instance attribute
        self.priority = priority  # instance attribute
        self.done = False         # instance attribute
```

`self.name = name` creates an **instance attribute** — a variable that belongs to *this* object alone. `category`, defined directly in the class body rather than inside `__init__`, is a **class attribute**: shared by every instance unless one instance is given its own copy that shadows it [1][3]. Notice `priority` has no default value — every `Task(...)` call must supply both `name` and `priority` as required, positional arguments, the same way you already call `print()` and `type()`. Python's default-parameter syntax is a feature of functions you haven't met yet, so every constructor in this topic takes required positional parameters only.

The diagram below traces exactly this: one `Task` blueprint, `__init__` building two separate instances from it, and what happens when a class attribute is overridden on just one of them.

![One class, many independent instances](artifacts/diagram.png)
*Instantiating `Task` twice through `__init__` produces two independent objects that share the class attribute `category` until one instance overrides it locally.*

Changing `Task.category` through the class changes what every instance without its own copy sees; assigning `t1.category = "personal"` instead creates a brand-new instance attribute on `t1` alone, which now shadows the class attribute for `t1` only — `t2` is untouched. Real Python's class-mechanics deep dive flags this as the most common source of confusion for people new to classes: assigning through an instance never changes the class attribute, it only creates or overwrites an attribute local to that one instance [3]. Use class attributes for values genuinely shared across every instance; use instance attributes, set via `self.attribute = value` inside `__init__`, for anything that varies per object — in practice, almost everything you model.

**Methods and `self`.** A **method** is a function defined inside a class body — the "what it can do" half of the ADT:

```python
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.done = False

    def mark_complete(self):
        self.done = True

    def describe(self):
        return f"{self.name} ({self.priority}) - done={self.done}"

t1 = Task("Write topic corpus", "normal")
t1.mark_complete()
print(t1.describe())   # Write topic corpus (normal) - done=True
```

`describe` interpolates the raw boolean `self.done` directly into the f-string (from 1.4) rather than branching on it — turning it into different text based on a condition is a job for the Conditionals topic later in this course. Every method takes `self` as its first parameter: it's how the method reaches back to the specific object it was called on. When you write `t1.mark_complete()`, Python automatically passes `t1` in as `self` — you never pass it explicitly. This is a naming convention, not a keyword, but every Python codebase uses `self`, so you should too [1]. Under the hood, Python looks up `mark_complete` on `t1`'s class (not on `t1` itself — instances don't carry their own copy of each method), finds the function, and *binds* it to `t1` so `self` inside the body means "this object" [3]. `mark_complete` and `describe` both need `self` and nothing else, because `self` already carries which task to act on.

## Worked Example

Building a class follows the same four steps every time. Here they are applied to a `BankAccount`, tying every piece above together.

**Step 1 — name the class**, `PascalCase`:

```python
class BankAccount:
    ...
```

**Step 2 — write `__init__`**, taking required positional parameters and assigning each to an instance attribute:

```python
class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
```

**Step 3 — add class attributes**, only for values every instance should share:

```python
class BankAccount:
    bank_name = "First National"   # class attribute

    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
```

**Step 4 — define methods**, always with `self` first:

```python
class BankAccount:
    bank_name = "First National"

    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def describe(self):
        return f"{self.owner_name}'s account at {self.bank_name}: {self.balance}"
```

Now use the finished class:

```python
account = BankAccount("Priya Nair", 500)
account.deposit(150)
account.withdraw(80)
print(account.describe())
# Priya Nair's account at First National: 570
```

Trace it step by step. `BankAccount("Priya Nair", 500)` allocates a blank object, calls `__init__` with that object bound to `self`, and sets `owner_name` and `balance` as instance attributes in order. `account.deposit(150)` looks up `deposit` on the class, binds `account` as `self`, and runs `self.balance = self.balance + amount` — reading `500`, adding `150`, writing `650` back into the same attribute. `account.withdraw(80)` repeats the pattern: reads `650`, writes back `570`. `account.describe()` reads two instance attributes (`owner_name`, `balance`) and one class attribute (`bank_name`), formatting all three into a single f-string — the same read-and-format shape as `Task.describe` above [1][3].

Watch the failure mode this prevents. If `deposit` were written `def deposit(amount):` — forgetting `self` — then `account.deposit(150)` raises a `TypeError`: Python still passes `account` in automatically as the first positional argument, so now `account` and `150` are both competing to fill the single parameter `amount`. Forgetting `self` is the single most common beginner mistake in Python OOP [1].

## In Practice

The state-in-`__init__`, behavior-in-methods, `self`-ties-them-together shape shows up everywhere real Python code models something with a lifecycle:

- **Account models** (web apps): instance attributes like `username`, `email`, `is_active`, `login_count`, with methods like `deactivate()` and `record_login()` that mutate that state through `self` [1][2].
- **Game entities**: a `Player` with `health` and `score` as instance attributes, so two players in the same game hold completely independent values — the same independence `first_task` and `second_task` demonstrated.
- **Inventory records**: a `Product` with `sku`, `price`, and `quantity_in_stock`, and methods like `restock()` and `sell()` — and no class attributes at all, since every product's values genuinely vary per instance. Not every class needs a class attribute.

Best practices to carry forward:

- **Initialize every attribute inside `__init__`, even ones that start at `False` or `0`.** An attribute only set by *some* methods doesn't exist until that method runs — reading it earlier raises `AttributeError`.
- **Reach for a class attribute only when a value truly shouldn't vary per instance.** When unsure, make it an instance attribute; it's easy to promote later, hard to untangle instances that accidentally share mutable state.
- **Never forget `self`** as a method's first parameter — omitting it produces confusing `TypeError`s about argument counts.
- **Keep `__init__` about setup, not heavy computation.**
- **Prefer required positional parameters** over reaching for default values you haven't formally learned yet — a required parameter forces every caller to make an explicit choice, which builds the habit of thinking through each instance's state deliberately.
- **Name instance attributes after what they represent** (`self.done`, `self.is_active`) rather than how they're stored (`self.flag1`) — costs nothing and saves every future reader a trip back to `__init__`.

## Key Takeaways

- An abstract data type describes a thing by its state and behavior together; a Python class is how you implement that idea [1].
- A class is a blueprint; an object/instance is a specific thing built from that blueprint, with its own independent state.
- `__init__` is the constructor — it runs automatically on creation and sets up instance attributes (`self.attribute = value`); class attributes, defined in the class body, are shared defaults across all instances until an instance overrides one locally.
- Methods are functions defined inside a class; `self` is how a method refers to the specific object it was called on, and Python supplies it automatically at the call site.

## References

[1] Python Software Foundation. "9. Classes." *The Python Tutorial*. https://docs.python.org/3/tutorial/classes.html

[2] Real Python. "Object-Oriented Programming (OOP) in Python 3." https://realpython.com/python3-object-oriented-programming/

[3] Real Python. "Python Classes: The Power of Object-Oriented Programming." https://realpython.com/python-classes/
