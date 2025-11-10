# 📚 Bayan AI Library Guide — دليل مكتبة الذكاء (AI)

The Bayan standard AI library provides simple, bilingual (AR/EN) building blocks for learning and teaching AI/ML concepts entirely inside Bayan.

> الهدف: وظائف تعليمية عملية وسهلة، بواجهات عربية وإنجليزية.

---

## 🚀 Quick Start — البداية السريعة

```bayan
hybrid {
  # English
  from ai.ml import linear_regression, k_means
  lr = linear_regression([1,2,3,4,5], [2,4,6,8,10])  # [slope, intercept]
  res = k_means([[0,0],[0,1],[10,10],[10,11]], 2, 10)
}
```

```bayan
hybrid {
  # العربية
  import ai.nlp as nlp
  ن = nlp.تجهيز_نص("المنتج رائع جدًا وسعره مناسب")
  م = nlp.كشف_مشاعر("هذا المنتج ممتاز ورائع")  # يعيد "إيجابي"/"سلبي"/"محايد"
}
```

---

## 🧠 NLP Module (ai.nlp)

- detect_language(text)
- remove_punctuation(text)
- preprocess_text(text, language="auto")
- tokenize_text(text, language="auto")
- detect_sentiment(text) → "positive" | "negative" | "neutral" (toy)
- ngrams_from_tokens(tokens, n)
- compute_tfidf(docs: [str]) → [dict(term→score)]


New (v2):
- remove_stopwords(text, language="auto")
- cosine_similarity_dicts(v1, v2)
- naive_bayes_train_text(docs, labels, alpha=1.0)
- naive_bayes_predict_text(model, doc)
- naive_bayes_predict_proba_text(model, doc)

Arabic wrappers (new):
- إزالة_كلمات_شائعة(نص, لغة="auto")
- تشابه_جيبي_قاموسي(قاموس1, قاموس2)
- تدريب_نايف_بايز_نص(نصوص, تسميات, ألفا=1.0)
- توقع_نايف_بايز_نص(نموذج, نص)
- احتمال_نايف_بايز_نص(نموذج, نص)


New (v4):
- bigram_lm_train(docs, alpha=1.0)
- bigram_lm_probability(model, w1, w2)
- bigram_lm_predict_next(model, w1, top_n=3)

Arabic wrappers (v4):
- تدريب_ثنائي_الكلمات(نصوص, ألفا=1.0)
- احتمال_ثنائي_الكلمات(نموذج, كلمة1, كلمة2)
- أفضل_التالي_ثنائي(نموذج, كلمة, أعلى=3)


New (v5):
- compute_tfidf_log_norm(docs)
- char_ngrams(text, n_min, n_max)
- trigram_lm_train(docs, alpha=1.0)
- trigram_lm_probability(model, w1, w2, w3)
- trigram_lm_predict_next(model, w1, w2, top_n=3)
- remove_stopwords_extended(text, language="auto")

Arabic wrappers (v5):
- تدريب_ثلاثي_الكلمات(نصوص, ألفا=1.0)
- احتمال_ثلاثي_الكلمات(نموذج, كلمة1, كلمة2, كلمة3)
- أفضل_التالي_ثلاثي(نموذج, كلمة1, كلمة2, أعلى=3)
- محارف_انجرام(نص, ادنى, اقصى)
- إزالة_كلمات_شائعة_موسعة(نص, لغة="auto")


New (v6):
- compute_tfidf_options(docs, sublinear_tf=True, smooth_idf=True)

Arabic wrappers (v6):
- حساب_tfidf_خيارات(نصوص, فرعي=True, تمهيد=True)


New (v7):
- bm25_build(docs, k1=1.5, b=0.75)
- bm25_score(model, qtext)
- jaccard_similarity(list1, list2)
- compute_tfidf_vocab_limit(docs, max_features, sublinear_tf=True, smooth_idf=True)

New (v8):
- dice_similarity(list1, list2)


New (v12):
- cosine_similarity(list1, list2)
- similarity(list1, list2, metric)
- bm25_score_with_term_weights(model, qtext, weights)

