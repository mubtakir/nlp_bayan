"""
Word Energy Matrix (WEM) System
===============================
Based on the "Letter Semantics" theory (Fiqh Al-Harf) by Researcher Basel Yahya Abdullah.
Implements the Hybrid Method (Sound + Shape + Psyche + Movement).
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from .letter_semantics import LetterSemanticsDatabase
from .enhanced_letter_semantics import EnhancedLetterSemantics
from .arabic_adapter import ArabicNLPAdapter

@dataclass
class LetterEnergy:
    char: str
    sound: str
    shape: str
    psyche: str
    meaning: str
    category: str = "General"

class WordEnergyMatrix:
    """
    Analyzes words based on letter energy and semantic meanings.
    Now enhanced with Camel Tools integration for accurate root extraction.
    """
    
    def __init__(self):
        self.letter_db = LetterSemanticsDatabase()
        self.enhanced_semantics = EnhancedLetterSemantics(self.letter_db)
        self.arabic_adapter = ArabicNLPAdapter()  # For accurate root extraction
        self.en_db = self._init_english_db()
        self.ar_db = self._init_arabic_db()

    def _init_english_db(self) -> Dict[str, LetterEnergy]:
        return {
            'a': LetterEnergy('A', 'Open/Start', 'Pyramid/Peak', 'Start/Rise', 'Start - Rise - Expansion - Focus', 'Vertical'),
            'b': LetterEnergy('B', 'Explosion/Block', 'Container/Filled', 'Pressure/Filling', 'Filling - Pressure - Carrying - Impact', 'Containment'),
            'c': LetterEnergy('C', 'Cut/Flow', 'Curve/Containment', 'Containment/Turn', 'Containment - Curve - Conversion', 'Curved'),
            'd': LetterEnergy('D', 'Hard Stop', 'Closed Curve', 'Decision/End', 'Definition - End - Limit - Determination', 'Stop'),
            'e': LetterEnergy('E', 'Extension', 'Levels', 'Revelation', 'Extension - Appearance - Balance', 'Horizontal'),
            'f': LetterEnergy('F', 'Air Flow', 'Direction', 'Release/Breath', 'Flow - Release - Spread - Forward Push', 'Flow'),
            'g': LetterEnergy('G', 'Deep Stop', 'Broken Circle', 'Grip/Force', 'Grip - Force - Taking - Heavy Impact', 'Grip'),
            'h': LetterEnergy('H', 'Breath', 'Bridge', 'Spirit/Lightness', 'Spirit - Breath - Connection - Lightness', 'Air'),
            'i': LetterEnergy('I', 'Sharp/Thin', 'Line', 'Focus/Self', 'Focus - Individuality - Point - Intensity', 'Vertical'),
            'j': LetterEnergy('J', 'Jump', 'Hook', 'Sudden Move', 'Jump - Turn - Dynamic - Jerk', 'Dynamic'),
            'k': LetterEnergy('K', 'Sharp Cut', 'Angle', 'Cut/Angle', 'Cut - Direction - Separation - Key', 'Cut'),
            'l': LetterEnergy('L', 'Flow', 'Angle/Reach', 'Softness/Link', 'Softness - Link - Approach - Light', 'Flow'),
            'm': LetterEnergy('M', 'Closed Lip', 'Waves/Mounds', 'Containment/Mother', 'Containment - Internal - Merging - Mother', 'Containment'),
            'n': LetterEnergy('N', 'Nasal', 'Connection', 'Continuity', 'Continuity - Path - Connection - Next', 'Flow'),
            'o': LetterEnergy('O', 'Circle', 'Circle', 'Wholeness/Cycle', 'Rotation - Continuity - Containment - Whole', 'Circle'),
            'p': LetterEnergy('P', 'Pop', 'Flag/Pin', 'Push/Point', 'Push - Pop - Projection - Pinpoint', 'Push'),
            'q': LetterEnergy('Q', 'Deep Cut', 'Circle+Tail', 'Deep Quest', 'Depth - Quest - Squeeze - Query', 'Deep'),
            'r': LetterEnergy('R', 'Vibration', 'Runner', 'Movement/Energy', 'Movement - Flow - Run - Rise', 'Movement'),
            's': LetterEnergy('S', 'Hiss', 'Snake', 'Flow/Slide', 'Flow - Slide - Spread - Smooth', 'Flow'),
            't': LetterEnergy('T', 'Stop', 'Cross', 'Limit/Stop', 'Cut - Limit - Definition - Target', 'Stop'),
            'u': LetterEnergy('U', 'Deep Vowel', 'Cup', 'Depth/Under', 'Containment - Depth - Under - Up', 'Deep'),
            'v': LetterEnergy('V', 'Vibration', 'Arrow', 'Focus/Victory', 'Focus - Direction - Energy - Vitality', 'Focus'),
            'w': LetterEnergy('W', 'Double U', 'Waves', 'Fluctuation', 'Wave - Fluctuation - Width - Wind', 'Wave'),
            'x': LetterEnergy('X', 'Clash', 'Cross', 'Conflict/Unknown', 'Crossing - Conflict - Unknown - Mix', 'Cross'),
            'y': LetterEnergy('Y', 'Semi-vowel', 'Fork', 'Choice/Path', 'Path - Choice - Yielding - Yearning', 'Path'),
            'z': LetterEnergy('Z', 'Buzz', 'Zigzag', 'Speed/Energy', 'Speed - Energy - Zone - Zeal', 'Speed'),
        }

    def _init_arabic_db(self) -> Dict[str, LetterEnergy]:
        # Based on COMPLETE_ARABIC_LETTER_MEANINGS.md and User Etymology Feedback
        return {
            # Vowels (Jaufiyah)
            'ا': LetterEnergy('ألف', 'Breath/Open', 'Vertical', 'Elevation', 'Ulfah (Connection) - Elevation - Tenderness - Foundation', 'Vertical'),
            'أ': LetterEnergy('ألف', 'Breath/Open', 'Vertical', 'Elevation', 'Ulfah (Connection) - Elevation - Tenderness - Foundation', 'Vertical'),
            'و': LetterEnergy('واو', 'Round', 'Loop', 'Advance', 'Attack - Advance - Rolling - Surprise - Connection', 'Openness'),
            'ي': LetterEnergy('ياء', 'Semi-vowel', 'Curved', 'Brokenness', 'Brokenness - Regret - Psychological Pain - Distress', 'Curvature'),
            
            # Consonants
            'ب': LetterEnergy('باء', 'Explosion', 'Boat/Dot', 'Impact', 'Baw\' (Returning/Bearing) - Crushing - Fullness - Carrying', 'Burst'),
            'ت': LetterEnergy('تاء', 'Sharp Stop', 'Bowl/Dots', 'Change', 'Stones - Building - Throwing - Movement/Change - Evolution', 'Burst'),
            'ث': LetterEnergy('ثاء', 'Friction', 'Bowl', 'Scattering', 'Random Scattering - Stuttering - Disorganized Dispersion', 'Flow'),
            'ج': LetterEnergy('جيم', 'Friction', 'Curved', 'Gathering', 'Jaam (Gathering) - Attraction - Cohesion - Comforting', 'Curvature'),
            'ح': LetterEnergy('حاء', 'Breath', 'Open Curve', 'Vitality', 'Haam (Circling/Hovering) - Affection - Thirst - Vitality', 'Openness'),
            'خ': LetterEnergy('خاء', 'Friction', 'Open Curve', 'Penetration', 'Expelling/Vomiting - Piercing - Investigation - Mockery', 'Deep'),
            'د': LetterEnergy('دال', 'Stop', 'Angle', 'Stability', 'Dalla (Indicating) - Stability - Firmness - Determination', 'Stop'),
            'ذ': LetterEnergy('ذال', 'Friction', 'Angle', 'Pleasure', 'Thalla (Lowering/Submission) - Relishing - Enjoyment - Flow', 'Flow'),
            'ر': LetterEnergy('راء', 'Trill', 'Slide', 'Flow', 'Raa/Rayy (Watering/Flow) - Repetition - Movement', 'Openness'),
            'ز': LetterEnergy('زاي', 'Buzz', 'Slide', 'Sliding', 'Azza (Pushing/Urging) - Sliding - Provisioning', 'Speed'),
            'س': LetterEnergy('سين', 'Hiss', 'Teeth', 'Seepage', 'Crawling - Friction - Wall/Fence - Hiding/Infiltration - Faintness', 'Flow'),
            'ش': LetterEnergy('شين', 'Spread', 'Teeth', 'Diffusion', 'Branching - Spreading - Dispersion - Ignition', 'Curvature'),
            'ص': LetterEnergy('صاد', 'Deep Hiss', 'Loop', 'Impact', 'Sayd (Hunting) - Echo - Severe Knocking - Listening', 'Flow'),
            'ض': LetterEnergy('ضاد', 'Deep Stop', 'Loop', 'Compression', 'Smallness - Severe Suppression - Atrophy - Stagnation', 'Stop'),
            'ط': LetterEnergy('طاء', 'Deep Stop', 'Vertical+Loop', 'Knocking', 'Knocking - Permission - Escaping - Soaring', 'Stop'),
            'ظ': LetterEnergy('ظاء', 'Deep Friction', 'Vertical+Loop', 'Roughness', 'Roughness - Severity - Thickness', 'Deep'),
            'ع': LetterEnergy('عين', 'Deep Constriction', 'Open Curve', 'Depth', 'Uprooting - Pushing - Depth/Severity - Strong Emotion - Knowledge', 'Deep'),
            'غ': LetterEnergy('غين', 'Gargle', 'Open Curve', 'Boiling', 'Boiling - Anger - Absence/Hiding - Overcoming', 'Deep'),
            'ف': LetterEnergy('فاء', 'Blow', 'Loop', 'Opening', 'Opening - Explosion - Gap - Sound of Explosion', 'Burst'),
            'ق': LetterEnergy('قاف', 'Deep Cut', 'Deep Circle', 'Precision', 'Precision - Distant Goal - Distance - Thinness/Delicacy', 'Vertical'),
            'ك': LetterEnergy('كاف', 'Push', 'Angle', 'Giving', 'Kafaa (Sufficiency/Giving) - Generosity - Carrying', 'Vertical'),
            'ل': LetterEnergy('لام', 'Lateral', 'Hook', 'Enfolding', 'Dragging - Gathering - Wrapping - Encompassing - Calling', 'Containment'),
            'م': LetterEnergy('ميم', 'Closed Lip', 'Mound', 'Containment', 'Joining - Silence - Concealment - Satisfaction - Containment', 'Containment'),
            'ن': LetterEnergy('نون', 'Nasal', 'Bowl', 'Emergence', 'Appearance - Stability - Genesis - Moaning', 'Containment'),
            'ه': LetterEnergy('هاء', 'Breath', 'Circle', 'Effort', 'Effort/Fatigue - Depth - Result/Fruit - Sighing', 'Deep'),
            'ء': LetterEnergy('همزة', 'Glottal Stop', 'Small', 'Surprise', 'Surprise Element - Horror/Fear Sound - Deep Pain - Shock', 'Vertical'),
            'ة': LetterEnergy('تاء مربوطة', 'Stop/Breath', 'Circle', 'Result', 'Result - Fruit - Femininity - End state', 'Stop'),
            'ى': LetterEnergy('ألف مقصورة', 'Breath', 'Curved', 'Internal Rise', 'Internal Elevation - Hidden Extension', 'Curvature'),
        }

    def get_letter_data(self, char: str, lang: str = 'en') -> Optional[LetterEnergy]:
        char = char.lower()
        if lang == 'en':
            return self.en_db.get(char)
        else:
            return self.ar_db.get(char)

    def analyze_word(self, word: str, lang: str = 'en') -> Dict:
        """
        Analyzes a word based on the Word Energy Matrix principles.
        Includes Root Analysis for Arabic and Suffix Analysis for English.
        """
        letters_analysis = []
        energy_profile = []
        
        # 1. Decomposition & Basic Lookup
        for char in word:
            data = self.get_letter_data(char, lang)
            if data:
                letters_analysis.append({
                    'char': char,
                    'data': data
                })
                energy_profile.append(data.meaning)
            else:
                letters_analysis.append({
                    'char': char,
                    'data': None
                })

        if not letters_analysis:
            return {"error": "No analyzable letters found"}

        # 2. Positional Analysis (Directional Principle)
        start_energy = letters_analysis[0]['data'].meaning if letters_analysis[0]['data'] else "Unknown"
        end_energy = letters_analysis[-1]['data'].meaning if letters_analysis[-1]['data'] else "Unknown"
        
        core_energies = []
        if len(letters_analysis) > 2:
            for i in range(1, len(letters_analysis) - 1):
                if letters_analysis[i]['data']:
                    core_energies.append(letters_analysis[i]['data'].meaning)
        elif len(letters_analysis) == 2:
             pass
        
        core_summary = " + ".join(core_energies) if core_energies else "Direct Transition"

        # 3. Synthesis & Advanced Features
        narrative = f"Starts with [{start_energy}], moves through [{core_summary}], and resolves in [{end_energy}]."
        
        suffix_effect = None
        root_analysis = None

        # English Suffix Logic: -ing
        if lang == 'en' and word.lower().endswith('ing') and len(word) > 3:
            # Base letter is the one before 'ing'
            base_char_index = len(word) - 4
            if base_char_index >= 0:
                base_char = word[base_char_index]
                base_data = self.get_letter_data(base_char, 'en')
                if base_data:
                    suffix_effect = f"Continuous [{base_data.meaning}]"
                    narrative += f" The 'ing' suffix indicates a continuous state of [{base_data.meaning}]."

        # Arabic Root Logic - Now using Camel Tools!
        if lang == 'ar':
            root = self.arabic_adapter.extract_root(word)
            if root and root != word:
                # Analyze the root's letter meanings
                root_letters = []
                for rc in root:
                    rd = self.get_letter_data(rc, 'ar')
                    if rd: root_letters.append(rd.meaning)
                
                root_narrative = " + ".join(root_letters)
                root_analysis = {
                    "root": root,
                    "meaning": root_narrative,
                    "method": "camel_tools"  # Indicate we used Camel Tools
                }
                narrative += f" Root analysis: [{root}] = {root_narrative}"

        return {
            "word": word,
            "lang": lang,
            "letters": letters_analysis,
            "structure": {
                "start": start_energy,
                "core": core_summary,
                "end": end_energy
            },
            "narrative": narrative,
            "suffix_effect": suffix_effect,
            "root_analysis": root_analysis
        }

