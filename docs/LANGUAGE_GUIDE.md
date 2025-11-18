# Bayan Language Guide - دليل لغة بيان

## Introduction - المقدمة

Bayan is a hybrid programming language that combines traditional imperative programming with logical programming. It supports both Python-like syntax and Prolog-like logical constructs.

بيان هي لغة برمجية هجينة تجمع بين البرمجة الإجرائية التقليدية والبرمجة المنطقية. تدعم كلا من بناء جملة يشبه Python والبنى المنطقية التي تشبه Prolog.

## Basic Syntax - بناء الجملة الأساسي
### Block Syntax and Indentation - صيغة الكتل والمسافات

- Bayan does NOT require indentation; block boundaries are defined by a colon `:` after control flow keywords and curly braces `{}`.
- لا تعتمد بيان على المسافات البادئة؛ تُحدَّد الكتل بالنقطتين بعد تراكيب التحكّم وبالأقواس المعقوفة `{}`.
- No semicolons; each statement goes on its own line.
- بلا فواصل منقوطة؛ كل تعليمة في سطر مستقل.

```bayan
# Blocks = colon + braces; indentation optional
if x > 0:
{
    print("positive")
}
```
Equivalent without indentation:

```bayan
if x > 0:
{
print("positive")
}
```



### Variables and Assignment - المتغيرات والإسناد

```bayan
x = 10
name = "Ahmed"
items = [1, 2, 3]
person = {name: "Ali", age: 30}
```

### Data Types - أنواع البيانات

- **Numbers**: `42`, `3.14`
- **Strings**: `"hello"`, `'world'`
- **Booleans**: `True`, `False`
- **Lists**: `[1, 2, 3]`
- **Dictionaries**: `{key: value}`
- **Logical Variables**: `?X`, `?Name`

### Control Flow - التحكم في التدفق

```bayan
# If statement
if x > 5:
{
    print("x is greater than 5")
}

# For loop
for i in range(10):
{
    print(i)
}

# While loop
while x > 0:
{
    x = x - 1
}
```

### Functions - الدوال

```bayan
def add(a, b):
{
    return a + b
}

result = add(5, 3)
```

### Temporal Constructs - البنى الزمنية

Bayan supports temporal programming constructs for time-based control flow (bilingual support).

تدعم بيان البنى الزمنية للتحكم في التدفق بناءً على الوقت (دعم ثنائي اللغة).

```bayan
# Temporal block - كتلة زمنية
temporal {
    first: x = 10,
    then: y = x * 2,
    lastly: z = y + 5
}

# Arabic version
زمنيا {
    أولا: س = 5,
    ثم: ص = س + 10,
    أخيرا: ع = ص * 2
}

# Delay - تأخير
delay 1.5 seconds
تأخير 2.0 ثواني

# Within block - كتلة خلال
within 5.0 seconds {
    result = compute()
}

خلال 3.0 ثواني {
    النتيجة = احسب()
}

# Schedule block - كتلة الجدولة
schedule every 2.0 seconds {
    check_status()
}

جدولة كل 1.0 ثانية {
    تحقق_من_الحالة()
}
```

**Keywords - الكلمات المفتاحية:**
- `temporal` / `زمنيا` - Temporal block
- `first` / `أولا` - First step
- `then` / `ثم` - Then/next step
- `lastly` / `أخيرا` - Last step
- `delay` / `تأخير` - Delay/pause
- `within` / `خلال` - Within time limit
- `schedule` / `جدولة` - Schedule
- `every` / `كل` - Every
- `seconds` / `ثانية` / `ثواني` - Seconds
- `minutes` / `دقيقة` / `دقائق` - Minutes
- `hours` / `ساعة` / `ساعات` - Hours

See [Temporal Constructs Guide](TEMPORAL_CONSTRUCTS_GUIDE.md) for complete documentation.

### Constraints & Validation - القيود والتحقق

Bayan supports Design by Contract programming with constraints and validation (bilingual support).

تدعم بيان البرمجة بنمط التصميم بالعقود مع القيود والتحقق (دعم ثنائي اللغة).

