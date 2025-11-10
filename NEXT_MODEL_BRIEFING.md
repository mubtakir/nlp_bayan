# NEXT_MODEL_BRIEFING — موجز تنفيذي للموديل التالي (One‑Page)

تاريخ: 2025‑11‑10
المستودع: https://github.com/mubtakir/bayaan-lang
الفرع: main

## 1) Snapshot — الحالة الآن
- الاختبارات: 379/379 ناجحة ✅
- IDE (الويب) — جديد في آخر دفعة:
  - [x] عرض متعدد للمخرجات (SVG + كل data:image/*) مع ترتيب الظهور
  - [x] شريط أدوات للمعاينة: السابق/التالي + نسخ + تنزيل (SVG/PNG/JPEG)
  - [x] إعادة ضبط المعاينة وإخفاء الشريط عند البدء/الخطأ
- gfx (الرسوم):
  - svg.bayan — أشكال أساسية/متقدمة + رسم حر + حركات بسيطة
  - waves.bayan — موجات + مغلفات ADSR + AM/FM + رسم إلى SVG
  - img.bayan — لوح نقطي عبر Pillow مع تصدير Data URI (PNG/JPEG)

## 2) كيف تبدأ بسرعة (Run/Verify)
- تشغيل IDE محلياً: `python web_ide/app.py` ثم افتح http://127.0.0.1:5001/ide
- جرّب أمثلة gfx من قائمة Examples (🟥) ثم Run — استخدم الشريط للتنقل/النسخ/التنزيل
- اختبارات: `pytest -q` (ينبغي أن تبقى 379/379 خضراء)

## 3) ما الذي تغيّر في هذه الدفعة؟
- web_ide/templates/ide.html:
  - استخراج كل المخرجات المطابقة (SVG + data:image/*) بترتيب الظهور
  - واجهة تنقّل (Prev/Next) وحفظ (Download) ونسخ (Copy)
  - تنزيل SVG عبر Blob مباشرة، وdata URI عبر فك base64 → Blob → حفظ بالامتداد الصحيح
- التوثيق المحدّث: README.md, README_AR.md, docs/developer_guide.md (ملخص مزايا IDE الجديدة)

## 4) أولويات العمل التالية (Next Steps)
- أولوية عالية — أمثلة gfx:
  - [ ] SVG Animations متقدّمة: تحريك مسار/لون/حجم (EN/AR)
  - [ ] مخططات بسيطة: شبكة محاور + Gradients + Themes (EN/AR)
  - [ ] Waves: أمثلة envelopes + noise + AM/FM بمعاملات متنوعة (EN/AR)
  - [ ] Raster: أمثلة طبقات (خلفية + أشكال + نص) + تصدير PNG/JPEG (EN/AR)
- اختياري/تعليمي:
  - [ ] waves: DFT تعليمي O(N^2) + moving-average filter
  - [ ] svg: polyline/polygon + stroke-dasharray/markers
  - [ ] raster: خيارات خط/سماكات/أنماط/مضلعات

## 5) قوائم فحص قابلة للتأشير (Checklists)
- IDE Preview (تم التنفيذ):
  - [x] جمع متعدد SVG + data:image/*
  - [x] ترتيب حسب الظهور + أول مخرج افتراضي
  - [x] Prev/Next + Copy + Download

- Examples (للإنجاز):
  - [ ] examples/svg_animation_advanced.md
  - [ ] examples/svg_chart_grid.md
  - [ ] examples/wave_envelope_examples.md
  - [ ] examples/raster_layers.md
  - [ ] النسخ العربية المقابلة تحت examples/ar_*.md

- Documentation (بعد إضافة الأمثلة):
  - [ ] README/README_AR — تحديث قسم gfx وروابط الأمثلة
  - [ ] docs/developer_guide.md — إضافة ملخص موجز مع لقطات (إن لزم)

- Verification & Push:
  - [ ] pytest -q — جميع الاختبارات ناجحة
  - [ ] git add -A && git commit -m "docs/examples: add ...; tests: 379/379"
  - [ ] git push origin main

## 6) دلائل سريعة (File Pointers)
- IDE: web_ide/templates/ide.html, web_ide/app.py
- gfx: gfx/svg.bayan, gfx/waves.bayan, gfx/img.bayan, gfx_img_py.py
- أمثلة: examples/* (EN/AR)
- وثائق: README.md, README_AR.md, docs/developer_guide.md, ai/AI_LIBRARY_GUIDE.md, AI_HANDOFF_REPORT.md

## 7) ملاحظات واعتماديات
- Pillow < 12.0 (تم التحقق مع 11.3.0) — مطلوبة لميزات الرستر
- التزام قواعد نحو البيان في الأمثلة (no `;`, no list comprehensions, `pow()` بدل **، ...)
- لا تغيّر التبعيات إلا عبر مدير الحزم وبإذن صريح

## 8) أوامر جاهزة (Quick Commands)
- اختبارات: `pytest -q`
- تشغيل IDE: `python web_ide/app.py`
- إصدار/دفع:
  - `git add -A && git commit -m "gfx/examples: ...; docs: ...; tests: 379/379"`
  - `git push origin main`

— انتهى —

