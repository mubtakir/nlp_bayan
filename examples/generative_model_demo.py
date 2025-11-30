"""
Generative Model Demo
=====================

Demonstrates the capability of the Bayan Generative Language Model
to construct words based on logical scenarios (Stories).
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
    
    print_separator("BAYAN GENERATIVE MODEL - SCENARIO BUILDER")
    print("Generating words from logical stories (Start -> Event -> Result)")

    # Test Case 1: Star (نجم)
    # Story: Something appears (Start), is gathered/solid (Event), but is unknown/hidden (Result)
    print_separator("Case 1: Generating 'Star' (نجم)")
    print("Story: Appearance -> Gathering -> Unknown")
    
    result = model.generate_from_story(
        start="appearance",
        event="gathering",
        result="unknown"
    )
    
    print(f"\nGenerated Word: {result['word']}")
    print("Explanation:")
    for step in result['explanation']:
        print(f"  - {step}")

    # Test Case 2: Tree (شجرة)
    # Story: Branching (Start) -> Gathering (Event) -> Flow (Event 2) -> Fruit (Result)
    # Note: Our simple builder does 3 steps, let's try to map it or analyze it
    print_separator("Case 2: Analyzing 'Tree' (شجرة)")
    analysis = model.analyze_word_story("شجرة")
    
    print(f"Word: {analysis['word']}")
    print("Story Analysis:")
    for step in analysis['story']:
        print(f"  - {step['letter']} ({step['stage']}): {', '.join(step['meanings'][:3])}...")

    # Test Case 3: Pen (قلم)
    # Story: Precision (Start) -> Pulling (Event) -> Containing (Result)
    print_separator("Case 3: Generating 'Pen' (قلم)")
    print("Story: Precision -> Pulling -> Containing")
    
    result = model.generate_from_story(
        start="precision",
        event="pulling",
        result="containing"
    )
    
    print(f"\nGenerated Word: {result['word']}")
    print("Explanation:")
    for step in result['explanation']:
        print(f"  - {step}")

    # Test Case 4: Generosity (كرم)
    # Story: Giving (Start) -> Flow (Event) -> Containing/Praise (Result)
    print_separator("Case 4: Generating 'Generosity' (كرم)")
    print("Story: Giving -> Flow -> Containing")
    
    result = model.generate_from_story(
        start="giving",
        event="flow",
        result="containing"
    )
    
    print(f"\nGenerated Word: {result['word']}")
    print("Explanation:")
    for step in result['explanation']:
        print(f"  - {step}")

if __name__ == "__main__":
    main()
