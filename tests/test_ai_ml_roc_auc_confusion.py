from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    return interp


def test_ml_roc_auc_and_confusion():
    code = """
from ai.ml import logistic_regression_train, logistic_regression_predict, logistic_regression_predict_proba, roc_curve, auc_roc, confusion_matrix
hybrid {
  X = [[0], [1], [2], [3], [4]]
  y = [0, 0, 1, 1, 1]
  wb = logistic_regression_train(X, y, 0.3, 300)
  w = wb[0]
  b = wb[1]
  probs = logistic_regression_predict_proba(X, w, b)
  res = roc_curve(y, probs, 1)
  fprs = res[0]
  tprs = res[1]
  auc = auc_roc(fprs, tprs)
  preds = logistic_regression_predict(X, w, b, 0.5)
  cm = confusion_matrix(y, preds, 1, 0)
}
"""
    interp = run_interp(code)
    env = interp.traditional.global_env
    auc = env["auc"]
    assert auc >= 0.9
    cm = env["cm"]
    # tp should be at least 2 for this simple separable dataset
    assert cm[1][1] >= 2

