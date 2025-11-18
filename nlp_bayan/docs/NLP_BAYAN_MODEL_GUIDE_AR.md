## دليل بناء نموذج التوليد اللغوي في nlp_bayan

هذا الدليل يشرح، خطوة بخطوة، كيف بنينا نموذج توليدي مبسّط باللغة العربية فوق محرك بايان (Bayan) بالاعتماد على مكتبة الذكاء الاصطناعي المدمجة ai/nlp.

هدفنا هنا بناء "نواة" توليد من نوع نموذج لغة إحصائي (ثنائي/ثلاثي الكلمات) مع مسار تطوير واضح نحو تكامل المنطق والمعرفة لاحقًا.

---

### المتطلبات والهيكلة
- المستودع يحوي:
  - nlp_bayan/core/generator_pipeline.bayan: منطق التوليد
  - ai/nlp.bayan: مكتبة NLP المدمجة (ثنائي/ثلاثي الكلمات، تشابهات، TF‑IDF، ...)
  - nlp_bayan/examples/demo_generation.bayan: مثال تشغيل سريع
  - tests/test_nlp_bayan_generation.py: اختبارات الوحدة الخاصة بالتوليد

شغّل الأمثلة:
```
python -m bayan nlp_bayan/examples/demo_generation.bayan
```

شغّل اختبارات الملف الحالي فقط:
```
pytest -q tests/test_nlp_bayan_generation.py
```

---

## الخطوة 1: مولّد ثلاثي الكلمات (Trigram LM) بسيط

أضفنا دالتين أوليتين:
1) generate_trigram_ar(seed1, seed2, steps=8)
   - تدريب مصغّر داخلي على مجموعة جُمل عربية بسيطة.
   - يبدأ بكلمتين seed1, seed2 ثم يولّد أفضل كلمة تالية (Top‑1) في كل خطوة.

2) generate_trigram_from_docs(seed1, seed2, docs, steps=8, top_k=1)
   - مثل السابقة لكن تقبل مصفوفة مستندات للتدريب (docs) لمرونة أكبر.

مقتطف مبسّط:
```bayan
def generate_trigram_from_docs(seed1, seed2, docs, steps=8, top_k=1): {
    model3 = nlp.trigram_lm_train(docs, 1.0)
    w1 = seed1; w2 = seed2; out = w1 + " " + w2; i = 0
    while i < steps: {
        top = nlp.trigram_lm_predict_next(model3, w1, w2, top_k)
        if len(top) == 0: { break }
        w3 = top[0]; out = out + " " + w3; w1 = w2; w2 = w3; i = i + 1
    }
    return out
}
```

اختبار بسيط (ملف tests/test_nlp_bayan_generation.py):
```python
def test_generate_trigram_ar_basic():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid { s = gen.generate_trigram_ar("محمد", "ذهب", 4) }
    """
    ...
    assert s.startswith("محمد ذهب")
```

---

## الخطوة 2: دعم السقوط إلى Bigram عند غياب سياق Trigram

لمعالجة الحالات التي لا يملك فيها النموذج الثلاثي سياقًا كافيًا (pair غير موجود)، أو يكون التقدير الثلاثي غير معلوماتي (بسبب التسوية Laplace)، أضفنا مسار سقوط تلقائي إلى نموذج ثنائي الكلمات.

الفكرة:
- ندرب نموذجين معًا على نفس النصوص: trigram وbigram.
- في كل خطوة توليد:
  - إن كان السياق (w1, w2) موجودًا في ثلاثي الكلمات، نستخدمه.
  - وإلا نجرّب bigram باستخدام w2 كسياق.
  - إن لم يتوفر أيضًا سياق ثنائي مناسب، نتوقف بأمان.

مقتطف أساسي من الدالة بعد التحديث:
```bayan
model3 = nlp.trigram_lm_train(docs, 1.0)
model2 = nlp.bigram_lm_train(docs, 1.0)
...
use_tri = False
tri_map = model3["tri"]
if w1 in tri_map: { if w2 in tri_map[w1]: { use_tri = True } }
if use_tri: { top = nlp.trigram_lm_predict_next(model3, w1, w2, top_k) } else { top = [] }
if len(top) == 0: {
    bi_map = model2["bi"]
    if w2 in bi_map: { top = nlp.bigram_lm_predict_next(model2, w2, top_k) } else { top = [] }
}
```

