# دليل المطوّرين للغة بيان (Bayan Developer Guide)

هذا الدليل موجّه لمن يرغب بالمساهمة في تطوير لغة بيان نفسها (المترجم/المفسّر، النحو، المنطق الهجين، ونظام الوحدات).
يشرح معمارية النظام، مكوّناته، تدفّق التنفيذ، أين تبدأ، وكيف تضيف ميزات جديدة بأمان مع الاختبارات.

المحتويات
- لمحة سريعة: ما هي بيان؟ وما الوضع الحالي؟
- بنية المستودع
- نظرة معمارية عالية المستوى
- تدفّق التنفيذ (من النص إلى التشغيل)
- المرمّز (Lexer)
- المحلّل النحوي (Parser) وAST
- المفسّر التقليدي (Traditional Interpreter)
- نظام الأصناف والوراثة (C3 MRO + super)
- المحرّك المنطقي والمنهج الهجين (Hybrid)
- نظام الاستيراد (Modules: Bayan + Python)
- الإبلاغ عن الأخطاء (Bayan stack + code frames + ألوان اختيارية)
- تشغيل الاختبارات وكتابة حالات جديدة
- إضافة ميزة لغة جديدة: منهجية العمل خطوة بخطوة
- خارطة طريق وأفكار مستقبلية

---

## لمحة سريعة: ما هي بيان؟ وما الوضع الحالي؟
- بيان لغة هجينة تجمع البرمجة التقليدية (تعريفات، دوال، أصناف، حلقات، شروط) مع برمجة منطقية شبيهة بـ Prolog (حقائق، قواعد، استعلامات) ضمن نفس الملف/الكتلة `hybrid { ... }`.
- تدعم المعرّفات العربية واللاتينية: `[a-zA-Z_\u0600-\u06FF][a-zA-Z0-9_\u0600-\u06FF]*`.
- الوراثة المتعددة مدعومة مع ترتيب طرق C3 (MRO) و`super()` بصيغتين: `super().m(...)` و`super(m, args)`.
- نظام أخطاء متقدّم مع تتبّع Bayan stack وإطارات كود ملوّنة اختيارياً ومؤشّر ^ محسوب عرضياً (عربي/محارف واسعة/تبويبات) واقتراحات "هل تقصد؟" للأسماء غير المعروفة.
- الوضع الحالي: جميع الاختبارات القائمة ناجحة (كما في بيئة التطوير المستخدمة أثناء التوثيق). راجع tests/ للاطلاع.

## بنية المستودع
- bayan/bayan/lexer.py: المرمّز إلى رموز (Tokens) مع معلومات (line, column)
- bayan/bayan/parser.py: المحلّل وبناء شجرة AST وإرفاق الموقع بكل عقدة
- bayan/bayan/traditional_interpreter.py: المفسّر للتراكيب التقليدية + النظام الكائني + الإبلاغ عن الأخطاء
- bayan/bayan/hybrid_interpreter.py: تنسيق التنفيذ الهجين بين التقليدي والمنطقي
- bayan/bayan/logical_engine.py: التعابير المنطقية (Term, Predicate, Fact, Rule) وخوارزميات التحقق
- bayan/bayan/import_system.py (إن وجد) أو داخل المفسّر: تحميل الوحدات (ببيان وبايثون) والتخزين المؤقت
- bayan/tests/: اختبارات pytest لوحدات اللغة وسلوكها
- docs/basics.md: دليل أساسيات اللغة
- docs/reference.md: مرجع نحوي وسلوكي مختصر-رسمي

## نظرة معمارية عالية المستوى
- طبقة Lexing: تحوّل النص إلى تسلسل Tokens وتحافظ على line/column.
- طبقة Parsing: تبني AST من الـ Tokens، وتضيف metadata: (line, column, filename) لكل عقدة عبر `with_pos`.
- طبقة Interpreting:
  - تقليدية: تقييم العبارات، بيئات المتغيرات، الدوال، الأصناف، الدوال السحرية.
  - منطقية: تمثيل الحقائق والقواعد والاستعلامات وتشغيلها.
  - هجينة: دمج الطبقتين داخل كتلة واحدة، مع واجهة Interpreter عليا تجمعهما.
- طبقة الاستيراد: تحميل وحدات بيان أولاً ثم محاولة بايثون الآمنة (قوائم بحث وتخزين مؤقت).
- طبقة الأخطاء: تتبّع مكدّس عقد Bayan وإظهار code frame ذكي مع خيارات تلوين.

