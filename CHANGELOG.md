# Changelog | سجل التغييرات

All notable changes to the Bayan Programming Language will be documented in this file.

---


## [Unreleased] | قيد التطوير

### Planned | الميزات المخططة
- Modularize integrated knowledge base into topic files (e.g., prob_kb.bayan, family_kb.bayan, ...), plus a composite loader; keep `load_selective` as a fast path.
- Enhance generator pipeline for context-aware, logic-verified generation; add demos and examples.
- Leverage Bayan's built-in AI/NLP libraries during actual model building.
- Expand tests covering nlp_bayan modules, selective loading, and end-to-end flows; consider CI matrix.
- Optional: allow opt-in linter scope beyond nlp_bayan without affecting Arabic-first projects; consider pre-push hook.
- Improve developer docs: architecture map, contribution guide, coding conventions.

## [2.0.0] - 2025-12-03

### Added | الإضافات ⭐

- ✅ **عقل بيان الموحد (Bayan Brain)** - `bayan/bayan/bayan_brain/`:
  - **دمج الفصين**: الفص المنطقي (سيميائية الحروف) + الفص الرياضي (بصيرة)
  - **BayanBrain**: الفئة الرئيسية التي تدمج كلا الفصين
  - **BrainHemisphere**: تعداد للفصين (منطقي/رياضي)
  - **ThoughtProcess**: عملية تفكير متكاملة
  - **BrainState**: حالة العقل (الفص النشط، الحمل المعرفي)

- ✅ **الجسر اللغوي-الرياضي (Linguistic-Math Bridge)** - `linguistic_math_bridge.py`:
  - `letter_to_equation()`: تحويل حرف إلى معادلة رياضية
  - `word_to_shape()`: تحويل كلمة إلى شكل هندسي
  - `meaning_to_parameters()`: تحويل معنى إلى معاملات رياضية
  - `LinguisticMathBridge`: فئة الجسر الموحد

- ✅ **نظام بصيرة للذكاء الرياضي (Baserah AI)** - `bayan/bayan/baserah_ai/`:
  - **النواة (core/)**:
    - `AdaptiveEquation`: المعادلات المتكيفة
    - `RevolutionaryLeadership`: النظريات الثلاث الثورية
    - `GeneralizedSigmoid`: دوال سيغمويد المعممة
  - **الوحدة الفنية (artistic/)**:
    - `DrawingUnit`: رسم الأشكال (دائرة، قلب، وردة، حلزون)
    - `InferenceUnit`: استنباط معادلة من نقاط
    - `ShapeGenerator`: مولد الأشكال (8 أشكال)
  - **الوحدات المتقدمة (advanced/)**:
    - `ThinkingCore`: 5 طبقات تفكير (رياضي، لغوي، منطقي، فيزيائي، تفسيري)
    - `ConsciousnessSystem`: نظام الوعي والانتباه

- ✅ **دوال عقل بيان للمفسر** - `brain_extension.py`:
  - `فكّر_في()`: التفكير في مدخل باستخدام الفصين
  - `حلّل_بعمق()`: تحليل عميق لكلمة
  - `ولّد_كلمة()`: توليد كلمة من معنى
  - `بدّل_الفص()`: تبديل الفص النشط
  - `حالة_العقل()`: حالة العقل
  - `حرف_إلى_معادلة()`: تحويل حرف لمعادلة
  - `كلمة_إلى_شكل()`: تحويل كلمة لشكل
  - `معنى_إلى_معاملات()`: تحويل معنى لمعاملات
  - `قارن_كلمتين()`: مقارنة كلمتين لغوياً ورياضياً
  - `أنشئ_معادلة_من_كلمة()`: إنشاء معادلة من كلمة

- ✅ **15 دالة بصيرة للمفسر** - `baserah_extension.py`:
  - دوال المعادلات المتكيفة
  - دوال النظريات الثورية (ثنائية الصفر، تعامد الأضداد، الفتائل)
  - دوال الرسم والاستنباط
  - دوال طبقات التفكير والوعي

### Improved | التحسينات
- ✅ **عقل بيان يفكر بفصين متكاملين** 🧠
- ✅ **تحويل المفاهيم اللغوية إلى تمثيلات رياضية والعكس**
- ✅ **28 دالة جديدة للمفسر** (13 عقل بيان + 15 بصيرة)

## [1.9.0] - 2025-12-03

### Added | الإضافات ⭐

