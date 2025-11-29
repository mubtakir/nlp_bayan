#!/usr/bin/env python3
"""
Letter Semantics Demo
=====================

Demonstrates the phonetic-semantic analysis of Arabic letters and words.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from bayan.bayan.letter_semantics import LetterSemanticsDatabase


def print_separator(char='=', length=70):
    print(char * length)


def demo_letter_analysis():
    """Demonstrate analysis of individual letters"""
    print_separator()
    print("تحليل الحروف الفردية / Individual Letter Analysis")
    print_separator()
    
    db = LetterSemanticsDatabase()
    
    for letter in ['ا', 'و', 'ي']:
        sem = db.get_letter_meanings(letter)
        if sem:
            print(f"\n📝 الحرف / Letter: {sem.letter}")
            print(f"   النوع / Type: {sem.letter_type.value}")
            
            print(f"\n   🔊 الدلالة الصوتية / Sound Semantics:")
            print(f"      الصوت / Phoneme: {sem.sound.phoneme}")
            if sem.sound.baby_cry_meaning:
                print(f"      معنى بكاء الطفل / Baby Cry: {sem.sound.baby_cry_meaning}")
            print(f"      المعاني / Meanings: {', '.join(sem.sound.meanings)}")
            
            print(f"\n   👁️  الدلالة الشكلية / Shape Semantics:")
            print(f"      الشكل العربي / Arabic Shape: {sem.shape.arabic_shape}")
            if sem.shape.latin_shape:
                print(f"      الشكل اللاتيني / Latin Shape: {sem.shape.latin_shape}")
            print(f"      المعاني / Meanings: {', '.join(sem.shape.meanings)}")
            
            print(f"\n   💡 المعاني المدمجة / Combined Meanings:")
            for meaning in sem.combined_meanings:
                print(f"      • {meaning}")
            
            print(f"\n   📚 أمثلة / Examples:")
            for word, explanation in sem.examples:
                print(f"      • {word}: {explanation}")
        
        print()


def demo_word_analysis():
    """Demonstrate analysis of complete words"""
    print_separator()
    print("تحليل الكلمات / Word Analysis")
    print_separator()
    
    db = LetterSemanticsDatabase()
    
    test_words = [
        'واو',    # wow - exclamation
        'أي',     # which - pointing
        'يا',     # oh - calling
        'أو',     # or - choice
    ]
    
    for word in test_words:
        print(f"\n🔍 تحليل كلمة / Analyzing word: {word}")
        analysis = db.analyze_word(word)
        
        print(f"\n   الحروف / Letters:")
        for letter_sem in analysis['letters']:
            print(f"      • {letter_sem.letter}: {letter_sem.combined_meanings[0]}")
        
        print(f"\n   المعاني الصوتية المدمجة / Combined Sound Meanings:")
        print(f"      {', '.join(analysis['combined_sound_meanings'][:5])}")
        
        print(f"\n   المعاني الشكلية المدمجة / Combined Shape Meanings:")
        print(f"      {', '.join(analysis['combined_shape_meanings'][:5])}")
        
        print(f"\n   💡 المعنى المستنبط / Inferred Meaning:")
        print(f"      {analysis['inferred_meaning']}")
        
        print()


def demo_statistics():
    """Show database statistics"""
    print_separator()
    print("إحصائيات قاعدة البيانات / Database Statistics")
    print_separator()
    
    db = LetterSemanticsDatabase()
    stats = db.get_statistics()
    
    print(f"\n📊 الإحصائيات / Statistics:")
    print(f"   إجمالي الحروف / Total Letters: {stats['total_letters']}")
    print(f"   حروف العلة / Vowels: {stats['vowels']}")
    print(f"   الحروف الساكنة / Consonants: {stats['consonants']}")
    print()


def demo_theory_explanation():
    """Explain the theory behind the system"""
    print_separator('=', 70)
    print("نظرية الدلالة الصوتية والشكلية للحروف")
    print("Phonetic-Semantic Theory of Letters")
    print_separator('=', 70)
    
    print("""
🎯 الفكرة الأساسية / Core Concept:
   "المعنى للكلمة ليس اعتباطاً بل هناك سر يجب كشفه"
   "The meaning of a word is not arbitrary - there is a secret to uncover"

📚 البحث / Research:
   • 40 سنة من الملاحظة والتحليل
   • 40 years of observation and analysis
   
🔬 المنهجية / Methodology:
   1. ملاحظة بكاء الأطفال / Observing baby cries
   2. تحليل الأصوات / Analyzing sounds
   3. دراسة الأشكال / Studying shapes
   4. ربط المعاني / Connecting meanings

💡 النتيجة / Result:
   كل حرف يحمل معنى من صوته ومن شكله
   Each letter carries meaning from its sound and shape
   
   معنى الكلمة = تعاضد معاني حروفها
   Word meaning = Synergy of its letters' meanings
""")


def main():
    """Run all demos"""
    demo_theory_explanation()
    input("\nPress Enter to continue...")
    
    demo_letter_analysis()
    input("\nPress Enter to continue...")
    
    demo_word_analysis()
    input("\nPress Enter to continue...")
    
    demo_statistics()
    
    print_separator()
    print("✅ العرض التوضيحي اكتمل / Demo Complete")
    print_separator()
    print("""
🚀 الخطوات التالية / Next Steps:
   1. إضافة باقي الحروف العربية (28 حرف)
   2. تحسين خوارزمية استنباط المعنى
   3. إضافة القدرة على توليد كلمات من معانٍ
   4. التكامل مع النموذج اللغوي لـ Bayan
   
📖 للمزيد / For More:
   راجع: docs/LETTER_SEMANTICS_THEORY.md
   See: docs/LETTER_SEMANTICS_THEORY.md
""")


if __name__ == '__main__':
    main()
