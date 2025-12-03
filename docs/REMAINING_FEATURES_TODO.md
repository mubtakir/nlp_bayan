# 📋 الميزات المتبقية للتنفيذ | Remaining Features TODO
# Bayan Language - Features Roadmap

<div dir="rtl">

## 🎯 نظرة عامة | Overview

هذا الملف يوثق الميزات المتبقية التي يجب تنفيذها لجعل لغة البيان لغة برمجة عالمية المستوى.

This document tracks remaining features to be implemented to make Bayan a world-class programming language.

---

## 📊 حالة التقدم | Progress Status

| الفئة | Category | المنجز | المتبقي | النسبة |
|-------|----------|--------|---------|--------|
| Core Language | اللغة الأساسية | 35 | 5 | 88% |
| OOP Features | البرمجة الكائنية | 12 | 2 | 86% |
| Async/Concurrency | التزامن | 4 | 2 | 67% |
| Module System | نظام الوحدات | 3 | 1 | 75% |
| Tooling | الأدوات | 5 | 2 | 71% |
| **Total** | **المجموع** | **59** | **12** | **83%** |

### ✅ الميزات المنجزة حديثاً (2025-12-01):
- ✅ ContextVar (متغير_سياق) - متغيرات السياق
- ✅ partial (جزئي) - التطبيق الجزئي للدوال
- ✅ reduce (قلص) - تقليص القوائم
- ✅ filter (صفي) - تصفية العناصر
- ✅ map (خريطة) - تطبيق دالة على كل عنصر
- ✅ zip (ادمج) - دمج القوائم
- ✅ enumerate (رقم) - الترقيم مع الفهرس
- ✅ all/any (الكل/أي) - التحقق من الشروط

---

## 🔴 الأولوية العالية | High Priority

### 1. `*args` و `**kwargs`
**الوصف**: دعم المعاملات المتغيرة في الدوال

```bayan
# الهدف
def func(*args, **kwargs): {
    for arg in args: {
        print(arg)
    }
    for key, value in kwargs.items(): {
        print(f"{key}: {value}")
    }
}

func(1, 2, 3, name="Ahmed", age=25)
```

**الملفات المطلوب تعديلها**:
- `bayan/bayan/lexer.py` - إضافة STAR_ARGS, DOUBLE_STAR_ARGS
- `bayan/bayan/parser.py` - تعديل parse_function_def
- `bayan/bayan/ast_nodes.py` - تعديل FunctionDef node
- `bayan/bayan/traditional_interpreter.py` - تعديل visit_function_call

---

### 2. Decorators with Arguments
**الوصف**: دعم المزخرفات مع معاملات

```bayan
# الهدف
def repeat(times): {
    def decorator(func): {
        def wrapper(*args): {
            for i in range(times): {
                func(*args)
            }
        }
        return wrapper
    }
    return decorator
}

@repeat(3)
def say_hello(): {
    print("Hello!")
}
```

---

### 3. Async/Await
**الوصف**: دعم البرمجة غير المتزامنة

```bayan
# الهدف
async def fetch_data(url): {
    response = await http.get(url)
    return response.json()
}

async def main(): {
    data = await fetch_data("https://api.example.com")
    print(data)
}
```

**الكلمات المفتاحية**:
- `async` / `متزامن`
- `await` / `انتظر`

---

### 4. @staticmethod و @classmethod
**الوصف**: دعم الدوال الثابتة ودوال الصنف

```bayan
class MyClass: {
    class_var = 0
    
    @staticmethod
    def static_method(): {
        return "I'm static"
    }
    
    @classmethod
    def class_method(cls): {
        cls.class_var += 1
        return cls.class_var
    }
}
```

---

### 5. Abstract Base Classes (ABC)
**الوصف**: دعم الأصناف المجردة

```bayan
from abc import ABC, abstractmethod

class Animal(ABC): {
    @abstractmethod
    def speak(self): {
        pass
    }
}

class Dog(Animal): {
    def speak(self): {
        return "Woof!"
    }
}
```

---

## 🟡 الأولوية المتوسطة | Medium Priority

### 6. نظام الوحدات | Module System

```bayan
# my_module.by
def helper(): {
    return "Help!"
}

# main.by
import my_module
from my_module import helper

result = my_module.helper()
result2 = helper()
```

---

### 7. Multiple Inheritance
**الوصف**: دعم الوراثة المتعددة

```bayan
class A: {
    def method_a(self): {
        return "A"
    }
}

class B: {
    def method_b(self): {
        return "B"
    }
}

class C(A, B): {
    def method_c(self): {
        return "C"
    }
}
```

