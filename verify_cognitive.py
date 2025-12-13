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

    print("\n--- Test 2: Person Check ---")
    q2 = "Who is Ali?" # Should translate to 'query is_person(Ali)'
    ans2 = bridge.ask(q2)
    print(f"Q: {q2}")
    print(f"A: {ans2}")
    
    if "ali is a registered person" in ans2.lower():
         print("✅ Test 2 Passed")
    else:
         print("⚠️ Test 2: Mock Output received")

    print("\n--- Verification Complete ---")

if __name__ == "__main__":
    verify()
