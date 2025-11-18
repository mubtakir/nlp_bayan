# مرجع لغة بيان (Bayan Language Reference)

هذا المرجع يعرّف نحويات وسلوكيات لغة "بيان" بدقة عملية، كما هي في المفسر والاختبارات الحالية.
اللغة هجينة: تقليدية (إجرائية/كائنية) + منطقية (Prolog-like) مع تكامل مع بايثون.

المحتويات (Contents)
- Lexical structure: المحارف، المعرّفات، الكلمات المحجوزة، الرموز
- Literals: الأعداد، النصوص، القوائم، القواميس
- Expressions: الوصول، الاستدعاء، الفهرسة، العوامل وأسبقيتها
- Statements: الإسناد، الكتل، if/elif/else، for، while، return، print
- Functions: التعريف، المعاملات، الاستدعاء
- Classes & Objects: التعريف، الوراثة (C3 MRO)، super()
- Special methods (dunder): السلوك الزائد (العمليات/الحاويات/الاستدعاء)
- Truthiness, Iteration, Membership
- Import System: وحدات بيان + بايثون
- Hybrid Logic: facts, rules (:-/←), queries, ?vars
- Errors & Debugging: Bayan stack، code frames، ألوان اختيارية، اقتراحات "هل تقصد؟"

---

## Lexical structure

- المعرّفات (Identifiers):
  - النمط: `[a-zA-Z_\u0600-\u06FF][a-zA-Z0-9_\u0600-\u06FF]*`
  - تدعم العربية واللاتينية والأرقام والشرطة السفلية.
- التعليقات: تبدأ بـ `#` حتى نهاية السطر.
- المسافات البيضاء: الفراغ، التاب، الإرجاع؛ والسطر الجديد `\n` يزيد عداد الأسطر.

### الكلمات المحجوزة (Keywords)

#### الكلمات التقليدية (Traditional Keywords):
`def`, `class`, `if`, `elif`, `else`, `for`, `while`, `in`, `print`, `return`, `break`, `continue`, `pass`, `True`, `False`, `None`, `and`, `or`, `not`, `self`, `super`, `import`, `from`, `as`, `try`, `except`, `finally`, `raise`, `with`, `async`, `await`, `yield`, `lambda`, `global`, `del`

#### الكلمات الهجينة/المنطقية (Hybrid/Logic Keywords):
`hybrid`, `query`, `fact`, `rule`

#### نظام السببية والدلالة (Causal-Semantic System): ⭐ جديد
- `cause_effect` / `سبب_نتيجة` - تعريف قانون سببي مع السبب الفيزيائي/المنطقي
- `relation` / `علاقة` - تعريف علاقة دلالية بين مفاهيم

**أمثلة:**
```bayan
hybrid {
    # قانون سببي: سبب_نتيجة(شرط, نتيجة, سبب, قوة)
    سبب_نتيجة("رفع_شيء_لفوق", "يسقط", "جاذبية", 1.0).

    # علاقة دلالية: علاقة(من, نوع_العلاقة, إلى, قوة)
    علاقة("الاستحمام", "في", "حمام", 0.9).

    # استعلام
    query سبب_نتيجة(?شرط, "يسقط", ?سبب, ?قوة).
}
```

#### نظام الكيانات (Entity System):
- `entity` / `كيان` - تعريف كيان
- `apply` / `طبق` - تطبيق فعل على كيان
- `concept` / `مفهوم` - تعريف مفهوم

#### الكلمات الزمنية (Temporal Keywords):
- `temporal` / `زمنيا` - كتلة زمنية
- `first` / `أولا` - الخطوة الأولى
- `then` / `ثم` - الخطوة التالية
- `lastly` / `أخيرا` - الخطوة الأخيرة
- `within` / `خلال` - خلال مدة زمنية
- `schedule` / `جدولة` - جدولة
- `delay` / `تأخير` - تأخير
- `every` / `كل` - كل (للتكرار)
- `seconds` / `ثانية` / `ثواني` - ثواني
- `minutes` / `دقيقة` / `دقائق` - دقائق
- `hours` / `ساعة` / `ساعات` - ساعات
- `once` / `مرة_واحدة` - مرة واحدة فقط
- `limit` / `حد` - حد أقصى

