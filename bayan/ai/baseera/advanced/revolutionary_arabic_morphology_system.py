#!/usr/bin/env python3
"""
نظام الصرف العربي الثوري - Revolutionary Arabic Morphology System
يعتمد على النظريات الثلاث الثورية لنظام بصيرة

🔤 تحليل صرفي متقدم بدون مكتبات NLP تقليدية
🧬 يستخدم النظريات الثلاث لاستخراج الجذور والأوزان
⚡ شفافية كاملة في عملية التحليل الصرفي

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import numpy as np
import json
import math
import re
from typing import Dict, List, Tuple, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
import uuid
from datetime import datetime

class WordType(Enum):
    """أنواع الكلمات"""
    NOUN = "اسم"
    VERB = "فعل"
    ADJECTIVE = "صفة"
    ADVERB = "ظرف"
    PREPOSITION = "حرف_جر"
    CONJUNCTION = "حرف_عطف"
    PARTICLE = "حرف"
    PRONOUN = "ضمير"
    UNKNOWN = "غير_محدد"

class RootType(Enum):
    """أنواع الجذور"""
    TRILATERAL = "ثلاثي"      # جذر ثلاثي
    QUADRILATERAL = "رباعي"   # جذر رباعي
    QUINQUELATERAL = "خماسي"  # جذر خماسي
    COMPOUND = "مركب"         # كلمة مركبة

class PatternType(Enum):
    """أنواع الأوزان الصرفية"""
    FAAL = "فعل"           # الوزن الأساسي
    FAAIL = "فعيل"         # صفة أو اسم
    FAAEL = "فاعل"         # اسم فاعل
    MAFOOL = "مفعول"       # اسم مفعول
    FAEELA = "فاعلة"       # مؤنث فاعل
    IFAAL = "إفعال"        # مصدر
    TAFEEL = "تفعيل"       # مصدر
    ISTIFAAL = "استفعال"   # مصدر
    MUFAAEL = "مفاعل"      # صيغة مبالغة
    UNKNOWN = "غير_محدد"

@dataclass
class MorphologicalFeatures:
    """الخصائص الصرفية"""
    gender: str = "غير_محدد"        # مذكر/مؤنث
    number: str = "غير_محدد"        # مفرد/مثنى/جمع
    case: str = "غير_محدد"          # رفع/نصب/جر
    definiteness: str = "غير_محدد"   # معرفة/نكرة
    tense: str = "غير_محدد"         # ماضي/مضارع/أمر
    voice: str = "غير_محدد"         # مبني للمعلوم/مجهول
    mood: str = "غير_محدد"          # مرفوع/منصوب/مجزوم

@dataclass
class RootAnalysis:
    """تحليل الجذر"""
    root_id: str
    root_letters: str
    root_type: RootType
    meaning_core: str
    semantic_field: str
    strength: float = 0.0
    confidence: float = 0.0
    related_roots: List[str] = field(default_factory=list)

@dataclass
class PatternAnalysis:
    """تحليل الوزن الصرفي"""
    pattern_id: str
    pattern_name: str
    pattern_type: PatternType
    template: str
    morphological_function: str
    semantic_role: str
    confidence: float = 0.0

@dataclass
class MorphologicalAnalysis:
    """التحليل الصرفي الكامل"""
    analysis_id: str
    original_word: str
    normalized_word: str
    root_analysis: RootAnalysis
    pattern_analysis: PatternAnalysis
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    infix: Optional[str] = None
    word_type: WordType = WordType.UNKNOWN
    morphological_features: MorphologicalFeatures = field(default_factory=MorphologicalFeatures)
    semantic_weight: float = 0.0
    confidence_score: float = 0.0
    alternative_analyses: List['MorphologicalAnalysis'] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)

class RevolutionaryArabicMorphologySystem:
    """نظام الصرف العربي الثوري"""
    
    def __init__(self, name: str = "RevolutionaryMorphologySystem"):
        self.name = name
        
        # المعاملات التكيفية للنظريات الثلاث
        self.zero_duality_params = {
            'alpha': [1.2, 0.9, 1.1],   # معاملات ثنائية الصفر
            'beta': [0.15, 0.12, 0.18], # عوامل التوازن
            'gamma': [2.8, 3.2, 2.5]    # عوامل التضخيم
        }
        
        self.perpendicularity_params = {
            'theta': [0.8, 1.2, 0.6],   # زوايا التعامد
            'phi': [1.4, 1.1, 1.6],     # معاملات التوازن
            'delta': [0.3, 0.25, 0.35]  # عوامل التصحيح
        }
        
        self.filament_params = {
            'lambda': [4.5, 5.0, 4.0],  # معاملات الفتائل
            'mu': [0.75, 0.8, 0.7],     # عوامل التشابك
            'sigma': [2.2, 2.5, 2.0]    # انحرافات التوزيع
        }
        
        # قواعد البيانات الصرفية
        self.root_database = self._initialize_root_database()
        self.pattern_database = self._initialize_pattern_database()
        self.prefix_database = self._initialize_prefix_database()
        self.suffix_database = self._initialize_suffix_database()
        
        # ذاكرة التحليل
        self.analysis_cache: Dict[str, MorphologicalAnalysis] = {}
        self.root_cache: Dict[str, RootAnalysis] = {}
        
        # إحصائيات النظام
        self.stats = {
            'total_analyses': 0,
            'successful_root_extractions': 0,
            'successful_pattern_identifications': 0,
            'average_confidence': 0.0,
            'processing_time': 0.0
        }
        
        print(f"🔤⚡ تم إنشاء نظام الصرف العربي الثوري: {name}")
        print(f"   🧬 النظريات الثلاث: نشطة")
        print(f"   📊 قواعد البيانات الصرفية: جاهزة")
        print(f"   🔍 محلل الجذور والأوزان: نشط")
    
    def analyze_word(self, word: str, context: str = None) -> MorphologicalAnalysis:
        """تحليل كلمة عربية صرفياً"""
        start_time = datetime.now()
        
        # تنظيف الكلمة
        normalized_word = self._normalize_word(word)
        
        # البحث في الذاكرة المؤقتة
        cache_key = f"{normalized_word}_{context or 'default'}"
        if cache_key in self.analysis_cache:
            return self.analysis_cache[cache_key]
        
        # تحليل الجذر باستخدام النظريات الثلاث
        root_analysis = self._extract_root_revolutionary(normalized_word)
        
        # تحليل الوزن الصرفي
        pattern_analysis = self._identify_pattern_revolutionary(normalized_word, root_analysis)
        
        # استخراج البادئات واللواحق
        prefix = self._extract_prefix(normalized_word)
        suffix = self._extract_suffix(normalized_word)
        infix = self._extract_infix(normalized_word)
        
        # تحديد نوع الكلمة
        word_type = self._classify_word_type(normalized_word, pattern_analysis)
        
        # تحليل الخصائص الصرفية
        morphological_features = self._analyze_morphological_features(
            normalized_word, word_type, pattern_analysis
        )
        
        # حساب الوزن الدلالي
        semantic_weight = self._calculate_semantic_weight(
            normalized_word, root_analysis, pattern_analysis
        )
        
        # حساب مستوى الثقة
        confidence_score = self._calculate_confidence_score(
            root_analysis, pattern_analysis, word_type
        )
        
        # إنشاء التحليل الكامل
        analysis = MorphologicalAnalysis(
            analysis_id=str(uuid.uuid4()),
            original_word=word,
            normalized_word=normalized_word,
            root_analysis=root_analysis,
            pattern_analysis=pattern_analysis,
            prefix=prefix,
            suffix=suffix,
            infix=infix,
            word_type=word_type,
            morphological_features=morphological_features,
            semantic_weight=semantic_weight,
            confidence_score=confidence_score
        )
        
        # حفظ في الذاكرة المؤقتة
        self.analysis_cache[cache_key] = analysis
        
        # تحديث الإحصائيات
        processing_time = (datetime.now() - start_time).total_seconds()
        self._update_stats(analysis, processing_time)
        
        return analysis
    
    def _extract_root_revolutionary(self, word: str) -> RootAnalysis:
        """استخراج الجذر باستخدام النظريات الثورية"""
        # 1. نظرية ثنائية الصفر - تحليل التوازن في الحروف
        zero_duality_analysis = self._apply_zero_duality_root_extraction(word)
        
        # 2. نظرية تعامد الأضداد - كشف الحروف الأساسية
        perpendicularity_analysis = self._apply_perpendicularity_root_extraction(word)
        
        # 3. نظرية الفتائل - تحليل الأنماط الصرفية
        filament_analysis = self._apply_filament_root_extraction(word)
        
        # دمج النتائج
        root_letters = self._merge_root_analyses(
            zero_duality_analysis, perpendicularity_analysis, filament_analysis
        )
        
        # تحديد نوع الجذر
        root_type = self._determine_root_type(root_letters)
        
        # استخراج المعنى الأساسي
        meaning_core = self._extract_meaning_core(root_letters)
        
        # تحديد الحقل الدلالي
        semantic_field = self._determine_semantic_field(root_letters, meaning_core)
        
        # حساب قوة الجذر
        strength = self._calculate_root_strength(root_letters, word)
        
        # حساب مستوى الثقة
        confidence = self._calculate_root_confidence(
            zero_duality_analysis, perpendicularity_analysis, filament_analysis
        )
        
        # البحث عن الجذور المرتبطة
        related_roots = self._find_related_roots(root_letters)
        
        return RootAnalysis(
            root_id=str(uuid.uuid4()),
            root_letters=root_letters,
            root_type=root_type,
            meaning_core=meaning_core,
            semantic_field=semantic_field,
            strength=strength,
            confidence=confidence,
            related_roots=related_roots
        )
    
    def _apply_zero_duality_root_extraction(self, word: str) -> Dict[str, Any]:
        """تطبيق نظرية ثنائية الصفر لاستخراج الجذر"""
        # تحليل توازن الحروف في الكلمة
        char_weights = {}
        
        for i, char in enumerate(word):
            # تطبيق معادلة ثنائية الصفر
            alpha = self.zero_duality_params['alpha'][0]
            beta = self.zero_duality_params['beta'][0]
            gamma = self.zero_duality_params['gamma'][0]
            
            # حساب الموقع النسبي
            position_ratio = i / max(1, len(word) - 1)
            
            # معادلة السيغمويد المعدلة
            char_value = ord(char) / 1000.0
            transformed_value = alpha * (1 / (1 + math.exp(-gamma * (char_value - 0.5)))) + beta
            
            # تطبيق التوازن الموضعي
            positional_weight = math.sin(position_ratio * math.pi) * transformed_value
            
            char_weights[char] = positional_weight
        
        # استخراج الحروف الأساسية (الأعلى وزناً)
        sorted_chars = sorted(char_weights.items(), key=lambda x: x[1], reverse=True)
        root_candidates = [char for char, weight in sorted_chars[:4]]  # أفضل 4 حروف
        
        return {
            'method': 'zero_duality',
            'char_weights': char_weights,
            'root_candidates': root_candidates,
            'confidence': min(1.0, sum(weight for _, weight in sorted_chars[:3]) / 3.0)
        }
    
    def _apply_perpendicularity_root_extraction(self, word: str) -> Dict[str, Any]:
        """تطبيق نظرية تعامد الأضداد لاستخراج الجذر"""
        # تحليل التناقضات والتعامدات في الحروف
        char_positions = {}
        
        for i, char in enumerate(word):
            char_positions[char] = i
        
        # تطبيق معادلة التعامد
        theta = self.perpendicularity_params['theta'][0]
        phi = self.perpendicularity_params['phi'][0]
        
        orthogonal_weights = {}
        
        for char, pos in char_positions.items():
            # حساب التعامد مع الموضع
            orthogonal_factor = phi * math.sin(theta * math.pi * pos / len(word))
            
            # حساب التعامد مع الحروف الأخرى
            char_value = ord(char)
            orthogonal_sum = 0
            
            for other_char, other_pos in char_positions.items():
                if char != other_char:
                    other_value = ord(other_char)
                    angle_diff = abs(char_value - other_value) / 100.0
                    orthogonal_sum += math.cos(angle_diff * math.pi / 2)
            
            orthogonal_weights[char] = orthogonal_factor * (1 + orthogonal_sum / len(char_positions))
        
        # استخراج الحروف المتعامدة (الأساسية)
        sorted_chars = sorted(orthogonal_weights.items(), key=lambda x: x[1], reverse=True)
        root_candidates = [char for char, weight in sorted_chars[:3]]  # أفضل 3 حروف
        
        return {
            'method': 'perpendicularity',
            'orthogonal_weights': orthogonal_weights,
            'root_candidates': root_candidates,
            'confidence': min(1.0, sum(weight for _, weight in sorted_chars[:3]) / 3.0)
        }
    
    def _apply_filament_root_extraction(self, word: str) -> Dict[str, Any]:
        """تطبيق نظرية الفتائل لاستخراج الجذر"""
        # تحليل الأنماط والتشابكات في الكلمة
        lambda_param = self.filament_params['lambda'][0]
        mu = self.filament_params['mu'][0]
        sigma = self.filament_params['sigma'][0]
        
        # تحليل الأنماط الصرفية المعروفة
        pattern_matches = {}
        
        for pattern_name, pattern_info in self.pattern_database.items():
            similarity = self._calculate_pattern_similarity(word, pattern_info['template'])
            
            if similarity > 0.3:  # عتبة التشابه
                # تطبيق معادلة الفتائل
                filament_strength = lambda_param * math.exp(-((similarity - mu) ** 2) / (2 * sigma ** 2))
                pattern_matches[pattern_name] = {
                    'similarity': similarity,
                    'filament_strength': filament_strength,
                    'expected_root_length': pattern_info.get('root_length', 3)
                }
        
        # استخراج الجذر بناء على أقوى نمط
        if pattern_matches:
            best_pattern = max(pattern_matches.items(), key=lambda x: x[1]['filament_strength'])
            pattern_name, pattern_data = best_pattern
            
            # استخراج الجذر بناء على النمط
            root_candidates = self._extract_root_from_pattern(word, pattern_name, pattern_data)
        else:
            # استخراج افتراضي
            root_candidates = list(word[:3])  # أول 3 حروف
        
        return {
            'method': 'filament',
            'pattern_matches': pattern_matches,
            'root_candidates': root_candidates,
            'confidence': max([data['filament_strength'] for data in pattern_matches.values()]) if pattern_matches else 0.3
        }
    
    def _merge_root_analyses(self, zero_duality: Dict, perpendicularity: Dict, filament: Dict) -> str:
        """دمج نتائج التحليلات الثلاث لاستخراج الجذر النهائي"""
        # جمع جميع المرشحين
        all_candidates = []
        all_candidates.extend(zero_duality['root_candidates'])
        all_candidates.extend(perpendicularity['root_candidates'])
        all_candidates.extend(filament['root_candidates'])
        
        # حساب تكرار كل حرف
        char_frequency = {}
        for char in all_candidates:
            char_frequency[char] = char_frequency.get(char, 0) + 1
        
        # ترجيح بناء على الثقة
        weighted_scores = {}
        for char in char_frequency:
            score = 0
            
            # وزن من ثنائية الصفر
            if char in zero_duality['root_candidates']:
                score += zero_duality['confidence'] * 0.35
            
            # وزن من التعامد
            if char in perpendicularity['root_candidates']:
                score += perpendicularity['confidence'] * 0.30
            
            # وزن من الفتائل
            if char in filament['root_candidates']:
                score += filament['confidence'] * 0.35
            
            weighted_scores[char] = score * char_frequency[char]
        
        # اختيار أفضل 3 حروف للجذر
        sorted_chars = sorted(weighted_scores.items(), key=lambda x: x[1], reverse=True)
        root_letters = ''.join([char for char, score in sorted_chars[:3]])
        
        return root_letters
    
    def _initialize_root_database(self) -> Dict[str, Dict[str, Any]]:
        """تهيئة قاعدة بيانات الجذور"""
        return {
            'كتب': {
                'meaning': 'الكتابة والتدوين',
                'semantic_field': 'علم وتعليم',
                'type': RootType.TRILATERAL,
                'strength': 0.9
            },
            'قرأ': {
                'meaning': 'القراءة والتلاوة',
                'semantic_field': 'علم وتعليم',
                'type': RootType.TRILATERAL,
                'strength': 0.95
            },
            'علم': {
                'meaning': 'المعرفة والإدراك',
                'semantic_field': 'علم ومعرفة',
                'type': RootType.TRILATERAL,
                'strength': 0.98
            },
            'حمد': {
                'meaning': 'الشكر والثناء',
                'semantic_field': 'عبادة وروحانية',
                'type': RootType.TRILATERAL,
                'strength': 0.92
            },
            'سلم': {
                'meaning': 'السلامة والأمان',
                'semantic_field': 'سلام وأمان',
                'type': RootType.TRILATERAL,
                'strength': 0.88
            }
        }
    
    def _initialize_pattern_database(self) -> Dict[str, Dict[str, Any]]:
        """تهيئة قاعدة بيانات الأوزان الصرفية"""
        return {
            'فعل': {
                'template': 'فعل',
                'type': PatternType.FAAL,
                'function': 'فعل ماضي',
                'root_length': 3,
                'semantic_role': 'حدث أو فعل'
            },
            'فاعل': {
                'template': 'فاعل',
                'type': PatternType.FAAEL,
                'function': 'اسم فاعل',
                'root_length': 3,
                'semantic_role': 'من يقوم بالفعل'
            },
            'مفعول': {
                'template': 'مفعول',
                'type': PatternType.MAFOOL,
                'function': 'اسم مفعول',
                'root_length': 3,
                'semantic_role': 'من يقع عليه الفعل'
            },
            'فعيل': {
                'template': 'فعيل',
                'type': PatternType.FAAIL,
                'function': 'صفة مشبهة',
                'root_length': 3,
                'semantic_role': 'صفة ثابتة'
            }
        }
    
    def _initialize_prefix_database(self) -> Dict[str, Dict[str, Any]]:
        """تهيئة قاعدة بيانات البادئات"""
        return {
            'ال': {'type': 'تعريف', 'function': 'أداة تعريف'},
            'و': {'type': 'عطف', 'function': 'حرف عطف'},
            'ف': {'type': 'عطف', 'function': 'حرف عطف'},
            'ب': {'type': 'جر', 'function': 'حرف جر'},
            'ك': {'type': 'جر', 'function': 'حرف جر'},
            'ل': {'type': 'جر', 'function': 'حرف جر'},
            'من': {'type': 'جر', 'function': 'حرف جر'},
            'إلى': {'type': 'جر', 'function': 'حرف جر'},
            'على': {'type': 'جر', 'function': 'حرف جر'},
            'في': {'type': 'جر', 'function': 'حرف جر'}
        }
    
    def _initialize_suffix_database(self) -> Dict[str, Dict[str, Any]]:
        """تهيئة قاعدة بيانات اللواحق"""
        return {
            'ة': {'type': 'تأنيث', 'function': 'علامة التأنيث'},
            'ان': {'type': 'تثنية', 'function': 'علامة التثنية'},
            'ين': {'type': 'جمع', 'function': 'جمع مذكر سالم'},
            'ون': {'type': 'جمع', 'function': 'جمع مذكر سالم'},
            'ات': {'type': 'جمع', 'function': 'جمع مؤنث سالم'},
            'ها': {'type': 'ضمير', 'function': 'ضمير متصل'},
            'هم': {'type': 'ضمير', 'function': 'ضمير متصل'},
            'هن': {'type': 'ضمير', 'function': 'ضمير متصل'},
            'كم': {'type': 'ضمير', 'function': 'ضمير متصل'},
            'كن': {'type': 'ضمير', 'function': 'ضمير متصل'}
        }
    
    def _normalize_word(self, word: str) -> str:
        """تطبيع الكلمة"""
        # إزالة التشكيل والرموز غير المرغوبة
        normalized = re.sub(r'[ًٌٍَُِّْ]', '', word)
        
        # توحيد الألف
        normalized = re.sub(r'[أإآ]', 'ا', normalized)
        
        # توحيد التاء
        normalized = re.sub(r'ة', 'ه', normalized)
        
        return normalized.strip()
    
    def _extract_prefix(self, word: str) -> Optional[str]:
        """استخراج البادئة"""
        for prefix in sorted(self.prefix_database.keys(), key=len, reverse=True):
            if word.startswith(prefix):
                return prefix
        return None
    
    def _extract_suffix(self, word: str) -> Optional[str]:
        """استخراج اللاحقة"""
        for suffix in sorted(self.suffix_database.keys(), key=len, reverse=True):
            if word.endswith(suffix):
                return suffix
        return None
    
    def _extract_infix(self, word: str) -> Optional[str]:
        """استخراج الحشو (إن وجد)"""
        # تنفيذ مبسط - يمكن تطويره
        if 'ت' in word[1:-1]:  # تاء في الوسط
            return 'ت'
        return None

    def _determine_root_type(self, root_letters: str) -> RootType:
        """تحديد نوع الجذر"""
        length = len(root_letters)
        if length == 3:
            return RootType.TRILATERAL
        elif length == 4:
            return RootType.QUADRILATERAL
        elif length == 5:
            return RootType.QUINQUELATERAL
        else:
            return RootType.COMPOUND

    def _extract_meaning_core(self, root_letters: str) -> str:
        """استخراج المعنى الأساسي للجذر"""
        if root_letters in self.root_database:
            return self.root_database[root_letters]['meaning']
        else:
            # تحليل تقديري بناء على الحروف
            return f"معنى مشتق من الجذر {root_letters}"

    def _determine_semantic_field(self, root_letters: str, meaning_core: str) -> str:
        """تحديد الحقل الدلالي"""
        if root_letters in self.root_database:
            return self.root_database[root_letters]['semantic_field']

        # تصنيف تلقائي بناء على المعنى
        if any(word in meaning_core for word in ['علم', 'معرفة', 'تعليم']):
            return 'علم ومعرفة'
        elif any(word in meaning_core for word in ['عبادة', 'دين', 'روح']):
            return 'عبادة وروحانية'
        elif any(word in meaning_core for word in ['سلام', 'أمان', 'حب']):
            return 'سلام وأمان'
        else:
            return 'عام'

    def _calculate_root_strength(self, root_letters: str, original_word: str) -> float:
        """حساب قوة الجذر"""
        # قوة أساسية بناء على طول الجذر
        base_strength = 0.7 if len(root_letters) == 3 else 0.6

        # تعديل بناء على وجود الجذر في قاعدة البيانات
        if root_letters in self.root_database:
            base_strength += 0.2

        # تعديل بناء على نسبة الجذر في الكلمة الأصلية
        root_ratio = len(root_letters) / len(original_word)
        strength_modifier = min(root_ratio * 1.5, 1.0)

        return min(base_strength * strength_modifier, 1.0)

    def _calculate_root_confidence(self, zero_duality: Dict, perpendicularity: Dict, filament: Dict) -> float:
        """حساب مستوى الثقة في استخراج الجذر"""
        # متوسط الثقة من النظريات الثلاث
        confidence_sum = (
            zero_duality['confidence'] * 0.35 +
            perpendicularity['confidence'] * 0.30 +
            filament['confidence'] * 0.35
        )

        return min(confidence_sum, 1.0)

    def _find_related_roots(self, root_letters: str) -> List[str]:
        """البحث عن الجذور المرتبطة"""
        related = []

        for root in self.root_database.keys():
            if root != root_letters:
                # حساب التشابه بين الجذور
                similarity = self._calculate_root_similarity(root_letters, root)
                if similarity > 0.6:  # عتبة التشابه
                    related.append(root)

        return related[:5]  # أفضل 5 جذور مرتبطة

    def _calculate_root_similarity(self, root1: str, root2: str) -> float:
        """حساب التشابه بين جذرين"""
        if len(root1) != len(root2):
            return 0.0

        common_chars = sum(1 for c1, c2 in zip(root1, root2) if c1 == c2)
        return common_chars / len(root1)

    def _identify_pattern_revolutionary(self, word: str, root_analysis: RootAnalysis) -> PatternAnalysis:
        """تحديد الوزن الصرفي باستخدام النظريات الثورية"""
        best_pattern = None
        best_confidence = 0.0

        for pattern_name, pattern_info in self.pattern_database.items():
            # حساب التطابق مع النمط
            similarity = self._calculate_pattern_similarity(word, pattern_info['template'])

            # تطبيق النظريات الثلاث لتحسين التحديد
            enhanced_confidence = self._enhance_pattern_confidence(
                word, pattern_name, similarity, root_analysis
            )

            if enhanced_confidence > best_confidence:
                best_confidence = enhanced_confidence
                best_pattern = pattern_name

        if best_pattern:
            pattern_info = self.pattern_database[best_pattern]
            return PatternAnalysis(
                pattern_id=str(uuid.uuid4()),
                pattern_name=best_pattern,
                pattern_type=pattern_info['type'],
                template=pattern_info['template'],
                morphological_function=pattern_info['function'],
                semantic_role=pattern_info['semantic_role'],
                confidence=best_confidence
            )
        else:
            # نمط افتراضي
            return PatternAnalysis(
                pattern_id=str(uuid.uuid4()),
                pattern_name="غير_محدد",
                pattern_type=PatternType.UNKNOWN,
                template="غير_محدد",
                morphological_function="غير_محدد",
                semantic_role="غير_محدد",
                confidence=0.3
            )

    def _calculate_pattern_similarity(self, word: str, template: str) -> float:
        """حساب التشابه مع النمط الصرفي"""
        if len(word) != len(template):
            return 0.0

        # مقارنة بسيطة - يمكن تطويرها
        matches = 0
        for i, (w_char, t_char) in enumerate(zip(word, template)):
            if t_char == 'ف' or t_char == 'ع' or t_char == 'ل':
                # هذه مواضع الجذر
                matches += 0.5  # وزن أقل للجذر
            elif w_char == t_char:
                matches += 1.0  # تطابق كامل

        return matches / len(template)

    def _enhance_pattern_confidence(self, word: str, pattern_name: str, base_similarity: float, root_analysis: RootAnalysis) -> float:
        """تحسين ثقة النمط باستخدام النظريات الثورية"""
        # 1. تطبيق ثنائية الصفر
        zero_duality_factor = self._apply_zero_duality_pattern_analysis(word, pattern_name)

        # 2. تطبيق التعامد
        perpendicularity_factor = self._apply_perpendicularity_pattern_analysis(word, pattern_name)

        # 3. تطبيق الفتائل
        filament_factor = self._apply_filament_pattern_analysis(word, pattern_name, root_analysis)

        # دمج العوامل
        enhanced_confidence = (
            base_similarity * 0.4 +
            zero_duality_factor * 0.2 +
            perpendicularity_factor * 0.2 +
            filament_factor * 0.2
        )

        return min(enhanced_confidence, 1.0)

    def _apply_zero_duality_pattern_analysis(self, word: str, pattern_name: str) -> float:
        """تطبيق ثنائية الصفر في تحليل النمط"""
        # تحليل التوازن في النمط
        pattern_info = self.pattern_database.get(pattern_name, {})
        template = pattern_info.get('template', '')

        if not template:
            return 0.5

        # حساب التوازن بين الجذر والزوائد
        root_positions = sum(1 for char in template if char in 'فعل')
        total_positions = len(template)

        if total_positions == 0:
            return 0.5

        balance_ratio = root_positions / total_positions

        # تطبيق معادلة ثنائية الصفر
        alpha = self.zero_duality_params['alpha'][1]
        beta = self.zero_duality_params['beta'][1]

        balance_score = alpha * (1 / (1 + math.exp(-5 * (balance_ratio - 0.5)))) + beta

        return min(balance_score, 1.0)

    def _apply_perpendicularity_pattern_analysis(self, word: str, pattern_name: str) -> float:
        """تطبيق التعامد في تحليل النمط"""
        # تحليل التعامد بين أجزاء النمط
        theta = self.perpendicularity_params['theta'][1]
        phi = self.perpendicularity_params['phi'][1]

        # حساب التعامد بناء على موقع النمط في الكلمة
        pattern_length = len(self.pattern_database.get(pattern_name, {}).get('template', ''))
        word_length = len(word)

        if word_length == 0:
            return 0.5

        length_ratio = pattern_length / word_length
        orthogonal_score = phi * math.sin(theta * math.pi * length_ratio)

        return min(abs(orthogonal_score), 1.0)

    def _apply_filament_pattern_analysis(self, word: str, pattern_name: str, root_analysis: RootAnalysis) -> float:
        """تطبيق الفتائل في تحليل النمط"""
        # تحليل التشابك بين النمط والجذر
        lambda_param = self.filament_params['lambda'][1]
        mu = self.filament_params['mu'][1]
        sigma = self.filament_params['sigma'][1]

        # حساب التوافق بين النمط ونوع الجذر
        pattern_info = self.pattern_database.get(pattern_name, {})
        expected_root_length = pattern_info.get('root_length', 3)
        actual_root_length = len(root_analysis.root_letters)

        length_compatibility = 1.0 - abs(expected_root_length - actual_root_length) / 3.0
        length_compatibility = max(0.0, length_compatibility)

        # تطبيق معادلة الفتائل
        filament_score = lambda_param * math.exp(-((length_compatibility - mu) ** 2) / (2 * sigma ** 2))

        return min(filament_score / lambda_param, 1.0)  # تطبيع النتيجة

    def _extract_root_from_pattern(self, word: str, pattern_name: str, pattern_data: Dict) -> List[str]:
        """استخراج الجذر بناء على النمط المحدد"""
        template = self.pattern_database.get(pattern_name, {}).get('template', '')

        if not template or len(word) != len(template):
            return list(word[:3])  # افتراضي

        root_chars = []
        for i, (w_char, t_char) in enumerate(zip(word, template)):
            if t_char in 'فعل':  # مواضع الجذر
                root_chars.append(w_char)

        return root_chars if root_chars else list(word[:3])

    def _classify_word_type(self, word: str, pattern_analysis: PatternAnalysis) -> WordType:
        """تصنيف نوع الكلمة"""
        # تصنيف بناء على النمط الصرفي
        pattern_type = pattern_analysis.pattern_type

        if pattern_type == PatternType.FAAL:
            return WordType.VERB
        elif pattern_type in [PatternType.FAAEL, PatternType.MAFOOL]:
            return WordType.NOUN
        elif pattern_type == PatternType.FAAIL:
            return WordType.ADJECTIVE

        # تصنيف بناء على خصائص الكلمة
        if word.endswith('ة'):
            return WordType.NOUN
        elif word.startswith('ال'):
            return WordType.NOUN
        elif len(word) == 3:
            return WordType.VERB
        else:
            return WordType.UNKNOWN

    def _analyze_morphological_features(self, word: str, word_type: WordType, pattern_analysis: PatternAnalysis) -> MorphologicalFeatures:
        """تحليل الخصائص الصرفية"""
        features = MorphologicalFeatures()

        # تحديد الجنس
        if word.endswith('ة'):
            features.gender = "مؤنث"
        else:
            features.gender = "مذكر"

        # تحديد العدد
        if word.endswith(('ان', 'ين')):
            features.number = "مثنى"
        elif word.endswith(('ون', 'ين', 'ات')):
            features.number = "جمع"
        else:
            features.number = "مفرد"

        # تحديد التعريف
        if word.startswith('ال'):
            features.definiteness = "معرفة"
        else:
            features.definiteness = "نكرة"

        # تحديد الزمن (للأفعال)
        if word_type == WordType.VERB:
            if pattern_analysis.pattern_type == PatternType.FAAL:
                features.tense = "ماضي"
            else:
                features.tense = "غير_محدد"

        return features

    def _calculate_semantic_weight(self, word: str, root_analysis: RootAnalysis, pattern_analysis: PatternAnalysis) -> float:
        """حساب الوزن الدلالي"""
        # وزن أساسي من قوة الجذر
        base_weight = root_analysis.strength * 0.6

        # وزن من ثقة النمط
        pattern_weight = pattern_analysis.confidence * 0.4

        # تعديل بناء على طول الكلمة
        length_factor = min(len(word) / 10.0, 1.0)

        semantic_weight = (base_weight + pattern_weight) * length_factor

        return min(semantic_weight, 1.0)

    def _calculate_confidence_score(self, root_analysis: RootAnalysis, pattern_analysis: PatternAnalysis, word_type: WordType) -> float:
        """حساب مستوى الثقة الإجمالي"""
        # ثقة الجذر
        root_confidence = root_analysis.confidence * 0.5

        # ثقة النمط
        pattern_confidence = pattern_analysis.confidence * 0.3

        # ثقة تصنيف نوع الكلمة
        type_confidence = 0.8 if word_type != WordType.UNKNOWN else 0.3
        type_confidence *= 0.2

        total_confidence = root_confidence + pattern_confidence + type_confidence

        return min(total_confidence, 1.0)

    def _update_stats(self, analysis: MorphologicalAnalysis, processing_time: float) -> None:
        """تحديث إحصائيات النظام"""
        self.stats['total_analyses'] += 1

        if analysis.root_analysis.confidence > 0.7:
            self.stats['successful_root_extractions'] += 1

        if analysis.pattern_analysis.confidence > 0.7:
            self.stats['successful_pattern_identifications'] += 1

        # تحديث متوسط الثقة
        current_avg = self.stats['average_confidence']
        total_analyses = self.stats['total_analyses']
        new_avg = ((current_avg * (total_analyses - 1)) + analysis.confidence_score) / total_analyses
        self.stats['average_confidence'] = new_avg

        # تحديث متوسط وقت المعالجة
        current_time_avg = self.stats['processing_time']
        new_time_avg = ((current_time_avg * (total_analyses - 1)) + processing_time) / total_analyses
        self.stats['processing_time'] = new_time_avg

    def get_analysis_report(self, analysis: MorphologicalAnalysis) -> str:
        """إنشاء تقرير تحليل مفصل"""
        report = f"""
