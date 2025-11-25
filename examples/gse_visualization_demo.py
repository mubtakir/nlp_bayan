"""
مثال شامل على محرك التصور البصري لـ GSE
==========================================

يوضح كيفية استخدام جميع دوال التصور البصري المستوحاة
من sigmoid-drawing-engine.bn

المؤلف: باسل يحيى عبد الله
"""

import sys
sys.path.insert(0, '/home/al-mubtakir/Documents/bayan_python_ide14')

from bayan.bayan.gse import GSEModel
from bayan.bayan.builtins import BuiltinFunctions as BF
import numpy as np

print("═══════════════════════════════════════════════════════")
print("   محرك التصور البصري لـ GSE - أمثلة كاملة")
print("═══════════════════════════════════════════════════════\n")

# ═══ مثال 1: visualize_components ═══
print("📊 مثال 1: رسم المكونات المنفصلة\n")

# إنشاء نموذج متعدد المكونات
model1 = BF.GSEModel(beta=0.5, gamma=1.0)
model1.add_sigmoid(alpha=2.0, n=3, k=10.0, x0=-2.0)
model1.add_sigmoid(alpha=1.5, n=2, k=5.0, x0=2.0)
model1.add_sigmoid(alpha=-1.0, n=1, k=3.0, x0=0.0)

print(f"النموذج: {len(model1.components)} مكونات sigmoid + مكون خطي")
print(f"  - Linear: {model1.beta}x + {model1.gamma}")
for i, comp in enumerate(model1.components):
    print(f"  - S{i+1}: α={comp['alpha']}, n={comp['n']}, k={comp['k']}, x₀={comp['x0']}")

# رسم جميع المكونات بألوان منفصلة
fig1 = BF.visualize_components(
    model1,
    x_range=(-5, 5),
    resolution=500,
    title="تحليل مكونات GSE - 3 Sigmoids + Linear",
    save_path="gse_components_visualization.png"
)

print("✓ تم حفظ: gse_components_visualization.png\n")

# ═══ مثال 2: plot_parametric ═══
print("─" * 60)
print("\n📐 مثال 2: رسم منحنى بارامتري (Lissajous Curve)\n")

# منحنيات Lissajous باستخدام GSE
# x = sin(3t), y = sin(2t)

x_model = BF.GSEModel(0, 0)
# تقريب sin(3t) بـ sigmoids
x_model.add_sigmoid(alpha=1.0, n=1, k=3.0, x0=1.57)    # pi/2
x_model.add_sigmoid(alpha=-2.0, n=1, k=3.0, x0=4.71)   # 3pi/2

y_model = BF.GSEModel(0, 0)
# تقريب sin(2t) بـ sigmoids
y_model.add_sigmoid(alpha=1.0, n=1, k=2.0, x0=1.57)
y_model.add_sigmoid(alpha=-2.0, n=1, k=2.0, x0=4.71)

fig2 = BF.plot_parametric(
    x_model,
    y_model,
    t_range=(0, 2*np.pi),
    resolution=600,
    title="منحنى بارامتري - Lissajous-like Curve",
    save_path="gse_parametric_curve.png"
)

print("✓ تم حفظ: gse_parametric_curve.png\n")

# ═══ مثال 3: compare_gse_models ═══
print("─" * 60)
print("\n📈 مثال 3: مقارنة عدة نماذج\n")

# نموذج خطي
linear_model = BF.GSEModel(beta=1.0, gamma=0.0)

# نموذج خطوة واحدة
step_model = BF.GSEModel(0, 0)
step_model.add_sigmoid(alpha=2.0, n=5, k=50.0, x0=0.0)

# نموذج موجة
wave_model = BF.GSEModel(0, 0)
wave_model.add_sigmoid(alpha=1.0, n=1, k=2.0, x0=-3.0)
wave_model.add_sigmoid(alpha=-1.0, n=1, k=2.0, x0=-1.0)
wave_model.add_sigmoid(alpha=1.0, n=1, k=2.0, x0=1.0)
wave_model.add_sigmoid(alpha=-1.0, n=1, k=2.0, x0=3.0)

fig3 = BF.compare_gse_models(
    [
        (linear_model, "Linear: y = x"),
        (step_model, "Step Function"),
        (wave_model, "Wave-like (4 sigmoids)")
    ],
    x_range=(-5, 5),
    resolution=500,
    title="مقارنة أنواع مختلفة من نماذج GSE",
    save_path="gse_models_comparison.png"
)

print("النماذج المقارنة:")
print("  1. Linear: y = x")
print("  2. Step: خطوة حادة واحدة")
print("  3. Wave: موجة بـ 4 مكونات sigmoid")
print("\n✓ تم حفظ: gse_models_comparison.png\n")

# ═══ مثال 4: plot_gse (بسيط) ═══
print("─" * 60)
print("\n📉 مثال 4: رسم نموذج بسيط\n")

simple_model = BF.GSEModel(0.5, 2.0)
simple_model.add_sigmoid(alpha=3.0, n=2, k=5.0, x0=0.0)

fig4 = BF.plot_gse(
    simple_model,
    x_range=(-3, 3),
    title="نموذج GSE بسيط - 1 Sigmoid + Linear",
    save_path="gse_simple_model.png"
)

print("✓ تم حفظ: gse_simple_model.png\n")

# ═══ الإحصائيات ═══
print("─" * 60)
print("\n📊 إحصائيات محرك الرسم:\n")

stats = BF.get_viz_stats()
for key, value in stats.items():
    key_ar = {
        'shapes_drawn': 'أشكال مرسومة',
        'components_visualized': 'مكونات مصورة',
        'points_plotted': 'نقاط مرسومة',
        'last_draw_time_ms': 'وقت آخر رسمة (ms)',
        'avg_points_per_shape': 'متوسط النقاط لكل شكل'
    }.get(key, key)
    print(f"  • {key_ar}: {value}")

print("\n✓ اكتملت جميع الأمثلة بنجاح!")
print("\nالملفات المحفوظة:")
print("  1. gse_components_visualization.png")
print("  2. gse_parametric_curve.png")
print("  3. gse_models_comparison.png")
print("  4. gse_simple_model.png")

# عرض الرسوم (اختياري)
# BF.show_plot()
