from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_data_min_max_range_and_zscore():
    code = """
    from ai.data import min_value, max_value, data_range, zscore_normalize
    hybrid {
      xs = [3, 1, 5, 4]
      mn = min_value(xs)
      mx = max_value(xs)
      rg = data_range(xs)
      zs = zscore_normalize([1, 2, 3])
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    assert env.get('mn') == 1
    assert env.get('mx') == 5
    assert env.get('rg') == 4
    zs = env.get('zs')
    # Mean approx 0 and std approx 1
    mean = sum(zs) / len(zs)
    var = sum((v - mean) ** 2 for v in zs) / len(zs)
    std = var ** 0.5
    assert abs(mean) < 1e-6
    assert abs(std - 1.0) < 1e-6

