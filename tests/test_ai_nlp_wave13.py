import pytest
from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_tfidf_cosine_similarity():
    code = """
    import ai.nlp as nlp
    hybrid {
      t1 = "machine learning is fun and useful"
      t2 = "learning machines are very useful"
      s = nlp.tfidf_cosine_similarity(t1, t2)
    }
    """
    interp = run_interp(code)
    s = interp.traditional.global_env.get('s')
    assert s > 0.2 and s <= 1.0


def test_nlp_bm25_top_k_basic():
    code = """
    import ai.nlp as nlp
    hybrid {
      docs = ["a a a", "a b", "b b b"]
      m = nlp.bm25_build(docs, 1.5, 0.75)
      top = nlp.bm25_top_k(m, "a b", 2)
      top0 = top[0]
      top1 = top[1]
      idx0 = top0[0]
      idx1 = top1[0]
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    idx0 = env.get('idx0')
    idx1 = env.get('idx1')
    # Expect doc 0 (heavy 'a') or doc 1 to be among top; doc 2 (only 'b') likely not top-1 for query "a b"
    assert idx0 in (0, 1)
    assert idx1 in (0, 1, 2)


def test_nlp_arabic_wrappers_wave13():
    code = """
    import ai.nlp as nlp
    hybrid {
      س = nlp.تشابه_جيبي_TFIDF("تعلم الآلة مفيد", "التعلم مفيد")
      أفضل = nlp.أفضل_BM25(nlp.bm25_build(["سلام عليكم", "تعلم مفيد"], 1.5, 0.75), "تعلم", 1)
      أفضل0 = أفضل[0]
      أفضل_المؤشر = أفضل0[0]
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    س = env.get('س')
    أفضل_المؤشر = env.get('أفضل_المؤشر')
    assert س >= 0.0 and س <= 1.0
    assert أفضل_المؤشر in (0, 1)

