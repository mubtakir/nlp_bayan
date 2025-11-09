from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_dice_similarity_wave8():
    code = """
    import ai.nlp as nlp
    hybrid {
      d = nlp.dice_similarity(["a","b"], ["b","c"])
    }
    """
    interp = run_interp(code)
    d = interp.traditional.global_env.get('d')
    assert abs(d - 0.5) < 1e-9

