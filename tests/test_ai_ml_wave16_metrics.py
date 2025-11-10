from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_ml_mcc_and_kappa_basic():
    code = """
    import ai.ml as ml
    hybrid {
      y_true = [1,1,0,0]
      y_pred_ok = [1,1,0,0]
      y_pred_bad = [1,0,1,0]
      mcc1 = ml.matthews_corrcoef(y_true, y_pred_ok, 1, 0)
      mcc2 = ml.matthews_corrcoef(y_true, y_pred_bad, 1, 0)
      kappa1 = ml.cohen_kappa_score(y_true, y_pred_ok, [])
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    mcc1 = env.get('mcc1')
    mcc2 = env.get('mcc2')
    kappa1 = env.get('kappa1')
    assert mcc1 > 0.99 and mcc1 <= 1.0
    assert abs(mcc2 - 0.0) < 1e-9
    assert kappa1 > 0.99 and kappa1 <= 1.0

