import sys
import os
import json

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bayan.bayan.reverse_glm import ReverseGLM

def main():
    print("=== Dynamic Circuit Builder Demo ===\n")
    print("Demonstrating on-the-fly circuit generation for inputs without pre-defined blueprints.\n")
    
    # Input text with NO known discourse markers
    # This should trigger the fallback to DynamicCircuitBuilder
    text = "السيارة تطير في السماء"  # "The car flies in the sky"
    
    print(f"Input Text: '{text}'")
    print("-" * 50)
    
    reverse_glm = ReverseGLM()
    circuits = reverse_glm.process_text(text)
    
    for i, circuit in enumerate(circuits):
        print(f"\nGenerated Circuit {i+1}:")
        print(f"  Source Segment: {circuit.get('source_text_segment')}")
        
        if "trace" in circuit:
            meta = circuit["trace"].get("meta", {})
            print(f"  Source: {meta.get('source')}")
            print(f"  Mode: {meta.get('mode')}")
            print(f"  Confidence: {meta.get('confidence')}")
            
            print("  Events:")
            for event in circuit["trace"].get("events", []):
                print(f"    - Action: {event.get('action')}")
                print(f"      Actors: {event.get('actors')}")
                print(f"      Context: {event.get('context')}")
        
        if "roles" in circuit:
            print("  Roles:")
            print(json.dumps(circuit["roles"], indent=4, ensure_ascii=False))

    print("\n" + "-" * 50)
    print("Demo Complete.")

if __name__ == "__main__":
    main()