```bayan
# Where clause - شرط حيث
x = 10
y = x * 2 where x > 0

س = 15
ص = س + 5 حيث س > 10

# Requires clause - شرط يتطلب (precondition)
def divide(a, b):
    requires b != 0
    {
        return a / b
    }

def قسمة(أ, ب):
    يتطلب ب != 0
    {
        return أ / ب
    }

# Ensures clause - شرط يضمن (postcondition)
def absolute_value(x):
    ensures result >= 0
    {
        if x < 0: {
            return -x
        }
        return x
    }

# Invariant clause - شرط ثابت (loop invariant)
total = 0
for i in range(5):
    invariant total >= 0
    {
        total = total + i
    }

مجموع = 0
for عدد in range(3):
    ثابت مجموع >= 0
    {
        مجموع = مجموع + عدد
    }
```

**New Keywords:**
- `where` / `حيث` - Where clause
- `requires` / `يتطلب` / `يشترط` - Requires clause (precondition)
- `ensures` / `يضمن` / `يكفل` - Ensures clause (postcondition)
- `invariant` / `ثابت` / `ثوابت` - Invariant clause

See [Constraints Guide](CONSTRAINTS_GUIDE.md) for complete documentation.

### Pattern Matching - مطابقة الأنماط

Bayan supports advanced pattern matching with destructuring and guards (bilingual support).

تدعم بيان مطابقة الأنماط المتقدمة مع التفكيك والحراس (دعم ثنائي اللغة).

```bayan
# Match with literal patterns - مطابقة مع أنماط حرفية
x = 2
match x:
{
    case 1: { print("one") }
    case 2: { print("two") }
    default: { print("other") }
}

# List destructuring - تفكيك القوائم
point = [10, 20]
match point:
{
    case [x, y]: { sum = x + y }
}

# Dictionary destructuring - تفكيك القواميس
person = {"name": "Ali", "age": 25}
match person:
{
    case {"name": n, "age": a}: {
        print(n + " is " + str(a) + " years old")
    }
}

# Guards - الحراس
number = 15
match number:
{
    case n when n < 10: { print("small") }
    case n when n >= 10: { print("medium") }
}

# Arabic version - النسخة العربية
عدد = 5
طابق عدد:
{
    حالة ع عندما ع < 10: { print("صغير") }
    حالة ع عندما ع >= 10: { print("متوسط") }
}
```

**Keywords - الكلمات المفتاحية:**
- `match` / `طابق` - Match statement
- `case` / `حالة` - Case clause
- `default` / `افتراضي` / `افتراضية` - Default case
- `when` / `عندما` - Guard condition

See [Pattern Matching Guide](PATTERN_MATCHING_GUIDE.md) for complete documentation.

### Reactive Programming - البرمجة التفاعلية

Bayan supports reactive programming with reactive variables, watch blocks, and computed properties (bilingual support).

تدعم بيان البرمجة التفاعلية مع المتغيرات التفاعلية وكتل المراقبة والخصائص المحسوبة (دعم ثنائي اللغة).

```bayan
# Reactive variables - متغيرات تفاعلية
reactive x = 10
تفاعلي س = 20

# Watch blocks - كتل المراقبة
reactive counter = 0
watch counter:
{
    print("Counter changed: " + str(counter))
}
counter = 1  # Triggers watch block

# Computed properties - خصائص محسوبة
reactive width = 10
reactive height = 20
computed area = width * height
print("Area: " + str(area))  # 200

width = 15  # area auto-updates to 300
print("New area: " + str(area))  # 300

# Arabic version - النسخة العربية
تفاعلي طول = 5
تفاعلي عرض = 8
محسوب مساحة = طول * عرض

راقب مساحة:
{
    print("المساحة تغيرت: " + str(مساحة))
}

طول = 10  # المساحة تتحدث تلقائياً
```

**Keywords - الكلمات المفتاحية:**
- `reactive` / `تفاعلي` / `تفاعلية` - Reactive variable declaration
- `watch` / `راقب` / `مراقبة` - Watch block
- `computed` / `محسوب` / `محسوبة` - Computed property

See [Reactive Programming Guide](REACTIVE_GUIDE.md) for complete documentation.

### Pipeline and Composition Operators - عوامل الأنابيب والتركيب

Bayan supports functional programming patterns with pipeline and composition operators.

تدعم بيان أنماط البرمجة الوظيفية مع عوامل الأنابيب والتركيب.

