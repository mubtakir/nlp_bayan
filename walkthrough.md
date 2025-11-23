# Graphical System Enhancements

## Overview
I have investigated the graphical system and enhanced it to fully support the concepts you asked about: Entities, Causal Networks, Probabilities, and Events.

## Changes Implemented

### 1. Visualization Engine (`bayan/bayan/visualization.py`)
- **Probabilities**: Added `probability` field to the exported graph links.
- **Causal Networks (Rules)**: Added logic to visualize `Rule` objects as distinct nodes (Group 4) connecting condition predicates to result predicates. This visualizes the "Event-Result" and "Causal" structure.

### 2. Web IDE Frontend (`web_ide/templates/logic_graph.html`)
- **Probability Visualization**: Links now use `stroke-opacity` and `stroke-dasharray` to represent probability. Lower probability facts appear fainter and dashed, visually representing "Skepticism" or "Doubt".
- **Rule Visualization**: Added styling for Rule nodes (Purple) to distinguish them from standard entities (Green) and events (Blue).

### 3. Logical Engine (`bayan/bayan/logical_engine.py`)
- **Proof Graph Export**: Added `export_proof_graph` method to the `LogicalEngine` class. This allows converting a dynamic proof trace into a D3 graph, paving the way for visualizing the *execution* of causal networks in the future (in addition to the static rule structure).

## Verification
- Created a debug script `debug_visualization.py` to verify the JSON export.
- Confirmed that:
    - Probabilistic facts (e.g., `color(sky, blue) [0.7]`) are exported with `probability: 0.7`.
    - Rules (e.g., `writes_code(X) :- programmer(X)`) are exported as `IMPLIES` nodes connecting `programmer` to `writes_code`.

## Conclusion
The graphical system now covers:
- **Entities**: Nodes (Green)
- **Facts**: Links
- **Events**: Nodes (Blue)
- **Causal Networks**: Rule Nodes (Purple) & Links
- **Probabilities/Skepticism**: Visual Styles (Opacity/Dashing)
