# 🤖 المساعد الذكي للبرمجة - AI Code Assistant

## نظرة عامة

المساعد الذكي للبرمجة هو نظام ذكاء اصطناعي مدمج في محرر البيان (Web IDE) يساعد المبرمجين على:
- فهم الأخطاء وإصلاحها
- إكمال الكود تلقائياً
- تحسين أداء الكود
- توليد كود من وصف طبيعي

---

## 📋 واجهة برمجة التطبيقات (API)

### 1️⃣ حالة المساعد

```http
GET /api/ai/status
```

**الاستجابة:**
```json
{
  "available": true,
  "features": ["completion", "error_explain", "optimization", "analysis", "generation"]
}
```

---

### 2️⃣ شرح الأخطاء

```http
POST /api/ai/explain-error
Content-Type: application/json

{
  "error": "NameError: name 'x' is not defined",
  "code": "print(x)"
}
```

**الاستجابة:**
```json
{
  "error_type": "NameError",
  "explanation": "المتغير 'x' غير معرّف. تأكد من تعريفه قبل استخدامه.",
  "fix": "قم بتعريف المتغير أولاً: x = قيمة",
  "example": "x = None  # أو القيمة المناسبة\n# ثم استخدم x",
  "concepts": ["المتغيرات", "نطاق المتغيرات"]
}
```

---

### 3️⃣ تحليل الكود

```http
POST /api/ai/analyze
Content-Type: application/json

{
  "code": "def test():\n    for i in range(len(items)):\n        print(items[i])"
}
```

**الاستجابة:**
```json
{
  "lines": 3,
  "functions": 1,
  "classes": 0,
  "imports": 0,
  "complexity": 1.36,
  "language": "python",
  "issues": [
    {"type": "debug", "line": 3, "message_ar": "تأكد من إزالة print للتصحيح"}
  ],
  "suggestions": [
    {"title": "استخدم enumerate()", "description": "enumerate أسرع وأوضح"}
  ]
}
```

---

### 4️⃣ تحسين الكود

```http
POST /api/ai/optimize
Content-Type: application/json

{
  "code": "for i in range(len(items)):\n    print(items[i])"
}
```

**الاستجابة:**
```json
{
  "suggestions": [
    {
      "text": "for i, item in enumerate(items):\n    print(item)",
      "type": "optimization",
      "confidence": 0.9,
      "description_ar": "استخدم enumerate() بدلاً من range(len())"
    }
  ]
}
```

---

### 5️⃣ توليد الكود

```http
POST /api/ai/generate
Content-Type: application/json

{
  "description": "أنشئ دالة لحساب مجموع قائمة أرقام"
}
```

**الاستجابة:**
```json
{
  "code": "def my_function():\n    \"\"\"أنشئ دالة لحساب مجموع قائمة أرقام\"\"\"\n    pass\n    return None\n"
}
```

---

### 6️⃣ المحادثة الذكية

```http
POST /api/ai/chat
Content-Type: application/json

{
  "message": "مرحباً، كيف يمكنني البدء؟"
}
```

**الاستجابة:**
```json
{
  "response": "🤖 **المساعد الذكي للبرمجة**\n\nأستطيع مساعدتك في:\n• شرح الأخطاء\n• توليد كود\n• تحليل كود\n..."
}
```

---

## 💻 الاستخدام في Python

```python
from extensions import AICodeAssistant

assistant = AICodeAssistant(language="ar")

# شرح خطأ
error = assistant.explain_error("NameError: name 'x' is not defined")
print(error.explanation)

# تحليل كود
analysis = assistant.analyze_code("def test(): pass")
print(f"عدد الدوال: {analysis.functions_count}")

# توليد كود
code = assistant.generate_code("أنشئ دالة للجمع")
print(code)
```

---

## 🎯 الأخطاء المدعومة

| نوع الخطأ | الشرح |
|-----------|-------|
| `NameError` | متغير غير معرّف |
| `SyntaxError` | خطأ في بناء الجملة |
| `TypeError` | خطأ في نوع البيانات |
| `IndexError` | فهرس خارج النطاق |
| `KeyError` | مفتاح غير موجود |
| `ValueError` | قيمة غير صالحة |
| `AttributeError` | خاصية غير موجودة |
| `ZeroDivisionError` | قسمة على صفر |
| `ImportError` | فشل الاستيراد |
| `IndentationError` | خطأ في المسافات البادئة |

---

**الإصدار:** 0.6.0  
**التاريخ:** 2025-12-06

