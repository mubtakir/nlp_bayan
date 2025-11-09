from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_ml_kmeans_pp_two_clusters():
    code = """
    from ai.ml import k_means_pp
    hybrid {
      data = [[0,0], [0,1], [10,10], [10,11]]
      res = k_means_pp(data, 2, 10)
      centers = res[0]
      labels = res[1]
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    centers = env.get('centers'); labels = env.get('labels')
    assert len(centers) == 2
    assert len(labels) == 4