- ✅ **نظام استنباط معاني الحروف الذكي** - `inference_engine.py`:
  - **محرك الاستنباط الشكلي (ShapeInferenceEngine)**:
    - استنباط المعاني من شكل الحرف (R = رجل يركض = حركة)
    - دعم الحروف العربية والإنجليزية
    - خرائط الأشكال والمعاني لـ 28 حرف عربي و 26 حرف إنجليزي

  - **محرك الاستنباط الصوتي (SoundInferenceEngine)**:
    - استنباط المعاني من صوت ومخرج الحرف
    - الحروف الجوفية = معاني نفسية
    - الحروف الشفوية = معاني مادية
    - معاني حروف العلة من بكاء الرضيع (آ = طلب الاحتضان، و = طلب اللحاق، ي = التعبير عن الألم)

  - **محرك استنباط اسم الحرف (LetterNameInferenceEngine)**:
    - استنباط المعنى من اسم الحرف (ألف ← ألفة، باء ← باء يبوء)
    - سلاسل سببية للمعاني المترابطة

  - **محرك الاستنباط المعجمي (LexicalInferenceEngine)**:
    - البحث عن كلمات مشتركة في حروف واستخراج المعاني المشتركة
    - مثال: "طلب، حلب، غلب، سحب" = الحمل والانتقال
    - أنماط الحروف المتعاقبة (سح = السحب، قط = القطع)

  - **المحرك المحسن (EnhancedMeaningInferenceEngine)**:
    - يدمج جميع المحركات الأربعة
    - يرتب المعاني حسب درجة الثقة
    - يدمج المعاني المتشابهة

- ✅ **دوال الاستنباط الجديدة للمفسر**:
  - `استنبط_كلمة()`/`infer_word()`: استنباط معنى كلمة جديدة من حروفها
  - `استنبط_حرف()`/`infer_letter()`: استنباط معاني حرف من كل المصادر
  - `حلل_حرف_كامل()`/`full_letter_analysis()`: تحليل شامل (شكلي + صوتي + اسمي + معجمي)

- ✅ **مولد الكلمات من المعاني** - `word_generator.py`:
  - `ابنِ_كلمة()`/`build_word()`: بناء كلمة جديدة من معنى
  - `ولّد_كلمة()`/`generate_word()`: توليد كلمات مقترحة
  - `اقترح_اسم()`/`suggest_name()`: اقتراح اسم لمفهوم

- ✅ **ملحق سيميائية الحروف للمفسر** - `letter_semiotics_extension.py`:
  - إضافة 12 دالة سيميائية للمفسر بدون تعديل الملف المقفل
  - دعم ثنائي اللغة لجميع الدوال

### Improved | التحسينات
- ✅ **النظام قادر على استنباط معاني كلمات جديدة لم يرها من قبل!** 🧠
- ✅ **تحديث `__init__.py`** لتصدير محركات الاستنباط الجديدة
- ✅ **إصدار سيميائية الحروف 2.2.0** - مع محرك الاستنباط

## [1.8.0] - 2025-12-02

### Added | الإضافات ⭐
- ✅ **مكتبة توليد النص الطبيعي (NLG)** - `nlg_lib.py`:
  - `generate_sentence()`/`ولّد_جملة()`: توليد جمل من قوالب
  - `generate_paragraph()`/`ولّد_فقرة()`: توليد فقرات بربط الجمل
  - `generate_list()`/`ولّد_قائمة()`: توليد قوائم منسقة
  - `generate_question()`/`ولّد_سؤال()`: توليد أسئلة
  - `get_connector()`/`احصل_على_رابط()`: الحصول على روابط
  - قوالب عربية وإنجليزية للجمل الشرطية والسببية والزمنية

### Improved | التحسينات
- ✅ **تحسين Bytecode Optimizer**:
  - إضافة Pattern: LOAD_VAR + POP → Remove
  - إضافة Pattern: NOT NOT → Remove (double negation)
  - إضافة Pattern: STORE_VAR + LOAD_VAR → DUP + STORE
  - إضافة Dead Code Elimination بعد RETURN

- ✅ **تحسين IDE Syntax Highlighting**:
  - إضافة 50+ كلمة عربية جديدة للـ highlighting
  - إضافة دوال البرمجة الوصفية
  - إضافة الدوال المدمجة (builtins) بلون مختلف

- ✅ **9 مكتبات قياسية** (كانت 8)

