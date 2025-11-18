# Cognitive-Semantic Model Guide
# دليل النموذج المعرفي-الدلالي

## Overview | نظرة عامة

The Cognitive-Semantic Model is a revolutionary feature in Bayan that allows you to represent ideas, meanings, and knowledge in a structured way. It's based on the philosophical concept that **an idea consists of three elements: entities (things), events (actions), and results (outcomes)**.

النموذج المعرفي-الدلالي هو ميزة ثورية في لغة بيان تتيح لك تمثيل الأفكار والمعاني والمعرفة بطريقة منظمة. يعتمد على المفهوم الفلسفي أن **الفكرة تتكون من ثلاثة عناصر: كيانات (أشياء)، أحداث (أفعال)، ونتائج (مخرجات)**.

## Core Concepts | المفاهيم الأساسية

### 1. Cognitive Entities | الكيانات المعرفية

Cognitive entities are objects with dynamic properties that can change based on events.

الكيانات المعرفية هي كائنات ذات خصائص ديناميكية يمكن تغييرها بناءً على الأحداث.

**Syntax:**
```bayan
cognitive_entity <name>:
{
    property1: value1
    property2: value2
    ...
}

# Arabic
كيان_معرفي <اسم>:
{
    خاصية1: قيمة1
    خاصية2: قيمة2
    ...
}
```

**Example:**
```bayan
cognitive_entity أرض:
{
    لون: "بني"
    حالة: "جافة"
    خصوبة: 0.2
}

# Access properties
print(أرض["لون"])  # Output: بني
```

### 2. Cognitive Events | الأحداث المعرفية

Cognitive events represent actions that occur between entities, with participants having degrees of involvement (0-1).

الأحداث المعرفية تمثل أفعالاً تحدث بين الكيانات، مع درجات مشاركة للمشاركين (0-1).

**Syntax:**
```bayan
cognitive_event <name>:
{
    participants: {
        "entity1": {"role": "...", "degree": 0.8},
        "entity2": {"role": "...", "degree": 1.0}
    },
    strength: 0.9,
    transform: {
        "entity.property": new_value,
        ...
    },
    reactions: [
        {"event": "event_name", "probability": 0.8}
    ]
}

# Arabic
حدث_معرفي <اسم>:
{
    مشاركون: {
        "كيان1": {"دور": "...", "درجة": 0.8},
        "كيان2": {"دور": "...", "درجة": 1.0}
    },
    قوة: 0.9,
    تحويل: {
        "كيان.خاصية": قيمة_جديدة,
        ...
    },
    ردود_فعل: [
        {"حدث": "اسم_الحدث", "احتمال": 0.8}
    ]
}
```

**Example:**
```bayan
حدث_معرفي نزول_المطر:
{
    مشاركون: {
        "أرض": {"دور": "متأثر", "درجة": 1.0}
    },
    قوة: 0.8,
    تحويل: {
        "أرض.لون": "أخضر",
        "أرض.حالة": "رطبة"
    }
}
```

### 3. Triggering Events | إطلاق الأحداث

To execute a cognitive event, use the `trigger` keyword.

لتنفيذ حدث معرفي، استخدم كلمة `trigger` أو `أطلق`.

**Syntax:**
```bayan
trigger <event_name>

# Arabic
أطلق <اسم_الحدث>
```

**Example:**
```bayan
أطلق نزول_المطر
# This will transform the أرض entity
```

### 4. Reaction System | نظام ردود الفعل

Events can trigger other events as reactions, creating cascading effects.

يمكن للأحداث أن تطلق أحداثاً أخرى كردود فعل، مما يخلق تأثيرات متسلسلة.

**Example:**
```bayan
حدث_معرفي دراسة:
{
    مشاركون: {
        "طالب": {"دور": "فاعل", "درجة": 1.0}
    },
    قوة: 0.8,
    تحويل: {
        "طالب.معرفة": 0.7
    },
    ردود_فعل: [
        {"حدث": "تخرج", "احتمال": 1.0}
    ]
}

حدث_معرفي تخرج:
{
    مشاركون: {
        "طالب": {"دور": "فاعل", "درجة": 1.0}
    },
    قوة: 1.0,
    تحويل: {
        "طالب.حالة": "خريج"
    }
}

# Triggering دراسة will also trigger تخرج
أطلق دراسة
```

### 5. Concurrent Events | الأحداث المتزامنة

Multiple events can occur simultaneously with different strengths.

يمكن أن تحدث أحداث متعددة في نفس الوقت بقوى مختلفة.

**Syntax:**
```bayan
concurrent <name>:
{
    events: [
        ("event1", strength1),
        ("event2", strength2)
    ]
}

# Arabic
متزامن <اسم>:
{
    أحداث: [
        ("حدث1", قوة1),
        ("حدث2", قوة2)
    ]
}
```

**Example:**
```bayan
concurrent يوم_عادي:
{
    events: [
        ("عمل", 0.8),
        ("لعب", 0.6)
    ]
}
```

