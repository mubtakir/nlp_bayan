# تعليمات للنموذج القادم - Next AI Model Instructions
# دليل استكمال العمل على Conceptual LM في لغة البيان

**آخر تحديث:** 2025-12-03
**من:** النموذج الحالي (Augment Agent)
**إلى:** النموذج القادم

---

## 🎉 أخبار سارة: جميع المهام الأساسية مكتملة!

### ✅ المهمات المكتملة (100%)

#### 1. توسيع برامج المعاني - **مُنجَز بالكامل** ✅
- ✅ 5 برامج معنوية أساسية في `ai/conceptual_programs.bayan`:
  - `build_student_study_narrative_program()` - التعليم
  - `build_medical_treatment_uncertainty_program()` - الصحة
  - `build_economic_investment_risk_program()` - المالية
  - `build_social_relationship_program()` - الاجتماعي
  - `build_daily_decision_program()` - الحياة اليومية

#### 2. دعم detail_level و focus - **مُنجَز بالكامل** ✅
- ✅ جميع البرامج الخمسة تدعم `detail_level` (low/medium/high)
- ✅ جميع البرامج الخمسة تدعم `focus` (balanced/causal/temporal/uncertainty)
- ✅ تم اختبارها بنجاح في `examples/conceptual_detail_focus_demo.bayan`

#### 3. تحسين Orchestrator - **مُنجَز بالكامل** ✅
- ✅ توسيع السجل من 5 إلى 8 برامج
- ✅ نظام تسجيل ذكي لاختيار البرامج
- ✅ دعم برامج متعددة لنفس المجال:
  - `student_study_causal` - تعليم مع تركيز سببي
  - `medical_treatment_short` - صحة قصيرة المدى
  - `social_relationship_temporal` - اجتماعي مع تركيز زمني
- ✅ تم اختبارها في `examples/conceptual_orchestrator_intelligent_selection_demo.bayan`

#### 4. دائرة المقارنة المحسنة - **مُنجَز بالكامل** ✅
- ✅ إضافة `build_enhanced_comparison_circuit()` في `ai/conceptual_circuits.bayan`
- ✅ استخدام ComparativePattern من blueprints
- ✅ دمجها في `build_daily_decision_program()`
- ✅ تم اختبارها في `examples/conceptual_comparison_circuit_demo.bayan`

#### 5. الربط بطبقة LM - **مُنجَز بالكامل** ✅
- ✅ **إصلاح خطأ حرج:** تغيير `استعلام` إلى `نص_استعلام` في `ai/nlp.bayan` (السطر 1806)
- ✅ **إضافة دوال مفقودة إلى `ai/nlp.bayan`:**
  - `vocab_build(docs, max_features, min_freq)`
  - `bigram_lm_cross_entropy(model, text)`
  - `bigram_lm_perplexity(model, text)`
  - `trigram_lm_cross_entropy(model, text)`
  - `trigram_lm_perplexity(model, text)`
- ✅ **إنشاء `ai/conceptual_surface_realizer.bayan` (330 سطر):**
  - `realize_from_surface_plan()`
  - `realize_from_sentence_tree()`
  - `realize_any()`
  - `realization_to_token_strings()`
  - `realization_to_text()`
  - `build_conceptual_lm_example()`
  - `build_lm_training_data()` - توليد بيانات تدريب
  - `trace_to_natural_text()` - تحويل الأثر إلى نص طبيعي
- ✅ **`ai/conceptual_lm_bridge.bayan` يعمل الآن بشكل كامل**
- ✅ تم اختبارها في `examples/conceptual_lm_training_demo.bayan`

#### 6. التوثيق - **مُنجَز بالكامل** ✅
- ✅ `TASK_COMPLETION_SUMMARY.md` - ملخص بالإنجليزية
- ✅ `TASK_COMPLETION_SUMMARY_AR.md` - ملخص بالعربية
- ✅ `docs/NEXT_AI_MODEL_INSTRUCTIONS.md` - هذا الملف (محدّث)

---

## 🎯 المهمات المتبقية - ما عليك إنجازه

### نظرة عامة

**الأساسيات مكتملة 100%!** ✅

