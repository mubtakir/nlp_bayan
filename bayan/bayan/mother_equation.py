"""
نظام المعادلة الأم (Mother Equation System)
===========================================

نظام رياضي شامل يمثل الأشياء وخصائصها وحالاتها وأشكالها.

الصيغة الرياضية:
    Object = (id, Φ, Ψ(t), Γ)
    
    حيث:
        id: معرف فريد للشيء
        Φ: الخصائص الثابتة (Fixed Properties)
        Ψ(t): الحالات الديناميكية (Dynamic States)
        Γ: معادلة الشكل (Shape Equation)

المؤلف: باسل يحيى عبد الله
التاريخ: 2025-11-25
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from enum import Enum
import json

from .gse import GSEModel


# ═══════════════════════════════════════════════════════════════
# 1. التعريفات الأساسية
# ═══════════════════════════════════════════════════════════════

class PropertyDomain(Enum):
    """مجالات الخصائص المختلفة"""
    PHYSICAL = "فيزيائي"
    CHEMICAL = "كيميائي"
    PSYCHOLOGICAL = "نفسي"
    SOCIAL = "اجتماعي"
    LINGUISTIC = "لغوي"
    GEOMETRIC = "هندسي"
    BIOLOGICAL = "بيولوجي"
    LOGICAL = "منطقي"
    TEMPORAL = "زمني"
    SPATIAL = "مكاني"


@dataclass
class Property:
    """خاصية واحدة للشيء"""
    name: str
    value: Any
    domain: PropertyDomain
    unit: Optional[str] = None
    changeable: bool = True
    metadata: Dict = field(default_factory=dict)
    
    def __str__(self):
        unit_str = f" {self.unit}" if self.unit else ""
        return f"{self.name}: {self.value}{unit_str} [{self.domain.value}]"
    
    def to_dict(self):
        """تحويل إلى قاموس للتخزين"""
        return {
            'name': self.name,
            'value': self.value,
            'domain': self.domain.value,
            'unit': self.unit,
            'changeable': self.changeable,
            'metadata': self.metadata
        }


@dataclass
class State:
    """حالة واحدة للشيء (قيمة ضبابية بين 0 و 1)"""
    name: str
    value: float  # 0.0 إلى 1.0 (fuzzy state)
    timestamp: Optional[float] = None
    metadata: Dict = field(default_factory=dict)
    
    def __post_init__(self):
        """التحقق من صحة القيمة"""
        if not 0.0 <= self.value <= 1.0:
            raise ValueError(f"قيمة الحالة يجب أن تكون بين 0 و 1، القيمة المعطاة: {self.value}")
    
    def __str__(self):
        return f"{self.name}: {self.value:.2f}"
    
    def to_dict(self):
        """تحويل إلى قاموس للتخزين"""
        return {
            'name': self.name,
            'value': self.value,
            'timestamp': self.timestamp,
            'metadata': self.metadata
        }


# ═══════════════════════════════════════════════════════════════
# 2. المعادلة الأم - الكائن الرئيسي
# ═══════════════════════════════════════════════════════════════

class MotherEquation:
    """
    المعادلة الأم: تمثيل شامل للأشياء
    
    Object = (id, Φ, Ψ(t), Γ)
    
    حيث:
        - id: معرف فريد للكائن
        - Φ: الخصائص الثابتة {لون، مادة، كتلة، ...}
        - Ψ(t): الحالات الديناميكية {جوع، سعادة، تعب، ...}
        - Γ: معادلة الشكل (GSE Model)
    """
    
    def __init__(self, object_id: str, object_name: str):
        """
        إنشاء كائن جديد.
        
        Args:
            object_id: معرف فريد
            object_name: اسم الكائن
        """
        self.id = object_id
        self.name = object_name
        
        # Φ - الخصائص الثابتة
        self.fixed_properties: Dict[str, Property] = {}
        
        # Ψ(t) - الحالات الديناميكية
        self.dynamic_states: Dict[str, State] = {}
        
        # Γ - معادلة الشكل
        self.shape_equation: Optional[GSEModel] = None
        
        # تاريخ التغيرات
        self.history: List[Dict] = []
        
        # البيانات الوصفية
        self.metadata = {
            'created_at': None,
            'category': None,
            'tags': []
        }
    
    # ───────────────────────────────────────────────────────────
    # إدارة الخصائص الثابتة (Φ)
    # ───────────────────────────────────────────────────────────
    
    def add_property(self, name: str, value: Any, domain: PropertyDomain, 
                     unit: Optional[str] = None, changeable: bool = True):
        """
        إضافة خاصية ثابتة جديدة.
        
        Args:
            name: اسم الخاصية
            value: قيمتها
            domain: المجال (فيزيائي، كيميائي، إلخ)
            unit: الوحدة (اختياري)
            changeable: هل يمكن تغييرها لاحقاً
        """
        self.fixed_properties[name] = Property(
            name=name,
            value=value,
            domain=domain,
            unit=unit,
            changeable=changeable
        )
        self._log_change('property_added', name, value)
    
    def update_property(self, name: str, new_value: Any):
        """
        تحديث قيمة خاصية موجودة.
        
        Args:
            name: اسم الخاصية
            new_value: القيمة الجديدة
            
        Raises:
            ValueError: إذا كانت الخاصية غير قابلة للتغيير
            KeyError: إذا لم تكن الخاصية موجودة
        """
        if name not in self.fixed_properties:
            raise KeyError(f"الخاصية '{name}' غير موجودة")
        
        prop = self.fixed_properties[name]
        if not prop.changeable:
            raise ValueError(f"الخاصية '{name}' غير قابلة للتغيير")
        
        old_value = prop.value
        prop.value = new_value
        self._log_change('property_updated', name, {
            'old': old_value,
            'new': new_value
        })
    
    def get_property(self, name: str) -> Any:
        """الحصول على قيمة خاصية"""
        if name not in self.fixed_properties:
            raise KeyError(f"الخاصية '{name}' غير موجودة")
        return self.fixed_properties[name].value
    
    # ───────────────────────────────────────────────────────────
    # إدارة الحالات الديناميكية (Ψ)
    # ───────────────────────────────────────────────────────────
    
    def add_state(self, name: str, value: float):
        """
        إضافة حالة ديناميكية جديدة.
        
        Args:
            name: اسم الحالة
            value: قيمة بين 0 و 1
            
        Raises:
            ValueError: إذا كانت القيمة خارج النطاق [0, 1]
        """
        if not 0 <= value <= 1:
            raise ValueError(f"قيمة الحالة يجب أن تكون بين 0 و 1، القيمة: {value}")
        
        self.dynamic_states[name] = State(name=name, value=value)
        self._log_change('state_added', name, value)
    
    def update_state(self, name: str, new_value: float):
        """
        تحديث حالة موجودة.
        
        Args:
            name: اسم الحالة
            new_value: القيمة الجديدة (بين 0 و 1)
            
        Raises:
            ValueError: إذا كانت القيمة خارج النطاق
            KeyError: إذا لم تكن الحالة موجودة
        """
        if not 0 <= new_value <= 1:
            raise ValueError(f"قيمة الحالة يجب أن تكون بين 0 و 1، القيمة: {new_value}")
        
        if name not in self.dynamic_states:
            raise KeyError(f"الحالة '{name}' غير موجودة")
        
        old_value = self.dynamic_states[name].value
        self.dynamic_states[name].value = new_value
        self._log_change('state_updated', name, {
            'old': old_value,
            'new': new_value
        })
    
    def get_state(self, name: str) -> float:
        """الحصول على قيمة حالة"""
        if name not in self.dynamic_states:
            raise KeyError(f"الحالة '{name}' غير موجودة")
        return self.dynamic_states[name].value
    
    # ───────────────────────────────────────────────────────────
    # إدارة معادلة الشكل (Γ)
    # ───────────────────────────────────────────────────────────
    
    def set_shape_equation(self, shape_eq: GSEModel):
        """
        تعيين معادلة الشكل.
        
        Args:
            shape_eq: نموذج GSE يمثل شكل الكائن
        """
        self.shape_equation = shape_eq
        num_components = len(shape_eq.components) if shape_eq else 0
        self._log_change('shape_equation_set', 'shape', {
            'components': num_components,
            'linear': f"{shape_eq.beta}x + {shape_eq.gamma}" if shape_eq else None
        })
    
    def render_shape(self, x_range: tuple = (-10, 10), resolution: int = 100):
        """
        رسم الشكل باستخدام المعادلة.
        
        Args:
            x_range: نطاق قيم x (min, max)
            resolution: عدد النقاط
            
        Returns:
            np.ndarray: قيم y المحسوبة
            
        Raises:
            ValueError: إذا لم يتم تعيين معادلة شكل
        """
        if self.shape_equation is None:
            raise ValueError(f"لم يتم تعيين معادلة شكل للكائن '{self.name}'")
        
        x = np.linspace(x_range[0], x_range[1], resolution)
        return self.shape_equation.evaluate(x)
    
    # ───────────────────────────────────────────────────────────
    # المساعدات والأدوات
    # ───────────────────────────────────────────────────────────
    
    def _log_change(self, change_type: str, key: str, value: Any):
        """تسجيل التغيير في التاريخ"""
        self.history.append({
            'type': change_type,
            'key': key,
            'value': value,
            'timestamp': None  # يمكن إضافة وقت حقيقي
        })
    
    def get_complete_state(self) -> Dict:
        """
        الحصول على الحالة الكاملة للكائن.
        
        Returns:
            قاموس يحتوي على جميع المعلومات
        """
        return {
            'id': self.id,
            'name': self.name,
            'fixed_properties': {k: str(v) for k, v in self.fixed_properties.items()},
            'dynamic_states': {k: str(v) for k, v in self.dynamic_states.items()},
            'has_shape': self.shape_equation is not None,
            'metadata': self.metadata,
            'history_length': len(self.history)
        }
    
    def to_json(self, indent: int = 2) -> str:
        """
        تصدير الكائن إلى JSON.
        
        Args:
            indent: المسافة البادئة للتنسيق
            
        Returns:
            نص JSON
        """
        data = {
            'id': self.id,
            'name': self.name,
            'fixed_properties': {
                k: v.to_dict() for k, v in self.fixed_properties.items()
            },
            'dynamic_states': {
                k: v.to_dict() for k, v in self.dynamic_states.items()
            },
            'shape_equation': self._serialize_shape_equation(),
            'metadata': self.metadata
        }
        return json.dumps(data, ensure_ascii=False, indent=indent)
    
    def _serialize_shape_equation(self) -> Optional[Dict]:
        """تحويل معادلة الشكل إلى قاموس"""
        if self.shape_equation is None:
            return None
        
        return {
            'beta': self.shape_equation.beta,
            'gamma': self.shape_equation.gamma,
            'components': self.shape_equation.components
        }
    
    @classmethod
    def from_json(cls, json_str: str) -> 'MotherEquation':
        """
        استيراد كائن من JSON.
        
        Args:
            json_str: نص JSON
            
        Returns:
            كائن MotherEquation
        """
        data = json.loads(json_str)
        
        # إنشاء الكائن
        obj = cls(data['id'], data['name'])
        obj.metadata = data.get('metadata', {})
        
        # استيراد الخصائص
        for prop_data in data.get('fixed_properties', {}).values():
            domain = PropertyDomain(prop_data['domain'])
            obj.add_property(
                prop_data['name'],
                prop_data['value'],
                domain,
                prop_data.get('unit'),
                prop_data.get('changeable', True)
            )
        
        # استيراد الحالات
        for state_data in data.get('dynamic_states', {}).values():
            obj.add_state(state_data['name'], state_data['value'])
        
        # استيراد معادلة الشكل
        shape_data = data.get('shape_equation')
        if shape_data:
            model = GSEModel(shape_data['beta'], shape_data['gamma'])
            for comp in shape_data.get('components', []):
                model.add_sigmoid(
                    comp['alpha'], comp['n'], comp['k'], comp['x0']
                )
            obj.set_shape_equation(model)
        
        return obj
    
    def __repr__(self):
        return (f"MotherEquation(id='{self.id}', name='{self.name}', "
                f"properties={len(self.fixed_properties)}, "
                f"states={len(self.dynamic_states)})")
    
    def __str__(self):
        lines = [
            f"╔══════════════════════════════════════╗",
            f"║ المعادلة الأم: {self.name:^22} ║",
            f"╠══════════════════════════════════════╣",
            f"║ المعرف: {self.id:29} ║",
            f"║ الخصائص الثابتة: {len(self.fixed_properties):17} ║",
            f"║ الحالات الديناميكية: {len(self.dynamic_states):16} ║",
            f"║ معادلة شكل: {'✓' if self.shape_equation else '✗':21} ║",
            f"╚══════════════════════════════════════╝"
        ]
        return '\n'.join(lines)


# ═══════════════════════════════════════════════════════════════
# 3. أمثلة تطبيقية
# ═══════════════════════════════════════════════════════════════

def create_example_human() -> MotherEquation:
    """
    مثال: إنشاء كائن إنسان بخصائص وحالات كاملة.
    
    Returns:
        كائن MotherEquation يمثل إنساناً
    """
    human = MotherEquation("human_001", "محمد")
    
    # خصائص فيزيائية
    human.add_property("الطول", 175, PropertyDomain.PHYSICAL, "cm")
    human.add_property("الوزن", 70, PropertyDomain.PHYSICAL, "kg")
    human.add_property("لون_العيون", "بني", PropertyDomain.PHYSICAL)
    human.add_property("فصيلة_الدم", "O+", PropertyDomain.BIOLOGICAL, changeable=False)
    
    # خصائص نفسية
    human.add_property("الشخصية", "انطوائي", PropertyDomain.PSYCHOLOGICAL)
    human.add_property("الذكاء", "عالي", PropertyDomain.PSYCHOLOGICAL)
    
    # خصائص اجتماعية
    human.add_property("المهنة", "مهندس", PropertyDomain.SOCIAL)
    
    # حالات ديناميكية
    human.add_state("مستوى_الجوع", 0.3)
    human.add_state("مستوى_السعادة", 0.7)
    human.add_state("مستوى_التعب", 0.4)
    human.add_state("مستوى_التركيز", 0.8)
    
    # بيانات وصفية
    human.metadata['category'] = 'كائن_حي'
    human.metadata['tags'] = ['إنسان', 'ذكر', 'بالغ']
    
    return human


def create_example_tree() -> MotherEquation:
    """
    مثال: إنشاء كائن شجرة مع معادلة شكل.
    
    Returns:
        كائن MotherEquation يمثل شجرة
    """
    tree = MotherEquation("tree_001", "شجرة_تفاح")
    
    # خصائص فيزيائية
    tree.add_property("الطول", 5.0, PropertyDomain.PHYSICAL, "m")
    tree.add_property("قطر_الجذع", 0.3, PropertyDomain.PHYSICAL, "m")
    
    # خصائص بيولوجية
    tree.add_property("العمر", 10, PropertyDomain.BIOLOGICAL, "سنة")
    tree.add_property("النوع", "تفاح أحمر", PropertyDomain.BIOLOGICAL)
    tree.add_property("موسم_الإزهار", "ربيع", PropertyDomain.BIOLOGICAL)
    
    # حالات ديناميكية
    tree.add_state("مستوى_الرطوبة", 0.6)
    tree.add_state("مرحلة_النمو", 0.8)
    tree.add_state("صحة_الأوراق", 0.9)
    
    # معادلة شكل بسيطة (جذع + تاج)
    shape = GSEModel(beta=0.0, gamma=0.0)
    # مكون للجذع (خطوة حادة عند الأرض)
    shape.add_sigmoid(alpha=2.0, n=5, k=50.0, x0=0.0)
    # مكون للتاج (شكل بيضوي)
    shape.add_sigmoid(alpha=3.0, n=2, k=2.0, x0=3.0)
    
    tree.set_shape_equation(shape)
    
    # بيانات وصفية
    tree.metadata['category'] = 'نبات'
    tree.metadata['tags'] = ['شجرة', 'فاكهة', 'معمرة']
    
    return tree


def create_example_building() -> MotherEquation:
    """
    مثال: إنشاء كائن مبنى (كائن مركب من أجزاء).
    
    Returns:
        كائن MotherEquation يمثل مبنى
    """
    building = MotherEquation("building_001", "مدرسة_النور")
    
    # خصائص هندسية
    building.add_property("عدد_الطوابق", 3, PropertyDomain.GEOMETRIC)
    building.add_property("المساحة", 1200, PropertyDomain.GEOMETRIC, "m²")
    building.add_property("الارتفاع", 12.0, PropertyDomain.PHYSICAL, "m")
    
    # خصائص مادية
    building.add_property("المادة_الأساسية", "خرسانة", PropertyDomain.PHYSICAL)
    building.add_property("سنة_البناء", 2010, PropertyDomain.TEMPORAL, "سنة")
    
    # خصائص اجتماعية
    building.add_property("الغرض", "تعليم", PropertyDomain.SOCIAL)
    building.add_property("السعة", 500, PropertyDomain.SOCIAL, "طالب")
    
    # حالات ديناميكية
    building.add_state("مستوى_الصيانة", 0.75)
    building.add_state("نسبة_الإشغال", 0.8)
    building.add_state("الأمان", 0.95)
    
    # معادلة شكل (مبنى مستطيل ثلاثي الطوابق)
    shape = GSEModel(beta=0.0, gamma=0.0)
    # طابق أرضي
    shape.add_sigmoid(alpha=4.0, n=7, k=100.0, x0=0.0)
    # طابق أول
    shape.add_sigmoid(alpha=4.0, n=7, k=100.0, x0=4.0)
    # طابق ثاني
    shape.add_sigmoid(alpha=4.0, n=7, k=100.0, x0=8.0)
    
    building.set_shape_equation(shape)
    
    building.metadata['category'] = 'بناء'
    building.metadata['tags'] = ['مدرسة', 'تعليم', 'عام']
    
    return building
