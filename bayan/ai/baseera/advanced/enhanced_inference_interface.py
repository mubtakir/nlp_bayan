#!/usr/bin/env python3
"""
واجهة النظام الثوري المحسن لاستنباط المعادلات من الصور
🧬 المطور: باسل يحيى عبدالله
🌟 الاستراتيجية المحسنة: الطرق المعتادة أولاً، ثم المكتبة المرجعية
🎯 واجهة سهلة الاستخدام للنظام المحسن
"""

import os
import sys
import time
try:
    from .enhanced_revolutionary_inference_system import EnhancedRevolutionaryInferenceSystem
except ImportError:
    from enhanced_revolutionary_inference_system import EnhancedRevolutionaryInferenceSystem

def print_header():
    """
    طباعة رأس البرنامج
    """
    print("🧬" + "=" * 78 + "🧬")
    print("🌟                    النظام الثوري المحسن لاستنباط المعادلات                    🌟")
    print("🧬                          Enhanced Revolutionary Inference                          🧬")
    print("🌟                              المطور: باسل يحيى عبدالله                              🌟")
    print("🧬" + "=" * 78 + "🧬")
    print()
    print("🎯 الاستراتيجية المحسنة:")
    print("   1️⃣ تطبيق الطرق المعتادة أولاً (النظام الثوري الأساسي)")
    print("   2️⃣ إذا لم تحقق دقة مقبولة، تطبيق الحل الأخير (المكتبة المرجعية)")
    print("   3️⃣ البحث المنهجي في آلاف المعادلات الأساسية")
    print("   4️⃣ تحت إشراف الخبير/المستكشف في كل مرحلة")
    print()

def print_menu():
    """
    طباعة القائمة الرئيسية
    """
    print("📋 القائمة الرئيسية:")
    print("   1️⃣ استنباط معادلة من صورة واحدة")
    print("   2️⃣ اختبار النظام على صور متعددة")
    print("   3️⃣ عرض إحصائيات النظام والمكتبة")
    print("   4️⃣ تشغيل الاختبار الشامل")
    print("   5️⃣ مقارنة الأداء مع النظام الأساسي")
    print("   6️⃣ إعدادات النظام المتقدمة")
    print("   0️⃣ خروج")
    print()

def infer_single_image(inference_system):
    """
    استنباط معادلة من صورة واحدة
    """
    print("🖼️ استنباط معادلة من صورة واحدة")
    print("-" * 50)
    
    # طلب مسار الصورة
    image_path = input("📁 أدخل مسار الصورة: ").strip()
    
    if not os.path.exists(image_path):
        print("❌ الملف غير موجود!")
        return
    
    # طلب عدد التكرارات
    try:
        max_iterations = int(input("🔄 عدد التكرارات القصوى (افتراضي: 10): ") or "10")
    except ValueError:
        max_iterations = 10
    
    print(f"\n🚀 بدء الاستنباط المحسن...")
    print(f"📁 الصورة: {os.path.basename(image_path)}")
    print(f"🔄 التكرارات القصوى: {max_iterations}")
    print()
    
    try:
        # تشغيل النظام المحسن
        start_time = time.time()
        result = inference_system.infer_equation_from_image_enhanced(image_path, max_iterations)
        total_time = time.time() - start_time
        
        # عرض النتائج
        print("\n🏆 النتائج النهائية:")
        print("=" * 60)
        print(f"✅ نجح: {'نعم' if result['success'] else 'لا'}")
        print(f"🎯 الدقة الإجمالية: {result['overall_accuracy']:.3f}")
        print(f"🔧 الطريقة المستخدمة: {result['method_used']}")
        print(f"📐 عدد المعادلات المكتشفة: {len(result.get('equations', []))}")
        print(f"⏱️ وقت المعالجة الإجمالي: {total_time:.2f} ثانية")
        
        # تفاصيل مقارنة الطرق
        if 'basic_method_accuracy' in result:
            print(f"\n📊 مقارنة الطرق:")
            print(f"   🔧 الطريقة الأساسية: {result['basic_method_accuracy']:.3f}")
            print(f"   📚 طريقة المكتبة: {result['library_method_accuracy']:.3f}")
            print(f"   📈 تحسن محقق: {'نعم' if result.get('improvement_achieved', False) else 'لا'}")
            
            if result.get('improvement_factor', 0) not in [0, float('inf')]:
                print(f"   🚀 عامل التحسن: {result.get('improvement_factor', 1):.2f}x")
        
        # تفاصيل البحث في المكتبة
        if 'library_equations_tested' in result:
            print(f"\n📚 تفاصيل البحث في المكتبة:")
            print(f"   🔍 معادلات مختبرة: {result['library_equations_tested']}")
            print(f"   ⏱️ وقت البحث: {result.get('library_search_time', 0):.2f} ثانية")
        
        # عرض المعادلات المكتشفة
        equations = result.get('equations', [])
        if equations:
            print(f"\n📐 المعادلات المكتشفة:")
            for i, eq in enumerate(equations[:3]):  # عرض أول 3 معادلات
                if isinstance(eq, dict):
                    print(f"   {i+1}. نوع: {eq.get('shape_type', 'غير محدد')}")
                    print(f"      دقة: {eq.get('accuracy', 0):.3f}")
                    if 'equation' in eq and eq['equation']:
                        eq_id = eq['equation'].get('id', 'غير محدد')
                        print(f"      معرف: {eq_id}")
        
        # توصيات
        print(f"\n💡 التوصيات:")
        if result['overall_accuracy'] >= 0.8:
            print("   🌟 نتيجة ممتازة! المعادلة دقيقة جداً")
        elif result['overall_accuracy'] >= 0.6:
            print("   👍 نتيجة جيدة، يمكن الاعتماد عليها")
        elif result['overall_accuracy'] >= 0.4:
            print("   ⚠️ نتيجة متوسطة، قد تحتاج تحسين الصورة")
        else:
            print("   ❌ نتيجة ضعيفة، جرب صورة أوضح أو أبسط")
        
    except Exception as e:
        print(f"❌ خطأ في الاستنباط: {str(e)}")

