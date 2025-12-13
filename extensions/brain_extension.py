"""
امتداد عقل بيان للمفسر - Bayan Brain Extension
================================================

ربط عقل بيان الموحد (الفصين معاً) بمفسر البيان.
يُحمّل جميع الدوال في البيئة العامة للمفسر.

المؤلف: باسل يحيى عبدالله
"""

from typing import Dict, Any, List

# استيراد عقل بيان الموحد
from .bayan_brain import (
    BayanBrain,
    BrainHemisphere,
    LinguisticMathBridge,
    letter_to_equation,
    word_to_shape,
    meaning_to_parameters
)

# استيراد امتدادات الفصين
try:
    from .baserah_extension import inject_baserah_functions
except ImportError:
    def inject_baserah_functions(env):
        return []


# إنشاء عقل بيان العام
_global_brain = None


def get_brain() -> BayanBrain:
    """الحصول على عقل بيان العام"""
    global _global_brain
    if _global_brain is None:
        _global_brain = BayanBrain("عقل_بيان_الرئيسي")
    return _global_brain


def inject_brain_functions(global_env: Dict[str, Any]) -> List[str]:
    """
    حقن دوال عقل بيان الموحد في البيئة العامة للمفسر
    """
    
    brain = get_brain()
    bridge = LinguisticMathBridge()
    
    # ═══════════════════════════════════════════════════════════════
    # 1. دوال عقل بيان الموحد
    # ═══════════════════════════════════════════════════════════════
    
    def فكّر_في(مدخل, استخدم_الفصين: bool = True):
        """التفكير في مدخل باستخدام عقل بيان"""
        process = brain.think(مدخل, استخدم_الفصين)
        return {
            "المدخل": str(مدخل),
            "الفص_النشط": process.hemisphere.value,
            "النتيجة_اللغوية": process.logical_result,
            "النتيجة_الرياضية": process.mathematical_result,
            "النتيجة_المتكاملة": process.integrated_result,
            "الثقة": process.confidence,
            "الرؤى": process.insights
        }
    
    def حلّل_بعمق(كلمة: str):
        """تحليل عميق لكلمة باستخدام الفصين"""
        return brain.analyze_word_deeply(كلمة)
    
    def ولّد_كلمة(معنى: str):
        """توليد كلمة من معنى"""
        return brain.generate_word(معنى)
    
    def بدّل_الفص(فص: str = "منطقي"):
        """تبديل الفص النشط"""
        if فص == "منطقي":
            brain.switch_hemisphere(BrainHemisphere.LOGICAL)
        else:
            brain.switch_hemisphere(BrainHemisphere.MATHEMATICAL)
        return f"تم التبديل إلى الفص ال{فص}"
    
    def حالة_العقل():
        """الحصول على حالة العقل"""
        return brain.get_status()
    
    # ═══════════════════════════════════════════════════════════════
    # 2. دوال الجسر اللغوي-الرياضي
    # ═══════════════════════════════════════════════════════════════
    
    def حرف_إلى_معادلة(حرف: str):
        """تحويل حرف إلى معادلة رياضية"""
        eq = letter_to_equation(حرف)
        if eq:
            return {
                "الحرف": eq.letter,
                "alpha": eq.alpha,
                "k": eq.k,
                "x0": eq.x0,
                "المعاني": eq.meanings
            }
        return None
    
    def كلمة_إلى_شكل(كلمة: str, مقياس: float = 1.0):
        """تحويل كلمة إلى شكل هندسي"""
        x, y = word_to_shape(كلمة, مقياس)
        return {"x": x.tolist()[:30], "y": y.tolist()[:30], "عدد_النقاط": len(x)}
    
    def معنى_إلى_معاملات(معنى: str):
        """تحويل معنى إلى معاملات رياضية"""
        return meaning_to_parameters(معنى)
    
    def حلّل_لغوياً_ورياضياً(نص: str):
        """تحليل نص لغوياً ورياضياً"""
        return bridge.analyze(نص)
    
    def قارن_كلمتين(كلمة1: str, كلمة2: str):
        """مقارنة كلمتين لغوياً ورياضياً"""
        return bridge.compare_words(كلمة1, كلمة2)
    
    def أنشئ_معادلة_من_كلمة(كلمة: str):
        """إنشاء معادلة متكيفة من كلمة"""
        eq = bridge.create_equation_from_word(كلمة)
        return {
            "الاسم": eq.name,
            "alpha": eq.alpha,
            "k": eq.k,
            "beta": eq.beta
        }
    
    # ═══════════════════════════════════════════════════════════════
    # حقن الدوال
    # ═══════════════════════════════════════════════════════════════
    
    brain_functions = {
        # عقل بيان الموحد
        "فكّر_في": فكّر_في,
        "حلّل_بعمق": حلّل_بعمق,
        "ولّد_كلمة": ولّد_كلمة,
        "بدّل_الفص": بدّل_الفص,
        "حالة_العقل": حالة_العقل,
        
        # الجسر اللغوي-الرياضي
        "حرف_إلى_معادلة": حرف_إلى_معادلة,
        "كلمة_إلى_شكل": كلمة_إلى_شكل,
        "معنى_إلى_معاملات": معنى_إلى_معاملات,
        "حلّل_لغوياً_ورياضياً": حلّل_لغوياً_ورياضياً,
        "قارن_كلمتين": قارن_كلمتين,
        "أنشئ_معادلة_من_كلمة": أنشئ_معادلة_من_كلمة,
        
        # الكائنات
        "عقل_بيان": brain,
        "الجسر_اللغوي_الرياضي": bridge,
    }
    
    global_env.update(brain_functions)
    return list(brain_functions.keys())


def inject_all_bayan_functions(global_env: Dict[str, Any]) -> Dict[str, List[str]]:
    """
    حقن جميع دوال بيان في البيئة العامة

    يجمع بين:
    - دوال بصيرة (الفص الرياضي)
    - دوال عقل بيان الموحد (الدمج)
    """
    result = {}

    # حقن دوال بصيرة
    try:
        baserah_funcs = inject_baserah_functions(global_env)
        result["بصيرة"] = baserah_funcs
    except Exception as e:
        result["بصيرة"] = f"خطأ: {e}"

    # حقن دوال عقل بيان الموحد
    try:
        brain_funcs = inject_brain_functions(global_env)
        result["عقل_بيان"] = brain_funcs
    except Exception as e:
        result["عقل_بيان"] = f"خطأ: {e}"

    return result


# قائمة جميع الدوال
ALL_BRAIN_FUNCTIONS = [
    # عقل بيان
    "فكّر_في", "حلّل_بعمق", "ولّد_كلمة", "بدّل_الفص", "حالة_العقل",
    # الجسر
    "حرف_إلى_معادلة", "كلمة_إلى_شكل", "معنى_إلى_معاملات",
    "حلّل_لغوياً_ورياضياً", "قارن_كلمتين", "أنشئ_معادلة_من_كلمة"
]

