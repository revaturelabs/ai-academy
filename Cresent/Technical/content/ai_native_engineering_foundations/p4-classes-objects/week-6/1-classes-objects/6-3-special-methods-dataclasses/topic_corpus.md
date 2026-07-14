---
topic_id: 6.3
title: Special Methods & Dataclasses
position_in_module: 3
generated_at: 2026-07-14T00:00:00Z
resource_count: 3
---

# 1. Special Methods & Dataclasses — Topic Corpus

## 2. Prerequisites

This topic builds directly on **6.1 Object-Oriented Foundations** and **6.2 Inheritance & Encapsulation**, and reuses their vocabulary and running examples without redefining them:
- **Class vs instance/object, `__init__`, instance vs class attributes, methods and `self`** — from 6.1.
- **Inheritance (`super()`, MRO), single- and double-underscore naming conventions** — from 6.2.
- **`is` for identity comparison** and **`type()`/`isinstance()`** — both used in 6.1 and 6.2 to distinguish "same object" from "same kind of object."
- The `Task` class (`name`, `priority`, `done`, `mark_complete()`, `describe()`), the `RegulatoryTask(Task)` subclass, and the `Person` → `Student` → `GraduateStudent` hierarchy from 6.1 and 6.2 are the running examples this topic extends. 6.2's closing paragraph explicitly promised this moment: a way to control how objects print and compare, starting from the `describe()`-style methods already built, plus a shortcut for classes that are mostly just structured data.

## 3. Learning Objectives

By the end of this topic, you should be able to:
- Explain the difference between `__repr__` and `__str__`, and implement both on a class so that `print()`, `str()`, and the interactive interpreter each show the string you intend.
- Implement `__eq__` so that `==` compares two instances by their attribute values instead of falling back to Python's default identity comparison.
- Apply the `@dataclass` decorator to a class made mostly of attributes, and explain which methods it generates for you.
- Declare dataclass fields with type annotations, including fields with default values, and explain the ordering rule those defaults impose.
- Organize a class into its own module and import it from another file.

## 4. Introduction

Every `describe()` method built in 6.1 and 6.2 exists because Python doesn't automatically know how to turn a `Task` or a `Person` into a readable string, or how to compare two of them meaningfully:

```python
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.done = False

t1 = Task("Write topic corpus", "normal")
t2 = Task("Write topic corpus", "normal")
print(t1)           # <__main__.Task object at 0x7f2b1c0a4d90>
print(t1 == t2)      # False -- same data, different objects
```

`print(t1)` gives a memory address, not the task's actual state. `t1 == t2` is `False` even though every attribute matches, because Python has no idea, on its own, what "equal" should mean for a `Task` — it falls back to the same identity check `is` performs, which 6.1 and 6.2 already used deliberately (`first_task is second_task`, `alice is bob`) to show that two instances are separate objects. That fallback is *correct behaviour*, not a bug: you have to tell Python what "equal" means for your class.

This topic is about telling it — formally, through the small set of special methods Python's own printing and comparison machinery calls automatically, instead of through a hand-rolled `describe()` you have to remember to call yourself. It then goes one step further: once a class settles into being mostly a bundle of attributes with predictable `__init__`, `__repr__`, and `__eq__` methods — exactly the shape `Task` and `Person` are trending toward — Python offers `@dataclass`, a decorator that generates all three for you from a short list of field declarations. The topic closes with the last piece of this module's outline: once you have more than one or two classes, where do you actually put them, and how does other code reach them?

## 5. Core Concepts

### 5.1 Special Methods and the Data Model

A **special method** (also called a **dunder method**, for "double underscore") is a method whose name begins and ends with two underscores — `__init__`, `__str__`, `__repr__`, `__eq__`, and dozens more — that Python calls *implicitly*, on your behalf, in response to some built-in operation. You've already met one: `__init__` is called implicitly the instant you write `Task(...)`; you never call `t1.__init__(...)` yourself. The collection of all such methods, and the rules for when Python calls each one, is documented as Python's **data model** [1]. This topic covers three more of them — `__repr__`, `__str__`, and `__eq__` — chosen specifically because `print()`, `str()`, f-strings, and `==` all consult them automatically.