```bayan
# Pipeline operator |> - عامل الأنابيب
def double(x):
{
    return x * 2
}

def increment(x):
{
    return x + 1
}

# Apply function to value
result1 = 5 |> double  # result1 = 10

# Chain operations
result2 = 5 |> double |> increment  # result2 = 11

# With built-in functions
length = [1, 2, 3, 4, 5] |> len  # length = 5

# Composition operator >> - عامل التركيب
# Combine functions into new function
composed = double >> increment

result3 = composed(5)  # result3 = 11
# Equivalent to: increment(double(5))

# Chain compositions
def square(x):
{
    return x * x
}

transform = double >> increment >> square
result4 = transform(3)  # result4 = 49
# Equivalent to: square(increment(double(3)))

# Combine pipeline and composition
process = double >> increment
result5 = 10 |> process  # result5 = 21
```

**Operators - العوامل:**
- `|>` - Pipeline operator (apply function to value)
- `>>` - Composition operator (combine functions)

See [Pipelines Guide](PIPELINES_GUIDE.md) for complete documentation.

## Logical Programming - البرمجة المنطقية

### Facts - الحقائق

```bayan
parent("john", "mary").
parent("mary", "susan").
```

- Probabilistic facts — حقائق احتمالية:
  - الصيغة: `fact[0.8] p(args).` داخل كتلة hybrid
  - مثال:

```bayan
hybrid {
  fact[0.9] parent("john", "mary").
}
```

### Rules - القواعد

```bayan
grandparent(?X, ?Z) :- parent(?X, ?Y), parent(?Y, ?Z).
```

### Queries - الاستعلامات

```bayan
query parent("john", ?X).
```


### Probabilistic inference — الاستدلال الاحتمالي

- حلول الاستعلامات تحافظ على «احتمال» مركّب يضرب احتمالات الحقائق عبر سلسلة الإثبات.
- بُنى مدمجة للتعامل مع الاحتمال الحالي للحل:
  - `maybe()` أو `maybe(thr)` — ينجح إذا كان احتمال الحل ≥ العتبة (الافتراضي 0.5)
  - `likely()` أو `likely(thr)` — ينجح إذا كان احتمال الحل ≥ العتبة (الافتراضي 0.8)
  - `prob_ge(thr)` — ينجح إذا كان احتمال الحل ≥ العتبة
  - `probability(?P)` — يربط المتغيّر `?P` باحتمال الحل الحالي
- ملاحظة هامّة: توجد أيضًا سوابق معرفية باسم `maybe/2` و`likely/2` في بعض الحزم (مثل KB). الاستدعاءات ذات وسيطين تُعامل كعلاقات عاديّة ولا تتداخل مع البنى المدمجة أعلاه (التي تعمل فقط بصفر أو وسيط واحد).

مثال سريع:
```bayan
hybrid {
  fact[0.9] link("a", "x").
  fact[0.3] link("a", "y").

  high(?Z)  :- link("a", ?Z), maybe().      # افتراضي 0.5
  strong(?Z) :- link("a", ?Z), likely().     # افتراضي 0.8

  query high(?Z).
  query strong(?Z).
}
```


### Collect/TopK/Argmax — جمع وترتيب حلول منطقية

- جمع كل الحلول إلى قائمة: `xs = collect ?X from predicate(...)`
- اختيار الأفضل/الأعلى K حسب درجة:
  - `best = argmax ?Z by ?S where p(...)`
  - `top = topk 3 of ?Z by ?S where p(...)`
- في حال كانت درجة `?S` غير معرّفة أو غير رقمية، سيعتمد المفسّر تلقائيًا على «احتمال الحل» المجمّع (من الاستدلال الاحتمالي) لترتيب النتائج.

مثال سريع:
```bayan
hybrid {
  fact[0.9] link("a", "x").
  fact[0.3] link("a", "y").
  best = argmax ?Z by ?S where link("a", ?Z)
  # عند غياب ?S يُستخدم احتمال الحل لترتيب النتائج
}
```

## Hybrid Blocks - الكتل الهجينة

```bayan
hybrid {
    # Traditional code
    x = 10
    y = 20

    # Logical facts
    number(10).
    number(20).

    # Mixed code
    if number(x):
    {
        print("x is a number")
    }
}
```
## Similarity/Synonyms - المترادفات/التشابه

- يمكنك التصريح عن علاقات ترادف/تقارب مباشرة بصيغة: `Head(term:score, term:score, ...)`.
- تُولَّد حقائق منطقية تلقائيًا: `similar(Head, Term, Score, "syn", "lexicon")` مع توليد عكسي (تماثل).
- تُستخدم كتعليمة مستقلة أو داخل كتلة hybrid (ويُنصَح بإنهائها بنقطة داخل hybrid مثل الحقائق).

