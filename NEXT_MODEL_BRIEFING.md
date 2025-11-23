# NEXT_MODEL_BRIEFING — موجز تنفيذي للموديل التالي (One‑Page)

**تاريخ**: 2025‑11‑17
**المستودع**: https://github.com/mubtakir/nlp_bayan
**الفرع**: main
**الحالة**: نظام متقدم - أولوية: إصلاح الاختبارات

---

## 1) Snapshot — الحالة الآن

### الاختبارات:
- ✅ **461/605 ناجحة** (76.2%)
- ❌ **144 فاشلة** (23.8%)
- 🎯 **الهدف**: 95%+ (أقل من 30 فاشل)

### الإنجازات الكبرى:
- ✅ **42 ملف تعليمي** (21 عربي + 21 إنجليزي) - **جديد!**
- ✅ **9,318+ سطر توثيق** تعليمي
- ✅ **نظام Conceptual LM** كامل (4 طبقات، 6 دوائر، 5 برامج)
- ✅ **نظام NLP حواري** متقدم (استدلال، سياق، زمن، سياسات)
- ✅ **محرك الشبكات السببية**
- ✅ **نظام الكيانات الديناميكي**
- ✅ **الشبكات الدلالية**
- ✅ **نظام المترادفات والتشابه**
- ✅ **الاستدلال الاحتمالي**

