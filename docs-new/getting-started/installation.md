# 💾 التثبيت التفصيلي

دليل شامل لتثبيت Bayan على أنظمة مختلفة.

---

## المتطلبات الأساسية

- **Python**: 3.8 أو أحدث
- **pip**: مدير حزم Python
- **Git**: (اختياري) للاستنساخ من GitHub

### التحقق من المتطلبات

```bash
python --version    # يجب أن يكون 3.8+
pip --version      # يجب أن يكون موجود
git --version      # اختياري
```

---

## طرق التثبيت

### 1. التثبيت من GitHub (موصى به)

#### أ. باستخدام Git

```bash
# استنساخ المشروع
git clone https://github.com/mubtakir/nlp_bayan.git
cd nlp_bayan

# التثبيت في وضع التطوير
pip install -e .
```

#### ب. تحميل ZIP

1. اذهب إلى: https://github.com/mubtakir/nlp_bayan
2. اضغط "Code" → "Download ZIP"
3. استخرج الملف
4. في terminal:

```bash
cd nlp_bayan-main
pip install -e .
```

---

### 2. التثبيت في بيئة افتراضية (موصى به للمطورين)

#### Linux / macOS

```bash
# إنشاء بيئة افتراضية
python -m venv bayan_env

# تفعيلها
source bayan_env/bin/activate

# التثبيت
git clone https://github.com/mubtakir/nlp_bayan.git
cd nlp_bayan
pip install -e .
```

#### Windows

```cmd
REM إنشاء بيئة افتراضية
python -m venv bayan_env

REM تفعيلها
bayan_env\Scripts\activate

REM التثبيت
git clone https://github.com/mubtakir/nlp_bayan.git
cd nlp_bayan
pip install -e .
```

---

## التحقق من التثبيت

### 1. اختبار بسيط

```bash
echo 'print("التثبيت نجح!")' > test.bayan
python -m bayan.bayan.cli test.bayan
```

**يجب أن ترى:**
```
التثبيت نجح!
```

### 2. تشغيل الاختبارات

```bash
cd nlp_bayan
pytest tests/ -v
```

### 3. تشغيل Web IDE

```bash
cd web_ide
python app.py
```

افتح المتصفح على: `http://localhost:5000`

---

## حل المشاكل

### مشكلة: `command not found: python`

**الحل:**
```bash
python3 --version  # جرب python3 بدلاً من python
# أو ثبّت Python من python.org
```

### مشكلة: `No module named 'bayan'`

**الحل:**
```bash
# تأكد من التثبيت في وضع التطوير
cd nlp_bayan
pip install -e .
```

### مشكلة: `Permission denied`

**الحل:**
```bash
# استخدم --user
pip install --user -e .

# أو استخدم بيئة افتراضية (موصى به)
python -m venv venv
source venv/bin/activate
pip install -e .
```

---

## التحديث

```bash
cd nlp_bayan
git pull origin main
pip install -e . --upgrade
```

---

## إلغاء التثبيت

```bash
pip uninstall bayan
# واحذف المجلد إذا أردت
rm -rf nlp_bayan
```

---

## الخطوة التالية

✅ التثبيت تم بنجاح!

📘 الآن: [اكتب أول برنامج](first-program.md)

---

[← البداية](README.md) | [أول برنامج →](first-program.md)