أمثلة:

```bayan
أسد(غضنفر:0.8, هيضم:0.5)

hybrid {
  ذهب(راح:0.8).
}
```

> للمزيد من الأمثلة والخطوات التفصيلية، راجع الدرس الموسّع: [docs/similarity_tutorial_ar.md](similarity_tutorial_ar.md)
> English version: [docs/similarity_tutorial_en.md](similarity_tutorial_en.md)


## Generation & Sampling - التوليد وأخذ العينات

### Weighted Choice — الاختيار الموزون: choose / اختر
- صيغة مختصرة لاختيار عنصر واحد وفق أوزان:
- Syntax:
  - choose { "A":0.6, "B":0.3, "C":0.1 }
  - اختر { "انطلق":0.5, "سار":0.3, "ذهب":0.2 }
- تعيد قيمة واحدة من المفاتيح بحسب الأوزان.

مثال:
```bayan
hybrid {
  فعل = choose { "انطلق":0.5, "سار":0.3, "ذهب":0.2 }
  print(فعل)
}
```

### Distribution Sampling — أخذ العينات من التوزيعات: x ~ Dist(args)
- صيغة إسناد توليدي: `x ~ uniform(0,1)` أو `n ~ normal(0,1)` أو `b ~ bernoulli(0.5)`
- المفسّر يوفّر دوالًا مدمجة للتوزيعات الأساسية:
  - uniform(a,b), normal(mu,sigma), bernoulli(p)
- للتحكم بقابلية إعادة الإنتاج استخدم: `seed(N)`.

مثال:
```bayan
hybrid {
  seed(123)
  x ~ uniform(0, 1)
  n ~ normal(0, 1)
  b ~ bernoulli(0.7)
}
```

ملاحظات:
- `choose {k:w, ...}` ينخفض إلى اختيار موزون داخل المفسّر دون الحاجة لكتابة منطق يدوي.
- عامل `~` خاص بالتوليد ويعمل كإسناد: يقيّم التوزيع ويخزّن الناتج في المتغيّر على يساره.
- جميع الأمثلة تعمل داخل كتلة hybrid.


> دليل موسّع: راجع أيضًا دليل التوليد المفصّل: [docs/GENERATION_GUIDE_AR.md](GENERATION_GUIDE_AR.md)


## Templates & Match — القوالب والمطابقة

تسمح القوالب باشتقاق (استخراج) متغيّرات من نصوص، وكذلك توليد نصوص بملء حقول.

- إنشاء قالب: `tpl = template("سافر {اسم} إلى {مدينة}")`
- مطابقة: `m = match(tpl, النص)` — تعيد قاموسًا أو `None`
- توليد: `out = render(tpl, {"اسم":"خالد", "مدينة":"مكة"})`

المواضع داخل `{...}` هي حقول؛ ويمكن تزويد نمط (Regex) اختياريًا:
- `"User {name} scored {score:\\d+}"` يجعل `{score}` يقبل أرقامًا فقط.


## Concepts & Membership — المفاهيم والانتماء

تتيح لك المفاهيم تعريف مجموعات مسماة ثم استخدامها منطقيًا وتطبيقيًا:

- التصريح: `concept Animal = {"أسد","نمر","فهد"}` أو `مفهوم مدينة = {"مكة","القاهرة"}`
- تُنشَأ مجموعة وقت التشغيل باسم `Animal` لاختبارات الانتماء: `"أسد" in Animal` أو `"أسد" ∈ Animal`
- كما تُولَّد حقائق منطقية: `in_concept("Animal", "أسد").`

مثال:
```bayan
hybrid {
  concept Animal = {"أسد", "نمر"}
  ok = "أسد" ∈ Animal   # True
  query in_concept("Animal", ?X).
}
```

مثال سريع:
```bayan
hybrid {
  النص = "سافر خالد إلى مكة"
  tpl = template("سافر {اسم} إلى {مدينة}")
  m = match(tpl, النص)
  if m { print(m["اسم"]) }
  out = render(tpl, {"اسم":"سعد", "مدينة":"الرياض"})
}
```

