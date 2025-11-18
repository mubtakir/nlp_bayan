from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_nlp_lm_eval_and_pipeline_ar_en_wrappers():
    code = """
    import ai.nlp as nlp
    hybrid {
      docs = ["أحب البيان", "البيان لغة جميلة"]

      vocab = nlp.vocab_build(docs, 100, 1)

      seqs = nlp.lm_prepare_id_sequences(docs, vocab)
      io = nlp.lm_make_input_target(seqs)
      inputs = io["inputs"]
      targets = io["targets"]

      seqs_ar = nlp.تتابعات_معرفات_من_نصوص(docs, vocab)
      io_ar = nlp.مدخلات_اهداف_من_تتابعات(seqs_ar)
      inputs_ar = io_ar["inputs"]
      targets_ar = io_ar["targets"]

      model_bg = nlp.bigram_lm_train(docs, 1.0)
      logs_bg = nlp.bigram_lm_text_log_probs(model_bg, "أحب البيان")
      ce_bg = nlp.bigram_lm_cross_entropy(model_bg, "أحب البيان")
      pp_bg = nlp.bigram_lm_perplexity(model_bg, "أحب البيان")

      logs_bg_ar = nlp.لوغ_احتمالات_ثنائي_من_نص(model_bg, "أحب البيان")
      ce_bg_ar = nlp.انتروبي_ثنائي_من_نص(model_bg, "أحب البيان")
      pp_bg_ar = nlp.بيربلكسيتي_ثنائي_من_نص(model_bg, "أحب البيان")

      model_tg = nlp.trigram_lm_train(docs, 1.0)
      logs_tg = nlp.trigram_lm_text_log_probs(model_tg, "أحب البيان لغة")
      ce_tg = nlp.trigram_lm_cross_entropy(model_tg, "أحب البيان لغة")
      pp_tg = nlp.trigram_lm_perplexity(model_tg, "أحب البيان لغة")

      logs_tg_ar = nlp.لوغ_احتمالات_ثلاثي_من_نص(model_tg, "أحب البيان لغة")
      ce_tg_ar = nlp.انتروبي_ثلاثي_من_نص(model_tg, "أحب البيان لغة")
      pp_tg_ar = nlp.بيربلكسيتي_ثلاثي_من_نص(model_tg, "أحب البيان لغة")
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env

    # LM prepare sequences
    seqs = env.get("seqs")
    seqs_ar = env.get("seqs_ar")
    assert isinstance(seqs, list)
    assert isinstance(seqs_ar, list)
    assert seqs == seqs_ar
    assert len(seqs) == 2

    io = env.get("io")
    io_ar = env.get("io_ar")
    inputs = env.get("inputs")
    targets = env.get("targets")
    inputs_ar = env.get("inputs_ar")
    targets_ar = env.get("targets_ar")

    assert isinstance(io, dict)
    assert isinstance(io_ar, dict)
    assert inputs == io["inputs"]
    assert targets == io["targets"]
    assert inputs_ar == io_ar["inputs"]
    assert targets_ar == io_ar["targets"]
    assert inputs == inputs_ar
    assert targets == targets_ar
    assert len(inputs) == len(targets) > 0

    logs_bg = env.get("logs_bg")
    logs_bg_ar = env.get("logs_bg_ar")
    assert isinstance(logs_bg, list)
    assert logs_bg == logs_bg_ar
    assert len(logs_bg) > 0
    for v in logs_bg:
        assert isinstance(v, float)
        assert v <= 0.0

    ce_bg = env.get("ce_bg")
    ce_bg_ar = env.get("ce_bg_ar")
    pp_bg = env.get("pp_bg")
    pp_bg_ar = env.get("pp_bg_ar")

    assert isinstance(ce_bg, float)
    assert isinstance(pp_bg, float)
    assert ce_bg > 0.0
    assert pp_bg >= 1.0
    assert abs(ce_bg - ce_bg_ar) < 1e-6
    assert abs(pp_bg - pp_bg_ar) < 1e-6

    logs_tg = env.get("logs_tg")
    logs_tg_ar = env.get("logs_tg_ar")
    assert isinstance(logs_tg, list)
    assert logs_tg == logs_tg_ar
    # For a 3-token sentence we expect exactly 1 trigram
    assert len(logs_tg) == 1

    ce_tg = env.get("ce_tg")
    ce_tg_ar = env.get("ce_tg_ar")
    pp_tg = env.get("pp_tg")
    pp_tg_ar = env.get("pp_tg_ar")

    assert isinstance(ce_tg, float)
    assert isinstance(pp_tg, float)
    assert ce_tg > 0.0
    assert pp_tg >= 1.0
    assert abs(ce_tg - ce_tg_ar) < 1e-6
    assert abs(pp_tg - pp_tg_ar) < 1e-6

