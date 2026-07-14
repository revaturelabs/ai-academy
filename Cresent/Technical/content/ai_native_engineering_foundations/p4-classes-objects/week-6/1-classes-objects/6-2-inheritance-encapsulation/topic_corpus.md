---
topic_id: 6.2
title: Inheritance & Encapsulation
position_in_module: 2
generated_at: 2026-07-14T00:00:00Z
resource_count: 3
---

# 1. Inheritance & Encapsulation — Topic Corpus

## 2. Prerequisites

This topic builds directly on **6.1 Object-Oriented Foundations**, and reuses its vocabulary without redefining it:
- **Class vs instance/object** — a class is a blueprint; an instance is a specific object built from it.
- **Constructor (`__init__`)** — the method that runs automatically at creation time to set up instance attributes.
- **Instance vs class attributes** — attributes set inside `__init__` belong to one instance; attributes set in the class body are shared until an instance shadows them.
- **Methods and `self`** — functions defined in a class body, automatically bound to the instance they're called on.
- The `Task` class (`name`, `priority`, `done`, `mark_complete()`, `describe()`) and the `Person` class (`name`, `age`, `email`, `species`, `greet()`, `have_birthday()`) from 6.1 are the running examples this topic extends. 6.1 explicitly set up a `RegulatoryTask` to be built from `Task` "later in the module" — this is that moment.

## 3. Learning Objectives

