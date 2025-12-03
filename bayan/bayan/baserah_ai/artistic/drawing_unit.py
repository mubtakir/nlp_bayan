"""
وحدة الرسم - Drawing Unit
==========================

تحويل المعادلات الرياضية إلى أشكال مرئية.
معادلة → شكل

المؤلف: باسل يحيى عبدالله
"""

import numpy as np
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass, field
from enum import Enum


@dataclass
class ShapeParameters:
    """معاملات الشكل للرسم"""
    # معاملات السيغمويد
    alpha: List[float] = field(default_factory=lambda: [1.0])
    k: List[float] = field(default_factory=lambda: [1.0])
    x0: List[float] = field(default_factory=lambda: [0.0])
    n: List[int] = field(default_factory=lambda: [1])
    
    # المعاملات الخطية
    beta: float = 0.0
    gamma: float = 0.0
    
    # خصائص الشكل
    resolution: int = 500
    x_range: Tuple[float, float] = (-5, 5)
    closed: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "alpha": self.alpha,
            "k": self.k,
            "x0": self.x0,
            "n": self.n,
            "beta": self.beta,
            "gamma": self.gamma,
            "resolution": self.resolution,
            "x_range": self.x_range,
            "closed": self.closed
        }


class DrawingUnit:
    """
    وحدة الرسم - تحويل المعادلات إلى أشكال
    
    الصيغة العامة:
    f(x) = Σ αᵢ·σₙᵢ(x; kᵢ, x₀ᵢ) + βx + γ
    """
    
    def __init__(self):
        self.shapes: List[Dict[str, Any]] = []
        self.current_params = ShapeParameters()
    
    def set_parameters(self, params: ShapeParameters):
        """تعيين معاملات الرسم"""
        self.current_params = params
    
    def generalized_sigmoid(self, x: np.ndarray, alpha: float, 
                           k: float, x0: float, n: int) -> np.ndarray:
        """دالة سيغمويد المعممة"""
        term = np.power(x - x0, n)
        return alpha / (1.0 + np.exp(-k * term))
    
    def compute_shape(self, params: ShapeParameters = None) -> Tuple[np.ndarray, np.ndarray]:
        """
        حساب نقاط الشكل من المعادلة
        
        Returns:
            (x, y): مصفوفتي الإحداثيات
        """
        if params is None:
            params = self.current_params
        
        x = np.linspace(params.x_range[0], params.x_range[1], params.resolution)
        y = np.zeros_like(x)
        
        # مجموع مكونات السيغمويد
        num_components = min(len(params.alpha), len(params.k), 
                            len(params.x0), len(params.n))
        
        for i in range(num_components):
            y += self.generalized_sigmoid(
                x, params.alpha[i], params.k[i], 
                params.x0[i], params.n[i]
            )
        
        # إضافة المركب الخطي
        y += params.beta * x + params.gamma
        
        return x, y
    
    def draw_circle(self, radius: float = 1.0, center: Tuple[float, float] = (0, 0),
                    resolution: int = 100) -> Tuple[np.ndarray, np.ndarray]:
        """رسم دائرة"""
        t = np.linspace(0, 2 * np.pi, resolution)
        x = center[0] + radius * np.cos(t)
        y = center[1] + radius * np.sin(t)
        return x, y
    
    def draw_heart(self, scale: float = 1.0, resolution: int = 100) -> Tuple[np.ndarray, np.ndarray]:
        """رسم قلب"""
        t = np.linspace(0, 2 * np.pi, resolution)
        x = scale * 16 * np.sin(t)**3 / 16
        y = scale * (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)) / 16
        return x, y
    
    def draw_flower(self, petals: int = 5, scale: float = 1.0,
                    resolution: int = 200) -> Tuple[np.ndarray, np.ndarray]:
        """رسم وردة"""
        t = np.linspace(0, 2 * np.pi, resolution)
        r = scale * np.cos(petals * t)
        x = r * np.cos(t)
        y = r * np.sin(t)
        return x, y
    
    def draw_spiral(self, turns: float = 3, scale: float = 0.1,
                    resolution: int = 200) -> Tuple[np.ndarray, np.ndarray]:
        """رسم حلزون"""
        t = np.linspace(0, turns * 2 * np.pi, resolution)
        r = scale * t
        x = r * np.cos(t)
        y = r * np.sin(t)
        return x, y
    
    def draw_wave(self, frequency: float = 1.0, amplitude: float = 1.0,
                  x_range: Tuple[float, float] = (-5, 5),
                  resolution: int = 200) -> Tuple[np.ndarray, np.ndarray]:
        """رسم موجة"""
        x = np.linspace(x_range[0], x_range[1], resolution)
        y = amplitude * np.sin(frequency * x)
        return x, y
    
    def get_equation_string(self, params: ShapeParameters = None) -> str:
        """الحصول على نص المعادلة"""
        if params is None:
            params = self.current_params
        
        parts = []
        for i in range(len(params.alpha)):
            α, k, x0, n = params.alpha[i], params.k[i], params.x0[i], params.n[i]
            parts.append(f"{α:.2f}·σ_{n}(x; {k:.2f}, {x0:.2f})")
        
        eq = " + ".join(parts)
        if params.beta != 0:
            eq += f" + {params.beta:.2f}x"
        if params.gamma != 0:
            eq += f" + {params.gamma:.2f}"
        
        return f"f(x) = {eq}"