The pattern is always the same: you write a method with the exact special name Python expects, and some built-in syntax or function — `print()`, `==`, `str()` — looks for that method on the object's class and calls it for you, instead of you calling it directly. This is precisely why `t1.mark_complete()` in 6.1 is *not* a special method (you call it explicitly, by name) while the methods in this topic *are* — nothing in your code will ever say `t1.__str__()` or `t1.__eq__(t2)` directly; `print(t1)` and `t1 == t2` trigger them instead [1].

### 5.2 `__repr__` and `__str__`: Controlling How an Object Prints

Every Python object has some string representation available even if you write no code at all — that's where `<__main__.Task object at 0x7f2b1c0a4d90>` came from in the Introduction. That default comes from `object`, the base class every class ultimately inherits from (the same `object` that appeared at the end of every `__mro__` tuple in 6.2), and it is deliberately unhelpful: an address in memory tells you an object exists and what class built it, nothing about its state [1].

**`__repr__`** is the special method responsible for an object's *unambiguous, developer-facing* representation — the string meant for someone debugging, logging, or inspecting the object at the interactive interpreter. The convention, described in the data model and reinforced by Real Python's comparison of the two methods, is to make `__repr__` look like the exact code that would recreate the object: `ClassName(field1=value1, field2=value2, ...)` [1][3].

```python
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.done = False

    def __repr__(self):
        return f"Task(name={self.name!r}, priority={self.priority!r}, done={self.done!r})"

t1 = Task("Write topic corpus", "normal")
print(t1)
# Task(name='Write topic corpus', priority='normal', done=False)
```

Trace what changed. `print(t1)` still does exactly what it always did — it asks the object for a string and prints it — but now, because `Task` defines `__repr__`, Python finds that method instead of falling through to `object`'s default. The `!r` inside each `{self.name!r}` f-string placeholder is a **conversion flag**: it tells the f-string to call `repr()` on that specific value rather than `str()`, which is why the printed name shows quote marks (`'Write topic corpus'`) instead of the bare text — matching how you'd actually type that string as Python source code, exactly the "recreate the object" convention `__repr__` is meant to follow [1][3].

**`__str__`** is the special method responsible for an object's *human-readable*, user-facing representation — the string meant for someone who just wants to know what the object represents, not how to reconstruct it in code. `print()`, `str()`, and f-string interpolation (`f"{t1}"`) all prefer `__str__` over `__repr__` when both exist [1][3]:

```python
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.done = False

    def __repr__(self):
        return f"Task(name={self.name!r}, priority={self.priority!r}, done={self.done!r})"

    def __str__(self):
        return f"{self.name} ({self.priority}) - done={self.done}"

t1 = Task("Write topic corpus", "normal")
print(t1)          # Write topic corpus (normal) - done=False
print(repr(t1))    # Task(name='Write topic corpus', priority='normal', done=False)
```

Notice `__str__`'s body is exactly `Task.describe()`'s body from 6.1, moved into a special method with a special name. That's the whole point of this section: `describe()` worked, but it required every caller to remember to call `t1.describe()` by hand. `__str__` does the identical job automatically, the instant anyone writes `print(t1)`, `str(t1)`, or `f"{t1}"` — no explicit call needed anywhere.

There is one fallback rule worth tracing carefully, because it explains behaviour you'll see constantly once you start writing dataclasses in 5.4: `object`'s own default `__str__` is implemented to simply call `self.__repr__()`. So if a class defines `__repr__` but *not* `__str__`, `print()` still shows something useful — it falls through to the inherited `__str__`, which calls the class's own `__repr__` [1]. Only when a class defines both does `print()` prefer the more human-readable one. This is why, back in the first code sample of this section — `__repr__` only, no `__str__` yet — `print(t1)` already produced a sensible, non-default output before `__str__` was ever added.

