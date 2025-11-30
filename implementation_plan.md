# خطة تطوير نظام الصرف العربي (Arabic Morphology Expansion)

## الهدف
توسيع قدرات المعالجة الصرفية العربية في `ai/morphology.bayan` باستخدام مكتبة `camel-tools` المفتوحة المصدر (إذا توفرت) مع الحفاظ على تنفيذ احتياطي (Fallback) بلغة Bayan، لتلبية ملاحظات المطورين وجعل النظام أكثر قوة وواقعية.

## التغييرات المقترحة

### 1. التكامل مع `camel-tools` (Python Integration)
*   **تعديل `bayan/bayan/hybrid_interpreter.py`**:
    *   محاولة استيراد `camel_tools`.
    *   إضافة دوال native (`native_conjugate`, `native_extract_root`) إلى بيئة Bayan إذا كانت المكتبة متوفرة.
    *   إضافة متغير `HAS_ADVANCED_MORPHOLOGY` للتحقق من التوفر.

### 2. تحسين تصريف الأفعال (`conjugate_arabic_verb`)
*   **تحديث `ai/morphology.bayan`**:
    *   استخدام `native_conjugate` إذا كان `HAS_ADVANCED_MORPHOLOGY` صحيحاً.
    *   **الخطة الاحتياطية (Fallback)**: تحسين التنفيذ اليدوي الحالي لدعم:
        *   المثنى (Dual).
        *   صيغة الأمر (Imperative).

### 2. إضافة نظام الجذور والأوزان (Roots & Patterns) - [جديد]
*   **دالة `apply_pattern(root, pattern)`**:
    *   تأخذ جذراً ثلاثياً (مثل "كتب") ووزناً (مثل "فاعل").
    *   تنتج الكلمة (مثل "كاتب").
    *   دعم الأوزان الشائعة: فاعل، مفعول، فعّال، افتعل، استفعال، إلخ.

### 4. استخراج الجذور (Root Extraction) - [جديد]
*   **دالة `extract_root(word)`**:
    *   استخدام `native_extract_root` (عبر `camel-tools`) إذا توفرت.
    *   تحسين الخوارزمية اليدوية (Heuristic) كبديل.

### 4. التكامل مع المنطق (Logic Integration)
*   إضافة أمثلة توضح كيف يمكن استخدام هذه الدوال داخل القواعد المنطقية (Logical Rules).

## ملفات للتعديل
*   `ai/morphology.bayan`
*   `bayan/bayan/hybrid_interpreter.py`

## خطة التحقق
1.  إنشاء سكريبت اختبار `tests/test_morphology.bayan`.
2.  تجربة توليد كلمات مختلفة من جذور مختلفة.
3.  التحقق من صحة التصريفات الجديدة.
