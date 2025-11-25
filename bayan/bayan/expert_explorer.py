"""
نظام الخبير-المستكشف - Expert-Explorer System
==============================================

نظام ذكي لاتخاذ القرارات يجمع بين الخبرة (المعرفة المجربة)
والاستكشاف (البحث عن حلول جديدة).

يعتمد على ثلاث نظريات:
1. ثنائية الصفر (Zero Duality)
2. تعامد الأضداد (Perpendicular Opposites)
3. نظرية الفتائل (Filament Theory)

مستوحى من: baserah-bayan/brain/expert-explorer-system.bn

المؤلف: باسل يحيى عبدالله
التاريخ: 2025-11-25
"""

import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import random


# ═══════════════════════════════════════════════════════════════
# التعدادات
# ═══════════════════════════════════════════════════════════════

class DecisionType(Enum):
    """نوع القرار"""
    EXPERT_ONLY = "خبير_فقط"           # قرار الخبير فقط
    EXPLORER_ONLY = "مستكشف_فقط"       # قرار المستكشف فقط
    BALANCED = "متوازن"                 # قرار متوازن
    EXPERT_DOMINANT = "خبير_مهيمن"      # الخبير مهيمن
    EXPLORER_DOMINANT = "مستكشف_مهيمن"  # المستكشف مهيمن


class ConfidenceLevel(Enum):
    """مستوى الثقة"""
    VERY_HIGH = ("عالية_جداً", 0.9, 1.0)
    HIGH = ("عالية", 0.7, 0.9)
    MEDIUM = ("متوسطة", 0.5, 0.7)
    LOW = ("منخفضة", 0.3, 0.5)
    VERY_LOW = ("منخفضة_جداً", 0.0, 0.3)
    
    def __init__(self, arabic_name, min_val, max_val):
        self.arabic_name = arabic_name
        self.min_val = min_val
        self.max_val = max_val
    
    @classmethod
    def from_value(cls, value: float):
        """تحديد مستوى الثقة من قيمة"""
        for level in cls:
            if level.min_val <= value < level.max_val:
                return level
        return cls.VERY_LOW


# ═══════════════════════════════════════════════════════════════
# الفئات الأساسية
# ═══════════════════════════════════════════════════════════════

@dataclass
class KnowledgeItem:
    """
    عنصر معرفي في قاعدة معرفة الخبير.
    
    Attributes:
        pattern: النمط الذي يعرفه الخبير
        solution: الحل المرتبط بالنمط
        confidence: مستوى الثقة (0-1)
        usage_count: عدد مرات الاستخدام
        success_rate: معدل النجاح (0-1)
    """
    pattern: str
    solution: Any
    confidence: float = 1.0
    usage_count: int = 0
    success_rate: float = 1.0
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def update_success(self, was_successful: bool):
        """تحديث معدل النجاح"""
        self.usage_count += 1
        # متوسط متحرك
        alpha = 0.1  # معامل التعلم
        self.success_rate = (1 - alpha) * self.success_rate + alpha * (1.0 if was_successful else 0.0)
        self.confidence = self.success_rate


@dataclass
class ExplorationResult:
    """
    نتيجة استكشاف.
    
    Attributes:
        solution: الحل المكتشف
        novelty: مستوى الجدة/الابتكار (0-1)
complexity: مستوى التعقيد (0-1)
        confidence: مستوى الثقة (0-1)
        exploration_path: مسار الاستكشاف
    """
    solution: Any
    novelty: float = 0.5
    complexity: float = 0.5
    confidence: float = 0.5
    exploration_path: List[str] = field(default_factory=list)


@dataclass
class Decision:
    """
    قرار نهائي من نظام Brain.
    
    Attributes:
        solution: الحل المختار
        decision_type: نوع القرار
        expert_confidence: ثقة الخبير
        explorer_confidence: ثقة المستكشف
        final_confidence: الثقة النهائية
        reasoning: التفسير/السبب
    """
    solution: Any
    decision_type: DecisionType
    expert_confidence: float
    explorer_confidence: float
    final_confidence: float
    reasoning: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """تحويل إلى قاموس"""
        return {
            'solution': str(self.solution),
            'type': self.decision_type.value,
            'expert_confidence': self.expert_confidence,
            'explorer_confidence': self.explorer_confidence,
            'final_confidence': self.final_confidence,
            'confidence_level': ConfidenceLevel.from_value(self.final_confidence).arabic_name,
            'reasoning': self.reasoning,
            'metadata': self.metadata
        }


# ═══════════════════════════════════════════════════════════════
# النظريات الثلاث
# ═══════════════════════════════════════════════════════════════

