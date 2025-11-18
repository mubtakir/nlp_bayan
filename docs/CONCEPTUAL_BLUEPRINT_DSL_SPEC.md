# مواصفة أولية لـ DSL تعريف التصوّرات العامة في بيان

هذا المستند يقدّم مواصفة أولية لـ **لغة تعريف تصوّرات عامة** (DSL)
تُكتب داخل بيان، لتعريف أنماط مثل: `Generic_Interaction_Event`, `State_Change_Template`,
`Basic_Cause_Effect`, `ActionSentencePattern`... وفق المنهجية في:

- `GENERAL_CONCEPTUAL_BLUEPRINT_METHOD.md`
- `CONCEPTUAL_PATTERNS_LIBRARY.md`

> هذه المواصفة **مفاهيمية**، تمهّد لاحقًا لبناء Parser/مفسّر فعلي داخل نظام بيان.

---

## 1. الهدف من الـ DSL

- تمكين مبرمج بيان من تعريف/توسيع **مكتبة التصوّرات العامة** بطريقة:
  - منسّقة وثابتة البنية.
  - قابلة للمعالجة الآلية (توليد هياكل conceptual patterns).
  - متكاملة مع `conceptual_trace` والجسر اللغوي.

- لا تُستخدم هذه الـ DSL لتصريح أمثلة نهائية (زيد، مدرسة...)
  بل لتعريف **قوالب عامة** تعمل فوق أي مجال.

---

## 2. التصميم العام للـ DSL

نقترح أن تُكتب التصوّرات داخل وحدة/ملف بيان مخصّص، بصياغة مثل:

```bayan
hybrid {
  تصور_عام State_Change_Template {
    نوع: StatePattern

    أدوار: {
      Entity:        {kind: "entity"}
      PropertyAxis:  {kind: "axis"}
      BeforeValue:   {kind: "value", range: [0, 1]}
      AfterValue:    {kind: "value", range: [0, 1]}
      Delta:         {kind: "derived"}
      Context:       {kind: "context"}
      CauseEvent?:   {kind: "event", optional: true}
    }

    شروط: {
      requires_transform: true
      require_axis_definition: true
    }

    بنية: {
      entity:    Entity
      property:  PropertyAxis
      before:    BeforeValue
      after:     AfterValue
      delta:     AfterValue - BeforeValue
      context:   Context
      caused_by: CauseEvent?
    }

    خرائط_أثر: {
      from_transforms: true
      entity_ref:   "transforms[k].entity_id"
      property_ref: "transforms[k].state_name"
      before_ref:   "transforms[k].before"
      after_ref:    "transforms[k].after"
    }

    قوالب_لغوية: [StateChangeSentencePattern]
  }
}
```

> هذه الصياغة تقريبية، قابلة للتعديل عند تنفيذ الـ Parser الفعلي.

---

## 3. العناصر الأساسية في الـ DSL

### 3.1 رأس التعريف

- الكلمة الأساسية: `تصور_عام` (أو `concept_blueprint` بالإنجليزية).
- الشكل العام:

```bayan
تصور_عام اسم_التصور {
  نوع: ...
  أدوار: {...}
  شروط: {...}
  بنية: {...}
  خرائط_أثر: {...}
  قوالب_لغوية: [...]
}
```

### 3.2 حقل "نوع" (Pattern Type)

- يأخذ قيمًا ثابتة:
  - `EventPattern`
  - `StatePattern`
  - `CausalPattern`
  - `InteractionPattern`
  - `PropertyMappingPattern`
  - `LanguageBridgePattern`

### 3.3 حقل "أدوار" (Roles)

- يعرّف الأدوار المفاهيمية التي سيملؤها الأثر التصوّري.
- الشكل العام داخل `أدوار`:

```bayan
أدوار: {
  RoleName: {kind: "...", optional: true/false, range: ...}
  ...
}
```

- أمثلة للحقول الممكنة:
  - `kind`: "entity" | "event" | "axis" | "value" | "context" | ...
  - `range`: مثل `[0,1]` أو مجموعة قيم رمزية.
  - `optional`: هل الدور اختياري؟

### 3.4 حقل "شروط" (Preconditions)

- يعبّر عن شروط عامة لتطبيق النمط على `conceptual_trace`.
- يمكن أن يكون:
  - حقول منطقية بسيطة (`requires_transform: true`).
  - أو تعبيرات منطقية أعلى (لاحقًا يمكن ربطها بقواعد في محرك المنطق).

