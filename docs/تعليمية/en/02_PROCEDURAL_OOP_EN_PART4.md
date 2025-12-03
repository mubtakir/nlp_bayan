# Bayan Tutorial (EN) — Part 2.D: Procedural & OOP — Part 4 (Advanced)

> Quick Nav: [PART1](02_PROCEDURAL_OOP_EN_PART1.md) | [PART2](02_PROCEDURAL_OOP_EN_PART2.md) | [PART3](02_PROCEDURAL_OOP_EN_PART3.md) | [PART4](02_PROCEDURAL_OOP_EN_PART4.md)

This part covers advanced Python-style features available in Bayan: decorators, generators, async/await, context managers, and flexible argument passing.

## 15) Decorators

Decorators wrap one function with another to add behavior before or after the original call.
Here `my_decorator` prints messages around the call to `square`, but you could also use this pattern for logging, timing, or access control.
```bayan
hybrid {
    def my_decorator(fn): {
        def wrapper(x): { print("before"); r = fn(x); print("after"); return r }
        return wrapper
    }
    @my_decorator
    def square(n): { return n * n }
    print(str(square(3)))
}
```

## 16) Generators

Generators are functions that yield a sequence of values over time instead of returning a single value.
`count_up_to` yields numbers from `1` to `n`, and the `for` loop consumes them one by one.
```bayan
hybrid {
    def count_up_to(n): {
        i = 1
        while (i <= n) { yield i; i = i + 1 }
    }
    for v in (count_up_to(3)) { print(v) }
}
```

## 17) Async / Await

Bayan mirrors Python's `async` / `await` syntax for asynchronous functions.
This minimal example only defines an async function; running it requires an event loop provided by the host environment.
```bayan
hybrid {
    async def fetch(x): { return x + 1 }
    # Example only; actual event loop usage depends on host integration
}
```

## 18) Context Managers

Context managers manage a resource for a limited block of time and guarantee cleanup.
Here `FileManager` prints messages when entering and exiting the `with` block and exposes a `write` method.
```bayan
hybrid {
    class FileManager: {
        def __enter__(self): { print("enter"); return self }
        def __exit__(self, exc_type, exc, tb): { print("exit"); return False }
        def write(self, msg): { print("write: " + msg) }
    }
    with FileManager() as f: { f.write("hello") }
}
```

## 19) *args / **kwargs

`*args` collects positional arguments into a tuple and `**kwargs` collects keyword arguments into a dictionary.
The example below shows a simple `sum_all` that adds any number of arguments and a `print_info` helper that prints keyword arguments.
```bayan
hybrid {
    def sum_all(*args): {
        s = 0
        for v in (args) { s = s + v }
        return s
    }
    def print_info(**kwargs): { print(str(kwargs)) }
    print(str(sum_all(1, 2, 3)))
    print_info(name="Ali", age=30)
}
```

---

## 20) New Advanced Features (2025)

### 20.1 Match/Case Pattern Matching
```bayan
hybrid {
    x = 2
    match x: {
        case 1: { print("one") }
        case 2: { print("two") }
        case _: { print("other") }
    }
}
```

### 20.2 Enums
```bayan
hybrid {
    enum Color: {
        RED = 1
        GREEN = 2
        BLUE = 3
    }

    print(Color.RED)  # 1
}
```

### 20.3 Ternary Operator
```bayan
hybrid {
    x = 10
    result = "big" if x > 5 else "small"
    print(result)  # big
}
```

### 20.4 Tuple Unpacking
```bayan
hybrid {
    a, b, c = 1, 2, 3
    print(a, b, c)  # 1 2 3

    # Swap values
    a, b = b, a
}
```

### 20.5 Spread Operator for Lists
```bayan
hybrid {
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [*list1, *list2]
    print(list3)  # [1, 2, 3, 4, 5, 6]
}
```

### 20.6 Dict Spread
```bayan
hybrid {
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3}
    merged = {**dict1, **dict2}
    print(merged)  # {"a": 1, "b": 2, "c": 3}
}
```

### 20.7 Negative Step Slicing
```bayan
hybrid {
    nums = [1, 2, 3, 4, 5]
    print(nums[::-1])  # [5, 4, 3, 2, 1]
}
```

### 20.8 Global Variables
```bayan
hybrid {
    counter = 0

    def increment(): {
        global counter
        counter = counter + 1
    }

    increment()
    increment()
    print(counter)  # 2
}
```

### 20.9 Nullish Coalescing
```bayan
hybrid {
    x = None
    y = x ?? 10
    print(y)  # 10
}
```

### 20.10 Chained Comparisons
```bayan
hybrid {
    x = 5
    if 0 < x < 10: {
        print("x is between 0 and 10")
    }
}
```

### 20.11 F-Strings
```bayan
hybrid {
    name = "Ahmed"
    age = 25
    print(f"Name: {name}, Age: {age}")
}
```

### 20.12 Enhanced Exceptions
```bayan
hybrid {
    def divide(a, b): {
        if b == 0: {
            raise ValueError("Cannot divide by zero")
        }
        return a / b
    }

    try: {
        result = divide(10, 0)
    } except ValueError as e: {
        print("Error:", str(e))
    }
}
```

---

> **Note**: For more details, see [ADVANCED_FEATURES_2025.md](../../ADVANCED_FEATURES_2025.md)

> Quick Nav: [PART1](02_PROCEDURAL_OOP_EN_PART1.md) | [PART2](02_PROCEDURAL_OOP_EN_PART2.md) | [PART3](02_PROCEDURAL_OOP_EN_PART3.md) | [PART4](02_PROCEDURAL_OOP_EN_PART4.md)
