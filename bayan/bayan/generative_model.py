"""
Generative Language Model (GLM) for Bayan
=========================================

A revolutionary system that understands and generates language from its roots.
Based on 40 years of research by Basil Yahya Abdullah.

Core Components:
1. Letter Semantics Engine: 28 Arabic letters with deep meanings.
2. Scenario Builder: Constructs words as logical stories (Start -> Event -> Result).
3. Causal/Semantic Networks: Manages relationships between concepts.
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
from .causal_semantic_network import CausalSemanticNetwork, RelationType
from .word_energy_matrix import WordEnergyMatrix

class ArticulationPoint(Enum):
    THROAT = "throat"       # جوف - Psychological/Emotional
    LABIAL = "labial"       # شفاه - Physical/Material
    ALVEOLAR = "alveolar"   # لثة
    PALATAL = "palatal"     # حنك
    VELAR = "velar"         # طبق
    DENTAL = "dental"       # أسنان

@dataclass
class Letter:
    char: str
    name: str
    meanings: List[str]
    articulation: ArticulationPoint
    attributes: List[str]  # e.g., "strength", "softness", "flow"

class LetterSemanticsEngine:
    """
    Engine for managing letter meanings and their attributes.
    Contains the complete database of 28 Arabic letters.
    """
    def __init__(self):
        self.letters: Dict[str, Letter] = self._initialize_database()

    def _initialize_database(self) -> Dict[str, Letter]:
        """Initialize the 28-letter database from research."""
        db = {}
        
        # --- Vowels (3) ---
        db['ا'] = Letter('ا', 'Alif', ['elevation', 'tenderness', 'straightness', 'beginning'], ArticulationPoint.THROAT, ['vertical', 'open'])
        db['و'] = Letter('و', 'Waw', ['attack', 'rolling', 'connection', 'surprise'], ArticulationPoint.LABIAL, ['circular', 'movement'])
        db['ي'] = Letter('ي', 'Ya', ['breaking', 'sorrow', 'psychological pain', 'bending'], ArticulationPoint.PALATAL, ['curved', 'painful'])

        # --- Consonants (25) ---
        db['ب'] = Letter('ب', 'Ba', ['eruption', 'filling', 'saturation', 'carrying', 'transport', 'proximity', 'effort'], ArticulationPoint.LABIAL, ['explosive', 'physical'])
        db['ت'] = Letter('ت', 'Ta', ['building', 'stones', 'projection', 'multiplication', 'result'], ArticulationPoint.ALVEOLAR, ['explosive', 'productive'])
        db['ث'] = Letter('ث', 'Tha', ['scattering', 'randomness', 'stuttering'], ArticulationPoint.DENTAL, ['chaotic', 'weak'])
        db['ج'] = Letter('ج', 'Jeem', ['gathering', 'cohesion', 'attraction', 'solidity', 'trunk'], ArticulationPoint.PALATAL, ['strong', 'unifying'])
        db['ح'] = Letter('ح', 'Ha', ['hardship', 'vitality', 'heat', 'affection', 'relief'], ArticulationPoint.THROAT, ['warm', 'emotional'])
        db['خ'] = Letter('خ', 'Kha', ['piercing', 'investigation', 'good/bad'], ArticulationPoint.VELAR, ['rough', 'penetrating'])
        db['د'] = Letter('د', 'Dal', ['stability', 'firmness', 'opening', 'determination'], ArticulationPoint.ALVEOLAR, ['solid', 'foundational'])
        db['ذ'] = Letter('ذ', 'Thal', ['pleasure', 'enjoyment', 'aversion'], ArticulationPoint.DENTAL, ['sensory', 'fluctuating'])
        db['ر'] = Letter('ر', 'Ra', ['flow', 'repetition', 'movement', 'smoothness'], ArticulationPoint.ALVEOLAR, ['liquid', 'repeating'])
        db['ز'] = Letter('ز', 'Zay', ['sliding', 'provision', 'slipping'], ArticulationPoint.ALVEOLAR, ['sharp', 'sliding'])
        db['س'] = Letter('س', 'Seen', ['crawling', 'friction', 'wall', 'hiding', 'stealth'], ArticulationPoint.ALVEOLAR, ['hissing', 'barrier'])
        db['ش'] = Letter('ش', 'Sheen', ['branching', 'spreading', 'scattering', 'diffusion'], ArticulationPoint.PALATAL, ['spreading', 'diffusive'])
        db['ص'] = Letter('ص', 'Sad', ['insight', 'listening', 'strong impact', 'patience', 'seeing'], ArticulationPoint.ALVEOLAR, ['emphatic', 'perceptive'])
        db['ض'] = Letter('ض', 'Dad', ['compression', 'stagnation', 'littleness', 'pressure'], ArticulationPoint.ALVEOLAR, ['emphatic', 'heavy'])
        db['ط'] = Letter('ط', 'Ta_Emphatic', ['knocking', 'permission', 'flying', 'release'], ArticulationPoint.ALVEOLAR, ['emphatic', 'percussive'])
        db['ظ'] = Letter('ظ', 'Dha', ['thickness', 'severity', 'darkness'], ArticulationPoint.DENTAL, ['emphatic', 'harsh'])
        db['ع'] = Letter('ع', 'Ain', ['depth', 'intensity', 'pulling', 'knowledge'], ArticulationPoint.THROAT, ['deep', 'strong'])
        db['غ'] = Letter('غ', 'Ghain', ['boiling', 'anger', 'absence', 'overcoming'], ArticulationPoint.THROAT, ['gurgling', 'obscuring'])
        db['ف'] = Letter('ف', 'Fa', ['opening', 'explosion', 'gap', 'release'], ArticulationPoint.LABIAL, ['blowing', 'releasing'])
        db['ق'] = Letter('ق', 'Qaf', ['precision', 'thinness', 'distance', 'depth'], ArticulationPoint.VELAR, ['explosive', 'precise'])
        db['ك'] = Letter('ك', 'Kaf', ['giving', 'generosity', 'carrying', 'containment'], ArticulationPoint.VELAR, ['open', 'giving'])
        db['ل'] = Letter('ل', 'Lam', ['pulling', 'wrapping', 'gathering', 'calling'], ArticulationPoint.ALVEOLAR, ['liquid', 'connecting'])
        db['م'] = Letter('م', 'Meem', ['containing', 'silence', 'hiding', 'unknown', 'gathering'], ArticulationPoint.LABIAL, ['nasal', 'containing'])
        db['ن'] = Letter('ن', 'Noon', ['appearance', 'emergence', 'stability', 'point'], ArticulationPoint.ALVEOLAR, ['nasal', 'manifesting'])
        db['ه'] = Letter('ه', 'Ha_Soft', ['effort', 'depth', 'result', 'sighing'], ArticulationPoint.THROAT, ['breathy', 'final'])
        db['ء'] = Letter('ء', 'Hamza', ['surprise', 'shock', 'suddenness'], ArticulationPoint.THROAT, ['glottal', 'sudden'])
        db['ة'] = Letter('ة', 'Ta_Marbuta', ['fruit', 'result', 'femininity'], ArticulationPoint.ALVEOLAR, ['productive', 'final'])

        return db

    def get_letter(self, char: str) -> Optional[Letter]:
        return self.letters.get(char)

    def find_letters_by_meaning(self, meaning_keyword: str) -> List[Letter]:
        """Find letters that carry a specific meaning."""
        results = []
        for letter in self.letters.values():
            if any(meaning_keyword.lower() in m.lower() for m in letter.meanings):
                results.append(letter)
        return results

@dataclass
class ScenarioStep:
    stage: str          # "Start", "Event", "Result"
    concept: str        # e.g., "Appearance", "Gathering"
    letter: Optional[str] = None

class ScenarioBuilder:
    """
    Constructs words based on logical stories/scenarios.
    Method: Start -> Event -> Result
    """
    def __init__(self, semantics_engine: LetterSemanticsEngine):
        self.engine = semantics_engine

    def build_scenario(self, start_concept: str, event_concept: str, result_concept: str) -> List[ScenarioStep]:
        """Create a standard 3-step scenario."""
        return [
            ScenarioStep("Start", start_concept),
            ScenarioStep("Event", event_concept),
            ScenarioStep("Result", result_concept)
        ]

    def build_custom_scenario(self, steps: List[Tuple[str, str]]) -> List[ScenarioStep]:
        """
        Create a custom scenario with arbitrary steps.
        Args:
            steps: List of (stage_name, concept) tuples.
        """
        scenario = []
        for stage, concept in steps:
            scenario.append(ScenarioStep(stage, concept))
        return scenario

    def generate_word(self, scenario: List[ScenarioStep]) -> Dict[str, Any]:
        """
        Generate a word from a scenario by selecting the best fitting letters.
        """
        word_chars = []
        explanation = []

        for step in scenario:
            candidates = self.engine.find_letters_by_meaning(step.concept)
            if not candidates:
                # Fallback: try to find synonyms or related concepts (simplified here)
                return {"error": f"No letter found for concept: {step.concept}"}
            
            # Selection logic: 
            # For now, pick the first one, but ideally we'd score them based on context
            selected = candidates[0]
            word_chars.append(selected.char)
            step.letter = selected.char
            explanation.append(f"{step.stage} ({step.concept}) -> {selected.char} ({', '.join(selected.meanings[:2])})")

        word = "".join(word_chars)
        return {
            "word": word,
            "scenario": scenario,
            "explanation": explanation
        }

class GenerativeLanguageModel:
    """
    The main interface for the Bayan Generative System.
    """
    def __init__(self):
        self.semantics = LetterSemanticsEngine()
        self.scenario_builder = ScenarioBuilder(self.semantics)
        self.network = CausalSemanticNetwork()
        self.wem = WordEnergyMatrix()  # Word Energy Matrix integration
        self._initialize_network_knowledge()

    def _initialize_network_knowledge(self):
        """Initialize some basic causal knowledge for demonstration."""
        # Causal chain for 'Morning' (صبح)
        self.network.add_relation("seeing", "effort", RelationType.LEADS_TO, 0.9)
        self.network.add_relation("effort", "relief", RelationType.LEADS_TO, 0.8)
        
        # Causal chain for 'Star' (نجم)
        self.network.add_relation("appearance", "gathering", RelationType.LEADS_TO, 0.8)
        self.network.add_relation("gathering", "unknown", RelationType.LEADS_TO, 0.7)

        # Causal chain for 'Tree' (شجرة)
        self.network.add_relation("branching", "gathering", RelationType.REQUIRES, 0.9)
        self.network.add_relation("gathering", "flow", RelationType.ENABLES, 0.8)
        self.network.add_relation("flow", "fruit", RelationType.LEADS_TO, 0.9)

    def suggest_story_completion(self, start_concept: str) -> Dict[str, List[str]]:
        """Suggest events and results based on a start concept."""
        return self.network.suggest_scenario_completion(start_concept)

    def generate_from_story(self, start: str, event: str, result: str) -> Dict[str, Any]:
        """
        Generate a word from a story description.
        Example: start="appearance", event="gathering", result="unknown" -> "نجم"
        """
        scenario = self.scenario_builder.build_scenario(start, event, result)
        return self.scenario_builder.generate_word(scenario)

    def analyze_word_story(self, word: str, include_wem: bool = False) -> Dict[str, Any]:
        """
        Reverse engineer the story of a word.
        Args:
            word: The word to analyze
            include_wem: If True, includes Word Energy Matrix analysis
        """
        story = []
        for i, char in enumerate(word):
            letter = self.semantics.get_letter(char)
            if letter:
                stage = "Start" if i == 0 else "Result" if i == len(word)-1 else "Event"
                story.append({
                    "stage": stage,
                    "letter": char,
                    "meanings": letter.meanings
                })
        
        result = {"word": word, "story": story}
        
        if include_wem:
            # Detect language (simple heuristic: if any Arabic char, it's Arabic)
            lang = 'ar' if any('\u0600' <= c <= '\u06FF' for c in word) else 'en'
            result["wem_analysis"] = self.wem.analyze_word(word, lang)
        
        return result

    def analyze_word_energy(self, word: str, lang: str = 'ar') -> Dict[str, Any]:
        """
        Perform deep semantic analysis using the Word Energy Matrix.
        This is the primary method for symbol interpretation and dream analysis.
        
        Args:
            word: The word to analyze
            lang: Language ('ar' for Arabic, 'en' for English)
            
        Returns:
            Complete WEM analysis including surface meaning, root analysis (for Arabic),
            and suffix effects (for English)
        """
        return self.wem.analyze_word(word, lang)

