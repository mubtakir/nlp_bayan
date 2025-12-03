# -*- coding: utf-8 -*-
"""
محرك استنباط معاني الحروف والكلمات
Letter & Word Meaning Inference Engine

نظام ذكي لاستنباط المعاني بدلاً من الاعتماد فقط على قاعدة البيانات.
يستخدم عدة طرق استنباطية مبنية على بحث 40 سنة:

1. الاستنباط الشكلي - من شكل الحرف
2. الاستنباط الصوتي - من صوت ومخرج الحرف  
3. الاستنباط المعجمي - من كلمات مشتركة في الحروف
4. استنباط اسم الحرف - من اسم الحرف نفسه
5. السلاسل السببية - ربط المعاني بعلاقات سببية

المبادئ الأساسية:
- الحرف يحمل معناه من شكله وصوته (ليس اعتباطياً)
- الحرف يحمل المعنى وضده (معيار)
- الحرف "رمز بين" - حمّال أوجه
- الحروف الجوفية = نفسية/عاطفية، الشفوية = مادية/واقعية
- معاني الحرف الواحد مترابطة بسلاسل سببية

المطور: باسل يحيى عبدالله - العراق/الموصل (40 سنة بحث)
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set, Tuple, Any
from enum import Enum

from .core import (
    ArticulationDepth, MeaningType, RelationType,
    ArticulationPlace, ArticulationManner, ShapeType,
    LetterMeaning, MeaningRelation, CausalChain
)


# ==================== أنواع الاستنباط ====================

class InferenceMethod(Enum):
    """طرق الاستنباط"""
    SHAPE = "شكلي"           # من شكل الحرف
    SOUND = "صوتي"           # من صوت الحرف
    LEXICAL = "معجمي"        # من كلمات مشتركة
    LETTER_NAME = "اسمي"     # من اسم الحرف
    CAUSAL = "سببي"          # من سلاسل سببية
    DATABASE = "قاعدة_بيانات" # من قاعدة البيانات


@dataclass
class InferredMeaning:
    """معنى مستنبط"""
    meaning: str
    method: InferenceMethod
    confidence: float  # 0.0 - 1.0
    evidence: List[str] = field(default_factory=list)
    opposite: Optional[str] = None
    related_meanings: List[str] = field(default_factory=list)


@dataclass
class ShapeAnalysis:
    """تحليل شكل الحرف"""
    letter: str
    shape_types: List[ShapeType]
    natural_resemblances: List[str]  # يشبه: جبل، نهر، رجل يركض
    implied_meanings: List[str]      # المعاني المستنتجة
    visual_patterns: List[str]       # أنماط بصرية


@dataclass
class SoundAnalysis:
    """تحليل صوت الحرف"""
    letter: str
    articulation_place: ArticulationPlace
    articulation_manner: ArticulationManner
    depth: ArticulationDepth         # جوفي/متوسط/خارجي
    meaning_type: MeaningType        # نفسي/مادي/مختلط
    emotional_score: float           # 0.0 - 1.0
    physical_score: float            # 0.0 - 1.0
    implied_meanings: List[str]


# ==================== قواعد الشكل ====================

# خريطة الأشكال والمعاني للحروف العربية
ARABIC_SHAPE_MEANINGS: Dict[str, Dict] = {
    "ا": {
        "shapes": [ShapeType.STRAIGHT],
        "resembles": ["عمود ممدود", "شخص واقف", "جبل مرتفع"],
        "meanings": ["الارتفاع", "العلو", "الامتداد", "الألفة", "الود"],
        "patterns": ["خط عمودي"]
    },
    "ب": {
        "shapes": [ShapeType.CURVED, ShapeType.OPEN],
        "resembles": ["وعاء مفتوح", "حوض", "باطن اليد"],
        "meanings": ["الاحتواء", "الحمل", "الدك", "التشبع", "البناء"],
        "patterns": ["منحنى مفتوح للأعلى"]
    },
    "ت": {
        "shapes": [ShapeType.CURVED],
        "resembles": ["طبق", "سطح مستوٍ"],
        "meanings": ["التمام", "الاكتمال", "التثبيت"],
        "patterns": ["قوس مع نقطتين"]
    },
    "ج": {
        "shapes": [ShapeType.ANGULAR, ShapeType.OPEN],
        "resembles": ["جبل", "زاوية", "انكسار"],
        "meanings": ["الجمع", "التجميع", "الانكسار", "التدفق"],
        "patterns": ["زاوية مع نقطة"]
    },
    "ح": {
        "shapes": [ShapeType.CURVED, ShapeType.OPEN],
        "resembles": ["فم مفتوح", "حنجرة"],
        "meanings": ["الحرارة", "الجهد", "التعب", "الحياة"],
        "patterns": ["منحنى مفتوح"]
    },
    "د": {
        "shapes": [ShapeType.CURVED],
        "resembles": ["ظهر منحني", "باب"],
        "meanings": ["الدلالة", "البداية", "المبادرة"],
        "patterns": ["قوس"]
    },
    "ر": {
        "shapes": [ShapeType.CURVED],
        "resembles": ["نهر متدفق", "ذراع منحنية", "تدفق"],
        "meanings": ["التدفق", "الانسياب", "الحركة", "الكرم"],
        "patterns": ["منحنى للأسفل"]
    },
    "س": {
        "shapes": [ShapeType.CURVED],
        "resembles": ["أمواج", "تموجات", "رقص"],
        "meanings": ["الانسياب", "السلاسة", "الحركة الناعمة"],
        "patterns": ["ثلاث موجات"]
    },
    "ص": {
        "shapes": [ShapeType.CIRCULAR, ShapeType.CLOSED],
        "resembles": ["عين", "أذن", "فم مغلق"],
        "meanings": ["الإصغاء", "البصر", "الصمت", "الصد"],
        "patterns": ["دائرة مغلقة"]
    },
    "ع": {
        "shapes": [ShapeType.CURVED, ShapeType.OPEN],
        "resembles": ["عين مفتوحة", "معول", "غصن"],
        "meanings": ["العمق", "الرؤية", "العمل", "المعرفة"],
        "patterns": ["منحنى مفتوح للأعلى"]
    },
    "ك": {
        "shapes": [ShapeType.ANGULAR],
        "resembles": ["شخص يحمل شيء", "جسد مع ذراعين"],
        "meanings": ["الحمل", "العطاء", "الكرم", "الملك"],
        "patterns": ["خط مع انحناء"]
    },
    "ل": {
        "shapes": [ShapeType.CURVED],
        "resembles": ["لسان منعكف", "لف", "التفاف"],
        "meanings": ["الإحاطة", "اللف", "المناداة", "القبول"],
        "patterns": ["خط مع انعكاف"]
    },
    "م": {
        "shapes": [ShapeType.CLOSED, ShapeType.CIRCULAR],
        "resembles": ["فم مغلق", "احتواء", "ضم"],
        "meanings": ["الاحتواء", "الضم", "الثناء", "الأمومة"],
        "patterns": ["دائرة مغلقة"]
    },
    "ن": {
        "shapes": [ShapeType.CURVED, ShapeType.OPEN],
        "resembles": ["وعاء", "سفينة", "حضن"],
        "meanings": ["النور", "الظهور", "الإنبات"],
        "patterns": ["قوس مع نقطة"]
    },
    "و": {
        "shapes": [ShapeType.CIRCULAR],
        "resembles": ["عجلة", "دائرة متدحرجة"],
        "meanings": ["التدحرج", "اللحاق", "المجاورة", "الذهاب معاً"],
        "patterns": ["دائرة مع ذيل"]
    },
    "ي": {
        "shapes": [ShapeType.CURVED],
        "resembles": ["حية تتلوى", "ألم", "انحناء"],
        "meanings": ["الألم", "الضيق النفسي", "التلوي"],
        "patterns": ["خط متلوٍ"]
    },
    "ه": {
        "shapes": [ShapeType.CIRCULAR, ShapeType.OPEN],
        "resembles": ["نفَس", "هواء", "زفير"],
        "meanings": ["النفس", "الجهد", "التعب", "الراحة"],
        "patterns": ["دائرة مفتوحة"]
    },
}

# خريطة الأشكال والمعاني للحروف الإنجليزية
ENGLISH_SHAPE_MEANINGS: Dict[str, Dict] = {
    "A": {
        "shapes": [ShapeType.ANGULAR, ShapeType.POINTED],
        "resembles": ["جبل", "قمة", "خيمة"],
        "meanings": ["الارتفاع", "العلو", "القمة", "البداية"],
        "patterns": ["مثلث"]
    },
    "B": {
        "shapes": [ShapeType.CURVED, ShapeType.CLOSED],
        "resembles": ["جسم ممتلئ", "بطن", "حمل"],
        "meanings": ["الامتلاء", "الحمل", "البناء"],
        "patterns": ["خط مع قوسين"]
    },
    "C": {
        "shapes": [ShapeType.CURVED, ShapeType.OPEN],
        "resembles": ["فم مفتوح", "احتضان", "قوس"],
        "meanings": ["الاحتواء", "الاستقبال", "الانفتاح"],
        "patterns": ["قوس مفتوح"]
    },
    "O": {
        "shapes": [ShapeType.CIRCULAR, ShapeType.CLOSED],
        "resembles": ["عجلة", "دائرة", "شمس"],
        "meanings": ["التدحرج", "الاندفاع", "الكمال", "الدوران"],
        "patterns": ["دائرة كاملة"]
    },
    "R": {
        "shapes": [ShapeType.ANGULAR, ShapeType.CURVED],
        "resembles": ["رجل يركض", "شخص يتحرك"],
        "meanings": ["الحركة", "الركض", "السرعة", "النشاط"],
        "patterns": ["خط مع قوس وساق"]
    },
    "r": {
        "shapes": [ShapeType.CURVED],
        "resembles": ["ساق وقدم", "خطوة"],
        "meanings": ["الحركة", "الخطو", "المشي"],
        "patterns": ["خط مع انحناء صغير"]
    },
    "S": {
        "shapes": [ShapeType.CURVED],
        "resembles": ["ثعبان", "موجة", "تلوي"],
        "meanings": ["الانسياب", "التلوي", "الحركة المتعرجة"],
        "patterns": ["منحنى مزدوج"]
    },
    "V": {
        "shapes": [ShapeType.ANGULAR, ShapeType.OPEN],
        "resembles": ["وادي", "انفتاح", "انتصار"],
        "meanings": ["الانفتاح", "النصر", "الانطلاق"],
        "patterns": ["خطان متقاطعان"]
    },
    "W": {
        "shapes": [ShapeType.ANGULAR],
        "resembles": ["أمواج", "تموجات", "ماء"],
        "meanings": ["الماء", "التموج", "الازدواج"],
        "patterns": ["موجتان"]
    },
    "X": {
        "shapes": [ShapeType.ANGULAR],
        "resembles": ["تقاطع", "رفض", "ذراعان متقاطعتان"],
        "meanings": ["الرفض", "التقاطع", "المنع"],
        "patterns": ["خطان متقاطعان"]
    },
    "Y": {
        "shapes": [ShapeType.ANGULAR, ShapeType.OPEN],
        "resembles": ["شجرة", "غصن متفرع", "ذراعان مرفوعتان"],
        "meanings": ["التفرع", "النمو", "التساؤل"],
        "patterns": ["تفرع للأعلى"]
    },
}


# ==================== قواعد الصوت والمخرج ====================

# الحروف الجوفية (نفسية/عاطفية) vs الشفوية (مادية/واقعية)
ARTICULATION_MEANING_MAP = {
    # الحروف الحلقية والحنجرية = نفسية/عاطفية
    ArticulationPlace.GLOTTAL: {
        "depth": ArticulationDepth.INTERNAL,
        "type": MeaningType.PSYCHOLOGICAL,
        "emotional_score": 0.9,
        "physical_score": 0.2,
        "general_meanings": ["الجهد النفسي", "التعب", "الراحة", "النفَس"]
    },
    ArticulationPlace.PHARYNGEAL: {
        "depth": ArticulationDepth.INTERNAL,
        "type": MeaningType.PSYCHOLOGICAL,
        "emotional_score": 0.85,
        "physical_score": 0.3,
        "general_meanings": ["العمق", "العطش", "السخرية", "الغموض"]
    },
    # الحروف اللهوية والغارية = متوسطة
    ArticulationPlace.VELAR: {
        "depth": ArticulationDepth.MIDDLE,
        "type": MeaningType.MIXED,
        "emotional_score": 0.5,
        "physical_score": 0.5,
        "general_meanings": ["القوة", "القطع", "الثبات"]
    },
    ArticulationPlace.PALATAL: {
        "depth": ArticulationDepth.MIDDLE,
        "type": MeaningType.MIXED,
        "emotional_score": 0.6,
        "physical_score": 0.5,
        "general_meanings": ["الامتداد", "الانبساط"]
    },
    # الحروف اللثوية والأسنانية = متوسطة-مادية
    ArticulationPlace.ALVEOLAR: {
        "depth": ArticulationDepth.MIDDLE,
        "type": MeaningType.MIXED,
        "emotional_score": 0.4,
        "physical_score": 0.6,
        "general_meanings": ["الفعل", "الحركة", "التأثير"]
    },
    ArticulationPlace.DENTAL: {
        "depth": ArticulationDepth.EXTERNAL,
        "type": MeaningType.PHYSICAL,
        "emotional_score": 0.3,
        "physical_score": 0.7,
        "general_meanings": ["النفاذ", "الحدة", "القطع"]
    },
    # الحروف الشفوية = مادية/واقعية
    ArticulationPlace.LABIAL: {
        "depth": ArticulationDepth.EXTERNAL,
        "type": MeaningType.PHYSICAL,
        "emotional_score": 0.3,
        "physical_score": 0.8,
        "general_meanings": ["البناء", "الانفجار", "الضم", "الإغلاق"]
    },
}

# أصوات البكاء وحروف العلة
VOWEL_MEANINGS = {
    "ا": {  # آ - الألف الممدودة
        "cry_type": "طلب الحنان",
        "infant_meaning": "يريد الرفع على الأكتاف والعناية",
        "general_meanings": ["الألفة", "الود", "الارتفاع", "العلو"]
    },
    "و": {  # واو
        "cry_type": "طلب اللحاق",
        "infant_meaning": "يريد اللحاق والمجاورة والذهاب مع ذويه",
        "general_meanings": ["اللحاق", "المجاورة", "التدحرج", "الذهاب معاً"]
    },
    "ي": {  # ياء
        "cry_type": "تعبير عن ألم",
        "infant_meaning": "يعبر عن ألم وضيق نفسي يحز به",
        "general_meanings": ["الألم", "الضيق النفسي", "التلوي"]
    },
}


# ==================== قواعد اسم الحرف ====================

# استنباط المعنى من اسم الحرف نفسه
LETTER_NAME_MEANINGS = {
    # العربية
    "ا": {"name": "ألف", "derived_from": "ألفة", "meanings": ["الألفة", "الود", "التآلف"]},
    "ب": {"name": "باء", "derived_from": "باء يبوء", "meanings": ["التحمل", "الدك", "التشبع", "البناء"]},
    "ج": {"name": "جيم", "derived_from": "جام غضبه", "meanings": ["الجمع", "التدفق دفعة واحدة"]},
    "د": {"name": "دال", "derived_from": "دلّ يدل", "meanings": ["الدلالة", "المبادرة", "الابتداء"]},
    "ص": {"name": "صاد", "derived_from": "صاد يصيد", "meanings": ["القنص", "الصيد", "الصد", "الصدى"]},
    "ذ": {"name": "ذال", "derived_from": "ذلّ يذل", "meanings": ["الذل", "الخضوع"]},
    "ع": {"name": "عين", "derived_from": "عين", "meanings": ["الرؤية", "العمق", "المعرفة", "العين"]},
    "ر": {"name": "راء", "derived_from": "رأى يرى", "meanings": ["الرؤية", "التدفق"]},
    "ك": {"name": "كاف", "derived_from": "كفى", "meanings": ["الكفاية", "العطاء"]},
    "م": {"name": "ميم", "derived_from": "أم", "meanings": ["الأمومة", "الاحتواء", "الضم"]},
    "ن": {"name": "نون", "derived_from": "نور", "meanings": ["النور", "الظهور"]},
    "ل": {"name": "لام", "derived_from": "لمّ", "meanings": ["اللم", "الجمع", "الإحاطة"]},
    "ه": {"name": "هاء", "derived_from": "هو", "meanings": ["الهوية", "الذات", "النفس"]},

    # الإنجليزية - قاعدة ing
    "K": {"name": "K", "ing_meaning": "king=ملك", "meanings": ["الاستمرار", "العطاء", "الملك"]},
    "S": {"name": "S", "ing_meaning": "sing=غناء", "meanings": ["الاستمرار", "الالتواء", "الرقص"]},
    "R": {"name": "R", "ing_meaning": "ring=حلقة", "meanings": ["الدوران", "الاستمرار"]},
}


# ==================== محركات الاستنباط ====================

class ShapeInferenceEngine:
    """محرك الاستنباط الشكلي - من شكل الحرف"""

    def infer(self, letter: str) -> List[InferredMeaning]:
        """استنباط المعاني من شكل الحرف"""
        results = []

        # البحث في الحروف العربية
        if letter in ARABIC_SHAPE_MEANINGS:
            data = ARABIC_SHAPE_MEANINGS[letter]
            for meaning in data["meanings"]:
                results.append(InferredMeaning(
                    meaning=meaning,
                    method=InferenceMethod.SHAPE,
                    confidence=0.8,
                    evidence=[
                        f"الشكل يشبه: {', '.join(data['resembles'])}",
                        f"النمط البصري: {', '.join(data['patterns'])}"
                    ]
                ))

        # البحث في الحروف الإنجليزية
        if letter in ENGLISH_SHAPE_MEANINGS:
            data = ENGLISH_SHAPE_MEANINGS[letter]
            for meaning in data["meanings"]:
                results.append(InferredMeaning(
                    meaning=meaning,
                    method=InferenceMethod.SHAPE,
                    confidence=0.8,
                    evidence=[
                        f"الشكل يشبه: {', '.join(data['resembles'])}",
                        f"النمط البصري: {', '.join(data['patterns'])}"
                    ]
                ))

        return results

    def get_shape_analysis(self, letter: str) -> Optional[ShapeAnalysis]:
        """الحصول على تحليل شكلي كامل"""
        data = ARABIC_SHAPE_MEANINGS.get(letter) or ENGLISH_SHAPE_MEANINGS.get(letter)
        if not data:
            return None

        return ShapeAnalysis(
            letter=letter,
            shape_types=data["shapes"],
            natural_resemblances=data["resembles"],
            implied_meanings=data["meanings"],
            visual_patterns=data["patterns"]
        )


class SoundInferenceEngine:
    """محرك الاستنباط الصوتي - من صوت ومخرج الحرف"""

    # خريطة الحروف ومخارجها
    LETTER_ARTICULATION = {
        # الحروف الحنجرية (جوفية - نفسية)
        "ء": ArticulationPlace.GLOTTAL,
        "ه": ArticulationPlace.GLOTTAL,
        # الحروف الحلقية (جوفية - نفسية)
        "ع": ArticulationPlace.PHARYNGEAL,
        "غ": ArticulationPlace.PHARYNGEAL,
        "ح": ArticulationPlace.PHARYNGEAL,
        "خ": ArticulationPlace.PHARYNGEAL,
        # الحروف اللهوية (متوسطة)
        "ك": ArticulationPlace.VELAR,
        "ق": ArticulationPlace.VELAR,
        # الحروف الغارية (متوسطة)
        "ي": ArticulationPlace.PALATAL,
        "ش": ArticulationPlace.PALATAL,
        "ج": ArticulationPlace.PALATAL,
        # الحروف اللثوية (متوسطة-مادية)
        "ت": ArticulationPlace.ALVEOLAR,
        "د": ArticulationPlace.ALVEOLAR,
        "ط": ArticulationPlace.ALVEOLAR,
        "ض": ArticulationPlace.ALVEOLAR,
        "ن": ArticulationPlace.ALVEOLAR,
        "ل": ArticulationPlace.ALVEOLAR,
        "ر": ArticulationPlace.ALVEOLAR,
        "س": ArticulationPlace.ALVEOLAR,
        "ز": ArticulationPlace.ALVEOLAR,
        "ص": ArticulationPlace.ALVEOLAR,
        # الحروف الأسنانية (خارجية - مادية)
        "ث": ArticulationPlace.DENTAL,
        "ذ": ArticulationPlace.DENTAL,
        "ظ": ArticulationPlace.DENTAL,
        # الحروف الشفوية (خارجية - مادية)
        "ب": ArticulationPlace.LABIAL,
        "م": ArticulationPlace.LABIAL,
        "و": ArticulationPlace.LABIAL,
        "ف": ArticulationPlace.LABIAL,
        # الألف
        "ا": ArticulationPlace.GLOTTAL,
    }

    def infer(self, letter: str) -> List[InferredMeaning]:
        """استنباط المعاني من صوت ومخرج الحرف"""
        results = []

        place = self.LETTER_ARTICULATION.get(letter)
        if not place:
            return results

        meaning_data = ARTICULATION_MEANING_MAP.get(place)
        if not meaning_data:
            return results

        for meaning in meaning_data["general_meanings"]:
            results.append(InferredMeaning(
                meaning=meaning,
                method=InferenceMethod.SOUND,
                confidence=0.75,
                evidence=[
                    f"المخرج: {place.value}",
                    f"العمق: {meaning_data['depth'].value}",
                    f"نوع المعنى: {meaning_data['type'].value}"
                ]
            ))

        # إضافة معاني حروف العلة
        if letter in VOWEL_MEANINGS:
            vowel_data = VOWEL_MEANINGS[letter]
            for meaning in vowel_data["general_meanings"]:
                results.append(InferredMeaning(
                    meaning=meaning,
                    method=InferenceMethod.SOUND,
                    confidence=0.85,
                    evidence=[
                        f"نوع البكاء: {vowel_data['cry_type']}",
                        f"معنى الرضيع: {vowel_data['infant_meaning']}"
                    ]
                ))

        return results

    def get_sound_analysis(self, letter: str) -> Optional[SoundAnalysis]:
        """الحصول على تحليل صوتي كامل"""
        place = self.LETTER_ARTICULATION.get(letter)
        if not place:
            return None

        meaning_data = ARTICULATION_MEANING_MAP.get(place, {})

        return SoundAnalysis(
            letter=letter,
            articulation_place=place,
            articulation_manner=ArticulationManner.PLOSIVE,  # افتراضي
            depth=meaning_data.get("depth", ArticulationDepth.MIDDLE),
            meaning_type=meaning_data.get("type", MeaningType.MIXED),
            emotional_score=meaning_data.get("emotional_score", 0.5),
            physical_score=meaning_data.get("physical_score", 0.5),
            implied_meanings=meaning_data.get("general_meanings", [])
        )


class LetterNameInferenceEngine:
    """محرك استنباط اسم الحرف - من اسم الحرف نفسه"""

    def infer(self, letter: str) -> List[InferredMeaning]:
        """استنباط المعاني من اسم الحرف"""
        results = []

        if letter in LETTER_NAME_MEANINGS:
            data = LETTER_NAME_MEANINGS[letter]
            for meaning in data["meanings"]:
                evidence = [f"اسم الحرف: {data['name']}"]
                if "derived_from" in data:
                    evidence.append(f"مشتق من: {data['derived_from']}")
                if "ing_meaning" in data:
                    evidence.append(f"قاعدة ing: {data['ing_meaning']}")

                results.append(InferredMeaning(
                    meaning=meaning,
                    method=InferenceMethod.LETTER_NAME,
                    confidence=0.9,
                    evidence=evidence
                ))

        return results


# ==================== المحرك الرئيسي الموحد ====================

class MeaningInferenceEngine:
    """
    المحرك الرئيسي لاستنباط معاني الحروف والكلمات

    يجمع كل محركات الاستنباط ويوفر واجهة موحدة:
    1. الاستنباط الشكلي - من شكل الحرف
    2. الاستنباط الصوتي - من صوت ومخرج الحرف
    3. استنباط اسم الحرف - من اسم الحرف نفسه
    4. الاستنباط المعجمي - من كلمات مشتركة (سيُضاف لاحقاً)
    5. السلاسل السببية - ربط المعاني (سيُضاف لاحقاً)
    """

    def __init__(self):
        self.shape_engine = ShapeInferenceEngine()
        self.sound_engine = SoundInferenceEngine()
        self.name_engine = LetterNameInferenceEngine()

    def infer_letter_meanings(self, letter: str) -> List[InferredMeaning]:
        """
        استنباط جميع معاني الحرف من كل المصادر

        Args:
            letter: الحرف المراد تحليله

        Returns:
            قائمة بالمعاني المستنبطة مع مستوى الثقة والأدلة
        """
        all_meanings = []

        # جمع المعاني من كل المحركات
        all_meanings.extend(self.shape_engine.infer(letter))
        all_meanings.extend(self.sound_engine.infer(letter))
        all_meanings.extend(self.name_engine.infer(letter))

        # ترتيب حسب الثقة
        all_meanings.sort(key=lambda x: x.confidence, reverse=True)

        # دمج المعاني المتكررة وزيادة ثقتها
        merged = self._merge_similar_meanings(all_meanings)

        return merged

    def infer_word_meaning(self, word: str) -> Dict[str, Any]:
        """
        استنباط معنى كلمة كاملة من معاني حروفها

        Args:
            word: الكلمة المراد تحليلها

        Returns:
            قاموس يحتوي على تحليل الكلمة
        """
        letter_analyses = []
        all_meanings = []

        for i, letter in enumerate(word):
            meanings = self.infer_letter_meanings(letter)
            letter_analyses.append({
                "letter": letter,
                "position": i + 1,
                "meanings": meanings
            })
            all_meanings.extend(meanings)

        # حساب المعنى المركب
        combined_meaning = self._combine_meanings(all_meanings)

        # حساب النوع (نفسي/مادي)
        emotional_score, physical_score = self._calculate_scores(word)

        return {
            "word": word,
            "letters": letter_analyses,
            "combined_meaning": combined_meaning,
            "emotional_score": emotional_score,
            "physical_score": physical_score,
            "meaning_type": "نفسي" if emotional_score > physical_score else "مادي",
            "top_meanings": self._get_top_meanings(all_meanings, 5)
        }

    def _merge_similar_meanings(self, meanings: List[InferredMeaning]) -> List[InferredMeaning]:
        """دمج المعاني المتشابهة وزيادة ثقتها"""
        merged = {}
        for m in meanings:
            if m.meaning in merged:
                # زيادة الثقة عند التكرار
                old = merged[m.meaning]
                old.confidence = min(1.0, old.confidence + 0.1)
                old.evidence.extend(m.evidence)
            else:
                merged[m.meaning] = m
        return list(merged.values())

    def _combine_meanings(self, meanings: List[InferredMeaning]) -> str:
        """تجميع المعاني في نص واحد"""
        unique_meanings = list(set(m.meaning for m in meanings if m.confidence > 0.5))
        return " + ".join(unique_meanings[:5])

    def _calculate_scores(self, word: str) -> Tuple[float, float]:
        """حساب درجة النفسي والمادي للكلمة"""
        emotional_total = 0.0
        physical_total = 0.0
        count = 0

        for letter in word:
            analysis = self.sound_engine.get_sound_analysis(letter)
            if analysis:
                emotional_total += analysis.emotional_score
                physical_total += analysis.physical_score
                count += 1

        if count == 0:
            return 0.5, 0.5

        return emotional_total / count, physical_total / count

    def _get_top_meanings(self, meanings: List[InferredMeaning], n: int) -> List[str]:
        """الحصول على أهم n معاني"""
        sorted_meanings = sorted(meanings, key=lambda x: x.confidence, reverse=True)
        seen = set()
        result = []
        for m in sorted_meanings:
            if m.meaning not in seen:
                seen.add(m.meaning)
                result.append(m.meaning)
                if len(result) >= n:
                    break
        return result

    def get_full_letter_analysis(self, letter: str) -> Dict[str, Any]:
        """الحصول على تحليل كامل للحرف"""
        shape_analysis = self.shape_engine.get_shape_analysis(letter)
        sound_analysis = self.sound_engine.get_sound_analysis(letter)
        inferred_meanings = self.infer_letter_meanings(letter)

        return {
            "letter": letter,
            "shape": {
                "types": [s.value for s in shape_analysis.shape_types] if shape_analysis else [],
                "resembles": shape_analysis.natural_resemblances if shape_analysis else [],
                "patterns": shape_analysis.visual_patterns if shape_analysis else []
            } if shape_analysis else None,
            "sound": {
                "articulation_place": sound_analysis.articulation_place.value if sound_analysis else None,
                "depth": sound_analysis.depth.value if sound_analysis else None,
                "type": sound_analysis.meaning_type.value if sound_analysis else None,
                "emotional_score": sound_analysis.emotional_score if sound_analysis else 0.5,
                "physical_score": sound_analysis.physical_score if sound_analysis else 0.5
            } if sound_analysis else None,
            "inferred_meanings": [
                {
                    "meaning": m.meaning,
                    "method": m.method.value,
                    "confidence": m.confidence,
                    "evidence": m.evidence
                }
                for m in inferred_meanings
            ]
        }


# ==================== الدوال المساعدة ====================

def infer_meanings(letter: str) -> List[InferredMeaning]:
    """دالة مختصرة لاستنباط معاني حرف"""
    engine = MeaningInferenceEngine()
    return engine.infer_letter_meanings(letter)


def analyze_word(word: str) -> Dict[str, Any]:
    """دالة مختصرة لتحليل كلمة"""
    engine = MeaningInferenceEngine()
    return engine.infer_word_meaning(word)


# ==================== محرك الاستنباط المعجمي ====================

class LexicalInferenceEngine:
    """
    محرك الاستنباط المعجمي - من كلمات مشتركة في حروف

    الطريقة المثلى لاستنباط معاني الحروف هي الرجوع العكسي للمعاجم:
    - البحث عن كلمات تشترك في حرف أو حرفين
    - استخراج المعاني المشتركة بينها

    مثال: "طلب، حلب، غلب، سحب، نهب، هرب" - كلها تشترك في معنى الحمل والانتقال
    """

    # قاعدة بيانات الكلمات المشتركة ومعانيها
    # يمكن توسيعها لاحقاً بربطها بمعاجم عربية حقيقية
    SHARED_LETTER_PATTERNS = {
        # كلمات تشترك في حرف الباء
        "ب": {
            "words": ["طلب", "حلب", "غلب", "سحب", "نهب", "هرب", "كسب", "ربح"],
            "common_meaning": "الحمل والانتقال",
            "evidence": "كل هذه الكلمات تتضمن معنى حمل شيء ونقله"
        },
        # كلمات تشترك في حرف السين
        "س": {
            "words": ["سحل", "سحب", "سال", "سار", "سقط"],
            "common_meaning": "الانسياب والحركة الناعمة",
            "evidence": "السين تفيد الحركة السلسة والانزلاق"
        },
        # كلمات تشترك في حرف الراء
        "ر": {
            "words": ["جرى", "مر", "سار", "طار", "دار"],
            "common_meaning": "التدفق والحركة المستمرة",
            "evidence": "الراء تفيد التكرار والتدفق"
        },
        # كلمات تشترك في حرف اللام
        "ل": {
            "words": ["لف", "لوى", "سحل", "قبول", "لولب"],
            "common_meaning": "الإحاطة والالتفاف",
            "evidence": "اللام تفيد اللف والإحاطة"
        },
        # كلمات تشترك في حرف الميم
        "م": {
            "words": ["ضم", "جمع", "لم", "أم", "احتوى"],
            "common_meaning": "الاحتواء والضم",
            "evidence": "الميم تفيد الاحتواء والإغلاق"
        },
        # كلمات تشترك في حرف الصاد
        "ص": {
            "words": ["بصر", "نظر", "أصم", "صمت", "إصغاء"],
            "common_meaning": "الحواس والإدراك",
            "evidence": "شكل الصاد البيضاوي يرمز للعين والأذن"
        },
        # كلمات تشترك في حرف القاف
        "ق": {
            "words": ["قطع", "قص", "قسم", "قطف", "قطر"],
            "common_meaning": "القطع والفصل",
            "evidence": "القاف تفيد القطع والانفصال"
        },
        # كلمات تشترك في حرف الكاف
        "ك": {
            "words": ["كرم", "ملك", "كفى", "حك", "فك"],
            "common_meaning": "العطاء والتملك",
            "evidence": "الكاف تفيد الحمل والعطاء"
        },
        # كلمات تشترك في حرف العين
        "ع": {
            "words": ["عمل", "علم", "عرف", "رأى", "نظر"],
            "common_meaning": "العمق والمعرفة",
            "evidence": "العين تفيد الرؤية والإدراك العميق"
        },
        # كلمات تشترك في حرف الحاء
        "ح": {
            "words": ["حرارة", "حياة", "روح", "نفح", "سبح"],
            "common_meaning": "الحرارة والحياة",
            "evidence": "الحاء صوت الجهد والعطش"
        },
    }

    # أنماط الحروف المتعاقبة ومعانيها المشتركة
    LETTER_PAIR_PATTERNS = {
        "سح": {
            "words": ["سحل", "سحب", "سحق", "سحر"],
            "common_meaning": "السحب والجذب",
            "evidence": "تتابع السين والحاء يفيد السحب"
        },
        "بل": {
            "words": ["بلع", "بلغ", "بلد", "قبل"],
            "common_meaning": "البلوغ والوصول",
            "evidence": "الباء واللام معاً تفيد الوصول"
        },
        "قط": {
            "words": ["قطع", "قطف", "قطر", "نقط"],
            "common_meaning": "القطع والتجزئة",
            "evidence": "القاف والطاء معاً تفيد القطع الحاد"
        },
    }

    def infer(self, letter: str) -> List[InferredMeaning]:
        """استنباط معاني حرف من كلمات مشتركة"""
        results = []

        if letter in self.SHARED_LETTER_PATTERNS:
            data = self.SHARED_LETTER_PATTERNS[letter]
            results.append(InferredMeaning(
                meaning=data["common_meaning"],
                method=InferenceMethod.LEXICAL,
                confidence=0.85,
                evidence=[
                    f"كلمات مشتركة: {', '.join(data['words'][:5])}",
                    data["evidence"]
                ]
            ))

        return results

    def infer_from_pair(self, letter1: str, letter2: str) -> List[InferredMeaning]:
        """استنباط معاني من زوج حروف متعاقبة"""
        results = []
        pair = letter1 + letter2

        if pair in self.LETTER_PAIR_PATTERNS:
            data = self.LETTER_PAIR_PATTERNS[pair]
            results.append(InferredMeaning(
                meaning=data["common_meaning"],
                method=InferenceMethod.LEXICAL,
                confidence=0.9,
                evidence=[
                    f"كلمات مشتركة: {', '.join(data['words'][:5])}",
                    data["evidence"]
                ]
            ))

        return results

    def find_similar_words(self, letters: List[str]) -> List[str]:
        """البحث عن كلمات تشترك في حروف معينة"""
        all_words = set()
        for letter in letters:
            if letter in self.SHARED_LETTER_PATTERNS:
                all_words.update(self.SHARED_LETTER_PATTERNS[letter]["words"])
        return list(all_words)


# تحديث المحرك الرئيسي ليشمل الاستنباط المعجمي
class EnhancedMeaningInferenceEngine(MeaningInferenceEngine):
    """محرك استنباط محسن يشمل الاستنباط المعجمي"""

    def __init__(self):
        super().__init__()
        self.lexical_engine = LexicalInferenceEngine()

    def infer_letter_meanings(self, letter: str) -> List[InferredMeaning]:
        """استنباط جميع معاني الحرف من كل المصادر"""
        all_meanings = super().infer_letter_meanings(letter)

        # إضافة الاستنباط المعجمي
        all_meanings.extend(self.lexical_engine.infer(letter))

        # ترتيب حسب الثقة
        all_meanings.sort(key=lambda x: x.confidence, reverse=True)

        return self._merge_similar_meanings(all_meanings)

    def infer_word_meaning(self, word: str) -> Dict[str, Any]:
        """استنباط معنى كلمة مع تحليل أنماط الحروف"""
        result = super().infer_word_meaning(word)

        # البحث عن أنماط حروف متعاقبة
        pair_meanings = []
        for i in range(len(word) - 1):
            pair_meanings.extend(
                self.lexical_engine.infer_from_pair(word[i], word[i+1])
            )

        if pair_meanings:
            result["pair_patterns"] = [
                {"meaning": m.meaning, "evidence": m.evidence}
                for m in pair_meanings
            ]

        return result

    def get_full_letter_analysis(self, letter: str) -> Dict[str, Any]:
        """
        تحليل كامل لحرف واحد من جميع المصادر

        Returns:
            قاموس يحتوي على:
            - shape_analysis: تحليل الشكل
            - sound_analysis: تحليل الصوت
            - name_analysis: تحليل الاسم
            - lexical_analysis: تحليل معجمي
            - all_meanings: جميع المعاني المستنبطة
        """
        result = {
            "letter": letter,
            "الحرف": letter,
            "shape_analysis": None,
            "تحليل_الشكل": None,
            "sound_analysis": None,
            "تحليل_الصوت": None,
            "name_analysis": None,
            "تحليل_الاسم": None,
            "lexical_analysis": None,
            "تحليل_معجمي": None,
            "all_meanings": [],
            "جميع_المعاني": []
        }

        # تحليل الشكل
        shape_meanings = self.shape_engine.infer(letter)
        if shape_meanings:
            result["shape_analysis"] = {
                "meanings": [m.meaning for m in shape_meanings],
                "evidence": shape_meanings[0].evidence if shape_meanings else []
            }
            result["تحليل_الشكل"] = result["shape_analysis"]

        # تحليل الصوت
        sound_meanings = self.sound_engine.infer(letter)
        if sound_meanings:
            result["sound_analysis"] = {
                "meanings": [m.meaning for m in sound_meanings],
                "evidence": sound_meanings[0].evidence if sound_meanings else []
            }
            result["تحليل_الصوت"] = result["sound_analysis"]

        # تحليل الاسم
        name_meanings = self.name_engine.infer(letter)
        if name_meanings:
            result["name_analysis"] = {
                "meanings": [m.meaning for m in name_meanings],
                "evidence": name_meanings[0].evidence if name_meanings else []
            }
            result["تحليل_الاسم"] = result["name_analysis"]

        # تحليل معجمي
        lexical_meanings = self.lexical_engine.infer(letter)
        if lexical_meanings:
            result["lexical_analysis"] = {
                "meanings": [m.meaning for m in lexical_meanings],
                "evidence": lexical_meanings[0].evidence if lexical_meanings else [],
                "similar_words": self.lexical_engine.find_similar_words([letter])
            }
            result["تحليل_معجمي"] = result["lexical_analysis"]

        # جميع المعاني
        all_meanings = self.infer_letter_meanings(letter)
        result["all_meanings"] = [
            {
                "meaning": m.meaning,
                "method": m.method.value,
                "confidence": m.confidence
            }
            for m in all_meanings
        ]
        result["جميع_المعاني"] = result["all_meanings"]

        return result

