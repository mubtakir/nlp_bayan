from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_cooccurrence_build_and_similarity():
    code = """
    import ai.nlp as nlp
    hybrid {
      docs = ["أحب البيان", "البيان لغة", "أحب لغة البيان"]
      model = nlp.cooccurrence_build(docs, 1)
      v1 = nlp.cooccurrence_vector(model, "البيان")
      v2 = nlp.cooccurrence_vector(model, "لغة")
      sim = nlp.cooccurrence_similarity(model, "البيان", "لغة")
      sim_self = nlp.cooccurrence_similarity(model, "البيان", "البيان")

      model_ar = nlp.بناء_تضمين_تلازم(docs, 1)
      v1_ar = nlp.متجه_تلازم(model_ar, "البيان")
      sim_ar = nlp.تشابه_تلازم(model_ar, "البيان", "لغة")
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env

    model = env.get("model")
    v1 = env.get("v1")
    v2 = env.get("v2")
    sim = env.get("sim")
    sim_self = env.get("sim_self")
    model_ar = env.get("model_ar")
    v1_ar = env.get("v1_ar")
    sim_ar = env.get("sim_ar")

    # basic structure checks
    assert isinstance(model, dict)
    vocab = model["vocab"]
    cooc = model["cooc"]
    assert isinstance(vocab, dict)
    assert isinstance(cooc, dict)

    # co-occurrence vectors should be non-empty for frequent words
    assert isinstance(v1, dict) and len(v1) > 0
    assert isinstance(v2, dict) and len(v2) > 0

    # similarity values should be within [0, 1]
    assert isinstance(sim, float)
    assert 0.0 <= sim <= 1.0
    assert isinstance(sim_self, float)
    assert 0.0 <= sim_self <= 1.0
    # a word should not be less similar to itself than to another word
    assert sim_self >= sim

    # Arabic wrappers should behave consistently with the English API
    assert isinstance(model_ar, dict)
    assert isinstance(v1_ar, dict)
    assert v1_ar == v1
    assert isinstance(sim_ar, float)
    assert sim_ar == sim

