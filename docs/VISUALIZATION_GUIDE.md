# دليل التصور - Visualization Guide

## 📊 نظرة عامة - Overview

يوفر **بيان** أدوات تصور قوية للنموذج الوجودي، تسمح لك بتصور:
- البيئات مع أبعادها (Environments with dimensions)
- العلاقات بين الكائنات (Relations between beings)
- الكائنات في سياقها (Beings in context)
- المجالات الكاملة (Complete domains)

**Bayan** provides powerful visualization tools for the existential model, allowing you to visualize:
- Environments with their dimensions
- Relations between beings
- Beings in their context
- Complete domains

---

## 🎨 الدوال المتاحة - Available Functions

### 1. `visualize_environment(env_name)` - تصور البيئة

تصور بيئة مع جميع أبعادها (المكانية، الزمانية، المجالية).

Visualizes an environment with all its dimensions (spatial, temporal, domain-specific).

**المعاملات - Parameters:**
- `env_name` (str): اسم البيئة - Environment name

**الإرجاع - Returns:**
- كود Mermaid diagram - Mermaid diagram code

**مثال - Example:**
```bayan
diagram = visualize_environment("محلول_مائي")
print(diagram)
```

---

### 2. `visualize_relations(domain_name)` - تصور العلاقات

تصور العلاقات بين الكائنات كرسم بياني.

Visualizes relations between beings as a graph.

**المعاملات - Parameters:**
- `domain_name` (str, optional): اسم المجال (None لجميع المجالات) - Domain name (None for all domains)

**الإرجاع - Returns:**
- كود Mermaid diagram - Mermaid diagram code

**مثال - Example:**
```bayan
# تصور علاقات مجال معين
diagram = visualize_relations("الكيمياء")

# تصور جميع العلاقات
all_diagram = visualize_relations(None)
```

---

### 3. `visualize_being(being_name)` - تصور الكائن

تصور كائن مع جميع خصائصه، علاقاته، ومعانيه.

Visualizes a being with all its properties, relations, and meanings.

**المعاملات - Parameters:**
- `being_name` (str): اسم الكائن - Being name

**الإرجاع - Returns:**
- كود Mermaid diagram - Mermaid diagram code

**مثال - Example:**
```bayan
diagram = visualize_being("صوديوم")
print(diagram)
```

---

### 4. `visualize_domain(domain_name)` - تصور المجال

تصور مجال كامل مع إحصائيات عن الكائنات، العلاقات، الأفعال، والقوانين.

Visualizes a complete domain with statistics about beings, relations, actions, and laws.

**المعاملات - Parameters:**
- `domain_name` (str): اسم المجال - Domain name

**الإرجاع - Returns:**
- كود Mermaid diagram - Mermaid diagram code

**مثال - Example:**
```bayan
diagram = visualize_domain("الكيمياء")
print(diagram)
```

---

### 5. `save_visualization(mermaid_code, filename, title)` - حفظ التصور

حفظ تصور كملف HTML تفاعلي.

Saves a visualization as an interactive HTML file.

**المعاملات - Parameters:**
- `mermaid_code` (str): كود Mermaid - Mermaid diagram code
- `filename` (str): اسم الملف - File name
- `title` (str, optional): عنوان الصفحة - Page title

**الإرجاع - Returns:**
- اسم الملف المحفوظ - Saved file name

**مثال - Example:**
```bayan
diagram = visualize_domain("الكيمياء")
save_visualization(diagram, "chemistry_viz.html", "مجال الكيمياء")
```

---

## 📝 أمثلة كاملة - Complete Examples

### مثال 1: تصور بيئة - Environment Visualization

```bayan
# تعريف بيئة
بيئة "محلول_مائي" في_مجال "الكيمياء":
{
    "أبعاد": {
        "مكاني": {
            "حجم": "1 لتر",
            "درجة_حرارة": "25 درجة مئوية"
        },
        "زماني": {
            "زمن_التفاعل": "10 دقائق"
        },
        "مجالي": {
            "pH": 7.0,
            "تركيز": "1 مولار"
        }
    }
}

# تصور البيئة
env_diagram = visualize_environment("محلول_مائي")
save_visualization(env_diagram, "environment.html", "البيئة المائية")
```

---

### مثال 2: تصور العلاقات - Relations Visualization

```bayan
# تصور العلاقات بين العناصر الكيميائية
relations_diagram = visualize_relations("الكيمياء")
save_visualization(relations_diagram, "relations.html", "العلاقات الكيميائية")
```

---

### مثال 3: تصور كائن - Being Visualization

```bayan
# تصور عنصر الصوديوم
sodium_diagram = visualize_being("صوديوم")
save_visualization(sodium_diagram, "sodium.html", "عنصر الصوديوم")
```

---

### مثال 4: تصور مجال كامل - Domain Visualization

```bayan
# تصور مجال الكيمياء بالكامل
chemistry_diagram = visualize_domain("الكيمياء")
save_visualization(chemistry_diagram, "chemistry.html", "مجال الكيمياء")
```

---

## 🎯 حالات استخدام متقدمة - Advanced Use Cases

### 1. مقارنة كائنات - Comparing Beings

```bayan
# تصور عنصرين للمقارنة
sodium_viz = visualize_being("صوديوم")
gold_viz = visualize_being("ذهب")

save_visualization(sodium_viz, "sodium.html", "الصوديوم - عنصر نشط")
save_visualization(gold_viz, "gold.html", "الذهب - عنصر خامل")
```

