from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def _run(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def _build_and_compare_soft_vs_hard(text1, text2, corpus, thr=0.9):
    code = f"""
    import ai.nlp as NLP
    hybrid {{
        model = NLP.soft_tfidf_build({corpus}, {thr})
        ssoft = NLP.soft_tfidf_cosine_similarity({text1!r}, {text2!r}, model)
        shard = NLP.tfidf_cosine_similarity({text1!r}, {text2!r})
        v1 = NLP.soft_tfidf_vector({text1!r}, model)
        v2 = NLP.soft_tfidf_vector({text2!r}, model)
    }}
    """
    interp = _run(code)
    env = interp.traditional.global_env
    return env.get('ssoft'), env.get('shard'), env.get('v1'), env.get('v2')


def test_soft_tfidf_improves_similarity_with_typos():
    t1 = "new york city is great"
    t2 = "new yrok ctiy is grat"  # typos: york->yrok, city->ctiy, great->grat
    corpus = [t1, t2]
    ssoft, shard, v1, v2 = _build_and_compare_soft_vs_hard(t1, t2, corpus, thr=0.88)

    # Soft TF-IDF should yield a higher similarity than standard TF-IDF for typos
    assert ssoft > shard
    # Vectors are non-empty
    assert isinstance(v1, dict) and isinstance(v2, dict)
    assert len(v1) > 0 and len(v2) > 0


def test_soft_tfidf_identical_texts_high_similarity():
    t = "machine learning is fun"
    corpus = [t]
    ssoft, shard, v1, v2 = _build_and_compare_soft_vs_hard(t, t, corpus)
    assert ssoft >= 0.99
    assert shard >= 0.99

