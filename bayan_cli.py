#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
واجهة سطر أوامر تفاعلية لبيان (Bayan CLI)
مثال عملي من المقترحات التطويرية

الميزات:
- تحليل الجمل العربية
- دعم اللهجات (مصرية، خليجية، شامية، مغربية)
- تحويل تلقائي من العامية إلى الفصحى
"""

import cmd
import sys
import os

# إضافة مسار المشروع
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# استخدام الطبقة الوسيطية بدلاً من الملفات المقفلة
from extensions.extended_istinbat import ExtendedIstinbatEngine
from extensions.dialect_adapter import DialectAdapter
from extensions.bayan_tutor import BayanTutor
from extensions.equation_visualizer import EquationVisualizer
from extensions.dialogue_system import IntelligentDialogueSystem
from extensions.bayan_baserah_bridge import BayanBaserahBridge
from extensions.visual_semantic_engine import VisualSemanticEngine
from bayan.bayan.linguistic_equation import KnowledgeBase, LinguisticEquationParser

class BayanCLI(cmd.Cmd):
    """واجهة سطر أوامر تفاعلية لبيان"""

    intro = """
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║                  🧠 بيان - محرك الاستنباط                      ║
║                  Bayan - Istinbat Engine CLI                    ║
║                                                                  ║
║  اكتب جملة عربية لتحليلها، أو 'help' للمساعدة                 ║
║  يدعم اللهجات: مصرية، خليجية، شامية، مغربية                   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

💡 أمثلة (فصحى):
  • أحمد ضرب الكرة
  • محمد أكل تفاحة

🌍 أمثلة (لهجات):
  • أحمد عايز ياكل تفاحة (مصري)
  • محمد يبي ياكل رز (خليجي)
  • سارة بدها تشرب ماء (شامي)

📝 أوامر خاصة:
  • help - عرض المساعدة
  • stats - عرض الإحصائيات
  • dialects - عرض اللهجات المدعومة
  • convert <لهجة> <نص> - تحويل من لهجة للفصحى
  • detect <نص> - اكتشاف اللهجة
  • learn - 🎓 بدء الدروس التفاعلية
  • visualize <جملة> - 📊 تصور بصري للمعادلة
  • chat - 🤖 وضع المحادثة الذكية
  • baserah <كلمة> - 👁️ تحليل بصري-دلالي (بصيرة)
  • letter <حرف> - 📝 تحليل حرف بصرياً
  • compare <ح1> <ح2> - 🔍 مقارنة حرفين
  • exit - الخروج
