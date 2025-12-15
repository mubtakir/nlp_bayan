"""
محرك الاستنباط العكسي - Abduction Engine
==========================================

استدلال عكسي: من النتيجة إلى السبب المحتمل.
يجيب على "لماذا حدث هذا؟"

المكونات:
- HypothesisGenerator: توليد الفرضيات
- CausalReasoner: الاستدلال السببي
- AbductionEngine: المحرك الرئيسي

المطور: باسل يحيى عبدالله
"""

import sys
import os
from typing import List, Dict, Any, Optional, Tuple, Set
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

# Ensure we can import bayan packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from bayan.bayan.istinbat_engine import IstinbatEngine
from bayan.bayan.causal_semantic_network import CausalSemanticNetwork, RelationType


class HypothesisType(Enum):
    """أنواع الفرضيات"""
    DIRECT_CAUSE = "direct_cause"      # سبب مباشر
    INDIRECT_CAUSE = "indirect_cause"  # سبب غير مباشر
    CONDITION = "condition"            # شرط مسبق
    ENABLER = "enabler"                # عامل تمكين
    TRIGGER = "trigger"                # محفز


@dataclass
class Hypothesis:
    """فرضية محتملة"""
    statement: str
    hypothesis_type: HypothesisType
    probability: float  # 0.0 - 1.0
    supporting_evidence: List[str] = field(default_factory=list)
    contradicting_evidence: List[str] = field(default_factory=list)
    explanation: str = ""
    
    def score(self) -> float:
        """حساب درجة الفرضية"""
        support = len(self.supporting_evidence) * 0.1
        contradict = len(self.contradicting_evidence) * 0.1
        return min(1.0, max(0.0, self.probability + support - contradict))
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "statement": self.statement,
            "type": self.hypothesis_type.value,
            "probability": self.probability,
            "score": self.score(),
            "supporting": self.supporting_evidence,
            "contradicting": self.contradicting_evidence,
            "explanation": self.explanation
        }


@dataclass
class AbductionResult:
    """نتيجة الاستنباط العكسي"""
    observation: str
    hypotheses: List[Hypothesis]
    best_explanation: Optional[Hypothesis]
    reasoning_chain: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "observation": self.observation,
            "hypotheses": [h.to_dict() for h in self.hypotheses],
            "best_explanation": self.best_explanation.to_dict() if self.best_explanation else None,
            "reasoning_chain": self.reasoning_chain
        }


class HypothesisGenerator:
    """
    مولد الفرضيات
    
    يولد فرضيات محتملة لتفسير ملاحظة.
    """
    
    def __init__(self, causal_network: Optional[CausalSemanticNetwork] = None):
        self.network = causal_network or CausalSemanticNetwork()
        
        # قاعدة معرفة الأسباب الشائعة
        self.common_causes = {
            "فشل": ["نقص الموارد", "سوء التخطيط", "عدم الخبرة", "ظروف خارجية"],
            "نجاح": ["جهد مستمر", "تخطيط جيد", "موارد كافية", "حظ"],
            "تأخر": ["ازدحام", "مشاكل تقنية", "سوء تقدير الوقت"],
            "زيادة": ["طلب مرتفع", "نقص العرض", "نمو السوق"],
            "انخفاض": ["منافسة", "تغير الأذواق", "مشاكل جودة"],
            "خطأ": ["سوء فهم", "نقص معلومات", "تسرع"],
            "عطل": ["تآكل", "سوء استخدام", "عيب تصنيع"],
        }
    
    def generate(self, observation: str, context: Optional[Dict[str, Any]] = None) -> List[Hypothesis]:
        """توليد فرضيات لملاحظة"""
        hypotheses = []
        
        # 1. البحث في الشبكة السببية
        network_hypotheses = self._search_network(observation)
        hypotheses.extend(network_hypotheses)
        
        # 2. توليد من الأسباب الشائعة
        common_hypotheses = self._generate_from_common(observation)
        hypotheses.extend(common_hypotheses)
        
        # 3. توليد فرضيات سياقية
        if context:
            contextual = self._generate_contextual(observation, context)
            hypotheses.extend(contextual)
        
        # 4. ترتيب حسب الاحتمالية
        hypotheses.sort(key=lambda h: h.probability, reverse=True)
        
        return hypotheses[:10]  # أعلى 10 فرضيات
    
    def _search_network(self, observation: str) -> List[Hypothesis]:
        """البحث في الشبكة السببية"""
        hypotheses = []
        
        # استخراج الكلمات المفتاحية
        keywords = observation.split()
        
        for keyword in keywords:
            # البحث عن علاقات سببية
            try:
                causes = self.network.get_causes(keyword)
                for cause in causes:
                    h = Hypothesis(
                        statement=f"{cause} قد يكون سبب {keyword}",
                        hypothesis_type=HypothesisType.DIRECT_CAUSE,
                        probability=0.7,
                        explanation="مستنتج من الشبكة السببية"
                    )
                    hypotheses.append(h)
            except:
                pass
        
        return hypotheses
    
    def _generate_from_common(self, observation: str) -> List[Hypothesis]:
        """توليد من الأسباب الشائعة"""
        hypotheses = []
        obs_lower = observation.lower()
        
        for effect, causes in self.common_causes.items():
            if effect in obs_lower:
                for cause in causes:
                    h = Hypothesis(
                        statement=cause,
                        hypothesis_type=HypothesisType.DIRECT_CAUSE,
                        probability=0.5,
                        explanation=f"سبب شائع لـ '{effect}'"
                    )
                    hypotheses.append(h)
        
        return hypotheses
    
    def _generate_contextual(self, observation: str, context: Dict[str, Any]) -> List[Hypothesis]:
        """توليد فرضيات سياقية"""
        hypotheses = []
        
        # إذا كان هناك كيانات في السياق
        entities = context.get("entities", {})
        for entity, entity_type in entities.items():
            h = Hypothesis(
                statement=f"قد يكون '{entity}' له علاقة بالحدث",
                hypothesis_type=HypothesisType.CONDITION,
                probability=0.4,
                explanation="مستنتج من السياق"
            )
            hypotheses.append(h)
        
        # الزمن
        if context.get("temporal"):
            h = Hypothesis(
                statement=f"التوقيت قد يكون عاملاً",
                hypothesis_type=HypothesisType.ENABLER,
                probability=0.3,
                explanation="عامل زمني محتمل"
            )
            hypotheses.append(h)
        
        return hypotheses