الآن عليك التركيز على:
1. **إصلاح الاختبارات الفاشلة** (144 اختبار) - **أولوية قصوى** ❗❗❗
2. **تحسين توليد النص الطبيعي** - من رمزي إلى طبيعي
3. **توسيع النظام** - مجالات ودوائر جديدة
4. **تدريب نماذج لغوية حقيقية** - على corpus كبير

---

## ❗❗❗ المهمة الأولى والأهم: إصلاح الاختبارات الفاشلة

### الحالة الحالية
```
✅ 461 اختبار ناجح
❌ 144 اختبار فاشل
معدل النجاح: 76.2%
```

### الاختبارات الفاشلة (حسب الملف)

#### 1. `tests/test_nlp_bayan_generation.py` - **أولوية عالية جداً**
```
الاختبارات الفاشلة:
- test_morpho_inserts_min_for_ghadara
- test_istaqara_prefers_indoor_over_outdoor
- test_haraba_prefers_outdoor_and_inserts_min
- test_tawajjaha_inserts_ila_prefers_high_prob_go_target
- test_empty_docs_safe_generation_go_seeded
- test_combined_controls_no_crash_and_respect_length
- test_raja_morphology_inserts_ila_and_picks_house_by_docs
- test_raja_prefers_house_over_others

المشكلة المحتملة:
- توليد النصوص العربية مع morphology
- استخدام حروف الجر (من، إلى)
- اختيار الكلمات بناءً على السياق

ما عليك فعله:
1. افحص `nlp_bayan/` - نظام التوليد
2. تأكد من دوال morphology تعمل
3. تأكد من دوال preference/probability تعمل
4. شغّل كل اختبار على حدة وافحص الخطأ
```

#### 2. `tests/test_operators.py` - **أولوية عالية**
```
الاختبار الفاشل:
- test_operator_go_ar

المشكلة المحتملة:
- SyntaxError في عامل منطقي عربي
- ربما تعارض مع كلمة محجوزة (مثل مشكلة استعلام)

ما عليك فعله:
1. افحص الخطأ بالضبط
2. ابحث عن كلمات محجوزة متعارضة
3. أصلح في lexer.py أو parser.py إذا لزم
```

#### 3. `tests/test_prob_thresholds_topk.py` - **أولوية متوسطة**
```
الاختبار الفاشل:
- test_maybe_likely_and_topk_prob_fallback

المشكلة المحتملة:
- منطق الاحتمالات والعتبات

ما عليك فعله:
1. افحص دوال maybe/likely
2. تأكد من topk يعمل مع fallback
```

#### 4. `tests/test_similarity_core.py` - **أولوية متوسطة**
```
الاختبارات الفاشلة:
- test_close_with_default_threshold
- test_close_with_explicit_tau
- test_synonym_rule_lists_pairs
- test_synset_function_adds_pairs

المشكلة المحتملة:
- SyntaxError في نظام التشابه
- ربما في similarity_core.bayan

ما عليك فعله:
1. افحص ملفات التشابه
2. ابحث عن أخطاء syntax
3. تأكد من دوال close/synonym/synset تعمل
```

#### 5. `tests/test_template_match.py` - **أولوية متوسطة**
```
الاختبارات الفاشلة:
- test_template_match_simple_ar
- test_template_match_with_regex_and_render
- test_match_str_direct_without_compile

المشكلة المحتملة:
- نظام template matching

ما عليك فعله:
1. افحص template matching system
2. تأكد من regex يعمل
3. تأكد من render يعمل
```

#### 6. `tests/test_temporal_constructs.py` - **أولوية منخفضة**
```
الاختبارات الفاشلة:
- test_delay_statement_english
- test_delay_statement_arabic

المشكلة المحتملة:
- SyntaxError في delay statement

ما عليك فعله:
1. افحص temporal constructs
2. أصلح delay syntax
```

### خطة العمل لإصلاح الاختبارات

