#!/usr/bin/env python3
"""
معادلة الشكل العام المحسنة - نظام بصيرة الثوري
Enhanced General Shape Equation - Revolutionary Basera System

🧬 تطوير معادلة الشكل العام لتشمل خصائص الشكل والكائن
📊 دعم المتجهات اللغوية والخصائص الدلالية مستقبلاً
🎯 فصل واضح بين الرياضيات وخصائص الكائن

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import numpy as np
import math
from typing import Dict, List, Any, Optional, Tuple, Union
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum

@dataclass
class ShapeMetadata:
    """بيانات وصفية للشكل والكائن"""
    name: str = ""              # اسم الكائن: "قطة"
    state: str = ""             # حالة الكائن: "واقفة"
    color: str = ""             # لون الكائن: "بيضاء"
    size: str = ""              # حجم الكائن: "كبيرة"
    texture: str = ""           # ملمس الكائن: "ناعمة"
    position: str = ""          # موضع الكائن: "في الحديقة"
    properties: Dict[str, Any] = field(default_factory=dict)  # خصائص إضافية
    
    def get_full_description(self) -> str:
        """وصف كامل للكائن"""
        parts = []
        if self.color: parts.append(self.color)
        if self.size: parts.append(self.size)
        if self.texture: parts.append(self.texture)
        if self.name: parts.append(self.name)
        if self.state: parts.append(self.state)
        if self.position: parts.append(self.position)
        
        return " ".join(parts) if parts else "كائن غير محدد"
    
    def to_vector_representation(self) -> Dict[str, float]:
        """تحويل الخصائص إلى تمثيل متجهي (للمتجهات اللغوية مستقبلاً)"""
        vector_rep = {}
        
        # تحويل النصوص إلى قيم رقمية مؤقتة (سيتم تطويرها لاحقاً)
        if self.name:
            vector_rep['name_vector'] = sum(ord(c) for c in self.name) / len(self.name)
        if self.state:
            vector_rep['state_vector'] = sum(ord(c) for c in self.state) / len(self.state)
        if self.color:
            vector_rep['color_vector'] = sum(ord(c) for c in self.color) / len(self.color)
        
        return vector_rep

class ShapeType(Enum):
    """أنواع الأشكال المدعومة"""
    CIRCLE = "circle"
    HEART = "heart"
    FLOWER = "flower"
    SPIRAL = "spiral"
    WAVE = "wave"
    LINE = "line"
    POLYGON = "polygon"
    CUSTOM = "custom"

class EnhancedGeneralShapeEquation:
    """
    معادلة الشكل العام المحسنة
    
    🧬 تجمع بين:
    - الرياضيات البحتة (sigmoid + linear)
    - خصائص الشكل والكائن (اسم، حالة، لون، إلخ)
    - دعم المتجهات اللغوية مستقبلاً
    - فصل واضح بين المسؤوليات
    """
    
    def __init__(self, shape_name: str = "", shape_state: str = "", 
                 shape_color: str = "", shape_type: ShapeType = ShapeType.CUSTOM):
        self.creation_time = datetime.now()
        self.equation_id = f"shape_eq_{int(self.creation_time.timestamp())}"
        
        # خصائص الشكل والكائن (الإضافة الجديدة)
        self.metadata = ShapeMetadata(
            name=shape_name,
            state=shape_state,
            color=shape_color
        )
        
        self.shape_type = shape_type
        
        # المعادلات الرياضية البحتة (الموجودة حالياً)
        self.sigmoid_components: List[Dict[str, float]] = []
        self.linear_components: List[Dict[str, float]] = []
        self.cutting_factors: List[float] = []
        
        # معاملات الشكل الرياضية
        self.mathematical_parameters = {
            'alpha': [],  # معاملات السيجمويد
            'k': [],      # معاملات الحدة
            'x0': [],     # نقاط الإزاحة
            'beta': [],   # معاملات خطية
            'gamma': []   # ثوابت
        }
        
        # إعدادات التقطيع والتكميم
        self.quantization_levels = 1000
        self.cutting_threshold = 0.5
        
        # دعم المتجهات اللغوية (للمستقبل)
        self.linguistic_vectors: Dict[str, np.ndarray] = {}
        self.semantic_embeddings: Dict[str, Any] = {}
        
        print(f"🧮⚡ تم إنشاء معادلة شكل عام محسنة: {self.get_shape_description()}")
    
    def set_shape_properties(self, name: str = None, state: str = None, 
                           color: str = None, size: str = None, 
                           texture: str = None, position: str = None,
                           additional_props: Dict[str, Any] = None):
        """تحديد خصائص الشكل والكائن"""
        if name is not None:
            self.metadata.name = name
        if state is not None:
            self.metadata.state = state
        if color is not None:
            self.metadata.color = color
        if size is not None:
            self.metadata.size = size
        if texture is not None:
            self.metadata.texture = texture
        if position is not None:
            self.metadata.position = position
        if additional_props:
            self.metadata.properties.update(additional_props)
    
    def get_shape_description(self) -> str:
        """وصف كامل للشكل"""
        return self.metadata.get_full_description()
    
    def add_sigmoid_component(self, alpha: float, k: float, x0: float, n: int = None):
        """إضافة مكون سيجمويدي"""
        component = {
            'alpha': alpha,
            'k': k,
            'x0': x0,
            'n': n or self.quantization_levels
        }
        self.sigmoid_components.append(component)
        
        # تحديث المعاملات
        self.mathematical_parameters['alpha'].append(alpha)
        self.mathematical_parameters['k'].append(k)
        self.mathematical_parameters['x0'].append(x0)
    
    def add_linear_component(self, beta: float, gamma: float):
        """إضافة مكون خطي"""
        component = {
            'beta': beta,
            'gamma': gamma
        }
        self.linear_components.append(component)
        
        # تحديث المعاملات
        self.mathematical_parameters['beta'].append(beta)
        self.mathematical_parameters['gamma'].append(gamma)
    
    def compute_shape_equation(self, x: np.ndarray) -> np.ndarray:
        """
        حساب معادلة الشكل العام
        f̂(x) = Σ(αᵢ · σₙᵢ(x; kᵢ, x₀ᵢ) + βᵢx + γᵢ)
        """
        result = np.zeros_like(x, dtype=float)
        
        # المكونات السيجمويدية
        for component in self.sigmoid_components:
            alpha = component['alpha']
            k = component['k']
            x0 = component['x0']
            n = component['n']
            
            sigmoid_part = alpha * self._modified_sigmoid(x, k, x0, n)
            result += sigmoid_part
        
        # المكونات الخطية
        for component in self.linear_components:
            beta = component['beta']
            gamma = component['gamma']
            
            linear_part = beta * x + gamma
            result += linear_part
        
        # تطبيق عوامل التقطيع
        if self.cutting_factors:
            for cutting_factor in self.cutting_factors:
                result = self._apply_cutting_factor(result, cutting_factor)
        
        return result
    
    def _modified_sigmoid(self, x: np.ndarray, k: float, x0: float, n: int) -> np.ndarray:
        """دالة السيجمويد المعدلة مع التكميم"""
        # السيجمويد الأساسي
        basic_sigmoid = 1 / (1 + np.exp(-k * (x - x0)))
        
        # تطبيق التكميم للدوال المتقطعة
        if n > 1:
            quantized = np.round(basic_sigmoid * n) / n
            return quantized
        
        return basic_sigmoid
    
    def _apply_cutting_factor(self, data: np.ndarray, factor: float) -> np.ndarray:
        """تطبيق عامل التقطيع"""
        return np.where(data > factor, data, 0)
    
    def generate_linguistic_vector(self) -> Dict[str, float]:
        """توليد متجه لغوي للشكل (للاستخدام المستقبلي)"""
        return self.metadata.to_vector_representation()
    
    def prepare_for_semantic_analysis(self) -> Dict[str, Any]:
        """إعداد البيانات للتحليل الدلالي المستقبلي"""
        return {
            'shape_description': self.get_shape_description(),
            'linguistic_vector': self.generate_linguistic_vector(),
            'mathematical_signature': {
                'sigmoid_count': len(self.sigmoid_components),
                'linear_count': len(self.linear_components),
                'complexity_score': len(self.sigmoid_components) + len(self.linear_components)
            },
            'metadata': {
                'name': self.metadata.name,
                'state': self.metadata.state,
                'color': self.metadata.color,
                'properties': self.metadata.properties
            }
        }
    
    def get_equation_summary(self) -> Dict[str, Any]:
        """ملخص شامل للمعادلة"""
        return {
            'equation_id': self.equation_id,
            'creation_time': self.creation_time,
            'shape_description': self.get_shape_description(),
            'shape_type': self.shape_type.value,
            'mathematical_components': {
                'sigmoid_components': len(self.sigmoid_components),
                'linear_components': len(self.linear_components),
                'cutting_factors': len(self.cutting_factors)
            },
            'parameters': self.mathematical_parameters,
            'metadata': self.metadata,
            'linguistic_support': bool(self.linguistic_vectors),
            'semantic_support': bool(self.semantic_embeddings)
        }

# ==================== اختبار المعادلة المحسنة ====================

def test_enhanced_general_shape_equation():
    """اختبار شامل للمعادلة المحسنة"""
    print("🧪 اختبار معادلة الشكل العام المحسنة")
    print("=" * 60)
    
    # إنشاء معادلة لقطة بيضاء واقفة
    cat_equation = EnhancedGeneralShapeEquation(
        shape_name="قطة",
        shape_state="واقفة", 
        shape_color="بيضاء",
        shape_type=ShapeType.CUSTOM
    )
    
    # إضافة خصائص إضافية
    cat_equation.set_shape_properties(
        size="متوسطة",
        texture="ناعمة",
        position="في الحديقة",
        additional_props={
            "عمر": "صغيرة",
            "مزاج": "هادئة",
            "نشاط": "مستريحة"
        }
    )
    
    # إضافة مكونات رياضية
    cat_equation.add_sigmoid_component(alpha=1.0, k=2.0, x0=0.0)
    cat_equation.add_sigmoid_component(alpha=0.5, k=1.5, x0=math.pi)
    cat_equation.add_linear_component(beta=0.3, gamma=0.1)
    
    # اختبار الحسابات
    x = np.linspace(-5, 5, 100)
    y = cat_equation.compute_shape_equation(x)
    
    print(f"\n📊 وصف الشكل: {cat_equation.get_shape_description()}")
    print(f"🧮 تم حساب {len(y)} نقطة للشكل")
    print(f"📈 نطاق القيم: [{y.min():.3f}, {y.max():.3f}]")
    
    # اختبار المتجه اللغوي
    linguistic_vector = cat_equation.generate_linguistic_vector()
    print(f"\n🔤 المتجه اللغوي: {linguistic_vector}")
    
    # اختبار التحليل الدلالي
    semantic_data = cat_equation.prepare_for_semantic_analysis()
    print(f"\n🧠 بيانات التحليل الدلالي:")
    print(f"   📝 الوصف: {semantic_data['shape_description']}")
    print(f"   🧮 التعقيد الرياضي: {semantic_data['mathematical_signature']['complexity_score']}")
    
    # ملخص المعادلة
    summary = cat_equation.get_equation_summary()
    print(f"\n📋 ملخص المعادلة:")
    print(f"   🆔 المعرف: {summary['equation_id']}")
    print(f"   📊 المكونات: {summary['mathematical_components']}")
    
    print("\n✅ تم الانتهاء من اختبار المعادلة المحسنة!")

if __name__ == "__main__":
    test_enhanced_general_shape_equation()
