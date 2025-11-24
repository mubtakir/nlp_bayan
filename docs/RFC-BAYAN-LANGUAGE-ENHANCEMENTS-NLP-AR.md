## RFC: اقتراحات لترقية لغة «البيان» لدعم توليد تسلسلي منضبط ومنطقي (عامة، غير محصورة بالنموذج اللغوي)

الغرض: رفع مفاهيم برمجناها داخل nlp_bayan إلى مستوى «ميزات لغوية/مكتبة قياسية» عامة، بحيث تسهِّل بناء مولدات/مخطِّطات/أنظمة قرار تتكامل فيها:
- الاستدلال المنطقي (Logic)
- التوزيعات الاحتمالية والاختيار الموزون (Probabilistic Choice)
- القيود/المرشِّحات (Constraints)
- قواعد الصياغة/التوليد الشكلي (Declarative Rewrite Rules)
- سياق/حالة محادثة أو جلسة (Context)

بدلاً من أن تكون هذه الأنماط مكررة داخل نموذج لغوي واحد، نقترح جعلها جزءًا من «بنية البيان» أو مكتبته القياسية.

---

### 1) جسر منطقي-إجرائي أصيل (Logic–Imperative Interop)
المشكلة الحالية: اضطررنا لاستخدام متغيّر منطقي (?F) من داخل دوال إجرائية لتفعيل الاستعلام. هذا يُعقِّد القراءة ويقيِّد الاستفادة.

المقترح:
- دوال معيارية آمنة للربط (exists/first/all/collect) تعمل داخل السياق الإجرائي وتنفّذ استعلامات منطقية مباشرةً:
  - exists(pred, ...): bool
  - first(pred, ...) → أول حل/None
  - collect(pred, ...) → قائمة حلول (مع حد أقصى اختياري)
- دعم «ربط موّحد» (unify) يعود بقيم مُرتبطة أو False بدل اللجوء إلى ?F.

فوائد عامة: ليست محصورة بـ NLP؛ أي مشروع يجمع منطقًا وإجراءً سيستفيد.

مثال (صياغة مبدئية):
```bayan
if (exists maybe("is_green","garden")) { ok = True } else: { ok = False }
sol = first path("A","B")
xs = collect isa("x", "entity"), limit=10
```

---

### 2) توزيعات واحتمالات ككائنات من الدرجة الأولى (First-class Distributions)
المشكلة الحالية: أخذ العينات (temperature/top-k/top-p) والتعزيز (boost) و«التفسير» مبعثرة داخل الدوال.

المقترح:
- نوع قياسي dist يمثل توزيعًا على مرشحين مع عمليات سلسلة (سيرورة أنابيب):
  - dist({...}).filter(fn).boost(fn, factor).nucleus(p).temperature(t).normalize().sample(rng_seed=?, trace=?).
- واجهة «تتبّع» trace موحّدة تعطي أسباب الاختيار (إحصائي/قواعد KB/تفضيل سياق...).

فوائد عامة: كل أنظمة الاختيار الموزون/المفاضلة (تخطيط، توصية، ألعاب، محاكاة) تستفيد.

مثال مختصر:
```bayan
d = dist({"المدرسة":1.0,"البيت":0.9})
d = d.boost(lambda x: kb_return_direct(subj,x), 1.6).nucleus(0.8).temperature(0.7)
choice, t = sample(d, rng_seed=42, trace=:on)
```

---

### 3) مُركِّبات قيود عامة (Constraint Combinators)
المشكلة الحالية: «تصفية المرشحين» بقواعد KB والحرّاسات مثل no_repeat_ngram/stop_tokens مضمّنة محليًا.

المقترح:
- مكتبة قياسية لحرس/قيود التسلسل:
  - filter_by(predicate)
  - prefer(rule, weight) (تعزيز)
  - guard.no_repeat(ngram=n, key=fn)
  - guard.stop_when(fn) أو stop_tokens({...})
- تُستخدم مع dist/سيرورة توليد دون تقييد بالمجال اللغوي.

مثال عام:
```bayan
cands = dist(candidates)
cands = cands.filter(lambda w: domain_ok(w)).boost(lambda w: rule_ok(w), 1.2)
seq = sequence(seeds=[w1,w2]).with_guard(no_repeat(2)).stop_when(lambda w: w in stops)
```

---

### 4) قواعد صياغة/إخراج تصريحية (Declarative Rewrite Rules)
المشكلة الحالية: قواعد صرفية/إملائية مثل إدراج «الى» أو دمج «ب+ال» مكتوبة كإجراءات.

المقترح:
- DSL صغيرة لتصريح قواعد «إعادة كتابة» عامة بطبقات:
  - rewrite after <pattern> when <cond> do <action>
  - قوالب مطابقة token-level/feature-level، قابلة للتطبيق في أي نطاق إخراج (ليس للغة فقط).

مثال:
```bayan
rule insert_prep:
  after verb in {"عاد","رجع","دخل","ذهب"} when next is Place insert "الى"
rule merge_b_al: replace ["ب","ال", X] -> ["بال", X]
```

---