The same two methods apply identically to `Person`, extending 6.1's `greet()`-based introduction with real print support:

```python
class Person:
    species = "Homo sapiens"

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r}, email={self.email!r})"

    def __str__(self):
        return f"{self.name}, age {self.age} ({self.email})"

alice = Person("Alice Chen", 29, "alice@example.com")
print(alice)         # Alice Chen, age 29 (alice@example.com)
print(repr(alice))   # Person(name='Alice Chen', age=29, email='alice@example.com')
```

### 5.3 `__eq__`: Value-Based Equality

By default, `==` between two instances of the same custom class behaves exactly like `is` — both check whether the two names refer to the *same object in memory*, not whether the two objects hold equal data. This is inherited from `object`, the same base class responsible for the default `__repr__` in 5.2 [1]:

```python
t1 = Task("Write topic corpus", "normal")
t2 = Task("Write topic corpus", "normal")
print(t1 == t2)     # False -- same data, different objects
print(t1 == t1)     # True  -- same object
```

`t1 == t2` is `False` for the identical reason `first_task is second_task` was `False` in 6.1: two separate `Task()` calls allocate two separate objects, and neither identity nor the inherited default equality check cares that their attributes happen to match.

**`__eq__`** is the special method `==` calls implicitly, and defining it lets you decide what "equal" actually means for your class — typically: same class, and every attribute that matters holds the same value [1]:

```python
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.done = False

    def __repr__(self):
        return f"Task(name={self.name!r}, priority={self.priority!r}, done={self.done!r})"

    def __str__(self):
        return f"{self.name} ({self.priority}) - done={self.done}"

    def __eq__(self, other):
        return (isinstance(other, Task)
                and self.name == other.name
                and self.priority == other.priority
                and self.done == other.done)

t1 = Task("Write topic corpus", "normal")
t2 = Task("Write topic corpus", "normal")
print(t1 == t2)     # True -- same class, same attribute values
t1.mark_complete = lambda: None  # not relevant to equality; describe() only reads attributes
print(t1 == t2)
```

Trace `t1 == t2` carefully. Python looks up `__eq__` on `t1`'s class, `Task`, finds the method just written, and calls it with `self` bound to `t1` and `other` bound to `t2` — the same lookup-then-bind mechanism 6.1 traced for `mark_complete()`. The body is a single boolean expression, four operands chained with `and` (from 1.3), and `and` short-circuits: it evaluates left to right and stops the instant an operand is `False`, without evaluating anything after it. `isinstance(other, Task)` comes first for exactly this reason — if `other` isn't a `Task` at all (a plain string, a number, an unrelated object), that first operand is `False`, `and` stops right there, and the expression returns `False` without ever touching `other.name`, which might not exist. `isinstance()` was introduced in 6.2 for exactly this kind of "is this usable as a `Task`?" check, and it applies here identically. Only once `other` is confirmed to be a `Task` do the remaining three operands run, comparing `name`, `priority`, and `done` in turn with plain `==` — the whole expression is `True` only if all four operands are `True` [1].

`RegulatoryTask`, inheriting from `Task`, needs its own `__eq__` if a regulation code should also factor into equality — inheritance gives `RegulatoryTask` `Task`'s `__eq__` automatically (the same method-lookup rule 6.2 traced for every other method), but that inherited version only ever compares `name`, `priority`, and `done`, never `regulation_code`, unless `RegulatoryTask` overrides it. Following 6.2's extension pattern with `super()`:

```python
class RegulatoryTask(Task):
    def __init__(self, name, priority, regulation_code):
        super().__init__(name, priority)
        self.regulation_code = regulation_code

    def __eq__(self, other):
        return (isinstance(other, RegulatoryTask)
                and super().__eq__(other)
                and self.regulation_code == other.regulation_code)
```

