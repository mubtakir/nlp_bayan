from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    return interp


def test_nlp_naive_bayes_basic():
    code = """
from ai.nlp import naive_bayes_train_text, naive_bayes_predict_text, naive_bayes_predict_proba_text
hybrid {
  docs = ["good movie", "excellent film", "bad film", "terrible movie"]
  y = [1, 1, 0, 0]
  m = naive_bayes_train_text(docs, y, 1.0)
  p1 = naive_bayes_predict_text(m, "good excellent")
  p2 = naive_bayes_predict_text(m, "terrible")
  probs = naive_bayes_predict_proba_text(m, "good")
}
"""
    interp = run_interp(code)
    env = interp.traditional.global_env
    assert env["p1"] == 1
    assert env["p2"] == 0
    probs = env["probs"]
    assert probs[1] > probs[0]

