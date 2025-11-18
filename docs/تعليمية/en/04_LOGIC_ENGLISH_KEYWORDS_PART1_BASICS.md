# Logic in Bayan Language (1): Basics with English Keywords

> This tutorial lays the foundation for the advanced logic tutorials (probabilities, causal networks, entities, semantics…).
> The focus here is on the basics, with **fully English examples** wherever possible.

## 1. Important Note About the `hybrid` Keyword

- Technically, to activate Bayan's hybrid engine we need the keyword:

  ```bayan
  hybrid {
      # Here we write facts, rules, and queries
  }
  ```

- In this version of the interpreter **you can use both** `hybrid` or `هجين` to open the hybrid block:
  - The English block `hybrid { ... }` in examples, noting that the Arabic form `هجين { ... }` is also available for those who want to read older examples or technical files.
  - `hybrid { ... }` for the full English equivalent.
  There is no longer a single English exception; what was previously said about the lack of an Arabic equivalent was an oversight/forgetfulness, and has now been corrected in the interpreter itself.
- Otherwise we will use:
  - **English names** for relations and variables.
  - **The English keyword** `query` instead of `استعلام` when running queries.

## 2. Facts (True Statements About the World)

### 2.1 Example: Simple Family

```bayan
hybrid {
    father("Ahmad", "Mohammed").
    father("Mohammed", "Layan").

    mother("Fatima", "Mohammed").
    mother("Layla", "Layan").
}
```

- Each line of the form `relation(value, value).` is a **fact**.
- The period `.` at the end is an essential part of the syntax.
- Values can be text strings as shown above.

### 2.2 Person Attributes

```bayan
hybrid {
    age("Ahmad", 45).
    age("Mohammed", 20).
    age("Layan", 5).

    profession("Ahmad", "engineer").
    profession("Fatima", "doctor").
}
```

Here we store **symbolic knowledge** about the world (ages, professions…) without any computation yet.

## 3. Logic Variables `?`

- A logic variable is written like this: `?name` (starts with a question mark).
- Its function is to tell the engine: "find a value that fits this position".

### 3.1 Simple Example Inside a Rule

```bayan
hybrid {
    father("Ahmad", "Mohammed").
    father("Mohammed", "Layan").

    grandfather(?grandpa, ?grandchild) :-
        father(?grandpa, ?intermediate_father),
        father(?intermediate_father, ?grandchild).
}
```

- `?grandpa`, `?grandchild`, `?intermediate_father` are logic variables.
- The rule says: **a grandfather is someone who is the father of a father of someone**.

## 4. Rules (If-Then Logic)

General rule syntax:

```bayan
result(... variables ...) :- condition1, condition2, ... .
```

- The symbol `:-` reads as: "if".
- The comma `,` means **AND** between conditions.

### 4.1 Example: Adult Person

```bayan
hybrid {
    age("Ahmad", 45).
    age("Mohammed", 20).
    age("Layan", 5).

    adult(?person) :-
        age(?person, ?years),
        ?years >= 18.
}
```

- The rule: **someone is an adult if they have a known age, and that age is ≥ 18**.
- Notice the natural mixing of logic (relations) and numerical computation (`>=`).

## 5. Queries Using the English Keyword `query`

To ask the Bayan engine about something, we write a **query**:

### 5.1 Query About Children

Assume we have in a `.by` file:

```bayan
hybrid {
    father("Ahmad", "Mohammed").
    father("Ahmad", "Sarah").
    father("Mohammed", "Layan").
}
```

Then in the Bayan interactive interface (REPL) or on a separate line we use:

```bayan
query father("Ahmad", ?child)?
```

- Here we tell the engine: **give me all possible values for `?child` such that `father("Ahmad", ?child)` is true**.
- The result will be a list of solutions like:
  - `?child = "Mohammed"`
  - `?child = "Sarah"`

### 5.2 Query Using a Rule

Using the `grandfather` rule from before:

```bayan
query grandfather(?from, ?to)?
```

- The engine returns all pairs `(grandfather, grandchild)` that make the rule true.

## 6. Summary of This Part

- We used **fully English facts** to describe a small family.
- We defined a **logic rule** that combines multiple facts (grandfather, adult).
- We executed **queries** using the English keyword `query` and English variables.
- The hybrid block can now be opened with either `hybrid` or `هجين`, with preference for `hybrid` in fully English examples.

In the next part we will build on these basics to explain:
- Complex and recursive rules,
- Lists in logic,
- How to organize the knowledge base in larger projects.

And in later parts (4–10) you will see how this logic connects to probabilities, causal networks, entities, semantic networks, and pre-language model layers (Conceptual LM).

