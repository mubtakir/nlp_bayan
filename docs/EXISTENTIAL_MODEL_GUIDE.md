# النموذج الوجودي العام (Generic Existential Model)

## نظرة عامة (Overview)

النموذج الوجودي العام هو إطار عمل فلسفي-برمجي يسمح بتمثيل الكائنات (Beings/Entities) في سياقها البيئي والزماني والمكاني مع جميع العلاقات الأساسية. هذا النموذج **عام وقابل للتخصيص** لأي مجال معرفي.

The Generic Existential Model is a philosophical-programming framework that allows representing beings/entities in their environmental, temporal, and spatial context with all fundamental relationships. This model is **generic and customizable** for any knowledge domain.

## الفلسفة (Philosophy)

الفكرة الأساسية هي أن **الكائن لا يُفهم بمعزل عن بيئته**. كل كائن:
- يوجد في **بيئة** لها أبعاد مكانية وزمانية ومجالية
- يرث **معانٍ من البيئة** (مثل الموقع، الزمان)
- له **معانٍ ذاتية** خاصة به
- له **علاقات** مع غيره من الكائنات
- يقوم **بأفعال** في بيئته
- له **حالات** مختلفة

The core idea is that **a being cannot be understood in isolation from its environment**. Every being:
- Exists in an **environment** with spatial, temporal, and domain-specific dimensions
- Inherits **meanings from the environment** (such as position, time)
- Has **intrinsic meanings** specific to itself
- Has **relations** with other beings
- Performs **actions** in its environment
- Has different **states**

## المكونات الأساسية (Core Components)

### 1. المجال (Domain)

تعريف مجال معرفي بكائناته الأساسية وبيئته وقوانينه.

```bayan
مجال "اسم_المجال":
{
    "كائن_أساسي": "نوع_الكائن",
    "بيئة": "نوع_البيئة",
    "معانٍ_أساسية": ["معنى1", "معنى2"],
    "علاقات": ["علاقة1", "علاقة2"],
    "خصائص": ["خاصية1", "خاصية2"]
}

# English
domain "domain_name":
{
    "basic_entity": "entity_type",
    "environment": "environment_type",
    "basic_meanings": ["meaning1", "meaning2"],
    "relations": ["relation1", "relation2"],
    "properties": ["property1", "property2"]
}
```

**مثال (Example):**

```bayan
مجال "الكيمياء":
{
    "كائن_أساسي": "عنصر",
    "بيئة": "محلول",
    "معانٍ_أساسية": ["تفاعل", "ذوبان", "ترسيب"],
    "علاقات": ["يتفاعل_مع", "يذوب_في"],
    "خصائص": ["عدد_ذري", "كتلة_ذرية", "تكافؤ"]
}
```

### 2. البيئة العامة (Generic Environment)

تعريف بيئة بأبعادها المكانية والزمانية والمجالية.

```bayan
بيئة "اسم_البيئة" في_مجال "اسم_المجال":
{
    "أبعاد": {
        "مكاني": ["فوق", "تحت", "يمين", "يسار"],
        "زماني": ["قبل", "بعد", "أثناء"],
        "مجالي": ["بُعد_خاص1", "بُعد_خاص2"]
    },
    "خصائص": {"خاصية1": قيمة1},
    "قوانين": ["قانون1", "قانون2"]
}

# English
environment "environment_name" in_domain "domain_name":
{
    "dimensions": {
        "spatial": ["above", "below", "left", "right"],
        "temporal": ["before", "after", "during"],
        "domain_specific": ["custom_dim1", "custom_dim2"]
    },
    "properties": {"property1": value1},
    "laws": ["law1", "law2"]
}
```

**مثال (Example):**

```bayan
بيئة "محلول_حمضي" في_مجال "الكيمياء":
{
    "أبعاد": {
        "مكاني": ["سطح", "قاع", "وسط"],
        "زماني": ["قبل_التفاعل", "أثناء_التفاعل", "بعد_التفاعل"],
        "مجالي": ["تركيز", "حرارة", "ضغط"]
    },
    "خصائص": {"pH": 3, "حرارة": 25},
    "قوانين": ["قانون_الكتلة", "قانون_الطاقة"]
}
```

