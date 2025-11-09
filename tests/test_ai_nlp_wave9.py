from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_overlap_coefficient():
    code = """
    from ai.nlp import overlap_coefficient
    hybrid {
      a = ["this","is","a","test"]
      b = ["this","is","b"]
      s = overlap_coefficient(a, b)
    }
    """
    interp = run_interp(code)
    s = interp.traditional.global_env.get('s')
    assert abs(s - (2.0/3.0)) < 1e-6