مثال بسيط:

```bayan
شروط: {
  requires_transform: true
  require_axis_definition: true
}
```

### 3.5 حقل "بنية" (Abstract Structure)

- يصف شكل النمط المجرد كهيكل حقول:

```bayan
بنية: {
  entity:    Entity
  property:  PropertyAxis
  before:    BeforeValue
  after:     AfterValue
  delta:     AfterValue - BeforeValue
}
```

- يسمح بوجود تعبيرات مشتقّة (`AfterValue - BeforeValue`) تُفسَّر في طبقة التنفيذ.

### 3.6 حقل "خرائط_أثر" (Trace Mappings)

- يربط الأدوار بمسارات داخل `conceptual_trace`.
- الهدف: جعل تطبيق النمط آليًّا على أي أثر.

مثال:

```bayan
خرائط_أثر: {
  from_transforms: true
  entity_ref:   "transforms[k].entity_id"
  property_ref: "transforms[k].state_name"
  before_ref:   "transforms[k].before"
  after_ref:    "transforms[k].after"
}
```

### 3.7 حقل "قوالب_لغوية" (Language Hooks)

- يربط النمط بقوالب الجسر اللغوي المناسبة:

```bayan
قوالب_لغوية: [StateChangeSentencePattern, UncertaintyPattern]
```

- هذه الأسماء تشير إلى أنماط أخرى من نوع `LanguageBridgePattern` معرفة في نفس الـ DSL أو في مكتبة أخرى.

---

## 4. مثال ثانٍ: Basic_Cause_Effect

```bayan
تصور_عام Basic_Cause_Effect {
  نوع: CausalPattern

  أدوار: {
    CauseEvent:  {kind: "event"}
    EffectEvent: {kind: "event"}
    Strength:    {kind: "value", range: [0,1]}
  }

  شروط: {
    requires_causal_link: true
  }

  بنية: {
    cause:    CauseEvent
    effect:   EffectEvent
    strength: Strength
  }

  خرائط_أثر: {
    from_causal_network: true
    cause_ref:  "networks.causal[i].cause_event_id"
    effect_ref: "networks.causal[i].effect_event_id"
    strength_ref: "networks.causal[i].strength"
  }

  قوالب_لغوية: [CausalSentencePattern]
}
```

---

## 5. مثال لأنماط الجسر اللغوي في الـ DSL

### 5.1 ActionSentencePattern

```bayan
تصور_عام ActionSentencePattern {
  نوع: LanguageBridgePattern

  أدوار: {
    Actor:       {kind: "entity"}
    Action:      {kind: "event_type"}
    Target?:     {kind: "entity", optional: true}
    Context?:    {kind: "context", optional: true}
    Intensity?:  {kind: "value", range: [0,1], optional: true}
    Uncertainty?:{kind: "value", range: [0,1], optional: true}
  }

  شروط: {
    requires_event_pattern: "Generic_Interaction_Event"
  }

  بنية: {
    action_sentence: ActionSentence(Actor, Action, Target?, Context?, Intensity?, Uncertainty?)
  }

  خرائط_أثر: {
    from_event_pattern: "Generic_Interaction_Event"
  }

  قوالب_لغوية: []  # هذا النمط نفسه جسر لغوي
}
```

---

## 6. ملاحظات تنفيذية مستقبلية

1. **المفسّر/المحلّل**:
   - يمكن بناء وحدة في بايثون/بيان تقرأ هذه التعاريف وتحوّلها إلى
     هياكل بيانات (dictionaries / classes) تُستخدم أثناء التحليل والتوليد.

2. **التكامل مع conceptual_trace**:
   - تبني طبقة مطابقة (matcher) تقوم بـ:
     - استعراض الأثر.
     - التحقّق من الشروط.
     - ملء الأدوار تلقائيًا وفق `خرائط_أثر`.

3. **التوسع**:
   - يمكن لاحقًا إضافة حقول أخرى (مثل أولوية النمط، سياسات فض تعارض).

4. **ثنائية اللغة**:
   - يمكن توفير كلمات مفتاحية مكافئة بالإنجليزية (`concept_blueprint`, `roles`, `conditions`...)
     مع الحفاظ على نفس البنية المفاهيمية.

هذه المواصفة كافية كبداية لبناء DSL فعلية داخل بيان، وتظل منسجمة مع
رؤية الطبقة التصورية والمعمارية العامة للنموذج اللغوي التوليدي.

