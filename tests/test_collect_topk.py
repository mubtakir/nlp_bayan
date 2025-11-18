# -*- coding: utf-8 -*-
"""
Tests for collect / topk / argmax sugar inside hybrid blocks.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'bayan'))

from bayan.hybrid_interpreter import HybridInterpreter
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


def test_collect_topk_argmax_with_similarity():
    code = u"""
    hybrid {
      import bayan.core.similarity as sim
      sim.load_selective(logical, ["similarity"])
      أسد(غضنفر:0.8, هيضم:0.5).

      xs = collect ?Y from similar("أسد", ?Y, ?S, "syn", "lexicon")
      best = argmax ?Y by ?S where similar("أسد", ?Y, ?S, "syn", "lexicon")
      top = topk 1 of ?Y by ?S where similar("أسد", ?Y, ?S, "syn", "lexicon")
    }
    """
    interp = run(code)

    env = interp.traditional.global_env
    xs = env.get('xs')
    best = env.get('best')
    top = env.get('top')

    assert isinstance(xs, list)
    assert set(xs) >= set([u"غضنفر", u"هيضم"])  # contains both

    assert best == u"غضنفر"
    assert isinstance(top, list) and len(top) == 1 and top[0] == u"غضنفر"

