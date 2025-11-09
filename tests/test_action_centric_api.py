"""
Tests for the action-centric API (perform/نفذ) without changing syntax grammar.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Ensure we import local package, not any globally installed one
import sys as _sys
_sys.modules.pop('bayan', None)
_sys.modules.pop('bayan.bayan', None)

from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run(code: str):
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.traditional.set_source(code, filename=None)
    last = interp.interpret(ast)
    return interp, last


def test_perform_arabic_alias_and_string_participants():
    code = """
    hybrid {
        entity Ahmed {
          "properties": {"x": {"type": "numeric", "value": 0.0}},
          "actions": {
            "go": {"effects": [ {"on": "x", "formula": "value + 3*sensitivity"} ]}
          }
        }
        entity Ali   { "properties": {"x": {"type": "numeric", "value": 1.0}} }

        # نفذ(action, participants-as-strings)
        نفذ("go", ["Ahmed.1.0", "Ali.0.5"])
    }

    query property("Ahmed", "x", ?AX).
    """
    interp, resA = run(code)
    assert resA, "Expected Ahmed.x query results"
    AX = getattr(resA[0]['AX'], 'value', resA[0]['AX'])
    assert abs(AX - 3.0) < 1e-6

    # Check Ali.x
    code2 = """
    query property("Ali", "x", ?BX).
    """
    interp.traditional.set_source(code2, filename=None)
    ast2 = HybridParser(HybridLexer(code2).tokenize()).parse()
    resB = interp.interpret(ast2)
    BX = getattr(resB[0]['BX'], 'value', resB[0]['BX'])
    assert abs(BX - 2.5) < 1e-6




def test_groups_and_last_reference_en():
    code = """
    hybrid {
      entity Ahmed { "properties": {"x": {"type": "numeric", "value": 0.0}},
                     "actions": {"go": {"effects": [{"on": "x", "formula": "value + 2*sensitivity"}]}} }
      entity Ali   { "properties": {"x": {"type": "numeric", "value": 1.0}} }

      define_group("Team", ["Ahmed", "Ali"])
      perform("go", ["group:Team.0.5"])
      perform("go", ["last.0.2"])
    }
    """
    interp, _ = run(code)
    # Ensure group created
    engine = interp._get_or_create_engine()
    assert engine.get_group_members("Team") == ["Ahmed", "Ali"]

    # Verify participant normalization for group spec
    assert engine._normalize_participants(["group:Team.0.5"]) == [("Ahmed", 0.5), ("Ali", 0.5)]

    assert engine.groups.get("Team", []) == ["Ahmed", "Ali"]
    assert engine._normalize_participants([("group:Team", 0.5)]) == [("Ahmed", 0.5), ("Ali", 0.5)]


    # Query Ahmed.x
    q1 = """
    query property("Ahmed", "x", ?AX).
    """
    interp.traditional.set_source(q1, filename=None)
    ast_q1 = HybridParser(HybridLexer(q1).tokenize()).parse()
    res1 = interp.interpret(ast_q1)
    AX = getattr(res1[0]['AX'], 'value', res1[0]['AX'])
    assert abs(AX - 1.4) < 1e-6

    # Query Ali.x
    q2 = """
    query property("Ali",   "x", ?BX).
    """
    interp.traditional.set_source(q2, filename=None)
    ast_q2 = HybridParser(HybridLexer(q2).tokenize()).parse()
    res2 = interp.interpret(ast_q2)
    BX = getattr(res2[0]['BX'], 'value', res2[0]['BX'])
    assert abs(BX - 2.4) < 1e-6


def test_groups_and_last_reference_ar():
    code = """
    hybrid {
      كيان أحمد { "خصائص": {"س": {"نوع": "عددي", "قيمة": 0.0}},
                  "أفعال": {"اذهب": {"تأثيرات": [{"on": "س", "formula": "value + 2*sensitivity"}]}} }
      كيان علي   { "خصائص": {"س": {"نوع": "عددي", "قيمة": 1.0}} }

      define_group("الفريق", ["أحمد", "علي"])
      نفذ("اذهب", ["مجموعة:الفريق.0.5"])
      نفذ("اذهب", ["last.0.2"])
    }
    """
    interp, _ = run(code)

    q1 = """
    query property("أحمد", "س", ?AX).
    """
    interp.traditional.set_source(q1, filename=None)
    ast_q1 = HybridParser(HybridLexer(q1).tokenize()).parse()
    res1 = interp.interpret(ast_q1)
    AX = getattr(res1[0]['AX'], 'value', res1[0]['AX'])
    assert abs(AX - 1.4) < 1e-6

    q2 = """
    query property("علي",  "س", ?BX).
    """
    interp.traditional.set_source(q2, filename=None)
    ast_q2 = HybridParser(HybridLexer(q2).tokenize()).parse()
    res2 = interp.interpret(ast_q2)
    BX = getattr(res2[0]['BX'], 'value', res2[0]['BX'])
    assert abs(BX - 2.4) < 1e-6
