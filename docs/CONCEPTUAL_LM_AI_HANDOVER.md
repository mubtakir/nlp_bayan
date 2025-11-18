# دليل تسليم العمل لنموذج الذكاء التالي (Conceptual LM in Bayan)

> هذه الوثيقة موجّهة إلى **نموذج ذكاء جديد** سيُكمِل تطوير طبقات النموذج
> اللغوي التصوّري فوق بيان. الهدف أن تعرف "أين وصلنا؟" و"ماذا تبقّى؟" و"كيف
> تكمّل بنفس الروح".

---

## 1. أين وصل المشروع الآن؟ (ملخص تنفيذي)

تم تنفيذ سلسلة أساسية من الطبقات، بعضها **رمزي وقبل-لغوي** بالكامل
وبعضها يشكّل جسرًا نحو نموذج لغوي تصوّري أوسع:

1. **تنسيق أثر تصوّري موحّد** `conceptual_trace` (موثَّق في
   `CONCEPTUAL_TRACE_FORMAT.md`).
2. **مكتبة تصوّرات عامة** (14 نمطًا) في DSL خاص:
   - الملف: `ai/conceptual_blueprints.bayan`
   - التوثيق: `docs/CONCEPTUAL_PATTERNS_LIBRARY.md`.
   - تشمل الأنماط الأساسية (Cause/Effect، وصف، شدة، عدم يقين...) بالإضافة إلى
     ثلاثة أنماط مضافة حديثًا: `ComparativePattern`, `TemporalOrderPattern`,
     `ContextualizationPattern`.
3. **طبقة الجسر اللغوي التنفيذية** (قبل-لغوية):
   - الملف: `ai/conceptual_language_bridge.bayan`
   - تحوّل هياكل `*SentencePattern` إلى أدوار جملة عامة:
     - `ActionSentence`, `StateChangeSentence`, `UncertaintySentence`,
       `CausalSentence`, `DescriptionSentence`, `IntensitySentence`.
4. **طبقة التخطيط السطحي الرمزي**:
   - الملف: `ai/conceptual_surface_planner.bayan`
   - ترتّب الأدوار في تسلسل رمزي يعتمد على منظور لغوي بسيط
     (`lang = "english"` SVO، `lang = "arabic"` VSO/ترتيب سببي مختلف).
5. **طبقة شجرة الجملة الرمزية** (Sentence Tree Layer):
   - الملف: `ai/conceptual_sentence_tree.bayan`
   - ترفع الخطة السطحية إلى بنية شجرية رمزية `SentenceTree`.
6. **طبقة التوليد الرمزي فوق الشجرة + واجهة نموذج لغوي رمزي**:
   - الملفات:
     - `ai/conceptual_surface_realizer.bayan`
     - `ai/conceptual_lm_bridge.bayan`
   - دوال لتوليد أمثلة رمزية وتدريب نماذج n-gram بسيطة (bigram/trigram)
     فوق corpus رمزي مضبوط (موثَّق في
     `docs/CONCEPTUAL_LM_BLUEPRINT.md` و
     `docs/CONCEPTUAL_LM_INTEGRATION_GUIDE.md`، مع أمثلة في
     `examples/conceptual_lm_corpus_demo.bayan`,
     `examples/conceptual_lm_extended_patterns_demo.bayan`,
     `examples/conceptual_lm_full_pipeline_demo.bayan`).
7. **طبقة الدوائر التصوّرية (Conceptual Circuits) وبرامج المعاني**:
   - الملفات:
     - `ai/conceptual_circuits.bayan`
     - `ai/conceptual_programs.bayan`
   - تنفّذ ٦ دوائر تصوّرية معيارية وتُركّبها في **٥ برامج معاني**:
     1. طالب يذاكر (Student study narrative)
     2. علاج طبي مع عدم يقين (Medical treatment with uncertainty)
     3. استثمار اقتصادي مع مخاطرة (Economic investment with risk)
     4. **بناء علاقات اجتماعية (Social relationship building)** - جديد ✅
     5. **اتخاذ قرارات يومية (Daily decision-making)** - جديد ✅
     موثَّقة في: `docs/CONCEPTUAL_CIRCUITS_AND_PROGRAMS.md` مع أمثلة في
     `examples/conceptual_circuit_*_demo.bayan` و
     `examples/conceptual_program_*_demo.bayan`.