### 2. تصور نتائج الاستعلامات - Visualizing Query Results

```bayan
# استعلام عن العناصر النشطة
active_elements = استعلام_وجودي:
{
    "في_مجال": "الكيمياء",
    "عن": "عنصر",
    "شروط": {"نشاط": "عالي"}
}

# تصور العلاقات بين العناصر النشطة
active_relations = visualize_relations("الكيمياء")
save_visualization(active_relations, "active_elements.html", "العناصر النشطة")
```

### 3. تصور متعدد المجالات - Multi-Domain Visualization

```bayan
# تصور مجالات مختلفة
chemistry_viz = visualize_domain("الكيمياء")
physics_viz = visualize_domain("الفيزياء")
math_viz = visualize_domain("الرياضيات")

save_visualization(chemistry_viz, "chemistry.html", "الكيمياء")
save_visualization(physics_viz, "physics.html", "الفيزياء")
save_visualization(math_viz, "mathematics.html", "الرياضيات")
```

---

## 🔧 التخصيص - Customization

### تخصيص ملفات HTML - Customizing HTML Files

الملفات المحفوظة هي ملفات HTML قياسية يمكن تخصيصها:

The saved files are standard HTML files that can be customized:

1. **تغيير الألوان - Change Colors**: عدّل CSS في الملف
2. **إضافة محتوى - Add Content**: أضف نصوص أو صور إضافية
3. **تغيير التخطيط - Change Layout**: عدّل هيكل HTML

---

## 📊 تنسيق Mermaid - Mermaid Format

جميع التصورات تستخدم **Mermaid.js** لإنشاء رسوم بيانية تفاعلية.

All visualizations use **Mermaid.js** to create interactive diagrams.

### أنواع الرسوم - Diagram Types

1. **graph TD** - رسم بياني من أعلى لأسفل (Top-Down graph)
2. **graph LR** - رسم بياني من اليسار لليمين (Left-Right graph)

### العناصر المستخدمة - Elements Used

- **Nodes** (العقد): مستطيلات تمثل الكائنات والخصائص
- **Edges** (الحواف): أسهم تمثل العلاقات
- **Labels** (التسميات): نصوص توضيحية

---

## 🎨 الرموز التعبيرية - Emojis

التصورات تستخدم رموز تعبيرية لتحسين الوضوح:

Visualizations use emojis to improve clarity:

| الرمز | Emoji | المعنى | Meaning |
|-------|-------|--------|---------|
| 🌟 | Star | كائن وجودي | Existential being |
| 🌍 | Globe | بيئة | Environment |
| 📚 | Books | مجال | Domain |
| 🧭 | Compass | أبعاد مكانية | Spatial dimensions |
| ⏰ | Clock | أبعاد زمانية | Temporal dimensions |
| 🔬 | Microscope | أبعاد مجالية | Domain-specific dimensions |
| ⚙️ | Gear | خصائص | Properties |
| 🔗 | Link | علاقات | Relations |
| 💡 | Bulb | معانٍ | Meanings |
| 👥 | People | كائنات | Beings |
| ⚡ | Lightning | أفعال | Actions |
| ⚖️ | Scale | قوانين | Laws |

---

## 🚀 نصائح للأداء - Performance Tips

### 1. تحديد المجال - Specify Domain

عند تصور العلاقات، حدد المجال لتحسين الأداء:

When visualizing relations, specify the domain for better performance:

```bayan
# أفضل - Better
diagram = visualize_relations("الكيمياء")

# أبطأ - Slower
diagram = visualize_relations(None)  # جميع المجالات
```

### 2. تحديد النطاق - Limit Scope

للمجالات الكبيرة، استخدم الاستعلامات لتصفية الكائنات:

For large domains, use queries to filter beings:

```bayan
# استعلام محدد
specific_beings = استعلام_وجودي:
{
    "في_مجال": "الكيمياء",
    "عن": "عنصر",
    "شروط": {"مجموعة": "فلزات"},
    "حد": 10
}
```

### 3. حفظ الملفات - Save Files

احفظ التصورات كملفات HTML بدلاً من طباعة كود Mermaid:

Save visualizations as HTML files instead of printing Mermaid code:

```bayan
# أفضل - Better
save_visualization(diagram, "output.html", "العنوان")

# أقل فائدة - Less useful
print(diagram)
```

---

## 📖 أمثلة إضافية - Additional Examples

راجع الملفات التالية لأمثلة كاملة:

See the following files for complete examples:

- `examples/visualization_demo.by` - أمثلة شاملة
- `tests/test_visualization.py` - اختبارات التصور

---

## 🎊 الخلاصة - Conclusion

أدوات التصور في **بيان** تجعل من السهل:
- فهم البنية المعقدة للنموذج الوجودي
- استكشاف العلاقات بين الكائنات
- توثيق المجالات المعرفية
- مشاركة المعرفة بصرياً

Visualization tools in **Bayan** make it easy to:
- Understand complex existential model structures
- Explore relations between beings
- Document knowledge domains
- Share knowledge visually

**بيان - لغة البرمجة الفلسفية الأولى في العالم!**

**Bayan - The World's First Philosophical Programming Language!**

