import sys
import os
import unittest

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bayan.bayan.arabic_adapter import ArabicNLPAdapter
from bayan.bayan.english_adapter import EnglishNLPAdapter

class TestNLPAdapters(unittest.TestCase):
    def test_arabic_adapter_init(self):
        """Test that Arabic adapter initializes without crashing."""
        adapter = ArabicNLPAdapter()
        self.assertIsNotNone(adapter)
        # Check fallback behavior if libs missing
        print(f"Arabic Adapter Initialized. Analyzer present: {adapter.morphology_analyzer is not None}")

    def test_english_adapter_init(self):
        """Test that English adapter initializes without crashing."""
        adapter = EnglishNLPAdapter()
        self.assertIsNotNone(adapter)
        print(f"English Adapter Initialized. NLP present: {adapter.nlp is not None}")

    def test_arabic_tokenize_fallback(self):
        """Test tokenization (should work even in fallback)."""
        adapter = ArabicNLPAdapter()
        text = "بسم الله الرحمن الرحيم"
        tokens = adapter.tokenize(text)
        self.assertTrue(len(tokens) > 0)
        print(f"Arabic Tokens: {tokens}")

    def test_english_analyze_fallback(self):
        """Test analysis (should work even in fallback)."""
        adapter = EnglishNLPAdapter()
        text = "Hello world"
        analysis = adapter.analyze(text)
        self.assertTrue(len(analysis) > 0)
        print(f"English Analysis: {analysis}")

if __name__ == '__main__':
    unittest.main()