def test_multiple_images(inference_system):
    """
    اختبار النظام على صور متعددة
    """
    print("🖼️ اختبار النظام على صور متعددة")
    print("-" * 50)
    
    # طلب مجلد الصور
    folder_path = input("📁 أدخل مسار مجلد الصور: ").strip()
    
    if not os.path.exists(folder_path):
        print("❌ المجلد غير موجود!")
        return
    
    # البحث عن ملفات الصور
    image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']
    image_files = []
    
    for file in os.listdir(folder_path):
        if any(file.lower().endswith(ext) for ext in image_extensions):
            image_files.append(os.path.join(folder_path, file))
    
    if not image_files:
        print("❌ لم يتم العثور على صور في المجلد!")
        return
    
    print(f"📊 تم العثور على {len(image_files)} صورة")
    
    # تشغيل الاختبار
    try:
        results = inference_system.test_system_performance(image_files)
        
        print(f"\n🏆 تقرير الأداء:")
        print("=" * 60)
        print(f"📊 معدل النجاح: {results['test_summary']['success_rate']:.1f}%")
        print(f"🎯 متوسط الدقة: {results['test_summary']['average_accuracy']:.3f}")
        print(f"⏱️ متوسط وقت المعالجة: {results['test_summary']['average_processing_time']:.2f} ثانية")
        print(f"🏅 تقييم الأداء: {results['performance_grade']}")
        
        # توزيع الطرق
        print(f"\n📋 توزيع الطرق المستخدمة:")
        for method, count in results['method_distribution'].items():
            percentage = (count / results['test_summary']['total_tests']) * 100
            print(f"   🔧 {method}: {count} ({percentage:.1f}%)")
        
    except Exception as e:
        print(f"❌ خطأ في الاختبار: {str(e)}")

