#!/usr/bin/env python3
"""
جسر بيان-بصيرة: ربط النظام اللغوي بالنظام البصري
Bayan-Baserah Bridge: Connecting Linguistic and Visual Systems

🧬 الفكرة الثورية:
   - بيان: يستنبط معنى الحرف من شكله (سيميائية الحروف)
   - بصيرة: يستنبط معادلة الشكل من الصورة
   - الجسر: يربط بين العالمين - حرف ↔ شكل ↔ معادلة ↔ معنى

المطور: باسل يحيى عبدالله
"""

import sys
import os
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

# إضافة مسارات الاستيراد
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد من بيان (سيميائية الحروف)
try:
    from bayan.bayan.letter_semiotics import (
        ArabicLetterDatabase, LetterAnalyzer, WordAnalyzer,
        ShapeType as BayanShapeType
    )
    from bayan.bayan.letter_semiotics.inference_engine import (
        ARABIC_SHAPE_MEANINGS, ShapeInferenceEngine
    )
    BAYAN_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ تحذير: لم يتم العثور على سيميائية الحروف: {e}")
    BAYAN_AVAILABLE = False

# استيراد من بصيرة
try:
    from baserah_ai_main.core.enhanced_general_shape_equation import (
        EnhancedGeneralShapeEquation, ShapeMetadata, ShapeType as BaserahShapeType
    )
    from baserah_ai_main.core.revolutionary_mother_equation import RevolutionaryMotherEquation
    BASERAH_AVAILABLE = True
except ImportError:
    try:
        # محاولة استيراد من المسار البديل
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'baserah_ai-main'))
        from core.enhanced_general_shape_equation import (
            EnhancedGeneralShapeEquation, ShapeMetadata, ShapeType as BaserahShapeType
        )
        BASERAH_AVAILABLE = True
    except ImportError as e:
        print(f"⚠️ تحذير: لم يتم العثور على بصيرة: {e}")
        BASERAH_AVAILABLE = False


class LetterShapeType(Enum):
    """أنواع أشكال الحروف العربية"""
    STRAIGHT = "مستقيم"      # ا، ل
    CURVED = "منحني"         # ب، ت، ث، ن
    CIRCULAR = "دائري"       # و، م
    ANGULAR = "زاوي"         # ح، ج، خ
    POINTED = "مدبب"         # ي، ق
    OPEN = "مفتوح"           # ع، غ
    CLOSED = "مغلق"          # ص، ض، ط، ظ
    ASCENDING = "صاعد"       # ك، ط
    DESCENDING = "نازل"      # ي، ر


@dataclass
class LetterVisualAnalysis:
    """تحليل بصري للحرف"""
    letter: str
    shape_type: LetterShapeType
    visual_features: Dict[str, float] = field(default_factory=dict)
    baserah_equation: Optional[Dict] = None
    semantic_meanings: List[str] = field(default_factory=list)
    confidence: float = 0.0


# ربط أشكال الحروف بمعادلات بصيرة
LETTER_SHAPE_EQUATIONS = {
    # الحروف المستقيمة - معادلة خطية
    "ا": {"type": "linear", "params": {"angle": 90, "length": 1.0}},
    "ل": {"type": "linear", "params": {"angle": 90, "length": 0.8, "hook": True}},
    
    # الحروف المنحنية - معادلة سيجمويد
    "ب": {"type": "sigmoid", "params": {"k": 2.0, "open": "up"}},
    "ت": {"type": "sigmoid", "params": {"k": 2.0, "dots": 2}},
    "ث": {"type": "sigmoid", "params": {"k": 2.0, "dots": 3}},
    "ن": {"type": "sigmoid", "params": {"k": 3.0, "open": "up", "dot": 1}},
    
    # الحروف الدائرية - معادلة دائرة
    "و": {"type": "circle", "params": {"radius": 0.3, "tail": True}},
    "م": {"type": "circle", "params": {"radius": 0.25, "closed": True}},
    "ه": {"type": "circle", "params": {"radius": 0.2, "double": True}},
    
    # الحروف الزاوية - معادلة مركبة
    "ح": {"type": "angular", "params": {"depth": 0.5, "open": True}},
    "ج": {"type": "angular", "params": {"depth": 0.5, "dot": "inside"}},
    "خ": {"type": "angular", "params": {"depth": 0.5, "dot": "above"}},
    
    # الحروف المفتوحة
    "ع": {"type": "open_curve", "params": {"depth": 0.7, "hook": True}},
    "غ": {"type": "open_curve", "params": {"depth": 0.7, "dot": "above"}},
    
    # حروف أخرى
    "ر": {"type": "curve", "params": {"direction": "down", "angle": 45}},
    "ز": {"type": "curve", "params": {"direction": "down", "angle": 45, "dot": 1}},
    "س": {"type": "wave", "params": {"peaks": 3}},
    "ش": {"type": "wave", "params": {"peaks": 3, "dots": 3}},
    "ص": {"type": "closed_curve", "params": {"tail": True}},
    "ض": {"type": "closed_curve", "params": {"tail": True, "dot": 1}},
    "ط": {"type": "closed_curve", "params": {"vertical": True}},
    "ظ": {"type": "closed_curve", "params": {"vertical": True, "dot": 1}},
    "ف": {"type": "circle_stem", "params": {"dot": "above"}},
    "ق": {"type": "circle_stem", "params": {"dots": 2}},
    "ك": {"type": "ascending", "params": {"hamza": True}},
    "ي": {"type": "descending", "params": {"dots": 2}},
    "ء": {"type": "hamza", "params": {"standalone": True}},
    "ة": {"type": "circle", "params": {"dots": 2, "ta_marbuta": True}},
    "ى": {"type": "descending", "params": {"alef_maqsura": True}},
    "د": {"type": "angular_simple", "params": {"open": "right"}},
    "ذ": {"type": "angular_simple", "params": {"open": "right", "dot": 1}},
}


