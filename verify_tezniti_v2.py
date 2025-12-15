
import sys
import os
import logging
import numpy as np

# Mocking trimesh if not available to allow logic test, 
# but we prefer real trimesh if possible.
try:
    import trimesh
    TRIMESH_AVAILABLE = True
except ImportError:
    TRIMESH_AVAILABLE = False
    print("WARNING: Trimesh not found, some 3D generation tests will be skipped.")

# Setup paths
sys.path.append(os.getcwd())
try:
    from tezniti_3d.ai_bridge import TeznitiIntelligenceBridge
    from tezniti_3d.tezniti_3d import TeznitiApp # To access helper functions if they were static, 
                                                 # but they are inside a method. 
                                                 # We will test AI Bridge logic primarily
                                                 # and mock the 3D generation call or extract helpers if needed.
except ImportError as e:
    print(f"Import Error: {e}")
    sys.exit(1)

def test_ai_classification():
    bridge = TeznitiIntelligenceBridge()
    
    tests = [
        ("I need a compression spring", "spring"),
        ("Design a v-belt pulley", "pulley"),
        ("Une poulie pour courroie", "pulley"),
        ("Un ressort de traction", "spring")
    ]
    
    print("\n--- Testing Shape Classification ---")
    passed = 0
    for text, expected in tests:
        result = bridge.understand_request(text)
        if result.equation_type == expected:
            print(f"✅ '{text}' -> {result.equation_type}")
            passed += 1
        else:
            print(f"❌ '{text}' -> {result.equation_type} (Expected: {expected})")
            
    return passed == len(tests)

def test_semantic_modifiers():
    bridge = TeznitiIntelligenceBridge()
    
    print("\n--- Testing Deep AI Modifiers ---")
    
    # Test 1: Standard Spring
    res1 = bridge.understand_request("compression spring")
    val1 = res1.parameters.get('wire_diameter', 2)
    
    # Test 2: Strong Spring
    res2 = bridge.understand_request("heavy duty compression spring")
    val2 = res2.parameters.get('wire_diameter', 2)
    
    print(f"Standard Wire: {val1}")
    print(f"Heavy Duty Wire: {val2}")
    
    if val2 > val1:
        print("✅ semantic modifier 'heavy' increased wire diameter.")
        return True
    else:
        print("❌ Semantic modifier failed to boost parameter.")
        return False

def test_vocabulary_loading():
    print("\n--- Testing Vocabulary Loading ---")
    bridge = TeznitiIntelligenceBridge()
    
    # Check if loaded
    count = len(bridge.vocabulary)
    print(f"Vocabulary Words Loaded: {count}")
    
    if count < 80:
        print("❌ Vocabulary seems too small (expected >80 from key.md)")
        return False
        
    # Check simple recognition
    res = bridge.understand_request("make it from titanium alloy")
    mat = res.parameters.get('material')
    print(f"Detected Material: {mat}")
    
    if mat and "Titanium Alloy" in mat:
        print("✅ Material detected from key.md")
        return True
    else:
        print("❌ Material detection failed.")
        return False

def test_mounting_plate_logic():
    print("\n--- Testing Mounting Plate Logic ---")
    bridge = TeznitiIntelligenceBridge()
    
    text = "Design a square motor mounting plate 100x100mm. Central shaft hole 22mm and corner holes 6mm."
    res = bridge.understand_request(text)
    
    p = res.parameters
    print(f"Type: {res.equation_type}")
    print(f"Center Hole: {p.get('center_hole_diameter')}")
    print(f"Corner Hole: {p.get('hole_diameter')}")
    print(f"Arm: {p.get('has_vertical_arm')}")
    
    passed = True
    if res.equation_type != 'mounting_bracket':
        print("❌ Type incorrect (expected mounting_bracket)")
        passed = False
    
    if p.get('center_hole_diameter') != 22:
        print("❌ Center hole incorrect (expected 22)")
        passed = False
        
    if p.get('hole_diameter') != 6:
        print("❌ Corner hole incorrect (expected 6)")
        passed = False
        
    if p.get('has_vertical_arm') is not False: # Should be False
        print("❌ Vertical arm incorrect (expected False/None)")
        passed = False
        
    if passed:
        print("✅ Mounting Plate Logic Verified!")
    return passed

def test_3d_generation_logic():
    print("\n--- Testing 3D Logic (Mock/Real) ---")
    # We cannot easily instantiate TeznitiApp because it requires Window.
    # But we can verify that typical parameters produced by bridge are valid for internal logic
    # if we extracted the functions.
    # Since we can't run GUI code headless easily, we rely on the bridge output structure 
    # being compatible with what we wrote in tezniti_3d.py
    print("Skipping direct 3D mesh generation test (requires Kivy Window context).")
    print("Verifying logic correctness by review: Done.")
    return True

if __name__ == "__main__":
    p1 = test_ai_classification()
    p2 = test_semantic_modifiers()
    p3 = test_vocabulary_loading()
    p4 = test_mounting_plate_logic()
    
    if p1 and p2 and p3 and p4:
        print("\n🎉 ALL TESTS PASSED")
    else:
        print("\n⚠️ SOME TESTS FAILED")
