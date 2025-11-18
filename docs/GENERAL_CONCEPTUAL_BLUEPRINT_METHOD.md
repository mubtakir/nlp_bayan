# منهجية كتابة "التصوّر العام" قبل النموذج اللغوي في بيان

هذا المستند يلخّص ويعيد تنظيم أفكار **نموذج4** و **نموذج5** كمنهجية عملية لكتابة
"التصوّرات العامة" (General Conceptual Blueprints) التي تشكّل **الطبقة قبل-اللغوية**
للنموذج اللغوي التوليدي في بيان.

يرتبط هذا المستند مع:
- `CONCEPTUAL_LM_BLUEPRINT.md`  — رؤية الطبقات والمعمارية العامة.
- `CONCEPTUAL_TRACE_FORMAT.md`  — تنسيق الأثر التصوّري الموحد.
- `CONCEPTUAL_LM_INTEGRATION_GUIDE.md` — ربط الأثر بإمكانات بيان (كيانات، شبكات، تشابه، احتمال).

الهدف هنا هو: **وصف طريقة منهجية ثابتة** لكتابة أي "تصوّر عام" جديد يمكن
أن يُستخدم فوق الأثر التصوّري وتحت طبقة اللغة.

---

## 1. تعريف "التصوّر العام" (General Conceptual Blueprint)

"التصوّر العام" هو **نمط مفاهيمي محايد**:

- لا يتضمّن أسماء أشخاص أو أشياء أو أفعال خاصة بمجال معيّن.
- يعمل كجسر بين:
  - العالم الوجودي/المعرفي في بيان:
    - كيانات، حالات [0..1]، خصائص، أفعال، أحداث، تحوّلات، معادلات.
    - شبكات سببية ودلالية، علاقات تشابه/مترادفات.
    - درجات احتمال/تشكيك.
  - طبقة اللغة:
    - التي تستقبل معنى مجرّدًا (conceptual trace) وتحوّله إلى جمل.

التصوّر العام يحدّد:

1. **النمط المفاهيمي** للحدث/الحالة/العلاقة (حدث، تحوّل، سببـنتيجة، وصف حالة...).
2. **الأدوار الأساسية** (Actor, Target, PropertyAxis, Cause, Result, Context, ...).
3. **القيَم والعلاقات** المطلوبة (درجات، احتمالات، علاقات سببية/دلالية...).
4. **وصلات الجسر اللغوي**: نوع القالب اللغوي الذي سيُستخدم لاحقًا (دون
   تحديد الألفاظ الآن).

---

## 2. الهيكل القياسي لأي "تصوّر عام" (6 أقسام)

كل تصوّر عام يُكتب وفق قالب ثابت مكوَّن من ستة أجزاء:

### 2.1 الهوية المفاهيمية (Concept Identity)

- **اسم عام للتصوّر** (رمزي، غير مجالي)، مثل:
  - `Generic_Action_Pattern`
  - `State_Change_Template`
  - `Basic_Causal_Link`
- **التصنيف** (Concept Type):
  - `EventPattern` / `StatePattern` / `CausalPattern` /
    `InteractionPattern` / `PropertyMappingPattern` /
    `LanguageBridgePattern`.

### 2.2 الأدوار المفاهيمية (Conceptual Roles)

قائمة بالمتغيّرات المفاهيمية التي يملؤها الأثر التصوّري، مثل:

- `Actor`       — كيان يقوم بدور فاعل.
- `Target`      — كيان يتأثّر.
- `PropertyAxis` — محور خاصية له أضداد (حر/برد، قوة/ضعف...).
- `StateValue`  — قيمة حالة ∈ [0..1].
- `EventType`   — نوع حدث (معرفي/مجرد، غير لغوي).
- `Domain` / `Environment` — من الأثر.
- `Cause` / `Effect` — مراجع لأحداث/تحوّلات.
- `Intensity` / `Probability` / `Confidence` — درجات.

هذه الأدوار **أماكن** تُملأ من `conceptual_trace` وليست أسماء نهائية.

### 2.3 الشروط العامة (General Preconditions)

تصف متى يكون الـ trace مناسبًا لتطبيق هذا النمط، مثلاً:

- وجود حدث في `events` يملك:
  - `Actor` من مجموعة كيانات معيّنة.
  - `Target` موجود وله `PropertyAxis` محدّد.
- وجود تحوّل في `transforms`:
  - `changed(Entity, Property, Before, After)` مع `Before ≠ After`.
- وجود رابط سببي اختياري بين حدث ونتيجة.

هذه الشروط أشبه بـ **حراس (guards)** للنمط.

### 2.4 البنية المجرّدة (Abstract Structure)

