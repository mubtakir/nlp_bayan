#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 اختبار سريع - نظام بصيرة الثوري
===================================

اختبار سريع للتأكد من عمل جميع مكونات النظام بشكل صحيح

الاستخدام:
    python3 quick_test.py

المطور: باسل يحيى عبدالله
"""

import sys
import time
import os
from datetime import datetime

# إضافة المسار الجذر للمشروع
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def print_status(message, status="info"):
    """طباعة حالة مع ألوان"""
    colors = {
        "success": "\033[92m✅",
        "error": "\033[91m❌", 
        "warning": "\033[93m⚠️",
        "info": "\033[94mℹ️"
    }
    reset = "\033[0m"
    print(f"{colors.get(status, colors['info'])} {message}{reset}")

def test_imports():
    """اختبار استيراد المكتبات"""
    print("🔍 اختبار استيراد المكتبات...")
    
    try:
        from knowledge.revolutionary_knowledge_system import RevolutionaryKnowledgeSystem
        print_status("تم استيراد النظام الشامل", "success")
    except Exception as e:
        print_status(f"فشل استيراد النظام الشامل: {e}", "error")
        return False
    
    try:
        from knowledge.knowledge_harvester import KnowledgeHarvester
        print_status("تم استيراد حاصد المعرفة", "success")
    except Exception as e:
        print_status(f"فشل استيراد حاصد المعرفة: {e}", "error")
        return False
    
    return True

def test_system_initialization():
    """اختبار تهيئة النظام"""
    print("\n🚀 اختبار تهيئة النظام...")
    
    try:
        from knowledge.revolutionary_knowledge_system import RevolutionaryKnowledgeSystem
        system = RevolutionaryKnowledgeSystem()
        print_status("تم تهيئة النظام الشامل", "success")
        return system
    except Exception as e:
        print_status(f"فشل في تهيئة النظام: {e}", "error")
        return None

def test_file_operations():
    """اختبار عمليات الملفات"""
    print("\n📁 اختبار عمليات الملفات...")
    
    import os
    
    # فحص الملفات الأساسية
    required_files = [
        "knowledge/revolutionary_knowledge_system.py",
        "knowledge/knowledge_harvester.py",
        "docs/دليل_المستخدم_الشامل.md"
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print_status(f"الملف موجود: {file}", "success")
        else:
            print_status(f"الملف مفقود: {file}", "error")
            missing_files.append(file)
    
    # فحص مجلد قواعد البيانات
    if os.path.exists("databases"):
        print_status("مجلد قواعد البيانات موجود", "success")
    else:
        print_status("مجلد قواعد البيانات مفقود", "warning")
    
    return len(missing_files) == 0

def generate_test_report(results):
    """إنتاج تقرير الاختبار"""
    print("\n" + "="*50)
    print("📋 تقرير الاختبار السريع")
    print("="*50)
    
    total_tests = len(results)
    passed_tests = sum(1 for result in results.values() if result)
    failed_tests = total_tests - passed_tests
    
    print(f"📊 إجمالي الاختبارات: {total_tests}")
    print(f"✅ نجح: {passed_tests}")
    print(f"❌ فشل: {failed_tests}")
    
    success_rate = (passed_tests / total_tests) * 100
    print(f"📈 معدل النجاح: {success_rate:.1f}%")
    
    print("\n📝 تفاصيل الاختبارات:")
    for test_name, result in results.items():
        status = "✅ نجح" if result else "❌ فشل"
        print(f"  {test_name}: {status}")
    
    # التقييم العام
    if success_rate >= 90:
        print_status("\n🎉 ممتاز! النظام يعمل بكفاءة عالية", "success")
    elif success_rate >= 70:
        print_status("\n👍 جيد! النظام يعمل مع بعض المشاكل البسيطة", "warning")
    else:
        print_status("\n⚠️ يحتاج إصلاح! هناك مشاكل في النظام", "error")
    
    # التوصيات
    print("\n💡 التوصيات:")
    if not results.get("استيراد المكتبات", True):
        print("  - تحقق من تثبيت جميع الملفات المطلوبة")
    if not results.get("عمليات قاعدة البيانات", True):
        print("  - تحقق من صحة قاعدة البيانات")
    if not results.get("عمليات الملفات", True):
        print("  - تأكد من وجود جميع الملفات المطلوبة")

def main():
    """الدالة الرئيسية"""
    print("🧪 اختبار سريع لنظام بصيرة الثوري")
    print(f"⏰ وقت البدء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50)
    
    results = {}
    
    # تشغيل الاختبارات
    results["استيراد المكتبات"] = test_imports()
    
    if results["استيراد المكتبات"]:
        system = test_system_initialization()
        results["تهيئة النظام"] = system is not None
        
        if system:
            results["اتصال Ollama"] = test_ollama_connection(system)
            results["عمليات قاعدة البيانات"] = test_database_operations(system)
            
            # اختبار استخراج المعرفة فقط إذا كان Ollama يعمل
            if results["اتصال Ollama"]:
                results["استخراج المعرفة"] = test_knowledge_extraction(system)
            else:
                results["استخراج المعرفة"] = False
                print_status("تم تخطي اختبار استخراج المعرفة (Ollama غير متاح)", "warning")
        else:
            results["اتصال Ollama"] = False
            results["عمليات قاعدة البيانات"] = False
            results["استخراج المعرفة"] = False
    else:
        results["تهيئة النظام"] = False
        results["اتصال Ollama"] = False
        results["عمليات قاعدة البيانات"] = False
        results["استخراج المعرفة"] = False
    
    results["عمليات الملفات"] = test_file_operations()
    
    # إنتاج التقرير
    generate_test_report(results)
    
    print(f"\n⏰ وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🎉 انتهى الاختبار السريع!")

if __name__ == "__main__":
    main()
