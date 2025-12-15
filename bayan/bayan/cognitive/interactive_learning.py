"""
التعلم التفاعلي - Interactive Learning
======================================

نظام يتعلم حقائق وقواعد جديدة من المحادثات.

المكونات:
- FactExtractor: استخراج الحقائق من النصوص
- RuleInducer: استنباط قواعد جديدة
- LearningAgent: وكيل التعلم الشامل

المطور: باسل يحيى عبدالله
"""

import sys
import os
import re
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

# Ensure we can import bayan packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from bayan.bayan.istinbat_engine import IstinbatEngine
from bayan.bayan.logical_engine import Fact, Predicate, Term, Rule


class FactType(Enum):
    """أنواع الحقائق"""
    DEFINITION = "definition"      # X هو Y
    PROPERTY = "property"          # X له خاصية Y
    RELATION = "relation"          # X علاقة Y
    CAUSATION = "causation"        # X يسبب Y
    TEMPORAL = "temporal"          # X قبل/بعد Y
    LOCATION = "location"          # X في Y


@dataclass
class ExtractedFact:
    """حقيقة مستخرجة"""
    text: str
    fact_type: FactType
    subject: str
    predicate: str
    object: Optional[str]
    confidence: float
    source: str
    timestamp: datetime = field(default_factory=datetime.now)
    
    def to_logical_fact(self) -> Fact:
        """تحويل لحقيقة منطقية"""
        if self.object:
            return Fact(Predicate(self.predicate, [Term(self.subject), Term(self.object)]))
        else:
            return Fact(Predicate(self.predicate, [Term(self.subject)]))
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "text": self.text,
            "type": self.fact_type.value,
            "subject": self.subject,
            "predicate": self.predicate,
            "object": self.object,
            "confidence": self.confidence,
            "source": self.source,
            "timestamp": self.timestamp.isoformat()
        }


@dataclass
class InducedRule:
    """قاعدة مستنبطة"""
    condition: str
    conclusion: str
    support: int  # عدد الأمثلة الداعمة
    confidence: float
    examples: List[str] = field(default_factory=list)
    
    def to_logical_rule(self) -> Rule:
        """تحويل لقاعدة منطقية"""
        # تحليل بسيط: إذا X ف Y
        cond_pred = Predicate(self.condition, [Term("X")])
        conc_pred = Predicate(self.conclusion, [Term("X")])
        return Rule(head=conc_pred, body=[cond_pred])


