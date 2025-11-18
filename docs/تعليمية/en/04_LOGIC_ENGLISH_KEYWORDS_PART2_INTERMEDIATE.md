# Logic in Bayan Language (2): Complex Rules, Recursion, Lists, and Logic Operations

> This part builds on the basics in **Part (1)**, and explains how to write more powerful rules:
> - Complex rules containing more than one condition.
> - Recursive rules (defining something in terms of itself).
> - Lists in logic.
> - Logical operations (AND / OR) between rules.
>
> We will continue using:
> - The English block `hybrid { ... }` in examples, noting once that `هجين { ... }` is the equivalent Arabic name in older code.
> - The English keyword `query` instead of `استعلام`.
> - Fully English relations, names, and variables wherever possible.

## 6. Complex Rules (More Than One Condition)

Sometimes we want to define a concept that depends on **multiple facts together**. For example: "tea_and_coffee_lover" is someone who loves tea and loves coffee.

```bayan
hybrid {
    loves_drink("Ahmad", "tea").
    loves_drink("Ahmad", "coffee").
    loves_drink("Fatima", "coffee").

    tea_and_coffee_lover(?person) :-
        loves_drink(?person, "tea"),
        loves_drink(?person, "coffee").
}
```

- The rule says: **a person is a tea_and_coffee_lover if both conditions are met**.
- The comma `,` means **AND** between conditions.

Query:

```bayan
query tea_and_coffee_lover(?who)?
```

- The result will be: `?who = "Ahmad"` only.

## 7. Recursion (Defining Something in Terms of Itself)

Recursion allows us to define concepts like: "path" between two points in a road network.

### 7.1 Example: Path Between Cities

```bayan
hybrid {
    road("Riyadh", "Qassim").
    road("Qassim", "Hail").
    road("Hail", "Jouf").

    path(?from, ?to) :-
        road(?from, ?to).

    path(?from, ?to) :-
        road(?from, ?intermediate),
        path(?intermediate, ?to).
}
```

- The first rule: there is a direct path if there is a direct "road".
- The second rule (recursive): there is a path if there is a road to an **intermediate** point, and from that point there is a path to the destination.

Query:

```bayan
query path("Riyadh", ?final_city)?
```

Returns for example:

- `?final_city = "Qassim"`
- `?final_city = "Hail"`
- `?final_city = "Jouf"`

### 7.2 Example: Ancestor

```bayan
hybrid {
    father("Ahmad", "Mohammed").
    father("Mohammed", "Layan").
    father("Layan", "Sarah").

    ancestor(?earlier, ?later) :-
        father(?earlier, ?later).

    ancestor(?earlier, ?later) :-
        father(?earlier, ?intermediate),
        ancestor(?intermediate, ?later).
}
```

- Now both `ancestor("Ahmad", "Layan")` and `ancestor("Ahmad", "Sarah")` are true.

## 8. Lists in Logic

Bayan language supports lists within logic similar to Prolog lists.

- Empty list: `[]`.
- List with elements: `[1, 2, 3]` or `["Ahmad", "Fatima"]`.
- Head/tail pattern: `[ ?head | ?tail ]`.

### 8.1 Example: Member of a List

```bayan
hybrid {
    member_of_list(?element, [ ?element | ?_ ]).

    member_of_list(?element, [ ?_ | ?rest ]) :-
        member_of_list(?element, ?rest).
}
```

Query:

```bayan
query member_of_list("Fatima", ["Ahmad", "Sarah", "Fatima"])?
```

- The engine answers that the query is **true** because "Fatima" exists in the list.

### 8.2 Example: List Length (Simplified)

```bayan
hybrid {
    list_length([], 0).

    list_length([ ?_ | ?rest ], ?length) :-
        list_length(?rest, ?rest_length),
        ?length is ?rest_length + 1.
}
```

- We use here a mix of logic and numerical computation (`is` + `+`).

Query:

```bayan
query list_length([1, 2, 3, 4], ?result)?
```

- Returns: `?result = 4`.

## 9. Logical Operations (AND / OR) Between Rules

We can express **OR** by using multiple definitions for the same rule.

### 9.1 Example: loves_sweets (person who loves some type of sweets)

```bayan
hybrid {
    loves("Ahmad", "ice_cream").
    loves("Ahmad", "bitter_coffee").
    loves("Fatima", "cake").

    loves_sweets(?person) :- loves(?person, "ice_cream").
    loves_sweets(?person) :- loves(?person, "cake").
}
```

- Here we used **two different rules** for `loves_sweets/1`:
  - Either loves ice cream.
  - Or loves cake.

Query:

```bayan
query loves_sweets(?who)?
```

- The result approximately: `?who = "Ahmad"` and `?who = "Fatima"`.

## 10. Organizing the Knowledge Base

In real projects we need to organize knowledge:

- Separate general facts (like "facts about cities") from application-specific facts.
- Separate rules specific to each domain.
- Write clear names for relations and variables so queries become understandable.

Simple example of separating two sections in the same file:

```bayan
hybrid {
    # Section: facts about cities
    city("Riyadh"). city("Qassim"). city("Hail").

    # Section: road relations
    road("Riyadh", "Qassim").
    road("Qassim", "Hail").

    # Section: path rules
    path(?from, ?to) :- road(?from, ?to).
    path(?from, ?to) :- road(?from, ?intermediate), path(?intermediate, ?to).
}
```

In the next part we will move to **the advanced level**:

- Advanced rules for collecting solutions (`findall` and relatives) but with English examples.
- Dynamic knowledge base (adding/removing facts during execution).
- Integrating logic with procedural/object-oriented parts in larger projects.

And these building blocks will be your entry later to parts 4–10 where we deal with probabilities, causal networks, entities, semantic networks, and pre-language model layers (Conceptual LM).

