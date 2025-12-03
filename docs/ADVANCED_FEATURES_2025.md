# 🚀 الميزات المتقدمة في لغة البيان 2025
# Advanced Features in Bayan Language 2025

<div dir="rtl">

## 📋 فهرس المحتويات | Table of Contents

1. [نظام الأنواع | Type System](#1-نظام-الأنواع--type-system)
2. [إعادة تحميل العوامل | Operator Overloading](#2-إعادة-تحميل-العوامل--operator-overloading)
3. [الفهم المتقدم | Comprehensions](#3-الفهم-المتقدم--comprehensions)
4. [مدراء السياق | Context Managers](#4-مدراء-السياق--context-managers)
5. [الخصائص | Properties](#5-الخصائص--properties)
6. [أصناف البيانات | Dataclasses](#6-أصناف-البيانات--dataclasses)
7. [الدوال المجهولة والإغلاق | Lambda & Closures](#7-الدوال-المجهولة-والإغلاق--lambda--closures)
8. [التأكيدات | Assert](#8-التأكيدات--assert)
9. [دمج القيم الفارغة | Nullish Coalescing](#9-دمج-القيم-الفارغة--nullish-coalescing)
10. [السلسلة الاختيارية | Optional Chaining](#10-السلسلة-الاختيارية--optional-chaining)
11. [المقارنات المتسلسلة | Chained Comparisons](#11-المقارنات-المتسلسلة--chained-comparisons)
12. [تفكيك المجموعات | Tuple Unpacking](#12-تفكيك-المجموعات--tuple-unpacking)
13. [عامل الإسناد التعبيري | Walrus Operator](#13-عامل-الإسناد-التعبيري--walrus-operator)
14. [مطابقة الأنماط | Match/Case](#14-مطابقة-الأنماط--matchcase)
15. [التعدادات | Enums](#15-التعدادات--enums)
16. [عامل النشر | Spread Operator](#16-عامل-النشر--spread-operator)
17. [التقطيع المتقدم | Advanced Slicing](#17-التقطيع-المتقدم--advanced-slicing)
18. [نشر القواميس | Dict Spread](#18-نشر-القواميس--dict-spread)
19. [النطاقات | Global/Nonlocal](#19-النطاقات--globalnonlocal)
20. [العامل الثلاثي | Ternary Operator](#20-العامل-الثلاثي--ternary-operator)
21. [المولدات | Generators](#21-المولدات--generators)
22. [F-Strings](#22-f-strings)
23. [الاستثناءات المحسنة | Enhanced Exceptions](#23-الاستثناءات-المحسنة--enhanced-exceptions)

---

## 1. نظام الأنواع | Type System

### العربية
```bayan
# تعليقات الأنواع
دالة جمع(أ: عدد_صحيح، ب: عدد_صحيح) -> عدد_صحيح: {
    ارجع أ + ب
}

# أنواع القوائم
قائمة_أرقام: قائمة[عدد_صحيح] = [1، 2، 3]

# أنواع القواميس
بيانات: قاموس[نص، عدد_صحيح] = {"عمر": 25}
```

### English
```bayan
# Type annotations
def add(a: int, b: int) -> int: {
    return a + b
}

# List types
numbers: list[int] = [1, 2, 3]

# Dict types
data: dict[str, int] = {"age": 25}
```

---

## 2. إعادة تحميل العوامل | Operator Overloading

### العربية
```bayan
صنف متجه: {
    دالة __init__(self، س، ص): {
        self.س = س
        self.ص = ص
    }
    
    دالة __add__(self، آخر): {
        ارجع متجه(self.س + آخر.س، self.ص + آخر.ص)
    }
    
    دالة __str__(self): {
        ارجع f"متجه({self.س}، {self.ص})"
    }
}

م1 = متجه(1، 2)
م2 = متجه(3، 4)
م3 = م1 + م2
اطبع(م3)  # متجه(4، 6)
```

### English
```bayan
class Vector: {
    def __init__(self, x, y): {
        self.x = x
        self.y = y
    }
    
    def __add__(self, other): {
        return Vector(self.x + other.x, self.y + other.y)
    }
    
    def __str__(self): {
        return f"Vector({self.x}, {self.y})"
    }
}

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Vector(4, 6)
```

---

## 3. الفهم المتقدم | Comprehensions

### List Comprehension
```bayan
# العربية
أرقام = [س * 2 لكل س في range(5)]

# English
numbers = [x * 2 for x in range(5)]
```

### Dict Comprehension
```bayan
# العربية
مربعات = {س: س * س لكل س في range(5)}

# English
squares = {x: x * x for x in range(5)}
```

### Set Comprehension
```bayan
# العربية
فريدة = {س % 3 لكل س في range(10)}

# English
unique = {x % 3 for x in range(10)}
```

---

## 4. مدراء السياق | Context Managers

### العربية
```bayan
مع فتح("ملف.txt"، "r") كـ ملف: {
    محتوى = ملف.read()
    اطبع(محتوى)
}
# الملف يُغلق تلقائياً
```

### English
```bayan
with open("file.txt", "r") as f: {
    content = f.read()
    print(content)
}
# File is automatically closed
```

---

## 5. الخصائص | Properties

```bayan
class Circle: {
    def __init__(self, radius): {
        self._radius = radius
    }

    @property
    def radius(self): {
        return self._radius
    }

    @radius.setter
    def radius(self, value): {
        if value < 0: {
            raise ValueError("Radius cannot be negative")
        }
        self._radius = value
    }
}
```

---

## 6. أصناف البيانات | Dataclasses

```bayan
@dataclass
class Person: {
    name: str
    age: int
    city: str = "Unknown"
}

p = Person("Ahmed", 25)
print(p.name)  # Ahmed
print(p.age)   # 25
print(p.city)  # Unknown
```

---

## 7. الدوال المجهولة والإغلاق | Lambda & Closures

### Lambda
```bayan
# دالة مجهولة
square = lambda x: x * x
print(square(5))  # 25

# مع filter
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # [2, 4]
```

### Closures
```bayan
def make_multiplier(n): {
    def multiplier(x): {
        return x * n
    }
    return multiplier
}

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))  # 10
print(triple(5))  # 15
```

---

## 8. التأكيدات | Assert

```bayan
# العربية
تأكد س > 0، "القيمة يجب أن تكون موجبة"

# English
assert x > 0, "Value must be positive"

# مثال عملي
def divide(a, b): {
    assert b != 0, "Cannot divide by zero"
    return a / b
}
```

---

## 9. دمج القيم الفارغة | Nullish Coalescing

```bayan
# إذا كانت القيمة None، استخدم القيمة البديلة
name = user.name ?? "Anonymous"

# مثال
x = None
y = x ?? 10
print(y)  # 10

a = 5
b = a ?? 10
print(b)  # 5
```

---

## 10. السلسلة الاختيارية | Optional Chaining

```bayan
# الوصول الآمن للخصائص
city = user?.address?.city

# مثال
class User: {
    def __init__(self): {
        self.address = None
    }
}

user = User()
# بدون optional chaining سيحدث خطأ
# city = user.address.city  # Error!

# مع optional chaining
city = user?.address?.city  # None بدلاً من خطأ
```

---

## 11. المقارنات المتسلسلة | Chained Comparisons

```bayan
# بدلاً من: x > 0 and x < 10
if 0 < x < 10: {
    print("x is between 0 and 10")
}

# أمثلة أخرى
a = 5
print(1 < a < 10)    # True
print(1 < a < 3)     # False
print(1 <= a <= 5)   # True
```

---

## 12. تفكيك المجموعات | Tuple Unpacking

```bayan
# تفكيك بسيط
a, b, c = 1, 2, 3

# تفكيك من قائمة
x, y, z = [10, 20, 30]

# تبديل القيم
a, b = b, a

# في حلقة for
items = [("a", 1), ("b", 2), ("c", 3)]
for key, value in items: {
    print(key, value)
}
```

---

## 13. عامل الإسناد التعبيري | Walrus Operator

```bayan
# تعيين وفحص في نفس الوقت
if (n := len(items)) > 10: {
    print(f"Too many items: {n}")
}

# في حلقة while
while (line := input()) != "quit": {
    print(f"You entered: {line}")
}
```

---

## 14. مطابقة الأنماط | Match/Case

```bayan
# العربية
x = 2
طابق x: {
    حالة 1: { اطبع("واحد") }
    حالة 2: { اطبع("اثنان") }
    حالة _: { اطبع("آخر") }
}

# English
x = 2
match x: {
    case 1: { print("one") }
    case 2: { print("two") }
    case _: { print("other") }
}

# مطابقة متقدمة
match point: {
    case (0, 0): { print("Origin") }
    case (x, 0): { print(f"On x-axis at {x}") }
    case (0, y): { print(f"On y-axis at {y}") }
    case (x, y): { print(f"Point at ({x}, {y})") }
}
```

---

## 15. التعدادات | Enums

```bayan
# العربية
تعداد اللون: {
    أحمر = 1
    أخضر = 2
    أزرق = 3
}

# English
enum Color: {
    RED = 1
    GREEN = 2
    BLUE = 3
}

# الاستخدام
my_color = Color.RED
print(my_color)  # 1

match my_color: {
    case Color.RED: { print("Stop!") }
    case Color.GREEN: { print("Go!") }
    case Color.BLUE: { print("Sky") }
}
```

---

## 16. عامل النشر | Spread Operator

```bayan
# نشر القوائم
a = [1, 2, 3]
b = [4, 5, 6]
c = [*a, *b]
print(c)  # [1, 2, 3, 4, 5, 6]

# دمج مع عناصر إضافية
d = [0, *a, 10, *b, 20]
print(d)  # [0, 1, 2, 3, 10, 4, 5, 6, 20]

# في استدعاء الدوال
def sum_three(x, y, z): {
    return x + y + z
}
args = [1, 2, 3]
result = sum_three(*args)
print(result)  # 6
```

---

## 17. التقطيع المتقدم | Advanced Slicing

```bayan
nums = [1, 2, 3, 4, 5]

# عكس القائمة
print(nums[::-1])  # [5, 4, 3, 2, 1]

# خطوة سالبة
print(nums[4:1:-1])  # [5, 4, 3]

# كل عنصرين بالعكس
print(nums[::-2])  # [5, 3, 1]

# نسخ عكسية
reversed_copy = nums[::-1]
```

---

## 18. نشر القواميس | Dict Spread

```bayan
# دمج القواميس
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(merged)  # {"a": 1, "b": 2, "c": 3, "d": 4}

# مع قيم إضافية
extended = {"x": 0, **dict1, "y": 5, **dict2, "z": 10}

# تجاوز القيم
base = {"name": "Unknown", "age": 0}
updated = {**base, "name": "Ahmed"}
print(updated)  # {"name": "Ahmed", "age": 0}
```

---

## 19. النطاقات | Global/Nonlocal

### Global
```bayan
# العربية
عداد = 0
دالة زيادة(): {
    عام عداد
    عداد = عداد + 1
}
زيادة()
زيادة()
اطبع(عداد)  # 2

# English
counter = 0
def increment(): {
    global counter
    counter = counter + 1
}
increment()
increment()
print(counter)  # 2
```

### Nonlocal
```bayan
def outer(): {
    x = 10
    def inner(): {
        nonlocal x
        x = x + 5
    }
    inner()
    return x
}
print(outer())  # 15
```

---

## 20. العامل الثلاثي | Ternary Operator

```bayan
# الصيغة: value_if_true if condition else value_if_false

x = 10
result = "big" if x > 5 else "small"
print(result)  # big

# العربية
العمر = 20
الحالة = "بالغ" اذا العمر >= 18 والا "قاصر"
اطبع(الحالة)  # بالغ

# متداخل
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)  # B
```

---

## 21. المولدات | Generators

```bayan
# دالة مولدة
def count_up(n): {
    i = 0
    while i < n: {
        yield i
        i = i + 1
    }
}

# الاستخدام
for num in count_up(5): {
    print(num)
}
# 0, 1, 2, 3, 4

# مولد فيبوناتشي
def fibonacci(limit): {
    a, b = 0, 1
    while a < limit: {
        yield a
        a, b = b, a + b
    }
}

for fib in fibonacci(100): {
    print(fib)
}
```

---

## 22. F-Strings

```bayan
# النصوص المنسقة
name = "Ahmed"
age = 25
print(f"Name: {name}, Age: {age}")

# العربية
الاسم = "أحمد"
العمر = 25
اطبع(f"الاسم: {الاسم}، العمر: {العمر}")

# تعبيرات داخل F-string
x = 5
print(f"Square of {x} is {x * x}")  # Square of 5 is 25

# تنسيق الأرقام
pi = 3.14159
print(f"Pi = {pi:.2f}")  # Pi = 3.14
```

---

## 23. الاستثناءات المحسنة | Enhanced Exceptions

```bayan
# استثناءات مدمجة
# Exception, ValueError, TypeError, KeyError, IndexError
# AttributeError, RuntimeError, ZeroDivisionError
# FileNotFoundError, IOError, StopIteration
# AssertionError, NotImplementedError, NameError

# رفع استثناء محدد
def divide(a, b): {
    if b == 0: {
        raise ValueError("Cannot divide by zero")
    }
    return a / b
}

# التقاط استثناء محدد
try: {
    result = divide(10, 0)
} except ValueError as e: {
    print(f"Caught: {e}")
}

# التقاط متعدد
try: {
    risky_operation()
} except ValueError as e: {
    print("Value error")
} except TypeError as e: {
    print("Type error")
} except Exception as e: {
    print("Other error")
} finally: {
    print("Cleanup")
}
```

---

</div>

## 📝 ملاحظات | Notes

- جميع هذه الميزات تدعم الكلمات المفتاحية العربية والإنجليزية
- All features support both Arabic and English keywords
- يمكن استخدام هذه الميزات داخل كتلة `hybrid { }` أو `هجين { }`
- These features can be used within `hybrid { }` or `هجين { }` blocks

---

**تاريخ آخر تحديث | Last Updated**: 2025-12-01