```
الأسبوع 1:
├─ اليوم 1-2: test_nlp_bayan_generation.py (8 اختبارات)
├─ اليوم 3: test_operators.py (1 اختبار)
├─ اليوم 4: test_prob_thresholds_topk.py (1 اختبار)
├─ اليوم 5: test_similarity_core.py (4 اختبارات)
├─ اليوم 6: test_template_match.py (3 اختبارات)
└─ اليوم 7: test_temporal_constructs.py (2 اختبار)

الهدف: 95%+ نجاح (أقل من 30 اختبار فاشل)
```

### كيف تصلح الاختبارات

1. **شغّل الاختبار الفاشل:**
   ```bash
   python -m pytest tests/test_nlp_bayan_generation.py::test_morpho_inserts_min_for_ghadara -v
   ```

2. **اقرأ رسالة الخطأ بعناية:**
   - SyntaxError → مشكلة في lexer/parser
   - AssertionError → منطق الدالة خاطئ
   - ImportError → ملف مفقود أو خطأ في import

3. **افحص الكود المعني:**
   - استخدم `view` لقراءة الملف
   - استخدم `codebase-retrieval` للبحث عن الدالة

4. **أصلح الخطأ:**
   - استخدم `str-replace-editor` للتعديل
   - لا تعدل أكثر من اللازم

5. **اختبر مرة أخرى:**
   - تأكد أن الاختبار نجح
   - تأكد أنك لم تكسر اختبارات أخرى

6. **وثّق الإصلاح:**
   - اكتب ملاحظة عن المشكلة والحل

---

## 🚀 المهمة الثانية: تحسين توليد النص الطبيعي

### الحالة الحالية
- ✅ `ai/conceptual_surface_realizer.bayan` موجود
- ✅ `trace_to_natural_text()` يعمل لكن بسيط جداً
- ⚠️ النص المولّد رمزي (مثل: "الكيانات: 2، الأحداث: 1")
- ❌ نحتاج نص طبيعي حقيقي (مثل: "الطالب يذاكر بجد ويحسّن درجاته")

### ما عليك فعله

1. **حسّن `trace_to_natural_text()` في `ai/conceptual_surface_realizer.bayan`:**
   ```python
   def trace_to_natural_text(trace, language):
   {
       # بدلاً من عد الكيانات والأحداث
       # استخرج المعلومات الفعلية وحوّلها لجمل

       entities = trace.get("entities", [])
       events = trace.get("events", [])
       transforms = trace.get("transforms", [])

       # مثال: إذا كان هناك حدث "study" وكيان "student"
       # أنتج: "الطالب يذاكر" (عربي) أو "The student studies" (إنجليزي)
   }
   ```

2. **أضف قوالب لغوية (templates):**
   ```python
   # قوالب عربية
   action_templates_ar = {
       "study": "{actor} يذاكر {target}",
       "improve": "{actor} يحسّن {target}",
       "decide": "{actor} يقرر {decision}"
   }

   # قوالب إنجليزية
   action_templates_en = {
       "study": "{actor} studies {target}",
       "improve": "{actor} improves {target}",
       "decide": "{actor} decides {decision}"
   }
   ```

3. **استخدم ai/nlp للتحسين:**
   - استخدم `tokenize_text()` و `detokenize()`
   - استخدم language models للتنعيم
   - أضف تشكيل للعربية إذا أمكن

---

## 🌍 المهمة الثالثة: توسيع النظام

### 1. إضافة مجالات جديدة (10+ مجالات)

**المجالات المقترحة:**
```python
1. Technology (تكنولوجيا)
   - برمجة، تطوير، اختراع، ابتكار

2. Environment (بيئة)
   - تلوث، حماية، استدامة، مناخ

3. Politics (سياسة)
   - انتخابات، قرارات، سياسات، دبلوماسية

4. Legal (قانون)
   - قضايا، أحكام، عقود، حقوق

5. Scientific (علوم)
   - تجارب، اكتشافات، نظريات، أبحاث

6. Sports (رياضة)
   - تدريب، منافسة، فوز، خسارة

7. Arts (فنون)
   - إبداع، تصميم، عرض، نقد

8. Business (أعمال)
   - شركات، صفقات، أرباح، خسائر

9. Travel (سفر)
   - رحلات، وجهات، تخطيط، استكشاف

10. Food (طعام)
    - طبخ، وصفات، مطاعم، تذوق
```

