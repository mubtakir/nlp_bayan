# Constraints & Validation Guide - دليل القيود والتحقق

## Overview - نظرة عامة

This guide covers the **Constraints & Validation** features in Bayan, which enable **Design by Contract** programming. These features help you write more robust code by explicitly stating preconditions, postconditions, and invariants.

يغطي هذا الدليل ميزات **القيود والتحقق** في لغة البيان، والتي تمكّن من البرمجة بنمط **التصميم بالعقود**. تساعدك هذه الميزات على كتابة كود أكثر قوة من خلال تحديد الشروط المسبقة والشروط اللاحقة والثوابت بشكل صريح.

---

## 1. Where Clauses - شروط حيث

### Description - الوصف

**Where clauses** allow you to add constraints to expressions. If the constraint is not satisfied, an error is raised.

تسمح لك **شروط حيث** بإضافة قيود على التعابير. إذا لم يتم استيفاء القيد، يتم رفع خطأ.

### Syntax - الصيغة

```bayan
# English
expression where condition

# Arabic
تعبير حيث شرط
```

### Keywords - الكلمات المفتاحية

| English | Arabic | Meaning |
|---------|--------|---------|
| `where` | `حيث` | Where clause |

### Examples - أمثلة

```bayan
# English example
x = 10
y = x * 2 where x > 0  # OK: x is positive
z = x * 2 where x < 0  # ERROR: condition fails

# Arabic example
س = 15
ص = س + 5 حيث س > 10  # صحيح: س أكبر من 10
ع = س + 5 حيث س < 0   # خطأ: الشرط فاشل
```

### Use Cases - حالات الاستخدام

- ✅ Input validation
- ✅ Filtering data
- ✅ Ensuring preconditions inline
- ✅ التحقق من المدخلات
- ✅ تصفية البيانات
- ✅ ضمان الشروط المسبقة مباشرة

---

## 2. Requires Clauses - شروط يتطلب

### Description - الوصف

**Requires clauses** specify **preconditions** that must be true before a function executes. If a precondition fails, a `ContractError` is raised.

تحدد **شروط يتطلب** **الشروط المسبقة** التي يجب أن تكون صحيحة قبل تنفيذ الدالة. إذا فشل شرط مسبق، يتم رفع `ContractError`.

### Syntax - الصيغة

```bayan
# English
def function_name(params):
    requires condition1
    requires condition2
    {
        # function body
    }

# Arabic
def اسم_الدالة(معاملات):
    يتطلب شرط1
    يتطلب شرط2
    {
        # جسم الدالة
    }
```

### Keywords - الكلمات المفتاحية

| English | Arabic 1 | Arabic 2 | Meaning |
|---------|----------|----------|---------|
| `requires` | `يتطلب` | `يشترط` | Requires clause (precondition) |

### Examples - أمثلة

```bayan
# English example
def divide(a, b):
    requires b != 0
    {
        return a / b
    }

result = divide(10, 2)  # OK
result = divide(10, 0)  # ERROR: ContractError

# Arabic example
def قسمة(أ, ب):
    يتطلب ب != 0
    {
        return أ / ب
    }

نتيجة = قسمة(20, 4)  # صحيح
نتيجة = قسمة(20, 0)  # خطأ: ContractError

# Multiple requires
def safe_sqrt(x):
    requires x >= 0
    requires x <= 1000
    {
        return pow(x, 0.5)
    }
```

### Use Cases - حالات الاستخدام

- ✅ Validate function arguments
- ✅ Prevent invalid states
- ✅ Document function assumptions
- ✅ التحقق من معاملات الدالة
- ✅ منع الحالات غير الصالحة
- ✅ توثيق افتراضات الدالة

---

## 3. Ensures Clauses - شروط يضمن

### Description - الوصف

**Ensures clauses** specify **postconditions** that must be true after a function executes. The special variable `result` holds the return value.

تحدد **شروط يضمن** **الشروط اللاحقة** التي يجب أن تكون صحيحة بعد تنفيذ الدالة. المتغير الخاص `result` يحمل القيمة المرجعة.

### Syntax - الصيغة

```bayan
# English
def function_name(params):
    ensures condition_with_result
    {
        # function body
    }

# Arabic
def اسم_الدالة(معاملات):
    يضمن شرط_مع_result
    {
        # جسم الدالة
    }
```

### Keywords - الكلمات المفتاحية

| English | Arabic 1 | Arabic 2 | Meaning |
|---------|----------|----------|---------|
| `ensures` | `يضمن` | `يكفل` | Ensures clause (postcondition) |

### Special Variables - المتغيرات الخاصة

- `result` - holds the return value of the function (يحمل القيمة المرجعة من الدالة)

### Examples - أمثلة

