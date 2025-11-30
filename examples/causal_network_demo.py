"""
Causal Network Integration Demo
===============================

Demonstrates how the Causal Semantic Network enhances the Generative Model
by suggesting logical story flows and inferring consequences.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../bayan'))

from bayan.generative_model import GenerativeLanguageModel

def print_separator(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def main():
    model = GenerativeLanguageModel()
    
    print_separator("BAYAN CAUSAL NETWORK INTEGRATION")
    print("Using causal logic to drive word generation")

    # Scenario 1: Inferring from "Appearance" (Start of 'Star')
    start_concept = "appearance"
    print_separator(f"1. Suggesting completion for: '{start_concept}'")
    
    suggestions = model.suggest_story_completion(start_concept)
    print(f"Suggested Events: {suggestions['events']}")
    print(f"Suggested Results: {suggestions['results']}")
    
    if suggestions['events'] and suggestions['results']:
        event = suggestions['events'][0]
        result = suggestions['results'][0]
        print(f"\n-> Auto-generating word for story: {start_concept} -> {event} -> {result}")
        
        word_data = model.generate_from_story(start_concept, event, result)
        print(f"Generated Word: {word_data['word']}")
        print("Explanation:")
        for step in word_data['explanation']:
            print(f"  - {step}")

    # Scenario 2: Inferring from "Branching" (Start of 'Tree')
    start_concept = "branching"
    print_separator(f"2. Suggesting completion for: '{start_concept}'")
    
    # Note: In our init data, branching REQUIRES gathering, which enables flow -> fruit
    # The simple suggest_scenario_completion looks for consequences.
    # Let's see what it finds based on the graph we built.
    suggestions = model.suggest_story_completion(start_concept)
    # Since 'requires' isn't strictly 'leads_to' in our simple inference, we might need to adjust logic
    # or just check what relations exist.
    
    # Let's manually check relations for demonstration
    print("Direct relations from 'branching':")
    relations = model.network.get_relations("branching")
    for r in relations:
        print(f"  - {r.type.value} -> {r.target}")
        
    # Let's try to generate 'Tree' knowing the path (Branching -> Gathering -> Flow -> Fruit)
    print("\n-> Generating 'Tree' from full 4-step story:")
    # Use the new custom scenario builder for 4 steps
    tree_scenario = model.scenario_builder.build_custom_scenario([
        ("Start", "branching"),
        ("Event 1", "gathering"),
        ("Event 2", "flow"),
        ("Result", "fruit")
    ])
    word_data = model.scenario_builder.generate_word(tree_scenario)
    print(f"Generated Word: {word_data['word']}")

    # Scenario 3: Causal Chain Analysis
    print_separator("3. Analyzing Causal Chain: Seeing -> Relief")
    chains = model.network.find_causal_chain("seeing", "relief")
    for i, chain in enumerate(chains):
        print(f"Chain {i+1}: {' -> '.join(chain)}")
        
    print("\n-> This chain corresponds to 'Morning' (صبح)")
    print("\n-> This chain corresponds to 'Morning' (صبح)")
    word_data = model.generate_from_story("seeing", "effort", "relief")
    
    if "error" in word_data:
        print(f"Error: {word_data['error']}")
    else:
        print(f"Generated Word: {word_data['word']}")
        print("Explanation:")
        for step in word_data['explanation']:
            print(f"  - {step}")

if __name__ == "__main__":
    main()