## [1.7.0] - 2025-12-02

### Added | الإضافات ⭐
- ✅ **البرمجة الوصفية (Metaprogramming)** - `metaprogramming.py`:
  - `eval()`/`قيّم()`: تقييم تعبيرات بيان ديناميكياً
  - `exec()`/`نفّذ()`: تنفيذ كود بيان ديناميكياً
  - `compile()`/`ترجم()`: ترجمة كود إلى AST بدون تنفيذ
  - `exec_compiled()`/`نفذ_مترجم()`: تنفيذ كود مترجم مسبقاً
  - `create_function()`/`أنشئ_دالة()`: إنشاء دوال ديناميكياً
  - `modify_function()`/`عدّل_دالة()`: تعديل دوال موجودة
  - `delete_function()`/`احذف_دالة()`: حذف دوال
  - `get_function_info()`/`معلومات_دالة()`: معلومات عن دالة
  - `list_functions()`/`قائمة_الدوال()`: قائمة الدوال المعرفة
  - `introspect()`/`تأمل()`: تأمل الكائنات
  - **الكود يستطيع الآن تعديل نفسه!** 🧬

- ✅ **مثال البرمجة الوصفية** - `metaprogramming_demo.by`:
  - عرض شامل لجميع ميزات البرمجة الوصفية
  - أمثلة على الكود الذي يعدل نفسه
  - مصنع الدوال (Function Factory)

### Improved | التحسينات
- ✅ **دمج البرمجة الوصفية مع المفسر** - جميع الدوال متاحة في البيئة العامة
- ✅ **جميع الأمثلة تعمل بنجاح** - 74/74 (100%) 🎉

## [1.6.4] - 2025-12-02

### Added | الإضافات ⭐
- ✅ **مثال المكتبة القياسية** - `stdlib_demo.by`:
  - عرض شامل لجميع المكتبات الـ 8
  - أمثلة عملية لكل مكتبة
  - توثيق الدوال بالعربية والإنجليزية

### Improved | التحسينات
- ✅ **تحديث التوثيق الشامل**:
  - تحديث `START_HERE_AI.md` بالميزات الجديدة
  - تحديث `NEXT_AI_MODEL_README.md` بالإنجازات
  - تحديث قائمة المهام المقترحة
- ✅ **جميع الأمثلة تعمل بنجاح** - 73/73 (100%) 🎉

## [1.6.3] - 2025-12-02

### Added | الإضافات ⭐
- ✅ **نظام رسائل الأخطاء المحسن** - `error_messages.py`:
  - 29 رسالة خطأ ثنائية اللغة (عربي/إنجليزي)
  - اقتراحات لإصلاح الأخطاء الشائعة
  - عرض سياق الكود مع تحديد موقع الخطأ
  - اقتراح أسماء مشابهة للمتغيرات المكتوبة خطأ
  - فئات الأخطاء: SYNTAX, RUNTIME, TYPE, NAME, IMPORT, LOGIC, VALUE, INDEX, KEY, ATTRIBUTE, DIVISION, FILE, ARGUMENT
  - فئة `BayanError` المحسنة مع دعم ثنائي اللغة

### Improved | التحسينات
- ✅ **جميع الأمثلة تعمل بنجاح** - 72/72 (100%)

## [1.6.2] - 2025-12-02

### Added | الإضافات ⭐
- ✅ **توسيع المكتبة القياسية** - 4 مكتبات جديدة:
  - `io_lib` / `إدخال_إخراج`: عمليات الملفات والمجلدات
    - `read_file`/`اقرأ_ملف`, `write_file`/`اكتب_ملف`, `append_file`/`ألحق_بملف`
    - `file_exists`/`ملف_موجود`, `dir_exists`/`مجلد_موجود`
    - `list_dir`/`قائمة_مجلد`, `make_dir`/`أنشئ_مجلد`
    - `join_path`/`ادمج_مسار`, `get_extension`/`امتداد_ملف`
  - `json_lib` / `جيسون`: تحليل ومعالجة JSON
    - `parse_json`/`حلل_جيسون`, `to_json`/`إلى_جيسون`
    - `read_json`/`اقرأ_جيسون`, `write_json`/`اكتب_جيسون`
    - `get_value`/`احصل_على_قيمة`, `merge_json`/`ادمج_جيسون`
  - `regex_lib` / `تعبيرات_نمطية`: التعبيرات النمطية
    - `match`/`طابق`, `search`/`ابحث`, `find_all`/`جد_الكل`
    - `replace`/`استبدل`, `split`/`قسم`
    - `is_email`/`هل_بريد`, `is_url`/`هل_رابط`, `is_arabic`/`هل_عربي`
    - أنماط جاهزة: `EMAIL_PATTERN`, `URL_PATTERN`, `ARABIC_PATTERN`
  - `http_lib` / `شبكة`: طلبات HTTP
    - `get`/`احصل`, `post`/`أرسل`
    - `get_json`/`احصل_جيسون`, `post_json`/`أرسل_جيسون`
    - `encode_url`/`رمز_رابط`, `decode_url`/`فك_رابط`
    - `download`/`حمل`, `parse_url`/`حلل_رابط`

