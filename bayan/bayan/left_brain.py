"""
الفص الأيسر - Left Brain (المنطقي)
====================================

يمثل الجانب المنطقي من الدماغ المزدوج.
يتعامل مع:
- المعالجة المنطقية
- القواعد والحقائق
- الكيانات وحالاتها
- الاستنتاج القواعدي

المؤلف: باسل يحيى عبدالله
التاريخ: 2025-11-25
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from .logical_engine import LogicalEngine, Fact, Rule, Term, Predicate
from .entity_engine import EntityEngine


@dataclass
class LogicalAnalysis:
    """
    نتيجة التحليل المنطقي.
    
    Attributes:
        facts: الحقائق المستخرجة
        rules: القواعد المطبقة
        entities: الكيانات المحددة
        queries: الاستعلامات
        confidence: مستوى الثقة (0-1)
        reasoning: التفسير المنطقي
        is_consistent: هل النتيجة متسقة منطقياً؟
    """
    facts: List[Fact] = field(default_factory=list)
    rules: List[Rule] = field(default_factory=list)
    entities: Dict[str, Any] = field(default_factory=dict)
    queries: List[Any] = field(default_factory=list)
    confidence: float = 0.5
    reasoning: str = ""
    is_consistent: bool = True
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """تحويل إلى قاموس"""
        return {
            'facts_count': len(self.facts),
            'rules_count': len(self.rules),
            'entities_count': len(self.entities),
            'confidence': self.confidence,
            'is_consistent': self.is_consistent,
            'reasoning': self.reasoning
        }


class LeftBrain:
    """
    الفص الأيسر من الدماغ المزدوج.
    
    المسؤوليات:
    - معالجة منطقية للغة الطبيعية
    - استنتاج قواعدي
    - إدارة الكيانات
    - التحقق من الاتساق المنطقي
    """
    
    def __init__(self):
        """تهيئة الفص الأيسر"""
        self.logical_engine = LogicalEngine()
        self.entity_engine = EntityEngine(self.logical_engine)
        
        # إحصائيات
        self.total_analyses = 0
        self.successful_analyses = 0
        self.contradictions_found = 0
    
    def analyze(self, input_text: str, context: Optional[Dict] = None) -> LogicalAnalysis:
        """
        تحليل منطقي للمدخل.
        
        Args:
            input_text: النص المدخل
            context: السياق الإضافي
        
        Returns:
            LogicalAnalysis
        """
        self.total_analyses += 1
        
        analysis = LogicalAnalysis()
        
        # 1. استخراج الحقائق من النص
        facts = self._extract_facts(input_text)
        analysis.facts = facts
        
        # 2. تحديد الكيانات
        entities = self._identify_entities(input_text, facts)
        analysis.entities = entities
        
        # 3. استنتاج قواعدي
        inferred_facts = self._apply_rules(facts)
        analysis.facts.extend(inferred_facts)
        
        # 4. التحقق من الاتساق
        is_consistent, reasoning = self._check_consistency(analysis.facts)
        analysis.is_consistent = is_consistent
        analysis.reasoning = reasoning
        
        if not is_consistent:
            self.contradictions_found += 1
            analysis.confidence = 0.0
        else:
            analysis.confidence = self._calculate_confidence(analysis)
            self.successful_analyses += 1
        
        # metadata
        analysis.metadata = {
            'input_length': len(input_text),
            'context': context or {}
        }
        
        return analysis
    
    def _extract_facts(self, text: str) -> List[Fact]:
        """
        استخراج حقائق من النص.
        
        هذا تطبيق بسيط - يمكن تحسينه بـ NLP
        """
        facts = []
        
        # أمثلة بسيطة
        if "جائع" in text or "جوع" in text:
            # fact: state(X, hunger, high)
            # سنستخدم تمثيل مبسط
            facts.append({"type": "state", "entity": None, "property": "hunger", "value": "high"})
        
        if "أكل" in text or "eat" in text.lower():
            facts.append({"type": "action", "action": "eat"})
        
        # يمكن إضافة المزيد من قواعد الاستخراج
        
        return facts
    
    def _identify_entities(self, text: str, facts: List) -> Dict[str, Any]:
        """تحديد الكيانات في النص"""
        entities = {}
        
        # استخراج أسماء بسيط (يمكن استخدام NER)
        words = text.split()
        for word in words:
            # إذا كانت كلمة ت بدأ بحرف كبير (في الإنجليزية)
            # أو أسماء شائعة في العربية
            if word in ["محمد", "أحمد", "فاطمة", "سارة", "علي", "زيد"]:
                if word not in entities:
                    entities[word] = {
                        'type': 'person',
                        'states': {}
                    }
        
        return entities
    
    def _apply_rules(self, facts: List) -> List:
        """تطبيق قواعد الاستنتاج"""
        inferred = []
        
        # قاعدة بسيطة: إذا أكل شخص، يقل جوعه
        has_eat_action = any(f.get('action') == 'eat' for f in facts if f.get('type') == 'action')
        
        if has_eat_action:
            inferred.append({
                'type': 'inference',
                'fact': 'hunger_decreases',
                'confidence': 0.9
            })
        
        return inferred
    
    def _check_consistency(self, facts: List) -> tuple:
        """
        التحقق من الاتساق المنطقي.
        
        Returns:
            (is_consistent, reasoning)
        """
        # فحص تعارضات بسيط
        hunger_states = [f for f in facts if f.get('property') == 'hunger']
        
        if len(hunger_states) > 1:
            # تحقق من التعارض
            values = [f.get('value') for f in hunger_states]
            if 'high' in values and 'low' in values:
                return False, "تعارض: جائع وشبعان في نفس الوقت"
        
        return True, "لا تعارضات منطقية"
    
    def _calculate_confidence(self, analysis: LogicalAnalysis) -> float:
        """حساب مستوى الثقة"""
        base_confidence = 0.5
        
        # زيادة الثقة بناءً على عدد الحقائق
        fact_bonus = min(0.3, len(analysis.facts) * 0.05)
        
        # زيادة إذا كانت الكيانات محددة
        entity_bonus = min(0.2, len(analysis.entities) * 0.1)
        
        total = base_confidence + fact_bonus + entity_bonus
        return min(1.0, total)
    
    def verify_consistency(self, result: Any) -> bool:
        """
        التحقق من اتساق نتيجة خارجية.
        
        Args:
            result: نتيجة من الفص الأيمن
        
        Returns:
            bool
        """
        # تحقق بسيط - يمكن توسيعه
        if isinstance(result, dict):
            # تحقق من القيم المنطقية
            for key, value in result.items():
                if isinstance(value, (int, float)):
                    if value < 0 or value > 1:
                        # قيمة خارج النطاق المنطقي للحالات الضبابية
                        return False
        
        return True
    
    def get_statistics(self) -> Dict[str, Any]:
        """إحصائيات الفص الأيسر"""
        success_rate = (self.successful_analyses / self.total_analyses * 100
                       if self.total_analyses > 0 else 0)
        
        return {
            'total_analyses': self.total_analyses,
            'successful': self.successful_analyses,
            'contradictions_found': self.contradictions_found,
            'success_rate': f"{success_rate:.1f}%"
        }
