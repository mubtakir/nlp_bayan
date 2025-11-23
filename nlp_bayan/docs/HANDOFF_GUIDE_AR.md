## دليل الاستلام لنموذج nlp_bayan (مختصر وعملي)

هذا المستند يجمع كل ما يخص نموذج اللغة داخل nlp_bayan ويعطي خطوات عملية لما يجب على النموذج الذكي القادم تنفيذه لإكمال العمل.

---

### أين يوجد كل شيء؟
- النواة (التوليد): nlp_bayan/core/generator_pipeline.bayan
- قاعدة المعرفة المتكاملة: nlp_bayan/core/integrated_kb.bayan
- الكيانات والتصنيفات: nlp_bayan/core/entities.bayan
- القواعد الصرفية: nlp_bayan/core/morphosyntactic_rules.bayan
- أمثلة التشغيل: nlp_bayan/examples/*.bayan
- واجهة API مبسطة: nlp_bayan/api/simple_api.bayan
- نظرة تصميمية: nlp_bayan/docs/DESIGN_OVERVIEW_AR.md
- الدليل التفصيلي: nlp_bayan/docs/NLP_BAYAN_MODEL_GUIDE_AR.md
- اختبارات الوحدة: tests/test_nlp_bayan_generation.py

---

### ما الذي يعمل الآن؟ (ملخّص الميزات)
- نموذج ثلاثي الكلمات مع سقوط إلى ثنائي الكلمات عند الحاجة.
- دمج ذكي لقيود قاعدة المعرفة في أول خطوة توليد (i==0) لفرض تفضيلات دلالية.
- أخذ عينات احتمالية:
  - top_k ديناميكي
  - temperature (0.0 حتمي، >0.0 احتمالي)
  - top_p (nucleus)
  - تعزيز أوزان المرشحين المتوافقين مع KB داخل top_p/temperature (1.6 للمباشر، 1.2 للموروث)
- طبقة صرفية بعد التوليد لإدراج حروف الجر المناسبة تلقائيًا (الى/من/في/ب) للأفعال الحركية.
- ضبط الجودة: no_repeat_ngram_size، stop_tokens، min/max_length، دمج "ب+ال" → "بال".
- دعم الأفعال الدلالية الأساسية: ذهب، دخل، خرج، عاد، رجع، جلس، سافر، زار، مرّ، غادر، استقر، توجه، انتقل، اتجه، قصد، هرب، وصل.
- "رجع" صار مرادفًا تامًا لـ"عاد" صرفيًا ودلاليًا (return).
- نظافة الملف الأساسية: generator_pipeline.bayan خالٍ من أحرف التحكم؛ اختباراتنا تمر جميعًا.

أوامر تحقق سريعة:
- تشغيل مثال: python -m bayan nlp_bayan/examples/demo_generation.bayan
- تشغيل الاختبارات: pytest -q tests/test_nlp_bayan_generation.py (أو pytest -q)


### حوار/استدلال (بسيط وجاهز)
- تشغيل العرض: `python3 bayan/main.py nlp_bayan/final_real_dialogue.bayan`
- يدعم: المرادفات (ثنائي الاتجاه)، تعدّي "هو"، وراثة `نوع من`→`له`، أسئلة متعددة الصيغ، أفضل N بالنِسَب، سياق/زمن، سياسات ترجيح (most_frequent/most_recent/highest_confidence) وتفسير سلسلة الاستدلال.
- الملفات: `nlp_bayan/simple_kb.bayan`, `nlp_bayan/simple_inference.bayan`, `nlp_bayan/simple_parser.bayan`.


### ما يجب عليك فعله عند الاستلام
1) اقرأ الأدلة المحدثة بسرعة: docs/LANGUAGE_GUIDE.md، docs/GENERATION_GUIDE_AR.md، nlp_bayan/docs/NLP_BAYAN_MODEL_GUIDE_AR.md، وهذا المستند.
2) شغّل الاختبارات محليًا: `pytest -q` (يُفترض أن تمر جميعها). جرّب أيضًا المثال: `python -m bayan nlp_bayan/examples/demo_generation.bayan`.
3) افهم التمييز الحرج: البنى المدمجة `maybe()/likely()` تعمل فقط بصفر/وسيط واحد؛ علاقات KB المسماة `maybe/2` و`likely/2` (وسيطان) لا تتأثر وتبقى كما هي. راجع bayan/bayan/logical_engine.py.
4) اختبر الاستدلال الاحتمالي: راجع الاختبارات `tests/test_probabilistic_inference.py` و`tests/test_prob_thresholds_topk.py`.
5) اتبع إرشادات الأسلوب: حافظ على English-only identifiers في ملفات Python/CI فقط، ولا تفرض ذلك على ملفات Bayan العربية. أضف/حدث الاختبارات لكل تغيير وظيفي.
6) عند توسيع النموذج (أفعال/كيانات/سياسات اختيار): اتبع قسم "كيف توسّع النموذج؟" وأضف اختبارات تغطي الصرف، تفضيلات KB، وضبط sampling.
7) إعداد فحوص ما قبل الالتزام (pre-commit) محليًا:
   - اختياريًا ثبّت pre-commit وشغّله محليًا لالتقاط الأحرف غير المطبوعة ولمطابقة English-only داخل nlp_bayan/:
     - pip install pre-commit
     - pre-commit install
     - pre-commit run --all-files
   - المهوِّدات المضافة:
     - scripts/check_non_printable.py على جميع ملفات النص (يمنع الأحرف غير المطبوعة وBOM/Zero‑Width)
     - scripts/check_python_identifiers_english.py على nlp_bayan/**/*.py فقط