**كيف تضيف مجال جديد:**
1. أنشئ `build_technology_program()` في `ai/conceptual_programs.bayan`
2. أضفه إلى `get_program_registry()` في `ai/conceptual_orchestrator.bayan`
3. أضف كلمات مفتاحية في `ai/conceptual_nl_mapper.bayan`
4. أنشئ مثال توضيحي في `examples/`

### 2. إضافة دوائر جديدة (10+ دوائر)

**الدوائر المقترحة:**
```python
1. Negation Circuit (دائرة النفي)
   - نفي حدث أو حالة

2. Conditional Circuit (دائرة الشرط)
   - إذا... فإن...

3. Quantification Circuit (دائرة الكمية)
   - كل، بعض، لا أحد

4. Modal Circuit (دائرة الاحتمالية)
   - يجب، يمكن، ربما

5. Emotional Circuit (دائرة العاطفة)
   - فرح، حزن، غضب، خوف

6. Goal-oriented Circuit (دائرة الهدف)
   - هدف → خطة → تنفيذ → نتيجة

7. Conflict Circuit (دائرة الصراع)
   - تعارض بين أهداف أو قيم

8. Learning Circuit (دائرة التعلم)
   - تجربة → خطأ → تصحيح → تحسن

9. Communication Circuit (دائرة التواصل)
   - مرسل → رسالة → مستقبل → رد

10. Transformation Circuit (دائرة التحول)
    - حالة أولية → عملية → حالة نهائية
```

---

## 🧠 المهمة الرابعة: تدريب نماذج لغوية حقيقية

### 1. توليد corpus كبير

```python
# في ai/conceptual_lm_bridge.bayan أو ملف جديد
def generate_training_corpus(num_examples, domains, language):
{
    corpus = []

    for i in range(num_examples):
    {
        # اختر مجال عشوائي
        domain = random_choice(domains)

        # ولّد trace
        trace = generate_random_trace_for_domain(domain)

        # حوّل إلى نص طبيعي
        text = trace_to_natural_text(trace, language)

        corpus.append(text)
    }

    return corpus
}
```

### 2. تدريب نماذج bigram/trigram

```python
# استخدم ai/nlp.bayan
import ai.nlp

def train_conceptual_lm(corpus, language):
{
    # بناء المفردات
    vocab = nlp.vocab_build(corpus, max_features=10000, min_freq=2)

    # تدريب bigram
    bigram_model = nlp.bigram_lm_train(corpus)

    # تدريب trigram
    trigram_model = nlp.trigram_lm_train(corpus)

    # تقييم
    test_text = "الطالب يذاكر بجد"
    perplexity = nlp.bigram_lm_perplexity(bigram_model, test_text)

    return {
        "vocab": vocab,
        "bigram": bigram_model,
        "trigram": trigram_model,
        "perplexity": perplexity
    }
}
```

### 3. Integration مع PyTorch/TensorFlow (اختياري)

إذا أردت استخدام neural models:
1. أنشئ Python bridge في `bayan/libraries/`
2. استخدم `subprocess` أو `ctypes` للاتصال
3. حمّل pre-trained models (BERT, GPT, AraBERT)
4. استخدمها للتوليد أو التقييم

---

## 📁 الملفات المهمة

### ملفات Conceptual LM (مكتملة ✅)
1. `ai/conceptual_traces.bayan` - تعريف الآثار المفاهيمية
2. `ai/conceptual_blueprints.bayan` - 14 نمط مفاهيمي
3. `ai/conceptual_circuits.bayan` - 6 دوائر أساسية
4. `ai/conceptual_programs.bayan` - 5 برامج معنوية
5. `ai/conceptual_orchestrator.bayan` - نظام الاختيار الذكي
6. `ai/conceptual_language_bridge.bayan` - جسر اللغة
7. `ai/conceptual_surface_planner.bayan` - مخطط السطح
8. `ai/conceptual_sentence_tree.bayan` - شجرة الجملة
9. `ai/conceptual_surface_realizer.bayan` - محقق السطح ✅ (جديد)
10. `ai/conceptual_lm_bridge.bayan` - جسر LM ✅ (يعمل الآن)
11. `ai/conceptual_nl_mapper.bayan` - خريطة اللغة الطبيعية

