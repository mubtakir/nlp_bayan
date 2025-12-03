# -*- coding: utf-8 -*-
"""
قاعدة بيانات الحروف العربية الموحدة
Unified Arabic Letters Database

يحتوي على 28 حرف عربي مع معانيها الكاملة
يستخدم الهياكل من core.py

المطور: باسل يحيى عبدالله - العراق/الموصل
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
import json
from pathlib import Path

from .core import (
    ArticulationDepth, MeaningType, RelationType,
    ArticulationPlace, ArticulationManner, ShapeType,
    LetterMeaning, MeaningRelation, CausalChain, OppositesPair,
    SymbolicRepresentation, PhoneticFeatures, ShapeFeatures,
    UnifiedLetterData
)


class ArabicLetter(Enum):
    """تعداد الحروف العربية"""
    ALIF = "ا"
    BA = "ب"
    TA = "ت"
    THA = "ث"
    JIM = "ج"
    HA = "ح"
    KHA = "خ"
    DAL = "د"
    DHAL = "ذ"
    RA = "ر"
    ZAY = "ز"
    SIN = "س"
    SHIN = "ش"
    SAD = "ص"
    DAD = "ض"
    TAA = "ط"
    ZAA = "ظ"
    AIN = "ع"
    GHAIN = "غ"
    FA = "ف"
    QAF = "ق"
    KAF = "ك"
    LAM = "ل"
    MIM = "م"
    NUN = "ن"
    HAA = "ه"
    WAW = "و"
    YA = "ي"


# للتوافق مع الكود القديم
@dataclass
class ArabicLetterData:
    """بيانات الحرف العربي الكاملة - للتوافق"""
    letter: str
    name: str
    position: int
    articulation_point: str
    articulation_depth: str
    phonetic_type: str
    emotional_strength: float
    physical_strength: float
    meaning_type: str
    shape_description: str
    shape_meaning: str
    sound_description: str
    sound_meaning: str
    developer_meanings: List[LetterMeaning] = field(default_factory=list)
    inferred_meanings: List[Dict] = field(default_factory=list)
    opposite_letter: Optional[str] = None
    similar_letters: List[str] = field(default_factory=list)
    example_words: List[str] = field(default_factory=list)
    philosophical_meaning: str = ""
    confidence: float = 0.0


class ArabicLetterDatabase:
    """قاعدة بيانات الحروف العربية الموحدة"""
    
    def __init__(self):
        self._letters: Dict[str, ArabicLetterData] = {}
        self._load_database()
    
    def _load_database(self):
        """تحميل قاعدة البيانات"""
        # سيتم تحميل البيانات من ملف JSON
        db_path = Path(__file__).parent / "data" / "arabic_letters.json"
        if db_path.exists():
            with open(db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for letter_key, letter_data in data.get('letters', {}).items():
                    self._letters[letter_key] = self._parse_letter_data(letter_data)
        else:
            # تحميل البيانات الافتراضية
            self._load_default_data()
    
    def _parse_letter_data(self, data: Dict) -> ArabicLetterData:
        """تحويل البيانات من JSON إلى كائن"""
        meanings = []
        for m in data.get('developer_meanings', []):
            letter_meaning = LetterMeaning(
                meaning=m.get('meaning', ''),
                opposite=m.get('opposite'),
                examples=m.get('examples', []),
                strength=m.get('strength', 1.0)
            )
            # إضافة العلاقات السببية
            for rel_type, targets in m.get('relations', {}).items():
                for target in (targets if isinstance(targets, list) else [targets]):
                    try:
                        rtype = RelationType(rel_type) if rel_type in [rt.value for rt in RelationType] else RelationType.CAUSAL
                        letter_meaning.add_relation(target, rtype)
                    except:
                        pass
            meanings.append(letter_meaning)
        
        return ArabicLetterData(
            letter=data.get('letter', ''),
            name=data.get('name', ''),
            position=data.get('position_in_alphabet', 0),
            articulation_point=data.get('articulation_point', ''),
            articulation_depth=data.get('articulation_depth', ''),
            phonetic_type=data.get('phonetic_type', ''),
            emotional_strength=data.get('emotional_strength', 0.5),
            physical_strength=data.get('physical_strength', 0.5),
            meaning_type=data.get('meaning_type', ''),
            shape_description=data.get('shape_general', ''),
            shape_meaning=data.get('shape_meaning', ''),
            sound_description=data.get('sound_description', ''),
            sound_meaning=data.get('sound_meaning', ''),
            developer_meanings=meanings,
            inferred_meanings=data.get('inferred_meanings', []),
            opposite_letter=data.get('opposite_letter'),
            similar_letters=data.get('similar_shape_letters', []),
            example_words=data.get('example_words', []),
            philosophical_meaning=data.get('philosophical_meaning', ''),
            confidence=data.get('confidence', 0.0)
        )
    
    def _load_default_data(self):
        """تحميل البيانات الافتراضية - سيتم استكمالها"""
        pass
    
    def get_letter(self, letter: str) -> Optional[ArabicLetterData]:
        """الحصول على بيانات حرف"""
        return self._letters.get(letter)
    
    @property
    def letters(self) -> Dict[str, ArabicLetterData]:
        """الحصول على جميع الحروف (خاصية)"""
        return self._letters

    def get_all_letters(self) -> Dict[str, ArabicLetterData]:
        """الحصول على جميع الحروف"""
        return self._letters
    
    def get_meanings(self, letter: str) -> List[str]:
        """الحصول على معاني حرف"""
        data = self._letters.get(letter)
        if data:
            return [m.meaning for m in data.developer_meanings]
        return []

