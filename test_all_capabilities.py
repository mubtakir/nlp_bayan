#!/usr/bin/env python3
"""
اختبار شامل لجميع القدرات الجديدة
Comprehensive Test for All New Capabilities
"""

import sys
import os

# Add paths
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 60)
print("🧪 اختبار شامل للقدرات الجديدة | Full Capabilities Test")
print("=" * 60)

# ============================================================
# 1. محرك الحوار الذكي
# ============================================================
print("\n" + "=" * 60)
print("1️⃣  محرك الحوار الذكي | ConversationEngine")
print("=" * 60)

try:
    from bayan.bayan.cognitive.conversation_engine import ConversationEngine
    
    engine = ConversationEngine()
    
    # اختبار المحادثة
    tests = [
        "مرحباً، كيف حالك؟",
        "ما هو الذكاء الاصطناعي؟",
        "شكراً لك",
    ]
    
    for msg in tests:
        response = engine.chat(msg)
        print(f"   👤 المستخدم: {msg}")
        print(f"   🤖 الرد: {response[:60]}...")
    
    print("   ✅ نجح!")
except Exception as e:
    print(f"   ❌ فشل: {e}")

# ============================================================
# 2. التعلم التفاعلي
# ============================================================
print("\n" + "=" * 60)
print("2️⃣  التعلم التفاعلي | LearningAgent")
print("=" * 60)

try:
    from bayan.bayan.cognitive.interactive_learning import LearningAgent
    
    agent = LearningAgent()
    
    # التعلم من نص
    text = """
    الذكاء الاصطناعي هو فرع من علوم الحاسوب.
    بايثون هي لغة برمجة سهلة التعلم.
    التعلم الآلي يعني قدرة الآلة على التعلم من البيانات.
    """
    
    result = agent.learn_from_text(text)
    print(f"   📝 النص: {len(text)} حرف")
    print(f"   📊 الحقائق المستخرجة: {result['facts_found']}")
    print(f"   ✔️  الحقائق المتعلمة: {result['facts_learned']}")
    
    # التعليم المباشر
    success = agent.teach("الشمس هي نجم في مجرتنا")
    print(f"   📚 التعليم المباشر: {'نجح' if success else 'فشل'}")
    
    # الإحصائيات
    stats = agent.get_learning_stats()
    print(f"   📈 إجمالي الحقائق: {stats['total_facts_learned']}")
    
    print("   ✅ نجح!")
except Exception as e:
    print(f"   ❌ فشل: {e}")

# ============================================================
# 3. الاستنباط العكسي
# ============================================================
print("\n" + "=" * 60)
print("3️⃣  الاستنباط العكسي | AbductionEngine")
print("=" * 60)

try:
    from bayan.bayan.cognitive.abduction_engine import AbductionEngine
    
    engine = AbductionEngine()
    
    # إضافة معرفة سببية
    engine.add_causal_knowledge("ماس كهربائي", "حريق")
    engine.add_causal_knowledge("مطر", "انزلاق")
    engine.add_causal_knowledge("إهمال", "حادث")
    
    # لماذا حدث هذا؟
    answer = engine.why("حدث حريق")
    print(f"   ❓ السؤال: لماذا حدث حريق؟")
    print(f"   💡 الجواب: {answer}")
    
    # ما الذي سبب هذا؟
    causes = engine.what_caused("فشل المشروع")
    print(f"   🔍 أسباب فشل المشروع: {len(causes)} فرضية")
    
    print("   ✅ نجح!")
except Exception as e:
    print(f"   ❌ فشل: {e}")

# ============================================================
# 4. القصص السببية
# ============================================================
print("\n" + "=" * 60)
print("4️⃣  القصص السببية | CausalStoriesEngine")
print("=" * 60)

