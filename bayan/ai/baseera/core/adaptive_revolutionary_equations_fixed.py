#!/usr/bin/env python3
"""
المعادلات المتكيفة الثورية - Adaptive Revolutionary Equations (إصدار مُصحح)
نظام بصيرة المتكامل

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import numpy as np
import matplotlib.pyplot as plt
import json
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass, field
from enum import Enum
import copy

class AdaptationType(Enum):
    """أنواع التكيف المختلفة"""
    ZERO_DUALITY = "zero_duality"
    PERPENDICULAR_OPPOSITES = "perpendicular_opposites"
    FILAMENT_THEORY = "filament_theory"
    COMBINED_ADAPTATION = "combined_adaptation"

class AdaptationTrigger(Enum):
    """محفزات التكيف"""
    PERFORMANCE_THRESHOLD = "performance_threshold"
    ERROR_ACCUMULATION = "error_accumulation"
    PATTERN_DETECTION = "pattern_detection"
    TIME_BASED = "time_based"
    USER_FEEDBACK = "user_feedback"

@dataclass
class AdaptationStep:
    """خطوة تكيف واحدة"""
    step_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)
    adaptation_type: AdaptationType = AdaptationType.ZERO_DUALITY
    trigger: AdaptationTrigger = AdaptationTrigger.PERFORMANCE_THRESHOLD
    
    # المعاملات قبل التكيف
    alpha_before: List[float] = field(default_factory=list)
    k_before: List[float] = field(default_factory=list)
    beta_before: List[float] = field(default_factory=list)
    
    # المعاملات بعد التكيف
    alpha_after: List[float] = field(default_factory=list)
    k_after: List[float] = field(default_factory=list)
    beta_after: List[float] = field(default_factory=list)
    
    # مقاييس الأداء
    performance_before: float = 0.0
    performance_after: float = 0.0
    adaptation_strength: float = 0.1
    
    # معلومات إضافية
    description: str = ""
    success: bool = False

class AdaptiveRevolutionaryEquation:
    """
    المعادلة الثورية المتكيفة
    
    تطبق قدرات التكيف الذاتي:
    - تطبيق النظريات الثلاث في التكيف
    - تعلم من الأخطاء والأنماط
    - تطوير المعاملات تلقائياً
    - حفظ تاريخ التكيف
    """
    
    def __init__(self, name: str, initial_alpha: List[float] = None, 
                 initial_k: List[float] = None, initial_beta: List[float] = None):
        self.name = name
        self.creation_time = datetime.now()
        
        # المعاملات الأولية
        self.alpha = initial_alpha or [1.0, 0.5, 0.3]
        self.k = initial_k or [2.0, 3.0, 4.0]
        self.beta = initial_beta or [0.1, 0.05, 0.02]
        
        # تاريخ التكيف
        self.adaptation_history: List[AdaptationStep] = []
        self.performance_history: List[float] = []
        self.error_accumulation: List[float] = []
        
        # إعدادات التكيف
        self.adaptation_enabled = True
        self.adaptation_threshold = 0.1
        self.max_adaptation_strength = 0.5
        self.learning_rate = 0.01
        
        # إحصائيات
        self.total_adaptations = 0
        self.successful_adaptations = 0
        self.adaptation_efficiency = 0.0
        
        print(f"🧬⚡ تم إنشاء معادلة متكيفة: {name}")
        print(f"   📊 معاملات أولية: α={self.alpha}, k={self.k}, β={self.beta}")
    
    def compute_general_shape_equation(self, x_data: np.ndarray) -> np.ndarray:
        """حساب المعادلة العامة للشكل"""
        result = np.zeros_like(x_data, dtype=float)
        
        # تطبيق المعادلة: f(x) = Σ(αᵢ·σ(x;kᵢ,x₀ᵢ) + βᵢx + γᵢ)
        for i in range(min(len(self.alpha), len(self.k), len(self.beta))):
            # دالة السيجمويد
            sigmoid_part = self.alpha[i] / (1 + np.exp(-self.k[i] * x_data))
            
            # الجزء الخطي
            linear_part = self.beta[i] * x_data
            
            result += sigmoid_part + linear_part
        
        return result
    
    def evaluate_performance(self, x_data: np.ndarray, target_data: np.ndarray = None) -> float:
        """تقييم أداء المعادلة الحالية"""
        try:
            # حساب النتيجة الحالية
            result = self.compute_general_shape_equation(x_data)
            
            if target_data is not None:
                # حساب الخطأ مقارنة بالهدف
                error = np.mean((result - target_data) ** 2)
                performance = 1.0 / (1.0 + error)
            else:
                # تقييم بناءً على الخصائص الرياضية
                smoothness = self._calculate_smoothness(result)
                elegance = self._calculate_mathematical_elegance()
                performance = (smoothness + elegance) / 2.0
            
            self.performance_history.append(performance)
            return performance
            
        except Exception as e:
            print(f"❌ خطأ في تقييم الأداء: {e}")
            return 0.0
    
    def _calculate_smoothness(self, data: np.ndarray) -> float:
        """حساب نعومة البيانات"""
        if len(data) < 2:
            return 1.0
        
        # حساب التغيرات
        differences = np.diff(data)
        smoothness = 1.0 / (1.0 + np.std(differences))
        return min(smoothness, 1.0)
    
    def _calculate_mathematical_elegance(self) -> float:
        """حساب الأناقة الرياضية للمعاملات"""
        # تطبيق نظرية ثنائية الصفر
        zero_balance = self._calculate_zero_duality_balance()
        
        # تطبيق نظرية تعامد الأضداد
        perpendicular_harmony = self._calculate_perpendicular_harmony()
        
        # تطبيق نظرية الفتائل
        filament_coherence = self._calculate_filament_coherence()
        
        elegance = (zero_balance + perpendicular_harmony + filament_coherence) / 3.0
        return elegance
    
    def _calculate_zero_duality_balance(self) -> float:
        """حساب توازن ثنائية الصفر"""
        # مجموع المعاملات الموجبة والسالبة
        positive_sum = sum(abs(x) for x in self.alpha if x > 0)
        negative_sum = sum(abs(x) for x in self.alpha if x < 0)
        
        if positive_sum + negative_sum == 0:
            return 1.0
        
        balance = 1.0 - abs(positive_sum - negative_sum) / (positive_sum + negative_sum)
        return max(balance, 0.0)
    
    def _calculate_perpendicular_harmony(self) -> float:
        """حساب انسجام تعامد الأضداد"""
        if len(self.k) < 2:
            return 1.0
        
        # حساب التعامد بين المعاملات
        harmony_sum = 0.0
        count = 0
        
        for i in range(len(self.k)):
            for j in range(i + 1, len(self.k)):
                # حساب درجة التعامد
                dot_product = self.k[i] * self.k[j]
                perpendicularity = 1.0 / (1.0 + abs(dot_product))
                harmony_sum += perpendicularity
                count += 1
        
        return harmony_sum / count if count > 0 else 1.0
    
    def _calculate_filament_coherence(self) -> float:
        """حساب تماسك الفتائل"""
        # حساب الترابط بين المعاملات
        coherence_factors = []
        
        # ترابط alpha-k
        if len(self.alpha) == len(self.k):
            alpha_k_coherence = np.corrcoef(self.alpha, self.k)[0, 1]
            if not np.isnan(alpha_k_coherence):
                coherence_factors.append(abs(alpha_k_coherence))
        
        # ترابط k-beta
        if len(self.k) == len(self.beta):
            k_beta_coherence = np.corrcoef(self.k, self.beta)[0, 1]
            if not np.isnan(k_beta_coherence):
                coherence_factors.append(abs(k_beta_coherence))
        
        return np.mean(coherence_factors) if coherence_factors else 0.5
    
    def should_adapt(self, current_performance: float) -> Tuple[bool, AdaptationTrigger]:
        """تحديد ما إذا كان يجب التكيف"""
        if not self.adaptation_enabled:
            return False, None
        
        # فحص عتبة الأداء
        if current_performance < self.adaptation_threshold:
            return True, AdaptationTrigger.PERFORMANCE_THRESHOLD
        
        # فحص تراكم الأخطاء
        if len(self.error_accumulation) > 5:
            recent_errors = self.error_accumulation[-5:]
            if np.mean(recent_errors) > 0.2:
                return True, AdaptationTrigger.ERROR_ACCUMULATION
        
        # فحص اكتشاف الأنماط
        if len(self.performance_history) > 10:
            recent_performance = self.performance_history[-10:]
            if np.std(recent_performance) < 0.01:  # أداء مستقر
                return True, AdaptationTrigger.PATTERN_DETECTION
        
        return False, None
    
    def adapt_zero_duality(self, adaptation_strength: float = 0.1) -> AdaptationStep:
        """تكيف باستخدام نظرية ثنائية الصفر"""
        step = AdaptationStep(
            adaptation_type=AdaptationType.ZERO_DUALITY,
            trigger=AdaptationTrigger.PERFORMANCE_THRESHOLD,
            alpha_before=copy.deepcopy(self.alpha),
            k_before=copy.deepcopy(self.k),
            beta_before=copy.deepcopy(self.beta),
            adaptation_strength=adaptation_strength
        )
        
        try:
            # تطبيق ثنائية الصفر: كل معامل له ضده
            for i in range(len(self.alpha)):
                # إضافة تنويع يحافظ على التوازن
                variation = np.random.normal(0, adaptation_strength)
                self.alpha[i] += variation
                
                # إضافة ضد التنويع في معامل آخر للحفاظ على التوازن
                if i + 1 < len(self.alpha):
                    self.alpha[i + 1] -= variation * 0.5
            
            # تطبيق نفس المبدأ على k
            for i in range(len(self.k)):
                variation = np.random.normal(0, adaptation_strength * 0.5)
                self.k[i] += variation
                if i + 1 < len(self.k):
                    self.k[i + 1] -= variation * 0.3
            
            step.alpha_after = copy.deepcopy(self.alpha)
            step.k_after = copy.deepcopy(self.k)
            step.beta_after = copy.deepcopy(self.beta)
            step.success = True
            step.description = "تكيف ثنائية الصفر: توازن المعاملات الموجبة والسالبة"
            
        except Exception as e:
            step.success = False
            step.description = f"فشل تكيف ثنائية الصفر: {e}"
        
        return step
    
    def perform_adaptation(self, adaptation_type: AdaptationType = None, 
                          adaptation_strength: float = None) -> AdaptationStep:
        """تنفيذ عملية تكيف"""
        if adaptation_strength is None:
            adaptation_strength = min(self.learning_rate * (1 + len(self.adaptation_history) * 0.1), 
                                    self.max_adaptation_strength)
        
        # اختيار نوع التكيف
        if adaptation_type is None:
            adaptation_type = AdaptationType.ZERO_DUALITY
        
        # تنفيذ التكيف
        step = self.adapt_zero_duality(adaptation_strength)
        
        # حفظ الخطوة
        self.adaptation_history.append(step)
        self.total_adaptations += 1
        if step.success:
            self.successful_adaptations += 1
        
        # تحديث الإحصائيات
        self.adaptation_efficiency = self.successful_adaptations / self.total_adaptations if self.total_adaptations > 0 else 0.0
        
        print(f"🔄 تكيف {adaptation_type.value}: {'نجح' if step.success else 'فشل'}")
        print(f"   📊 قوة التكيف: {adaptation_strength:.3f}")
        print(f"   📈 كفاءة التكيف: {self.adaptation_efficiency:.3f}")
        
        return step
    
    def auto_adapt(self, x_data: np.ndarray, target_data: np.ndarray = None, 
                   max_iterations: int = 5) -> List[AdaptationStep]:
        """تكيف تلقائي ذكي"""
        adaptation_steps = []
        
        print(f"🤖 بدء التكيف التلقائي (حد أقصى {max_iterations} تكرار)")
        
        for iteration in range(max_iterations):
            # تقييم الأداء الحالي
            current_performance = self.evaluate_performance(x_data, target_data)
            
            # فحص الحاجة للتكيف
            should_adapt, trigger = self.should_adapt(current_performance)
            
            if not should_adapt:
                print(f"   ✅ التكرار {iteration + 1}: لا حاجة للتكيف (أداء: {current_performance:.3f})")
                break
            
            # تنفيذ التكيف
            step = self.perform_adaptation()
            step.trigger = trigger
            step.performance_before = current_performance
            
            # تقييم الأداء بعد التكيف
            new_performance = self.evaluate_performance(x_data, target_data)
            step.performance_after = new_performance
            
            adaptation_steps.append(step)
            
            print(f"   🔄 التكرار {iteration + 1}: {current_performance:.3f} → {new_performance:.3f}")
            
            # فحص التحسن
            if new_performance < current_performance:
                print(f"   ⚠️  تراجع الأداء، إيقاف التكيف")
                break
        
        print(f"🏁 انتهى التكيف التلقائي: {len(adaptation_steps)} خطوات")
        return adaptation_steps

# ==================== اختبار المعادلات المتكيفة ====================

def test_adaptive_equations():
    """اختبار شامل للمعادلات المتكيفة"""
    print("🧪 اختبار المعادلات المتكيفة الثورية")
    print("="*60)
    
    # إنشاء معادلة متكيفة
    adaptive_eq = AdaptiveRevolutionaryEquation(
        "TestAdaptive",
        initial_alpha=[1.0, 0.5, 0.3],
        initial_k=[2.0, 3.0, 4.0],
        initial_beta=[0.1, 0.05, 0.02]
    )
    
    # بيانات اختبار
    x_test = np.linspace(0, 2*np.pi, 100)
    target_circle = np.sin(x_test)  # هدف بسيط
    
    print(f"\n📊 الأداء الأولي:")
    initial_performance = adaptive_eq.evaluate_performance(x_test, target_circle)
    print(f"   الأداء: {initial_performance:.4f}")
    
    # اختبار التكيف
    print(f"\n🔄 اختبار التكيف:")
    step = adaptive_eq.adapt_zero_duality(0.1)
    print(f"   النتيجة: {'نجح' if step.success else 'فشل'}")
    print(f"   الوصف: {step.description}")
    
    # اختبار التكيف التلقائي
    print(f"\n🤖 اختبار التكيف التلقائي:")
    auto_steps = adaptive_eq.auto_adapt(x_test, target_circle, max_iterations=3)
    print(f"   تم تنفيذ {len(auto_steps)} خطوات تكيف تلقائي")
    
    # تقرير نهائي
    print(f"\n📋 التقرير النهائي:")
    final_performance = adaptive_eq.evaluate_performance(x_test, target_circle)
    print(f"   الأداء النهائي: {final_performance:.4f}")
    print(f"   التحسن: {final_performance - initial_performance:.4f}")
    print(f"   إجمالي خطوات التكيف: {adaptive_eq.total_adaptations}")
    print(f"   كفاءة التكيف: {adaptive_eq.adaptation_efficiency:.3f}")
    
    print(f"\n✅ انتهى اختبار المعادلات المتكيفة!")
    return adaptive_eq

if __name__ == "__main__":
    test_adaptive_equations()