8. **طبقة orchestrator + NL mapper أعلى برامج المعاني**:
   - الملفات:
     - `ai/conceptual_orchestrator.bayan` (تم تحديثه ✅)
     - `ai/conceptual_nl_mapper.bayan` (تم توسيعه ✅)
   - تسمح لك بتمرير رسالة تحكّم structured أو نص طبيعي (عربي/إنجليزي)
     ليتم تحويله إلى `control_message` ثم اختيار برنامج المعاني المناسب
     وتوليد أمثلة LM رمزية تلقائيًا.
   - **المجالات المدعومة الآن (5 مجالات):**
     1. Education (طالب، مذاكرة، دراسة)
     2. Health (مريض، دواء، علاج)
     3. Economy (استثمار، سوق، أسهم)
     4. **Social (صداقة، علاقة، ثقة)** - جديد ✅
     5. **Daily Life (قرار، اختيار، حياة يومية)** - جديد ✅
   - أمثلة تشغيل:
     - `examples/conceptual_orchestrator_demo.bayan`
     - `examples/conceptual_nl_mapper_demo.bayan`
     - `examples/conceptual_interactive_orchestrator_repl.bayan`
     - **`examples/conceptual_orchestrator_social_demo.bayan`** - جديد ✅
       (حلقة تفاعلية من سطر الأوامر).

كل ذلك في طبقات التمثيل والتوليد يجري **بدون إنتاج جمل طبيعية نهائية**؛
المخرجات حتى الآن رمزية بالكامل (traces/circuits/examples)، مع وجود طبقة
صغيرة لقراءة النص الطبيعي كمدخل للتحكّم (NL mapper) فقط.

---

## 2. أهم الملفات التي تهمّك كـ "نموذج مُكمِّل"

### 2.1 طبقة الـ DSL للتصوّرات العامة

- `ai/conceptual_blueprints.bayan`
  - يعرّف 14 نمطًا باستخدام DSL `تصور_عام / conceptual_blueprint`.
  - الأنواع الرئيسة:
    - EventPattern, StatePattern, CausalPattern, LanguageBridgePattern.
  - من بينها أنماط مضافة حديثًا للتوسّع في المقارنة والزمن والسياق:
    - `ComparativePattern`, `TemporalOrderPattern`, `ContextualizationPattern`.
- `docs/CONCEPTUAL_PATTERNS_LIBRARY.md`
  - يشرح كل نمط بالهيكل ذي الأجزاء الستة (هوية، أدوار، شروط، بنية، خرائط، وصلات).

### 2.2 طبقة الجسر اللغوي التنفيذية

- `ai/conceptual_language_bridge.bayan`
  - دوال من نوع `realize_*` + دالة `realize(bp)` عامة.
  - تُدخِل:
    - قاموسًا بالشكل `{ "pattern": <name>, "slots": {...} }`.
  - وتُخرِج:
    - قاموسًا يلخّص نوع الجملة وأدوارها (`type`, `subject`, `predicate`, ...).

### 2.3 طبقة التخطيط السطحي + شجرة الجملة

- `ai/conceptual_surface_planner.bayan`
  - دالة `plan_surface(sentence_roles, lang)` توحّد الواجهة.
  - دوال متخصّصة حاليًا لـ:
    - `ActionSentence`, `StateChangeSentence`, `UncertaintySentence`,
      `CausalSentence` (مع موصل سببي رمزي).
- `ai/conceptual_sentence_tree.bayan`
  - دالة `build_tree(sentence_roles, plan)` + دوال متخصصة لـ:
    - `ActionSentence` (جذر `S` مع عقد Subject/Predicate/Object).
    - `CausalSentence` (جذر `CAUSE_EFFECT` مع CauseEvent/EffectEvent).
  - أنواع أخرى تُعامَل حاليًا عبر مسار fallback عام.

### 2.4 الأمثلة والوثائق التعليمية (الطبقات الأساسية)