class ZeroDualityTheory:
    """
    نظرية ثنائية الصفر.
    
    المبدأ: كل قيمة لها ضد، ومجموع التأثيرات = 0 في التوازن المثالي.
    التطبيق: حساب التوازن بين الإيجابي والسلبي.
    """
    
    @staticmethod
    def calculate_balance(positive: float, negative: float) -> float:
        """
        حساب عامل التوازن.
        
        كلما اقترب من 0، كان التوازن أفضل.
        """
        return abs(positive + negative - 1.0)
    
    @staticmethod
    def adjust_confidence(confidence: float, positive: float, negative: float) -> float:
        """
        تعديل الثقة بناءً على التوازن.
        """
        balance_factor = ZeroDualityTheory.calculate_balance(positive, negative)
        # كلما كان التوازن أفضل (قريب من 0)، كانت الثقة أعلى
        adjusted = confidence * (1 - balance_factor)
        return max(0.0, min(1.0, adjusted))


class PerpendicularOppositesTheory:
    """
    نظرية تعامد الأضداد.
    
    المبدأ: كل اتجاه له ضد متعامد.
    التطبيق: استكشاف اتجاهات جديدة متعامدة على الاتجاه الحالي.
    """
    
    @staticmethod
    def get_perpendicular_direction(direction: np.ndarray) -> np.ndarray:
        """
        الحصول على اتجاه متعامد.
        
        في 2D: perpendicular of (x, y) = (-y, x) or (y, -x)
        """
        if len(direction) == 2:
            # 2D rotation by 90 degrees
            return np.array([-direction[1], direction[0]])
        else:
            # للأبعاد الأعلى: اختر محور عشوائي متعامد
            random_vector = np.random.randn(len(direction))
            # جعله متعامداً باستخدام Gram-Schmidt
            perpendicular = random_vector - np.dot(random_vector, direction) / np.dot(direction, direction) * direction
            # تطبيع
            norm = np.linalg.norm(perpendicular)
            return perpendicular / norm if norm > 0 else random_vector
    
    @staticmethod
    def explore_perpendicular(primary_solution: np.ndarray, exploration_ratio: float = 0.3) -> np.ndarray:
        """
        استكشاف في اتجاه متعامد.
        
        Args:
            primary_solution: الحل الأساسي
            exploration_ratio: نسبة الاستكشاف (0-1)
        
        Returns:
            حل جديد
        """
        perpendicular = PerpendicularOppositesTheory.get_perpendicular_direction(primary_solution)
        return (1 - exploration_ratio) * primary_solution + exploration_ratio * perpendicular


class FilamentTheory:
    """
    نظرية الفتائل.
    
    المبدأ: النتيجة المعقدة مبنية من فتائل بسيطة (sigmoid + linear).
    التطبيق: بناء القرارات المعقدة من مكونات بسيطة.
    """
    
    @staticmethod
    def sigmoid(x: float, k: float = 1.0, x0: float = 0.0) -> float:
        """دالة sigmoid بسيطة"""
        return 1.0 / (1.0 + np.exp(-k * (x - x0)))
    
    @staticmethod
    def linear(x: float, slope: float = 1.0, intercept: float = 0.0) -> float:
        """دالة خطية بسيطة"""
        return slope * x + intercept
    
    @staticmethod
    def combine_filaments(components: List[Tuple[str, float, Dict]], x: float) -> float:
        """
        دمج عدة فتائل.
        
        Args:
            components: قائمة من (type, weight, params)
                type: 'sigmoid' أو 'linear'
                weight: وزن المكون
                params: معاملات (k, x0 للسيغمويد، slope, intercept للخطي)
            x: المدخل
        
        Returns:
            الناتج المجمع
        """
        result = 0.0
        for comp_type, weight, params in components:
            if comp_type == 'sigmoid':
                result += weight * FilamentTheory.sigmoid(x, params.get('k', 1.0), params.get('x0', 0.0))
            elif comp_type == 'linear':
                result += weight * FilamentTheory.linear(x, params.get('slope', 1.0), params.get('intercept', 0.0))
        return result


# ═══════════════════════════════════════════════════════════════
# نظام الخبير
# ═══════════════════════════════════════════════════════════════

