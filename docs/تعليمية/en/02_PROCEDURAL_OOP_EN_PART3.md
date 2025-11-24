# Bayan Tutorial (EN) — Part 2.C: Procedural & OOP — Part 3 (OOP)

> Quick Nav: [PART1](02_PROCEDURAL_OOP_EN_PART1.md) | [PART2](02_PROCEDURAL_OOP_EN_PART2.md) | [PART3](02_PROCEDURAL_OOP_EN_PART3.md) | [PART4](02_PROCEDURAL_OOP_EN_PART4.md)

This part introduces object-oriented programming (OOP) in Bayan: classes, inheritance, `super()`, multiple inheritance, encapsulation, and polymorphism.

## 11) Classes & Objects

Object-oriented programming in Bayan is very close to Python: you define classes with `class`, methods with `def`, and create instances by calling the class.
The `Person` class below stores a name and age and exposes an `info()` method to format them.
```bayan
hybrid {
    class Person: {
        def __init__(self, name, age): { self.name = name; self.age = age }
        def info(self): { return self.name + ": " + str(self.age) }
    }
    p = Person("Ali", 30)
    print(p.info())
}
```

## 12) Inheritance

Inheritance lets you define a general base class and then specialize it in derived classes.
`Dog` inherits from `Animal` and overrides the `speak()` method to provide a concrete implementation.
```bayan
hybrid {
    class Animal: { def speak(self): { print("...") } }
    class Dog(Animal): { def speak(self): { print("Woof") } }
    d = Dog()
    d.speak()
}
```

### 12.2 super()

The `super()` call lets a subclass delegate part of its work to the parent implementation.
In this example, `Sub.greet()` first calls `Base.greet()` and then prints an additional message.
```bayan
hybrid {
    class Base: { def greet(self): { print("Base") } }
    class Sub(Base): {
        def greet(self): { super().greet(); print("Sub") }
    }
    s = Sub(); s.greet()
}
```

### 12.3 Multiple Inheritance (Duck example)

Multiple inheritance lets a class inherit behavior from more than one parent.
`Duck` combines the abilities of `Flyable` and `Swimmable`, so a single object can both `fly()` and `swim()`.
```bayan
hybrid {
    class Flyable: { def fly(self): { print("flying") } }
    class Swimmable: { def swim(self): { print("swimming") } }
    class Duck(Flyable, Swimmable): { def __init__(self, name): { self.name = name } }

    duck = Duck("Daffy"); duck.fly(); duck.swim()
}
```

## 13) Encapsulation

Encapsulation hides internal state behind methods so that other code cannot modify it directly.
`BankAccount` stores the balance in a "private" attribute `__balance` and exposes `get_balance` / `set_balance` methods to control updates.
```bayan
hybrid {
    class BankAccount: {
        def __init__(self, balance): { self.__balance = balance }
        def get_balance(self): { return self.__balance }
        def set_balance(self, amount): { if (amount >= 0) { self.__balance = amount } }
    }
    acc = BankAccount(1000)
    print(acc.get_balance())
    acc.set_balance(2000)
    print(acc.get_balance())
}
```

## 14) Polymorphism

Polymorphism lets different classes share the same interface (method names) while providing different implementations.
Here `Rectangle` and `Circle` both implement `area()`, so we can call `area()` on either shape and get the correct result.
```bayan
hybrid {
    class Shape: { def area(self): { return 0 } }
    class Rectangle: { def __init__(self, w, h): { self.w = w; self.h = h } def area(self): { return self.w * self.h } }
    class Circle: { def __init__(self, r): { self.r = r } def area(self): { return 3.14 * self.r * self.r } }
    print(Rectangle(4, 5).area())
    print(Circle(3).area())
}
```

