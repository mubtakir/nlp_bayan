#!/usr/bin/env python3
"""
Comprehensive Arabic Morphology Verification Demo
Tests all conjugation capabilities including dual and imperative
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bayan.bayan.arabic_adapter import ArabicNLPAdapter

def main():
    print("=" * 70)
    print("Arabic Morphology Comprehensive Test")
    print("=" * 70)
    
    adapter = ArabicNLPAdapter()
    
    # Test verb: كتب (to write)
    lemma = "كتب"
    
    print(f"\n📝 Testing verb: {lemma}")
    print("-" * 70)
    
    # Test Past Tense (all persons, including dual)
    print("\n1️⃣  PAST TENSE (الماضي)")
    print("-" * 40)
    test_cases_past = [
        ("3ms", "هو"),
        ("3fs", "هي"),
        ("3md", "هما (مذكر)"),
        ("3fd", "هما (مؤنث)"),
        ("3mp", "هم"),
        ("3fp", "هن"),
        ("2ms", "أنتَ"),
        ("2fs", "أنتِ"),
        ("2md", "أنتما"),
        ("2mp", "أنتم"),
        ("2fp", "أنتن"),
        ("1s", "أنا"),
        ("1p", "نحن"),
    ]
    
    for pgn, pronoun in test_cases_past:
        result = adapter.conjugate_verb(lemma, "past", pgn)
        print(f"  {pronoun:15} ({pgn}): {result}")
    
    # Test Present Tense (including dual)
    print("\n2️⃣  PRESENT TENSE (المضارع)")
    print("-" * 40)
    test_cases_present = [
        ("3ms", "هو"),
        ("3fs", "هي"),
        ("3md", "هما (مذكر)"),
        ("3fd", "هما (مؤنث)"),
        ("3mp", "هم"),
        ("3fp", "هن"),
        ("2ms", "أنتَ"),
        ("2fs", "أنتِ"),
        ("2md", "أنتما"),
        ("2mp", "أنتم"),
        ("2fp", "أنتن"),
        ("1s", "أنا"),
        ("1p", "نحن"),
    ]
    
    for pgn, pronoun in test_cases_present:
        result = adapter.conjugate_verb(lemma, "present", pgn)
        print(f"  {pronoun:15} ({pgn}): {result}")
    
    # Test Imperative (الأمر) - only 2nd person
    print("\n3️⃣  IMPERATIVE (الأمر)")
    print("-" * 40)
    test_cases_imperative = [
        ("2ms", "أنتَ"),
        ("2fs", "أنتِ"),
        ("2md", "أنتما"),
        ("2mp", "أنتم"),
        ("2fp", "أنتن"),
    ]
    
    for pgn, pronoun in test_cases_imperative:
        result = adapter.conjugate_verb(lemma, "imperative", pgn)
        print(f"  {pronoun:15} ({pgn}): {result}")
    
    # Test Future
    print("\n4️⃣  FUTURE (المستقبل)")
    print("-" * 40)
    result_future = adapter.conjugate_verb(lemma, "future", "3ms")
    print(f"  هو (3ms): {result_future}")
    
    # Test Root Extraction
    print("\n5️⃣  ROOT EXTRACTION (استخراج الجذر)")
    print("-" * 40)
    test_words = ["مدرسة", "مكتبة", "كاتب", "مكتوب", "استعمار"]
    for word in test_words:
        root = adapter.extract_root(word)
        print(f"  {word:15} → {root}")
    
    print("\n" + "=" * 70)
    print("✅ Test Complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()
