"""
الجسر اللغوي-الرياضي - Linguistic-Mathematical Bridge
======================================================

تحويل المفاهيم اللغوية إلى تمثيلات رياضية والعكس.

المؤلف: باسل يحيى عبدالله
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
import numpy as np

# استيراد من الفص المنطقي
from ..letter_semiotics import ArabicLetterDatabase, WordAnalyzer

# استيراد من الفص الرياضي
from ..baserah_ai import (
    AdaptiveEquation,
    GeneralizedSigmoid, SigmoidParameters,
    DrawingUnit, ShapeGenerator
)

# قاعدة بيانات الحروف العامة
_letter_db = None

def _get_letter_db():
    global _letter_db
    if _letter_db is None:
        _letter_db = ArabicLetterDatabase()
    return _letter_db

def get_letter_info(letter: str):
    """الحصول على معلومات الحرف"""
    db = _get_letter_db()
    info = db.get_letter(letter)
    if info:
        return {
            "الحرف": letter,
            "المعاني": info.meanings if hasattr(info, 'meanings') else [],
            "الشكل": info.shape_features if hasattr(info, 'shape_features') else None
        }
    return None

def analyze_word(word: str):
    """تحليل كلمة"""
    try:
        analyzer = WordAnalyzer(use_camel=False)
        return analyzer.analyze_word(word)
    except:
        return None


@dataclass
class LetterEquation:
    """معادلة الحرف"""
    letter: str
    alpha: float      # قوة المعنى
    k: float          # حدة التأثير
    x0: float         # نقطة التوازن
    meanings: List[str]


def letter_to_equation(letter: str) -> Optional[LetterEquation]:
    """
    تحويل حرف إلى معادلة رياضية
    
    الفكرة: كل حرف له خصائص يمكن تمثيلها رياضياً
    """
    info = get_letter_info(letter)
    if not info:
        return None
    
    meanings = info.get("المعاني", [])
    
    # حساب المعاملات من خصائص الحرف
    # alpha: قوة المعنى (عدد المعاني)
    alpha = min(len(meanings) / 5.0, 1.0) if meanings else 0.5
    
    # k: حدة التأثير (من الموقع في الأبجدية)
    if ord(letter) >= ord('ا') and ord(letter) <= ord('ي'):
        # حرف عربي
        k = (ord(letter) - ord('ا')) / 28.0 * 5.0 + 1.0
    elif letter.isalpha():
        # حرف إنجليزي
        k = (ord(letter.lower()) - ord('a')) / 26.0 * 5.0 + 1.0
    else:
        k = 2.0
    
    # x0: نقطة التوازن (مركز معنى الحرف)
    x0 = 0.0
    
    return LetterEquation(
        letter=letter,
        alpha=alpha,
        k=k,
        x0=x0,
        meanings=meanings
    )


def word_to_shape(word: str, scale: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    تحويل كلمة إلى شكل هندسي
    
    الفكرة: كل كلمة لها "بصمة شكلية" تعكس معناها
    """
    drawer = DrawingUnit()
    
    # تحليل الكلمة
    letters = list(word.replace(" ", ""))
    n = len(letters)
    
    if n == 0:
        return np.array([]), np.array([])
    
    # إنشاء شكل مركب من الحروف
    all_x = []
    all_y = []
    
    for i, letter in enumerate(letters):
        eq = letter_to_equation(letter)
        if eq:
            # رسم دائرة صغيرة لكل حرف
            t = np.linspace(0, 2*np.pi, 20)
            radius = eq.alpha * scale * 0.3
            offset_x = i * scale * 0.8
            offset_y = eq.k * 0.1
            
            x = radius * np.cos(t) + offset_x
            y = radius * np.sin(t) + offset_y
            
            all_x.extend(x)
            all_y.extend(y)
    
    return np.array(all_x), np.array(all_y)


