import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

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


def test_event_texts_en_and_ar():
    code = """
    hybrid {
      entity Ahmed { "properties": {"x": {"type": "numeric", "value": 0.0}},
                     "actions": {"go": {"effects": [{"on": "x", "formula": "value + sensitivity"}]}} }
      entity Ali   { "properties": {"x": {"type": "numeric", "value": 1.0}} }
      perform("go", ["Ahmed:1.0", "Ali:0.5"])     
      perform("go", ["they:0.2"])                  
    }
    """
    interp, _ = run(code)
    env = interp.traditional.global_env
    en = env['event_texts']('en')
    ar = env['نص_الأحداث']('ar')
    assert len(en) == len(ar) >= 2
    assert 'Ahmed' in en[0] and 'go' in en[0]
    assert '\x7f' not in ar[0]  # quick sanity: should be printable

