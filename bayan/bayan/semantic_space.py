"""
الفضاء الدلالي - Semantic Space (Tasawwur)
==========================================

نظام فضاء 4D للتصور الذهني يجمع بين الأبعاد المكانية والزمانية.

المحاور:
- X: أفقي (يمين + / يسار -)
- Y: عمودي (فوق + / تحت -)
- Z: عمق (أمام + / خلف -)
- T: زمني (مستقبل + / ماضي -)

مستوحى من: src/extensions/ai/mental-imagery/semanticSpace.ts في Bayan JS

المطور الأصلي: باسل يحيى عبدالله
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, Tuple
from enum import Enum
import math


class SpatialDirection(Enum):
    """الاتجاهات المكانية"""
    RIGHT = "يمين"
    LEFT = "يسار"
    UP = "فوق"
    DOWN = "تحت"
    FRONT = "أمام"
    BACK = "خلف"
    FUTURE = "مستقبل"
    PAST = "ماضي"
    HERE = "هنا"
    NOW = "الآن"


@dataclass
class SemanticVector:
    """
    متجه دلالي 4D للفضاء الزماني-المكاني.
    
    يمثل موقعاً أو اتجاهاً في الفضاء الدلالي رباعي الأبعاد.
    
    Attributes:
        x: البعد الأفقي (يمين موجب، يسار سالب)
        y: البعد العمودي (فوق موجب، تحت سالب)
        z: البعد العمقي (أمام موجب، خلف سالب)
        t: البعد الزمني (مستقبل موجب، ماضي سالب)
    """
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    t: float = 0.0
    
    def add(self, other: 'SemanticVector') -> 'SemanticVector':
        """جمع متجهين"""
        return SemanticVector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.t + other.t
        )
    
    def subtract(self, other: 'SemanticVector') -> 'SemanticVector':
        """طرح متجه من آخر"""
        return SemanticVector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.t - other.t
        )
    
    def invert(self) -> 'SemanticVector':
        """عكس المتجه (الاتجاه المعاكس)"""
        return SemanticVector(-self.x, -self.y, -self.z, -self.t)
    
    def scale(self, factor: float) -> 'SemanticVector':
        """تكبير/تصغير المتجه"""
        return SemanticVector(
            self.x * factor,
            self.y * factor,
            self.z * factor,
            self.t * factor
        )
    
    def magnitude(self) -> float:
        """حساب طول المتجه"""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.t**2)
    
    def normalize(self) -> 'SemanticVector':
        """تطبيع المتجه (جعل طوله 1)"""
        mag = self.magnitude()
        if mag == 0:
            return SemanticVector(0, 0, 0, 0)
        return self.scale(1.0 / mag)
    
    def dot(self, other: 'SemanticVector') -> float:
        """الجداء النقطي"""
        return (self.x * other.x + self.y * other.y + 
                self.z * other.z + self.t * other.t)
    
    def distance_to(self, other: 'SemanticVector') -> float:
        """حساب المسافة إلى متجه آخر"""
        return self.subtract(other).magnitude()
    
    def equals(self, other: 'SemanticVector', tolerance: float = 0.0001) -> bool:
        """مقارنة متجهين"""
        return (abs(self.x - other.x) < tolerance and
                abs(self.y - other.y) < tolerance and
                abs(self.z - other.z) < tolerance and
                abs(self.t - other.t) < tolerance)
    
    def to_tuple(self) -> Tuple[float, float, float, float]:
        """تحويل إلى tuple"""
        return (self.x, self.y, self.z, self.t)
    
    def to_dict(self) -> Dict[str, float]:
        """تحويل إلى قاموس"""
        return {'x': self.x, 'y': self.y, 'z': self.z, 't': self.t}
    
    def __str__(self) -> str:
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f}, {self.t:.2f})"
    
    def __repr__(self) -> str:
        return f"SemanticVector(x={self.x}, y={self.y}, z={self.z}, t={self.t})"
    
    # ═══════════════════════════════════════════════════════════════
    # الاتجاهات المعيارية - Standard Directions
    # ═══════════════════════════════════════════════════════════════
    
    @classmethod
    def ZERO(cls) -> 'SemanticVector':
        """نقطة الأصل"""
        return cls(0, 0, 0, 0)
    
    # الاتجاهات المكانية - Spatial
    @classmethod
    def RIGHT(cls) -> 'SemanticVector':
        """يمين"""
        return cls(1, 0, 0, 0)
    
    @classmethod
    def LEFT(cls) -> 'SemanticVector':
        """يسار"""
        return cls(-1, 0, 0, 0)
    
    @classmethod
    def UP(cls) -> 'SemanticVector':
        """فوق"""
        return cls(0, 1, 0, 0)
    
    @classmethod
    def DOWN(cls) -> 'SemanticVector':
        """تحت"""
        return cls(0, -1, 0, 0)
    
    @classmethod
    def FRONT(cls) -> 'SemanticVector':
        """أمام"""
        return cls(0, 0, 1, 0)
    
    @classmethod
    def BACK(cls) -> 'SemanticVector':
        """خلف"""
        return cls(0, 0, -1, 0)
    
    # الاتجاهات الزمنية - Temporal
    @classmethod
    def FUTURE(cls) -> 'SemanticVector':
        """مستقبل"""
        return cls(0, 0, 0, 1)
    
    @classmethod
    def PAST(cls) -> 'SemanticVector':
        """ماضي"""
        return cls(0, 0, 0, -1)
    
    @classmethod
    def NOW(cls) -> 'SemanticVector':
        """الآن (الحاضر)"""
        return cls(0, 0, 0, 0)


@dataclass
class SpatialRelation:
    """
    علاقة مكانية-زمنية بين مفهومين.
    
    مثال: "أحمد أمام البيت" → SpatialRelation("أحمد", FRONT, "البيت")
    
    Attributes:
        subject: الفاعل (الشيء الذي نصفه)
        vector: المتجه الدلالي للعلاقة
        object: المفعول به (المرجع)
        strength: قوة العلاقة (0-1)
    """
    subject: str
    vector: SemanticVector
    object: str
    strength: float = 1.0
    
    def invert(self) -> 'SpatialRelation':
        """
        عكس العلاقة.
        
        مثال: "أحمد أمام البيت" ← → "البيت خلف أحمد"
        """
        return SpatialRelation(
            self.object,
            self.vector.invert(),
            self.subject,
            self.strength
        )
    
    def to_natural_language(self, language: str = 'ar') -> str:
        """تحويل العلاقة إلى لغة طبيعية"""
        direction = self._vector_to_direction(language)
        
        if language == 'ar':
            return f"{self.subject} {direction} {self.object}"
        else:
            return f"{self.subject} is {direction} {self.object}"
    
    def _vector_to_direction(self, language: str = 'ar') -> str:
        """تحويل المتجه إلى وصف اتجاهي"""
        directions_ar = {
            (1, 0, 0, 0): "يمين",
            (-1, 0, 0, 0): "يسار",
            (0, 1, 0, 0): "فوق",
            (0, -1, 0, 0): "تحت",
            (0, 0, 1, 0): "أمام",
            (0, 0, -1, 0): "خلف",
            (0, 0, 0, 1): "بعد",
            (0, 0, 0, -1): "قبل",
        }
        
        directions_en = {
            (1, 0, 0, 0): "to the right of",
            (-1, 0, 0, 0): "to the left of",
            (0, 1, 0, 0): "above",
            (0, -1, 0, 0): "below",
            (0, 0, 1, 0): "in front of",
            (0, 0, -1, 0): "behind",
            (0, 0, 0, 1): "after",
            (0, 0, 0, -1): "before",
        }
        
        # تطبيع المتجه للمقارنة
        normalized = self.vector.normalize()
        key = (
            round(normalized.x),
            round(normalized.y),
            round(normalized.z),
            round(normalized.t)
        )
        
        directions = directions_ar if language == 'ar' else directions_en
        return directions.get(key, "بالقرب من" if language == 'ar' else "near")
    
    def to_dict(self) -> Dict[str, Any]:
        """تحويل إلى قاموس"""
        return {
            'subject': self.subject,
            'vector': self.vector.to_dict(),
            'object': self.object,
            'strength': self.strength
        }
    
    def __str__(self) -> str:
        return self.to_natural_language('ar')


@dataclass
class MentalObject:
    """
    كائن ذهني في الفضاء الدلالي.
    
    يمثل مفهوماً أو كائناً مع موقعه وخصائصه في الفضاء 4D.
    
    Attributes:
        name: اسم الكائن
        position: موقعه في الفضاء الدلالي
        scale: حجمه (0-1+)
        properties: خصائص إضافية
    """
    name: str
    position: SemanticVector = field(default_factory=SemanticVector.ZERO)
    scale: float = 1.0
    properties: Dict[str, Any] = field(default_factory=dict)
    
    def move_by(self, delta: SemanticVector) -> 'MentalObject':
        """تحريك الكائن"""
        return MentalObject(
            self.name,
            self.position.add(delta),
            self.scale,
            self.properties.copy()
        )
    
    def move_to(self, new_position: SemanticVector) -> 'MentalObject':
        """نقل الكائن إلى موقع جديد"""
        return MentalObject(
            self.name,
            new_position,
            self.scale,
            self.properties.copy()
        )
    
    def distance_to(self, other: 'MentalObject') -> float:
        """المسافة إلى كائن آخر"""
        return self.position.distance_to(other.position)
    
    def relation_to(self, other: 'MentalObject') -> SpatialRelation:
        """العلاقة المكانية مع كائن آخر"""
        vector = other.position.subtract(self.position)
        return SpatialRelation(self.name, vector, other.name)
    
    def to_dict(self) -> Dict[str, Any]:
        """تحويل إلى قاموس"""
        return {
            'name': self.name,
            'position': self.position.to_dict(),
            'scale': self.scale,
            'properties': self.properties
        }


@dataclass
class MentalScene:
    """
    مشهد ذهني يحتوي على كائنات متعددة.
    
    يمثل "صورة ذهنية" كاملة مع جميع الكائنات والعلاقات.
    """
    name: str = "مشهد"
    objects: List[MentalObject] = field(default_factory=list)
    relations: List[SpatialRelation] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def add_object(self, obj: MentalObject) -> None:
        """إضافة كائن للمشهد"""
        self.objects.append(obj)
    
    def add_relation(self, relation: SpatialRelation) -> None:
        """إضافة علاقة للمشهد"""
        self.relations.append(relation)
    
    def get_object(self, name: str) -> Optional[MentalObject]:
        """البحث عن كائن بالاسم"""
        for obj in self.objects:
            if obj.name == name:
                return obj
        return None
    
    def get_relations_for(self, name: str) -> List[SpatialRelation]:
        """الحصول على جميع علاقات كائن معين"""
        return [r for r in self.relations 
                if r.subject == name or r.object == name]
    
    def compute_all_relations(self) -> List[SpatialRelation]:
        """حساب جميع العلاقات بين الكائنات"""
        relations = []
        for i, obj1 in enumerate(self.objects):
            for obj2 in self.objects[i+1:]:
                relations.append(obj1.relation_to(obj2))
        return relations
    
    def describe(self, language: str = 'ar') -> str:
        """وصف المشهد بلغة طبيعية"""
        descriptions = []
        
        if language == 'ar':
            descriptions.append(f"المشهد: {self.name}")
            descriptions.append(f"عدد الكائنات: {len(self.objects)}")
            
            for relation in self.relations:
                descriptions.append(f"  - {relation.to_natural_language('ar')}")
        else:
            descriptions.append(f"Scene: {self.name}")
            descriptions.append(f"Objects: {len(self.objects)}")
            
            for relation in self.relations:
                descriptions.append(f"  - {relation.to_natural_language('en')}")
        
        return "\n".join(descriptions)
    
    def to_dict(self) -> Dict[str, Any]:
        """تحويل إلى قاموس"""
        return {
            'name': self.name,
            'objects': [o.to_dict() for o in self.objects],
            'relations': [r.to_dict() for r in self.relations],
            'metadata': self.metadata
        }


# ═══════════════════════════════════════════════════════════════
# دوال مساعدة - Helper Functions
# ═══════════════════════════════════════════════════════════════

def create_scene_from_sentence(sentence: str) -> MentalScene:
    """
    إنشاء مشهد ذهني من جملة.
    
    مثال: "أحمد أمام البيت" → مشهد بكائنين وعلاقة
    """
    scene = MentalScene(name=sentence)
    
    # كلمات الاتجاهات
    direction_words = {
        'أمام': SemanticVector.FRONT(),
        'خلف': SemanticVector.BACK(),
        'فوق': SemanticVector.UP(),
        'تحت': SemanticVector.DOWN(),
        'يمين': SemanticVector.RIGHT(),
        'يسار': SemanticVector.LEFT(),
        'قبل': SemanticVector.PAST(),
        'بعد': SemanticVector.FUTURE(),
        'in front of': SemanticVector.FRONT(),
        'behind': SemanticVector.BACK(),
        'above': SemanticVector.UP(),
        'below': SemanticVector.DOWN(),
        'before': SemanticVector.PAST(),
        'after': SemanticVector.FUTURE(),
    }
    
    # تحليل بسيط (يمكن تحسينه لاحقاً)
    words = sentence.split()
    
    for direction, vector in direction_words.items():
        if direction in sentence:
            # محاولة استخراج الفاعل والمفعول
            parts = sentence.split(direction)
            if len(parts) == 2:
                subject = parts[0].strip()
                obj = parts[1].strip()
                
                if subject and obj:
                    # إنشاء الكائنات
                    subj_obj = MentalObject(subject, SemanticVector.ZERO())
                    obj_obj = MentalObject(obj, vector)
                    
                    scene.add_object(subj_obj)
                    scene.add_object(obj_obj)
                    scene.add_relation(SpatialRelation(subject, vector, obj))
                    break
    
    return scene


def interpolate_vectors(v1: SemanticVector, v2: SemanticVector, 
                        t: float) -> SemanticVector:
    """
    استيفاء خطي بين متجهين.
    
    Args:
        v1: المتجه الأول
        v2: المتجه الثاني
        t: معامل الاستيفاء (0-1)
    
    Returns:
        المتجه الناتج
    """
    t = max(0, min(1, t))  # تقييد t بين 0 و 1
    return SemanticVector(
        v1.x + (v2.x - v1.x) * t,
        v1.y + (v2.y - v1.y) * t,
        v1.z + (v2.z - v1.z) * t,
        v1.t + (v2.t - v1.t) * t
    )


# تصدير الكلاسات والدوال
__all__ = [
    'SemanticVector',
    'SpatialRelation', 
    'SpatialDirection',
    'MentalObject',
    'MentalScene',
    'create_scene_from_sentence',
    'interpolate_vectors'
]
