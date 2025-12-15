import sys
import os

# Ensure we can import bayan packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from bayan.bayan.istinbat_engine import IstinbatEngine, Predicate, Term, DeductionResult
from .llm_interface import LLMInterface

class CognitiveBridge:
    """
    The Brain that bridges Natural Language and Logical Reasoning.
    Uses LLM to translate User Query -> Logic -> Answer.
    """
    def __init__(self, model_path=None):
        self.llm = LLMInterface(model_path)
        self.engine = IstinbatEngine()
        self._seed_knowledge()

    def _seed_knowledge(self):
        """Seed some basic facts for testing the bridge."""
        from bayan.bayan.logical_engine import Fact
        # Sun is hot
        self.engine.logical_engine.add_fact(Fact(Predicate("is_hot", [Term("Sun")])))
        # Ali is a person
        self.engine.logical_engine.add_fact(Fact(Predicate("is_person", [Term("Ali")])))

    def ask(self, question: str) -> str:
        """
        Main entry point: Ask a natural language question.
        Returns a natural language answer based on logic.
        """
        print(f"🗣️  User asked: {question}")
        
        # 1. Translate Natural -> Logic
        logic_query_str = self._translate_to_logic(question)
        print(f"🤔 Thought (Logic): {logic_query_str}")
        
        # Handle "fact" injection (Learning)
        if logic_query_str.startswith("fact"):
            try:
                from bayan.bayan.logical_engine import Fact
                content = logic_query_str.replace("fact", "").strip()
                pred_name = content.split('(')[0].strip()
                arg_str = content[content.find('(')+1 : content.rfind(')')]
                args = [Term(a.strip()) for a in arg_str.split(',')]
                
                self.engine.logical_engine.add_fact(Fact(Predicate(pred_name, args)))
                return f"I have learned that {arg_str} is {pred_name.replace('is_', '')}."
            except Exception as e:
                print(f"❌ Learning failed: {e}")
                return "I tried to learn that, but I got confused."

        if not logic_query_str.startswith("query"):
            return "I am not sure how to translate that to logic yet."

        # 2. Execute Logic
        try:
            content = logic_query_str.replace("query", "").strip()
            pred_name = content.split('(')[0].strip()
            arg_str = content[content.find('(')+1 : content.rfind(')')]
            args = [Term(a.strip()) for a in arg_str.split(',')]
            
            results = self.engine.logical_engine.query(Predicate(pred_name, args))
            success = len(results) > 0
        except Exception as e:
            print(f"❌ Logic execution failed: {e}")
            return "I encountered a logical error."

        # 3. Synthesize Answer (Logic -> Natural)
        answer = self._synthesize_answer(question, logic_query_str, success)
        return answer

    def _translate_to_logic(self, question: str) -> str:
        """
        Uses LLM (or Mock) to convert question to logical query.
        """
        prompt = f"Translate to logic: {question}"
        return self.llm.generate(prompt).strip()

    def _synthesize_answer(self, query: str, deduction_result: DeductionResult) -> str:
        """
        Converts the logical result back into natural language.
        Now uses the FactGenerator for stylistic variety.
        """
        success = deduction_result.success
        
        # New: Use Fact Generator for Voice
        try:
            from bayan.cognitive.fact_generator import FactGenerator
            generator = FactGenerator()
            
            if success:
                 # Generate a success statement
                 facts = deduction_result.trace_log # Use trace as 'facts'
                 return generator.generate_narrative(facts, style="philosophical")
            else:
                 return generator.generate_narrative(["The logic did not hold.", "The path was blocked."], style="analytical")
                 
        except ImportError:
            # Fallback if generator missing
            if success:
                return f"Logic Confirmed. {deduction_result.reasoning}"
            else:
                return "Logic could not be established."

if __name__ == "__main__":
    # Test
    bridge = CognitiveBridge()
    print("---")
    print("Answer:", bridge.ask("Is the sun hot?"))
    print("---")
    print("Answer:", bridge.ask("Who is Ali?"))
