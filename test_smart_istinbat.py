#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبار محرك الاستنباط الذكي (Smart Istinbat Engine)
Test Smart Istinbat Engine with 3-Layer Inference
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bayan.bayan.istinbat_engine import IstinbatEngine
from bayan.bayan.smart_knowledge_base import SmartKnowledgeBase

def print_header(title):
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)

def test_smart_inference():
    print_header("🧠 اختبار محرك الاستنباط الذكي")
    
    engine = IstinbatEngine()
    
    # التأكد من أن قاعدة المعرفة هي SmartKnowledgeBase
    if isinstance(engine.kb, SmartKnowledgeBase):
        print("✅ تم تفعيل SmartKnowledgeBase بنجاح")
    else:
        print("❌ خطأ: قاعدة المعرفة ليست ذكية!")
        return

    test_cases = [
        # 1. القواعد اليدوية (Manual Rules)
        {
            "title": "🎯 المستوى 1: القواعد اليدوية (أكل)",
            "sentence": "محمد أكل تفاحة",
            "expected_source": "Manual"
        },
        # 2. معجم الراموز (Arramooz Dictionary)
        {
            "title": "🔍 المستوى 2: معجم الراموز (ركض - حركة)",
            "sentence": "اللاعب ركض في الملعب",
            "expected_source": "Arramooz"
        },
        {
            "title": "🔍 المستوى 2: معجم الراموز (فرح - شعور)",
            "sentence": "الطالب فرح بالنتيجة",
            "expected_source": "Arramooz"
        },
        # 3. سيميائية الحروف (Letter Semiotics)
        {
            "title": "🔮 المستوى 3: سيميائية الحروف (كرشف - كلمة مخترعة)",
            "sentence": "الرجل كرشف الصندوق",
            "expected_source": "Semiotics"
        }
    ]
    
    for case in test_cases:
        print(f"\n{'-'*50}")
        print(f"{case['title']}")
        print(f"📝 الجملة: \"{case['sentence']}\"")
        
        result = engine.process(case['sentence'])
        
        if result:
            print(f"   ✅ تم التحليل بنجاح")
            print(f"   الحدث: {result.equation.event}")
            
            if result.consequences:
                print("   النتائج المستنتجة:")
                for cons in result.consequences:
                    print(f"     • {cons.entity_name}: {cons.state_changes} ({cons.description})")
            else:
                print("   ⚠️ لا توجد نتائج (قد يكون الفعل غير معروف تماماً)")
        else:
            print("   ❌ فشل التحليل")

def main():
    try:
        test_smart_inference()
        print_header("✅ انتهت الاختبارات")
    except Exception as e:
        print(f"\n❌ حدث خطأ: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
