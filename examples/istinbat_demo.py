import sys
import os
import json

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bayan.bayan.istinbat_engine import IstinbatEngine

def main():
    print("=== Istinbat Engine (Deep Inference) Demo ===\n")
    print("Demonstrating the unified pipeline: Text -> Equation -> Causal Logic -> Entity State -> Circuit.\n")
    
    # Input text supported by the basic KnowledgeBase
    text = "أحمد ضرب الكرة"  # "Ahmed hit the ball"
    
    print(f"Input Text: '{text}'")
    print("-" * 50)
    
    engine = IstinbatEngine()
    result = engine.process(text)
    
    if result:
        print("\n1. Linguistic Equation:")
        print(f"   Event: {result.equation.event} ({result.equation.event_type})")
        print(f"   Entities: {result.equation.entities}")
        
        print("\n2. Causal Consequences (Inferred):")
        for consequence in result.consequences:
            print(f"   - {consequence.entity_name}: {consequence.state_changes}")
            
        print("\n3. Generated Conceptual Circuit:")
        # Pretty print the circuit trace
        trace = result.circuit.get("trace", {})
        print(json.dumps(trace, indent=4, ensure_ascii=False))
        
    else:
        print("Failed to process text.")

    print("\n" + "-" * 50)
    print("Demo Complete.")

if __name__ == "__main__":
    main()
