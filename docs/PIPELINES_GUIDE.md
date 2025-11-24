# Pipeline and Composition Operators Guide
# دليل عوامل الأنابيب والتركيب

## Overview - نظرة عامة

Bayan supports functional programming patterns through pipeline and composition operators, enabling clean and readable data transformation chains.

تدعم بيان أنماط البرمجة الوظيفية من خلال عوامل الأنابيب والتركيب، مما يتيح سلاسل تحويل بيانات نظيفة وقابلة للقراءة.

---

## Pipeline Operator (`|>`) - عامل الأنابيب

### Syntax - البنية

```bayan
value |> function
```

### Description - الوصف

The pipeline operator `|>` takes a value on the left and applies a function on the right. It's equivalent to calling the function with the value as an argument.

عامل الأنابيب `|>` يأخذ قيمة على اليسار ويطبق دالة على اليمين. وهو مكافئ لاستدعاء الدالة مع القيمة كمعامل.

**Equivalence - التكافؤ:**
```bayan
x |> f    ≡    f(x)
```

### Examples - أمثلة

#### Basic Pipeline - أنابيب أساسية

```bayan
def double(x):
{
    return x * 2
}

result = 5 |> double  # result = 10
```

#### Chained Pipelines - أنابيب متسلسلة

```bayan
def double(x):
{
    return x * 2
}

def increment(x):
{
    return x + 1
}

# Chain multiple operations
result = 5 |> double |> increment  # result = 11
# Equivalent to: increment(double(5))
```

#### Pipeline with Built-in Functions - أنابيب مع دوال مدمجة

```bayan
numbers = [1, 2, 3, 4, 5]
length = numbers |> len  # length = 5

text = "Hello"
text_length = text |> len  # text_length = 5
```

#### Complex Expressions - تعبيرات معقدة

```bayan
def square(x):
{
    return x * x
}

x = 3
y = 7
result = (x + y) |> square  # result = 100
# Equivalent to: square(3 + 7) = square(10) = 100
```

---

## Composition Operator (`>>`) - عامل التركيب

### Syntax - البنية

```bayan
function1 >> function2
```

### Description - الوصف

The composition operator `>>` combines two functions into a new function. The resulting function applies the first function, then applies the second function to the result.

عامل التركيب `>>` يدمج دالتين في دالة جديدة. الدالة الناتجة تطبق الدالة الأولى، ثم تطبق الدالة الثانية على النتيجة.

**Equivalence - التكافؤ:**
```bayan
(f >> g)(x)    ≡    g(f(x))
```

### Examples - أمثلة

#### Basic Composition - تركيب أساسي

```bayan
def double(x):
{
    return x * 2
}

def increment(x):
{
    return x + 1
}

# Create composed function
composed = double >> increment

# Use composed function
result = composed(5)  # result = 11
# Equivalent to: increment(double(5))
```

#### Chained Composition - تركيب متسلسل

```bayan
def double(x):
{
    return x * 2
}

def increment(x):
{
    return x + 1
}

def square(x):
{
    return x * x
}

# Compose multiple functions
transform = double >> increment >> square

result = transform(3)  # result = 49
# Equivalent to: square(increment(double(3)))
#                = square(increment(6))
#                = square(7)
#                = 49
```

#### Reusable Compositions - تركيبات قابلة لإعادة الاستخدام

```bayan
def add_ten(x):
{
    return x + 10
}

def multiply_by_three(x):
{
    return x * 3
}

# Create reusable composed function
transform = add_ten >> multiply_by_three

# Use multiple times
result1 = transform(5)   # result1 = 45
result2 = transform(10)  # result2 = 60
result3 = transform(0)   # result3 = 30
```

---

## Combining Pipeline and Composition
## دمج الأنابيب والتركيب

You can combine both operators for powerful data transformations:

يمكنك دمج كلا العاملين لتحويلات بيانات قوية:

```bayan
def double(x):
{
    return x * 2
}

def increment(x):
{
    return x + 1
}

# Create composed function
transform = double >> increment

# Use in pipeline
result = 10 |> transform  # result = 21

# Process multiple values
values = [1, 2, 3, 4, 5]
for v in (values) {
    transformed = v |> transform
    print(str(v) + " -> " + str(transformed))
}
# Output:
# 1 -> 3
# 2 -> 5
# 3 -> 7
# 4 -> 9
# 5 -> 11
```

---

