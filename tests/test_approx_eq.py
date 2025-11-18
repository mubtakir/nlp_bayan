# -*- coding: utf-8 -*-
"""
Tests for approximate equality operator ~= and ≈
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
from bayan.bayan.hybrid_interpreter import HybridInterpreter


def run(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    return interp


def test_numeric_approx_eq_default_epsilon():
    code = u"""
    hybrid {
      x = 3.14
      y = 22 / 7
      ok = x ~= y
      ok2 = 3.0 ≈ 3.0000001
    }
    """
    interp = run(code)
    env = interp.traditional.global_env
    assert env.get('ok') is True
    assert env.get('ok2') is True


def test_string_semantic_approx_eq_lexicon():
    code = u"""
    hybrid {
      import bayan.core.similarity as sim
      sim.load_selective(logical, ["similarity"])  # loads close/3
      a = "أسد"
      b = "غضنفر"
      c = "هيضم"
      ok = a ~= b         # 0.8 >= default syn threshold 0.7
      bad = a ~= c        # 0.5 < 0.7
    }
    """
    interp = run(code)
    env = interp.traditional.global_env
    assert env.get('ok') is True
    assert env.get('bad') is False

