# -*- coding: utf-8 -*-
"""
مولد الكلمات من المعاني - Word Generator
==========================================

يقوم بتوليد كلمات جديدة بناءً على المعاني المطلوبة.
هذا يعطي لغة بيان ذكاءً لغوياً فريداً.

المبدأ: معنى → حروف مناسبة → كلمة جديدة

المطور: باسل يحيى عبدالله - العراق/الموصل
"""

from typing import List, Dict, Optional, Tuple, Set
from dataclasses import dataclass, field
from .arabic_letters import ArabicLetterDatabase
from .core import MeaningType


@dataclass
class GeneratedWord:
    """كلمة مولدة مع تفاصيلها"""
    word: str
    letters: List[str]
    meanings_matched: List[str]
    confidence: float
    emotional_score: float
    physical_score: float
    explanation: str


@dataclass
class LetterScore:
    """تقييم حرف لمعنى معين"""
    letter: str
    meaning_match: float  # 0.0 - 1.0
    matched_meanings: List[str]


class WordGenerator:
    """
    مولد الكلمات من المعاني
    
    يأخذ معنى أو مجموعة معاني ويولد كلمات مناسبة
    """
    
    def __init__(self):
        self.db = ArabicLetterDatabase()
        self._build_meaning_index()
    
    def _build_meaning_index(self):
        """بناء فهرس المعاني → الحروف"""
        self.meaning_to_letters: Dict[str, List[Tuple[str, float]]] = {}
        self.keyword_to_letters: Dict[str, List[str]] = {}
        
        for letter, data in self.db.letters.items():
            for meaning_obj in data.developer_meanings:
                meaning = meaning_obj.meaning
                
                # إضافة للفهرس الكامل
                if meaning not in self.meaning_to_letters:
                    self.meaning_to_letters[meaning] = []
                self.meaning_to_letters[meaning].append((letter, meaning_obj.strength))
                
                # تقسيم المعنى لكلمات مفتاحية
                keywords = self._extract_keywords(meaning)
                for keyword in keywords:
                    if keyword not in self.keyword_to_letters:
                        self.keyword_to_letters[keyword] = []
                    if letter not in self.keyword_to_letters[keyword]:
                        self.keyword_to_letters[keyword].append(letter)
    
    def _extract_keywords(self, meaning: str) -> List[str]:
        """استخراج الكلمات المفتاحية من المعنى"""
        # إزالة "و" و "ال"
        words = meaning.replace("و", " ").replace("ال", "").split()
        return [w.strip() for w in words if len(w) > 2]
    
    def find_letters_for_meaning(self, target_meaning: str, include_related: bool = True) -> List[LetterScore]:
        """البحث عن الحروف المناسبة لمعنى معين"""
        scores: Dict[str, LetterScore] = {}
        target_keywords = set(self._extract_keywords(target_meaning.lower()))
        target_words = set(target_meaning.lower().replace("ال", "").split())

        for letter, data in self.db.letters.items():
            matched_meanings = []
            total_match = 0.0

            for meaning_obj in data.developer_meanings:
                meaning = meaning_obj.meaning.lower()
                meaning_words = set(meaning.replace("ال", "").split())
                meaning_keywords = set(self._extract_keywords(meaning))

                # تطابق مباشر
                if target_meaning.lower() in meaning or meaning in target_meaning.lower():
                    total_match += 1.0
                    matched_meanings.append(meaning_obj.meaning)
                # تطابق بالجذر (كلمات تشترك بنفس الجذر)
                elif any(self._share_root(tw, mw) for tw in target_words for mw in meaning_words):
                    total_match += 0.8
                    matched_meanings.append(meaning_obj.meaning)
                # تطابق جزئي بالكلمات المفتاحية
                elif target_keywords & meaning_keywords:
                    overlap = len(target_keywords & meaning_keywords)
                    match = overlap / max(len(target_keywords), 1)
                    total_match += match * 0.7
                    matched_meanings.append(meaning_obj.meaning)
                # تطابق بكلمات المعنى
                elif target_words & meaning_words:
                    total_match += 0.5
                    matched_meanings.append(meaning_obj.meaning)
                # تطابق جزئي بالأحرف (3+ أحرف مشتركة)
                elif include_related and any(
                    len(set(tw) & set(mw)) >= 3
                    for tw in target_words for mw in meaning_words if len(tw) > 2 and len(mw) > 2
                ):
                    total_match += 0.3
                    matched_meanings.append(meaning_obj.meaning)

            if total_match > 0:
                scores[letter] = LetterScore(
                    letter=letter,
                    meaning_match=min(total_match, 1.0),
                    matched_meanings=matched_meanings
                )

        # إذا لم نجد كفاية، نضيف حروفاً ذات معاني قريبة
        if include_related and len(scores) < 5:
            for letter, data in self.db.letters.items():
                if letter not in scores and data.developer_meanings:
                    # إضافة حروف بناءً على القوة النفسية/المادية
                    scores[letter] = LetterScore(
                        letter=letter,
                        meaning_match=0.1,
                        matched_meanings=[data.developer_meanings[0].meaning]
                    )

        # ترتيب حسب التطابق
        return sorted(scores.values(), key=lambda x: x.meaning_match, reverse=True)

    def _share_root(self, word1: str, word2: str) -> bool:
        """فحص إذا كانت كلمتان تشتركان بنفس الجذر (تقريبي)"""
        if len(word1) < 2 or len(word2) < 2:
            return False
        # مقارنة الأحرف الأولى والأخيرة
        return word1[:2] == word2[:2] or word1[-2:] == word2[-2:]
    
    def generate_word(
        self,
        meanings: List[str],
        min_letters: int = 3,
        max_letters: int = 5,
        prefer_type: Optional[str] = None  # "نفسي" أو "مادي"
    ) -> List[GeneratedWord]:
        """
        توليد كلمات من قائمة معاني
        
        Args:
            meanings: قائمة المعاني المطلوبة
            min_letters: الحد الأدنى لعدد الحروف
            max_letters: الحد الأقصى لعدد الحروف
            prefer_type: تفضيل نوع المعنى (نفسي/مادي)
        
        Returns:
            قائمة الكلمات المولدة مرتبة حسب الملاءمة
        """
        # جمع الحروف المناسبة لكل معنى
        all_letter_scores: Dict[str, float] = {}
        all_matched: Dict[str, List[str]] = {}
        
        for meaning in meanings:
            letter_scores = self.find_letters_for_meaning(meaning)
            for ls in letter_scores:
                if ls.letter not in all_letter_scores:
                    all_letter_scores[ls.letter] = 0
                    all_matched[ls.letter] = []
                all_letter_scores[ls.letter] += ls.meaning_match
                all_matched[ls.letter].extend(ls.matched_meanings)
        
        # ترتيب الحروف حسب الدرجة
        sorted_letters = sorted(
            all_letter_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        # توليد الكلمات
        generated = []
        
        for length in range(min_letters, max_letters + 1):
            # أخذ أفضل الحروف
            top_letters = [l[0] for l in sorted_letters[:length + 2]]
            
            if len(top_letters) < length:
                continue
            
            # توليد تركيبات
            from itertools import permutations
            for perm in list(permutations(top_letters, length))[:10]:
                word = "".join(perm)
                letters = list(perm)
                
                # حساب الدرجات
                emotional = 0
                physical = 0
                matched = []
                
                for letter in letters:
                    data = self.db.get_letter(letter)
                    if data:
                        emotional += data.emotional_strength
                        physical += data.physical_strength
                        matched.extend(all_matched.get(letter, [])[:2])
                
                num_letters = len(letters)
                emotional /= num_letters
                physical /= num_letters
                
                # حساب الثقة
                confidence = sum(all_letter_scores.get(l, 0) for l in letters)
                confidence = min(confidence / len(meanings), 1.0)
                
                # تفضيل النوع
                if prefer_type == "نفسي" and emotional < 0.5:
                    confidence *= 0.7
                elif prefer_type == "مادي" and physical < 0.5:
                    confidence *= 0.7
                
                # بناء التفسير
                explanation = self._build_explanation(letters, matched)
                
                generated.append(GeneratedWord(
                    word=word,
                    letters=letters,
                    meanings_matched=list(set(matched))[:5],
                    confidence=confidence,
                    emotional_score=emotional,
                    physical_score=physical,
                    explanation=explanation
                ))
        
        # إزالة التكرار وترتيب
        seen = set()
        unique = []
        for g in sorted(generated, key=lambda x: x.confidence, reverse=True):
            if g.word not in seen:
                seen.add(g.word)
                unique.append(g)
        
        return unique[:10]

    def _build_explanation(self, letters: List[str], matched: List[str]) -> str:
        """بناء تفسير للكلمة المولدة"""
        parts = []
        for letter in letters:
            data = self.db.get_letter(letter)
            if data and data.developer_meanings:
                primary = data.developer_meanings[0].meaning
                parts.append(f"{letter}({primary})")

        return " + ".join(parts)

    def suggest_name(
        self,
        concept: str,
        style: str = "قوي"  # "قوي", "ناعم", "متوازن"
    ) -> List[GeneratedWord]:
        """
        اقتراح اسم لمفهوم معين

        Args:
            concept: المفهوم المراد تسميته
            style: أسلوب الاسم (قوي، ناعم، متوازن)

        Returns:
            قائمة الأسماء المقترحة
        """
        # تحليل المفهوم لمعاني
        meanings = self._concept_to_meanings(concept)

        prefer_type = None
        if style == "قوي":
            prefer_type = "مادي"
        elif style == "ناعم":
            prefer_type = "نفسي"

        return self.generate_word(meanings, prefer_type=prefer_type)

    def _concept_to_meanings(self, concept: str) -> List[str]:
        """تحويل مفهوم إلى قائمة معاني"""
        concept_map = {
            "قوة": ["القوة", "الشدة", "الصلابة"],
            "حب": ["الحب", "المودة", "الحنان"],
            "ذكاء": ["الذكر", "الفهم", "الإدراك"],
            "سرعة": ["الحركة", "السرعة", "الانطلاق"],
            "جمال": ["الجمال", "الحسن", "البهاء"],
            "علم": ["العلم", "المعرفة", "الفهم"],
            "نور": ["النور", "الإضاءة", "الظهور"],
            "حياة": ["الحياة", "الحيوية", "النشاط"],
            "أمان": ["الأمان", "السلامة", "الحماية"],
            "إبداع": ["الإبداع", "الابتكار", "الخلق"],
            "تقنية": ["التقنية", "الصناعة", "البناء"],
            "برمجة": ["البناء", "التركيب", "النظام"],
        }

        # البحث المباشر
        if concept in concept_map:
            return concept_map[concept]

        # البحث الجزئي
        for key, values in concept_map.items():
            if key in concept or concept in key:
                return values

        # تقسيم المفهوم
        return concept.split()

    def find_opposite_word(self, word: str) -> List[GeneratedWord]:
        """
        توليد كلمة معاكسة في المعنى

        Args:
            word: الكلمة الأصلية

        Returns:
            قائمة الكلمات المعاكسة المقترحة
        """
        opposite_meanings = []

        for letter in word:
            data = self.db.get_letter(letter)
            if data:
                # الحصول على الأضداد
                for meaning_obj in data.developer_meanings:
                    if meaning_obj.opposites:
                        opposite_meanings.extend(meaning_obj.opposites[:2])

        if not opposite_meanings:
            return []

        return self.generate_word(opposite_meanings[:5])


# دوال مساعدة للاستخدام المباشر

def generate_word_from_meaning(meaning: str) -> List[GeneratedWord]:
    """توليد كلمة من معنى واحد"""
    generator = WordGenerator()
    return generator.generate_word([meaning])


def suggest_name_for_concept(concept: str, style: str = "متوازن") -> List[GeneratedWord]:
    """اقتراح اسم لمفهوم"""
    generator = WordGenerator()
    return generator.suggest_name(concept, style)