## تدفّق التنفيذ (من النص إلى التشغيل)
1) Lexer: إدخال نص → Tokens (مع line/column).
2) Parser: Tokens → AST (Program/Block/Statements/Expressions...) مع filename/line/column.
3) Hybrid/Traditional Interpreter: زيارة العقد حسب نوعها، إدارة بيئات التنفيذ، ودفع/سحب إطارات المكدّس.
4) عند الخطأ: تشكيل رسالة تتضمن Bayan stack + code frame حسب الموضع.

## المرمّز (Lexer)
- يتعرّف:
  - المعرّفات العربية/اللاتينية.
  - الأعداد (صحيحة/عشرية)، السلاسل النصية، `True/False/None`.
  - الكلمات: `def, class, if, elif, else, for, while, in, print, return, break, continue, pass, and, or, not, self, super, import, from, as, hybrid, query, fact, rule`.
  - العوامل: `== != <= >= < > + - * / %`, و`in` للمحددات، و`:-` أو `←` للقواعد المنطقية.
- كل Token يحمل (type, value, line, column).

## المحلّل النحوي (Parser) وAST
- يستقبل اختياريًا `filename` ويًرفقه لكل عقدة عبر `_with_pos` → `node.with_pos(line, column, filename)`.
- يدعم:
  - التعاريف: `def`, `class` (وراثة مفردة/متعددة: `class C(A,B): { ... }`).
  - الجمل: `if/elif/else`, `for`, `while`, `return`, `print`.
  - التعبيرات: أعداد، نصوص، منطقية، متغيرات (بما فيها المنطقية `?X` داخل المنطق)، قوائم `{}` وقواميس `[]` حسب الملف، الوصول، الاستدعاء، الفهرسة.
  - `self` مع سلاسل لاحقة، و`super()` بصيغتيها المذكورتين.
  - المنطق: facts/rules/queries داخل أو خارج `hybrid {}` حسب القواعد.
- AST يضم عقدًا مثل: Program, Block, Assignment, AttributeAssignment, SubscriptAssignment, IfStatement, ForLoop, WhileLoop, ReturnStatement, PrintStatement, FunctionDef, ClassDef, Number, String, Boolean, Variable, List, Dict, FunctionCall, MethodCall, AttributeAccess, SubscriptAccess, UnaryOp, BinaryOp, SelfReference, SuperCall، إضافة إلى Predicate/Fact/Rule/Query للمنطق.

## المفسّر التقليدي (Traditional Interpreter)
- بيئات:
  - `global_env` و`local_env` (المجال الحالي)، مع جداول `functions` و`classes`.
