# 🤖 Bayan Language - Complete Guide for AI Models
# لغة البيان - الدليل الشامل للنماذج اللغوية

**Version**: 0.6.0 | **Date**: 2025-12-06

> ⚠️ **IMPORTANT**: This is the ONLY file you need to understand Bayan and write correct code.

---

## 🎯 What is Bayan?

**Bayan (البيان)** is the world's first **true hybrid programming language** that combines:
- ✅ **Procedural Programming** (like Python)
- ✅ **Object-Oriented Programming** (like Java)
- ✅ **Logic Programming** (like Prolog)
- ✅ **Full Bilingual Support** (Arabic + English keywords)

---

## ⭐ KEY FEATURES (READ CAREFULLY!)

### 1. 🔥 NO INDENTATION DEPENDENCY!
Unlike Python, Bayan uses **braces `{ }`** for blocks, NOT indentation.

```bayan
# ✅ CORRECT - braces define the block
if (x > 5) {
    print("big")
}

# ✅ ALSO CORRECT - same line
if (x > 5) { print("big") }
```

### 2. 🔥 COLON BEFORE BRACES!
Functions, classes, and control structures need `:` before `{`

```bayan
# ✅ CORRECT
def add(a, b): {
    return a + b
}

class Person: {
    def __init__(self, name): {
        self.name = name
    }
}

# ❌ WRONG - missing colon
def add(a, b) {
    return a + b
}
```

### 3. 🔥 EVERYTHING INSIDE `hybrid { }`!
All Bayan code MUST be wrapped in `hybrid { }`:

```bayan
hybrid {
    # Your code here
    print("Hello Bayan!")
}
```

### 4. 🔥 BILINGUAL KEYWORDS!
You can use Arabic OR English keywords:

| English | العربية | Usage |
|---------|---------|-------|
| `def` | `دالة` / `عرّف` | Function definition |
| `class` | `صنف` / `فئة` | Class definition |
| `if` | `إذا` / `لو` | Condition |
| `else` | `وإلا` | Else branch |
| `elif` | `وإلا_إذا` | Else if |
| `for` | `لكل` / `كرر` | For loop |
| `while` | `طالما` / `بينما` | While loop |
| `return` | `أرجع` / `ارجع` | Return value |
| `print` | `اطبع` | Print output |
| `True` | `صحيح` | Boolean true |
| `False` | `خطأ` | Boolean false |
| `None` | `لاشيء` / `عدم` | Null value |
| `and` | `و` | Logical AND |
| `or` | `أو` | Logical OR |
| `not` | `ليس` / `لا` | Logical NOT |
| `self` | `ذاتي` / `نفسي` | Self reference |
| `try` | `حاول` | Try block |
| `except` | `استثنِ` / `عدا` | Except block |
| `import` | `استورد` | Import module |

---

## 📝 SYNTAX RULES (10 Golden Rules)

1. **Wrap ALL code in `hybrid { }`**
2. **Use `:` before `{` in def, class, if, for, while**
3. **Use `{ }` for ALL blocks (not indentation)**
4. **Logic facts end with `.`** (e.g., `fact parent("أحمد", "محمد").`)
5. **Logic variables start with `?`** (e.g., `?X`, `?Name`)
6. **Strings use `"` or `'`**
7. **Comments use `#`**
8. **Lists use `[ ]`**
9. **Dicts use `{ key: value }`**
10. **Parentheses `( )` for conditions are REQUIRED**

---

## 🔤 COMPLETE SYNTAX EXAMPLES

### Variables & Types
```bayan
hybrid {
    # Numbers
    x = 10
    y = 3.14

    # Strings
    name = "أحمد"
    greeting = 'Hello'

    # Boolean
    active = True  # or صحيح

    # Lists
    numbers = [1, 2, 3, 4, 5]

    # Dictionary
    person = {"name": "محمد", "age": 25}
}
```

