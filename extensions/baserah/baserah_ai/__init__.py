"""
نظام بصيرة للذكاء الرياضي - Baserah AI Mathematical Intelligence System
=========================================================================

نظام الذكاء الرياضي المتكامل للغة البيان.
يمثل "الفص الأيمن" من عقل البيان (الذكاء الرياضي والمعادلات المتكيفة).

المكونات الأساسية:
1. المعادلات المتكيفة (Adaptive Equations) - core/
2. نظام الخبير/المستكشف (Expert/Explorer System) - expert_explorer.py
3. الوحدة الفنية (Artistic Unit) - artistic/
4. نظام الوعي والانتباه (Consciousness & Attention)
5. طبقات التفكير المتعددة (Multi-Layer Thinking)

النظريات الثورية الثلاث:
1. ثنائية الصفر (Zero Duality)
2. تعامد الأضداد (Perpendicular Opposites)
3. نظرية الفتائل (Filament Theory)

المؤلف: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

__version__ = "1.0.0"
__author__ = "باسل يحيى عبدالله"

# المكونات الأساسية من البيان (موجودة سابقاً)
try:
    from ..mother_equation import MotherEquation, Property, State, PropertyDomain
    from ..gse import GSEModel, generalized_sigmoid, linear_component
    from ..expert_explorer import ExpertExplorer, Expert, Explorer
except ImportError:
    # في حالة الاستيراد المستقل
    MotherEquation = None
    GSEModel = None
    ExpertExplorer = None

# النواة: المعادلات المتكيفة والقيادة الثورية
from .core.adaptive_equations import (
    AdaptiveEquation,
    AdaptationType,
    AdaptationTrigger,
    AdaptationStep
)

from .core.generalized_sigmoid import (
    GeneralizedSigmoid,
    SigmoidParameters,
    ComplexExponent,
    SigmoidType
)

from .core.revolutionary_leadership import (
    RevolutionaryLeadership,
    LeadershipMode,
    TheoryResult
)

# الوحدة الفنية: الرسم والاستنباط
from .artistic.drawing_unit import DrawingUnit, ShapeParameters
from .artistic.inference_unit import InferenceUnit, InferenceResult
from .artistic.shape_generator import ShapeGenerator, ShapeType, ShapeSpec

# النظريات الثورية الثلاث
REVOLUTIONARY_THEORIES = {
    "ثنائية_الصفر": "zero_duality",
    "تعامد_الأضداد": "perpendicular_opposites",
    "نظرية_الفتائل": "filament_theory"
}

# أنواع التكيف
ADAPTATION_TYPES = {
    "صفري": "zero_duality",
    "تعامدي": "perpendicular",
    "فتائلي": "filament",
    "مركب": "combined"
}


def get_version():
    """الحصول على إصدار النظام"""
    return __version__


def get_theories():
    """الحصول على قائمة النظريات الثورية"""
    return REVOLUTIONARY_THEORIES


def create_baserah_system(name: str = "بصيرة"):
    """إنشاء نظام بصيرة متكامل"""
    return {
        "الاسم": name,
        "الإصدار": __version__,
        "المعادلات_المتكيفة": AdaptiveEquation(name),
        "القيادة_الثورية": RevolutionaryLeadership(),
        "وحدة_الرسم": DrawingUnit(),
        "وحدة_الاستنباط": InferenceUnit(),
        "مولد_الأشكال": ShapeGenerator()
    }


__all__ = [
    # الإصدار
    '__version__',
    '__author__',
    'get_version',
    'get_theories',
    'create_baserah_system',

    # المعادلات المتكيفة
    'AdaptiveEquation',
    'AdaptationType',
    'AdaptationTrigger',
    'AdaptationStep',

    # دوال سيغمويد المعممة
    'GeneralizedSigmoid',
    'SigmoidParameters',
    'ComplexExponent',
    'SigmoidType',

    # القيادة الثورية
    'RevolutionaryLeadership',
    'LeadershipMode',
    'TheoryResult',

    # الوحدة الفنية
    'DrawingUnit',
    'ShapeParameters',
    'InferenceUnit',
    'InferenceResult',
    'ShapeGenerator',
    'ShapeType',
    'ShapeSpec',

    # الثوابت
    'REVOLUTIONARY_THEORIES',
    'ADAPTATION_TYPES',
]