- بروتوكولات مدعومة عبر الدوال السحرية (dunder):
  - حسابية/مقارنات: `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__mod__`, `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, وأحادي `__neg__`.
  - نصية/تمثيل: `__repr__`.
  - حقيقة وطول: `__bool__`, `__len__`.
  - حاويات: `__getitem__`, `__setitem__`, `__contains__`.
  - تكرار: `__iter__`.
  - قابلية الاستدعاء: `__call__`.
- الحقيقة (truthiness): يفضّل `__bool__`، ثم `__len__`، وإلا فالحقيقة الافتراضية.

## نظام الأصناف والوراثة (C3 MRO + super)
- الأصناف تدعم وراثة متعددة مع حساب ترتيب C3.
- استدعاء `super()`:
  - `super().method(args)`، أو الصيغة القديمة `super(method, args)`.
- المفسّر يحافظ على owner stack (السياق المالك للوسيلة) لضمان تخطّي الصنف الحالي في تسلسل MRO.

## المحرّك المنطقي والمنهج الهجين (Hybrid)
- هياكل: `Term`, `Predicate`, `Fact`, `Rule`.
- القواعد: `head(X) :- body1(X), body2(X).` أو `head(X) ← body1(X), body2(X).`
- الاستعلام: `query predicate(...)`. المتغير المنطقي يبدأ بـ `?`.
- الكتلة `hybrid { ... }`: تُدمج فيها التصريحات التقليدية مع حقائق/قواعد/استعلامات.

## نظام الاستيراد (Modules)
- صيغ:
  - `import pkg.module [as alias]`
  - `from pkg.module import Name[, Name]*`
- يحمّل وحدات بيان (`.bayan`) أولاً من مسارات محدّدة (مثل cwd وtests/ وtests/bayan_modules/ إذا كانت مهيّأة)، ثم يحاول استيراد بايثون الآمن.
- التخزين المؤقت يمنع إعادة التحميل لنفس الوحدة.
- يتم عرض محتوى الوحدة عبر Proxy يتيح الوصول إلى الأصناف/الدوال/المتغيرات التي عرّفتها الوحدة.

## الإبلاغ عن الأخطاء (Bayan stack + code frames)
- كل زيارة لعقدة تضيف إطارًا إلى `_call_stack` بصيغة `(NodeType, line, column, filename)`، ويزال بعد التقييم.
- عند التقاط خطأ، يُبنى `BayanRuntimeError` مع:
  - Bayan stack: `Node@file:line:col -> ...`
  - إطار كود (code frame) اختياري التلوين: اسم الملف، سطور سياقية مرقّمة، إبراز السطر الحالي، مؤشر `^` بمحاذاة عرضية صحيحة (يدعم تبويبات ومحارف واسعة).
- واجهات الإعداد:
  - `set_source(code, filename=None)` لتوفير النص لأطر الكود.
  - `set_error_formatting(colors: bool, context_lines: int, tabstop: int)` لتخصيص العرض.
- اقتراحات "هل تقصد؟" لأسماء غير معرّفة عبر مسافة Levenshtein قصيرة على رموز البيئة الحالية (محلي/عام + أسماء الدوال/الأصناف).

## تشغيل الاختبارات وكتابة حالات جديدة
- من مجلد bayan/: شغّل: `pytest -q`
- تشغيل ملف واحد: `pytest -q tests/test_error_reporting.py`
- تشغيل اختبار مسمّى: `pytest -q -k name_substring`
- إضافة اختبار:
  - ضع ملفًا في tests/ يبدأ بـ `test_*.py`.
  - أنشئ حالات إيجابية/سلبية تغطي السلوك الجديد ومواضع الخطأ وحدود الحالات.

## إضافة ميزة لغة جديدة: منهجية العمل خطوة بخطوة
1) حدّد المتطلبات بدقة وأضف اختبارات أولًا (TDD إن أمكن).
2) Lexer:
   - إن كانت الميزة تتطلب رمزًا/كلمة محجوزة جديدة، أضف TokenType والقواعد.
3) Parser:
   - حدّث القواعد، وأعد استخدام `_with_pos` لكل عقدة تُنشِئها.
   - راعِ تداخل السلاسل (الوصول/الفهرسة/الاستدعاء) وملكية الموضع (token الأنسب).
4) Interpreter:
   - أضف زائر العقدة الجديدة وممنهجية تقييمها.
   - إن كانت علاقة بمشغّلات/dunder فادمجها مع المنطق القائم بحذر.
5) التوثيق:
   - حدّث docs/basics.md وdocs/reference.md بما يعكس السلوك الجديد.
6) التحقّق:
   - شغّل اختبارات الملف المعني ثم المجموعة كاملة.

## خارطة طريق وأفكار مستقبلية
- اللغة:
  - وسائط افتراضية ومعاملات مسماة للـ functions.
  - سلاسل نصية متعددة الأسطر وهروب محارف موسّع.
  - استثناءات مخصّصة (raise/try/except) ومزيد من أنواع الأخطاء الدلالية.
  - تحسين التكامل مع بايثون (Typed interop، تحويلات أنواع آمنة).
- الأدوات:
  - تنسيق تلقائي للشفرة وتحقق ساكن (lint/type-check) إن تقرّر.
  - قناة REPL تفاعلية مع إبراز نحوي وتكامل الألوان.
- تشخيص الأخطاء:
  - سياق أسطر متعدد قابل للتهيئة عالميًا.
  - اقتراحات أغنى (spellcheck متعدد اللغات، اقتراح استيراد مفقود).

## من أين أبدأ؟
- اقرأ docs/basics.md وdocs/reference.md لتفهم السلوك الحالي.
- شغّل الاختبارات بـ `pytest -q` للتأكد من صحة البيئة.
- جرّب تعديلًا صغيرًا (على سبيل المثال تحسين رسالة خطأ) وأضف اختبارًا له.
- عند إضافة نحو جديد: ابدأ من lexer → parser → interpreter → tests → docs.

انتهى.



---

## ملحق تسليم — مكتبة الذكاء الاصطناعي (AI Stdlib) — 2025-11-09

هذا الملحق يوجّه المطوّر التالي المستلم للمشروع بخصوص مكتبة الذكاء الاصطناعي القياسية داخل بيان، وما أُنجز وما تبقّى.

### الغاية العامة
- الهدف العملي الذي تبنّيناه: «كل تعبير برمجي يفيد لاحقاً في بناء نموذج لغوي».
- لذلك تم بناء مكتبة AI/ML تعليمية بالكامل داخل بيان (بدون تبعيات خارجية)، بثنائية عربية/إنجليزية، مع اختبارات شاملة.

### أين وصلنا؟ (وضع الموجات)
- Waves 1–15: مكتملة ومُوثّقة ومُمَرَّرة بالاختبارات (361/361 ناجحة).
  - Data: CSV/JSON I/O، إحصاء وصفي (mean/var/std/median/percentile)، PRNG، scalers (standard/robust/minmax) fit+transform.
  - NLP: TF-IDF (خيارات/لوغ/حدود مفردات)، BM25، تشابه Jaccard/Dice، تجهيز نص عربي أساسي.
  - ML: الانحدار الخطي/اللوجستي، KNN (عادي/موزون)، K-means (+k-means++ احتمال)، Perceptron (+OvR)، أشجار قرار، غابة عشوائية، قياسات ROC/AUC وتقارير تصنيف.
- Wave 9: مكتملة (ML OvR + Bagging، NLP overlap_coefficient، Data bin_equal_width + one_hot_encode).
  - ML: linear_svm_ovr_train/predict + Arabic wrappers (تدريب_SVM_OVR/توقع_SVM_OVR).
  - ML: bagging_train/predict (تجميع قائم على «stumps» تعليمية) + Arabic wrappers (تدريب_باغينغ/توقع_باغينغ).
  - NLP: overlap_coefficient(list1, list2) — PASS.
  - Data: bin_equal_width و one_hot_encode — مع أغلفة عربية: تجزئة_عرض_متساوي، ترميز_واحد_ساخن.

- Wave 10: مكتملة (Data encoders: label/frequency/target) مع نمط fit/transform وأغلفة عربية.

- Wave 11: مكتملة (NLP: levenshtein_distance + مسافة_ليفنشتاين).

- Wave 12: مكتملة (NLP: cosine_similarity + similarity() + bm25_score_with_term_weights).
- Wave 13: مكتملة (NLP: tfidf_cosine_similarity + bm25_top_k؛ ML: AdaBoost؛ أغلفة عربية: تشابه_جيبي_TFIDF، أفضل_BM25، تدريب_ادابوست، توقع_ادابوست).

- Wave 14: مكتملة (NLP: lcs_length + jaccard_char_ngrams؛ ML: naive_bayes_train/predict؛ أغلفة عربية).


### حالة الاختبارات (وقت التسليم)
- المجموع المُمَرّر حالياً: 361/361 (Waves 1–15).
- Wave 9:
  - tests/test_ai_data_wave9.py: PASS.
  - tests/test_ai_ml_wave9.py: PASS.
  - tests/test_ai_nlp_wave9.py: PASS.
- Wave 10:
  - tests/test_ai_data_wave10.py: PASS.
- Wave 11:
  - tests/test_ai_nlp_wave11.py: PASS.
- Wave 12:
  - tests/test_ai_nlp_wave12.py: PASS.
- Wave 13:
  - tests/test_ai_nlp_wave13.py: PASS.
  - tests/test_ai_ml_wave13.py: PASS.

- Wave 14:
  - tests/test_ai_nlp_wave14.py: PASS.
- Wave 15:
  - tests/test_ai_nlp_wave15.py: PASS.

  - tests/test_ai_ml_wave14_nb.py: PASS.


### إنجازات Wave 9

1) إتمام ML OvR + Bagging:
   - ملف: ai/ml.bayan
   - التحقّقات النحوية: وُضعت ":" بعد كل if/elif/else/for/while وبدون ";".
   - استبدال int(...) بحساب أرضي يدوي لقيمة m.
   - pytest -q tests/test_ai_ml_wave9.py → PASS.

2) NLP Wave 9:
   - overlap_coefficient → PASS (pytest -q tests/test_ai_nlp_wave9.py).

3) Data Wave 9 — أغلفة عربية:
   - أُضيفت: تجزئة_عرض_متساوي، ترميز_واحد_ساخن في ai/data.bayan → PASS.

4) التوثيق والشارات:
   - ai/AI_LIBRARY_GUIDE.md و README.md محدّثان إلى 353/353.

### تذكير مهم — «Cheat‑Sheet» نحو بيان
- ضع ":" بعد كلمات التحكّم (if/elif/else/for/while).
- لا يوجد ";" للفصل بين الجمل.
- الكلمة المحجوزة "query" لا تُستخدم كاسم متغيّر/معامل.
- لا توجد list comprehensions؛ استخدم حلقات صريحة.
- استخدم pow() بدل **، ولا يوجد //؛ عالج القسمة الصحيحة/الباقي يدوياً عند الحاجة.
- لا تستخدم شرائح سالبة المؤشّر؛ استخدم [0:len(x)-n].
- لا توجد ternary expressions؛ استخدم if/else كاملة.

### ما بعد Wave 9 (مقترح موجات تالية)
- Wave 10:
  - Data: LabelEncoder بسيط، Frequency/Target Encoding (تعليمي)، كائنات fit/transform خفيفة.
  - NLP: Levenshtein (تقريبي)، تحسين BM25 بخيارات stopwords/normalization hooks، حزمة مقاييس overlap/dice/coef موسّعة.
  - ML: Platt scaling (معايرة احتمالات)، One‑vs‑Rest للأصناف المتعدّدة للوجستي، Bagging عام لواجهات قابلة للتمرير.
- Wave 11–12:
  - Data: Binning موسّع + One‑hot/Ordinal/Hashing.
  - NLP: Soundex/Metaphone تقريبي عربي/إنجليزي.
  - ML: AdaBoost تعليمي، SVM خطي مع تدرّج منظّم أفضل، تقارير متقدّمة.

### روابط سريعة
- دليل مكتبة الذكاء: ai/AI_LIBRARY_GUIDE.md
- الاختبارات الجديدة: tests/test_ai_data_wave9.py, tests/test_ai_ml_wave9.py, tests/test_ai_nlp_wave9.py
- الملفات ذات الصلة: ai/data.bayan, ai/ml.bayan, ai/nlp.bayan


---

## ملحق تسليم — مكتبة الذكاء الاصطناعي (Wave 16) + دليل استلام للمطوّر التالي (نموذج ذكي)

هذا الملحق موجّه مباشرةً للمطوّر/النموذج الذكي الذي سيُكمل بقية الموجات. ستجد هنا تعريفًا سريعًا بلغة البيان، قواعدها العملية داخل هذا المستودع، وما أُنجز وما ينبغي عليك فعله خطوة بخطوة.

### 1) تعريف سريع بلغة البيان (Cheat‑Sheet عملي)
- البيان لغة هجينة: تقليدي + كائني + منطقي داخل كتلة واحدة `hybrid { ... }`.
- القواعد النحوية الحرجة:
  - ضع دائمًا `:` بعد `if/elif/else/for/while`.
  - لا تستخدم `;` مطلقاً (كل جملة في سطر مستقل).
  - الكلمة `query` محجوزة (لا تستخدمها كاسم متغيّر).
  - لا توجد list comprehensions: استخدم حلقات صريحة.
  - استخدم `pow()` بدل `**`؛ تجنب `//`؛ لا تستخدم شرائح سالبة؛ لا توجد تعابير ثلاثية.
  - تجنّب `None` كقيمة تشغيلية؛ استخدم أعداد/قوائم مناسبة.