- `examples/conceptual_trace_demo.bayan`
- `examples/conceptual_causal_demo.bayan`
- `docs/CONCEPTUAL_TRACE_DEMO.md`
- `docs/CONCEPTUAL_LM_BLUEPRINT.md`
- `docs/CONCEPTUAL_LM_INTEGRATION_GUIDE.md`

### 2.5 طبقة الدوائر التصوّرية وبرامج المعاني

- `ai/conceptual_circuits.bayan`
- `ai/conceptual_programs.bayan`
- `docs/CONCEPTUAL_CIRCUITS_AND_PROGRAMS.md`
- أمثلة:
  - `examples/conceptual_circuit_*_demo.bayan`
  - `examples/conceptual_program_*_demo.bayan`

### 2.6 طبقة orchestrator و NL mapper

- `ai/conceptual_orchestrator.bayan`
- `ai/conceptual_nl_mapper.bayan`
- أمثلة:
  - `examples/conceptual_orchestrator_demo.bayan`
  - `examples/conceptual_nl_mapper_demo.bayan`
  - `examples/conceptual_interactive_orchestrator_repl.bayan`

هذه المجموعات الثلاث هي **نقطة الانطلاق التعليمية** لأي تطوير لاحق
على النموذج اللغوي التصوّري (Circuits/Programs/Orchestrator/NL mapper).

---

## 3. قيود تقنية مهمّة يجب أن تلتزم بها

1. **لا تستخدم معاملات مسمّاة في استدعاء الدوال في بيان**:
   - الصيغة `fn(x=1)` غير مدعومة؛ استخدم فقط استدعاءات بمواقع
     (`fn(1, 2, 3)`).
2. **اجعل كل هذه الطبقات رمزية بالكامل**:
   - يمنع حشو كلمات عربية/إنجليزية حقيقية في هذه الملفات.
   - اسم الفعل/الصفة/المحور يجب أن يكون معرّفًا مفاهيميًا، لا كلمة نهائية.
3. **التزم بفلسفة "نصمّم الصفوف لا الكائنات"**:
   - ركّز على الأنماط والواجهات والبُنى العامة، لا على سيناريوهات جاهزة.
4. **لا تعدّل ملفات إعداد الحزم يدويًا** (مثل `requirements.txt`) دون
   استعمال مدير حزم، حسب سياسة هذا المساعد.
5. **اعتبر أن عيوب اللغة الأساسية الخاصة بـ `None` والفهرسة المتداخلة قد حُلَّت**:
   - يمكنك استخدام `None` كلترال حقيقية في بيان؛ تُترجَم إلى `None` في بايثون.
   - يمكن استعمال الفهرسة المتداخلة داخل قيم القواميس مثل `event["actors"][0]` بأمان.
   - يوجد ملف صغير لاختبار ذلك: `examples/_parser_index_none_regression.bayan`.

---

## 4. ما المطلوب منك أن تكمله؟ (خريطة طريق مقترَحة)

### 4.0 ماذا أنجز هذا الجيل قبلَك؟ (ملخص سريع)

قبل أن تبدأ في تنفيذ العناصر أدناه، من المهم أن تعرف ما الذي تم إنجازه
في هذه النسخة من الشفرة:

1. **برامج المعاني أصبحت تستقبل إعدادات تحكّم**:
   - في `ai/conceptual_programs.bayan` أصبحت التواقيع على الشكل:
     - `build_student_study_narrative_program(settings)`
     - `build_medical_treatment_uncertainty_program(settings)`
     - `build_economic_investment_risk_program(settings)`
     - **`build_social_relationship_program(settings)`** - جديد ✅
     - **`build_daily_decision_program(settings)`** - جديد ✅
   - وتستخدم هذه البرامج الحقول `scenario_variant` و`time_horizon` من
     `settings` لتعديل قيم الاحتمالات وشدّة الروابط في الدوائر التي تبنيها.

2. **orchestrator يمرّر settings إلى برامج المعاني**:
   - في `ai/conceptual_orchestrator.bayan` يتم الآن استدعاء دوال البناء
     بحيث يمرَّر كائن الإعدادات (مثلًا: `program_output = builder(settings)`).
   - أي أن `control_message.settings` لم يعد مجرد حقل معلوماتي، بل
     يُؤثِّر فعليًا في القيم داخل البرامج.
   - **تم إضافة برنامجين جديدين إلى السجل:**
     - `social_relationship` (المجالات: social, friendship, relationships)
     - `daily_decision` (المجالات: daily_life, personal, decision)

