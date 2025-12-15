"""
محرك القصص السببية - Causal Stories Engine
============================================

إنشاء سيناريوهات "ماذا لو" باستخدام العوالم المتوازية.

المكونات:
- StorySimulator: محاكاة السيناريوهات
- WorldBrancher: تفرع العوالم
- OutcomePredictor: توقع النتائج

المطور: باسل يحيى عبدالله
"""

import sys
import os
from typing import List, Dict, Any, Optional, Tuple, Set
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import copy

# Ensure we can import bayan packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from bayan.bayan.istinbat_engine import IstinbatEngine


class ScenarioType(Enum):
    """أنواع السيناريوهات"""
    WHAT_IF = "what_if"          # ماذا لو
    BEST_CASE = "best_case"      # أفضل حالة
    WORST_CASE = "worst_case"    # أسوأ حالة
    ALTERNATIVE = "alternative"   # بديل
    CONSEQUENCE = "consequence"   # تبعات


@dataclass
class StoryEvent:
    """حدث في القصة"""
    description: str
    timestamp: int  # ترتيب زمني
    probability: float
    consequences: List[str] = field(default_factory=list)
    conditions: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "description": self.description,
            "timestamp": self.timestamp,
            "probability": self.probability,
            "consequences": self.consequences,
            "conditions": self.conditions
        }


@dataclass
class Scenario:
    """سيناريو كامل"""
    name: str
    scenario_type: ScenarioType
    initial_conditions: Dict[str, Any]
    events: List[StoryEvent]
    final_outcome: str
    probability: float
    world_name: str
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "type": self.scenario_type.value,
            "initial_conditions": self.initial_conditions,
            "events": [e.to_dict() for e in self.events],
            "final_outcome": self.final_outcome,
            "probability": self.probability,
            "world_name": self.world_name
        }


@dataclass
class StoryBranch:
    """فرع في القصة"""
    branch_point: str
    choice_made: str
    resulting_scenario: Scenario
    alternatives: List[str] = field(default_factory=list)


class StorySimulator:
    """
    محاكي القصص
    
    يحاكي تسلسل الأحداث بناءً على الشروط.
    """
    
    def __init__(self):
        self.event_templates: Dict[str, List[str]] = {
            "conflict": [
                "يحدث خلاف",
                "تتصاعد التوترات",
                "يتم التوصل لاتفاق",
                "ينفصل الطرفان"
            ],
            "project": [
                "يبدأ المشروع",
                "تظهر تحديات",
                "يتم إيجاد حلول",
                "ينجح المشروع",
                "يفشل المشروع"
            ],
            "journey": [
                "تبدأ الرحلة",
                "يواجه عقبات",
                "يتغلب عليها",
                "يصل للهدف"
            ],
            "learning": [
                "يبدأ التعلم",
                "يواجه صعوبات",
                "يمارس باستمرار",
                "يتقن المهارة"
            ]
        }
        
        self.consequence_rules: Dict[str, List[Tuple[str, float]]] = {
            "نجاح": [("رضا", 0.8), ("ثقة", 0.7), ("فرص جديدة", 0.6)],
            "فشل": [("خيبة", 0.7), ("تعلم", 0.5), ("محاولة جديدة", 0.4)],
            "خلاف": [("توتر", 0.8), ("انفصال", 0.4), ("تفاهم", 0.3)],
            "تعلم": [("معرفة", 0.9), ("مهارة", 0.7), ("نمو", 0.6)],
        }
    
    def simulate(self, initial_state: Dict[str, Any], 
                 steps: int = 5) -> List[StoryEvent]:
        """محاكاة قصة"""
        events = []
        current_state = copy.deepcopy(initial_state)
        
        for i in range(steps):
            event = self._generate_event(current_state, i)
            events.append(event)
            current_state = self._update_state(current_state, event)
        
        return events
    
    def _generate_event(self, state: Dict[str, Any], timestamp: int) -> StoryEvent:
        """توليد حدث"""
        # اختيار نوع الحدث بناءً على الحالة
        context = state.get("context", "project")
        templates = self.event_templates.get(context, self.event_templates["project"])
        
        event_idx = min(timestamp, len(templates) - 1)
        description = templates[event_idx]
        
        # توليد التبعات
        consequences = []
        for key, rules in self.consequence_rules.items():
            if key in description.lower():
                for cons, prob in rules:
                    consequences.append(cons)
        
        return StoryEvent(
            description=description,
            timestamp=timestamp,
            probability=0.7,
            consequences=consequences[:3]
        )
    
    def _update_state(self, state: Dict[str, Any], event: StoryEvent) -> Dict[str, Any]:
        """تحديث الحالة بعد حدث"""
        new_state = copy.deepcopy(state)
        new_state["last_event"] = event.description
        new_state["history"] = state.get("history", []) + [event.description]
        return new_state


