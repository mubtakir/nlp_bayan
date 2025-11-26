from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_tfidf_log_rarity_vs_common():
    code = """
    import ai.nlp as nlp
    hybrid {
      docs = ["this this common", "this common", "rare term"]
      vecs = nlp.compute_tfidf_log(docs)
      v1 = vecs[0]
      v3 = vecs[2]
      if ("rare" in v3) {
        rare_w = v3["rare"]
      }
      else
      {
        rare_w = 0.0
      }
      if ("this" in v1) {
        this_w = v1["this"]
      }
      else
      {
        this_w = 0.0
      }
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    rare_w = env.get('rare_w')
    this_w = env.get('this_w')
    assert rare_w > 0.0
    assert rare_w > this_w