- الأمثلة التالية هي النمط المعتمد في هذا المشروع:

```bayan
hybrid {
  # حلقة مع شرط
  s = 0
  for i in range(5): {
    if i > 2: {
      s = s + i
    }
  }
}
```

### 2) معايير الكود الخاصة بمكتبة AI التعليمية
- بدون تبعيات خارجية (لا NumPy/SciPy): اكتب كل شيء بوضوح وباستخدام قوائم/حلقات.
- العشوائية: إن احتجت، استخدم LCG (a=1103515245, c=12345, m=2^31) + Fisher–Yates.
- القسمة الصحيحة/التقريب: لا تستخدم تحويلات `int(...)`; اعتمد على عمليات تراكمية أو حلقات للاقتراب العددي (مثال: التقريب إلى الأقرب عبر `t = x + 0.5` ثم زيادة عدّاد صحيح حتى ≤ t).
- دوال عربية: إن أضفت وظيفة إنجليزية عامة، أضف غلافًا عربيًا عند الحاجة (نفس التواقيع بالعربية قدر الإمكان).
- الاختبارات أولًا قدر الإمكان (TDD)، ثم تنفيذ الدوال، ثم تحديث الوثائق.

### 3) أين وصلنا الآن؟
- Waves 1–16: مكتملة.
  - Wave 16 (جديد):
    - ML: stratified_k_fold_indices, train_test_split_stratified
    - ML Metrics: matthews_corrcoef, cohen_kappa_score
    - NLP: damerau_levenshtein_distance + غلاف عربي: مسافة_دامراو_ليفنشتاين
