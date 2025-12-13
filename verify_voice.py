#!/usr/bin/env python3
"""
Verify Generative Voice
Verifies the Fact-Informed Generator and Semantic Fallback.
"""
import sys
import os

# Ensure import paths
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from bayan.bayan.cognitive.llm_interface import LLMInterface
from bayan.bayan.cognitive.fact_generator import FactGenerator
from bayan.bayan.logical_engine import Fact, Predicate, Term

def verify():
    print("🗣️  Initializing Generative Voice...")
    
    # 1. Initialize Interface (Will likely use Semantic Fallback if no model)
    llm = LLMInterface() 
    
    # 2. Initialize Generator
    gen = FactGenerator(llm)
    
    # 3. Create some facts to narrate
    print("\n--- Test 1: Fact-Informed Narrative ---")
    facts = [
        Fact(Predicate("is_hot", [Term("Sun")])),
        Fact(Predicate("gives_light", [Term("Sun")])),
        Fact(Predicate("is_star", [Term("Sun")]))
    ]
    
    print("Facts:")
    for f in facts:
        print(f"  - {f}")
        
    print("\nGenerating Narrative (Style: Philosophical)...")
    narrative = gen.generate_narrative(facts, style="philosophical")
    print(f"OUTPUT: {narrative}")
    
    # Check if we got something specific to the fallback keywords
    if "Sun" in narrative or "Shams" in narrative or "mock" in narrative.lower():
        print("✅ Narrative Generated (Content Check Passed)")
    else:
        print("⚠️  Narrative generic or empty")

    # 4. Direct Generation
    print("\n--- Test 2: Direct Prompting ---")
    direct_out = llm.generate("Narrate the truth about logic.")
    print(f"OUTPUT: {direct_out}")
    if "Logic" in direct_out:
        print("✅ Direct Generation Passed")
    else:
        print("⚠️ Direct Generation ambiguous")

    print("\n--- Verification Complete ---")

if __name__ == "__main__":
    verify()