### Improved | التحسينات
- ✅ **تحديث `stdlib/__init__.py`** لتضمين المكتبات الجديدة
- ✅ **جميع الأمثلة تعمل بنجاح** - 72/72 (100%)

## [1.6.1] - 2025-12-02

### Added | الإضافات ⭐
- ✅ **إضافة الكلمات المفتاحية العربية الناقصة** - 518 كلمة مفتاحية فريدة
  - `صنف`/`فئة` لـ class
  - `إذا`/`لو` لـ if
  - `وإلا`/`غير_ذلك` لـ else
  - `وإلا_إذا`/`أو_إذا` لـ elif
  - `لكل`/`كرر` لـ for
  - `طالما`/`بينما` لـ while
  - `اطبع` لـ print
  - `أرجع`/`ارجع` لـ return
  - `أنتج`/`انتج` لـ yield
  - `اكسر`/`توقف` لـ break
  - `استمر`/`تابع` لـ continue
  - `مرر`/`تجاوز` لـ pass
  - `صحيح`/`صح` لـ True
  - `خطأ`/`خاطئ` لـ False
  - `لاشيء`/`فارغ`/`عدم` لـ None
  - `و` لـ and
  - `أو` لـ or
  - `ليس`/`لا` لـ not
  - `ذاتي`/`نفسي` لـ self
  - `حاول`/`جرب` لـ try
  - `استثنِ`/`استثن`/`عدا` لـ except
  - `أخيراً`/`في_النهاية` لـ finally
  - `أطلق_خطأ`/`ارفع` لـ raise
  - `هو`/`يكون` لـ is
  - `مع`/`باستخدام` لـ with

### Fixed | الإصلاحات
- ✅ **إصلاح 12 تكرار في الكلمات المفتاحية** (تعارضات بسبب عمل نماذج متعددة على المشروع)
  - `صحيح`: TRUE vs TYPE_INT → استخدام `نوع_صحيح` لـ TYPE_INT
  - `تجاوز`: PASS vs OVERRIDE → استخدام `تخطي`/`استبدال` لـ OVERRIDE
  - `عام`: GLOBAL vs PUBLIC → استخدام `عمومي` لـ GLOBAL و `علني`/`عامة` لـ PUBLIC
  - `أخيراً`: FINALLY vs LASTLY → استخدام `ختاماً`/`في_الختام` لـ LASTLY
  - `infer_from`: تعارض → استخدام `infer_from_text` و `infer`
  - إزالة التكرارات: `query`, `match`, `طابق`, `temporal`, `in`, `from`, `من`

### Statistics | الإحصائيات
- **الكلمات المفتاحية الفريدة**: 518 كلمة
- **معدل نجاح الأمثلة**: 72/72 = 100% ✅ 🎉
- **جميع التحديات البرمجية**: 8/8 تعمل (100%) ✅
  - كشف الاحتيال، مستشار التغذية، جدولة الموظفين، تشخيص السيارات
  - المستشار الاستثماري، إدارة الأزمات، المستشار القانوني، المدينة الذكية

### Fixes | الإصلاحات
- **إصلاح `pattern_matching_demo.by`**: تغيير المتغير `فئة` إلى `فصيلة` لأن `فئة` كلمة محجوزة (CLASS)

---

## [1.6.0] - 2025-12-02