🔤 تقرير التحليل الصرفي الثوري
{'='*50}

📝 الكلمة الأصلية: {analysis.original_word}
🔧 الكلمة المطبعة: {analysis.normalized_word}

🌱 تحليل الجذر:
   📌 الجذر: {analysis.root_analysis.root_letters}
   📊 النوع: {analysis.root_analysis.root_type.value}
   💡 المعنى الأساسي: {analysis.root_analysis.meaning_core}
   🎯 الحقل الدلالي: {analysis.root_analysis.semantic_field}
   💪 القوة: {analysis.root_analysis.strength:.2f}
   ✅ الثقة: {analysis.root_analysis.confidence:.2f}

⚖️ تحليل الوزن الصرفي:
   📐 الوزن: {analysis.pattern_analysis.pattern_name}
   🏷️ النوع: {analysis.pattern_analysis.pattern_type.value}
   🔧 الوظيفة: {analysis.pattern_analysis.morphological_function}
   🎭 الدور الدلالي: {analysis.pattern_analysis.semantic_role}
   ✅ الثقة: {analysis.pattern_analysis.confidence:.2f}

🔍 تحليل المكونات:
   ⬅️ البادئة: {analysis.prefix or 'لا توجد'}
   ➡️ اللاحقة: {analysis.suffix or 'لا توجد'}
   🔄 الحشو: {analysis.infix or 'لا يوجد'}