### 3. الكائن الوجودي (Existential Being)

تعريف كائن في مجال معين مع معانيه الموروثة والذاتية.

```bayan
كائن_وجودي "اسم_الكائن" من_نوع "نوع" في_مجال "مجال":
{
    "بيئة": "اسم_البيئة",
    "خصائص_ذاتية": {"خاصية": قيمة},
    "معانٍ_موروثة": ["معنى_من_البيئة"],
    "معانٍ_ذاتية": ["معنى_خاص"],
    "علاقات": {"علاقة": ["كائن_آخر"]},
    "أفعال": {"فعل": "نتيجة"},
    "حالات": ["حالة1", "حالة2"]
}

# English
existential_being "being_name" of_type "type" in_domain "domain":
{
    "environment": "environment_name",
    "intrinsic_properties": {"property": value},
    "inherited_meanings": ["meaning_from_environment"],
    "intrinsic_meanings": ["specific_meaning"],
    "relations": {"relation": ["other_being"]},
    "actions": {"action": "result"},
    "states": ["state1", "state2"]
}
```

**مثال (Example):**

```bayan
كائن_وجودي "صوديوم" من_نوع "عنصر" في_مجال "الكيمياء":
{
    "بيئة": "محلول_حمضي",
    "خصائص_ذاتية": {"عدد_ذري": 11, "رمز": "Na"},
    "معانٍ_موروثة": ["موقع_في_المحلول", "زمن_الإضافة"],
    "معانٍ_ذاتية": ["نشاط_كيميائي_عالي"],
    "علاقات": {"يتفاعل_مع": ["كلور", "ماء"]},
    "أفعال": {"تفاعل": "ينتج_ملح"},
    "حالات": ["صلب", "منحل", "متفاعل"]
}
```

### 4. العلاقة المجالية (Domain Relation)

تعريف علاقة بين كائنات في مجال.

```bayan
علاقة_مجالية "اسم_العلاقة" في_مجال "مجال":
{
    "نوع": "ثنائية" | "متعددة",
    "متماثلة": 1 | 0,
    "شروط": {"شرط": قيمة},
    "نتيجة": "ما_ينتج"
}

# English
domain_relation "relation_name" in_domain "domain":
{
    "type": "binary" | "multiple",
    "symmetric": 1 | 0,
    "conditions": {"condition": value},
    "result": "what_results"
}
```

### 5. الفعل المجالي (Domain Action)

تعريف فعل يمكن للكائنات القيام به.

```bayan
فعل_مجالي "اسم_الفعل" في_مجال "مجال":
{
    "فاعل": "نوع_الفاعل",
    "مفعول": "نوع_المفعول",
    "شروط": {"شرط": قيمة},
    "نتيجة": {"ما_ينتج": قيمة}
}

# English
domain_action "action_name" in_domain "domain":
{
    "actor": "actor_type",
    "object": "object_type",
    "conditions": {"condition": value},
    "result": {"what_results": value}
}
```

### 6. المعنى المجازي (Metaphorical Meaning)

تعريف معنى مجازي مبني على معانٍ أساسية.

```bayan
معنى_مجازي "اسم_المعنى" في_مجال "مجال":
{
    "تعريف": "تعريف_المعنى",
    "يُبنى_على": ["معنى_أساسي1", "معنى_أساسي2"],
    "يُطبق_على": ["نوع_الكائنات"],
    "شروط": {"شرط": قيمة}
}

# English
metaphorical_meaning "meaning_name" in_domain "domain":
{
    "definition": "meaning_definition",
    "built_on": ["basic_meaning1", "basic_meaning2"],
    "applies_to": ["entity_types"],
    "conditions": {"condition": value}
}
```

**مثال (Example):**

```bayan
معنى_مجازي "عدالة" في_مجال "عام":
{
    "تعريف": "كل كائن يأخذ ما يكفيه حسب طبيعته",
    "يُبنى_على": ["احتياج", "طبيعة", "توزيع"],
    "يُطبق_على": ["كل_الكائنات"],
    "شروط": {"لكل": "كائن", "يوجد": "احتياج"}
}
```

### 7. القانون المجالي (Domain Law)

تعريف قانون يحكم المجال.

