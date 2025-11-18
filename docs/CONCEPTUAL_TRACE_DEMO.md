## سيناريو تجريبي: من الأثر التصوّري إلى الجسر اللغوي في بيان

هذه الوثيقة تشرح مثالًا تعليميًا مكتملًا يربط بين أربع طبقات:

1. **الأثر التصوّري** `conceptual_trace` (كيانات + أحداث + تحوّلات + سياق).
2. **التصوّرات العامة** (General Conceptual Blueprints) المعرَّفة عبر DSL في
   `ai/conceptual_blueprints.bayan`.
3. **هياكل الجسر اللغوي المجرّدة** (Language-Bridge Structures) في
   `examples/conceptual_trace_demo.bayan`، والتي تبقى قبل-لغوية (لا كلمات سطحية).
4. **طبقة التخطيط السطحي الرمزي + شجرة الجملة الرمزية** في
   `ai/conceptual_surface_planner.bayan` و `ai/conceptual_sentence_tree.bayan`.

الهدف: تقديم سيناريو مرجعي يوضّح كيف يعمل نموذج لغوي **تصوّري** فوق بيان، قبل أن
نصل إلى الطبقة اللغوية الحقيقية.

---

## 1. الأثر التصوّري conceptual_trace

في الملف:

- `examples/conceptual_trace_demo.bayan`

نعرّف في كتلة `hybrid { ... }` أثرًا تصوّريًا مبسّطًا:

- كيانان رمزيان: `Entity_A`, `Entity_B`.
- حدث تفاعلي واحد: `Event_1` بنوع فعل عام `GenericAction`، مع:
  - قائمة فاعلين `actors = ["Entity_A"]`
  - قائمة متلقّين `targets = ["Entity_B"]`
  - شدة/احتمال: `intensity = 0.7`, `probability = 0.85`
- تحوّل حالة واحد (state change) على محور خصائص رمزي `PropertyAxis`:
  - قبل: `0.3`
  - بعد: `0.6`
  - قانون: `"default_state_change"`
- معلومات ميتا:
  - `source = "abstract_example"`
  - `confidence = 0.9`

هذا الأثر لا يذكر أسماء حقيقية ولا سياق واقعي؛ كل شيء رمزي ومحايد مجاليًا.

---

## 2. تحميل التصوّرات العامة عبر DSL

في البداية نستورد مكتبة التصوّرات العامة:

- `import ai.conceptual_blueprints as blueprints`

في ملف:

- `ai/conceptual_blueprints.bayan`

عرّفنا ١١ تصوّرًا عامًا باستخدام DSL `تصور_عام / conceptual_blueprint`، منها:

- `Generic_Interaction_Event` (نمط حدث تفاعل عام)
- `State_Change_Template` (نمط تغيّر حالة على محور خصائص)
- `Basic_Cause_Effect`، `OppositesAxisTemplate`،
- `Probabilistic_Causation`
- `ActionSentencePattern`، `StateChangeSentencePattern`، `UncertaintyPattern`
- **مضاف حديثًا**: `CausalSentencePattern`, `DescriptionPattern`, `IntensityPattern`.

عند تشغيل المثال، يحمِّل المترجم هذه التصوّرات إلى سجلّ داخلي:

- `blueprints._conceptual_blueprints`

ويطبع عددها وأسماءها للتثبّت من أن طبقة الـ DSL تعمل كما هو متوقّع.

---

## 3. تعبئة الأدوار من الأثر التصوّري (Role Filling)

### 3.1 نمط الحدث: Generic_Interaction_Event

بدل كتابة خوارزمية مطابقة كاملة، يوضّح المثال **فكرة** تعبئة الأدوار من الـ trace
بصورة رمزية مبسّطة:

- `Actor`  `Entity_A`
- `Target`  `Entity_B`
- `ActionKind`  `GenericAction`
- `Context`  `AbstractContext`
- `Probability`  `0.85`

هذه القيم هي إعادة استخدام مباشرة للمعلومات في `conceptual_trace`، مع تعليقات في
الملف توضح كيف تُستخرج (مثلًا من `events[0]`).

### 3.2 نمط تغيّر الحالة: State_Change_Template

بالمثل، نملأ أدوار نمط تغيّر حالة عام:

- `Entity`  `Entity_A`
- `PropertyAxis`  `PropertyAxis`
- `BeforeValue`  `0.3`
- `AfterValue`  `0.6`
- `Delta`  `0.3`
- `CauseEvent`  `Event_1`
- `Context`  `AbstractContext`

هنا **طبقة التصوّرات العامة** تعطي معنى مفاهيمي واضحًا: حدث تفاعل سبّب تغيّرًا في
حالة كيان على محور معيّن.

---

## 4. هياكل الجسر اللغوي (Language-Bridge Structures)

بعد تعبئة الأدوار، يبني المثال ثلاث هياكل مجرّدة تمثّل **خطط جمل** (sentence
plans) قبل-لغوية:

1. `ActionSentencePattern`
2. `StateChangeSentencePattern`
3. `UncertaintyPattern`

كل هيكل عبارة عن قاموس بالشكل:

- `{"pattern": <اسم النمط>, "slots": {...}}`

حيث `slots` يحتوي على توزيع القيم على أدوار لغوية عامة (Actor, Action, Target,
PropertyAxis, Degree, Context, ...). النتيجة هي طبقة وسيطة بين:

- العالم التصوّري (entities, events, transforms, meta)
- والطبقة اللغوية اللاحقة (التي ستختار اللغة والكلمات والتركيب النحوي).

