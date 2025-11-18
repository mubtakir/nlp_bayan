from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_simple_api_basic_generation():
    code = """
    import nlp_bayan.api.simple_api as api
    hybrid {
        docs = ["سعد جلس المقهى", "المقهى جميل"]
        tok_map = {"سعد":"person", "المقهى":"cafe"}
        s = api.gen_sentence("سعد", "جلس", docs, tok_map, 10, 3, 0.0, 7, 0.0, True, ["المقهى"], 2, 2, 5)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    assert isinstance(s, str) and len(s.split()) >= 2
    assert "سعد" in s


def test_cli_demo_runs_and_returns_string():
    code = """
    import nlp_bayan.examples.cli_generator as cli
    hybrid {
        out = cli.demo()
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    out = env.get('out')
    assert isinstance(out, str)
    assert len(out.split()) >= 2

