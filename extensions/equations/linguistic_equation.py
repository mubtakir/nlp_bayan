"""
نظام المعادلات اللغوية (Linguistic Equation System)
===================================================

تمثيل المعلومات والأفكار كمعادلات رياضية لغوية.

الفلسفة الأساسية:
    الفكرة = (أشياء + حدث + نتيجة)
    
    حيث:
        - الأشياء: الكيانات المشاركة في الحدث
        - الحدث: الفعل أو التفاعل
        - النتيجة: التغيرات في خصائص وحالات الأشياء

الصيغة الرياضية:
    الأشياء + الحدث = النتيجة
    
    مثال:
    محمد (فاعل) + أكل (فعل) + تفاحة (مفعول به) = 
        [محمد: جوع↓، طاقة↑] + [تفاحة: موجود=False]

المؤلف: باسل يحيى عبد الله
التاريخ: 2025-11-25
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum
import re


# ═══════════════════════════════════════════════════════════════
# 1. التعريفات الأساسية
# ═══════════════════════════════════════════════════════════════

class Role(Enum):
    """دور الكائن في المعادلة اللغوية"""
    SUBJECT = "فاعل"           # الذي يقوم بالفعل
    OBJECT = "مفعول_به"       # الذي يقع عليه الفعل
    PASSIVE_RECEIVER = "متلقي"  # متلقي غير مباشر
    INSTRUMENT = "أداة"         # أداة الفعل
    LOCATION = "مكان"           # مكان الحدث
    TIME = "زمان"               # زمان الحدث
    CAUSE = "سبب"               # سبب الحدث
    RESULT = "نتيجة"            # نتيجة الحدث


class EventType(Enum):
    """أنواع الأحداث/الأفعال"""
    PHYSICAL_ACTION = "فعل_مادي"      # أكل، ضرب، كسر
    MENTAL_ACTION = "فعل_عقلي"        # فكر، تذكر، نسي
    COMMUNICATION = "تواصل"            # قال، كتب، سأل
    MOVEMENT = "حركة"                  # ذهب، جاء، رجع
    TRANSFORMATION = "تحول"            # أصبح، تحول، تغير
    POSSESSION = "امتلاك"              # ملك، أخذ، أعطى
    EMOTION = "انفعال"                 # غضب، فرح، حزن
    CREATION = "إنشاء"                 # بنى، كتب، صنع
    DESTRUCTION = "تدمير"              # هدم، كسر، أتلف


@dataclass
class EntityState:
    """
    حالة الكائن بعد الحدث.
    
    يصف التغيرات التي طرأت على خصائص وحالات الكائن.
    """
    entity_name: str
    state_changes: Dict[str, Any]  # التغيرات: {اسم_الحالة: التغير}
    description: str = ""
    
    def __str__(self):
        changes_str = ", ".join([f"{k}: {v}" for k, v in self.state_changes.items()])
        return f"{self.entity_name} [{changes_str}]"
    
    def to_dict(self):
        """تحويل إلى قاموس"""
        return {
            'entity_name': self.entity_name,
            'state_changes': self.state_changes,
            'description': self.description
        }


# ═══════════════════════════════════════════════════════════════
# 2. المعادلة اللغوية الأساسية
# ═══════════════════════════════════════════════════════════════

@dataclass
class LinguisticEquation:
    """
    المعادلة اللغوية: الأشياء + الحدث = النتيجة
    
    مثال: 
        محمد (فاعل) + أكل (فعل) + تفاحة (مفعول به) = 
            [محمد شبع، التفاحة اختفت]
    """
    
    # المدخلات
    entities: Dict[str, Role]  # {اسم_الكائن: دوره}
    event: str                  # الفعل/الحدث
    event_type: EventType
    
    # السياق
    location: Optional[str] = None
    time: Optional[str] = None
    preposition: Optional[str] = None  # حرف الجر
    adverb: Optional[str] = None       # الظرف
    adjective: Optional[str] = None    # الصفة
    condition: Optional[str] = None    # الشرط
    conditions: List[str] = field(default_factory=list)
    
    # النتائج
    results: List[EntityState] = field(default_factory=list)
    
    # البيانات الوصفية
    confidence: float = 1.0
    source: str = "manual"
    
    def compute_results(self, knowledge_base: 'KnowledgeBase') -> List[EntityState]:
        """
        حساب النتائج بناءً على قاعدة المعرفة.
        
        Args:
            knowledge_base: قاعدة المعرفة السببية
            
        Returns:
            قائمة بالنتائج المتوقعة
        """
        # إذا كانت النتائج محددة مسبقاً، نعيدها
        if self.results:
            return self.results
        
        # وإلا نستنتجها من قاعدة المعرفة
        subject = self._get_entity_by_role(Role.SUBJECT)
        obj = self._get_entity_by_role(Role.OBJECT)
        
        return knowledge_base.infer_results(self.event, subject, obj)
    
    def _get_entity_by_role(self, role: Role) -> Optional[str]:
        """الحصول على كيان بدور معين"""
        for entity, entity_role in self.entities.items():
            if entity_role == role:
                return entity
        return None
    
    def to_natural_language(self) -> str:
        """
        تحويل المعادلة إلى جملة طبيعية عربية.
        
        Returns:
            جملة عربية تصف المعادلة
        """
        # إيجاد الفاعل والمفعول به
        subject = self._get_entity_by_role(Role.SUBJECT)
        obj = self._get_entity_by_role(Role.OBJECT)
        
        # بناء الجملة الأساسية
        sentence = f"{subject} {self.event}" if subject else self.event
        if obj:
            sentence += f" {obj}"
        
        # إضافة السياق
        if self.location:
            sentence += f" في {self.location}"
        if self.time:
            sentence += f" {self.time}"
        
        return sentence
    
    def to_formal_notation(self) -> str:
        """
        تحويل المعادلة إلى صيغة رسمية رياضية.
        
        Returns:
            الصيغة الرياضية: أشياء + حدث = نتائج
        """
        # الأشياء
        entities_str = " + ".join([f"{k}({v.value})" for k, v in self.entities.items()])
        
        # النتائج
        results_str = " + ".join([str(r) for r in self.results]) if self.results else "؟"
        
        return f"{entities_str} + {self.event} = {results_str}"
    
    def to_dict(self):
        """تحويل إلى قاموس للتخزين"""
        return {
            'entities': {k: v.value for k, v in self.entities.items()},
            'event': self.event,
            'event_type': self.event_type.value,
            'location': self.location,
            'time': self.time,
            'conditions': self.conditions,
            'results': [r.to_dict() for r in self.results],
            'confidence': self.confidence,
            'source': self.source
        }
    
    def __str__(self):
        nl = self.to_natural_language()
        formal = self.to_formal_notation()
        return f"{nl}\n  → {formal}"


# ═══════════════════════════════════════════════════════════════
# 3. قاعدة المعرفة اللغوية
# ═══════════════════════════════════════════════════════════════

class KnowledgeBase:
    """
    قاعدة معرفة تخزن المعادلات اللغوية والعلاقات السببية.
    
    تحتوي على:
        - معادلات لغوية سابقة
        - علاقات سببية (حدث → نتائج)
        - نتائج متوقعة للأفعال
    """
    
    def __init__(self):
        # قاعدة المعادلات المخزنة
        self.equations: List[LinguisticEquation] = []
        
        # قاعدة العلاقات السببية
        self.causal_relations: Dict[str, List[str]] = {}
        
        # قاموس الأفعال ونتائجها المتوقعة
        self.event_outcomes: Dict[str, Dict[str, Any]] = {}
        
        self._initialize_basic_knowledge()
    
    def _initialize_basic_knowledge(self):
        """تهيئة معرفة أساسية"""
        
        # علاقات سببية أساسية
        self.causal_relations = {
            "أكل": ["شبع", "انتعش", "نقص_الطعام"],
            "ضرب": ["ألم", "أذى", "غضب"],
            "ذهب": ["انتقل", "غياب", "وصول"],
            "نام": ["استراحة", "تعب_أقل", "غياب_وعي"],
            "شرب": ["ارتواء", "نقص_العطش", "نقص_الماء"],
            "كتب": ["إنشاء_نص", "تعب_يد", "استهلاك_ورق"],
            "بنى": ["إنشاء_مبنى", "تعب", "استهلاك_مواد"],
        }
        
        # نتائج الأفعال المتوقعة (على الفاعل والمفعول به)
        self.event_outcomes = {
            "أكل": {
                "subject_changes": {"جوع": -0.5, "طاقة": +0.3, "سعادة": +0.1},
                "object_changes": {"موجود": False, "كمية": -1.0}
            },
            "ضرب": {
                "subject_changes": {"غضب": +0.2, "تعب": +0.1},
                "object_changes": {"ألم": +0.6, "سعادة": -0.4}
            },
            "شرب": {
                "subject_changes": {"عطش": -0.6, "رطوبة": +0.3},
                "object_changes": {"كمية": -1.0, "موجود": False}
            },
            "ذهب": {
                "subject_changes": {"موقع": "جديد", "تعب": +0.2},
                "object_changes": {}
            },
            "نام": {
                "subject_changes": {"تعب": -0.7, "طاقة": +0.6, "وعي": -1.0},
                "object_changes": {}
            },
            "كتب": {
                "subject_changes": {"تعب_يد": +0.3, "تركيز": -0.2},
                "object_changes": {"موجود": True, "نوع": "نص"}
            }
        }
    
    def add_equation(self, equation: LinguisticEquation):
        """
        إضافة معادلة جديدة إلى قاعدة المعرفة.
        
        Args:
            equation: المعادلة اللغوية
        """
        self.equations.append(equation)
    
    def find_similar_equations(self, event: str, entities: List[str]) -> List[LinguisticEquation]:
        """
        البحث عن معادلات مشابهة.
        
        Args:
            event: الحدث المطلوب
            entities: قائمة بأسماء الكيانات
            
        Returns:
            قائمة بالمعادلات المشابهة
        """
        similar = []
        for eq in self.equations:
            if eq.event == event:
                # تحقق من التشابه في الكائنات
                eq_entities = set(eq.entities.keys())
                if any(e in eq_entities for e in entities):
                    similar.append(eq)
        return similar
    
    def infer_results(self, event: str, subject: Optional[str] = None, 
                     obj: Optional[str] = None) -> List[EntityState]:
        """
        استنتاج النتائج المحتملة لحدث معين.
        
        Args:
            event: اسم الحدث/الفعل
            subject: الفاعل
            obj: المفعول به
            
        Returns:
            قائمة بالنتائج المستنتجة
        """
        results = []
        
        if event in self.event_outcomes:
            outcomes = self.event_outcomes[event]
            
            # نتائج الفاعل
            if subject and "subject_changes" in outcomes:
                results.append(EntityState(
                    entity_name=subject,
                    state_changes=outcomes["subject_changes"],
                    description="تغييرات الفاعل"
                ))
            
            # نتائج المفعول به
            if obj and "object_changes" in outcomes:
                results.append(EntityState(
                    entity_name=obj,
                    state_changes=outcomes["object_changes"],
                    description="تغييرات المفعول به"
                ))
        
        return results
    
    def add_custom_event(self, event: str, subject_changes: Dict[str, Any], 
                        object_changes: Dict[str, Any] = None):
        """
        إضافة حدث مخصص مع نتائجه.
        
        Args:
            event: اسم الحدث
            subject_changes: التغيرات على الفاعل
            object_changes: التغيرات على المفعول به (اختياري)
        """
        self.event_outcomes[event] = {
            "subject_changes": subject_changes,
            "object_changes": object_changes or {}
        }


# ═══════════════════════════════════════════════════════════════
# 4. محلل المعادلات اللغوية
# ═══════════════════════════════════════════════════════════════

class LinguisticEquationParser:
    """
    تحليل الجمل الطبيعية وتحويلها إلى معادلات لغوية.
    
    يدعم أنماط بسيطة:
        - فاعل + فعل
        - فاعل + فعل + مفعول به
        - جمل أكثر تعقيداً مع سياق
    """
    
    def __init__(self, knowledge_base: KnowledgeBase):
        """
        إنشاء محلل جديد.
        
        Args:
            knowledge_base: قاعدة المعرفة للاستنتاج
        """
        self.kb = knowledge_base
        
        # أنماط نحوية بسيطة (يمكن توسيعها)
        self.patterns = [
            r"([\u0600-\u06FF]+)\s+([\u0600-\u06FF]+)\s+([\u0600-\u06FF]+)",  # فاعل فعل مفعول
            r"([\u0600-\u06FF]+)\s+([\u0600-\u06FF]+)",  # فاعل فعل
        ]
    
    def parse(self, sentence: str) -> Optional[LinguisticEquation]:
        """
        تحليل جملة وإرجاع معادلة لغوية.
        
        Args:
            sentence: الجملة العربية
            
        Returns:
            معادلة لغوية أو None إذا فشل التحليل
        """
        # تنظيف الجملة
        sentence = sentence.strip()
        words = sentence.split()
        
        if len(words) < 2:
            return None
        
        # نفترض بنية بسيطة:
        # الكلمة الأولى: فاعل
        # الكلمة الثانية: فعل
        # الكلمة الثالثة (إن وجدت): مفعول به
        
        subject = words[0]
        event = words[1]
        obj = words[2] if len(words) > 2 else None
        
        # بناء القاموس
        entities = {subject: Role.SUBJECT}
        if obj:
            entities[obj] = Role.OBJECT
        
        # استنتاج النتائج من قاعدة المعرفة
        results = self.kb.infer_results(event, subject, obj)
        
        # إنشاء المعادلة
        equation = LinguisticEquation(
            entities=entities,
            event=event,
            event_type=self._infer_event_type(event),
            results=results,
            source="parsed"
        )
        
        return equation
    
    def _infer_event_type(self, event: str) -> EventType:
        """
        استنتاج نوع الحدث من اسمه.
        
        Args:
            event: اسم الفعل
            
        Returns:
            نوع الحدث
        """
        # تصنيف بسيط (يمكن تحسينه)
        physical_verbs = ["أكل", "ضرب", "كسر", "بنى", "شرب"]
        mental_verbs = ["فكر", "تذكر", "نسي", "فهم"]
        communication_verbs = ["قال", "كتب", "سأل", "أجاب"]
        movement_verbs = ["ذهب", "جاء", "رجع", "ركض"]
        
        if event in physical_verbs:
            return EventType.PHYSICAL_ACTION
        elif event in mental_verbs:
            return EventType.MENTAL_ACTION
        elif event in communication_verbs:
            return EventType.COMMUNICATION
        elif event in movement_verbs:
            return EventType.MOVEMENT
        else:
            return EventType.PHYSICAL_ACTION  # افتراضي


# ═══════════════════════════════════════════════════════════════
# 5. أمثلة تطبيقية
# ═══════════════════════════════════════════════════════════════

def example_basic_equations():
    """أمثلة على معادلات لغوية أساسية"""
    
    print("═══════════════════════════════════════════════════════")
    print("     أمثلة على المعادلات اللغوية الأساسية")
    print("═══════════════════════════════════════════════════════\n")
    
    kb = KnowledgeBase()
    
    # مثال 1: محمد أكل تفاحة
    print("📌 مثال 1: محمد أكل تفاحة\n")
    
    eq1 = LinguisticEquation(
        entities={"محمد": Role.SUBJECT, "تفاحة": Role.OBJECT},
        event="أكل",
        event_type=EventType.PHYSICAL_ACTION,
        results=[
            EntityState("محمد", {"جوع": -0.5, "طاقة": +0.3}, "شبع وانتعش"),
            EntityState("تفاحة", {"موجود": False}, "اختفت")
        ]
    )
    
    print(eq1)
    print()
    
    # مثال 2: أحمد ضرب الكرة
    print("📌 مثال 2: أحمد ضرب الكرة\n")
    
    eq2 = LinguisticEquation(
        entities={"أحمد": Role.SUBJECT, "الكرة": Role.OBJECT},
        event="ضرب",
        event_type=EventType.PHYSICAL_ACTION,
        results=[
            EntityState("أحمد", {"حماس": +0.2}, "استمتع باللعب"),
            EntityState("الكرة", {"سرعة": +5.0, "مسافة": +10.0}, "تحركت")
        ]
    )
    
    print(eq2)
    print()
    
    # مثال 3: فاطمة ذهبت إلى المدرسة
    print("📌 مثال 3: فاطمة ذهبت إلى المدرسة\n")
    
    eq3 = LinguisticEquation(
        entities={"فاطمة": Role.SUBJECT, "المدرسة": Role.LOCATION},
        event="ذهب",
        event_type=EventType.MOVEMENT,
        location="المدرسة",
        time="صباحاً",
        results=[
            EntityState("فاطمة", {"موقع": "المدرسة", "حالة": "في_الطريق"}, "انتقلت")
        ]
    )
    
    print(eq3)
    print()


def example_parsing():
    """مثال على تحليل جمل طبيعية"""
    
    print("\n" + "═" * 60)
    print("     تحليل الجمل الطبيعية إلى معادلات")
    print("═" * 60 + "\n")
    
    kb = KnowledgeBase()
    parser = LinguisticEquationParser(kb)
    
    sentences = [
        "زيد أكل خبز",
        "سارة شربت ماء",
        "علي ضرب كرة",
        "ليلى كتبت رسالة"
    ]
    
    for sentence in sentences:
        print(f"📝 الجملة: {sentence}")
        equation = parser.parse(sentence)
        if equation:
            print(f"   المعادلة: {equation.to_formal_notation()}")
            if equation.results:
                print("   النتائج المستنتجة:")
                for result in equation.results:
                    print(f"     • {result}")
        else:
            print("   ❌ فشل التحليل")
        print()


# ═══════════════════════════════════════════════════════════════
# 6. دوال مساعدة
# ═══════════════════════════════════════════════════════════════

def create_simple_equation(subject: str, event: str, obj: str = None, 
                          kb: KnowledgeBase = None) -> LinguisticEquation:
    """
    إنشاء معادلة بسيطة بسرعة.
    
    Args:
        subject: الفاعل
        event: الفعل
        obj: المفعول به (اختياري)
        kb: قاعدة المعرفة (اختياري)
        
    Returns:
        معادلة لغوية
    """
    if kb is None:
        kb = KnowledgeBase()
    
    entities = {subject: Role.SUBJECT}
    if obj:
        entities[obj] = Role.OBJECT
    
    results = kb.infer_results(event, subject, obj)
    
    return LinguisticEquation(
        entities=entities,
        event=event,
        event_type=EventType.PHYSICAL_ACTION,
        results=results
    )


if __name__ == "__main__":
    # تشغيل الأمثلة
    example_basic_equations()
    example_parsing()
    
    print("✅ جميع الأمثلة اكتملت بنجاح!")
