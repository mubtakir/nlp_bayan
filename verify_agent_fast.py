import sys
import os
from unittest.mock import MagicMock

# Mock heavy dependencies BEFORE importing modules that use them
sys.modules['bayan.bayan.istinbat_engine'] = MagicMock()
sys.modules['bayan.bayan.logical_engine'] = MagicMock()
sys.modules['bayan.bayan.generative_model'] = MagicMock()

# Now import the logic we want to test
# Ensure path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from bayan.bayan.cognitive.thinking_loop import ThinkingLoop, AgentState
from bayan.bayan.cognitive.logic_police import LogicPolice
# We can't import CognitiveBridge easily if it imports IstinbatEngine which we mocked as MagicMock object,
# but we want to test CognitiveBridge's logic too?
# Actually CognitiveBridge needs to be tested. 
# Let's import it, but its imports of IstinbatEngine will get the Mock.

# Mocking the specific classes inside the mocked modules to behave as expected
mock_istinbat = sys.modules['bayan.bayan.istinbat_engine']
mock_istinbat.IstinbatEngine = MagicMock
mock_istinbat.Predicate = MagicMock
mock_istinbat.Term = MagicMock
mock_istinbat.Fact = MagicMock
# DeductionResult is needed?
mock_istinbat.DeductionResult = MagicMock

from bayan.bayan.cognitive.cognitive_bridge import CognitiveBridge

class MockMind:
    def __init__(self):
        self.bridge = CognitiveBridge()
        # Mock bridge methods to return strings directly to avoid LLM/Engine logic
        self.bridge.ask = MagicMock(side_effect=self._mock_ask)
        self.engine = MagicMock() # Mock Engine
        self.police = LogicPolice(self.engine)
        self.loop = ThinkingLoop(self, interval=0)
    
    def _mock_ask(self, input_text):
        if "sun" in input_text and "cold" in input_text:
             # Learning logic would happen here in real bridge
             return "I have learned that Sun is cold."
        if "moon" in input_text and "cold" in input_text:
             return "I have learned that Moon is cold."
        return f"Mock Answer to: {input_text}"

    def interact(self, text):
        self.loop.trigger_thought(text)

def verify():
    print("🚀 Running Verify Agent Fast...")
    mind = MockMind()
    
    # Test 1: Contradiction
    print("\n--- Test 1: Contradiction Check ---")
    print("Input: 'The sun is cold.'")
    mind.interact("The sun is cold.")
    
    # Check if Police caught it
    # We inspect the stdout manually for now, or check internal state if possible?
    # LogicPolice.check_thought is what we want to verify.
    # It checks string "sun...cold".
    
    verdict = mind.police.check_thought("The sun is cold.")
    print(f"Manual Police Check: {verdict}")
    if "contradicts" in verdict:
        print("✅ SUCCESS: Logic Police caught the sun contradiction.")
    else:
        print(f"❌ FAILURE: Logic Police missed it: {verdict}")

    print("\n--- Test 2: Safe Statement ---")
    mind.interact("The moon is cold.")
    verdict2 = mind.police.check_thought("The moon is cold.")
    print(f"Manual Police Check: {verdict2}")
    if verdict2 == "SAFE":
        print("✅ SUCCESS: Logic Police allowed safe statement.")
    else:
        print("❌ FAILURE: Logic Police rejected safe statement.")

if __name__ == "__main__":
    verify()
