from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    return interp


def test_ml_kmeanspp_prob_clusters():
    code = """
from ai.ml import k_means_pp_prob
hybrid {
  data = [[0,0], [0,1], [10,10], [10,11]]
  res = k_means_pp_prob(data, 2, 10, 123)
  centers = res[0]
  labels = res[1]
}
"""
    interp = run_interp(code)
    env = interp.traditional.global_env
    labels = env["labels"]
    # Same cluster for the two points near (0,0)
    assert labels[0] == labels[1]
    # Same cluster for the two points near (10,10)
    assert labels[2] == labels[3]
    # Different clusters across the groups
    assert labels[0] != labels[2]