#### كلمات القيود (Constraint Keywords):
- `where` / `حيث` - شرط where
- `requires` / `يتطلب` / `يشترط` - شرط مسبق (precondition)
- `ensures` / `يضمن` / `يكفل` - شرط لاحق (postcondition)
- `invariant` / `ثابت` / `ثوابت` - ثابت (invariant)

#### كلمات مطابقة الأنماط (Pattern Matching Keywords):
- `match` / `طابق` - جملة match
- `case` / `حالة` - حالة case
- `default` / `افتراضي` / `افتراضية` - الحالة الافتراضية
- `when` / `عندما` - شرط guard

#### كلمات البرمجة التفاعلية (Reactive Programming Keywords):
- `reactive` / `تفاعلي` / `تفاعلية` - متغير تفاعلي
- `watch` / `راقب` / `مراقبة` - كتلة مراقبة
- `computed` / `محسوب` / `محسوبة` - خاصية محسوبة

#### كلمات النموذج المعرفي-الدلالي (Cognitive-Semantic Model Keywords):
- `cognitive_entity` / `كيان_معرفي` - كيان معرفي
- `cognitive_event` / `حدث_معرفي` - حدث معرفي
- `event` / `حدث` - حدث عام
- `trigger` / `أطلق` - إطلاق حدث
- `concurrent` / `متزامن` - أحداث متزامنة
- `pattern` / `قالب` - قالب لغوي
- `conceptual_blueprint` / `مخطط_مفاهيمي` - مخطط مفاهيمي
- `idea` / `فكرة` - فكرة
- `participants` / `مشاركون` - مشاركون
- `strength` / `قوة` - قوة
- `transform` / `تحويل` - تحويل
- `reactions` / `ردود_فعل` / `ردود` - ردود فعل
- `structure` / `بنية` - بنية
- `express` / `تعبير` - تعبير
- `entities` / `كيانات` - كيانات
- `result` / `نتيجة` - نتيجة
- `state_changes` / `تغييرات_الحالة` / `تغييرات` - تغييرات الحالة
- `linguistic_forms` / `أشكال_لغوية` / `أشكال` - أشكال لغوية
- `degree` / `درجة` - درجة
- `role` / `دور` - دور

#### كلمات البرمجة الدلالية وإدارة المعرفة (Semantic Programming & Knowledge Management):
- `meaning` / `معنى` - معنى دلالي
- `semantic_query` / `استعلام_دلالي` - استعلام دلالي
- `information` / `معلومة` - معلومة
- `content` / `محتوى` - محتوى
- `context` / `سياق` - سياق
- `time` / `زمن` - زمن
- `place` / `مكان` - مكان
- `source` / `مصدر` - مصدر
- `certainty` / `يقين` - يقين
- `inference_rule` / `قاعدة_استنتاج` - قاعدة استنتاج
- `infer_from` / `استنتج_من` - استنتج من
- `contradiction` / `تناقض` - تناقض
- `between` / `بين` - بين
- `resolve` / `حل` - حل
- `evolving_knowledge` / `معرفة_متطورة` - معرفة متطورة
- `knowledge` / `معرفة` - معرفة
- `current_value` / `قيمة_حالية` - قيمة حالية
- `history` / `تاريخ` - تاريخ
- `future_prediction` / `توقع_مستقبلي` - توقع مستقبلي
- `ontology` / `أنطولوجيا` - أنطولوجيا
- `root` / `جذر` - جذر
- `taxonomy` / `تصنيف` - تصنيف
- `memory` / `ذاكرة` - ذاكرة
- `store` / `خزن` - تخزين
- `retrieve` / `استرجع` - استرجاع
- `similarity` / `تشابه` - تشابه
- `narrative` / `سرد` - سرد
- `characters` / `شخصيات` - شخصيات
- `generate_narrative` / `ولد_سرد` - توليد سرد
- `based_on` / `بناء_على` - بناءً على
- `current_context` / `السياق_الحالي` - السياق الحالي