---

### كيف توسّع النموذج؟ (خطوات عملية)
1) إضافة فعل جديد مع قواعد KB:
- integrated_kb.bayan: أضف predicates من نمط default_<verb>_target و *_direct إن لزم (مع التصنيفات المناسبة: visitable/travel_place/...)
- generator_pipeline.bayan:
  - أدخل الفعل في مسارات: allow_direct (i==0)، allow_any (i==0)، تعزيز top_p، وتعزيز temperature بنفس منطق الأفعال المماثلة.
  - إن كان فعلاً حركيًا يتطلب حرف جر، أضفه إلى خريطة الحروف في طبقة الصرف.
- أضف اختبارات تغطي: صرف الحرف، تفضيل KB، واحترام الضوابط (stop_tokens/no_repeat).

2) إضافة كيان/تصنيف جديد:
- entities.bayan: أضف الكيان والتصنيفات (indoor/outdoor/visitable/travel_place/...)
- integrated_kb.bayan: اربطه بقواعد الأفعال ذات الصلة.
- أضف أمثلة في tests تظهر التفضيل الدلالي الصحيح.

3) ضبط سياسات الاختيار:
- غيّر أوزان التعزيز (KB_BOOST_DIRECT/ANY) بحذر، ثم ثبّت سلوك top_p/temperature باختبارات إعادة إنتاج (rng_seed ثابت).
- راقب جودة المخرجات مع no_repeat_ngram_size وstop_tokens.

4) الصرف والتحسين الشكلي:
- فعّل merge_bi_al=True حيث يلزم.
- عند إضافة أفعال حركية جديدة، حدّد حرف الجر المناسب في جدول واحد مركزي لتقليل التباين.

---

### إرشادات أسلوبية وتقنية
- حافظ على فصل المنطق (KB/predicates) عن سلاسل التوليد الإحصائي.
- اجعل كل إضافة مغطاة باختبار واحد على الأقل (صرف، KB، sampling).
- تجنّب إدخال أحرف تحكّم غير مطبوعة داخل الملفات. إن ظهرت، نظّفها مباشرة.
- لا تغيّر واجهات الدوال العامة دون تحديث الأمثلة والاختبارات.

ملاحظة: سياسة الهوية/الأسماء داخل nlp_bayan قد تحتاج مُلحق linter خاص باللغة؛ إن رغبت بفرض "English-only identifiers" على ملفات Python/أدوات CI فقط، افصل ذلك عن ملفات Bayan العربية حتى لا تتأثر.

---

### خارطة طريق مقترحة للمكمّل الذكي (Next steps)
- تغطية لغوية أوسع:
  - أفعال إضافية (اقترب/ابتعد/عاد بصيغ أخرى/أقام/بات...) وربطها بالتصنيفات المناسبة.
  - كيانات جديدة (حديقة عامة/متحف وطني/جامعة محددة) مع خصائص إضافية.
