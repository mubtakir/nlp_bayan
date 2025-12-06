"""
🔌 Extensions Layer for Bayan Language
الطبقة الوسيطية لتوسيع لغة البيان

هذا المجلد يحتوي على الإضافات والتوسيعات للغة البيان
دون تعديل ملفات النواة المقفلة في bayan/bayan/

This folder contains extensions for the Bayan language
without modifying the locked core files in bayan/bayan/

المكونات:
- DialectAdapter: محول اللهجات العربية
- ExtendedIstinbatEngine: محرك الاستنباط الموسع
- EquationVisualizer: مُصوِّر المعادلات اللغوية
- BayanTutor: نظام تعليمي تفاعلي
- IntelligentDialogueSystem: نظام الحوار الذكي
- BayanBaserahBridge: 🌉 جسر بيان-بصيرة (ربط اللغوي بالبصري)
- VisualSemanticEngine: 🧬 محرك الدلالات البصرية (نظريات بصيرة)
- AICodeAssistant: 🤖 المساعد الذكي للبرمجة (جديد في v0.6.0)
"""

__version__ = "0.6.0"
__author__ = "باسل يحيى عبدالله"

# تصدير المكونات
from .dialect_adapter import DialectAdapter, Dialect, ConversionResult
from .extended_istinbat import ExtendedIstinbatEngine
from .equation_visualizer import EquationVisualizer, visualize
from .bayan_tutor import BayanTutor, start_tutorial, Lesson, Exercise
from .dialogue_system import IntelligentDialogueSystem, Intent, Emotion, chat

# 🌉 جسر بيان-بصيرة (جديد في v0.5.0)
from .bayan_baserah_bridge import (
    BayanBaserahBridge,
    LetterShapeType,
    LetterVisualAnalysis,
    LETTER_SHAPE_EQUATIONS,
    SHAPE_MEANING_BRIDGE,
    create_bridge
)

# 🧬 محرك الدلالات البصرية (جديد في v0.5.0)
from .visual_semantic_engine import (
    VisualSemanticEngine,
    SemanticVector
)

# 🤖 المساعد الذكي للبرمجة (جديد في v0.6.0)
from .ai_code_assistant import (
    AICodeAssistant,
    CodeSuggestion,
    CodeAnalysis,
    ErrorExplanation,
    CodeLanguage,
    SuggestionType
)

__all__ = [
    # دعم اللهجات
    'DialectAdapter',
    'Dialect',
    'ConversionResult',
    'ExtendedIstinbatEngine',
    # التصور البصري
    'EquationVisualizer',
    'visualize',
    # النظام التعليمي
    'BayanTutor',
    'start_tutorial',
    'Lesson',
    'Exercise',
    # نظام الحوار
    'IntelligentDialogueSystem',
    'Intent',
    'Emotion',
    'chat',
    # 🌉 جسر بيان-بصيرة
    'BayanBaserahBridge',
    'LetterShapeType',
    'LetterVisualAnalysis',
    'LETTER_SHAPE_EQUATIONS',
    'SHAPE_MEANING_BRIDGE',
    'create_bridge',
    # 🧬 محرك الدلالات البصرية
    'VisualSemanticEngine',
    'SemanticVector',
    # 🤖 المساعد الذكي للبرمجة
    'AICodeAssistant',
    'CodeSuggestion',
    'CodeAnalysis',
    'ErrorExplanation',
    'CodeLanguage',
    'SuggestionType',
]

