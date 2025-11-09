# Entity System Guide — دليل نظام الكيانات

هذا الدليل يشرح نظام "الكيانات" المدمج في لغة بيان لإدارة الحالة (0..1) والتفاعلات بشكل مباشر من داخل اللغة، مع دعمٍ ثنائي اللغة (English + العربية).

---

## Keywords — الكلمات المفتاحية
- English: `entity`, `apply`, body keys: `states`, `properties`, `actions`, `reactions`
- العربية: `كيان`, `طبق`, مفاتيح الجسم: `"حالات"`, `"خصائص"`, `"أفعال"`, `"ردود_أفعال"`

ملاحظة: مفاتيح القواميس ينبغي أن تكون نصوصاً صريحة (strings) مثل `"states"` أو `"حالات"`.

افتراضياً القيم رقمية ضبابية ضمن [0.0 .. 1.0] ويتم قصّها تلقائياً؛ ويمكن تعريف أنواع اختيارية تجعل بعض القيم غير محدودة (numeric) أو ذات نطاق مخصص (bounded).

---

## Basic Syntax — البنية الأساسية

مثال عربي مختصر:

```bayan
hybrid {
    # تعريف كيانين
    كيان أحمد { "حالات": {"جوع": 0.6} }
    كيان محمد { "أفعال": {
        "تقديم_وجبة": {"قوة": 1.0, "تأثيرات": [ {"on": "جوع", "formula": "value - 0.4*action_value"} ] }
    }}

    # تطبيق فعل على هدف
    طبق محمد.تقديم_وجبة(أحمد, قيمة_الفعل=1.0)
}

# الاستعلام (خارج الكتلة) كي يكون هو النتيجة الراجعة من البرنامج
query state("أحمد", "جوع", ?V).
```

English variant:

```bayan
hybrid {
    entity Ahmed { "states": {"hunger": 0.6} }
    entity John  { "actions": {
        "feed": {"power": 1.0, "effects": [ {"on": "hunger", "formula": "value - 0.4*action_value"} ] }
    }}

    apply John.feed(Ahmed, action_value=1.0)
}

query state("Ahmed", "hunger", ?V).
```

---

## Entity Body — محتوى الكيان
يدعم المفاتيح التالية (باللغتين):
- states | "حالات": قاموس لحالات الكيان (0..1)
- properties | "خصائص": قاموس لخصائص شبه ثابتة (0..1)
- actions | "أفعال": أفعال يملكها الفاعل (Actor)
  - داخل كل فعل:
    - power | "قوة": رقم 0..1 يؤثر في شدة التأثير
    - effects | "تأثيرات": قائمة تأثيرات، كل تأثير كائن JSON-like:
      - on: مفتاح الحالة المتأثرة عند الهدف
      - formula: معادلة نصية مبسطة (ترى أدناه)
      - condition (اختياري): شرط تفعيل التأثير
- reactions | "ردود_أفعال": ردود فعل لدى الهدف عند استقبال فعل معيّن
  - sensitivity: حساسية (0..1)
  - response: تعبير بسيط من الشكل `STATE += expr` أو `STATE -= expr`

مثال مختصر لرد فعل:

```bayan
كيان أحمد { "حالات": {"سعادة": 0.5}, "ردود_أفعال": {
  "تقديم_وجبة": {"sensitivity": 0.7, "response": "سعادة += sensitivity*0.3"}
}}
```

---

## Effect Formula — معادلة التأثير الآمنة
داخل `formula` و`condition` تتوفر أسماء:
- `value` (القيمة الحالية للحالة)
- `action_value` (القيمة الممرّرة إلى apply)
- `power` (قوة الفعل)
- `sensitivity` (حساسية الهدف)

وتتوفر دوال: `min`, `max`, `clamp(x, lo, hi)`, `sqrt`, `abs`, `sin`, `cos`, `tan`, `exp`, `log`, `rand()`.

