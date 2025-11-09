from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_ml_kfold_indices_basic():
    code = """
    import ai.ml as ml
    hybrid {
      folds = ml.k_fold_indices(10, 5, True, 42)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    folds = env.get('folds')
    assert isinstance(folds, list)
    assert len(folds) == 5
    # each fold is [train_idx, val_idx]
    total_val = 0
    seen = set()
    for tv in folds:
        train_idx, val_idx = tv[0], tv[1]
        assert isinstance(train_idx, list) and isinstance(val_idx, list)
        total_val += len(val_idx)
        for v in val_idx:
            assert v not in seen
            seen.add(v)
    assert total_val == 10
    assert seen == set(range(10))

