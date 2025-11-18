# Bayan Language - Quick Reference for LLMs

**Last Updated**: 2025-11-17

**Project Status**:
- ✅ 461/605 tests passing (76.2%)
- ✅ 42 tutorial files (21 Arabic + 21 English)
- ✅ 9,318+ lines of documentation
- ✅ Conceptual LM system (4 layers, 6 circuits, 5 programs)
- ✅ Advanced NLP dialogue system
- ✅ Causal networks, entity system, semantic networks

---

## Essential Rules

1. **Wrap all code in `hybrid { ... }`**
2. **Use `:` before `{` in functions, classes, and control structures**
3. **Use `{ }` braces for all blocks**
4. **End logic facts/rules with `.`**
5. **Logic variables start with `?`**

## Syntax Template

```bayan
hybrid {
    # Imperative
    x = 10
    
    # Function
    def function_name(param): {
        return param * 2
    }
    
    # Class
    class ClassName: {
        def __init__(self, value): {
            self.value = value
        }
    }
    
    # Control flow
    if condition: {
        statement
    }
    
    for item in items: {
        statement
    }
    
    # Logic
    fact("data").
    rule(?X) :- condition(?X).
    results = query rule(?X)?
}
```

## Keywords

### Traditional Keywords (الكلمات التقليدية)

**English**: `if`, `elif`, `else`, `for`, `in`, `while`, `def`, `return`, `class`, `self`, `True`, `False`, `None`, `and`, `or`, `not`, `try`, `except`, `finally`, `raise`, `with`, `async`, `await`, `yield`, `lambda`, `import`, `from`, `as`, `global`, `del`, `pass`, `break`, `continue`

**Arabic**: `اذا`, `والا_اذا`, `والا`, `لكل`, `في`, `بينما`, `دالة`, `ارجع`, `صنف`, `الذات`, `صحيح`, `خطأ`, `لاشيء`

### Hybrid/Logic Keywords (الكلمات الهجينة/المنطقية)

**English**: `hybrid`, `query`, `fact`, `rule`

### Causal-Semantic System (نظام السببية والدلالة) ⭐ NEW

**English**: `cause_effect`, `relation`

**Arabic**: `سبب_نتيجة`, `علاقة`

**Usage**:
```bayan
hybrid {
    # Causal law with reason
    سبب_نتيجة("رفع_شيء_لفوق", "يسقط", "جاذبية", 1.0).

    # Semantic relation
    علاقة("الاستحمام", "في", "حمام", 0.9).

    # Query
    query سبب_نتيجة(?condition, "يسقط", ?cause, ?strength).
}
```

### Entity System (نظام الكيانات)

**English**: `entity`, `apply`, `concept`

**Arabic**: `كيان`, `طبق`, `مفهوم`

### Temporal Keywords (الكلمات الزمنية)

**English**: `temporal`, `first`, `then`, `lastly`, `within`, `schedule`, `delay`, `every`, `seconds`, `minutes`, `hours`, `once`, `limit`

**Arabic**: `زمنيا`, `أولا`, `ثم`, `أخيرا`, `خلال`, `جدولة`, `تأخير`, `كل`, `ثانية`, `ثواني`, `دقيقة`, `دقائق`, `ساعة`, `ساعات`, `مرة_واحدة`, `حد`

### Constraint Keywords (كلمات القيود)

**English**: `where`, `requires`, `ensures`, `invariant`

**Arabic**: `حيث`, `يتطلب`, `يشترط`, `يضمن`, `يكفل`, `ثابت`, `ثوابت`

### Pattern Matching (مطابقة الأنماط)

**English**: `match`, `case`, `default`, `when`

**Arabic**: `طابق`, `حالة`, `افتراضي`, `افتراضية`, `عندما`

### Reactive Programming (البرمجة التفاعلية)

**English**: `reactive`, `watch`, `computed`

**Arabic**: `تفاعلي`, `تفاعلية`, `راقب`, `مراقبة`, `محسوب`, `محسوبة`

### Cognitive-Semantic Model (النموذج المعرفي-الدلالي)

**English**: `cognitive_entity`, `cognitive_event`, `event`, `trigger`, `concurrent`, `pattern`, `conceptual_blueprint`, `idea`, `participants`, `strength`, `transform`, `reactions`, `structure`, `express`, `entities`, `result`, `state_changes`, `linguistic_forms`, `degree`, `role`