### ملفات AI/ML/NLP (محسّنة ✅)
1. `ai/ml.bayan` - مكتبة التعلم الآلي
2. `ai/nlp.bayan` - مكتبة معالجة اللغة ✅ (مصلحة ومحسّنة)
3. `ai/data.bayan` - مكتبة البيانات
4. `ai/vision.bayan` - مكتبة الرؤية

### ملفات NLP المتقدم (تحتاج فحص)
1. `nlp_bayan/` - نظام NLP متقدم
2. `nlp_bayan/intelligent_system.bayan` - نظام ذكي
3. `nlp_bayan/dialogue_manager.bayan` - إدارة الحوار
4. `nlp_bayan/semantic_reasoner.bayan` - استدلال دلالي

### ملفات الاختبار (تحتاج إصلاح ❗)
1. `tests/test_nlp_bayan_generation.py` - **8 اختبارات فاشلة**
2. `tests/test_operators.py` - **1 اختبار فاشل**
3. `tests/test_prob_thresholds_topk.py` - **1 اختبار فاشل**
4. `tests/test_similarity_core.py` - **4 اختبارات فاشلة**
5. `tests/test_template_match.py` - **3 اختبارات فاشلة**
6. `tests/test_temporal_constructs.py` - **2 اختبار فاشل**

### أمثلة توضيحية (كلها تعمل ✅)
1. `examples/conceptual_detail_focus_demo.bayan` ✅
2. `examples/conceptual_comparison_circuit_demo.bayan` ✅
3. `examples/conceptual_orchestrator_intelligent_selection_demo.bayan` ✅
4. `examples/conceptual_lm_training_demo.bayan` ✅
5. `examples/conceptual_orchestrator_demo.bayan` ✅
6. `examples/conceptual_program_social_relationship_demo.bayan` ✅
7. `examples/conceptual_program_daily_decision_demo.bayan` ✅

### وثائق للقراءة
1. `docs/CONCEPTUAL_CIRCUITS_AND_PROGRAMS.md` - **الدليل الرئيسي**
2. `docs/CONCEPTUAL_LM_AI_HANDOVER.md` - دليل التسليم الأصلي
3. `TASK_COMPLETION_SUMMARY.md` - ملخص الإنجازات (إنجليزي)
4. `TASK_COMPLETION_SUMMARY_AR.md` - ملخص الإنجازات (عربي)
5. `docs/NEXT_AI_MODEL_INSTRUCTIONS.md` - **هذا الملف**

---

## 🧪 كيف تختبر عملك

### 1. اختبار Conceptual LM (كلها تعمل ✅):
```bash
cd /home/al-mubtakir/Documents/bayan_python_ide10
python bayan/main.py examples/conceptual_detail_focus_demo.bayan
python bayan/main.py examples/conceptual_comparison_circuit_demo.bayan
python bayan/main.py examples/conceptual_orchestrator_intelligent_selection_demo.bayan
python bayan/main.py examples/conceptual_lm_training_demo.bayan
```

### 2. اختبار الاختبارات (144 فاشل ❌):
```bash
# شغّل كل الاختبارات
python -m pytest tests/ -v

# شغّل ملف واحد
python -m pytest tests/test_nlp_bayan_generation.py -v

# شغّل اختبار واحد
python -m pytest tests/test_nlp_bayan_generation.py::test_morpho_inserts_min_for_ghadara -v
```

### 3. اختبار تفاعلي:
```bash
python bayan/main.py examples/conceptual_interactive_orchestrator_repl.bayan
```

---

## 📊 معلومات إحصائية

### حجم المشروع
```
- 14,484 سطر في ai/*.bayan و nlp_bayan/*.bayan
- 11,664 سطر في ai/ فقط
- 6 دوائر مفاهيمية
- 5 برامج معنوية (+ 3 متغيرات)
- 14 نمط مفاهيمي (blueprints)
- 461 اختبار ناجح
- 144 اختبار فاشل
```

