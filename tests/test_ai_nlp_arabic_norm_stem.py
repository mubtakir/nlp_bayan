from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_arabic_normalize_and_stem():
    code = """
    import ai.nlp as nlp
    hybrid {
      n1 = nlp.تطبيع_عربي("أحمد")
      n2 = nlp.تطبيع_عربي("مسؤول")
      stems = nlp.تجذيع_عربي_خفيف_كلمات(["والكتاب", "كتابه", "مدرسات"])
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    assert env.get('n1') == 'احمد'
    assert env.get('n2') == 'مسوول'
    stems = env.get('stems')
    assert stems == ['كتاب', 'كتاب', 'مدرس']