- الحالة: 364/364 اختبار ناجح.

### 4) ما الذي يجب عليك فعله الآن (خارطة الطريق المختصرة)
- Wave 17 — PCA + VarianceThreshold + Pipelines بسيطة:
  - ML:
    - pca_fit(X, n_components) → [components, mean]
    - pca_transform(X, components, mean)
    - variance_threshold_fit(X, thr) → mask
    - variance_threshold_transform(X, mask)
  - Data/Pipeline: كائن تحويل بسيط (قائمة من (name, fit_fn, transform_fn, params)) يُنفَّذ بالتتابع.
  - اختبارات: مصفوفات صغيرة للتحقّق من إسقاطات PCA والمعاد بناء (تناقص الخطأ مع زيادة المكوّنات)، وأقنعة variance.
  - توثيق: تحديث README/AI_LIBRARY_GUIDE/AI_HANDOFF_REPORT + إضافة release workflow.

- Wave 18 — Softmax متعدد الفئات + متوسطات micro/macro، وNLP: Soft TF‑IDF:
  - ML: لوغستي متعدد (softmax) train/predict + قياسات micro/macro (precision/recall/f1/accuracy).
  - NLP: Soft TF‑IDF (ادماج تشابه رموز مثل Jaro‑Winkler داخل وزن المصطلح).
  - اختبارات شاملة، أمثلة صغيرة.

