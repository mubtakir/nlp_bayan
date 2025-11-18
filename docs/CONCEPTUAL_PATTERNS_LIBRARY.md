# مكتبة أولية للتصوّرات العامة (General Conceptual Blueprints)

هذا المستند يعرّف **مجموعة أنماط عامة** (Blueprints) تُستخدم فوق
`conceptual_trace` وقبل طبقة اللغة، وفق المنهجية في:

- `GENERAL_CONCEPTUAL_BLUEPRINT_METHOD.md`

لكل نمط نستخدم البنية المختصرة ذات الأقسام الستة:

1. الهوية (Identity)
2. الأدوار (Roles)
3. الشروط (Preconditions)
4. البنية المجرّدة (Abstract Structure)
5. خرائط الارتباط مع الأثر (Trace Mappings)
6. وصلات الجسر اللغوي (Language Hooks)

> هذه الأنماط تجريدية تمامًا، قابلة للتخصيص لاحقًا من قِبَل المبرمج.

---

## 1. Generic_Interaction_Event (EventPattern)

1) **الهوية**
- الاسم: `Generic_Interaction_Event`
- النوع: `EventPattern`

2) **الأدوار**
- `Actor`       — كيان/كيانات تقوم بالفعل.
- `Target`      — كيان/كيانات تتأثر بالفعل.
- `Instrument?` — كيان يُستخدم أداة.
- `Context`     — {Domain, Environment, Time}.
- `Intensity`   — درجة شدة الحدث.
- `Probability` — احتمال وقوع الحدث.

3) **الشروط**
- وجود حدث في `events` له على الأقل Actor واحد.
- يمكن أن يكون له Target واحد أو أكثر.
- يمكن وجود درجة شدة واحتمال.

4) **البنية المجرّدة**
- `event_id`: E
- `actors`: { (Actor_i, degree_i) }
- `targets`: { (Target_j, degree_j) }
- `action`: EventType
- `context`: {domain, environment, time}
- `intensity`: Intensity ∈ [0..1]
- `probability`: Prob ∈ [0..1]

5) **خرائط الارتباط**
- من `conceptual_trace.events[k]` إلى الأدوار المذكورة.

6) **وصلات لغوية**
- يستخدم مع: `ActionSentencePattern`، وربما `UncertaintyPattern`.

---

## 2. State_Change_Template (StatePattern)

1) **الهوية**
- الاسم: `State_Change_Template`
- النوع: `StatePattern`

2) **الأدوار**
- `Entity`        — كيان يتغيّر.
- `PropertyAxis`  — محور خاصية له أضداد.
- `BeforeValue`   — قيمة قبل الحدث.
- `AfterValue`    — قيمة بعد الحدث.
- `Delta`         — مقدار التغيّر.
- `Context`       — {Domain, Environment, Time}.
- `CauseEvent?`   — حدث سببي محتمل.

3) **الشروط**
- وجود مدخلة في `transforms` مع `before ≠ after`.
- الخاصية معرفة كمحور في نظام الكيانات.

4) **البنية المجرّدة**
- `entity`: Entity
- `property`: PropertyAxis
- `before`: BeforeValue
- `after`: AfterValue
- `delta`: AfterValue - BeforeValue
- `context`: {domain, environment, time}
- `caused_by`: CauseEvent?

5) **خرائط الارتباط**
- من `transforms[k]`، و `entities[entity]`، وروابط السببية.

6) **وصلات لغوية**
- يستخدم مع: `StateChangeSentencePattern`، و `IntensityPattern`.

---

## 3. OppositesAxisTemplate (StatePattern)

1) **الهوية**
- الاسم: `OppositesAxisTemplate`
- النوع: `StatePattern`

2) **الأدوار**
- `Axis`      — محور خاصية ثنائي القطب.
- `Positive`  — القطب الموجب (اسم مفاهيمي).
- `Negative`  — القطب السالب.
- `Value`     — قيمة ∈ [0..1].
- `Degree`    — تصنيف لغوي (low/medium/high...).

