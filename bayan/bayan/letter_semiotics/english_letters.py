# -*- coding: utf-8 -*-
"""
قاعدة بيانات الحروف الإنجليزية الموحدة
Unified English Letters Database

يحتوي على 26 حرف إنجليزي مع معانيها الكاملة
Based on the same methodology as Arabic letters
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import json
from pathlib import Path


class EnglishLetter(Enum):
    """تعداد الحروف الإنجليزية"""
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    J = "J"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    U = "U"
    V = "V"
    W = "W"
    X = "X"
    Y = "Y"
    Z = "Z"


@dataclass
class EnglishLetterMeaning:
    """بنية معنى الحرف الإنجليزي"""
    meaning: str
    arabic_equivalent: Optional[str] = None
    examples: List[str] = field(default_factory=list)
    strength: float = 1.0


@dataclass
class EnglishLetterData:
    """بيانات الحرف الإنجليزي الكاملة"""
    letter: str
    name: str
    position: int
    sound_type: str  # نوع الصوت (vowel/consonant)
    phonetic_description: str  # وصف صوتي
    shape_description: str  # وصف الشكل
    shape_meaning: str  # معنى الشكل
    sound_meaning: str  # معنى الصوت
    psychological_meaning: str  # المعنى النفسي
    combined_meaning: str  # المعنى الجامع
    arabic_comparison: str  # المقارنة مع العربية
    developer_meanings: List[EnglishLetterMeaning] = field(default_factory=list)
    example_words: List[str] = field(default_factory=list)
    confidence: float = 0.0


class EnglishLetterDatabase:
    """قاعدة بيانات الحروف الإنجليزية الموحدة"""
    
    def __init__(self):
        self._letters: Dict[str, EnglishLetterData] = {}
        self._load_database()
    
    def _load_database(self):
        """تحميل قاعدة البيانات"""
        db_path = Path(__file__).parent / "data" / "english_letters.json"
        if db_path.exists():
            with open(db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for letter_key, letter_data in data.get('letters', {}).items():
                    self._letters[letter_key] = self._parse_letter_data(letter_data)
        else:
            self._load_default_data()
    
    def _parse_letter_data(self, data: Dict) -> EnglishLetterData:
        """تحويل البيانات من JSON إلى كائن"""
        meanings = []
        for m in data.get('developer_meanings', []):
            meanings.append(EnglishLetterMeaning(
                meaning=m.get('meaning', ''),
                arabic_equivalent=m.get('arabic_equivalent'),
                examples=m.get('examples', []),
                strength=m.get('strength', 1.0)
            ))

        return EnglishLetterData(
            letter=data.get('letter', ''),
            name=data.get('name', data.get('letter', '')),
            position=data.get('position_in_alphabet', data.get('position', 0)),
            sound_type=data.get('sound_type', ''),
            phonetic_description=data.get('sound_description', data.get('phonetic_description', '')),
            shape_description=data.get('shape_description', ''),
            shape_meaning=data.get('shape_meaning', ''),
            sound_meaning=data.get('sound_meaning', ''),
            psychological_meaning=data.get('psychic_meaning', data.get('psychological_meaning', '')),
            combined_meaning=data.get('combined_meaning', ''),
            arabic_comparison=data.get('arabic_equivalent', data.get('arabic_comparison', '')),
            developer_meanings=meanings,
            example_words=data.get('example_words', []),
            confidence=data.get('confidence', 0.0)
        )
    
    def _load_default_data(self):
        """تحميل البيانات الافتراضية"""
        pass
    
    def get_letter(self, letter: str) -> Optional[EnglishLetterData]:
        """الحصول على بيانات حرف"""
        return self._letters.get(letter.upper())
    
    @property
    def letters(self) -> Dict[str, EnglishLetterData]:
        """الحصول على جميع الحروف (خاصية)"""
        return self._letters

    def get_all_letters(self) -> Dict[str, EnglishLetterData]:
        """الحصول على جميع الحروف"""
        return self._letters
    
    def get_meanings(self, letter: str) -> List[str]:
        """الحصول على معاني حرف"""
        data = self._letters.get(letter.upper())
        if data:
            return [m.meaning for m in data.developer_meanings]
        return []

