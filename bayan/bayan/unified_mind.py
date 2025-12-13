import sys
import os

# Ensure import paths
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from bayan.bayan.cognitive.cognitive_bridge import CognitiveBridge
from bayan.bayan.cognitive.logic_police import LogicPolice
from bayan.bayan.cognitive.thinking_loop import ThinkingLoop
from bayan.bayan.istinbat_engine import IstinbatEngine

class UnifiedMind:
    """
    The General Artificial Intelligence (Genius AI).
    Integrates Logic, Intuition, Voice, and Agency.
    """
    def __init__(self):
        print("🌌 Awakening Unified Mind...")
        
        # 1. The Core Brain (Logic + Neural)
        self.engine = IstinbatEngine()
        # Seed basic knowledge for demo
        from bayan.bayan.logical_engine import Fact, Predicate, Term
        self.engine.logical_engine.add_fact(Fact(Predicate("is_hot", [Term("Sun")])))
        self.engine.logical_engine.add_fact(Fact(Predicate("is_person", [Term("Ali")])))
        
        # 2. The Translator
        self.bridge = CognitiveBridge()
        # Share the same engine instance!
        self.bridge.engine = self.engine 
        
        # 3. The Conscience
        self.police = LogicPolice(self.engine)
        
        # 4. The Consciousness Loop
        self.loop = ThinkingLoop(self)
        
        print("✨ Unified Mind is Online.")

    def interact(self, user_input: str):
        """
        The main interface for humans.
        Triggers the thinking loop.
        """
        self.loop.trigger_thought(user_input)

if __name__ == "__main__":
    mind = UnifiedMind()
    mind.interact("Is the sun hot?")
    print("-" * 20)
    mind.interact("Who is Ali?")
