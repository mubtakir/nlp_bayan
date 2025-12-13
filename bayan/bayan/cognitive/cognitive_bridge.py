import sys
import os

# Ensure we can import bayan packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from bayan.bayan.istinbat_engine import IstinbatEngine, Predicate, Term
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
        
        if not logic_query_str.startswith("query"):
            return "I am not sure how to translate that to logic yet."

        # 2. Execute Logic
        # Parse "query pred(arg)" -> simple parsing for now
        # logic_query_str expected format: "query is_hot(Sun)"
        try:
            content = logic_query_str.replace("query", "").strip()
            pred_name = content.split('(')[0]
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

    def _synthesize_answer(self, question: str, logic: str, success: bool) -> str:
        """
        Uses LLM (or Mock) to form a nice sentence.
        """
        status = "True" if success else "False"
        prompt = f"Translate to natural: Question='{question}', Logic='{logic}', Result='{status}'"
        return self.llm.generate(prompt).strip()

if __name__ == "__main__":
    # Test
    bridge = CognitiveBridge()
    print("---")
    print("Answer:", bridge.ask("Is the sun hot?"))
    print("---")
    print("Answer:", bridge.ask("Who is Ali?"))