## Use Cases - حالات الاستخدام

### 1. Data Processing Pipelines - أنابيب معالجة البيانات

```bayan
def filter_positive(lst):
{
    result = []
    for item in (lst) {
        if (item > 0) {
            result = result + [item]
        }
    }
    return result
}

def sum_list(lst):
{
    total = 0
    for item in (lst) {
        total = total + item
    }
    return total
}

data = [-2, 5, -1, 8, 3, -4, 7]
total = data |> filter_positive |> sum_list  # total = 23
```

### 2. String Transformations - تحويلات النصوص

```bayan
def add_greeting(name):
{
    return "Hello, " + name
}

def add_exclamation(text):
{
    return text + "!"
}

message = "Alice" |> add_greeting |> add_exclamation
# message = "Hello, Alice!"
```

### 3. Mathematical Transformations - التحويلات الرياضية

```bayan
def celsius_to_fahrenheit(c):
{
    return (c * 9 / 5) + 32
}

def round_to_int(x):
{
    return int(x)
}

temp_c = 25
temp_f = temp_c |> celsius_to_fahrenheit |> round_to_int
# temp_f = 77
```

### 4. Function Factories - مصانع الدوال

```bayan
def add(x):
{
    def adder(y):
    {
        return x + y
    }
    return adder
}

def multiply(x):
{
    def multiplier(y):
    {
        return x * y
    }
    return multiplier
}

# Create specialized functions
add_five = add(5)
double = multiply(2)

# Compose them
transform = add_five >> double

result = transform(10)  # result = 30
# (10 + 5) * 2 = 15 * 2 = 30
```

---

## Best Practices - أفضل الممارسات

### 1. Use Pipelines for Sequential Operations
### استخدم الأنابيب للعمليات المتسلسلة

**Good - جيد:**
```bayan
result = data |> filter |> transform |> aggregate
```

**Avoid - تجنب:**
```bayan
result = aggregate(transform(filter(data)))
```

### 2. Use Composition for Reusable Transformations
### استخدم التركيب للتحويلات القابلة لإعادة الاستخدام

**Good - جيد:**
```bayan
normalize = filter >> transform >> aggregate
result1 = data1 |> normalize
result2 = data2 |> normalize
```

### 3. Keep Functions Pure
### اجعل الدوال نقية

Functions used in pipelines and compositions should be pure (no side effects):

الدوال المستخدمة في الأنابيب والتركيبات يجب أن تكون نقية (بدون تأثيرات جانبية):

**Good - جيد:**
```bayan
def double(x):
{
    return x * 2
}
```

**Avoid - تجنب:**
```bayan
counter = 0
def double_with_side_effect(x):
{
    counter = counter + 1  # Side effect!
    return x * 2
}
```

### 4. Name Composed Functions Meaningfully
### سمِّ الدوال المركبة بأسماء ذات معنى

**Good - جيد:**
```bayan
validate_and_normalize = validate >> normalize
process_user_input = trim >> lowercase >> validate_and_normalize
```

**Avoid - تجنب:**
```bayan
f1 = validate >> normalize
f2 = trim >> lowercase >> f1
```

---

## Comparison with Other Languages
## المقارنة مع لغات أخرى

### Elixir
```elixir
# Elixir
result = data |> filter() |> transform() |> aggregate()
```

```bayan
# Bayan
result = data |> filter |> transform |> aggregate
```

### F#
```fsharp
// F#
let transform = double >> increment >> square
```

```bayan
# Bayan
transform = double >> increment >> square
```

### JavaScript (with libraries)
```javascript
// JavaScript (Ramda)
const transform = R.compose(square, increment, double);
```

```bayan
# Bayan
transform = double >> increment >> square
```

---

## Summary - الملخص

Pipeline and composition operators in Bayan provide:
- **Pipeline operator `|>`** for applying functions to values
- **Composition operator `>>`** for combining functions
- Clean, readable code for data transformations
- Functional programming patterns

عوامل الأنابيب والتركيب في بيان توفر:
- **عامل الأنابيب `|>`** لتطبيق الدوال على القيم
- **عامل التركيب `>>`** لدمج الدوال
- كود نظيف وقابل للقراءة لتحويلات البيانات
- أنماط البرمجة الوظيفية

These features enable building expressive, maintainable data processing pipelines.

هذه الميزات تمكّن من بناء أنابيب معالجة بيانات معبرة وقابلة للصيانة.