class ExpertSystem:
    """
    نظام الخبير - يدير المعرفة المجربة.
    
    المسؤوليات:
    - إدارة قاعدة المعرفة
    - البحث عن حلول مجربة
    - تقييم الثقة بناءً على الخبرة السابقة
    """
    
    def __init__(self, confidence_threshold: float = 0.7):
        """
        Args:
            confidence_threshold: عتبة الثقة للقبول
        """
        self.knowledge_base: Dict[str, KnowledgeItem] = {}
        self.confidence_threshold = confidence_threshold
        self.total_queries = 0
        self.successful_matches = 0
    
    def add_knowledge(self, pattern: str, solution: Any, confidence: float = 1.0):
        """إضافة معرفة جديدة"""
        self.knowledge_base[pattern] = KnowledgeItem(
            pattern=pattern,
            solution=solution,
            confidence=confidence
        )
    
    def find_solution(self, query: str) -> Optional[Tuple[Any, float]]:
        """
        البحث عن حل في قاعدة المعرفة.
        
        Args:
            query: الاستعلام
        
        Returns:
            (solution, confidence) أو None
        """
        self.total_queries += 1
        
        # بحث مباشر
        if query in self.knowledge_base:
            item = self.knowledge_base[query]
            self.successful_matches += 1
            return (item.solution, item.confidence)
        
        # بحث تقريبي (similarity-based)
        # يمكن تحسينه باستخدام embedding أو fuzzy matching
        best_match = None
        best_confidence = 0.0
        
        for pattern, item in self.knowledge_base.items():
            # حساب التشابه البسيط
            similarity = self._calculate_similarity(query, pattern)
            adjusted_confidence = item.confidence * similarity
            
            if adjusted_confidence > best_confidence and adjusted_confidence >= self.confidence_threshold:
                best_match = item.solution
                best_confidence = adjusted_confidence
        
        if best_match:
            self.successful_matches += 1
        
        return (best_match, best_confidence) if best_match else None
    
    def _calculate_similarity(self, str1: str, str2: str) -> float:
        """حساب التشابه بين نصين (بسيط جداً)"""
        # Jaccard similarity على مستوى الكلمات
        words1 = set(str1.lower().split())
        words2 = set(str2.lower().split())
        
        intersection = words1 & words2
        union = words1 | words2
        
        return len(intersection) / len(union) if union else 0.0
    
    def update_knowledge(self, pattern: str, was_successful: bool):
        """تحديث المعرفة بناءً على النتيجة"""
        if pattern in self.knowledge_base:
            self.knowledge_base[pattern].update_success(was_successful)
    
    def get_success_rate(self) -> float:
        """معدل النجاح الإجمالي"""
        return self.successful_matches / self.total_queries if self.total_queries > 0 else 0.0


# ═══════════════════════════════════════════════════════════════
# نظام المستكشف
# ═══════════════════════════════════════════════════════════════

class ExplorerSystem:
    """
    نظام المستكشف - يكتشف حلول جديدة.
    
    المسؤوليات:
    - استكشاف اتجاهات جديدة
    - تقييم جدة الحلول
    - استخدام النظريات للاستكشاف الذكي
    """
    
    def __init__(self, exploration_rate: float = 0.3):
        """
        Args:
            exploration_rate: معدل الاستكشاف (0-1)
        """
        self.exploration_rate = exploration_rate
        self.discovered_solutions: List[ExplorationResult] = []
        self.novelty_threshold = 0.5
    
    def explore(self, context: Any, expert_solution: Optional[Any] = None) -> ExplorationResult:
        """
        استكشاف حل جديد.
        
        Args:
            context: السياق
            expert_solution: حل الخبير (إن وُجد)
        
        Returns:
            ExplorationResult
        """
        if expert_solution is not None and isinstance(expert_solution, np.ndarray):
            # استكشاف متعامد على حل الخبير
            new_solution = PerpendicularOppositesTheory.explore_perpendicular(
                expert_solution,
                self.exploration_rate
            )
        else:
            # استكشاف عشوائي
            new_solution = self._random_exploration(context)
        
        novelty = self._calculate_novelty(new_solution)
        confidence = self._calculate_exploration_confidence(novelty)
        
        result = ExplorationResult(
            solution=new_solution,
            novelty=novelty,
            confidence=confidence,
            exploration_path=["perpendicular" if expert_solution is not None else "random"]
        )
        
        self.discovered_solutions.append(result)
        return result
    
    def _random_exploration(self, context: Any) -> Any:
        """استكشاف عشوائي"""
        # استكشاف بسيط - يمكن تحسينه
        return np.random.randn(3) * 0.5
    
    def _calculate_novelty(self, solution: Any) -> float:
        """حساب جدة الحل"""
        if not self.discovered_solutions:
            return 1.0  # أول حل دائماً جديد
        
        # قياس المسافة من الحلول السابقة
        if isinstance(solution, np.ndarray):
            min_distance = float('inf')
            for prev in self.discovered_solutions[-10:]:  # آخر 10 حلول
                if isinstance(prev.solution, np.ndarray):
                    distance = np.linalg.norm(solution - prev.solution)
                    min_distance = min(min_distance, distance)
            
            # تحويل المسافة إلى جدة (0-1)
            novelty = min(1.0, min_distance / 2.0)
            return novelty
        
        return 0.5  # افتراضي
    
    def _calculate_exploration_confidence(self, novelty: float) -> float:
        """حساب ثقة الاستكشاف"""
        # الثقة تعتمد على الجدة والخبرة السابقة
        base_confidence = 0.5
        novelty_bonus = novelty * 0.3
        return min(1.0, base_confidence + novelty_bonus)


