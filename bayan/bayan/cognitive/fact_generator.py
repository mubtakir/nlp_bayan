import sys
import os

# Ensure import paths
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from bayan.bayan.cognitive.llm_interface import LLMInterface
from bayan.bayan.logical_engine import Fact
from bayan.bayan.generative_model import LetterSemanticsEngine

class FactGenerator:
    """
    Generates Natural Language from Logical Facts.
    Uses 'Fact-Informed Generation' to ensure truthfulness while adding stylistic flair.
    """
    def __init__(self, llm_interface: LLMInterface):
        self.llm = llm_interface
        self.semantics = LetterSemanticsEngine()
        
    def generate_narrative(self, facts: list[Fact], style: str = "philosophical") -> str:
        """
        Turn a list of facts into a coherent paragraph.
        """
        if not facts:
            return "There are no facts to narrate."

        # 1. Convert Facts to Sentences
        fact_sentences = []
        concepts = set()
        for fact in facts:
            # e.g., is_hot(Sun) -> Sun is_hot
            args = ", ".join(str(a) for a in fact.predicate.args)
            fact_sentences.append(f"{args} is {fact.predicate.name}")
            
            # Collect concepts for semantic analysis
            for arg in fact.predicate.args:
                concepts.add(str(arg))

        combined_text = ". ".join(fact_sentences)

        # 2. Inject Semantic Flavor
        # Look up meanings of concepts to add to the prompt
        flavor_text = ""
        for concept in concepts:
            # Heuristic: analyze first letter if existing word
            if concept and len(concept) > 0:
                 # Check if we have letter semantics
                 # (Simplified for demo)
                 pass
        
        # 3. Construct Prompt
        prompt = (
            f"Style: {style}.\n"
            f"Facts: {combined_text}.\n"
            f"Task: Rewrite the above facts into a flowing, {style} narrative. "
            f"Use deep, meaningful language.\n"
            f"Narrative:"
        )

        # 4. Generate
        return self.llm.generate(prompt, max_length=150)

    def generate_answer(self, question: str, facts: list[Fact]) -> str:
        """
        Answer a specific question based on provided facts.
        """
        fact_text = ". ".join([f"{f.predicate.name}({','.join(str(a) for a in f.predicate.args)})" for f in facts])
        
        prompt = (
            f"Question: {question}\n"
            f"Relevant Facts: {fact_text}\n"
            f"Answer: Based on the facts, "
        )
        
        return self.llm.generate(prompt, max_length=100)

if __name__ == "__main__":
    # Test
    from bayan.bayan.logical_engine import Predicate, Term
    
    llm = LLMInterface() # Mock
    gen = FactGenerator(llm)
    
    f1 = Fact(Predicate("is_hot", [Term("Sun")]))
    f2 = Fact(Predicate("gives_light", [Term("Sun")]))
    
    print("--- Narrative ---")
    print(gen.generate_narrative([f1, f2]))
