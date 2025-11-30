"""
Enhanced Letter Semantics System
=================================

Improvements to the letter semantics system:
1. Better meaning inference algorithm
2. Root extraction
3. Morphological pattern analysis
4. Word generation from meanings
"""

from typing import Dict, List, Tuple, Optional, Set
from collections import Counter
import re


class EnhancedLetterSemantics:
    """Enhanced version with better algorithms"""
    
    def __init__(self, database):
        self.db = database
        # Initialize Arabic Adapter for advanced morphology
        try:
            from .arabic_adapter import ArabicNLPAdapter
            self.adapter = ArabicNLPAdapter()
        except ImportError:
            self.adapter = None
            print("Warning: ArabicNLPAdapter not found. Using fallback heuristics.")
        
    def extract_root(self, word: str) -> Optional[str]:
        """
        Extract the root (جذر) from an Arabic word.
        Uses Camel Tools if available, otherwise falls back to heuristics.
        """
        # Try Camel Tools first
        if self.adapter and self.adapter.morphology_analyzer:
            root = self.adapter.extract_root(word)
            if root and root != word:
                return root

        # Fallback Heuristics
        # Remove common prefixes
        prefixes = ['ال', 'و', 'ف', 'ب', 'ك', 'ل']
        temp_word = word
        for prefix in prefixes:
            if temp_word.startswith(prefix):
                temp_word = temp_word[len(prefix):]
        
        # Remove common suffixes
        suffixes = ['ة', 'ه', 'ها', 'هم', 'هن', 'ك', 'كم', 'كن', 'ي', 'نا']
        for suffix in suffixes:
            if temp_word.endswith(suffix):
                temp_word = temp_word[:-len(suffix)]
        
        # Extract consonants (remove vowels)
        consonants = ''.join([c for c in temp_word if c not in 'اوي'])
        
        # Most Arabic roots are 3 letters
        if len(consonants) >= 3:
            return consonants[:3]
        
        return consonants if consonants else None
    
    def analyze_morphological_pattern(self, word: str) -> Dict[str, any]:
        """
        Analyze the morphological pattern (وزن) of a word.
        
        Common patterns:
        - فَعَلَ (fa'ala): basic verb
        - فاعِل (fa'il): active participle
        - مَفعول (maf'ool): passive participle
        - etc.
        """
        root = self.extract_root(word)
        
        if not root or len(root) < 3:
            return {'pattern': 'unknown', 'root': root}
        
        # Map word to pattern using root letters
        pattern_map = {
            root[0]: 'ف',
            root[1]: 'ع',
            root[2]: 'ل',
        }
        
        pattern = ''
        for char in word:
            if char in pattern_map:
                pattern += pattern_map[char]
            else:
                pattern += char
        
        return {
            'pattern': pattern,
            'root': root,
            'word': word,
        }
    
    def infer_meaning_advanced(self, word: str) -> Dict[str, any]:
        """
        Advanced meaning inference using multiple strategies.
        """
        # Strategy 1: Letter-by-letter analysis
        letter_analysis = self.db.analyze_word(word)
        
        # Strategy 2: Root-based analysis
        root = self.extract_root(word)
        root_meanings = []
        if root:
            root_analysis = self.db.analyze_word(root)
            root_meanings = root_analysis.get('combined_sound_meanings', [])
        
        # Strategy 3: Pattern-based analysis
        pattern_info = self.analyze_morphological_pattern(word)
        
        # Strategy 4: Position-weighted analysis
        weighted_meanings = self._weight_by_position(word)
        
        return {
            'word': word,
            'letter_meanings': letter_analysis.get('inferred_meaning', ''),
            'root': root,
            'root_meanings': root_meanings[:5],
            'pattern': pattern_info.get('pattern', 'unknown'),
            'weighted_meanings': weighted_meanings,
            'confidence': self._calculate_confidence(word),
        }
    
    def _weight_by_position(self, word: str) -> List[Tuple[str, float]]:
        """
        Weight letter meanings by their position in the word.
        
        Positions have different importance:
        - First letter: 40% (primary action/quality)
        - Middle letters: 20% each (modifiers)
        - Last letter: 40% (result/outcome)
        """
        if not word:
            return []
        
        meanings_with_weights = []
        
        for i, letter in enumerate(word):
            sem = self.db.get_letter_meanings(letter)
            if not sem:
                continue
            
            # Calculate position weight
            if i == 0:
                weight = 0.4  # First letter
            elif i == len(word) - 1:
                weight = 0.4  # Last letter
            else:
                weight = 0.2 / max(1, len(word) - 2)  # Middle letters
            
            for meaning in sem.combined_meanings:
                meanings_with_weights.append((meaning, weight))
        
        # Sort by weight
        meanings_with_weights.sort(key=lambda x: x[1], reverse=True)
        return meanings_with_weights[:5]
    
    def _calculate_confidence(self, word: str) -> float:
        """
        Calculate confidence in the analysis.
        
        Higher confidence when:
        - All letters are in database
        - Word follows common patterns
        - Root is identifiable
        """
        total_letters = len(word)
        known_letters = sum(1 for c in word if self.db.get_letter_meanings(c))
        
        if total_letters == 0:
            return 0.0
        
        letter_coverage = known_letters / total_letters
        
        # Bonus for having a clear root
        root = self.extract_root(word)
        root_bonus = 0.2 if root and len(root) == 3 else 0.0
        
        confidence = min(1.0, letter_coverage + root_bonus)
        return round(confidence, 2)
    
    def generate_words_from_meaning(self, meaning_keywords: List[str]) -> List[Tuple[str, float]]:
        """
        Generate possible words that express given meanings.
        
        This is the reverse process: meaning → letters → words
        """
        # Find letters that match the meanings
        candidate_letters = []
        
        for letter, sem in self.db.letters.items():
            # Check if any of the letter's meanings match our keywords
            all_meanings = (
                sem.sound.meanings +
                sem.shape.meanings +
                [m.split(' - ')[0] for m in sem.combined_meanings]
            )
            
            score = 0
            for keyword in meaning_keywords:
                for meaning in all_meanings:
                    if keyword in meaning or meaning in keyword:
                        score += 1
            
            if score > 0:
                candidate_letters.append((letter, score))
        
        # Sort by relevance
        candidate_letters.sort(key=lambda x: x[1], reverse=True)
        
        # Generate word combinations (simplified)
        generated_words = []
        
        # Try 2-letter combinations
        for i in range(min(3, len(candidate_letters))):
            for j in range(min(3, len(candidate_letters))):
                if i != j:
                    word = candidate_letters[i][0] + candidate_letters[j][0]
                    score = (candidate_letters[i][1] + candidate_letters[j][1]) / 2
                    generated_words.append((word, score))
        
        # Try 3-letter combinations (roots)
        for i in range(min(3, len(candidate_letters))):
            for j in range(min(3, len(candidate_letters))):
                for k in range(min(3, len(candidate_letters))):
                    if i != j and j != k and i != k:
                        word = (candidate_letters[i][0] + 
                               candidate_letters[j][0] + 
                               candidate_letters[k][0])
                        score = (candidate_letters[i][1] + 
                                candidate_letters[j][1] + 
                                candidate_letters[k][1]) / 3
                        generated_words.append((word, score))
        
        # Sort by score and return top results
        generated_words.sort(key=lambda x: x[1], reverse=True)
        return generated_words[:10]
    
    def find_similar_words(self, word: str, threshold: float = 0.5) -> List[Tuple[str, float]]:
        """
        Find words with similar meanings based on letter semantics.
        """
        word_analysis = self.infer_meaning_advanced(word)
        word_root = word_analysis['root']
        
        # This would require a corpus of words to compare against
        # For now, return words with same root
        if word_root:
            return [(f"كلمة بجذر {word_root}", 1.0)]
        
        return []


# Example usage
if __name__ == '__main__':
    from bayan.bayan.letter_semantics import LetterSemanticsDatabase
    
    db = LetterSemanticsDatabase()
    enhanced = EnhancedLetterSemantics(db)
    
    # Test root extraction
    print("Root extraction:")
    print(f"  والكتاب → {enhanced.extract_root('والكتاب')}")
    print(f"  المعلم → {enhanced.extract_root('المعلم')}")
    
    # Test pattern analysis
    print("\nPattern analysis:")
    print(f"  كتب → {enhanced.analyze_morphological_pattern('كتب')}")
    
    # Test advanced inference
    print("\nAdvanced meaning inference:")
    result = enhanced.infer_meaning_advanced('واو')
    print(f"  Word: {result['word']}")
    print(f"  Confidence: {result['confidence']}")
    print(f"  Weighted meanings: {result['weighted_meanings'][:2]}")
    
    # Test word generation
    print("\nWord generation from meanings:")
    words = enhanced.generate_words_from_meaning(['رفع', 'دوران'])
    print(f"  Generated: {words[:5]}")