def show_system_stats(inference_system):
    """
    عرض إحصائيات النظام والمكتبة
    """
    print("📊 إحصائيات النظام والمكتبة")
    print("-" * 50)
    
    try:
        stats = inference_system.get_system_stats()
        
        print(f"🧬 نوع النظام: {stats['system_type']}")
        print(f"👨‍💻 المطور: {stats['creator']}")
        print(f"🔬 المنهجية: {stats['methodology']}")
        
        print(f"\n📚 إحصائيات المكتبة:")
        library_stats = stats['library_stats']
        print(f"   📐 إجمالي المعادلات: {library_stats['total_equations']}")
        print(f"   📂 عدد الفئات: {len(library_stats['categories'])}")
        
        print(f"\n📂 توزيع الفئات:")
        for category, count in library_stats['categories'].items():
            percentage = (count / library_stats['total_equations']) * 100
            print(f"   🔧 {category}: {count} ({percentage:.1f}%)")
        
        print(f"\n🎯 توزيع التعقيد:")
        complexity_dist = library_stats['complexity_distribution']
        for complexity, count in complexity_dist.items():
            if count > 0:
                percentage = (count / library_stats['total_equations']) * 100
                print(f"   📊 {complexity}: {count} ({percentage:.1f}%)")
        
        print(f"\n⚙️ إعدادات النظام:")
        config = stats['configuration']
        print(f"   🎯 حد الطريقة الأساسية: {config['basic_method_threshold']}")
        print(f"   📚 حد البحث في المكتبة: {config['library_search_threshold']}")
        print(f"   ⏰ حد وقت البحث: {config['max_library_search_time']} ثانية")
        
        print(f"\n🚀 قدرات النظام:")
        capabilities = stats['capabilities']
        for capability, enabled in capabilities.items():
            status = "✅" if enabled else "❌"
            print(f"   {status} {capability}")
        
    except Exception as e:
        print(f"❌ خطأ في عرض الإحصائيات: {str(e)}")

def run_comprehensive_test():
    """
    تشغيل الاختبار الشامل
    """
    print("🧪 تشغيل الاختبار الشامل")
    print("-" * 50)
    
    try:
        from test_enhanced_revolutionary_system import run_enhanced_comprehensive_test
        
        print("🚀 بدء الاختبار الشامل...")
        print("⏳ هذا قد يستغرق عدة دقائق...")
        print()
        
        results = run_enhanced_comprehensive_test()
        
        if results:
            print("\n✅ انتهى الاختبار الشامل بنجاح!")
        else:
            print("\n❌ فشل الاختبار الشامل!")
            
    except ImportError:
        print("❌ ملف الاختبار الشامل غير موجود!")
    except Exception as e:
        print(f"❌ خطأ في الاختبار الشامل: {str(e)}")

def compare_with_basic_system():
    """
    مقارنة الأداء مع النظام الأساسي
    """
    print("⚖️ مقارنة الأداء مع النظام الأساسي")
    print("-" * 50)
    print("🔄 هذه الميزة قيد التطوير...")
    print("💡 ستتيح مقارنة مفصلة بين النظام المحسن والأساسي")

def advanced_settings():
    """
    إعدادات النظام المتقدمة
    """
    print("⚙️ إعدادات النظام المتقدمة")
    print("-" * 50)
    print("🔄 هذه الميزة قيد التطوير...")
    print("💡 ستتيح تخصيص معاملات النظام والمكتبة")

def main():
    """
    الدالة الرئيسية للواجهة
    """
    print_header()
    
    try:
        # إنشاء النظام المحسن
        print("🔧 تحميل النظام الثوري المحسن...")
        inference_system = EnhancedRevolutionaryInferenceSystem()
        print("✅ تم تحميل النظام بنجاح!")
        print()
        
        while True:
            print_menu()
            choice = input("🎯 اختر من القائمة (0-6): ").strip()
            print()
            
            if choice == '1':
                infer_single_image(inference_system)
            elif choice == '2':
                test_multiple_images(inference_system)
            elif choice == '3':
                show_system_stats(inference_system)
            elif choice == '4':
                run_comprehensive_test()
            elif choice == '5':
                compare_with_basic_system()
            elif choice == '6':
                advanced_settings()
            elif choice == '0':
                print("👋 شكراً لاستخدام النظام الثوري المحسن!")
                print("🧬 المطور: باسل يحيى عبدالله")
                break
            else:
                print("❌ اختيار غير صحيح! حاول مرة أخرى.")
            
            print("\n" + "="*60 + "\n")
    
    except KeyboardInterrupt:
        print("\n\n⚠️ تم إيقاف البرنامج بواسطة المستخدم")
    except Exception as e:
        print(f"❌ خطأ في النظام: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
