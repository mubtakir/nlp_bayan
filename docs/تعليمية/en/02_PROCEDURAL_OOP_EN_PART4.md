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