أمثلة:
- "value - 0.4*action_value"
- "clamp(value + power*0.2, 0, 1)"
- شرط: "value > 0.3"

افتراضياً تُقصّ نتائج التأثير إلى [0..1] (نوع fuzzy). إذا عرّفت نوع "numeric" فلن يُطبَّق قصّ، وإذا عرّفت نوعاً "bounded" فسيُقصّ إلى [min,max].


---

## Action-centric API — نمط «نفّذ/perform»
أحيانًا يكون من الأسهل التفكير بالفعل أولًا ثم من يشارك فيه. لهذا وفّرنا دالة مساعدة في البيئة العالمية:
- English: `perform(action_name, participants, states=None, properties=None, action_value=1.0)`
- العربية: `نفذ(اسم_الفعل, المشاركون, الحالات=None, الخصائص=None, قيمة_الفعل=1.0)`

المشاركون يمكن أن يُكتبوا بعدة صيغ:
- قائمة سلاسل نصية من الشكل `"Name.0.8"` أو `"Name:0.8"` (الرقم = درجة الاستجابة/الحساسية)
- قائمة ثنائيات: `[ ("Name", 0.8), ... ]`
- قاموس: `{ "Name": 0.8, ... }`

كما يمكن ضبط قيم أولية قبل تنفيذ الفعل عبر:
- states / "حالات": إسنادات من الشكل `[ ("Entity", "state", value), ... ]` أو `{ "Entity": {"state": value} }`
- properties / "خصائص": نفس البنية.

السلوك:
- إذا كان جميع المشاركين Actors (أي يملكون الفعل المُسمّى)، فكل واحد «ينفذ» على نفسه فقط.
- إذا وُجد مشاركون لا يملكون الفعل، فإن كل Actor يطبّق الفعل على جميع المشاركين (بمن فيهم نفسه)، وتُستخدم درجة استجابة الهدف كما جاءت في قائمة المشاركين.

مثال EN:
```bayan
hybrid {
  entity Ahmed { "properties": {"x": {"type": "numeric", "value": 0.0}},
                 "actions": {"go": {"effects": [{"on": "x", "formula": "value + 3*sensitivity"}]}} }
  entity Ali   { "properties": {"x": {"type": "numeric", "value": 1.0}} }

  perform("go", ["Ahmed.1.0", "Ali.0.5"])  # Ahmed affects himself and Ali
}

query property("Ahmed", "x", ?AX).
```

مثال AR:
```bayan
hybrid {
  كيان أحمد { "خصائص": {"س": {"نوع": "عددي", "قيمة": 0.0}},
              "أفعال": {"اذهب": {"تأثيرات": [{"on": "س", "formula": "value + 3*sensitivity"}]}} }
  كيان علي   { "خصائص": {"س": {"نوع": "عددي", "قيمة": 1.0}} }

  نفذ("اذهب", ["أحمد.1.0", "علي.0.5"])  # يطبّق أحمد على نفسه وعلى علي
}

query property("أحمد", "س", ?V).
```


### Groups and pronoun-like references — المجموعات ومرجع "last/هم"
للتيسير على بناء نماذج لغوية، يمكنك تعريف مجموعات وإعادة استخدام آخر مجموعة مشاركين:

- تعريف مجموعة (داخل hybrid باستخدام الدالة المساعدة):
  - EN: `define_group("Team", ["Ahmed", "Ali"])`
  - AR: `عرّف_مجموعة("الفريق", ["أحمد", "علي"])`
- استخدام المجموعة داخل المشاركين:
  - كسلسلة: `"group:Team.0.7"` أو العربية: `"مجموعة:الفريق.0.7"`
  - كثنائية: `("group:Team", 0.7)`
- إعادة استخدام آخر مشاركين: `"last"` أو العربية `"هم"`
  - يمكن تمرير درجة موحّدة: `"last:0.3"` أو `"last.0.3"`
