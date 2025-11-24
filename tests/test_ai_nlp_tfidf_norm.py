from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_tfidf_log_norm_basic():
    code = """
    import ai.nlp as nlp
    hybrid {
      docs = ["rare rare rare common", "common common common common"]
      vecs = nlp.compute_tfidf_log_norm(docs)
      v1 = vecs[0]
      # compute l2 norm
      n2 = 0.0
      for t in (v1) { n2 = n2 + v1[t] * v1[t] }
      if ("rare" in v1) { rare_w = v1["rare"] } else: { rare_w = 0.0 }
      if ("common" in v1) { common_w = v1["common"] } else: { common_w = 0.0 }
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    n2 = env.get('n2')
    rare_w = env.get('rare_w')
    common_w = env.get('common_w')

    assert abs(n2 - 1.0) < 1e-6
    assert rare_w > common_w