`isinstance(other, RegulatoryTask)` guards the whole expression first, exactly as it does for `Task` above, and thanks to the same short-circuit behaviour, `super().__eq__(other)` never runs against something that isn't even a `RegulatoryTask`. `super().__eq__(other)` then reuses `Task`'s comparison for the three attributes `RegulatoryTask` inherits, and the final `and` clause adds the one attribute that's new — the identical "extend, don't duplicate" idea 6.2 used for `describe()`, applied here to equality instead.

### 5.4 `@dataclass`: Reducing Boilerplate

Look back at everything `Task` now requires to behave well: `__init__` assigning three attributes, `__repr__` formatting those same three attributes one way, `__str__` formatting them another way, and `__eq__` comparing them all pairwise. Every one of those four methods does nothing but read or assign the same three names — `name`, `priority`, `done` — in a completely mechanical, predictable pattern. For a class that is mostly a bundle of attributes like this, writing all four by hand is repetitive, and repetitive code is exactly where typos and missed-attribute bugs creep in (forget to add `done` to `__eq__` after adding it to `__init__`, and equality quietly stops checking it).

The **`dataclasses`** module's **`@dataclass`** decorator solves this by generating `__init__`, `__repr__`, and `__eq__` for you, from a short, declarative list of **fields** — attribute names paired with type annotations, written directly in the class body instead of inside a hand-written `__init__` [2]:

```python
from dataclasses import dataclass

@dataclass
class Task:
    name: str
    priority: str
    done: bool = False
```

That is the entire class. Using it looks identical to using the hand-written version from 5.2 and 5.3:

```python
t1 = Task("Write topic corpus", "normal")
t2 = Task("Write topic corpus", "normal")

print(t1)              # Task(name='Write topic corpus', priority='normal', done=False)
print(t1 == t2)         # True
```

Trace what `@dataclass` actually built here. Each line inside the class body — `name: str`, `priority: str`, `done: bool = False` — is a **field declaration**: a name, a type annotation (the same type-hint syntax introduced in 1.4), and, optionally, a default value. From those three declarations, the decorator generates:
- An `__init__` that takes `name` and `priority` as required positional parameters (no default given, so every call must supply them, matching every constructor built since 6.1) and `done` as an optional parameter defaulting to `False` if the caller doesn't supply it — assigning all three to `self` in the order they're declared, exactly the way 6.1's hand-written `Task.__init__` did.
- A `__repr__` in the same `ClassName(field=value, ...)` shape built by hand in 5.2, listing every field in declaration order.
- An `__eq__` that checks the other object is the same dataclass type and compares every field, the same shape built by hand in 5.3 — with the "same fields, in order" logic generated instead of typed out [2].

Notice `done: bool = False` is the one place in this course where a **default value in a signature** is not only allowed but is the actual mechanism being taught: a dataclass field default is how you declare "this attribute has a sensible starting value that most callers won't need to override," and it's a property of the *field declaration*, not of an ordinary function or method parameter list. Every plain method and constructor built across 6.1, 6.2, and the rest of this topic still takes required positional parameters only, exactly as before — `@dataclass` field defaults are a distinct, dataclass-specific mechanism, not a general license to add default parameter values elsewhere [2].

That default comes with one firm ordering rule, and the official documentation is explicit about it: once a field has a default value, every field declared after it must also have a default value — a required field cannot follow an optional one [2]:

```python
@dataclass
class Task:
    name: str
    done: bool = False
    priority: str          # error: non-default field follows default field
```

The reason mirrors positional-versus-keyword argument rules you'll meet formally later: the generated `__init__` places every field in declaration order as a parameter, defaulted fields becoming optional parameters — and Python cannot allow a required (positional, no-default) parameter to appear after an optional one in the same signature, because there would be no way for a caller to skip the optional one and still supply the required one after it.

