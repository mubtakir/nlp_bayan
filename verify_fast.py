
import sys
import os

# Mock the heavy imports to avoid hanging
import sys
from unittest.mock import MagicMock
sys.modules['bayan.bayan.istinbat_engine'] = MagicMock()
sys.modules['bayan.bayan.logical_engine'] = MagicMock()

# Add directory to path
sys.path.append('/home/al-mubtakir/bayan_python_ide22/tezniti_3d')
from ai_bridge import TeznitiIntelligenceBridge

def verify_fast():
    print("Initializing Bridge (Mocked)...")
    bridge = TeznitiIntelligenceBridge()
    
    if hasattr(bridge, '_classify_rule_based'):
        print("✅ SUCCESS: Method _classify_rule_based exists")
    else:
        print("❌ FAILURE: Method _classify_rule_based MISSING")

    if hasattr(bridge, 'understand_request'):
        print("✅ SUCCESS: Method understand_request exists")
    else:
        print("❌ FAILURE: Method understand_request MISSING")

    # --- Test 3: Motor Mounting Plate (Regression Test) ---
    print("\nTest 3: Motor Mounting Plate (100x100x8)")
    text = "Design a square motor mounting plate with dimensions 100 mm by 100 mm and thickness of 8 mm"
    result = bridge._classify_rule_based(text)
    
    print(f"Result Type: {result.equation_type}")
    print(f"Params: {result.parameters}")
    
    if result.equation_type == 'plate':
        l = result.parameters.get('length', 0)
        w = result.parameters.get('width', 0)
        t = result.parameters.get('thickness', 0)
        
        # We expect 100, 100, 8
        if l == 100 and w == 100 and t == 8:
            print("✅ PASS: Plate dimensions extracted correctly.")
        else:
            print(f"❌ FAIL: Expected 100x100x8, got {l}x{w}x{t}")
    else:
        print(f"❌ FAIL: Incorrect type. Expected 'plate', got '{result.equation_type}'")

    # Run logic test
    print("\n--- Logic Test: Coupling ---")
    text = "Create a cylindrical shaft coupling with an outer diameter of 50 mm, length of 40 mm, and a central bore of 20 mm diameter. The wall thickness should be uniform."
    try:
        result = bridge._classify_rule_based(text, [])
        print(f"Result Type: {result.equation_type}")
        print(f"Params: {result.parameters}")
        
        if result.equation_type == 'pipe': # Coupling maps to Pipe
             print("✅ LOGIC VALID: Identified as pipe (coupling)")
             
             p = result.parameters
             if p.get('outer_diameter') == 50 and p.get('length') == 40 and p.get('inner_diameter') == 20:
                 print("✅ PARAMETERS VALID: OD=50, L=40, ID=20")
                 if p.get('thickness') == 15.0:
                     print("✅ THICKNESS CALCULATED: 15.0")
                 else:
                     print(f"❌ THICKNESS WRONG: {p.get('thickness')}")
             else:
                 print(f"❌ PARAMETERS INVALID: {p}")
        else:
             print(f"❌ LOGIC INVALID: {result.equation_type}")
    except Exception as e:
        print(f"❌ EXECUTION ERROR: {e}")

if __name__ == "__main__":
    verify_fast()
