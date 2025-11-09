from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_ml_train_test_split_and_metrics():
    code = """
    from ai.ml import train_test_split, precision_score, recall_score, f1_score
    hybrid {
      X = [[0], [1], [2], [3]]
      y = [1, 0, 1, 0]
      parts = train_test_split(X, y, 0.5)
      Xtr = parts[0]
      Xte = parts[1]
      ytr = parts[2]
      yte = parts[3]
      p = precision_score([1,0,1,0], [1,0,0,0], 1)
      r = recall_score([1,0,1,0], [1,0,0,0], 1)
      f = f1_score([1,0,1,0], [1,0,0,0], 1)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    Xtr = env.get('Xtr'); Xte = env.get('Xte')
    ytr = env.get('ytr'); yte = env.get('yte')
    assert len(Xtr) == 2 and len(Xte) == 2
    assert len(ytr) == 2 and len(yte) == 2
    assert abs(env.get('p') - 1.0) < 1e-9
    assert abs(env.get('r') - 0.5) < 1e-6
    assert abs(env.get('f') - (2*1.0*0.5/1.5)) < 1e-6

