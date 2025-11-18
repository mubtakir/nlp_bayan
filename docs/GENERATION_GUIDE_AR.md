# دليل التوليد في بيان (Generation Guide)

هذا الدليل يشرح ميزات التوليد الجديدة في بيان وكيفية استعمالها عمليًا داخل كتل hybrid، مع أمثلة قصيرة قابلة للتشغيل.

المحتويات:
- بذرة العشوائية وضبط القابلية لإعادة الإنتاج
- الاختيار الموزون choose / اختر
- أخذ العينات من التوزيعات: uniform / normal / bernoulli / Categorical عبر عامل ~
- التحكم في الاستعلامات المنطقية: once / limit
- مطابقة النصوص: match ... in ... as
- المقارنة التقريبية: ~= / ≈
- دمج التوليد مع ميزات منطقية (collect/topk/argmax)
- ملاحظات وممارسات مفيدة

---

## 1) بذرة العشوائية: seed(N)
- استعمل `seed(N)` داخل hybrid لضبط مولّد الأرقام العشوائية الداخلي.
- نفس البذرة ⇒ نفس تسلسل العينات لاحقًا.

مثال:
```bayan
hybrid {
  seed(123)
  x ~ uniform(0, 1)
  seed(123)
  y ~ uniform(0, 1)
  # هنا x == y لأننا أعدنا نفس البذرة قبل السحب
}
```

---

## 2) الاختيار الموزون — choose / اختر
- صيغة مختصرة لاختيار عنصر واحد وفق أوزان:
- `choose { "A":0.6, "B":0.3, "C":0.1 }`
- `اختر { "انطلق":0.5, "سار":0.3, "ذهب":0.2 }`

مثال سريع:
```bayan
hybrid {
  best = choose { "A":0.0, "B":1.0, "C":0.0 }
  print(best)   # دائمًا "B" هنا
}
```

ملاحظات:
- إذا كانت جميع الأوزان ≤ 0 فالسلوك ي fallback إلى اختيار موحّد (متساوٍ) بين العناصر.
- الأوزان تُحوَّل إلى float؛ يُفضّل استعمال أعداد موجبة ومجموع غير صفري.

---

## 3) أخذ عينات من توزيعات — عامل الإسناد التوليدي `x ~ Dist(args)`
- يدعم حالياً:
  - `uniform(a, b)`
  - `normal(mu, sigma)`
  - `bernoulli(p)`  (يعيد 1 أو 0)
  - `Categorical({...})` أو `categorical({...})` (اختيار من قاموس موزون)

مثال:
```bayan
hybrid {
  seed(42)
  u ~ uniform(0, 1)
  n ~ normal(0, 1)
  b ~ bernoulli(0.7)
  c ~ Categorical({"A": 0.6, "B": 0.3, "C": 0.1})
  print(u)
  print(n)
  print(b)
  print(c)  # سيطبع "A" أو "B" أو "C" حسب الأوزان
}
```

ملاحظات:
- العامل `~` يعمل كإسناد: يقيّم التوزيع ويخزّن الناتج في المتغيّر على يساره.
- `uniform/normal` يعيدان float؛ `bernoulli` يعيد 0 أو 1.
- `Categorical` يختار عنصراً واحداً من القاموس حسب الأوزان (مشابه لـ `choose` لكن كتوزيع).

---

## 4) التحكم في الاستعلامات المنطقية — once / limit

### once (مرة)
- تنفيذ استعلام منطقي **مرة واحدة فقط** (أول حل):
```bayan
hybrid {
  parent("أحمد", "محمد").
  parent("أحمد", "علي").
  parent("محمد", "سارة").

  # استعلام عادي يعيد جميع الحلول
  all_children = collect ?X from parent("أحمد", ?X)
  print(all_children)  # ["محمد", "علي"]

  # استعلام مع once - حل واحد فقط
  once {
    parent("أحمد", ?Y).
    print(?Y)  # سيطبع "محمد" فقط (أول حل)
  }

  # أو كاستعلام مباشر
  once parent("أحمد", ?Z).
  print(?Z)  # "محمد"
}
```

### limit (حد)
- تحديد **عدد الحلول** المطلوبة:
```bayan
hybrid {
  parent("أحمد", "محمد").
  parent("أحمد", "علي").
  parent("أحمد", "سارة").

  # الحصول على أول حلين فقط
  limit 2 {
    parent("أحمد", ?X).
    print(?X)  # سيطبع "محمد" ثم "علي"
  }

  # أو كاستعلام مباشر
  limit 3 parent("أحمد", ?Y).

  # أو مع collect
  first_two = collect ?Z from parent("أحمد", ?Z) limit 2
  print(first_two)  # ["محمد", "علي"]
}
```

---

## 5) مطابقة النصوص — match ... in ... as

صيغة مختصرة لمطابقة نمط في نص واستخراج المتغيرات:

