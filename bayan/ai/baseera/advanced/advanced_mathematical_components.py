#!/usr/bin/env python3
"""
المكونات الرياضية المتقدمة - Advanced Mathematical Components
نظام بصيرة المتكامل

🧮 مكونات رياضية متقدمة للحسابات المعقدة
📐 دوال رياضية متخصصة للنظريات الثورية
⚡ حسابات محسنة للأداء العالي

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Any, Optional, Union, Callable
from dataclasses import dataclass, field
from enum import Enum
import time
import cmath
import math

class MathematicalDomain(Enum):
    """المجالات الرياضية"""
    REAL = "real"
    COMPLEX = "complex"
    INTEGER = "integer"
    RATIONAL = "rational"
    TRANSCENDENTAL = "transcendental"

class CalculationPrecision(Enum):
    """دقة الحسابات"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    ULTRA_HIGH = "ultra_high"
    REVOLUTIONARY = "revolutionary"

@dataclass
class MathematicalResult:
    """نتيجة رياضية"""
    value: Union[float, complex, np.ndarray]
    precision: float
    computation_time: float
    domain: MathematicalDomain
    metadata: Dict[str, Any] = field(default_factory=dict)
    revolutionary_theories_applied: List[str] = field(default_factory=list)

class AdvancedMathematicalComponents:
    """
    المكونات الرياضية المتقدمة
    
    🧮 مجموعة شاملة من الدوال الرياضية المتقدمة:
    - دوال السيجمويد المعممة والمتقدمة
    - دوال التكامل والتفاضل العددي
    - حل المعادلات التفاضلية
    - تحليل فورييه والتحويلات الرياضية
    - الجبر الخطي المتقدم
    - نظرية الأعداد والدوال الخاصة
    """
    
    def __init__(self, precision: CalculationPrecision = CalculationPrecision.HIGH):
        self.precision = precision
        self.creation_time = time.time()
        
        # معاملات الدقة
        self.precision_settings = {
            CalculationPrecision.LOW: {"rtol": 1e-3, "atol": 1e-6, "max_iter": 100},
            CalculationPrecision.MEDIUM: {"rtol": 1e-6, "atol": 1e-9, "max_iter": 500},
            CalculationPrecision.HIGH: {"rtol": 1e-9, "atol": 1e-12, "max_iter": 1000},
            CalculationPrecision.ULTRA_HIGH: {"rtol": 1e-12, "atol": 1e-15, "max_iter": 5000},
            CalculationPrecision.REVOLUTIONARY: {"rtol": 1e-15, "atol": 1e-18, "max_iter": 10000}
        }
        
        # إحصائيات الأداء
        self.total_calculations = 0
        self.total_computation_time = 0.0
        self.average_precision = 0.0
        
        print(f"🧮⚡ تم إنشاء المكونات الرياضية المتقدمة")
        print(f"   📊 دقة الحسابات: {precision.value}")
        print(f"   ⚙️ إعدادات الدقة: {self.precision_settings[precision]}")
    
    def revolutionary_sigmoid(self, x: Union[float, np.ndarray], 
                            alpha: float = 1.0, k: float = 1.0, x0: float = 0.0,
                            revolutionary_mode: bool = True) -> MathematicalResult:
        """دالة السيجمويد الثورية المتقدمة"""
        start_time = time.time()
        
        if isinstance(x, (int, float)):
            x = np.array([x])
            single_value = True
        else:
            x = np.asarray(x)
            single_value = False
        
        # تطبيق النظريات الثورية
        theories_applied = []
        
        if revolutionary_mode:
            # تطبيق نظرية ثنائية الصفر
            zero_duality_factor = self._apply_zero_duality_sigmoid(x, x0)
            theories_applied.append("Zero Duality Theory")
            
            # تطبيق نظرية تعامد الأضداد
            perpendicular_factor = self._apply_perpendicular_opposites_sigmoid(x, k)
            theories_applied.append("Perpendicular Opposites Theory")
            
            # تطبيق نظرية الفتائل
            filament_factor = self._apply_filament_theory_sigmoid(x, alpha)
            theories_applied.append("Filament Theory")
            
            # دمج النظريات
            enhanced_alpha = alpha * zero_duality_factor
            enhanced_k = k * perpendicular_factor
            enhanced_x0 = x0 + filament_factor
        else:
            enhanced_alpha, enhanced_k, enhanced_x0 = alpha, k, x0
        
        # حساب السيجمويد المحسن
        try:
            # تجنب overflow
            z = -enhanced_k * (x - enhanced_x0)
            z = np.clip(z, -500, 500)  # تجنب overflow
            
            result_values = enhanced_alpha / (1 + np.exp(z))
            
            if single_value:
                result_values = result_values[0]
            
        except (OverflowError, RuntimeWarning):
            # معالجة الحالات الحدية
            result_values = np.where(z > 0, 0, enhanced_alpha)
            if single_value:
                result_values = result_values[0]
        
        computation_time = time.time() - start_time
        precision = self._calculate_precision(result_values)
        
        # تحديث الإحصائيات
        self._update_statistics(computation_time, precision)
        
        return MathematicalResult(
            value=result_values,
            precision=precision,
            computation_time=computation_time,
            domain=MathematicalDomain.REAL,
            metadata={
                "alpha": enhanced_alpha,
                "k": enhanced_k,
                "x0": enhanced_x0,
                "revolutionary_mode": revolutionary_mode
            },
            revolutionary_theories_applied=theories_applied
        )
    
    def _apply_zero_duality_sigmoid(self, x: np.ndarray, x0: float) -> float:
        """تطبيق نظرية ثنائية الصفر على السيجمويد"""
        # حساب التوازن حول النقطة المرجعية
        positive_region = np.sum(x > x0)
        negative_region = np.sum(x <= x0)
        total_points = len(x)
        
        if total_points == 0:
            return 1.0
        
        balance = 1.0 - abs(positive_region - negative_region) / total_points
        return 0.5 + 0.5 * balance  # تعديل بين 0.5 و 1.0
    
    def _apply_perpendicular_opposites_sigmoid(self, x: np.ndarray, k: float) -> float:
        """تطبيق نظرية تعامد الأضداد على السيجمويد"""
        # حساب التنوع في القيم
        if len(x) < 2:
            return 1.0
        
        x_range = np.max(x) - np.min(x)
        x_std = np.std(x)
        
        if x_range == 0:
            return 1.0
        
        diversity = min(x_std / x_range, 1.0)
        return 0.7 + 0.3 * diversity  # تعديل بين 0.7 و 1.0
    
    def _apply_filament_theory_sigmoid(self, x: np.ndarray, alpha: float) -> float:
        """تطبيق نظرية الفتائل على السيجمويد"""
        # حساب الترابط في البيانات
        if len(x) < 2:
            return 0.0
        
        # حساب الارتباط التسلسلي
        correlations = []
        for i in range(len(x) - 1):
            if x[i+1] != x[i]:
                correlation = abs(x[i+1] - x[i]) / (abs(x[i+1]) + abs(x[i]) + 1e-10)
                correlations.append(correlation)
        
        if not correlations:
            return 0.0
        
        avg_correlation = np.mean(correlations)
        return 0.1 * avg_correlation  # تعديل صغير
    
    def revolutionary_linear(self, x: Union[float, np.ndarray], 
                           beta: float = 1.0, gamma: float = 0.0,
                           revolutionary_mode: bool = True) -> MathematicalResult:
        """الدالة الخطية الثورية المتقدمة"""
        start_time = time.time()
        
        if isinstance(x, (int, float)):
            x = np.array([x])
            single_value = True
        else:
            x = np.asarray(x)
            single_value = False
        
        theories_applied = []
        
        if revolutionary_mode:
            # تطبيق النظريات الثورية على الدالة الخطية
            zero_duality_adjustment = self._apply_zero_duality_linear(x, gamma)
            perpendicular_slope = self._apply_perpendicular_linear(x, beta)
            filament_intercept = self._apply_filament_linear(x, gamma)
            
            theories_applied = ["Zero Duality Theory", "Perpendicular Opposites Theory", "Filament Theory"]
            
            enhanced_beta = beta * perpendicular_slope
            enhanced_gamma = gamma + zero_duality_adjustment + filament_intercept
        else:
            enhanced_beta, enhanced_gamma = beta, gamma
        
        # حساب الدالة الخطية المحسنة
        result_values = enhanced_beta * x + enhanced_gamma
        
        if single_value:
            result_values = result_values[0]
        
        computation_time = time.time() - start_time
        precision = self._calculate_precision(result_values)
        
        self._update_statistics(computation_time, precision)
        
        return MathematicalResult(
            value=result_values,
            precision=precision,
            computation_time=computation_time,
            domain=MathematicalDomain.REAL,
            metadata={
                "beta": enhanced_beta,
                "gamma": enhanced_gamma,
                "revolutionary_mode": revolutionary_mode
            },
            revolutionary_theories_applied=theories_applied
        )
    
    def _apply_zero_duality_linear(self, x: np.ndarray, gamma: float) -> float:
        """تطبيق ثنائية الصفر على الدالة الخطية"""
        if len(x) == 0:
            return 0.0
        
        mean_x = np.mean(x)
        return 0.1 * (gamma - mean_x)  # تعديل صغير للتوازن
    
    def _apply_perpendicular_linear(self, x: np.ndarray, beta: float) -> float:
        """تطبيق تعامد الأضداد على الميل"""
        if len(x) < 2:
            return 1.0
        
        # حساب التغير في البيانات
        x_diff = np.diff(x)
        if len(x_diff) == 0:
            return 1.0
        
        variation = np.std(x_diff)
        return 0.9 + 0.1 * min(variation, 1.0)
    
    def _apply_filament_linear(self, x: np.ndarray, gamma: float) -> float:
        """تطبيق الفتائل على المقطع"""
        if len(x) < 2:
            return 0.0
        
        # حساب الترابط الخطي
        linear_trend = np.polyfit(range(len(x)), x, 1)[0] if len(x) > 1 else 0
        return 0.05 * linear_trend
    
    def revolutionary_general_form(self, x: Union[float, np.ndarray],
                                 alpha_list: List[float] = None,
                                 k_list: List[float] = None,
                                 x0_list: List[float] = None,
                                 beta_list: List[float] = None,
                                 gamma_list: List[float] = None) -> MathematicalResult:
        """معادلة الشكل العام الثورية: f(x) = Σ(αᵢ·σ(x;kᵢ,x₀ᵢ) + βᵢx + γᵢ)"""
        start_time = time.time()
        
        # القيم الافتراضية
        if alpha_list is None:
            alpha_list = [1.0, 0.5, 0.3]
        if k_list is None:
            k_list = [2.0, 3.0, 4.0]
        if x0_list is None:
            x0_list = [0.0, 1.0, -1.0]
        if beta_list is None:
            beta_list = [0.1, 0.05, 0.02]
        if gamma_list is None:
            gamma_list = [0.0, 0.1, -0.1]
        
        # توحيد الأطوال
        max_len = max(len(alpha_list), len(k_list), len(x0_list), len(beta_list), len(gamma_list))
        
        def extend_list(lst, target_len):
            if len(lst) < target_len:
                return lst + [lst[-1]] * (target_len - len(lst))
            return lst[:target_len]
        
        alpha_list = extend_list(alpha_list, max_len)
        k_list = extend_list(k_list, max_len)
        x0_list = extend_list(x0_list, max_len)
        beta_list = extend_list(beta_list, max_len)
        gamma_list = extend_list(gamma_list, max_len)
        
        if isinstance(x, (int, float)):
            x = np.array([x])
            single_value = True
        else:
            x = np.asarray(x)
            single_value = False
        
        # حساب المعادلة العامة
        result_values = np.zeros_like(x, dtype=float)
        
        for i in range(max_len):
            # الجزء السيجمويدي
            sigmoid_result = self.revolutionary_sigmoid(
                x, alpha_list[i], k_list[i], x0_list[i], revolutionary_mode=True
            )
            
            # الجزء الخطي
            linear_result = self.revolutionary_linear(
                x, beta_list[i], gamma_list[i], revolutionary_mode=True
            )
            
            # دمج النتائج
            result_values += sigmoid_result.value + linear_result.value
        
        if single_value:
            result_values = result_values[0]
        
        computation_time = time.time() - start_time
        precision = self._calculate_precision(result_values)
        
        self._update_statistics(computation_time, precision)
        
        return MathematicalResult(
            value=result_values,
            precision=precision,
            computation_time=computation_time,
            domain=MathematicalDomain.REAL,
            metadata={
                "components": max_len,
                "alpha_list": alpha_list,
                "k_list": k_list,
                "x0_list": x0_list,
                "beta_list": beta_list,
                "gamma_list": gamma_list
            },
            revolutionary_theories_applied=["Zero Duality Theory", "Perpendicular Opposites Theory", "Filament Theory"]
        )
    
    def numerical_derivative(self, func: Callable, x: float, h: float = None) -> MathematicalResult:
        """حساب المشتقة العددية بدقة عالية"""
        start_time = time.time()
        
        if h is None:
            h = self.precision_settings[self.precision]["rtol"] ** 0.5
        
        # استخدام طريقة الفروق المركزية للدقة العالية
        try:
            derivative = (func(x + h) - func(x - h)) / (2 * h)
        except:
            # في حالة الفشل، استخدم الفروق الأمامية
            derivative = (func(x + h) - func(x)) / h
        
        computation_time = time.time() - start_time
        precision = abs(h)  # دقة تقريبية
        
        self._update_statistics(computation_time, precision)
        
        return MathematicalResult(
            value=derivative,
            precision=precision,
            computation_time=computation_time,
            domain=MathematicalDomain.REAL,
            metadata={"method": "central_difference", "step_size": h}
        )
    
    def numerical_integral(self, func: Callable, a: float, b: float, 
                          method: str = "simpson") -> MathematicalResult:
        """حساب التكامل العددي بطرق متقدمة"""
        start_time = time.time()
        
        n = self.precision_settings[self.precision]["max_iter"]
        
        if method == "simpson":
            result = self._simpson_rule(func, a, b, n)
        elif method == "trapezoidal":
            result = self._trapezoidal_rule(func, a, b, n)
        elif method == "gaussian":
            result = self._gaussian_quadrature(func, a, b, n)
        else:
            result = self._simpson_rule(func, a, b, n)  # افتراضي
        
        computation_time = time.time() - start_time
        precision = abs(b - a) / n  # دقة تقريبية
        
        self._update_statistics(computation_time, precision)
        
        return MathematicalResult(
            value=result,
            precision=precision,
            computation_time=computation_time,
            domain=MathematicalDomain.REAL,
            metadata={"method": method, "intervals": n, "bounds": [a, b]}
        )
    
    def _simpson_rule(self, func: Callable, a: float, b: float, n: int) -> float:
        """قاعدة سيمبسون للتكامل"""
        if n % 2 == 1:
            n += 1  # يجب أن يكون زوجي
        
        h = (b - a) / n
        x = np.linspace(a, b, n + 1)
        y = np.array([func(xi) for xi in x])
        
        return h / 3 * (y[0] + 4 * np.sum(y[1::2]) + 2 * np.sum(y[2:-1:2]) + y[-1])
    
    def _trapezoidal_rule(self, func: Callable, a: float, b: float, n: int) -> float:
        """قاعدة شبه المنحرف للتكامل"""
        h = (b - a) / n
        x = np.linspace(a, b, n + 1)
        y = np.array([func(xi) for xi in x])
        
        return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])
    
    def _gaussian_quadrature(self, func: Callable, a: float, b: float, n: int) -> float:
        """التكامل بطريقة جاوس"""
        # تحويل المجال إلى [-1, 1]
        def transformed_func(t):
            x = 0.5 * (b - a) * t + 0.5 * (b + a)
            return func(x) * 0.5 * (b - a)
        
        # نقاط ووزن جاوس (مبسط لـ n=5)
        points = [-0.9061798459, -0.5384693101, 0.0, 0.5384693101, 0.9061798459]
        weights = [0.2369268851, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268851]
        
        result = 0.0
        for i in range(min(len(points), n)):
            result += weights[i] * transformed_func(points[i])
        
        return result
    
    def solve_ode(self, func: Callable, y0: float, t_span: Tuple[float, float], 
                  method: str = "rk4") -> MathematicalResult:
        """حل المعادلات التفاضلية العادية"""
        start_time = time.time()
        
        t_start, t_end = t_span
        n_steps = self.precision_settings[self.precision]["max_iter"] // 10
        h = (t_end - t_start) / n_steps
        
        t = np.linspace(t_start, t_end, n_steps + 1)
        y = np.zeros(n_steps + 1)
        y[0] = y0
        
        if method == "rk4":
            for i in range(n_steps):
                k1 = h * func(t[i], y[i])
                k2 = h * func(t[i] + h/2, y[i] + k1/2)
                k3 = h * func(t[i] + h/2, y[i] + k2/2)
                k4 = h * func(t[i] + h, y[i] + k3)
                y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        elif method == "euler":
            for i in range(n_steps):
                y[i+1] = y[i] + h * func(t[i], y[i])
        
        computation_time = time.time() - start_time
        precision = h  # دقة تقريبية
        
        self._update_statistics(computation_time, precision)
        
        return MathematicalResult(
            value=(t, y),
            precision=precision,
            computation_time=computation_time,
            domain=MathematicalDomain.REAL,
            metadata={"method": method, "steps": n_steps, "step_size": h}
        )
    
    def fourier_transform(self, signal: np.ndarray, sample_rate: float = 1.0) -> MathematicalResult:
        """تحويل فورييه المتقدم"""
        start_time = time.time()
        
        # تحويل فورييه السريع
        fft_result = np.fft.fft(signal)
        frequencies = np.fft.fftfreq(len(signal), 1/sample_rate)
        
        # حساب الطيف
        magnitude = np.abs(fft_result)
        phase = np.angle(fft_result)
        
        computation_time = time.time() - start_time
        precision = 1.0 / len(signal)  # دقة الترددات
        
        self._update_statistics(computation_time, precision)
        
        return MathematicalResult(
            value={
                "fft": fft_result,
                "frequencies": frequencies,
                "magnitude": magnitude,
                "phase": phase
            },
            precision=precision,
            computation_time=computation_time,
            domain=MathematicalDomain.COMPLEX,
            metadata={"sample_rate": sample_rate, "signal_length": len(signal)}
        )
    
    def matrix_operations(self, matrix: np.ndarray, operation: str = "eigenvalues") -> MathematicalResult:
        """عمليات المصفوفات المتقدمة"""
        start_time = time.time()
        
        if operation == "eigenvalues":
            eigenvals, eigenvecs = np.linalg.eig(matrix)
            result = {"eigenvalues": eigenvals, "eigenvectors": eigenvecs}
        elif operation == "svd":
            U, s, Vt = np.linalg.svd(matrix)
            result = {"U": U, "singular_values": s, "Vt": Vt}
        elif operation == "inverse":
            result = np.linalg.inv(matrix)
        elif operation == "determinant":
            result = np.linalg.det(matrix)
        elif operation == "rank":
            result = np.linalg.matrix_rank(matrix)
        else:
            result = matrix
        
        computation_time = time.time() - start_time
        precision = self._calculate_precision(matrix)
        
        self._update_statistics(computation_time, precision)
        
        return MathematicalResult(
            value=result,
            precision=precision,
            computation_time=computation_time,
            domain=MathematicalDomain.REAL if np.isrealobj(matrix) else MathematicalDomain.COMPLEX,
            metadata={"operation": operation, "matrix_shape": matrix.shape}
        )
    
    def _calculate_precision(self, value: Union[float, np.ndarray]) -> float:
        """حساب دقة النتيجة"""
        if isinstance(value, np.ndarray):
            if value.size == 0:
                return 1e-15
            # التأكد من أن النوع يدعم finfo
            if np.issubdtype(value.dtype, np.floating):
                return np.finfo(value.dtype).eps * np.max(np.abs(value))
            else:
                return np.finfo(float).eps * np.max(np.abs(value.astype(float)))
        else:
            return abs(value) * np.finfo(float).eps if value != 0 else 1e-15
    
    def _update_statistics(self, computation_time: float, precision: float):
        """تحديث إحصائيات الأداء"""
        self.total_calculations += 1
        self.total_computation_time += computation_time
        
        # تحديث متوسط الدقة
        current_precision_sum = self.average_precision * (self.total_calculations - 1)
        self.average_precision = (current_precision_sum + precision) / self.total_calculations
    
    def get_performance_statistics(self) -> Dict[str, Any]:
        """الحصول على إحصائيات الأداء"""
        avg_computation_time = self.total_computation_time / self.total_calculations if self.total_calculations > 0 else 0
        
        return {
            "total_calculations": self.total_calculations,
            "total_computation_time": self.total_computation_time,
            "average_computation_time": avg_computation_time,
            "average_precision": self.average_precision,
            "precision_level": self.precision.value,
            "precision_settings": self.precision_settings[self.precision],
            "creation_time": self.creation_time
        }