class WorldBrancher:
    """
    مفرّع العوالم
    
    يستخدم العوالم المتوازية في IstinbatEngine
    لإنشاء سيناريوهات متعددة.
    """
    
    def __init__(self, engine: IstinbatEngine):
        self.engine = engine
        self.branches: Dict[str, StoryBranch] = {}
        self.branch_counter = 0
    
    def create_branch(self, branch_point: str, choice: str, 
                      from_world: str = "default") -> str:
        """إنشاء فرع جديد"""
        self.branch_counter += 1
        world_name = f"branch_{self.branch_counter}_{choice[:10]}"
        
        # إنشاء عالم جديد
        try:
            self.engine.create_world(world_name, from_world)
        except:
            pass  # العالم موجود بالفعل
        
        return world_name
    
    def switch_to_branch(self, world_name: str):
        """التبديل لفرع"""
        try:
            self.engine.switch_world(world_name)
        except:
            pass
    
    def compare_branches(self, world1: str, world2: str) -> Dict[str, Any]:
        """مقارنة فرعين"""
        try:
            diff = self.engine.compare_worlds(world1, world2)
            return diff
        except:
            return {"error": "لا يمكن المقارنة"}
    
    def get_all_branches(self) -> List[str]:
        """الحصول على كل الفروع"""
        return list(self.branches.keys())


class OutcomePredictor:
    """
    متنبئ النتائج
    
    يتوقع نتائج سيناريو بناءً على الأحداث.
    """
    
    def __init__(self):
        self.outcome_weights: Dict[str, Dict[str, float]] = {
            "positive_factors": {
                "نجاح": 0.3,
                "تعاون": 0.2,
                "جهد": 0.2,
                "تخطيط": 0.2,
                "موارد": 0.1
            },
            "negative_factors": {
                "فشل": -0.3,
                "خلاف": -0.2,
                "إهمال": -0.2,
                "نقص": -0.15,
                "تأخر": -0.1
            }
        }
    
    def predict(self, events: List[StoryEvent]) -> Tuple[str, float]:
        """
        توقع النتيجة
        
        Returns:
            (وصف النتيجة، احتمالية)
        """
        score = 0.5  # محايد
        
        for event in events:
            # تحليل الحدث
            event_text = event.description.lower()
            
            for factor, weight in self.outcome_weights["positive_factors"].items():
                if factor in event_text:
                    score += weight
            
            for factor, weight in self.outcome_weights["negative_factors"].items():
                if factor in event_text:
                    score += weight
        
        # تحديد النتيجة
        score = max(0.0, min(1.0, score))
        
        if score >= 0.7:
            outcome = "نتيجة إيجابية: نجاح وتحقيق الأهداف"
        elif score >= 0.4:
            outcome = "نتيجة متوسطة: تقدم جزئي مع تحديات"
        else:
            outcome = "نتيجة سلبية: صعوبات وحاجة لإعادة تقييم"
        
        return outcome, score
    
    def analyze_risks(self, events: List[StoryEvent]) -> List[str]:
        """تحليل المخاطر"""
        risks = []
        
        risk_indicators = {
            "خلاف": "خطر تفكك الفريق",
            "تأخر": "خطر عدم الالتزام بالجدول",
            "نقص": "خطر نفاد الموارد",
            "فشل": "خطر عدم تحقيق الأهداف",
            "ضغط": "خطر الإرهاق"
        }
        
        for event in events:
            event_text = event.description.lower()
            for indicator, risk in risk_indicators.items():
                if indicator in event_text and risk not in risks:
                    risks.append(risk)
        
        return risks


