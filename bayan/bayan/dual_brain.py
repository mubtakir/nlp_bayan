"""
الدماغ المزدوج - Dual Brain System
===================================

نظام ثوري يجمع بين التفكير المنطقي والرياضياتي.

الفكرة: فصين يعملان معاً - كل واحد ينظر للمشكلة من زاوية مختلفة،
ثم يتفاوضان ويعززان بعضهما للوصول لحل أفضل.

المؤلف: باسل يحيى عبدالله  
التاريخ: 2025-11-25
"""

from dataclasses import dataclass, field
from typing import Any, Dict, Optional
import time

from .left_brain import LeftBrain, LogicalAnalysis
from .right_brain import RightBrain, MathAnalysis
from .integration_layer import IntegrationLayer, ValidationResult, Agreement


@dataclass
class DualResult:
    """
    النتيجة النهائية من الدماغ المزدوج.
    
    Attributes:
        logical: التحليل المنطقي
        mathematical: التحليل الرياضياتي
        validation: نتيجة التحقق المتبادل
        agreement: الاتفاق المدمج
        final_confidence: الثقة النهائية
        explanation: شرح شامل
        processing_time: وقت المعالجة
    """
    logical: LogicalAnalysis
    mathematical: MathAnalysis
    validation: ValidationResult
    agreement: Agreement
    final_confidence: float
    explanation: str
    processing_time: float
    metadata: Dict = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """تحويل إلى قاموس"""
        return {
            'logical_summary': self.logical.to_dict(),
            'mathematical_summary': self.mathematical.to_dict(),
            'consensus': self.validation.consensus,
            'consensus_level': self.validation.get_consensus_level().arabic_name,
            'final_confidence': self.final_confidence,
            'left_contribution': f"{self.agreement.left_contribution*100:.0f}%",
            'right_contribution': f"{self.agreement.right_contribution*100:.0f}%",
            'explanation': self.explanation,
            'processing_time_ms': round(self.processing_time * 1000, 2),
            'is_valid': self.validation.is_valid
        }
    
    def print_summary(self, language: str = "ar"):
        """طباعة ملخص النتيجة"""
        if language == "ar":
            print("═" * 60)
            print(" نتيجة الدماغ المزدوج")
            print("═" * 60)
            print(f"\n📊 التوافق: {self.validation.consensus*100:.0f}% "
                  f"({self.validation.get_consensus_level().arabic_name})")
            print(f"🧩 مساهمة منطقية: {self.agreement.left_contribution*100:.0f}%")
            print(f"🎨 مساهمة رياضياتية: {self.agreement.right_contribution*100:.0f}%")
            print(f"✨ الثقة النهائية: {self.final_confidence*100:.0f}%")
            print(f"⏱️  وقت المعالجة: {self.processing_time*1000:.2f} ms")
            print(f"\n💡 الشرح: {self.explanation}")
            
            if self.validation.conflicts:
                print(f"\n⚠️  التعارضات: {len(self.validation.conflicts)}")
            if self.validation.agreements:
                print(f"✅ نقاط الاتفاق: {len(self.validation.agreements)}")
        else:
            print("═" * 60)
            print(" Dual Brain Result")
            print("═" * 60)
            print(f"\n📊 Consensus: {self.validation.consensus*100:.0f}%")
            print(f"🧩 Logical contribution: {self.agreement.left_contribution*100:.0f}%")
            print(f"🎨 Mathematical contribution: {self.agreement.right_contribution*100:.0f}%")
            print(f"✨ Final confidence: {self.final_confidence*100:.0f}%")
            print(f"⏱️  Processing time: {self.processing_time*1000:.2f} ms")
            print(f"\n💡 Explanation: {self.explanation}")