# معاني الأشكال المشتركة بين بيان وبصيرة
SHAPE_MEANING_BRIDGE = {
    "مستقيم": {
        "bayan_meanings": ["الاستقامة", "الوضوح", "الارتفاع", "العلو"],
        "baserah_equation": "linear",
        "visual_concept": "الخط المستقيم يمثل الثبات والوضوح"
    },
    "منحني": {
        "bayan_meanings": ["الاحتواء", "الليونة", "المرونة", "الاستقبال"],
        "baserah_equation": "sigmoid",
        "visual_concept": "المنحنى يمثل الاحتضان والتكيف"
    },
    "دائري": {
        "bayan_meanings": ["الكمال", "الاستمرار", "الوحدة", "الشمول"],
        "baserah_equation": "circle",
        "visual_concept": "الدائرة تمثل الكمال والاستمرارية"
    },
    "زاوي": {
        "bayan_meanings": ["القوة", "الحدة", "التحول", "الانعطاف"],
        "baserah_equation": "angular",
        "visual_concept": "الزاوية تمثل التغيير والتحول"
    },
    "مفتوح": {
        "bayan_meanings": ["الانفتاح", "التقبل", "العمق", "البصيرة"],
        "baserah_equation": "open_curve",
        "visual_concept": "الانفتاح يمثل التقبل والفهم"
    },
}


