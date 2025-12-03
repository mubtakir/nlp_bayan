#!/usr/bin/env python3
"""
Demo for Unified Letter Semiotics System
Uses the new unified letter_semiotics module
"""
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# استخدام النظام الموحد الجديد
from bayan.bayan.letter_semiotics import (
    ArabicLetterDatabase,
    WordAnalyzer,
    LetterSemanticsDatabase,  # طبقة التوافقية
    EnhancedLetterSemantics   # طبقة التوافقية
)

def main():
    print("=" * 60)
    print("🔬 عرض نظام سيميائية الحروف الموحد")
    print("=" * 60)

    # استخدام النظام الجديد
    db = ArabicLetterDatabase()
    analyzer = WordAnalyzer(use_camel=True)

    print(f"\n📚 قاعدة البيانات: {len(db.letters)} حرف عربي")
    print(f"🔧 Camel Tools: {'متاح' if analyzer.arabic_adapter else 'غير متاح'}")

    words_to_test = ["مدرسة", "مكتبة", "استعمار", "انفجار"]

    print("\n" + "=" * 60)
    print("📖 تحليل الكلمات:")
    print("=" * 60)

    for word in words_to_test:
        print(f"\n🔍 الكلمة: {word}")

        result = analyzer.analyze_word(word)

        # الجذر
        if result.root_analysis:
            print(f"   الجذر: {result.root_analysis.root}")
            print(f"   معنى الجذر: {result.root_analysis.root_meaning}")

        # المعنى المركب
        print(f"   المعنى المركب: {result.combined_meaning}")

        # السلسلة السببية
        print(f"   السلسلة السببية: {' → '.join(result.causal_chain[:3])}")

        # الثقة
        print(f"   الثقة: {result.confidence:.0%}")

        # القوة النفسية والمادية
        print(f"   القوة النفسية: {result.emotional_score:.2f}")
        print(f"   القوة المادية: {result.physical_score:.2f}")

    print("\n" + "=" * 60)
    print("✅ انتهى العرض!")
    print("=" * 60)

if __name__ == "__main__":
    main()
