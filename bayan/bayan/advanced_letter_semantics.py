"""
Advanced Letter Semantics - Enhanced Data Structures
====================================================

Implements the three core principles:
1. Logical interconnection of meanings (causal chains)
2. Letters carry opposites (measurement scales)
3. Multi-faceted symbolic representation
"""

from typing import List, Tuple, Optional, Dict
from dataclasses import dataclass, field
from enum import Enum


class RelationshipType(Enum):
    """Types of relationships between meanings"""
    CAUSES = "causes"  # A causes B
    REQUIRES = "requires"  # A requires B
    LEADS_TO = "leads_to"  # A leads to B
    ACCOMPANIES = "accompanies"  # A accompanies B
    ENABLES = "enables"  # A enables B


@dataclass
class MeaningRelationship:
    """
    Relationship between two meanings.
    
    Example: "الحمل" (carrying) LEADS_TO "الدك" (pounding)
    """
    from_meaning: str
    to_meaning: str
    relationship_type: RelationshipType
    strength: float  # 0.0 to 1.0
    explanation: str = ""


@dataclass
class CausalChain:
    """
    A chain of causally related meanings.
    
    Example: الحمل → الدك → التشبع
    (carrying → pounding → saturation)
    """
    chain: List[MeaningRelationship]
    description: str = ""
    
    def get_meanings_sequence(self) -> List[str]:
        """Get the sequence of meanings in the chain"""
        if not self.chain:
            return []
        
        sequence = [self.chain[0].from_meaning]
        for rel in self.chain:
            sequence.append(rel.to_meaning)
        return sequence
    
    def __str__(self):
        meanings = self.get_meanings_sequence()
        return " → ".join(meanings)


@dataclass
class OppositesPair:
    """
    A pair of opposite meanings on the same dimension.
    
    The letter acts as a SCALE/MEASURE for this dimension.
    Example: برق (fast) ⟷ بطؤ (slow) on the "speed" dimension
    """
    meaning1: str
    meaning2: str
    dimension: str  # 'speed', 'weight', 'size', 'value', etc.
    examples: List[Tuple[str, str]] = field(default_factory=list)  # (word1, word2)
    explanation: str = ""


@dataclass
class SymbolicRepresentation:
    """
    A symbolic representation of the letter.
    
    The letter can symbolize different things based on shape/function.
    Example: ص (oval shape) can represent eye, ear, mouth
    """
    symbol_for: str  # what it symbolizes
    reason: str  # why (shape, function, etc.)
    context: str  # when this symbolism applies
    examples: List[str] = field(default_factory=list)


@dataclass
class AdvancedLetterSemantics:
    """
    Complete advanced semantics of a letter.
    
    Includes:
    - Basic meanings
    - Causal chains (how meanings relate)
    - Opposites (measurement dimensions)
    - Symbolic representations
    """
    letter: str
    basic_meanings: List[str]
    
    # Principle 1: Logical interconnection
    causal_chains: List[CausalChain] = field(default_factory=list)
    
    # Principle 2: Opposites
    opposites: List[OppositesPair] = field(default_factory=list)
    
    # Principle 3: Multi-faceted symbolism
    symbolic_representations: List[SymbolicRepresentation] = field(default_factory=list)
    
    # Examples
    example_words: Dict[str, str] = field(default_factory=dict)  # word: explanation
    
    def get_all_meanings(self) -> List[str]:
        """Get all meanings including those in chains"""
        meanings = set(self.basic_meanings)
        
        for chain in self.causal_chains:
            meanings.update(chain.get_meanings_sequence())
        
        for opp in self.opposites:
            meanings.add(opp.meaning1)
            meanings.add(opp.meaning2)
        
        return list(meanings)
    
    def find_causal_path(self, from_meaning: str, to_meaning: str) -> Optional[List[str]]:
        """Find causal path between two meanings"""
        for chain in self.causal_chains:
            sequence = chain.get_meanings_sequence()
            if from_meaning in sequence and to_meaning in sequence:
                from_idx = sequence.index(from_meaning)
                to_idx = sequence.index(to_meaning)
                if from_idx < to_idx:
                    return sequence[from_idx:to_idx+1]
        return None
    
    def get_opposite(self, meaning: str) -> Optional[Tuple[str, str]]:
        """Get the opposite of a meaning and the dimension"""
        for opp in self.opposites:
            if opp.meaning1 == meaning:
                return (opp.meaning2, opp.dimension)
            elif opp.meaning2 == meaning:
                return (opp.meaning1, opp.dimension)
        return None


