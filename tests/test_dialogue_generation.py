from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_generate_with_dialogue_prefers_last_place_and_morphology():
    code = """
    import nlp_bayan.core.dialogue_state as ds
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        ds.reset()
        ds.set_last_entity("سعد")
        ds.set_last_place("المدرسة")
        docs = ["سعد ذهب المدرسة"]
        tok_map = {"المدرسة": "school"}
        lp = ds.get_last_place()
        s = gen.generate_trigram_with_dialogue("سعد", "رجع", docs, 1, 1, tok_map, False, lp)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    assert isinstance(s, str)
    words = s.split()
    assert words[0] == "سعد" and words[1] == "رجع"
    # نتوقع تفضيل المكان الأخير + صرف "الى" لرجع عند ظهور مكان
    assert "المدرسة" in words
    if len(words) >= 4 and words[2] == "الى":
        assert words[3] == "المدرسة"
    else:
        # في حال لم تُضَف "الى"، يجب أن يكون المكان مباشرة بعد الفعل
        assert words[2] == "المدرسة"