3. **تم توسيع NL mapper لدعم المجالات الجديدة**:
   - في `ai/conceptual_nl_mapper.bayan` تمت إضافة كلمات مفتاحية:
     - **المجال الاجتماعي:** صداقة، صديق، علاقة، ثقة / friendship, friend, relationship, trust
     - **مجال الحياة اليومية:** قرار، اختيار، خيار / decision, choice, option

4. **تم اختبار المسار الكامل بالأمثلة**:
   - تم تشغيل `examples/conceptual_orchestrator_demo.bayan` للتأكد من أن
     المسار (NL mapper → orchestrator → programs → LM bridge) يعمل
     بعد هذه التغييرات.
   - **أمثلة جديدة تم إنشاؤها:**
     - `examples/conceptual_program_social_relationship_demo.bayan`
     - `examples/conceptual_orchestrator_social_demo.bayan`
     - `examples/conceptual_program_daily_decision_demo.bayan`
   - استخدم هذه الأمثلة كنقاط اختبار أساسية عند أي تعديل على الطبقات
     العليا (orchestrator / programs / circuits).

5. **تم توثيق العمل المنجز**:
   - `docs/CONCEPTUAL_PROGRAMS_EXPANSION_REPORT.md` - تقرير تقني مفصل
   - `CONCEPTUAL_PROGRAMS_COMPLETION_SUMMARY.md` - ملخص تنفيذي

لا تعِد تنفيذ هذه الخطوات؛ اعتبرها قاعدة ثابتة يمكنك البناء عليها أو
تحسينها.


### 4.1 إكمال تغطية التخطيط السطحي / شجرة الجملة

1. تم بالفعل إضافة مخطِّطات سطحية متخصّصة لـ:
   - `DescriptionSentence`, `IntensitySentence` في
     `ai/conceptual_surface_planner.bayan` (انظر الدوال
     `plan_description_sentence`, `plan_intensity_sentence`).
2. تم توسيع `ai/conceptual_sentence_tree.bayan` بدوال مثل:
   - `build_description_tree`, `build_intensity_tree`.
3. ما تبقّى لك في هذه الطبقة هو:
   - مراجعة هذه الدوال وتحسينها عند الحاجة.
   - إضافة مخططات/أنواع جمل جديدة عند إدخال أنماط تصوّرية جديدة.

### 4.2 تصميم طبقة توليد لغوي فعلية فوق الشجرة

1. تعريف طبقة جديدة مثلًا: `ai/conceptual_surface_realizer.bayan` تقوم بـ:
   - أخذ `SentenceTree` + معلومات عن اللغة/السجل (formal/informal).
   - إنتاج تسلسل Tokens رمزية أقرب إلى اللغة (مع إمكانية ربطها بمفردات).
2. لاحقًا يمكن ربط هذه الطبقة بنماذج `ai/nlp` (n-gram / LM أعمق) للتقييم
   أو الاختيار بين صيغ متعددة.

### 4.3 توسيع مكتبة التصوّرات العامة

- الأنماط التالية مضافة فعلًا في `ai/conceptual_blueprints.bayan` ومُوثَّقة في
  `docs/CONCEPTUAL_PATTERNS_LIBRARY.md`:
  - `ComparativePattern` (مقارنات بين كيانين على محور واحد).
  - `TemporalOrderPattern` (قبل/بعد، تسلسل سردي).
  - `ContextualizationPattern` (وضع الحدث ضمن إطار أوسع).
- ما تبقّى لك هنا:
  - التأكد من أن هذه الأنماط مدمجة بالكامل في الدوائر
    (`ai/conceptual_circuits.bayan`) وبرامج المعاني، وليس فقط موجودة في مستوى
    الـ blueprints.
  - إضافة مثال/أمثلة جديدة تستعمل هذه الأنماط في
    `CONCEPTUAL_CIRCUITS_AND_PROGRAMS.md` أو وثيقة تعليمية جديدة.

