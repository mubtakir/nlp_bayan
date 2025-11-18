from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_vocab_build_and_encode_decode():
    code = """
    import ai.nlp as nlp
    hybrid {
      docs = ["أحب البيان", "البيان لغة برمجة"]
      vocab = nlp.vocab_build(docs, 100, 1)
      ids = nlp.vocab_encode_tokens(["البيان", "لغة"], vocab)
      tokens = nlp.vocab_decode_ids(ids, vocab)

      vocab_ar = nlp.بناء_قاموس(docs, 100, 1)
      ids_ar = nlp.ترميز_كلمات_بقاموس(["البيان", "لغة"], vocab_ar)
      tokens_ar = nlp.فك_ترميز_معرفات_بقاموس(ids_ar, vocab_ar)

      ids_unknown = nlp.vocab_encode_tokens(["كلمةغيرمعروفة"], vocab)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env

    vocab = env.get("vocab")
    ids = env.get("ids")
    tokens = env.get("tokens")
    vocab_ar = env.get("vocab_ar")
    ids_ar = env.get("ids_ar")
    tokens_ar = env.get("tokens_ar")
    ids_unknown = env.get("ids_unknown")

    # basic structure checks
    assert isinstance(vocab, dict)
    token_to_id = vocab["token_to_id"]
    id_to_token = vocab["id_to_token"]

    # special tokens must exist with stable ids
    pad_id = vocab["pad_id"]
    unk_id = vocab["unk_id"]
    bos_id = vocab["bos_id"]
    eos_id = vocab["eos_id"]

    assert token_to_id["PAD"] == pad_id
    assert token_to_id["UNK"] == unk_id
    assert token_to_id["BOS"] == bos_id
    assert token_to_id["EOS"] == eos_id

    # encoding/decoding round-trip for known tokens
    assert ids == ids_ar
    # note: Arabic tokens are normalized internally ("لغة" -> "لغه")
    assert tokens == ["البيان", "لغه"]
    assert tokens_ar == tokens

    # unknown tokens should map to unk_id
    assert isinstance(ids_unknown, list) and len(ids_unknown) == 1
    assert ids_unknown[0] == unk_id

