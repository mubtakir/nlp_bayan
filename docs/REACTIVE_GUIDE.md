# Reactive Programming Guide - دليل البرمجة التفاعلية

## Overview - نظرة عامة

Reactive programming in Bayan allows you to create variables that automatically trigger updates when their values change. This enables building responsive, event-driven applications with minimal boilerplate code.

البرمجة التفاعلية في بيان تسمح لك بإنشاء متغيرات تُطلق تحديثات تلقائياً عند تغيير قيمها. هذا يمكّن من بناء تطبيقات متجاوبة ومدفوعة بالأحداث مع الحد الأدنى من الكود الإضافي.

## Features - الميزات

Bayan provides three main reactive programming features:

1. **Reactive Variables** - متغيرات تفاعلية
2. **Watch Blocks** - كتل المراقبة
3. **Computed Properties** - الخصائص المحسوبة

---

## 1. Reactive Variables - المتغيرات التفاعلية

### Syntax - البنية

```bayan
# English
reactive variable_name = initial_value

# Arabic
تفاعلي اسم_المتغير = القيمة_الأولية
تفاعلية اسم_المتغير = القيمة_الأولية
```

### Description - الوصف

Reactive variables are special variables that track changes. When a reactive variable is modified, it can trigger watchers and update computed properties that depend on it.

المتغيرات التفاعلية هي متغيرات خاصة تتتبع التغييرات. عندما يتم تعديل متغير تفاعلي، يمكنه تشغيل المراقبين وتحديث الخصائص المحسوبة التي تعتمد عليه.

### Examples - أمثلة

```bayan
# English example
reactive temperature = 20
print("Temperature: " + str(temperature))

temperature = 25  # This change is tracked
print("New temperature: " + str(temperature))

# Arabic example
تفاعلي درجة_الحرارة = 30
print("درجة الحرارة: " + str(درجة_الحرارة))

درجة_الحرارة = 35  # هذا التغيير يتم تتبعه
print("درجة الحرارة الجديدة: " + str(درجة_الحرارة))
```

### Keywords - الكلمات المفتاحية

- English: `reactive`
- Arabic: `تفاعلي`, `تفاعلية`

---

## 2. Watch Blocks - كتل المراقبة

### Syntax - البنية

```bayan
# English - single variable
watch variable_name:
{
    # code to execute when variable changes
}

# English - multiple variables
watch var1, var2, var3:
{
    # code to execute when any variable changes
}

# Arabic - single variable
راقب اسم_المتغير:
{
    # الكود الذي يتم تنفيذه عند تغيير المتغير
}

# Arabic - multiple variables
راقب متغير1, متغير2, متغير3:
{
    # الكود الذي يتم تنفيذه عند تغيير أي متغير
}
```

### Description - الوصف

Watch blocks execute automatically whenever one of the watched variables changes. This is useful for side effects, logging, UI updates, or any action that should happen in response to data changes.

كتل المراقبة تُنفذ تلقائياً كلما تغير أحد المتغيرات المراقبة. هذا مفيد للتأثيرات الجانبية، والتسجيل، وتحديثات واجهة المستخدم، أو أي إجراء يجب أن يحدث استجابةً لتغييرات البيانات.

### Examples - أمثلة

```bayan
# English example - single variable
reactive counter = 0
log = []

watch counter:
{
    log = log + [counter]
    print("Counter changed to: " + str(counter))
}

counter = 1  # Triggers watch block
counter = 2  # Triggers watch block again

# Arabic example - multiple variables
تفاعلي س = 10
تفاعلي ص = 20

راقب س, ص:
{
    print("س أو ص تغيرت. المجموع: " + str(س + ص))
}

س = 15  # يُطلق كتلة المراقبة
ص = 25  # يُطلق كتلة المراقبة مرة أخرى
```

### Keywords - الكلمات المفتاحية

- English: `watch`
- Arabic: `راقب`, `مراقبة`

---

## 3. Computed Properties - الخصائص المحسوبة

### Syntax - البنية

```bayan
# English
computed property_name = expression

# Arabic
محسوب اسم_الخاصية = التعبير
محسوبة اسم_الخاصية = التعبير
```

### Description - الوصف

Computed properties are automatically recalculated whenever their dependencies (reactive variables used in the expression) change. They are themselves reactive, so they can trigger watchers.

الخصائص المحسوبة يتم إعادة حسابها تلقائياً كلما تغيرت تبعياتها (المتغيرات التفاعلية المستخدمة في التعبير). وهي نفسها تفاعلية، لذا يمكنها تشغيل المراقبين.

### Examples - أمثلة

