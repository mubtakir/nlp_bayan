# نظام المعادلات اللغوية (Linguistic Equations System)

**آخر تحديث**: 2025-11-25

## نظرة عامة

نظام المعادلات اللغوية يحول **الأفكار اللغوية** إلى **معادلات رياضية** قابلة للمعالجة والتحليل.

##الفلسفة الأساسية

```
الفكرة = (أشياء + حدث + نتيجة)

Idea = (Objects + Event + Result)
```

## المكونات

### 1. Role (الدور)

8 أدوار للكيانات في المعادلة:

- `SUBJECT` / `فاعل` - الذي يقوم بالفعل
- `OBJECT` / `مفعول_به` - الذي يقع عليه الفعل
- `PASSIVE_RECEIVER` / `متلقي` - المتلقي غير المباشر
- `INSTRUMENT` / `أداة` - أداة الفعل
- `LOCATION` / `مكان` - مكان الحدث
- `TIME` / `زمان` - زمان الحدث
- `CAUSE` / `سبب` - سبب الحدث
- `RESULT` / `نتيجة` - نتيجة الحدث

### 2. EventType (نوع الحدث)

9 أنواع للأحداث:

- `PHYSICAL_ACTION` / `فعل_مادي` - أكل، ضرب، كسر
- `MENTAL_ACTION` / `فعل_عقلي` - فكر، تذكر، نسي
- `COMMUNICATION` / `تواصل` - قال، كتب، سأل
- `MOVEMENT` / `حركة` - ذهب، جاء، رجع
- `TRANSFORMATION` / `تحول` - أصبح، تحول، تغير
- `POSSESSION` / `امتلاك` - ملك، أخذ، أعطى
- `EMOTION` / `انفعال` - غضب، فرح، حزن
- `CREATION` / `إنشاء` - بنى، كتب، صنع
- `DESTRUCTION` / `تدمير` - هدم، كسر، أتلف

### 3. EntityState (حالة الكائن)

يصف التغيرات التي طرأت على الكائن:

```python
EntityState(
    entity_name="محمد",
    state_changes={"جوع": -0.5, "طاقة": +0.3},
    description="شبع وانتعش"
)
```

### 4. LinguisticEquation (المعادلة اللغوية)

المعادلة الكاملة:

```python
LinguisticEquation(
    entities={"محمد": Role.SUBJECT, "تفاحة": Role.OBJECT},
    event="أكل",
    event_type=EventType.PHYSICAL_ACTION,
    results=[...]
)
```

## الاستخدام

### تحليل جملة طبيعية

```bayan
hybrid {
    kb = KnowledgeBase()
    
    # تحليل تلقائي
    eq = parse_sentence("محمد أكل تفاحة", kb)
    
    # عرض بلغة طبيعية
    print(eq.to_natural_language())
    # → "محمد أكل تفاحة"
    
    # عرض كمعادلة رسمية
    print(eq.to_formal_notation())
    # → محمد(فاعل) + تفاحة(مفعول_به) + أكل = 
    #   [محمد: جوع↓, طاقة↑] + [تفاحة: موجود=False]
}
```

### إنشاء معادلة يدوياً

```bayan
hybrid {
    # معادلة كاملة
    eq = LinguisticEquation(
        {"أحمد": Role("فاعل"), "الكرة": Role("مفعول_به")},
        "ضرب",
        "فعل_مادي"
    )
    
    # حساب النتائج من قاعدة المعرفة
    kb = KnowledgeBase()
    results = eq.compute_results(kb)
    
    for r in results:
        print(r)
}
```

### معادلة سريعة

```bayan
hybrid {
    # إنشاء سريع
    eq = create_simple_equation("زيد", "شرب", "ماء")
    
    print(eq.to_formal_notation())
}
```

## قاعدة المعرفة (KnowledgeBase)

### الأفعال المُعرفة مسبقاً

7 أفعال جاهزة:

1. **أكل**: `جوع↓، طاقة↑` → `الطعام: موجود=False`
2. **شرب**: `عطش↓، رطوبة↑` → `الماء: موجود=False`
3. **ضرب**: `غضب↑، تعب↑` → `المضروب: ألم↑`
4. **ذهب**: `موقع=جديد، تعب↑`
5. **نام**: `تعب↓، طاقة↑، وعي↓`
6. **كتب**: `تعب_يد↑، تركيز↓` → `النص: موجود=True`
7. **بنى**: `تعب↑` → `المبنى: موجود=True`

### إضافة حدث مخصص

