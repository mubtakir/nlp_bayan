# Bayan Language Guide – Part 1: Introduction (EN)

> This introduction gives you a high‑level tour of the Bayan language and points you to the detailed tutorials.

Quick navigation:
- **Procedural & OOP tutorial (EN)**: `02_PROCEDURAL_OOP_EN_PART1..4.md`
- **Logic programming tutorial (EN)**: `03_LOGIC_PROGRAMMING_EN_PART1..4.md`
- **Arabic tutorials (AR)**: parallel files with `_AR` in the same folder

---

## 1. What is Bayan?

Bayan is a **hybrid programming language** that combines three styles in one place:

1. **Procedural / imperative** (Python‑like)
2. **Object‑oriented (OOP)** (classes, methods, inheritance)
3. **Logic programming** (Prolog‑style facts, rules, and queries)

The goal is to let you:
- Write normal Python‑style code when that is best.
- Switch to **logic rules and queries** for problems that are easier to express declaratively.
- Mix both styles inside the same file and even inside the same **`hybrid { }`** block.

Bayan is also **bilingual**:
- Keywords and some constructs have **English and Arabic forms**.
- The same code can often be written with English or Arabic keywords, or a mix, depending on your audience.

---

## 2. Hybrid blocks

Every Bayan program lives inside one or more **hybrid blocks**:

```bayan
hybrid {
    print("Hello from Bayan!")
}
```

Inside `hybrid { ... }` you can:
- Use Python‑style statements (variables, loops, functions, classes, etc.).
- Declare logic **facts** and **rules**.
- Send **queries** to the logic engine.

In Arabic tutorials you will also see the Arabic keyword:

```bayan
هجين {
    اطبع("مرحباً من البيان!")
}
```

Both `hybrid` and `هجين` open the same kind of block; which one you use depends on the language of the tutorial.

---

## 3. Bilingual keywords and style

Two important bilingual constructs are actually implemented in the interpreter:

- `hybrid { ... }`  ↔  `هجين { ... }`
- `query ...`       ↔  `استعلام ...`

In the **English** tutorials we use:
- English keywords (`if`, `for`, `while`, `def`, `class`, `return`, `True`, `False`, `None`, `print`, ...)
- English identifiers (`total`, `Person`, `age`, ...)

In the **Arabic** tutorials we:
- Prefer Arabic block keywords `هجين` and `استعلام`.
- Use Arabic identifiers (`مجموع`, `شخص`, `طالب`, ...).
- Keep Python keywords like `def`, `class`, `return` as they are, because the interpreter currently recognizes them only in English.

The idea is that **both languages teach the same concepts**, but each uses examples and naming that feel natural in its language.

---

## 4. First Bayan program

Create a file `hello.bayan` with:

```bayan
hybrid {
    def greet(name): {
        print("Hello, " + name)
    }

    greet("Bayan")
}
```

Run it using the Bayan runner integrated with Python (see `README.md` for installation and execution details in your environment).

What is happening here?
- We open a `hybrid { ... }` block.
- Define a function `greet` using Python‑style syntax.
- Call it with the string `"Bayan"`.

You can translate the same idea into Arabic‑style examples in `01_INTRODUCTION_AR.md`.

---

## 5. A taste of logic programming

Bayan also supports **Prolog‑style logic programming**. Inside a `hybrid` block you can add facts and rules:

```bayan
hybrid {
    fact parent("Ali", "Sara").
    fact parent("Sara", "Omar").

    rule grandparent(X,Y) :- parent(X,Z), parent(Z,Y).
}

query grandparent("Ali", ?G).
```

Here you:
- Declare two `parent/2` facts in the knowledge base.
- Define a `grandparent/2` rule.
- Ask a **query** outside the block to find all `?G` such that `grandparent("Ali", ?G)` holds.

For a full introduction to logic programming in Bayan, see:
- `03_LOGIC_PROGRAMMING_EN_PART1.md` (basics)
- `03_LOGIC_PROGRAMMING_EN_PART2.md` (rules, recursion, lists)
- `03_LOGIC_PROGRAMMING_EN_PART3.md` (meta‑predicates, dynamic KB, hybrid)
- `03_LOGIC_PROGRAMMING_EN_PART4.md` (probabilistic & causal)

---

## 6. Where to go next

If you are new to Bayan, a good learning path is:

1. **Read this introduction** (this file).
2. Study **procedural and OOP Bayan** in:
   - `02_PROCEDURAL_OOP_EN_PART1.md` (basics & data types)
   - `02_PROCEDURAL_OOP_EN_PART2.md` (control flow & functions)
   - `02_PROCEDURAL_OOP_EN_PART3.md` (OOP: classes, inheritance, polymorphism)
   - `02_PROCEDURAL_OOP_EN_PART4.md` (advanced: decorators, generators, async, context managers, *args/**kwargs)
3. Learn **logic programming** in:
   - `03_LOGIC_PROGRAMMING_EN_PART1.md` .. `PART4.md`
4. When you are comfortable, you can switch to the **Arabic tutorials**:
   - `01_INTRODUCTION_AR.md`, `02_PROCEDURAL_OOP_AR*.md`, `03_LOGIC_PROGRAMMING_AR*.md`
5. If you want to go deeper into **AI/NLP and the conceptual language model**:
   - `ai/AI_LIBRARY_GUIDE.md` — overview of `ai.nlp` and `ai.ml` building blocks.
   - `docs/CONCEPTUAL_LM_BLUEPRINT.md` — high-level architecture of the conceptual LM.
   - `docs/CONCEPTUAL_LM_AI_HANDOVER.md` — developer handover guide for extending the conceptual LM layers.

Both language tracks aim to stay in sync so that readers of Arabic and English get the **same capabilities and mental model** of Bayan.

