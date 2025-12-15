
import sys
import os

# Add directory to path
sys.path.append('/home/al-mubtakir/bayan_python_ide22/tezniti_3d')
from ai_bridge import TeznitiIntelligenceBridge

def verify():
    print("Initializing Bridge...")
    bridge = TeznitiIntelligenceBridge()
    
    print("\n--- Test 1: User's Complex Prompt ---")
    text = "Design a mechanical mounting bracket with a rectangular base of 120 mm length, 80 mm width, and 10 mm thickness. Add four bolt holes of 10 mm diameter, positioned 15 mm from each corner. Include a vertical support arm 80 mm high, 60 mm wide, and 10 mm thick."
    print(f"Input: {text[:50]}...")
    result = bridge.understand_request(text)
    print(f"Result Type: {result.equation_type}")
    print(f"Reasoning: {result.reasoning}")
    
    if result.equation_type == 'mounting_bracket':
        print("✅ SUCCESS: Correctly identified as mounting_bracket")
        # Check params
        p = result.parameters
        if p.get('base_length') == 120 and p.get('hole_diameter') == 10:
             print("✅ PARAMETERS: Extracted correctly (120mm, 10mm)")
        else:
             print(f"⚠️ PARAMETERS: Values might be off: {p}")
    else:
        print(f"❌ FAILURE: Identified as {result.equation_type}")

    print("\n--- Test 2: Conflict 'Bracket for mounting a bolt' ---")
    text2 = "Bracket for mounting a bolt"
    res2 = bridge.understand_request(text2)
    print(f"Result Type: {res2.equation_type}")
    if res2.equation_type in ['bracket', 'mounting_bracket']:
        print("✅ SUCCESS: Priority Correct")
    else:
        print(f"❌ FAILURE: Priority Incorrect ({res2.equation_type})")
        
    print("\n--- Test 3: Fallback Behavior ---")
    if hasattr(bridge, '_classify_rule_based'):
        print("✅ SUCCESS: Method _classify_rule_based exists")
    else:
        print("❌ FAILURE: Method _classify_rule_based MISSING")
        
    # To test fallback, force mock logic if possible, or just rely on the fact that engine might be fake
    # We can check if reasoning contains "Bayan Logic" which is from our new classifier
    if "Bayan Logic" in result.reasoning:
        print("✅ SUCCESS: Used _classify_rule_based logic")
    else:
        print("⚠️ WARNING: Did not see expected reasoning signature")

if __name__ == "__main__":
    verify()