By the end of this topic, you should be able to:
- Define a subclass that extends a superclass using single-level inheritance, and explain what a subclass inherits automatically versus what it must override.
- Use `super()` inside a subclass's `__init__` and its methods to extend the superclass's behaviour instead of duplicating it, across a chain of more than one level of inheritance.
- Explain, at a basic level, what Method Resolution Order (MRO) is, why it matters once a class has more than one direct base, and how to inspect it.
- Distinguish the single-underscore naming convention from double-underscore name mangling, and explain what each one actually does (and doesn't do) to attribute access.
- Build a small multi-level class hierarchy (`Person` → `Student` → `GraduateStudent`) that correctly threads shared state and behaviour through every level.

## 4. Introduction

6.1 left off with a `Task` class — `name`, `priority`, `done`, plus `mark_complete()` and `describe()` — and a promise: a `RegulatoryTask` would come along later and extend that same blueprint rather than copy it. This is that topic.

Picture a compliance team that needs to track regulated tasks alongside ordinary ones. A `RegulatoryTask` is still, fundamentally, a `Task` — it still has a name, a priority, a done flag, and the ability to be marked complete. But it also needs one more thing an ordinary `Task` doesn't: a regulation code identifying which rule it satisfies. Writing a second class from scratch, copying `Task`'s three attributes and two methods, and then adding the one new piece, works — until `Task` itself changes and the copy quietly drifts out of sync. **Inheritance** is Python's mechanism for saying "this class is a `Task`, plus a little more" without copying a single line of `Task`'s own code.

The same idea scales past one level. A `Student` is a `Person`, plus a student ID. A `GraduateStudent` is a `Student` — which is already a `Person` — plus a thesis title. Each level adds exactly one new idea on top of everything the level below already provides. Once more than one class is layered this way, two more questions become unavoidable: how do you call up to a specific ancestor's version of a method (`super()`), and, if a class ever has more than one direct ancestor, in what order does Python search them (Method Resolution Order)? This topic also covers **encapsulation** — the naming conventions Python gives you to signal which attributes are meant to stay internal to a class, once a hierarchy makes "internal to which class, exactly?" a real question.

## 5. Core Concepts

### 5.1 Single-Level Inheritance: A Subclass Extends a Superclass

A **subclass** (also called a derived or child class) is a class defined in terms of another class, called its **superclass** (or base/parent class). The subclass automatically has every attribute-setting and method that the superclass has, and can add new ones or replace existing ones. The syntax is `class Subclass(Superclass):` [1]:

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


class RegulatoryTask(Task):
    pass
```

`RegulatoryTask` has no body of its own yet beyond `pass`, but it is already fully usable:

```python
rt = RegulatoryTask("File quarterly report", "high")
rt.mark_complete()
print(rt.describe())
# File quarterly report (high) - done=True
```

Trace `rt = RegulatoryTask("File quarterly report", "high")` the same disciplined way 6.1 traced `Task(...)`. Python looks up `__init__` — first on `RegulatoryTask` itself, finds nothing there, then walks up to `RegulatoryTask`'s base, `Task`, and finds `Task.__init__` there. That inherited `__init__` runs exactly as written in `Task`, binding the new object as `self` and assigning `name`, `priority`, and `done`. `rt.mark_complete()` repeats the same lookup — nothing on `RegulatoryTask`, found on `Task` — and runs unchanged. Nothing about inheriting a method requires it to be rewritten anywhere; the subclass simply doesn't define its own version, so the search continues upward to the superclass, exactly the way attribute lookup in 6.1 always started at the specific instance and, for methods, continues to the instance's class [1].

Python gives you two builtin functions to check these relationships directly. `isinstance(rt, Task)` returns `True` — `rt` is usable anywhere a `Task` is expected, because `RegulatoryTask` **is a** `Task` plus more. `issubclass(RegulatoryTask, Task)` also returns `True` — that's a class-to-class relationship, not an instance-to-class one. `type(rt)` still reports `RegulatoryTask`, not `Task` — `type()` (from 1.2) always reports the exact class an object was built from, while `isinstance()` answers the broader "is this usable as a `Task`?" question that inheritance exists to support.

**Overriding** is what happens when a subclass *does* define its own version of a method the superclass already has. Because Python's method lookup checks the instance's own class first, a method defined directly on `RegulatoryTask` is found and used before the search would ever reach `Task`'s version:

```python
class RegulatoryTask(Task):
    def describe(self):
        return f"[REGULATED] {self.name} ({self.priority}) - done={self.done}"
```

Now `rt.describe()` never even looks at `Task.describe` — the search stops the moment it finds `describe` directly on `RegulatoryTask`. This is overriding: giving a method the same name in a subclass so the subclass's version wins.

But `RegulatoryTask` still needs one more thing a plain `Task` doesn't have: a regulation code. The tempting, naive way to add it is to override `__init__` and simply re-type everything `Task.__init__` already does:

```python
class RegulatoryTask(Task):
    def __init__(self, name, priority, regulation_code):
        self.name = name
        self.priority = priority
        self.done = False
        self.regulation_code = regulation_code

    def describe(self):
        return f"[{self.regulation_code}] {self.name} ({self.priority}) - done={self.done}"
```

This works, but it has exactly the duplication problem the Introduction warned about: the first three lines inside `RegulatoryTask.__init__` are a byte-for-byte copy of `Task.__init__`'s body. If `Task.__init__` ever gains a new attribute, or changes how `done` gets initialized, `RegulatoryTask`'s copy will not follow along automatically — someone has to remember to update both places. That's the exact problem `super()` exists to solve, covered next.

### 5.2 Multiple Levels of Inheritance: `super()` and Extending Behaviour

`super()` is a builtin that, called from inside a subclass's method, gives you a proxy object standing in for "whatever comes next after this class," letting you call the superclass's version of a method without naming that superclass explicitly [1][2]. Rewriting `RegulatoryTask.__init__` with `super()` removes the duplication entirely:

```python
class RegulatoryTask(Task):
    def __init__(self, name, priority, regulation_code):
        super().__init__(name, priority)
        self.regulation_code = regulation_code

    def describe(self):
        base_description = super().describe()
        return f"[{self.regulation_code}] {base_description}"
```

Trace `RegulatoryTask("File quarterly report", "high", "GDPR-7")` carefully. Python creates a blank `RegulatoryTask` object, binds it as `self`, and starts running `RegulatoryTask.__init__`. The first line, `super().__init__(name, priority)`, resolves to `Task.__init__`, called with that same `self` — so `Task.__init__`'s body runs exactly as it always does, setting `self.name`, `self.priority`, and `self.done` on the object currently under construction. Control then returns to `RegulatoryTask.__init__`, which continues with its own line, `self.regulation_code = regulation_code`, adding the one attribute that's actually new here. Nothing from `Task.__init__` was retyped — `super()` ran the original code in place.

`describe()` follows the identical pattern for a method that isn't a constructor: `super().describe()` calls `Task.describe`, which builds and returns `"File quarterly report (high) - done=False"` using only the attributes `Task` itself knows about. `RegulatoryTask.describe` then wraps that returned string with a `[GDPR-7]` prefix. This is **extending** behaviour, as distinct from the plain overriding shown in 5.1: the subclass's version still calls out to the superclass's version and builds on top of what it returns, rather than replacing it outright.

The same pattern holds across more than two levels, and each level only ever needs to know about the level directly above it — `super()` handles the rest of the chain automatically. Take `Person` from 6.1 and extend it twice:

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


class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id

    def greet(self):
        base_greeting = super().greet()
        return f"{base_greeting} I'm a student, ID {self.student_id}."


class GraduateStudent(Student):
    def __init__(self, name, age, email, student_id, thesis_title):
        super().__init__(name, age, email, student_id)
        self.thesis_title = thesis_title

    def greet(self):
        base_greeting = super().greet()
        return f"{base_greeting} My thesis is '{self.thesis_title}'."
```

Trace `gs = GraduateStudent("Maria Lopez", 27, "maria@example.edu", "S1029", "Federated Learning at the Edge")` one level at a time. `GraduateStudent.__init__` starts running with `self` bound to the new object. Its first line, `super().__init__(...)`, resolves to `Student.__init__` — the class directly above `GraduateStudent`. `Student.__init__` in turn starts with its own `super().__init__(...)`, which resolves to `Person.__init__` — the class directly above `Student`. `Person.__init__` runs first of all three, setting `name`, `age`, and `email`. Control returns to `Student.__init__`, which sets `student_id`. Control returns again to `GraduateStudent.__init__`, which sets `thesis_title` last. Three constructors ran, each contributing exactly the attributes it owns, and each one only had to call `super().__init__()` — none of them needed to know or care how many levels existed above it.

`gs.greet()` chains the same way in reverse order of *return*, though the same order of *call*: `GraduateStudent.greet` is found first (own class), calls `super().greet()` which runs `Student.greet`, which itself calls `super().greet()` which runs `Person.greet` first of all three — producing the base introduction string. That string returns up to `Student.greet`, which appends the student-ID sentence and returns *that* combined string up to `GraduateStudent.greet`, which appends the thesis sentence last. The final printed greeting contains all three contributions, built by three cooperating methods, none of which duplicated another's work [2].

Attribute lookup follows the identical MRO-based order, not just method calls, and it's worth tracing separately because it starts in a different place than a method call does. Trace `gs.species` against the same three-level hierarchy. Python first checks `gs`'s own instance dictionary — the one built up across all three `__init__` calls above, which by now holds `name`, `age`, `email`, `student_id`, and `thesis_title` — and `species` is not there, because no `__init__` in the chain ever assigned it to `self`. Only once the instance dictionary comes up empty does Python start walking the classes: `GraduateStudent`'s own class body defines no `species`, so the search continues to `Student`'s class body, which also defines none, and finally reaches `Person`'s class body, where `species = "Homo sapiens"` was defined directly as a class attribute in 6.1. The search stops there and returns `"Homo sapiens"` [1]. Contrast this with `gs.name`: the search never leaves the instance dictionary at all, because `Person.__init__` — the innermost call in the construction chain traced above — assigned `self.name` directly onto the object currently under construction, and instance-dictionary entries are always checked before any class in the hierarchy. This is the same rule 6.1 introduced for a single class — instance attributes shadow class attributes — extended across every level of a multi-class chain: the instance dictionary is checked first no matter how many superclasses exist above, and only once it comes up empty does Python start walking upward through the classes, one level at a time, in the same order `super()` uses [1].

### 5.3 Multiple Inheritance and Method Resolution Order (Brief)

Every example so far has a **single-inheritance chain**: `GraduateStudent` has exactly one direct base (`Student`), which has exactly one direct base (`Person`). Walking `super()` up such a chain is unambiguous — there's only ever one next class to go to.

**Multiple inheritance** is when a class lists more than one direct base: `class Sub(BaseA, BaseB):`. This raises a question a single-inheritance chain never has to answer: if both `BaseA` and `BaseB` (or something further up from both of them) define the same method name, which one does `super()` — or a plain attribute lookup — actually find first? Python answers this with the **Method Resolution Order (MRO)**: a fixed, computed ordering of every class in the hierarchy, decided once when the subclass is defined, using an algorithm called C3 linearization [1][3]. You rarely need to compute an MRO by hand — you only need to know it exists, that Python computes it automatically and consistently, and how to look it up.

The classic case that makes MRO visible is the **diamond problem**: two classes (`Left` and `Right`) both extend the same base (`Base`), and a fourth class (`Diamond`) extends both `Left` and `Right` [3]:

```python
class Base:
    def __init__(self, label):
        self.label = label

    def describe(self):
        return f"Base: {self.label}"


class Left(Base):
    def describe(self):
        return f"Left -> {super().describe()}"


class Right(Base):
    def describe(self):
        return f"Right -> {super().describe()}"


class Diamond(Left, Right):
    pass


d = Diamond("example")
print(d.describe())
print(Diamond.__mro__)
```

Running this prints:

```
Left -> Right -> Base: example
(<class '__main__.Diamond'>, <class '__main__.Left'>, <class '__main__.Right'>, <class '__main__.Base'>, <class 'object'>)
```

`Diamond.__mro__` is a tuple (per 1.4) showing the exact order Python searches: `Diamond`, then `Left`, then `Right`, then `Base`, then `object` (the class every class ultimately extends). Trace `d.describe()` against that order. `Diamond` itself defines no `describe`, so the search continues to the next name in the MRO, `Left`, which does define one. `Left.describe` runs and calls `super().describe()` — and this is the detail that trips people up: `super()` inside `Left` does **not** mean "go straight to `Base`." It means "continue from `Left`'s position in the MRO to whatever's next," which, per the printed order above, is `Right` — not `Base`. So `Right.describe` runs next, and *its* `super().describe()` call continues to the next name after `Right`, which finally is `Base`. `Base.describe` runs last, returning `"Base: example"`, which `Right` wraps into `"Right -> Base: example"`, which `Left` wraps into the final `"Left -> Right -> Base: example"` [2][3].

This is the core lesson of MRO for this stage of the course: `super()` always means "the next class in the computed MRO," never "my literal parent class." That's exactly what makes cooperative chains like 5.2's `Person → Student → GraduateStudent` work correctly even in more tangled hierarchies — every class only ever has to call `super()` once and trust that Python routes the call to the right next class. Multiple inheritance and MRO computation in full depth (the C3 algorithm's actual rules) is a topic for later, more advanced coursework; what matters here is recognizing the diamond shape, knowing `ClassName.__mro__` exists to inspect the order, and understanding that `super()` follows that order rather than a fixed parent name [1][2][3].

### 5.4 Encapsulation and Information Hiding

**Encapsulation** is the practice of controlling which parts of an object's state are meant to be used directly by outside code, and which parts are considered internal implementation detail that could change without notice. Python has no `private` keyword the way some other languages do — instead it uses two naming conventions, one purely social and one with an actual language mechanism behind it [1].

**Single leading underscore** (`_name`) is a convention, and only a convention: it signals to any reader (and to tools like linters) "this attribute is intended for internal use by this class or its subclasses — don't rely on it from outside code, it isn't part of the promised interface." Python does not stop external code from reading or writing it; the underscore is a note to the reader, not a lock [1]:

```python
class Task:
    def __init__(self, name, priority, internal_id):
        self.name = name
        self.priority = priority
        self.done = False
        self._internal_id = internal_id   # single underscore -- internal-use convention

    def mark_complete(self):
        self.done = True

    def describe(self):
        return f"{self.name} ({self.priority}) - done={self.done}"


t1 = Task("File quarterly report", "high", "T-1001")
print(t1._internal_id)   # T-1001 -- still fully accessible, just not part of the public contract
```

`t1._internal_id` prints without error. Nothing enforces the "don't touch this" intent — it is entirely on the reader of the code (and any subclass author) to respect the convention.

**Double leading underscore** (`__name`, with at most one trailing underscore) triggers an actual language mechanism: **name mangling**. The moment Python compiles a class body and sees `self.__pin` inside it, it silently rewrites that identifier, everywhere inside that class's own methods, to `self._ClassName__pin` — substituting in the literal name of the class the code was written in [1]:

```python
class SecureAccount:
    def __init__(self, owner_name, pin):
        self.owner_name = owner_name
        self.__pin = pin

    def verify_pin(self, attempt):
        return attempt == self.__pin


acct = SecureAccount("Priya Nair", 4477)
print(acct.verify_pin(4477))        # True
print(acct.__pin)                   # AttributeError: 'SecureAccount' object has no attribute '__pin'
print(acct._SecureAccount__pin)     # 4477 -- the mangled name, still reachable
```

`acct.__pin` raises `AttributeError` — not because Python enforced privacy in a security sense, but because that exact attribute name was never created in the first place. The real attribute living on `acct` is `_SecureAccount__pin`, and `acct._SecureAccount__pin` reaches it directly, proving the attribute is still just an ordinary attribute under a rewritten name [1].

The actual reason double-underscore mangling exists is **collision avoidance across an inheritance hierarchy**, not secrecy [1]. Consider a base and a subclass that happen to pick the same internal name:

```python
class Base:
    def __init__(self):
        self.__secret = "base secret"

    def reveal_base(self):
        return self.__secret


class Derived(Base):
    def __init__(self):
        super().__init__()
        self.__secret = "derived secret"

    def reveal_derived(self):
        return self.__secret


d = Derived()
print(d.reveal_base())      # base secret
print(d.reveal_derived())   # derived secret
```

Without mangling, `Derived.__init__`'s `self.__secret = "derived secret"` would silently overwrite the exact same attribute `Base.__init__` had just set, and `reveal_base()` would incorrectly return `"derived secret"`. Because Python mangles each occurrence using the class the code is written in, `Base`'s assignment actually creates `_Base__secret`, and `Derived`'s assignment creates a completely separate `_Derived__secret`. `d` genuinely holds both attributes at once, and each class's own methods only ever see the name mangled for that class, so neither can accidentally clobber the other's internal state [1].

Because of this, the general guidance is to default to single underscore for "internal, but a subclass might still legitimately need to see or extend this," and reach for double underscore specifically when a subclass accidentally reusing the same attribute name would actually cause a bug — not as a general-purpose "make this private" habit.

## 6. Implementation

Extending a class follows a repeatable recipe, whether it's one level deep or several. Each step below matches something Python's class machinery actually does at the moment the code runs, not just a stylistic convention — the citations point at exactly which piece of real behaviour each step depends on.

**Step 1 — decide what's shared and what's new.** Everything the subclass has in common with the superclass stays in the superclass, untouched. Only the genuinely new attributes and behaviour belong in the subclass. For `RegulatoryTask`, `name`/`priority`/`done` stay on `Task`; only `regulation_code` is new. This step is pure design and involves no Python mechanics yet, but getting it wrong is what causes the duplication problem from 5.1 in the first place.

**Step 2 — declare the subclass.** Writing `class Subclass(Superclass):` does real work the instant it executes: Python builds a new class object and records `Superclass` as its one and only base. That single act is what makes `Subclass.__mro__` come out as `(Subclass, Superclass, object)` — computed and fixed at class-definition time — even before a single method has been written on `Subclass`'s own body [1][3]. This is why the empty `RegulatoryTask(Task): pass` from 5.1 was already fully usable: attribute and method lookup walks that computed MRO, and `Task` is already in it.

**Step 3 — write `__init__` only if the subclass needs new constructor parameters.** If it doesn't, skip `__init__` entirely and let the superclass's constructor run unchanged (as the empty `RegulatoryTask(Task): pass` did) — Python's method lookup simply never finds an `__init__` on `RegulatoryTask` and continues to `Task`'s, exactly as described in 5.1's trace [1]. If it does, the very first line should be `super().__init__(...)`, passed the parameters the superclass needs, followed by assignments for whatever's new. `super()` resolves this call by finding `RegulatoryTask`'s position in its own computed MRO and calling the `__init__` belonging to whatever class comes immediately after it — which, for a single-inheritance chain, is the superclass, but which for a more tangled hierarchy could be a different class entirely, as 5.3's diamond example showed [1][2]:

```python
class RegulatoryTask(Task):
    def __init__(self, name, priority, regulation_code):
        super().__init__(name, priority)
        self.regulation_code = regulation_code
```

**Step 4 — override methods only where behaviour genuinely differs.** If the subclass's version should replace the superclass's entirely, define it with no `super()` call, as `RegulatoryTask.describe` did before `super()` was introduced in 5.2 — that's a legitimate choice, not a mistake, when the superclass's version truly doesn't apply. Python's method lookup finds the subclass's version first purely because it's earlier in the MRO than the superclass's version, per 5.1 and 5.3, so no special "override" syntax exists or is needed [1][3]. If the subclass's version should build on the superclass's, call `super().method_name(...)` and use its return value, as the improved `RegulatoryTask.describe` and every `greet()` in the `Person → Student → GraduateStudent` chain did — the same MRO-based resolution from Step 3 applies here too, just for an ordinary method instead of `__init__` [2].

**Step 5 — repeat Steps 2 through 4 for each further level.** `Student(Person)` and `GraduateStudent(Student)` are each just one more application of the same four steps; neither needed to know anything about levels further away than its own immediate base, because `super()` always resolves to "the next class in this object's MRO," per 5.3 — and each class's own computed MRO is recalculated by Python automatically the moment that class is defined, so a `GraduateStudent` never has to be told that `Person` exists two levels up [1][2].

**Step 6 — for multiple direct bases, check `ClassName.__mro__`.** This only becomes necessary once a class lists more than one base, as in `Diamond(Left, Right)`. For every single-inheritance chain in this course so far — `RegulatoryTask(Task)`, `Student(Person)`, `GraduateStudent(Student)` — the MRO is just the chain itself, read top to bottom, plus `object` at the end; there's nothing to check. The moment a second base appears, printing `ClassName.__mro__` directly is the reliable way to confirm which order `super()` will actually follow, rather than guessing from the `class` line alone, since the C3 linearization algorithm that produces it does not always match simple left-to-right intuition once bases share ancestors [1][3].

**Step 7 — apply naming conventions for any new internal attribute as you add it.** Any attribute added in Step 3 that outside code shouldn't rely on gets a single leading underscore, which changes nothing about how Python stores or finds the attribute — it is purely a signal to readers [1]. Any attribute where a subclass could plausibly reuse the same name and silently overwrite the superclass's value gets a double leading underscore instead; Python mangles that name into `_ClassName__name` at the moment the class body compiles, using whichever class the assignment is textually written inside, which is exactly the collision-avoidance mechanism traced in 5.4 [1].

**Step 8 — verify the result with `isinstance()`, `issubclass()`, and `type()`.** After building the hierarchy, confirm it behaves as intended. `isinstance(rt, Task)` should report `True` because Python computes the "is-a" answer by checking whether `Task` appears anywhere in `RegulatoryTask`'s full MRO, not just whether it's the single immediate base [1][3]. `type(rt)` should still report `RegulatoryTask` exactly, never `Task` — `type()` never consults the MRO, it only reports the exact class recorded on the object at construction time. This step catches the easy-to-miss mistake of forgetting to list the superclass in the `class` line at all, which silently produces a class with an MRO of just `(Subclass, object)` and no relationship whatsoever to the intended superclass.

Put together end to end, building `RegulatoryTask` from `Task` looks like this, from a completely blank slate:

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


class RegulatoryTask(Task):
    def __init__(self, name, priority, regulation_code):
        super().__init__(name, priority)
        self.regulation_code = regulation_code

    def describe(self):
        base_description = super().describe()
        return f"[{self.regulation_code}] {base_description}"


rt = RegulatoryTask("File quarterly report", "high", "GDPR-7")
rt.mark_complete()
print(rt.describe())
# [GDPR-7] File quarterly report (high) - done=True
print(isinstance(rt, Task))       # True
print(issubclass(RegulatoryTask, Task))  # True
```

Every line traces back to a step above. Step 1 decided `regulation_code` was the only new attribute. Step 2's `class RegulatoryTask(Task):` line fixed `RegulatoryTask.__mro__` at `(RegulatoryTask, Task, object)` the instant it was defined [1][3]. Step 3's `super().__init__(name, priority)` resolves by walking that MRO one position past `RegulatoryTask` itself, landing on `Task.__init__` [1][2]. Step 4 overrode `describe()` to extend rather than replace, using the identical MRO-based resolution for `super().describe()` [2][3]. Steps 5 and 6 don't apply here because this is a single level with a single base. Step 7 isn't exercised in this particular class, since `regulation_code` is meant to be public, not internal. Step 8 confirms `isinstance(rt, Task)` and `issubclass(RegulatoryTask, Task)` both report `True`, because `Task` genuinely appears in `RegulatoryTask`'s computed MRO [1][3].

## 7. Real-World Patterns

Inheritance hierarchies like `Person → Student → GraduateStudent` show up constantly in production code, wherever a domain naturally has "a more specific kind of X" relationships. Web frameworks model form fields and database columns this way — a `TextField` and an `IntegerField` both extend a shared `Field` base that handles validation plumbing common to every field type, and each subclass only overrides the piece that's actually different (how to validate *this* particular kind of value). GUI toolkits do the same thing with widgets: a `Button` and a `Checkbox` both extend a shared `Widget` base that handles positioning and rendering machinery, while each subclass overrides only its own drawing and click-handling logic. 6.1's `Player` class is a natural fit for the same pattern outside this course: a game engine's `Enemy` or `NPC` classes typically extend a shared `Player`-like base to reuse `health`, `take_damage()`, and `score` handling, adding only the behaviour that makes an enemy different from a player character.

Exception hierarchies are one of the clearest real-world uses of exactly the single- and multi-level inheritance mechanics built in 5.1 and 5.2. Python's own built-in error types form a hierarchy — `ValueError` and `TypeError` both extend a shared `Exception` base — and application code routinely extends that same base further for its own error types:

```python
class ValidationError(Exception):
    def __init__(self, field_name, message):
        super().__init__(message)
        self.field_name = field_name


class MissingFieldError(ValidationError):
    def __init__(self, field_name):
        super().__init__(field_name, f"{field_name} is required")
```

`MissingFieldError` extends `ValidationError`, which extends `Exception`, using the identical `super().__init__()` pattern as `RegulatoryTask(Task)`. Code elsewhere that checks `isinstance(some_error, ValidationError)` automatically reports `True` for a `MissingFieldError` instance too, without needing to check for every specific error type by name — the same "is-a" relationship from 5.1 that made `isinstance(rt, Task)` return `True` for a `RegulatoryTask`.

Database libraries that map Python objects onto database records (object-relational mappers, or ORMs) commonly ask every model class to extend one shared base class that handles saving and loading, so each specific model only has to declare its own fields:

```python
class Model:
    def __init__(self, record_id):
        self.record_id = record_id

    def save(self):
        return f"Saving record {self.record_id}"


class User(Model):
    def __init__(self, record_id, email):
        super().__init__(record_id)
        self.email = email

    def save(self):
        base_result = super().save()
        return f"{base_result} (user: {self.email})"
```

Every model in a real ORM reuses `Model`'s saving-and-loading plumbing through exactly the `super().__init__()` and `super().save()` extension pattern built in 5.2 and formalized in Section 6's step-by-step recipe — `User` only ever has to describe what's specific to a user record, and a `Product` or `Order` model elsewhere in the same system would follow the identical pattern against the same `Model` base.

**Mixins** — small classes that exist purely to be combined with others via multiple inheritance, contributing one focused piece of behaviour each — are the most common legitimate use of the multiple-inheritance mechanics from 5.3 in real code. A logging mixin, a serialization mixin, and a timestamping mixin can each be written once and combined into whatever classes need them, with Python's MRO ensuring each mixin's `super()` call correctly hands off to the next one in the combination [2][3].

Encapsulation conventions from 5.4 matter most once code ships as a library other people depend on. Published Python packages routinely expose attributes with a single leading underscore specifically to tell users "this might change between versions without warning — don't build on it," which is exactly the convention-based signal 5.4 described, just applied at the scale of an entire published API rather than one class [1].

The next topic in this module, 6.3, picks up right where this one leaves off: it adds ways to control how objects print and compare (starting from the `describe()`-style methods built here) and a shortcut, `@dataclass`, for classes that are mostly just structured data — both of which sit directly on top of the class and inheritance mechanics covered in this topic and 6.1.

## 8. Best Practices

- **Call `super().__init__()` first, before assigning any new attributes.** Every constructor in this topic followed that order — establish the inherited state completely, then add what's new. Assigning new attributes first and calling `super().__init__()` afterward still runs, but it invites bugs if a superclass's constructor ever needs to reference something the subclass hasn't set up yet.
- **Use `super()`, not the superclass's literal name, to call up the hierarchy.** Writing `Task.__init__(self, name, priority)` instead of `super().__init__(name, priority)` works for a single level, but breaks the cooperative chain the moment a class sits between `RegulatoryTask` and `Task` in some future refactor — `super()` always resolves correctly to whatever is actually next in the MRO, per 5.3.
- **Keep hierarchies shallow.** Two or three levels (`Person → Student → GraduateStudent`) stay easy to trace by hand. Every additional level makes tracing a `super()` chain by eye harder, and makes it easier to lose track of which class actually owns which attribute.
- **Reach for multiple inheritance only for narrow, focused mixins.** A class with two or more bases that each carry their own state and constructors is exactly the diamond-problem shape from 5.3 — manageable, but worth a deliberate decision, not a default.
- **Default to single underscore; reserve double underscore for actual collision risk.** As 5.4 explained, name mangling exists to stop a subclass's attribute from silently overwriting a base class's attribute of the same name — use it when that's a genuine risk, not as a general "make this private" habit, since Python never enforces true privacy either way [1].
- **Use `isinstance()` when a function should accept a subclass anywhere a superclass is expected**, rather than checking `type(obj) is Task` — the latter rejects a perfectly valid `RegulatoryTask` just because its exact class differs from `Task`, defeating the entire point of building the subclass in the first place.
- **Inherit only where an actual "is-a" relationship holds.** `RegulatoryTask` genuinely is a `Task`, and `GraduateStudent` genuinely is a `Person` — every attribute and method inherited makes sense on the subclass too. If a class only needs to reuse a method or two from another class without that relationship genuinely holding, forcing it through `class Sub(Other):` produces a hierarchy where `isinstance()` reports something that isn't actually true about the domain, misleading every future reader who checks it.
- **Make the override-vs-extend choice visible in the code, not just in your head.** A method that overrides without calling `super()` at all (5.1's first `describe()`) and a method that extends by calling `super()` first (5.2's improved `describe()`) look almost identical at a glance — a short comment noting which one was intended, and why, saves the next reader from having to trace the MRO by hand just to find out.

## 9. Hands-On Exercise

Extend `Person` (from 6.1) into a `Student` subclass with one additional required constructor parameter, `student_id`, assigned via `super().__init__()` for the shared parameters. Override `greet()` to call `super().greet()` and append a sentence naming the student ID. Then extend `Student` into a `GraduateStudent` subclass with one more required parameter, `thesis_title`, following the identical pattern. Create one `GraduateStudent` instance and print the result of calling `greet()` on it, confirming the final string contains all three layers' contributions.

Separately, extend `Task` (from 6.1) into a `RegulatoryTask` with a required `regulation_code` parameter and a required `_review_status` parameter (single underscore — internal-use convention, still a required positional parameter, no default value), assigned via `super().__init__()` plus one new line each. Override `describe()` to call `super().describe()` and prefix the regulation code. Create one instance, mark it complete, and print `describe()` to confirm the prefix and the inherited `done=True` both appear. Then add a second attribute, `__audit_code`, using double-underscore name mangling, and print `instance._RegulatoryTask__audit_code` directly to confirm you can locate the mangled name Python actually created.

## 10. Key Takeaways

- A subclass (`class Sub(Super):`) inherits every attribute-setting and method from its superclass automatically; it only needs to define what's new or different.
- `super()` calls the next class in the object's Method Resolution Order — not necessarily a hardcoded parent — letting a subclass extend inherited `__init__` and method logic instead of duplicating it, across any number of chained levels.
- MRO is the fixed order Python searches classes in, computed once per class definition; it matters most once a class has more than one direct base (the diamond problem), and is inspectable via `ClassName.__mro__`.
- A single leading underscore (`_name`) is a non-enforced convention meaning "internal use only"; a double leading underscore (`__name`) triggers real name mangling to `_ClassName__name`, which exists to prevent attribute name collisions across an inheritance hierarchy, not to provide security.
- `isinstance()` and `issubclass()` test "is-a" relationships created by inheritance; `type()` still reports the exact class an object was built from.

## 11. Next Steps

_System-derived from the next entry in curriculum/sequence.md._