📊 تصنيف الكلمة:
   🏷️ النوع: {analysis.word_type.value}

🎯 الخصائص الصرفية:
   👫 الجنس: {analysis.morphological_features.gender}
   🔢 العدد: {analysis.morphological_features.number}
   📖 التعريف: {analysis.morphological_features.definiteness}
   ⏰ الزمن: {analysis.morphological_features.tense}

📈 النتائج النهائية:
   🎯 الوزن الدلالي: {analysis.semantic_weight:.2f}
   ✅ مستوى الثقة الإجمالي: {analysis.confidence_score:.2f}
   🕐 وقت التحليل: {analysis.timestamp.strftime('%Y-%m-%d %H:%M:%S')}

🧬 تم التحليل باستخدام النظريات الثلاث الثورية لنظام بصيرة
"""
        return report

    def get_system_stats(self) -> str:
        """إحصائيات النظام"""
        success_rate_root = (self.stats['successful_root_extractions'] / max(1, self.stats['total_analyses'])) * 100
        success_rate_pattern = (self.stats['successful_pattern_identifications'] / max(1, self.stats['total_analyses'])) * 100

        return f"""
📊 إحصائيات نظام الصرف العربي الثوري
{'='*50}

📈 الإحصائيات العامة:
   🔢 إجمالي التحليلات: {self.stats['total_analyses']}
   ✅ نجاح استخراج الجذور: {self.stats['successful_root_extractions']} ({success_rate_root:.1f}%)
   ⚖️ نجاح تحديد الأوزان: {self.stats['successful_pattern_identifications']} ({success_rate_pattern:.1f}%)
   🎯 متوسط الثقة: {self.stats['average_confidence']:.3f}
   ⏱️ متوسط وقت المعالجة: {self.stats['processing_time']:.3f} ثانية

