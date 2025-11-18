# -*- coding: utf-8 -*-
"""
Tests for concept / مفهوم declarations and membership facts.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
from bayan.bayan.hybrid_interpreter import HybridInterpreter
from bayan.bayan.logical_engine import Fact


def run(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    return interp


def test_concept_runtime_and_logical_facts():
    code = u"""
    hybrid {
      concept Animal = {"\u0623\u0633\u062f", "\u0646\u0645\u0631", "\u0641\u0647\u062f"}
      ok1 = "\u0623\u0633\u062f" in Animal
      ok2 = "\u0642\u0637" in Animal
      ok3 = "\u0623\u0633\u062f" \u2208 Animal
    }
    """
    interp = run(code)
    env = interp.traditional.global_env
    assert env.get('ok1') is True
    assert env.get('ok2') is False
    assert env.get('ok3') is True
    kb = interp.logical.knowledge_base
    facts = [it for it in kb.get('in_concept', []) if isinstance(it, Fact)]
    # At least 3 facts asserted for Animal concept
    animals = [(f.predicate.args[0].value, f.predicate.args[1].value) for f in facts]
    assert (u"Animal", u"\u0623\u0633\u062f") in animals
    assert (u"Animal", u"\u0646\u0645\u0631") in animals
    assert (u"Animal", u"\u0641\u0647\u062f") in animals