class FactExtractor:
    """
    مستخرج الحقائق من النصوص
    
    يستخدم أنماط لغوية لاستخراج الحقائق.
    """
    
    def __init__(self):
        # أنماط الاستخراج
        self.patterns = {
            FactType.DEFINITION: [
                r"(.+?)\s+هو\s+(.+)",
                r"(.+?)\s+هي\s+(.+)",
                r"(.+?)\s+يعني\s+(.+)",
                r"(.+?)\s+عبارة عن\s+(.+)",
                r"تعريف\s+(.+?)\s*:\s*(.+)",
            ],
            FactType.PROPERTY: [
                r"(.+?)\s+له\s+(.+)",
                r"(.+?)\s+لها\s+(.+)",
                r"(.+?)\s+يتميز بـ?\s*(.+)",
                r"(.+?)\s+يتصف بـ?\s*(.+)",
                r"خصائص\s+(.+?)\s*:\s*(.+)",
            ],
            FactType.RELATION: [
                r"(.+?)\s+مثل\s+(.+)",
                r"(.+?)\s+يشبه\s+(.+)",
                r"(.+?)\s+جزء من\s+(.+)",
                r"(.+?)\s+نوع من\s+(.+)",
                r"(.+?)\s+ينتمي لـ?\s*(.+)",
            ],
            FactType.CAUSATION: [
                r"(.+?)\s+يسبب\s+(.+)",
                r"(.+?)\s+يؤدي إلى\s+(.+)",
                r"بسبب\s+(.+?)\s+يحدث\s+(.+)",
                r"إذا\s+(.+?)\s+فإن\s+(.+)",
                r"(.+?)\s+نتيجة\s+(.+)",
            ],
            FactType.TEMPORAL: [
                r"(.+?)\s+قبل\s+(.+)",
                r"(.+?)\s+بعد\s+(.+)",
                r"(.+?)\s+أثناء\s+(.+)",
                r"(.+?)\s+عندما\s+(.+)",
            ],
            FactType.LOCATION: [
                r"(.+?)\s+في\s+(.+)",
                r"(.+?)\s+على\s+(.+)",
                r"(.+?)\s+تحت\s+(.+)",
                r"(.+?)\s+فوق\s+(.+)",
                r"يوجد\s+(.+?)\s+في\s+(.+)",
            ]
        }
        
        # تحويل الأنماط لقواسم
        self.compiled_patterns = {
            fact_type: [re.compile(p, re.UNICODE) for p in patterns]
            for fact_type, patterns in self.patterns.items()
        }
    
    def extract(self, text: str, source: str = "conversation") -> List[ExtractedFact]:
        """استخراج الحقائق من نص"""
        facts = []
        
        # تقسيم النص لجمل
        sentences = self._split_sentences(text)
        
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 5:
                continue
            
            for fact_type, patterns in self.compiled_patterns.items():
                for pattern in patterns:
                    match = pattern.search(sentence)
                    if match:
                        subject = match.group(1).strip()
                        obj = match.group(2).strip() if match.lastindex >= 2 else None
                        
                        # تحديد المسند بناءً على نوع الحقيقة
                        predicate = self._get_predicate(fact_type, pattern.pattern)
                        
                        fact = ExtractedFact(
                            text=sentence,
                            fact_type=fact_type,
                            subject=subject,
                            predicate=predicate,
                            object=obj,
                            confidence=self._calculate_confidence(sentence, match),
                            source=source
                        )
                        facts.append(fact)
                        break  # خذ أول تطابق فقط
        
        return facts
    
    def _split_sentences(self, text: str) -> List[str]:
        """تقسيم النص لجمل"""
        # فواصل الجمل العربية والإنجليزية
        sentences = re.split(r'[.!?،؛\n]', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def _get_predicate(self, fact_type: FactType, pattern: str) -> str:
        """تحديد المسند من نوع الحقيقة"""
        predicates = {
            FactType.DEFINITION: "is_a",
            FactType.PROPERTY: "has_property",
            FactType.RELATION: "related_to",
            FactType.CAUSATION: "causes",
            FactType.TEMPORAL: "temporal_relation",
            FactType.LOCATION: "located_at"
        }
        return predicates.get(fact_type, "unknown_relation")
    
    def _calculate_confidence(self, sentence: str, match) -> float:
        """حساب الثقة في الاستخراج"""
        # الثقة تعتمد على:
        # 1. طول التطابق نسبة للجملة
        # 2. وجود كلمات مؤكدة
        
        match_ratio = len(match.group(0)) / len(sentence)
        
        # كلمات تزيد الثقة
        certainty_words = ["دائماً", "حتماً", "بالتأكيد", "فعلاً", "بالضبط"]
        uncertainty_words = ["ربما", "قد", "يمكن", "محتمل", "تقريباً"]
        
        confidence = 0.7 * match_ratio + 0.3
        
        for word in certainty_words:
            if word in sentence:
                confidence += 0.05
        
        for word in uncertainty_words:
            if word in sentence:
                confidence -= 0.1
        
        return max(0.1, min(1.0, confidence))


class RuleInducer:
    """
    مستنبط القواعد
    
    يستنبط قواعد عامة من مجموعة حقائق.
    """
    
    def __init__(self):
        self.fact_history: List[ExtractedFact] = []
        self.induced_rules: List[InducedRule] = []
        self.min_support = 2  # الحد الأدنى من الأمثلة لاستنباط قاعدة
    
    def add_fact(self, fact: ExtractedFact):
        """إضافة حقيقة للتحليل"""
        self.fact_history.append(fact)
        self._try_induce_rules()
    
    def add_facts(self, facts: List[ExtractedFact]):
        """إضافة مجموعة حقائق"""
        self.fact_history.extend(facts)
        self._try_induce_rules()
    
    def _try_induce_rules(self):
        """محاولة استنباط قواعد جديدة"""
        # تجميع الحقائق حسب النوع والمسند
        grouped = {}
        for fact in self.fact_history:
            key = (fact.fact_type, fact.predicate)
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(fact)
        
        # البحث عن أنماط متكررة
        for (fact_type, predicate), facts in grouped.items():
            if len(facts) >= self.min_support:
                rule = self._induce_from_group(fact_type, predicate, facts)
                if rule and not self._rule_exists(rule):
                    self.induced_rules.append(rule)
    
    def _induce_from_group(self, fact_type: FactType, predicate: str, 
                           facts: List[ExtractedFact]) -> Optional[InducedRule]:
        """استنباط قاعدة من مجموعة حقائق"""
        # البحث عن نمط مشترك في الكائنات
        objects = [f.object for f in facts if f.object]
        
        if not objects:
            return None
        
        # البحث عن تصنيفات مشتركة
        common_words = self._find_common_words(objects)
        
        if common_words:
            rule = InducedRule(
                condition=predicate,
                conclusion=f"implies_{common_words[0]}",
                support=len(facts),
                confidence=len(facts) / (len(facts) + 1),
                examples=[f.text for f in facts[:3]]
            )
            return rule
        
        return None
    
    def _find_common_words(self, texts: List[str]) -> List[str]:
        """العثور على كلمات مشتركة"""
        if not texts:
            return []
        
        word_sets = [set(t.split()) for t in texts]
        common = word_sets[0]
        for ws in word_sets[1:]:
            common &= ws
        
        return list(common)
    
    def _rule_exists(self, new_rule: InducedRule) -> bool:
        """التحقق من وجود قاعدة مشابهة"""
        for rule in self.induced_rules:
            if rule.condition == new_rule.condition and rule.conclusion == new_rule.conclusion:
                return True
        return False
    
    def get_rules(self, min_confidence: float = 0.5) -> List[InducedRule]:
        """الحصول على القواعد المستنبطة"""
        return [r for r in self.induced_rules if r.confidence >= min_confidence]


class LearningAgent:
    """
    وكيل التعلم التفاعلي
    
    يجمع بين استخراج الحقائق واستنباط القواعد
    لتحديث قاعدة المعرفة باستمرار.
    """
    
    def __init__(self, engine: Optional[IstinbatEngine] = None):
        self.engine = engine or IstinbatEngine()
        self.extractor = FactExtractor()
        self.inducer = RuleInducer()
        self.learned_facts: List[ExtractedFact] = []
        self.learning_log: List[Dict[str, Any]] = []
    
    def learn_from_text(self, text: str, source: str = "user_input") -> Dict[str, Any]:
        """
        التعلم من نص
        
        Returns:
            ملخص التعلم
        """
        # 1. استخراج الحقائق
        facts = self.extractor.extract(text, source)
        
        # 2. إضافة للمستنبط
        self.inducer.add_facts(facts)
        
        # 3. إضافة للمحرك المنطقي
        added_facts = []
        for fact in facts:
            if fact.confidence >= 0.5:  # حد أدنى للثقة
                try:
                    logical_fact = fact.to_logical_fact()
                    self.engine.logical_engine.add_fact(logical_fact)
                    added_facts.append(fact)
                    self.learned_facts.append(fact)
                except Exception as e:
                    pass  # تجاهل الحقائق التي لا يمكن إضافتها
        
        # 4. الحصول على القواعد المستنبطة
        new_rules = self.inducer.get_rules()
        
        # 5. تسجيل التعلم
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "source": source,
            "text_length": len(text),
            "facts_extracted": len(facts),
            "facts_added": len(added_facts),
            "rules_induced": len(new_rules)
        }
        self.learning_log.append(log_entry)
        
        return {
            "facts_found": len(facts),
            "facts_learned": len(added_facts),
            "rules_induced": len(new_rules),
            "sample_facts": [f.to_dict() for f in added_facts[:3]],
            "sample_rules": [{"condition": r.condition, "conclusion": r.conclusion} 
                           for r in new_rules[:3]]
        }
    
    def learn_from_conversation(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """التعلم من محادثة"""
        total_facts = 0
        total_rules = 0
        
        for msg in messages:
            if msg.get("role") == "user":
                result = self.learn_from_text(msg["content"], "conversation")
                total_facts += result["facts_learned"]
                total_rules += result["rules_induced"]
        
        return {
            "messages_processed": len(messages),
            "total_facts_learned": total_facts,
            "total_rules_induced": total_rules
        }
    
    def teach(self, fact_text: str, fact_type: str = "definition") -> bool:
        """
        تعليم حقيقة مباشرة
        
        مثال: agent.teach("الذكاء الاصطناعي هو محاكاة الذكاء البشري")
        """
        try:
            fact_type_enum = FactType(fact_type)
        except ValueError:
            fact_type_enum = FactType.DEFINITION
        
        facts = self.extractor.extract(fact_text, "direct_teaching")
        
        if facts:
            for fact in facts:
                fact.confidence = 1.0  # ثقة كاملة للتعليم المباشر
                logical_fact = fact.to_logical_fact()
                self.engine.logical_engine.add_fact(logical_fact)
                self.learned_facts.append(fact)
            return True
        
        return False
    
    def query_learned(self, query: str) -> List[str]:
        """استعلام الحقائق المتعلمة"""
        results = []
        query_words = set(query.lower().split())
        
        for fact in self.learned_facts:
            fact_words = set(fact.text.lower().split())
            if query_words & fact_words:
                results.append(fact.text)
        
        return results
    
    def get_learning_stats(self) -> Dict[str, Any]:
        """إحصائيات التعلم"""
        return {
            "total_facts_learned": len(self.learned_facts),
            "total_rules_induced": len(self.inducer.induced_rules),
            "fact_types": self._count_fact_types(),
            "learning_sessions": len(self.learning_log),
            "avg_confidence": self._avg_confidence()
        }
    
    def _count_fact_types(self) -> Dict[str, int]:
        """عد أنواع الحقائق"""
        counts = {}
        for fact in self.learned_facts:
            ft = fact.fact_type.value
            counts[ft] = counts.get(ft, 0) + 1
        return counts
    
    def _avg_confidence(self) -> float:
        """متوسط الثقة"""
        if not self.learned_facts:
            return 0.0
        return sum(f.confidence for f in self.learned_facts) / len(self.learned_facts)
    
    def export_knowledge(self) -> Dict[str, Any]:
        """تصدير المعرفة المتعلمة"""
        return {
            "facts": [f.to_dict() for f in self.learned_facts],
            "rules": [
                {
                    "condition": r.condition,
                    "conclusion": r.conclusion,
                    "support": r.support,
                    "confidence": r.confidence,
                    "examples": r.examples
                }
                for r in self.inducer.induced_rules
            ],
            "stats": self.get_learning_stats()
        }


# ============ اختبار ============
if __name__ == "__main__":
    print("=" * 50)
    print("اختبار التعلم التفاعلي")
    print("=" * 50)
    
    agent = LearningAgent()
    
    # اختبار التعلم من نص
    print("\n1. التعلم من نص:")
    text = """
    الذكاء الاصطناعي هو فرع من علوم الحاسوب.
    التعلم الآلي يعني قدرة الآلة على التعلم من البيانات.
    البرمجة هي عملية كتابة التعليمات للحاسوب.
    بايثون هي لغة برمجة سهلة التعلم.
    """
    result = agent.learn_from_text(text)
    print(f"   الحقائق المستخرجة: {result['facts_found']}")
    print(f"   الحقائق المتعلمة: {result['facts_learned']}")
    
    # اختبار التعليم المباشر
    print("\n2. التعليم المباشر:")
    success = agent.teach("الشمس هي نجم في مجرتنا")
    print(f"   نجاح التعليم: {success}")
    
    # اختبار الاستعلام
    print("\n3. استعلام المعرفة:")
    results = agent.query_learned("الذكاء")
    print(f"   النتائج: {results}")
    
    # إحصائيات
    print("\n4. الإحصائيات:")
    stats = agent.get_learning_stats()
    print(f"   إجمالي الحقائق: {stats['total_facts_learned']}")
    print(f"   متوسط الثقة: {stats['avg_confidence']:.2f}")
    
    print("\n✅ اكتمل الاختبار بنجاح!")
