# توثيق القدرات الإدراكية | Cognitive Capabilities Documentation
## Bayan Core - نواة بيان

---

## 1. محرك الحوار الذكي | ConversationEngine

**الملف:** `bayan/bayan/cognitive/conversation_engine.py`

### الوصف
نظام محادثة ذكي يتميز بذاكرة قصيرة وطويلة المدى، قادر على تتبع السياق وإدارة الحوار.

### المكونات الرئيسية

| الفئة | الوظيفة |
|-------|---------|
| `Message` | تمثيل رسالة واحدة (دور + محتوى + وقت + بيانات وصفية) |
| `ConversationTurn` | دور كامل (رسالة مستخدم + رد + لقطة سياق) |
| `ConversationMemory` | ذاكرة قصيرة/طويلة المدى مع حفظ/تحميل |
| `ContextTracker` | تحليل الرسائل واستخراج الموضوع والنية والكيانات |
| `DialogueManager` | إدارة تدفق الحوار وتحديد هيكل الاستجابة |
| `ConversationEngine` | المحرك الرئيسي الذي يجمع كل المكونات |

### الاستخدام
```python
from bayan.bayan.cognitive import ConversationEngine

engine = ConversationEngine()

# محادثة بسيطة
response = engine.chat("مرحباً، كيف حالك؟")
print(response)

# محادثة مع سياق
engine.chat("أريد معرفة عن الذكاء الاصطناعي")
engine.chat("ما هي تطبيقاته؟")  # يفهم السياق

# حفظ الذاكرة
engine.memory.save("conversation_history.json")
```

### الميزات
- ✅ ذاكرة قصيرة المدى (آخر 10 أدوار)
- ✅ ذاكرة طويلة المدى (ملخصات، حقائق، ملف تعريف)
- ✅ تتبع المواضيع والنوايا
- ✅ تحليل المزاج
- ✅ قوالب استجابة متعددة

---

## 2. التعلم التفاعلي | LearningAgent

**الملف:** `bayan/bayan/cognitive/interactive_learning.py`

### الوصف
نظام يتعلم حقائق وقواعد جديدة من النصوص والمحادثات ويضيفها لقاعدة المعرفة.

### المكونات الرئيسية

| الفئة | الوظيفة |
|-------|---------|
| `FactType` | أنواع الحقائق (تعريف، خاصية، علاقة، سببية...) |
| `ExtractedFact` | حقيقة مستخرجة مع ثقة ومصدر |
| `InducedRule` | قاعدة مستنبطة من أنماط متكررة |
| `FactExtractor` | استخراج الحقائق بأنماط لغوية عربية |
| `RuleInducer` | استنباط قواعد من مجموعة حقائق |
| `LearningAgent` | الوكيل الموحد للتعلم |

### الاستخدام
```python
from bayan.bayan.cognitive import LearningAgent

agent = LearningAgent()

# التعلم من نص
text = """
الذكاء الاصطناعي هو فرع من علوم الحاسوب.
التعلم الآلي يعني قدرة الآلة على التعلم.
"""
result = agent.learn_from_text(text)
print(f"الحقائق المتعلمة: {result['facts_learned']}")

# التعليم المباشر
agent.teach("الشمس هي نجم في مجرتنا")

# استعلام
results = agent.query_learned("الذكاء")

# إحصائيات
stats = agent.get_learning_stats()
```

### أنماط الاستخراج المدعومة
| النمط | المثال |
|-------|--------|
| تعريف | "X هو Y" |
| خاصية | "X له Y" |
| علاقة | "X مثل Y" |
| سببية | "X يسبب Y" |
| زمنية | "X قبل Y" |
| مكانية | "X في Y" |

---

## 3. الاستنباط العكسي | AbductionEngine

**الملف:** `bayan/bayan/cognitive/abduction_engine.py`

### الوصف
محرك استدلال عكسي - من النتيجة إلى السبب المحتمل. يجيب على "لماذا حدث هذا؟"

### المكونات الرئيسية

| الفئة | الوظيفة |
|-------|---------|
| `HypothesisType` | أنواع الفرضيات (سبب مباشر، غير مباشر، شرط...) |
| `Hypothesis` | فرضية مع احتمالية وأدلة داعمة/معارضة |
| `HypothesisGenerator` | توليد فرضيات محتملة |
| `CausalReasoner` | تحليل سلاسل السبب والنتيجة |
| `AbductionEngine` | المحرك الموحد |

### الاستخدام
```python
from bayan.bayan.cognitive import AbductionEngine

engine = AbductionEngine()

# إضافة معرفة سببية
engine.add_causal_knowledge("ماس كهربائي", "حريق")
engine.add_causal_knowledge("مطر", "انزلاق")

# لماذا حدث هذا؟
answer = engine.why("حدث حريق")
print(answer)  # "لأن ماس كهربائي"

# ما الذي سبب هذا؟
causes = engine.what_caused("فشل المشروع")
for cause in causes:
    print(f"- {cause}")

# هل هذا تفسير صحيح؟
valid, explanation = engine.is_valid_explanation("مطر", "انزلاق")
```

