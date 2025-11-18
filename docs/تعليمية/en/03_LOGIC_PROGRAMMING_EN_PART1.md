# Bayan Tutorial (EN) — Part 3.A: Logic Programming — Part 1 (Basics)

> Quick Nav: [PART1](03_LOGIC_PROGRAMMING_EN_PART1.md) | [PART2](03_LOGIC_PROGRAMMING_EN_PART2.md) | [PART3](03_LOGIC_PROGRAMMING_EN_PART3.md) | [PART4](03_LOGIC_PROGRAMMING_EN_PART4.md)

Bayan supports Prolog-style logic programming: facts, rules, and queries, inside `hybrid { }` blocks.

## 1) Facts

Facts are ground statements that the engine assumes to be true about the world.
Each line starting with `fact` introduces a predicate like `parent("Ali", "Sara")` into the knowledge base.
```bayan
hybrid {
    fact parent("Ali", "Sara").
    fact parent("Sara", "Omar").
}
```

## 2) Queries

Queries ask the logic engine to solve for variables that make a predicate true.
In the example, `parent("Ali", ?X)` asks: “for which values of `?X` is `parent("Ali", ?X)` a fact?”.
```bayan
query parent("Ali", ?X).
```

## 3) Logic Variables
- Variables start with `?`, e.g., `?X`, `?Y`.
- They unify with values during query solving.

## 4) Simple Rules

Rules let you define derived relations in terms of existing facts.
Here `grandparent(X,Y)` is true when `X` is a parent of some `Z` and `Z` is a parent of `Y`, written using `:-` and commas for "and".
```bayan
hybrid {
    fact parent("Ali", "Sara").
    fact parent("Sara", "Omar").
    rule grandparent(X,Y) :- parent(X,Z), parent(Z,Y).
}

query grandparent("Ali", ?G).
```


