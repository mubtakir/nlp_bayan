#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
سكريبت تجريبي سريع لنماذج الذكاء الاصطناعي في بيان
Quick Demo Script for Bayan AI Models
"""

import sys
import os

# إضافة مسار المشروع
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from bayan.ai.neuro_symbolic_loop import NeuroSymbolicLoop
from bayan.ai.llm_gateway import LLMGateway

def print_header(title):
    """طباعة عنوان منسق"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)

def check_mode_availability():
    """فحص الأوضاع المتاحة"""
    print_header("🔍 فحص الأوضاع المتاحة")
    
    modes = {
        "standalone": "المستقل (Standalone)",
        "local": "المحلي (Ollama)",
        "cloud": "السحابي (Gemini)"
    }
    
    available = []
    
    for mode_key, mode_name in modes.items():
        try:
            gateway = LLMGateway(mode=mode_key)
            info = gateway.get_info()
            is_available = info['available']
            
            status = "✅ متاح" if is_available else "❌ غير متاح"
            print(f"{mode_name}: {status}")
            
            if is_available:
                available.append(mode_key)
                print(f"  └─ Backend: {info['backend']}")
        except Exception as e:
            print(f"{mode_name}: ❌ خطأ - {str(e)}")
    
    return available

def demo_mode(mode, test_inputs):
    """تجربة وضع معين"""
    mode_names = {
        "standalone": "المستقل",
        "local": "المحلي (Ollama)",
        "cloud": "السحابي (Gemini)"
    }
    
    print_header(f"🚀 تجربة الوضع: {mode_names.get(mode, mode)}")
    
    try:
        loop = NeuroSymbolicLoop(mode=mode)
        
        # عرض معلومات الإعداد
        info = loop.get_info()
        print(f"\n📋 الإعداد:")
        print(f"  • الوضع: {info['gateway']['mode']}")
        print(f"  • Backend: {info['gateway']['backend']}")
        print(f"  • الحالة: {'✅ متاح' if info['gateway']['available'] else '❌ غير متاح'}")
        
        # معالجة النصوص
        print(f"\n📝 معالجة النصوص:")
        for i, text in enumerate(test_inputs, 1):
            print(f"\n  {i}. النص: \"{text}\"")
            
            try:
                result = loop.process(text, language="arabic")
                
                # عرض النتائج
                print(f"     ├─ الذرات المستخرجة:")
                atoms = result.get('dream', {}).get('atoms', [])
                if atoms:
                    for atom in atoms[:3]:  # أول 3 ذرات فقط
                        print(f"     │  • {atom.get('type', '?')}: {atom.get('value', '?')}")
                else:
                    print(f"     │  • لا توجد ذرات")
                
                print(f"     ├─ التحقق: {'✅ نجح' if result.get('reality_check', {}).get('verified') else '❌ فشل'}")
                print(f"     └─ النتيجة النهائية: \"{result.get('realization', 'لا توجد نتيجة')}\"")
                
            except Exception as e:
                print(f"     └─ ❌ خطأ: {str(e)}")
        
    except Exception as e:
        print(f"\n❌ فشل تشغيل الوضع: {str(e)}")
        import traceback
        traceback.print_exc()

def demo_llm_gateway():
    """تجربة LLM Gateway مباشرة"""
    print_header("🔧 تجربة LLM Gateway المباشرة")
    
    # جرب الوضع المستقل
    try:
        gateway = LLMGateway(mode="standalone")
        print("\n📝 توليد نص بسيط:")
        response = gateway.generate("أحمد يأكل تفاحة")
        print(f"النتيجة:\n{response}")
    except Exception as e:
        print(f"❌ خطأ: {str(e)}")

def main():
    """الدالة الرئيسية"""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║           🤖 تجربة نماذج الذكاء الاصطناعي في بيان             ║
║              Bayan AI Models Quick Demo                         ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
""")
    
    # نصوص تجريبية
    test_inputs = [
        "أحمد ضرب الكرة",
        "محمد يدرس البرمجة",
        "الطالب ينجح في الامتحان"
    ]
    
    # 1. فحص الأوضاع المتاحة
    available_modes = check_mode_availability()
    
    if not available_modes:
        print("\n❌ لا توجد أوضاع متاحة!")
        print("\nتأكد من:")
        print("  • تثبيت المكتبات المطلوبة")
        print("  • تشغيل Ollama (للوضع المحلي)")
        print("  • تعيين GEMINI_API_KEY (للوضع السحابي)")
        return
    
    # 2. تجربة الوضع المستقل (دائماً متاح)
    if "standalone" in available_modes:
        demo_mode("standalone", test_inputs)
    
    # 3. تجربة الوضع المحلي (إذا كان متاحاً)
    if "local" in available_modes:
        response = input("\n❓ هل تريد تجربة الوضع المحلي (Ollama)؟ (y/n): ")
        if response.lower() in ['y', 'yes', 'نعم', 'ن']:
            demo_mode("local", test_inputs)
    
    # 4. تجربة الوضع السحابي (إذا كان متاحاً)
    if "cloud" in available_modes:
        response = input("\n❓ هل تريد تجربة الوضع السحابي (Gemini)؟ (y/n): ")
        if response.lower() in ['y', 'yes', 'نعم', 'ن']:
            demo_mode("cloud", test_inputs)
    
    # 5. تجربة LLM Gateway
    response = input("\n❓ هل تريد تجربة LLM Gateway المباشرة؟ (y/n): ")
    if response.lower() in ['y', 'yes', 'نعم', 'ن']:
        demo_llm_gateway()
    
    # الخاتمة
    print_header("✅ انتهت التجربة")
    print("""
📚 للمزيد من المعلومات:
  • اقرأ: دليل_تشغيل_الذكاء_الاصطناعي.md
  • جرّب: examples/neuro_symbolic_demo.py
  • راجع: bayan/ai/llm_gateway.py

🎯 الأوضاع المتاحة:
""")
    for mode in available_modes:
        mode_names = {
            "standalone": "✅ المستقل (Standalone)",
            "local": "✅ المحلي (Ollama)",
            "cloud": "✅ السحابي (Gemini)"
        }
        print(f"  {mode_names.get(mode, mode)}")
    
    print("\n🚀 بالتوفيق في استخدام بيان!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  تم إيقاف البرنامج بواسطة المستخدم")
    except Exception as e:
        print(f"\n❌ خطأ غير متوقع: {str(e)}")
        import traceback
        traceback.print_exc()