### 5) سياق/حالة معيارية متعددة النِّطاق (Standard Context/Session)
المشكلة الحالية: احتجنا وحدة dialogue_state يدوية لتخزين آخر كيان/مكان/متحدّث.

المقترح:
- «سياق» Context من الدرجة الأولى مدعوم لغويًا، مع نِطاقات قياسية (process / request / session / user) قابلة للتعشيش.
- معاملات أمان ونطاق حياة واضحة؛ إمكان ربطه بالمنطق/المفسّر.

مثال:
```bayan
with context("dialogue") as ctx:
  ctx.last_place = "المدرسة"
  prefer_place = ctx.last_place or ""
```

فوائد عامة: جلسات ويب، سلاسل حوار، خطوط أنابيب بيانات، إلخ.

---

### 6) «مولد تسلسلي» معياري قابل للتركيب (Composable Sequence Generator)
المشكلة الحالية: منطق التوليد متداخل (n-gram + قيود + تفضيلات + أخذ عينات + قواعد إخراج).

المقترح:
- كائن sequence/generator عام يُبنى بوحدات: مصدر مرشحين → مرشّحات → مُعزِّزات → «مُختار» (sampler) → «قواعد إخراج».
- واجهة صريحة on_step(i, fn) لتخصيص سياسات حسب الخطوة.

مثال:
```bayan
seq = generator(seeds=["سعد","رجع"], steps=2)
seq.on_step(0, lambda pool: pool.prefer(ctx.last_place).via_kb(tok_map))
out = seq.run() |> apply_rules(ar_morpho)
```

---

### 7) عشوائية محكومة بنطاق (Scoped RNG)
المقترح:
- rng(seed){ ... } كتغليف يضمن حتمية داخل النطاق فقط، ويتكامل مع dist/sequence.

مثال:
```bayan
rng(42){ choice = sample(d) }
```

---

### 8) تفسير مُوحّد للقرارات (Unified Explainability)
المقترح:
- معيار تتبّع trace موحّد لأي «اختيار»/«تصفية» يُنتجه dist/sequence/rewrite:
  - المصدر (tri/bi/KB/Rule/Context)
  - الوزن قبل/بعد التعزيز
  - سبب الإقصاء/التفضيل

فوائد عامة: تصحيح/تدقيق/تحليلات.

---

### 9) واجهات استيراد منطقية انتقائية «أكثر سلاسة»
المشكلة الحالية: استدعاء kb.load_selective(...) نمطي.

المقترح:
- صيغة import انتقائية على مستوى المترجم: import kb::prob[*] أو import kb::{prob, entities} مع تحقق ثابت قدر الإمكان.

---

## التوافق العكسي والتنفيذ المرحلي
- المرحلة 1 (سهلة ومؤثرة): exists/first/collect + rng(scoped) + trace موحّد.
- المرحلة 2: dist/sequence كمكتبة قياسية (دون تعديل جوهر المترجم).
- المرحلة 3: DSL «rewrite» (كمحول بعدي اختياري يُستدعى صراحةً).
- المرحلة 4: context مدعوم لغويًا مع نِطاقات حياة وضوابط.
- المرحلة 5: تحسين import الانتقائي المنطقي.

يجب أن تُبنى كل مرحلة بحيث لا تكسر الكود الحالي وتبقى قابلة للاستخدام خارج نطاق NLP.

---

## أمثلة صغيرة متكاملة
```bayan
with context("dialogue") as ctx:
  ctx.last_place = "المدرسة"
  cands = dist({"المدرسة":1.0,"المتحف":0.6})
  cands = cands.prefer(lambda x: x==ctx.last_place, 1.6)
  w, tr = sample(cands.nucleus(0.8).temperature(0.7), rng_seed=7, trace=:on)
  out = ["سعد","رجع", w] |> apply_rules(ar_morpho)
```

```bayan
# جسر منطقي مباشر بلا ?F
ok = exists default_return_target("person","school")
xs = collect isa("x","place"), limit=20
```

```bayan
# قواعد إعادة كتابة عامة
rewrite {
  after verb in {"عاد","رجع"} when next is Place insert "الى"
  replace ["ب","ال", X] -> ["بال", X]
}
```

---

## لماذا في «البيان» نفسها؟
- هذه الأنماط تتكرر في مجالات عديدة (حوارات، توصية، محاكاة، روبوتات، تخطيط).
- رفعها إلى بنية/مكتبة قياسية يقلّل الأكواد المكررة ويرفع القابلية للتركيب والاختبار.
- يُبسّط الربط بين المنطق والاختيار الاحتمالي والتصريف/الإخراج.

## أسئلة مفتوحة
- تصميم DSL «rewrite»: هل تُنفّذ كمحول AST أم مكوّن تشغيل لاحق؟
- تعريف trace الموحّد: ما الحد الأدنى من الحقول؟ كيف نضمن تكلفة تشغيل مقبولة؟
- حراسة النِّطاق لـ context: كيف تُدار في البيئات المتعددة الخيوط/الطلبات؟

(ملاحظة) جميع الأمثلة صياغات مبدئية لتوضيح الفكرة؛ التفاصيل النهائية تُحسم بتصميم أدق واختبارات.