A dataclass is still an ordinary class underneath the decorator — you can add methods to it exactly as you would to any class from 6.1, and inheritance from 6.2 still works the same way:

```python
@dataclass
class Task:
    name: str
    priority: str
    done: bool = False

    def mark_complete(self):
        self.done = True
```

`mark_complete` here is not a field — it has no type annotation at the class level and isn't part of the generated `__init__`/`__repr__`/`__eq__` — it's a plain method, defined and called exactly as in 6.1. `@dataclass` only changes how `__init__`, `__repr__`, and `__eq__` get built; it doesn't restrict what else the class can contain [2].

One nuance is worth stating plainly, because it explains behaviour that otherwise looks inconsistent with 5.2: `@dataclass`, by default, generates `__repr__` and `__eq__`, but **not `__str__`** [2]. `print(t1)` on a plain dataclass instance therefore shows the same output as `repr(t1)` — not because `@dataclass` wrote a `__str__` that happens to match, but because of the exact fallback rule from 5.2: with no `__str__` defined, `object`'s inherited default `__str__` calls `self.__repr__()`, and the generated `__repr__` is what actually gets shown. If a dataclass genuinely needs a friendlier, human-facing string distinct from its debug repr, `__str__` still has to be written by hand, exactly as in 5.2 — the decorator only automates `__init__`, `__repr__`, and `__eq__`.

`@dataclass` also accepts optional arguments controlling exactly which methods it generates. Two worth knowing at this stage: `frozen=True` makes every field read-only after construction — attempting `t1.priority = "high"` afterward raises an error, giving you enforced immutability rather than the naming-convention-only encapsulation from 6.2's single underscore — and `order=True` additionally generates `__lt__`, `__le__`, `__gt__`, and `__ge__`, comparing instances field-by-field in declaration order, so that sorting or `<`/`>` comparisons become meaningful [2]:

```python
@dataclass(frozen=True)
class Task:
    name: str
    priority: str
    done: bool = False
```

Both `frozen` and `order` are configuration passed to the decorator itself, in parentheses after `@dataclass`, not a change to how fields are declared inside the class body.

`Person` refactors into a dataclass identically:

```python
@dataclass
class Person:
    name: str
    age: int
    email: str

    def greet(self):
        return f"Hi, I'm {self.name}, and my email is {self.email}."

    def have_birthday(self):
        self.age = self.age + 1
```

Every field (`name`, `age`, `email`) is required (no defaults), matching 6.1's original `Person.__init__`, which took all three as required positional parameters. `greet()` and `have_birthday()` carry over unchanged from 6.1 as ordinary methods, exactly as `mark_complete` did for `Task` above.

Trace what `@dataclass` builds for `Person` the same way this section traced it for `Task` above, because seeing the pattern generalize a second time is the point. From the three field declarations `name: str`, `age: int`, `email: str` — all three required, none defaulted — the decorator generates an `__init__(self, name, age, email)` that assigns all three to `self` in declaration order; a `__repr__` returning `Person(name=..., age=..., email=...)` in that exact field order, using `!r` internally so string fields show their quotes just as the hand-written version in 5.2 did; and an `__eq__` that checks `isinstance(other, Person)` and then every field in turn, structurally identical to the `and`-chained expression traced above, just generated instead of typed out [2]. Nothing about `age` being an `int` rather than a `str` changes the shape of any of the three generated methods — the decorator treats every field the same way regardless of its annotated type, using the annotation only to document intent, not to enforce it at runtime.

### 5.5 Organizing Classes into Modules

Every class in this topic and the two before it has lived in one file. Real programs don't stay that way for long: once you have `Task`, `RegulatoryTask`, `Person`, `Student`, and `GraduateStudent` together, one file becomes hard to navigate, and different parts of a program often only need some of these classes, not all of them.

A **module** is simply a single `.py` file, and any class (or function, or variable) defined at the top level of that file becomes available to other files through **`import`**. Moving `Task` into its own file makes this concrete. A file named `task.py`:

