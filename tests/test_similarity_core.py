# -*- coding: utf-8 -*-
"""
Core tests for Bayan similarity/synonyms module
اختبارات أساسية لوحدة التشابه/المترادفات في البيان
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'bayan'))

from bayan.hybrid_interpreter import HybridInterpreter
from bayan.logical_engine import Predicate, Term
from bayan.lexer import HybridLexer
from bayan.parser import HybridParser


def run(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    return interp


def test_close_with_default_threshold():
    code = u"""
    import bayan.core.similarity as sim
    # Load the defaults from the module into this interpreter's logical engine
    sim.load_into(logical)
    """
    interp = run(code)

    # close("أسد","غضنفر","syn") should succeed (0.8 >= 0.7)
    goal_ok = Predicate('close', [Term(u"أسد"), Term(u"غضنفر"), Term(u"syn")])
    sols_ok = interp.logical.query(goal_ok)
    assert len(sols_ok) >= 1

    # close("أسد","هيضم","syn") should fail by default (0.5 < 0.7)
    goal_bad = Predicate('close', [Term(u"أسد"), Term(u"هيضم"), Term(u"syn")])
    sols_bad = interp.logical.query(goal_bad)
    assert len(sols_bad) == 0


def test_close_with_explicit_tau():
    code = u"""
    import bayan.core.similarity as sim
    sim.load_into(logical)
    """
    interp = run(code)

    # close("أسد","هيضم", 0.5, "syn") should succeed with explicit tau
    goal = Predicate('close', [Term(u"أسد"), Term(u"هيضم"), Term(0.5), Term(u"syn")])
    sols = interp.logical.query(goal)
    assert len(sols) >= 1


def test_synonym_rule_lists_pairs():
    code = u"""
    import bayan.core.similarity as sim
    sim.load_into(logical)
    """
    interp = run(code)

    goal = Predicate('synonym', [Term(u"أسد"), Term('Y', is_variable=True), Term('S', is_variable=True)])
    sols = interp.logical.query(goal)
    # Should include غضنفر with score >= 0.8 and may include هيضم with 0.5
    seen = {(getattr(s.bindings['Y'], 'value', s.bindings['Y']), getattr(s.bindings['S'], 'value', s.bindings['S'])) for s in sols}
    assert any(y == u"غضنفر" and float(s) >= 0.8 for (y, s) in seen)
    assert any(y == u"هيضم" and abs(float(s) - 0.5) < 1e-9 for (y, s) in seen)


def test_synset_function_adds_pairs():
    code = u"""
    import bayan.core.similarity as sim
    sim.synset("قهوة", {"بُن": 1.0, "قهاوة": 0.6})
    sim.load_into(logical)
    """
    interp = run(code)

    # With default syn threshold 0.7, close("قهوة","بُن","syn") should pass, والقهاوة تفشل
    goal_ok = Predicate('close', [Term(u"قهوة"), Term(u"بُن"), Term(u"syn")])
    sols_ok = interp.logical.query(goal_ok)
    assert len(sols_ok) >= 1

    goal_bad = Predicate('close', [Term(u"قهوة"), Term(u"قهاوة"), Term(u"syn")])
    sols_bad = interp.logical.query(goal_bad)
    assert len(sols_bad) == 0

    # Explicit tau 0.6 should make it pass
    goal_tau = Predicate('close', [Term(u"قهوة"), Term(u"قهاوة"), Term(0.6), Term(u"syn")])
    sols_tau = interp.logical.query(goal_tau)
    assert len(sols_tau) >= 1

