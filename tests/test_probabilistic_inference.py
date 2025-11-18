# -*- coding: utf-8 -*-
"""
Probabilistic inference: ensure fact[prob] propagates into query solutions and through rules.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'bayan'))

from bayan.hybrid_interpreter import HybridInterpreter
from bayan.lexer import HybridLexer
from bayan.parser import HybridParser
from bayan.logical_engine import Predicate, Term


def run(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    return interp


def test_probabilities_on_facts_and_rules():
    code = u'''
    hybrid {
      fact[0.9] parent("john", "mary").
      fact[0.6] parent("mary", "susan").
      fact[0.3] parent("john", "alex").

      grandparent(?X, ?Z) :- parent(?X, ?Y), parent(?Y, ?Z).
    }
    '''
    interp = run(code)

    # Query single-step facts: parent(john, ?C)
    sols = interp.logical.query(Predicate('parent', [Term('john'), Term('C', True)]))
    # Extract mapping of child -> probability (dereferencing Terms)
    facts = {}
    for s in sols:
        raw = s.bindings.get('C')
        try:
            resolved = interp.logical._deref(raw, s)
        except Exception:
            resolved = raw
        child = getattr(resolved, 'value', resolved)
        facts[child] = getattr(s, 'probability', 1.0)
    # We expect two children mary (0.9) and alex (0.3)
    assert abs(facts.get('mary', 0.0) - 0.9) < 1e-9
    assert abs(facts.get('alex', 0.0) - 0.3) < 1e-9

    # Query composed rule: grandparent(john, ?Z) -> only susan with prob 0.9 * 0.6 = 0.54
    sols2 = interp.logical.query(Predicate('grandparent', [Term('john'), Term('Z', True)]))
    assert len(sols2) >= 1
    # Find the substitution for Z = 'susan' (dereferencing Terms)
    susan_sols = []
    for s in sols2:
        z_raw = s.bindings.get('Z')
        try:
            z_res = interp.logical._deref(z_raw, s)
        except Exception:
            z_res = z_raw
        z_val = getattr(z_res, 'value', z_res)
        if z_val == 'susan':
            susan_sols.append(s)
    assert susan_sols, "Expected a solution for Z='susan'"
    p = getattr(susan_sols[0], 'probability', 1.0)
    assert abs(p - (0.9 * 0.6)) < 1e-9

    print("\u2713 test_probabilities_on_facts_and_rules passed")