- Synonyms (aliases) for last-reference:
  - EN pronouns: `they`, `them`, `he`, `she`, `it`
  - AR pronouns: `هم`, `هو`, `هي`, `هما`, `هن`
  - All treated as alias of "last"; degree suffix is supported via `:0.2` or `.0.2` (e.g., `they:0.2`, `هما.0.5`).

مثال EN:
```bayan
hybrid {
  entity Ahmed { "properties": {"x": {"type": "numeric", "value": 0.0}},
                 "actions": {"go": {"effects": [{"on": "x", "formula": "value + 2*sensitivity"}]}} }
  entity Ali   { "properties": {"x": {"type": "numeric", "value": 1.0}} }

  define_group("Team", ["Ahmed", "Ali"])    # Group definition
  perform("go", ["group:Team.0.5"])          # Apply to group members
  perform("go", ["they:0.2"])                # Reuse last via pronoun alias
}
```

مثال AR:
```bayan
hybrid {
  كيان أحمد { "خصائص": {"س": {"نوع": "عددي", "قيمة": 0.0}},
              "أفعال": {"اذهب": {"تأثيرات": [{"on": "س", "formula": "value + 2*sensitivity"}]}} }
  كيان علي   { "خصائص": {"س": {"نوع": "عددي", "قيمة": 1.0}} }

  عرّف_مجموعة("الفريق", ["أحمد", "علي"])
  نفذ("اذهب", ["مجموعة:الفريق.0.5"])
  نفذ("اذهب", ["هما.0.2"])                    # مرجع ضمير مكافئ لـ last
}
```


### Equations / Constraints — نظام المعادلات
اربط حالات/خصائص الكيان بمعادلات تُطبَّق تلقائيًا بعد أي تحديث.

- EN helpers:
  - `define_equation(entity, scope, key, expr)` where `scope` is `state` or `property`
  - `equation_state(entity, key, expr)` / `equation_property(entity, key, expr)`
  - `define_complement(entity, scope, base_key, complement_key, total=1.0)` adds `complement_key = total - base_key`
  - `define_opposites(entity, scope, key_a, key_b, total=1.0)` adds both: `A = total - B` and `B = total - A`
- AR helpers:
  - `عرّف_معادلة(الكيان, "حالة|خاصية", المفتاح, "التعبير")`
  - `معادلة_حالة(...)` / `معادلة_خاصية(...)`
  - `عرّف_متمم(الكيان, "حالة|خاصية", الأساس, المتمم, المجموع=1.0)`
  - `عرّف_أضداد(الكيان, "حالة|خاصية", أ, ب, المجموع=1.0)` يضيف العلاقتين المتقابلتين.

Notes:

---

## Linguistic Templates — القوالب اللغوية (صفات/ألقاب/إضافة/ملكية)
لخدمة التعبير العربي والإنجليزي، وفرنا دوالاً مساعدة تُحوّل العبارات الشائعة إلى حقائق منطقية جاهزة للاستعلام:

- EN helpers:
  - `assert_is(subject, klass)` + alias `isa(...)` + unary `klass(subject)`
  - `assert_attrs(subject, ["generous", "brave:0.7"])`  → `attribute(subject, adj)` و `attribute(subject, adj, degree)` و `adj(subject)`
  - `assert_of(head, genitive)`  → `of(head, genitive)` + `genitive(...)` (+ `from(...)` للاستعمال البرمجي)
  - `assert_belongs(thing, owner)` → `belongs_to(thing, owner)` + `owner_of(owner, thing)`
  - `phrase("Mohammad the_doctor", relation="isa")`, `phrase("juice grapes", relation="of")`, `phrase("owner house", relation="belongs")`