Arabic wrappers (v12):
- تشابه_جيبي(قائمة1, قائمة2)


New (v13):
- tfidf_cosine_similarity(text1, text2)
- bm25_top_k(model, qtext, k=5)

Arabic wrappers (v13):
- تشابه_جيبي_TFIDF(نص1, نص2)
- أفضل_BM25(نموذج, استعلام, ك=5)

ML additions (v13):
- adaboost_train(X, y, n_estimators=10)
- adaboost_predict(model, X)

Arabic wrappers (v13 ML):
- تدريب_ادابوست(س, ت, عدد_مصنفات=10)
- توقع_ادابوست(نموذج, س)


New (v14):
- lcs_length(s1, s2)
- jaccard_char_ngrams(text1, text2, n=3)

Arabic wrappers (v14):
- طول_LCS(نص1, نص2)
- جاكارد_محارف(نص1, نص2, ن=3)

ML additions (v14):
- naive_bayes_train(docs_tokens, y, alpha=1.0)
- naive_bayes_predict(model, docs_tokens)

Arabic wrappers (v14 ML):
- تدريب_بايز_متعدد(وثائق, تسميات, ألفا=1.0)
- توقع_بايز_متعدد(نموذج, وثائق)



New (v15):
- jaro_similarity(s1, s2)
- jaro_winkler_similarity(s1, s2, p=0.1, max_prefix=4)
- dice_char_ngrams(text1, text2, n=2)

Arabic wrappers (v15):
- تشابه_جارو(نص1, نص2)
- تشابه_جارو_وينكلر(نص1, نص2, معامل=0.1, حد_بادئة=4)
- دايس_محارف(نص1, نص2, ن=2)


New (v16):
- damerau_levenshtein_distance(s1, s2)

Arabic wrappers (v16):
- مسافة_دامراو_ليفنشتاين(نص1, نص2)


Arabic wrappers:
- تجهيز_نص(نص, لغة="auto")
- تجزئة_نص(نص, لغة="auto")
- كشف_مشاعر(نص)
- حساب_tfidf(نصوص)

Notes:
- TF–IDF هنا بدون لوغاريتم (لاستخدام أوسع داخل المفسر)، الصيغة: idf = 1 + N/(df+1)
- التقطيع وتقليل الترقيم بسيطان؛ مناسب للتعليم والأمثلة السريعة

---

## 📈 ML Module (ai.ml)

- linear_regression(x: [num], y: [num]) → [slope, intercept]
- k_nearest_neighbors_predict(train_X, train_y, samples, k=3) → labels

New (v2):
- logistic_regression_predict_proba(X, w, b)
- confusion_matrix(y_true, y_pred, pos_label=1, neg_label=0)


New (v5):
- k_fold_cross_val_accuracy(X, y, model, k_folds, lr, epochs, k_neighbors, shuffle=True, seed=42)

New (v4):
- accuracy_score(y_true, y_pred)
- confusion_matrix_multi(y_true, y_pred, labels)
- classification_report(y_true, y_pred, labels)

New (v6):
- decision_tree_train(X, y, max_depth=3, criterion="gini", min_samples_split=2)
- decision_tree_predict(tree, X)

Arabic wrappers (v6):
- تدريب_شجرة_قرار(س, ت, عمق=3, معيار="gini", حد_تقسيم=2)
- توقع_شجرة_قرار(شجرة, س)

New (v7):
- perceptron_train(X, y, lr=1.0, epochs=20) / perceptron_predict(X, w, b)
- perceptron_ovr_train(X, y, lr=1.0, epochs=20) / perceptron_ovr_predict(model, X)
- k_nearest_neighbors_weighted_predict(train_X, train_y, samples, k=3)
- random_forest_train(X, y, n_trees=5, max_depth=3, min_samples_split=2, feature_ratio=1.0, sample_ratio=1.0, criterion="gini", seed=42)
- random_forest_predict(model, X)

