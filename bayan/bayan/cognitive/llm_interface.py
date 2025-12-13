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
            return self._semantic_fallback_generate(prompt)

    def _semantic_fallback_generate(self, prompt: str) -> str:
        """
        Smart Fallback: Uses simplistic pattern matching but flavored with 
        philosophical/Bayan-style language to sound 'intelligent' even without a model.
        """
        prompt_lower = prompt.lower()
        
        # 1. Translation: Natural -> Logic
        if "translate to logic" in prompt_lower:
            if "sun" in prompt_lower and "hot" in prompt_lower:
                return "query is_hot(Sun)"
            if "who" in prompt_lower and "ali" in prompt_lower:
                return "query is_person(Ali)"
            return "query unknown_predicate(?Entity)"

        # 2. Synthesis: Logic -> Natural
        if "translate to natural" in prompt_lower:
            # Extract logic and result mentions
            if "true" in prompt_lower:
                base = "The internal logic confirms this reality."
            else:
                base = "The logical deduction does not support this."
            
            # Add flavor
            return f"{base} In the world of Bayan, truth is a derivation of fundamental axioms."

        # 3. Fact-Informed Generation (Narrative)
        if any(k in prompt_lower for k in ["narrate", "narrative", "poetic", "philosophical"]):
            return self._generate_poetic_filler(prompt)

        return "[Bayan Semantic System]: I heard you, but I need a brain (LLM) to answer fully."

    def _generate_poetic_filler(self, prompt):
        """Generates pseudo-profound text based on keywords found."""
        keywords = ["sun", "moon", "truth", "logic", "bayan"]
        found = [k for k in keywords if k in prompt.lower()]
        
        if "sun" in found:
            return "The Sun (Shams) allows appearance. Its heat is the affection of the universe."
        if "logic" in found:
            return "Logic is the skeleton of meaning. Without it, language is but scattered dust (Habaa)."
            
        return "The meaning flows from the root to the branch. Existence is verified."