```bayan
قانون_مجالي "اسم_القانون" في_مجال "مجال":
{
    "صيغة": "صيغة_القانون",
    "ينطبق_على": ["ما_ينطبق_عليه"],
    "استثناءات": ["استثناء1"]
}

# English
domain_law "law_name" in_domain "domain":
{
    "formula": "law_formula",
    "applies_to": ["what_it_applies_to"],
    "exceptions": ["exception1"]
}
```

### 8. الاستعلام الوجودي (Existential Query)

استعلام عن كائنات في مجال.

```bayan
نتيجة = استعلام_وجودي:
{
    "في_مجال": "اسم_المجال",
    "عن": "نوع_الكائن",
    "شروط": {"شرط": قيمة}
}

# English
result = existential_query:
{
    "in_domain": "domain_name",
    "about": "entity_type",
    "conditions": {"condition": value}
}
```

## أمثلة كاملة (Complete Examples)

### مثال 1: مجال الكيمياء (Chemistry Domain)

```bayan
# تعريف المجال
مجال "الكيمياء":
{
    "كائن_أساسي": "عنصر",
    "بيئة": "محلول",
    "معانٍ_أساسية": ["تفاعل", "ذوبان", "ترسيب"],
    "علاقات": ["يتفاعل_مع", "يذوب_في"],
    "خصائص": ["عدد_ذري", "كتلة_ذرية"]
}

# تعريف البيئة
بيئة "محلول" في_مجال "الكيمياء":
{
    "أبعاد": {
        "مكاني": ["سطح", "قاع", "وسط"],
        "زماني": ["قبل", "أثناء", "بعد"],
        "مجالي": ["تركيز", "حرارة", "ضغط"]
    },
    "خصائص": {"pH": 7, "حرارة": 25}
}

# تعريف كائنات
كائن_وجودي "صوديوم" من_نوع "عنصر" في_مجال "الكيمياء":
{
    "بيئة": "محلول",
    "خصائص_ذاتية": {"عدد_ذري": 11, "رمز": "Na"},
    "علاقات": {"يتفاعل_مع": ["كلور", "ماء"], "نشاط": "عالي"}
}

كائن_وجودي "كلور" من_نوع "عنصر" في_مجال "الكيمياء":
{
    "بيئة": "محلول",
    "خصائص_ذاتية": {"عدد_ذري": 17, "رمز": "Cl"},
    "علاقات": {"يتفاعل_مع": ["صوديوم", "ماء"], "نشاط": "عالي"}
}

# استعلام
عناصر_نشطة = استعلام_وجودي:
{
    "في_مجال": "الكيمياء",
    "عن": "عنصر",
    "شروط": {"نشاط": "عالي"}
}

طباعة(عناصر_نشطة)  # ["صوديوم", "كلور"]
```

### مثال 2: مجال الإلكترونيات (Electronics Domain)

```bayan
domain "Electronics":
{
    "basic_entity": "transistor",
    "environment": "circuit",
    "basic_meanings": ["amplify", "switch", "conduct"],
    "relations": ["connected_to", "controls"],
    "properties": ["type", "beta", "Vbe"]
}

environment "circuit" in_domain "Electronics":
{
    "dimensions": {
        "spatial": ["input", "output", "ground"],
        "temporal": ["t0", "t1", "t2"],
        "domain_specific": ["voltage", "current", "resistance"]
    },
    "properties": {"voltage_source": 5, "frequency": 1000}
}

existential_being "Q1" of_type "transistor" in_domain "Electronics":
{
    "environment": "circuit",
    "intrinsic_properties": {"type": "NPN", "beta": 100, "Vbe": 0.7},
    "relations": {"connected_to": ["R1", "C1"], "controls": ["LED1"]}
}

existential_being "Q2" of_type "transistor" in_domain "Electronics":
{
    "environment": "circuit",
    "intrinsic_properties": {"type": "PNP", "beta": 150, "Vbe": 0.7},
    "relations": {"connected_to": ["R2", "C2"]}
}

npn_transistors = existential_query:
{
    "in_domain": "Electronics",
    "about": "transistor",
    "conditions": {"type": "NPN"}
}

print(npn_transistors)  # ["Q1"]
```