اختبارات مضافة لتغطية السقوط:
```python
def test_generate_trigram_from_docs_fallback_to_bigram():
    docs = ["سعد زار المدرسة", "الطالب زار المتحف"]
    s = gen.generate_trigram_from_docs("أحمد", "زار", docs, 2, 1)
    # لا يوجد سياق ثلاثي (أحمد، زار) → السقوط إلى bigram على "زار"
    assert s.split()[2] in {"المدرسة", "المتحف"}

def test_generate_trigram_from_docs_fallback_break_when_bigram_empty():
    docs = ["سعد ذهب المدرسة"]
    s = gen.generate_trigram_from_docs("أحمد", "زار", docs, 3, 1)
    # لا سياق ثلاثي ولا ثنائي → توقف دون أخطاء
    assert s.split() == ["أحمد", "زار"]
```

### تفضيل معرفي ذكي عبر كيانات KB (قبل Bigram وأيضًا قبل Trigram في الخطوة الأولى)

بدل تفعيل المعرفة فقط عندما يعجز Trigram، أصبحنا نُطبّق تفضيلًا معرفيًا مبكرًا عند الخطوة الأولى (i==0) متى توفّر تعيين token→entity للفاعل:
- كيانات مبسطة: isa(student, person). has(person, house) … إلخ.
- قواعد أهداف افتراضية عامة ومخصوصة بحسب الفعل:
  - عام: default_go_target (مباشر ثم موروث)
  - نوعية: enter/exit/return/sit/travel/visit/pass مع تفضيل المباشر ثم الموروث
- إن وُجد مرشح KB مباشر/موروث نعيد ترتيب/استبدال قائمة المرشحين بحيث تتقدّم مرشّحات KB على الإحصائي (trigram/bigram).

مقتطف موجز:
```bayan
kb.load_selective(logical, ["prob", "entities"])
...
if (len(token_entity_map) > 0) and (w1 in token_entity_map):
{   subj_ent = token_entity_map[w1]
    kb_dir = []; kb_any = []
    # نملأ kb_dir/kb_any عبر holds_default_* بحسب الفعل
    ...
    if len(kb_dir) > 0: { top = kb_dir; src_type = "kb" }
    elif len(kb_any) > 0: { top = kb_any; src_type = "kb" }
}
```
مثال: “الطالب ذهب …” → نُفضّل “البيت/المدرسة” إن دلّت قواعد KB على ذلك حتى لو كان لدى Trigram اقتراح آخر من التدريب.


### توسعة الكيانات والأفعال (مضافة حديثًا)
- أماكن جديدة: الجامعة، الفندق، الملعب، الشاطئ، المتجر، المقهى، المحطة، الميناء، المول
- تصنيفات: indoor/outdoor/seating_place + travel_place + visitable
  - indoor: university, hotel, store, cafe, station, mall
  - outdoor: beach, stadium, port
  - travel_place: airport, station, port
  - visitable: museum, library, mosque, garden, square, mall
- أفعال جديدة مرتبطة نوعيًا:
  - سافر → travel_place
  - زار → visitable
  - مرّ → outdoor
  - غادر → outdoor (depart)
  - استقر → indoor (settle)
- تُطبّق تفضيلات KB مباشرة في الخطوة الأولى مع تفضيل القواعد المباشرة ثم الموروثة.
- صرف + KB: "رجع" صار مرادفًا تامًا لـ"عاد" صرفيًا (إدراج "الى") ودلاليًا (قواعد return تفضّل "البيت").



---

## الخطوة 3: قيود معرفية من KB أثناء اختيار الكلمة التالية

