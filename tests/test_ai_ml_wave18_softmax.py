from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def _run(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def _train_softmax_and_predict(X, y, lr=0.1, epochs=300, l2=0.0):
    code = f"""
    import ai.ml as ML
    hybrid {{
        X = {X}
        y = {y}
        model = ML.softmax_train(X, y, {lr}, {epochs}, {l2})
        probs = ML.softmax_predict_proba(X, model)
        preds = ML.softmax_predict(X, model)
        rep = ML.classification_report(y, preds, [])
    }}
    """
    interp = _run(code)
    env = interp.traditional.global_env
    return env.get('model'), env.get('probs'), env.get('preds'), env.get('rep')


def test_softmax_shapes_and_prob_sums():
    # 3-class toy, linearly separable clusters
    X = [
        [3.0, 3.0], [2.5, 3.5], [3.5, 2.0],  # class 0
        [-3.0, -3.0], [-2.5, -3.5], [-3.5, -2.0],  # class 1
        [3.0, -3.0], [2.5, -3.5], [3.5, -2.0],  # class 2
    ]
    y = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    model, probs, preds, rep = _train_softmax_and_predict(X, y, lr=0.2, epochs=400)

    # Model structure
    assert isinstance(model, dict)
    assert set(model.keys()) == {"labels", "W", "b"}
    assert model["labels"] == [0, 1, 2]
    assert len(model["W"]) == 3 and len(model["W"][0]) == 2
    assert len(model["b"]) == 3

    # Probabilities shape and sum to 1
    assert len(probs) == len(X)
    for p in probs:
        assert len(p) == 3
        s = sum(p)
        assert abs(s - 1.0) < 1e-6

    # Predictions length
    assert len(preds) == len(y)


def test_softmax_accuracy_and_metrics():
    X = [
        [3.0, 3.0], [2.5, 3.5], [3.5, 2.0],
        [-3.0, -3.0], [-2.5, -3.5], [-3.5, -2.0],
        [3.0, -3.0], [2.5, -3.5], [3.5, -2.0],
    ]
    y = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    model, probs, preds, rep = _train_softmax_and_predict(X, y, lr=0.2, epochs=500)

    # Perfect (or near-perfect) classification on simple clusters
    acc = rep["accuracy"]
    assert acc >= 0.95

    micro = rep["micro_avg"]
    macro = rep["macro_avg"]
    for k in ("precision", "recall", "f1"):
        assert micro[k] >= 0.95
        assert macro[k] >= 0.95

    # Argmax mapping to labels order
    assert set(preds) <= {0, 1, 2}

