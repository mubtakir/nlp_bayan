import sys
import os

# Ensure path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from tezniti_3d.ai_bridge import TeznitiIntelligenceBridge

def test():
    bridge = TeznitiIntelligenceBridge()
    text = "Design a square motor mounting plate with dimensions 100 mm by 100 mm and thickness of 8 mm"
    print(f"Testing: {text}")
    result = bridge._classify_rule_based(text)
    print(f"Type: {result.equation_type}")
    print(f"Params: {result.parameters}")
    
    if result.parameters.get('length') == 100 and result.parameters.get('width') == 100:
        print("SUCCESS")
    else:
        print("FAIL")

if __name__ == "__main__":
    test()