نربط التوليد بالمعرفة الاحتمالية عبر قاعدة المعرفة الموحّدة integrated_kb:
- نحمّل نطاق الاحتمالات فقط: prob/threshold/maybe/likely باستخدام: `kb.load_selective(logical, ["prob"])`
- نزود خريطة token → entity مثل: `{"الحديقة": "garden", "الساحة": "square"}`
- بعد الحصول على مرشحي top‑k من trigram/bigram، نرشّحهم حسب KB.

مقتطف أساسي من الدالة الجديدة generate_trigram_kb_from_docs:
```bayan
# داخل الحلقة لكل مرشح cand
ent = token_entity_map[cand]
if kb_pred == "maybe":
{   if maybe(?F, ent): { allow = True } }   # نستخدم متغيّرًا منطقيًا ?F لتفعيل الاستعلام
elif kb_pred == "likely":
{   if likely(?F, ent): { allow = True } }
```
لماذا ?F؟ لأن استدعاء maybe/likely من داخل الدوال الإمبراطية لا يعمل كـ"دوال" عادية؛ لكن وجود متغير منطقي (يبدأ بـ ?) يجعل الاستدعاء يُنفَّذ كاستعلام منطقي ويعيد True/False حسب وجود حلول.

اختبار توضيحي (مبسط من tests/test_nlp_bayan_generation.py):
```python
code = """
import nlp_bayan.core.generator_pipeline as gen
hybrid {
  docs = ["سعد زار الحديقة", "سعد زار الساحة"]
  tok_map = {"الحديقة": "garden", "الساحة": "square"}
  s = gen.generate_trigram_kb_from_docs("سعد", "زار", docs, 1, 5, "maybe", "is_green", tok_map)
}
"""
```
النتيجة المتوقعة: تفضيل "الحديقة" لأن KB تحتوي prob("is_green","garden",0.7) وthreshold("maybe",0.5) ⇒ maybe تنطبق على garden ولا تنطبق على square.

---

---

## الخطوة 4: أخذ عينات احتمالية مضبوطة (Top‑k / Temperature)

بعد دمج قيود الـKB والسقوط الدلالي، أضفنا أخذ عينات احتمالية للتحكم بالتنوّع:
- المعامل temperature:
  - 0.0 ⇒ اختيار حتمي لأعلى مرشح (Top‑1).
  - >0 ⇒ نطبّق توزيعًا مُعاد ضبطه بالحرارة على مرشحي top‑k ثم نختار عشوائيًا وفق الأوزان.
- rng_seed: بذرة اختيارية لضمان قابلية إعادة الإنتاج عند استخدام عشوائية.

مقتطف موجز من الاستدعاء:
```bayan
s = gen.generate_trigram_kb_from_docs("سعد", "زار", docs, 1, 2, "any", "x", tok_map, 1.0, 123)
```
- temperature=1.0 يفعّل العيّنة الاحتمالية؛ تمرير rng_seed=123 يجعل النتيجة قابلة للتكرار.

وسلوك حتمي عندما تكون الحرارة صفرًا:
```bayan
s = gen.generate_trigram_kb_from_docs("سعد", "زار", docs, 1, 2, "any", "x", tok_map, 0.0, 77)
```
- يختار أعلى مرشح بعد الترشيح بالـKB.

### Top‑p (nucleus) sampling — مضاف حديثًا
- المعامل الاختياري top_p∈(0,1): نأخذ المرشحين من أصغر غلاف تراكمي تتجاوز احتمالاته top_p ثم نطبّق العيّنة الحرارية عليهم.
- يعمل قبل temperature، ولا يغيّر السلوك عندما temperature=0 (يبقى الاختيار Top‑1 من الغلاف).

مثال سريع:
```bayan
s = gen.generate_trigram_kb_from_docs("سعد", "زار", docs, 1, 5, "any", "x", tok_map, 1.0, 123, 0.5)
```
- هنا نستعمل top_p=0.5 مع temperature=1.0، ما يقيّد المرشحين إلى الغلاف النواتي قبل أخذ العيّنة.


