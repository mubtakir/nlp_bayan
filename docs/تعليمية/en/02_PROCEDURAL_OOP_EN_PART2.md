# Bayan Tutorial (EN) — Part 2.B: Procedural & OOP — Part 2 (Control Flow & Functions)

> Quick Nav: [PART1](02_PROCEDURAL_OOP_EN_PART1.md) | [PART2](02_PROCEDURAL_OOP_EN_PART2.md) | [PART3](02_PROCEDURAL_OOP_EN_PART3.md) | [PART4](02_PROCEDURAL_OOP_EN_PART4.md)

This part focuses on control flow in Bayan: conditionals, loops, functions, and simple error handling.

## 7) If / Elif / Else

Conditional statements control which block of code runs based on a Boolean condition.
Here we check whether `x` is greater than, equal to, or less than `5` and print a different message in each branch.
```bayan
hybrid {
    x = 10
    if x > 5: { print("x > 5") }
    elif x == 5: { print("x == 5") }
    else: { print("x < 5") }
}
```

## 8) Loops: for / while

Bayan supports both `for` and `while` loops. `for` is great when you know how many iterations you need, and `while` is better for open-ended conditions.
In this example, we loop forward with `range(3)` and then count down with a `while` loop.
```bayan
hybrid {
    for i in range(3): { print(i) }
    i = 2
    while i >= 0: { print(i); i = i - 1 }
}
```

## 9) Functions

Functions let you package reusable logic with parameters. Bayan uses Python-style `def` syntax, but the body of each function lives inside `{ }`.
The example defines a simple `add` function and a `greet` function with a default argument, then calls both.
```bayan
hybrid {
    def add(a, b): { return a + b }
    def greet(name="World"): { print("Hello, " + name) }
    print(add(2, 3))
    greet("Bayan")
}
```

## 10) Exceptions

Exceptions let you handle error cases, such as division by zero, without crashing the rest of the program.
In this example we check `b == 0` inside the `div` function, print an error message, and return `None` instead of raising a hard error.
```bayan
hybrid {
    def div(a, b): {
        if b == 0: { print("Error: division by zero"); return None }
        return a / b
    }
    print(str(div(10, 2)))
    print(str(div(5, 0)))
}
```

