"""
🌍 محول اللهجات العربية - Arabic Dialect Adapter
يحول النص من اللهجات العربية المختلفة إلى الفصحى

Converts text from various Arabic dialects to Modern Standard Arabic (MSA)

اللهجات المدعومة:
- المصرية (Egyptian)
- الخليجية (Gulf)
- الشامية (Levantine)
- المغربية (Moroccan)
- + أي لهجة مخصصة من ملفات JSON
"""

import os
import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Tuple, Optional
from pathlib import Path


class Dialect(Enum):
    """أنواع اللهجات المدعومة"""
    STANDARD = "standard"   # الفصحى
    EGYPTIAN = "egyptian"   # مصري
    GULF = "gulf"          # خليجي
    LEVANTINE = "levantine" # شامي
    MOROCCAN = "moroccan"   # مغربي


@dataclass
class ConversionResult:
    """نتيجة تحويل اللهجة"""
    original: str           # النص الأصلي
    converted: str          # النص المحول
    dialect: Dialect        # اللهجة المكتشفة
    confidence: float       # نسبة الثقة (0-1)
    changes: List[Tuple[str, str]]  # قائمة التغييرات (قبل، بعد)


class DialectAdapter:
    """
    محول اللهجات العربية
    يكتشف اللهجة تلقائياً ويحولها للفصحى
    """
    
    # قواميس اللهجات: كلمة_عامية -> كلمة_فصحى
    DIALECTS: Dict[str, Dict[str, str]] = {
        "egyptian": {
            # الأفعال
            "عايز": "يريد", "عاوز": "يريد", "عاوزة": "تريد",
            "راح": "ذهب", "مشي": "ذهب", "جه": "جاء", "جت": "جاءت",
            "شاف": "رأى", "قال": "قال", "عمل": "فعل",
            "اكل": "أكل", "شرب": "شرب", "نام": "نام",
            # الضمائر والإشارة
            "ده": "هذا", "دي": "هذه", "دول": "هؤلاء",
            "انا": "أنا", "انت": "أنت", "هو": "هو", "هي": "هي",
            # الظروف
            "امبارح": "أمس", "دلوقتي": "الآن", "بكره": "غداً",
            "كده": "هكذا", "ليه": "لماذا",
            # أدوات الاستفهام
            "ازاي": "كيف", "إيه": "ماذا", "فين": "أين", "مين": "من",
            # صفات ومتفرقات
            "كويس": "جيد", "حلو": "جميل", "وحش": "سيء",
            "اوي": "جداً", "خالص": "تماماً", "بتاع": "خاص_بـ",
        },
        "gulf": {
            # الأفعال
            "يبي": "يريد", "ابي": "أريد", "تبي": "تريد", "يبون": "يريدون",
            "راح": "ذهب", "يروح": "يذهب", "جا": "جاء",
            "شاف": "رأى", "يشوف": "يرى", "سوى": "فعل", "يسوي": "يفعل",
            # الضمائر
            "هذي": "هذه", "ذا": "هذا", "هذول": "هؤلاء",
            # الظروف
            "الحين": "الآن", "توه": "للتو", "باچر": "غداً", "امس": "أمس",
            # أدوات الاستفهام  
            "شلون": "كيف", "وين": "أين", "شنو": "ماذا", "منو": "من",
            "ليش": "لماذا",
            # صفات
            "زين": "جيد", "واجد": "كثير", "وايد": "كثير جداً",
            "مب": "ليس", "جذي": "هكذا", "چذي": "هكذا",
        },
        "levantine": {
            # الأفعال
            "بدي": "أريد", "بدو": "يريد", "بدها": "تريد", "بدهم": "يريدون",
            "راح": "ذهب", "اجا": "جاء", "اجت": "جاءت",
            "شاف": "رأى", "حكى": "تحدث", "عمل": "فعل",
            # الضمائر
            "هاد": "هذا", "هاي": "هذه", "هدول": "هؤلاء",
            # الظروف
            "هلق": "الآن", "هلأ": "الآن", "بكرا": "غداً", "مبارح": "أمس",
            "هيك": "هكذا",
            # أدوات الاستفهام
            "شو": "ماذا", "كيف": "كيف", "وين": "أين", "مين": "من",
            "ليش": "لماذا",
            # صفات
            "منيح": "جيد", "كتير": "كثير", "شوي": "قليل",
            "مش": "ليس", "ما": "لا",
        },
        "moroccan": {
            # الأفعال
            "بغيت": "أريد", "بغى": "يريد", "بغات": "تريد",
            "مشى": "ذهب", "جا": "جاء", "جات": "جاءت",
            "شاف": "رأى", "دار": "فعل", "كلا": "أكل",
            # الضمائر
            "هاد": "هذا", "هادي": "هذه", "هادو": "هؤلاء",
            # الظروف
            "دابا": "الآن", "غدا": "غداً", "البارح": "أمس",
            "هكا": "هكذا", "هكاك": "هكذا",
            # أدوات الاستفهام
            "كيفاش": "كيف", "فين": "أين", "شكون": "من", "علاش": "لماذا",
            "شنو": "ماذا", "اشنو": "ماذا",
            # صفات
            "مزيان": "جيد", "بزاف": "كثير", "شوية": "قليل",
            "ماشي": "ليس", "الدار": "المنزل", "خايب": "سيء",
        },
    }
    
    # كلمات مميزة لكل لهجة (للكشف التلقائي)
    DIALECT_MARKERS: Dict[str, List[str]] = {
        "egyptian": ["عايز", "عاوز", "عاوزة", "ازاي", "ده", "دي", "دول", "امبارح", "دلوقتي", "كده", "إيه", "فين", "ليه", "بتاع"],
        "gulf": ["يبي", "ابي", "تبي", "ودي", "شلون", "وين", "الحين", "وايد", "زين", "شنو", "منو", "جذي", "هذي"],
        "levantine": ["بدي", "بدو", "بدها", "بدهم", "شو", "هيك", "هون", "هلق", "منيح", "كتير", "هاد", "هاي", "ليش", "هدول"],
        "moroccan": ["بغيت", "بغى", "بغات", "كيفاش", "دابا", "بزاف", "مزيان", "شكون", "علاش", "هكا", "الدار", "خايب"],
    }
    
    def __init__(self, load_json_dialects: bool = True):
        """تهيئة المحول"""
        # بناء فهرس عكسي للكلمات
        self.word_to_dialect: Dict[str, str] = {}
        for dialect, words in self.DIALECTS.items():
            for word in words:
                self.word_to_dialect[word] = dialect

        # تحميل اللهجات من ملفات JSON
        if load_json_dialects:
            self._load_json_dialects()

    def _load_json_dialects(self):
        """تحميل اللهجات من ملفات JSON"""
        dialects_dir = Path(__file__).parent / "dialects"
        if not dialects_dir.exists():
            return

        # تحميل جميع ملفات JSON
        for json_file in dialects_dir.glob("*.json"):
            try:
                self.load_dialect_file(str(json_file))
            except Exception as e:
                print(f"⚠️ فشل تحميل {json_file.name}: {e}")

        # تحميل اللهجات المخصصة
        custom_dir = dialects_dir / "custom"
        if custom_dir.exists():
            for json_file in custom_dir.glob("*.json"):
                try:
                    self.load_dialect_file(str(json_file))
                except Exception as e:
                    print(f"⚠️ فشل تحميل {json_file.name}: {e}")

    def load_dialect_file(self, file_path: str) -> bool:
        """
        تحميل لهجة من ملف JSON

        Args:
            file_path: مسار ملف JSON للهجة

        Returns:
            True إذا تم التحميل بنجاح
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            code = data.get("code", "")
            if not code:
                return False

            # إضافة المفردات
            if "vocabulary" in data:
                if code not in self.DIALECTS:
                    self.DIALECTS[code] = {}
                self.DIALECTS[code].update(data["vocabulary"])

                # تحديث الفهرس العكسي
                for word in data["vocabulary"]:
                    self.word_to_dialect[word] = code

            # إضافة العلامات المميزة
            if "markers" in data:
                if code not in self.DIALECT_MARKERS:
                    self.DIALECT_MARKERS[code] = []
                self.DIALECT_MARKERS[code].extend(data["markers"])
                # إزالة التكرارات
                self.DIALECT_MARKERS[code] = list(set(self.DIALECT_MARKERS[code]))

            return True

        except Exception as e:
            print(f"❌ خطأ في تحميل الملف {file_path}: {e}")
            return False

    def add_dialect(self, code: str, name: str, vocabulary: Dict[str, str],
                    markers: List[str] = None) -> bool:
        """
        إضافة لهجة جديدة برمجياً

        Args:
            code: رمز اللهجة (مثل: sudanese)
            name: اسم اللهجة (مثل: السودانية)
            vocabulary: قاموس الكلمات {عامية: فصحى}
            markers: كلمات مميزة للكشف التلقائي

        Returns:
            True إذا تمت الإضافة بنجاح
        """
        try:
            self.DIALECTS[code] = vocabulary
            self.DIALECT_MARKERS[code] = markers or list(vocabulary.keys())[:10]

            # تحديث الفهرس العكسي
            for word in vocabulary:
                self.word_to_dialect[word] = code

            return True
        except Exception as e:
            print(f"❌ خطأ في إضافة اللهجة: {e}")
            return False

    def save_dialect_to_file(self, code: str, file_path: str = None) -> bool:
        """
        حفظ لهجة إلى ملف JSON

        Args:
            code: رمز اللهجة
            file_path: مسار الملف (اختياري)

        Returns:
            True إذا تم الحفظ بنجاح
        """
        if code not in self.DIALECTS:
            print(f"❌ اللهجة '{code}' غير موجودة")
            return False

        if file_path is None:
            dialects_dir = Path(__file__).parent / "dialects" / "custom"
            dialects_dir.mkdir(parents=True, exist_ok=True)
            file_path = str(dialects_dir / f"{code}.json")

        data = {
            "code": code,
            "vocabulary": self.DIALECTS[code],
            "markers": self.DIALECT_MARKERS.get(code, [])
        }

        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ تم حفظ اللهجة '{code}' في {file_path}")
            return True
        except Exception as e:
            print(f"❌ خطأ في الحفظ: {e}")
            return False

    def list_dialects(self) -> Dict[str, int]:
        """عرض قائمة اللهجات المتاحة مع عدد الكلمات"""
        return {code: len(words) for code, words in self.DIALECTS.items()}

    def add_word(self, dialect_code: str, dialect_word: str, standard_word: str) -> bool:
        """
        إضافة كلمة جديدة للهجة

        Args:
            dialect_code: رمز اللهجة
            dialect_word: الكلمة بالعامية
            standard_word: الكلمة بالفصحى
        """
        if dialect_code not in self.DIALECTS:
            self.DIALECTS[dialect_code] = {}

        self.DIALECTS[dialect_code][dialect_word] = standard_word
        self.word_to_dialect[dialect_word] = dialect_code
        return True

    def detect_dialect(self, text: str) -> Tuple[Dialect, float]:
        """
        اكتشاف اللهجة تلقائياً من النص
        """
        words = text.split()
        dialect_scores: Dict[str, int] = {d: 0 for d in self.DIALECTS.keys()}
        marker_found = False

        for word in words:
            clean_word = word.strip(".,!?،؟")
            for dialect, markers in self.DIALECT_MARKERS.items():
                if clean_word in markers:
                    dialect_scores[dialect] += 5
                    marker_found = True

        if not marker_found:
            return Dialect.STANDARD, 1.0

        max_score = max(dialect_scores.values())
        if max_score == 0:
            return Dialect.STANDARD, 1.0

        detected = max(dialect_scores, key=dialect_scores.get)
        confidence = min(max_score / (len(words) * 0.5), 1.0)
        return Dialect(detected), confidence

    def convert_to_standard(self, text: str, dialect: Optional[str] = None) -> ConversionResult:
        """
        تحويل النص من اللهجة إلى الفصحى
        """
        # اكتشاف اللهجة إذا لم تحدد
        if dialect:
            # دعم اللهجات الديناميكية (غير المعرفة في Enum)
            try:
                detected_dialect = Dialect(dialect)
            except ValueError:
                # لهجة مخصصة غير موجودة في Enum
                if dialect in self.DIALECTS:
                    # استخدام قيمة نصية بدلاً من Enum
                    dialect_code = dialect
                    confidence = 1.0

                    # التحويل المباشر
                    words = text.split()
                    converted_words = []
                    changes = []
                    dialect_dict = self.DIALECTS.get(dialect_code, {})

                    for word in words:
                        clean_word = word.strip(".,!?،؟")
                        if clean_word in dialect_dict:
                            new_word = dialect_dict[clean_word]
                            converted_words.append(new_word)
                            changes.append((clean_word, new_word))
                        else:
                            converted_words.append(word)

                    converted_text = " ".join(converted_words)
                    # إنشاء نتيجة مع لهجة custom
                    return ConversionResult(text, converted_text, Dialect.STANDARD, confidence, changes)
                else:
                    return ConversionResult(text, text, Dialect.STANDARD, 0.0, [])
            confidence = 1.0
        else:
            detected_dialect, confidence = self.detect_dialect(text)

        if detected_dialect == Dialect.STANDARD:
            return ConversionResult(text, text, Dialect.STANDARD, 1.0, [])

        # التحويل
        words = text.split()
        converted_words = []
        changes = []
        dialect_dict = self.DIALECTS.get(detected_dialect.value, {})

        for word in words:
            clean_word = word.strip(".,!?،؟")
            if clean_word in dialect_dict:
                new_word = dialect_dict[clean_word]
                converted_words.append(new_word)
                changes.append((clean_word, new_word))
            else:
                converted_words.append(word)

        converted_text = " ".join(converted_words)
        return ConversionResult(text, converted_text, detected_dialect, confidence, changes)

    def convert_sentence(self, text: str) -> str:
        """تحويل مباشر - إرجاع النص المحول فقط"""
        return self.convert_to_standard(text).converted


# دوال مساعدة
def to_standard(text: str, dialect: Optional[str] = None) -> str:
    """تحويل سريع من لهجة إلى فصحى"""
    adapter = DialectAdapter()
    return adapter.convert_to_standard(text, dialect).converted


def detect_dialect(text: str) -> Tuple[str, float]:
    """اكتشاف اللهجة"""
    adapter = DialectAdapter()
    dialect, conf = adapter.detect_dialect(text)
    return dialect.value, conf