> ملاحظة لغوية: ابتداءً من إصدار بيان الحالي، يمكنك أيضًا استعمال تعابير التوليد مباشرة في اللغة:
> - الاختيار الموزون: `choose {"خيار":0.7, "بديل":0.3}`
> - أخذ عينة من توزيع: `x ~ uniform(0,1)`، `n ~ normal(0,1)`، والتحكم بالإعادة عبر `seed(N)`
> هذا يفيد عند كتابة أمثلة/تجارب توليد سريعة داخل كتل hybrid دون المرور عبر طبقات بايثون.


> مستجدات في لغة بيان تفيد التوليد:
> - عامل التقارب `≈` و`~=`: يقارن عدديا بهامش `approx_eps` (افتراضيا 1e-2) ويستعلم دلاليا عبر `close/3` للنصوص عند تحميل وحدة التشابه
> - المفاهيم `concept/مفهوم`: تعريف مجموعات سريعة للاختبار (`in`/`∈`) وحقائق `in_concept/2`
> - الحقائق الاحتمالية: `fact[0.8] p(args).` لتخزين ثقة مرتبطة بالحقائق داخل المحرك المنطقي

> - جمع/ترتيب الحلول المنطقية: `collect/topk/argmax` مع سقوط تلقائي إلى استعمال «احتمال الحل» عند غياب درجة `?S` أو كانت غير رقمية.




### تحسينات سياسة الاختيار (مضاف حديثًا)
- top_k ديناميكي عند المصدر الإحصائي (tri/bi): إذا كانت ثقة أعلى مرشحين عالية (conf ≥ 0.7) نقتطع القائمة إلى Top‑1 فقط.
- تعزيز احتمالات المرشحين المتوافقين مع الKB (KB weight boosting):
  - داخل كل من nucleus وtemperature sampling نضاعف وزن المرشح المتوافق مع قواعد KB (1.6 للمباشر، 1.2 للموروث) في الخطوة الأولى.
- مثال اختبار: test_kb_weighting_prefers_visitable_in_top_p يثبت تفضيل "المتحف" (visitable) على "الفندق" مع top_p≈0.9 حتى لو كانت الاحتمالات متقاربة إحصائيًا.



### الاستدلال الاحتمالي (جديد)
- المحرك المنطقي يراكم احتمال الحل كمحصلة لضرب احتمالات الحقائق.
- عتبات جاهزة: `maybe()` و`likely()` (0/1 وسيط) و`prob_ge(thr)`، مع `probability(?P)` لقراءة قيمة الاحتمال.
- عند استعمال `argmax/topk` على حلول منطقية بدون درجة صريحة، يتم اعتماد احتمال الحل تلقائيًا للترتيب.
- تمييز مهم: علاقات KB المسماة `maybe/2` و`likely/2` (وسيطان) تبقى علاقات عادية ولا تتقاطع مع البنى المدمجة أعلاه.
- راجع أيضًا: docs/LANGUAGE_GUIDE.md قسم "الاستدلال الاحتمالي"، واختبارات: tests/test_probabilistic_inference.py، tests/test_prob_thresholds_topk.py.



---

## الخطوة 5: قوالب صرف/اتفاق مبسّطة بعد التوليد

أضفنا طبقة صرفية خفيفة تعمل بعد اختيار الكلمات لتحسين سلامة العربية:
- إدراج حرف جر مناسب بعد بعض الأفعال عند مجيء مكان بعده مباشرةً:
  - ذهب/دخل/عاد → الى
  - وصل/توجه/سافر → الى
  - خرج → من
  - غادر → من
  - اقترب → من
  - ابتعد → عن
  - مر → ب
  - جلس → في
  - استقر → في
- لا يتم التكرار إذا كان حرف الجر موجودًا أصلاً.
- التعرف على “المكان” يتم إمّا بالقائمة المضمّنة (مثل: البيت/المدرسة/المكتبة/المسجد/السوق/المتحف/الحديقة/الساحة/المكتب) أو عبر token_entity_map إن كانت الكلمة تعيَّن إلى كيانات مكانية مثل: house/school/library/mosque/market/workplace/...

مقتطف مبسّط من الدالة:

