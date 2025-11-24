from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_ml_stratified_kfold_and_split():
    code = """
    import ai.ml as ml
    hybrid {
      y = [0,0,0,0,0,0,0,0,0,0,1,1]
      folds = ml.stratified_k_fold_indices(y, 3, True, 42)
      # count ones in each validation fold
      v0 = folds[0][1]
      v1 = folds[1][1]
      v2 = folds[2][1]
      v0_ones = 0
      v1_ones = 0
      v2_ones = 0
      for i in (range(len(v0))) {
        if (y[v0[i]] == 1) {
          v0_ones = v0_ones + 1
        }
      }
      for i in (range(len(v1))) {
        if (y[v1[i]] == 1) {
          v1_ones = v1_ones + 1
        }
      }
      for i in (range(len(v2))) {
        if (y[v2[i]] == 1) {
          v2_ones = v2_ones + 1
        }
      }
      sum_ones = v0_ones + v1_ones + v2_ones
      # stratified train/test split
      X = []
      for i in (range(len(y))) {
        row = []
        row.append(i)
        X.append(row)
      }
      parts = ml.train_test_split_stratified(X, y, 0.25, True, 42)
      y_te = parts[3]
      test_ones = 0
      for i in (range(len(y_te))) {
        if (y_te[i] == 1) {
          test_ones = test_ones + 1
        }
      }
      test_total = len(y_te)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    v0_ones = env.get('v0_ones')
    v1_ones = env.get('v1_ones')
    v2_ones = env.get('v2_ones')
    sum_ones = env.get('sum_ones')
    test_ones = env.get('test_ones')
    test_total = env.get('test_total')
    assert sum_ones == 2
    assert max(v0_ones, v1_ones, v2_ones) <= 1
    assert min(v0_ones, v1_ones, v2_ones) >= 0
    assert test_total == 4
    assert test_ones == 1