```python
# task.py
from dataclasses import dataclass

@dataclass
class Task:
    name: str
    priority: str
    done: bool = False

    def mark_complete(self):
        self.done = True
```

A separate file, in the same directory, can now reach `Task` without redefining it:

```python
# main.py
from task import Task

t1 = Task("Write topic corpus", "normal")
t1.mark_complete()
print(t1)
```

`from task import Task` tells Python: look for a module named `task` (Python finds `task.py` in the same directory), run that file once, and bind the name `Task` — the class object it defines — into this file's own namespace. After that line, `Task` behaves in `main.py` exactly as if it had been defined there directly; the only difference is *where* its source code lives.

Trace what actually happens when that import line runs, because the sequence explains behaviour you'll rely on constantly. Python first checks whether a module named `task` has already been loaded; if not, it locates `task.py` and executes every top-level statement in that file exactly once — including the `@dataclass` decoration of the `Task` class body — storing the results in the module's own namespace. A **module object**, in Python's own data model, is one of the standard built-in types: it carries a namespace implemented as a dictionary, mapping every name defined at that file's top level (here, just `Task`) to the object it refers to [1]. `from task import Task` looks up the name `Task` inside that namespace and binds it into `main.py`'s namespace under the same name — which is why, after that one line, `main.py` can write `Task(...)` as though the class had been defined locally. Import the same module a second time, from anywhere else in the same program, and Python skips re-running the file entirely, reusing the module object it already built the first time — one more reason a class's identity, checked with `is` as in 6.1, stays consistent no matter how many files import it.

A second, closely related file, `person.py`, splits `Person` out of the same shared file the same way:

```python
# person.py
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str

    def greet(self):
        return f"Hi, I'm {self.name}, and my email is {self.email}."
```

`main.py` can now pull in both classes from their own files in one place, keeping each class's source in exactly one file while still using both together:

```python
# main.py
from task import Task
from person import Person

t1 = Task("Write topic corpus", "normal")
alice = Person("Alice Chen", 29, "alice@example.com")
print(t1)
print(alice)
```

A **package** extends this one level further: a directory containing multiple related modules (for example, a folder named `models` containing `task.py` and `person.py` together) groups related classes so that other code can import from the package as a unit rather than tracking many separate loose files. The mechanics of building packages in full — subdirectories, the special file that marks a directory as a package — belong to later coursework on tooling and project structure; what matters here is the basic shape this section has now traced twice: one class (or a few closely related classes) per module, and `import`/`from ... import ...` to reach a class defined somewhere else, with Python's module namespace doing the work of connecting the two files [1].

## 6. Implementation

Building or refactoring a class to use special methods and, where it fits, `@dataclass`, follows a repeatable sequence.

**Step 1 — decide whether the class is mostly data.** If nearly every line inside `__init__` is a plain `self.attribute = attribute` assignment, and `__repr__`/`__eq__` would just mechanically list those same attributes, the class is a strong candidate for `@dataclass` (5.4). If the class needs unusual construction logic, or `__eq__` needs to compare something other than a straight per-attribute match, write the special methods by hand instead (5.2, 5.3).

**Step 2 — write `__repr__`.** Format it as `ClassName(field1=value1, field2=value2, ...)`, using `!r` on each interpolated value so strings show their quotes, matching the convention traced in 5.2 [1][3]:

```python
def __repr__(self):
    return f"Task(name={self.name!r}, priority={self.priority!r}, done={self.done!r})"
```

**Step 3 — write `__str__`, if a human-facing string should differ from the debug repr.** If it wouldn't differ, skip this step entirely and rely on the fallback rule from 5.2 — `object`'s default `__str__` will call your `__repr__` automatically [1].

**Step 4 — write `__eq__`.** Return a single boolean expression chained with `and`: `isinstance(other, ClassName)` first, then every attribute that should count toward equality — `and`'s short-circuit evaluation means the attribute comparisons never run unless the `isinstance` check already passed, exactly as traced in 5.3 [1].

