# -*- coding: utf-8 -*-
"""Tests for Arabic equivalents of logic keywords in Bayan.

- هجين  (hybrid)
- حقيقة (fact)
- قاعدة (rule)
- استعلام (query, already supported but verified here)
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from bayan.bayan.lexer import HybridLexer, TokenType
from bayan.bayan.parser import HybridParser
from bayan.bayan.hybrid_interpreter import HybridInterpreter


def run_hybrid(code: str):
    """Helper to run a small hybrid block; should not raise."""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    return interp.interpret(ast)


def test_arabic_hybrid_keyword_lexing():
    """Ensure هجين is recognized as HYBRID keyword."""
    code = u"هجين { x = 5 }"
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    assert tokens[0].type == TokenType.HYBRID
    print("✓ test_arabic_hybrid_keyword_lexing passed")


def test_arabic_fact_and_rule_keywords_lexing():
    """Ensure حقيقة and قاعدة are recognized as FACT and RULE keywords."""
    code = u"""
    هجين {
        حقيقة[0.9] parent("john", "mary").
        قاعدة grandparent(?X, ?Z) :- parent(?X, ?Y), parent(?Y, ?Z).
    }
    """
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    fact_tokens = [t for t in tokens if t.type == TokenType.FACT]
    rule_tokens = [t for t in tokens if t.type == TokenType.RULE]
    assert fact_tokens, "Expected at least one FACT token for حقيقة"
    assert rule_tokens, "Expected at least one RULE token for قاعدة"
    assert fact_tokens[0].value == u"حقيقة"
    assert rule_tokens[0].value == u"قاعدة"
    print("✓ test_arabic_fact_and_rule_keywords_lexing passed")


def test_arabic_logic_keywords_end_to_end():
    """End-to-end test: هجين + حقيقة + قاعدة + استعلام inside one block."""
    code = u"""
    هجين {
        حقيقة[0.9] parent("john", "mary").
        حقيقة[0.8] parent("mary", "susan").

        قاعدة grandparent(?X, ?Z) :-
            parent(?X, ?Y),
            parent(?Y, ?Z).

        استعلام grandparent(?GP, ?GC).
    }
    """
    run_hybrid(code)
    print("✓ test_arabic_logic_keywords_end_to_end passed")