#### كلمات النموذج الوجودي (Existential Model Keywords):
- `domain` / `مجال` - مجال وجودي
- `basic_entity` / `كيان_أساسي` - كيان أساسي
- `environment` / `بيئة` - بيئة
- `in_domain` / `في_مجال` - في مجال
- `of_type` / `من_نوع` - من نوع
- `existential_being` / `كائن_وجودي` - كائن وجودي
- `dimensions` / `أبعاد` - أبعاد
- `spatial` / `مكاني` - مكاني
- `domain_specific` / `خاص_بالمجال` - خاص بالمجال
- `intrinsic_properties` / `خصائص_جوهرية` - خصائص جوهرية
- `inherited_meanings` / `معاني_موروثة` - معاني موروثة
- `intrinsic_meanings` / `معاني_جوهرية` - معاني جوهرية
- `laws` / `قوانين` - قوانين
- `domain_relation` / `علاقة_مجالية` - علاقة مجالية
- `domain_action` / `فعل_مجالي` - فعل مجالي
- `metaphorical_meaning` / `معنى_مجازي` - معنى مجازي
- `built_on` / `مبني_على` - مبني على
- `applies_to` / `ينطبق_على` - ينطبق على
- `domain_law` / `قانون_مجالي` - قانون مجالي
- `existential_query` / `استعلام_وجودي` - استعلام وجودي
- `about` / `حول` - حول

#### الاتجاهات المكانية (Spatial Directions):
`above` / `فوق`, `below` / `تحت`, `right` / `يمين`, `left` / `يسار`, `front` / `أمام`, `back` / `خلف`, `north` / `شمال`, `south` / `جنوب`, `east` / `شرق`, `west` / `غرب`

#### العلاقات الزمنية (Temporal Relations):
`before` / `قبل`, `after` / `بعد`, `during` / `أثناء`, `now` / `الآن`

#### حروف الجر (Prepositions):
`in` / `في`, `from` / `من`, `at` / `عند`, `on` / `على`, `to` / `إلى`

#### كلمات مجال الحياة (Life Domain Keywords):
`emergence` / `ظهور`, `life` / `حياة`, `growth` / `نمو`, `death` / `موت`, `decay` / `تحلل`, `living` / `حي`, `eat` / `أكل`, `drink` / `شرب`, `food` / `طعام`, `satiety` / `شبع`, `hunger` / `جوع`, `work` / `عمل`, `pain` / `ألم`, `effect` / `تأثير`, `affected` / `متأثر`, `struggle` / `كفاح`, `gain` / `كسب`, `loss` / `خسارة`, `interior` / `داخل`, `face` / `وجه`, `shadow` / `ظل`, `love` / `حب`, `affection` / `مودة`, `aversion` / `نفور`, `proximity` / `قرب`, `cooperation` / `تعاون`, `interaction` / `تفاعل`, `product` / `منتج`, `laugh` / `ضحك`, `cry` / `بكاء`, `speak` / `كلام`, `think` / `تفكير`, `inhabits` / `يسكن`, `moves_to` / `ينتقل_إلى`, `affected_by` / `متأثر_بـ`

#### ملاحظات:
- اللغة تدعم ثنائية اللغة (عربي/إنجليزي) لمعظم الكلمات المفتاحية
- بعض الكلمات لها مترادفات متعددة (مثل `lastly`/`أخيرا`, `finally` محجوزة لـ try/finally)
- الكلمات الجديدة تدعم ميزات متقدمة: Temporal, Reactive, Cognitive-Semantic, Existential Model


### الرموز (Symbols)
- أقواس: `() { } [ ]`
- فواصل: `, ; : .`
- إسناد: `=`
- عوامل مقارنة: `== != < <= > >=`
- عوامل حسابية: `+ - * / %`
- ضمن المنطق: `:-` أو السهم `←` بين الرأس والجسم في القواعد

