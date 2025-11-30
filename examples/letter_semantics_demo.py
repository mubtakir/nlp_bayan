#!/usr/bin/env python3
"""
Demo for Enhanced Letter Semantics with Camel Tools Integration
"""
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bayan.bayan.letter_semantics import LetterSemanticsDatabase
from bayan.bayan.enhanced_letter_semantics import EnhancedLetterSemantics

def main():
    print("Initializing Letter Semantics Database...")
    db = LetterSemanticsDatabase()
    enhanced = EnhancedLetterSemantics(db)
    
    words_to_test = ["مدرسة", "مكتبة", "استعمار", "انفجار"]
    
    print("\nTesting Root Extraction and Meaning Inference:")
    print("==============================================")
    
    for word in words_to_test:
        print(f"\nAnalyzing word: {word}")
        
        # 1. Extract Root
        root = enhanced.extract_root(word)
        print(f"  Extracted Root: {root}")
        
        # 2. Infer Meaning
        analysis = enhanced.infer_meaning_advanced(word)
        print(f"  Inferred Meaning (from letters): {analysis['letter_meanings']}")
        
        if analysis['root_meanings']:
            print(f"  Root Meanings: {analysis['root_meanings']}")
            
        print(f"  Confidence: {analysis['confidence']}")

if __name__ == "__main__":
    main()