- AR helpers:
  - `أثبت_يكون(الموضوع, الفئة)` + `يكون(...)` + مسند أحادي `الفئة(الموضوع)`
  - `أثبت_صفات("محمد", ["كريم", "شجاع:0.3"])`
  - `أثبت_إضافة(المضاف, المضاف_إليه)`
  - `أثبت_يعود(المملوك, المالك)`، ومرادفات `يعود(...)`
  - `عبارة("محمد الطبيب", relation="isa")`، `عبارة("عصير العنب", relation="of")`، `عبارة("مالك البيت", relation="belongs")`

ملاحظات:
- اللاحقة العددية للصفة تقبل `:0.7` أو `.0.7` (مثل `كريم:0.8`).
- `phrase/عبارة` يدعم خيار `strip_definite=True` افتراضيًا لإزالة "ال" من بداية الكلمات العربية الثانية الأكثر شيوعًا:
  - مثال: `عبارة("مالك البيت", relation="belongs")` → `belongs_to("بيت", "مالك")` و `owner_of("مالك", "بيت")`.

أمثلة سريعة (AR):
```bayan
hybrid {
  أثبت_صفات("محمد", ["كريم", "حكيم", "شجاع:0.4"])     # attribute + درجات
  أثبت_يكون("محمد", "طبيب")                           # isa + مسند أحادي: طبيب("محمد")
  أثبت_إضافة("عصير", "العنب")                         # of/genitive
  أثبت_يعود("البيت", "المالك")                         # belongs_to + owner_of
  عبارة("محمد الطبيب", relation="isa")
  عبارة("عصير العنب", relation="of")
}
```

راجع الأمثلة: `examples/phrases_ar.by`, `examples/phrases_en.by`.

### Grammar sugar in parser — سكر نحوي للعبارات الاسمية
يمكنك الآن كتابة العبارات الاسمية مباشرة داخل كتلة hybrid، بشرط إنهائها بنقطة:

```bayan
hybrid {
  محمد الطبيب.
  عصير العنب[of].       # [علاقة] اختيارية بين معقوفين: isa|of|belongs أو اسم قالب مخصص
  مالك البيت[belongs].   # belongs تُفسَّر افتراضياً بترتيب BA → belongs_to("بيت", "مالك")
}
```

### Programmable templates — قوالب قابلة للبرمجة
لتمكين التخصيص، وفرنا واجهات لتعريف قوالب واختصارات رءوس:
- EN:
  - `define_nominal_template(name, relation, order='AB', strip_definite=True)`
  - `define_head_template(head, template_or_relation, order='AB')`
- AR:
  - `عرّف_قالب_عبارة(الاسم, العلاقة, order='AB', strip_definite=True)`
  - `عرّف_قالب_رأس(الرأس, القالب_أو_العلاقة, order='AB')`

أمثلة سريعة:
```bayan
hybrid {
  define_nominal_template("ملك", relation="belongs", order="BA")
  مالك البيت[ملك].              # يستخدم القالب

  define_head_template("مالك", "belongs", order="BA")
  مالك البيت.                   # بدون معقوفات بفضل تلميح الرأس
}
```
### Built-in head hints — تلميحات رءوس جاهزة
لتيسير الاستخدام مباشرة دون تعريف قوالب، تتوفر تلميحات افتراضية للرءوس الشائعة (يمكن تجاوزها بتعريفاتك):
- مالك / owner → belongs (order=BA)
- صاحب → belongs (order=BA)
- عصير / juice → of (order=AB)
- باب / door → of (order=AB)
- صورة / picture → of (order=AB)
- كاتب / writer → of (order=AB)
- مدير / manager → of (order=AB)
- رئيس → of (order=AB)
- مؤلف / author → of (order=AB)
- كتاب / book → of (order=AB)
- صورة فوتوغرافية / photo → of (order=AB)



- استخدم أسماء المفاتيح كمتغيرات داخل التعبير (تُسمح معرفات عربية/إنجليزية)
- تُفرض المعادلات بعد أي `set_state`/`set_property` أو تأثير فعل