- جودة التوليد:
  - معايرة أفضل لـ top_p وtemperature حسب النوع (go/visit/return).
  - تحسين اختيار الكيانات عند تضارب KB والإحصائي مع سجلات تتبّع لسبب الاختيار.
- بيانات وتعلّم:
  - إضافة مُحمِّل نصوص بسيط (datasets/*.txt) لتغذية نموذج tri/bi بسهولة.
  - اختبار سلاسل أطول وتقييم التماسك.
- هندسة وتنظيم:
  - استخراج جداول الصرف إلى بنية قابلة للتوسعة (mapping واحدة).
  - تبسيط أقسام التعزيز المتكررة في generator_pipeline.bayan.

### الاستدلال الاحتمالي (جديد)
- كل حل منطقي يحمل احتمالًا مركّبًا يمر عبر سلسلة الإثبات.
- بُنى مدمجة:
  - `maybe()`/`likely()` (0 أو 1 وسيط) لتصفية الحلول حسب عتبات 0.5/0.8 (قابلة للتعديل).
  - `prob_ge(thr)` و`probability(?P)` للاستعلام عن احتمال الحل الحالي.
- `topk/argmax` تسقط تلقائيًا إلى استعمال احتمال الحل عند غياب درجة `?S` صريحة.
- تمييز مهم: علاقات KB `maybe/2` و`likely/2` (وسيطان) لا تتأثر بالبنى المدمجة أعلاه.
- اختبارات مرجعية: tests/test_probabilistic_inference.py، tests/test_prob_thresholds_topk.py.

- CI والضمان:
  - إضافة pre-commit لفحص الأحرف غير المطبوعة.
  - تشغيل pytest في CI مع ملخّص موجز.
  - مزامنة الشجرة الفرعية (إن وُجدت): إن كان تدفّق العمل يعتمد على nlp_bayan ← nlp_bayan، حافظ على مصدر المزج من nlp_bayan إلى mubtakir/nlp_bayan، وأضِف المتغيّر السري NLP_BAYAN_PUSH_TOKEN إلى أسرار مستودع nlp_bayan.
  - حافظ على نقاء مستودعات اللغة: لا تفرض فحوصات English-only على ملفات Bayan العربية؛ اجعلها محصورة بملفات Python/CI.


انتهى. أي مساهمة جديدة يُفضّل أن تأتي مع: (1) وصف موجز للتغيير، (2) مقتطف صغير قبل/بعد، (3) اختبار/اختباران يُظهران صحة السلوك.



---

### تكامل حالة الحوار (جديد)
- الوحدة: nlp_bayan/core/dialogue_state.bayan
  - reset(), set_last_entity()/get_last_entity(), set_last_place()/get_last_place(), set_last_speaker()/get_last_speaker()
- في أنبوب التوليد:
  - generate_trigram_with_dialogue(...) للتجارب السريعة
  - generate_trigram_kb_from_docs(...) يدعم use_dialogue_state=True و prefer_place=""
- مثال جولتين (تفضيل المكان الأخير + صرف "الى" مع رجع/عاد):
<augment_code_snippet mode="EXCERPT">
````bayan
import nlp_bayan.core.dialogue_state as ds
import nlp_bayan.core.generator_pipeline as gen
hybrid {
  ds.reset()
  docs = ["سعد ذهب المدرسة","سعد رجع المدرسة"]
  tok = {"سعد":"person","المدرسة":"school"}
  s1 = gen.generate_trigram_kb_from_docs("سعد","ذهب", docs, 1, 1, "maybe","is_green", tok, 0.0, 11, 0.0, False, [], 0, 0, -1, True, "")
  s2 = gen.generate_trigram_kb_from_docs("سعد","رجع", docs, 1, 1, "maybe","is_green", tok, 0.0, 22, 0.0, False, [], 0, 0, -1, True, "")
}
````
</augment_code_snippet>
- اختبارات: tests/test_dialogue_state.py, tests/test_dialogue_generation.py, tests/test_dialogue_two_turn_state.py
- مثال جاهز: nlp_bayan/examples/demo_dialogue_generation.bayan
