# Temporal Constructs Guide - دليل البنى الزمنية

## Overview - نظرة عامة

Bayan language now supports **temporal constructs** that allow you to express time-based logic and control flow in your programs. These constructs are fully bilingual, supporting both English and Arabic keywords.

لغة البيان تدعم الآن **البنى الزمنية** التي تسمح لك بالتعبير عن المنطق الزمني والتحكم في التدفق بناءً على الوقت. هذه البنى ثنائية اللغة بالكامل، وتدعم الكلمات المفتاحية بالإنجليزية والعربية.

---

## 1. Temporal Block - الكتلة الزمنية

### Syntax - الصيغة

**English:**
```bayan
temporal {
    first: statement1,
    then: statement2,
    lastly: statement3
}
```

**Arabic:**
```bayan
زمنيا {
    أولا: عبارة1,
    ثم: عبارة2,
    أخيرا: عبارة3
}
```

### Description - الوصف

Executes statements in a labeled sequence. Each step is executed in order: `first`, `then`, `lastly`.

تنفذ العبارات في تسلسل مُعنون. كل خطوة تُنفذ بالترتيب: `أولا`، `ثم`، `أخيرا`.

### Keywords - الكلمات المفتاحية

| English | Arabic | Meaning |
|---------|--------|---------|
| `temporal` | `زمنيا` / `زمني` | Temporal block |
| `first` | `أولا` / `أولاً` | First step |
| `then` | `ثم` | Then/next step |
| `lastly` | `أخيرا` / `أخيراً` | Last/final step |

### Example - مثال

```bayan
# English
temporal {
    first: x = 10,
    then: y = x * 2,
    lastly: z = y + 5
}
print(z)  # Output: 25

# Arabic
زمنيا {
    أولا: س = 5,
    ثم: ص = س + 10,
    أخيرا: ع = ص * 2
}
print(ع)  # الناتج: 30
```

---

## 2. Delay Statement - عبارة التأخير

### Syntax - الصيغة

**English:**
```bayan
delay <duration> <unit>
```

**Arabic:**
```bayan
تأخير <المدة> <الوحدة>
```

### Description - الوصف

Pauses execution for the specified duration.

توقف التنفيذ للمدة المحددة.

### Keywords - الكلمات المفتاحية

| English | Arabic | Meaning |
|---------|--------|---------|
| `delay` | `تأخير` / `أخر` | Delay/pause |
| `seconds` | `ثانية` / `ثواني` | Seconds |
| `minutes` | `دقيقة` / `دقائق` | Minutes |
| `hours` | `ساعة` / `ساعات` | Hours |

### Example - مثال

```bayan
# English
print("Starting...")
delay 1.5 seconds
print("Done!")

# Arabic
print("البداية...")
تأخير 2.0 ثواني
print("انتهى!")
```

---

## 3. Within Block - كتلة خلال

### Syntax - الصيغة

**English:**
```bayan
within <duration> <unit> {
    # code block
}
```

**Arabic:**
```bayan
خلال <المدة> <الوحدة> {
    # كتلة الكود
}
```

### Description - الوصف

Executes a block of code with a time constraint (timeout). If the block takes longer than the specified duration, a `TimeoutError` is raised.

تنفذ كتلة من الكود مع قيد زمني (مهلة). إذا استغرقت الكتلة وقتاً أطول من المدة المحددة، يُرفع خطأ `TimeoutError`.

### Keywords - الكلمات المفتاحية

| English | Arabic | Meaning |
|---------|--------|---------|
| `within` | `خلال` | Within/during |

### Example - مثال

```bayan
# English
within 5.0 seconds {
    result = expensive_computation()
}

# Arabic
خلال 3.0 ثواني {
    النتيجة = حساب_معقد()
}
```

---

## 4. Schedule Block - كتلة الجدولة

### Syntax - الصيغة

**English:**
```bayan
schedule every <interval> <unit> {
    # code block
}
```

**Arabic:**
```bayan
جدولة كل <الفترة> <الوحدة> {
    # كتلة الكود
}
```

### Description - الوصف

Schedules repeated execution of a block at the specified interval.

**Note:** Current implementation executes the block once. Future versions will support actual background scheduling.

تجدول التنفيذ المتكرر لكتلة بالفترة المحددة.

**ملاحظة:** التنفيذ الحالي ينفذ الكتلة مرة واحدة. الإصدارات المستقبلية ستدعم الجدولة الفعلية في الخلفية.

### Keywords - الكلمات المفتاحية

| English | Arabic | Meaning |
|---------|--------|---------|
| `schedule` | `جدولة` / `جدول` | Schedule |
| `every` | `كل` | Every |

### Example - مثال

```bayan
# English
schedule every 2.0 seconds {
    check_status()
}

# Arabic
جدولة كل 1.0 ثانية {
    تحقق_من_الحالة()
}
```

---

## Complete Example - مثال كامل

```bayan
# Complex temporal workflow
print("=== Temporal Workflow ===")

temporal {
    first: {
        print("Phase 1: Initialization")
        data = []
        delay 0.5 seconds
    },
    then: {
        print("Phase 2: Processing")
        within 2.0 seconds {
            for i in range(100):
                data.append(i * 2)
        }
    },
    lastly: {
        print("Phase 3: Finalization")
        total = sum(data)
        print(f"Total: {total}")
    }
}

print("Workflow complete!")
```

---

## Use Cases - حالات الاستخدام

1. **Narrative Generation**: Control timing of story events
   - **توليد السرد**: التحكم في توقيت أحداث القصة

2. **Game Development**: Schedule game events and animations
   - **تطوير الألعاب**: جدولة أحداث اللعبة والرسوم المتحركة

3. **Simulations**: Model time-dependent processes
   - **المحاكاة**: نمذجة العمليات المعتمدة على الوقت

4. **Testing**: Add delays and timeouts in tests
   - **الاختبار**: إضافة تأخيرات ومهل في الاختبارات

---

## Notes - ملاحظات

- All time units are converted to seconds internally
  - جميع وحدات الوقت تُحول إلى ثوان داخلياً

- Temporal blocks execute steps sequentially
  - الكتل الزمنية تنفذ الخطوات بالتسلسل

- Schedule blocks currently execute once (future: background scheduling)
  - كتل الجدولة حالياً تنفذ مرة واحدة (مستقبلاً: جدولة في الخلفية)

- Within blocks raise `TimeoutError` if time limit exceeded
  - كتل خلال ترفع `TimeoutError` إذا تجاوز الحد الزمني

---

## See Also - انظر أيضاً

- [Language Guide](LANGUAGE_GUIDE.md)
- [Examples](../examples/temporal_constructs_demo.by)

