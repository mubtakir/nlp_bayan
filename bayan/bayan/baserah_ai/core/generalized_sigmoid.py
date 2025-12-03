"""
دوال سيغمويد المعممة - Generalized Sigmoid Functions
=====================================================

نظام متقدم لدوال سيغمويد مع أسس معقدة (جزء حقيقي + تخيلي)
يستخدم لرسم أشكال معقدة بدقة عالية

المعادلة الأساسية:
σ(x, a+bi) = 1 / (1 + e^(-(a+bi)*x))

حيث:
- a: الجزء الحقيقي من الأس
- b: الجزء التخيلي من الأس
- x: المتغير المستقل

المؤلف: باسل يحيى عبدالله
"""

import numpy as np
import math
from dataclasses import dataclass
from typing import Union, List, Optional
from enum import Enum


class SigmoidType(Enum):
    """أنواع دوال سيغمويد المختلفة"""
    STANDARD = "قياسي"       # σ(x) = 1 / (1 + e^(-x))
    GENERALIZED = "معمم"     # مع أس معقد
    SMOOTH = "ناعم"          # نسخة ناعمة
    SHARP = "حاد"            # نسخة حادة
    CHOPPED = "مقطوع"        # مع معامل القطع n


@dataclass
class ComplexExponent:
    """تمثيل الأس المعقد (a + bi)"""
    real: float  # الجزء الحقيقي (a)
    imag: float = 0.0  # الجزء التخيلي (b)
    
    def to_complex(self) -> complex:
        """تحويل إلى عدد معقد"""
        return complex(self.real, self.imag)
    
    def magnitude(self) -> float:
        """حساب القيمة المطلقة"""
        return math.sqrt(self.real**2 + self.imag**2)
    
    def phase(self) -> float:
        """حساب الزاوية (phase)"""
        return math.atan2(self.imag, self.real)


@dataclass
class SigmoidParameters:
    """معاملات دالة سيغمويد"""
    k: float = 1.0                    # الحدة (sharpness)
    x0: float = 0.0                   # نقطة المنتصف
    n: int = 1                        # معامل القطع (chopping)
    scale: float = 1.0                # معامل التحجيم
    shift_y: float = 0.0              # إزاحة عمودية
    exponent: Optional[ComplexExponent] = None
    sigmoid_type: SigmoidType = SigmoidType.GENERALIZED


class GeneralizedSigmoid:
    """
    فئة دالة سيغمويد المعممة
    
    تدعم:
    - أسس معقدة (جزء حقيقي + تخيلي)
    - معامل القطع n للتحكم في شكل المنحنى
    - معاملات متعددة (تحجيم، إزاحة)
    - أنواع مختلفة من السيغمويد
    
    الصيغة: σₙ(x; k, x₀) = 1 / (1 + e^(-k(x - x₀)^n))
    """
    
    def __init__(self, params: SigmoidParameters = None):
        self.params = params or SigmoidParameters()
        self.cache = {}
    
    def evaluate(self, x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        """
        حساب قيمة دالة سيغمويد المعممة
        
        σₙ(x; k, x₀) = scale / (1 + e^(-k(x - x₀)^n)) + shift_y
        """
        x = np.asarray(x, dtype=np.float64)
        
        # تطبيق الإزاحة الأفقية
        term = x - self.params.x0
        
        # تطبيق معامل القطع
        if self.params.n != 1:
            term = np.power(term, self.params.n)
        
        # حساب الأس
        exponent = -self.params.k * term
        
        # حساب السيغمويد
        result = self.params.scale / (1.0 + np.exp(exponent))
        
        # تطبيق الإزاحة العمودية
        result += self.params.shift_y
        
        return result
    
    def derivative(self, x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        """حساب المشتقة الأولى"""
        s = self.evaluate(x)
        return self.params.k * s * (self.params.scale - s) / self.params.scale
    
    def inverse(self, y: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        """حساب الدالة العكسية"""
        y = np.asarray(y, dtype=np.float64)
        y_shifted = y - self.params.shift_y
        
        # تجنب القسمة على صفر
        ratio = np.clip(y_shifted / (self.params.scale - y_shifted), 1e-10, 1e10)
        
        term = -np.log(ratio) / self.params.k
        
        if self.params.n != 1:
            term = np.sign(term) * np.power(np.abs(term), 1.0/self.params.n)
        
        return term + self.params.x0
    
    @staticmethod
    def standard(x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        """دالة سيغمويد القياسية"""
        return 1.0 / (1.0 + np.exp(-np.asarray(x)))
    
    @staticmethod
    def chopped(x: Union[float, np.ndarray], n: int, k: float = 1.0, 
                x0: float = 0.0) -> Union[float, np.ndarray]:
        """دالة سيغمويد المقطوعة"""
        x = np.asarray(x, dtype=np.float64)
        term = np.power(x - x0, n)
        return 1.0 / (1.0 + np.exp(-k * term))
    
    def get_info(self) -> dict:
        """معلومات عن الدالة"""
        return {
            "النوع": self.params.sigmoid_type.value,
            "الحدة_k": self.params.k,
            "المركز_x0": self.params.x0,
            "معامل_القطع_n": self.params.n,
            "التحجيم": self.params.scale,
            "الإزاحة": self.params.shift_y
        }

