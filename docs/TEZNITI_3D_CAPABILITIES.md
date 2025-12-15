# توثيق قدرات تزنيتي 3D | Tezniti 3D Capabilities Documentation

---

## 1. نظام التجميعات | Assembly System

**الملف:** `tezniti_3d/assembly_system.py`

### الوصف
نظام لدمج عدة قطع في تجميع واحد مع علاقات التوصيل والقيود الهندسية.

### المكونات الرئيسية

| الفئة | الوظيفة |
|-------|---------|
| `ConstraintType` | أنواع القيود (تثبيت، تطابق، تمركز، توازي...) |
| `Transform` | تحويل هندسي (موقع + دوران) |
| `Part` | قطعة في التجميع |
| `Constraint` | قيد بين قطعتين |
| `ConstraintSolver` | حلّال القيود |
| `Assembly` | حاوية التجميع الرئيسية |
| `AssemblyBuilder` | بناء تجميعات من وصف نصي |

### أنواع القيود المدعومة

| القيد | الوظيفة |
|-------|---------|
| `FIXED` | تثبيت مطلق |
| `COINCIDENT` | تطابق نقاط |
| `CONCENTRIC` | تمركز (محاور متطابقة) |
| `PARALLEL` | توازي |
| `PERPENDICULAR` | تعامد |
| `DISTANCE` | مسافة محددة |
| `ANGLE` | زاوية محددة |
| `GEAR_MESH` | تعشيق تروس |

### الاستخدام
```python
from tezniti_3d.assembly_system import Assembly, AssemblyBuilder, ConstraintType

# إنشاء تجميع يدوي
assembly = Assembly("Gear Assembly")

# إضافة قطع
gear1 = assembly.add_part("Gear 1", "helical_gear", 
                          {"teeth": 24, "module": 2})
gear2 = assembly.add_part("Gear 2", "helical_gear",
                          {"teeth": 32, "module": 2})

# إضافة قيد تعشيق
assembly.add_constraint(ConstraintType.GEAR_MESH, gear1, gear2)

# حل القيود
assembly.solve_constraints()

# حفظ التجميع
assembly.save("my_assembly.json")

# بناء من وصف نصي
builder = AssemblyBuilder()
auto_assembly = builder.build_from_text("تجميع من 3 تروس متعشقة")
```

---

## 2. المحاكاة الحركية | Kinematic Simulation

**الملف:** `tezniti_3d/kinematic_sim.py`

### الوصف
محاكاة حركة التروس والمحاور مع حساب نسب التعشيق والسرعات.

### المكونات الرئيسية

| الفئة | الوظيفة |
|-------|---------|
| `JointType` | أنواع المفاصل (دوراني، انزلاقي، ثابت...) |
| `Joint` | مفصل في السلسلة الحركية |
| `Link` | وصلة (قطعة) في السلسلة |
| `KinematicChain` | سلسلة حركية |
| `GearMesh` | محاكاة تعشيق التروس |
| `MotionPlayer` | تشغيل الحركة مع إطارات رئيسية |
| `KinematicSimulator` | المحاكي الموحد |

### الاستخدام
```python
from tezniti_3d.kinematic_sim import KinematicSimulator, GearMesh
import math

# إنشاء المحاكي
sim = KinematicSimulator()

# إعداد سلسلة تروس
gears = [
    {"id": "gear_driver", "teeth": 20},
    {"id": "gear_driven", "teeth": 40},
    {"id": "gear_output", "teeth": 30}
]
sim.setup_gear_train(gears)

# عرض نسب التروس
for r in sim.get_gear_ratios():
    print(f"{r['gear1']} -> {r['gear2']}: {r['ratio']:.2f}")

# محاكاة الدوران
result = sim.simulate_rotation("gear_driver", rpm=100, duration=1.0)
print(f"سرعات الإخراج: {result['output_speeds']}")

# تعشيق تروس مباشر
mesh = GearMesh()
mesh.add_pair("g1", 20, "g2", 40)
angles = mesh.rotate_gear("g1", math.pi)  # نصف دورة
```

---

## 3. مساعد التصميم الذكي | Smart Design Assistant

**الملف:** `tezniti_3d/design_assistant.py`

### الوصف
يقدم تحليلات واقتراحات للتصميم الميكانيكي مع فحص التفاوتات ونصائح التصنيع.

### المكونات الرئيسية

| الفئة | الوظيفة |
|-------|---------|
| `WarningLevel` | مستوى التحذير (معلومات، تحذير، خطأ) |
| `DesignIssue` | مشكلة مكتشفة في التصميم |
| `PartRecommendation` | توصية بقطعة مناسبة |
| `DesignAdvisor` | تحليل واقتراحات |
| `PartSuggester` | اقتراح قطع مناسبة للوظيفة |
| `ToleranceChecker` | فحص التفاوتات |
| `ManufacturingAdvisor` | نصائح التصنيع |
| `SmartDesignAssistant` | المساعد الموحد |

### الاستخدام
```python
from tezniti_3d.design_assistant import SmartDesignAssistant

assistant = SmartDesignAssistant()

# قطع للتحليل
parts = [
    {"name": "Gear 1", "type": "gear", "teeth": 10, "module": 2},
    {"name": "Shaft", "type": "shaft", "diameter": 20, "length": 300}
]

# تحليل شامل
result = assistant.full_analysis(parts, purpose="نقل الحركة")

print(f"الأخطاء: {result['issue_count']['errors']}")
print(f"التحذيرات: {result['issue_count']['warnings']}")

# المشاكل المكتشفة
for issue in result['issues']:
    print(f"[{issue['level']}] {issue['message']}")
    print(f"   الحل: {issue['suggestion']}")

# اقتراحات القطع
for sugg in result['part_suggestions']:
    print(f"- {sugg['type']}: {sugg['reason']}")

# فحص التفاوت
fit = assistant.tolerance_checker.check_fit(25.02, 25.00)
print(f"نوع التوافق: {fit['fit_type']}")
```