### دمج إملائي اختياري: "ب + ال" → "بالـ"
- أضفنا معاملاً اختياريًا merge_bi_al=True لدمج حرف الجر "ب" مع "ال" التالية (على مستوى الإملاء فقط) بعد التوليد.
- مثال:
```bayan
s = gen.generate_trigram_kb_from_docs("سعد", "مر", ["سعد مر السوق"], 1, 5, "any", "x", {"سعد":"person","السوق":"market"}, 0.0, 7, 0.0, True)
# الناتج يتضمّن "بالسوق" بدل "ب السوق"
```
- لا يغيّر هذا الدمج المنطق الدلالي ولا قواعد KB؛ هو تلميع شكلي للناتج فقط.


### ضوابط جودة التوليد (مضافة حديثًا)
- no_repeat_ngram_size: يمنع تكرار n-gram داخل الجملة. مثال: 2 يمنع تكرار ثنائيات الكلمات.
- stop_tokens: قائمة رموز/كلمات يوقف التوليد عند ظهور أحدها بعد بلوغ الحد الأدنى للطول.
- min_length / max_length: التحكم بطول الجملة الأدنى/الأقصى.

مثال استخدام سريع:
<augment_code_snippet path="nlp_bayan/core/generator_pipeline.bayan" mode="EXCERPT">
````bayan
s = gen.generate_trigram_kb_from_docs(
  "سعد", "جلس", ["سعد جلس المقهى", "المقهى جميل"],
  10, 3, "any", "x", {"سعد":"person","المقهى":"cafe"}, 0.0, 7, 0.0,
  True, ["المقهى"], 2, 2, 5)
````
</augment_code_snippet>
- يوقف التوليد عند "المقهى" بعد توليد كلمتين على الأقل، ويمنع تكرار ثنائيات الكلمات، وبحد أقصى خمس كلمات.

```bayan
# داخل _apply_basic_morpho_words
if (w=="ذهب") or (w=="دخل") or (w=="عاد"): prep="الى"
elif w=="خرج": prep="من"
elif w=="جلس": prep="في"


if prep!="" and _is_place_token(nxt, token_entity_map): new_words.append(prep)
```

مثال قبل/بعد:
- قبل: "الطالب ذهب البيت" → بعد: "الطالب ذهب الى البيت"
- قبل: "سعد جلس المسجد" → بعد: "سعد جلس في المسجد"

وتتعاون هذه الطبقة مع السقوط الدلالي الذكي من الـKB:
- إن لم يجد Trigram مرشحًا، يُستدلُّ على وجهة من كيانات مثل: has(student, school)، has(person, house/market/mosque/workplace/library) ثم تُطبّق القاعدة الصرفية المناسبة على الناتج.



## واجهة API ومثال CLI (مضافة حديثًا)
- لاستهلاك النموذج برمجيًا عبر Python/Bayan، استخدم الدالة المبسطة:
<augment_code_snippet path="nlp_bayan/api/simple_api.bayan" mode="EXCERPT">
````bayan
i = api.gen_sentence("سعد","مر", ["سعد مر السوق"], {"سعد":"person","السوق":"market"}, 5, 3, 0.0, 7)
````
</augment_code_snippet>
- ولمثال جاهز للاستدعاء:
<augment_code_snippet path="nlp_bayan/examples/cli_generator.bayan" mode="EXCERPT">
````bayan
s = cli.demo()  # يعيد الجملة المتولدة لاختبار سريع
````
</augment_code_snippet>

## كيف أشغّل الأمثلة وأتأكد؟
- مثال سريع:
```
python -m bayan nlp_bayan/examples/demo_generation.bayan
```
- اختبارات الوحدة (هذا الملف فقط):
```
pytest -q tests/test_nlp_bayan_generation.py
```

---

## ما القادم؟ (خارطة طريق مختصرة)
1) تغطية لغوية أوسع: كيانات وأفعال وحالات إضافية (المتحف الوطني/الحديقة العامة/وصل/غادر/استقر...) حسب الحاجة.
2) تحسينات جودة التوليد: تقليل التكرار، التحكم بطول الجملة، إنهاء طبيعي (stop tokens) عند استنفاد السياق.
3) واجهة استخدام: مثال CLI وواجهة برمجية مبسطة (API) لاستهلاك الدالة من أدوات خارجية.
4) توسيع الاختبارات: حالات حدودية وتغطية أوسع للـ KB وسياسات الاختيار.