### الملفات الجديدة التي أنشأها النموذج الحالي
```
1. ai/conceptual_surface_realizer.bayan (330 سطر)
2. examples/conceptual_detail_focus_demo.bayan
3. examples/conceptual_comparison_circuit_demo.bayan
4. examples/conceptual_orchestrator_intelligent_selection_demo.bayan
5. examples/conceptual_lm_training_demo.bayan
6. TASK_COMPLETION_SUMMARY.md
7. TASK_COMPLETION_SUMMARY_AR.md
```

### الملفات المعدلة
```
1. ai/conceptual_programs.bayan - دعم detail_level و focus
2. ai/conceptual_orchestrator.bayan - اختيار ذكي
3. ai/conceptual_circuits.bayan - دائرة مقارنة محسنة
4. ai/nlp.bayan - إصلاح خطأ + 5 دوال جديدة
```

---

## ⚠️ ملاحظات مهمة جداً

### 1. الأولوية القصوى: إصلاح الاختبارات ❗❗❗
- **لا تبدأ بميزات جديدة قبل إصلاح الاختبارات**
- الهدف: 95%+ نجاح (أقل من 30 اختبار فاشل)
- ابدأ بـ `test_nlp_bayan_generation.py` (8 اختبارات)

### 2. لا تعدّل ملفات الحزم يدوياً
- استخدم `pip install` أو `npm install`
- لا تعدل `package.json` أو `requirements.txt` يدوياً

### 3. اختبر بعد كل تعديل
- لا تجمع تعديلات كثيرة قبل الاختبار
- شغّل الاختبارات بعد كل إصلاح
- تأكد أنك لم تكسر اختبارات أخرى

### 4. وثّق عملك
- أنشئ `TEST_FIXES_REPORT.md` لتوثيق الإصلاحات
- اكتب ملاحظة عن كل مشكلة وحلها
- حدّث `CHANGELOG.md` إذا لزم

### 5. استخدم نفس الأسلوب
- حافظ على نمط الكود الموجود
- استخدم نفس التسميات
- اتبع نفس البنية

### 6. الأمثلة ضرورية
- لكل ميزة جديدة، أنشئ مثال توضيحي
- تأكد أن المثال يعمل
- أضف تعليقات توضيحية

### 7. مشاكل معروفة يجب تجنبها

#### أ) كلمات محجوزة عربية
```python
# ❌ خطأ - استعلام كلمة محجوزة
def دالة(استعلام):
    pass

# ✅ صحيح - استخدم اسم مختلف
def دالة(نص_استعلام):
    pass
```

الكلمات المحجوزة العربية:
- `استعلام` (query)
- `حقيقة` (fact)
- `قاعدة` (rule)
- وغيرها... (راجع `bayan/lexer.py`)

#### ب) Default parameters
```python
# ✅ البيان تدعم default parameters
def دالة(أ, ب=5, ج="نص"):
    pass
```

#### ج) Import statements
```python
# ✅ صحيح
import ai.nlp
import ai.ml

# ❌ خطأ - تأكد أن الملف موجود
import ai.nonexistent
```

---

## 🎯 الأولويات (محدّثة)

### أولوية قصوى (ابدأ فوراً):
1. ❗❗❗ **إصلاح الاختبارات الفاشلة** (144 اختبار)
   - الهدف: أسبوع واحد
   - النتيجة المطلوبة: 95%+ نجاح

### أولوية عالية (بعد الاختبارات):
2. **تحسين توليد النص الطبيعي**
   - من رمزي إلى طبيعي
   - قوالب لغوية
   - استخدام ai/nlp

### أولوية متوسطة (بعد النص الطبيعي):
3. **توسيع المجالات** (10+ مجالات جديدة)
4. **إضافة دوائر جديدة** (10+ دوائر)

### أولوية منخفضة (إذا كان لديك وقت):
5. **تدريب نماذج لغوية حقيقية**
6. **Integration مع PyTorch/TensorFlow**
7. **Multi-modal support**

---

## 📞 إذا واجهت مشاكل

### 1. مشاكل الاختبارات
- اقرأ رسالة الخطأ بعناية
- استخدم `pytest -v` للتفاصيل
- شغّل اختبار واحد في كل مرة
- استخدم `print()` للتتبع

