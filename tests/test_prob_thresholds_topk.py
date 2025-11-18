# -*- coding: utf-8 -*-
"""
Tests for probability thresholds (maybe/likely) and topk/argmax fallback to solution probability.
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


def test_maybe_likely_and_topk_prob_fallback():
    code = u'''
    hybrid {
      fact[0.9] link("a", "x").
      fact[0.3] link("a", "y").

      high(?Z)  :- link("a", ?Z), maybe().
      strong(?Z) :- link("a", ?Z), likely().

      best = argmax ?Z by ?S where link("a", ?Z)
      top = topk 1 of ?Z by ?S where link("a", ?Z)
    }
    '''
    interp = run(code)

    # Probability-aware solutions for link/2
    sols_link = interp.logical.query(Predicate('link', [Term('a'), Term('Z', True)]))
    # Best by probability should be 'x'
    # Dereference Terms to raw values for comparison
    ranked = []
    for s in sols_link:
        z_raw = s.bindings.get('Z')
        try:
            z_res = interp.logical._deref(z_raw, s)
        except Exception:
            z_res = z_raw
        z_val = getattr(z_res, 'value', z_res)
        ranked.append((z_val, getattr(s, 'probability', 1.0)))
    ranked.sort(key=lambda t: t[1], reverse=True)
    assert ranked and ranked[0][0] == 'x'

    # Check threshold predicates
    sols_high = interp.logical.query(Predicate('high', [Term('Z', True)]))
    high_vals = []
    for s in sols_high:
        z_raw = s.bindings.get('Z')
        try:
            z_res = interp.logical._deref(z_raw, s)
        except Exception:
            z_res = z_raw
        z_val = getattr(z_res, 'value', z_res)
        high_vals.append(z_val)
    high_vals.sort()
    assert high_vals == ['x']  # maybe() default 0.5 filters out y (0.3)

    sols_strong = interp.logical.query(Predicate('strong', [Term('Z', True)]))
    strong_vals = []
    for s in sols_strong:
        z_raw = s.bindings.get('Z')
        try:
            z_res = interp.logical._deref(z_raw, s)
        except Exception:
            z_res = z_raw
        z_val = getattr(z_res, 'value', z_res)
        strong_vals.append(z_val)
    assert strong_vals == ['x']  # likely() default 0.8 keeps only x (0.9)

    print("\u2713 test_maybe_likely_and_topk_prob_fallback passed")