### Functions
```bayan
hybrid {
    # English
    def add(a, b): {
        return a + b
    }

    # Arabic
    دالة اجمع(أ, ب): {
        أرجع أ + ب
    }

    # With default parameters
    def greet(name, msg="مرحباً"): {
        print(msg + " " + name)
    }

### Control Flow
```bayan
hybrid {
    x = 10

    # If-elif-else
    if (x > 10) {
        print("كبير")
    } elif (x == 10) {
        print("متساوي")
    } else {
        print("صغير")
    }

    # For loop
    for i in (range(5)) {
        print(i)
    }

    # For each in list
    names = ["أحمد", "محمد", "علي"]
    for name in (names) {
        print(name)
    }

    # While loop
    count = 0
    while (count < 5) {
        print(count)
        count = count + 1
    }
}
```

### Logic Programming (Prolog-style)
```bayan
hybrid {
    # Facts - end with .
    fact parent("إبراهيم", "إسماعيل").
    fact parent("إبراهيم", "إسحاق").
    fact parent("إسحاق", "يعقوب").

    # Rules - use ?Variables
    rule grandparent(?X, ?Z): {
        parent(?X, ?Y),
        parent(?Y, ?Z)
    }

    # Query
    query grandparent("إبراهيم", ?Who)
}
```

### Exception Handling
```bayan
hybrid {
    try {
        x = 10 / 0
    } except (ZeroDivisionError) {
        print("لا يمكن القسمة على صفر!")
    }
}
```

### Modules & Import
```bayan
hybrid {
    import math

    result = math.sqrt(16)
    print(result)  # 4.0
}
```

---

## ❌ COMMON ERRORS & FIXES

### Error 1: Missing `hybrid { }`
```bayan
# ❌ WRONG
def test(): {
    print("hello")
}

