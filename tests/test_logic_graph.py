# import pytest
import sys
import os
sys.path.append(os.getcwd())
from bayan.bayan.logical_engine import LogicalEngine, Fact, Predicate, Term
from bayan.bayan.visualization import ExistentialVisualizer
from unittest.mock import MagicMock

def test_logic_trace():
    engine = LogicalEngine()
    # Add a simple rule: p(X) :- q(X).
    # Add a fact: q(a).
    
    # q(a)
    engine.add_fact(Fact(Predicate('q', [Term('a')])))
    
    # p(X) :- q(X)
    from bayan.bayan.logical_engine import Rule
    head = Predicate('p', [Term('X', is_variable=True)])
    body = [Predicate('q', [Term('X', is_variable=True)])]
    engine.add_rule(Rule(head, body))
    
    # Query p(a)
    goal = Predicate('p', [Term('a')])
    engine.query(goal)
    
    # Check trace
    assert len(engine.trace) > 0
    assert any("Goal: p(a)" in t for t in engine.trace)
    assert any("Applying rule" in t for t in engine.trace)
    assert any("✓ Solved" in t for t in engine.trace)

def test_contradiction_detection():
    engine = LogicalEngine()
    
    # Add conflicting facts: color(car, red) and color(car, blue)
    # Assuming last arg is value
    f1 = Fact(Predicate('color', [Term('car'), Term('red')]))
    f2 = Fact(Predicate('color', [Term('car'), Term('blue')]))
    
    engine.add_fact(f1)
    engine.add_fact(f2)
    
    contradictions = engine.check_contradictions()
    assert len(contradictions) == 1
    assert "conflicts with" in contradictions[0]

def test_graph_export():
    # Mock interpreter
    interpreter = MagicMock()
    engine = LogicalEngine()
    interpreter.logical = engine
    interpreter.logical_engine = engine # Fallback
    
    # Add some facts
    # link: friend(ali, omar)
    engine.add_fact(Fact(Predicate('friend', [Term('ali'), Term('omar')])))
    # node/prop: happy(ali)
    engine.add_fact(Fact(Predicate('happy', [Term('ali')])))
    
    viz = ExistentialVisualizer(interpreter)
    data = viz.export_d3_graph()
    
    nodes = data['nodes']
    links = data['links']
    
    # Check nodes
    node_ids = [n['id'] for n in nodes]
    assert 'ali' in node_ids
    assert 'omar' in node_ids
    assert 'ali_happy' in node_ids # Value node
    
    # Check links
    assert any(l['source'] == 'ali' and l['target'] == 'omar' and l['relationship'] == 'friend' for l in links)
    assert any(l['source'] == 'ali' and l['target'] == 'ali_happy' and l['relationship'] == 'is' for l in links)

if __name__ == "__main__":
    # Manual run if pytest not available
    try:
        test_logic_trace()
        print("test_logic_trace passed")
        test_contradiction_detection()
        print("test_contradiction_detection passed")
        test_graph_export()
        print("test_graph_export passed")
    except Exception as e:
        print(f"Tests failed: {e}")
        import traceback
        traceback.print_exc()
