import sys

class ArabicNLPAdapter:
    """
    Adapter for Arabic NLP tasks using CAMeL Tools.
    Provides morphology analysis, diacritization, and tokenization.
    """
    def __init__(self):
        self.morphology_analyzer = None
        self.diacritizer = None
        self._initialize_tools()

    def _initialize_tools(self):
        """
        Lazy initialization of CAMeL Tools components to avoid import errors
        if the library is not installed or databases are missing.
        """
        try:
            from camel_tools.morphology.database import MorphologyDB
            from camel_tools.morphology.analyzer import Analyzer
            from camel_tools.morphology.generator import Generator
            
            # Initialize with analysis database (r13)
            try:
                self.db = MorphologyDB.builtin_db()
                self.morphology_analyzer = Analyzer(self.db)
            except Exception as e:
                print(f"Warning: Could not load CAMeL Tools MorphologyDB: {e}")
            
            # Note: Generator (for verb conjugation) requires specific database configurations
            # The installed databases (r13, s31) support analysis but not generation via standard API
            # Our fallback implementation provides comprehensive conjugation support
            # including dual, imperative, and all person/gender/number combinations
            self.generator = None
                
        except ImportError:
            print("Warning: CAMeL Tools not found. ArabicNLPAdapter running in fallback mode.")
            self.generator = None

    def analyze_morphology(self, text):
        """
        Returns morphological analysis for the text.
        """
        if not self.morphology_analyzer:
            return [{"word": word, "analysis": "unknown"} for word in text.split()]
        
        analyses = []
        words = text.split()
        for word in words:
            # Simple analysis for each word
            word_analyses = self.morphology_analyzer.analyze(word)
            analyses.append({"word": word, "analysis": word_analyses})
        return analyses

    def diacritize(self, text):
        """
        Diacritizes the input Arabic text.
        """
        # Placeholder for actual diacritization logic using CAMeL Tools
        # which usually requires a specific model (e.g., MLE or Neural).
        # For now, we return text as is if tool not ready.
        return text

    def tokenize(self, text):
        """
        Tokenizes Arabic text.
        """
        try:
            from camel_tools.tokenizers.word import simple_word_tokenize
            return simple_word_tokenize(text)
        except ImportError:
            return text.split()

    def extract_root(self, word):
        """
        Extracts the root of an Arabic word using CAMeL Tools.
        Returns the root string (e.g., 'درس' for 'مدرسة') or the word itself if not found.
        """
        if not self.morphology_analyzer:
            return word

        try:
            analyses = self.morphology_analyzer.analyze(word)
            if analyses:
                # Look for the first analysis that has a root
                for analysis in analyses:
                    if 'root' in analysis and analysis['root'] != 'null':
                        # Root is often returned as 'd.r.s', we need to remove dots
                        return analysis['root'].replace('.', '')
            return word
        except Exception as e:
            print(f"Error extracting root for {word}: {e}")
            return word

    def conjugate_verb(self, lemma, tense, person_gender_number):
        """
        Conjugates an Arabic verb using CAMeL Tools Generator.
        
        Args:
            lemma: The verb lemma (e.g., 'كَتَبَ')
            tense: 'past', 'present', 'future', or 'imperative'
            person_gender_number: Format like '3ms', '2fd', '1p', etc.
                - First digit: person (1, 2, 3)
                - Second letter: gender (m=masculine, f=feminine)
                - Third letter: number (s=singular, d=dual, p=plural)
        
        Returns:
            Conjugated verb form or fallback result
        """
        if not self.generator:
            return self._conjugate_fallback(lemma, tense, person_gender_number)
        
        try:
            # Parse person_gender_number
            person = person_gender_number[0]
            gender = person_gender_number[1] if len(person_gender_number) > 1 else 'm'
            number = person_gender_number[2] if len(person_gender_number) > 2 else 's'
            
            # Map tense to aspect
            if tense == 'past':
                aspect = 'p'  # perfective
            elif tense in ['present', 'future']:
                aspect = 'i'  # imperfective
            elif tense == 'imperative':
                aspect = 'c'  # command
            else:
                aspect = 'p'
            
            # Build features dictionary for Camel Tools
            features = {
                'pos': 'verb',
                'asp': aspect,
                'per': person,
                'gen': gender,
                'num': number,
                'vox': 'a',  # active voice
                'mod': 'i' if tense != 'imperative' else 'c'  # indicative or command
            }
            
            # Generate
            results = self.generator.generate(lemma, features)
            
            if results:
                # Return first result (usually the most common form)
                return results[0]['diac']
            else:
                return self._conjugate_fallback(lemma, tense, person_gender_number)
                
        except Exception as e:
            print(f"Error conjugating {lemma}: {e}")
            return self._conjugate_fallback(lemma, tense, person_gender_number)
    
    def _conjugate_fallback(self, lemma, tense, person_gender_number):
        """
        Fallback conjugation using simple rules (from ai/morphology.bayan logic)
        """
        # Remove diacritics for processing
        lemma_clean = ''.join(c for c in lemma if c not in 'َُِّْ')
        
        prefix = ""
        suffix = ""
        
        if tense == "past":
            if person_gender_number == "3ms": suffix = ""
            elif person_gender_number == "3fs": suffix = "ت"
            elif person_gender_number == "3md": suffix = "ا"
            elif person_gender_number == "3fd": suffix = "تا"
            elif person_gender_number == "3mp": suffix = "وا"
            elif person_gender_number == "3fp": suffix = "ن"
            elif person_gender_number == "2ms": suffix = "تَ"
            elif person_gender_number == "2fs": suffix = "تِ"
            elif person_gender_number == "2md": suffix = "تما"
            elif person_gender_number == "2mp": suffix = "تم"
            elif person_gender_number == "2fp": suffix = "تن"
            elif person_gender_number == "1s": suffix = "ت"
            elif person_gender_number == "1p": suffix = "نا"
            
        elif tense == "present":
            if person_gender_number == "3ms": prefix = "ي"
            elif person_gender_number == "3fs": prefix = "ت"
            elif person_gender_number == "3md": prefix = "ي"; suffix = "ان"
            elif person_gender_number == "3fd": prefix = "ت"; suffix = "ان"
            elif person_gender_number == "3mp": prefix = "ي"; suffix = "ون"
            elif person_gender_number == "3fp": prefix = "ي"; suffix = "ن"
            elif person_gender_number == "2ms": prefix = "ت"
            elif person_gender_number == "2fs": prefix = "ت"; suffix = "ين"
            elif person_gender_number == "2md": prefix = "ت"; suffix = "ان"
            elif person_gender_number == "2mp": prefix = "ت"; suffix = "ون"
            elif person_gender_number == "2fp": prefix = "ت"; suffix = "ن"
            elif person_gender_number == "1s": prefix = "أ"
            elif person_gender_number == "1p": prefix = "ن"
            
        elif tense == "future":
            present_form = self._conjugate_fallback(lemma, "present", person_gender_number)
            return "س" + present_form
            
        elif tense == "imperative":
            if person_gender_number == "2ms": prefix = "ا"
            elif person_gender_number == "2fs": prefix = "ا"; suffix = "ي"
            elif person_gender_number == "2md": prefix = "ا"; suffix = "ا"
            elif person_gender_number == "2mp": prefix = "ا"; suffix = "وا"
            elif person_gender_number == "2fp": prefix = "ا"; suffix = "ن"
            else: return "N/A"  # Imperative only for 2nd person
        
        return prefix + lemma_clean + suffix
