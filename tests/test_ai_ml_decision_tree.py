from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_ml_decision_tree_xor_gini_and_entropy():
    code = """
    from ai.ml import decision_tree_train, decision_tree_predict
    hybrid {
      X = [[0,0], [0,1], [1,0], [1,1]]
      y = [0,1,1,0]
      tree_g = decision_tree_train(X, y, 2, "gini", 2)
      preds_g = decision_tree_predict(tree_g, X)
      tree_e = decision_tree_train(X, y, 2, "entropy", 2)
      preds_e = decision_tree_predict(tree_e, X)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    assert env.get('preds_g') == [0, 1, 1, 0]
    assert env.get('preds_e') == [0, 1, 1, 0]