**Step 5 — if Step 1 pointed toward a dataclass, replace Steps 2 through 4 with field declarations.** Import the decorator, list each attribute as `name: type`, add `= default_value` only to attributes that should be optional, and place every defaulted field after every non-defaulted one, per the ordering rule in 5.4 [2]. Any method beyond `__init__`/`__repr__`/`__eq__` — `mark_complete()`, `have_birthday()` — stays in the class body unchanged, written exactly as it would be in a non-dataclass.

**Step 6 — verify the generated behaviour.** Print an instance to confirm `__repr__` (or `__str__`) shows what you expect; compare two instances built with identical arguments to confirm `__eq__` reports `True`; compare two instances with a differing attribute to confirm it reports `False`.

**Step 7 — split into modules once the file holds more than one or two closely related classes.** Move each class (or a small group of tightly related classes) into its own `.py` file, and reach it from other files with `from module_name import ClassName`, as traced in 5.5.

Put together, refactoring `Task` from its 6.1/6.2 form into its final form for this topic looks like this, end to end:

```python
# task.py
from dataclasses import dataclass

@dataclass
class Task:
    name: str
    priority: str
    done: bool = False

    def mark_complete(self):
        self.done = True


class RegulatoryTask(Task):
    def __init__(self, name, priority, regulation_code):
        super().__init__(name, priority)
        self.regulation_code = regulation_code
```

`RegulatoryTask` here still uses a hand-written `__init__` rather than its own `@dataclass` field list, because it needs to call `super().__init__(...)`, threading the inherited fields through the dataclass-generated constructor of `Task` exactly the way 6.2 threaded `Person → Student → GraduateStudent`. Its signature is unchanged from 6.2 — `name`, `priority`, `regulation_code` — because `done` was already optional on `Task`'s own generated `__init__` (it defaults to `False`), so `RegulatoryTask` has no reason to accept or forward it explicitly. Mixing a plain subclass on top of a dataclass superclass like this is a normal, supported pattern — the decorator only changes how `Task` itself builds its three methods; it places no constraint on classes that inherit from it [2].

## 7. Real-World Patterns

Reliable `__repr__` output is one of the most consistently useful things you can add to any class, because it's what appears in error messages and log output the moment something goes wrong. A stack trace that shows `Task(name='Write topic corpus', priority='normal', done=False)` tells the person debugging it vastly more than `<__main__.Task object at 0x7f2b1c0a4d90>` — the entire reason production codebases treat "give every class a useful `__repr__`" as close to a non-negotiable rule [1][3].

`__eq__` matters most, in practice, the moment you start writing automated tests. A test that constructs an expected `Task` and compares it against the one your code actually produced only works if `==` compares values — without a real `__eq__`, every such test would need to compare each attribute individually by hand, which is exactly the tedious, error-prone work `__eq__` exists to remove.

`@dataclass` is the standard shape for what many codebases call a **DTO** (data transfer object) or a **record**: a small object whose entire job is to carry a fixed set of named values between parts of a system — an API response, a row read from a file, a configuration setting — with no significant behaviour of its own beyond what `@dataclass` already generates. The official documentation frames the decorator around exactly this use case: classes whose primary purpose is holding data, where `__init__`, `__repr__`, and `__eq__` would otherwise be near-identical boilerplate across dozens of similar classes in the same codebase [2].

`order=True` (introduced in 5.4) shows up whenever a program needs to rank or sort structured records — a to-do list ordering tasks by priority, a leaderboard ordering scores, a queue ordering jobs by deadline. Without it, sorting a list of plain `Task` instances raises an error, because Python has no idea how to compare two `Task` objects with `<`; declaring the class as `@dataclass(order=True)` instead makes sorting compare instances field-by-field in declaration order automatically, the same mechanical generation pattern `@dataclass` already uses for `__eq__` [2].

