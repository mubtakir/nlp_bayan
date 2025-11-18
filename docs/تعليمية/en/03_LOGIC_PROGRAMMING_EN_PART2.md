# Bayan Tutorial (EN) — Part 3.B: Logic Programming — Part 2 (Rules, Recursion, Lists)

> Quick Nav: [PART1](03_LOGIC_PROGRAMMING_EN_PART1.md) | [PART2](03_LOGIC_PROGRAMMING_EN_PART2.md) | [PART3](03_LOGIC_PROGRAMMING_EN_PART3.md) | [PART4](03_LOGIC_PROGRAMMING_EN_PART4.md)

This part goes deeper into logic programming with recursive and composite rules, path finding, list processing, and logical properties.

## 6) Composite Rules

Composite rules let you define a predicate in terms of itself and other predicates.
The two `ancestor/2` rules say that an ancestor is either a direct parent or a parent of an ancestor, giving a recursive definition.
```bayan
hybrid {
    rule ancestor(X,Y) :- parent(X,Y).
    rule ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y).
}
```

## 7) Recursion (path)

Recursive rules let you express reachability, transitive closure, and other repeated patterns.
Here `path(X,Y)` is true if there is a direct edge or a chain of edges from `X` to `Y`.
```bayan
hybrid {
    fact edge(a, b). fact edge(b, c). fact edge(c, d).
    rule path(X,Y) :- edge(X,Y).
    rule path(X,Y) :- edge(X,Z), path(Z,Y).
}

query path(a, ?N).
```

## 8) Lists in Logic

Lists can also appear inside logic predicates.
The classic `list_member/2` example shows how pattern matching and recursion traverse a list to check for membership.
```bayan
hybrid {
    rule list_member(X, [X|_]).
    rule list_member(X, [_|T]) :- list_member(X, T).
}

query list_member(2, [1,2,3]).
```

## 9) Logical Operations

Logical rules can encode properties such as "tea lover" or "coffee lover" based on more primitive facts.
Here we define `tea_lover/1` and `coffee_lover/1` in terms of the `likes/2` facts, then query for all people that satisfy each predicate.
```bayan
hybrid {
    fact likes("Ali", tea). fact likes("Sara", coffee).
    rule tea_lover(X)   :- likes(X, tea).
    rule coffee_lover(X):- likes(X, coffee).
}

query tea_lover(?P).
query coffee_lover(?P).
```

