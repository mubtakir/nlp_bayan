
import sys
import os
import unittest

# Setup path
sys.path.append(os.getcwd())

from tezniti_3d.ai_bridge import TeznitiIntelligenceBridge

class TestMountingPlate(unittest.TestCase):
    def test_logic(self):
        bridge = TeznitiIntelligenceBridge()
        # Mock vocabulary to speed up if needed, but it's fast enough local
        
        text = "Design a square motor mounting plate 100x100mm. Central shaft hole 22mm and corner holes 6mm."
        print(f"Testing text: '{text}'")
        
        res = bridge.understand_request(text)
        params = res.parameters
        
        print(f"Result Type: {res.equation_type}")
        print(f"Params: {params}")
        
        self.assertEqual(res.equation_type, 'mounting_bracket', "Should be mounting_bracket")
        self.assertEqual(params.get('center_hole_diameter'), 22.0, "Center hole should be 22")
        self.assertEqual(params.get('hole_diameter'), 6.0, "Corner hole should be 6")
        self.assertEqual(params.get('has_vertical_arm'), False, "Should not have vertical arm")

if __name__ == '__main__':
    unittest.main()
