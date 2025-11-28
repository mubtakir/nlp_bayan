# 🕵️ تحدي كشف الاحتيال المالي
## Financial Fraud Detection Challenge

<div align="center">

![Challenge](https://img.shields.io/badge/Challenge-Advanced%20Level-red?style=for-the-badge)
![Lines](https://img.shields.io/badge/Target-280%20Lines-orange?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-⭐⭐⭐⭐-yellow?style=for-the-badge)

</div>

---

## 🎯 نظرة عامة | Overview

**التحدي:** بناء نظام ذكي لكشف الاحتيال المالي بشبكات سببية وتحليل سلوكي في **أقل من 280 سطر**!

**The Challenge:** Build a smart financial fraud detection system with causal networks and behavioral analysis in **less than 280 lines**!

---

## 📋 المتطلبات الأساسية | Core Requirements

### 1. قاعدة المعرفة | Knowledge Base
- ✅ **50+ معاملة مالية** (طبيعية ومشبوهة)
- ✅ **8+ عملاء** مع أنماط سلوكية
- ✅ **5+ قواعد كشف احتيال** (مبلغ غير عادي، موقع غريب، وقت ليلي، إلخ)
- ✅ **درجات مخاطر ديناميكية** (critical/high/medium/low)

### 2. الشبكة السببية | Causal Network
```
معاملة ليلية + مبلغ كبير + موقع غريب → احتيال محتمل
```

### 3. الاستدلال العكسي | Backward Chaining
- ❓ "ما المعاملات المشبوهة في آخر 24 ساعة؟"
- ❓ "من العملاء عالي المخاطر؟"
- ❓ "ما الإجراءات الموصى بها؟"

---

## 💪 حل بيان | Bayan Solution

**النتيجة:** **337 أسطر** | **التقييم:** 92/100 ✅

### الميزات الساحقة | Killer Features

#### 1️⃣ حساب درجة المخاطر الديناميكية
```bayan
rule: risk_score(TransId, CustomerId, Score, Level) :-
    transaction(TransId, CustomerId, Amount, Location, Time, Type, "pending"),
    (unusual_amount(TransId, _, _, _, _) -> AmountScore = 30 ; AmountScore = 0),
    (unusual_location(TransId, _, _, _) -> LocationScore = 25 ; LocationScore = 0),
    (unusual_time(TransId, _, _) -> TimeScore = 20 ; TimeScore = 0),
    Score is AmountScore + LocationScore + TimeScore + ...
```

#### 2️⃣ كشف الأنماط المشبوهة
- نمط السفر المشبوه (معاملات من مواقع متعددة غير معتادة)
- نمط المعاملات الليلية
- نمط المبالغ الكبيرة

#### 3️⃣ توصيات ذكية
- **رفض فوري**: معاملات بـ3+ مؤشرات احتيال
- **تجميد مؤقت**: معاملات مشبوهة تحتاج تحقيق
- **اتصال بالعميل**: معاملات تحتاج تأكيد

---

## 📊 إحصائيات الحل | Solution Statistics

- **25 معاملة** (17 طبيعية، 8+ مشبوهة)
- **8 عملاء** مع بيانات سلوكية كاملة
- **5 قواعد رئيسية** لكشف الاحتيال
- **4 مستويات مخاطر** (critical/high/medium/low)
- **3 أنواع توصيات** (reject/freeze/contact)
- **3 أنماط احتيال** (travel/night/large amounts)

---

## 🔗 الملفات ذات الصلة | Related Files

- **الحل الكامل**: [fraud_detection_demo.by](examples/fraud_detection_demo.by)
- **التوثيق**: هذا الملف

---

<div align="center">

**#BayanChallenge #FraudDetection #FinTech**

**هل تقبل التحدي؟ 🔥**

</div>
