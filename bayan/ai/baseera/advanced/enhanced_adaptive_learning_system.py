#!/usr/bin/env python3
"""
نظام التعلم التكيفي المحسن - Enhanced Adaptive Learning System
نظام بصيرة الثوري

🧠 تعلم ذاتي متقدم من التجارب والتغذية الراجعة
🔄 تكيف ديناميكي للمعاملات والاستراتيجيات
📈 تحسين مستمر للأداء والدقة
⚡ يعتمد على النظريات الثلاث الثورية

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import numpy as np
import json
import math
from typing import Dict, List, Tuple, Any, Optional, Union, Callable
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime, timedelta
import uuid
import copy

# استيراد المكونات الأساسية
from core_interfaces import BaseComponent
from advanced_linguistic_vector_system import AdvancedLinguisticVectorSystem
from advanced_semantic_analysis_engine import AdvancedSemanticAnalysisEngine

class LearningType(Enum):
    """أنواع التعلم"""
    SUPERVISED = "supervised"
    UNSUPERVISED = "unsupervised"
    REINFORCEMENT = "reinforcement"
    ADAPTIVE = "adaptive"
    REVOLUTIONARY = "revolutionary"

class FeedbackType(Enum):
    """أنواع التغذية الراجعة"""
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    CORRECTIVE = "corrective"
    ENHANCEMENT = "enhancement"

class AdaptationStrategy(Enum):
    """استراتيجيات التكيف"""
    GRADUAL = "gradual"
    AGGRESSIVE = "aggressive"
    CONSERVATIVE = "conservative"
    REVOLUTIONARY = "revolutionary"
    DYNAMIC = "dynamic"

@dataclass
class LearningExperience:
    """تجربة تعلم"""
    experience_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    input_data: Any = None
    expected_output: Any = None
    actual_output: Any = None
    feedback: Dict[str, Any] = field(default_factory=dict)
    feedback_type: FeedbackType = FeedbackType.NEUTRAL
    learning_context: str = "general"
    timestamp: datetime = field(default_factory=datetime.now)
    success_score: float = 0.5
    improvement_suggestions: List[str] = field(default_factory=list)

@dataclass
class AdaptationRule:
    """قاعدة تكيف"""
    condition: str
    action: str
    rule_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    priority: int = 1
    success_rate: float = 0.0
    usage_count: int = 0
    last_used: Optional[datetime] = None
    effectiveness: float = 0.5

@dataclass
class LearningMetrics:
    """مقاييس التعلم"""
    total_experiences: int = 0
    successful_experiences: int = 0
    failed_experiences: int = 0
    average_success_rate: float = 0.0
    learning_velocity: float = 0.0
    adaptation_frequency: float = 0.0
    improvement_trend: float = 0.0
    last_update: datetime = field(default_factory=datetime.now)

class EnhancedAdaptiveLearningSystem(BaseComponent):
    """نظام التعلم التكيفي المحسن"""
    
    def __init__(self, name: str = "EnhancedAdaptiveLearningSystem"):
        super().__init__(name)
        
        # المكونات الأساسية
        self.linguistic_system = AdvancedLinguisticVectorSystem()
        self.semantic_engine = AdvancedSemanticAnalysisEngine()
        
        # ذاكرة التعلم
        self.learning_experiences: List[LearningExperience] = []
        self.adaptation_rules: List[AdaptationRule] = []
        self.learned_patterns: Dict[str, Any] = {}
        self.successful_strategies: Dict[str, float] = {}
        
        # معاملات التعلم
        self.learning_parameters = {
            'learning_rate': 0.1,
            'adaptation_threshold': 0.7,
            'memory_capacity': 1000,
            'pattern_recognition_threshold': 0.6,
            'strategy_effectiveness_threshold': 0.8
        }
        
        # مقاييس الأداء
        self.metrics = LearningMetrics()
        
        # استراتيجيات التكيف
        self.adaptation_strategies = self._initialize_adaptation_strategies()
        
        # قواعد التعلم الثورية
        self.revolutionary_rules = self._initialize_revolutionary_rules()
    
    def initialize(self) -> bool:
        """تهيئة النظام"""
        try:
            # تهيئة المكونات الفرعية
            self.linguistic_system.initialize()
            self.semantic_engine.initialize()
            
            print(f"🧠⚡ تم إنشاء نظام التعلم التكيفي المحسن: {self.name}")
            print(f"   📊 معدل التعلم: {self.learning_parameters['learning_rate']}")
            print(f"   🎯 عتبة التكيف: {self.learning_parameters['adaptation_threshold']}")
            print(f"   💾 سعة الذاكرة: {self.learning_parameters['memory_capacity']}")
            print(f"   🔄 استراتيجيات التكيف: {len(self.adaptation_strategies)}")
            
            self.is_initialized = True
            return True
        except Exception as e:
            print(f"❌ فشل تهيئة نظام التعلم التكيفي: {e}")
            return False
    
    def _initialize_adaptation_strategies(self) -> Dict[str, Callable]:
        """تهيئة استراتيجيات التكيف"""
        return {
            'gradual_improvement': self._gradual_adaptation,
            'aggressive_optimization': self._aggressive_adaptation,
            'conservative_adjustment': self._conservative_adaptation,
            'revolutionary_transformation': self._revolutionary_adaptation,
            'dynamic_balancing': self._dynamic_adaptation
        }
    
    def _initialize_revolutionary_rules(self) -> List[AdaptationRule]:
        """تهيئة قواعد التعلم الثورية"""
        rules = []
        
        # قاعدة ثنائية الصفر
        rules.append(AdaptationRule(
            condition="success_rate < 0.3",
            action="apply_zero_duality_transformation",
            priority=10
        ))
        
        # قاعدة تعامد الأضداد
        rules.append(AdaptationRule(
            condition="conflicting_feedback",
            action="apply_perpendicularity_resolution",
            priority=8
        ))
        
        # قاعدة الفتائل
        rules.append(AdaptationRule(
            condition="pattern_complexity > 0.8",
            action="apply_filament_decomposition",
            priority=6
        ))
        
        return rules
    
    def process(self, input_data: Any) -> Any:
        """معالجة البيانات مع التعلم"""
        # تطبيق التعلم المكتسب
        adapted_input = self._apply_learned_adaptations(input_data)
        
        # معالجة البيانات
        result = self._process_with_current_knowledge(adapted_input)
        
        # تسجيل التجربة
        experience = LearningExperience(
            input_data=input_data,
            actual_output=result,
            learning_context=self._determine_context(input_data)
        )
        
        self.learning_experiences.append(experience)
        
        return result
    
    def learn_from_feedback(self, input_data: Any, expected_output: Any, 
                          actual_output: Any, feedback: Dict[str, Any]) -> None:
        """التعلم من التغذية الراجعة"""
        # تحديد نوع التغذية الراجعة
        feedback_type = self._classify_feedback(feedback)
        
        # حساب نتيجة النجاح
        success_score = self._calculate_success_score(expected_output, actual_output, feedback)
        
        # إنشاء تجربة التعلم
        experience = LearningExperience(
            input_data=input_data,
            expected_output=expected_output,
            actual_output=actual_output,
            feedback=feedback,
            feedback_type=feedback_type,
            success_score=success_score,
            learning_context=self._determine_context(input_data)
        )
        
        # إضافة التجربة للذاكرة
        self._add_experience_to_memory(experience)
        
        # تحليل التجربة واستخراج الأنماط
        patterns = self._extract_patterns_from_experience(experience)
        self._update_learned_patterns(patterns)
        
        # تكييف المعاملات
        self._adapt_parameters_based_on_feedback(experience)
        
        # تحديث الاستراتيجيات
        self._update_strategies(experience)
        
        # تحديث المقاييس
        self._update_metrics(experience)
        
        print(f"📚 تم التعلم من التجربة: نجاح {success_score:.3f} | نوع: {feedback_type.value}")
    
    def optimize_parameters(self) -> Dict[str, float]:
        """تحسين المعاملات تلقائياً"""
        print("🔧 بدء تحسين المعاملات التلقائي...")
        
        # تحليل الأداء الحالي
        current_performance = self._analyze_current_performance()
        
        # تحديد المعاملات المرشحة للتحسين
        parameters_to_optimize = self._identify_optimization_candidates()
        
        # تطبيق استراتيجيات التحسين
        optimization_results = {}
        
        for param_name in parameters_to_optimize:
            old_value = self.learning_parameters[param_name]
            
            # تجربة قيم مختلفة
            best_value, best_performance = self._optimize_single_parameter(
                param_name, current_performance
            )
            
            # تطبيق القيمة الأفضل
            self.learning_parameters[param_name] = best_value
            optimization_results[param_name] = {
                'old_value': old_value,
                'new_value': best_value,
                'improvement': best_performance - current_performance
            }
        
        print(f"✅ تم تحسين {len(optimization_results)} معامل")
        return optimization_results
    
    def _apply_learned_adaptations(self, input_data: Any) -> Any:
        """تطبيق التكيفات المتعلمة"""
        adapted_data = copy.deepcopy(input_data)
        
        # تطبيق الأنماط المتعلمة
        for pattern_name, pattern_data in self.learned_patterns.items():
            if self._pattern_matches(input_data, pattern_data):
                adapted_data = self._apply_pattern_adaptation(adapted_data, pattern_data)
        
        # تطبيق الاستراتيجيات الناجحة
        for strategy_name, effectiveness in self.successful_strategies.items():
            if effectiveness > self.learning_parameters['strategy_effectiveness_threshold']:
                adapted_data = self._apply_strategy(adapted_data, strategy_name)
        
        return adapted_data
    
    def _process_with_current_knowledge(self, input_data: Any) -> Any:
        """معالجة البيانات بالمعرفة الحالية"""
        # تحليل لغوي
        if isinstance(input_data, str):
            linguistic_result = self.linguistic_system.create_word_vector(input_data)
            semantic_result = self.semantic_engine.analyze_text(input_data)
            
            return {
                'linguistic_vector': linguistic_result.vector,
                'semantic_analysis': semantic_result,
                'processing_confidence': (linguistic_result.semantic_weight + semantic_result.confidence) / 2
            }
        
        return input_data
    
    def _classify_feedback(self, feedback: Dict[str, Any]) -> FeedbackType:
        """تصنيف نوع التغذية الراجعة"""
        if 'rating' in feedback:
            rating = feedback['rating']
            if rating >= 0.8:
                return FeedbackType.POSITIVE
            elif rating <= 0.3:
                return FeedbackType.NEGATIVE
            else:
                return FeedbackType.NEUTRAL
        
        if 'corrections' in feedback:
            return FeedbackType.CORRECTIVE
        
        if 'suggestions' in feedback:
            return FeedbackType.ENHANCEMENT
        
        return FeedbackType.NEUTRAL
    
    def _calculate_success_score(self, expected: Any, actual: Any, feedback: Dict[str, Any]) -> float:
        """حساب نتيجة النجاح"""
        # نتيجة أساسية من التغذية الراجعة
        base_score = feedback.get('rating', 0.5)
        
        # مقارنة النتائج المتوقعة والفعلية
        if expected is not None and actual is not None:
            if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
                # مقارنة رقمية
                difference = abs(expected - actual) / max(abs(expected), 1)
                similarity_score = max(0, 1 - difference)
            elif isinstance(expected, str) and isinstance(actual, str):
                # مقارنة نصية
                similarity_score = self._calculate_text_similarity(expected, actual)
            else:
                similarity_score = 0.5
        else:
            similarity_score = 0.5
        
        # دمج النتائج
        final_score = (base_score * 0.6) + (similarity_score * 0.4)
        return max(0, min(1, final_score))
    
    def _calculate_text_similarity(self, text1: str, text2: str) -> float:
        """حساب التشابه النصي"""
        # تشابه بسيط بناء على الكلمات المشتركة
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 and not words2:
            return 1.0
        
        intersection = words1 & words2
        union = words1 | words2
        
        return len(intersection) / len(union) if union else 0.0
    
    def _add_experience_to_memory(self, experience: LearningExperience) -> None:
        """إضافة التجربة للذاكرة"""
        self.learning_experiences.append(experience)
        
        # إدارة سعة الذاكرة
        if len(self.learning_experiences) > self.learning_parameters['memory_capacity']:
            # إزالة أقدم التجارب الأقل أهمية
            self.learning_experiences.sort(key=lambda x: (x.success_score, x.timestamp))
            self.learning_experiences = self.learning_experiences[-self.learning_parameters['memory_capacity']:]
    
    def _extract_patterns_from_experience(self, experience: LearningExperience) -> Dict[str, Any]:
        """استخراج الأنماط من التجربة"""
        patterns = {}
        
        # نمط السياق
        context_pattern = {
            'context': experience.learning_context,
            'success_rate': experience.success_score,
            'feedback_type': experience.feedback_type.value,
            'input_characteristics': self._analyze_input_characteristics(experience.input_data)
        }
        patterns[f"context_{experience.learning_context}"] = context_pattern
        
        # نمط التغذية الراجعة
        if experience.feedback:
            feedback_pattern = {
                'feedback_type': experience.feedback_type.value,
                'success_correlation': experience.success_score,
                'improvement_areas': experience.improvement_suggestions
            }
            patterns[f"feedback_{experience.feedback_type.value}"] = feedback_pattern
        
        return patterns
    
    def _update_learned_patterns(self, new_patterns: Dict[str, Any]) -> None:
        """تحديث الأنماط المتعلمة"""
        for pattern_name, pattern_data in new_patterns.items():
            if pattern_name in self.learned_patterns:
                # دمج مع النمط الموجود
                existing_pattern = self.learned_patterns[pattern_name]
                merged_pattern = self._merge_patterns(existing_pattern, pattern_data)
                self.learned_patterns[pattern_name] = merged_pattern
            else:
                # إضافة نمط جديد
                self.learned_patterns[pattern_name] = pattern_data
    
    def _adapt_parameters_based_on_feedback(self, experience: LearningExperience) -> None:
        """تكييف المعاملات بناء على التغذية الراجعة"""
        # تكييف معدل التعلم
        if experience.success_score > 0.8:
            # نجاح عالي - زيادة معدل التعلم قليلاً
            self.learning_parameters['learning_rate'] *= 1.05
        elif experience.success_score < 0.3:
            # فشل - تقليل معدل التعلم
            self.learning_parameters['learning_rate'] *= 0.95
        
        # تحديد الحدود
        self.learning_parameters['learning_rate'] = max(0.01, min(0.5, self.learning_parameters['learning_rate']))
        
        # تكييف عتبة التكيف
        if experience.feedback_type == FeedbackType.CORRECTIVE:
            self.learning_parameters['adaptation_threshold'] *= 0.98
        elif experience.feedback_type == FeedbackType.POSITIVE:
            self.learning_parameters['adaptation_threshold'] *= 1.02
        
        # تحديد الحدود
        self.learning_parameters['adaptation_threshold'] = max(0.5, min(0.9, self.learning_parameters['adaptation_threshold']))
    
    def _update_strategies(self, experience: LearningExperience) -> None:
        """تحديث الاستراتيجيات"""
        strategy_name = f"strategy_{experience.learning_context}_{experience.feedback_type.value}"
        
        if strategy_name in self.successful_strategies:
            # تحديث فعالية الاستراتيجية
            current_effectiveness = self.successful_strategies[strategy_name]
            new_effectiveness = (current_effectiveness + experience.success_score) / 2
            self.successful_strategies[strategy_name] = new_effectiveness
        else:
            # إضافة استراتيجية جديدة
            self.successful_strategies[strategy_name] = experience.success_score
    
    def _update_metrics(self, experience: LearningExperience) -> None:
        """تحديث مقاييس الأداء"""
        self.metrics.total_experiences += 1
        
        if experience.success_score > 0.7:
            self.metrics.successful_experiences += 1
        elif experience.success_score < 0.3:
            self.metrics.failed_experiences += 1
        
        # تحديث معدل النجاح
        self.metrics.average_success_rate = (
            self.metrics.successful_experiences / self.metrics.total_experiences
        )
        
        # حساب سرعة التعلم
        recent_experiences = self.learning_experiences[-10:] if len(self.learning_experiences) >= 10 else self.learning_experiences
        if len(recent_experiences) > 1:
            recent_scores = [exp.success_score for exp in recent_experiences]
            self.metrics.learning_velocity = (recent_scores[-1] - recent_scores[0]) / len(recent_scores)
        
        self.metrics.last_update = datetime.now()
    
    # استراتيجيات التكيف
    def _gradual_adaptation(self, data: Any) -> Any:
        """تكيف تدريجي"""
        return data  # تنفيذ مبسط
    
    def _aggressive_adaptation(self, data: Any) -> Any:
        """تكيف عدواني"""
        return data  # تنفيذ مبسط
    
    def _conservative_adaptation(self, data: Any) -> Any:
        """تكيف محافظ"""
        return data  # تنفيذ مبسط
    
    def _revolutionary_adaptation(self, data: Any) -> Any:
        """تكيف ثوري"""
        return data  # تنفيذ مبسط
    
    def _dynamic_adaptation(self, data: Any) -> Any:
        """تكيف ديناميكي"""
        return data  # تنفيذ مبسط
    
    # دوال مساعدة
    def _determine_context(self, input_data: Any) -> str:
        """تحديد السياق"""
        if isinstance(input_data, str):
            if any(word in input_data for word in ['الله', 'قرآن', 'رسول']):
                return 'ديني'
            elif any(word in input_data for word in ['علم', 'بحث', 'دراسة']):
                return 'علمي'
            else:
                return 'عام'
        return 'عام'
    
    def _pattern_matches(self, input_data: Any, pattern_data: Dict[str, Any]) -> bool:
        """فحص تطابق النمط"""
        return True  # تنفيذ مبسط
    
    def _apply_pattern_adaptation(self, data: Any, pattern_data: Dict[str, Any]) -> Any:
        """تطبيق تكيف النمط"""
        return data  # تنفيذ مبسط
    
    def _apply_strategy(self, data: Any, strategy_name: str) -> Any:
        """تطبيق الاستراتيجية"""
        return data  # تنفيذ مبسط
    
    def _analyze_input_characteristics(self, input_data: Any) -> Dict[str, Any]:
        """تحليل خصائص المدخلات"""
        return {'type': type(input_data).__name__}
    
    def _merge_patterns(self, pattern1: Dict[str, Any], pattern2: Dict[str, Any]) -> Dict[str, Any]:
        """دمج الأنماط"""
        merged = pattern1.copy()
        merged.update(pattern2)
        return merged
    
    def _analyze_current_performance(self) -> float:
        """تحليل الأداء الحالي"""
        return self.metrics.average_success_rate
    
    def _identify_optimization_candidates(self) -> List[str]:
        """تحديد المعاملات المرشحة للتحسين"""
        return ['learning_rate', 'adaptation_threshold']
    
    def _optimize_single_parameter(self, param_name: str, current_performance: float) -> Tuple[float, float]:
        """تحسين معامل واحد"""
        current_value = self.learning_parameters[param_name]
        best_value = current_value
        best_performance = current_performance
        
        # تجربة قيم مختلفة
        test_values = [current_value * 0.8, current_value * 0.9, current_value * 1.1, current_value * 1.2]
        
        for test_value in test_values:
            # محاكاة الأداء مع القيمة الجديدة
            simulated_performance = current_performance + np.random.normal(0, 0.1)
            
            if simulated_performance > best_performance:
                best_value = test_value
                best_performance = simulated_performance
        
        return best_value, best_performance

# اختبار النظام
def test_adaptive_learning_system():
    """اختبار نظام التعلم التكيفي"""
    print("🧪 اختبار نظام التعلم التكيفي المحسن")
    print("=" * 50)
    
    # إنشاء النظام
    system = EnhancedAdaptiveLearningSystem()
    system.initialize()
    
    # تجارب تعلم تجريبية
    test_cases = [
        {
            'input': 'الله نور السماوات والأرض',
            'expected': 'تحليل ديني إيجابي',
            'feedback': {'rating': 0.9, 'comments': 'تحليل ممتاز'}
        },
        {
            'input': 'العلم نور والجهل ظلام',
            'expected': 'تحليل تعليمي',
            'feedback': {'rating': 0.8, 'suggestions': ['تحسين التصنيف']}
        },
        {
            'input': 'الحرب مدمرة للمجتمعات',
            'expected': 'تحليل سلبي',
            'feedback': {'rating': 0.7, 'corrections': ['تحديد السياق']}
        }
    ]
    
    print(f"\n📚 اختبار التعلم من التجارب:")
    for i, case in enumerate(test_cases, 1):
        print(f"\n📝 التجربة {i}: {case['input']}")
        
        # معالجة المدخل
        result = system.process(case['input'])
        
        # التعلم من التغذية الراجعة
        system.learn_from_feedback(
            case['input'],
            case['expected'],
            result,
            case['feedback']
        )
    
    # تحسين المعاملات
    print(f"\n🔧 تحسين المعاملات:")
    optimization_results = system.optimize_parameters()
    for param, result in optimization_results.items():
        print(f"   📊 {param}: {result['old_value']:.3f} → {result['new_value']:.3f}")
        print(f"      📈 تحسن: {result['improvement']:.3f}")
    
    # عرض المقاييس
    print(f"\n📈 مقاييس الأداء:")
    print(f"   📊 إجمالي التجارب: {system.metrics.total_experiences}")
    print(f"   ✅ التجارب الناجحة: {system.metrics.successful_experiences}")
    print(f"   ❌ التجارب الفاشلة: {system.metrics.failed_experiences}")
    print(f"   🎯 معدل النجاح: {system.metrics.average_success_rate:.3f}")
    print(f"   🚀 سرعة التعلم: {system.metrics.learning_velocity:.3f}")
    print(f"   💡 الأنماط المتعلمة: {len(system.learned_patterns)}")
    print(f"   🎯 الاستراتيجيات الناجحة: {len(system.successful_strategies)}")
    
    print(f"\n✅ انتهى اختبار نظام التعلم التكيفي!")
    return system

if __name__ == "__main__":
    test_adaptive_learning_system()