ملاحظات:
- القيم المطابقة في القاموس تكون نصوصًا.
- إذا كان الحقل مفقودًا أثناء `render` يُترك مكانه كما في القالب الأصلي.
- المطابقة غير جشِعة افتراضيًا لكل حقل: `{اسم}` ⇐ `.+?`.




## Built-in Functions - الدوال المدمجة

- `print(value)` - Print to console
- `len(list)` - Get length
- `range(n)` - Create range
- `str(value)` - Convert to string
- `int(value)` - Convert to integer
- `float(value)` - Convert to float

## Arabic Support - دعم اللغة العربية

```bayan
hybrid {
    الاسم = "أحمد"
    العمر = 30

    شخص("أحمد", 30).
    شخص("فاطمة", 25).

    print(الاسم)
}
```

## Examples - أمثلة

### Family Relations

```bayan
hybrid {
    parent("john", "mary").
    parent("mary", "susan").

    grandparent(?X, ?Z) :- parent(?X, ?Y), parent(?Y, ?Z).

    query grandparent("john", ?X).
}
```

### Calculator

```bayan
hybrid {
    def add(a, b):
    {
        return a + b
    }

    result = add(10, 5)
    print(result)
}
```

## Comments - التعليقات

```bayan
# This is a comment
# هذا تعليق
```

## Operators - المعاملات

### Arithmetic - الحسابية
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Modulo

### Comparison - المقارنة
- `==` Equal
- `!=` Not equal
- `<` Less than
- `>` Greater than
- `<=` Less than or equal
- `>=` Greater than or equal
- `≈` or `~=` Approximate equality
  - للأعداد: مقارنة بفاصل صغير epsilon (افتراضيًا `approx_eps = 1e-2` ويمكن تغييره داخل البيئة)
  - للنصوص: إذا حُمّلت وحدة التشابه، تُستخدم `close/3` مع Kind الافتراضي `"syn"`

### Logical - المنطقية
- `and` AND
- `or` OR
- `not` NOT

### Membership - الانتماء
- `in` وكذلك الرمز `∈`
- أمثلة: `"أسد" in Animal`، أو `"أسد" ∈ Animal`

## String Operations - عمليات النصوص

```bayan
s = "hello"
s2 = s + " world"
length = len(s)
```

## List Operations - عمليات القوائم

```bayan
items = [1, 2, 3]
items.append(4)
first = items[0]
```

## Dictionary Operations - عمليات القواميس

## Entity System - نظام الكيانات (ثنائي اللغة)

يدعم بيان تعريف كيانات بحالات/خصائص وتأثيرات أفعال، بالكلمات المفتاحية الإنجليزية والعربية.

**الصيغة الجديدة الموحدة** (مُوصى بها - مفاتيح بدون علامات اقتباس):

```bayan
hybrid {
    entity Ahmed {
        states: {"hunger": 0.7},
        reactions: {
            "praise": {"sensitivity": 0.3, "effects": [{"on": "happiness", "formula": "min(value + 0.2*action_value, 1.0)"}]}
        }
    }

    entity John {
        actions: {"feed": {"effects": [{"on": "hunger", "formula": "max(value - 0.5*action_value, 0.0)"}]}}
    }

    apply John.feed(Ahmed, action_value=1.0)
}
```

**الصيغة القديمة** (لا تزال مدعومة - مفاتيح بعلامات اقتباس):

```bayan
hybrid {
    entity Ahmed {
        "states": {"hunger": 0.7},
        "actions": {"feed": {"effects": [...]}}
    }
}
```

الكلمات المفتاحية: `entity/apply` ⇄ `كيان/طبق`. انظر أيضًا: docs/ENTITY_SYSTEM_GUIDE.md


```bayan
person = {name: "Ali", age: 30}
name = person[name]
```

## Tips and Best Practices - نصائح وأفضل الممارسات

1. Use hybrid blocks to combine traditional and logical code
2. Use logical variables with `?` prefix
3. Use facts for static data
4. Use rules for relationships
5. Use queries to find solutions
6. Support Arabic identifiers for better readability



## Entity System (0..1)

See docs/ENTITY_SYSTEM_GUIDE.md for the complete guide and examples.

---

## Cognitive-Semantic Model | النموذج المعرفي-الدلالي

The Cognitive-Semantic Model is a revolutionary feature that allows you to represent ideas, meanings, and knowledge in a structured way. It's based on the concept that **an idea consists of three elements: entities (things), events (actions), and results (outcomes)**.

