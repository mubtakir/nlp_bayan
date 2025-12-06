#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبار سريع للنظام المعجمي الموحد
Quick Test for Unified Lexicon System
"""

import sys
import os

# إضافة مسار المشروع
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bayan.bayan.complete_vocabulary import get_complete_vocabulary

def test_foundation_vocabulary():
    """اختبار القاموس الأساسي"""
    print("\n" + "="*70)
    print("  🧪 اختبار القاموس الأساسي الكامل")
    print("="*70)
    
    vocab = get_complete_vocabulary()
    
    # عرض الإحصائيات
    vocab.print_statistics()
    
    # عرض أمثلة
    vocab.show_examples()
    
    # اختبار البحث
    print("\n🔍 اختبار البحث:")
    test_words = ["أرض", "سماء", "أكل", "شمس", "ليل"]
    
    for word in test_words:
        result = vocab.get_word(word)
        if result:
            print(f"\n   ✅ {word}:")
            print(f"      النوع: {result.word_type.value}")
            print(f"      الفئة: {result.category.value}")
            print(f"      المعنى: {result.core_meaning}")
        else:
            print(f"   ❌ {word}: غير موجودة")
    
    # اختبار البحث بالمعنى
    print("\n🔎 البحث بالمعنى 'ماء':")
    results = vocab.search_by_meaning('ماء')
    for word in results[:5]:
        print(f"   • {word.arabic}: {word.core_meaning}")
    
    print("\n✅ انتهى الاختبار بنجاح!")

if __name__ == "__main__":
    try:
        test_foundation_vocabulary()
    except Exception as e:
        print(f"\n❌ خطأ: {e}")
        import traceback
        traceback.print_exc()