**Arabic**: `كيان_معرفي`, `حدث_معرفي`, `حدث`, `أطلق`, `متزامن`, `قالب`, `مخطط_مفاهيمي`, `فكرة`, `مشاركون`, `قوة`, `تحويل`, `ردود_فعل`, `ردود`, `بنية`, `تعبير`, `كيانات`, `نتيجة`, `تغييرات_الحالة`, `تغييرات`, `أشكال_لغوية`, `أشكال`, `درجة`, `دور`

### Semantic Programming & Knowledge (البرمجة الدلالية والمعرفة)

**English**: `meaning`, `semantic_query`, `information`, `content`, `context`, `time`, `place`, `source`, `certainty`, `inference_rule`, `infer_from`, `contradiction`, `between`, `resolve`, `evolving_knowledge`, `knowledge`, `current_value`, `history`, `future_prediction`, `ontology`, `root`, `taxonomy`, `memory`, `store`, `retrieve`, `similarity`, `narrative`, `characters`, `generate_narrative`, `based_on`, `current_context`

**Arabic**: `معنى`, `استعلام_دلالي`, `معلومة`, `محتوى`, `سياق`, `زمن`, `مكان`, `مصدر`, `يقين`, `قاعدة_استنتاج`, `استنتج_من`, `تناقض`, `بين`, `حل`, `معرفة_متطورة`, `معرفة`, `قيمة_حالية`, `تاريخ`, `توقع_مستقبلي`, `أنطولوجيا`, `جذر`, `تصنيف`, `ذاكرة`, `خزن`, `استرجع`, `تشابه`, `سرد`, `شخصيات`, `ولد_سرد`, `بناء_على`, `السياق_الحالي`

### Existential Model (النموذج الوجودي)

**English**: `domain`, `basic_entity`, `environment`, `in_domain`, `of_type`, `existential_being`, `dimensions`, `spatial`, `domain_specific`, `intrinsic_properties`, `inherited_meanings`, `intrinsic_meanings`, `laws`, `domain_relation`, `domain_action`, `metaphorical_meaning`, `built_on`, `applies_to`, `domain_law`, `existential_query`, `about`

**Arabic**: `مجال`, `كيان_أساسي`, `بيئة`, `في_مجال`, `من_نوع`, `كائن_وجودي`, `أبعاد`, `مكاني`, `خاص_بالمجال`, `خصائص_جوهرية`, `معاني_موروثة`, `معاني_جوهرية`, `قوانين`, `علاقة_مجالية`, `فعل_مجالي`, `معنى_مجازي`, `مبني_على`, `ينطبق_على`, `قانون_مجالي`, `استعلام_وجودي`, `حول`

### Spatial & Temporal Relations (العلاقات المكانية والزمنية)

**Spatial**: `above`/`فوق`, `below`/`تحت`, `right`/`يمين`, `left`/`يسار`, `front`/`أمام`, `back`/`خلف`, `north`/`شمال`, `south`/`جنوب`, `east`/`شرق`, `west`/`غرب`

**Temporal**: `before`/`قبل`, `after`/`بعد`, `during`/`أثناء`, `now`/`الآن`

**Prepositions**: `in`/`في`, `from`/`من`, `at`/`عند`, `on`/`على`, `to`/`إلى`

### Life Domain (مجال الحياة)

**English**: `emergence`, `life`, `growth`, `death`, `decay`, `living`, `eat`, `drink`, `food`, `satiety`, `hunger`, `work`, `pain`, `effect`, `affected`, `struggle`, `gain`, `loss`, `interior`, `face`, `shadow`, `love`, `affection`, `aversion`, `proximity`, `cooperation`, `interaction`, `product`, `laugh`, `cry`, `speak`, `think`, `inhabits`, `moves_to`, `affected_by`

**Arabic**: `ظهور`, `حياة`, `نمو`, `موت`, `تحلل`, `حي`, `أكل`, `شرب`, `طعام`, `شبع`, `جوع`, `عمل`, `ألم`, `تأثير`, `متأثر`, `كفاح`, `كسب`, `خسارة`, `داخل`, `وجه`, `ظل`, `حب`, `مودة`, `نفور`, `قرب`, `تعاون`, `تفاعل`, `منتج`, `ضحك`, `بكاء`, `كلام`, `تفكير`, `يسكن`, `ينتقل_إلى`, `متأثر_بـ`

