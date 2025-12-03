# -*- coding: utf-8 -*-
"""
طبقة التوافقية - Compatibility Layer
=====================================

توفر واجهات متوافقة مع الملفات القديمة لتسهيل الترحيل.
هذه الطبقة تسمح للكود القديم بالعمل مع النظام الموحد الجديد.

Author: Basil Yahya Abdullah - Iraq/Mosul
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum

# استيراد من النظام الموحد
from .core import (
    ArticulationDepth, MeaningType, RelationType,
    LetterMeaning, CausalChain, OppositesPair,
    MeaningRelation, UnifiedLetterData
)
from .arabic_letters import ArabicLetterDatabase
from .english_letters import EnglishLetterDatabase
from .letter_analyzer import WordAnalyzer, LetterAnalyzer


# ============================================================
# توافقية مع letter_semantics.py القديم
# ============================================================

class LetterSemanticsDatabase:
    """
    Compatibility wrapper for old LetterSemanticsDatabase.
    Maps to the new ArabicLetterDatabase.
    """
    
    def __init__(self):
        self._db = ArabicLetterDatabase()
    
    def get_letter(self, letter: str) -> Optional[Dict]:
        """Get letter data in old format"""
        data = self._db.get_letter(letter)
        if not data:
            return None
        
        return {
            'letter': data.letter,
            'name': data.name,
            'meanings': [m.meaning for m in data.developer_meanings],
            'articulation_point': data.articulation_point,
            'meaning_type': data.meaning_type,
            'shape_meaning': data.shape_meaning,
            'sound_meaning': data.sound_meaning
        }
    
    def get_meanings(self, letter: str) -> List[str]:
        """Get letter meanings"""
        return self._db.get_meanings(letter)
    
    def get_all_letters(self) -> Dict[str, Dict]:
        """Get all letters in old format"""
        result = {}
        for letter in self._db.letters:
            result[letter] = self.get_letter(letter)
        return result


# ============================================================
# توافقية مع enhanced_letter_semantics.py القديم
# ============================================================

class EnhancedLetterSemantics:
    """
    Compatibility wrapper for old EnhancedLetterSemantics.
    Uses Camel Tools through the unified WordAnalyzer.
    """
    
    def __init__(self, db=None):
        self._analyzer = WordAnalyzer(use_camel=True)
        self._db = db or LetterSemanticsDatabase()
    
    def extract_root(self, word: str) -> Optional[str]:
        """Extract root using Camel Tools"""
        result = self._analyzer.analyze_word(word)
        if result.root_analysis:
            return result.root_analysis.root
        return None
    
    def analyze_word(self, word: str) -> Dict[str, Any]:
        """Analyze word with enhanced semantics"""
        result = self._analyzer.analyze_word(word)
        return {
            'word': word,
            'letters': [l.letter for l in result.letters],
            'meanings': result.combined_meaning,
            'root': result.root_analysis.root if result.root_analysis else None,
            'confidence': result.confidence
        }


# ============================================================
# توافقية مع advanced_letter_semantics.py القديم
# ============================================================

@dataclass
class AdvancedLetterData:
    """Compatibility class for old AdvancedLetterData"""
    letter: str
    name: str
    meanings: List[str] = field(default_factory=list)
    opposites: List[str] = field(default_factory=list)
    causal_chains: List[List[str]] = field(default_factory=list)
    articulation_point: str = ""
    meaning_type: str = ""


class AdvancedLetterDatabase:
    """
    Compatibility wrapper for old AdvancedLetterDatabase.
    """
    
    def __init__(self):
        self._db = ArabicLetterDatabase()
    
    def get_letter(self, letter: str) -> Optional[AdvancedLetterData]:
        """Get letter with advanced data"""
        data = self._db.get_letter(letter)
        if not data:
            return None

        # جمع الأضداد
        opposites = [m.opposite for m in data.developer_meanings if m.opposite]

        # جمع السلاسل السببية من العلاقات
        causal_chains = []
        for m in data.developer_meanings:
            # استخراج العلاقات السببية
            causal_targets = [
                r.target_meaning for r in m.relations
                if r.relation_type == RelationType.CAUSAL
            ]
            if causal_targets:
                causal_chains.append([m.meaning] + causal_targets)

        return AdvancedLetterData(
            letter=data.letter,
            name=data.name,
            meanings=[m.meaning for m in data.developer_meanings],
            opposites=opposites,
            causal_chains=causal_chains,
            articulation_point=data.articulation_point,
            meaning_type=data.meaning_type
        )
    
    def get_causal_chain(self, letter: str) -> List[List[str]]:
        """Get causal chains for a letter"""
        data = self.get_letter(letter)
        if data:
            return data.causal_chains
        return []
    
    def get_opposites(self, letter: str) -> List[str]:
        """Get opposites for a letter"""
        data = self.get_letter(letter)
        if data:
            return data.opposites
        return []