class AdvancedLetterDatabase:
    """Database with advanced letter semantics"""
    
    def __init__(self):
        self.letters: Dict[str, AdvancedLetterSemantics] = {}
        self._initialize_ba()
    
    def _initialize_ba(self):
        """Initialize letter Ba (ب) with full advanced semantics"""
        
        # Create causal chains
        chain1 = CausalChain(
            chain=[
                MeaningRelationship(
                    'الحمل', 'الدك', 
                    RelationshipType.LEADS_TO, 
                    0.9,
                    'الحمل يؤدي إلى الدك في المكان'
                ),
                MeaningRelationship(
                    'الدك', 'التشبع',
                    RelationshipType.CAUSES,
                    0.8,
                    'الدك يسبب التشبع والامتلاء'
                ),
            ],
            description='سلسلة الحمل والدك والتشبع'
        )
        
        chain2 = CausalChain(
            chain=[
                MeaningRelationship(
                    'الحمل', 'البناء',
                    RelationshipType.REQUIRES,
                    0.7,
                    'البناء يتطلب حمل المواد'
                ),
            ],
            description='البناء يتطلب الحمل'
        )
        
        # Create opposites
        opposites = [
            OppositesPair(
                'سريع', 'بطيء',
                'speed',
                [('برق', 'بطؤ')],
                'الباء يحدد بُعد السرعة'
            ),
            OppositesPair(
                'غالي', 'رخيص',
                'value',
                [('باهض', 'بخس')],
                'الباء يحدد بُعد القيمة'
            ),
            OppositesPair(
                'بناء', 'هدم',
                'construction',
                [('بناء', 'خراب')],
                'الباء يحدد بُعد البناء/الهدم'
            ),
            OppositesPair(
                'ذكي', 'غبي',
                'intelligence',
                [('بصير', 'باهت'), ('بصير', 'بليد')],
                'الباء يحدد بُعد الذكاء'
            ),
            OppositesPair(
                'حركة', 'سكون',
                'motion',
                [('بدأ', 'برك'), ('بادر', 'برك')],
                'الباء يحدد بُعد الحركة'
            ),
        ]
        
        # Create symbolic representations
        symbols = [
            SymbolicRepresentation(
                'البيت والاحتواء',
                'الشكل: نقطة تحت خط = أساس وسقف',
                'في كلمات البناء والمكان',
                ['بيت', 'باحة', 'باب']
            ),
            SymbolicRepresentation(
                'الحمل والنقل',
                'الصوت: انفجاري يوحي بالقوة',
                'في كلمات الحمل والنقل',
                ['حمل', 'نقل', 'بلغ']
            ),
        ]
        
        # Create example words
        examples = {
            'بلع': 'حمل + دك + تشبع: حمل الطعام ودكه في الفم حتى التشبع',
            'بناء': 'حمل + دك + بناء: حمل المواد ودكها لبناء البيت',
            'إبلاغ': 'حمل + نقل + وصول: حمل الرسالة ونقلها حتى الوصول',
            'بلوغ': 'حمل + نقل + وصول: الوصول بعد الحمل والنقل',
            'بيت': 'بناء + احتواء: مكان البناء والاحتواء',
            'باحة': 'بناء + مكان واسع: مكان واسع للبناء',
            'ربح': 'حمل + جمع: حمل وجمع المكاسب',
            'كسب': 'حمل + جمع: حمل وجمع الفوائد',
            'كبح': 'دك + إيقاف: دك وإيقاف الحركة',
            'حبك': 'دك + إحكام: دك وإحكام الربط',
        }
        
        # Create the complete letter
        self.letters['ب'] = AdvancedLetterSemantics(
            letter='ب',
            basic_meanings=['الدك', 'التشبع', 'الحمل', 'النقل', 'البناء'],
            causal_chains=[chain1, chain2],
            opposites=opposites,
            symbolic_representations=symbols,
            example_words=examples
        )
    
    def get_letter(self, letter: str) -> Optional[AdvancedLetterSemantics]:
        """Get advanced semantics for a letter"""
        return self.letters.get(letter)
    
    def analyze_word_advanced(self, word: str) -> Dict:
        """
        Advanced word analysis using causal chains and opposites.
        """
        letters_analysis = []
        all_chains = []
        all_opposites = []
        
        for letter in word:
            sem = self.get_letter(letter)
            if sem:
                letters_analysis.append(sem)
                all_chains.extend(sem.causal_chains)
                all_opposites.extend(sem.opposites)
        
        return {
            'word': word,
            'letters': letters_analysis,
            'causal_chains': all_chains,
            'opposites': all_opposites,
            'inferred_meaning': self._infer_from_chains(word, all_chains),
        }
    
    def _infer_from_chains(self, word: str, chains: List[CausalChain]) -> str:
        """Infer meaning using causal chains"""
        if not chains:
            return "معنى غير محدد"
        
        # Combine meanings from chains
        all_meanings = []
        for chain in chains:
            all_meanings.extend(chain.get_meanings_sequence())
        
        # Return top meanings
        return " + ".join(all_meanings[:3])


# Example usage
if __name__ == '__main__':
    db = AdvancedLetterDatabase()
    
    # Get letter Ba
    ba = db.get_letter('ب')
    if ba:
        print(f"Letter: {ba.letter}")
        print(f"\nBasic meanings: {', '.join(ba.basic_meanings)}")
        
        print(f"\nCausal chains:")
        for chain in ba.causal_chains:
            print(f"  {chain}")
        
        print(f"\nOpposites:")
        for opp in ba.opposites:
            print(f"  {opp.meaning1} ⟷ {opp.meaning2} ({opp.dimension})")
            for w1, w2 in opp.examples:
                print(f"    {w1} ⟷ {w2}")
        
        print(f"\nExample words:")
        for word, explanation in list(ba.example_words.items())[:3]:
            print(f"  {word}: {explanation}")
