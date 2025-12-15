
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'tezniti_3d')))
sys.path.append(os.getcwd())

# Mock Bayan Engine import if needed
import tezniti_3d.ai_bridge as ai_bridge

def verify_logic():
    print("Testing User Case Isolation...")
    bridge = ai_bridge.TeznitiIntelligenceBridge()
    
    text_complex = "Design a mechanical mounting bracket with a rectangular base of 120 mm length, 80 mm width, and 10 mm thickness. Add four bolt holes of 10 mm diameter, positioned 15 mm from each corner. Include a vertical support arm 80 mm high, 60 mm wide, and 10 mm thick."
    print(f"\n   Input User Case: '{text_complex}'")
    
    result = bridge.understand_request(text_complex)
    print(f"   Result: Type={result.equation_type}")
    print(f"   Reasoning: {result.reasoning}")
    
    if result.equation_type == 'mounting_bracket':
         print("   ✅ SUCCESS: Identified as mounting_bracket.")
    else:
         print(f"   ❌ FAILURE: Identified as {result.equation_type}.")

if __name__ == "__main__":
    verify_logic()
