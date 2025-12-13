# -*- coding: utf-8 -*-
"""
محلل الحروف والكلمات الموحد
Unified Letter and Word Analyzer

يقوم بتحليل الحروف والكلمات واستنباط معانيها
يدمج مع Camel Tools لاستخراج الجذور والأوزان

المطور: باسل يحيى عبدالله - العراق/الموصل
"""

from typing import List, Dict, Optional, Tuple, Any
from dataclasses import dataclass, field
from .arabic_letters import ArabicLetterDatabase, ArabicLetterData
from .english_letters import EnglishLetterDatabase, EnglishLetterData
from .core import RelationType, MeaningType, CausalChain, MeaningRelation


@dataclass
class LetterAnalysis:
    """نتيجة تحليل حرف"""
    letter: str
    position_in_word: int
    meanings: List[str]
    opposites: List[str] = field(default_factory=list)
    articulation_point: str = ""
    meaning_type: str = ""
    contribution_to_word: str = ""
    emotional_strength: float = 0.5
    physical_strength: float = 0.5


@dataclass
class RootAnalysis:
    """نتيجة تحليل الجذر"""
    root: str
    root_letters: List[LetterAnalysis]
    root_meaning: str
    method: str = "camel_tools"  # camel_tools or heuristic


@dataclass
class WordAnalysis:
    """نتيجة تحليل كلمة"""
    word: str
    letters: List[LetterAnalysis]
    combined_meaning: str
    causal_chain: List[str]
    root_analysis: Optional[RootAnalysis] = None
    morphological_pattern: str = ""  # الوزن الصرفي
    confidence: float = 0.0
    emotional_score: float = 0.0
    physical_score: float = 0.0


class LetterAnalyzer:
    """محلل الحروف"""
    
    def __init__(self):
        self.arabic_db = ArabicLetterDatabase()
        self.english_db = EnglishLetterDatabase()
    
    def is_arabic(self, char: str) -> bool:
        """التحقق من أن الحرف عربي"""
        return '\u0600' <= char <= '\u06FF' or '\u0750' <= char <= '\u077F'
    
    def analyze_letter(self, letter: str, position: int = 0) -> Optional[LetterAnalysis]:
        """تحليل حرف واحد"""
        if self.is_arabic(letter):
            data = self.arabic_db.get_letter(letter)
            if data:
                # جمع الأضداد
                opposites = [m.opposite for m in data.developer_meanings if m.opposite]
                return LetterAnalysis(
                    letter=letter,
                    position_in_word=position,
                    meanings=[m.meaning for m in data.developer_meanings],
                    opposites=opposites,
                    articulation_point=data.articulation_point,
                    meaning_type=data.meaning_type,
                    contribution_to_word=self._get_position_contribution(position, data),
                    emotional_strength=data.emotional_strength,
                    physical_strength=data.physical_strength
                )
        else:
            data = self.english_db.get_letter(letter)
            if data:
                return LetterAnalysis(
                    letter=letter,
                    position_in_word=position,
                    meanings=[m.meaning for m in data.developer_meanings],
                    articulation_point=data.sound_type,
                    meaning_type="",
                    contribution_to_word=data.combined_meaning,
                    emotional_strength=0.5,
                    physical_strength=0.5
                )
        return None
    
    def _get_position_contribution(self, position: int, data: ArabicLetterData) -> str:
        """الحصول على مساهمة الحرف حسب موقعه"""
        if position == 0:
            return f"بداية: {data.shape_meaning}"
        elif position == -1:
            return f"نهاية: {data.philosophical_meaning}"
        else:
            return f"وسط: {data.sound_meaning}"
    
    def get_letter_meanings(self, letter: str) -> List[str]:
        """الحصول على معاني حرف"""
        if self.is_arabic(letter):
            return self.arabic_db.get_meanings(letter)
        else:
            return self.english_db.get_meanings(letter)