---

## 4. القصص السببية | CausalStoriesEngine

**الملف:** `bayan/bayan/cognitive/causal_stories.py`

### الوصف
إنشاء سيناريوهات "ماذا لو" باستخدام العوالم المتوازية لمحرك الاستنباط.

### المكونات الرئيسية

| الفئة | الوظيفة |
|-------|---------|
| `StoryEvent` | حدث في القصة مع تبعات وشروط |
| `Scenario` | سيناريو كامل مع أحداث ونتيجة |
| `StorySimulator` | محاكاة تسلسل الأحداث |
| `WorldBrancher` | تفرع العوالم المتوازية |
| `OutcomePredictor` | توقع نتائج السيناريو |
| `CausalStoriesEngine` | المحرك الموحد |

### الاستخدام
```python
from bayan.bayan.cognitive import CausalStoriesEngine

engine = CausalStoriesEngine()

# ماذا لو؟
scenario1 = engine.what_if("بدأنا المشروع بميزانية أكبر")
print(f"النتيجة: {scenario1.final_outcome}")
print(f"الاحتمالية: {scenario1.probability:.2f}")

# أفضل حالة
best = engine.best_case("إطلاق المنتج")

# أسوأ حالة
worst = engine.worst_case("التأخر في التسليم")

# مقارنة السيناريوهات
comparison = engine.compare_scenarios(best, worst)
print(comparison['recommendation'])

# تحليل المخاطر
risks = engine.get_risks(worst)
```

---

## 5. تصدير المعرفة | KnowledgeExporter

**الملف:** `bayan/bayan/cognitive/knowledge_export.py`

### الوصف
تصدير قاعدة المعرفة بصيغ متعددة للتكامل مع أنظمة أخرى.

### الصيغ المدعومة

| الصيغة | الاستخدام |
|--------|----------|
| JSON | APIs والتطبيقات |
| RDF/Turtle | الويب الدلالي |
| OWL/XML | الأنطولوجيا |
| YAML | ملفات التكوين |
| Markdown | التوثيق |

### الاستخدام
```python
from bayan.bayan.cognitive import KnowledgeExporter

exporter = KnowledgeExporter()

# تصدير JSON
json_content = exporter.export_json("knowledge.json")

# تصدير RDF
rdf_content = exporter.export_rdf("knowledge.ttl")

# تصدير OWL
owl_content = exporter.export_owl("knowledge.owl")

# تصدير Markdown
md_content = exporter.export_markdown("knowledge.md", 
                                       title="قاعدة المعرفة")

# تصدير كل الصيغ معاً
files = exporter.export_all("/output/", "my_knowledge")
```

---

## 6. الوكيل الذكي | BayanAgent

**الملف:** `bayan/bayan/cognitive/intelligent_agent.py`

### الوصف
نظام وكيل يجمع كل القدرات ويمكنه تخطيط وتنفيذ مهام معقدة متعددة الخطوات.

### المكونات الرئيسية

| الفئة | الوظيفة |
|-------|---------|
| `Task` | مهمة مع حالة وأولوية وتبعيات |
| `Tool` | أداة متاحة للوكيل |
| `TaskPlanner` | تحليل وتقسيم المهام |
| `ToolExecutor` | تنفيذ الأدوات |
| `BayanAgent` | الوكيل الموحد |

### الاستخدام
```python
from bayan.bayan.cognitive import BayanAgent

agent = BayanAgent()

# تنفيذ هدف معقد
result = agent.execute_goal("صمم ترس حلزوني للمحرك")
print(f"نجاح: {result['success']}")
print(f"المهام: {len(result['tasks'])}")

# طرح سؤال
answer = agent.ask("ما هو الذكاء الاصطناعي؟")

# تذكر/استرجاع
agent.remember("project_name", "بيان")
name = agent.recall("project_name")

# عرض القدرات
for cap in agent.list_capabilities():
    print(f"- {cap}")
```

### الأدوات المتاحة
- `query_knowledge` - البحث في قاعدة المعرفة
- `add_fact` - إضافة حقيقة
- `reason` - الاستنباط المنطقي
- `explain_why` - شرح الأسباب
- `generate_text` - توليد نص
- `create_3d_part` - إنشاء قطعة 3D

---

## الاستيراد الموحد

```python
from bayan.bayan.cognitive import (
    ConversationEngine,
    ConversationMemory,
    LearningAgent,
    FactExtractor,
    AbductionEngine,
    HypothesisGenerator,
    CausalStoriesEngine,
    KnowledgeExporter,
    BayanAgent,
    TaskPlanner,
    ToolExecutor
)
```

---

*تاريخ التوثيق: 2025-12-14*
