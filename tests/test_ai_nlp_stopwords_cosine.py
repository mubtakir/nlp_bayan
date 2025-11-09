from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_remove_stopwords_and_cosine_similarity():
    code = """
    import ai.nlp as nlp
    hybrid {
      s = nlp.remove_stopwords("This is the best of the best", "english")
      docs = ["cats and dogs are awesome", "cats dogs awesome", "bad awful"]
      vecs = nlp.compute_tfidf(docs)
      v1 = vecs[0]
      v2 = vecs[1]
      v3 = vecs[2]
      sim_same = nlp.cosine_similarity_dicts(v1, v1)
      sim_close = nlp.cosine_similarity_dicts(v1, v2)
      sim_far = nlp.cosine_similarity_dicts(v1, v3)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    assert ' the ' not in (' ' + s + ' ')
    assert env.get('sim_same') == 1.0
    assert env.get('sim_close') > env.get('sim_far')
    assert env.get('sim_far') <= 0.5

