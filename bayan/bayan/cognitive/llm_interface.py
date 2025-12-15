import sys
import os
import random

# Try to import Bayan components for Semantic Fallback
try:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
    from bayan.bayan.generative_model import LetterSemanticsEngine
except ImportError:
    LetterSemanticsEngine = None

class LLMInterface:
    """
    Unified Interface for Large Language Models.
    Supports local HuggingFace models via transformers pipeline.
    Provides a 'Smart Semantic Fallback' using Bayan's Letter Engine if no model is loaded.
    """
    def __init__(self, model_name_or_path=None):
        self.model_name = model_name_or_path
        self.pipeline = None
        self.mock_mode = False
        self.semantics = LetterSemanticsEngine() if LetterSemanticsEngine else None
        self._initialize_model()

    def _initialize_model(self):
        """Try to load the model, fallback to mock/semantic if failed or not provided."""
        if not self.model_name:
            print("⚠️ No model provided. Switching to Semantic Fallback Mode.")
            self.mock_mode = True
            return

        try:
            print(f"🔄 Loading LLM: {self.model_name}...")
            from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
            
            # Use pipeline for ease of use
            self.pipeline = pipeline(
                'text-generation', 
                model=self.model_name,
                device_map="auto" # Use GPU if available
            )
            print("✅ LLM loaded successfully.")
        except Exception as e:
            print(f"❌ Failed to load model: {e}")
            print("⚠️ Switching to Semantic Fallback Mode.")
            self.mock_mode = True

    def generate(self, prompt: str, max_length: int = 100, temperature: float = 0.7) -> str:
        """Generate text based on prompt."""
        if self.mock_mode:
            return self._semantic_fallback_generate(prompt)
        
        try:
            output = self.pipeline(
                prompt, 
                max_length=max_length, 
                num_return_sequences=1,
                temperature=temperature,
                do_sample=True,
                truncation=True
            )
            return output[0]['generated_text']
        except Exception as e:
            print(f"❌ Generation Error: {e}")
            return self._semantic_fallback_generate(prompt, max_length)

    def _semantic_fallback_generate(self, prompt: str, max_tokens: int) -> str:
        """
        A sophisticated rule-based generator that simulates LLM behavior
        when no actual model is loaded.
        """
        prompt_lower = prompt.lower() # Fix: Define variable
        import re
        
        if "translate to logic" in prompt_lower:
            clean_q = prompt.split("logic:")[-1].strip().lower()
            
            # Pattern: Is X Y? (e.g., Is the sun hot?)
            # Regex: is (the )?(\w+) (\w+)\?
            match_is = re.search(r"is (?:the )?(\w+) (\w+)\??", clean_q)
            if match_is:
                obj, adj = match_is.groups()
                # Predicate convention: is_adj(Obj)
                return f"query is_{adj}({obj.capitalize()})"

            # Pattern: Who/What is X?
            match_who = re.search(r"(?:who|what) is (?:the )?(\w+)\??", clean_q)
            if match_who:
                obj = match_who.group(1)
                return f"query is_person({obj.capitalize()})"

            # Pattern: Statement "X is Y" (Learning)
            # Relaxed regex: No strict dot required at end
            match_stmt = re.search(r"(?:the )?(\w+) is (\w+)(?:\.)?$", clean_q)
            if match_stmt:
                obj, adj = match_stmt.groups()
                return f"fact is_{adj}({obj.capitalize()})"

            return "query unknown_predicate(?Entity)"

        # --- 2. Synthesis: Logic -> Natural ---
        if "translate to natural" in prompt_lower:
            # Parse input: "Question='...', Logic='...', Result='...'"
            # Simple heuristic extraction
            is_true = "result='true'" in prompt_lower or "result=true" in prompt_lower
            
            # Try to extract the core triple from logic if possible
            # Logic='query is_hot(Sun)'
            match_logic = re.search(r"is_(\w+)\((\w+)\)", prompt)
            
            if match_logic:
                adj, obj = match_logic.groups()
                if is_true:
                    return f"Yes, the {obj} is {adj}. This is a confirmed reality."
                else:
                    return f"No, I do not have evidence that the {obj} is {adj}."
            
            if is_true:
                return "The internal logic validates this truth."
            else:
                return "My reasoning engine does not support this conclusion."

        # --- 3. Fact-Informed Generation (Narrative) ---
        if any(k in prompt_lower for k in ["narrate", "narrative", "poetic", "philosophical"]):
            # Extract the raw facts from the prompt if they exist
            # Prompt format from FactGenerator: "Facts: Sun is is_hot. ..."
            return self._generate_poetic_filler(prompt)

        return "[Bayan Semantic System]: I heard you, but I need a brain (LLM) to answer fully."

    def _generate_poetic_filler(self, prompt):
        """Generates pseudo-profound text based on keywords found."""
        keywords = ["sun", "moon", "truth", "logic", "bayan", "ali", "human"]
        found = [k for k in keywords if k in prompt.lower()]
        
        # Dynamic template selection
        templates = []
        if "sun" in found:
            templates.append("The Sun (Shams) is the eye of the day. Its heat is the warmth of existence.")
        if "moon" in found:
            templates.append("The Moon reflects what is hidden.")
        if "ali" in found or "human" in found:
            templates.append("A human is a universe wrapped in a body.")
        if "logic" in prompt.lower():
            templates.append("Logic is the skeleton of meaning. Without it, language is but scattered dust (Habaa).")
        
        if templates:
            return " ".join(templates)
            
        return "The meaning flows from the root to the branch. Existence is verified from the core."
