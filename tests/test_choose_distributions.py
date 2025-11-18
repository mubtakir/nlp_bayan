# -*- coding: utf-8 -*-
import math
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


def test_choose_weighted_trivial_max_weight():
    code = u"""
    hybrid {
      # highest weight should always be selected even without seeding
      pick = choose { "A":0.0, "B":1.0, "C":0.0 }
    }
    """
    interp = run(code)
    env = interp.traditional.global_env
    assert env.get('pick') == u"B"


def test_seed_and_uniform_reproducible():
    code = u"""
    hybrid {
      seed(123)
      x ~ uniform(0, 1)
      y ~ uniform(0, 1)
      seed(123)
      w ~ uniform(0, 1)
    }
    """
    interp = run(code)
    env = interp.traditional.global_env
    x, y, w = env.get('x'), env.get('y'), env.get('w')
    assert isinstance(x, float) and isinstance(y, float) and isinstance(w, float)
    assert x == w  # same seed ⇒ same first sample
    assert x != y  # sequential draws differ
    assert 0.0 <= x <= 1.0 and 0.0 <= y <= 1.0


def test_normal_and_bernoulli_edges():
    code = u"""
    hybrid {
      seed(42)
      n ~ normal(0, 1)
      b0 ~ bernoulli(0.0)
      b1 ~ bernoulli(1.0)
    }
    """
    interp = run(code)
    env = interp.traditional.global_env
    n = env.get('n')
    b0 = env.get('b0')
    b1 = env.get('b1')
    assert isinstance(n, float)
    assert b0 == 0 and b1 == 1