Arabic wrappers (v7):
- تدريب_بيرسبترون(س, ت, lr=1.0, epochs=20) / توقع_بيرسبترون(س, اوزان, انحياز)
- توقع_KNN_موزون(بيانات, تسميات, عينات, ك=3)

New (v8):
- linear_svm_train(X, y, lr=0.1, epochs=50, C=1.0)
- linear_svm_predict(X, w, b)

Arabic wrappers (v8):
- تدريب_SVM_خطي(س, ت, lr=0.1, epochs=50, C=1.0)
- توقع_SVM_خطي(س, اوزان, انحياز)

- تدريب_غابة_عشوائية(س, ت, عدد_أشجار=5, أقصى_عمق=3, حد_تقسيم=2, نسبة_ميزات=1.0, نسبة_عينات=1.0, معيار="gini", بذرة=42)
- توقع_غابة_عشوائية(نموذج, س)

- k_fold_evaluate_logistic(X, y, k=5, lr=0.1, epochs=200)
- k_fold_evaluate_knn(X, y, k_folds=5, k_neighbors=3)

Arabic wrappers (v4):
- دقة(حقيقة, توقع)
- مصفوفة_الالتباس_متعددة(حقيقة, توقع, تسميات)


- تقرير_تصنيف(حقيقة, توقع, تسميات)
- تقييم_طي_تقاطعي_لوجستي(س, ت, ك=5)
- تقييم_طي_تقاطعي_KNN(س, ت, طيات=5, جيران=3)

- roc_curve(y_true, y_scores, pos_label=1) → [fprs, tprs, thresholds]
- auc_roc(fprs, tprs)
- k_means_pp_prob(data, k, max_iters=10, seed=42)

Arabic wrappers (new):

New (v7):
- quantiles(xs, qs)
- iqr(xs)
- pearson_r(xs, ys)
- minmax_normalize(xs)

Arabic wrappers (v7):
- نسب_مئوية_متعددة(قائمة, نسب)
- مدى_ربيعي(قائمة)
- ارتباط_بيرسون(س, ص)
- تطبيع_أدنى_أقصى(قائمة)

New (v16):
- stratified_k_fold_indices(y, k, shuffle=True, seed=42)
- train_test_split_stratified(X, y, test_ratio=0.25, shuffle=True, seed=42)
- matthews_corrcoef(y_true, y_pred, pos_label=1, neg_label=0)
- cohen_kappa_score(y_true, y_pred, labels)

Arabic wrappers (v16):
- تقسيم_طي_تقاطعي_طبقي_مؤشرات(ت, ك, عشوائي=True, بذرة=42)


- توقع_انحدار_لوجستي_احتمال(س, اوزان, انحياز)
- مصفوفة_الالتباس(الحقيقة, التوقع)
- منحنى_ROC(حقيقة, درجات)
- مساحة_ROC(معدلات_موجبة_كاذبة, معدلات_حقيقية_موجبة)
- تجميع_كي_مينز_PP_احتمالي(بيانات, ك, مرات=10, بذرة=42)

- k_means(data, k, max_iters=10) → [centers, labels]

## 🧮 Data Module (ai.data)

New (v5):
- parse_csv_rows(lines, delimiter=",") / to_csv_rows(rows, delimiter=",")
- read_csv_string(text, delimiter=",") / write_csv_string(rows, delimiter=",")
- mean(xs), variance(xs), stddev(xs), median(xs), percentile(xs, p)
- read_json_string(text)

New (v6):
- min_value(xs), max_value(xs), data_range(xs)
- zscore_normalize(xs)

Arabic wrappers (v6):
-     ( )
-     ( )
-    ( )
-     _Z( )

Arabic wrappers (v6) — corrected:
- أدنى(قائمة)
- أقصى(قائمة)
- مجال(قائمة)

New (v8):
- standard_scaler_fit(xs) / standard_scaler_transform(xs, mean, std)
- robust_scaler_fit(xs) / robust_scaler_transform(xs, median, iqr)
- minmax_scaler_fit(xs) / minmax_scaler_transform(xs, lo, hi)