### IDE (الويب):
- ✅ عرض متعدد للمخرجات (SVG + data:image/*)
- ✅ شريط أدوات: السابق/التالي + نسخ + تنزيل
- ✅ معاينة SVG مباشرة

### gfx (الرسوم):
- ✅ svg.bayan — أشكال + رسم حر + حركات
- ✅ waves.bayan — موجات + ADSR + AM/FM
- ✅ img.bayan — لوح نقطي + تصدير PNG/JPEG

---

## 2) كيف تبدأ بسرعة (Run/Verify)

### التحقق من الاختبارات (أولوية قصوى):
```bash
# شغّل جميع الاختبارات
python -m pytest tests/ -v

# شغّل اختبار محدد
python -m pytest tests/test_nlp_bayan_generation.py::test_morpho_inserts_min_for_ghadara -v -s
```

### التحقق من نظام NLP الحواري:
```bash
python3 bayan/main.py nlp_bayan/final_real_dialogue.bayan
```

### التحقق من Conceptual LM:
```bash
python bayan/main.py examples/conceptual_detail_focus_demo.bayan
python bayan/main.py examples/conceptual_lm_training_demo.bayan
```

### تشغيل Web IDE:
```bash
python web_ide/app.py
# ثم افتح http://127.0.0.1:5001/ide
```

---

## 3) ما الذي تغيّر في آخر دفعة؟

### التوثيق التعليمي (إنجاز ضخم! 🎉):
- ✅ **10 ملفات إنجليزية جديدة** (Parts 4.1-4.10)
- ✅ **تكافؤ كامل**: 21 عربي + 21 إنجليزي
- ✅ **ملف فهرس شامل**: docs/تعليمية/README.md
- ✅ **تحديث README_AR.md** بجميع المراجع

### الملفات المحدّثة:
- README_AR.md - تحديث شامل (575 سطر)
- docs/LLM_SYSTEM_PROMPT.txt - إضافة الميزات المتقدمة
- START_HERE_AI.md - تحديث كامل
- NEXT_MODEL_BRIEFING.md - هذا الملف

---

## 4) أولويات العمل التالية (Next Steps)

### 🔴 أولوية قصوى (الأسبوع 1):
- [ ] **إصلاح 144 اختبار فاشل** - الهدف: 95%+
  - [ ] test_nlp_bayan_generation.py (8 اختبارات)
  - [ ] test_operators.py (1 اختبار)
  - [ ] test_prob_thresholds_topk.py (1 اختبار)
  - [ ] test_similarity_core.py (4 اختبارات)
  - [ ] test_template_match.py (3 اختبارات)
  - [ ] test_temporal_constructs.py (2 اختبار)

### ⚠️ أولوية عالية (الأسبوع 2):
- [ ] تحسين توليد النص الطبيعي (من رمزي إلى طبيعي)
- [ ] توسيع أمثلة Conceptual LM
- [ ] إضافة اختبارات لـ nlp_bayan

### 📝 أولوية متوسطة (الأسبوع 3-4):
- [ ] أمثلة gfx متقدمة (SVG Animations، مخططات)
- [ ] توسيع الدوائر المفاهيمية (من 6 إلى 11)
- [ ] توسيع المجالات (من 5 إلى 10)

---

## 5) قوائم فحص قابلة للتأشير (Checklists)

### التوثيق التعليمي (مكتمل! ✅):
- [x] 10 ملفات إنجليزية جديدة (Parts 4.1-4.10)
- [x] ملف فهرس شامل (docs/تعليمية/README.md)
- [x] تحديث README_AR.md
- [x] تحديث LLM_SYSTEM_PROMPT.txt
- [x] تحديث START_HERE_AI.md
- [x] تحديث NEXT_MODEL_BRIEFING.md

### إصلاح الاختبارات (للإنجاز - أولوية قصوى):
- [ ] test_nlp_bayan_generation.py (8 اختبارات)
- [ ] test_operators.py (1 اختبار)
- [ ] test_prob_thresholds_topk.py (1 اختبار)
- [ ] test_similarity_core.py (4 اختبارات)
- [ ] test_template_match.py (3 اختبارات)
- [ ] test_temporal_constructs.py (2 اختبار)
- [ ] الهدف: 95%+ معدل نجاح

### IDE Preview (مكتمل! ✅):
- [x] جمع متعدد SVG + data:image/*
- [x] ترتيب حسب الظهور + أول مخرج افتراضي
- [x] Prev/Next + Copy + Download

### Verification & Push:
- [ ] pytest -v — 95%+ اختبارات ناجحة
- [ ] جميع الأمثلة تعمل
- [ ] git add -A && git commit -m "fix: tests passing 95%+; docs: updated"
- [ ] git push origin main

---

## 6) دلائل سريعة (File Pointers)

### للنماذج الذكية (ابدأ هنا):
- **NEXT_AI_MODEL_README.md** ⭐⭐⭐
- **docs/NEXT_AI_MODEL_INSTRUCTIONS.md** ⭐⭐⭐
- **docs/TEST_FIXING_GUIDE.md** ⭐⭐⭐
- **HANDOVER_TO_NEXT_AI_MODEL.md**
- **TEST_FIXES_REPORT.md**

### التوثيق التعليمي:
- **docs/تعليمية/README.md** - فهرس شامل
- **docs/تعليمية/ar/** - 21 ملف عربي
- **docs/تعليمية/en/** - 21 ملف إنجليزي
- **README_AR.md** - الملف الرئيسي

### نظام Conceptual LM:
- ai/conceptual_circuits.bayan
- ai/conceptual_programs.bayan
- ai/conceptual_orchestrator.bayan
- ai/conceptual_surface_realizer.bayan
- docs/CONCEPTUAL_CIRCUITS_AND_PROGRAMS.md

### نظام NLP الحواري:
- nlp_bayan/simple_kb.bayan
- nlp_bayan/simple_inference.bayan
- nlp_bayan/simple_parser.bayan
- nlp_bayan/final_real_dialogue.bayan
- nlp_bayan/COMPLETE_SYSTEM_GUIDE.md

### IDE والرسوم:
- web_ide/templates/ide.html, web_ide/app.py
- gfx/svg.bayan, gfx/waves.bayan, gfx/img.bayan

### الاختبارات:
- tests/ - 461 ناجح + 144 فاشل
- docs/TEST_FIXING_GUIDE.md

---

## 7) ملاحظات واعتماديات
- **Python**: 3.8+
- **Pillow**: < 12.0 (مطلوبة لميزات الرستر)
- **pytest**: للاختبارات
- **التزام قواعد نحو البيان**: no `;`, no list comprehensions, `pow()` بدل `**`
- **لا تغيّر التبعيات** إلا عبر مدير الحزم وبإذن صريح

---

## 8) أوامر جاهزة (Quick Commands)

### الاختبارات:
```bash
# جميع الاختبارات
python -m pytest tests/ -v

# اختبار محدد
python -m pytest tests/test_nlp_bayan_generation.py -v -s

# تقرير مختصر
pytest -q
```

### التشغيل:
```bash
# Web IDE
python web_ide/app.py

# نظام NLP
python3 bayan/main.py nlp_bayan/final_real_dialogue.bayan

# Conceptual LM
python bayan/main.py examples/conceptual_detail_focus_demo.bayan
```

### Git:
```bash
git add -A
git commit -m "fix: tests 95%+; docs: updated"
git push origin main
```

---

**— انتهى —**

**الحالة**: جاهز للعمل
**الأولوية**: إصلاح الاختبارات (144 فاشل → أقل من 30)
**الهدف**: 95%+ معدل نجاح