class CausalReasoner:
    """
    المستدل السببي
    
    يحلل سلاسل السبب والنتيجة.
    """
    
    def __init__(self, engine: Optional[IstinbatEngine] = None):
        self.engine = engine
        self.causal_rules: List[Tuple[str, str]] = []  # (سبب، نتيجة)
        self._init_base_rules()
    
    def _init_base_rules(self):
        """تهيئة القواعد السببية الأساسية"""
        self.causal_rules = [
            ("حرارة", "تمدد"),
            ("برودة", "انكماش"),
            ("ضغط", "انضغاط"),
            ("قوة", "حركة"),
            ("احتكاك", "حرارة"),
            ("ماء", "رطوبة"),
            ("نار", "حرارة"),
            ("كهرباء", "إضاءة"),
            ("تعلم", "معرفة"),
            ("تدريب", "مهارة"),
        ]
    
    def add_rule(self, cause: str, effect: str):
        """إضافة قاعدة سببية"""
        self.causal_rules.append((cause, effect))
    
    def find_causes(self, effect: str) -> List[str]:
        """البحث عن أسباب لنتيجة"""
        causes = []
        effect_lower = effect.lower()
        
        for cause, eff in self.causal_rules:
            if eff.lower() in effect_lower or effect_lower in eff.lower():
                causes.append(cause)
        
        return causes
    
    def find_effects(self, cause: str) -> List[str]:
        """البحث عن نتائج لسبب"""
        effects = []
        cause_lower = cause.lower()
        
        for cau, effect in self.causal_rules:
            if cau.lower() in cause_lower or cause_lower in cau.lower():
                effects.append(effect)
        
        return effects
    
    def build_causal_chain(self, start: str, target: str, max_depth: int = 5) -> Optional[List[str]]:
        """بناء سلسلة سببية من البداية للهدف"""
        visited: Set[str] = set()
        
        def dfs(current: str, path: List[str], depth: int) -> Optional[List[str]]:
            if depth > max_depth:
                return None
            if current.lower() == target.lower():
                return path
            if current in visited:
                return None
            
            visited.add(current)
            
            for cause, effect in self.causal_rules:
                if cause.lower() == current.lower():
                    result = dfs(effect, path + [effect], depth + 1)
                    if result:
                        return result
            
            return None
        
        return dfs(start, [start], 0)
    
    def explain_relation(self, cause: str, effect: str) -> str:
        """شرح العلاقة بين السبب والنتيجة"""
        chain = self.build_causal_chain(cause, effect)
        
        if chain:
            return f"'{cause}' يؤدي إلى '{effect}' عبر: {' → '.join(chain)}"
        else:
            return f"لم أجد علاقة سببية مباشرة بين '{cause}' و '{effect}'"


