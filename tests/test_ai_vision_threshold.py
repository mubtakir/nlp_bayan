from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_vision_threshold_basic():
    code = """
    import ai.vision as vis
    hybrid {
      img = [[10, 200], [150, 50]]
      out = vis.threshold(img, 100, 255, 0)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    out = env.get('out')
    assert out == [[0,255],[255,0]]

