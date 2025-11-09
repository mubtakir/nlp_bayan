from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_tfidf_options_sublinear_and_smoothing():
    code = """
    import ai.nlp as nlp
    hybrid {
      docs1 = ["a a", "a", "a"]
      vecs_s = nlp.compute_tfidf_options(docs1, True, True)
      vecs_ns = nlp.compute_tfidf_options(docs1, True, False)
      v0s = vecs_s[0]
      v0ns = vecs_ns[0]
      ws = v0s["a"]
      wns = v0ns["a"]

      docs2 = ["a a a", "a", "b"]
      vecs_sub = nlp.compute_tfidf_options(docs2, True, True)
      vecs_raw = nlp.compute_tfidf_options(docs2, False, True)
      v2s = vecs_sub[0]
      v2r = vecs_raw[0]
      ws2 = v2s["a"]
      wr2 = v2r["a"]
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    # Smoothing keeps idf positive when df == N
    assert env.get('ws') > 0.0
    # Without smoothing, idf ~ ln(N/df) = 0 -> weight ~ 0 (allow small numeric error)
    assert abs(env.get('wns')) < 1e-6
    # Sublinear tf should produce smaller weight than raw counts
    assert env.get('ws2') < env.get('wr2')