إن رغبت بنقل هذه الخطوات إلى مثال واحد متكامل، سنضيف مثالًا جديدًا تحت nlp_bayan/examples يبيّن كامل المسار (docs المخصّصة + قيود KB + التوليد).



---

## ملخص الحالة الحالية (Quick status)
- تكامل KB في الخطوة الأولى (i==0) + تعزيز أوزان داخل top_p/temperature (1.6 مباشر، 1.2 موروث).
- دعم top_k / top_p / temperature + rng_seed.
- صرف حروف الجر للحركة (الى/من/في/ب) + دمج اختياري "ب+ال" → "بال".
- ضوابط جودة: no_repeat_ngram_size، stop_tokens، min/max_length.
- "رجع" مرادف تام لـ"عاد" (صرفيًا ودلاليًا).
- تنظيف كامل للكتل/الأحرف التالفة في generator_pipeline.bayan؛ الملف الآن نظيف.
- الاختبارات: 437 passed (pytest -q).

أوامر تحقق سريعة:
- python -m bayan nlp_bayan/examples/demo_generation.bayan
- pytest -q tests/test_nlp_bayan_generation.py

## فهرس ملفات النمذجة داخل nlp_bayan
- core/generator_pipeline.bayan — أنبوب التوليد (tri/bi + KB + sampling + صرف + ضوابط).
- core/integrated_kb.bayan — القواعد الدلالية والاحتمالات.
- core/entities.bayan — الكيانات/التصنيفات الأساسية.
- api/simple_api.bayan — واجهة مبسطة للاستدعاء.
- examples/*.bayan — أمثلة تشغيل.
- docs/DESIGN_OVERVIEW_AR.md — نظرة تصميمية.

## خطوات مقترحة للمكمّل الذكي (Next steps)
- توسيع الأفعال والكيانات وربطها بتصنيفات KB (visitable/travel_place/...)
- معايرة top_p/temperature/boost للأفعال المختلفة مع اختبارات إعادة إنتاج (rng_seed ثابت).
- استخراج جدول الصرف إلى خريطة واحدة مركزية لتقليل تكرار المنطق.
- إضافة محمّل نصوص datasets/ لتغذية tri/bi بسهولة.
- CI: فحص الأحرف غير المطبوعة + تشغيل pytest.
- تحديث الوثائق كلما توسّعت الأفعال/الكيانات.


---

## حالة الحوار والمرجعية (مضاف حديثًا)
- نتابع آخر كيان/مكان/متحدّث عبر الوحدة: nlp_bayan/core/dialogue_state.bayan
- عند أفعال "عاد/رجع" نُفضّل المكان الأخير من الحالة في أول خطوة (i==0).
- الدوال ذات الصلة:
  - generate_trigram_with_dialogue(...)
  - generate_trigram_kb_from_docs(..., use_dialogue_state=True, prefer_place="")
- مثال جولتين صغير:
<augment_code_snippet mode="EXCERPT">
````bayan
import nlp_bayan.core.dialogue_state as ds
import nlp_bayan.core.generator_pipeline as gen
hybrid {
  ds.reset(); docs=["سعد ذهب المدرسة","سعد رجع المدرسة"]
  tok={"سعد":"person","المدرسة":"school"}
  s1 = gen.generate_trigram_kb_from_docs("سعد","ذهب", docs, 1, 1, "maybe","is_green", tok, 0.0, 11, 0.0, False, [], 0, 0, -1, True, "")
  s2 = gen.generate_trigram_kb_from_docs("سعد","رجع", docs, 1, 1, "maybe","is_green", tok, 0.0, 22, 0.0, False, [], 0, 0, -1, True, "")
}
````
</augment_code_snippet>
- ملاحظة: تُدرَج "الى" تلقائيًا قبل المكان مع "عاد/رجع"، ويمكن دمج "ب+ال" اختياريًا.
