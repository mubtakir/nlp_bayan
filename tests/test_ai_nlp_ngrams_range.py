from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_ngrams_range_tokens():
    code = """
    import ai.nlp as nlp
    hybrid {
      grams = nlp.ngrams_range_from_tokens(["a", "b", "c"], 1, 2)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    grams = env.get('grams')
    assert grams == ["a", "b", "c", "a b", "b c"]