```bayan
hybrid {
  # مثال عربي
  text = "سافر خالد إلى مكة"
  match "سافر {اسم} إلى {مدينة}" in text as m

  if m: {
    who = m["اسم"]
    where = m["مدينة"]
    print(who)    # "خالد"
    print(where)  # "مكة"
  }

  # مثال إنجليزي مع regex
  data = "Temperature: 25.5 degrees"
  match "Temperature: {temp:\\d+\\.\\d+} degrees" in data as result

  if result: {
    temp = result["temp"]
    print(temp)  # "25.5"
  }

  # يمكن استخدام template() أيضاً
  line = "User Ali scored 42"
  tpl = template("User {name} scored {score:\\d+}")
  match tpl in line as m2

  if m2: {
    print(m2["name"])   # "Ali"
    print(m2["score"])  # "42"
  }
}
```

ملاحظات:
- `match pattern in text as var` مكافئ لـ `var = match(pattern, text)`
- يدعم الأنماط العربية والإنجليزية
- يدعم regex داخل `{name:pattern}`
- إذا لم يتطابق النمط، `var` يكون `None`

---

## 6) المقارنة التقريبية — ~= / ≈

مقارنة الأعداد أو النصوص بشكل تقريبي:

```bayan
hybrid {
  # مقارنة أعداد
  x = 3.14159
  y = 3.14160

  if x ~= y: {
    print("متقاربان!")  # سيطبع لأن الفرق < 0.0001 (epsilon الافتراضي)
  }

  # يمكن استخدام الرمز ≈ أيضاً
  if x ≈ y: {
    print("متقاربان!")
  }

  # مقارنة نصوص (تساوي دقيق)
  a = "مرحبا"
  b = "مرحبا"
  if a ~= b: {
    print("متطابقان!")
  }

  # استخدام في سياق عربي
  درجة1 = 98.5
  درجة2 = 98.50001
  if درجة1 ≈ درجة2: {
    print("الدرجتان متقاربتان")
  }
}
```

ملاحظات:
- للأعداد: يتحقق من `abs(a - b) < epsilon` (epsilon الافتراضي = 0.0001)
- للنصوص: يتحقق من التساوي الدقيق
- يدعم الرمزين `~=` و `≈`

---

## 7) التوليد + المنطق (collect/topk/argmax)
يمكنك جمع مرشّحات منطقية ثم أخذ عينة منها:

```bayan
hybrid {
  import bayan.core.similarity as sim
  sim.load_selective(logical, ["similarity"])  # تفعيل حقائق/قواعد التشابه
  أسد(غضنفر:0.8, هيضم:0.5).

  # اجمع أوائل المرشحين
  xs = collect ?Y from similar("أسد", ?Y, ?S, "syn", "lexicon") limit 2 unique

  seed(7)
  r ~ uniform(0, 1)
  i = int(r * len(xs))   # فهرس بسيط من 0..len-1
  pick = xs[i]
  print(pick)
}
```

ملاحظات:
- يمكنك المزج مع `topk/argmax` إذا كان لديك درجات وتريد أخذ أفضل K أولاً ثم العينة منهم.


ملاحظة مستحدثة:
- عند استعمال `argmax/topk` فوق حلول منطقية بدون درجة صريحة (أو كانت غير رقمية)، سيستخدم المفسّر تلقائيًا «احتمال الحل» المجمّع لترتيب النتائج. يمكن دمج ذلك مع عتبات `maybe()/likely()` لتصفية المرشحين قبل الترتيب.

---

## 7.5) التكامل مع الاستدلال الاحتمالي
- حلول المنطق الآن تحمل احتمالًا مركّبًا (ناتج ضرب احتمالات الحقائق عبر سلسلة الإثبات).
- يمكنك استعمال `maybe()/likely()/prob_ge()` لتصفية النتائج قبل `topk/argmax`.
- إذا كانت درجة `?S` غير متاحة أو غير رقمية، سيستعمل `argmax/topk` احتمال الحل تلقائيًا.

مثال قصير:
```bayan
hybrid {
  fact[0.9] link("a","x").
  fact[0.3] link("a","y").

  best = argmax ?Z by ?S where link("a", ?Z)
  strong(?Z) :- link("a", ?Z), likely().  # ≥0.8 فقط

  print(best)
}
```


## 5) ممارسات مفيدة
- دوّن `seed(N)` في أمثلة/اختبارات لضمان التحكّم بسلوك العشوائية.
- عند استعمال choose { … } حافظ على أوزان واضحة ومجموع غير صفري لضمان سلوك بديهي.
- للتجارب التفاعلية، ضع print(...) على القيم المولَّدة لتتبّع السلوك بسرعة.

---

انظر أيضًا:
- قسم “التوليد وأخذ العينات” في دليل اللغة العام (LANGUAGE_GUIDE.md)
- أمثلة IDE:
  - examples/choose_weighted.md
  - examples/distributions_sampling.md
  - examples/probabilistic_facts.md
  - examples/template_matching.md

اختبارات الميزات الجديدة:
  - tests/test_once_limit.py - اختبارات once و limit
  - tests/test_categorical.py - اختبارات Categorical distribution
  - tests/test_approx_eq_operator.py - اختبارات ~= و ≈
  - tests/test_match_in_as.py - اختبارات match ... in ... as
