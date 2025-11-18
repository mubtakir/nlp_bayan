from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_sequence_utils_and_metrics():
    code = """
    import ai.nlp as nlp
    hybrid {
      docs = ["أحب البيان", "البيان لغة"]
      vocab = nlp.vocab_build(docs, 100, 1)

      pad_id = vocab["pad_id"]
      bos_id = vocab["bos_id"]
      eos_id = vocab["eos_id"]

      ids1 = nlp.vocab_encode_tokens(["أحب", "البيان"], vocab)
      ids2 = nlp.vocab_encode_tokens(["البيان", "لغة"], vocab)

      seq1 = nlp.sequence_add_bos_eos(ids1, bos_id, eos_id)
      seq2 = nlp.sequence_add_bos_eos(ids2, bos_id, eos_id)

      # Arabic wrappers for sequence utilities
      seq1_ar = nlp.اضافة_بداية_نهاية_تسلسل(ids1, bos_id, eos_id)

      padded = nlp.sequence_pad([seq1, seq2], pad_id, 8)
      padded_ar = nlp.حشو_تسلسلات([seq1_ar, seq2], pad_id, 8)

      batches = nlp.sequence_batch(padded, 1)
      batches_ar = nlp.دفعات_تسلسلات(padded_ar, 1)

      log_probs = [-0.1, -0.2, -0.3]
      ce = nlp.sequence_cross_entropy_from_log_probs(log_probs)
      pp = nlp.sequence_perplexity_from_log_probs(log_probs)

      ce_ar = nlp.انتروبي_تتابع_من_لوغ(log_probs)
      pp_ar = nlp.بيربلكسيتي_تتابع_من_لوغ(log_probs)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env

    vocab = env.get("vocab")
    pad_id = vocab["pad_id"]
    bos_id = vocab["bos_id"]
    eos_id = vocab["eos_id"]

    seq1 = env.get("seq1")
    seq1_ar = env.get("seq1_ar")
    padded = env.get("padded")
    padded_ar = env.get("padded_ar")
    batches = env.get("batches")
    batches_ar = env.get("batches_ar")
    ce = env.get("ce")
    pp = env.get("pp")
    ce_ar = env.get("ce_ar")
    pp_ar = env.get("pp_ar")

    # Arabic wrapper for BOS/EOS should match English function
    assert isinstance(seq1, list)
    assert seq1_ar == seq1

    # basic structure checks for padded sequences
    assert isinstance(padded, list) and len(padded) == 2
    for seq in padded:
        assert isinstance(seq, list)
        assert len(seq) == 8
        # BOS/EOS should appear and padding should use pad_id
        assert seq[0] == bos_id
        assert pad_id in seq

    # Arabic wrapper for padding should match English function
    assert isinstance(padded_ar, list)
    assert padded_ar == padded

    # batches should wrap sequences in outer list
    assert isinstance(batches, list) and len(batches) == 2
    assert isinstance(batches[0], list) and len(batches[0]) == 1
    assert batches[0][0] == padded[0]

    # Arabic wrapper for batching should match English function
    assert isinstance(batches_ar, list)
    assert batches_ar == batches

    # cross-entropy from log-probabilities
    assert isinstance(ce, float)
    assert abs(ce - 0.2) < 1e-9

    # Arabic wrapper should match English function (within tolerance)
    assert abs(ce_ar - ce) < 1e-9

    # perplexity should be exp(ce)
    e = 2.718281828
    expected_pp = e ** ce
    assert isinstance(pp, float)
    assert abs(pp - expected_pp) < 1e-6

    # Arabic wrapper should match English perplexity
    assert abs(pp_ar - pp) < 1e-6