In practice, module organization compounds as a codebase grows: many real Python projects converge on a single `models.py` (or, in a package, a `models/` directory) holding every data-bearing class — `Task`, `Person`, `Student` — while a separate file holds the logic that operates on them. Nothing in the language enforces this split; it's a convention many teams settle on independently, precisely because it lets one part of a team work on data shapes while another works on behaviour, each importing only the classes it actually needs, the same `from module import ClassName` mechanism traced in 5.5.

## 8. Best Practices

- **Write `__repr__` before `__str__`, and skip `__str__` when it would just repeat `__repr__`.** The fallback rule from 5.2 means `print()` still works correctly with only `__repr__` defined — don't write a `__str__` that duplicates it verbatim.
- **Always guard `__eq__` with `isinstance()`, as the first operand of the `and` chain.** Comparing `self.name == other.name` against an `other` that isn't even the right class risks an `AttributeError` the moment someone writes `t1 == "not a task"` — putting the `isinstance` check first and relying on `and`'s short-circuit evaluation turns that into a clean `False` instead.
- **Reach for `@dataclass` when the class is mostly attributes; write methods by hand when construction or equality needs real logic beyond "assign every field" / "compare every field."** Forcing a class with unusual constructor logic into `@dataclass`'s field-declaration shape usually produces worse code than just writing `__init__` directly.
- **Order dataclass fields with every default-valued field after every required one**, per the rule in 5.4 — this isn't a style preference, it's enforced by Python and will raise an error otherwise [2].
- **Remember `@dataclass` does not generate `__str__`.** If a friendlier, human-facing string genuinely differs from the debug-style `__repr__`, write `__str__` by hand even on a dataclass.
- **One class (or a few tightly related classes) per module.** A file that has grown to hold five unrelated classes is a sign it's time to split, following 5.5's pattern.

## 9. Hands-On Exercise

Take the `Task` class from 6.1 (name, priority, done, `mark_complete()`) and, without using `@dataclass` yet, add a `__repr__` (in the `ClassName(field=value, ...)` shape from 5.2), a `__str__` (reusing the wording `describe()` used in 6.1), and an `__eq__` (a single `and`-chained boolean expression starting with an `isinstance` check, comparing all three attributes). Create two `Task` instances with identical arguments and confirm `t1 == t2` reports `True`; change one attribute on `t2` and confirm it now reports `False`.

Then rewrite the same class as a `@dataclass`: declare `name` and `priority` as required fields and `done` as a field defaulting to `False`, keep `mark_complete()` as an ordinary method in the class body, and confirm `print()`, `==`, and construction all behave the same way they did with the hand-written version. Finally, move the dataclass version into its own file, `task.py`, and import it from a second file to construct and print one instance.

## 10. Key Takeaways

- `__repr__` and `__str__` are special methods that control how an object turns into a string — `__repr__` for an unambiguous, developer-facing representation, `__str__` for a human-readable one — and Python calls them implicitly through `print()`, `str()`, and f-strings rather than being called directly.
- Without a `__str__`, `print()` falls back to `__repr__`, because `object`'s default `__str__` calls `self.__repr__()`.
- Without `__eq__`, `==` between custom-class instances falls back to identity comparison (the same check `is` performs); `__eq__` lets you define equality as a single `and`-chained boolean expression — "same class, and same attribute values" — instead.
- `@dataclass` generates `__init__`, `__repr__`, and `__eq__` from a list of annotated field declarations, cutting out repetitive boilerplate for classes that are mostly structured data — but it does not generate `__str__`, and defaulted fields must all come after non-defaulted ones.
- A dataclass is still an ordinary class: it can hold plain methods, and it participates in inheritance exactly as any other class does.
- Once a program has more than a class or two, splitting them into their own modules (`.py` files) and using `import` / `from module import Name` keeps related code together and lets other files reach only what they need.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