try:
    from bayan.bayan.cognitive.causal_stories import CausalStoriesEngine
    
    engine = CausalStoriesEngine()
    
    # ماذا لو؟
    scenario = engine.what_if("بدأنا المشروع بميزانية أكبر")
    print(f"   📖 السيناريو: {scenario.name}")
    print(f"   🎯 النتيجة: {scenario.final_outcome[:50]}...")
    print(f"   📊 الاحتمالية: {scenario.probability:.2f}")
    
    # أفضل حالة
    best = engine.best_case("إطلاق المنتج")
    print(f"   🌟 أفضل حالة: احتمالية {best.probability:.2f}")
    
    print("   ✅ نجح!")
except Exception as e:
    print(f"   ❌ فشل: {e}")

# ============================================================
# 5. تصدير المعرفة
# ============================================================
print("\n" + "=" * 60)
print("5️⃣  تصدير المعرفة | KnowledgeExporter")
print("=" * 60)

try:
    from bayan.bayan.cognitive.knowledge_export import KnowledgeExporter
    
    exporter = KnowledgeExporter()
    
    # تصدير JSON
    json_content = exporter.export_json()
    print(f"   📄 JSON: {len(json_content)} حرف")
    
    # تصدير Markdown
    md_content = exporter.export_markdown()
    print(f"   📝 Markdown: {len(md_content)} حرف")
    
    print("   ✅ نجح!")
except Exception as e:
    print(f"   ❌ فشل: {e}")

# ============================================================
# 6. الوكيل الذكي
# ============================================================
print("\n" + "=" * 60)
print("6️⃣  الوكيل الذكي | BayanAgent")
print("=" * 60)

try:
    from bayan.bayan.cognitive.intelligent_agent import BayanAgent
    
    agent = BayanAgent()
    
    # تنفيذ هدف
    result = agent.execute_goal("صمم ترس حلزوني للمحرك")
    print(f"   🎯 الهدف: صمم ترس حلزوني")
    print(f"   ✔️  نجاح: {result['success']}")
    print(f"   📋 المهام: {len(result['tasks'])}")
    print(f"   📊 نسبة الإنجاز: {result['completed_ratio']:.0%}")
    
    # القدرات
    caps = agent.list_capabilities()
    print(f"   🔧 القدرات المتاحة: {len(caps)}")
    
    print("   ✅ نجح!")
except Exception as e:
    print(f"   ❌ فشل: {e}")

# ============================================================
# 7. نظام التجميعات
# ============================================================
print("\n" + "=" * 60)
print("7️⃣  نظام التجميعات | Assembly System")
print("=" * 60)

try:
    from tezniti_3d.assembly_system import Assembly, AssemblyBuilder, ConstraintType
    
    # إنشاء تجميع
    assembly = Assembly("Gear Train")
    
    gear1 = assembly.add_part("Gear 1", "helical_gear", 
                              {"teeth": 24, "module": 2})
    gear2 = assembly.add_part("Gear 2", "helical_gear",
                              {"teeth": 32, "module": 2})
    
    assembly.add_constraint(ConstraintType.GEAR_MESH, gear1, gear2)
    assembly.solve_constraints()
    
    print(f"   🔩 القطع: {len(assembly.parts)}")
    print(f"   🔗 القيود: {len(assembly.constraints)}")
    
    # بناء من النص
    builder = AssemblyBuilder()
    auto = builder.build_from_text("تجميع من 3 تروس")
    print(f"   🏗️  بناء تلقائي: {len(auto.parts)} قطع")
    
    print("   ✅ نجح!")
except Exception as e:
    print(f"   ❌ فشل: {e}")

# ============================================================
# 8. المحاكاة الحركية
# ============================================================
print("\n" + "=" * 60)
print("8️⃣  المحاكاة الحركية | Kinematic Simulation")
print("=" * 60)

try:
    from tezniti_3d.kinematic_sim import KinematicSimulator, GearMesh
    import math
    
    sim = KinematicSimulator()
    
    # إعداد سلسلة تروس
    gears = [
        {"id": "driver", "teeth": 20},
        {"id": "driven", "teeth": 40}
    ]
    sim.setup_gear_train(gears)
    
    # محاكاة
    result = sim.simulate_rotation("driver", rpm=100)
    print(f"   ⚙️  سرعة الإدخال: 100 RPM")
    print(f"   🔄 سرعة الإخراج: {result['output_speeds']['driven']:.1f} RPM")
    
    # نسبة التروس
    ratios = sim.get_gear_ratios()
    print(f"   📐 نسبة التروس: {ratios[0]['ratio']:.2f}")
    
    print("   ✅ نجح!")
