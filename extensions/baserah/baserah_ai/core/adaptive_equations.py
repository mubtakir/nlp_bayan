"""
المعادلات المتكيفة الثورية - Adaptive Revolutionary Equations
============================================================

نظام معادلات قادر على التكيف الذاتي باستخدام النظريات الثلاث:
1. ثنائية الصفر (Zero Duality)
2. تعامد الأضداد (Perpendicular Opposites)
3. نظرية الفتائل (Filament Theory)

المؤلف: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import numpy as np
import uuid
import copy
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass, field
from enum import Enum


class AdaptationType(Enum):
    """أنواع التكيف المختلفة"""
    ZERO_DUALITY = "ثنائية_الصفر"
    PERPENDICULAR = "تعامد_الأضداد"
    FILAMENT = "نظرية_الفتائل"
    COMBINED = "تكيف_مركب"


class AdaptationTrigger(Enum):
    """محفزات التكيف"""
    PERFORMANCE = "عتبة_الأداء"
    ERROR = "تراكم_الأخطاء"
    PATTERN = "اكتشاف_نمط"
    TIME = "زمني"
    FEEDBACK = "تغذية_راجعة"


@dataclass
class AdaptationStep:
    """خطوة تكيف واحدة"""
    step_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)
    adaptation_type: AdaptationType = AdaptationType.ZERO_DUALITY
    trigger: AdaptationTrigger = AdaptationTrigger.PERFORMANCE
    
    # المعاملات قبل وبعد التكيف
    params_before: Dict[str, List[float]] = field(default_factory=dict)
    params_after: Dict[str, List[float]] = field(default_factory=dict)
    
    # مقاييس الأداء
    performance_before: float = 0.0
    performance_after: float = 0.0
    strength: float = 0.1
    
    description: str = ""
    success: bool = False


class AdaptiveEquation:
    """
    المعادلة المتكيفة الثورية
    
    تطبق قدرات التكيف الذاتي:
    - تطبيق النظريات الثلاث في التكيف
    - تعلم من الأخطاء والأنماط
    - تطوير المعاملات تلقائياً
    - حفظ تاريخ التكيف
    """
    
    def __init__(self, name: str, alpha: List[float] = None, 
                 k: List[float] = None, beta: List[float] = None):
        self.name = name
        self.creation_time = datetime.now()
        
        # المعاملات الأولية
        self.alpha = alpha or [1.0, 0.5, 0.3]
        self.k = k or [2.0, 3.0, 4.0]
        self.beta = beta or [0.1, 0.05, 0.02]
        
        # تاريخ التكيف
        self.history: List[AdaptationStep] = []
        self.performance_history: List[float] = []
        self.errors: List[float] = []
        
        # إعدادات التكيف
        self.enabled = True
        self.threshold = 0.1
        self.max_strength = 0.5
        self.learning_rate = 0.01
        
        # إحصائيات
        self.total_adaptations = 0
        self.successful = 0
        self.efficiency = 0.0
    
    def compute(self, x: np.ndarray) -> np.ndarray:
        """حساب المعادلة العامة للشكل"""
        result = np.zeros_like(x, dtype=float)
        
        for i in range(min(len(self.alpha), len(self.k), len(self.beta))):
            sigmoid = self.alpha[i] / (1 + np.exp(-self.k[i] * x))
            linear = self.beta[i] * x
            result += sigmoid + linear
        
        return result
    
    def evaluate(self, x: np.ndarray, target: np.ndarray = None) -> float:
        """تقييم أداء المعادلة"""
        result = self.compute(x)
        
        if target is not None:
            error = np.mean((result - target) ** 2)
            performance = 1.0 / (1.0 + error)
        else:
            performance = self._calculate_elegance()
        
        self.performance_history.append(performance)
        return performance
    
    def _calculate_elegance(self) -> float:
        """حساب الأناقة الرياضية"""
        zero_balance = self._zero_duality_balance()
        perp_harmony = self._perpendicular_harmony()
        filament_coherence = self._filament_coherence()
        return (zero_balance + perp_harmony + filament_coherence) / 3.0
    
    def _zero_duality_balance(self) -> float:
        """توازن ثنائية الصفر"""
        pos = sum(abs(x) for x in self.alpha if x > 0)
        neg = sum(abs(x) for x in self.alpha if x < 0)
        if pos + neg == 0:
            return 1.0
        return 1.0 - abs(pos - neg) / (pos + neg)
    
    def _perpendicular_harmony(self) -> float:
        """انسجام تعامد الأضداد"""
        if len(self.k) < 2:
            return 1.0
        harmony = 0.0
        count = 0
        for i in range(len(self.k)):
            for j in range(i + 1, len(self.k)):
                dot = self.k[i] * self.k[j]
                harmony += 1.0 / (1.0 + abs(dot))
                count += 1
        return harmony / count if count > 0 else 1.0
    
    def _filament_coherence(self) -> float:
        """تماسك الفتائل"""
        factors = []
        if len(self.alpha) == len(self.k):
            c = np.corrcoef(self.alpha, self.k)[0, 1]
            if not np.isnan(c):
                factors.append(abs(c))
        return np.mean(factors) if factors else 0.5

    def should_adapt(self, performance: float) -> Tuple[bool, Optional[AdaptationTrigger]]:
        """تحديد ما إذا كان يجب التكيف"""
        if not self.enabled:
            return False, None

        if performance < self.threshold:
            return True, AdaptationTrigger.PERFORMANCE

        if len(self.errors) > 5 and np.mean(self.errors[-5:]) > 0.2:
            return True, AdaptationTrigger.ERROR

        if len(self.performance_history) > 10:
            if np.std(self.performance_history[-10:]) < 0.01:
                return True, AdaptationTrigger.PATTERN

        return False, None

    def adapt_zero_duality(self, strength: float = 0.1) -> AdaptationStep:
        """تكيف باستخدام نظرية ثنائية الصفر"""
        step = AdaptationStep(
            adaptation_type=AdaptationType.ZERO_DUALITY,
            params_before={'alpha': copy.deepcopy(self.alpha),
                          'k': copy.deepcopy(self.k)},
            strength=strength
        )

        try:
            for i in range(len(self.alpha)):
                v = np.random.normal(0, strength)
                self.alpha[i] += v
                if i + 1 < len(self.alpha):
                    self.alpha[i + 1] -= v * 0.5

            step.params_after = {'alpha': copy.deepcopy(self.alpha),
                                'k': copy.deepcopy(self.k)}
            step.success = True
            step.description = "تكيف ثنائية الصفر: توازن المعاملات"
        except Exception as e:
            step.success = False
            step.description = f"فشل: {e}"

        return step

    def adapt_perpendicular(self, strength: float = 0.1) -> AdaptationStep:
        """تكيف باستخدام نظرية تعامد الأضداد"""
        step = AdaptationStep(
            adaptation_type=AdaptationType.PERPENDICULAR,
            params_before={'alpha': copy.deepcopy(self.alpha),
                          'k': copy.deepcopy(self.k)},
            strength=strength
        )

        try:
            for i in range(len(self.k)):
                angle = np.pi / 2 * np.random.uniform(0.8, 1.2)
                rotation = np.array([[np.cos(angle), -np.sin(angle)],
                                    [np.sin(angle), np.cos(angle)]])
                if i + 1 < len(self.k):
                    vec = np.array([self.k[i], self.k[i+1]])
                    rotated = rotation @ vec * strength
                    self.k[i] += rotated[0] * 0.1
                    self.k[i+1] += rotated[1] * 0.1

            step.params_after = {'alpha': copy.deepcopy(self.alpha),
                                'k': copy.deepcopy(self.k)}
            step.success = True
            step.description = "تكيف تعامدي: دوران المعاملات"
        except Exception as e:
            step.success = False
            step.description = f"فشل: {e}"

        return step

    def adapt(self, adapt_type: AdaptationType = None, strength: float = None) -> AdaptationStep:
        """تنفيذ عملية تكيف"""
        if strength is None:
            strength = min(self.learning_rate * (1 + len(self.history) * 0.1),
                          self.max_strength)

        if adapt_type is None or adapt_type == AdaptationType.ZERO_DUALITY:
            step = self.adapt_zero_duality(strength)
        elif adapt_type == AdaptationType.PERPENDICULAR:
            step = self.adapt_perpendicular(strength)
        else:
            step = self.adapt_zero_duality(strength)

        self.history.append(step)
        self.total_adaptations += 1
        if step.success:
            self.successful += 1

        self.efficiency = self.successful / self.total_adaptations if self.total_adaptations > 0 else 0.0
        return step

    def get_stats(self) -> Dict[str, Any]:
        """الحصول على إحصائيات التكيف"""
        return {
            "الاسم": self.name,
            "إجمالي_التكيفات": self.total_adaptations,
            "الناجحة": self.successful,
            "الكفاءة": f"{self.efficiency:.2%}",
            "المعاملات": {
                "alpha": self.alpha,
                "k": self.k,
                "beta": self.beta
            }
        }