🧬 النظريات الثورية المستخدمة:
   ⚡ نظرية ثنائية الصفر: نشطة
   🔄 نظرية تعامد الأضداد: نشطة
   🌀 نظرية الفتائل: نشطة

💾 ذاكرة النظام:
   🗃️ تحليلات محفوظة: {len(self.analysis_cache)}
   🌱 جذور محفوظة: {len(self.root_cache)}
   📚 جذور في قاعدة البيانات: {len(self.root_database)}
   ⚖️ أوزان في قاعدة البيانات: {len(self.pattern_database)}

🚀 النظام جاهز للتحليل الصرفي المتقدم!
"""

def main():
    """اختبار النظام"""
    print("🔤⚡ اختبار نظام الصرف العربي الثوري")
    print("="*60)

    # إنشاء النظام
    morphology_system = RevolutionaryArabicMorphologySystem()

    # كلمات للاختبار
    test_words = [
        "كتاب",
        "المعلم",
        "يكتبون",
        "مكتوب",
        "كاتب",
        "مكتبة",
        "الطلاب",
        "يدرسون",
        "معلمة",
        "دراسة"
    ]

    print(f"\n🧪 اختبار {len(test_words)} كلمات:")
    print("-" * 40)

    for word in test_words:
        print(f"\n🔍 تحليل كلمة: {word}")
        analysis = morphology_system.analyze_word(word)

        print(f"   🌱 الجذر: {analysis.root_analysis.root_letters}")
        print(f"   ⚖️ الوزن: {analysis.pattern_analysis.pattern_name}")
        print(f"   🏷️ النوع: {analysis.word_type.value}")
        print(f"   ✅ الثقة: {analysis.confidence_score:.2f}")

    # عرض الإحصائيات
    print(f"\n{morphology_system.get_system_stats()}")

    # تقرير مفصل لكلمة واحدة
    detailed_analysis = morphology_system.analyze_word("المعلمون")
    print(f"\n{morphology_system.get_analysis_report(detailed_analysis)}")

if __name__ == "__main__":
    main()