### 4.4 ربط أوضح مع طبقة الـ LM الموجودة في `ai/nlp`

- تصميم واجهة بين `SentenceTree` أو التسلسلات الرمزية وبين وحدات:
  - `ai/nlp/vocab`, `ai/nlp/language_model`, إلخ.
- الفكرة: تصبح بيانات التدريب من النوع:
  - `(conceptual_trace, blueprint_roles, sentence_tree) -> text`.

### 4.5 طبقة الدوائر/البرامج/orchestrator/NL mapper: ما تبقّى لك

#### 4.5.1 ✅ توسيع برامج المعاني إلى مجالات أخرى - **مُنجَز**
   - ✅ تم إضافة برنامجين جديدين:
     - `build_social_relationship_program()` - مجال العلاقات الاجتماعية
     - `build_daily_decision_program()` - مجال القرارات اليومية
   - ✅ كلا البرنامجين يستخدمان نفس الدوائر الست الأساسية
   - ✅ تم اختبارهما بنجاح في الأمثلة التوضيحية
   - **يمكنك إضافة المزيد من المجالات** (مثلًا: تعليم مهني، رياضة، سفر، إلخ)
2. **جعل الإعدادات تؤثّر فعليًا في القيم**:
   - في النسخة الحالية، يتم استخدام `scenario_variant` و`time_horizon` فعليًا
     داخل `ai/conceptual_programs.bayan` لتعديل احتمالات الأحداث
     وشدّة الروابط السببية في البرامج الثلاثة الأساسية.
   - ما يزال بإمكانك توسيع ذلك لاستغلال الحقول `detail_level` و`focus`
     (وحتى `scenario_variant` بدرجة أعمق) لاختيار أي الدوائر تُضمَّن أو تُهمَل،
     وكيف تُجزَّأ القصص أو تُبسَّط حسب مستوى التفصيل.
3. **توسيع الـ NL mapper**:
   - زيادة تغطية المفردات والتعابير لكل مجال، مع إبقاء المنطق واضحًا
     وقابلًا للتوسعة (قواعد بسيطة أولًا، ثم يمكن لاحقًا دمج LM خارجي).
4. **تحسين orchestrator واختيار البرامج**:
   - دعم برامج متعددة لنفس المجال/القصد مع سياسة اختيار مرنة
     (مثلًا اختيار برنامج مختلف حسب `scenario_variant` أو `time_horizon`).
5. **إضافة أمثلة تعليمية جديدة**:
   - توثيق سيناريوهات إدخال حقيقية (عربي/إنجليزي) والـ `control_message`
     الناتج عنها وما ينتجه الـ LM الرمزي؛ أضف هذه الأمثلة إلى
     `CONCEPTUAL_CIRCUITS_AND_PROGRAMS.md` أو وثيقة تعليمية جديدة إذا لزم.

---

## 5. كيف تتعامل مع الشفرة الحالية أثناء التوسعة؟

1. **استعمل الأمثلة كنماذج اختبارية**:
   - أي تعديل في الطبقات يجب أن يُختبَر على
     `conceptual_trace_demo.bayan` و `conceptual_causal_demo.bayan`.
2. **حافظ على الواجهات القائمة** قدر الإمكان:
   - لا تغيّر توقيعات الدوال العامة (`realize`, `plan_surface`,
     `build_tree`) إلا لسبب قوي، ومع تحديث الأمثلة والوثائق.
3. **أضِف ولا تستبدِل بشكل عشوائي**:
   - إن احتجت سلوكًا بديلًا، فكّر في إضافة خيار أو نمط جديد بدل حذف القديم.
4. **حدّث الوثائق التعليمية مع كل توسعة مهمّة**:
   - خاصة: `CONCEPTUAL_TRACE_DEMO.md`, `CONCEPTUAL_PATTERNS_LIBRARY.md`.

بهذا تكون لديك خريطة واضحة لتكميل المسير: من أثر تصوّري عام، إلى أنماط
وتخطيط وشجرة جملة رمزية، ثم إلى طبقة توليد لغوي حقيقية يمكنك أنت تصميمها
وتطويرها بالأسلوب الذي تراه مناسبًا.

