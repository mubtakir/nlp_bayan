from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_dialogue_state_basic():
    code = """
    import nlp_bayan.core.dialogue_state as ds
    hybrid {
        ds.reset()
        ds.set_last_entity("سعد")
        ds.set_last_place("المدرسة")
        e = ds.get_last_entity()
        p = ds.get_last_place()
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    e = env.get('e')
    p = env.get('p')
    assert e == "سعد"
    assert p == "المدرسة"

