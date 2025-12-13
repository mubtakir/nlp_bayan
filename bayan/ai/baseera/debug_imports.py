
import sys
import os
import traceback

# Add root to path
sys.path.append(os.getcwd())

print("Attempting to import advanced.enhanced_revolutionary_inference_system...")
try:
    from advanced import enhanced_revolutionary_inference_system
    print("Success!")
except Exception:
    traceback.print_exc()

print("\nAttempting to import advanced.revolutionary_image_inference_system...")
try:
    from advanced import revolutionary_image_inference_system
    print("Success!")
except Exception:
    traceback.print_exc()