class AbductionEngine:
    """
    محرك الاستنباط العكسي الموحد
    
    يجمع توليد الفرضيات والاستدلال السببي
    للإجابة على "لماذا حدث هذا؟"
    """
    
    def __init__(self, engine: Optional[IstinbatEngine] = None):
        self.engine = engine or IstinbatEngine()
        self.generator = HypothesisGenerator()
        self.reasoner = CausalReasoner(self.engine)
        self.history: List[AbductionResult] = []
    
    def explain(self, observation: str, context: Optional[Dict[str, Any]] = None) -> AbductionResult:
        """
        تفسير ملاحظة
        
        Args:
            observation: الملاحظة/النتيجة المراد تفسيرها
            context: سياق إضافي
            
        Returns:
            نتيجة الاستنباط مع الفرضيات
        """
        reasoning_chain = []
        reasoning_chain.append(f"الملاحظة: {observation}")
        
        # 1. توليد الفرضيات
        hypotheses = self.generator.generate(observation, context)
        reasoning_chain.append(f"تم توليد {len(hypotheses)} فرضية محتملة")
        
        # 2. تقييم كل فرضية
        for h in hypotheses:
            self._evaluate_hypothesis(h, observation)
        
        # 3. إعادة الترتيب بعد التقييم
        hypotheses.sort(key=lambda h: h.score(), reverse=True)
        
        # 4. اختيار أفضل تفسير
        best = hypotheses[0] if hypotheses else None
        
        if best:
            reasoning_chain.append(f"أفضل تفسير: {best.statement} (ثقة: {best.score():.2f})")
        
        # 5. بناء النتيجة
        result = AbductionResult(
            observation=observation,
            hypotheses=hypotheses,
            best_explanation=best,
            reasoning_chain=reasoning_chain
        )
        
        self.history.append(result)
        return result
    
    def _evaluate_hypothesis(self, hypothesis: Hypothesis, observation: str):
        """تقييم فرضية"""
        # البحث عن أدلة في محرك الاستنباط
        try:
            # البحث في قاعدة المعرفة
            search_results = self.engine.neural_search(hypothesis.statement, top_k=3)
            if search_results:
                hypothesis.supporting_evidence.extend([str(r) for r in search_results[:2]])
                hypothesis.probability += 0.1
        except:
            pass
        
        # البحث عن علاقات سببية
        causes = self.reasoner.find_causes(observation)
        for cause in causes:
            if cause.lower() in hypothesis.statement.lower():
                hypothesis.supporting_evidence.append(f"قاعدة سببية: {cause} → ؟")
                hypothesis.probability += 0.1
    
    def why(self, effect: str) -> str:
        """
        واجهة بسيطة: لماذا حدث هذا؟
        
        مثال: engine.why("انهار المبنى")
        """
        result = self.explain(effect)
        
        if result.best_explanation:
            return f"لأن {result.best_explanation.statement}"
        else:
            return "لا أستطيع تحديد السبب بدقة"
    
    def what_caused(self, effect: str) -> List[str]:
        """ما الذي سبب هذا؟"""
        result = self.explain(effect)
        return [h.statement for h in result.hypotheses[:5]]
    
    def is_valid_explanation(self, cause: str, effect: str) -> Tuple[bool, str]:
        """هل هذا تفسير صحيح؟"""
        chain = self.reasoner.build_causal_chain(cause, effect)
        
        if chain:
            return True, self.reasoner.explain_relation(cause, effect)
        else:
            return False, f"لم أجد علاقة سببية بين '{cause}' و '{effect}'"
    
    def add_causal_knowledge(self, cause: str, effect: str):
        """إضافة معرفة سببية"""
        self.reasoner.add_rule(cause, effect)


# ============ اختبار ============
if __name__ == "__main__":
    print("=" * 50)
    print("اختبار محرك الاستنباط العكسي")
    print("=" * 50)
    
    engine = AbductionEngine()
    
    # إضافة معرفة سببية
    engine.add_causal_knowledge("ماس كهربائي", "حريق")
    engine.add_causal_knowledge("إهمال", "حادث")
    engine.add_causal_knowledge("مطر", "انزلاق")
    
    # اختبار لماذا
    print("\n1. اختبار 'لماذا':")
    print(f"   السؤال: لماذا حدث الحريق؟")
    print(f"   الجواب: {engine.why('حدث الحريق')}")
    
    # اختبار ما الذي سبب
    print("\n2. اختبار 'ما الذي سبب':")
    print(f"   السؤال: ما الذي سبب فشل المشروع؟")
    causes = engine.what_caused("فشل المشروع")
    for i, cause in enumerate(causes, 1):
        print(f"   {i}. {cause}")
    
    # اختبار صحة التفسير
    print("\n3. اختبار صحة التفسير:")
    valid, explanation = engine.is_valid_explanation("مطر", "انزلاق")
    print(f"   هل المطر يسبب الانزلاق؟ {valid}")
    print(f"   التفسير: {explanation}")
    
    print("\n✅ اكتمل الاختبار بنجاح!")
