# Bayan Language Guide – Part 3: Logic Programming (EN)

> This guide introduces Prolog-style logic programming in Bayan. It mirrors the Arabic guide in structure and topics.

Parts:
- [PART1](03_LOGIC_PROGRAMMING_EN_PART1.md)
- [PART2](03_LOGIC_PROGRAMMING_EN_PART2.md)
- [PART3](03_LOGIC_PROGRAMMING_EN_PART3.md)
- [PART4](03_LOGIC_PROGRAMMING_EN_PART4.md)

For the Arabic version, see:
- `03_LOGIC_PROGRAMMING_AR.md`
- `03_LOGIC_PROGRAMMING_AR_PART1..4.md`

---

## 📚 Table of Contents

### Section 1: Basics (Beginner)
1. [Introduction to logic programming](#1-introduction-to-logic-programming)
2. [Facts](#2-facts)
3. [Queries](#3-queries)
4. [Logic variables](#4-logic-variables)
5. [Simple rules](#5-simple-rules)

### Section 2: Intermediate
6. [Composite rules](#6-composite-rules)
7. [Recursion (paths)](#7-recursion-paths)
8. [Lists in logic](#8-lists-in-logic)
9. [Logical properties](#9-logical-properties)

### Section 3: Advanced
10. [Meta-predicates](#10-meta-predicates)
11. [Dynamic knowledge base](#11-dynamic-knowledge-base)
12. [Hybrid programming](#12-hybrid-programming)
13. [Advanced examples](#13-advanced-examples)
14. [Probabilistic reasoning](#14-probabilistic-reasoning)
15. [Causal network engine](#15-causal-network-engine)

---

## Section 1: Basics

PART1 explains the core building blocks of logic programming in Bayan:
- **Facts** that describe the world (e.g., `parent("Ali", "Sara")`).
- **Queries** that ask the engine to solve for variables.
- **Logic variables** such as `?X`, `?Y`.
- **Simple rules** that derive new relations from existing facts.

Example:

```bayan
hybrid {
    fact parent("Ali", "Sara").
    fact parent("Sara", "Omar").
    rule grandparent(X,Y) :- parent(X,Z), parent(Z,Y).
}

query grandparent("Ali", ?G).
```

For detailed explanations, see `03_LOGIC_PROGRAMMING_EN_PART1.md`.

---

## Section 2: Intermediate topics

PART2 goes deeper into rules and data structures:
- **Composite rules** like `ancestor/2` defined in terms of `parent/2`.
- **Recursive rules** such as `path/2` over a graph.
- **Lists** in predicates, using pattern matching and recursion.
- **Logical properties** like `tea_lover/1` and `coffee_lover/1`.

See `03_LOGIC_PROGRAMMING_EN_PART2.md` for the full code.

---

## Section 3: Advanced topics

PART3 introduces tools for working with sets of solutions and evolving knowledge:
- **Meta-predicates** (`findall`, `bagof`, `setof`) to collect results into lists.
- **Dynamic knowledge bases** updated at runtime using `assertz`, `asserta`, `retract`.
- **Hybrid programs** that mix imperative Bayan code and logic facts/rules in the same file.

See `03_LOGIC_PROGRAMMING_EN_PART3.md` for examples.

---

## Section 4: Probabilistic and causal reasoning

PART4 summarizes higher-level reasoning features:
- **Probabilistic reasoning**: attach confidence values to states and transitions; reason under uncertainty.
- **Causal network engine**: define nodes and causal links; perform inference and interventions.

For more details on causal networks, see the separate reference:
- `bayan/docs/CAUSAL_NETWORK_ENGINE_GUIDE.md`

And for structured probabilistic logic examples, see `03_LOGIC_PROGRAMMING_EN_PART4.md`.

