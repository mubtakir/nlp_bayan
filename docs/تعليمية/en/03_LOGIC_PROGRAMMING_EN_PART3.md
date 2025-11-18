# Bayan Tutorial (EN) — Part 3.C: Logic Programming — Part 3 (Meta-predicates, Dynamic KB, Hybrid)

> Quick Nav: [PART1](03_LOGIC_PROGRAMMING_EN_PART1.md) | [PART2](03_LOGIC_PROGRAMMING_EN_PART2.md) | [PART3](03_LOGIC_PROGRAMMING_EN_PART3.md) | [PART4](03_LOGIC_PROGRAMMING_EN_PART4.md)

This part introduces more advanced logic programming tools in Bayan: meta-predicates, dynamic knowledge bases, and hybrid imperative/logic programs.

## 10) Meta-predicates: findall/bagof/setof

Meta-predicates operate on other predicates and their solutions.
`findall/3` collects all solutions of a query into a list, as we do here for everyone who likes tea.
```bayan
hybrid {
    fact likes("Ali", tea). fact likes("Sara", tea). fact likes("Omar", coffee).
}

# Collect all tea lovers
query findall(?X, likes(?X, tea), ?List).
```

## 11) Dynamic Knowledge Base

A dynamic knowledge base can be updated at runtime using meta-predicates such as `assertz`, `asserta`, and `retract`.
The example shows how to insert `friend/2` facts, query them, then retract one fact and query again.
```bayan
hybrid {
    assertz(friend("Ali", "Omar")).
    asserta(friend("Omar", "Nora")).
}

query friend(?A, ?B).

hybrid {
    retract(friend("Ali", "Omar")).
}

query friend(?A, ?B).
```

## 12) Hybrid Programming

Bayan lets you mix imperative and logic code inside the same file and even inside the same `hybrid { }` block.
In this example, we build a Python-style list and loop over it, and also declare logic facts that we can query afterwards.
```bayan
hybrid {
    # Imperative
    names = ["Ali", "Sara", "Omar"]
    for n in names: { print(n) }

    # Logic
    fact parent("Ali", "Sara").
    fact parent("Sara", "Omar").
}

# Query logic facts
query parent(?P, ?C).
```