class DualBrain:
    """
    الدماغ المزدوج - نظام ذكاء متكامل.
    
    يجمع بين:
    - الفص الأيسر (منطقي): logical_engine + entity_engine
    - الفص الأيمن (رياضياتي): GSE + mother_equation + expert_explorer
    - طبقة التكامل: تنسيق وتفاوض ونقد متبادل
    
    النتيجة: تحليل أعمق وأدق من أي فص بمفرده!
    """
    
    def __init__(self):
        """تهيئة الدماغ المزدوج"""
        # الفصان
        self.left_brain = LeftBrain()
        self.right_brain = RightBrain()
        
        # طبقة التكامل
        self.integration = IntegrationLayer()
        
        # سجل المعالجات
        self.processing_history = []
        self.total_processes = 0
        self.successful_processes = 0
    
    def process(
        self,
        input_text: str,
        context: Optional[Dict] = None,
        debug: bool = False
    ) -> DualResult:
        """
        معالجة مزدوجة للمدخل.
        
        المراحل:
        1. الفص الأيسر يحلل منطقياً
        2. الفص الأيمن يحلل رياضياتياً
        3. التحقق المتبادل
        4. التفاوض والدمج
        5. النتيجة النهائية
        
        Args:
            input_text: النص المدخل
            context: السياق الإضافي
            debug: طباعة معلومات تصحيح
        
        Returns:
            DualResult
        """
        start_time = time.time()
        self.total_processes += 1
        
        if debug:
            print(f"\n🧠 بدء المعالجة المزدوجة: '{input_text}'\n")
        
        # المرحلة 1: التحليل المنطقي
        if debug:
            print("🧩 المرحلة 1: التحليل المنطقي...")
        logical = self.left_brain.analyze(input_text, context)
        if debug:
            print(f"   ✓ الثقة المنطقية: {logical.confidence*100:.0f}%")
            print(f"   ✓ حقائق: {len(logical.facts)}, كيانات: {len(logical.entities)}")
        
        # المرحلة 2: التحليل الرياضياتي
        if debug:
            print("\n🎨 المرحلة 2: التحليل الرياضياتي...")
        mathematical = self.right_brain.analyze(input_text, context)
        if debug:
            print(f"   ✓ الثقة الرياضياتية: {mathematical.confidence*100:.0f}%")
            print(f"   ✓ معادلات: {len(mathematical.equations)}, "
                  f"نتائج عددية: {len(mathematical.numerical_results)}")
        
        # المرحلة 3: التحقق المتبادل
        if debug:
            print("\n🔍 المرحلة 3: التحقق المتبادل...")
        validation = self.integration.cross_validate(logical, mathematical)
        if debug:
            print(f"   ✓ التوافق: {validation.consensus*100:.0f}%")
            print(f"   ✓ {validation.explanation}")
        
        # المرحلة 4: التفاوض
        if debug:
            print("\n🤝 المرحلة 4: التفاوض...")
        agreement = self.integration.negotiate(logical, mathematical, validation)
        if debug:
            print(f"   ✓ {agreement.explanation}")
        
        # المرحلة 5: النتيجة النهائية
        final_confidence = agreement.confidence
        explanation = self._generate_final_explanation(
            logical, mathematical, validation, agreement
        )
        
        processing_time = time.time() - start_time
        
        result = DualResult(
            logical=logical,
            mathematical=mathematical,
            validation=validation,
            agreement=agreement,
            final_confidence=final_confidence,
            explanation=explanation,
            processing_time=processing_time,
            metadata={
                'input_text': input_text,
                'context': context or {}
            }
        )
        
        # حفظ في السجل
        self.processing_history.append(result)
        
        if final_confidence > 0.5:
            self.successful_processes += 1
        
        if debug:
            print(f"\n✨ النتيجة النهائية:")
            print(f"   الثقة: {final_confidence*100:.0f}%")
            print(f"   الوقت: {processing_time*1000:.2f} ms\n")
        
        return result
    
    def _generate_final_explanation(
        self,
        logical: LogicalAnalysis,
        mathematical: MathAnalysis,
        validation: ValidationResult,
        agreement: Agreement
    ) -> str:
        """توليد شرح نهائي شامل"""
        parts = []
        
        # التحليل المنطقي
        if logical.reasoning:
            parts.append(f"منطقياً: {logical.reasoning}")
        
        # التحليل الرياضياتي
        if mathematical.reasoning:
            parts.append(f"رياضياتياً: {mathematical.reasoning}")
        
        # التوافق
        consensus_level = validation.get_consensus_level().arabic_name
        parts.append(f"التوافق: {consensus_level}")
        
        # القرار
        if agreement.explanation:
            parts.append(agreement.explanation)
        
        return " | ".join(parts) if parts else "تحليل مزدوج ناجح"
    
    def get_consensus_level(self) -> float:
        """
        الحصول على متوسط مستوى التوافق للمعالجات الأخيرة.
        
        Returns:
            متوسط التوافق (0-1)
        """
        if not self.processing_history:
            return 0.0
        
        recent = self.processing_history[-10:]  # آخر 10
        avg_consensus = sum(r.validation.consensus for r in recent) / len(recent)
        return avg_consensus
    
    def get_statistics(self) -> Dict[str, Any]:
        """إحصائيات الدماغ المزدوج"""
        success_rate = (self.successful_processes / self.total_processes * 100
                       if self.total_processes > 0 else 0)
        
        left_stats = self.left_brain.get_statistics()
        right_stats = self.right_brain.get_statistics()
        integration_stats = self.integration.get_statistics()
        
        avg_consensus = self.get_consensus_level()
        
        return {
            'total_processes': self.total_processes,
            'successful': self.successful_processes,
            'success_rate': f"{success_rate:.1f}%",
            'average_consensus': f"{avg_consensus*100:.0f}%",
            'left_brain': left_stats,
            'right_brain': right_stats,
            'integration': integration_stats
        }
    
    def reset(self):
        """إعادة تعيين الدماغ"""
        self.processing_history.clear()
        self.total_processes = 0
        self.successful_processes = 0
        
        # يمكن أيضاً إعادة تعيين الفصين وطبقة التكامل
        # لكن نترك المعرفة المكتسبة