class WordAnalyzer:
    """محلل الكلمات الموحد - يدمج مع Camel Tools"""

    def __init__(self, use_camel: bool = True):
        self.letter_analyzer = LetterAnalyzer()
        self.arabic_adapter = None

        # محاولة تحميل Camel Tools
        if use_camel:
            try:
                from ..arabic_adapter import ArabicNLPAdapter
                self.arabic_adapter = ArabicNLPAdapter()
            except ImportError:
                pass

    def analyze_word(self, word: str) -> WordAnalysis:
        """تحليل كلمة كاملة"""
        letters = []
        all_meanings = []
        emotional_total = 0.0
        physical_total = 0.0

        for i, char in enumerate(word):
            if char.isalpha():
                position = i if i < len(word) - 1 else -1
                analysis = self.letter_analyzer.analyze_letter(char, position)
                if analysis:
                    letters.append(analysis)
                    all_meanings.extend(analysis.meanings)
                    emotional_total += analysis.emotional_strength
                    physical_total += analysis.physical_strength

        # بناء السلسلة السببية
        causal_chain = self._build_causal_chain(letters)

        # حساب المعنى المركب
        combined = self._combine_meanings(all_meanings)

        # تحليل الجذر باستخدام Camel Tools
        root_analysis = self._analyze_root(word) if self.arabic_adapter else None

        # حساب القوة النفسية والمادية
        num_letters = len(letters) if letters else 1
        emotional_score = emotional_total / num_letters
        physical_score = physical_total / num_letters

        return WordAnalysis(
            word=word,
            letters=letters,
            combined_meaning=combined,
            causal_chain=causal_chain,
            root_analysis=root_analysis,
            confidence=self._calculate_confidence(letters),
            emotional_score=emotional_score,
            physical_score=physical_score
        )

    def _analyze_root(self, word: str) -> Optional[RootAnalysis]:
        """تحليل جذر الكلمة باستخدام Camel Tools"""
        if not self.arabic_adapter:
            return None

        root = self.arabic_adapter.extract_root(word)
        if not root or root == word:
            return None

        # تحليل حروف الجذر
        root_letters = []
        root_meanings = []
        for char in root:
            analysis = self.letter_analyzer.analyze_letter(char)
            if analysis:
                root_letters.append(analysis)
                root_meanings.extend(analysis.meanings)

        return RootAnalysis(
            root=root,
            root_letters=root_letters,
            root_meaning=" + ".join(root_meanings[:3]),
            method="camel_tools"
        )

    def _build_causal_chain(self, letters: List[LetterAnalysis]) -> List[str]:
        """بناء السلسلة السببية للكلمة"""
        chain = []
        for letter in letters:
            if letter.meanings:
                chain.append(f"{letter.letter}: {letter.meanings[0]}")
        return chain

    def _combine_meanings(self, meanings: List[str]) -> str:
        """دمج المعاني في معنى واحد"""
        if not meanings:
            return ""
        unique = list(dict.fromkeys(meanings))
        return " + ".join(unique[:5])

    def _calculate_confidence(self, letters: List[LetterAnalysis]) -> float:
        """حساب مستوى الثقة في التحليل"""
        if not letters:
            return 0.0
        with_meanings = sum(1 for l in letters if l.meanings)
        return with_meanings / len(letters)

    def analyze_word_deep(self, word: str) -> Dict[str, Any]:
        """تحليل عميق للكلمة - يشمل كل التفاصيل"""
        analysis = self.analyze_word(word)

        return {
            "word": word,
            "letters_count": len(analysis.letters),
            "letters": [
                {
                    "letter": l.letter,
                    "position": l.position_in_word,
                    "meanings": l.meanings,
                    "type": l.meaning_type,
                    "emotional": l.emotional_strength,
                    "physical": l.physical_strength
                }
                for l in analysis.letters
            ],
            "root": {
                "root": analysis.root_analysis.root if analysis.root_analysis else None,
                "meaning": analysis.root_analysis.root_meaning if analysis.root_analysis else None,
                "method": analysis.root_analysis.method if analysis.root_analysis else None
            } if analysis.root_analysis else None,
            "combined_meaning": analysis.combined_meaning,
            "causal_chain": analysis.causal_chain,
            "scores": {
                "emotional": analysis.emotional_score,
                "physical": analysis.physical_score,
                "confidence": analysis.confidence
            }
        }