# ═══════════════════════════════════════════════════════════════
# نظام الدماغ (Brain)
# ═══════════════════════════════════════════════════════════════

class BrainSystem:
    """
    نظام الدماغ - ينسق بين الخبير والمستكشف.
    
    المسؤوليات:
    - تلقي المدخلات
    - استشارة الخبير والمستكشف
    - اتخاذ القرار النهائي
    - التعلم من النتائج
    """
    
    def __init__(
        self,
        expert_weight: float = 0.7,
        explorer_weight: float = 0.3
    ):
        """
        Args:
            expert_weight: وزن الخبير
            explorer_weight: وزن المستكشف
        """
        self.expert = ExpertSystem()
        self.explorer = ExplorerSystem()
        self.expert_weight = expert_weight
        self.explorer_weight = explorer_weight
        self.decision_history: List[Decision] = []
    
    def decide(self, query: str, context: Any = None) -> Decision:
        """
        اتخاذ قرار.
        
        Args:
            query: الاستعلام/المشكلة
            context: السياق الإضافي
        
        Returns:
            Decision
        """
        # 1. استشارة الخبير
        expert_result = self.expert.find_solution(query)
        expert_solution, expert_confidence = expert_result if expert_result else (None, 0.0)
        
        # 2. استشارة المستكشف
        explorer_result = self.explorer.explore(context, expert_solution)
        explorer_solution = explorer_result.solution
        explorer_confidence = explorer_result.confidence
        
        # 3. اتخاذ القرار النهائي
        decision = self._make_final_decision(
            query,
            expert_solution, expert_confidence,
            explorer_solution, explorer_confidence
        )
        
        self.decision_history.append(decision)
        return decision
    
    def _make_final_decision(
        self,
        query: str,
        expert_solution: Any, expert_confidence: float,
        explorer_solution: Any, explorer_confidence: float
    ) -> Decision:
        """اتخاذ القرار النهائي"""
        
        # تطبيق نظرية ثنائية الصفر
        balance = ZeroDualityTheory.calculate_balance(
            expert_confidence,
            1.0 - expert_confidence
        )
        
        # تعديل الثقة
        adjusted_expert_conf = ZeroDualityTheory.adjust_confidence(
            expert_confidence,
            expert_confidence,
            1.0 - expert_confidence
        )
        
        # حساب الثقة النهائية
        final_confidence = (
            self.expert_weight * adjusted_expert_conf +
            self.explorer_weight * explorer_confidence
        )
        
        # اختيار الحل
        if expert_confidence >= 0.8:
            # ثقة عالية من الخبير
            decision_type = DecisionType.EXPERT_DOMINANT
            final_solution = expert_solution
            reasoning = "حل الخبير موثوق (ثقة عالية)"
        elif explorer_confidence >= 0.7:
            # استكشاف واعد
            decision_type = DecisionType.EXPLORER_DOMINANT
            final_solution = explorer_solution
            reasoning = "حل مستكشف جديد واعد"
        elif expert_solution is not None:
            # توازن
            decision_type = DecisionType.BALANCED
            final_solution = expert_solution
            reasoning = "توازن بين الخبرة والاستكشاف"
        else:
            # استكشاف فقط
            decision_type = DecisionType.EXPLORER_ONLY
            final_solution = explorer_solution
            reasoning = "لا معرفة سابقة - استكشاف بحت"
        
        return Decision(
            solution=final_solution,
            decision_type=decision_type,
            expert_confidence=expert_confidence,
            explorer_confidence=explorer_confidence,
            final_confidence=final_confidence,
            reasoning=reasoning,
            metadata={'query': query, 'balance': balance}
        )
    
    def learn(self, query: str, was_successful: bool):
        """التعلم من النتيجة"""
        self.expert.update_knowledge(query, was_successful)
    
    def get_statistics(self) -> Dict[str, Any]:
        """إحصائيات النظام"""
        return {
            'total_decisions': len(self.decision_history),
            'expert_success_rate': self.expert.get_success_rate(),
            'expert_weight': self.expert_weight,
            'explorer_weight': self.explorer_weight,
            'average_confidence': (
                sum(d.final_confidence for d in self.decision_history) / len(self.decision_history)
                if self.decision_history else 0.0
            )
        }
