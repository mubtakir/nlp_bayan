"""
مثال على نظام الدماغ المزدوج
==============================

يوضح كيفية استخدام DualBrain للحصول على تحليل أفضل من خلال
الجمع بين المعالجة المنطقية والرياضياتية.

المؤلف: باسل يحيى عبدالله
"""

import sys
sys.path.insert(0, '/home/al-mubtakir/Documents/bayan_python_ide14')

from bayan.bayan.dual_brain import DualBrain

print("═══════════════════════════════════════════════════════")
print("   نظام الدماغ المزدوج - Dual Brain System")
print("═══════════════════════════════════════════════════════\n")

# إنشاء الدماغ المزدوج
brain = DualBrain()

# ═══ مثال 1: تحليل جملة بسيطة ═══
print("📝 مثال 1: تحليل جملة بسيطة\n")

result1 = brain.process("محمد أكل تفاحة", debug=True)
print("\n" + "─" * 60)
result1.print_summary()

# ═══ مثال 2: جملة بدون سياق ═══
print("\n\n" + "═" * 60)
print("\n📝 مثال 2: جملة بدون سياق كافٍ\n")

result2 = brain.process("الطقس جميل اليوم", debug=False)
result2.print_summary()

# ═══ مثال 3: مع سياق إضافي ═══
print("\n\n" + "═" * 60)
print("\n📝 مثال 3: مع سياق إضافي\n")

context = {
    "time": "morning",
    "location": "home"
}

result3 = brain.process("محمد جائع", context=context, debug=False)
result3.print_summary()

# ═══ الإحصائيات ═══
print("\n\n" + "═" * 60)
print("\n📊 إحصائيات الدماغ المزدوج:\n")

stats = brain.get_statistics()

print("🧠 الإجمالي:")
print(f"  • إجمالي المعالجات: {stats['total_processes']}")
print(f"  • الناجحة: {stats['successful']}")
print(f"  • معدل النجاح: {stats['success_rate']}")
print(f"  • متوسط التوافق: {stats['average_consensus']}")

print("\n🧩 الفص الأيسر (منطقي):")
left_stats = stats['left_brain']
print(f"  • التحليلات: {left_stats['total_analyses']}")
print(f"  • الناجحة: {left_stats['successful']}")
print(f"  • تعارضات مكتشفة: {left_stats['contradictions_found']}")

print("\n🎨 الفص الأيمن (رياضياتي):")
right_stats = stats['right_brain']
print(f"  • التحليلات: {right_stats['total_analyses']}")
print(f"  • الحسابات الناجحة: {right_stats['successful_computations']}")
print(f"  • كائنات المعادلة الأم: {right_stats['mother_objects_count']}")

print("\n🌉 طبقة التكامل:")
int_stats = stats['integration']
print(f"  • التكاملات: {int_stats['total_integrations']}")
print(f"  • الناجحة: {int_stats['successful']}")
print(f"  • تعارضات حُلّت: {int_stats['conflicts_resolved']}")

# ═══ مثال 4: تحليل متعدد ═══
print("\n\n" + "═" * 60)
print("\n📝 مثال 4: تحليل متعدد لأمثلة مختلفة\n")

examples = [
    "أحمد سعيد",
    "الشمس مشرقة",
    "2 + 2 = 4",
    "القط على السجادة"
]

print("النتائج السريعة:")
for i, example in enumerate(examples, 1):
    result = brain.process(example, debug=False)
    print(f"\n{i}. '{example}'")
    print(f"   ثقة: {result.final_confidence*100:.0f}% | "
          f"توافق: {result.validation.consensus*100:.0f}% | "
          f"وقت: {result.processing_time*1000:.1f}ms")

# ═══ النتيجة النهائية ═══
print("\n\n" + "═" * 60)
print("\n✅ اكتملت جميع الأمثلة بنجاح!")
print("\n💡 الخلاصة:")
print("  نظام الدماغ المزدوج يجمع بين:")
print("  • التفكير المنطقي (الفص الأيسر)")
print("  • التفكير الرياضياتي (الفص الأيمن)")
print("  • التحقق المتبادل والنقد المشترك")
print("  → النتيجة: تحليل أعمق وأدق! 🚀")

print("\n" + "═" * 60)