### 6. Linguistic Patterns | القوالب اللغوية

Linguistic patterns define templates for expressing ideas in natural language.

القوالب اللغوية تعرّف قوالب للتعبير عن الأفكار باللغة الطبيعية.

**Syntax:**
```bayan
pattern <name>:
{
    structure: ["element1", "element2", ...],
    express: "template string with {placeholders}"
}

# Arabic
قالب <اسم>:
{
    بنية: ["عنصر1", "عنصر2", ...],
    تعبير: "نص القالب مع {متغيرات}"
}
```

**Example:**
```bayan
pattern فعل_ونتيجة:
{
    structure: ["فاعل", "فعل", "مفعول"],
    express: "قام {فاعل} بـ {فعل} {مفعول}"
}
```

### 7. Ideas | الأفكار

Ideas are high-level cognitive concepts that combine entities, events, and results.

الأفكار هي مفاهيم معرفية عالية المستوى تجمع بين الكيانات والأحداث والنتائج.

**Syntax:**
```bayan
idea "<name>":
{
    entities: {
        "entity1": {"property": "value"},
        ...
    },
    event: "event_name",
    result: {
        "state_changes": {
            "entity.property": "new_value"
        }
    }
}

# Arabic
فكرة "<اسم>":
{
    كيانات: {
        "كيان1": {"خاصية": "قيمة"},
        ...
    },
    حدث: "اسم_الحدث",
    نتيجة: {
        "تغييرات_الحالة": {
            "كيان.خاصية": "قيمة_جديدة"
        }
    }
}
```

**Example:**
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

## Keywords | الكلمات المفتاحية

### English Keywords
- `cognitive_entity` - Define a cognitive entity
- `cognitive_event` - Define a cognitive event
- `event` - Generic event keyword
- `trigger` - Trigger an event
- `concurrent` - Define concurrent events
- `pattern` - Define a linguistic pattern
- `idea` - Define an idea
- `participants` - Event participants
- `strength` - Event strength
- `transform` - State transformations
- `reactions` - Event reactions
- `structure` - Pattern structure
- `express` - Pattern expression
- `entities` - Idea entities
- `result` - Idea result
- `state_changes` - State changes
- `linguistic_forms` - Linguistic forms
- `degree` - Participation degree
- `role` - Participant role

### Arabic Keywords | الكلمات المفتاحية العربية
- `كيان_معرفي` / `كيان` - تعريف كيان معرفي
- `حدث_معرفي` / `حدث` - تعريف حدث معرفي
- `أطلق` - إطلاق حدث
- `متزامن` - تعريف أحداث متزامنة
- `قالب` - تعريف قالب لغوي
- `فكرة` - تعريف فكرة
- `مشاركون` - مشاركو الحدث
- `قوة` - قوة الحدث
- `تحويل` - تحويلات الحالة
- `ردود_فعل` / `ردود` - ردود فعل الحدث
- `بنية` - بنية القالب
- `تعبير` - تعبير القالب
- `كيانات` - كيانات الفكرة
- `نتيجة` - نتيجة الفكرة
- `تغييرات_الحالة` / `تغييرات` - تغييرات الحالة
- `أشكال_لغوية` / `أشكال` - أشكال لغوية
- `درجة` - درجة المشاركة
- `دور` - دور المشارك

## Use Cases | حالات الاستخدام

### 1. Text Generation | توليد النصوص
Use cognitive entities and events to generate narrative text based on state changes.

### 2. Meaning Analysis | تحليل المعاني
Represent semantic relationships between concepts using entities and events.

### 3. Event Simulation | محاكاة الأحداث
Simulate complex scenarios with multiple entities and cascading events.

### 4. Cognitive Modeling | النمذجة المعرفية
Model how ideas and knowledge are formed and transformed.

### 5. Knowledge Representation | تمثيل المعرفة
Represent domain knowledge using entities, events, and their relationships.

## Best Practices | أفضل الممارسات

1. **Use meaningful names** - Choose descriptive names for entities and events
2. **Set appropriate degrees** - Use participation degrees (0-1) to represent involvement levels
3. **Chain reactions carefully** - Be mindful of cascading events to avoid infinite loops
4. **Document patterns** - Document linguistic patterns for reusability
5. **Test transformations** - Verify that state transformations produce expected results

## Examples | أمثلة

See `examples/cognitive_semantic_demo.by` for comprehensive examples of all features.

## Integration with Other Features | التكامل مع الميزات الأخرى

The Cognitive-Semantic Model integrates seamlessly with:
- **Logical Programming** - Use entities in logical queries
- **Probabilistic Programming** - Use probability in reactions
- **Reactive Programming** - React to entity state changes
- **Pattern Matching** - Match on entity properties

---

**Note:** This is an experimental feature that represents a new paradigm in programming. We welcome feedback and suggestions for improvement!

**ملاحظة:** هذه ميزة تجريبية تمثل نموذجاً جديداً في البرمجة. نرحب بالملاحظات والاقتراحات للتحسين!