### Fixed | الإصلاحات ⭐
- ✅ **إصلاح جميع ملفات الأمثلة** - 72/72 ملف يعمل بنجاح (100%)
  - إصلاح `existential_integration_demo.by`: تغيير من `entity "name": {...}` إلى `name = {...}` للتوافق مع استخدام المتغيرات
  - إصلاح `ai/adaptive_math.by`: تغيير `random.normal()` إلى `random.gauss()` (Python standard library)
  - إضافة معالجة `EntityDef` في `traditional_interpreter.py` للتوجيه الصحيح لـ `visit_entity_def()`

### Technical Details | التفاصيل التقنية
- **ملف `bayan/bayan/traditional_interpreter.py`**:
  - إضافة `elif isinstance(node, EntityDef): return self.visit_entity_def(node)` في `_interpret_core()`

- **ملف `examples/existential_integration_demo.by`**:
  - تغيير تعريف الكيانات من صيغة `entity "name":` إلى متغيرات عادية `name = {...}`

- **ملف `ai/adaptive_math.by`**:
  - استبدال `random.normal(0, strength)` بـ `random.gauss(0, strength)` لأن Python القياسي لا يحتوي على `random.normal()`

### Statistics | الإحصائيات
- **معدل نجاح الأمثلة**: 72/72 = 100% ✅
- **تحسن من**: ~70/72 (97%) إلى 72/72 (100%)

## [1.0.0] - 2024-11-05

### 🎉 Initial Release | الإصدار الأول

This is the first public release of Bayan Programming Language!

### ✨ Features | الميزات

#### Core Language Features
- ✅ **Hybrid Programming** - Three paradigms in one language:
  - Imperative programming
  - Object-oriented programming (OOP)
  - Logic programming (Prolog-style)
- ✅ **Bilingual Keywords** - Full support for Arabic and English keywords
- ✅ **Arabic Text Support** - Perfect handling of Arabic text without external libraries
- ✅ **Modern Syntax** - Clean, Python-inspired syntax with `hybrid { }` wrapper

#### Data Types
- ✅ Integer, Float, String, Boolean, None
- ✅ Lists with indexing and slicing
- ✅ Dictionaries
- ✅ Tuples

#### Control Flow
- ✅ `if`, `elif`, `else` statements
- ✅ `for` loops with `range()` and iterables
- ✅ `while` loops
- ✅ `break` and `continue`

#### Functions
- ✅ Function definitions with `def`
- ✅ Return values
- ✅ Default parameters
- ✅ `*args` and `**kwargs`
- ✅ Lambda functions
- ✅ Nested functions
- ✅ Closures

#### Object-Oriented Programming
- ✅ Class definitions
- ✅ `__init__` constructor
- ✅ Instance methods and attributes
- ✅ Inheritance (single and multiple)
- ✅ `super()` for parent class access
- ✅ Polymorphism
- ✅ Encapsulation
- ✅ Special methods (`__str__`, `__repr__`, `__add__`, etc.)

#### Logic Programming
- ✅ Facts (e.g., `parent("أحمد", "محمد").`)
- ✅ Rules (e.g., `grandparent(?X, ?Z) :- parent(?X, ?Y), parent(?Y, ?Z).`)
- ✅ Queries (e.g., `query parent(?X, "محمد")?`)
- ✅ Unification with pattern matching
- ✅ Backtracking
- ✅ Cut operator (`!`)
- ✅ Dynamic knowledge base:
  - `assertz()` - Add facts at runtime
  - `retract()` - Remove facts at runtime
- ✅ Meta-predicates:
  - `bagof()` - Collect all solutions
  - `setof()` - Collect unique solutions
- ✅ List pattern matching (e.g., `[?H|?T]`)
- ✅ `is` operator for arithmetic evaluation

#### Advanced Features
- ✅ **Generators** - `yield` keyword with proper state preservation
- ✅ **Async/Await** - Asynchronous programming support
- ✅ **Decorators** - Function decorators with `@` syntax
- ✅ **Context Managers** - `with` statement support
- ✅ **Exception Handling** - `try`, `except`, `finally`, `raise`
- ✅ **Import System** - Import Bayan and Python modules

#### Built-in Functions
- ✅ **I/O**: `print()`, `input()`
- ✅ **Type Conversion**: `int()`, `float()`, `str()`, `bool()`, `list()`, `dict()`, `tuple()`
- ✅ **Type Checking**: `type()`, `isinstance()`
- ✅ **Utilities**: `len()`, `range()`
- ✅ **AI/ML Functions**:
  - `sum()`, `min()`, `max()`
  - `sorted()`, `reversed()`
  - `enumerate()`, `zip()`
  - `map()`, `filter()`
  - `all()`, `any()`
  - `abs()`, `round()`, `pow()`

