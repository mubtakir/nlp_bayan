"""
عقل بيان - Bayan Brain
========================

النظام الموحد الذي يدمج الفصين:
1. الفص المنطقي/اللغوي: سيميائية الحروف ومحركات الاستنباط
2. الفص الرياضي: نظام بصيرة والمعادلات المتكيفة

المؤلف: باسل يحيى عبدالله
"""

__version__ = "1.0.0"
__author__ = "باسل يحيى عبدالله"

from .integration import (
    BayanBrain,
    BrainHemisphere,
    ThoughtProcess,
    BrainState
)

from .linguistic_math_bridge import (
    LinguisticMathBridge,
    letter_to_equation,
    word_to_shape,
    meaning_to_parameters
)

__all__ = [
    # العقل الموحد
    'BayanBrain',
    'BrainHemisphere',
    'ThoughtProcess',
    'BrainState',
    
    # الجسر اللغوي-الرياضي
    'LinguisticMathBridge',
    'letter_to_equation',
    'word_to_shape',
    'meaning_to_parameters',
]