- Wave 19 — Ensembles + اختيار نموذج:
  - VotingClassifier (hard/soft) + Stacking بسيط.
  - Grid search صغيرة للمعاملات.

- Wave 20 — Polish + v1.0:
  - تثبيت الواجهات، أمثلة تعليمية، تحسين الأداء حيث يلزم، التوثيق النهائي.

### 5) سير العمل لكل موجة (خطوات ثابتة)
1. أضِف الاختبارات في `tests/` (اسم يبدأ بـ `test_ai_*_waveXX.py`).
2. نفّذ الدوال داخل `ai/*.bayan`، وأضِف الأغلفة العربية إذا لزم.
3. شغّل: `pytest -q tests/test_ai_..._waveXX.py` ثم `pytest -q` كاملًا.
4. حدّث الوثائق:
   - README: الشارة وعدّاد الاختبارات (364 → 3 أرقام جديدة عند الحاجة).
   - ai/AI_LIBRARY_GUIDE.md: قسم vXX الجديد + حالة التسليم Waves 1–XX complete.
   - docs/developer_guide.md: أضف ملحق موجة جديدة إذا كانت كبيرة.
   - AI_HANDOFF_REPORT.md: Addendum للموجة.
5. أضِف ملف إصدار: `.github/workflows/release-waveXX.yml` (نفس نمط الأمواج السابقة).
6. التزم وسِم وادفع (حسب سياسة المستودع):
   - الرسالة: `AI stdlib Wave XX — ...; tests: NNN/NNN passing`.
   - الوسم: `ai-stdlib-vXX`.

### 6) أمثلة صغيرة قد تنفعك أثناء التطوير
- مصفوفات/قوائم ومقارنة عناصر:
```bayan
hybrid {
  X = []
  row = []; row.append(1); row.append(2); X.append(row)
  row = []; row.append(3); row.append(4); X.append(row)
}
```

- عدّاد/شرط بدون فواصل منقوطة:
```bayan
hybrid {
  c = 0
  for i in range(3): {
    if i == 1: {
      c = c + 1
    }
  }
}
```

> تذكير نهائي: راعِ قواعد بيان بحزم (النقطتان بعد تراكيب التحكّم، عدم استخدام `;`، عدم استخدام `query` كمُعرّف، وتفادي التحويلات السريعة لأنواع الأعداد عبر int()).