هنا نرسم الهيكل المفاهيمي بدون لغة طبيعية ولا كود تنفيذ، مثلاً:

- **نمط حدث (EventPattern):**
  - `event_id`: E
  - `actors`: {Actor_i (role, degree)}
  - `targets`: {Target_j (role)}
  - `action`: EventType
  - `context`: {domain, environment, time}

- **نمط تحوّل حالة (StateTransition):**
  - `entity`: Target
  - `property`: PropertyAxis
  - `before`: v1
  - `after`: v2
  - `delta`: v2 - v1
  - `law_applied`: L?

- **نمط سببي (CausalPattern):**
  - `cause_event`: E1
  - `effect_event`: E2
  - `strength`: S ∈ [0..1]
  - `justification`: J?

### 2.5 خرائط الارتباط مع الأثر (Trace Mappings)

تحدد بدقة كيف تُملأ الأدوار من `conceptual_trace`:

- `Entity`       ← من `entities` (معرف، نوع، مجال...).
- `PropertyAxis` ← من `transforms[k].state_name` أو تعريف محور في نظام الكيانات.
- `BeforeValue`  ← من `transforms[k].before`.
- `AfterValue`   ← من `transforms[k].after`.
- `CauseEvent`   ← من `transforms[k].event_id` أو من شبكة سببية.
- `Domain`       ← من `entities[Entity].domain`.
- درجات الاحتمال/الثقة ← من حقول `events.probability`, `meta.confidence`, روابط الشبكات.

### 2.6 وصلات الجسر اللغوي (Language Bridge Hooks)

من دون صياغة كلمات، نحدد **نوع القالب اللغوي** المناسب للنمط، مثل:

- `ActionSentencePattern(Actor, Action, Target, Context)`.
- `StateChangeSentencePattern(Entity, PropertyAxis, Before, After, Delta, Context)`.
- `CausalSentencePattern(Cause, Effect, Strength)`.
- `UncertaintyPattern(Content, Degree)`.

هذه الوصلات تخبر طبقة الجسر: "أي نوع من الجملة يجب أن يُستخدم"،
لا "كيف تُكتب الجملة".

---

## 3. عائلات التصوّرات التي يجب تغطيتها

عند بناء مكتبة "الطبقة السفلى"، يُستحسن تغطية أربع عائلات رئيسة:

1. **تصوّرات أحداث (Event Blueprints)**
   - `Generic_Interaction_Event`
   - `Transfer_Event`
   - `Motion_Event`
   - `Perception_Event`
   - `Influence_Event`
   - `Cognitive_Event`
   - `Communication_Event`.

2. **تصوّرات حالات (State Patterns)**
   - `PropertyAxisMapping`
   - `OppositesAxisTemplate`
   - `MultiPropertyState`
   - `ThresholdEvaluation`
   - `DegreeInterpretation` (low/medium/high).

3. **تصوّرات سببية (Causal Patterns)**
   - `Basic_Cause_Effect`
   - `MultiCause_MultiEffect`
   - `Probabilistic_Causation`
   - `Temporal_Causation`
   - `Conditional_Causation`.

4. **تصوّرات جسر لغوي (Language Bridge Patterns)**
   - `ActionSentencePattern`
   - `StateChangeSentencePattern`
   - `CausalSentencePattern`
   - `DescriptionPattern` (وصف خصائص فقط)
   - `ComparativePattern`
   - `UncertaintyPattern`
   - `IntensityPattern`
   - `ContextualizationPattern` (زمان/مكان/مجال).

كل واحد من هذه التصوّرات يُكتب وفق الأقسام الستة أعلاه.

---

## 4. خطوات بناء مكتبة كاملة من التصوّرات

لبناء مكتبة عملية فوق بيان:

1. **تحديد النوع** لكل نمط جديد:
   - هل هو حدث؟ حالة؟ سببي؟ جسر لغوي؟
2. **تعريف الأدوار المفاهيمية** بدقة، مع ذكر أنواعها وقيمها المتوقعة.
3. **وضع الشروط العامة** التي يجب أن يحقّقها `conceptual_trace` لتطبيق النمط.
4. **رسم البنية المجرّدة** للنمط (هيكل مفاهيمي فقط).
5. **كتابة خرائط الارتباط** مع مكونات الأثر (entities, states, events, transforms, networks).
6. **تحديد نوع القوالب اللغوية** التي ستستخدم هذا النمط لاحقًا.

بتكرار هذه الخطوات عبر عائلات الأنماط أعلاه، نحصل على
"مكتبة تصوّرات عامة" تشكّل طبقة ثابتة وقابلة لإعادة الاستخدام فوق
الأثر التصوّري وتحت النموذج اللغوي.

