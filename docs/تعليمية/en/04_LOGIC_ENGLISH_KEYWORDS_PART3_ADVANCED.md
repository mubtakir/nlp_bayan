# Logic in Bayan Language (3): Advanced Logic and Dynamic Knowledge Base

> In this part we move to a deeper level:
> - **Collecting all solutions** to a logic query in a list.
> - **Counting the number of solutions** in a logical way.
> - **Modifying the knowledge base during execution** (adding/removing facts).
>
> We will continue using:
> - The `hybrid { ... }` block (the English form preferred in examples).
> - The English keyword `query` in queries.
> - Fully English relation names, variables, and data.
>
> Technical note: There are some built-in tools in the interpreter with their original English names like `findall`, `bagof`, `setof`, `assertz`, `retract`. They currently have no Arabic equivalents in the interpreter, so we will use them **inside English rules** as fixed technical names, and build clear English interfaces around them.

## 11. Collecting Solutions in a List (Concept of "All Who Meet the Condition")

Sometimes we don't want just one solution, but **all solutions** in one place (a list). For example: everyone who loves tea.

```bayan
hybrid {
    loves_drink("Ahmad", "tea").
    loves_drink("Ahmad", "coffee").
    loves_drink("Fatima", "tea").
    loves_drink("Layan", "juice").

    all_tea_lovers(?person_list) :-
        findall(?person,
                loves_drink(?person, "tea"),
                ?person_list).
}
query all_tea_lovers(?names)?
```

- The rule `all_tea_lovers/1` is an **English interface** around the technical tool `findall`.
- `findall` takes:
  - The variable whose values we want to collect (`?person`).
  - The condition to verify (`loves_drink(?person, "tea")`).
  - The result list variable (`?person_list`).
- The query returns for example: `?names = ["Ahmad", "Fatima"]`.

## 12. Counting the Number of Solutions (How Many Meet the Condition?)

We can use the same idea with the list_length/2 function we defined in the previous part.

```bayan
hybrid {
    loves_tea("Ahmad"). loves_tea("Fatima"). loves_tea("Sarah").

    all_who_love_tea(?list) :-
        findall(?person, loves_tea(?person), ?list).

    count_tea_lovers(?count) :-
        all_who_love_tea(?list),
        list_length(?list, ?count).
}
query count_tea_lovers(?result)?
```

- First we collect all who meet the condition in a list.
- Then we use the `list_length/2` rule to count the elements.
- The result: `?result = 3` in the previous example.

## 13. Dynamic Knowledge Base (Adding/Removing Facts)

One of the powerful features in Bayan is the ability to **change the knowledge base during execution**:
- Add a new fact.
- Remove an existing fact.

### 13.1 Example: Who is in the Library Now?

Suppose we want to represent people currently present in a library.

```bayan
hybrid {
    in_library("Ahmad").
    in_library("Fatima").

    add_person_to_library(?person) :-
        assertz(in_library(?person)).

    remove_person_from_library(?person) :-
        retract(in_library(?person)).
}
```

- `add_person_to_library/1` is an English interface that calls `assertz` to add a fact at the end of the knowledge base.
- `remove_person_from_library/1` is an English interface around `retract` to remove one fact matching the pattern.

Practical usage (in interactive sequence):

1. Query who is currently present:
   ```bayan
   query in_library(?who)?
   ```
2. Add a new person:
   ```bayan
   add_person_to_library("Sarah").
   ```
3. Query again:
   ```bayan
   query in_library(?who)?
   ```
4. Remove a person:
   ```bayan
   remove_person_from_library("Ahmad").
   ```

This way you can build a simple **state system** based on logic facts that are updated during execution.

## 14. Summary of This Part

- We learned how to collect all solutions to a logic query in a **list** using English interfaces over the `findall` tool.
- We used that to count **the number of solutions** using `list_length/2`.
- We learned how to make the knowledge base **dynamic** via English interfaces (`add_person_to_library`, `remove_person_from_library`) built on the `assertz` and `retract` tools.

In the following parts we will move to more distinctive and innovative features in Bayan:
- Probabilistic reasoning and uncertainty.
- Causal networks.
- Entities, equations, and linguistic operators.
- The idea–event–result model.
- Synonyms/similarity, semantic networks, and Conceptual LM layers before the language model.