# ✅ CORRECT
hybrid {
    def test(): {
        print("hello")
    }
}
```

### Error 2: Missing colon before `{`
```bayan
# ❌ WRONG
def add(a, b) {
    return a + b
}

# ✅ CORRECT
def add(a, b): {
    return a + b
}
```

### Error 3: Using indentation instead of braces
```bayan
# ❌ WRONG (Python style)
if x > 5:
    print("big")

# ✅ CORRECT (Bayan style)
if (x > 5) {
    print("big")
}
```

### Error 4: Missing parentheses in conditions
```bayan
# ❌ WRONG
if x > 5 {
    print("big")
}

# ✅ CORRECT
if (x > 5) {
    print("big")
}
```

### Error 5: Missing `.` in logic facts
```bayan
# ❌ WRONG
fact parent("أحمد", "محمد")

# ✅ CORRECT
fact parent("أحمد", "محمد").
```

---

## 🎨 COMPLETE WORKING EXAMPLES

### Example 1: Calculator
```bayan
hybrid {
    class Calculator: {
        def add(self, a, b): {
            return a + b
        }

        def subtract(self, a, b): {
            return a - b
        }

        def multiply(self, a, b): {
            return a * b
        }

        def divide(self, a, b): {
            if (b == 0) {
                return "خطأ: القسمة على صفر"
            }
            return a / b
        }
    }

    calc = Calculator()
    print(calc.add(10, 5))       # 15
    print(calc.multiply(4, 3))   # 12
}
```

### Example 2: Factorial (Recursive)
```bayan
hybrid {
    def factorial(n): {
        if (n <= 1) {
            return 1
        }
        return n * factorial(n - 1)
    }

    print(factorial(5))  # 120
}
```

### Example 3: Arabic Full Example
```bayan
hybrid {
    صنف شخص: {
        دالة __init__(ذاتي, الاسم, العمر): {
            ذاتي.الاسم = الاسم
            ذاتي.العمر = العمر
        }

        دالة تحية(ذاتي): {
            اطبع("مرحباً، أنا " + ذاتي.الاسم)
        }

        دالة هل_بالغ(ذاتي): {
            إذا (ذاتي.العمر >= 18) {
                أرجع صحيح
            } وإلا {
                أرجع خطأ
            }
        }
    }

    أحمد = شخص("أحمد", 25)
    أحمد.تحية()

    إذا (أحمد.هل_بالغ()) {
        اطبع("بالغ")
    }
}
```

### Example 4: Family Tree (Logic)
```bayan
hybrid {
    # Define facts
    fact أب("إبراهيم", "إسماعيل").
    fact أب("إبراهيم", "إسحاق").
    fact أب("إسحاق", "يعقوب").
    fact أب("يعقوب", "يوسف").

    # Define rules
    rule جد(?X, ?Z): {
        أب(?X, ?Y),
        أب(?Y, ?Z)
    }

    rule سلف(?X, ?Y): {
        أب(?X, ?Y)
    }

    rule سلف(?X, ?Z): {
        أب(?X, ?Y),
        سلف(?Y, ?Z)
    }

    # Query
    query جد("إبراهيم", ?حفيد)
    # Result: ?حفيد = "يعقوب"
}
```

### Example 5: List Operations
```bayan
hybrid {
    numbers = [1, 2, 3, 4, 5]

    # Sum
    total = 0
    for n in (numbers) {
        total = total + n
    }
    print("المجموع: " + str(total))

    # Filter even
    even = []
    for n in (numbers) {
        if (n % 2 == 0) {
            even.append(n)
        }
    }
    print("الأزواج: " + str(even))

    # Map (double)
    doubled = []
    for n in (numbers) {
        doubled.append(n * 2)
    }
    print("المضاعف: " + str(doubled))
}
```

---

## 🧠 ADVANCED FEATURES

### 1. Dual Brain Architecture
Bayan has a unique conceptual architecture with linguistic equations:
- `Subject (فاعل) + Verb (فعل) + Object (مفعول)`
- Derived from Arabic linguistic theory (النحو العربي)

### 2. Extensions Layer (v0.6.0)
| Extension | Description |
|-----------|-------------|
| `AICodeAssistant` | Smart coding assistant |
| `DialectAdapter` | Arabic dialect support |
| `EquationVisualizer` | Visualize linguistic equations |
| `BayanTutor` | Interactive learning system |
| `IntelligentDialogueSystem` | NLP dialogue |

### 3. Web IDE
Bayan has a web-based IDE at `web_ide/` with:
- Code editor with syntax highlighting
- Run, Save, Load functionality
- AI assistant integration

---

## 📋 QUICK REFERENCE TABLE

| Task | Bayan Code |
|------|------------|
| Print | `print("text")` or `اطبع("نص")` |
| Variable | `x = 10` |
| Function | `def name(): { }` or `دالة اسم(): { }` |
| Class | `class Name: { }` or `صنف اسم: { }` |
| If | `if (cond) { }` or `إذا (شرط) { }` |
| For | `for x in (list) { }` or `لكل x في (قائمة) { }` |
| While | `while (cond) { }` or `طالما (شرط) { }` |
| Return | `return value` or `أرجع قيمة` |
| Logic Fact | `fact name(args).` |
| Logic Rule | `rule name(args): { conditions }` |
| Query | `query predicate(args)` |

---

## 🔗 RESOURCES

- **GitHub**: https://github.com/mubtakir/nlp_bayan
- **Examples**: `examples/` folder (74 working examples)
- **Tutorials**: `tutorials/` folder (42 tutorials)
- **Web IDE**: `web_ide/` folder

---

## ✅ CHECKLIST FOR WRITING BAYAN CODE

- [ ] Wrapped in `hybrid { }`?
- [ ] Using `:` before `{` in functions/classes?
- [ ] Using `{ }` for blocks (not indentation)?
- [ ] Parentheses `( )` around conditions?
- [ ] Logic facts end with `.`?
- [ ] Logic variables start with `?`?

---

**Remember**: Bayan is NOT Python! Use braces, not indentation!
