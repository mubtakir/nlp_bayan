"""
أمثلة على نظام الخبير-المستكشف
===================================

يوضح كيفية استخدام BrainSystem للجمع بين الخبرة والاستكشاف.

المؤلف: باسل يحيى عبدالله
"""

import sys
sys.path.insert(0, '/home/al-mubtakir/Documents/bayan_python_ide14')

from bayan.bayan.expert_explorer import (
    ExpertSystem, ExplorerSystem, BrainSystem,
    DecisionType, ConfidenceLevel
)
import numpy as np

print("═══════════════════════════════════════════════════════")
print("   نظام الخبير-المستكشف - أمثلة شاملة")
print("═══════════════════════════════════════════════════════\n")

# ═══ مثال 1: نظام الخبير فقط ═══
print("📚 مثال 1: نظام الخبير\n")

expert = ExpertSystem(confidence_threshold=0.6)

# إضافة معرفة
expert.add_knowledge("كيف أتعلم Python؟", "ابدأ بالأساسيات ثم مارس المشاريع", confidence=0.95)
expert.add_knowledge("ما هي أفضل لغة برمجة؟", "Python للمبتدئين، Rust للأداء", confidence=0.8)
expert.add_knowledge("كيف أحل مشكلة معينة؟", "حلل المشكلة ثم قسمها لخطوات", confidence=0.9)

# استعلام مباشر
solution, conf = expert.find_solution("كيف أتعلم Python؟")
print(f"✅ سؤال: كيف أتعلم Python؟")
print(f"   الحل: {solution}")
print(f"   الثقة: {conf*100:.1f}%\n")

# استعلام تقريبي
result = expert.find_solution("كيف أتعلم البرمجة؟")
if result:
    solution2, conf2 = result
    print(f"✅ سؤال: كيف أتعلم البرمجة؟ (تقريبي)")
    print(f"   الحل: {solution2}")
    print(f"   الثقة: {conf2*100:.1f}%\n")
else:
    print("❌ لم يجد الخبير حل مناسب\n")

# ═══ مثال 2: نظام المستكشف فقط ═══
print("─" * 60)
print("\n🔍 مثال 2: نظام المستكشف\n")

explorer = ExplorerSystem(exploration_rate=0.3)

# استكشاف بدون حل سابق
result1 = explorer.explore(context="مشكلة جديدة")
print(f"كشاف 1:")
print(f"  - الجدة: {result1.novelty*100:.1f}%")
print(f"  - الثقة: {result1.confidence*100:.1f}%")
print(f"  - المسار: {result1.exploration_path}\n")

# استكشاف متعامد
expert_sol = np.array([1.0, 0.0, 0.0])
result2 = explorer.explore(context="مشكلة", expert_solution=expert_sol)
print(f"استكشاف 2 (متعامد):")
print(f"  - الجدة: {result2.novelty*100:.1f}%")
print(f"  - الثقة: {result2.confidence*100:.1f}%\n")

# ═══ مثال 3: نظام الدماغ (Brain) ═══
print("─" * 60)
print("\n🧠 مثال 3: نظام الدماغ المتكامل\n")

brain = BrainSystem(expert_weight=0.7, explorer_weight=0.3)

# إضافة معرفة للخبير
brain.expert.add_knowledge(
    "ما هو الذكاء الاصطناعي؟",
    "مجال يهتم بجعل الآلات تتصرف بذكاء",
    confidence=0.95
)
brain.expert.add_knowledge(
    "كيف أبني chatbot؟",
    "استخدم NLP + نموذج لغة + واجهة محادثة",
    confidence=0.85
)

# قرار 1: الخبير لديه معرفة
print("القرار 1: سؤال معروف للخبير")
decision1 = brain.decide("ما هو الذكاء الاصطناعي؟")
print(f"  نوع القرار: {decision1.decision_type.value}")
print(f"  الحل: {decision1.solution}")
print(f"  ثقة الخبير: {decision1.expert_confidence*100:.1f}%")
print(f"  ثقة المستكشف: {decision1.explorer_confidence*100:.1f}%")
print(f"  الثقة النهائية: {decision1.final_confidence*100:.1f}%")
print(f"  السبب: {decision1.reasoning}\n")

# قرار 2: الخبير ليس متأكد تماماً
print("القرار 2: سؤال تقريبي")
decision2 = brain.decide("كيف أنشئ روبوت محادثة؟")
print(f"  نوع القرار: {decision2.decision_type.value}")
print(f"  ثقة الخبير: {decision2.expert_confidence*100:.1f}%")
print(f"  ثقة المستكشف: {decision2.explorer_confidence*100:.1f}%")
print(f"  الثقة النهائية: {decision2.final_confidence*100:.1f}%")
print(f"  السبب: {decision2.reasoning}\n")

# قرار 3: سؤال جديد تماماً
print("القرار 3: سؤال جديد تماماً")
decision3 = brain.decide("ما هو quantum computing؟")
print(f"  نوع القرار: {decision3.decision_type.value}")
print(f"  ثقة الخبير: {decision3.expert_confidence*100:.1f}%")
print(f"  ثقة المستكشف: {decision3.explorer_confidence*100:.1f}%")
print(f"  الثقة النهائية: {decision3.final_confidence*100:.1f}%")
print(f"  السبب: {decision3.reasoning}\n")

# ═══ مثال 4: النظريات الثلاث ═══
print("─" * 60)
print("\n⚛️ مثال 4: النظريات الثلاث\n")

from bayan.bayan.expert_explorer import (
    ZeroDualityTheory, PerpendicularOppositesTheory, FilamentTheory
)

# 1. ثنائية الصفر
print("1. نظرية ثنائية الصفر:")
positive = 0.8
negative = 0.2
balance = ZeroDualityTheory.calculate_balance(positive, negative)
print(f"   إيجابي: {positive}, سلبي: {negative}")
print(f"   عامل التوازن: {balance:.3f}")
print(f"   (كلما اقترب من 0، كان أفضل)\n")

# 2. تعامد الأضداد
print("2. نظرية تعامد الأضداد:")
direction = np.array([1.0, 0.0])
perpendicular = PerpendicularOppositesTheory.get_perpendicular_direction(direction)
print(f"   الاتجاه الأساسي: {direction}")
print(f"   الاتجاه المتعامد: {perpendicular}")
print(f"   التحقق (يجب أن = 0): {np.dot(direction, perpendicular):.10f}\n")

# 3. نظرية الفتائل
print("3. نظرية الفتائل:")
filaments = [
    ('sigmoid', 1.0, {'k': 5.0, 'x0': 0.0}),
    ('linear', 0.5, {'slope': 0.2, 'intercept': 0.1})
]
x_test = 1.0
result = FilamentTheory.combine_filaments(filaments, x_test)
print(f"   الفتائل: 1 sigmoid + 1 linear")
print(f"   f({x_test}) = {result:.3f}\n")

# ═══ الإحصائيات ═══
print("─" * 60)
print("\n📊 إحصائيات نظام الدماغ:\n")

stats = brain.get_statistics()
for key, value in stats.items():
    key_ar = {
        'total_decisions': 'إجمالي القرارات',
        'expert_success_rate': 'معدل نجاح الخبير',
        'expert_weight': 'وزن الخبير',
        'explorer_weight': 'وزن المستكشف',
        'average_confidence': 'متوسط الثقة'
    }.get(key, key)
    
    if isinstance(value, float):
        print(f"  • {key_ar}: {value:.2f}")
    else:
        print(f"  • {key_ar}: {value}")

print("\n✅ اكتملت جميع الأمثلة بنجاح!")
