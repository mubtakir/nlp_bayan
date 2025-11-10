from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_damerau_levenshtein_transposition():
    code = """
    import ai.nlp as nlp
    hybrid {
      d_lev = nlp.levenshtein_distance("ab", "ba")
      d_dam = nlp.damerau_levenshtein_distance("ab", "ba")
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    d_lev = env.get('d_lev')
    d_dam = env.get('d_dam')
    assert d_lev == 2
    assert d_dam == 1