## التكامل مع ميزات بيان الأخرى (Integration with Other Bayan Features)

### مع الكيانات المعرفية (With Cognitive Entities)

```bayan
# يمكن دمج النموذج الوجودي مع الكيانات المعرفية
كيان_معرفي "عالم_الكيمياء":
{
    "معرفة": {
        "مجالات": ["الكيمياء"],
        "كائنات": ["صوديوم", "كلور"]
    },
    "أفعال": {
        "يستعلم": استعلام_وجودي: {
            "في_مجال": "الكيمياء",
            "عن": "عنصر",
            "شروط": {"نشاط": "عالي"}
        }
    }
}
```

### مع الشبكات الدلالية (With Semantic Networks)

```bayan
# يمكن بناء شبكة دلالية من الكائنات الوجودية
شبكة_معاني "شبكة_العناصر":
{
    "عقد": ["صوديوم", "كلور", "ملح"],
    "علاقات": [
        {"من": "صوديوم", "إلى": "كلور", "نوع": "يتفاعل_مع"},
        {"من": "صوديوم", "إلى": "ملح", "نوع": "ينتج"},
        {"من": "كلور", "إلى": "ملح", "نوع": "ينتج"}
    ]
}
```

## الكلمات المفتاحية (Keywords)

### العربية (Arabic)
- `مجال` - Domain
- `بيئة` - Environment
- `في_مجال` - in_domain
- `من_نوع` - of_type
- `كائن_وجودي` - Existential Being
- `أبعاد` - Dimensions
- `مكاني` - Spatial
- `زماني` - Temporal
- `مجالي` - Domain-specific
- `خصائص_ذاتية` - Intrinsic Properties
- `معانٍ_موروثة` - Inherited Meanings
- `معانٍ_ذاتية` - Intrinsic Meanings
- `علاقات` - Relations
- `أفعال` - Actions
- `حالات` - States
- `علاقة_مجالية` - Domain Relation
- `فعل_مجالي` - Domain Action
- `معنى_مجازي` - Metaphorical Meaning
- `قانون_مجالي` - Domain Law
- `استعلام_وجودي` - Existential Query
- `فوق`, `تحت`, `يمين`, `يسار`, `أمام`, `خلف` - Spatial directions
- `شمال`, `جنوب`, `شرق`, `غرب` - Cardinal directions
- `قبل`, `بعد`, `أثناء`, `الآن` - Temporal relations
- `في`, `على`, `إلى`, `عن`, `من` - Prepositions

### English
- `domain` - Domain
- `environment` - Environment
- `in_domain` - in_domain
- `of_type` - of_type
- `existential_being` - Existential Being
- `dimensions` - Dimensions
- `spatial` - Spatial
- `temporal` - Temporal
- `domain_specific` - Domain-specific
- `intrinsic_properties` - Intrinsic Properties
- `inherited_meanings` - Inherited Meanings
- `intrinsic_meanings` - Intrinsic Meanings
- `relations` - Relations
- `actions` - Actions
- `states` - States
- `domain_relation` - Domain Relation
- `domain_action` - Domain Action
- `metaphorical_meaning` - Metaphorical Meaning
- `domain_law` - Domain Law
- `existential_query` - Existential Query
- `above`, `below`, `left`, `right`, `front`, `back` - Spatial directions
- `north`, `south`, `east`, `west` - Cardinal directions
- `before`, `after`, `during`, `now` - Temporal relations
- `in`, `on`, `to`, `from`, `at` - Prepositions

## حالات الاستخدام (Use Cases)

1. **النمذجة العلمية** - Scientific Modeling
2. **الذكاء الاصطناعي الفلسفي** - Philosophical AI
3. **أنظمة المعرفة** - Knowledge Systems
4. **المحاكاة** - Simulation
5. **التعليم** - Education
6. **البحث الفلسفي** - Philosophical Research

---

**ملاحظة**: هذا النموذج هو الأساس العام. في الخطوة التالية، سنبني **مكتبة مجال الحياة** التي تطبق هذا النموذج على الكائنات الحية في بيئاتها الطبيعية.

**Note**: This model is the generic foundation. In the next step, we will build the **Life Domain Library** that applies this model to living beings in their natural environments.


