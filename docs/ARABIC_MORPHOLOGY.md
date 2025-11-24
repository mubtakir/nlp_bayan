# Arabic Morphology System in Bayan
# نظام المورفولوجيا العربية في بيان

This document describes the Arabic morphology system integrated into Bayan language.

## Overview / نظرة عامة

The Arabic morphology system provides comprehensive support for:
1. **Root-Pattern System** (نظام الجذر والوزن)
2. **Verb Conjugation** (تصريف الأفعال)
3. **Root Extraction** (استخراج الجذر)

## Features / المميزات

### 1. Pattern Application (تطبيق الأوزان)

The `apply_pattern(root, pattern)` function generates words from trilateral roots using Arabic morphological patterns:

```bayan
root = "كتب"
word = apply_pattern(root, "فاعل")  # Returns: "كاتب"
```

**Supported Patterns:**
- `فاعل` - Active participle (اسم الفاعل)
- `مفعول` - Passive participle (اسم المفعول)
- `فعال` - Intensive form
- `أفعل` - Form IV
- `تفعيل` - Form II verbal noun
- `مفاعل` - Place noun
- `افتعال` - Form VIII verbal noun
- `استفعال` - Form X verbal noun
- `مستفعل` - Form X active participle

### 2. Verb Conjugation (تصريف الأفعال)

The `conjugate_arabic_verb(lemma, tense, person_gender_number)` function conjugates Arabic verbs:

```bayan
verb = "كتب"
past_3ms = conjugate_arabic_verb(verb, "past", "3ms")     # كتب
present_3ms = conjugate_arabic_verb(verb, "present", "3ms") # يكتب
imperative_2ms = conjugate_arabic_verb(verb, "imperative", "2ms") # اكتب
```

**Supported Tenses:**
- `past` (الماضي)
- `present` (المضارع)
- `future` (المستقبل)
- `imperative` (الأمر)

**Person-Gender-Number Codes:**
- **3ms**: 3rd person, masculine, singular (هو)
- **3fs**: 3rd person, feminine, singular (هي)
- **3md**: 3rd person, masculine, dual (هما)
- **3fd**: 3rd person, feminine, dual (هما)
- **3mp**: 3rd person, masculine, plural (هم)
- **3fp**: 3rd person, feminine, plural (هن)
- **2ms**: 2nd person, masculine, singular (أنتَ)
- **2fs**: 2nd person, feminine, singular (أنتِ)
- **2md**: 2nd person, dual (أنتما)
- **2mp**: 2nd person, masculine, plural (أنتم)
- **2fp**: 2nd person, feminine, plural (أنتن)
- **1s**: 1st person, singular (أنا)
- **1p**: 1st person, plural (نحن)

### 3. Root Extraction (استخراج الج ذر)

The `extract_root(word)` function extracts the trilateral root from Arabic words:

```bayan
root = extract_root("كاتب")    # Returns: "كتب"
root = extract_root("مكتوب")   # Returns: "كتب"
root = extract_root("استكتاب") # Returns: "كتاب"
```

## Integration with Logic Engine / التكامل مع المحرك المنطقي

The morphology functions are fully integrated with Bayan's logic engine and can be used in:
- Facts and rules
- Logical queries
- Hybrid blocks

Example:

```bayan
hybrid {
    fact root_of("كتب", "ك", "ت", "ب").
    fact pattern_meaning("فاعل", "active_participle").
}

# Use morphology in traditional code
word = apply_pattern("كتب", "فاعل")
print(word)  # Output: كاتب
```

## Usage Examples / أمثلة الاستخدام

### Example 1: Word Family Generation

```bayan
include("ai/morphology.bayan")

root = "كتب"
patterns = ["فاعل", "مفعول", "فعال", "أفعل"]
for pat in patterns: {
    word = apply_pattern(root, pat)
    print(pat + ": " + word)
}
```

**Output:**
```
فاعل: كاتب
مفعول: مكتوب
فعال: كتاب
أفعل: أكتب
```

### Example 2: Verb Conjugation Table

```bayan
include("ai/morphology.bayan")

verb = "درس"
persons = ["3ms", "3fs", "3md", "3mp"]
for p in persons: {
    conjugated = conjugate_arabic_verb(verb, "present", p)
    print(p + ": " + conjugated)
}
```

**Output:**
```
3ms: يدرس
3fs: تدرس
3md: يدرسان
3mp: يدرسون
```

### Example 3: Root Analysis

```bayan
include("ai/morphology.bayan")

words = ["كاتب", "مكتوب", "الكاتبة", "يكتبون"]
for w in words: {
    r = extract_root(w)
    print(w + " → " + r)
}
```

**Output:**
```
كاتب → كتب
مكتوب → كتب
الكاتبة → كتب
يكتبون → يكتب
```

## File Location / موقع الملفات

- **Implementation**: `ai/morphology.bayan`
- **Tests**: `tests/test_morphology.bayan`
- **Demo**: `examples/demo_morphology_logic.bayan`

## Future Enhancements / التحسينات المستقبلية

1. Support for quadrilateral roots (الجذور الرباعية)
2. Broken plural patterns (جموع التكسير)
3. Noun declension (إعراب الأسماء)
4. Diacritics generation (توليد الحركات)
5. Morphological analysis with ambiguity resolution

## References / المراجع

- Arabic morphology follows traditional Arabic grammar rules
- Root-pattern system based on classical Arabic morphology
- Verb conjugation patterns from standard Arabic grammar

---

**Version**: 1.0  
**Last Updated**: 2025-11-24  
**Language**: Bayan
