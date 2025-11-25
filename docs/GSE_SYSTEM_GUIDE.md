# نظام GSE - معادلات الشكل المعممة التكيفية

**آخر تحديث**: 2025-11-25

## نظرة عامة

نظام **GSE** (Generalized Shape Equation) هو محرك رياضي تكيفي يتعلم من البيانات لاكتشاف المعادلات الرياضية التي تصف الأنماط.

## الفلسفة

بدلاً من استخدام **الشبكات العصبية** (black box)، نستخدم **معادلات رياضية صريحة** قابلة للتفسير:

```
f(x) = β·x + γ + Σ[αᵢ · sigmoid(k, n, x₀)]
```

## المكونات الأساسية

### 1. Sigmoid المعمم

```python
sigmoid(x, n, k, x₀) = 1 / (1 + exp(-k · (x - x₀)ⁿ))
```

**المعاملات**:
- `n`: معامل القطع (chopping coefficient) - يحدد حدة الانتقال
- `k`: الحدة (sharpness) - سرعة الانتقال
- `x₀`: نقطة المنتصف (midpoint) - مركز الانتقال
- `α`: السعة (amplitude) - ارتفاع الخطوة

### 2. GSEModel

نموذج كامل يجمع بين:
- **مكون خطي**: `β·x + γ`
- **مكونات sigmoid**: عدة خطوات/موجات

## الاستخدام الأساسي

### إنشاء نموذج يدوياً

```bayan
hybrid {
    # إنشاء نموذج جديد
    model = GSEModel(beta=0.5, gamma=1.0)
    
    # إضافة مكون sigmoid
    model.add_sigmoid(
        alpha=2.0,  # السعة
        n=3,        # القطع
        k=10.0,     # الحدة
        x0=0.0      # المنتصف
    )
    
    # تقييم عند نقطة
    x = [0.0, 0.5, 1.0, 1.5]
    y = model.evaluate(x)
    
    print(y)
}
```

### التعلم من البيانات

```bayan
hybrid {
    # بيانات التدريب
    x_data = [0, 1, 2, 3, 4, 5]
    y_data = [0, 1, 4, 9, 16, 25]  # y = x²
    
    # تعلم النموذج (يتطلب scipy)
    model = learn(
        "square_model",     # اسم النموذج
        x_data, 
        y_data,
        max_components=5,   # أقصى عدد مكونات
        epsilon=1e-4,       # عتبة التقارب
        verbose=True        # طباعة التقدم
    )
    
    # استنباط قيمة جديدة
    y_pred = infer("square_model", 2.5)
    print(f"f(2.5) = {y_pred}")  # ≈ 6.25
}
```

## خوارزمية التعلم التكيفي (ADEI)

### المرحلة 1: البناء الجشع (Greedy Build-up)

1. ملاءمة مكون خطي أولاً: `β·x + γ`
2. حساب الخطأ المتبقي (residual)
3. إضافة مكون sigmoid لتقليل الخطأ الأكبر
4. تكرار حتى:
   - الوصول لأقصى عدد مكونات، أو
   - الخطأ أقل من `epsilon`

### المرحلة 2: التحسين الشامل (Global Fine-Tuning)

- تحسين **جميع المعاملات** معاً
- استخدام `scipy.optimize.minimize`
- الهدف: تقليل MSE (Mean Squared Error)

## مثال كامل: دالة معقدة

```bayan
hybrid {
    import numpy as np
    
    # توليد بيانات مشوشة
    x = np.linspace(-5, 5, 100)
    y_true = np.sin(x) + 0.5*x
    y_noisy = y_true + np.random.normal(0, 0.1, 100)
    
    # تعلم النموذج
    model = learn(
        "complex_func",
        x.tolist(),
        y_noisy.tolist(),
        max_components=8,
        verbose=True
    )
    
    # تقييم الأداء
    y_pred = infer("complex_func", x.tolist())
    mse = np.mean((y_pred - y_true)**2)
    
    print(f"MSE: {mse:.6f}")
    print(f"Components: {len(model.components)}")
    
    # طباعة المعادلة المكتشفة
    print("\nDiscovered equation:")
    print(f"f(x) = {model.beta:.3f}·x + {model.gamma:.3f}")
    for i, comp in enumerate(model.components):
        print(f"  + {comp['alpha']:.3f} · sigmoid(k={comp['k']:.2f}, n={comp['n']}, x₀={comp['x0']:.2f})")
}
```

