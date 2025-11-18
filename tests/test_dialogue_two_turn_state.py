from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_two_turn_dialogue_coreference_with_kb_and_state():
    code = """
    import nlp_bayan.core.dialogue_state as ds
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        ds.reset()
        docs = ["سعد ذهب المدرسة", "سعد رجع المدرسة"]
        tok_map = {"سعد": "person", "المدرسة": "school"}
        # الجولة الأولى
        s1 = gen.generate_trigram_kb_from_docs("سعد", "ذهب", docs, 1, 1, "maybe", "is_green", tok_map, 0.0, 11, 0.0, False, [], 0, 0, -1, True, "")
        # الجولة الثانية (يفترض تفضيل المدرسة من حالة الحوار)
        s2 = gen.generate_trigram_kb_from_docs("سعد", "رجع", docs, 1, 1, "maybe", "is_green", tok_map, 0.0, 22, 0.0, False, [], 0, 0, -1, True, "")
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s1 = env.get('s1')
    s2 = env.get('s2')
    assert isinstance(s1, str) and isinstance(s2, str)
    # تحقق أن السطر الثاني يحمل إحالة إلى المدرسة (مع أو بدون "الى")
    words2 = s2.split()
    assert words2[0] == "سعد" and words2[1] == "رجع"
    assert "المدرسة" in words2
    if len(words2) >= 4 and words2[2] == "الى":
        assert words2[3] == "المدرسة"

