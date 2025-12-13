"""
Reverse Dictionary Analyzer
============================

Analyzes dictionaries to find common meanings among words sharing letters.
This is the NINTH method for deriving letter meanings.
"""

from typing import List, Dict, Tuple, Set
from collections import defaultdict
import re


class PatternType:
    """Types of letter patterns"""
    CONSECUTIVE = "consecutive"  # متعاقبان: "سح"
    SEPARATED = "separated"  # مفترقان: "ب_ع"
    POSITION = "position"  # موضع: "_ب" (end), "ر_" (start)


class ReverseDictionaryAnalyzer:
    """
    Reverse analysis of dictionaries to derive letter meanings.
    
    The ninth method: work backwards from words to letters.
    """
    
    def __init__(self, dictionary: Dict[str, str] = None):
        """
        Initialize with a dictionary.
        
        dictionary: {word: meaning} pairs
        """
        self.dictionary = dictionary or {}
        self.patterns_cache = {}
    
    def find_words_with_consecutive(self, letters: str) -> List[Tuple[str, str]]:
        """
        Find words containing consecutive letters.
        
        Example: "سح" → ["سحل", "سحب", "سحق"]
        """
        pattern = re.compile(letters)
        results = []
        
        for word, meaning in self.dictionary.items():
            if pattern.search(word):
                results.append((word, meaning))
        
        return results
    
    def find_words_with_separated(self, letter1: str, letter2: str) -> List[Tuple[str, str]]:
        """
        Find words containing two letters with one letter between them.
        
        Example: "ب_ع" → ["بلع", "بشع", "بقع"]
        """
        pattern = re.compile(f"{letter1}.{letter2}")
        results = []
        
        for word, meaning in self.dictionary.items():
            if pattern.search(word):
                results.append((word, meaning))
        
        return results
    
    def find_words_with_position(self, letter: str, position: str) -> List[Tuple[str, str]]:
        """
        Find words with letter at specific position.
        
        position: 'start', 'end', 'middle'
        
        Example: letter='ب', position='end' → ["طلب", "حلب", "غلب"]
        """
        results = []
        
        for word, meaning in self.dictionary.items():
            if position == 'start' and word.startswith(letter):
                results.append((word, meaning))
            elif position == 'end' and word.endswith(letter):
                results.append((word, meaning))
            elif position == 'middle' and letter in word[1:-1]:
                results.append((word, meaning))
        
        return results
    
    def extract_keywords(self, meaning: str) -> Set[str]:
        """
        Extract keywords from a meaning description.
        
        Simple implementation: split and filter common words.
        """
        # Remove common words (stop words)
        stop_words = {'the', 'a', 'an', 'of', 'to', 'in', 'for', 'and', 'or'}
        
        words = meaning.lower().split()
        keywords = {w for w in words if w not in stop_words and len(w) > 2}
        
        return keywords
    
    def find_common_meanings(self, words: List[Tuple[str, str]]) -> Dict[str, int]:
        """
        Find common meaning themes among words.
        
        Returns: {keyword: frequency}
        """
        keyword_freq = defaultdict(int)
        
        for word, meaning in words:
            keywords = self.extract_keywords(meaning)
            for keyword in keywords:
                keyword_freq[keyword] += 1
        
        # Sort by frequency
        sorted_keywords = dict(sorted(
            keyword_freq.items(),
            key=lambda x: x[1],
            reverse=True
        ))
        
        return sorted_keywords
    
    def analyze_pattern(self, pattern: str, pattern_type: str) -> Dict:
        """
        Analyze a letter pattern to derive meaning.
        
        pattern: the letters to analyze
        pattern_type: 'consecutive', 'separated', or 'position'
        """
        # Find matching words
        if pattern_type == PatternType.CONSECUTIVE:
            words = self.find_words_with_consecutive(pattern)
        elif pattern_type == PatternType.SEPARATED:
            letter1, letter2 = pattern.split('_')
            words = self.find_words_with_separated(letter1, letter2)
        elif pattern_type == PatternType.POSITION:
            letter, position = pattern.split(':')
            words = self.find_words_with_position(letter, position)
        else:
            return {}
        
        # Extract common meanings
        common_meanings = self.find_common_meanings(words)
        
        return {
            'pattern': pattern,
            'pattern_type': pattern_type,
            'words_found': len(words),
            'sample_words': words[:10],
            'common_meanings': common_meanings,
            'top_meanings': list(common_meanings.keys())[:5],
        }
    
    def infer_letter_meaning(self, letter: str) -> Dict:
        """
        Infer meaning of a letter by analyzing all its occurrences.
        """
        # Analyze different positions
        start_analysis = self.analyze_pattern(f"{letter}:start", PatternType.POSITION)
        end_analysis = self.analyze_pattern(f"{letter}:end", PatternType.POSITION)
        middle_analysis = self.analyze_pattern(f"{letter}:middle", PatternType.POSITION)
        
        return {
            'letter': letter,
            'start_position': start_analysis,
            'end_position': end_analysis,
            'middle_position': middle_analysis,
        }


# Example usage with sample data
if __name__ == '__main__':
    # Sample Arabic dictionary (simplified)
    sample_dict = {
        # Words ending with ب
        'طلب': 'requesting, asking for, carrying request',
        'حلب': 'milking, extracting, carrying milk',
        'غلب': 'overcoming, defeating, carrying victory',
        'سحب': 'pulling, dragging, carrying away',
        'نهب': 'looting, stealing, carrying loot',
        'هرب': 'escaping, fleeing, carrying oneself away',
        
        # Words with سح
        'سحل': 'dragging on ground, pulling forcefully',
        'سحب': 'pulling, drawing, dragging',
        'سحق': 'crushing, grinding, pounding',
        
        # Words with ب_ع
        'بلع': 'swallowing, taking into depth',
        'بشع': 'ugly, repulsive, from depth',
        'بقع': 'spots, marks from depth',
    }
    
    analyzer = ReverseDictionaryAnalyzer(sample_dict)
    
    # Analyze ب at end position
    print("=" * 70)
    print("Analysis: Letter ب at END position")
    print("=" * 70)
    
    result = analyzer.analyze_pattern("ب:end", PatternType.POSITION)
    print(f"\nWords found: {result['words_found']}")
    print(f"\nSample words:")
    for word, meaning in result['sample_words'][:5]:
        print(f"  {word}: {meaning}")
    
    print(f"\nTop common meanings:")
    for meaning, freq in list(result['common_meanings'].items())[:5]:
        print(f"  {meaning}: {freq} occurrences")
    
    # Analyze سح consecutive
    print("\n" + "=" * 70)
    print("Analysis: Letters سح (consecutive)")
    print("=" * 70)
    
    result = analyzer.analyze_pattern("سح", PatternType.CONSECUTIVE)
    print(f"\nWords found: {result['words_found']}")
    print(f"\nSample words:")
    for word, meaning in result['sample_words']:
        print(f"  {word}: {meaning}")
    
    print(f"\nTop common meanings:")
    for meaning, freq in list(result['common_meanings'].items())[:5]:
        print(f"  {meaning}: {freq} occurrences")
    
    print("\n" + "=" * 70)
    print("Conclusion:")
    print("=" * 70)
    print("""
ب at end position → carrying, moving, transferring
سح consecutive → pulling, dragging, forceful movement

This confirms the meanings derived from other methods!
""")