```bayan
# English example
def absolute_value(x):
    ensures result >= 0
    {
        if x < 0: {
            return -x
        }
        return x
    }

val = absolute_value(-5)  # OK: result is 5
val = absolute_value(7)   # OK: result is 7

# Arabic example
def جذر_تربيعي(عدد):
    يتطلب عدد >= 0
    يضمن result >= 0
    {
        return pow(عدد, 0.5)
    }

نتيجة = جذر_تربيعي(25)  # صحيح: result هو 5.0

# Combined requires and ensures
def safe_divide(a, b):
    requires b != 0
    requires a >= 0
    ensures result >= 0
    {
        return a / b
    }
```

### Use Cases - حالات الاستخدام

- ✅ Validate function output
- ✅ Ensure correctness guarantees
- ✅ Document function behavior
- ✅ التحقق من مخرجات الدالة
- ✅ ضمان صحة النتائج
- ✅ توثيق سلوك الدالة

---

## 4. Invariant Clauses - شروط ثابت

### Description - الوصف

**Invariant clauses** specify conditions that must remain true throughout loop execution. They are checked at the start and end of each iteration.

تحدد **شروط ثابت** الشروط التي يجب أن تبقى صحيحة طوال تنفيذ الحلقة. يتم فحصها في بداية ونهاية كل تكرار.

### Syntax - الصيغة

```bayan
# English - For loop
for var in iterable:
    invariant condition1
    invariant condition2
    {
        # loop body
    }

# English - While loop
while condition:
    invariant condition1
    invariant condition2
    {
        # loop body
    }

# Arabic - For loop
for متغير in قابل_للتكرار:
    ثابت شرط1
    ثابت شرط2
    {
        # جسم الحلقة
    }

# Arabic - While loop
while شرط:
    ثابت شرط1
    ثابت شرط2
    {
        # جسم الحلقة
    }
```

### Keywords - الكلمات المفتاحية

| English | Arabic 1 | Arabic 2 | Meaning |
|---------|----------|----------|---------|
| `invariant` | `ثابت` | `ثوابت` | Invariant clause |

### Examples - أمثلة

```bayan
# English - For loop
total = 0
for i in range(5):
    invariant total >= 0
    {
        total = total + i
    }

# English - While loop with multiple invariants
counter = 0
sum_val = 0
while counter < 5:
    invariant sum_val >= 0
    invariant counter >= 0
    {
        sum_val = sum_val + counter
        counter = counter + 1
    }

# Arabic - For loop
مجموع = 0
for عدد in range(3):
    ثابت مجموع >= 0
    {
        مجموع = مجموع + عدد
    }

# Complex example with factorial
def factorial(n):
    requires n >= 0
    ensures result >= 1
    {
        result_val = 1
        i = 1
        while i <= n:
            invariant result_val >= 1
            invariant i >= 1
            {
                result_val = result_val * i
                i = i + 1
            }
        return result_val
    }
```

### Use Cases - حالات الاستخدام

- ✅ Verify loop correctness
- ✅ Detect logic errors early
- ✅ Document loop assumptions
- ✅ التحقق من صحة الحلقات
- ✅ اكتشاف الأخطاء المنطقية مبكراً
- ✅ توثيق افتراضات الحلقة

---

## 5. Complete Example - مثال كامل

```bayan
# Factorial with full contracts
def factorial(n):
    requires n >= 0
    requires n <= 10
    ensures result >= 1
    {
        result_val = 1
        i = 1
        while i <= n:
            invariant result_val >= 1
            invariant i >= 1
            invariant i <= n + 1
            {
                result_val = result_val * i
                i = i + 1
            }
        return result_val
    }

# Usage
result = factorial(5)  # OK: returns 120
result = factorial(-1) # ERROR: requires clause fails
result = factorial(20) # ERROR: requires clause fails
```

---

## Summary - الملخص

### New Keywords - الكلمات المفتاحية الجديدة

| Feature | English | Arabic | Purpose |
|---------|---------|--------|---------|
| Where clause | `where` | `حيث` | Add constraints to expressions |
| Requires clause | `requires` | `يتطلب`, `يشترط` | Specify preconditions |
| Ensures clause | `ensures` | `يضمن`, `يكفل` | Specify postconditions |
| Invariant clause | `invariant` | `ثابت`, `ثوابت` | Specify loop invariants |

### Benefits - الفوائد

1. **Improved Code Quality** - جودة كود أفضل
2. **Early Error Detection** - اكتشاف الأخطاء مبكراً
3. **Better Documentation** - توثيق أفضل
4. **Formal Verification** - التحقق الرسمي
5. **Bilingual Support** - دعم ثنائي اللغة

---

## See Also - انظر أيضاً

- [Language Guide](LANGUAGE_GUIDE.md) - دليل اللغة
- [Temporal Constructs Guide](TEMPORAL_CONSTRUCTS_GUIDE.md) - دليل البنى الزمنية
- [Examples](../examples/constraints_demo.by) - أمثلة