3) **الشروط**
- وجود تعريف أضداد في نظام الكيانات/الأثر.
- قيمة رقمية على المحور.

4) **البنية المجرّدة**
- `axis`: Axis
- `value`: Value
- `polarity`: {positive, negative, balanced}
- `degree_label`: Degree

5) **خرائط الارتباط**
- من تعريفات الأضداد + `states` أو `properties` على ذلك المحور.

6) **وصلات لغوية**
- يستخدم مع: `DescriptionPattern`, `IntensityPattern`.

---

## 4. Basic_Cause_Effect (CausalPattern)

1) **الهوية**
- الاسم: `Basic_Cause_Effect`
- النوع: `CausalPattern`

2) **الأدوار**
- `CauseEvent`   — حدث سبب.
- `EffectEvent`  — حدث نتيجة.
- `Strength`     — قوة الرابطة السببية.
- `Conditions?`  — شروط إضافية.

3) **الشروط**
- وجود رابط سببي بين حدثين في شبكة السببية أو transforms.

4) **البنية المجرّدة**
- `cause`: CauseEvent
- `effect`: EffectEvent
- `strength`: S ∈ [0..1]
- `conditions`: {condition_i}?

5) **خرائط الارتباط**
- من `conceptual_trace.networks.causal`.

6) **وصلات لغوية**
- يستخدم مع: `CausalSentencePattern`.

---

## 5. Probabilistic_Causation (CausalPattern)

1) **الهوية**
- الاسم: `Probabilistic_Causation`
- النوع: `CausalPattern`

2) **الأدوار**
- `CauseEvent`
- `EffectEvent`
- `CausalStrength`   — قوة العلاقة.
- `ConditionalProb`  — P(Effect | Cause).

3) **الشروط**
- وجود رابط سببي مع حقل احتمالية أو ثقة.

4) **البنية المجرّدة**
- `cause`: CauseEvent
- `effect`: EffectEvent
- `strength`: CausalStrength
- `probability`: ConditionalProb

5) **خرائط الارتباط**
- من شبكة السببية + حقول الاحتمال.

6) **وصلات لغوية**
- يستخدم مع: `CausalSentencePattern` + `UncertaintyPattern`.

---

## 6. ActionSentencePattern (LanguageBridgePattern)

1) **الهوية**
- الاسم: `ActionSentencePattern`
- النوع: `LanguageBridgePattern`

2) **الأدوار**
- `Actor`
- `Action`
- `Target?`
- `Instruments?`
- `Context?`
- `Intensity?`
- `Uncertainty?`

3) **الشروط**
- وجود نمط حدث مناسب (مثل `Generic_Interaction_Event`).

4) **البنية المجرّدة**
- قالب منطقي: `ActionSentence(Actor, Action, Target, Context, Intensity, Uncertainty)`.

5) **خرائط الارتباط**
- الأدوار تُملأ من الحدث والنمط التصوّري المرتبط به.

6) **الاستخدام اللغوي**
- يحدد فقط شكل الجملة، لا الكلمات.

---

## 7. StateChangeSentencePattern (LanguageBridgePattern)

1) **الهوية**
- الاسم: `StateChangeSentencePattern`
- النوع: `LanguageBridgePattern`

2) **الأدوار**
- `Entity`
- `PropertyAxis`
- `BeforeValue`
- `AfterValue`
- `Delta`
- `Context?`

3) **الشروط**
- وجود نمط `State_Change_Template` مُطبَّق.

4) **البنية المجرّدة**
- `StateChangeSentence(Entity, PropertyAxis, Before, After, Delta, Context)`.

5) **خرائط الارتباط**
- من حقول `State_Change_Template`.

6) **الاستخدام اللغوي**
- يدعم جملًا من نوع: "كيان يتغيّر من حالة إلى حالة".

