# -*- coding: utf-8 -*-
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


def test_template_match_simple_ar():
    code = u"""
    hybrid {
      النص = "سافر خالد إلى مكة"
      tpl = template("سافر {اسم} إلى {مدينة}")
      m = match(tpl, النص)
      if m: {
        who = m["اسم"]
        where = m["مدينة"]
      }
    }
    """
    interp = run(code)
    env = interp.traditional.global_env
    assert env.get('who') == u"خالد"
    assert env.get('where') == u"مكة"


def test_template_match_with_regex_and_render():
    code = u"""
    hybrid {
      line = "User Ali scored 42"
      tpl = template("User {name} scored {score:\\d+}")
      m = match(tpl, line)
      if m: {
        uname = m["name"]
        uscore = m["score"]
      }
      out = render(tpl, {"name":"Omar", "score":99})
    }
    """
    interp = run(code)
    env = interp.traditional.global_env
    assert env.get('uname') == u"Ali"
    assert env.get('uscore') == u"42"
    assert env.get('out') == u"User Omar scored 99"


def test_match_str_direct_without_compile():
    code = u"""
    hybrid {
      m = match("مرحبا {اسم}", "مرحبا سارة")
      if m: { who = m["اسم"] }
    }
    """
    interp = run(code)
    env = interp.traditional.global_env
    assert env.get('who') == u"سارة"

