"""
EntityEngine integration tests


- Creates entities and actions
- Applies action and verifies logical query sees updated state
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import importlib
# Ensure we import the local package, not any globally installed package with same name
import sys as _sys
_sys.modules.pop('bayan', None)
_sys.modules.pop('bayan.bayan', None)


from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter

def run(code: str):
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.traditional.set_source(code, filename=None)
    last = interp.interpret(ast)
    return interp, last


def test_entity_engine_action_updates_state_and_is_queryable():
    code = """
    # Create engine bound to logical engine
    engine = EntityEngine(logical)
    # Entities
    engine.create_entity("أحمد", states={"جوع": 0.6})
    engine.create_entity("محمد")
    # Define action on actor: تقديم_وجبة reduces target's جوع by 0.4 * action_value
    engine.define_action("محمد", "تقديم_وجبة", effects=[{"on": "جوع", "formula": "value - 0.4*action_value"}])
    # Apply: محمد يقدم وجبة لأحمد
    engine.apply_action("محمد", "تقديم_وجبة", "أحمد", action_value=1.0)

    # Query updated state via logic
    query state("أحمد", "جوع", ?V).
    """
    interp, result = run(code)
    assert isinstance(result, list) and result, "Expected non-empty query results"
    v = result[0].get('V')
    num = getattr(v, 'value', v)
    assert abs(num - 0.2) < 1e-6, f"Expected hunger 0.2, got {v}"


def test_entity_engine_reaction_response():
    code = """
    engine = EntityEngine(logical)
    # Target has a reaction to this action: increase سعادة by sensitivity * 0.3
    engine.create_entity("أحمد", states={"جوع": 0.6}, reactions={"تقديم_وجبة": {"sensitivity": 0.7, "response": "سعادة += sensitivity*0.3"}})
    engine.create_entity("محمد")

    engine.define_action("محمد", "تقديم_وجبة", effects=[{"on": "جوع", "formula": "value - 0.4*action_value"}])
    engine.apply_action("محمد", "تقديم_وجبة", "أحمد", action_value=1.0)

    # Check سعادة increase: 0.5 default + 0.21 = 0.71
    query state("أحمد", "سعادة", ?S).
    """
    interp, resS = run(code)
    assert resS, "Expected non-empty query results"
    s = resS[0]['S']
    sval = getattr(s, 'value', s)
    assert abs(sval - 0.71) < 1e-6




def test_numeric_property_unbounded_and_bounded_state_clamping():
    code = """
    engine = EntityEngine(logical)
    # Numeric property: x should be unbounded
    engine.create_entity("Ball", properties={"x": {"type": "numeric", "value": 10.0}})
    engine.create_entity("Mover")
    engine.define_action("Mover", "move_x", effects=[{"on": "x", "formula": "value + 5.0*action_value"}])
    engine.apply_action("Mover", "move_x", "Ball", action_value=3.0)  # x = 25.0

    # Bounded state: temperature clamped to [-273, 1000]
    engine.create_entity("Thermo", states={"temperature": {"type": {"bounded": [-273.0, 1000.0]}, "value": 0.0}})
    engine.define_action("Mover", "cool", effects=[{"on": "temperature", "formula": "value - 300*action_value"}])
    engine.apply_action("Mover", "cool", "Thermo", action_value=1.0)

    query property("Ball", "x", ?X).
    """
    interp, res_prop = run(code)
    assert res_prop, "Expected property query results"
    X = res_prop[0]['X']
    xv = getattr(X, 'value', X)
    assert abs(xv - 25.0) < 1e-6

    # Now query temperature state (should be clamped at -273)
    code2 = """
    query state("Thermo", "temperature", ?T).
    """
    interp.traditional.set_source(code2, filename=None)
    ast2 = HybridParser(HybridLexer(code2).tokenize()).parse()
    res_temp = interp.interpret(ast2)
    assert res_temp, "Expected temperature state query results"
    T = res_temp[0]['T']
    tv = getattr(T, 'value', T)
    assert abs(tv + 273.0) < 1e-6


def test_default_fuzzy_clamp_still_applies_for_plain_numbers():
    code = """
    engine = EntityEngine(logical)
    engine.create_entity("Ahmed", states={"hunger": 0.9})
    engine.create_entity("John")
    engine.define_action("John", "feed", effects=[{"on": "hunger", "formula": "value + 0.5"}])
    engine.apply_action("John", "feed", "Ahmed", action_value=1.0)

    query state("Ahmed", "hunger", ?V).
    """
    _, res = run(code)
    assert res, "Expected state query results"
    V = res[0]['V']
    vv = getattr(V, 'value', V)
    assert abs(vv - 1.0) < 1e-6



def test_perform_action_multi_actors_self_target_and_preassignments():
    code = """
    engine = EntityEngine(logical)
    # Define actions on actors: move increases x by sensitivity*delta
    engine.create_entity("A", properties={"x": {"type": "numeric", "value": 0.0}})
    engine.define_action("A", "move", effects=[{"on": "x", "formula": "value + 10*sensitivity"}])

    engine.create_entity("B", properties={"x": {"type": "numeric", "value": 1.0}})
    engine.define_action("B", "move", effects=[{"on": "x", "formula": "value + 10*sensitivity"}])

    # Pre-assign via perform: set B.x to 5 before moving
    res = engine.perform_action("move", participants=[("A", 1.0), ("B", 0.5)], properties=[("B", "x", 5.0)])

    query property("A", "x", ?XA).
    """
    interp, resA = run(code)
    assert resA, "Expected results for A.x"
    XA = getattr(resA[0]['XA'], 'value', resA[0]['XA'])
    # A: 0 + 10*1.0 = 10
    assert abs(XA - 10.0) < 1e-6

    # Query B.x
    code2 = """
    query property("B", "x", ?XB).
    """
    interp.traditional.set_source(code2, filename=None)
    ast2 = HybridParser(HybridLexer(code2).tokenize()).parse()
    resB = interp.interpret(ast2)
    XB = getattr(resB[0]['XB'], 'value', resB[0]['XB'])
    # B pre-assigned to 5, then + 10*0.5 = 10
    assert abs(XB - 10.0) < 1e-6