---

## 8. UncertaintyPattern (LanguageBridgePattern)

1) **الهوية**
- الاسم: `UncertaintyPattern`
- النوع: `LanguageBridgePattern`

2) **الأدوار**
- `Content`   — محتوى الجملة أو الحدث.
- `Degree`    — درجة يقين ∈ [0..1].

3) **الشروط**
- وجود حقل احتمال/ثقة مرتبط بالحدث أو بالحكم ككل.

4) **البنية المجرّدة**
- `Uncertainty(Content, Degree)`.

5) **خرائط الارتباط**
- من `events.probability` أو `meta.confidence`.

6) **الاستخدام اللغوي**
- يختار طبقة التعبير (ربما، غالبًا، بالتأكيد...) بناءً على `Degree`.

---

## 9. CausalSentencePattern (LanguageBridgePattern)

1) **الهوية**
- الاسم: `CausalSentencePattern`
- النوع: `LanguageBridgePattern`

2) **الأدوار**
- `CauseEvent`   — حدث سبب (من نمط `Basic_Cause_Effect` أو `Probabilistic_Causation`).
- `EffectEvent`  — حدث نتيجة.
- `Strength?`    — قوة الرابطة السببية (∈ [0..1]).
- `Probability?` — احتمال/ثقة في العلاقة السببية.
- `Context?`     — سياق عام (مجال/بيئة/زمن...).

3) **الشروط**
- وجود نمط سببي مطبَّق مثل:
  - `Basic_Cause_Effect`
  - `Probabilistic_Causation`

4) **البنية المجرّدة**
- `CausalSentence(CauseEvent, EffectEvent, Strength, Probability, Context)`.

5) **خرائط الارتباط**
- من نتائج تطبيق الأنماط السببية على `conceptual_trace.causal_links` أو ما يماثلها.

6) **الاستخدام اللغوي**
- يعبّر عن جمل من نمط: "بسبب {السبب} حدث {النتيجة}"، مع بقاء جميع العناصر رمزية وغير لغوية.

---

## 10. DescriptionPattern (LanguageBridgePattern)

1) **الهوية**
- الاسم: `DescriptionPattern`
- النوع: `LanguageBridgePattern`

2) **الأدوار**
- `Entity`  — كيان يوصف.
- `Axis`    — محور أضداد (من `OppositesAxisTemplate`).
- `Degree`  — تسمية رمزية لدرجة (High/Medium/Low...).
- `Value?`  — قيمة رقمية ∈ [0..1] إن وجدت.

3) **الشروط**
- وجود محور أضداد مع قيمة حالة/خاصية لذلك الكيان.

4) **البنية المجرّدة**
- `Description(Entity, Axis, Degree, Value)`.

5) **خرائط الارتباط**
- من `states` أو `properties` المرتبطة بمحور الأضداد.

6) **الاستخدام اللغوي**
- يعبّر عن جمل وصفية مثل: "الكيان على المحور كذا بدرجة كذا" (بشكل رمزي).

---

## 11. IntensityPattern (LanguageBridgePattern)

1) **الهوية**
- الاسم: `IntensityPattern`
- النوع: `LanguageBridgePattern`

2) **الأدوار**
- `Axis`   — محور أضداد.
- `Value`  — قيمة رقمية ∈ [0..1].
- `Degree` — تصنيف رمزي للدرجة (High/Medium/Low...).

3) **الشروط**
- وجود قيمة عددية على محور أضداد معروف.

4) **البنية المجرّدة**
- `Intensity(Axis, Value, Degree)`.

5) **خرائط الارتباط**
- من قيم المحور في نظام الكيانات أو `states`.

6) **الاستخدام اللغوي**
- يربط قيمة عددية بدرجة تعبيرية (ضعيف/متوسط/قوي...) دون اختيار كلمات حقيقية.


---

## 12. ComparativePattern (LanguageBridgePattern)

