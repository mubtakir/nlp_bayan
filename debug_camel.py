from bayan.bayan.arabic_adapter import ArabicNLPAdapter
import sys

print("Initializing Adapter...")
try:
    adapter = ArabicNLPAdapter()
    print(f"Analyzer loaded: {adapter.morphology_analyzer is not None}")
    if adapter.morphology_analyzer:
        print("Analyzer is ready.")
        print(f"Test 'مدرسة': {adapter.extract_root('مدرسة')}")
    else:
        print("Analyzer failed to load.")
except Exception as e:
    print(f"Error: {e}")
