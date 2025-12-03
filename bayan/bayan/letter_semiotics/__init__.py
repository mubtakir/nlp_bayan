# -*- coding: utf-8 -*-
"""
نظام سيميائية الحروف الموحد - Unified Letter Semiotics System
=============================================================

هذا النظام يوحد جميع ملفات سيميائية الحروف في نظام واحد متكامل.
يدعم الحروف العربية (28 حرف) والإنجليزية (26 حرف).

المبادئ الأساسية:
1. الحرف كـ "رمز بين" - يرمز لأشكال ومفاهيم متعددة
2. الحرف كـ "ضد ومعيار" - يحمل المعنى ونقيضه
3. دلالات الشكل والصوت والمخرج
4. يدمج مع Camel Tools لاستخراج الجذور والأوزان

Author: Basil Yahya Abdullah - Iraq/Mosul
Version: 2.0.0 - Unified Edition
"""

# الهياكل الأساسية
from .core import (
    # التعدادات
    ArticulationDepth,
    MeaningType,
    RelationType,
    ShapeType,
    ArticulationPlace,
    ArticulationManner,
    # هياكل البيانات
    MeaningRelation,
    CausalChain,
    OppositesPair,
    SymbolicRepresentation,
    LetterMeaning,
    PhoneticFeatures,
    ShapeFeatures,
    UnifiedLetterData
)

# قواعد البيانات
from .arabic_letters import ArabicLetterDatabase, ArabicLetter, ArabicLetterData
from .english_letters import EnglishLetterDatabase, EnglishLetter

# المحللات
from .letter_analyzer import (
    LetterAnalyzer,
    WordAnalyzer,
    LetterAnalysis,
    WordAnalysis,
    RootAnalysis
)

# السلاسل السببية
from .causal_chains import CausalChainEngine

# مولد الكلمات من المعاني
from .word_generator import (
    WordGenerator,
    GeneratedWord,
    LetterScore,
    generate_word_from_meaning,
    suggest_name_for_concept
)

# طبقة التوافقية (للكود القديم)
from .compatibility import (
    LetterSemanticsDatabase,
    EnhancedLetterSemantics,
    AdvancedLetterDatabase,
    AdvancedLetterData
)

# محرك الاستنباط الذكي
from .inference_engine import (
    MeaningInferenceEngine,
    ShapeInferenceEngine,
    SoundInferenceEngine,
    LetterNameInferenceEngine,
    InferenceMethod,
    InferredMeaning,
    ShapeAnalysis,
    SoundAnalysis,
    infer_meanings,
    analyze_word as infer_word_meaning
)

__version__ = "2.2.0"  # إضافة محرك الاستنباط
__author__ = "Basil Yahya Abdullah"

__all__ = [
    # التعدادات
    'ArticulationDepth',
    'MeaningType',
    'RelationType',
    'ShapeType',
    'ArticulationPlace',
    'ArticulationManner',
    # هياكل البيانات
    'MeaningRelation',
    'CausalChain',
    'OppositesPair',
    'SymbolicRepresentation',
    'LetterMeaning',
    'PhoneticFeatures',
    'ShapeFeatures',
    'UnifiedLetterData',
    # قواعد البيانات
    'ArabicLetterDatabase',
    'ArabicLetter',
    'ArabicLetterData',
    'EnglishLetterDatabase',
    'EnglishLetter',
    # المحللات
    'LetterAnalyzer',
    'WordAnalyzer',
    'LetterAnalysis',
    'WordAnalysis',
    'RootAnalysis',
    # السلاسل السببية
    'CausalChainEngine',
    # مولد الكلمات
    'WordGenerator',
    'GeneratedWord',
    'LetterScore',
    'generate_word_from_meaning',
    'suggest_name_for_concept',
    # طبقة التوافقية
    'LetterSemanticsDatabase',
    'EnhancedLetterSemantics',
    'AdvancedLetterDatabase',
    'AdvancedLetterData',
    # محرك الاستنباط الذكي
    'MeaningInferenceEngine',
    'ShapeInferenceEngine',
    'SoundInferenceEngine',
    'LetterNameInferenceEngine',
    'InferenceMethod',
    'InferredMeaning',
    'ShapeAnalysis',
    'SoundAnalysis',
    'infer_meanings',
    'infer_word_meaning'
]

