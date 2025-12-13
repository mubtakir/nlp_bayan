# -*- coding: utf-8 -*-
"""
النواة الأساسية لنظام سيميائية الحروف
Core Letter Semiotics System

هذا الملف يجمع كل العناصر الأساسية للنظام الموحد:
1. هياكل البيانات الأساسية (DataClasses)
2. التعدادات (Enums) 
3. العلاقات السببية
4. أنواع المعاني

المطور: باسل يحيى عبدالله - العراق/الموصل
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any, Set


# ==================== التعدادات ====================

class ArticulationDepth(Enum):
    """عمق المخرج - يحدد طبيعة المعنى"""
    INTERNAL = "جوفي"      # داخلي - نفسي/انفعالي
    MIDDLE = "متوسط"       # متوسط - مختلط
    EXTERNAL = "خارجي"     # خارجي - مادي/واقعي


class MeaningType(Enum):
    """نوع المعنى"""
    PSYCHOLOGICAL = "نفسي"    # نفسي/انفعالي
    PHYSICAL = "مادي"         # مادي/واقعي
    MIXED = "مختلط"           # مختلط


class RelationType(Enum):
    """نوع العلاقة بين المعاني"""
    CAUSAL = "سببي"          # يسبب
    LOGICAL = "منطقي"        # يتطلب منطقياً
    SEQUENTIAL = "تتابعي"    # يؤدي إلى تتابعياً  
    OPPOSITE = "ضد"          # نقيض


class ShapeType(Enum):
    """أنواع الأشكال"""
    CURVED = "منحني"
    STRAIGHT = "مستقيم"
    CIRCULAR = "دائري"
    ANGULAR = "زاوي"
    OPEN = "مفتوح"
    CLOSED = "مغلق"
    POINTED = "مدبب"
    ROUNDED = "مدور"


class ArticulationPlace(Enum):
    """مخرج الحرف"""
    LABIAL = "شفوي"        # ب، م، و
    DENTAL = "أسناني"      # ث، ذ، ظ
    ALVEOLAR = "لثوي"      # ت، د، ط، ض، ن، ل، ر
    PALATAL = "غاري"       # ي، ش، ج
    VELAR = "لهوي"         # ك، ق
    PHARYNGEAL = "حلقي"    # ع، غ، ح، خ
    GLOTTAL = "حنجري"      # ء، ه


class ArticulationManner(Enum):
    """طريقة النطق"""
    PLOSIVE = "انفجاري"      # ب، ت، د، ط، ض، ك، ق
    FRICATIVE = "احتكاكي"    # ف، ث، ذ، س، ز، ش، ص، ظ
    NASAL = "أنفي"           # م، ن
    LATERAL = "جانبي"        # ل
    TRILL = "تكراري"         # ر
    APPROXIMANT = "شبه صائت"  # و، ي


# ==================== هياكل البيانات الأساسية ====================

@dataclass
class MeaningRelation:
    """علاقة بين معنيين"""
    source_meaning: str
    target_meaning: str
    relation_type: RelationType
    strength: float = 1.0  # 0.0 - 1.0
    
    def __str__(self):
        return f"{self.source_meaning} --[{self.relation_type.value}]--> {self.target_meaning}"


@dataclass
class CausalChain:
    """سلسلة سببية للمعاني"""
    start_meaning: str
    chain: List[MeaningRelation] = field(default_factory=list)
    
    def add_link(self, target: str, relation_type: RelationType, strength: float = 1.0):
        """إضافة حلقة للسلسلة"""
        if self.chain:
            source = self.chain[-1].target_meaning
        else:
            source = self.start_meaning
        self.chain.append(MeaningRelation(source, target, relation_type, strength))
    
    def get_all_meanings(self) -> List[str]:
        """الحصول على جميع المعاني في السلسلة"""
        meanings = [self.start_meaning]
        for link in self.chain:
            meanings.append(link.target_meaning)
        return meanings


@dataclass  
class OppositesPair:
    """زوج من الأضداد"""
    positive: str
    negative: str
    context: str = ""
    
    def __str__(self):
        return f"{self.positive} ↔ {self.negative}"


@dataclass
class SymbolicRepresentation:
    """تمثيل رمزي للحرف"""
    symbol_type: str        # "شكل", "حركة", "حالة"
    description: str
    natural_examples: List[str] = field(default_factory=list)


@dataclass
class LetterMeaning:
    """معنى واحد من معاني الحرف"""
    meaning: str
    opposite: Optional[str] = None
    examples: List[str] = field(default_factory=list)
    strength: float = 1.0
    relations: List[MeaningRelation] = field(default_factory=list)
    
    def add_relation(self, target: str, rel_type: RelationType, strength: float = 1.0):
        """إضافة علاقة مع معنى آخر"""
        self.relations.append(MeaningRelation(self.meaning, target, rel_type, strength))


@dataclass
class PhoneticFeatures:
    """الخصائص الصوتية للحرف"""
    articulation_place: ArticulationPlace
    articulation_manner: ArticulationManner
    is_voiced: bool = True          # مجهور
    is_emphatic: bool = False       # مفخم
    is_internal: bool = False       # جوفي (نفسي) أم خارجي (مادي)
    strength: float = 0.5           # قوة الصوت
    sharpness: float = 0.5          # حدة الصوت
    softness: float = 0.5           # نعومة الصوت


@dataclass
class ShapeFeatures:
    """الخصائص الشكلية للحرف"""
    shape_types: List[ShapeType] = field(default_factory=list)
    visual_patterns: List[str] = field(default_factory=list)
    natural_resemblances: List[str] = field(default_factory=list)
    semantic_implications: List[str] = field(default_factory=list)


@dataclass
class UnifiedLetterData:
    """بيانات الحرف الموحدة الشاملة"""

    # المعلومات الأساسية
    letter: str
    name: str
    position: int  # موقعه في الأبجدية

    # المخرج والصوت
    articulation_point: str
    articulation_depth: ArticulationDepth
    meaning_type: MeaningType
    phonetic_features: Optional[PhoneticFeatures] = None

    # الشكل
    shape_features: Optional[ShapeFeatures] = None

    # القوة
    emotional_strength: float = 0.5  # قوة التعبير النفسي
    physical_strength: float = 0.5   # قوة التعبير المادي

    # المعاني
    developer_meanings: List[LetterMeaning] = field(default_factory=list)
    opposites: List[OppositesPair] = field(default_factory=list)
    causal_chains: List[CausalChain] = field(default_factory=list)
    symbolic_representations: List[SymbolicRepresentation] = field(default_factory=list)

    # العلاقات مع الحروف الأخرى
    similar_letters: List[str] = field(default_factory=list)
    opposite_letter: Optional[str] = None

    # الأمثلة
    example_words: List[str] = field(default_factory=list)

    # معلومات إضافية
    philosophical_meaning: str = ""
    confidence: float = 0.5

    def get_primary_meaning(self) -> Optional[LetterMeaning]:
        """الحصول على المعنى الأساسي"""
        if not self.developer_meanings:
            return None
        return max(self.developer_meanings, key=lambda m: m.strength)

    def get_all_meanings(self) -> List[str]:
        """الحصول على جميع المعاني كنصوص"""
        return [m.meaning for m in self.developer_meanings]

    def get_all_opposites(self) -> List[str]:
        """الحصول على جميع الأضداد"""
        opposites = []
        for m in self.developer_meanings:
            if m.opposite:
                opposites.append(m.opposite)
        for pair in self.opposites:
            opposites.append(pair.negative)
        return list(set(opposites))

    def get_causal_effects(self, meaning: str) -> List[str]:
        """الحصول على التأثيرات السببية لمعنى معين"""
        effects = []
        for chain in self.causal_chains:
            if chain.start_meaning == meaning:
                effects.extend(chain.get_all_meanings()[1:])
        return effects

