# -*- coding: utf-8 -*-
"""
اختبار المحلل النحوي المتقدم (Advanced Parser Verification)
===========================================================

يختبر قدرة النظام على تحليل الجمل المعقدة:
1. الجمل الشرطية
2. الجمل الظرفية (زمان/مكان)
3. الجمل الوصفية (الصفات)
4. الجمل مع حروف الجر
"""

import sys
import os

# إضافة المسار الحالي للمشروع
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bayan.bayan.istinbat_engine import IstinbatEngine
from bayan.bayan.linguistic_equation import Role

def test_advanced_parsing():
    print("\n" + "="*60)
    print("  🚀 اختبار المحلل النحوي المتقدم (Advanced Parser)")
    print("="*60 + "\n")
    
    engine = IstinbatEngine()
    
    test_cases = [
        {
            "type": "شرطية",
            "sentence": "إذا درس الطالب فإن الطالب ينجح",
            "expected_event": "شرط",
            "check": lambda res: res.equation.condition == "درس الطالب"
        },
        {
            "type": "حرف جر",
            "sentence": "محمد ذهب إلى المدرسة",
            "expected_event": "ذهب",
            "check": lambda res: res.equation.preposition == "إلى" and "المدرسة" in res.equation.entities
        },
        {
            "type": "ظرف زمان",
            "sentence": "أحمد أكل التفاحة صباحاً",
            "expected_event": "أكل",
            "check": lambda res: res.equation.time == "صباحاً"
        },
        {
            "type": "صفة",
            "sentence": "الرجل ضرب الكرة الكبيرة",
            "expected_event": "ضرب",
            "check": lambda res: res.equation.adjective == "الكبيرة"
        }
    ]
    
    passed = 0
    
    for i, case in enumerate(test_cases, 1):
        print(f"🔹 اختبار {i}: {case['type']}")
        print(f"   الجملة: '{case['sentence']}'")
        
        result = engine.process(case['sentence'])
        
        if result:
            print(f"   ✅ تم التحليل: الحدث = {result.equation.event}")
            
            # التحقق من التفاصيل
            if case['check'](result):
                print(f"   ✨ النتيجة مطابقة للتوقعات!")
                passed += 1
            else:
                print(f"   ⚠️ النتيجة غير مطابقة للتوقعات.")
                print(f"   تفاصيل المعادلة: {result.equation}")
        else:
            print(f"   ❌ فشل التحليل (لم يتم استخراج معادلة)")
            
        print("-" * 40)
        
    print(f"\n📊 النتيجة النهائية: {passed}/{len(test_cases)} اختبارات ناجحة.")

if __name__ == "__main__":
    test_advanced_parsing()