Arabic wrappers (v8):
- ملاءمة_قياسي(قائمة) / تحويل_قياسي(قائمة, متوسط, انحراف)
- ملاءمة_قوي(قائمة) / تحويل_قوي(قائمة, وسيط_قيمة, مدى_ربيعي_قيمة)
- ملاءمة_أدنى_أقصى(قائمة) / تحويل_أدنى_أقصى(قائمة, أدنى, أقصى)

- تطبيع_Z(قائمة)


- write_json_array_string(lst), write_json_object_string(obj)


Arabic wrappers (v5) — encoding artifact (ignore):
-    _CSV_ ( , ",") /    _CSV_ ( , ",")
-    _CSV_ ( , ",") /    _CSV_ ( , ",")
-      (قائمة),      (قائمة),      _     (قائمة),    ( ),    ( ,  )

Arabic wrappers (v5) — corrected:
- قراءة_JSON_نص(نص)
- كتابة_JSON_قائمة(قائمة), كتابة_JSON_كائن(كائن)

- قراءة_CSV_سطور(سطور, ",") / كتابة_CSV_سطور(صفوف, ",")
- قراءة_CSV_نص(نص, ",") / كتابة_CSV_نص(صفوف, ",")
- متوسط(قائمة), تباين(قائمة), انحراف_معياري(قائمة), وسيط(قائمة), مئين(قائمة, نسبة)



- random_permutation(n, seed=42)
- train_test_split_shuffle(X, y, test_ratio=0.25, seed=42)


New (v4):
- set_seed(seed)
- rand()
- randint(a, b)
- shuffle_list(lst)
- sample_list(lst, k)

Arabic wrappers (v4):
- تعيين_بذرة(بذرة)
- عشوائي_0_1()
- عشوائي_صحيح_بين(أ, ب)
- خلط_قائمة(قائمة)
- عينة_من_قائمة(قائمة, ك)

Arabic wrappers:
- ترتيب_عشوائي(n, بذرة=42)
- تقسيم_عشوائي_تدريب_اختبار(س, ت, نسبة_اختبار=0.25, بذرة=42)

## 👁️ Vision Module (ai.vision)

- conv2d_valid_3x3(image, kernel)
- sobel_edges(image)  → magnitude image

Arabic wrappers:
- التفاف3x3_صحيح(صورة, مرشح)
- سوبل_حواف(صورة)

- logistic_regression_train(X, y, lr=0.1, epochs=200) → [weights, bias]
- logistic_regression_predict(X, weights, bias, threshold=0.5) → [0/1,...]

Arabic wrappers:
- انحدار_خطي(س, ص)
- توقع_k_متجاور_أقرب(بيانات, تسميات, عينات, k=3)
- تجميع_كي_مينز(بيانات, ك, مرات=10)
- تدريب_انحدار_لوجستي(س, ت, lr=0.1, epochs=200)
- توقع_انحدار_لوجستي(س, اوزان, انحياز, threshold=0.5)

Notes:
- تم استخدام pow(e, -z) بدل exp() لعدم الحاجة لاعتماد خارجي

```bayan
hybrid {
  # Bigram LM (train and predict)
  import ai.nlp as nlp
  model = nlp.bigram_lm_train(["this is fine", "this is good"])
  top = nlp.bigram_lm_predict_next(model, "is", 2)
}
```

```bayan
hybrid {
  # Multi-class report
  import ai.ml as ml
  y_true = [0,1,2,1,0,2]
  y_pred = [0,2,2,1,0,1]
  rep = ml.classification_report(y_true, y_pred, [0,1,2])
}
```

- المسافات في k-means هي مسافة إقليدية مربعة (بدون جذر) للمقارنة فقط

---

## 📋 Examples — أمثلة

```bayan
hybrid {
  # Linear regression
  from ai.ml import linear_regression
  m_b = linear_regression([1,2,3], [2,4,6])
  m = m_b[0]; b = m_b[1]
}
```

```bayan
hybrid {
  # KNN
  from ai.ml import k_nearest_neighbors_predict
  preds = k_nearest_neighbors_predict([[0,0],[10,10]], ["A","B"], [[1,1],[9,9]], 1)
}
```

