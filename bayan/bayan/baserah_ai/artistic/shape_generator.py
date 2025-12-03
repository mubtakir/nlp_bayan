"""
مولد الأشكال - Shape Generator
================================

إنشاء أشكال متنوعة باستخدام معادلة الشكل العام.

المؤلف: باسل يحيى عبدالله
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
from enum import Enum
from dataclasses import dataclass


class ShapeType(Enum):
    """أنواع الأشكال"""
    CIRCLE = "دائرة"
    ELLIPSE = "قطع_ناقص"
    HEART = "قلب"
    FLOWER = "وردة"
    SPIRAL = "حلزون"
    WAVE = "موجة"
    STAR = "نجمة"
    CUSTOM = "مخصص"


@dataclass
class ShapeSpec:
    """مواصفات الشكل"""
    shape_type: ShapeType
    scale: float = 1.0
    rotation: float = 0.0
    center: Tuple[float, float] = (0.0, 0.0)
    params: Dict = None
    
    def __post_init__(self):
        if self.params is None:
            self.params = {}


class ShapeGenerator:
    """
    مولد الأشكال باستخدام المعادلات الرياضية
    """
    
    def __init__(self, resolution: int = 200):
        self.resolution = resolution
        self.shapes_generated = 0
    
    def generate(self, spec: ShapeSpec) -> Tuple[np.ndarray, np.ndarray]:
        """
        توليد شكل بناءً على المواصفات
        """
        generators = {
            ShapeType.CIRCLE: self._gen_circle,
            ShapeType.ELLIPSE: self._gen_ellipse,
            ShapeType.HEART: self._gen_heart,
            ShapeType.FLOWER: self._gen_flower,
            ShapeType.SPIRAL: self._gen_spiral,
            ShapeType.WAVE: self._gen_wave,
            ShapeType.STAR: self._gen_star,
        }
        
        gen_func = generators.get(spec.shape_type, self._gen_circle)
        x, y = gen_func(spec)
        
        # تطبيق الدوران
        if spec.rotation != 0:
            x, y = self._rotate(x, y, spec.rotation)
        
        # تطبيق المركز
        x += spec.center[0]
        y += spec.center[1]
        
        self.shapes_generated += 1
        return x, y
    
    def _gen_circle(self, spec: ShapeSpec) -> Tuple[np.ndarray, np.ndarray]:
        """توليد دائرة"""
        t = np.linspace(0, 2 * np.pi, self.resolution)
        x = spec.scale * np.cos(t)
        y = spec.scale * np.sin(t)
        return x, y
    
    def _gen_ellipse(self, spec: ShapeSpec) -> Tuple[np.ndarray, np.ndarray]:
        """توليد قطع ناقص"""
        a = spec.params.get('a', spec.scale)
        b = spec.params.get('b', spec.scale * 0.5)
        t = np.linspace(0, 2 * np.pi, self.resolution)
        x = a * np.cos(t)
        y = b * np.sin(t)
        return x, y
    
    def _gen_heart(self, spec: ShapeSpec) -> Tuple[np.ndarray, np.ndarray]:
        """توليد قلب"""
        t = np.linspace(0, 2 * np.pi, self.resolution)
        x = spec.scale * 16 * np.sin(t)**3 / 16
        y = spec.scale * (13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)) / 16
        return x, y
    
    def _gen_flower(self, spec: ShapeSpec) -> Tuple[np.ndarray, np.ndarray]:
        """توليد وردة"""
        petals = spec.params.get('petals', 5)
        t = np.linspace(0, 2 * np.pi, self.resolution)
        r = spec.scale * np.cos(petals * t)
        x = r * np.cos(t)
        y = r * np.sin(t)
        return x, y
    
    def _gen_spiral(self, spec: ShapeSpec) -> Tuple[np.ndarray, np.ndarray]:
        """توليد حلزون"""
        turns = spec.params.get('turns', 3)
        t = np.linspace(0, turns * 2 * np.pi, self.resolution)
        r = spec.scale * t / (turns * 2 * np.pi)
        x = r * np.cos(t)
        y = r * np.sin(t)
        return x, y
    
    def _gen_wave(self, spec: ShapeSpec) -> Tuple[np.ndarray, np.ndarray]:
        """توليد موجة"""
        frequency = spec.params.get('frequency', 1.0)
        x = np.linspace(-np.pi * 2, np.pi * 2, self.resolution)
        y = spec.scale * np.sin(frequency * x)
        return x, y
    
    def _gen_star(self, spec: ShapeSpec) -> Tuple[np.ndarray, np.ndarray]:
        """توليد نجمة"""
        points = spec.params.get('points', 5)
        inner_ratio = spec.params.get('inner_ratio', 0.4)
        
        angles = np.linspace(0, 2 * np.pi, 2 * points + 1)
        radii = np.array([spec.scale if i % 2 == 0 else spec.scale * inner_ratio 
                         for i in range(2 * points + 1)])
        
        x = radii * np.cos(angles - np.pi/2)
        y = radii * np.sin(angles - np.pi/2)
        return x, y
    
    def _rotate(self, x: np.ndarray, y: np.ndarray, 
                angle: float) -> Tuple[np.ndarray, np.ndarray]:
        """تدوير النقاط"""
        cos_a = np.cos(angle)
        sin_a = np.sin(angle)
        x_rot = x * cos_a - y * sin_a
        y_rot = x * sin_a + y * cos_a
        return x_rot, y_rot
    
    def get_available_shapes(self) -> List[str]:
        """الحصول على الأشكال المتاحة"""
        return [s.value for s in ShapeType]
    
    def get_stats(self) -> Dict:
        """إحصائيات المولد"""
        return {
            "الأشكال_المولدة": self.shapes_generated,
            "الدقة": self.resolution,
            "الأشكال_المتاحة": len(ShapeType)
        }