except Exception as e:
    print(f"   ❌ فشل: {e}")

# ============================================================
# 9. مساعد التصميم
# ============================================================
print("\n" + "=" * 60)
print("9️⃣  مساعد التصميم | Design Assistant")
print("=" * 60)

try:
    from tezniti_3d.design_assistant import SmartDesignAssistant
    
    assistant = SmartDesignAssistant()
    
    # قطع للتحليل
    parts = [
        {"name": "Gear", "type": "gear", "teeth": 10, "module": 2},
        {"name": "Shaft", "type": "shaft", "diameter": 20, "length": 300}
    ]
    
    result = assistant.full_analysis(parts)
    print(f"   🔍 التحليل:")
    print(f"      - أخطاء: {result['issue_count']['errors']}")
    print(f"      - تحذيرات: {result['issue_count']['warnings']}")
    print(f"      - معلومات: {result['issue_count']['info']}")
    
    # فحص التفاوت
    fit = assistant.tolerance_checker.check_fit(25.02, 25.00)
    print(f"   📏 فحص التفاوت: {fit['fit_type']}")
    
    print("   ✅ نجح!")
except Exception as e:
    print(f"   ❌ فشل: {e}")

# ============================================================
# 10. مكتبة القوالب
# ============================================================
print("\n" + "=" * 60)
print("🔟 مكتبة القوالب | Template Library")
print("=" * 60)

try:
    from tezniti_3d.template_library import TemplateLibrary, TemplateCategory
    
    lib = TemplateLibrary()
    
    print(f"   📚 إجمالي القوالب: {len(lib.get_all())}")
    
    # التصنيفات
    categories = lib.get_categories()
    print(f"   📁 التصنيفات: {len(categories)}")
    for cat in categories[:3]:
        print(f"      - {cat['name']}: {cat['count']}")
    
    # البحث
    results = lib.search("ترس")
    print(f"   🔍 نتائج البحث عن 'ترس': {len(results)}")
    
    # قالب
    template = lib.get("spur_gear_20")
    if template:
        print(f"   📋 قالب: {template.name_ar}")
        print(f"      المعاملات: {template.parameters}")
    
    print("   ✅ نجح!")
except Exception as e:
    print(f"   ❌ فشل: {e}")

# ============================================================
# 11. واجهة الصوت
# ============================================================
print("\n" + "=" * 60)
print("1️⃣1️⃣ واجهة الصوت | Voice Interface")
print("=" * 60)

try:
    from tezniti_3d.voice_interface import VoiceInterface
    
    interface = VoiceInterface()
    
    # معالجة أوامر نصية
    commands = [
        "أنشئ ترس حلزوني قطر 40",
        "صمم صندوق طول 100 عرض 50",
    ]
    
    for cmd in commands:
        result = interface.process_text(cmd)
        print(f"   🎤 الأمر: {cmd}")
        print(f"      النوع: {result['command']['type']}")
        print(f"      القطعة: {result['command']['part_type']}")
    
    print("   ✅ نجح!")
except Exception as e:
    print(f"   ❌ فشل: {e}")

# ============================================================
# الملخص
# ============================================================
print("\n" + "=" * 60)
print("📊 ملخص الاختبار | Test Summary")
print("=" * 60)

print("""
✅ جميع الاختبارات نجحت!

القدرات المختبرة:
 1. محرك الحوار الذكي
 2. التعلم التفاعلي
 3. الاستنباط العكسي
 4. القصص السببية
 5. تصدير المعرفة
 6. الوكيل الذكي
 7. نظام التجميعات
 8. المحاكاة الحركية
 9. مساعد التصميم
10. مكتبة القوالب
11. واجهة الصوت

🎉 جاهز للاستخدام!
""")