## Literals
- Number: صحيحة أو عشرية (مثل `42`, `3.14`).
- String: محصورة بعلامات اقتباس مفردة `'...'` أو مزدوجة "..." (لا يوجد هروب معقد حالياً).
- List: `[expr, ...]`
- Dict: `{ key: value, ... }` حيث `key` و`value` تعبيرات بيان (قد تكون أعداداً أو نصوصاً أو غيرها).

## Expressions

### الوصول والسلاسل (Chaining)
- الوصول إلى خاصية: `expr.attr`
- الفهرسة: `expr[index]`
- الاستدعاء: `fn(args)` أو `obj.method(args)`
- يمكن السلسلة: `fn(...).attr[idx].method(...).other`.

### self و super
- `self` يُشير إلى الكائن الحالي داخل طرق الأصناف.
- `super` مدعوم بصيغتين:
  - `super().method(args)`
  - الصيغة القديمة: `super(method[, args])`

### المنطق البسيط
- المتغير المنطقي يبدأ بـ `?` مثل `?X` ويُستخدم داخل المنطق الهجين.

### العوامل وأسبقيتها (من الأعلى إلى الأدنى تقريباً)
1) أحادية: `not`, و`-` الأحادي
2) ضرب/قسمة/باقي: `* / %`
3) جمع/طرح: `+ -`
4) المقارنات: `== != < <= > >= in`
5) المنطق: `and` ثم `or`
- التقييم يسار→يمين لكل مستوى.

## Statements

### الكتل (Blocks)
- تُكتب الكتل بين أقواس معقوفة `{ ... }` مسبوقة بنقطتين `:` بعد رأس البنية.

### الإسناد (Assignment)
- بسيط: `name = expr`
- خصائص: `obj.attr = expr`
- فهرسة: `obj[index] = expr`
- سلاسل الأهداف مدعومة: `obj.attr[idx] = expr`

### التحكم (Control)
- if/elif/else:
  ```bayan
  if cond:
  {
      ...
  }
  elif other:
  {
      ...
  }
  else:
  {
      ...
  }
  ```
- for-in (أي قابل للتكرار):
  ```bayan
  for x in iterable:
  {
      ...
  }
  ```
- while، و`break`/`continue` داخل الحلقات.
- return من داخل الدوال: `return expr` (أو بلا قيمة).
- print: `print(expr)`.

## Functions
- التعريف:
  ```bayan
  def name(a, b):
  {
      return a + b
  }
  ```
- الاستدعاء: `name(1, 2)`.
- المعاملات: لائحة معرّفات؛ لا توجد قيم افتراضية/أسماء مسماة حالياً.

## Classes & Objects
- التعريف:
  ```bayan
  class C:
  {
      def __init__(): { self.x = 0 }
      def get(): { return self.x }
  }
  ```
  - لا تمرير صريح لـ `self` في قائمة المعاملات؛ الكلمة `self` متاحة ضمن جسم الطريقة.
- الوراثة:
  - مفردة: `class D(C): { ... }`
  - متعددة: `class E(A, B): { ... }` (حساب الترتيب عبر C3 MRO).
- super():
  - `super().method(args)` أو `super(method, args)`
- إنشاء الكائنات: `c = C()`

### حلّ الطرق (Method Resolution)
- يتبع ترتيب C3 MRO للأصناف المتعددة.
- أثناء `super()`, يُستخدم سياق المالك (owner stack) لضمان تخطي طريقة الصنف الحالي.

