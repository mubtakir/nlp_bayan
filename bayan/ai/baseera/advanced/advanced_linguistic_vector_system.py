#!/usr/bin/env python3
"""
نظام المتجهات اللغوية المتقدم - Advanced Linguistic Vector System
نظام بصيرة الثوري

🔤 تحويل الكلمات والنصوص إلى متجهات رياضية
🧬 يعتمد على النظريات الثلاث الثورية
⚡ معالجة متقدمة للغة العربية
🎯 دعم التحليل الدلالي والسياقي

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import numpy as np
import re
import json
import math
from typing import Dict, List, Tuple, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import uuid

# استيراد المكونات الأساسية
from core_interfaces import BaseComponent
from revolutionary_mother_equation import RevolutionaryMotherEquation

class VectorType(Enum):
    """أنواع المتجهات اللغوية"""
    WORD_VECTOR = "word_vector"
    SENTENCE_VECTOR = "sentence_vector"
    SEMANTIC_VECTOR = "semantic_vector"
    CONTEXTUAL_VECTOR = "contextual_vector"
    MORPHOLOGICAL_VECTOR = "morphological_vector"

class LanguageType(Enum):
    """أنواع اللغات المدعومة"""
    ARABIC = "arabic"
    ENGLISH = "english"
    MIXED = "mixed"

@dataclass
class LinguisticVector:
    """متجه لغوي"""
    word: str
    vector: np.ndarray
    vector_type: VectorType
    language: LanguageType
    semantic_weight: float = 1.0
    contextual_weight: float = 1.0
    morphological_features: Dict[str, Any] = field(default_factory=dict)
    creation_time: datetime = field(default_factory=datetime.now)
    vector_id: str = field(default_factory=lambda: str(uuid.uuid4()))

@dataclass
class SemanticRelationship:
    """علاقة دلالية بين الكلمات"""
    word1: str
    word2: str
    relationship_type: str  # synonym, antonym, related, etc.
    strength: float  # 0-1
    context: Optional[str] = None

class ArabicMorphologyAnalyzer:
    """محلل الصرف العربي المطور - يستخدم النظريات الثلاث الثورية"""

    def __init__(self):
        # قواعد الصرف العربية المتقدمة
        self.prefixes = {
            'ال': {'type': 'تعريف', 'weight': 0.9},
            'و': {'type': 'عطف', 'weight': 0.7},
            'ف': {'type': 'عطف', 'weight': 0.7},
            'ب': {'type': 'جر', 'weight': 0.8},
            'ك': {'type': 'جر', 'weight': 0.8},
            'ل': {'type': 'جر', 'weight': 0.8},
            'من': {'type': 'جر', 'weight': 0.8},
            'إلى': {'type': 'جر', 'weight': 0.8},
            'على': {'type': 'جر', 'weight': 0.8},
            'في': {'type': 'جر', 'weight': 0.8},
            'مع': {'type': 'جر', 'weight': 0.7},
            'عن': {'type': 'جر', 'weight': 0.7},
            'بعد': {'type': 'جر', 'weight': 0.6},
            'قبل': {'type': 'جر', 'weight': 0.6}
        }

        self.suffixes = {
            'ة': {'type': 'تأنيث', 'weight': 0.9},
            'ان': {'type': 'تثنية', 'weight': 0.8},
            'ين': {'type': 'جمع_مذكر', 'weight': 0.8},
            'ون': {'type': 'جمع_مذكر', 'weight': 0.8},
            'ات': {'type': 'جمع_مؤنث', 'weight': 0.8},
            'ها': {'type': 'ضمير_مؤنث', 'weight': 0.7},
            'هم': {'type': 'ضمير_مذكر_جمع', 'weight': 0.7},
            'هن': {'type': 'ضمير_مؤنث_جمع', 'weight': 0.7},
            'كم': {'type': 'ضمير_جمع', 'weight': 0.6},
            'كن': {'type': 'ضمير_مؤنث_جمع', 'weight': 0.6},
            'نا': {'type': 'ضمير_جمع', 'weight': 0.7},
            'ني': {'type': 'ضمير_متكلم', 'weight': 0.6},
            'ك': {'type': 'ضمير_مخاطب', 'weight': 0.6}
        }

        # أوزان صرفية متقدمة مع النظريات الثورية
        self.revolutionary_patterns = {
            'فعل': {
                'template': 'فعل',
                'type': 'فعل_ماضي',
                'root_positions': [0, 1, 2],
                'semantic_weight': 0.9,
                'zero_duality_factor': 0.8,
                'perpendicularity_factor': 0.7,
                'filament_factor': 0.9
            },
            'فاعل': {
                'template': 'فاعل',
                'type': 'اسم_فاعل',
                'root_positions': [0, 2, 3],
                'semantic_weight': 0.85,
                'zero_duality_factor': 0.9,
                'perpendicularity_factor': 0.8,
                'filament_factor': 0.7
            },
            'مفعول': {
                'template': 'مفعول',
                'type': 'اسم_مفعول',
                'root_positions': [1, 2, 3],
                'semantic_weight': 0.8,
                'zero_duality_factor': 0.7,
                'perpendicularity_factor': 0.9,
                'filament_factor': 0.8
            },
            'فعيل': {
                'template': 'فعيل',
                'type': 'صفة_مشبهة',
                'root_positions': [0, 1, 3],
                'semantic_weight': 0.75,
                'zero_duality_factor': 0.8,
                'perpendicularity_factor': 0.6,
                'filament_factor': 0.9
            },
            'فعال': {
                'template': 'فعال',
                'type': 'صيغة_مبالغة',
                'root_positions': [0, 1, 3],
                'semantic_weight': 0.8,
                'zero_duality_factor': 0.9,
                'perpendicularity_factor': 0.7,
                'filament_factor': 0.8
            },
            'مفعل': {
                'template': 'مفعل',
                'type': 'اسم_مكان',
                'root_positions': [1, 2, 3],
                'semantic_weight': 0.7,
                'zero_duality_factor': 0.6,
                'perpendicularity_factor': 0.8,
                'filament_factor': 0.7
            },
            'تفعيل': {
                'template': 'تفعيل',
                'type': 'مصدر',
                'root_positions': [1, 2, 4],
                'semantic_weight': 0.85,
                'zero_duality_factor': 0.8,
                'perpendicularity_factor': 0.9,
                'filament_factor': 0.8
            },
            'استفعال': {
                'template': 'استفعال',
                'type': 'مصدر_استفعال',
                'root_positions': [2, 3, 5],
                'semantic_weight': 0.9,
                'zero_duality_factor': 0.9,
                'perpendicularity_factor': 0.8,
                'filament_factor': 0.9
            }
        }

        # قاعدة بيانات الجذور المتقدمة
        self.advanced_roots = {
            'كتب': {
                'meaning': 'الكتابة والتدوين والتسجيل',
                'semantic_field': 'علم وتعليم',
                'strength': 0.95,
                'related_concepts': ['علم', 'تعليم', 'معرفة', 'تدوين'],
                'derivatives': ['كاتب', 'مكتوب', 'كتاب', 'مكتبة', 'كتابة']
            },
            'قرأ': {
                'meaning': 'القراءة والتلاوة والمطالعة',
                'semantic_field': 'علم وتعليم',
                'strength': 0.98,
                'related_concepts': ['تلاوة', 'مطالعة', 'دراسة', 'فهم'],
                'derivatives': ['قارئ', 'مقروء', 'قراءة', 'قرآن']
            },
            'علم': {
                'meaning': 'المعرفة والإدراك والفهم',
                'semantic_field': 'علم ومعرفة',
                'strength': 0.99,
                'related_concepts': ['معرفة', 'فهم', 'إدراك', 'حكمة'],
                'derivatives': ['عالم', 'معلوم', 'تعليم', 'معلم', 'علامة']
            },
            'حمد': {
                'meaning': 'الشكر والثناء والحمد',
                'semantic_field': 'عبادة وروحانية',
                'strength': 0.96,
                'related_concepts': ['شكر', 'ثناء', 'تقدير', 'امتنان'],
                'derivatives': ['حامد', 'محمود', 'حمد', 'أحمد']
            },
            'سلم': {
                'meaning': 'السلامة والأمان والسلام',
                'semantic_field': 'سلام وأمان',
                'strength': 0.94,
                'related_concepts': ['أمان', 'طمأنينة', 'استقرار', 'هدوء'],
                'derivatives': ['سالم', 'مسلم', 'سلام', 'سلامة', 'تسليم']
            },
            'درس': {
                'meaning': 'التعلم والدراسة والبحث',
                'semantic_field': 'علم وتعليم',
                'strength': 0.92,
                'related_concepts': ['تعلم', 'بحث', 'تحصيل', 'استيعاب'],
                'derivatives': ['دارس', 'مدروس', 'دراسة', 'مدرسة', 'مدرس']
            },
            'فهم': {
                'meaning': 'الإدراك والاستيعاب والفهم',
                'semantic_field': 'علم ومعرفة',
                'strength': 0.91,
                'related_concepts': ['إدراك', 'استيعاب', 'وعي', 'بصيرة'],
                'derivatives': ['فاهم', 'مفهوم', 'فهم', 'تفهيم']
            }
        }

        # معاملات النظريات الثورية للتحليل الصرفي
        self.zero_duality_params = {
            'alpha': [1.3, 0.9, 1.1],
            'beta': [0.15, 0.12, 0.18],
            'gamma': [2.8, 3.2, 2.5]
        }

        self.perpendicularity_params = {
            'theta': [0.8, 1.2, 0.6],
            'phi': [1.4, 1.1, 1.6],
            'delta': [0.3, 0.25, 0.35]
        }

        self.filament_params = {
            'lambda': [4.5, 5.0, 4.0],
            'mu': [0.75, 0.8, 0.7],
            'sigma': [2.2, 2.5, 2.0]
        }
    
    def analyze_word(self, word: str) -> Dict[str, Any]:
        """تحليل كلمة عربية باستخدام النظريات الثورية"""
        # تنظيف الكلمة
        normalized_word = self._normalize_word(word)

        # التحليل الثوري للجذر
        root_analysis = self._revolutionary_root_extraction(normalized_word)

        # التحليل الثوري للوزن
        pattern_analysis = self._revolutionary_pattern_identification(normalized_word, root_analysis)

        # استخراج البادئات واللواحق المتقدم
        prefix_analysis = self._advanced_prefix_extraction(normalized_word)
        suffix_analysis = self._advanced_suffix_extraction(normalized_word)

        # تصنيف نوع الكلمة المتقدم
        word_type_analysis = self._advanced_word_classification(normalized_word, pattern_analysis)

        # تحليل الخصائص الصرفية المتقدم
        morphological_features = self._advanced_morphological_analysis(
            normalized_word, word_type_analysis, pattern_analysis
        )

        # حساب الوزن الدلالي الثوري
        semantic_weight = self._calculate_revolutionary_semantic_weight(
            normalized_word, root_analysis, pattern_analysis
        )

        # حساب مستوى الثقة الشامل
        confidence_score = self._calculate_comprehensive_confidence(
            root_analysis, pattern_analysis, word_type_analysis
        )

        analysis = {
            'original_word': word,
            'normalized_word': normalized_word,
            'root_analysis': root_analysis,
            'pattern_analysis': pattern_analysis,
            'prefix_analysis': prefix_analysis,
            'suffix_analysis': suffix_analysis,
            'word_type_analysis': word_type_analysis,
            'morphological_features': morphological_features,
            'semantic_weight': semantic_weight,
            'confidence_score': confidence_score,
            'revolutionary_theories_applied': {
                'zero_duality': True,
                'perpendicularity': True,
                'filament': True
            }
        }
        return analysis

    def _normalize_word(self, word: str) -> str:
        """تطبيع الكلمة العربية"""
        import re

        # إزالة التشكيل
        normalized = re.sub(r'[ًٌٍَُِّْ]', '', word)

        # توحيد الألف
        normalized = re.sub(r'[أإآ]', 'ا', normalized)

        # توحيد التاء المربوطة
        normalized = re.sub(r'ة', 'ه', normalized)

        # توحيد الياء
        normalized = re.sub(r'ى', 'ي', normalized)

        return normalized.strip()

    def _revolutionary_root_extraction(self, word: str) -> Dict[str, Any]:
        """استخراج الجذر باستخدام النظريات الثلاث الثورية"""
        # 1. تطبيق نظرية ثنائية الصفر
        zero_duality_result = self._apply_zero_duality_root_analysis(word)

        # 2. تطبيق نظرية تعامد الأضداد
        perpendicularity_result = self._apply_perpendicularity_root_analysis(word)

        # 3. تطبيق نظرية الفتائل
        filament_result = self._apply_filament_root_analysis(word)

        # دمج النتائج الثورية
        merged_root = self._merge_revolutionary_root_results(
            zero_duality_result, perpendicularity_result, filament_result
        )

        # تحليل الجذر المستخرج
        root_info = self._analyze_extracted_root(merged_root, word)

        return {
            'extracted_root': merged_root,
            'root_info': root_info,
            'zero_duality_analysis': zero_duality_result,
            'perpendicularity_analysis': perpendicularity_result,
            'filament_analysis': filament_result,
            'confidence': root_info.get('confidence', 0.5)
        }

    def _apply_zero_duality_root_analysis(self, word: str) -> Dict[str, Any]:
        """تطبيق نظرية ثنائية الصفر لاستخراج الجذر"""
        char_weights = {}

        for i, char in enumerate(word):
            # معاملات ثنائية الصفر
            alpha = self.zero_duality_params['alpha'][0]
            beta = self.zero_duality_params['beta'][0]
            gamma = self.zero_duality_params['gamma'][0]

            # حساب الموقع النسبي
            position_ratio = i / max(1, len(word) - 1)

            # تحويل الحرف إلى قيمة رقمية
            char_value = ord(char) / 1000.0

            # تطبيق معادلة ثنائية الصفر المعدلة
            sigmoid_value = alpha * (1 / (1 + math.exp(-gamma * (char_value - 0.5))))
            positional_weight = math.sin(position_ratio * math.pi) * sigmoid_value + beta

            # تطبيق التوازن الكوني (المجموع = صفر)
            balance_factor = math.cos(position_ratio * 2 * math.pi)

            final_weight = positional_weight * balance_factor
            char_weights[char] = abs(final_weight)  # القيمة المطلقة للوزن

        # ترتيب الحروف حسب الوزن
        sorted_chars = sorted(char_weights.items(), key=lambda x: x[1], reverse=True)

        # استخراج أفضل 3-4 حروف كمرشحين للجذر
        root_candidates = [char for char, weight in sorted_chars[:4]]

        return {
            'method': 'zero_duality',
            'char_weights': char_weights,
            'root_candidates': root_candidates,
            'confidence': min(1.0, sum(weight for _, weight in sorted_chars[:3]) / 3.0)
        }

    def _apply_perpendicularity_root_analysis(self, word: str) -> Dict[str, Any]:
        """تطبيق نظرية تعامد الأضداد لاستخراج الجذر"""
        orthogonal_weights = {}

        # معاملات التعامد
        theta = self.perpendicularity_params['theta'][0]
        phi = self.perpendicularity_params['phi'][0]
        delta = self.perpendicularity_params['delta'][0]

        for i, char in enumerate(word):
            # حساب التعامد الموضعي
            position_angle = (i / len(word)) * math.pi
            positional_orthogonality = phi * math.sin(theta * position_angle)

            # حساب التعامد مع الحروف الأخرى
            char_value = ord(char)
            orthogonal_sum = 0

            for j, other_char in enumerate(word):
                if i != j:
                    other_value = ord(other_char)
                    value_difference = abs(char_value - other_value)

                    # تطبيق معادلة التعامد
                    angle_factor = (value_difference / 100.0) * math.pi / 2
                    orthogonal_contribution = math.cos(angle_factor) * delta
                    orthogonal_sum += orthogonal_contribution

            # الوزن النهائي للحرف
            final_weight = positional_orthogonality + (orthogonal_sum / len(word))
            orthogonal_weights[char] = abs(final_weight)

        # ترتيب الحروف حسب التعامد
        sorted_chars = sorted(orthogonal_weights.items(), key=lambda x: x[1], reverse=True)
        root_candidates = [char for char, weight in sorted_chars[:3]]

        return {
            'method': 'perpendicularity',
            'orthogonal_weights': orthogonal_weights,
            'root_candidates': root_candidates,
            'confidence': min(1.0, sum(weight for _, weight in sorted_chars[:3]) / 3.0)
        }

    def _apply_filament_root_analysis(self, word: str) -> Dict[str, Any]:
        """تطبيق نظرية الفتائل لاستخراج الجذر"""
        # معاملات الفتائل
        lambda_param = self.filament_params['lambda'][0]
        mu = self.filament_params['mu'][0]
        sigma = self.filament_params['sigma'][0]

        pattern_matches = {}

        # تحليل التطابق مع الأوزان المعروفة
        for pattern_name, pattern_info in self.revolutionary_patterns.items():
            template = pattern_info['template']

            # حساب التشابه مع النمط
            similarity = self._calculate_pattern_similarity(word, template)

            if similarity > 0.2:  # عتبة التشابه
                # تطبيق معادلة الفتائل
                filament_strength = lambda_param * math.exp(-((similarity - mu) ** 2) / (2 * sigma ** 2))

                pattern_matches[pattern_name] = {
                    'similarity': similarity,
                    'filament_strength': filament_strength,
                    'root_positions': pattern_info['root_positions'],
                    'expected_root': self._extract_root_from_pattern(word, pattern_info)
                }

        # اختيار أفضل نمط
        if pattern_matches:
            best_pattern = max(pattern_matches.items(), key=lambda x: x[1]['filament_strength'])
            pattern_name, pattern_data = best_pattern
            root_candidates = list(pattern_data['expected_root'])
        else:
            # استخراج افتراضي
            root_candidates = list(word[:3])

        return {
            'method': 'filament',
            'pattern_matches': pattern_matches,
            'root_candidates': root_candidates,
            'confidence': max([data['filament_strength'] for data in pattern_matches.values()]) if pattern_matches else 0.3
        }

    def _calculate_pattern_similarity(self, word: str, template: str) -> float:
        """حساب التشابه مع النمط الصرفي"""
        if len(word) != len(template):
            # تعديل للأطوال المختلفة
            min_len = min(len(word), len(template))
            word_part = word[:min_len]
            template_part = template[:min_len]
        else:
            word_part = word
            template_part = template

        matches = 0
        total = len(template_part)

        for i, (w_char, t_char) in enumerate(zip(word_part, template_part)):
            if t_char in 'فعل':  # مواضع الجذر
                matches += 0.5  # وزن أقل للجذر
            elif w_char == t_char:
                matches += 1.0  # تطابق كامل
            elif self._are_similar_chars(w_char, t_char):
                matches += 0.7  # تشابه جزئي

        return matches / total if total > 0 else 0.0

    def _are_similar_chars(self, char1: str, char2: str) -> bool:
        """فحص التشابه بين الحروف"""
        similar_groups = [
            ['ا', 'أ', 'إ', 'آ'],
            ['ة', 'ه', 'ت'],
            ['ي', 'ى'],
            ['و', 'ؤ'],
            ['ذ', 'ز'],
            ['س', 'ص'],
            ['ت', 'ط'],
            ['د', 'ض']
        ]

        for group in similar_groups:
            if char1 in group and char2 in group:
                return True

        return False

    def _extract_root_from_pattern(self, word: str, pattern_info: Dict) -> str:
        """استخراج الجذر بناء على النمط"""
        root_positions = pattern_info.get('root_positions', [0, 1, 2])
        root_chars = []

        for pos in root_positions:
            if pos < len(word):
                root_chars.append(word[pos])

        return ''.join(root_chars)

    def _merge_revolutionary_root_results(self, zero_duality: Dict, perpendicularity: Dict, filament: Dict) -> str:
        """دمج نتائج النظريات الثلاث لاستخراج الجذر النهائي"""
        # جمع جميع المرشحين
        all_candidates = []
        all_candidates.extend(zero_duality['root_candidates'])
        all_candidates.extend(perpendicularity['root_candidates'])
        all_candidates.extend(filament['root_candidates'])

        # حساب تكرار وأوزان الحروف
        char_scores = {}

        for char in set(all_candidates):
            score = 0

            # وزن من ثنائية الصفر
            if char in zero_duality['root_candidates']:
                idx = zero_duality['root_candidates'].index(char)
                score += zero_duality['confidence'] * (1.0 - idx * 0.1) * 0.35

            # وزن من التعامد
            if char in perpendicularity['root_candidates']:
                idx = perpendicularity['root_candidates'].index(char)
                score += perpendicularity['confidence'] * (1.0 - idx * 0.1) * 0.30

            # وزن من الفتائل
            if char in filament['root_candidates']:
                idx = filament['root_candidates'].index(char)
                score += filament['confidence'] * (1.0 - idx * 0.1) * 0.35

            char_scores[char] = score

        # اختيار أفضل 3 حروف
        sorted_chars = sorted(char_scores.items(), key=lambda x: x[1], reverse=True)
        root_letters = ''.join([char for char, score in sorted_chars[:3]])

        return root_letters

    def _analyze_extracted_root(self, root: str, original_word: str) -> Dict[str, Any]:
        """تحليل الجذر المستخرج"""
        if root in self.advanced_roots:
            root_data = self.advanced_roots[root]
            confidence = root_data['strength']
        else:
            # تحليل تقديري للجذور غير المعروفة
            root_data = {
                'meaning': f'معنى مشتق من الجذر {root}',
                'semantic_field': 'عام',
                'strength': 0.6,
                'related_concepts': [],
                'derivatives': []
            }
            confidence = 0.6

        # حساب قوة الجذر في السياق
        contextual_strength = len(root) / len(original_word)
        final_confidence = min((confidence + contextual_strength) / 2, 1.0)

        return {
            'root': root,
            'meaning': root_data['meaning'],
            'semantic_field': root_data['semantic_field'],
            'strength': root_data['strength'],
            'confidence': final_confidence,
            'related_concepts': root_data.get('related_concepts', []),
            'derivatives': root_data.get('derivatives', [])
        }
    
    def _revolutionary_pattern_identification(self, word: str, root_analysis: Dict) -> Dict[str, Any]:
        """تحديد الوزن الصرفي باستخدام النظريات الثورية"""
        best_pattern = None
        best_confidence = 0.0
        pattern_scores = {}

        for pattern_name, pattern_info in self.revolutionary_patterns.items():
            # حساب التطابق الأساسي
            base_similarity = self._calculate_pattern_similarity(word, pattern_info['template'])

            # تطبيق النظريات الثورية لتحسين التحديد
            revolutionary_enhancement = self._apply_revolutionary_pattern_enhancement(
                word, pattern_name, pattern_info, root_analysis
            )

            # حساب النتيجة النهائية
            final_score = (base_similarity * 0.4) + (revolutionary_enhancement * 0.6)
            pattern_scores[pattern_name] = final_score

            if final_score > best_confidence:
                best_confidence = final_score
                best_pattern = pattern_name

        if best_pattern:
            pattern_info = self.revolutionary_patterns[best_pattern]
            return {
                'identified_pattern': best_pattern,
                'pattern_type': pattern_info['type'],
                'template': pattern_info['template'],
                'semantic_weight': pattern_info['semantic_weight'],
                'confidence': best_confidence,
                'all_scores': pattern_scores,
                'revolutionary_factors': {
                    'zero_duality': pattern_info['zero_duality_factor'],
                    'perpendicularity': pattern_info['perpendicularity_factor'],
                    'filament': pattern_info['filament_factor']
                }
            }
        else:
            return {
                'identified_pattern': 'غير_محدد',
                'pattern_type': 'غير_معروف',
                'template': 'غير_محدد',
                'semantic_weight': 0.5,
                'confidence': 0.3,
                'all_scores': pattern_scores,
                'revolutionary_factors': {
                    'zero_duality': 0.5,
                    'perpendicularity': 0.5,
                    'filament': 0.5
                }
            }

    def _apply_revolutionary_pattern_enhancement(self, word: str, pattern_name: str, pattern_info: Dict, root_analysis: Dict) -> float:
        """تطبيق النظريات الثورية لتحسين تحديد النمط"""
        # 1. عامل ثنائية الصفر
        zero_duality_factor = self._calculate_zero_duality_pattern_factor(word, pattern_info)

        # 2. عامل التعامد
        perpendicularity_factor = self._calculate_perpendicularity_pattern_factor(word, pattern_info)

        # 3. عامل الفتائل
        filament_factor = self._calculate_filament_pattern_factor(word, pattern_info, root_analysis)

        # دمج العوامل الثورية
        revolutionary_score = (
            zero_duality_factor * pattern_info['zero_duality_factor'] * 0.35 +
            perpendicularity_factor * pattern_info['perpendicularity_factor'] * 0.30 +
            filament_factor * pattern_info['filament_factor'] * 0.35
        )

        return min(revolutionary_score, 1.0)

    def _calculate_zero_duality_pattern_factor(self, word: str, pattern_info: Dict) -> float:
        """حساب عامل ثنائية الصفر للنمط"""
        template = pattern_info['template']
        root_positions = pattern_info['root_positions']

        # تحليل التوازن بين الجذر والزوائد
        root_chars = len(root_positions)
        total_chars = len(template)

        if total_chars == 0:
            return 0.5

        # نسبة التوازن
        balance_ratio = root_chars / total_chars

        # تطبيق معادلة ثنائية الصفر
        alpha = self.zero_duality_params['alpha'][1]
        gamma = self.zero_duality_params['gamma'][1]

        # معادلة السيغمويد المعدلة للتوازن
        balance_score = alpha * (1 / (1 + math.exp(-gamma * (balance_ratio - 0.5))))

        # تطبيق التوازن الكوني
        cosmic_balance = math.cos(balance_ratio * math.pi)

        return min(abs(balance_score * cosmic_balance), 1.0)

    def _calculate_perpendicularity_pattern_factor(self, word: str, pattern_info: Dict) -> float:
        """حساب عامل التعامد للنمط"""
        template = pattern_info['template']

        # معاملات التعامد
        theta = self.perpendicularity_params['theta'][1]
        phi = self.perpendicularity_params['phi'][1]

        # حساب التعامد بناء على طول النمط
        pattern_length = len(template)
        word_length = len(word)

        if word_length == 0:
            return 0.5

        # نسبة الطول
        length_ratio = pattern_length / word_length

        # تطبيق معادلة التعامد
        orthogonal_score = phi * math.sin(theta * math.pi * length_ratio)

        return min(abs(orthogonal_score), 1.0)

    def _calculate_filament_pattern_factor(self, word: str, pattern_info: Dict, root_analysis: Dict) -> float:
        """حساب عامل الفتائل للنمط"""
        # معاملات الفتائل
        lambda_param = self.filament_params['lambda'][1]
        mu = self.filament_params['mu'][1]
        sigma = self.filament_params['sigma'][1]

        # حساب التوافق بين النمط والجذر المستخرج
        extracted_root = root_analysis.get('extracted_root', '')
        expected_root_length = len(pattern_info['root_positions'])
        actual_root_length = len(extracted_root)

        # حساب التوافق
        if expected_root_length == 0:
            compatibility = 0.5
        else:
            compatibility = 1.0 - abs(expected_root_length - actual_root_length) / expected_root_length
            compatibility = max(0.0, compatibility)

        # تطبيق معادلة الفتائل
        filament_score = lambda_param * math.exp(-((compatibility - mu) ** 2) / (2 * sigma ** 2))

        return min(filament_score / lambda_param, 1.0)

    def _advanced_prefix_extraction(self, word: str) -> Dict[str, Any]:
        """استخراج البادئات المتقدم"""
        detected_prefixes = []
        remaining_word = word

        # البحث عن البادئات بترتيب الطول (الأطول أولاً)
        for prefix in sorted(self.prefixes.keys(), key=len, reverse=True):
            if remaining_word.startswith(prefix):
                prefix_info = self.prefixes[prefix]
                detected_prefixes.append({
                    'prefix': prefix,
                    'type': prefix_info['type'],
                    'weight': prefix_info['weight']
                })
                remaining_word = remaining_word[len(prefix):]
                break  # نأخذ أول (أطول) بادئة فقط

        return {
            'detected_prefixes': detected_prefixes,
            'remaining_word': remaining_word,
            'has_prefix': len(detected_prefixes) > 0,
            'prefix_confidence': detected_prefixes[0]['weight'] if detected_prefixes else 0.0
        }

    def _advanced_suffix_extraction(self, word: str) -> Dict[str, Any]:
        """استخراج اللواحق المتقدم"""
        detected_suffixes = []
        remaining_word = word

        # البحث عن اللواحق بترتيب الطول (الأطول أولاً)
        for suffix in sorted(self.suffixes.keys(), key=len, reverse=True):
            if remaining_word.endswith(suffix):
                suffix_info = self.suffixes[suffix]
                detected_suffixes.append({
                    'suffix': suffix,
                    'type': suffix_info['type'],
                    'weight': suffix_info['weight']
                })
                remaining_word = remaining_word[:-len(suffix)]
                break  # نأخذ أول (أطول) لاحقة فقط

        return {
            'detected_suffixes': detected_suffixes,
            'remaining_word': remaining_word,
            'has_suffix': len(detected_suffixes) > 0,
            'suffix_confidence': detected_suffixes[0]['weight'] if detected_suffixes else 0.0
        }

    def _advanced_word_classification(self, word: str, pattern_analysis: Dict) -> Dict[str, Any]:
        """تصنيف نوع الكلمة المتقدم"""
        pattern_type = pattern_analysis.get('pattern_type', 'غير_معروف')
        confidence = pattern_analysis.get('confidence', 0.5)

        # تصنيف بناء على النمط الصرفي
        if 'فعل' in pattern_type:
            word_type = 'فعل'
            type_confidence = confidence * 0.9
        elif 'اسم' in pattern_type:
            word_type = 'اسم'
            type_confidence = confidence * 0.8
        elif 'صفة' in pattern_type:
            word_type = 'صفة'
            type_confidence = confidence * 0.8
        elif 'مصدر' in pattern_type:
            word_type = 'مصدر'
            type_confidence = confidence * 0.7
        else:
            # تصنيف بناء على خصائص الكلمة
            if word.endswith('ة'):
                word_type = 'اسم_مؤنث'
                type_confidence = 0.7
            elif word.startswith('ال'):
                word_type = 'اسم_معرف'
                type_confidence = 0.8
            elif len(word) == 3:
                word_type = 'فعل_محتمل'
                type_confidence = 0.6
            else:
                word_type = 'غير_محدد'
                type_confidence = 0.3

        return {
            'word_type': word_type,
            'confidence': type_confidence,
            'classification_method': 'pattern_based' if confidence > 0.5 else 'heuristic_based'
        }

    def _advanced_morphological_analysis(self, word: str, word_type_analysis: Dict, pattern_analysis: Dict) -> Dict[str, Any]:
        """تحليل الخصائص الصرفية المتقدم"""
        features = {}

        # تحديد الجنس
        if word.endswith('ة'):
            features['gender'] = 'مؤنث'
            features['gender_confidence'] = 0.9
        elif 'مؤنث' in word_type_analysis.get('word_type', ''):
            features['gender'] = 'مؤنث'
            features['gender_confidence'] = 0.8
        else:
            features['gender'] = 'مذكر'
            features['gender_confidence'] = 0.7

        # تحديد العدد
        if word.endswith(('ان', 'ين')) and len(word) > 3:
            features['number'] = 'مثنى'
            features['number_confidence'] = 0.9
        elif word.endswith(('ون', 'ين', 'ات')):
            features['number'] = 'جمع'
            features['number_confidence'] = 0.8
        else:
            features['number'] = 'مفرد'
            features['number_confidence'] = 0.8

        # تحديد التعريف
        if word.startswith('ال'):
            features['definiteness'] = 'معرفة'
            features['definiteness_confidence'] = 0.95
        else:
            features['definiteness'] = 'نكرة'
            features['definiteness_confidence'] = 0.8

        # تحديد الزمن (للأفعال)
        word_type = word_type_analysis.get('word_type', '')
        if 'فعل' in word_type:
            pattern_name = pattern_analysis.get('identified_pattern', '')
            if pattern_name == 'فعل':
                features['tense'] = 'ماضي'
                features['tense_confidence'] = 0.8
            elif 'يفعل' in pattern_name or 'مضارع' in pattern_name:
                features['tense'] = 'مضارع'
                features['tense_confidence'] = 0.8
            else:
                features['tense'] = 'غير_محدد'
                features['tense_confidence'] = 0.3

        return features

    def _calculate_revolutionary_semantic_weight(self, word: str, root_analysis: Dict, pattern_analysis: Dict) -> float:
        """حساب الوزن الدلالي باستخدام النظريات الثورية"""
        # وزن من قوة الجذر
        root_weight = root_analysis.get('confidence', 0.5) * 0.4

        # وزن من النمط الصرفي
        pattern_weight = pattern_analysis.get('semantic_weight', 0.5) * 0.3

        # وزن من ثقة النمط
        pattern_confidence_weight = pattern_analysis.get('confidence', 0.5) * 0.2

        # وزن من طول الكلمة (الكلمات الأطول قد تكون أكثر تعقيداً)
        length_weight = min(len(word) / 10.0, 1.0) * 0.1

        total_weight = root_weight + pattern_weight + pattern_confidence_weight + length_weight

        return min(total_weight, 1.0)

    def _calculate_comprehensive_confidence(self, root_analysis: Dict, pattern_analysis: Dict, word_type_analysis: Dict) -> float:
        """حساب مستوى الثقة الشامل"""
        # ثقة الجذر
        root_confidence = root_analysis.get('confidence', 0.5) * 0.4

        # ثقة النمط
        pattern_confidence = pattern_analysis.get('confidence', 0.5) * 0.35

        # ثقة تصنيف نوع الكلمة
        type_confidence = word_type_analysis.get('confidence', 0.5) * 0.25

        total_confidence = root_confidence + pattern_confidence + type_confidence

        return min(total_confidence, 1.0)
    
    def _extract_prefix(self, word: str) -> Optional[str]:
        """استخراج البادئة"""
        for prefix in self.prefixes:
            if word.startswith(prefix):
                return prefix
        return None
    
    def _extract_suffix(self, word: str) -> Optional[str]:
        """استخراج اللاحقة"""
        for suffix in self.suffixes:
            if word.endswith(suffix):
                return suffix
        return None
    
    def _identify_pattern(self, word: str) -> str:
        """تحديد الوزن الصرفي"""
        # تبسيط لتحديد الوزن
        if len(word) == 3:
            return "فعل"
        elif len(word) == 4:
            return "فعال"
        elif len(word) == 5:
            return "فاعل"
        else:
            return "مركب"
    
    def _classify_word_type(self, word: str) -> str:
        """تصنيف نوع الكلمة"""
        # تصنيف مبسط
        if word.endswith('ة'):
            return "اسم_مؤنث"
        elif word.startswith('ال'):
            return "اسم_معرف"
        else:
            return "اسم_نكرة"
    
    def _extract_features(self, word: str) -> Dict[str, Any]:
        """استخراج الخصائص الصرفية"""
        return {
            'length': len(word),
            'has_prefix': self._extract_prefix(word) is not None,
            'has_suffix': self._extract_suffix(word) is not None,
            'vowel_count': len([c for c in word if c in 'اةيوأإآ']),
            'consonant_count': len([c for c in word if c not in 'اةيوأإآ'])
        }

class AdvancedLinguisticVectorSystem(BaseComponent):
    """نظام المتجهات اللغوية المتقدم"""
    
    def __init__(self, name: str = "AdvancedLinguisticVectorSystem"):
        super().__init__(name)
        
        # المكونات الأساسية
        self.morphology_analyzer = ArabicMorphologyAnalyzer()
        self.word_vectors: Dict[str, LinguisticVector] = {}
        self.semantic_relationships: List[SemanticRelationship] = []
        self.vector_dimension = 100  # أبعاد المتجه
        
        # المعادلة الأم للحسابات
        self.mother_equation = None
        self._initialize_mother_equation()
        
        # قواميس دلالية أساسية
        self.semantic_categories = self._initialize_semantic_categories()
        self.contextual_weights = self._initialize_contextual_weights()
        
        # إحصائيات النظام
        self.stats = {
            'total_vectors': 0,
            'arabic_vectors': 0,
            'english_vectors': 0,
            'semantic_relationships': 0,
            'processing_time': 0.0
        }
    
    def initialize(self) -> bool:
        """تهيئة النظام"""
        try:
            print(f"🔤⚡ تم إنشاء نظام المتجهات اللغوية المتقدم: {self.name}")
            print(f"   📊 أبعاد المتجه: {self.vector_dimension}")
            print(f"   🧬 محلل الصرف العربي: نشط")
            print(f"   📚 الفئات الدلالية: {len(self.semantic_categories)}")
            
            self.is_initialized = True
            return True
        except Exception as e:
            print(f"❌ فشل تهيئة نظام المتجهات اللغوية: {e}")
            return False
    
    def _initialize_mother_equation(self):
        """تهيئة المعادلة الأم"""
        try:
            # إنشاء معادلة أم مخصصة للمتجهات اللغوية
            class LinguisticMotherEquation(RevolutionaryMotherEquation):
                def __init__(self, name):
                    super().__init__(name)
                
                def process_input(self, input_data: Any) -> Any:
                    return input_data
                
                def generate_output(self, processed_data: Any) -> Any:
                    return processed_data
            
            self.mother_equation = LinguisticMotherEquation("LinguisticVectorEquation")
        except Exception as e:
            print(f"⚠️ تحذير: فشل إنشاء المعادلة الأم للمتجهات: {e}")
    
    def _initialize_semantic_categories(self) -> Dict[str, List[str]]:
        """تهيئة الفئات الدلالية"""
        return {
            'إيجابي': ['خير', 'نور', 'حب', 'سلام', 'فرح', 'أمل', 'نجاح', 'جمال'],
            'سلبي': ['شر', 'ظلام', 'كره', 'حرب', 'حزن', 'يأس', 'فشل', 'قبح'],
            'طبيعة': ['شمس', 'قمر', 'نجم', 'بحر', 'جبل', 'شجر', 'زهر', 'ماء'],
            'إنسان': ['رجل', 'امرأة', 'طفل', 'أب', 'أم', 'أخ', 'أخت', 'صديق'],
            'علم': ['كتاب', 'قلم', 'مدرسة', 'معلم', 'طالب', 'درس', 'امتحان', 'شهادة'],
            'دين': ['الله', 'رسول', 'قرآن', 'صلاة', 'صوم', 'حج', 'زكاة', 'إيمان'],
            'زمن': ['يوم', 'ليل', 'صباح', 'مساء', 'أمس', 'اليوم', 'غد', 'سنة'],
            'مكان': ['بيت', 'مدينة', 'قرية', 'شارع', 'حديقة', 'مسجد', 'مدرسة', 'مستشفى']
        }
    
    def _initialize_contextual_weights(self) -> Dict[str, float]:
        """تهيئة أوزان السياق"""
        return {
            'قرآني': 1.0,
            'ديني': 0.9,
            'أدبي': 0.8,
            'علمي': 0.7,
            'يومي': 0.6,
            'عامي': 0.5
        }
    
    def process(self, input_data: Any) -> Any:
        """معالجة البيانات اللغوية"""
        if isinstance(input_data, str):
            return self.create_word_vector(input_data)
        elif isinstance(input_data, list):
            return [self.create_word_vector(word) for word in input_data]
        else:
            return None
    
    def create_word_vector(self, word: str, context: str = "عام") -> LinguisticVector:
        """إنشاء متجه لكلمة"""
        start_time = datetime.now()
        
        # تحديد نوع اللغة
        language = self._detect_language(word)
        
        # تحليل صرفي للعربية
        morphological_features = {}
        if language == LanguageType.ARABIC:
            morphological_features = self.morphology_analyzer.analyze_word(word)
        
        # إنشاء المتجه الأساسي
        base_vector = self._generate_base_vector(word, language)
        
        # إضافة الخصائص الدلالية
        semantic_vector = self._add_semantic_features(base_vector, word)
        
        # إضافة الخصائص السياقية
        contextual_vector = self._add_contextual_features(semantic_vector, word, context)
        
        # إضافة الخصائص الصرفية
        final_vector = self._add_morphological_features(contextual_vector, morphological_features)
        
        # إنشاء المتجه اللغوي
        linguistic_vector = LinguisticVector(
            word=word,
            vector=final_vector,
            vector_type=VectorType.WORD_VECTOR,
            language=language,
            semantic_weight=self._calculate_semantic_weight(word),
            contextual_weight=self.contextual_weights.get(context, 0.5),
            morphological_features=morphological_features
        )
        
        # حفظ المتجه
        self.word_vectors[word] = linguistic_vector
        
        # تحديث الإحصائيات
        self._update_stats(language, start_time)
        
        return linguistic_vector
    
    def _detect_language(self, word: str) -> LanguageType:
        """كشف نوع اللغة"""
        arabic_chars = set('ابتثجحخدذرزسشصضطظعغفقكلمنهوياةأإآ')
        english_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        
        word_chars = set(word)
        
        if word_chars & arabic_chars:
            if word_chars & english_chars:
                return LanguageType.MIXED
            else:
                return LanguageType.ARABIC
        elif word_chars & english_chars:
            return LanguageType.ENGLISH
        else:
            return LanguageType.MIXED
    
    def _generate_base_vector(self, word: str, language: LanguageType) -> np.ndarray:
        """إنشاء المتجه الأساسي"""
        # استخدام المعادلة الأم لإنشاء المتجه
        vector = np.zeros(self.vector_dimension)
        
        # تحويل الأحرف إلى قيم رقمية
        for i, char in enumerate(word[:self.vector_dimension]):
            char_value = ord(char) / 1000.0
            
            # تطبيق النظريات الثلاث الثورية
            if self.mother_equation:
                # نظرية ثنائية الصفر
                zero_duality = math.sin(char_value * math.pi) * math.cos(char_value * math.pi)
                
                # نظرية تعامد الأضداد
                perpendicular = math.sin(char_value) * math.cos(char_value + math.pi/2)
                
                # نظرية الفتائل
                filament = math.exp(-char_value) * math.sin(char_value * 2 * math.pi)
                
                # دمج النظريات
                vector[i % self.vector_dimension] = (zero_duality + perpendicular + filament) / 3
            else:
                vector[i % self.vector_dimension] = char_value
        
        # تطبيع المتجه
        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm
        
        return vector
    
    def _add_semantic_features(self, base_vector: np.ndarray, word: str) -> np.ndarray:
        """إضافة الخصائص الدلالية"""
        semantic_vector = base_vector.copy()
        
        # البحث في الفئات الدلالية
        for category, words in self.semantic_categories.items():
            if word in words:
                # إضافة وزن دلالي للفئة
                category_weight = hash(category) % 100 / 100.0
                semantic_vector += category_weight * 0.1
        
        return semantic_vector
    
    def _add_contextual_features(self, semantic_vector: np.ndarray, word: str, context: str) -> np.ndarray:
        """إضافة الخصائص السياقية"""
        contextual_vector = semantic_vector.copy()
        
        # تطبيق وزن السياق
        context_weight = self.contextual_weights.get(context, 0.5)
        contextual_vector *= context_weight
        
        return contextual_vector
    
    def _add_morphological_features(self, contextual_vector: np.ndarray, morphological_features: Dict[str, Any]) -> np.ndarray:
        """إضافة الخصائص الصرفية"""
        final_vector = contextual_vector.copy()
        
        if morphological_features:
            # إضافة خصائص الجذر
            if 'root' in morphological_features:
                root = morphological_features['root']
                root_weight = len(root) / 10.0
                final_vector += root_weight * 0.05
            
            # إضافة خصائص الوزن
            if 'pattern' in morphological_features:
                pattern = morphological_features['pattern']
                pattern_weight = hash(pattern) % 100 / 100.0
                final_vector += pattern_weight * 0.03
        
        return final_vector
    
    def _calculate_semantic_weight(self, word: str) -> float:
        """حساب الوزن الدلالي"""
        weight = 0.5  # وزن افتراضي
        
        # زيادة الوزن للكلمات في الفئات الدلالية
        for category, words in self.semantic_categories.items():
            if word in words:
                if category in ['دين', 'قرآني']:
                    weight += 0.3
                elif category in ['إيجابي', 'علم']:
                    weight += 0.2
                else:
                    weight += 0.1
        
        return min(weight, 1.0)  # تحديد الحد الأقصى
    
    def _update_stats(self, language: LanguageType, start_time: datetime):
        """تحديث الإحصائيات"""
        self.stats['total_vectors'] += 1
        
        if language == LanguageType.ARABIC:
            self.stats['arabic_vectors'] += 1
        elif language == LanguageType.ENGLISH:
            self.stats['english_vectors'] += 1
        
        processing_time = (datetime.now() - start_time).total_seconds()
        self.stats['processing_time'] += processing_time

# اختبار النظام
def test_linguistic_vector_system():
    """اختبار نظام المتجهات اللغوية"""
    print("🧪 اختبار نظام المتجهات اللغوية المتقدم")
    print("=" * 50)
    
    # إنشاء النظام
    system = AdvancedLinguisticVectorSystem()
    system.initialize()
    
    # كلمات تجريبية
    test_words = ['الله', 'رسول', 'قرآن', 'نور', 'هداية', 'cat', 'love', 'peace']
    
    print(f"\n🔤 اختبار إنشاء المتجهات:")
    for word in test_words:
        vector = system.create_word_vector(word, 'ديني')
        print(f"   📊 {word}: متجه {vector.vector.shape} | لغة: {vector.language.value}")
        print(f"      🎯 وزن دلالي: {vector.semantic_weight:.3f}")
        print(f"      🧬 وزن سياقي: {vector.contextual_weight:.3f}")
    
    # عرض الإحصائيات
    print(f"\n📈 إحصائيات النظام:")
    print(f"   📊 إجمالي المتجهات: {system.stats['total_vectors']}")
    print(f"   🔤 متجهات عربية: {system.stats['arabic_vectors']}")
    print(f"   🔤 متجهات إنجليزية: {system.stats['english_vectors']}")
    print(f"   ⏱️ وقت المعالجة: {system.stats['processing_time']:.3f}s")
    
    print(f"\n✅ انتهى اختبار نظام المتجهات اللغوية!")
    return system

if __name__ == "__main__":
    test_linguistic_vector_system()