#### Testing
- ✅ **267 Tests** - Comprehensive test suite
- ✅ **100% Pass Rate** - All tests passing
- ✅ **Test Coverage**:
  - Lexer tests
  - Parser tests
  - Interpreter tests
  - OOP tests
  - Logic programming tests
  - Advanced features tests
  - Arabic text handling tests
  - AI/ML integration tests

#### Documentation
- ✅ **Comprehensive Tutorials** (5,594+ lines):
  - Part 1: Introduction (515 lines)
  - Part 2: Procedural & OOP (1,394 lines)
  - Part 3: Logic Programming (1,154 lines)
- ✅ **LLM Integration Files** (2,531+ lines):
  - System Prompt for AI models
  - Quick Reference
  - Complete Guide with 10 examples
  - Usage Guide
  - Test Prompts
- ✅ **Technical Documentation**:
  - Language Guide
  - Architecture
  - Examples
  - Arabic Text Support

#### Examples
- ✅ **15+ Working Examples**:
  - Hello World
  - Calculator
  - Family tree (logic programming)
  - Student management (hybrid)
  - Async/await example
  - Generators example
  - Decorators example
  - Context managers example
  - Arabic text demo
  - And more...

### 🐛 Bug Fixes | إصلاح الأخطاء

- ✅ Fixed generator state preservation
- ✅ Fixed async/await coroutine handling
- ✅ Fixed Arabic text rendering (RTL, character joining, diacritics)
- ✅ Fixed exception handling for Python exceptions
- ✅ Fixed multiple inheritance method resolution
- ✅ Fixed list pattern matching in logic programming
- ✅ Fixed `is` operator for arithmetic evaluation

### 📚 Documentation | الوثائق

- ✅ Added comprehensive Arabic tutorials
- ✅ Added LLM integration guides
- ✅ Added technical documentation
- ✅ Added code examples
- ✅ Added README with badges
- ✅ Added CONTRIBUTING guide
- ✅ Added LICENSE (MIT)
- ✅ Added AUTHORS file
- ✅ Added this CHANGELOG

### 🔧 Internal Changes | التغييرات الداخلية

- ✅ Refactored interpreter architecture
- ✅ Improved error messages
- ✅ Optimized performance
- ✅ Enhanced code organization
- ✅ Added comprehensive comments

---

## [Unreleased] | قيد التطوير

### Planned Features | الميزات المخططة

#### Short-term (Next Release)
- [ ] Standard library modules
- [ ] File I/O operations
- [ ] Regular expressions
- [ ] JSON support
- [ ] Better error messages with line numbers
- [ ] REPL improvements

#### Medium-term
- [ ] Package manager
- [ ] Debugger
- [ ] Profiler
- [ ] Code formatter
- [ ] Syntax highlighting for popular editors
- [ ] Language server protocol (LSP)

#### Long-term
- [ ] JIT compilation for performance
- [ ] Native executable generation
- [ ] Web assembly support
- [ ] Mobile platform support
- [ ] IDE plugins (VSCode, PyCharm, etc.)
- [ ] Online playground

### Known Issues | المشاكل المعروفة

Currently, there are no known critical issues. All 267 tests are passing.

