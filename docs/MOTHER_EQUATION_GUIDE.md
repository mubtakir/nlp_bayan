# نظام المعادلة الأم (Mother Equation System)

**آخر تحديث**: 2025-11-25

## نظرة عامة

نظام المعادلة الأم هو نظام رياضي شامل يمثل الأشياء بصورة كاملة تجمع بين:
- **الخصائص الثابتة** (Φ)
- **الحالات الديناميكية** (Ψ(t))
- **معادلة الشكل** (Γ)

## الصيغة الرياضية

```
Object = (id, Φ, Ψ(t), Γ)

حيث:
  id: معرف فريد للكائن
  Φ: الخصائص الثابتة {لون، مادة، كتلة، ...}
  Ψ(t): الحالات الديناميكية {جوع، سعادة، تعب، ...}
  Γ: معادلة الشكل (GSE-based)
```

## المكونات الأساسية

### 1. PropertyDomain (مجالات الخصائص)

10 مجالات متاحة:
- `PHYSICAL` / `فيزيائي` - الخصائص الفيزيائية (طول، وزن، كتلة)
- `CHEMICAL` / `كيميائي` - التركيب الكيميائي
- `PSYCHOLOGICAL` / `نفسي` - الحالة النفسية والشخصية
- `SOCIAL` / `اجتماعي` - العلاقات والمكانة
- `BIOLOGICAL` / `بيولوجي` - الخصائص الحيوية
- `GEOMETRIC` / `هندسي` - الشكل والأبعاد
- `LINGUISTIC` / `لغوي` - الخصائص اللغوية
- `LOGICAL` / `منطقي` - القيم المنطقية
- `TEMPORAL` / `زمني` - الزمن والتاريخ
- `SPATIAL` / `مكاني` - الموقع والمكان

### 2. Property (الخاصية)

```python
Property(
    name="العمر",
    value=25,
    domain=PropertyDomain.BIOLOGICAL,
    unit="سنة",
    changeable=True
)
```

### 3. State (الحالة)

حالة ديناميكية بقيمة ضبابية (fuzzy) بين 0 و 1:

```python
State(name="الجوع", value=0.5)  # 0.0 = لا جوع، 1.0 = جوع شديد
```

### 4. MotherEquation (المعادلة الأم)

الكائن الرئيسي الذي يجمع كل شيء:

```python
obj = MotherEquation("H001", "محمد")
```

## الاستخدام

### إنشاء كائن

```bayan
hybrid {
    # إنشاء كائن إنسان
    person = MotherEquation("P001", "سارة")
    
    # إضافة خصائص ثابتة
    person.add_property("الطول", 165, PropertyDomain("فيزيائي"), "cm")
    person.add_property("الوزن", 60, PropertyDomain("فيزيائي"), "kg")
    person.add_property("فصيلة_الدم", "O+", PropertyDomain("بيولوجي"))
    person.add_property("المهنة", "مهندسة", PropertyDomain("اجتماعي"))
    
    # إضافة حالات ديناميكية
    person.add_state("الجوع", 0.3)
    person.add_state("السعادة", 0.8)
    person.add_state("التعب", 0.2)
    
    # تحديث حالة
    person.update_state("الجوع", 0.7)
    
    # الحصول على قيمة حالة
    hunger = person.get_state("الجوع")
    print("مستوى الجوع: " + str(hunger))
}
```

### إضافة معادلة شكل

```bayan
hybrid {
    tree = MotherEquation("T001", "شجرة_تفاح")
    
    # إنشاء معادلة شكل GSE
    shape = GSEModel(0.0, 0.0)
    
    # إضافة مكونات sigmoid
    shape.add_sigmoid(2.0, 5, 50.0, 0.0)  # الجذع
    shape.add_sigmoid(3.0, 2, 2.0, 3.0)   # التاج
    
    # ربط المعادلة بالكائن
    tree.set_shape_equation(shape)
    
    # رسم الشكل
    y_vals = render_shape(tree, (0, 6), 50)
}
```

### التصدير والاستيراد

```bayan
hybrid {
    person = create_example_human()
    
    # تصدير إلى JSON
    json_str = person.to_json()
    print(json_str)
    
    # استيراد من JSON
    restored = MotherEquation.from_json(json_str)
    
    print(restored.name)  # → "محمد"
    print(len(restored.fixed_properties))  # → 7
}
```

## الدوال المتاحة

### إدارة الخصائص

- `add_property(name, value, domain, unit=None, changeable=True)` - إضافة خاصية
- `update_property(name, new_value)` - تحديث خاصية
- `get_property(name)` - الحصول على قيمة خاصية

### إدارة الحالات

- `add_state(name, value)` - إضافة حالة (0..1)
- `update_state(name, new_value)` - تحديث حالة
- `get_state(name)` - الحصول على قيمة حالة

### معادلة الشكل

- `set_shape_equation(gse_model)` - تعيين معادلة الشكل
- `render_shape(x_range, resolution)` - رسم الشكل

### التصدير والاستيراد

- `to_json(indent=2)` - تصدير إلى JSON
- `from_json(json_str)` - استيراد من JSON (class method)
- `get_complete_state()` - الحصول على الحالة الكاملة

## الأمثلة المدمجة

### مثال إنسان

```bayan
human = create_example_human()
print(human)
```

يُنشئ كائن إنسان مع:
- 7 خصائص (طول، وزن، لون العيون، فصيلة الدم، إلخ)
- 4 حالات (جوع، سعادة، تعب، تركيز)

### مثال شجرة

```bayan
tree = create_example_tree()
```

يُنشئ شجرة تفاح مع:
- خصائص فيزيائية وبيولوجية
- معادلة شكل GSE (جذع + تاج)

### مثال مبنى

```bayan
building = create_example_building()
```

يُنشئ مبنى مدرسة مع:
- خصائص هندسية واجتماعية
- معادلة شكل ثلاثية الطوابق

## المزايا

1. **تمثيل شامل**: يجمع الخصائص والحالات والأشكال في كيان واحد
2. **10 مجالات**: تصنيف دقيق للخصائص
3. **حالات ضبابية**: قيم موحدة (0..1) لسهولة المقارنة
4. **معادلات شكل**: دمج مع نظام GSE للأشكال الرياضية
5. **قابلية التوسع**: سهولة إضافة خصائص وحالات جديدة
6. **تتبع التاريخ**: تسجيل جميع التغيرات
7. **JSON**: تصدير/استيراد كامل

## الملفات ذات الصلة

- **الكود المصدري**: [`bayan/bayan/mother_equation.py`](file:///home/al-mubtakir/Documents/bayan_python_ide14/bayan/bayan/mother_equation.py)
- **الأمثلة**: [`examples/mother_equation_demo.bayan`](file:///home/al-mubtakir/Documents/bayan_python_ide14/examples/mother_equation_demo.bayan)
- **API في builtins**: [`bayan/bayan/builtins.py`](file:///home/al-mubtakir/Documents/bayan_python_ide14/bayan/bayan/builtins.py)

## انظر أيضاً

- [نظام GSE](GSE_SYSTEM_GUIDE.md) - معادلات الشكل العامة
- [المعادلات اللغوية](LINGUISTIC_EQUATIONS_GUIDE.md) - تحويل اللغة إلى معادلات
- [دليل اللغة](LANGUAGE_GUIDE.md) - مرجع لغة البيان الكامل
