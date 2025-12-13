"""
Arabic NLP Extension
معالجة اللغة العربية الطبيعية

This extension provides Arabic NLP capabilities:
- Arabic Adapter (CAMeL Tools integration)
- Arramooz Dictionary
- Advanced Arabic Parser
"""

from .arabic_adapter import ArabicNLPAdapter
from .advanced_arabic_parser import AdvancedArabicParser

__all__ = [
    'ArabicNLPAdapter',
    'AdvancedArabicParser'
]