If you find a bug, please report it on GitHub: [Issues](https://github.com/mubtakir/nlp_bayan/issues)

---

## Version History | تاريخ الإصدارات

### [1.0.0] - 2024-11-05
- Initial public release
- 154 files
- 41,889 lines of code and documentation
- 267 passing tests
- Full feature set as described above

---

## How to Upgrade | كيفية الترقية

### From Source

```bash
cd nlp_bayan
git pull origin main
```

### Fresh Install

```bash
git clone https://github.com/mubtakir/nlp_bayan.git
cd nlp_bayan
```

---

## Breaking Changes | التغييرات الجذرية

### Version 1.0.0
- First release, no breaking changes

---

## Deprecations | الميزات المهملة

### Version 1.0.0
- No deprecations in first release

---

## Contributors | المساهمون

### Version 1.0.0
- **Basel Yahya Abdullah** - Creator and lead developer
- **AI Language Models** - Development assistance

See [AUTHORS.md](AUTHORS.md) for more details.

---

## Links | الروابط

- **Repository**: https://github.com/mubtakir/nlp_bayan
- **Issues**: https://github.com/mubtakir/nlp_bayan/issues
- **Discussions**: https://github.com/mubtakir/nlp_bayan/discussions
- **Documentation**: [docs/](docs/)

---

## Changelog Format | تنسيق سجل التغييرات

This changelog follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### Categories
- **Added** - New features
- **Changed** - Changes in existing functionality
- **Deprecated** - Soon-to-be removed features
- **Removed** - Removed features
- **Fixed** - Bug fixes
- **Security** - Security fixes

---

**Developed by: Basel Yahya Abdullah (باسل يحيى عبدالله)**
**With assistance from: AI Language Models**

---

**🌟 Bayan - The World's First True Hybrid Programming Language 🌟**


## [1.4.0] - 2025-11-06

### Added - الإضافات
- ✨ **نظام الاستدلال الاحتمالي والتشكيك** - Probabilistic Reasoning and Uncertainty System
  - قاعدة بيانات الحقائق الاحتمالية `prob(fact, entity, probability)`
  - 5 أدوات تشكيك ثنائية اللغة (عربي + إنجليزي):
    - `ربما/maybe` (احتمال > 50%)
    - `محتمل/likely` (احتمال > 70%)
    - `غير_محتمل/unlikely` (احتمال < 30%)
    - `ممكن/possible` (احتمال بين 20% و 80%)
    - `مؤكد/certain` (احتمال > 95%)
  - حساب الحالات المتعددة (Multiple States)
  - الاستدلال الشرطي الاحتمالي (Conditional Probabilistic Inference)
  - ملف جديد: `bayan_solutions/probabilistic_reasoning.by` (~209 سطر)
  - وثائق جديدة: `docs/04_PROBABILISTIC_REASONING_AR.md`

### Features - الميزات
- 🎲 التعبير عن عدم اليقين بشكل صريح ورقمي
- 🌍 دعم كامل للكلمات المفتاحية العربية والإنجليزية
- 📊 حسابات احتمالية شفافة وقابلة للتفسير
- ⚙️ استدلال شرطي مبني على الاحتمالات
- ✅ أمثلة عملية (الحديقة، المركب الكيميائي)

### Technical Details - التفاصيل التقنية
- استخدام بنية مسطحة (flat structure) لتجنب الأقواس المتداخلة
- عمليات احتمالية: AND (P(A∧B) = P(A)×P(B)), NOT (P(¬A) = 1-P(A))
- دعم 4 حالات متعددة لكل زوج من المتغيرات
- شفافية كاملة - كل احتمال قابل للتتبع

### Use Cases - حالات الاستخدام
- 🏥 التشخيص الطبي
- 💼 التنبؤ بالمبيعات
- 🔒 تقييم المخاطر
- �� أنظمة الخبراء الاحتمالية
- 📈 اتخاذ القرارات المبنية على البيانات



## [1.5.0] - 2025-11-11

### Added | الإضافات
- docs/DEVELOPER_GUIDE.md — دليل شامل للمطورين (سياسات، أدوات، تشغيل، اختبارات، أمثلة)
- scripts/bayan_lint_identifiers.py — لينتر لفرض «المعرّفات الإنجليزية فقط» داخل nlp_bayan
- .githooks/pre-commit — هوك يفحص فقط ملفات .bayan/.by ضمن nlp_bayan قبل الالتزام
- .github/workflows/lint-and-test.yml — سير عمل CI لتشغيل اللينتر والاختبارات تلقائيًا
- tests/test_integrated_kb_selective.py — اختبارات للتحقق من التحميل الانتقائي للقاعدة
- load_selective(target_logical, only) داخل nlp_bayan/core/integrated_kb.bayan — تحميل مجالات معرفية محددة

### Changed | تعديلات
- تحديث nlp_bayan/examples/demo_generation.bayan ليحمّل القاعدة المتكاملة للحصول على نتائج استعلام أغنى
- توحيد المعرّفات إلى الإنجليزية داخل nlp_bayan/core مع الإبقاء على حرية البيانات النصية بالعربية

### Fixed/Improved | إصلاحات/تحسينات (متعلقة بالسياق)
- تحسين طباعة نتائج الاستعلامات داخل hybrid بعرض متغيّرات الاستعلام فقط وبقيم مفككة
- دعم مقارنات مثل `?p > 0.5` داخل جسم القاعدة عبر تحويلها لمسندات مقارنة خاصة أثناء التحليل