### 2. مشاكل Syntax
- افحص `bayan/lexer.py` للكلمات المحجوزة
- افحص `bayan/parser.py` للقواعد النحوية
- استخدم `view` لقراءة الملفات

### 3. مشاكل Import
- تأكد أن الملف موجود
- تأكد من المسار صحيح
- تأكد من عدم وجود أخطاء syntax في الملف المستورد

### 4. مشاكل Logic
- استخدم `print()` لطباعة القيم
- افحص الأمثلة الموجودة
- راجع التوثيق

---

## 📚 موارد مفيدة

### وثائق Conceptual LM
1. `docs/CONCEPTUAL_CIRCUITS_AND_PROGRAMS.md` - **الدليل الرئيسي**
2. `docs/CONCEPTUAL_LM_AI_HANDOVER.md` - دليل التسليم
3. `docs/CONCEPTUAL_LM_BLUEPRINT.md` - مخطط النظام
4. `docs/CONCEPTUAL_PATTERNS_LIBRARY.md` - مكتبة الأنماط

### وثائق لغة البيان
1. `README.md` - نظرة عامة
2. `QUICKSTART.md` - دليل البدء السريع
3. `docs/LANGUAGE_GUIDE.md` - دليل اللغة
4. `docs/DEVELOPER_GUIDE.md` - دليل المطور

### أمثلة توضيحية
1. `examples/` - جميع الأمثلة
2. `examples/conceptual_*.bayan` - أمثلة Conceptual LM
3. `examples/family.bayan` - مثال بسيط للبيان

---

## 🎓 ما تعلمه النموذج الحالي

### 1. مشاكل تم حلها
- ✅ كلمة `استعلام` محجوزة → استخدم `نص_استعلام`
- ✅ دوال مفقودة في ai/nlp → أضفناها
- ✅ ai/conceptual_surface_realizer مفقود → أنشأناه
- ✅ detail_level و focus لا يعملان → أصلحناهما
- ✅ Orchestrator بسيط → حسّناه

### 2. أفضل الممارسات
- استخدم `codebase-retrieval` قبل التعديل
- استخدم `view` لقراءة الملفات
- استخدم `str-replace-editor` للتعديل (ليس save-file)
- اختبر بعد كل تعديل
- وثّق عملك

### 3. نصائح مهمة
- الاختبارات أولاً، الميزات ثانياً
- لا تكسر ما يعمل
- ابدأ بسيط ثم حسّن
- الأمثلة أفضل من الشرح

---

## 🚀 خطة العمل المقترحة

### الأسبوع 1: إصلاح الاختبارات
```
اليوم 1-2: test_nlp_bayan_generation.py (8 اختبارات)
اليوم 3: test_operators.py (1 اختبار)
اليوم 4: test_prob_thresholds_topk.py (1 اختبار)
اليوم 5: test_similarity_core.py (4 اختبارات)
اليوم 6: test_template_match.py (3 اختبارات)
اليوم 7: test_temporal_constructs.py (2 اختبار)

الهدف: 95%+ نجاح
```

### الأسبوع 2: تحسين النص الطبيعي
```
اليوم 1-2: قوالب لغوية عربية
اليوم 3-4: قوالب لغوية إنجليزية
اليوم 5-6: تحسين trace_to_natural_text()
اليوم 7: اختبار وتوثيق

الهدف: نص طبيعي حقيقي
```

### الأسبوع 3-4: توسيع النظام
```
الأسبوع 3: إضافة 5 مجالات جديدة
الأسبوع 4: إضافة 5 دوائر جديدة

الهدف: 10 مجالات، 11 دائرة
```

### الأسبوع 5-6: نماذج لغوية
```
الأسبوع 5: توليد corpus كبير
الأسبوع 6: تدريب وتقييم

الهدف: نموذج لغوي مدرب
```

---

**بالتوفيق! 🚀**

**ملخص:**
- ✅ الأساسيات مكتملة 100%
- ❗ 144 اختبار فاشل - **أولوية قصوى**
- 🎯 الهدف: نظام مستقر وموثوق
- 📈 ثم التوسع والتحسين

**النموذج الحالي أنجز جميع المهام الأساسية. دورك الآن: إصلاح الاختبارات ثم التوسع.**