## Special methods (dunder)
- حسابية/مقارنات: `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__mod__`,
  `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, وأحادي `__neg__`.
- نصّي: `__repr__` (تُستدعى في `repr(x)`).
- منطقية/طول: `__bool__`, `__len__` (تؤثّر على if/while/not).
- فهارس: `__getitem__`, `__setitem__`.
- عضوية: `__contains__` لاستعمال `x in y`.
- تكرار: `__iter__` (يجب أن يعيد قابلاً للتكرار).
- قابل للاستدعاء: `__call__` (جعل الكائن يُستدعى كدالة).

ملاحظات:
- عند تنفيذ عامل ثنائي على كائنات "بيان"، يحاول المفسّر استدعاء الدوال السحرية أولاً؛ وإلا يعود لسلوك بايثون عند الإمكان.

## Truthiness, Iteration, Membership
- الحقيقة (if/while/not):
  - إن كان الكائن من نوع بيان ويمتلك `__bool__` تُستدعى وتُحوَّل لِـ bool.
  - وإلا إن امتلك `__len__` تُستدعى ويُستنبط منها bool.
  - وإلا فالحقيقة الافتراضية `True` لكائنات بيان.
- التكرار: إذا امتلك الكائن `__iter__`، يُستخدم في `for`.
- العضوية: `x in y` يستدعي `y.__contains__(x)` إن وُجدت.

## Import System
- الصيَغ:
  - `import pkg.module [as alias]`
  - `from pkg.module import name[, name]*`
- وحدات بيان (`.bayan` ثم `.by`) تُحمَّل أولاً؛ وعند عدم العثور، يُحاوَل استيراد بايثون الآمن.
- المسارات الافتراضية للبحث عن وحدات بيان (نسخة حالية):
  - مجلد العمل الحالي (cwd)
  - `tests/`
  - `tests/bayan_modules/`
- التخزين المؤقت: تُحفظ الوحدات المحمّلة في ذاكرة مؤقتة لمنع التحميل المتكرر.
- `import m` يُعيد وكيلاً (proxy) يتيح الوصول إلى الأصناف/الدوال/المتغيرات المعرّفة في الوحدة.
- `from m import Name` ينسخ التعريفات المحددة إلى بيئة المفسر الحالية (أصناف/دوال/متغيرات).

## Hybrid Logic
- داخل كتلة `hybrid { ... }` يمكنك خلط التصريحات التقليدية مع حقائق/قواعد/استعلامات منطقية.
- حقائق (facts) تنتهي بنقطة: `fact parent(Ali, Omar).`
- قواعد (rules): `rule head(X) :- body1(X), body2(X).` أو `head(X) ← body1(X), body2(X).`
- استعلام (query): `query parent(Ali, ?Who).`
- المتغيرات المنطقية تبدأ بـ `?` مثل `?X`.

### تصريح المترادفات (Similarity Declarations)
- الصيغة: `Head(term:score, term:score, ...)`
- المواضع المسموحة:
  - كتعبير مستقل في المستوى الأعلى.
  - داخل كتل hybrid كتعليمة منطقية (ويُفضَّل إنهاؤها بنقطة `.` مثل الحقائق).
- الدلالة: تُولَّد حقائق `similar(Head, Term, Score, "syn", "lexicon")` ويُولَّد العكس تلقائيًا لتحقيق التماثل.
- الدرجة `score` عددية ويجب كتابتها صراحة (قرار تصميـمي مقصود).
- أمثلة:
  ```bayan
  أسد(غضنفر:0.8, هيضم:0.5)
  hybrid { ذهب(راح:0.8). }
  ```


## Errors & Debugging
- عند حدوث استثناء، يُغلّف برسالة تتضمن:
  - رأس الاستثناء الأصلي وسببُه.
  - تتبع Bayan stack بشكل `NodeType@file:line:col -> ...`.
  - إطار الشفرة (code frame) مع ترقيم الأسطر وسهم ^ عند العمود.
- تفعيل إطار الشفرة:
  - مرّر المصدر والاسم إلى المفسر: `set_source(code, filename="file.by")`.
  - إعدادات المخرجات:
    - `set_error_formatting(colors=True|False, context_lines=N, tabstop=M)`
    - colors: ANSI ألوان اختيارية (يُجمّل العناوين والسطر الحالي والمؤشر).
    - context_lines: عدد أسطر السياق قبل/بعد السطر الخاطئ.
    - tabstop: لضبط محاذاة السهم مع التبوّيب والمحارف واسعة العرض.
- اقتراحات "هل تقصد؟": عند اسم غير معرّف، تُقاس مسافة Levenshtein مقابل رموز البيئة الحالية
  (المحلية/العامة + أسماء الدوال + أسماء الأصناف) ويُقترح حتى 3 أقرب تطابقات.

## Grammar sketch (غير صارمة، للتوضيح)

```
program        := statement*
statement      := hybrid_block | def | class | if | for | while | return | print |
                  import | from_import | assignment | expr | similarity_decl_stmt