### القواعد المدمجة
- فحص حد أدنى لأسنان الترس (< 12 = تحذير)
- فحص نسبة طول/قطر العمود (> 10 = تحذير)
- فحص سمك الجدران (< 2mm = خطأ)
- فحص توافق موديول التروس

---

## 4. مكتبة القوالب الجاهزة | Template Library

**الملف:** `tezniti_3d/template_library.py`

### الوصف
كتالوج من 28+ قالب تصميمي جاهز مصنف حسب الفئات.

### الفئات المتاحة

| الفئة | العدد | الأمثلة |
|-------|-------|---------|
| `GEARS` | 5 | ترس مستقيم، حلزوني، مخروطي، دودي |
| `BEARINGS` | 4 | رومان كروي، أسطواني، دفعي |
| `FASTENERS` | 4 | براغي، صواميل، حلقات |
| `SHAFTS` | 4 | عمود صلب، بخابور، متدرج |
| `HOUSINGS` | 2 | غلاف رومان، صندوق تروس |
| `BRACKETS` | 2 | كتيفة L، حامل محرك |
| `CONTAINERS` | 2 | صندوق، حاوية إلكترونيات |
| `FURNITURE` | 3 | سطح طاولة، رف، ظهر كرسي |
| `MECHANICAL_SYSTEMS` | 2 | زوج تروس، عمود مع رومان |

### الاستخدام
```python
from tezniti_3d.template_library import TemplateLibrary, TemplateCategory

lib = TemplateLibrary()

# عدد القوالب
print(f"إجمالي القوالب: {len(lib.get_all())}")

# التصنيفات
for cat in lib.get_categories():
    print(f"- {cat['name']}: {cat['count']} قالب")

# البحث
results = lib.search("ترس")
for t in results:
    print(f"- {t.name_ar}")

# قوالب حسب الفئة
gears = lib.get_by_category(TemplateCategory.GEARS)

# الحصول على قالب
template = lib.get("spur_gear_20")
print(f"المعاملات: {template.parameters}")

# تخصيص قالب
custom = template.customize({"teeth": 28, "module": 2.5})

# إضافة قالب مستخدم
user_id = lib.add_user_template("My Gear", "helical_gear", 
                                 {"teeth": 30, "module": 3})
```

---

## 5. واجهة الأوامر الصوتية | Voice Interface

**الملف:** `tezniti_3d/voice_interface.py`

### الوصف
تحويل الأوامر الصوتية العربية لنماذج 3D مع دعم Vosk للتعرف على الصوت.

### المكونات الرئيسية

| الفئة | الوظيفة |
|-------|---------|
| `CommandType` | أنواع الأوامر (إنشاء، تعديل، حذف...) |
| `VoiceCommand` | أمر صوتي محلل |
| `ArabicCommandParser` | تحليل الأوامر العربية |
| `VoiceRecognizer` | التعرف على الصوت (Vosk) |
| `VoiceInterface` | الواجهة الموحدة |

### الأوامر المدعومة

| الأمر | الكلمات المفتاحية |
|-------|------------------|
| إنشاء | أنشئ، صمم، اعمل، ارسم |
| تعديل | عدّل، غيّر، كبّر، صغّر |
| حذف | احذف، أزل، امسح |
| تصدير | صدّر، احفظ |
| تراجع | تراجع، ألغِ |
| مساعدة | ساعدني، كيف |

### الاستخدام
```python
from tezniti_3d.voice_interface import VoiceInterface

interface = VoiceInterface()

# معالجة نص مباشرة (بدون صوت)
result = interface.process_text("أنشئ ترس حلزوني قطر 40")
print(f"النوع: {result['command']['type']}")
print(f"القطعة: {result['command']['part_type']}")
print(f"المعاملات: {result['command']['parameters']}")

# الاستماع من الميكروفون (يتطلب vosk)
# result = interface.listen_and_execute(duration=5.0)

# تسجيل معالج مخصص
def my_handler(command):
    print(f"تنفيذ: {command.text}")
    return {"executed": True}

interface.register_handler(CommandType.CREATE, my_handler)

# عرض الأوامر المتاحة
for cmd in interface.get_available_commands():
    print(f"- {cmd}")
```

### تثبيت Vosk (اختياري)
```bash
pip install vosk sounddevice

# تحميل نموذج عربي
# https://alphacephei.com/vosk/models
```

---

## الاستيراد الموحد

```python
# التجميعات
from tezniti_3d.assembly_system import (
    Assembly, AssemblyBuilder, 
    Part, Constraint, ConstraintType
)

# المحاكاة الحركية
from tezniti_3d.kinematic_sim import (
    KinematicSimulator, GearMesh,
    KinematicChain, MotionPlayer
)

# مساعد التصميم
from tezniti_3d.design_assistant import SmartDesignAssistant

# مكتبة القوالب
from tezniti_3d.template_library import TemplateLibrary, TemplateCategory

# واجهة الصوت
from tezniti_3d.voice_interface import VoiceInterface, CommandType
```

---

*تاريخ التوثيق: 2025-12-14*