مثال AR:
```bayan
hybrid {
  كيان الطقس { "حالات": {"حر": {"نوع": "ضبابي", "قيمة": 0.0}, "برد": {"نوع": "ضبابي", "قيمة": 1.0}} }
  عرّف_أضداد("الطقس", "حالة", "حر", "برد", 1.0)
  عين_حالة("الطقس", "برد", 0.2)
}
query state("الطقس", "حر", ?H).
```
مثال EN:
```bayan
hybrid {
  entity Light { "properties": {"on": {"type": "fuzzy", "value": 0.0}, "off": {"type": "fuzzy", "value": 1.0}} }
  define_opposites("Light", "property", "on", "off", 1.0)
  set_property("Light", "off", 0.3)
}
query property("Light", "on", ?V).
```


### Event History — سجل الأحداث
لتيسير التعليل الزمني وبناء بيانات تدريبية، يسجّل محرك الكيانات كل تطبيق لفعل كحدث في `engine.events` ويعرض دوالاً مساعدة:
- EN: `events(actor=None, action=None, target=None)`, `clear_events()`, `last_participants()`, `event_texts(lang='en')` / `describe_events(lang='en')`
- AR: `الأحداث(...)`, `سجل_الأحداث(...)` (مرادف)، `امسح_الأحداث()`, `آخر_مشاركين()`, `نص_الأحداث('ar')` / `وصف_الأحداث('ar')`

شكل كل حدث:
```python
{
  'actor': 'Ahmed', 'action': 'go', 'target': 'Ali',
  'value': 1.0, 'power': 1.0, 'sensitivity': 0.5,
  'changes': [{'key': 'x', 'old': 1.0, 'new': 2.0}, ...],
  'summary_en': 'Ahmed -> go -> Ali (value=1.0, power=1.0, sensitivity=0.5)',
  'summary_ar': 'Ahmed -> go -> Ali (قيمة=1.0، قدرة=1.0، حساسية=0.5)'
}
```

مثال مختصر:
```bayan
hybrid {
  entity Ahmed { "properties": {"x": {"type": "numeric", "value": 0.0}},
                 "actions": {"go": {"effects": [{"on": "x", "formula": "value + 2*sensitivity"}]}} }
  entity Ali   { "properties": {"x": {"type": "numeric", "value": 1.0}} }

  perform("go", ["Ahmed.1.0", "Ali.0.5"])
  # لاحقًا يمكنك استرجاع السجل نصيًا عبر describe_events('en') / نص_الأحداث('ar')
}
```


### Linguistic Operators — مشغلات لغوية (Wrappers)
Wrappers that call the action-centric engine with conventional names; useful for readability and LLM training data.

- English: `Go(participants, states=None, properties=None, value=1.0)`, `Affect(...)`, `Consume(...)`, `Bond(...)`, `Transform(...)`
- العربية: `اذهب(...)`, `أثّر(...)`, `أكل(...)`, `اربط(...)`, `حوّل(...)`

Note: These wrappers are thin aliases over `perform("<verb>", participants, ...)`. The verb must have an action/effects defined on the target entities to induce change, or pair with state/property setters where appropriate.

Example (EN):
```bayan
hybrid {
  entity Ahmed { "properties": {"x": {"type": "numeric", "value": 0.0}},
                 "actions": {"go": {"effects": [{"on": "x", "formula": "value + 3*sensitivity"}]}} }
  Go(["Ahmed.0.5"])  # x += 1.5
}
```
Example (AR):
```bayan
hybrid {
  كيان أحمد { "خصائص": {"س": {"نوع": "عددي", "قيمة": 0.0}},
              "أفعال": {"اذهب": {"تأثيرات": [{"on": "س", "formula": "value + 2*sensitivity"}]}} }
  اذهب(["أحمد.0.5"])  # س += 1.0
}
```

#### Defining custom operators — تعريف مشغلات مخصّصة
Programmers can define their own operator names at runtime as thin wrappers over `perform`.
- EN: `define_operator(name, action=None, alias=None)`
- AR: `عرّف_مشغل(الاسم، action=None، alias=None)`

