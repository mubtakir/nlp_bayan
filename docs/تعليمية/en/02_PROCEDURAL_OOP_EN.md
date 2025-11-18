# Bayan Language Guide – Part 2: Procedural & OOP (EN)

> This guide is large and is split into several parts for easier reading. It mirrors the Arabic guide in structure and topics.

Parts:
- [PART1](02_PROCEDURAL_OOP_EN_PART1.md)
- [PART2](02_PROCEDURAL_OOP_EN_PART2.md)
- [PART3](02_PROCEDURAL_OOP_EN_PART3.md)
- [PART4](02_PROCEDURAL_OOP_EN_PART4.md)

For the Arabic version, see:
- `02_PROCEDURAL_OOP_AR.md`
- `02_PROCEDURAL_OOP_AR_PART1..4.md`

---

## 📚 Table of Contents

### Section 1: Basics (Beginner)
1. [Variables and data types](#1-variables-and-data-types)
2. [Arithmetic and logical operations](#2-arithmetic-and-logical-operations)
3. [Strings](#3-strings)
4. [Lists](#4-lists)
5. [Dictionaries](#5-dictionaries)
6. [Sets](#6-sets)

### Section 2: Control flow (Intermediate)
7. [Conditionals (if/elif/else)](#7-conditionals-ifelifelse)
8. [Loops (for/while)](#8-loops-forwhile)
9. [Functions](#9-functions)
10. [Exception handling](#10-exception-handling)

### Section 3: Object-oriented programming (Advanced)
11. [Classes and objects](#11-classes-and-objects)
12. [Inheritance](#12-inheritance)
13. [Encapsulation](#13-encapsulation)
14. [Polymorphism](#14-polymorphism)

### Section 4: Advanced features (Expert)
15. [Decorators](#15-decorators)
16. [Generators](#16-generators)
17. [Async/Await](#17-asyncawait)
18. [Context managers](#18-context-managers)
19. [*args and **kwargs](#19-args-and-kwargs)

---

## Section 1: Basics

In this section you learn the core data types and basic operations in Bayan, using Python-like syntax inside `hybrid { }` blocks.
For detailed examples and exercises, see `02_PROCEDURAL_OOP_EN_PART1.md`.

### 1. Variables and data types

Bayan uses dynamic typing. You can freely assign integers, floats, strings, booleans, and containers:

```bayan
hybrid {
    x = 10
    price = 3.99
    name = "Sara"
    ok = True
    items = [1, 2, 3]
    person = {name: "Ali", age: 30}
}
```

### 2–6. Operations, strings, lists, dictionaries, sets

These topics follow the usual Python model (operators, slicing, list methods, dictionary lookups, set operations), with explanations and examples in PART1.

---

## Section 2: Control flow

PART2 shows how to control execution:
- Conditionals with `if / elif / else`
- Loops with `for` and `while`
- Function definitions with optional/default parameters
- Basic exception handling with `try / except / finally`

For code and comments, see `02_PROCEDURAL_OOP_EN_PART2.md`.

---

## Section 3: Object-oriented programming

PART3 introduces classes, objects, inheritance, encapsulation, and polymorphism, using a Python-style syntax inside Bayan.

Key ideas:
- Define classes with `class Name:` blocks.
- Use `self` for instance attributes.
- Derive child classes and call `super()` to reuse behavior.

See `02_PROCEDURAL_OOP_EN_PART3.md` for full examples.

---

## Section 4: Advanced features

PART4 covers advanced constructs that are useful in real-world code:
- **Decorators** to wrap and extend functions.
- **Generators** to yield sequences lazily.
- **Async/Await** for asynchronous functions.
- **Context managers** for resource management.
- `*args` and `**kwargs` for flexible function arguments.

See `02_PROCEDURAL_OOP_EN_PART4.md` for worked examples and explanations.