## الدوال المتاحة

### في `builtins.py`

#### إنشاء نماذج

```python
# إنشاء نموذج فارغ
model = GSEModel(beta=0.0, gamma=0.0)

# إضافة مكون
model.add_sigmoid(alpha, n, k, x0)

# تقييم
y = model.evaluate(x_values)
```

#### التعلم والاستنباط

```python
# تعلم نموذج
model = learn(name, x_data, y_data, max_components=10, epsilon=1e-4, verbose=False)

# استنباط
y = infer(model_name, x_value)
```

### دوال مساعدة

```python
# sigmoid واححد
y = generalized_sigmoid(x, n, k, x0)

# بوابة تقريبية (خطوة)
y = approximate_gate(x, x_min, x_max, n, k)
```

## أمثلة التطبيقات

### 1. تقريب الدوال

```bayan
# تعلم y = x³
x = range(-10, 11)
y = [i**3 for i in x]
model = learn("cubic", x, y, max_components=3)
```

### 2. تحليل البيانات

```bayan
# بيانات حقيقية من sensor
temps = [20.1, 22.3, 24.5, 23.8, 21.2, ...]
times = [0, 1, 2, 3, 4, ...]

model = learn("temperature_pattern", times, temps)
next_temp = infer("temperature_pattern", 24)  # التنبؤ بالساعة 24
```

### 3. معادلات الشكل

```bayan
# شكل جسم ثلاثي الأبعاد
tree = MotherEquation("T001", "شجرة")
shape = GSEModel(0.0, 0.0)
shape.add_sigmoid(2.0, 7, 100.0, 0.0)  # الجذع
shape.add_sigmoid(3.0, 3, 5.0, 3.0)    # الفروع
tree.set_shape_equation(shape)

y = render_shape(tree, (-5, 10), 100)
```

## المزايا

1. **قابل للتفسير**: معادلة واضحة، ليس صندوق أسود
2. **تكيفي**: يتعلم من البيانات تلقائياً
3. **دقيق**: خطأ منخفض جداً مع مكونات قليلة
4. **مرن**: يعمل مع جميع أنواع الدوال
5. **سريع**: التقييم O(n) حيث n = عدد المكونات
6. **بدون تدريب ثقيل**: لا يحتاج GPU أو epochs

## المتطلبات

- **numpy**: موجود افتراضياً
- **scipy**: مطلوب للتعلم التكيفي (`learn()`)
  ```bash
  pip install scipy
  ```

## الملفات ذات الصلة

- **الكود المصدري**:
  - [`bayan/bayan/gse.py`](file:///home/al-mubtakir/Documents/bayan_python_ide14/bayan/bayan/gse.py) - النموذج الأساسي
  - [`bayan/bayan/gse_fitting.py`](file:///home/al-mubtakir/Documents/bayan_python_ide14/bayan/bayan/gse_fitting.py) - محرك التعلم
- **الأمثلة**:
  - [`examples/gse_adaptive_demo.py`](file:///home/al-mubtakir/Documents/bayan_python_ide14/examples/gse_adaptive_demo.py) - مثال Python كامل
  - [`examples/gse_usage.bayan`](file:///home/al-mubtakir/Documents/bayan_python_ide14/examples/gse_usage.bayan) - أمثلة Bayan
- **API**: [`bayan/bayan/builtins.py`](file:///home/al-mubtakir/Documents/bayan_python_ide14/bayan/bayan/builtins.py)

## انظر أيضاً

- [نظام المعادلة الأم](MOTHER_EQUATION_GUIDE.md) - استخدام GSE للأشكال
- [المعادلات اللغوية](LINGUISTIC_EQUATIONS_GUIDE.md) - تحليل اللغة
- [أمثلة متقدمة](EXAMPLES.md) - المزيد من الأمثلة