1) **الهوية**
- الاسم: `ComparativePattern`
- النوع: `LanguageBridgePattern`

2) **الأدوار**
- `Entity1` — الكيان الأول في المقارنة.
- `Entity2` — الكيان الثاني في المقارنة.
- `Axis` — محور أضداد واحد تتم المقارنة عليه.
- `Value1` — قيمة ∈ [0..1] لكيان 1 على هذا المحور.
- `Value2` — قيمة ∈ [0..1] لكيان 2 على هذا المحور.
- `ComparisonType` — تسمية رمزية (greater/less/equal).

3) **الشروط**
- وجود قيم عددية لـ `Entity1` و `Entity2` على نفس المحور.
- يُفضَّل أن يكون المحور معرَّفًا عبر `OppositesAxisTemplate`.

4) **البنية المجرّدة**
- `ComparativeSentence(Entity1, Entity2, Axis, Value1, Value2, ComparisonType)`.

5) **خرائط الارتباط**
- من `states` أو `properties` التي تحفظ القيم على محور أضداد مشترك.

6) **الاستخدام اللغوي**
- يدعم جملًا من نمط: "كيان 1 أعلى/أقوى من كيان 2 على محور معين" بشكل رمزي، دون اختيار كلمات حقيقية.

---

## 13. TemporalOrderPattern (TemporalPattern)

1) **الهوية**
- الاسم: `TemporalOrderPattern`
- النوع: `TemporalPattern`

2) **الأدوار**
- `Event1` — الحدث الأول.
- `Event2` — الحدث الثاني.
- `TemporalRelation` — علاقة زمنية (before/after/during...).

3) **الشروط**
- توفر ترتيب زمني أو طابع زمني (timestamp) للأحداث في `conceptual_trace.events`.

4) **البنية المجرّدة**
- `TemporalOrder(Event1, Event2, TemporalRelation)`.

5) **خرائط الارتباط**
- من ترتيب الأحداث في `events` أو من حقل زمن صريح إن وُجد.

6) **الاستخدام اللغوي**
- يدعم جملًا من نمط: "بعد أن حدث {Event1}، حدث {Event2}" بشكل رمزي.

---

## 14. ContextualizationPattern (LanguageBridgePattern)

1) **الهوية**
- الاسم: `ContextualizationPattern`
- النوع: `LanguageBridgePattern`

2) **الأدوار**
- `FocusEvent` — الحدث الذي نريد وصفه.
- `ContextFrame` — إطار سياقي أوسع (مجال، بيئة، حالة عامة...).
- `Scope` — مدى تغطية السياق (local/global/background...).

3) **الشروط**
- توفّر سياق عام للحدث في `conceptual_trace.meta` أو حقول مشابهة.

4) **البنية المجرّدة**
- `Contextualized(FocusEvent, ContextFrame, Scope)`.

5) **خرائط الارتباط**
- من حقول `events` (مثل domain/environment) أو من `meta` على مستوى المشهد.

6) **الاستخدام اللغوي**
- يمكّن من وضع الحدث في إطار أوسع عند التوليد: "ضمن سياق {ContextFrame}، حدث {FocusEvent}" بشكل رمزي.


1) **الهوية**
- الاسم: `UncertaintyPattern`
- النوع: `LanguageBridgePattern`

2) **الأدوار**
- `Content`   — محتوى الجملة أو الحدث.
- `Degree`    — درجة يقين ∈ [0..1].

3) **الشروط**
- وجود حقل احتمال/ثقة مرتبط بالحدث أو بالحكم ككل.

4) **البنية المجرّدة**
- `Uncertainty(Content, Degree)`.

5) **خرائط الارتباط**
- من `events.probability` أو `meta.confidence`.

6) **الاستخدام اللغوي**
- يختار طبقة التعبير (ربما، غالبًا، بالتأكيد...) بناءً على `Degree`.

