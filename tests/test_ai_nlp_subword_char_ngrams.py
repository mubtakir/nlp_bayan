from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_char_ngram_vocab_and_encode():
    code = """
    import ai.nlp as nlp
    hybrid {
      docs = ["البيان", "بيان"]
      vocab = nlp.char_ngram_vocab_build(docs, 2, 100, 1)
      ids = nlp.char_ngram_encode("البيان", vocab, 2)
      tokens = nlp.vocab_decode_ids(ids, vocab)

      vocab_ar = nlp.بناء_قاموس_محارف(docs, 2, 100, 1)
      ids_ar = nlp.ترميز_محارف_بانجرام("البيان", vocab_ar, 2)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env

    vocab = env.get("vocab")
    ids = env.get("ids")
    tokens = env.get("tokens")
    vocab_ar = env.get("vocab_ar")
    ids_ar = env.get("ids_ar")

    assert isinstance(vocab, dict)
    token_to_id = vocab["token_to_id"]
    id_to_token = vocab["id_to_token"]

    # basic sanity checks on vocab structure
    assert isinstance(token_to_id, dict)
    assert isinstance(id_to_token, dict)
    assert vocab["pad_id"] == token_to_id["PAD"]
    assert vocab["unk_id"] == token_to_id["UNK"]

    # ids and tokens should be non-empty and same length
    assert isinstance(ids, list) and len(ids) > 0
    assert isinstance(tokens, list) and len(tokens) == len(ids)

    # all decoded tokens should be n-grams of length 2
    assert all(isinstance(t, str) and len(t) == 2 for t in tokens)

    # Arabic wrappers should behave consistently with the English API
    assert isinstance(vocab_ar, dict)
    assert isinstance(ids_ar, list)
    assert ids_ar == ids

