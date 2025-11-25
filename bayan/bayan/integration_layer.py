"""
طبقة التكامل - Integration Layer
==================================

تنسق بين الفص الأيسر (منطقي) والفص الأيمن (رياضياتي).

المسؤوليات:
- التحقق المتبادل (Cross-Validation)
- التفاوض للوصول لحل مُجمع
- حل التعارضات
- التعزيز المتبادل

المؤلف: باسل يحيى عبدالله
التاريخ: 2025-11-25
"""

from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Tuple
from enum import Enum

from .left_brain import LogicalAnalysis
from .right_brain import MathAnalysis


class ConsensusLevel(Enum):
    """مستوى التوافق بين الفصين"""
    FULL_AGREEMENT = ("اتفاق_كامل", 0.9, 1.0)
    HIGH_AGREEMENT = ("اتفاق_عالي", 0.7, 0.9)
    PARTIAL_AGREEMENT = ("اتفاق_جزئي", 0.5, 0.7)
    LOW_AGREEMENT = ("اتفاق_منخفض", 0.3, 0.5)
    DISAGREEMENT = ("اختلاف", 0.0, 0.3)
    
    def __init__(self, arabic_name, min_val, max_val):
        self.arabic_name = arabic_name
        self.min_val = min_val
        self.max_val = max_val
    
    @classmethod
    def from_value(cls, value: float):
        """تحديد مستوى التوافق من قيمة"""
        for level in cls:
            if level.min_val <= value < level.max_val:
                return level
        return cls.DISAGREEMENT


@dataclass
class ValidationResult:
    """
    نتيجة التحقق المتبادل.
    
    Attributes:
        is_valid: هل النتائج صحيحة؟
        consensus: مستوى التوافق
        conflicts: قائمة التعارضات
        agreements: قائمة نقاط الاتفاق
        explanation: شرح النتيجة
    """
    is_valid: bool
    consensus: float
    conflicts: list = field(default_factory=list)
    agreements: list = field(default_factory=list)
    explanation: str = ""
    
    def get_consensus_level(self) -> ConsensusLevel:
        """الحصول على مستوى التوافق"""
        return ConsensusLevel.from_value(self.consensus)


@dataclass
class Agreement:
    """
    اتفاق بين الفصين.
    
    Attributes:
        solution: الحل المتفق عليه
        left_contribution: مساهمة الفص الأيسر
        right_contribution: مساهمة الفص الأيمن
        confidence: مستوى الثقة في الاتفاق
        explanation: شرح الاتفاق
    """
    solution: Any
    left_contribution: float  # 0-1
    right_contribution: float  # 0-1
    confidence: float
    explanation: str
    metadata: Dict = field(default_factory=dict)


