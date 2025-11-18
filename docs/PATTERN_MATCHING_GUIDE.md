# Pattern Matching Guide - دليل مطابقة الأنماط

## Overview - نظرة عامة

Pattern matching is a powerful feature in Bayan that allows you to match values against patterns and extract data from complex structures. It provides a more expressive and safer alternative to traditional if-else chains.

مطابقة الأنماط هي ميزة قوية في لغة البيان تسمح لك بمطابقة القيم مع الأنماط واستخراج البيانات من الهياكل المعقدة. توفر بديلاً أكثر تعبيراً وأماناً لسلاسل if-else التقليدية.

## Keywords - الكلمات المفتاحية

| English | Arabic | Meaning |
|---------|--------|---------|
| `match` | `طابق` | Match statement |
| `case` | `حالة` | Case clause |
| `default` | `افتراضي` / `افتراضية` | Default case |
| `when` | `عندما` | Guard condition |

## Basic Syntax - البنية الأساسية

### English Syntax

```bayan
match value:
{
    case pattern1: { body1 }
    case pattern2: { body2 }
    default: { default_body }
}
```

### Arabic Syntax

```bayan
طابق قيمة:
{
    حالة نمط1: { جسم1 }
    حالة نمط2: { جسم2 }
    افتراضي: { جسم_افتراضي }
}
```

## Pattern Types - أنواع الأنماط

### 1. Literal Patterns - الأنماط الحرفية

Match exact values:

```bayan
x = 2
match x:
{
    case 1: { print("one") }
    case 2: { print("two") }
    case 3: { print("three") }
}
```

Arabic version:

```bayan
س = 1
طابق س:
{
    حالة 1: { print("واحد") }
    حالة 2: { print("اثنان") }
    حالة 3: { print("ثلاثة") }
}
```

### 2. Variable Patterns - أنماط المتغيرات

Bind the matched value to a variable:

```bayan
x = 42
match x:
{
    case n: { print("Value is: " + str(n)) }
}
```

### 3. List Patterns - أنماط القوائم

Destructure lists and extract elements:

```bayan
point = [10, 20]
match point:
{
    case [x, y]: { 
        print("x = " + str(x) + ", y = " + str(y))
    }
}
```

Arabic version:

```bayan
نقطة = [5, 15]
طابق نقطة:
{
    حالة [س, ص]: { 
        print("س = " + str(س) + ", ص = " + str(ص))
    }
}
```

### 4. Dictionary Patterns - أنماط القواميس

Destructure dictionaries and extract values:

```bayan
person = {"name": "Ali", "age": 25}
match person:
{
    case {"name": n, "age": a}: { 
        print(n + " is " + str(a) + " years old")
    }
}
```

Arabic version:

```bayan
شخص = {"اسم": "فاطمة", "عمر": 30}
طابق شخص:
{
    حالة {"اسم": اسم, "عمر": عمر}: { 
        print(اسم + " عمرها " + str(عمر) + " سنة")
    }
}
```

## Guards - الحراس

Guards allow you to add additional conditions to patterns using the `when` keyword:

```bayan
number = 15
match number:
{
    case n when n < 10: { print("small") }
    case n when n >= 10 and n < 100: { print("medium") }
    case n when n >= 100: { print("large") }
}
```

Arabic version:

```bayan
عدد = 5
طابق عدد:
{
    حالة ع عندما ع < 10: { print("صغير") }
    حالة ع عندما ع >= 10 and ع < 100: { print("متوسط") }
    حالة ع عندما ع >= 100: { print("كبير") }
}
```

## Default Case - الحالة الافتراضية

The `default` case matches any value if no other case matches:

```bayan
x = 99
match x:
{
    case 1: { print("one") }
    case 2: { print("two") }
    default: { print("other") }
}
```

Arabic version:

```bayan
س = 99
طابق س:
{
    حالة 1: { print("واحد") }
    حالة 2: { print("اثنان") }
    افتراضي: { print("أخرى") }
}
```

## Complex Patterns - الأنماط المعقدة

You can nest patterns to match complex structures:

```bayan
data = {"type": "point", "coords": [100, 200]}
match data:
{
    case {"type": t, "coords": [x, y]}: {
        print(t + " at (" + str(x) + ", " + str(y) + ")")
    }
}
```

## Use Cases - حالات الاستخدام

### 1. Data Classification - تصنيف البيانات

```bayan
def classify_number(n):
{
    result = ""
    match n:
    {
        case x when x < 0: { result = "negative" }
        case 0: { result = "zero" }
        case x when x > 0 and x < 10: { result = "small positive" }
        case x when x >= 10: { result = "large positive" }
    }
    return result
}
```

### 2. Data Extraction - استخراج البيانات

```bayan
user = {"name": "Ahmed", "role": "admin", "permissions": ["read", "write"]}
match user:
{
    case {"role": "admin", "permissions": perms}: {
        print("Admin with permissions: " + str(perms))
    }
    case {"role": "user"}: {
        print("Regular user")
    }
}
```

### 3. Coordinate Processing - معالجة الإحداثيات

```bayan
def process_point(point):
{
    match point:
    {
        case [0, 0]: { return "origin" }
        case [x, 0]: { return "on x-axis" }
        case [0, y]: { return "on y-axis" }
        case [x, y] when x == y: { return "on diagonal" }
        case [x, y]: { return "general point" }
    }
}
```

### 4. State Machine - آلة الحالات

```bayan
state = "running"
event = "stop"

match [state, event]:
{
    case ["idle", "start"]: { new_state = "running" }
    case ["running", "pause"]: { new_state = "paused" }
    case ["running", "stop"]: { new_state = "stopped" }
    case ["paused", "resume"]: { new_state = "running" }
    default: { new_state = state }
}
```

## Error Handling - معالجة الأخطاء

If no case matches and there's no default case, a `ValueError` is raised:

```bayan
x = 99
match x:
{
    case 1: { print("one") }
    case 2: { print("two") }
}
# Raises: ValueError: No matching case for value: 99
```

## Best Practices - أفضل الممارسات

1. **Always include a default case** when not all values are covered
   - دائماً قم بتضمين حالة افتراضية عندما لا تكون جميع القيم مغطاة

2. **Use guards for complex conditions** instead of nested if statements
   - استخدم الحراس للشروط المعقدة بدلاً من عبارات if المتداخلة

3. **Keep patterns simple** - complex patterns can be hard to read
   - حافظ على الأنماط بسيطة - الأنماط المعقدة يمكن أن تكون صعبة القراءة

4. **Order cases from specific to general** - more specific patterns should come first
   - رتب الحالات من الخاص إلى العام - الأنماط الأكثر تحديداً يجب أن تأتي أولاً

## Examples - أمثلة

See `examples/pattern_matching_demo.by` for comprehensive examples.

انظر `examples/pattern_matching_demo.by` للحصول على أمثلة شاملة.

## Related Features - الميزات ذات الصلة

- **Constraints & Validation**: Use `where` clauses for simple value validation
- **Temporal Constructs**: Combine with `temporal` blocks for time-based pattern matching
- **Logical Programming**: Pattern matching complements Prolog-style unification

## Technical Notes - ملاحظات تقنية

- Pattern matching is evaluated top-to-bottom
- The first matching case is executed
- Variables in patterns create new bindings in the case body scope
- List patterns require exact length match
- Dictionary patterns only check for specified keys (extra keys are ignored)
- Guards are evaluated after pattern matching succeeds

---

**Version**: 2025-11-13
**Status**: Stable ✅


