# Bayan Tutorial (EN) — Part 2.A: Procedural & OOP — Part 1 (Basics)

> Quick Nav: [PART1](02_PROCEDURAL_OOP_EN_PART1.md) | [PART2](02_PROCEDURAL_OOP_EN_PART2.md) | [PART3](02_PROCEDURAL_OOP_EN_PART3.md) | [PART4](02_PROCEDURAL_OOP_EN_PART4.md)

This part introduces the basic syntax for traditional programming in Bayan.
## Contents
- Variables and basic types
- Arithmetic and logical operators
- Strings
- Lists
- Dictionaries
- Notes and tips

This part assumes you already know a bit of Python or another imperative language and want to see how the same ideas look in Bayan.

---


## 1) Variables & Types
In Bayan you create variables with simple assignments like `name = value`. The interpreter infers the type from the value, similar to Python.
This example shows integers, floats, strings, lists, and dictionaries all in one `hybrid { ... }` block.

Try changing the values (for example, `x = 100` or `name = "Bayan"`) and re-running the example to see how the output changes.


```bayan
hybrid {
    x = 10
    y = 3.14
    name = "Ahmed"
    ok = True
    items = [1, 2, 3]
    person = {name: "Ali", age: 30}
    print(str(x) + ", " + name)
}
```

## 2) Arithmetic and Logical Operators
These operators behave just like in Python: arithmetic operators work on numbers, comparison operators return `True` or `False`, and logical operators combine conditions.
The example below prints the result of simple arithmetic and a compound logical expression.


- `+ - * / %`
- Comparisons: `== != < <= > >=`
- Logical: `and or not`

```bayan
hybrid {
    a = 5
    b = 2
    print(a + b)      # 7
    print(a > b)      # True
    print((a > 1) and (b < 3))
}
```

## 3) Strings

Strings in Bayan are similar to Python strings. You can concatenate them with `+`, index into them, and call functions from the standard library.
The next example builds a new string and prints it.
```bayan
hybrid {
    s = "hello"
    s2 = s + " world"
    print(s2)
}
```

## 4) Lists

Lists in Bayan are ordered collections, just like Python lists. You can iterate over them with `for`, index into them, and call functions like `len`.
The example below prints each element, the length, and the first element.
```bayan
hybrid {
    numbers = [1, 2, 3]
    for n in (numbers) { print(n) }
    print(len(numbers))
    print(numbers[0])
}
```

## 5) Dictionaries

Dictionaries in Bayan map keys to values, similar to Python `dict`. In the example, the `person` dictionary stores a name and an age, and we read both fields.
```bayan
hybrid {
    person = {name: "Sara", age: 22}
    print(person[name])
    print(str(person[age]))
}
```

## 6) Notes
- Code blocks use `{ }` with a preceding `:` (Python-like semantics, brace-delimited blocks).
- You can mix logic programming in later parts using `hybrid { }` blocks with facts/rules/queries.

