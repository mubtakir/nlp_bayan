from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_ml_linear_svm_wave8():
    code = """
    from ai.ml import linear_svm_train, linear_svm_predict
    hybrid {
      X = [[0.0,0.0],[0.0,1.0],[1.0,0.0],[1.0,1.0]]
      y = [0,0,0,1]
      wb = linear_svm_train(X, y, 0.2, 400, 2.0)
      preds = linear_svm_predict(X, wb[0], wb[1])
    }
    """
    interp = run_interp(code)
    preds = interp.traditional.global_env.get('preds')
    assert preds == [0,0,0,1]

