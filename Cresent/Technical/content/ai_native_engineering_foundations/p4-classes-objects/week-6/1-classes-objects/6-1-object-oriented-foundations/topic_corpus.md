---
topic_id: 6.1
title: Object-Oriented Foundations
position_in_module: 1
generated_at: 2026-07-14T00:00:00Z
resource_count: 3
---

# 1. Object-Oriented Foundations — Topic Corpus

## 2. Prerequisites

This topic builds directly on:
- **1.1 The Python Environment** — the interpreter, the runtime, and `print()`, which you'll use to inspect objects as you build them.
- **1.2 Variables, Identifiers & Types** — variables, assignment, identifier naming rules (snake_case), `type()`, and dynamic typing. A class attribute or instance attribute is still just a variable; you're only changing *where it lives*.
- **1.4 Statements, Conversion & Output** — f-strings and the introductory syntax for type hints, both of which show up in constructor and method signatures below.

## 3. Learning Objectives

By the end of this topic, you should be able to:
- Explain what an abstract data type (ADT) is and why bundling state with behaviour is a useful way to model a real-world thing in code.
- Distinguish a **class** (a blueprint) from an **object**/**instance** (a specific thing built from that blueprint), and create instances from a class.
- Write a constructor (`__init__`) that initializes instance attributes, and explain the difference between an instance attribute and a class attribute.
- Define instance methods, correctly use the `self` parameter, and call methods on an object.

## 4. Introduction

Every program so far has kept data and the logic that acts on it as two separate things — a variable and the statements that operate on it. That works for small scripts, but it falls apart once you're tracking several related pieces of information about the same thing (a task's name, priority, and done status) alongside a growing pile of logic that needs all three at once.

Object-oriented programming (OOP) is a way of packaging state (data) and behaviour (the logic that acts on that data) together into a single unit. Instead of a task being three loose variables (`task_name`, `task_priority`, `task_done`) passed around between functions, it becomes one `Task` object that knows its own name, priority, and completion status — and knows how to mark itself complete. This is the foundation everything else in this course sits on: inheritance, encapsulation, operator overloading, and dataclasses are all refinements of the idea you'll meet here first.

This topic introduces the vocabulary and mechanics you need before any of that: what a class is, what an object is, how an object gets its initial state, and how it exposes behaviour through methods.

## 5. Core Concepts

### 5.1 Abstract Data Types: Thinking in Objects

An **abstract data type (ADT)** is a way of describing a "thing" by *what it is and what it can do*, without worrying yet about how that's implemented in memory. A `Task` is an ADT if you can say: "a Task has a name, a priority, and a done/not-done status (its **state**), and it can be marked complete (its **behaviour**)." Notice that description mentions nothing about strings, booleans, or functions — those are implementation details. The ADT is the concept; the class is how Python lets you implement that concept [1].

Before you had classes, you'd model a Task with three loose variables and a function:

```python
task_name = "Write topic corpus"
task_priority = "normal"
task_done = False

def mark_complete(done):
    return True

task_done = mark_complete(task_done)
print(task_name, task_priority, task_done)
```

This works for one task. It falls apart the moment you have several: `task_name_2`, `task_priority_2`, `task_done_2`, and nothing in the language stops you from writing `mark_complete(task_priority)` by mistake and quietly corrupting a task's priority instead of its completion flag. Nothing ties `task_name` to `task_priority` to `task_done` — they're just three variables that happen to sit near each other in your source file. The official Python tutorial frames the class mechanism as exactly the fix for this: a way to bundle data and the functions that operate on it into one object, so the association between them is enforced by the language itself rather than by the programmer's memory [1].

This matters because a class is really two things wearing one name: a **contract** (what attributes and methods you can rely on any instance having) and an **implementation** (how those attributes are stored and those methods are written). Two different `Task` implementations could store `priority` as a string today and, later, as some other representation entirely — as long as `t1.priority` still means the same thing to code that calls it, nothing outside the class needs to know the difference. That separation between "what it does" and "how it does it" is the entire reason ADT thinking is worth the mental shift [1].

Bundling state and behaviour together is not unique to tasks. A `Person` is an equally good ADT: a person has a name, an age, and an email address (state), and can introduce themselves or have a birthday (behaviour). Whatever "thing" you're modeling, the same question applies: what does it know about itself, and what can it do? You'll build both a `Task` class and a `Person` class through the rest of this topic, side by side, so you can see the same mechanics apply regardless of what the object represents [2].

### 5.2 Classes and Objects: Class vs Instance

A **class** is a blueprint. It defines what attributes (state) and methods (behaviour) every object built from it will have — but a class by itself is not a "thing" you can use; it's the template. Python's data model treats a class itself as an object too (you can inspect it, pass it around), but for now think of it purely as the plan [1].

An **object**, also called an **instance**, is a specific thing created from that blueprint, with its own actual values. You can create as many instances of one class as you like, and each one holds its own independent state.

```python
class Task:
    pass

first_task = Task()
second_task = Task()

print(type(first_task))            # <class '__main__.Task'>
print(first_task is second_task)   # False -- two separate objects
```

Here `Task` is the class. `first_task` and `second_task` are two separate instances of that class — same blueprint, two independent objects. This mirrors `type()` from 1.2: calling `type(first_task)` reports the class the object was built from, the same way `type(3.14)` reports `float` [1].

Walk through what actually happens on the line `first_task = Task()`. Python (1) looks up the name `Task` and finds the class object you defined, (2) calls it like a function, which allocates a brand-new, empty object in memory, (3) since this `Task` has no `__init__` yet, no further setup happens, and (4) the reference to that new object is handed back and bound to the name `first_task`. The second call, `Task()`, repeats the same four steps and produces a second, distinct object — which is exactly why `first_task is second_task` prints `False`: `is` compares object identity, and these are two different objects sitting at two different memory addresses, even though they came from the identical blueprint [1].

The same mechanics apply to any class, not just `Task`. Define an empty `Person` class the same way, and the pattern repeats exactly:

```python
class Person:
    pass

alice = Person()
bob = Person()

print(type(alice))               # <class '__main__.Person'>
print(alice is bob)              # False
print(type(alice) is type(bob))  # True -- same class, different objects
```

`alice` and `bob` are both `Person` instances — `type(alice) is type(bob)` confirms they were built from the same blueprint — but `alice is bob` is `False` because they are two separate objects, exactly as `first_task` and `second_task` were. This is the pattern to internalize before adding any state: *one class, many independent instances*.

By convention, class names use `PascalCase` (`Task`, `Person`, not `task`, `person`), while instance names follow the `snake_case` rule you already know from 1.2. This isn't enforced by Python — it's a convention every professional codebase follows so that a name alone tells you whether you're looking at a blueprint or a thing built from one [2].

### 5.3 The Constructor: `__init__`, Instance vs Class Attributes

An empty class isn't useful — a `Task` with no name isn't a task, and a `Person` with no name isn't a person. The **constructor** is a special method, `__init__`, that Python calls automatically every time you create a new instance. Its job is to set up that instance's starting state [1].

```python
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.done = False

first_task = Task("Write topic corpus", "normal")
second_task = Task("Review pull request", "high")

print(first_task.name, first_task.priority, first_task.done)
# Write topic corpus normal False
print(second_task.name, second_task.priority)
# Review pull request high
```

Notice `priority` has no default value — every `Task()` call must supply both `name` and `priority`, in that order, as plain positional arguments. That's a deliberate constraint at this stage of the course: Python's default-parameter-value syntax (`priority="normal"`) is a feature of functions you haven't met yet, so every constructor here takes its parameters as required, positional arguments, the same way you already call `print()` and `type()` with positional arguments.

Trace exactly what happens on `first_task = Task("Write topic corpus", "normal")`: (1) Python creates a new, blank `Task` object, (2) it calls `__init__`, automatically passing that new object in as `self`, plus your two arguments as `name` and `priority`, (3) the first line inside, `self.name = name`, creates a brand-new attribute called `name` on *this* object and stores the string in it, (4) `self.priority = priority` does the same for `priority`, (5) `self.done = False` creates a third attribute, `done`, and sets it to the boolean `False` — note this one isn't a parameter at all, it's just always `False` for a brand-new task, and (6) once `__init__` finishes, the fully-initialized object is handed back and bound to `first_task`. Run the same six steps for `second_task = Task("Review pull request", "high")` and you get a second, completely independent object with its own `name`, `priority`, and `done`.

`self.name = name` creates an **instance attribute**: a variable that belongs to *this specific object*, not to the class in general. `first_task.name` and `second_task.name` are two different strings living in two different objects, exactly as you'd expect from the "each instance holds its own state" idea in 5.2. The Python tutorial calls these "data attributes" and notes they spring into existence the moment they're assigned inside `__init__` — there's no separate declaration step like you might expect from other languages [1].

A **class attribute**, by contrast, is defined directly in the class body (not inside `__init__`) and is shared by every instance unless an individual instance overrides it [1][3]:

```python
class Task:
    category = "general"   # class attribute -- shared by every Task

    def __init__(self, name, priority):
        self.name = name          # instance attribute
        self.priority = priority  # instance attribute
        self.done = False         # instance attribute

t1 = Task("Write topic corpus", "normal")
t2 = Task("Review pull request", "high")
print(t1.category, t2.category)   # general general
```

Watch what happens if you change the class attribute through the class itself, versus through one instance:

```python
Task.category = "work"
print(t1.category, t2.category)   # work work -- both changed, neither has its own

t1.category = "personal"
print(t1.category, t2.category)   # personal work -- t1 now has its own copy
```

`Task.category = "work"` changes the shared value, so every instance that doesn't have its own `category` attribute sees the new value — `t1` and `t2` both read `work`. But `t1.category = "personal"` does something different: it creates a *new instance attribute* on `t1` alone, called `category`, which now shadows the class attribute for `t1` only. `t2` still has no instance attribute named `category`, so it keeps reading the shared class value. This is the exact mechanic Real Python's class-mechanics deep dive flags as the most common source of confusion for people new to classes: assigning through an instance never changes the class attribute, it just creates (or overwrites) an attribute local to that one instance [3].

Use class attributes for values that are genuinely the same across every instance (a default category, a shared configuration constant). Use instance attributes — set inside `__init__` via `self.attribute = value` — for anything that varies per object, which in practice is almost everything you'll model.

The same distinction applies immediately to `Person`. Every person shares the fact that they're a member of the same species, but each person has their own name, age, and email:

```python
class Person:
    species = "Homo sapiens"   # class attribute -- true of every Person

    def __init__(self, name, age, email):
        self.name = name    # instance attribute
        self.age = age      # instance attribute
        self.email = email  # instance attribute

alice = Person("Alice Chen", 29, "alice@example.com")
bob = Person("Bob Diaz", 34, "bob@example.com")

print(alice.species, bob.species)   # Homo sapiens Homo sapiens
print(alice.name, bob.name)         # Alice Chen Bob Diaz
```

`species` is defined once, in the class body, and both `alice` and `bob` read the same value from it — exactly like `category` on `Task`. `name`, `age`, and `email`, by contrast, are set fresh inside `__init__` for every `Person`, so `alice` and `bob` each have their own independent copies. That's the general rule, restated once more with a second, unrelated class: state that is genuinely universal belongs on the class; state that describes one specific object belongs on the instance, created inside `__init__` [1][3].

### 5.4 Methods: Defining Methods, the `self` Parameter

A **method** is a function defined inside a class body. It's how an object exposes behaviour — the "what it can do" half of the ADT from 5.1 [1].

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

`describe` deliberately reports the raw boolean value of `self.done` rather than branching on it — turning a boolean into one string versus another based on a condition is a job for the Conditionals topic later in this course, so `describe` here just interpolates `self.done` directly into the f-string (from 1.4) and lets Python's own string conversion (`True`/`False`) do the work.

Every method you define takes `self` as its first parameter. `self` is how the method refers back to the specific object it was called on — it's what lets `self.done = True` inside `mark_complete` change *this* task's `done` attribute and not some other task's. When you write `t1.mark_complete()`, Python automatically passes `t1` in as `self`; you never pass it explicitly at the call site. The official tutorial is explicit that this is a naming convention, not a keyword — you could technically call the parameter anything, but every Python codebase you'll ever read uses `self`, so you should too [1].

Trace `t1.mark_complete()` the same careful way you traced construction earlier. Python (1) looks up `mark_complete` — not on `t1` itself (instances don't carry their own copy of each method; only their own attributes), but on `t1`'s class, `Task`, (2) finds the function defined there, (3) automatically *binds* it to `t1`, meaning `t1` is slotted in as the `self` argument, and (4) executes the body, `self.done = True`, which — because `self` is `t1` — sets the `done` attribute on `t1` specifically. Real Python's walkthrough of class mechanics describes this lookup-then-bind step as exactly what separates a plain function from a method: the object you called it on is threaded through automatically as the first argument [3].

Notice `describe` reads two instance attributes (`self.name`, `self.priority`) plus the mutated `self.done`, and builds one f-string from all three at once — this is exactly the "state and behaviour bundled together" payoff from 5.1. Neither `mark_complete` nor `describe` needs any arguments describing *which* task to act on, because `self` already carries that.

`Person` needs its own behaviour too. A person can introduce themselves, and a person's age changes over time:

```python
class Person:
    species = "Homo sapiens"

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def greet(self):
        return f"Hi, I'm {self.name}, and my email is {self.email}."

    def have_birthday(self):
        self.age = self.age + 1

alice = Person("Alice Chen", 29, "alice@example.com")
print(alice.greet())          # Hi, I'm Alice Chen, and my email is alice@example.com.
alice.have_birthday()
print(alice.age)              # 30
```

Compare the four methods you've now written across two classes. `mark_complete` and `have_birthday` both *mutate* state — they reassign an instance attribute and return nothing useful. `describe` and `greet` both *read* state and *format* it into a returned string, changing nothing. Every method you write from here on will be a variation on one of these two shapes: change something about the object, or report something about the object, using `self` to reach the object's own attributes either way [1][3].

It helps to place `Task`'s and `Person`'s construction side by side and trace both in identical, mechanical terms. `Task("Write topic corpus", "normal")` allocates one blank object, binds it as `self` inside `Task.__init__`, and creates exactly three instance attributes on it, in the order the assignments appear: `name`, then `priority`, then `done` — each one a separate entry in that object's own attribute storage, invisible to any other `Task`. `Person("Alice Chen", 29, "alice@example.com")` runs the identical four-step sequence traced in 5.3, only with a different `__init__` body: one blank object, `self` bound to it, and three instance attributes created in order — `name`, then `age`, then `email`. Both constructions do exactly the same *kind* of work — allocate, bind `self`, assign attributes in source order, hand back the finished object — and neither the interpreter nor `__init__` itself needs to know or care which class supplied the blueprint. That's why a `t1.name` lookup and an `alice.name` lookup both succeed in finding an attribute called `name`, yet resolve to two entirely separate values stored on two entirely separate objects: attribute lookup always starts at the specific instance you called it on, never at some object built from a different class, however similarly the two classes happen to be written [1].

## 6. Implementation

Building a class generally follows the same four steps, in this order. Walking through them once, in full, for a slightly larger example than `Task` or `Person` alone, ties every piece from Section 5 together.

**Step 1 — name the class.** Use `class ClassName:` with `PascalCase`, matching the convention every Python style guide and the official tutorial's own examples use [1][2]:

```python
class BankAccount:
    ...
```

**Step 2 — write `__init__`.** Decide what values every instance absolutely needs at creation time, and take them as required positional parameters (no defaults, per the constraint explained in 5.3), then assign each one to an instance attribute:

```python
class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
```

Calling `BankAccount("Priya Nair", 500)` runs the same four-step construction sequence traced in 5.3: a blank object is created, `__init__` is invoked with that object bound to `self`, both assignments run in order, and the fully-set-up object is handed back. The assignment order matters for readability, not correctness — Python executes `self.owner_name = owner_name` before `self.balance = balance` simply because that's the order they're written, and each line's attribute exists the instant it's assigned, exactly as the official tutorial describes for instance attributes generally [1].

**Step 3 — add class attributes, if any.** Only for values every instance should share by default:

```python
class BankAccount:
    bank_name = "First National"   # class attribute -- shared by every account

    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
```

Every `BankAccount` instance reads the same `bank_name` unless one of them is given its own instance attribute of that name later — the same shadowing behaviour demonstrated with `Task.category` in 5.3 applies here without any change in mechanics [1][3].

**Step 4 — define methods.** Each behaviour the ADT needs becomes a method, always with `self` first, reading or writing `self.attribute` as needed:

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

Put all four steps together and use the finished class:

```python
account = BankAccount("Priya Nair", 500)
account.deposit(150)
account.withdraw(80)
print(account.describe())
# Priya Nair's account at First National: 570
```

Trace this the same disciplined way as before. `BankAccount("Priya Nair", 500)` constructs the object and sets `owner_name` and `balance` as instance attributes, exactly as Step 2 defined. `account.deposit(150)` looks up `deposit` on the class, binds `account` as `self`, and runs `self.balance = self.balance + amount` — reading the current `balance` (500), adding `150`, and writing `650` back into the same attribute. `account.withdraw(80)` repeats the pattern, reading `650` and writing back `570`. `account.describe()` then reads three attributes — two instance (`owner_name`, `balance`), one class (`bank_name`) — and formats them into a single string with an f-string, the same read-and-format shape as `Task.describe` and `Person.greet` in 5.4 [1][3].

It's worth seeing the failure mode this prevents, too. If Step 4's `deposit` method forgot `self` as its first parameter — written as `def deposit(amount): ...` instead of `def deposit(self, amount): ...` — calling `account.deposit(150)` would raise a `TypeError` about too many arguments, because Python still tries to pass `account` in automatically as the first positional argument, and now there are two values (`account` and `150`) trying to fill one parameter (`amount`). This is precisely the mistake Section 8's Best Practices calls the single most common beginner error in Python OOP [1].

The four steps don't have to happen in exactly this textual order inside the class body — Python reads the whole class body once, top to bottom, before any instance is created, so a class attribute defined after `__init__` in the source is just as visible as one defined before it. The order shown above (name, constructor, class attributes, methods) is a *readability* convention, not a technical requirement [1].

To use any class you build this way, the pattern is always the same: call `ClassName(...)` to construct an instance (this triggers `__init__` automatically, per Step 2's mechanics), and call `instance.method(...)` to invoke behaviour on that specific object (per Step 4's mechanics, with `self` bound automatically as described in 5.4) [1].

## 7. Real-World Patterns

This is exactly the shape you'll use in the week's lab work: a `Task` class with `name`, `priority`, and `done` state, plus a `mark_complete` method, is a small but honest example of how real systems model entities. A `RegulatoryTask` later in the module will extend this same `Task` blueprint rather than duplicating it — that's inheritance, coming next, but it only works because `Task` itself is built the way described here: state in `__init__`, behaviour in methods, `self` tying them together.

Outside the classroom, this exact pattern — attributes set in `__init__`, behaviour exposed through methods, `self` threading state through every call — is how production Python code models almost everything with a lifecycle. Three concrete examples:

**A web application's account model.** Every framework that handles user accounts ends up with something shaped like this, even before you add a database behind it:

```python
class Account:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True
        self.login_count = 0

    def deactivate(self):
        self.is_active = False

    def change_email(self, new_email):
        self.email = new_email

    def record_login(self):
        self.login_count = self.login_count + 1
```

`Account` has exactly the shape every class in this topic has had: instance attributes (`username`, `email`, `is_active`, `login_count`) set in `__init__`, and methods (`deactivate`, `change_email`, `record_login`) that mutate that state through `self`. `record_login` in particular shows a pattern you'll use constantly once you're modeling anything with a history: a counter, initialized once at `0` inside `__init__`, incremented by exactly one instance attribute assignment every time the behaviour it tracks happens — the same `self.attribute = self.attribute + 1` shape `Person.have_birthday` used for `age` in 5.4. A real account system adds validation, persistence to a database, and password handling — but the core object at the center is this same class-with-`__init__`-and-methods shape [1][2].

**A game's player entity.** Games track a moving, changing set of values per player — health, score, position — which is exactly the "state that varies per instance" case instance attributes exist for:

```python
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.score = 0

    def take_damage(self, amount):
        self.health = self.health - amount

    def add_score(self, points):
        self.score = self.score + points
```

Two `Player` instances in the same game — one for each of two people playing — hold completely independent `health` and `score`, the same way `first_task` and `second_task` held independent `name` and `priority` back in 5.2. Nothing about `Player` is conceptually new; it's `Task` and `BankAccount`'s exact shape applied to a different domain [1][3].

**An inventory record in a small business system.** Products, orders, and line items in e-commerce and inventory software are almost always modeled the same way:

```python
class Product:
    def __init__(self, sku, name, price, quantity_in_stock):
        self.sku = sku
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def restock(self, amount):
        self.quantity_in_stock = self.quantity_in_stock + amount

    def sell(self, amount):
        self.quantity_in_stock = self.quantity_in_stock - amount
```

`Product` again follows the same four-step recipe from Section 6: instance attributes for everything that varies per product (`sku`, `name`, `price`, `quantity_in_stock`), methods (`restock`, `sell`) that read and write that state through `self`, and — because every `Product` needs its own SKU, name, price, and stock count — no class attributes at all here, which is a perfectly normal outcome; not every class needs one.

Across all three examples — `Account`, `Player`, `Product` — and the `Task`, `Person`, and `BankAccount` classes built earlier in this topic, the pattern never changes: identify the state an instance of this thing needs, set it up in `__init__`, and expose whatever behaviour the thing needs as methods that read and write that state through `self`. Real Python's introduction to OOP in Python makes the same point about scale: this is the shape you reach for whether you're modeling a five-line script's data or a production system's core domain objects [2][3].

## 8. Best Practices

- **Always initialize every attribute the object needs inside `__init__`.** An object with attributes that only sometimes exist (because they were only set by *some* methods) is a common source of bugs. For example:

  ```python
  class Task:
      def __init__(self, name, priority):
          self.name = name
          self.priority = priority
          # done not set here

      def mark_complete(self):
          self.done = True  # only exists after this runs

  t1 = Task("Write topic corpus", "normal")
  print(t1.done)   # AttributeError: 'Task' object has no attribute 'done'
  ```

  `t1.done` doesn't exist until `mark_complete()` has actually been called at least once — read it any earlier and Python raises `AttributeError`, exactly the tutorial's point about instance attributes only existing once assigned [1]. Set every attribute the object could ever need inside `__init__`, even if its starting value is just `False` or `0`, so every instance is fully formed the moment it's constructed.
- **Reach for a class attribute only when the value truly shouldn't vary per instance.** If you're unsure, make it an instance attribute — it's easy to promote a value to shared later, and much harder to untangle instances that accidentally share mutable state through a class attribute.
- **Never forget `self`.** Leaving it off a method definition, or forgetting to use it to read/write attributes inside a method, is the single most common beginner mistake in Python OOP — it produces confusing `TypeError`s about argument counts, as traced in Section 6.
- **Keep `__init__` about setup, not computation.** If a value needs heavy logic to produce, compute it in a method or a helper — `__init__`'s job is to establish valid starting state, quickly.
- **Prefer required positional parameters until you've learned keyword and default arguments properly.** It's tempting to reach for `priority="normal"`-style defaults the moment you see them in someone else's code, but skipping past *why* a parameter needs a default (and what happens when a caller omits it) tends to produce constructors that silently succeed with wrong values instead of failing loudly. A required positional parameter forces every caller to make an explicit choice for every value the object needs — exactly what you want while you're still building the habit of thinking through each instance's state deliberately, before functions (3.1) introduce a more flexible way to handle optional values.
- **Don't use a class attribute to fake a default parameter value.** Because constructors in this course take required positional parameters only (5.3), it can be tempting to write something like a class-level `priority = "normal"` so a `Task` always "starts out" with a value, and then rely on `__init__` never overriding it for some instances. That reintroduces the exact shared-state confusion demonstrated with `Task.category` in 5.3: every instance that never receives its own `priority` instance attribute would silently read the one shared class value. If a value must be supplied per instance, take it as a required constructor parameter; reserve class attributes for values that are genuinely constant across every instance, the way `BankAccount.bank_name` and `Account`'s shared framework-level defaults would be, not for values you merely wish had a fallback.
- **Name instance attributes after what they represent, not how they happen to be stored.** `self.done`, `self.is_active`, and `self.quantity_in_stock` each state plainly what they hold; a name like `self.flag1` or `self.val` forces every reader of the class to go find the exact line inside `__init__` just to learn what the attribute even means. Every class built across Sections 5 through 7 — `Task`, `Person`, `BankAccount`, `Account`, `Player`, `Product` — follows this rule without a single exception, and it costs nothing to keep following it.

## 9. Hands-On Exercise

Define a `Task` class with instance attributes `name`, `priority`, and `done`, initialized in `__init__`. Make `name` and `priority` required positional parameters (no default values — every `Task(...)` call must supply both explicitly), and set `done` to `False` unconditionally inside `__init__` since a brand-new task is never already complete. Add two methods: `mark_complete()`, which sets `done` to `True`, and `describe()`, which returns an f-string reporting the task's name, priority, and `done` value (interpolate `self.done` directly, the same way Section 5.4's `Task.describe` does — no conditional needed).

Create two `Task` instances with different names and priorities, mark one complete, and print both `describe()` results to confirm each instance holds independent state — the second task's `describe()` output should still show `done=False` even after you call `mark_complete()` on the first.

For extra practice, repeat the same exercise with the `Person` class from Section 5: give it `name`, `age`, and `email` as required positional constructor parameters, add a `have_birthday()` method that increments `age` by one, and a `greet()` method that returns an introduction string. Create two `Person` instances, call `have_birthday()` on only one, and print both instances' `age` values to confirm the same independent-state guarantee holds regardless of which class you're working with.

## 10. Key Takeaways

- An abstract data type describes a thing by its state and behaviour together; a Python class is how you implement that idea.
- A class is a blueprint; an object/instance is a specific thing built from that blueprint, with its own independent state.
- `__init__` is the constructor — it runs automatically on creation and is where instance attributes (`self.attribute = value`) are set up; class attributes, defined in the class body, are shared defaults across all instances.
- Methods are functions defined inside a class; the `self` parameter is how a method refers to the specific object it was called on, and Python supplies it automatically at the call site.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
