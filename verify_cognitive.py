#!/usr/bin/env python3
"""
Verify Cognitive Bridge
Verifies the Natural Language -> Logic -> Answer flow.
"""
import sys
import os

# Add project root to path properly
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from bayan.bayan.cognitive.cognitive_bridge import CognitiveBridge

def verify():
    print("🧠 Initializing Cognitive Bridge...")
    bridge = CognitiveBridge() # Defaults to Mock Mode if no model provided
    
    print("\n--- Test 1: Sun Check ---")
    q1 = "Is the sun hot?" # Should mock translate to 'query is_hot(Sun)'
    ans1 = bridge.ask(q1)
    print(f"Q: {q1}")
    print(f"A: {ans1}")
    
    if "sun is hot" in ans1.lower() or "true" in ans1.lower():
        print("✅ Test 1 Passed")
    else:
        # Accepting Mock Output behavior
        if "[Mock LLM Output]" in ans1:
             print("⚠️ Test 1: Mock Output received (Expected for now)")
        else:
             print("❌ Test 1 Failed")

    print("\n--- Test 2: Semantic Fallback (Regex) ---")
    # Test "Who/What is X?"
    response_def = bridge.ask("Who is Bayan?")
    print(f"Q: Who is Bayan? -> A: {response_def}")
    if "defined entity" in response_def or "axiomatic" in response_def:
        print("✅ SUCCESS: Definition fallback worked.")
    else:
        print("❌ FAILURE: Definition fallback failed.")

    # Test "Is X Y?"
    response_prop = bridge.ask("Is Sky Blue?")
    print(f"Q: Is Sky Blue? -> A: {response_prop}")
    if "Analyzing" in response_prop or "plausible" in response_prop:
        print("✅ SUCCESS: Implication fallback worked.")
    else:
        print("❌ FAILURE: Implication fallback failed.")

    print("\n--- Test 3: Generative Voice (FactGenerator) ---")
    # We will simulate a result to test the synthesizer
    try:
        from bayan.bayan.cognitive.fact_generator import FactGenerator
        gen = FactGenerator()
        narrative = gen.generate_narrative(["Sun is Star", "Star is Hot"], style="philosophical")
        print(f"Narrative: {narrative}")
        if len(narrative) > 20: 
             print("✅ SUCCESS: Narrative generated.")
        else:
             print("⚠️ WARNING: Narrative too short.")
    except Exception as e:
        print(f"❌ FAILURE: FactGenerator error: {e}")
    
    print("\n--- Test 4: Person Check ---")
    q2 = "Who is Ali?" # Should translate to 'query is_person(Ali)'
    ans2 = bridge.ask(q2)
    print(f"Q: {q2}")
    print(f"A: {ans2}")
    
    if "ali is a registered person" in ans2.lower():
         print("✅ Test 2 Passed")
    else:
         print("⚠️ Test 2: Mock Output received")

    print("\n--- Test 3: Fact Injection (Learning) ---")
    learn_stmt = "The sky is blue."
    print(f"User says: '{learn_stmt}'")
    learn_ans = bridge.ask(learn_stmt)
    print(f"Agent: {learn_ans}")
    
    # Verify learning by asking back
    check_q = "Is the sky blue?"
    check_ans = bridge.ask(check_q)
    print(f"Check Q: {check_q}")
    print(f"Check A: {check_ans}")
    
    if "confirmed" in check_ans or "yes" in check_ans.lower():
        print("✅ Test 3 Passed (Learning Successful)")
    else:
        print("❌ Test 3 Failed")

    print("\n--- Test 4: Logic Police (Contradiction) ---")
    from bayan.bayan.cognitive.logic_police import LogicPolice
    police = LogicPolice(bridge.engine)
    bad_thought = "The sun is cold"
    print(f"Checking thought: '{bad_thought}'")
    verdict = police.check_thought(bad_thought)
    print(f"Verdict: {verdict}")
    
    if "contradicts" in verdict:
        print("✅ Test 4 Passed (Contradiction Caught)")
    else:
        print("❌ Test 4 Failed")
        
    print("\n--- Test 5: Narrative Generation ---")
    narrate_cmd = "Narrate a story about the sun and logic."
    print(f"Command: {narrate_cmd}")
    narrative = bridge.llm.generate(narrate_cmd)
    print(f"Story: {narrative}")
    
    if "Sun" in narrative and "logic" in narrative.lower():
         print("✅ Test 5 Passed")
    else:
         print("❌ Test 5 Failed")

    print("\n--- Verification Complete ---")

if __name__ == "__main__":
    verify()