def meaning_to_parameters(meaning: str) -> Dict[str, float]:
    """
    تحويل معنى إلى معاملات رياضية
    
    الفكرة: المعاني المختلفة لها "توقيعات رياضية" مختلفة
    """
    # معاملات افتراضية
    params = {
        "alpha": 0.5,
        "k": 2.0,
        "beta": 0.1,
        "x0": 0.0
    }
    
    # تحليل المعنى
    word_analysis = analyze_word(meaning)
    
    # تعديل المعاملات بناءً على التحليل
    if word_analysis:
        letters_count = len(meaning.replace(" ", ""))
        params["alpha"] = min(letters_count / 10.0, 1.0)
        params["k"] = 1.0 + letters_count * 0.2
    
    # كلمات خاصة
    positive_words = ["قوة", "نور", "خير", "جمال", "حب"]
    negative_words = ["ضعف", "ظلام", "شر", "قبح", "كره"]
    
    for pw in positive_words:
        if pw in meaning:
            params["alpha"] += 0.2
            params["x0"] += 1.0
    
    for nw in negative_words:
        if nw in meaning:
            params["alpha"] += 0.2
            params["x0"] -= 1.0
    
    return params


class LinguisticMathBridge:
    """
    الجسر اللغوي-الرياضي الموحد
    
    يوفر واجهة موحدة للتحويل بين التمثيلات اللغوية والرياضية
    """
    
    def __init__(self):
        self.drawer = DrawingUnit()
        self.shape_generator = ShapeGenerator()
        self.cache: Dict[str, Any] = {}
    
    def analyze(self, text: str) -> Dict:
        """تحليل نص لغوياً ورياضياً"""
        if text in self.cache:
            return self.cache[text]
        
        result = {
            "النص": text,
            "الحروف": [],
            "المعادلات": [],
            "الشكل": None,
            "المعاملات": meaning_to_parameters(text)
        }

        # تحليل الحروف
        for char in text:
            if char.strip():
                eq = letter_to_equation(char)
                if eq:
                    result["الحروف"].append({
                        "الحرف": char,
                        "alpha": eq.alpha,
                        "k": eq.k,
                        "المعاني": eq.meanings[:3]
                    })
                    result["المعادلات"].append(eq)

        # إنشاء الشكل
        x, y = word_to_shape(text)
        if len(x) > 0:
            result["الشكل"] = {"x": x.tolist()[:50], "y": y.tolist()[:50]}

        self.cache[text] = result
        return result

    def create_equation_from_word(self, word: str) -> AdaptiveEquation:
        """إنشاء معادلة متكيفة من كلمة"""
        analysis = self.analyze(word)

        alphas = [eq.alpha for eq in analysis["المعادلات"]]
        ks = [eq.k for eq in analysis["المعادلات"]]

        if not alphas:
            alphas = [0.5]
            ks = [2.0]

        return AdaptiveEquation(
            name=f"معادلة_{word}",
            alpha=alphas,
            k=ks,
            beta=[0.1] * len(alphas)
        )

    def visualize_meaning(self, meaning: str) -> Tuple[np.ndarray, np.ndarray]:
        """تصوير المعنى كشكل"""
        params = meaning_to_parameters(meaning)

        # اختيار الشكل بناءً على المعاملات
        if params["x0"] > 0:
            # معنى إيجابي -> شكل مفتوح
            return self.drawer.draw_flower(5, params["alpha"])
        elif params["x0"] < 0:
            # معنى سلبي -> شكل مغلق
            return self.drawer.draw_spiral(3, params["alpha"] * 0.1)
        else:
            # معنى محايد -> دائرة
            return self.drawer.draw_circle(params["alpha"])

    def compare_words(self, word1: str, word2: str) -> Dict:
        """مقارنة كلمتين لغوياً ورياضياً"""
        analysis1 = self.analyze(word1)
        analysis2 = self.analyze(word2)

        # حساب التشابه
        params1 = analysis1["المعاملات"]
        params2 = analysis2["المعاملات"]

        similarity = 1.0 - abs(params1["alpha"] - params2["alpha"])
        similarity += 1.0 - abs(params1["k"] - params2["k"]) / 5.0
        similarity /= 2.0

        return {
            "الكلمة_1": word1,
            "الكلمة_2": word2,
            "التشابه": f"{similarity:.2%}",
            "معاملات_1": params1,
            "معاملات_2": params2
        }