## Data Types

```bayan
hybrid {
    integer = 42
    floating = 3.14
    string = "text"
    arabic_string = "نص عربي"
    boolean = True
    none_value = None
    list_data = [1, 2, 3]
    dict_data = {"key": "value"}
    set_data = {1, 2, 3}
}
```

## Control Flow

```bayan
hybrid {
    # If-elif-else
    if x > 0: {
        print("positive")
    }
    elif x < 0: {
        print("negative")
    }
    else: {
        print("zero")
    }
    
    # For loop
    for i in range(5): {
        print(i)
    }
    
    # While loop
    while x < 10: {
        x = x + 1
    }
}
```

## Functions

```bayan
hybrid {
    # Basic
    def add(a, b): {
        return a + b
    }
    
    # Default params
    def greet(name, msg="Hello"): {
        return msg + " " + name
    }
    
    # *args
    def sum_all(*nums): {
        total = 0
        for n in nums: {
            total = total + n
        }
        return total
    }
    
    # **kwargs
    def print_info(**info): {
        for key in info: {
            print(key + ": " + str(info[key]))
        }
    }
}
```

## Classes

```bayan
hybrid {
    class Person: {
        def __init__(self, name, age): {
            self.name = name
            self.age = age
        }
        
        def greet(self): {
            return "Hello, " + self.name
        }
    }
    
    person = Person("أحمد", 25)
    print(person.greet())
}
```

## Logic Programming

```bayan
hybrid {
    # Facts (end with .)
    parent("أحمد", "محمد").
    parent("محمد", "علي").
    
    # Rules (use :-)
    grandparent(?X, ?Z) :- parent(?X, ?Y), parent(?Y, ?Z).
    
    # Query (use ?)
    results = query grandparent(?GP, "علي")?
    
    for result in results: {
        print(result["?GP"])
    }
    
    # Dynamic KB
    assertz(new_fact("data"))
    retract(old_fact("data"))
    
    # Meta-predicates
    all_results = query findall(?X, fact(?X), ?List)?
}
```

## Built-in Functions

```bayan
hybrid {
    # Type conversion
    int("123"), float("3.14"), str(456)
    
    # String
    upper("text"), lower("TEXT"), len("text")
    
    # List/Collection
    len([1,2,3]), sorted([3,1,2]), sum([1,2,3])
    min([1,2,3]), max([1,2,3]), reversed([1,2,3])
    
    # Functional
    list(map(lambda x: x*2, [1,2,3]))
    list(filter(lambda x: x>0, [-1,0,1]))
    enumerate([1,2,3]), zip([1,2], [3,4])
}
```

## Common Patterns

### Pattern 1: Hybrid OOP + Logic
```bayan
hybrid {
    class Student: {
        def __init__(self, name, grade): {
            self.name = name
            self.grade = grade
            assertz(student(name, grade))
        }
    }
    
    s1 = Student("أحمد", 85)
    s2 = Student("فاطمة", 95)
    
    results = query student(?N, ?G), ?G >= 90?
    for r in results: {
        print(r["?N"])
    }
}
```

### Pattern 2: Expert System
```bayan
hybrid {
    symptom("p1", "fever").
    symptom("p1", "cough").
    
    diagnosis(?P, "flu") :- symptom(?P, "fever"), symptom(?P, "cough").
    
    results = query diagnosis("p1", ?D)?
    print(results[0]["?D"])
}
```

### Pattern 3: Data Processing
```bayan
hybrid {
    data = [85, 92, 78, 95, 88]

    avg = sum(data) / len(data)
    high = list(filter(lambda x: x >= 90, data))

    print("Average: " + str(avg))
    print("High: " + str(high))
}
```

