#!/usr/bin/env python3
"""
Advanced Letter Semantics Demo
===============================

Demonstrates the three core principles:
1. Logical interconnection (causal chains)
2. Opposites (measurement scales)
3. Multi-faceted symbolism
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from bayan.bayan.advanced_letter_semantics import AdvancedLetterDatabase


def print_header(title, char='='):
    print(f"\n{char * 70}")
    print(title)
    print(f"{char * 70}\n")


def demo_letter_ba():
    """Demonstrate complete analysis of letter Ba"""
    print_header("حرف الباء (ب) - تحليل كامل / Letter Ba - Complete Analysis")
    
    db = AdvancedLetterDatabase()
    ba = db.get_letter('ب')
    
    if not ba:
        print("Letter Ba not found!")
        return
    
    print(f"📝 الحرف / Letter: {ba.letter}\n")
    
    # Basic meanings
    print("🔤 المعاني الأساسية / Basic Meanings:")
    for meaning in ba.basic_meanings:
        print(f"   • {meaning}")
    
    # Causal chains
    print(f"\n🔗 السلاسل السببية / Causal Chains:")
    for i, chain in enumerate(ba.causal_chains, 1):
        print(f"   {i}. {chain}")
        print(f"      {chain.description}")
        for rel in chain.chain:
            print(f"      → {rel.from_meaning} {rel.relationship_type.value} {rel.to_meaning}")
            print(f"        ({rel.explanation})")
    
    # Opposites
    print(f"\n⚖️  الأضداد / Opposites (المعيار / Scale):")
    for opp in ba.opposites:
        print(f"   • البُعد / Dimension: {opp.dimension}")
        print(f"     {opp.meaning1} ⟷ {opp.meaning2}")
        print(f"     أمثلة / Examples:")
        for w1, w2 in opp.examples:
            print(f"       {w1} ⟷ {w2}")
    
    # Symbolic representations
    print(f"\n🎭 التمثيلات الرمزية / Symbolic Representations:")
    for sym in ba.symbolic_representations:
        print(f"   • يرمز لـ / Symbolizes: {sym.symbol_for}")
        print(f"     السبب / Reason: {sym.reason}")
        print(f"     السياق / Context: {sym.context}")
        print(f"     أمثلة / Examples: {', '.join(sym.examples)}")
    
    # Example words
    print(f"\n📚 كلمات أمثلة / Example Words:")
    for word, explanation in ba.example_words.items():
        print(f"   • {word}: {explanation}")


def demo_causal_chains():
    """Demonstrate causal chain analysis"""
    print_header("تحليل السلاسل السببية / Causal Chain Analysis", '-')
    
    db = AdvancedLetterDatabase()
    ba = db.get_letter('ب')
    
    if not ba:
        return
    
    print("🔍 البحث عن مسار سببي / Finding causal path:\n")
    
    # Find path from "الحمل" to "التشبع"
    path = ba.find_causal_path('الحمل', 'التشبع')
    if path:
        print(f"   من 'الحمل' إلى 'التشبع':")
        print(f"   {' → '.join(path)}")
        print(f"\n   التفسير / Explanation:")
        print(f"   الحمل (carrying) يؤدي إلى الدك (pounding)")
        print(f"   الدك (pounding) يسبب التشبع (saturation)")
    
    # Find path from "الحمل" to "البناء"
    path2 = ba.find_causal_path('الحمل', 'البناء')
    if path2:
        print(f"\n   من 'الحمل' إلى 'البناء':")
        print(f"   {' → '.join(path2)}")
        print(f"\n   التفسير / Explanation:")
        print(f"   البناء (building) يتطلب الحمل (carrying)")


def demo_opposites():
    """Demonstrate opposites analysis"""
    print_header("تحليل الأضداد / Opposites Analysis", '-')
    
    db = AdvancedLetterDatabase()
    ba = db.get_letter('ب')
    
    if not ba:
        return
    
    print("⚖️  الباء كمعيار / Ba as a Measurement Scale:\n")
    
    test_meanings = ['سريع', 'بناء', 'حركة']
    
    for meaning in test_meanings:
        opposite_info = ba.get_opposite(meaning)
        if opposite_info:
            opposite, dimension = opposite_info
            print(f"   {meaning} ⟷ {opposite}")
            print(f"   البُعد / Dimension: {dimension}")
            print(f"   الباء يحدد هذا البُعد، الحروف الأخرى تحدد الاتجاه\n")


def demo_word_analysis():
    """Demonstrate word analysis using advanced semantics"""
    print_header("تحليل الكلمات / Word Analysis", '-')
    
    db = AdvancedLetterDatabase()
    
    test_words = ['بلع', 'بناء', 'برق']
    
    for word in test_words:
        print(f"🔍 تحليل كلمة / Analyzing: {word}\n")
        
        ba = db.get_letter('ب')
        if ba and word in ba.example_words:
            print(f"   التفسير / Explanation:")
            print(f"   {ba.example_words[word]}\n")
        
        # Advanced analysis
        analysis = db.analyze_word_advanced(word)
        if analysis['causal_chains']:
            print(f"   السلاسل السببية المستخدمة / Causal chains used:")
            for chain in analysis['causal_chains'][:2]:
                print(f"   • {chain}")
        
        print()


def main():
    """Run all demos"""
    print("\n" + "=" * 70)
    print("نظام الدلالة الصوتية المتقدم - المبادئ الثلاثة")
    print("Advanced Phonetic-Semantic System - Three Core Principles")
    print("=" * 70)
    
    print("""
المبادئ الثلاثة / Three Principles:
1️⃣  الترابط المنطقي - معاني الحرف مترابطة في سلاسل سببية
   Logical Interconnection - meanings form causal chains

2️⃣  الحرف يحمل المعنى وضده - الحرف كمعيار (وزن، طول، سرعة...)
   Opposites - letter as measurement scale (weight, length, speed...)

3️⃣  الحرف رمز متعدد الأوجه - يرمز لأشياء مختلفة حسب السياق
   Multi-faceted Symbol - symbolizes different things by context
""")
    
    input("اضغط Enter للمتابعة / Press Enter to continue...")
    
    demo_letter_ba()
    input("\nاضغط Enter للمتابعة / Press Enter to continue...")
    
    demo_causal_chains()
    input("\nاضغط Enter للمتابعة / Press Enter to continue...")
    
    demo_opposites()
    input("\nاضغط Enter للمتابعة / Press Enter to continue...")
    
    demo_word_analysis()
    
    print_header("✅ العرض التوضيحي اكتمل / Demo Complete")
    
    print("""
🎯 ما تم إنجازه / What Was Accomplished:

✅ تنفيذ المبادئ الثلاثة الأساسية
   Implemented three core principles

✅ حرف الباء (ب) كامل مع:
   Complete letter Ba (ب) with:
   • 5 معانٍ أساسية / basic meanings
   • 2 سلاسل سببية / causal chains
   • 5 أزواج أضداد / opposites pairs
   • 2 تمثيلات رمزية / symbolic representations
   • 10 كلمات أمثلة / example words

✅ خوارزميات متقدمة:
   Advanced algorithms:
   • البحث في السلاسل السببية / Causal path finding
   • إيجاد الأضداد / Finding opposites
   • تحليل الكلمات / Word analysis

📚 للمزيد / For More:
   docs/ADVANCED_LETTER_PRINCIPLES.md
""")


if __name__ == '__main__':
    main()
