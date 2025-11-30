#!/usr/bin/env python3
"""
Enhanced Letter Semantics Demo
===============================

Demonstrates advanced features:
- Root extraction
- Morphological pattern analysis
- Position-weighted inference
- Word generation from meanings
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from bayan.bayan.letter_semantics import LetterSemanticsDatabase
from bayan.bayan.enhanced_letter_semantics import EnhancedLetterSemantics


def print_header(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def demo_root_extraction():
    """Demo root extraction from Arabic words"""
    print_header("استخراج الجذر / Root Extraction")
    
    db = LetterSemanticsDatabase()
    enhanced = EnhancedLetterSemantics(db)
    
    test_words = [
        'والكتاب',   # the book (with prefix)
        'المعلم',     # the teacher
        'كتابة',      # writing (with suffix)
        'يكتبون',     # they write
        'مكتوب',      # written
    ]
    
    print("\nأمثلة / Examples:")
    for word in test_words:
        root = enhanced.extract_root(word)
        print(f"  {word:15s} → جذر: {root}")


def demo_pattern_analysis():
    """Demo morphological pattern analysis"""
    print_header("تحليل الأوزان الصرفية / Morphological Pattern Analysis")
    
    db = LetterSemanticsDatabase()
    enhanced = EnhancedLetterSemantics(db)
    
    test_words = [
        'كتب',    # wrote
        'كاتب',   # writer
        'مكتوب',  # written
    ]
    
    print("\nأمثلة / Examples:")
    for word in test_words:
        pattern_info = enhanced.analyze_morphological_pattern(word)
        print(f"\n  كلمة / Word: {word}")
        print(f"  جذر / Root: {pattern_info['root']}")
        print(f"  وزن / Pattern: {pattern_info['pattern']}")


def demo_advanced_inference():
    """Demo advanced meaning inference"""
    print_header("الاستنباط المتقدم للمعاني / Advanced Meaning Inference")
    
    db = LetterSemanticsDatabase()
    enhanced = EnhancedLetterSemantics(db)
    
    test_words = ['واو', 'أي', 'يا']
    
    for word in test_words:
        print(f"\n🔍 تحليل متقدم لكلمة / Advanced analysis of: {word}")
        result = enhanced.infer_meaning_advanced(word)
        
        print(f"\n   الجذر / Root: {result['root']}")
        print(f"   الوزن / Pattern: {result['pattern']}")
        print(f"   الثقة / Confidence: {result['confidence'] * 100}%")
        
        print(f"\n   المعاني المرجحة / Weighted meanings:")
        for meaning, weight in result['weighted_meanings'][:3]:
            print(f"      • {meaning[:50]}... (وزن: {weight:.2f})")
        
        if result['root_meanings']:
            print(f"\n   معاني الجذر / Root meanings:")
            print(f"      {', '.join(result['root_meanings'][:3])}")


def demo_word_generation():
    """Demo word generation from meanings"""
    print_header("توليد الكلمات من المعاني / Word Generation from Meanings")
    
    db = LetterSemanticsDatabase()
    enhanced = EnhancedLetterSemantics(db)
    
    test_meanings = [
        ['رفع', 'علو'],           # elevation, height
        ['دوران', 'وصل'],         # rotation, connection
        ['ألم', 'ضيق'],           # pain, distress
    ]
    
    for meanings in test_meanings:
        print(f"\n💡 المعاني المطلوبة / Desired meanings: {', '.join(meanings)}")
        generated = enhanced.generate_words_from_meaning(meanings)
        
        print(f"   الكلمات المقترحة / Suggested words:")
        for word, score in generated[:5]:
            print(f"      • {word} (درجة: {score:.2f})")


def demo_comparison():
    """Compare basic vs enhanced analysis"""
    print_header("مقارنة: التحليل الأساسي vs المتقدم / Comparison: Basic vs Enhanced")
    
    db = LetterSemanticsDatabase()
    enhanced = EnhancedLetterSemantics(db)
    
    word = 'واو'
    
    print(f"\nالكلمة / Word: {word}\n")
    
    # Basic analysis
    print("📊 التحليل الأساسي / Basic Analysis:")
    basic = db.analyze_word(word)
    print(f"   {basic['inferred_meaning'][:100]}...")
    
    # Enhanced analysis
    print("\n🚀 التحليل المتقدم / Enhanced Analysis:")
    advanced = enhanced.infer_meaning_advanced(word)
    print(f"   الثقة / Confidence: {advanced['confidence'] * 100}%")
    print(f"   الجذر / Root: {advanced['root']}")
    print(f"   الوزن / Pattern: {advanced['pattern']}")
    print(f"   أهم المعاني / Top meanings:")
    for meaning, weight in advanced['weighted_meanings'][:2]:
        print(f"      • {meaning[:60]}... ({weight:.2f})")


def main():
    """Run all demos"""
    print("\n" + "=" * 70)
    print("نظام الدلالة الصوتية والشكلية المتقدم")
    print("Enhanced Phonetic-Semantic System")
    print("=" * 70)
    
    demo_root_extraction()
    input("\nاضغط Enter للمتابعة / Press Enter to continue...")
    
    demo_pattern_analysis()
    input("\nاضغط Enter للمتابعة / Press Enter to continue...")
    
    demo_advanced_inference()
    input("\nاضغط Enter للمتابعة / Press Enter to continue...")
    
    demo_word_generation()
    input("\nاضغط Enter للمتابعة / Press Enter to continue...")
    
    demo_comparison()
    
    print("\n" + "=" * 70)
    print("✅ العرض التوضيحي اكتمل / Demo Complete")
    print("=" * 70)
    
    print("""
🎯 الميزات الجديدة / New Features:
   ✓ استخراج الجذر / Root extraction
   ✓ تحليل الأوزان الصرفية / Morphological patterns
   ✓ استنباط مرجح بالموقع / Position-weighted inference
   ✓ توليد كلمات من معانٍ / Word generation from meanings
   ✓ درجة الثقة / Confidence scoring

📝 الخطوة التالية / Next Step:
   نحتاج معاني الحروف الساكنة (25 حرف) من الباحث
   We need consonant meanings (25 letters) from the researcher
   
   راجع: docs/LETTER_MEANINGS_REQUEST.md
   See: docs/LETTER_MEANINGS_REQUEST.md
""")


if __name__ == '__main__':
    main()
