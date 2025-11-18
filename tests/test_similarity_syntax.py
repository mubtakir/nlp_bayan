# -*- coding: utf-8 -*-
"""
Tests for the new similarity declaration sugar:
  Head(term:score, term:score, ...)
E.g., أسد(غضنفر:0.8, هيضم:0.5)
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


def test_similarity_sugar_basic_pairs():
    code = u"""
    # Declare synonyms via sugar
    أسد(غضنفر:0.8, هيضم:0.5)
    """
    interp = run(code)

    # Check forward fact
    goal1 = Predicate('similar', [Term(u"أسد"), Term(u"غضنفر"), Term(0.8), Term(u"syn"), Term(u"lexicon")])
    sols1 = interp.logical.query(goal1)
    assert len(sols1) >= 1

    # Check reverse fact materialized
    goal2 = Predicate('similar', [Term(u"غضنفر"), Term(u"أسد"), Term(0.8), Term(u"syn"), Term(u"lexicon")])
    sols2 = interp.logical.query(goal2)
    assert len(sols2) >= 1

    # Check second pair
    goal3 = Predicate('similar', [Term(u"أسد"), Term(u"هيضم"), Term(0.5), Term(u"syn"), Term(u"lexicon")])
    sols3 = interp.logical.query(goal3)
    assert len(sols3) >= 1


def test_similarity_sugar_inside_hybrid_block_with_dot():
    code = u"""
    hybrid {
      # with trailing dot
      ذهب(راح:0.8).
    }
    """
    interp = run(code)

    goal = Predicate('similar', [Term(u"ذهب"), Term(u"راح"), Term(0.8), Term(u"syn"), Term(u"lexicon")])
    sols = interp.logical.query(goal)
    assert len(sols) >= 1