Notes:
- If `action` is omitted, the operator name itself is used as the action verb.
- `alias` adds a second callable name pointing to the same operator.

Example (EN):
```bayan
hybrid {
  entity Pusher { "properties": {"x": {"type":"numeric","value":0.0}},
                  "actions": {"go": {"effects":[{"on":"x","formula":"value + sensitivity"}]}} }
  define_operator("Push", action="go")
  Push(["Pusher:1.0"])
}
```
Example (AR):
```bayan
hybrid {
  كيان دافع { "خصائص": {"س": {"نوع":"عددي","قيمة":0.0}},
              "أفعال": {"اذهب": {"تأثيرات":[{"on":"س","formula":"value + sensitivity"}]}} }
  عرّف_مشغل("ادفع", action="اذهب")
  ادفع(["دافع:1.0"])
}
```


---
## Property/State Types (Optional) — أنواع الخصائص/الحالات (اختياري)
By default all values are fuzzy [0..1]. You can opt into other kinds per key:
- fuzzy (default): clamped to [0..1]
- numeric: unbounded real numbers (e.g., coordinates x,y)
- bounded[min,max]: custom range (e.g., temperature)

Use a typed entry with a small object: {"type": ..., "value": ...}. Arabic keys are accepted: "نوع" و"قيمة".

Example (EN):

```bayan
hybrid {
  entity Ball {
    "properties": {
      "x": {"type": "numeric", "value": 10.5},
      "y": {"type": "numeric", "value": -3.2}
    },
    "states": {
      "energy": {"type": "fuzzy", "value": 0.7},
      "temperature": {"type": {"bounded": [-273.0, 1000.0]}, "value": 25.0}
    }
  }
}
```

مثال (AR):

```bayan
hybrid {
  كيان كرة {
    "خصائص": {
      "س": {"نوع": "عددي", "قيمة": 10.5},
      "ص": {"نوع": "عددي", "قيمة": -3.2}
    },
    "حالات": {
      "طاقة": {"نوع": "ضبابي", "قيمة": 0.7},
      "درجة_الحرارة": {"نوع": {"نطاق": [-273.0, 1000.0]}, "قيمة": 25.0}
    }
  }
}
```

Runtime behavior — السلوك أثناء التنفيذ:
- fuzzy: values auto-clamped to [0..1]
- numeric: no clamping
- bounded: auto-clamped to [min,max]


## Logic Integration — التكامل مع المنطق
محرك الكيانات يزامن الحقائق التالية مع قاعدة المعرفة المنطقية:
- `entity(Name).`
- `state(Entity, Key, Value).`
- `property(Entity, Key, Value).`
- `event(Actor, Action, Target, ActionValue).`
- `changed(Target, Key, Old, New).`

لذلك يمكنك الاستعلام مباشرةً:

```bayan
query state("Ahmed", "hunger", ?V).
```

---

## Best Practices — أفضل الممارسات
- استخدم أسماء حالات وخصائص واضحة ودلالية.
- عرّف التأثيرات بصيغ بسيطة قابلة للتحقق.
- ضع الاستعلامات خارج كتلة `hybrid {}` إذا أردت أن تكون النتيجة النهائية للبرنامج.
- استعمل مفاتيح نصية صريحة في القواميس: "states"/"حالات" إلخ.
- اختبر تفاعلاتك تدريجياً، وتحقق من حقائق `changed/4` و`event/4` لتتبع الأثر.

---

## Notes — ملاحظات
- الكلمات المفتاحية ثنائية اللغة: `entity` ⇄ `كيان`، و`apply` ⇄ `طبق`.
- أسماء الكيانات والأفعال يمكن أن تكون عربية بالكامل (مسموح كمعرفات).
- القيم ضبابية ضمن [0..1] ويتم قصّها تلقائياً.

