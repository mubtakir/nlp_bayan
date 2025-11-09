from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_data_binning_and_one_hot():
    code = """
    from ai.data import bin_equal_width, one_hot_encode
    hybrid {
      xs = [0.0, 2.4, 2.6, 5.0, 9.9, 10.0]
      idx = bin_equal_width(xs, 2)
      oh = one_hot_encode(idx, 2)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    idx = env.get('idx')
    oh = env.get('oh')
    assert idx == [0, 0, 0, 1, 1, 1]
    assert oh == [[1,0],[1,0],[1,0],[0,1],[0,1],[0,1]]