class IntegrationLayer:
    """
    طبقة التكامل بين الفصين.
    
    تنسق بين المنطق والرياضيات لتحقيق نتائج أفضل.
    """
    
    def __init__(self):
        """تهيئة طبقة التكامل"""
        self.integration_history = []
        self.total_integrations = 0
        self.successful_integrations = 0
        self.conflicts_resolved = 0
    
    def cross_validate(
        self,
        logical: LogicalAnalysis,
        mathematical: MathAnalysis
    ) -> ValidationResult:
        """
        التحقق المتبادل بين النتائج المنطقية والرياضياتية.
        
        Args:
            logical: التحليل المنطقي
            mathematical: التحليل الرياضياتي
        
        Returns:
            ValidationResult
        """
        conflicts = []
        agreements = []
        
        # 1. التحقق من الاتساق المنطقي للنتائج الرياضياتية
        if not logical.is_consistent:
            conflicts.append({
                'type': 'logical_inconsistency',
                'description': logical.reasoning
            })
        
        # 2. التحقق من صحة الحسابات العددية
        for key, value in mathematical.numerical_results.items():
            # تحقق من النطاق المنطقي
            if value < 0 or value > 1:
                # قيمة خارج نطاق الحالات الضبابية
                conflicts.append({
                    'type': 'numerical_out_of_range',
                    'key': key,
                    'value': value
                })
            else:
                agreements.append({
                    'type': 'valid_numerical',
                    'key': key,
                    'value': value
                })
        
        # 3. مقارنة مستويات الثقة
        conf_diff = abs(logical.confidence - mathematical.confidence)
        if conf_diff < 0.3:
            agreements.append({
                'type': 'confidence_agreement',
                'left': logical.confidence,
                'right': mathematical.confidence
            })
        else:
            conflicts.append({
                'type': 'confidence_mismatch',
                'left': logical.confidence,
                'right': mathematical.confidence,
                'difference': conf_diff
            })
        
        # حساب مستوى التوافق
        total_points = len(conflicts) + len(agreements)
        if total_points == 0:
            consensus = 0.5  # افتراضي
        else:
            consensus = len(agreements) / total_points
        
        is_valid = len(conflicts) == 0
        
        # شرح
        explanation = self._generate_validation_explanation(
            is_valid, consensus, conflicts, agreements
        )
        
        return ValidationResult(
            is_valid=is_valid,
            consensus=consensus,
            conflicts=conflicts,
            agreements=agreements,
            explanation=explanation
        )
    
    def negotiate(
        self,
        logical: LogicalAnalysis,
        mathematical: MathAnalysis,
        validation: ValidationResult
    ) -> Agreement:
        """
        التفاوض بين الفصين للوصول لحل مُجمع.
        
        Args:
            logical: التحليل المنطقي
            mathematical: التحليل الرياضياتي
            validation: نتيجة التحقق المتبادل
        
        Returns:
            Agreement
        """
        self.total_integrations += 1
        
        # حساب مساهمة كل فص
        left_weight = logical.confidence
        right_weight = mathematical.confidence
        
        # تعديل الأوزان بناءً على التوافق
        if validation.consensus > 0.7:
            # توافق عالي - نثق في كليهما
            left_contribution = left_weight / (left_weight + right_weight)
            right_contribution = right_weight / (left_weight + right_weight)
        elif validation.consensus < 0.3:
            # اختلاف - نحتاج استراتيجية أخرى
            # نختار الأكثر ثقة
            if left_weight > right_weight:
                left_contribution = 0.8
                right_contribution = 0.2
            else:
                left_contribution = 0.2
                right_contribution = 0.8
        else:
            # توافق متوسط - توزيع متوازن
            left_contribution = 0.5
            right_contribution = 0.5
        
        # دمج الحلول
        solution = self._synthesize_solution(
            logical, mathematical, 
            left_contribution, right_contribution
        )
        
        # حساب الثقة النهائية
        final_confidence = (
            left_contribution * logical.confidence +
            right_contribution * mathematical.confidence
        ) * validation.consensus
        
        # شرح
        explanation = self._generate_agreement_explanation(
            left_contribution, right_contribution, 
            final_confidence, validation
        )
        
        if final_confidence > 0.6:
            self.successful_integrations += 1
        
        return Agreement(
            solution=solution,
            left_contribution=left_contribution,
            right_contribution=right_contribution,
            confidence=final_confidence,
            explanation=explanation,
            metadata={
                'consensus_level': validation.get_consensus_level().arabic_name
            }
        )
    
    def resolve_conflict(self, conflict: Dict) -> Optional[Dict]:
        """
        حل تعارض محدد.
        
        Args:
            conflict: التعارض
        
        Returns:
            الحل أو None
        """
        conflict_type = conflict.get('type')
        
        if conflict_type == 'numerical_out_of_range':
            # تصحيح القيم خارج النطاق
            value = conflict.get('value', 0)
            corrected = max(0.0, min(1.0, value))  # قص إلى [0, 1]
            
            self.conflicts_resolved += 1
            
            return {
                'type': 'correction',
                'original': value,
                'corrected': corrected,
                'method': 'clipping'
            }
        
        elif conflict_type == 'confidence_mismatch':
            # استخدام المتوسط
            left = conflict.get('left', 0.5)
            right = conflict.get('right', 0.5)
            average = (left + right) / 2
            
            self.conflicts_resolved += 1
            
            return {
                'type': 'averaging',
                'result': average
            }
        
        # تعارضات أخرى - لم يُحل
        return None
    
    def _synthesize_solution(
        self,
        logical: LogicalAnalysis,
        mathematical: MathAnalysis,
        left_weight: float,
        right_weight: float
    ) -> Dict:
        """دمج الحلول من الفصين"""
        solution = {
            'logical_components': {
                'facts': logical.facts,
                'entities': list(logical.entities.keys()),
                'reasoning': logical.reasoning
            },
            'mathematical_components': {
                'numerical_results': mathematical.numerical_results,
                'objects': list(mathematical.mother_objects.keys()),
                'reasoning': mathematical.reasoning
            },
            'weights': {
                'logical': left_weight,
                'mathematical': right_weight
            }
        }
        
        return solution
    
    def _generate_validation_explanation(
        self,
        is_valid: bool,
        consensus: float,
        conflicts: list,
        agreements: list
    ) -> str:
        """توليد شرح للتحقق"""
        if is_valid:
            return (f"التحقق ناجح ✓ | التوافق: {consensus*100:.0f}% | "
                   f"اتفاقات: {len(agreements)}")
        else:
            return (f"تعارضات: {len(conflicts)} | التوافق: {consensus*100:.0f}% | "
                   f"اتفاقات: {len(agreements)}")
    
    def _generate_agreement_explanation(
        self,
        left: float,
        right: float,
        confidence: float,
        validation: ValidationResult
    ) -> str:
        """توليد شرح للاتفاق"""
        consensus_level = validation.get_consensus_level().arabic_name
        
        return (f"مساهمة منطقية: {left*100:.0f}% | "
               f"مساهمة رياضياتية: {right*100:.0f}% | "
               f"الثقة النهائية: {confidence*100:.0f}% | "
               f"التوافق: {consensus_level}")
    
    def get_statistics(self) -> Dict:
        """إحصائيات التكامل"""
        success_rate = (self.successful_integrations / self.total_integrations * 100
                       if self.total_integrations > 0 else 0)
        
        return {
            'total_integrations': self.total_integrations,
            'successful': self.successful_integrations,
            'conflicts_resolved': self.conflicts_resolved,
            'success_rate': f"{success_rate:.1f}%"
        }