### Pattern 4: Probabilistic Reasoning (NEW! 🎲)
```bayan
hybrid {
    # Probabilistic facts
    prob("is_green", "garden", 0.7).
    prob("has_trees", "garden", 0.6).

    # Uncertainty tools (bilingual)
    query ربما("is_green", "garden").      # maybe (70% > 50%) ✅
    query محتمل("is_green", "garden").     # likely (70% > 70%) ❌
    query maybe("has_trees", "garden").    # maybe (60% > 50%) ✅

    # Multiple states calculation
    state_green_with_trees("garden", ?prob) :-
        prob("is_green", "garden", ?p1),
        prob("has_trees", "garden", ?p2),
        ?prob is ?p1 * ?p2.  # 0.7 × 0.6 = 0.42 (42%)

    query state_green_with_trees("garden", ?p).
}
```

**Uncertainty Tools:**
- `ربما/maybe` - probability > 50%
- `محتمل/likely` - probability > 70%
- `غير_محتمل/unlikely` - probability < 30%
- `ممكن/possible` - probability between 20% and 80%
- `مؤكد/certain` - probability > 95%

## ✅ Checklist for LLMs

- [ ] Code wrapped in `hybrid { }`
- [ ] `:` before `{` in def/class/if/for/while
- [ ] `{ }` braces for all blocks
- [ ] `.` at end of facts/rules
- [ ] `?` prefix for logic variables
- [ ] String concatenation with `+` (not multiple print args)
- [ ] Arabic text supported in strings

## Common Mistakes to Avoid

❌ **Wrong**: Missing `hybrid`
```bayan
x = 10  # ERROR
```

❌ **Wrong**: Missing `:`
```bayan
hybrid {
    def f(x) {  # ERROR: missing :
        return x
    }
}
```

❌ **Wrong**: Missing braces
```bayan
hybrid {
    if x > 0:  # ERROR: missing { }
        print(x)
}
```

❌ **Wrong**: Missing `.` in logic
```bayan
hybrid {
    parent("a", "b")  # ERROR: missing .
}
```

✅ **Correct**:
```bayan
hybrid {
    def f(x): {
        return x
    }

    if x > 0: {
        print(x)
    }

    parent("a", "b").
}
```

---

## Advanced Features Quick Reference

### Causal Networks
```bayan
create_network("name", "desc", "custom")
add_node("net", "node", "type", "label")
add_causal_relation("net", "from", "to", "type", "strength")
infer_causal_chain("net", "start", "end", "max_depth")
```

### Entity System
```bayan
entity EntityName: {
    states: {"state1": 0.5, "state2": 0.8},
    actions: {
        "action1": {
            formula: "value * states['state1']",
            effects: {"state1": "+0.1", "state2": "-0.2"}
        }
    }
}
perform("action", ["Entity.1.0"], action_value=1.0)
```

### NLP Dialogue
```bayan
add_fact("subject", "predicate", "object")
add_fact("X = Y")  # Bidirectional synonym
ask("ما هو X؟")
get_answer_with_policy("query", "most_recent")
```

### Conceptual LM
```bayan
run_meaning_program("program_name", {"detail_level": "high", "focus": "causal"})
realize_surface(trace, "ar", "high")
```

### Semantic Networks
```bayan
meaning("X", "Y")
information("X", "relation", "Y")
inference_rule("pattern", "conclusion")
```

### Causal-Semantic Knowledge Graphs ⭐ NEW
```bayan
# Define causal laws
سبب_نتيجة("رفع_شيء_لفوق", "يسقط", "جاذبية", 1.0).
سبب_نتيجة("دراسة_مجتهدة", "نجاح", "اكتساب_معرفة", 0.9).

# Define semantic relations
علاقة("الاستحمام", "في", "حمام", 0.9).
علاقة("البيت", "فيه", "حمام", 0.95).
علاقة("النهر", "هو", "ماء", 1.0).

# Query causal laws
query سبب_نتيجة("رفع_شيء_لفوق", ?result, ?cause, ?strength).
# Returns: ?result="يسقط", ?cause="جاذبية", ?strength=1.0

# Query semantic relations
query علاقة("الاستحمام", ?relation_type, ?place, ?strength).
# Returns: ?relation_type="في", ?place="حمام", ?strength=0.9
```

### Similarity & Synonyms
```bayan
similar(?X, ?Y, ?Score, ?Kind, ?Domain)
synonym(?X, ?Y, ?S)
close(?X, ?Y, ?Kind)
```

---

**Use this reference when generating Bayan code. Follow the syntax strictly!**

**For more details**: See `docs/تعليمية/README.md` for 42 comprehensive tutorial files.