النموذج المعرفي-الدلالي هو ميزة ثورية تتيح لك تمثيل الأفكار والمعاني والمعرفة بطريقة منظمة. يعتمد على مفهوم أن **الفكرة تتكون من ثلاثة عناصر: كيانات (أشياء)، أحداث (أفعال)، ونتائج (مخرجات)**.

### Cognitive Entities | الكيانات المعرفية

Define entities with dynamic properties:

```bayan
cognitive_entity أرض:
{
    لون: "بني"
    حالة: "جافة"
    خصوبة: 0.2
}

# Arabic alternative
كيان_معرفي أرض:
{
    لون: "بني"
    حالة: "جافة"
}
```

### Cognitive Events | الأحداث المعرفية

Define events that transform entity states:

```bayan
cognitive_event نزول_المطر:
{
    participants: {
        "أرض": {"role": "متأثر", "degree": 1.0}
    },
    strength: 0.8,
    transform: {
        "أرض.لون": "أخضر",
        "أرض.حالة": "رطبة"
    }
}

# Trigger the event
trigger نزول_المطر

# Arabic alternative
أطلق نزول_المطر
```

### Reaction System | نظام ردود الفعل

Events can trigger other events as reactions:

```bayan
حدث_معرفي دراسة:
{
    مشاركون: {
        "طالب": {"دور": "فاعل", "درجة": 1.0}
    },
    تحويل: {
        "طالب.معرفة": 0.7
    },
    ردود_فعل: [
        {"حدث": "تخرج", "احتمال": 1.0}
    ]
}
```

### Concurrent Events | الأحداث المتزامنة

Execute multiple events simultaneously:

```bayan
concurrent يوم_عادي:
{
    events: [
        ("عمل", 0.8),
        ("لعب", 0.6)
    ]
}
```

### Linguistic Patterns | القوالب اللغوية

Define templates for expressing ideas:

```bayan
pattern فعل_ونتيجة:
{
    structure: ["فاعل", "فعل", "مفعول"],
    express: "قام {فاعل} بـ {فعل} {مفعول}"
}
```

### Ideas | الأفكار

Define high-level cognitive concepts:

```bayan
idea "الأرض الخضراء":
{
    entities: {
        "أرض": {"state": "جافة"},
        "ماء": {"state": "متوفر"}
    },
    event: "نزول_المطر",
    result: {
        "state_changes": {
            "أرض.لون": "أخضر"
        }
    }
}
```

**Keywords:** `cognitive_entity`/`كيان_معرفي`, `cognitive_event`/`حدث_معرفي`, `event`/`حدث`, `trigger`/`أطلق`, `concurrent`/`متزامن`, `pattern`/`قالب`, `idea`/`فكرة`, `participants`/`مشاركون`, `strength`/`قوة`, `transform`/`تحويل`, `reactions`/`ردود_فعل`/`ردود`, `structure`/`بنية`, `express`/`تعبير`, `entities`/`كيانات`, `result`/`نتيجة`, `state_changes`/`تغييرات_الحالة`/`تغييرات`, `linguistic_forms`/`أشكال_لغوية`/`أشكال`, `degree`/`درجة`, `role`/`دور`

**See also:** `docs/COGNITIVE_SEMANTIC_GUIDE.md` for comprehensive documentation and examples.

---

## Complete Keywords Reference - مرجع شامل للكلمات المفتاحية

For a complete, categorized list of all Bayan keywords (traditional, hybrid/logic, entity system, temporal, constraints, pattern matching, reactive, cognitive-semantic, semantic programming, existential model, spatial/temporal relations, life domain, etc.), please refer to:

للحصول على قائمة كاملة ومصنفة لجميع الكلمات المفتاحية في بيان (التقليدية، الهجينة/المنطقية، نظام الكيانات، الزمنية، القيود، مطابقة الأنماط، التفاعلية، المعرفية-الدلالية، البرمجة الدلالية، النموذج الوجودي، العلاقات المكانية/الزمنية، مجال الحياة، إلخ)، يرجى الرجوع إلى:

- **`docs/reference.md`** - Complete language reference with all keywords categorized / المرجع الكامل للغة مع جميع الكلمات المفتاحية مصنفة
- **`docs/LLM_QUICK_REFERENCE.md`** - Quick reference for LLMs with all keywords / مرجع سريع للنماذج اللغوية مع جميع الكلمات المفتاحية