class CausalStoriesEngine:
    """
    المحرك الرئيسي للقصص السببية
    
    يجمع كل المكونات لإنشاء سيناريوهات "ماذا لو".
    """
    
    def __init__(self, engine: Optional[IstinbatEngine] = None):
        self.engine = engine or IstinbatEngine()
        self.simulator = StorySimulator()
        self.brancher = WorldBrancher(self.engine)
        self.predictor = OutcomePredictor()
        self.scenarios: List[Scenario] = []
    
    def what_if(self, condition: str, context: Dict[str, Any] = None) -> Scenario:
        """
        ماذا لو؟
        
        Args:
            condition: الشرط الافتراضي
            context: سياق إضافي
            
        Returns:
            سيناريو كامل
        """
        # إعداد الحالة الأولية
        initial_state = context or {}
        initial_state["condition"] = condition
        initial_state["context"] = self._detect_context(condition)
        
        # إنشاء فرع جديد
        world_name = self.brancher.create_branch(
            branch_point="what_if",
            choice=condition[:20]
        )
        
        # محاكاة الأحداث
        events = self.simulator.simulate(initial_state, steps=5)
        
        # توقع النتيجة
        outcome, probability = self.predictor.predict(events)
        
        # بناء السيناريو
        scenario = Scenario(
            name=f"ماذا لو {condition}",
            scenario_type=ScenarioType.WHAT_IF,
            initial_conditions=initial_state,
            events=events,
            final_outcome=outcome,
            probability=probability,
            world_name=world_name
        )
        
        self.scenarios.append(scenario)
        return scenario
    
    def best_case(self, goal: str, context: Dict[str, Any] = None) -> Scenario:
        """أفضل سيناريو"""
        initial_state = context or {}
        initial_state["condition"] = f"نجاح {goal}"
        initial_state["context"] = "project"
        initial_state["optimistic"] = True
        
        world_name = self.brancher.create_branch("best_case", goal[:20])
        events = self.simulator.simulate(initial_state, steps=5)
        
        # تعديل للتفاؤل
        for event in events:
            event.probability = min(1.0, event.probability + 0.2)
        
        outcome, probability = self.predictor.predict(events)
        
        scenario = Scenario(
            name=f"أفضل حالة لـ {goal}",
            scenario_type=ScenarioType.BEST_CASE,
            initial_conditions=initial_state,
            events=events,
            final_outcome=outcome,
            probability=min(1.0, probability + 0.2),
            world_name=world_name
        )
        
        self.scenarios.append(scenario)
        return scenario
    
    def worst_case(self, situation: str, context: Dict[str, Any] = None) -> Scenario:
        """أسوأ سيناريو"""
        initial_state = context or {}
        initial_state["condition"] = f"فشل {situation}"
        initial_state["context"] = "conflict"
        initial_state["pessimistic"] = True
        
        world_name = self.brancher.create_branch("worst_case", situation[:20])
        events = self.simulator.simulate(initial_state, steps=5)
        
        # تعديل للتشاؤم
        for event in events:
            event.probability = max(0.0, event.probability - 0.2)
        
        outcome, probability = self.predictor.predict(events)
        
        scenario = Scenario(
            name=f"أسوأ حالة لـ {situation}",
            scenario_type=ScenarioType.WORST_CASE,
            initial_conditions=initial_state,
            events=events,
            final_outcome=outcome,
            probability=max(0.0, probability - 0.2),
            world_name=world_name
        )
        
        self.scenarios.append(scenario)
        return scenario
    
    def compare_scenarios(self, scenario1: Scenario, scenario2: Scenario) -> Dict[str, Any]:
        """مقارنة سيناريوهين"""
        return {
            "scenario1": scenario1.name,
            "scenario2": scenario2.name,
            "probability_diff": scenario1.probability - scenario2.probability,
            "outcome1": scenario1.final_outcome,
            "outcome2": scenario2.final_outcome,
            "recommendation": self._recommend(scenario1, scenario2)
        }
    
    def _recommend(self, s1: Scenario, s2: Scenario) -> str:
        """توصية بناءً على المقارنة"""
        if s1.probability > s2.probability:
            return f"'{s1.name}' أكثر احتمالاً للنجاح"
        elif s2.probability > s1.probability:
            return f"'{s2.name}' أكثر احتمالاً للنجاح"
        else:
            return "كلا السيناريوهين متساويان"
    
    def _detect_context(self, text: str) -> str:
        """اكتشاف سياق النص"""
        contexts = {
            "project": ["مشروع", "عمل", "تطوير", "بناء"],
            "conflict": ["خلاف", "نزاع", "مشكلة"],
            "journey": ["رحلة", "سفر", "انتقال"],
            "learning": ["تعلم", "دراسة", "تدريب"]
        }
        
        text_lower = text.lower()
        for context, keywords in contexts.items():
            if any(kw in text_lower for kw in keywords):
                return context
        
        return "project"
    
    def get_risks(self, scenario: Scenario) -> List[str]:
        """الحصول على مخاطر سيناريو"""
        return self.predictor.analyze_risks(scenario.events)
    
    def get_all_scenarios(self) -> List[Dict[str, Any]]:
        """الحصول على كل السيناريوهات"""
        return [s.to_dict() for s in self.scenarios]


# ============ اختبار ============
if __name__ == "__main__":
    print("=" * 50)
    print("اختبار محرك القصص السببية")
    print("=" * 50)
    
    engine = CausalStoriesEngine()
    
    # اختبار ماذا لو
    print("\n1. سيناريو 'ماذا لو':")
    scenario1 = engine.what_if("بدأنا المشروع بميزانية أكبر")
    print(f"   الاسم: {scenario1.name}")
    print(f"   النتيجة: {scenario1.final_outcome}")
    print(f"   الاحتمالية: {scenario1.probability:.2f}")
    
    # اختبار أفضل حالة
    print("\n2. سيناريو 'أفضل حالة':")
    scenario2 = engine.best_case("إطلاق المنتج")
    print(f"   الاسم: {scenario2.name}")
    print(f"   النتيجة: {scenario2.final_outcome}")
    
    # اختبار أسوأ حالة
    print("\n3. سيناريو 'أسوأ حالة':")
    scenario3 = engine.worst_case("التأخر في التسليم")
    print(f"   الاسم: {scenario3.name}")
    print(f"   النتيجة: {scenario3.final_outcome}")
    
    # مقارنة
    print("\n4. مقارنة السيناريوهات:")
    comparison = engine.compare_scenarios(scenario2, scenario3)
    print(f"   التوصية: {comparison['recommendation']}")
    
    # المخاطر
    print("\n5. تحليل المخاطر:")
    risks = engine.get_risks(scenario3)
    for risk in risks:
        print(f"   ⚠️ {risk}")
    
    print("\n✅ اكتمل الاختبار بنجاح!")
