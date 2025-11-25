"""
الفص الأيمن - Right Brain (الرياضياتي/البصري)
=============================================

يمثل الجانب الرياضياتي/البصري من الدماغ المزدوج.
يتعامل مع:
- المعالجة الرياضياتية
- الحسابات العددية
- التمثيل الشامل (Mother Equation)
- القرارات (Expert + Explorer)

المؤلف: باسل يحيى عبدالله
التاريخ: 2025-11-25
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import numpy as np

from .gse import GSEModel
from .mother_equation import MotherEquation
from .linguistic_equation import LinguisticEquation, KnowledgeBase
from .expert_explorer import BrainSystem, Decision


@dataclass
class MathAnalysis:
    """
    نتيجة التحليل الرياضياتي.
    
    Attributes:
        equations: المعادلات اللغوية
        mother_objects: كائنات المعادلة الأم
        numerical_results: النتائج العددية
        gse_models: نماذج GSE المستخدمة
        decision: القرار من نظام الخبير-المستكشف
        confidence: مستوى الثقة (0-1)
        reasoning: التفسير الرياضياتي
    """
    equations: List[LinguisticEquation] = field(default_factory=list)
    mother_objects: Dict[str, MotherEquation] = field(default_factory=dict)
    numerical_results: Dict[str, float] = field(default_factory=dict)
    gse_models: Dict[str, GSEModel] = field(default_factory=dict)
    decision: Optional[Decision] = None
    confidence: float = 0.5
    reasoning: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """تحويل إلى قاموس"""
        return {
            'equations_count': len(self.equations),
            'objects_count': len(self.mother_objects),
            'numerical_results': self.numerical_results,
            'decision_confidence': self.decision.final_confidence if self.decision else 0.0,
            'confidence': self.confidence,
            'reasoning': self.reasoning
        }


class RightBrain:
    """
    الفص الأيمن من الدماغ المزدوج.
    
    المسؤوليات:
    - معالجة رياضياتية/بصرية
    - حسابات عددية دقيقة
    - تمثيل شامل للكائنات (Mother Equation)
    - قرارات ذكية (Expert + Explorer)
    """
    
    def __init__(self):
        """تهيئة الفص الأيمن"""
        self.brain_system = BrainSystem(expert_weight=0.7, explorer_weight=0.3)
        self.knowledge_base = KnowledgeBase()
        
        # مخزن الكائنات الرياضياتية
        self.mother_equations: Dict[str, MotherEquation] = {}
        self.gse_models: Dict[str, GSEModel] = {}
        
        # إحصائيات
        self.total_analyses = 0
        self.successful_computations = 0
    
    def analyze(self, input_text: str, context: Optional[Dict] = None) -> MathAnalysis:
        """
        تحليل رياضياتي للمدخل.
        
        Args:
            input_text: النص المدخل
            context: السياق الإضافي
        
        Returns:
            MathAnalysis
        """
        self.total_analyses += 1
        
        analysis = MathAnalysis()
        
        # 1. تحليل لغوي → معادلات
        equations = self._parse_to_equations(input_text)
        analysis.equations = equations
        
        # 2. إنشاء/تحديث كائنات المعادلة الأم
        mother_objs = self._create_mother_objects(input_text, equations)
        analysis.mother_objects = mother_objs
        
        # 3. حسابات عددية
        numerical = self._compute_numerical(equations, mother_objs)
        analysis.numerical_results = numerical
        
        # 4. قرار من نظام الخبير-المستكشف
        decision = self.brain_system.decide(input_text, context=numerical)
        analysis.decision = decision
        
        # 5. حساب الثقة
        analysis.confidence = self._calculate_confidence(analysis, decision)
        analysis.reasoning = self._generate_reasoning(analysis)
        
        if analysis.confidence > 0.5:
            self.successful_computations += 1
        
        # metadata
        analysis.metadata = {
            'input_length': len(input_text),
            'context': context or {}
        }
        
        return analysis
    
    def _parse_to_equations(self, text: str) -> List[LinguisticEquation]:
        """
        تحويل النص إلى معادلات لغوية.
        """
        equations = []
        
        # تحليل بسيط - يمكن تحسينه
        if "أكل" in text or "eat" in text.lower():
            # محاولة إنشاء معادلة لغوية
            try:
                from .linguistic_equation import create_simple_equation
                eq = create_simple_equation("أكل", ["شخص", "طعام"])
                if eq:
                    equations.append(eq)
            except:
                pass
        
        return equations
    
    def _create_mother_objects(
        self, 
        text: str, 
        equations: List[LinguisticEquation]
    ) -> Dict[str, MotherEquation]:
        """
        إنشاء/تحديث كائنات المعادلة الأم.
        """
        objects = {}
        
        # استخراج أسماء الكيانات
        entities = self._extract_entity_names(text)
        
        for entity_name in entities:
            if entity_name not in self.mother_equations:
                # إنشاء جديد - MotherEquation يحتاج (id, object_name)
                obj = MotherEquation(f"obj_{entity_name}", entity_name)
                self.mother_equations[entity_name] = obj
            
            objects[entity_name] = self.mother_equations[entity_name]
        
        return objects
    
    def _extract_entity_names(self, text: str) -> List[str]:
        """استخراج أسماء الكيانات"""
        # قائمة بسيطة - يمكن تحسينها بـ NER
        common_names = ["محمد", "أحمد", "فاطمة", "سارة", "علي", "زيد"]
        
        entities = []
        for name in common_names:
            if name in text:
                entities.append(name)
        
        return entities
    
    def _compute_numerical(
        self,
        equations: List[LinguisticEquation],
        mother_objs: Dict[str, MotherEquation]
    ) -> Dict[str, float]:
        """
        حسابات عددية.
        
        Returns:
            قاموس من اسم_الخاصية → القيمة
        """
        results = {}
        
        # حسابات من المعادلات اللغوية
        for eq in equations:
            # استخدام KnowledgeBase لحساب النتائج
            try:
                outcomes = self.knowledge_base.predict_outcome(eq)
                for entity_name, changes in outcomes.items():
                    for state_name, value in changes.items():
                        key = f"{entity_name}.{state_name}"
                        results[key] = value
            except:
                pass
        
        # حسابات من كائنات المعادلة الأم
        for obj_name, obj in mother_objs.items():
            # الحصول على الحالات الحالية
            if hasattr(obj, 'dynamic_states'):
                for state_name, state_value in obj.dynamic_states.items():
                    key = f"{obj_name}.{state_name}"
                    if isinstance(state_value, (int, float)):
                        results[key] = state_value
        
        return results
    
    def _calculate_confidence(
        self, 
        analysis: MathAnalysis,
        decision: Decision
    ) -> float:
        """حساب مستوى الثقة الرياضياتية"""
        base_confidence = 0.5
        
        # زيادة بناءً على عدد المعادلات
        eq_bonus = min(0.2, len(analysis.equations) * 0.1)
        
        # زيادة بناءً على ثقة القرار
        decision_bonus = decision.final_confidence * 0.3 if decision else 0.0
        
        # زيادة بناءً على دقة الحسابات
        numerical_bonus = 0.1 if len(analysis.numerical_results) > 0 else 0.0
        
        total = base_confidence + eq_bonus + decision_bonus + numerical_bonus
        return min(1.0, total)
    
    def _generate_reasoning(self, analysis: MathAnalysis) -> str:
        """توليد تفسير رياضياتي"""
        parts = []
        
        if analysis.equations:
            parts.append(f"تم تحليل {len(analysis.equations)} معادلة لغوية")
        
        if analysis.mother_objects:
            parts.append(f"تتبع {len(analysis.mother_objects)} كائن")
        
        if analysis.numerical_results:
            parts.append(f"حساب {len(analysis.numerical_results)} قيمة عددية")
        
        if analysis.decision:
            parts.append(f"قرار: {analysis.decision.reasoning}")
        
        return " | ".join(parts) if parts else "تحليل رياضياتي بسيط"
    
    def compute_numerical_value(self, expression: str) -> Optional[float]:
        """
        حساب قيمة عددية من تعبير.
        
        Args:
            expression: تعبير رياضياتي
        
        Returns:
            القيمة أو None
        """
        try:
            # حساب بسيط وآمن
            # في الإنتاج، استخدم parser آمن
            result = eval(expression, {"__builtins__": {}}, {})
            if isinstance(result, (int, float)):
                return float(result)
        except:
            pass
        
        return None
    
    def visualize_object(self, obj_name: str) -> Optional[Dict]:
        """
        تصور كائن باستخدام معادلة الشكل (Γ).
        
        Args:
            obj_name: اسم الكائن
        
        Returns:
            تمثيل بصري أو None
        """
        if obj_name in self.mother_equations:
            obj = self.mother_equations[obj_name]
            
            # الحصول على معادلة الشكل
            if hasattr(obj, 'shape_equation') and obj.shape_equation:
                return {
                    'object': obj_name,
                    'shape': obj.shape_equation,
                    'visualization': 'available'
                }
        
        return None
    
    def get_statistics(self) -> Dict[str, Any]:
        """إحصائيات الفص الأيمن"""
        success_rate = (self.successful_computations / self.total_analyses * 100
                       if self.total_analyses > 0 else 0)
        
        brain_stats = self.brain_system.get_statistics()
        
        return {
            'total_analyses': self.total_analyses,
            'successful_computations': self.successful_computations,
            'success_rate': f"{success_rate:.1f}%",
            'mother_objects_count': len(self.mother_equations),
            'gse_models_count': len(self.gse_models),
            'brain_system': brain_stats
        }