المثال يطبع هذه الهياكل كما هي، لتوضيح بنيتها وعدم احتوائها على أي كلمات من لغة
طبيعية.

---

## 5. الطبقات التنفيذية الحالية فوق الهياكل الجسرية

في النسخة الحالية من المشروع، تمّ بالفعل تنفيذ الطبقات التالية فوق الهياكل المجرّدة
السابقة:

1. **طبقة الجسر اللغوي التنفيذية** في
   `ai/conceptual_language_bridge.bayan`:
   - تحوّل هياكل `ActionSentencePattern` و `StateChangeSentencePattern`
     و`UncertaintyPattern` (وأيضًا `CausalSentencePattern`، `DescriptionPattern`,
     `IntensityPattern`) إلى **أدوار جملة عامة** من نوع:
     - `type = ActionSentence / StateChangeSentence / ...`
     - حقول مثل: `subject`, `predicate`, `object`, `entity`, `property_axis`, ...
2. **طبقة التخطيط السطحي الرمزي** في
   `ai/conceptual_surface_planner.bayan`:
   - تأخذ هذه الأدوار وتبني خطة سطحية رمزية (قائمة `sequence`) بترتيب يعتمد على
     منظور لغوي رمزي (مثلاً: SVO للإنجليزية، VSO للعربية).
3. **طبقة شجرة الجملة الرمزية** في
   `ai/conceptual_sentence_tree.bayan`:
   - ترفع الخطة السطحية إلى **شجرة جملة رمزية** `SentenceTree` مع جذر `S` أو
     `CAUSE_EFFECT` وأبناء يمثّلون الأدوار الرئيسة، مع الاحتفاظ بالترتيب السطحي
     والـ modifiers في الحقول المناسبة.

هذه الطبقات الثلاث تبقى كلّها قبل لغوية (لا يوجد اختيار كلمات حقيقية بعد)، لكنها تمثّل
جسرًا كاملاً من `conceptual_trace` إلى تمثيل رمزي غني للجملة يمكن أن يُغذّي لاحقًا
مولّدًا لغويًا فعليًا.
---

## 6. المثال السببي الثاني (conceptual_causal_demo)

### 6.1 الهدف

الملف:
- `examples/conceptual_causal_demo.bayan`

يقدّم سيناريوًا تجريديًا ثانيًا يركّز على:

1. **روابط سببية صريحة** بين حدث سبب وحدث نتيجة (`causal_links`).
2. **محور أضداد رمزي** `OppositesAxisTemplate` لوصف حالة كيان.
3. **أنماط جسر لغوي جديدة**:
   - `CausalSentencePattern`
   - `DescriptionPattern`
   - `IntensityPattern`

### 6.2 بنية trace السببية

الأثر `causal_trace` يحتوي على:

- كيانين رمزيين: `Entity_C`, `Entity_D`.
- حدث سبب: `Event_Cause` بنوع `AbstractCauseAction`.
- حدث نتيجة: `Event_Effect` بنوع `AbstractEffectAction`.
- رابط سببي في `causal_links`:
  - `cause = Event_Cause`
  - `effect = Event_Effect`
  - `strength = 0.8`
  - `prob = 0.75`
- حالة على محور أضداد رمزي لكيان `Entity_D`:
  - `name = "AbstractAxis"`
  - `value = 0.7`

### 6.3 تعبئة الأنماط السببية والوصفية

يبني المثال ثلاثة قواميس أدوار:

1. `basic_cause_roles` لنمط `Basic_Cause_Effect`.
2. `probabilistic_roles` لنمط `Probabilistic_Causation`.
3. `opposites_roles` لنمط `OppositesAxisTemplate`.

ثم تُبنى منها هياكل الجسر اللغوي:

- `CausalSentencePattern` لجملة سببية عامة.
- `DescriptionPattern` لوصف حالة كيان على محور أضداد.
- `IntensityPattern` لتمثيل شدة/درجة على محور أضداد.

### 6.4 تحقيق الجمل رمزيًا والتخطيط السطحي

يُستدعى `conceptual_language_bridge.realize` لإنتاج هياكل من الأنواع:

- `CausalSentence`
- `DescriptionSentence`
- `IntensitySentence`

بعد ذلك يُجرَّب تخطيط سطحي رمزي للجملة السببية فقط عبر:

- `ai.conceptual_surface_planner.plan_surface` مع منظورين:
  - `lang = "english"` (ترتيب سبب → رابط سببي → نتيجة)
  - `lang = "arabic"` (ترتيب نتيجة ← رابط سببي ← سبب)

### 6.5 شجرة الجملة السببية

أخيرًا، يبيّن المثال كيف تُرفع الخطة السطحية السببية إلى **شجرة جملة رمزية** عبر:

- `ai.conceptual_sentence_tree.build_tree(realized_causal, plan_causal_*)`

حيث الجذر يحمل التسمية `CAUSE_EFFECT` وله ابن **CauseEvent** وابن **EffectEvent**،
بينما تبقى المعلّمات الرقمية (القوة، الاحتمال، السياق) في حقل `modifiers` في العقدة
العلوية، دون تحويلها إلى كلمات.


بهذا المثال، تصبح لدينا سلسلة كاملة واضحة:

- `conceptual_trace`  **تصوّرات عامة**  **هياكل جسر لغوي مجرّدة**،

جاهزة لأن تُستخدم كأساس لنموذج لغوي توليدي يعمل فوق بيان، مع فصلٍ واضح بين
الطبقة التصوّرية والطبقة اللغوية.

