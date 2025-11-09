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
- roc_curve(y_true, y_scores, pos_label=1) → [fprs, tprs, thresholds]
- auc_roc(fprs, tprs)
- k_means_pp_prob(data, k, max_iters=10, seed=42)

Arabic wrappers (new):
- توقع_انحدار_لوجستي_احتمال(س, اوزان, انحياز)
- مصفوفة_الالتباس(الحقيقة, التوقع)
- منحنى_ROC(حقيقة, درجات)
- مساحة_ROC(معدلات_موجبة_كاذبة, معدلات_حقيقية_موجبة)
- تجميع_كي_مينز_PP_احتمالي(بيانات, ك, مرات=10, بذرة=42)

- k_means(data, k, max_iters=10) → [centers, labels]

## 🧮 Data Module (ai.data)

- random_permutation(n, seed=42)
- train_test_split_shuffle(X, y, test_ratio=0.25, seed=42)

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
- TF–IDF مبسَّط (بدون log)، والـ KNN/K-means/LogReg نسخ تعليمية

---

## 🗺️ Roadmap — خارطة الطريق
- NLP: stopwords عربية/إنجليزية، تجذيع/تطبيع عربي، n-grams متقدّم، cosine similarity
- ML: metrics (precision/recall/F1)، train/test split، k-means++، regularization
- Data: CSV/JSON I/O، وصف إحصائي (mean/var/std)
- Vision: تمارين فلاتر بسيطة بمصفوفات بكسل رمزية للتعليم