class BayanBaserahBridge:
    """
    الجسر الثوري بين بيان وبصيرة

    🧬 يربط بين:
       - سيميائية الحروف في بيان (شكل → معنى)
       - معادلات الأشكال في بصيرة (شكل → معادلة)

    🎯 التكامل:
       حرف ↔ شكل ↔ معادلة ↔ معنى
    """

    def __init__(self):
        self.creator = "باسل يحيى عبدالله"
        self.version = "1.0.0"

        # تهيئة مكونات بيان
        if BAYAN_AVAILABLE:
            self.arabic_db = ArabicLetterDatabase()
            self.letter_analyzer = LetterAnalyzer()
            self.word_analyzer = WordAnalyzer()
            self.shape_engine = ShapeInferenceEngine()
        else:
            self.arabic_db = None
            self.letter_analyzer = None
            self.word_analyzer = None
            self.shape_engine = None

        # تهيئة مكونات بصيرة
        if BASERAH_AVAILABLE:
            self.shape_equation = EnhancedGeneralShapeEquation()
        else:
            self.shape_equation = None

        print("🌉 جسر بيان-بصيرة: تم التهيئة")
        print(f"   📝 بيان (سيميائية الحروف): {'✅' if BAYAN_AVAILABLE else '❌'}")
        print(f"   👁️ بصيرة (معادلات الأشكال): {'✅' if BASERAH_AVAILABLE else '❌'}")

    def analyze_letter_visually(self, letter: str) -> LetterVisualAnalysis:
        """
        تحليل بصري متكامل للحرف

        يجمع بين:
        - شكل الحرف من بيان
        - معادلة الشكل من بصيرة
        - المعاني المستنبطة
        """
        # تحديد نوع الشكل
        shape_type = self._get_letter_shape_type(letter)

        # الحصول على معادلة بصيرة
        baserah_eq = LETTER_SHAPE_EQUATIONS.get(letter, {})

        # الحصول على المعاني من بيان
        meanings = []
        if letter in ARABIC_SHAPE_MEANINGS:
            meanings = ARABIC_SHAPE_MEANINGS[letter].get("meanings", [])

        # حساب الخصائص البصرية
        visual_features = self._extract_visual_features(letter)

        # حساب الثقة
        confidence = 0.8 if baserah_eq and meanings else 0.5

        return LetterVisualAnalysis(
            letter=letter,
            shape_type=shape_type,
            visual_features=visual_features,
            baserah_equation=baserah_eq,
            semantic_meanings=meanings,
            confidence=confidence
        )

    def _get_letter_shape_type(self, letter: str) -> LetterShapeType:
        """تحديد نوع شكل الحرف"""
        straight = "ال"
        curved = "بتثنى"
        circular = "ومهة"
        angular = "حجخ"
        pointed = "يق"
        open_letters = "عغ"
        closed = "صضطظ"

        if letter in straight:
            return LetterShapeType.STRAIGHT
        elif letter in curved:
            return LetterShapeType.CURVED
        elif letter in circular:
            return LetterShapeType.CIRCULAR
        elif letter in angular:
            return LetterShapeType.ANGULAR
        elif letter in pointed:
            return LetterShapeType.POINTED
        elif letter in open_letters:
            return LetterShapeType.OPEN
        elif letter in closed:
            return LetterShapeType.CLOSED
        else:
            return LetterShapeType.CURVED

    def _extract_visual_features(self, letter: str) -> Dict[str, float]:
        """استخراج الخصائص البصرية للحرف"""
        eq = LETTER_SHAPE_EQUATIONS.get(letter, {})
        params = eq.get("params", {})

        features = {
            "has_dots": 1.0 if "dot" in params or "dots" in params else 0.0,
            "dot_count": params.get("dots", 1 if "dot" in params else 0),
            "is_open": 1.0 if params.get("open") else 0.0,
            "is_closed": 1.0 if params.get("closed") else 0.0,
            "has_tail": 1.0 if params.get("tail") else 0.0,
            "vertical_emphasis": 1.0 if params.get("vertical") or params.get("angle") == 90 else 0.0,
        }
        return features

    def letter_to_equation(self, letter: str) -> Dict[str, Any]:
        """
        تحويل حرف إلى معادلة رياضية (بصيرة)

        🎯 حرف → شكل → معادلة
        """
        if letter not in LETTER_SHAPE_EQUATIONS:
            return {"error": f"الحرف '{letter}' غير مدعوم حالياً"}

        eq_data = LETTER_SHAPE_EQUATIONS[letter]
        eq_type = eq_data["type"]
        params = eq_data["params"]

        # بناء المعادلة حسب النوع
        if eq_type == "linear":
            equation = f"y = x * tan({params.get('angle', 0)}°)"
        elif eq_type == "sigmoid":
            k = params.get("k", 2.0)
            equation = f"y = 1 / (1 + e^(-{k}*x))"
        elif eq_type == "circle":
            r = params.get("radius", 0.3)
            equation = f"x² + y² = {r}²"
        elif eq_type == "wave":
            peaks = params.get("peaks", 3)
            equation = f"y = sin({peaks}*x)"
        else:
            equation = f"معادلة مركبة من نوع: {eq_type}"

        return {
            "letter": letter,
            "equation_type": eq_type,
            "equation": equation,
            "parameters": params,
            "visual_features": self._extract_visual_features(letter)
        }

    def equation_to_meaning(self, equation_type: str) -> List[str]:
        """
        تحويل نوع المعادلة إلى معاني دلالية

        🎯 معادلة → شكل → معنى
        """
        type_to_shape = {
            "linear": "مستقيم",
            "sigmoid": "منحني",
            "circle": "دائري",
            "angular": "زاوي",
            "open_curve": "مفتوح",
            "wave": "منحني",
            "curve": "منحني",
        }

        shape_name = type_to_shape.get(equation_type, "منحني")
        bridge_data = SHAPE_MEANING_BRIDGE.get(shape_name, {})

        return bridge_data.get("bayan_meanings", [])

    def word_visual_analysis(self, word: str) -> Dict[str, Any]:
        """
        تحليل بصري لكلمة كاملة

        يحلل كل حرف ويجمع النتائج
        """
        letters_analysis = []
        combined_meanings = []
        equations = []

        for letter in word:
            if letter.isalpha():
                analysis = self.analyze_letter_visually(letter)
                letters_analysis.append({
                    "letter": letter,
                    "shape": analysis.shape_type.value,
                    "meanings": analysis.semantic_meanings[:3],
                    "equation": analysis.baserah_equation
                })
                combined_meanings.extend(analysis.semantic_meanings)
                if analysis.baserah_equation:
                    equations.append(analysis.baserah_equation)

        # إزالة المعاني المكررة مع الحفاظ على الترتيب
        seen = set()
        unique_meanings = []
        for m in combined_meanings:
            if m not in seen:
                seen.add(m)
                unique_meanings.append(m)

        return {
            "word": word,
            "letters_count": len(letters_analysis),
            "letters_analysis": letters_analysis,
            "combined_meanings": unique_meanings[:10],
            "equations_summary": equations,
            "visual_harmony": self._calculate_visual_harmony(letters_analysis)
        }

    def _calculate_visual_harmony(self, letters_analysis: List[Dict]) -> float:
        """حساب التناغم البصري بين الحروف"""
        if len(letters_analysis) < 2:
            return 1.0

        shapes = [l["shape"] for l in letters_analysis]

        # التناغم يزيد عندما تتكرر أنواع الأشكال
        unique_shapes = len(set(shapes))
        harmony = 1.0 - (unique_shapes / len(shapes)) * 0.5

        return round(harmony, 2)

    def generate_shape_from_meaning(self, meaning: str) -> Dict[str, Any]:
        """
        توليد شكل من معنى (العملية العكسية)

        🎯 معنى → شكل → معادلة
        """
        # البحث عن الشكل المناسب للمعنى
        for shape_name, data in SHAPE_MEANING_BRIDGE.items():
            if meaning in data["bayan_meanings"]:
                return {
                    "meaning": meaning,
                    "suggested_shape": shape_name,
                    "equation_type": data["baserah_equation"],
                    "visual_concept": data["visual_concept"],
                    "related_meanings": data["bayan_meanings"]
                }

        return {"error": f"لم يتم العثور على شكل مناسب للمعنى: {meaning}"}

    def infer_meaning_from_shape_equation(self, equation_type: str, params: Dict) -> Dict[str, Any]:
        """
        استنباط المعنى من معادلة الشكل (بصيرة → بيان)

        🎯 معادلة → خصائص → معاني
        """
        meanings = self.equation_to_meaning(equation_type)

        # تحليل المعاملات لاستنباط معاني إضافية
        additional_meanings = []

        if params.get("open"):
            additional_meanings.append("الانفتاح")
        if params.get("closed"):
            additional_meanings.append("الإحاطة")
        if params.get("dots"):
            additional_meanings.append("التمييز")
        if params.get("tail"):
            additional_meanings.append("الاستمرار")
        if params.get("hook"):
            additional_meanings.append("التعلق")

        return {
            "equation_type": equation_type,
            "base_meanings": meanings,
            "param_meanings": additional_meanings,
            "combined": meanings + additional_meanings
        }

    def compare_letters_visually(self, letter1: str, letter2: str) -> Dict[str, Any]:
        """
        مقارنة بصرية بين حرفين

        يحلل التشابه والاختلاف في الشكل والمعنى
        """
        analysis1 = self.analyze_letter_visually(letter1)
        analysis2 = self.analyze_letter_visually(letter2)

        # حساب التشابه في الشكل
        shape_similarity = 1.0 if analysis1.shape_type == analysis2.shape_type else 0.0

        # حساب التشابه في المعاني
        meanings1 = set(analysis1.semantic_meanings)
        meanings2 = set(analysis2.semantic_meanings)
        common_meanings = meanings1.intersection(meanings2)

        if meanings1 or meanings2:
            meaning_similarity = len(common_meanings) / len(meanings1.union(meanings2))
        else:
            meaning_similarity = 0.0

        # حساب التشابه في المعادلات
        eq1 = analysis1.baserah_equation or {}
        eq2 = analysis2.baserah_equation or {}
        equation_similarity = 1.0 if eq1.get("type") == eq2.get("type") else 0.0

        overall_similarity = (shape_similarity + meaning_similarity + equation_similarity) / 3

        return {
            "letter1": letter1,
            "letter2": letter2,
            "shape_similarity": round(shape_similarity, 2),
            "meaning_similarity": round(meaning_similarity, 2),
            "equation_similarity": round(equation_similarity, 2),
            "overall_similarity": round(overall_similarity, 2),
            "common_meanings": list(common_meanings),
            "relationship": self._describe_relationship(overall_similarity)
        }

    def _describe_relationship(self, similarity: float) -> str:
        """وصف العلاقة بين الحرفين"""
        if similarity > 0.8:
            return "متشابهان جداً"
        elif similarity > 0.6:
            return "متشابهان"
        elif similarity > 0.4:
            return "متقاربان"
        elif similarity > 0.2:
            return "مختلفان"
        else:
            return "متضادان"

    def find_opposite_letter(self, letter: str) -> Dict[str, Any]:
        """
        إيجاد الحرف المضاد بصرياً

        🎯 يطبق نظرية تعامد الأضداد من بصيرة
        """
        analysis = self.analyze_letter_visually(letter)
        current_shape = analysis.shape_type

        # الأضداد البصرية
        opposites_map = {
            LetterShapeType.STRAIGHT: LetterShapeType.CURVED,
            LetterShapeType.CURVED: LetterShapeType.STRAIGHT,
            LetterShapeType.OPEN: LetterShapeType.CLOSED,
            LetterShapeType.CLOSED: LetterShapeType.OPEN,
            LetterShapeType.ASCENDING: LetterShapeType.DESCENDING,
            LetterShapeType.DESCENDING: LetterShapeType.ASCENDING,
        }

        opposite_shape = opposites_map.get(current_shape, LetterShapeType.CURVED)

        # البحث عن حرف بالشكل المضاد
        opposite_letters = []
        for l in "ابتثجحخدذرزسشصضطظعغفقكلمنهوي":
            l_analysis = self.analyze_letter_visually(l)
            if l_analysis.shape_type == opposite_shape:
                opposite_letters.append(l)

        return {
            "original_letter": letter,
            "original_shape": current_shape.value,
            "opposite_shape": opposite_shape.value,
            "opposite_letters": opposite_letters[:5],
            "theory": "تعامد الأضداد (بصيرة)"
        }


