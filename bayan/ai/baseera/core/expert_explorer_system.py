#!/usr/bin/env python3
"""
نظام الخبير/المستكشف الثوري - Expert/Explorer Revolutionary System
نظام بصيرة المتكامل

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله

هذا النظام يطبق مفهوم الخبير/المستكشف الذي يقود النظام:
- الخبير: يدير العمليات المعروفة والمجربة
- المستكشف: يكتشف أنماط وحلول جديدة
- القيادة المزدوجة: تنسيق بين الخبير والمستكشف
"""

import numpy as np
import matplotlib.pyplot as plt
import json
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum
import copy
import random

# استيراد النظام الأم والمعادلات المتكيفة
from .revolutionary_mother_equation import RevolutionaryMotherEquation
from .adaptive_revolutionary_equations_fixed import AdaptiveRevolutionaryEquation, AdaptationType

class ExpertiseLevel(Enum):
    """مستويات الخبرة"""
    NOVICE = "novice"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"
    MASTER = "master"

class ExplorationStrategy(Enum):
    """استراتيجيات الاستكشاف"""
    RANDOM_SEARCH = "random_search"
    GUIDED_EXPLORATION = "guided_exploration"
    PATTERN_BASED = "pattern_based"
    HYBRID_APPROACH = "hybrid_approach"
    REVOLUTIONARY_DISCOVERY = "revolutionary_discovery"

class DecisionType(Enum):
    """أنواع القرارات"""
    EXPERT_DECISION = "expert_decision"
    EXPLORER_DECISION = "explorer_decision"
    COLLABORATIVE_DECISION = "collaborative_decision"
    EMERGENCY_DECISION = "emergency_decision"

@dataclass
class ExpertKnowledge:
    """معرفة الخبير"""
    knowledge_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    domain: str = ""
    expertise_level: ExpertiseLevel = ExpertiseLevel.NOVICE
    
    # المعرفة المخزنة
    patterns: Dict[str, Any] = field(default_factory=dict)
    solutions: Dict[str, Any] = field(default_factory=dict)
    best_practices: List[str] = field(default_factory=list)
    
    # إحصائيات الأداء
    success_rate: float = 0.0
    usage_count: int = 0
    last_used: datetime = field(default_factory=datetime.now)
    
    # تقييم الجودة
    reliability_score: float = 0.5
    efficiency_score: float = 0.5

@dataclass
class ExplorationResult:
    """نتيجة الاستكشاف"""
    exploration_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)
    strategy: ExplorationStrategy = ExplorationStrategy.RANDOM_SEARCH
    
    # البيانات المكتشفة
    discovered_patterns: List[Dict[str, Any]] = field(default_factory=list)
    new_solutions: List[Dict[str, Any]] = field(default_factory=list)
    innovation_score: float = 0.0
    
    # تقييم النتائج
    success: bool = False
    potential_value: float = 0.0
    risk_level: float = 0.5

@dataclass
class Decision:
    """قرار النظام"""
    decision_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)
    decision_type: DecisionType = DecisionType.COLLABORATIVE_DECISION
    
    # محتوى القرار
    action: str = ""
    parameters: Dict[str, Any] = field(default_factory=dict)
    confidence: float = 0.5
    
    # مصدر القرار
    expert_contribution: float = 0.5
    explorer_contribution: float = 0.5
    
    # النتائج
    executed: bool = False
    success: bool = False
    outcome: Dict[str, Any] = field(default_factory=dict)