---

### 8. NamedTuple

```bayan
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)  # 10 20
```

---

### 9. TypedDict

```bayan
from typing import TypedDict

class Person(TypedDict): {
    name: str
    age: int
}

p: Person = {"name": "Ahmed", "age": 25}
```

---

### 10. Protocol (Structural Typing)

```bayan
from typing import Protocol

class Drawable(Protocol): {
    def draw(self): ...
}

class Circle: {
    def draw(self): {
        print("Drawing circle")
    }
}

# Circle is a Drawable because it has draw()
```

---

## 🟢 الأولوية المنخفضة | Low Priority

### 11. Metaclasses

```bayan
class Meta(type): {
    def __new__(cls, name, bases, attrs): {
        # Custom class creation logic
        return super().__new__(cls, name, bases, attrs)
    }
}

class MyClass(metaclass=Meta): {
    pass
}
```

---

### 12. Descriptors

```bayan
class Validator: {
    def __get__(self, obj, objtype=None): {
        return self.value
    }

    def __set__(self, obj, value): {
        self.validate(value)
        self.value = value
    }
}
```

---

### 13. __slots__

```bayan
class Point: {
    __slots__ = ["x", "y"]

    def __init__(self, x, y): {
        self.x = x
        self.y = y
    }
}
```

---

### 14. Context Variables

```bayan
from contextvars import ContextVar

user_id: ContextVar[int] = ContextVar("user_id")

def process_request(): {
    token = user_id.set(42)
    try: {
        # Process
        pass
    } finally: {
        user_id.reset(token)
    }
}
```

---

## 🛠️ أدوات التطوير | Development Tools

### 15. Unit Testing Framework

```bayan
import unittest

class TestMath(unittest.TestCase): {
    def test_addition(self): {
        self.assertEqual(1 + 1, 2)
    }

    def test_subtraction(self): {
        self.assertEqual(5 - 3, 2)
    }
}

unittest.main()
```

---

### 16. Type Checking (Static)

```bayan
# bayan --check file.by
# يفحص الأنواع دون تشغيل الكود

def add(a: int, b: int) -> int: {
    return a + b
}

# سيعطي تحذير:
result = add("hello", 5)  # Type error!
```

---

### 17. Debugger Integration

```bayan
import pdb

def buggy_function(): {
    x = 10
    pdb.set_trace()  # Breakpoint
    y = x / 0
}
```

---

### 18. Profiler

```bayan
import cProfile

def slow_function(): {
    total = 0
    for i in range(1000000): {
        total += i
    }
    return total
}

cProfile.run("slow_function()")
```

---

## 📚 المكتبة القياسية | Standard Library

### 19. Regular Expressions

```bayan
import re

pattern = r"\d+"
text = "There are 123 apples and 456 oranges"
matches = re.findall(pattern, text)
print(matches)  # ["123", "456"]
```

---

### 20. JSON Handling

```bayan
import json

data = {"name": "Ahmed", "age": 25}
json_str = json.dumps(data)
parsed = json.loads(json_str)
```

---

### 21. HTTP Client

```bayan
import http

response = http.get("https://api.example.com/data")
data = response.json()
```

---

### 22. Database Connectivity

```bayan
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
```

---

## 📋 خطة التنفيذ | Implementation Plan

### المرحلة 1 (أسبوعين)
1. ✅ *args, **kwargs
2. ✅ Decorators with arguments
3. ✅ @staticmethod, @classmethod

### المرحلة 2 (أسبوعين)
4. ✅ Abstract Base Classes
5. ✅ Module System (import/export)
6. ✅ Multiple Inheritance

### المرحلة 3 (أسبوعين)
7. ✅ Async/Await
8. ✅ NamedTuple
9. ✅ TypedDict

### المرحلة 4 (أسبوعين)
10. ✅ Unit Testing Framework
11. ✅ Type Checking
12. ✅ Standard Library Extensions

---

</div>

## 📝 ملاحظات التنفيذ | Implementation Notes

عند تنفيذ كل ميزة، تأكد من:
1. إضافة الكلمات المفتاحية العربية والإنجليزية
2. كتابة اختبارات شاملة
3. تحديث الوثائق
4. إضافة أمثلة في مجلد `examples/`

When implementing each feature, ensure:
1. Add Arabic and English keywords
2. Write comprehensive tests
3. Update documentation
4. Add examples in `examples/` folder

---

**تاريخ الإنشاء | Created**: 2025-12-01
**آخر تحديث | Last Updated**: 2025-12-01


