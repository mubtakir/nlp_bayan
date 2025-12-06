# -*- coding: utf-8 -*-
"""
محول اللهجات العربية (Arabic Dialect Adapter)
==============================================

يحول النصوص من اللهجات العربية المختلفة إلى العربية الفصحى
لتسهيل معالجتها بواسطة محرك الاستنباط.

اللهجات المدعومة:
- المصرية (Egyptian)
- الخليجية (Gulf)
- الشامية (Levantine)
- المغربية (Moroccan)

المؤلف: باسل يحيى عبدالله
التاريخ: 2025-12-05
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class Dialect(Enum):
    """أنواع اللهجات المدعومة"""
    STANDARD = "standard"      # الفصحى
    EGYPTIAN = "egyptian"      # المصرية
    GULF = "gulf"              # الخليجية
    LEVANTINE = "levantine"    # الشامية
    MOROCCAN = "moroccan"      # المغربية


@dataclass
class ConversionResult:
    """نتيجة تحويل النص"""
    original: str              # النص الأصلي
    converted: str             # النص المحول
    dialect: Dialect           # اللهجة المكتشفة
    confidence: float          # نسبة الثقة (0-1)
    changes: List[Tuple[str, str]]  # التغييرات (من، إلى)


class DialectAdapter:
    """
    محول اللهجات العربية إلى الفصحى
    
    يقوم بـ:
    1. اكتشاف اللهجة تلقائياً
    2. تحويل الكلمات العامية إلى الفصحى
    3. الحفاظ على المعنى الأصلي
    """
    
    # قاموس اللهجات (عامي ← فصحى)
    DIALECTS: Dict[str, Dict[str, str]] = {
        # ═══════════════════════════════════════════════════════════
        # اللهجة المصرية
        # ═══════════════════════════════════════════════════════════
        "egyptian": {
            # الأفعال
            "عايز": "يريد",
            "عاوز": "يريد", 
            "عاوزة": "تريد",
            "راح": "ذهب",
            "جه": "جاء",
            "جت": "جاءت",
            "اتكلم": "تحدث",
            "قال": "قال",
            "شاف": "رأى",
            "سمع": "سمع",
            "اكل": "أكل",
            "شرب": "شرب",
            "نام": "نام",
            "صحي": "استيقظ",
            "مشي": "مشى",
            "جري": "جرى",
            "وقع": "سقط",
            "ضرب": "ضرب",
            "كتب": "كتب",
            "قرا": "قرأ",
            "فهم": "فهم",
            "عرف": "عرف",
            "نسي": "نسي",
            "فاكر": "يتذكر",
            "بيحب": "يحب",
            "بيكره": "يكره",
            "خلص": "أنهى",
            "بدأ": "بدأ",
            "وقف": "توقف",
            
            # الضمائر والأدوات
            "ده": "هذا",
            "دي": "هذه",
            "دول": "هؤلاء",
            "إيه": "ماذا",
            "ليه": "لماذا",
            "فين": "أين",
            "إمتى": "متى",
            "ازاي": "كيف",
            "مين": "من",
            "كده": "هكذا",
            "هنا": "هنا",
            "هناك": "هناك",
            
            # الصفات والأحوال
            "كويس": "جيد",
            "وحش": "سيء",
            "كتير": "كثير",
            "شوية": "قليل",
            "بسرعة": "بسرعة",
            "دلوقتي": "الآن",
            "بكرة": "غداً",
            "امبارح": "أمس",
            "النهارده": "اليوم",
            
            # الأسماء الشائعة
            "البيت": "المنزل",
            "الشغل": "العمل",
            "الأكل": "الطعام",
            "العيل": "الطفل",
            "العيال": "الأطفال",
            "الست": "المرأة",
            "الراجل": "الرجل",
        },

        # ═══════════════════════════════════════════════════════════
        # اللهجة الخليجية
        # ═══════════════════════════════════════════════════════════
        "gulf": {
            # الأفعال
            "يبي": "يريد",
            "ابي": "أريد",
            "تبي": "تريد",
            "ودي": "أريد",
            "راح": "ذهب",
            "يا": "جاء",
            "شاف": "رأى",
            "سمع": "سمع",
            "اكل": "أكل",
            "شرب": "شرب",
            "نام": "نام",
            "قام": "استيقظ",
            "مشى": "مشى",
            "ركض": "جرى",
            "طاح": "سقط",
            "ضرب": "ضرب",
            "كتب": "كتب",
            "قرا": "قرأ",
            "درس": "درس",
            "خلص": "أنهى",
            "بدا": "بدأ",
            "وقف": "توقف",
            "يحب": "يحب",
            "يكره": "يكره",

            # الضمائر والأدوات
            "هذا": "هذا",
            "هذي": "هذه",
            "ذولا": "هؤلاء",
            "شنو": "ماذا",
            "ليش": "لماذا",
            "وين": "أين",
            "متى": "متى",
            "شلون": "كيف",
            "منو": "من",
            "جذي": "هكذا",
            "هني": "هنا",
            "هناك": "هناك",

            # الصفات والأحوال
            "زين": "جيد",
            "مو زين": "سيء",
            "وايد": "كثير",
            "شوي": "قليل",
            "الحين": "الآن",
            "باجر": "غداً",
            "امس": "أمس",
            "اليوم": "اليوم",

            # الأسماء الشائعة
            "البيت": "المنزل",
            "الدوام": "العمل",
            "الأكل": "الطعام",
            "الولد": "الطفل",
            "العيال": "الأطفال",
            "الحرمة": "المرأة",
            "الريال": "الرجل",
        },

        # ═══════════════════════════════════════════════════════════
        # اللهجة الشامية (سورية/لبنانية/فلسطينية/أردنية)
        # ═══════════════════════════════════════════════════════════
        "levantine": {
            # الأفعال
            "بدي": "أريد",
            "بدو": "يريد",
            "بدها": "تريد",
            "راح": "ذهب",
            "إجا": "جاء",
            "إجت": "جاءت",
            "حكى": "تحدث",
            "شاف": "رأى",
            "سمع": "سمع",
            "أكل": "أكل",
            "شرب": "شرب",
            "نام": "نام",
            "فاق": "استيقظ",
            "مشي": "مشى",
            "ركض": "جرى",
            "وقع": "سقط",
            "ضرب": "ضرب",
            "كتب": "كتب",
            "قرا": "قرأ",
            "خلص": "أنهى",
            "بلش": "بدأ",
            "وقف": "توقف",
            "بيحب": "يحب",
            "بيكره": "يكره",

            # الضمائر والأدوات
            "هاد": "هذا",
            "هاي": "هذه",
            "هدول": "هؤلاء",
            "شو": "ماذا",
            "ليش": "لماذا",
            "وين": "أين",
            "إيمتى": "متى",
            "كيف": "كيف",
            "مين": "من",
            "هيك": "هكذا",
            "هون": "هنا",
            "هونيك": "هناك",

            # الصفات والأحوال
            "منيح": "جيد",
            "مش منيح": "سيء",
            "كتير": "كثير",
            "شوي": "قليل",
            "هلق": "الآن",
            "بكرا": "غداً",
            "مبارح": "أمس",
            "اليوم": "اليوم",

            # الأسماء الشائعة
            "البيت": "المنزل",
            "الشغل": "العمل",
            "الأكل": "الطعام",
            "الولد": "الطفل",
            "الولاد": "الأطفال",
            "المرا": "المرأة",
            "الزلمة": "الرجل",
        },

        # ═══════════════════════════════════════════════════════════
        # اللهجة المغربية
        # ═══════════════════════════════════════════════════════════
        "moroccan": {
            # الأفعال
            "بغيت": "أريد",
            "بغى": "يريد",
            "بغات": "تريد",
            "مشى": "ذهب",
            "جا": "جاء",
            "جات": "جاءت",
            "هضر": "تحدث",
            "شاف": "رأى",
            "سمع": "سمع",
            "كلا": "أكل",
            "شرب": "شرب",
            "نعس": "نام",
            "فاق": "استيقظ",
            "مشا": "مشى",
            "جرى": "جرى",
            "طاح": "سقط",
            "ضرب": "ضرب",
            "كتب": "كتب",
            "قرا": "قرأ",
            "سالى": "أنهى",
            "بدا": "بدأ",
            "وقف": "توقف",
            "كيحب": "يحب",
            "كيكره": "يكره",

            # الضمائر والأدوات
            "هاد": "هذا",
            "هادي": "هذه",
            "هادو": "هؤلاء",
            "شنو": "ماذا",
            "علاش": "لماذا",
            "فين": "أين",
            "إمتى": "متى",
            "كيفاش": "كيف",
            "شكون": "من",
            "هكا": "هكذا",
            "هنا": "هنا",
            "لهيه": "هناك",

            # الصفات والأحوال
            "مزيان": "جيد",
            "خايب": "سيء",
            "بزاف": "كثير",
            "شوية": "قليل",
            "دابا": "الآن",
            "غدا": "غداً",
            "البارح": "أمس",
            "اليوم": "اليوم",

            # الأسماء الشائعة
            "الدار": "المنزل",
            "الخدمة": "العمل",
            "الماكلة": "الطعام",
            "الدري": "الطفل",
            "الدراري": "الأطفال",
            "المرا": "المرأة",
            "الراجل": "الرجل",
        },
    }

    # كلمات مميزة لكل لهجة (للكشف التلقائي)
    DIALECT_MARKERS: Dict[str, List[str]] = {
        "egyptian": ["عايز", "عاوز", "عاوزة", "ازاي", "ده", "دي", "دول", "امبارح", "دلوقتي", "كده", "إيه", "فين", "ليه", "بتاع"],
        "gulf": ["يبي", "ابي", "تبي", "ودي", "شلون", "وين", "الحين", "وايد", "زين", "شنو", "منو", "جذي", "هذي"],
        "levantine": ["بدي", "بدو", "بدها", "بدهم", "شو", "هيك", "هون", "هلق", "منيح", "كتير", "هاد", "هاي", "ليش", "هدول"],
        "moroccan": ["بغيت", "بغى", "بغات", "كيفاش", "دابا", "بزاف", "مزيان", "شكون", "علاش", "هكا", "الدار", "خايب"],
    }

    def __init__(self, default_dialect: Optional[Dialect] = None):
        """
        تهيئة محول اللهجات

        Args:
            default_dialect: اللهجة الافتراضية (None = اكتشاف تلقائي)
        """
        self.default_dialect = default_dialect
        self._build_reverse_lookup()

    def _build_reverse_lookup(self):
        """بناء قاموس عكسي للبحث السريع"""
        self.word_to_dialect: Dict[str, str] = {}
        for dialect, words in self.DIALECTS.items():
            for word in words.keys():
                if word not in self.word_to_dialect:
                    self.word_to_dialect[word] = dialect

    def detect_dialect(self, text: str) -> Tuple[Dialect, float]:
        """
        اكتشاف اللهجة تلقائياً من النص

        Args:
            text: النص المراد تحليله

        Returns:
            (اللهجة المكتشفة، نسبة الثقة)
        """
        words = text.split()
        dialect_scores: Dict[str, int] = {d: 0 for d in self.DIALECTS.keys()}
        marker_found = False  # هل وجدنا كلمة مميزة؟

        for word in words:
            # إزالة علامات الترقيم
            clean_word = word.strip(".,!?،؟")

            # البحث في الكلمات المميزة (وزن عالي جداً)
            for dialect, markers in self.DIALECT_MARKERS.items():
                if clean_word in markers:
                    dialect_scores[dialect] += 5  # وزن أعلى للكلمات المميزة
                    marker_found = True

        # إذا لم نجد كلمات مميزة، النص فصحى
        if not marker_found:
            return Dialect.STANDARD, 1.0

        # إيجاد اللهجة الأعلى درجة
        max_score = max(dialect_scores.values())

        if max_score == 0:
            return Dialect.STANDARD, 1.0

        detected = max(dialect_scores, key=dialect_scores.get)
        confidence = min(max_score / (len(words) * 0.5), 1.0)

        return Dialect(detected), confidence

    def convert_to_standard(self, text: str, dialect: Optional[str] = None) -> ConversionResult:
        """
        تحويل النص من لهجة إلى الفصحى

        Args:
            text: النص باللهجة
            dialect: اسم اللهجة (None = اكتشاف تلقائي)

        Returns:
            نتيجة التحويل
        """
        # اكتشاف اللهجة إذا لم تُحدد
        if dialect is None:
            detected_dialect, confidence = self.detect_dialect(text)
            if detected_dialect == Dialect.STANDARD:
                return ConversionResult(
                    original=text,
                    converted=text,
                    dialect=Dialect.STANDARD,
                    confidence=1.0,
                    changes=[]
                )
            dialect = detected_dialect.value
        else:
            detected_dialect = Dialect(dialect)
            confidence = 1.0

        # التحويل
        words = text.split()
        converted_words = []
        changes = []

        dialect_dict = self.DIALECTS.get(dialect, {})

        for word in words:
            # إزالة علامات الترقيم مؤقتاً
            prefix = ""
            suffix = ""
            clean_word = word

            # الحفاظ على علامات الترقيم
            while clean_word and clean_word[0] in ".,!?،؟()[]{}«»":
                prefix += clean_word[0]
                clean_word = clean_word[1:]
            while clean_word and clean_word[-1] in ".,!?،؟()[]{}«»":
                suffix = clean_word[-1] + suffix
                clean_word = clean_word[:-1]

            # البحث عن الكلمة في القاموس
            if clean_word in dialect_dict:
                converted = dialect_dict[clean_word]
                changes.append((clean_word, converted))
                converted_words.append(prefix + converted + suffix)
            else:
                converted_words.append(word)

        converted_text = " ".join(converted_words)

        return ConversionResult(
            original=text,
            converted=converted_text,
            dialect=detected_dialect,
            confidence=confidence,
            changes=changes
        )

    def convert_sentence(self, text: str) -> str:
        """
        تحويل مختصر - يرجع النص المحول فقط

        Args:
            text: النص باللهجة

        Returns:
            النص بالفصحى
        """
        result = self.convert_to_standard(text)
        return result.converted

    def get_supported_dialects(self) -> List[str]:
        """إرجاع قائمة اللهجات المدعومة"""
        return list(self.DIALECTS.keys())

    def get_dialect_words(self, dialect: str) -> Dict[str, str]:
        """إرجاع قاموس كلمات لهجة معينة"""
        return self.DIALECTS.get(dialect, {})

    def add_word(self, dialect: str, colloquial: str, standard: str):
        """
        إضافة كلمة جديدة للقاموس

        Args:
            dialect: اسم اللهجة
            colloquial: الكلمة العامية
            standard: الكلمة الفصحى
        """
        if dialect in self.DIALECTS:
            self.DIALECTS[dialect][colloquial] = standard
            self.word_to_dialect[colloquial] = dialect

    def __repr__(self):
        return f"DialectAdapter(dialects={list(self.DIALECTS.keys())})"


# ═══════════════════════════════════════════════════════════════
# دوال مساعدة للاستخدام السريع
# ═══════════════════════════════════════════════════════════════

# نسخة عامة من المحول
_default_adapter = None

def get_adapter() -> DialectAdapter:
    """الحصول على المحول الافتراضي"""
    global _default_adapter
    if _default_adapter is None:
        _default_adapter = DialectAdapter()
    return _default_adapter

def to_standard(text: str, dialect: Optional[str] = None) -> str:
    """تحويل سريع إلى الفصحى"""
    return get_adapter().convert_sentence(text)

def detect_dialect(text: str) -> Tuple[str, float]:
    """اكتشاف اللهجة"""
    dialect, conf = get_adapter().detect_dialect(text)
    return dialect.value, conf

