from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_data_csv_rows_and_stats():
    code = """
    import ai.data as data
    hybrid {
      rows_str = ["a,b", "1,2", "x,y"]
      parsed = data.parse_csv_rows(rows_str, ",")
      back_rows = data.to_csv_rows(parsed, ",")
      m = data.mean([1,2,3,4])
      v = data.variance([1,2,3,4])
      s = data.stddev([1,2,3,4])
      ar_m = data.متوسط([1,2,3,4])
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    parsed = env.get('parsed'); back_rows = env.get('back_rows')
    assert parsed[0] == ['a','b'] and back_rows[0] == 'a,b'
    m = env.get('m'); v = env.get('v'); s = env.get('s'); ar_m = env.get('ar_m')
    assert abs(m - 2.5) < 1e-9 and abs(ar_m - 2.5) < 1e-9
    assert abs(v - 1.25) < 1e-9
    assert abs(s - (1.25**0.5)) < 1e-9