hybrid_block   := 'hybrid' '{' (traditional_stmt|logic_stmt)* '}'
logic_stmt     := fact_stmt | rule_stmt | query_stmt | similarity_decl_stmt
fact_stmt      := ('fact')? predicate '.'
rule_stmt      := ('rule')? predicate (':-'|'←') predicate (',' predicate)* '.'?
query_stmt     := 'query' predicate '.'?
similarity_decl_stmt := IDENT '(' pair (',' pair)* ')' '.'?
pair           := (IDENT | STRING) ':' expr

predicate      := IDENT '(' (logic_term (',' logic_term)*)? ')'
logic_term     := VARIABLE | STRING | NUMBER | IDENT

block          := '{' statement* '}'
assignment     := target '=' expr
target         := IDENT ('.' IDENT | '[' expr ']')*
expr           := or_expr
or_expr        := and_expr ('or' and_expr)*
and_expr       := cmp_expr ('and' cmp_expr)*
cmp_expr       := add_expr ((OP| 'in') add_expr)*
add_expr       := mul_expr ((+|-) mul_expr)*
mul_expr       := unary_expr ((*|/|%) unary_expr)*
unary_expr     := ('not' | '-') unary_expr | primary
primary        := NUMBER | STRING | True | False | None |
                  IDENT call_or_chain? |
                  self chain? |
                  super_call |
                  '[' ... ']' | '{' ... '}' |
                  '(' expr ')' chain?
call_or_chain  := '(' args ')' chain?
chain          := ('.' IDENT call? | '[' expr ']')*
call           := '(' args ')'
args           := (expr (',' expr)*)?
```


### إضافات نحو نظام الكيانات (غير صارمة)
```
# Statements (إضافة جديدة):
statement      := ... | entity_stmt | apply_stmt