# ==================== اختبار المكونات الرياضية ====================

def test_advanced_mathematical_components():
    """اختبار شامل للمكونات الرياضية المتقدمة"""
    print("🧮 اختبار المكونات الرياضية المتقدمة")
    print("="*60)
    
    # إنشاء المكونات الرياضية
    math_comp = AdvancedMathematicalComponents(CalculationPrecision.HIGH)
    
    print(f"\n🔢 اختبار الدوال الأساسية:")
    
    # اختبار السيجمويد الثوري
    x_test = np.linspace(-5, 5, 11)
    sigmoid_result = math_comp.revolutionary_sigmoid(x_test, alpha=2.0, k=1.5, revolutionary_mode=True)
    print(f"\n📈 السيجمويد الثوري:")
    print(f"   🎯 الدقة: {sigmoid_result.precision:.2e}")
    print(f"   ⏱️ الوقت: {sigmoid_result.computation_time:.6f}s")
    print(f"   🧬 النظريات المطبقة: {len(sigmoid_result.revolutionary_theories_applied)}")
    
    # اختبار الدالة الخطية الثورية
    linear_result = math_comp.revolutionary_linear(x_test, beta=0.5, gamma=1.0, revolutionary_mode=True)
    print(f"\n📏 الدالة الخطية الثورية:")
    print(f"   🎯 الدقة: {linear_result.precision:.2e}")
    print(f"   ⏱️ الوقت: {linear_result.computation_time:.6f}s")
    print(f"   🧬 النظريات المطبقة: {len(linear_result.revolutionary_theories_applied)}")
    
    # اختبار معادلة الشكل العام
    general_result = math_comp.revolutionary_general_form(
        x_test, 
        alpha_list=[1.0, 0.5], 
        k_list=[2.0, 3.0], 
        beta_list=[0.1, 0.05]
    )
    print(f"\n🌟 معادلة الشكل العام:")
    print(f"   🎯 الدقة: {general_result.precision:.2e}")
    print(f"   ⏱️ الوقت: {general_result.computation_time:.6f}s")
    print(f"   🔢 المكونات: {general_result.metadata['components']}")
    
    print(f"\n🧮 اختبار العمليات المتقدمة:")
    
    # اختبار المشتقة العددية
    def test_func(x):
        return x**3 + 2*x**2 - x + 1
    
    derivative_result = math_comp.numerical_derivative(test_func, 2.0)
    print(f"\n📐 المشتقة العددية عند x=2:")
    print(f"   📊 النتيجة: {derivative_result.value:.6f}")
    print(f"   🎯 الدقة: {derivative_result.precision:.2e}")
    print(f"   ⏱️ الوقت: {derivative_result.computation_time:.6f}s")
    
    # اختبار التكامل العددي
    integral_result = math_comp.numerical_integral(test_func, 0, 2, method="simpson")
    print(f"\n∫ التكامل العددي من 0 إلى 2:")
    print(f"   📊 النتيجة: {integral_result.value:.6f}")
    print(f"   🎯 الدقة: {integral_result.precision:.2e}")
    print(f"   ⏱️ الوقت: {integral_result.computation_time:.6f}s")
    
    # اختبار حل المعادلة التفاضلية
    def ode_func(t, y):
        return -2 * y + 1
    
    ode_result = math_comp.solve_ode(ode_func, y0=0, t_span=(0, 2), method="rk4")
    print(f"\n🔄 حل المعادلة التفاضلية:")
    print(f"   📊 نقاط الحل: {len(ode_result.value[1])}")
    print(f"   🎯 الدقة: {ode_result.precision:.2e}")
    print(f"   ⏱️ الوقت: {ode_result.computation_time:.6f}s")
    
    # اختبار تحويل فورييه
    signal = np.sin(2 * np.pi * 5 * np.linspace(0, 1, 100)) + 0.5 * np.sin(2 * np.pi * 10 * np.linspace(0, 1, 100))
    fft_result = math_comp.fourier_transform(signal, sample_rate=100)
    print(f"\n🌊 تحويل فورييه:")
    print(f"   📊 طول الطيف: {len(fft_result.value['magnitude'])}")
    print(f"   🎯 الدقة: {fft_result.precision:.2e}")
    print(f"   ⏱️ الوقت: {fft_result.computation_time:.6f}s")
    
    # اختبار عمليات المصفوفات
    test_matrix = np.array([[1, 2], [3, 4]])
    matrix_result = math_comp.matrix_operations(test_matrix, operation="eigenvalues")
    print(f"\n🔢 القيم الذاتية للمصفوفة:")
    print(f"   📊 القيم الذاتية: {matrix_result.value['eigenvalues']}")
    print(f"   🎯 الدقة: {matrix_result.precision:.2e}")
    print(f"   ⏱️ الوقت: {matrix_result.computation_time:.6f}s")
    
    # عرض إحصائيات الأداء
    print(f"\n📊 إحصائيات الأداء:")
    stats = math_comp.get_performance_statistics()
    print(f"   📈 إجمالي العمليات: {stats['total_calculations']}")
    print(f"   ⏱️ إجمالي الوقت: {stats['total_computation_time']:.6f}s")
    print(f"   📊 متوسط الوقت: {stats['average_computation_time']:.6f}s")
    print(f"   🎯 متوسط الدقة: {stats['average_precision']:.2e}")
    
    print(f"\n✅ انتهى اختبار المكونات الرياضية المتقدمة!")
    return math_comp

if __name__ == "__main__":
    test_advanced_mathematical_components()

