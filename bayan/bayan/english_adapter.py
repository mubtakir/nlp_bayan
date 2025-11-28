import sys

class EnglishNLPAdapter:
    """
    Adapter for English NLP tasks using spaCy.
    Provides POS tagging, lemmatization, and dependency parsing.
    """
    def __init__(self, model="en_core_web_sm"):
        self.nlp = None
        self.model_name = model
        self._initialize_tools()

    def _initialize_tools(self):
        """
        Lazy initialization of spaCy.
        """
        try:
            import spacy
            try:
                self.nlp = spacy.load(self.model_name)
            except OSError:
                print(f"Warning: spaCy model '{self.model_name}' not found. Please download it.")
                # Fallback to blank English model if specific model missing
                self.nlp = spacy.blank("en")
        except ImportError:
            print("Warning: spaCy not found. EnglishNLPAdapter running in fallback mode.")

    def analyze(self, text):
        """
        Returns POS tags and lemmas.
        """
        if not self.nlp:
            return [{"word": word, "pos": "UNKNOWN", "lemma": word} for word in text.split()]
        
        doc = self.nlp(text)
        results = []
        for token in doc:
            results.append({
                "word": token.text,
                "pos": token.pos_,
                "lemma": token.lemma_,
                "dep": token.dep_
            })
        return results

    def lemmatize(self, text):
        """
        Returns just the lemmas.
        """
        analysis = self.analyze(text)
        return " ".join([item["lemma"] for item in analysis])