"""
    prompt = "بيان> "

    def __init__(self):
        super().__init__()
        # استخدام المحرك الموسع من الطبقة الوسيطية
        self.engine = ExtendedIstinbatEngine(enable_dialect_support=True)
        self.kb = self.engine.kb
        self.parser = LinguisticEquationParser(self.kb)
        self.dialect_adapter = DialectAdapter()
        self.tutor = BayanTutor()
        self.visualizer = EquationVisualizer()
        self.dialogue = IntelligentDialogueSystem()
        self.bridge = BayanBaserahBridge()
        self.semantic_engine = VisualSemanticEngine()
        self.history = []
        self.chat_mode = False  # وضع المحادثة
        self.current_dialect = None  # None = اكتشاف تلقائي
    
    def default(self, line):
        """تحليل أي جملة يدخلها المستخدم"""
        if not line.strip():
            return

        # حفظ في التاريخ
        self.history.append(line)

        print()  # سطر فارغ
        result = self.engine.process(line, dialect=self.current_dialect)

        if result:
            print("✅ تم التحليل بنجاح!")

            # عرض معلومات اللهجة إذا تم اكتشافها
            if result.dialect:
                print(f"   🌍 اللهجة: {result.dialect}")
                print(f"   📝 الأصل: {result.original_text}")
                print(f"   ✨ الفصحى: {result.converted_text}")

            print(f"   ├─ الحدث: {result.equation.event}")
            print(f"   ├─ الكيانات: {list(result.equation.entities.keys())}")

            if result.consequences:
                print(f"   └─ النتائج:")
                for cons in result.consequences:
                    print(f"      • {cons.entity_name}:")
                    for state, change in cons.state_changes.items():
                        if isinstance(change, (int, float)):
                            sign = "+" if change > 0 else ""
                            print(f"        - {state}: {sign}{change}")
                        else:
                            print(f"        - {state}: {change}")
            else:
                print(f"   └─ النتائج: (لا توجد نتائج مستنتجة)")
        else:
            print("❌ لم أتمكن من تحليل الجملة")
            print("💡 تأكد من:")
            print("   • الجملة بالعربية (فصحى أو لهجة)")
            print("   • تحتوي على فاعل وفعل على الأقل")
            print("   • جرب: dialects لمعرفة اللهجات المدعومة")
        print()
    
    def do_add_verb(self, line):
        """
        إضافة فعل جديد
        الاستخدام: add_verb <فعل> <تأثير_فاعل> <تأثير_مفعول>
        مثال: add_verb يدرس معرفة:+0.5,تعب:+0.3 فهم:+0.6
        """
        if not line.strip():
            print("\n❌ الاستخدام: add_verb <فعل> <تأثير_فاعل> <تأثير_مفعول>")
            print("مثال: add_verb يدرس معرفة:+0.5,تعب:+0.3 فهم:+0.6\n")
            return
        
        parts = line.split()
        if len(parts) < 2:
            print("\n❌ يجب تحديد الفعل والتأثيرات\n")
            return
        
        verb = parts[0]
        subject_effects = self._parse_effects(parts[1]) if len(parts) > 1 else {}
        object_effects = self._parse_effects(parts[2]) if len(parts) > 2 else {}
        
        self.kb.add_custom_event(verb, subject_effects, object_effects)
        print(f"\n✅ تم إضافة الفعل '{verb}' بنجاح!")
        print(f"   ├─ تأثير الفاعل: {subject_effects}")
        print(f"   └─ تأثير المفعول: {object_effects}\n")
    
    def _parse_effects(self, effects_str: str) -> dict:
        """تحليل سلسلة التأثيرات"""
        effects = {}
        for effect in effects_str.split(','):
            if ':' in effect:
                key, value = effect.split(':')
                try:
                    effects[key] = float(value)
                except:
                    effects[key] = value
        return effects
    
    def do_list_verbs(self, line):
        """عرض جميع الأفعال المتاحة"""
        print("\n📚 الأفعال المتاحة:")
        for i, verb in enumerate(self.kb.event_outcomes.keys(), 1):
            print(f"   {i}. {verb}")
        print()

    def do_dialects(self, line):
        """عرض اللهجات المدعومة"""
        print("\n🌍 اللهجات المدعومة:")
        dialects_info = {
            "egyptian": ("مصري", "عايز، ازاي، ده، دي، امبارح"),
            "gulf": ("خليجي", "يبي، ودي، شلون، وين، الحين"),
            "levantine": ("شامي", "بدي، شو، هيك، هون، منيح"),
            "moroccan": ("مغربي", "بغيت، كيفاش، دابا، بزاف، مزيان"),
        }
        for dialect, (name, examples) in dialects_info.items():
            status = "✓" if self.current_dialect == dialect else " "
            print(f"   [{status}] {dialect}: {name}")
            print(f"       أمثلة: {examples}")
        print(f"\n   💡 الوضع الحالي: {'اكتشاف تلقائي' if not self.current_dialect else self.current_dialect}")
        print()

    def do_set_dialect(self, line):
        """تعيين اللهجة الافتراضية: set_dialect <اسم> أو auto"""
        if not line.strip():
            print("\n❌ الاستخدام: set_dialect <egyptian|gulf|levantine|moroccan|auto>")
            return

        dialect = line.strip().lower()
        if dialect == "auto":
            self.current_dialect = None
            print("\n✅ تم تفعيل الاكتشاف التلقائي للهجة\n")
        elif dialect in self.dialect_adapter.DIALECTS:
            self.current_dialect = dialect
            print(f"\n✅ تم تعيين اللهجة: {dialect}\n")
        else:
            print(f"\n❌ لهجة غير معروفة: {dialect}")
            print("   اللهجات المتاحة: egyptian, gulf, levantine, moroccan, auto\n")

    def do_convert(self, line):
        """تحويل نص من لهجة إلى الفصحى: convert <نص>"""
        if not line.strip():
            print("\n❌ الاستخدام: convert <نص باللهجة>")
            print("   مثال: convert أحمد عايز ياكل تفاحة\n")
            return

        result = self.dialect_adapter.convert_to_standard(line.strip())

        print(f"\n📝 التحويل:")
        print(f"   ├─ النص الأصلي: {result.original}")
        print(f"   ├─ اللهجة المكتشفة: {result.dialect.value}")
        print(f"   ├─ نسبة الثقة: {result.confidence:.0%}")
        print(f"   ├─ النص المحول: {result.converted}")
        if result.changes:
            print(f"   └─ التغييرات:")
            for old, new in result.changes:
                print(f"      • {old} → {new}")
        print()

    def do_detect(self, line):
        """اكتشاف لهجة النص: detect <نص>"""
        if not line.strip():
            print("\n❌ الاستخدام: detect <نص>")
            print("   مثال: detect أحمد عايز ياكل تفاحة\n")
            return

        dialect, confidence = self.dialect_adapter.detect_dialect(line.strip())

        dialect_names = {
            "standard": "فصحى",
            "egyptian": "مصري",
            "gulf": "خليجي",
            "levantine": "شامي",
            "moroccan": "مغربي",
        }

        print(f"\n🔍 نتيجة الاكتشاف:")
        print(f"   ├─ اللهجة: {dialect.value} ({dialect_names.get(dialect.value, '')})")
        print(f"   └─ الثقة: {confidence:.0%}")
        print()
    
    def do_stats(self, line):
        """عرض إحصائيات قاعدة المعرفة"""
        print("\n📊 إحصائيات قاعدة المعرفة:")
        print(f"   ├─ عدد الأفعال: {len(self.kb.event_outcomes)}")
        print(f"   ├─ عدد المعادلات المحفوظة: {len(self.kb.equations)}")
        print(f"   ├─ عدد الجمل المحللة: {len(self.history)}")
        print(f"   └─ آخر جملة: {self.history[-1] if self.history else 'لا توجد'}")
        print()
    
    def do_history(self, line):
        """عرض تاريخ الجمل المحللة"""
        if not self.history:
            print("\n📝 لا يوجد تاريخ بعد\n")
            return
        
        print("\n📝 تاريخ الجمل المحللة:")
        for i, sentence in enumerate(self.history, 1):
            print(f"   {i}. {sentence}")
        print()
    
    def do_clear(self, line):
        """مسح الشاشة"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print(self.intro)
    
    def do_help(self, line):
        """عرض المساعدة"""
        print("""
╔══════════════════════════════════════════════════════════════════╗
║                         📚 المساعدة                             ║
╚══════════════════════════════════════════════════════════════════╝

🎯 الأوامر المتاحة:

  📝 تحليل الجمل:
     • اكتب أي جملة عربية مباشرة (فصحى أو لهجة)
     • مثال: أحمد ضرب الكرة
     • مثال: أحمد عايز ياكل (مصري)

  🌍 أوامر اللهجات:
     • dialects - عرض اللهجات المدعومة
     • set_dialect <اسم> - تعيين لهجة (egyptian/gulf/levantine/moroccan/auto)
     • convert <نص> - تحويل من لهجة للفصحى
     • detect <نص> - اكتشاف لهجة النص

  ⚙️ إدارة الأفعال:
     • add_verb <فعل> <تأثيرات> - إضافة فعل جديد
     • list_verbs - عرض جميع الأفعال

  📊 المعلومات:
     • stats - عرض الإحصائيات
     • history - عرض تاريخ الجمل

  🛠️ أدوات:
     • clear - مسح الشاشة
     • help - عرض هذه المساعدة
     • exit - الخروج من البرنامج

🌍 أمثلة اللهجات:
  بيان> أحمد عايز ياكل تفاحة          (مصري → يريد)
  بيان> محمد يبي يروح السوق           (خليجي → يريد + يذهب)
  بيان> سارة بدها تشرب ماء            (شامي → تريد)
  بيان> علي بغى يمشي للدار            (مغربي → يريد + يذهب + المنزل)

💡 نصائح:
  • النظام يكتشف اللهجة تلقائياً
  • استخدم set_dialect لتحديد لهجة معينة
  • استخدم convert لرؤية التحويل بالتفصيل
""")

    def do_learn(self, line):
        """🎓 بدء الدروس التفاعلية"""
        print("\n🎓 نظام بيان التعليمي")
        print("=" * 50)

        # عرض الدروس
        lessons = self.tutor.list_lessons()
        print("\n📚 الدروس المتاحة:")
        for i, lesson in enumerate(lessons, 1):
            print(f"   {i}. {lesson['status']} {lesson['title']}")
            print(f"      المستوى: {lesson['level']} | التمارين: {lesson['exercises_count']}")

        print("\n💡 أدخل رقم الدرس للبدء (أو 'رجوع' للعودة):")

        # بدء الدرس التفاعلي
        lesson_map = {str(i): lesson['id'] for i, lesson in enumerate(lessons, 1)}

        choice = input("   اختيارك: ").strip()
        if choice in lesson_map:
            self.tutor.run_interactive(lesson_map[choice])
        elif choice == "رجوع" or choice == "":
            print("   👍 تم الرجوع")
        else:
            print("   ❌ اختيار غير صحيح")

    def do_visualize(self, line):
        """📊 تصور بصري للمعادلة اللغوية"""
        if not line.strip():
            print("❌ الاستخدام: visualize <جملة>")
            print("   مثال: visualize أحمد أكل تفاحة")
            return

        # تحليل الجملة
        result = self.engine.process(line)

        if result and result.equation:
            # استخراج العناصر
            entities = list(result.equation.entities.keys())
            subject = entities[0] if len(entities) > 0 else "?"
            obj = entities[1] if len(entities) > 1 else "?"
            verb = result.equation.event or "?"

            # إنشاء النتائج
            results_data = []
            if result.consequences:
                for cons in result.consequences[:3]:
                    for state, change in cons.state_changes.items():
                        results_data.append({
                            "entity": cons.entity_name,
                            "change": f"{state}: {change}"
                        })

            # إنشاء التصور
            svg = self.visualizer.visualize_equation(subject, verb, obj, results_data)

            # حفظ في ملف
            filename = "equation_visualization.html"
            self.visualizer.save_to_file(svg, filename)

            print(f"\n✅ تم إنشاء التصور البصري!")
            print(f"   📂 الملف: {filename}")
            print(f"   📐 المعادلة: {subject} + {verb} → {obj}")
            print(f"\n💡 افتح الملف في المتصفح لرؤية التصور")
        else:
            print("❌ لم يتم التعرف على بنية الجملة")

    def do_progress(self, line):
        """📊 عرض تقدم التعلم"""
        progress = self.tutor.get_progress()
        print("\n📊 تقدمك في التعلم:")
        print(f"   ⭐ النقاط: {progress['total_points']}")
        print(f"   📚 الدروس المكتملة: {progress['completed_lessons']}/{progress['total_lessons']}")
        print(f"   📈 نسبة الإنجاز: {progress['percentage']}%")

        # شريط تقدم بسيط
        filled = int(progress['percentage'] / 10)
        bar = "█" * filled + "░" * (10 - filled)
        print(f"   [{bar}]")

    def do_chat(self, line):
        """🤖 وضع المحادثة الذكية"""
        print("\n🤖 وضع المحادثة الذكية")
        print("=" * 50)
        print("💡 تحدث مع بيان بشكل طبيعي!")
        print("   اكتب 'خروج' للعودة للوضع العادي")
        print("=" * 50)

        self.dialogue.reset()

        while True:
            try:
                user_input = input("\n👤 أنت: ").strip()

                if not user_input:
                    continue

                if user_input in ["خروج", "exit", "quit"]:
                    print("\n👍 تم الخروج من وضع المحادثة")
                    break

                response = self.dialogue.chat(user_input)
                print(f"🤖 بيان: {response}")

            except KeyboardInterrupt:
                print("\n\n👍 تم الخروج من وضع المحادثة")
                break

    def do_baserah(self, line):
        """👁️ تحليل بصري-دلالي للكلمة باستخدام بصيرة"""
        if not line.strip():
            print("❌ الرجاء إدخال كلمة للتحليل")
            print("   مثال: baserah عقل")
            return

        word = line.strip()
        print(f"\n👁️ تحليل بصيرة للكلمة: {word}")
        print("=" * 50)

        # تحليل شامل
        result = self.semantic_engine.full_analysis(word)

        print(f"\n📊 التحليل البصري:")
        print(f"   المعاني: {', '.join(result['visual_analysis']['meanings'][:5])}")
        print(f"   التناغم: {result['visual_analysis']['harmony']}")

        print(f"\n🧵 نظرية الخيوط:")
        print(f"   التماسك: {result['filament_theory']['cohesion']}")
        print(f"   التفسير: {result['filament_theory']['interpretation']}")

        print(f"\n📍 الموقع في الفضاء الدلالي:")
        pos = result['space_position']
        print(f"   X (مادي↔نفسي): {pos.get('x', 0)}")
        print(f"   Y (سلبي↔إيجابي): {pos.get('y', 0)}")
        print(f"   Z (سطحي↔عميق): {pos.get('z', 0)}")
        print(f"   التفسير: {result['space_interpretation']}")

        print(f"\n⚡ ثنائية الأضداد:")
        for d in result['dualities'][:3]:
            print(f"   {d['letter']} ↔ {d['opposite']}")

        print(f"\n📝 الملخص: {result['summary']}")
        print()

    def do_letter(self, line):
        """📝 تحليل حرف بصرياً"""
        if not line.strip():
            print("❌ الرجاء إدخال حرف للتحليل")
            print("   مثال: letter ع")
            return

        letter = line.strip()[0]  # أخذ الحرف الأول فقط
        print(f"\n📝 تحليل الحرف: {letter}")
        print("=" * 50)

        # تحليل بصري
        analysis = self.bridge.analyze_letter_visually(letter)
        print(f"\n🔍 الشكل: {analysis.shape_type.value}")
        print(f"📚 المعاني: {', '.join(analysis.semantic_meanings[:5])}")

        # المعادلة
        eq = self.bridge.letter_to_equation(letter)
        print(f"\n📐 المعادلة:")
        print(f"   النوع: {eq.get('equation_type', 'غير محدد')}")
        print(f"   الصيغة: {eq.get('equation', 'غير متوفرة')}")

        # الضد
        opposite = self.bridge.find_opposite_letter(letter)
        print(f"\n⚡ الضد البصري:")
        print(f"   الشكل المضاد: {opposite['opposite_shape']}")
        print(f"   الحروف المضادة: {', '.join(opposite['opposite_letters'][:3])}")

        # ثنائية الصفر
        duality = self.semantic_engine.apply_zero_duality(letter)
        if "error" not in duality:
            print(f"\n🌀 ثنائية الصفر:")
            print(f"   الموقع: {duality['position']}")
            print(f"   أقرب ضد: {duality['closest_opposite_letter']}")
        print()

    def do_compare(self, line):
        """🔍 مقارنة حرفين بصرياً"""
        parts = line.strip().split()
        if len(parts) < 2:
            print("❌ الرجاء إدخال حرفين للمقارنة")
            print("   مثال: compare ب ت")
            return

        letter1 = parts[0][0]
        letter2 = parts[1][0]

        print(f"\n🔍 مقارنة بين '{letter1}' و '{letter2}'")
        print("=" * 50)

        # مقارنة بصرية
        comparison = self.bridge.compare_letters_visually(letter1, letter2)
        print(f"\n📊 التشابه:")
        print(f"   الشكل: {comparison['shape_similarity']}")
        print(f"   المعنى: {comparison['meaning_similarity']}")
        print(f"   المعادلة: {comparison['equation_similarity']}")
        print(f"   الكلي: {comparison['overall_similarity']}")
        print(f"\n🔗 العلاقة: {comparison['relationship']}")

        if comparison['common_meanings']:
            print(f"📚 المعاني المشتركة: {', '.join(comparison['common_meanings'][:5])}")

        # التعامد
        perp = self.semantic_engine.apply_perpendicularity(letter1, letter2)
        if "error" not in perp:
            print(f"\n📐 التعامد:")
            print(f"   الزاوية: {perp['angle_degrees']}°")
            print(f"   العلاقة: {perp['relationship']}")
        print()

    def do_exit(self, line):
        """الخروج من البرنامج"""
        print("\n👋 شكراً لاستخدامك بيان!")
        print("🌟 نراك قريباً!\n")
        return True

    def do_quit(self, line):
        """الخروج من البرنامج"""
        return self.do_exit(line)

    def emptyline(self):
        """لا تفعل شيئاً عند الضغط على Enter فقط"""
        pass

def main():
    """الدالة الرئيسية"""
    try:
        BayanCLI().cmdloop()
    except KeyboardInterrupt:
        print("\n\n⚠️  تم إيقاف البرنامج بواسطة المستخدم")
        print("👋 مع السلامة!\n")
    except Exception as e:
        print(f"\n❌ خطأ غير متوقع: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