class BaserahExpertCore(AdaptiveRevolutionaryEquation):
    """
    نواة الخبير الثورية
    
    ترث من المعادلة المتكيفة وتضيف قدرات الخبرة:
    - إدارة المعرفة المتراكمة
    - تطبيق أفضل الممارسات
    - اتخاذ قرارات مدروسة
    - تحسين الأداء المستمر
    """
    
    def __init__(self, name: str, domain: str = "general"):
        super().__init__(name)
        
        self.domain = domain
        self.expertise_level = ExpertiseLevel.NOVICE
        
        # قاعدة المعرفة
        self.knowledge_base: Dict[str, ExpertKnowledge] = {}
        self.decision_history: List[Decision] = []
        
        # إحصائيات الخبرة
        self.total_decisions = 0
        self.successful_decisions = 0
        self.expertise_score = 0.0
        
        # إعدادات الخبير
        self.confidence_threshold = 0.7
        self.learning_rate = 0.05
        self.knowledge_retention = 0.9
        
        print(f"🧠👨‍🏫 تم إنشاء نواة الخبير: {name} (مجال: {domain})")
    
    def add_knowledge(self, domain: str, patterns: Dict[str, Any], 
                     solutions: Dict[str, Any], best_practices: List[str] = None) -> str:
        """إضافة معرفة جديدة لقاعدة البيانات"""
        knowledge = ExpertKnowledge(
            domain=domain,
            patterns=patterns,
            solutions=solutions,
            best_practices=best_practices or [],
            expertise_level=self.expertise_level
        )
        
        self.knowledge_base[knowledge.knowledge_id] = knowledge
        print(f"📚 تم إضافة معرفة جديدة: {domain}")
        return knowledge.knowledge_id
    
    def find_relevant_knowledge(self, query: Dict[str, Any]) -> List[ExpertKnowledge]:
        """البحث عن المعرفة ذات الصلة"""
        relevant_knowledge = []
        
        for knowledge in self.knowledge_base.values():
            relevance_score = self._calculate_relevance(knowledge, query)
            if relevance_score > 0.3:  # عتبة الصلة
                relevant_knowledge.append((knowledge, relevance_score))
        
        # ترتيب حسب الصلة
        relevant_knowledge.sort(key=lambda x: x[1], reverse=True)
        return [k[0] for k in relevant_knowledge]
    
    def _calculate_relevance(self, knowledge: ExpertKnowledge, query: Dict[str, Any]) -> float:
        """حساب درجة الصلة بين المعرفة والاستعلام"""
        relevance = 0.0
        
        # مطابقة المجال
        if knowledge.domain == query.get('domain', ''):
            relevance += 0.4
        
        # مطابقة الأنماط
        query_patterns = query.get('patterns', {})
        for pattern_key in query_patterns:
            if pattern_key in knowledge.patterns:
                relevance += 0.3
        
        # تقييم الجودة
        relevance += knowledge.reliability_score * 0.2
        relevance += knowledge.efficiency_score * 0.1
        
        return min(relevance, 1.0)
    
    def make_expert_decision(self, problem: Dict[str, Any]) -> Decision:
        """اتخاذ قرار خبير مدروس"""
        decision = Decision(
            decision_type=DecisionType.EXPERT_DECISION,
            expert_contribution=1.0,
            explorer_contribution=0.0
        )
        
        try:
            # البحث عن المعرفة ذات الصلة
            relevant_knowledge = self.find_relevant_knowledge(problem)
            
            if not relevant_knowledge:
                # لا توجد معرفة كافية
                decision.action = "insufficient_knowledge"
                decision.confidence = 0.1
                decision.parameters = {"reason": "لا توجد معرفة كافية في قاعدة البيانات"}
            else:
                # استخدام أفضل معرفة متاحة
                best_knowledge = relevant_knowledge[0]
                
                # تحديد الحل الأنسب
                problem_type = problem.get('type', 'unknown')
                if problem_type in best_knowledge.solutions:
                    solution = best_knowledge.solutions[problem_type]
                    decision.action = "apply_known_solution"
                    decision.parameters = solution
                    decision.confidence = best_knowledge.reliability_score
                else:
                    # تطبيق أفضل الممارسات
                    decision.action = "apply_best_practices"
                    decision.parameters = {
                        "practices": best_knowledge.best_practices,
                        "patterns": best_knowledge.patterns
                    }
                    decision.confidence = best_knowledge.reliability_score * 0.8
                
                # تحديث إحصائيات الاستخدام
                best_knowledge.usage_count += 1
                best_knowledge.last_used = datetime.now()
        
        except Exception as e:
            decision.action = "error"
            decision.confidence = 0.0
            decision.parameters = {"error": str(e)}
        
        self.decision_history.append(decision)
        self.total_decisions += 1
        
        print(f"🧠 قرار خبير: {decision.action} (ثقة: {decision.confidence:.3f})")
        return decision
    
    def learn_from_outcome(self, decision_id: str, outcome: Dict[str, Any], success: bool):
        """التعلم من نتائج القرارات"""
        # البحث عن القرار
        decision = None
        for d in self.decision_history:
            if d.decision_id == decision_id:
                decision = d
                break
        
        if decision is None:
            print(f"❌ لم يتم العثور على القرار: {decision_id}")
            return
        
        # تحديث القرار
        decision.executed = True
        decision.success = success
        decision.outcome = outcome
        
        if success:
            self.successful_decisions += 1
        
        # تحديث المعرفة ذات الصلة
        self._update_knowledge_from_outcome(decision, outcome, success)
        
        # تحديث مستوى الخبرة
        self._update_expertise_level()
        
        print(f"📈 تم التعلم من النتيجة: {'نجح' if success else 'فشل'}")
    
    def _update_knowledge_from_outcome(self, decision: Decision, outcome: Dict[str, Any], success: bool):
        """تحديث المعرفة بناءً على النتائج"""
        if decision.action == "apply_known_solution":
            # تحديث موثوقية الحل
            solution_key = list(decision.parameters.keys())[0] if decision.parameters else None
            if solution_key:
                for knowledge in self.knowledge_base.values():
                    if solution_key in knowledge.solutions:
                        if success:
                            knowledge.reliability_score = min(knowledge.reliability_score + self.learning_rate, 1.0)
                        else:
                            knowledge.reliability_score = max(knowledge.reliability_score - self.learning_rate, 0.0)
        
        elif decision.action == "apply_best_practices":
            # تحديث فعالية أفضل الممارسات
            for knowledge in self.knowledge_base.values():
                if success:
                    knowledge.efficiency_score = min(knowledge.efficiency_score + self.learning_rate, 1.0)
                else:
                    knowledge.efficiency_score = max(knowledge.efficiency_score - self.learning_rate, 0.0)
    
    def _update_expertise_level(self):
        """تحديث مستوى الخبرة"""
        if self.total_decisions == 0:
            return
        
        success_rate = self.successful_decisions / self.total_decisions
        self.expertise_score = success_rate
        
        # تحديد مستوى الخبرة
        if success_rate >= 0.9 and self.total_decisions >= 100:
            self.expertise_level = ExpertiseLevel.MASTER
        elif success_rate >= 0.8 and self.total_decisions >= 50:
            self.expertise_level = ExpertiseLevel.EXPERT
        elif success_rate >= 0.7 and self.total_decisions >= 20:
            self.expertise_level = ExpertiseLevel.ADVANCED
        elif success_rate >= 0.6 and self.total_decisions >= 10:
            self.expertise_level = ExpertiseLevel.INTERMEDIATE
        else:
            self.expertise_level = ExpertiseLevel.NOVICE

