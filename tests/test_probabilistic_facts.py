# -*- coding: utf-8 -*-
"""
Tests for probabilistic facts: fact[0.8] p(args).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from bayan.lexer import HybridLexer
from bayan.parser import HybridParser
from bayan.hybrid_interpreter import HybridInterpreter
from bayan.logical_engine import Fact


def run(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    return interp


def test_probabilistic_fact_storage():
    code = u"""
    hybrid {
      fact[0.9] parent("john", "mary").
      fact[0.6] parent("john", "alex").
    }
    """
    interp = run(code)
    kb = interp.logical.knowledge_base
    assert 'parent' in kb
    facts = [it for it in kb['parent'] if isinstance(it, Fact)]
    assert len(facts) >= 2
    # Find mary fact
    pf = None
    for f in facts:
        args = [t.value for t in f.predicate.args]
        if args == [u"john", u"mary"]:
            pf = f
            break
    assert pf is not None
    assert abs(pf.probability - 0.9) < 1e-9

