from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_ml_adaboost_and_dataset():
    code = """
    from ai.ml import adaboost_train, adaboost_predict
    hybrid {
      # AND dataset in 2D: only [1,1] -> 1
      X = [[0.0,0.0],[0.0,1.0],[1.0,0.0],[1.0,1.0]]
      y = [0,0,0,1]
      model = adaboost_train(X, y, 5)
      preds = adaboost_predict(model, X)
    }
    """
    interp = run_interp(code)
    preds = interp.traditional.global_env.get('preds')
    assert preds == [0,0,0,1]


def test_ml_adaboost_threshold_1d():
    code = """
    from ai.ml import adaboost_train, adaboost_predict
    hybrid {
      # Simple 1D threshold problem
      X = [[0.1],[0.2],[0.8],[0.9]]
      y = [0,0,1,1]
      model = adaboost_train(X, y, 3)
      preds2 = adaboost_predict(model, [[0.15],[0.85]])
      p0 = preds2[0]
      p1 = preds2[1]
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    assert env.get('p0') == 0
    assert env.get('p1') == 1


def test_ml_adaboost_arabic_wrappers():
    code = """
    import ai.ml as ml
    hybrid {
      X = [[0.0,0.0],[1.0,1.0]]
      y = [0,1]
      نموذج = ml.تدريب_ادابوست(X, y, 3)
      تنبؤ = ml.توقع_ادابوست(نموذج, X)
      ت0 = تنبؤ[0]
      ت1 = تنبؤ[1]
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    assert env.get('ت0') == 0
    assert env.get('ت1') == 1