entity_stmt    := ('entity'|'كيان') IDENT '{' dict '}'
apply_stmt     := ('apply'|'طبق') IDENT '.' IDENT '(' args ')'
```

- يدعم جسم `entity` مفاتيح القواميس الثنائية اللغة: `states/حالات`, `properties/خصائص`, `actions/أفعال`, `reactions/ردود_أفعال`.
- `apply` يمرر `action_value`/`قيمة_الفعل` اختيارياً.
- يُزاوِج محرك الكيانات حقائق runtime: `entity/1`, `state/3`, `property/3`, `event/4`, `changed/4`.


## اختلافات عن بايثون (ملحوظات)
- بنية الكتل ليست بالمسافة البادئة بل بأقواس `{}` مع `:`.
- لا يُمرَّر `self` كمعامل صريح؛ الكلمة `self` متاحة ضمن الطريقة.
- دعم المنطق الهجين داخل `hybrid {}` مع حقائق/قواعد/استعلامات.
- تحميل الوحدات: وحدات بيان أولاً ثم بايثون.


---

## جداول الأسبقيات والربط (تفصيلي)

| المستوى (من الأعلى) | العوامل                         | الربط (Associativity) |
|---------------------|----------------------------------|-----------------------|
| أحادي               | `not`, أحادي `-`                | يمين → يسار           |
| ضرب/قسمة/باقي       | `*`, `/`, `%`                    | يسار → يمين           |
| جمع/طرح             | `+`, `-`                         | يسار → يمين           |
| مقارنات             | `==`, `!=`, `<`, `<=`, `>`, `>=`, `in` | يسار → يمين     |
| منطق                | `and` ثم `or`                    | يسار → يمين           |

- `and` و`or` قصيران (short-circuit):
  - `A and B`: إن كانت حقيقة `A` كاذبة، لا يُقيّم `B`.
  - `A or B`: إن كانت حقيقة `A` صادقة، لا يُقيّم `B`.
- المكافآت النموذجية:
  - `not -x == y` → يُفسَّر كـ `not ((-x) == y)`.
  - `a + b * c` → `a + (b * c)`.
  - `x in a and y in b` → `(x in a) and (y in b)`.

### ترتيب تقييم الوسائط
- تُقيَّم وسيطات الاستدعاء يسار→يمين قبل الدخول إلى الدالة/الطريقة.
- في سلاسل كـ `expr.attr[idx].method(args)`:
  1) يُقيّم `expr`، ثم الوصول إلى `attr`، ثم `idx`، ثم الاستدعاء `method(args)`.
  2) أي أثر جانبي في خطوة يؤثّر على التالية وفق هذا الترتيب.

## مرجع الدوال السحرية (تفصيلي)

| الدالة        | تثار بواسطة                | التوقيع التقريبي             | القيمة المتوقعة                  |
|---------------|----------------------------|-------------------------------|----------------------------------|
| `__add__`     | `a + b`                    | `def __add__(other)`          | قيمة ناتجة عن الجمع             |
| `__sub__`     | `a - b`                    | `def __sub__(other)`          | قيمة                             |
| `__mul__`     | `a * b`                    | `def __mul__(other)`          | قيمة                             |
| `__truediv__` | `a / b`                    | `def __truediv__(other)`      | قيمة                             |
| `__mod__`     | `a % b`                    | `def __mod__(other)`          | قيمة                             |
| `__eq__`      | `a == b`                   | `def __eq__(other)`           | `True/False`                     |
| `__ne__`      | `a != b`                   | `def __ne__(other)`           | `True/False`                     |
| `__lt__`      | `a < b`                    | `def __lt__(other)`           | `True/False`                     |
| `__le__`      | `a <= b`                   | `def __le__(other)`           | `True/False`                     |
| `__gt__`      | `a > b`                    | `def __gt__(other)`           | `True/False`                     |
| `__ge__`      | `a >= b`                   | `def __ge__(other)`           | `True/False`                     |
| `__neg__`     | أحادي `-a`                 | `def __neg__()`               | قيمة                             |
| `__repr__`    | `repr(a)`                  | `def __repr__()`              | نص يمثّل الكائن                 |
| `__bool__`    | if/while/not               | `def __bool__()`              | `True` أو `False`                |
| `__len__`     | if/while/not (بديل)       | `def __len__()`               | عدد صحيح غير سالب               |
| `__getitem__` | `a[i]`                     | `def __getitem__(i)`          | قيمة العنصر                      |
| `__setitem__` | `a[i] = v`                 | `def __setitem__(i, v)`       | لا شيء (إجراء)                  |
| `__contains__`| `x in a`                   | `def __contains__(x)`         | `True/False`                     |
| `__iter__`    | `for x in a`               | `def __iter__()`              | كائن قابل للتكرار               |
| `__call__`    | `a(...)`                   | `def __call__(args...)`       | نتيجة الاستدعاء                 |

ملاحظات:
- الحقيقة (truthiness): يُفضَّل `__bool__`، وإلا يُستعمل `__len__`، وإلا تُعتبر الكائنات صادقة افتراضياً.
- يجب أن تعيد مقارنات المساواة/التفاوت قيمة منطقية.

## قيود وملحوظات تنفيذية
- لا توجد معاملات افتراضية أو معاملات مسمّاة في تعريف الدوال حالياً.
- سلاسل النص لا تملك هروب محارف موسّع (escape) في هذه النسخة.
- لا تتوفر بنى رفع/التقاط الاستثناءات (raise/try/except) حتى الآن؛ الأخطاء تُغلف ضمن BayanRuntimeError مع إطار كود اختياري.


انتهى.