```bayan
hybrid {
    kb = KnowledgeBase()
    
    # إضافة فعل جديد
    kb.add_custom_event(
        event="درس",
        subject_changes={
            "تعب": +0.3,
            "معرفة": +0.6,
            "تركيز": -0.2
        },
        object_changes={
            "مستوى_الفهم": +0.5
        }
    )
    
    # استخدام الفعل الجديد
    eq = create_simple_equation("خالد", "درس", "رياضيات", kb)
    print(eq.to_formal_notation())
}
```

## التحليل التلقائي (Parser)

```bayan
hybrid {
    kb = KnowledgeBase()
    parser = LinguisticEquationParser(kb)
    
    sentences = [
        "محمد أكل تفاحة",
        "سارة شربت ماء",
        "أحمد ضرب كرة",
        "فاطمة كتبت رسالة"
    ]
    
    for sentence in sentences:
        eq = parser.parse(sentence)
        if eq:
            print(f"{sentence} →")
            print(f"  {eq.to_formal_notation()}")
            
            # عرض النتائج المستنتجة
            for result in eq.results:
                print(f"    • {result}")
}
```

## أمثلة متقدمة

### مثال 1: سلسلة أحداث

```bayan
hybrid {
    kb = KnowledgeBase()
    
    # حدث 1: محمد ذهب إلى السوق
    eq1 = LinguisticEquation(
        {"محمد": Role("فاعل"), "السوق": Role("مكان")},
        "ذهب",
        "حركة"
    )
    eq1.location = "السوق"
    
    # حدث 2: محمد أكل تفاحة
    eq2 = parse_sentence("محمد أكل تفاحة", kb)
    
    # حدث 3: محمد رجع البيت
    eq3 = parse_sentence("محمد رجع البيت", kb)
    
    # تسلسل الأحداث
    events = [eq1, eq2, eq3]
    for i, eq in enumerate(events, 1):
        print(f"{i}. {eq.to_natural_language()}")
}
```

### مثال 2: تحليل قصة

```bayan
hybrid {
    story = """
    أحمد ذهب المدرسة
    أحمد كتب واجب
    أحمد رجع البيت
    """
    
    kb = KnowledgeBase()
    parser = LinguisticEquationParser(kb)
    
    # تحليل كل جملة
    equations = []
    for line in story.strip().split("\n"):
        eq = parser.parse(line.strip())
        if eq:
            equations.append(eq)
    
    # عرض التحليل الكامل
    print("تحليل القصة:")
    for eq in equations:
        print(f"\nالجملة: {eq.to_natural_language()}")
        print(f"المعادلة: {eq.to_formal_notation()}")
}
```

## الدوال المتاحة

### في `builtins.py`

```python
# قاعدة معرفة
kb = KnowledgeBase()

# تحليل جملة
eq = parse_sentence("محمد أكل تفاحة", kb)

# معادلة سريعة
eq = create_simple_equation("أحمد", "ضرب", "كرة", kb)

# معادلة كاملة
eq = LinguisticEquation(entities, event, event_type)

# استنتاج النتائج
results = eq.compute_results(kb)

# تحويل إلى لغة طبيعية
text = eq.to_natural_language()

# تحويل إلى صيغة رسمية
formula = eq.to_formal_notation()
```

## المزايا

1. **لغة طبيعية → رياضيات**: تحويل تلقائي للجمل
2. **استنتاج سببي**: استنتاج النتائج من قاعدة المعرفة
3. **قابلية التوسع**: إضافة أحداث مخصصة بسهولة
4. **تحليل تلقائي**: Parser للجمل العربية
5. **8 أدوار**: تصنيف دقيق للكيانات
6. **9 أنواع أحداث**: تغطية شاملة
7. **قابلية التصدير**: تحويل إلى JSON

## الملفات ذات الصلة

- **الكود المصدري**: [`bayan/bayan/linguistic_equation.py`](file:///home/al-mubtakir/Documents/bayan_python_ide14/bayan/bayan/linguistic_equation.py)
- **الأمثلة**: [`examples/linguistic_equations_demo.bayan`](file:///home/al-mubtakir/Documents/bayan_python_ide14/examples/linguistic_equations_demo.bayan)
- **API**: [`bayan/bayan/builtins.py`](file:///home/al-mubtakir/Documents/bayan_python_ide14/bayan/bayan/builtins.py)

## انظر أيضاً

- [نظام المعادلة الأم](MOTHER_EQUATION_GUIDE.md) - تمثيل شامل للأشياء
- [نظام GSE](GSE_SYSTEM_GUIDE.md) - التعلم التكيفي
- [أمثلة متقدمة](EXAMPLES.md) - المزيد من الأمثلة