```bayan
hybrid {
  # TF–IDF
  import ai.nlp as nlp
  docs = ["This is excellent", "This is bad"]
  vecs = nlp.compute_tfidf(docs)
}
```

```bayan
hybrid {
  # Logistic regression
  from ai.ml import logistic_regression_train, logistic_regression_predict
  X = [[0],[1],[2],[3]]
  y = [0,0,1,1]
  model = logistic_regression_train(X, y, 0.5, 300)
  w = model[0]; b = model[1]
  preds = logistic_regression_predict([[0.5],[2.5]], w, b, 0.5)
}
```

---

## ⚠️ Limitations — حدود حالية
- الأداء غير مُحسَّن لمجموعات بيانات كبيرة (تعليمي بالدرجة الأولى)
- لا توجد اعتماديات خارجية (NumPy/SciPy)، كل شيء مكتوب ببيان
- TF–IDF الأساسي متوفر مع نسخ لوغاريتمية ومعيارية L2؛ وخوارزميات KNN/K-means/LogReg نسخ تعليمية

---

## 🗺️ Roadmap — خارطة الطريق
- NLP: stopwords عربية/إنجليزية، تجذيع/تطبيع عربي، n-grams متقدّم، cosine similarity
- ML: metrics (precision/recall/F1)، train/test split، k-means++، regularization
- Data: CSV/JSON I/O، وصف إحصائي (mean/var/std)
- Vision: تمارين فلاتر بسيطة بمصفوفات بكسل رمزية للتعليم



---

## 🔄 Update (v9) — November 2025

### NLP (ai.nlp)
- New (v9):
  - overlap_coefficient(list1, list2) → تشابه قائم على تقاطع المجموعتين مقسوماً على أصغر الحجمين.

### ML (ai.ml)
- New (v9):
  - linear_svm_ovr_train(X, y, lr=0.1, epochs=50, C=1.0)
  - linear_svm_ovr_predict(model, X)
  - bagging_train(X, y, n_estimators=5, max_depth=3, min_samples_split=2, sample_ratio=1.0, seed=42)
  - bagging_predict(model, X)
- Arabic wrappers:
  - تدريب_SVM_OVR(س, ت, ...)، توقع_SVM_OVR(نموذج, س)
  - تدريب_باغينغ(...), توقع_باغينغ(...)
- Notes:
  - OvR يُدرِّب مصنِّف SVM ثنائي لكل فئة ويختار أعلى درجة.
  - Bagging هنا تعليمي (قواعد قرار بسيطة/عتبات) دون تجزئة ميزات؛ مناسب لبيانات تعليمية صغيرة.

### Data (ai.data)
- New (v9):
  - bin_equal_width(xs, bins)
  - one_hot_encode(indices, num_classes)
- Arabic wrappers:
  - تجزئة_عرض_متساوي(قائمة, صناديق)
  - ترميز_واحد_ساخن(فهارس, عدد_فئات)


## Wave 10 — Data Encoders (fit/transform)

- label_encoder_fit(xs)
- label_encoder_transform(xs, vocab)
- frequency_encoder_fit(xs)
- frequency_encoder_transform(xs, freqs)
- target_encoder_fit(xs, ys)
- target_encoder_transform(xs, enc)

Arabic wrappers:
- ملاءمة_ترميز_تسميات(قائمة)
- تحويل_ترميز_تسميات(قائمة, مفردات)
- ملاءمة_ترميز_تكرار(قائمة)
- تحويل_ترميز_تكرار(قائمة, تكرارات)
- ملاءمة_ترميز_هدفي(قيم, أهداف)
- تحويل_ترميز_هدفي(قيم, مشفر)


## Wave 11 — NLP Enhancements

- levenshtein_distance(s1, s2)

Arabic wrappers:
- مسافة_ليفنشتاين(نص1, نص2)

### Handoff status
- Waves 1–16: complete, 364 tests passing.
- All Wave 9–16 tests are passing.
