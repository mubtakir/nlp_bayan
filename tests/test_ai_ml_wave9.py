from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_ml_svm_ovr_and_bagging():
    code = """
    from ai.ml import linear_svm_ovr_train, linear_svm_ovr_predict
    from ai.ml import bagging_train, bagging_predict
    hybrid {
      # Three-class clustered data (linearly separable in 2D via OvR)
      X = [[0.0,0.0],[0.0,1.5],[0.0,2.0],[2.0,0.0],[1.5,0.0]]
      y = [0,1,1,2,2]
      model = linear_svm_ovr_train(X, y, 0.2, 500, 2.0)
      Xt = [[0.0,0.1],[0.0,1.9],[1.9,0.0]]
      preds_ovr = linear_svm_ovr_predict(model, Xt)

      # Bagging wrapper (over decision trees) on simple threshold data
      X2 = [[0.0],[1.0],[0.2],[0.8]]
      y2 = [0,1,0,1]
      bg = bagging_train(X2, y2, 5, 1, 2, 1.0, 42)
      preds_bg = bagging_predict(bg, X2)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    assert env.get('preds_ovr') == [0, 1, 2]
    assert env.get('preds_bg') == [0, 1, 0, 1]

