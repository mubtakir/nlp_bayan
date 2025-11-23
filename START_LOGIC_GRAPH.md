# دليل تشغيل واجهة المنطق الرسومية
# Guide to Running the Logic Graph Interface

## الخطوات السريعة / Quick Steps

### 1. تثبيت المتطلبات / Install Requirements
```bash
# إنشاء بيئة افتراضية (مرة واحدة فقط)
# Create virtual environment (one time only)
python3 -m venv venv

# تفعيل البيئة الافتراضية
# Activate virtual environment
source venv/bin/activate

# تثبيت Flask
# Install Flask
pip install flask
```

### 2. تشغيل الخادم / Start Server
```bash
# من مجلد المشروع الرئيسي
# From main project folder
cd /home/al-mubtakir/Documents/bayan_python_ide14
source venv/bin/activate
python3 web_ide/app.py
```

### 3. فتح المتصفح / Open Browser
افتح المتصفح وانتقل إلى:
Open browser and go to:
```
http://127.0.0.1:5001/logic_graph
```

## أمثلة للتجربة / Examples to Try

### مثال 1: حقائق بسيطة / Simple Facts
```
أحمد هو مبرمج.
المبرمج يكتب الكود.
س: ماذا يفعل أحمد؟
```

### مثال 2: قياس منطقي / Logical Syllogism
```
كل إنسان فان.
سقراط إنسان.
س: هل سقراط فان؟
```

### مثال 3: احتمالات / Probabilities
```
السماء زرقاء. [0.8]
الطقس مشمس. [0.6]
```

### مثال 4: شبكة سببية / Causal Network
```
المطر يسبب البلل.
البلل يسبب الانزلاق.
س: هل المطر يسبب الانزلاق؟
```

## استخدام الواجهة / Using the Interface

1. **المحرر (يسار)**: اكتب كود بيان هنا
   **Editor (left)**: Write Bayan code here

2. **زر "تحقق وتنفيذ ▶"**: اضغط لتشغيل الكود
   **"Verify & Run ▶" button**: Click to run code

3. **الرسم البياني (يمين)**: سيظهر الرسم البياني التفاعلي
   **Graph (right)**: Interactive graph will appear

4. **مسار التحقق**: يظهر خطوات الاستنتاج المنطقي
   **Verification Trace**: Shows logical inference steps

## الألوان في الرسم البياني / Graph Colors

- 🟢 **أخضر / Green**: كيانات (Entities)
- 🔵 **أزرق / Blue**: أحداث (Events)  
- 🟣 **بنفسجي / Purple**: قواعد سببية (Causal Rules)
- 🟠 **برتقالي / Orange**: قيم (Values)

## الخطوط / Lines

- **خط متصل**: حقيقة مؤكدة (Certain fact)
- **خط متقطع شفاف**: حقيقة احتمالية (Probabilistic fact)

## إيقاف الخادم / Stop Server
اضغط `Ctrl+C` في الطرفية
Press `Ctrl+C` in terminal