class BaserahExplorerCore(AdaptiveRevolutionaryEquation):
    """
    نواة المستكشف الثورية
    
    ترث من المعادلة المتكيفة وتضيف قدرات الاستكشاف:
    - اكتشاف أنماط جديدة
    - تجريب حلول مبتكرة
    - المخاطرة المحسوبة
    - الإبداع والابتكار
    """
    
    def __init__(self, name: str, exploration_domain: str = "general"):
        super().__init__(name)
        
        self.exploration_domain = exploration_domain
        self.exploration_history: List[ExplorationResult] = []
        
        # إعدادات الاستكشاف
        self.curiosity_level = 0.8
        self.risk_tolerance = 0.6
        self.innovation_threshold = 0.5
        
        # إحصائيات الاستكشاف
        self.total_explorations = 0
        self.successful_discoveries = 0
        self.innovation_score = 0.0
        
        print(f"🔍🚀 تم إنشاء نواة المستكشف: {name} (مجال: {exploration_domain})")
    
    def explore_random(self, search_space: Dict[str, Tuple[float, float]], 
                      num_samples: int = 10) -> ExplorationResult:
        """استكشاف عشوائي في مساحة البحث"""
        result = ExplorationResult(
            strategy=ExplorationStrategy.RANDOM_SEARCH
        )
        
        try:
            discovered_patterns = []
            
            for _ in range(num_samples):
                # توليد عينة عشوائية
                sample = {}
                for param, (min_val, max_val) in search_space.items():
                    sample[param] = random.uniform(min_val, max_val)
                
                # تقييم العينة
                pattern_score = self._evaluate_pattern(sample)
                if pattern_score > self.innovation_threshold:
                    discovered_patterns.append({
                        "pattern": sample,
                        "score": pattern_score,
                        "type": "random_discovery"
                    })
            
            result.discovered_patterns = discovered_patterns
            result.innovation_score = np.mean([p["score"] for p in discovered_patterns]) if discovered_patterns else 0.0
            result.success = len(discovered_patterns) > 0
            
        except Exception as e:
            result.success = False
            result.innovation_score = 0.0
        
        self.exploration_history.append(result)
        self.total_explorations += 1
        if result.success:
            self.successful_discoveries += 1
        
        print(f"🔍 استكشاف عشوائي: {len(result.discovered_patterns)} أنماط مكتشفة")
        return result
    
    def explore_guided(self, current_best: Dict[str, Any], 
                      exploration_radius: float = 0.2) -> ExplorationResult:
        """استكشاف موجه حول أفضل حل حالي"""
        result = ExplorationResult(
            strategy=ExplorationStrategy.GUIDED_EXPLORATION
        )
        
        try:
            discovered_patterns = []
            
            # استكشاف حول النقطة الحالية
            for _ in range(15):
                # إضافة تنويع محدود
                new_pattern = {}
                for key, value in current_best.items():
                    if isinstance(value, (int, float)):
                        variation = random.gauss(0, exploration_radius * abs(value))
                        new_pattern[key] = value + variation
                    else:
                        new_pattern[key] = value
                
                # تقييم النمط الجديد
                pattern_score = self._evaluate_pattern(new_pattern)
                if pattern_score > self.innovation_threshold:
                    discovered_patterns.append({
                        "pattern": new_pattern,
                        "score": pattern_score,
                        "type": "guided_discovery",
                        "distance_from_best": self._calculate_distance(current_best, new_pattern)
                    })
            
            result.discovered_patterns = discovered_patterns
            result.innovation_score = np.mean([p["score"] for p in discovered_patterns]) if discovered_patterns else 0.0
            result.success = len(discovered_patterns) > 0
            
        except Exception as e:
            result.success = False
            result.innovation_score = 0.0
        
        self.exploration_history.append(result)
        self.total_explorations += 1
        if result.success:
            self.successful_discoveries += 1
        
        print(f"🎯 استكشاف موجه: {len(result.discovered_patterns)} أنماط مكتشفة")
        return result
    
    def explore_revolutionary(self, problem_context: Dict[str, Any]) -> ExplorationResult:
        """استكشاف ثوري باستخدام النظريات الثلاث"""
        result = ExplorationResult(
            strategy=ExplorationStrategy.REVOLUTIONARY_DISCOVERY
        )
        
        try:
            discovered_patterns = []
            
            # 1. تطبيق نظرية ثنائية الصفر
            zero_duality_patterns = self._explore_zero_duality(problem_context)
            discovered_patterns.extend(zero_duality_patterns)
            
            # 2. تطبيق نظرية تعامد الأضداد
            perpendicular_patterns = self._explore_perpendicular_opposites(problem_context)
            discovered_patterns.extend(perpendicular_patterns)
            
            # 3. تطبيق نظرية الفتائل
            filament_patterns = self._explore_filament_theory(problem_context)
            discovered_patterns.extend(filament_patterns)
            
            result.discovered_patterns = discovered_patterns
            result.innovation_score = np.mean([p["score"] for p in discovered_patterns]) if discovered_patterns else 0.0
            result.success = len(discovered_patterns) > 0
            result.potential_value = result.innovation_score * 1.5  # الاستكشاف الثوري له قيمة أعلى
            
        except Exception as e:
            result.success = False
            result.innovation_score = 0.0
        
        self.exploration_history.append(result)
        self.total_explorations += 1
        if result.success:
            self.successful_discoveries += 1
        
        print(f"🌟 استكشاف ثوري: {len(result.discovered_patterns)} أنماط ثورية مكتشفة")
        return result
    
    def _explore_zero_duality(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """استكشاف باستخدام نظرية ثنائية الصفر"""
        patterns = []
        
        # إنشاء أنماط متوازنة (مجموعها صفر)
        for _ in range(5):
            positive_values = [random.uniform(0.1, 1.0) for _ in range(3)]
            negative_values = [-sum(positive_values) / 3 for _ in range(3)]
            
            pattern = {
                "positive_components": positive_values,
                "negative_components": negative_values,
                "balance_score": abs(sum(positive_values) + sum(negative_values)),
                "theory": "zero_duality"
            }
            
            score = self._evaluate_pattern(pattern)
            if score > self.innovation_threshold:
                patterns.append({
                    "pattern": pattern,
                    "score": score,
                    "type": "zero_duality_discovery"
                })
        
        return patterns
    
    def _explore_perpendicular_opposites(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """استكشاف باستخدام نظرية تعامد الأضداد"""
        patterns = []
        
        # إنشاء أنماط متعامدة
        for _ in range(5):
            angle = random.uniform(0, 2 * np.pi)
            perpendicular_angle = angle + np.pi/2
            
            vector1 = [np.cos(angle), np.sin(angle)]
            vector2 = [np.cos(perpendicular_angle), np.sin(perpendicular_angle)]
            
            pattern = {
                "vector1": vector1,
                "vector2": vector2,
                "dot_product": np.dot(vector1, vector2),
                "theory": "perpendicular_opposites"
            }
            
            score = self._evaluate_pattern(pattern)
            if score > self.innovation_threshold:
                patterns.append({
                    "pattern": pattern,
                    "score": score,
                    "type": "perpendicular_discovery"
                })
        
        return patterns
    
    def _explore_filament_theory(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """استكشاف باستخدام نظرية الفتائل"""
        patterns = []
        
        # إنشاء أنماط مترابطة (فتائل)
        for _ in range(5):
            # إنشاء سلسلة مترابطة من القيم
            base_value = random.uniform(0.1, 1.0)
            filament_chain = [base_value]
            
            for i in range(4):
                # كل قيمة تعتمد على السابقة
                next_value = filament_chain[-1] * random.uniform(0.8, 1.2)
                filament_chain.append(next_value)
            
            pattern = {
                "filament_chain": filament_chain,
                "connection_strength": np.std(filament_chain),
                "coherence": np.corrcoef(filament_chain[:-1], filament_chain[1:])[0, 1],
                "theory": "filament_theory"
            }
            
            score = self._evaluate_pattern(pattern)
            if score > self.innovation_threshold:
                patterns.append({
                    "pattern": pattern,
                    "score": score,
                    "type": "filament_discovery"
                })
        
        return patterns
    
    def _evaluate_pattern(self, pattern: Dict[str, Any]) -> float:
        """تقييم جودة النمط المكتشف"""
        score = 0.0
        
        # تقييم الأصالة
        novelty_score = self._calculate_novelty(pattern)
        score += novelty_score * 0.4
        
        # تقييم الفائدة المحتملة
        utility_score = self._calculate_utility(pattern)
        score += utility_score * 0.3
        
        # تقييم الأناقة الرياضية
        elegance_score = self._calculate_elegance(pattern)
        score += elegance_score * 0.3
        
        return min(score, 1.0)
    
    def _calculate_novelty(self, pattern: Dict[str, Any]) -> float:
        """حساب درجة الأصالة"""
        # مقارنة مع الأنماط المكتشفة سابقاً
        if not self.exploration_history:
            return 1.0
        
        max_similarity = 0.0
        for exploration in self.exploration_history:
            for discovered in exploration.discovered_patterns:
                similarity = self._calculate_similarity(pattern, discovered["pattern"])
                max_similarity = max(max_similarity, similarity)
        
        novelty = 1.0 - max_similarity
        return max(novelty, 0.0)
    
    def _calculate_utility(self, pattern: Dict[str, Any]) -> float:
        """حساب الفائدة المحتملة"""
        # تقييم بسيط للفائدة
        utility = 0.5
        
        # إضافة نقاط للأنماط المعقدة
        if len(pattern) > 3:
            utility += 0.2
        
        # إضافة نقاط للأنماط المتوازنة
        if "balance_score" in pattern and pattern["balance_score"] < 0.1:
            utility += 0.3
        
        return min(utility, 1.0)
    
    def _calculate_elegance(self, pattern: Dict[str, Any]) -> float:
        """حساب الأناقة الرياضية"""
        elegance = 0.5
        
        # تقييم البساطة
        if len(pattern) <= 5:
            elegance += 0.2
        
        # تقييم التماثل
        if "theory" in pattern:
            elegance += 0.3
        
        return min(elegance, 1.0)
    
    def _calculate_similarity(self, pattern1: Dict[str, Any], pattern2: Dict[str, Any]) -> float:
        """حساب التشابه بين نمطين"""
        common_keys = set(pattern1.keys()) & set(pattern2.keys())
        if not common_keys:
            return 0.0
        
        similarity_sum = 0.0
        for key in common_keys:
            if isinstance(pattern1[key], (int, float)) and isinstance(pattern2[key], (int, float)):
                # تشابه رقمي
                diff = abs(pattern1[key] - pattern2[key])
                max_val = max(abs(pattern1[key]), abs(pattern2[key]), 1.0)
                similarity_sum += 1.0 - (diff / max_val)
            elif pattern1[key] == pattern2[key]:
                # تطابق تام
                similarity_sum += 1.0
        
        return similarity_sum / len(common_keys)
    
    def _calculate_distance(self, pattern1: Dict[str, Any], pattern2: Dict[str, Any]) -> float:
        """حساب المسافة بين نمطين"""
        return 1.0 - self._calculate_similarity(pattern1, pattern2)

class BaserahIntegratedExpertExplorer(AdaptiveRevolutionaryEquation):
    """
    النظام المتكامل للخبير/المستكشف
    
    يجمع بين قدرات الخبير والمستكشف في نظام موحد:
    - تنسيق القرارات بين الخبير والمستكشف
    - توزيع المهام حسب الحالة
    - التعلم المشترك
    - القيادة التكيفية
    """
    
    def __init__(self, name: str, domain: str = "general"):
        super().__init__(name)
        
        self.domain = domain
        
        # إنشاء الخبير والمستكشف
        self.expert = BaserahExpertCore(f"{name}_Expert", domain)
        self.explorer = BaserahExplorerCore(f"{name}_Explorer", domain)
        
        # إعدادات التكامل
        self.expert_weight = 0.6
        self.explorer_weight = 0.4
        self.collaboration_threshold = 0.5
        
        # تاريخ القرارات المتكاملة
        self.integrated_decisions: List[Decision] = []
        
        print(f"🤝 تم إنشاء النظام المتكامل: {name}")
        print(f"   👨‍🏫 الخبير: {self.expert.name}")
        print(f"   🔍 المستكشف: {self.explorer.name}")
    
    def analyze_situation(self, problem: Dict[str, Any]) -> Dict[str, Any]:
        """تحليل الموقف لتحديد النهج الأنسب"""
        analysis = {
            "problem_complexity": self._assess_complexity(problem),
            "knowledge_availability": self._assess_knowledge_availability(problem),
            "innovation_requirement": self._assess_innovation_requirement(problem),
            "risk_level": self._assess_risk_level(problem)
        }
        
        # تحديد النهج المناسب
        if analysis["knowledge_availability"] > 0.7 and analysis["problem_complexity"] < 0.5:
            analysis["recommended_approach"] = "expert_led"
            analysis["expert_weight"] = 0.8
            analysis["explorer_weight"] = 0.2
        elif analysis["innovation_requirement"] > 0.7 or analysis["knowledge_availability"] < 0.3:
            analysis["recommended_approach"] = "explorer_led"
            analysis["expert_weight"] = 0.2
            analysis["explorer_weight"] = 0.8
        else:
            analysis["recommended_approach"] = "collaborative"
            analysis["expert_weight"] = 0.5
            analysis["explorer_weight"] = 0.5
        
        return analysis
    
    def make_integrated_decision(self, problem: Dict[str, Any]) -> Decision:
        """اتخاذ قرار متكامل"""
        # تحليل الموقف
        situation_analysis = self.analyze_situation(problem)
        
        # الحصول على قرارات من كلا النواتين
        expert_decision = self.expert.make_expert_decision(problem)
        
        # قرار المستكشف (استكشاف ثوري)
        exploration_result = self.explorer.explore_revolutionary(problem)
        
        # دمج القرارات
        integrated_decision = Decision(
            decision_type=DecisionType.COLLABORATIVE_DECISION,
            expert_contribution=situation_analysis["expert_weight"],
            explorer_contribution=situation_analysis["explorer_weight"]
        )
        
        # تحديد الإجراء النهائي
        if situation_analysis["recommended_approach"] == "expert_led":
            integrated_decision.action = expert_decision.action
            integrated_decision.parameters = expert_decision.parameters
            integrated_decision.confidence = expert_decision.confidence * 0.9
        elif situation_analysis["recommended_approach"] == "explorer_led":
            if exploration_result.success and exploration_result.discovered_patterns:
                best_pattern = max(exploration_result.discovered_patterns, 
                                 key=lambda x: x["score"])
                integrated_decision.action = "apply_discovered_pattern"
                integrated_decision.parameters = best_pattern["pattern"]
                integrated_decision.confidence = exploration_result.innovation_score
            else:
                # الاستكشاف فشل، استخدم الخبير كبديل
                integrated_decision.action = expert_decision.action
                integrated_decision.parameters = expert_decision.parameters
                integrated_decision.confidence = expert_decision.confidence * 0.5
        else:
            # نهج تعاوني
            if expert_decision.confidence > 0.7 and exploration_result.innovation_score > 0.6:
                # دمج الحلول
                integrated_decision.action = "hybrid_solution"
                integrated_decision.parameters = {
                    "expert_solution": expert_decision.parameters,
                    "explorer_discovery": exploration_result.discovered_patterns[0]["pattern"] if exploration_result.discovered_patterns else {},
                    "blend_ratio": [situation_analysis["expert_weight"], situation_analysis["explorer_weight"]]
                }
                integrated_decision.confidence = (expert_decision.confidence + exploration_result.innovation_score) / 2
            elif expert_decision.confidence > exploration_result.innovation_score:
                # اعتماد على الخبير
                integrated_decision.action = expert_decision.action
                integrated_decision.parameters = expert_decision.parameters
                integrated_decision.confidence = expert_decision.confidence
            else:
                # اعتماد على المستكشف
                if exploration_result.discovered_patterns:
                    best_pattern = max(exploration_result.discovered_patterns, 
                                     key=lambda x: x["score"])
                    integrated_decision.action = "apply_discovered_pattern"
                    integrated_decision.parameters = best_pattern["pattern"]
                    integrated_decision.confidence = exploration_result.innovation_score
        
        self.integrated_decisions.append(integrated_decision)
        
        print(f"🤝 قرار متكامل: {integrated_decision.action}")
        print(f"   👨‍🏫 مساهمة الخبير: {integrated_decision.expert_contribution:.2f}")
        print(f"   🔍 مساهمة المستكشف: {integrated_decision.explorer_contribution:.2f}")
        print(f"   🎯 الثقة: {integrated_decision.confidence:.3f}")
        
        return integrated_decision
    
    def _assess_complexity(self, problem: Dict[str, Any]) -> float:
        """تقييم تعقيد المشكلة"""
        complexity = 0.0
        
        # عدد المتغيرات
        num_variables = len(problem.get('variables', {}))
        complexity += min(num_variables / 10.0, 0.5)
        
        # وجود قيود
        if 'constraints' in problem:
            complexity += 0.3
        
        # عدم اليقين
        if problem.get('uncertainty', 0) > 0.5:
            complexity += 0.2
        
        return min(complexity, 1.0)
    
    def _assess_knowledge_availability(self, problem: Dict[str, Any]) -> float:
        """تقييم توفر المعرفة"""
        relevant_knowledge = self.expert.find_relevant_knowledge(problem)
        if not relevant_knowledge:
            return 0.0
        
        # متوسط موثوقية المعرفة المتاحة
        avg_reliability = np.mean([k.reliability_score for k in relevant_knowledge])
        return avg_reliability
    
    def _assess_innovation_requirement(self, problem: Dict[str, Any]) -> float:
        """تقييم الحاجة للابتكار"""
        innovation_req = 0.0
        
        # مشكلة جديدة
        if problem.get('novelty', 0) > 0.7:
            innovation_req += 0.4
        
        # فشل الحلول التقليدية
        if problem.get('traditional_solutions_failed', False):
            innovation_req += 0.3
        
        # طلب صريح للإبداع
        if problem.get('requires_creativity', False):
            innovation_req += 0.3
        
        return min(innovation_req, 1.0)
    
    def _assess_risk_level(self, problem: Dict[str, Any]) -> float:
        """تقييم مستوى المخاطرة"""
        risk = problem.get('risk_level', 0.5)
        
        # تعديل بناءً على السياق
        if problem.get('critical', False):
            risk += 0.2
        
        if problem.get('reversible', True):
            risk -= 0.1
        
        return max(min(risk, 1.0), 0.0)
    
    def get_system_status(self) -> Dict[str, Any]:
        """حالة النظام المتكامل"""
        expert_stats = {
            "expertise_level": self.expert.expertise_level.value,
            "total_decisions": self.expert.total_decisions,
            "success_rate": self.expert.successful_decisions / max(self.expert.total_decisions, 1),
            "knowledge_base_size": len(self.expert.knowledge_base)
        }
        
        explorer_stats = {
            "total_explorations": self.explorer.total_explorations,
            "successful_discoveries": self.explorer.successful_discoveries,
            "discovery_rate": self.explorer.successful_discoveries / max(self.explorer.total_explorations, 1),
            "innovation_score": self.explorer.innovation_score
        }
        
        integrated_stats = {
            "total_integrated_decisions": len(self.integrated_decisions),
            "expert_weight": self.expert_weight,
            "explorer_weight": self.explorer_weight
        }
        
        return {
            "expert": expert_stats,
            "explorer": explorer_stats,
            "integrated": integrated_stats,
            "system_health": (expert_stats["success_rate"] + explorer_stats["discovery_rate"]) / 2
        }

# ==================== اختبار نظام الخبير/المستكشف ====================

def test_expert_explorer_system():
    """اختبار شامل لنظام الخبير/المستكشف"""
    print("🧪 اختبار نظام الخبير/المستكشف الثوري")
    print("="*60)
    
    # إنشاء النظام المتكامل
    system = BaserahIntegratedExpertExplorer("TestSystem", "mathematics")
    
    # إضافة معرفة للخبير
    print(f"\n📚 إضافة معرفة للخبير:")
    knowledge_id = system.expert.add_knowledge(
        domain="mathematics",
        patterns={
            "linear_equation": {"type": "ax + b = 0", "complexity": "low"},
            "quadratic_equation": {"type": "ax² + bx + c = 0", "complexity": "medium"}
        },
        solutions={
            "linear_equation": {"method": "direct_solving", "steps": ["isolate_x"]},
            "quadratic_equation": {"method": "quadratic_formula", "steps": ["apply_formula"]}
        },
        best_practices=["check_discriminant", "verify_solution", "simplify_result"]
    )
    
    # اختبار مشاكل مختلفة
    problems = [
        {
            "type": "linear_equation",
            "domain": "mathematics",
            "variables": {"a": 2, "b": -4},
            "complexity": 0.2,
            "novelty": 0.1,
            "requires_creativity": False
        },
        {
            "type": "unknown_equation",
            "domain": "mathematics", 
            "variables": {"x": "complex", "y": "nonlinear"},
            "complexity": 0.8,
            "novelty": 0.9,
            "requires_creativity": True,
            "traditional_solutions_failed": True
        },
        {
            "type": "optimization_problem",
            "domain": "mathematics",
            "variables": {"constraints": 5, "objectives": 2},
            "complexity": 0.6,
            "novelty": 0.5,
            "uncertainty": 0.7
        }
    ]
    
    # اختبار كل مشكلة
    for i, problem in enumerate(problems, 1):
        print(f"\n🎯 اختبار المشكلة {i}: {problem['type']}")
        
        # تحليل الموقف
        analysis = system.analyze_situation(problem)
        print(f"   📊 تحليل الموقف: {analysis['recommended_approach']}")
        print(f"   🧠 وزن الخبير: {analysis['expert_weight']:.2f}")
        print(f"   🔍 وزن المستكشف: {analysis['explorer_weight']:.2f}")
        
        # اتخاذ قرار متكامل
        decision = system.make_integrated_decision(problem)
        
        # محاكاة تنفيذ القرار
        success = random.choice([True, False, True])  # محاكاة نتيجة
        outcome = {"result": "success" if success else "failure", "score": random.uniform(0.3, 0.9)}
        
        # التعلم من النتيجة
        system.expert.learn_from_outcome(decision.decision_id, outcome, success)
        
        print(f"   📈 النتيجة: {'نجح' if success else 'فشل'}")
    
    # اختبار الاستكشاف المستقل
    print(f"\n🔍 اختبار الاستكشاف المستقل:")
    
    # استكشاف عشوائي
    search_space = {
        "alpha": (0.1, 2.0),
        "beta": (-1.0, 1.0),
        "gamma": (0.0, 5.0)
    }
    random_result = system.explorer.explore_random(search_space, num_samples=8)
    print(f"   🎲 استكشاف عشوائي: {len(random_result.discovered_patterns)} أنماط")
    
    # استكشاف ثوري
    revolutionary_result = system.explorer.explore_revolutionary({"domain": "mathematics"})
    print(f"   🌟 استكشاف ثوري: {len(revolutionary_result.discovered_patterns)} أنماط ثورية")
    
    # تقرير حالة النظام
    print(f"\n📊 حالة النظام:")
    status = system.get_system_status()
    print(f"   👨‍🏫 الخبير - مستوى الخبرة: {status['expert']['expertise_level']}")
    print(f"   👨‍🏫 الخبير - معدل النجاح: {status['expert']['success_rate']:.3f}")
    print(f"   🔍 المستكشف - معدل الاكتشاف: {status['explorer']['discovery_rate']:.3f}")
    print(f"   🤝 صحة النظام: {status['system_health']:.3f}")
    
    print(f"\n✅ انتهى اختبار نظام الخبير/المستكشف!")
    return system

if __name__ == "__main__":
    test_expert_explorer_system()
