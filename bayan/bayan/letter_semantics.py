"""
Letter Semantics System for Bayan
==================================

A revolutionary approach to understanding language through the inherent
meanings of letters based on their sound and shape.

Based on 40 years of research into the phonetic and visual semantics of letters.
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class LetterType(Enum):
    """Types of letters"""
    VOWEL = "vowel"
    CONSONANT = "consonant"
    SEMI_VOWEL = "semi_vowel"


@dataclass
class SoundSemantics:
    """Semantic meanings derived from sound"""
    phoneme: str
    baby_cry_meaning: Optional[str]
    sound_qualities: List[str]
    meanings: List[str]


@dataclass
class ShapeSemantics:
    """Semantic meanings derived from visual shape"""
    arabic_shape: str
    latin_shape: Optional[str]
    visual_qualities: List[str]
    meanings: List[str]


@dataclass
class LetterSemantics:
    """Complete semantics of a letter"""
    letter: str
    letter_type: LetterType
    sound: SoundSemantics
    shape: ShapeSemantics
    combined_meanings: List[str]
    examples: List[Tuple[str, str]]  # (word, explanation)


class LetterSemanticsDatabase:
    """
    Database of letter meanings based on phonetic and visual analysis.
    
    This implements the theory that letters carry meaning through:
    1. Their sound (phonetic semantics)
    2. Their shape (visual semantics)
    
    The meaning of a word emerges from the combination of its letters' meanings.
    """
    
    def __init__(self):
        self.letters: Dict[str, LetterSemantics] = {}
        self._initialize_vowels()
    
    def _initialize_vowels(self):
        """Initialize the three Arabic vowels with their core meanings"""
        
        # Alif (ا / A) - Elevation and Rising
        self.letters['ا'] = LetterSemantics(
            letter='ا',
            letter_type=LetterType.VOWEL,
            sound=SoundSemantics(
                phoneme='aa',
                baby_cry_meaning='seeking_elevation_and_care',
                sound_qualities=['long', 'open', 'rising'],
                meanings=[
                    'رفع',      # elevation
                    'علو',      # height
                    'طلب',      # request
                    'حنان',     # tenderness
                    'رعاية',    # care
                ]
            ),
            shape=ShapeSemantics(
                arabic_shape='vertical_line',
                latin_shape='mountain_peak',
                visual_qualities=['straight', 'vertical', 'ascending'],
                meanings=[
                    'استقامة',   # straightness
                    'ارتفاع',    # rising
                    'أساس',      # foundation
                    'بداية',     # beginning
                ]
            ),
            combined_meanings=[
                'الرفع والعلو - elevation and height',
                'الطلب والاحتياج - request and need',
                'الامتداد والاستقامة - extension and straightness',
                'الأساس والبداية - foundation and beginning',
            ],
            examples=[
                ('أب', 'father - the elevated one, the pillar'),
                ('أعلى', 'highest - ultimate elevation'),
                ('أول', 'first - the beginning'),
            ]
        )
        
        # Waw (و / O) - Rotation and Connection
        self.letters['و'] = LetterSemantics(
            letter='و',
            letter_type=LetterType.VOWEL,
            sound=SoundSemantics(
                phoneme='oo',
                baby_cry_meaning='seeking_proximity_and_joining',
                sound_qualities=['rounded', 'continuous', 'flowing'],
                meanings=[
                    'لحاق',     # following
                    'مجاورة',   # proximity
                    'وصل',      # connection
                    'ذهاب',     # going
                ]
            ),
            shape=ShapeSemantics(
                arabic_shape='circle',
                latin_shape='complete_circle',
                visual_qualities=['round', 'rolling', 'containing'],
                meanings=[
                    'دوران',    # rotation
                    'احتواء',   # containment
                    'تدحرج',    # rolling
                    'إحاطة',    # surrounding
                ]
            ),
            combined_meanings=[
                'الدوران والحركة الدائرية - rotation and circular motion',
                'الاحتواء والإحاطة - containment and surrounding',
                'المجاورة والقرب - proximity and nearness',
                'الاتصال والوصل - connection and joining',
            ],
            examples=[
                ('وصل', 'connected - joining together'),
                ('دوران', 'rotation - circular motion'),
                ('واو', 'wow - exclamation of connection to something high'),
            ]
        )
        
        # Ya (ي / I) - Pain and Narrowness
        self.letters['ي'] = LetterSemantics(
            letter='ي',
            letter_type=LetterType.VOWEL,
            sound=SoundSemantics(
                phoneme='ee',
                baby_cry_meaning='expressing_pain_and_distress',
                sound_qualities=['high', 'sharp', 'piercing'],
                meanings=[
                    'ألم',      # pain
                    'ضيق',      # distress
                    'حزن',      # sadness
                    'معاناة',   # suffering
                ]
            ),
            shape=ShapeSemantics(
                arabic_shape='curved_line',
                latin_shape='thin_vertical',
                visual_qualities=['curved', 'twisting', 'narrow'],
                meanings=[
                    'تلوي',     # twisting
                    'انحناء',   # bending
                    'دقة',      # precision
                    'نحافة',    # thinness
                ]
            ),
            combined_meanings=[
                'الألم والضيق - pain and distress',
                'التلوي والانحناء - twisting and bending',
                'الدقة والنحافة - precision and thinness',
                'الاتجاه والإشارة - direction and pointing',
            ],
            examples=[
                ('أي', 'which - pointing/indicating'),
                ('يد', 'hand - the pointing limb'),
                ('بكى', 'cried - expressing pain'),
            ]
        )
    
    def add_letter(self, semantics: LetterSemantics):
        """Add a letter's semantics to the database"""
        self.letters[semantics.letter] = semantics
    
    def get_letter_meanings(self, letter: str) -> Optional[LetterSemantics]:
        """Get the semantic meanings of a letter"""
        return self.letters.get(letter)
    
    def analyze_word(self, word: str) -> Dict[str, any]:
        """
        Analyze a word by combining the meanings of its letters.
        
        Returns:
            Dictionary with:
            - letters: list of letter semantics
            - combined_sound_meanings: meanings from sounds
            - combined_shape_meanings: meanings from shapes
            - inferred_meaning: best guess at word meaning
        """
        letters_analysis = []
        sound_meanings = []
        shape_meanings = []
        
        for letter in word:
            sem = self.get_letter_meanings(letter)
            if sem:
                letters_analysis.append(sem)
                sound_meanings.extend(sem.sound.meanings)
                shape_meanings.extend(sem.shape.meanings)
        
        return {
            'word': word,
            'letters': letters_analysis,
            'combined_sound_meanings': sound_meanings,
            'combined_shape_meanings': shape_meanings,
            'inferred_meaning': self._infer_meaning(letters_analysis),
        }
    
    def _infer_meaning(self, letters: List[LetterSemantics]) -> str:
        """
        Infer the meaning of a word from its letters.
        
        This is a simplified version. A full implementation would use
        more sophisticated combination rules.
        """
        if not letters:
            return "unknown"
        
        # Combine meanings with weights
        # First letter often carries primary meaning
        # Last letter often carries result/outcome
        # Middle letters modify
        
        meanings = []
        for i, letter in enumerate(letters):
            weight = 1.0
            if i == 0:
                weight = 1.5  # First letter more important
            elif i == len(letters) - 1:
                weight = 1.2  # Last letter somewhat important
            
            for meaning in letter.combined_meanings:
                meanings.append((meaning, weight))
        
        # Sort by weight and return top meanings
        meanings.sort(key=lambda x: x[1], reverse=True)
        return " + ".join([m[0] for m in meanings[:3]])
    
    def generate_word_from_meaning(self, meaning_description: str) -> List[str]:
        """
        Generate possible words that could express a given meaning.
        
        This is the reverse process: from meaning to letters to words.
        """
        # This is a placeholder for future implementation
        # Would need sophisticated mapping from meanings to letters
        return []
    
    def get_statistics(self) -> Dict[str, any]:
        """Get statistics about the database"""
        return {
            'total_letters': len(self.letters),
            'vowels': sum(1 for l in self.letters.values() if l.letter_type == LetterType.VOWEL),
            'consonants': sum(1 for l in self.letters.values() if l.letter_type == LetterType.CONSONANT),
        }


# Example usage
if __name__ == '__main__':
    db = LetterSemanticsDatabase()
    
    # Analyze a word
    analysis = db.analyze_word('واو')
    print(f"Word: {analysis['word']}")
    print(f"Inferred meaning: {analysis['inferred_meaning']}")
    
    # Get statistics
    stats = db.get_statistics()
    print(f"\nDatabase statistics: {stats}")