```bayan
# English example
reactive width = 10
reactive height = 20
computed area = width * height

print("Area: " + str(area))  # Output: Area: 200

width = 15  # area automatically updates to 300
print("New area: " + str(area))  # Output: New area: 300

height = 30  # area automatically updates to 450
print("Final area: " + str(area))  # Output: Final area: 450

# Arabic example
تفاعلي طول = 5
تفاعلي عرض = 8
محسوب مساحة = طول * عرض

print("المساحة: " + str(مساحة))  # الناتج: المساحة: 40

طول = 10  # المساحة تتحدث تلقائياً إلى 80
print("المساحة الجديدة: " + str(مساحة))  # الناتج: المساحة الجديدة: 80
```

### Keywords - الكلمات المفتاحية

- English: `computed`
- Arabic: `محسوب`, `محسوبة`

---

## Combined Usage - الاستخدام المركب

You can combine reactive variables, watch blocks, and computed properties to create powerful reactive systems:

يمكنك دمج المتغيرات التفاعلية وكتل المراقبة والخصائص المحسوبة لإنشاء أنظمة تفاعلية قوية:

```bayan
# Temperature monitoring system
reactive celsius = 25
computed fahrenheit = (celsius * 9 / 5) + 32
computed kelvin = celsius + 273.15

alerts = []

watch celsius:
{
    if (celsius > 30) {
        alerts = alerts + ["High temperature warning!"]
    }
    print("Temperature changed:")
    print("  Celsius: " + str(celsius))
    print("  Fahrenheit: " + str(fahrenheit))
    print("  Kelvin: " + str(kelvin))
}

celsius = 35  # Triggers watch block, updates computed properties
celsius = 40  # Triggers watch block again
```

---

## Use Cases - حالات الاستخدام

### 1. UI State Management - إدارة حالة واجهة المستخدم

```bayan
reactive username = ""
reactive password = ""
computed is_valid = len(username) > 0 and len(password) >= 8

watch is_valid:
{
    if (is_valid) {
        print("Form is valid")
    }
    else:
    {
        print("Form is invalid")
    }
}
```

### 2. Data Synchronization - مزامنة البيانات

```bayan
reactive local_data = []
sync_log = []

watch local_data:
{
    sync_log = sync_log + ["Syncing data..."]
    # Sync to server
}
```

### 3. Derived Calculations - الحسابات المشتقة

```bayan
reactive price = 100
reactive quantity = 5
reactive tax_rate = 0.1

computed subtotal = price * quantity
computed tax = subtotal * tax_rate
computed total = subtotal + tax

watch total:
{
    print("Total updated: " + str(total))
}
```

### 4. Event Logging - تسجيل الأحداث

```bayan
reactive user_action = ""
action_history = []

watch user_action:
{
    action_history = action_history + [user_action]
}

user_action = "login"
user_action = "view_profile"
user_action = "logout"
```

---

## Best Practices - أفضل الممارسات

1. **Use reactive variables for state** - استخدم المتغيرات التفاعلية للحالة
   - Mark variables as reactive only if you need to track their changes
   - ضع علامة على المتغيرات كتفاعلية فقط إذا كنت بحاجة لتتبع تغييراتها

2. **Keep watch blocks simple** - اجعل كتل المراقبة بسيطة
   - Watch blocks should perform quick operations
   - كتل المراقبة يجب أن تنفذ عمليات سريعة

3. **Use computed properties for derived data** - استخدم الخصائص المحسوبة للبيانات المشتقة
   - Computed properties are perfect for calculations based on reactive variables
   - الخصائص المحسوبة مثالية للحسابات المبنية على المتغيرات التفاعلية

4. **Avoid circular dependencies** - تجنب التبعيات الدائرية
   - Don't create situations where A depends on B and B depends on A
   - لا تنشئ حالات حيث A يعتمد على B و B يعتمد على A

---

## Summary - الملخص

Reactive programming in Bayan provides:
- **Reactive variables** (`reactive`/`تفاعلي`) for trackable state
- **Watch blocks** (`watch`/`راقب`) for automatic side effects
- **Computed properties** (`computed`/`محسوب`) for derived values

These features enable building responsive, maintainable applications with clear data flow.

البرمجة التفاعلية في بيان توفر:
- **متغيرات تفاعلية** (`reactive`/`تفاعلي`) للحالة القابلة للتتبع
- **كتل المراقبة** (`watch`/`راقب`) للتأثيرات الجانبية التلقائية
- **خصائص محسوبة** (`computed`/`محسوب`) للقيم المشتقة

هذه الميزات تمكّن من بناء تطبيقات متجاوبة وقابلة للصيانة مع تدفق بيانات واضح.


