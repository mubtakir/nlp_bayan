# مكتبات بيان - Bayan Libraries

هذا المجلد يحتوي على مكتبات بيان القياسية والمجالية.

This folder contains Bayan's standard and domain-specific libraries.

---

## المكتبات المتاحة - Available Libraries

### 1. مكتبة مجال الحياة - Life Domain Library

**الملف**: `life_domain.by`

**الوصف**: مكتبة شاملة تطبق النموذج الوجودي العام على مجال الكائنات الحية في بيئاتها الطبيعية.

**Description**: A comprehensive library that applies the Generic Existential Model to the domain of living beings in their natural environments.

**المحتويات - Contents**:
- ✅ تعريف مجال الحياة (Life Domain Definition)
- ✅ البيئة الطبيعية (Natural Environment)
- ✅ العلاقات المجالية (Domain Relations): حب، تعاون، تفاعل، يسكن، يتأثر_بـ
- ✅ الأفعال المجالية (Domain Actions): أكل، نمو، تواصل
- ✅ المعانٍ المجازية (Metaphorical Meanings): عدالة، نقاش، حرية، سعادة
- ✅ القوانين المجالية (Domain Laws): قانون_دورة_الحياة، قانون_البقاء، قانون_الظل
- ✅ أمثلة على كائنات حية (Living Being Examples): إنسان، شجرة

**الاستخدام - Usage**:

```bayan
# استيراد المكتبة
import "bayan/libraries/life_domain.by"

# الآن يمكنك استخدام مجال الحياة
كائن_وجودي "علي" من_نوع "كائن_حي" في_مجال "الحياة":
{
    "بيئة": "بيئة_طبيعية",
    "خصائص_ذاتية": {
        "عمر": 25,
        "جنس": "ذكر"
    },
    "معانٍ_موروثة": ["فوق", "تحت", "قبل", "بعد"],
    "معانٍ_ذاتية": ["تفكير", "إبداع"],
    "علاقات": {
        "حب": ["أسرة"],
        "تعاون": ["أصدقاء"]
    }
}

# استعلام عن الكائنات
كائنات_واعية = استعلام_وجودي:
{
    "في_مجال": "الحياة",
    "عن": "كائن_حي",
    "شروط": {"وعي": "عالي"}
}
```

**الفلسفة - Philosophy**:

الكائن الحي لا يُفهم بمعزل عن بيئته. كل كائن حي:
- يوجد في بيئة طبيعية لها خط أفق، أرض، سماء، ضوء
- يرث معانٍ مكانية (فوق، تحت، يمين، يسار، ...)
- يرث معانٍ زمانية (قبل، بعد، أثناء، الآن)
- له معانٍ حياتية (انبثاق، حياة، نمو، موت، ...)
- له علاقات مع غيره (حب، ود، نفور، تعاون، ...)
- له علاقات مع نفسه (ضحك، بكاء، تكلم، تفكر)
- له علاقات مع البيئة (يسكن، ينتقل_إلى، يتأثر_بـ)

A living being cannot be understood in isolation from its environment. Every living being:
- Exists in a natural environment with horizon, earth, sky, light
- Inherits spatial meanings (above, below, left, right, ...)
- Inherits temporal meanings (before, after, during, now)
- Has life meanings (emergence, life, growth, death, ...)
- Has relations with others (love, affection, aversion, cooperation, ...)
- Has relations with self (laugh, cry, speak, think)
- Has relations with environment (inhabits, moves_to, affected_by)

---

## كيفية إنشاء مكتبة مجالية جديدة - How to Create a New Domain Library

### الخطوات - Steps

1. **حدد المجال** - Define the domain
   - ما هو الكائن الأساسي؟ (What is the basic entity?)
   - ما هي البيئة؟ (What is the environment?)
   - ما هي المعانٍ الأساسية؟ (What are the basic meanings?)

2. **عرّف المجال** - Define the domain
   ```bayan
   مجال "اسم_المجال":
   {
       "كائن_أساسي": "...",
       "بيئة": "...",
       "معانٍ_أساسية": [...],
       "علاقات": [...],
       "خصائص": [...]
   }
   ```

3. **عرّف البيئة** - Define the environment
   ```bayan
   بيئة "اسم_البيئة" في_مجال "اسم_المجال":
   {
       "أبعاد": {
           "مكاني": [...],
           "زماني": [...],
           "مجالي": [...]
       }
   }
   ```

4. **عرّف الكائنات** - Define beings
   ```bayan
   كائن_وجودي "اسم" من_نوع "نوع" في_مجال "اسم_المجال":
   {
       "خصائص_ذاتية": {...},
       "معانٍ_موروثة": [...],
       "معانٍ_ذاتية": [...],
       "علاقات": {...},
       "أفعال": {...}
   }
   ```

5. **عرّف العلاقات والأفعال** - Define relations and actions

6. **عرّف المعانٍ المجازية** - Define metaphorical meanings

7. **عرّف القوانين** - Define laws

### أمثلة على مجالات ممكنة - Examples of Possible Domains

- **الكيمياء** (Chemistry): عناصر، تفاعلات، محاليل
- **الإلكترونيات** (Electronics): ترانزستورات، دوائر، إشارات
- **الفيزياء** (Physics): جسيمات، مجالات، قوى
- **الرياضيات** (Mathematics): أعداد، عمليات، مجموعات
- **الموسيقى** (Music): نغمات، إيقاعات، سلالم
- **الطبخ** (Cooking): مكونات، وصفات، أطباق
- **الرياضة** (Sports): لاعبون، فرق، مباريات
- **الاقتصاد** (Economics): سلع، أسواق، أسعار

---

## المساهمة - Contributing

نرحب بمساهماتكم في إنشاء مكتبات مجالية جديدة!

We welcome your contributions in creating new domain libraries!

**الخطوات**:
1. اختر مجالاً (Choose a domain)
2. اتبع الهيكل أعلاه (Follow the structure above)
3. أنشئ ملف `.by` في هذا المجلد (Create a `.by` file in this folder)
4. أضف توثيقاً (Add documentation)
5. أضف أمثلة (Add examples)
6. أرسل طلب دمج (Submit a pull request)

---

## الترخيص - License

جميع المكتبات في هذا المجلد مرخصة تحت نفس ترخيص بيان.

All libraries in this folder are licensed under the same license as Bayan.