# دالة مساعدة للاستخدام السريع
def create_bridge() -> BayanBaserahBridge:
    """إنشاء جسر بيان-بصيرة"""
    return BayanBaserahBridge()


# للاختبار
if __name__ == "__main__":
    bridge = create_bridge()

    print("\n" + "=" * 60)
    print("🧪 اختبار جسر بيان-بصيرة")
    print("=" * 60)

    # اختبار تحليل حرف
    print("\n📝 تحليل حرف 'ع':")
    analysis = bridge.analyze_letter_visually("ع")
    print(f"   الشكل: {analysis.shape_type.value}")
    print(f"   المعاني: {analysis.semantic_meanings[:3]}")
    print(f"   المعادلة: {analysis.baserah_equation}")

    # اختبار تحويل حرف لمعادلة
    print("\n📐 تحويل حرف 'ب' إلى معادلة:")
    eq = bridge.letter_to_equation("ب")
    print(f"   المعادلة: {eq.get('equation', 'N/A')}")
    print(f"   النوع: {eq.get('equation_type', 'N/A')}")

    # اختبار تحليل كلمة
    print("\n📚 تحليل كلمة 'بيان':")
    word_analysis = bridge.word_visual_analysis("بيان")
    print(f"   عدد الحروف: {word_analysis['letters_count']}")
    print(f"   المعاني المجمعة: {word_analysis['combined_meanings'][:5]}")
    print(f"   التناغم البصري: {word_analysis['visual_harmony']}")

    # اختبار مقارنة الحروف
    print("\n🔍 مقارنة بين 'ب' و 'ت':")
    comparison = bridge.compare_letters_visually("ب", "ت")
    print(f"   التشابه الكلي: {comparison['overall_similarity']}")
    print(f"   العلاقة: {comparison['relationship']}")

    # اختبار إيجاد الضد
    print("\n⚡ الحرف المضاد لـ 'ا':")
    opposite = bridge.find_opposite_letter("ا")
    print(f"   الشكل الأصلي: {opposite['original_shape']}")
    print(f"   الشكل المضاد: {opposite['opposite_shape']}")
    print(f"   الحروف المضادة: {opposite['opposite_letters'][:3]}")

    print("\n" + "=" * 60)
    print("✅ اكتمل الاختبار!")
    print("=" * 60)

