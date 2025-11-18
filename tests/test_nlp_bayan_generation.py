from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_generate_trigram_ar_basic():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        s = gen.generate_trigram_ar("محمد", "ذهب", 4)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')

    assert isinstance(s, str)
    assert s.startswith("محمد ذهب")
    assert len(s.split()) >= 2



def test_generate_trigram_from_docs_custom():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد ذهب المدرسة", "محمد يحب القراءة", "الطالب يقرأ الدرس"]
        s2 = gen.generate_trigram_from_docs("محمد", "ذهب", docs, 4, 1)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s2 = env.get('s2')

    assert isinstance(s2, str)
    assert s2.startswith("محمد ذهب")
    assert len(s2.split()) >= 2



def test_generate_trigram_from_docs_fallback_to_bigram():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد زار المدرسة", "الطالب زار المتحف"]
        s = gen.generate_trigram_from_docs("أحمد", "زار", docs, 2, 1)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "أحمد" and words[1] == "زار"
    assert len(words) >= 3
    assert words[2] in {"المدرسة", "المتحف"}


def test_generate_trigram_from_docs_fallback_break_when_bigram_empty():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد ذهب المدرسة"]
        s = gen.generate_trigram_from_docs("أحمد", "زار", docs, 3, 1)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words == ["أحمد", "زار"]




def test_generate_trigram_kb_prefers_allowed_candidate():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد زار الحديقة", "سعد زار الساحة"]
        tok_map = {"الحديقة": "garden", "الساحة": "square"}
        s = gen.generate_trigram_kb_from_docs("سعد", "زار", docs, 1, 5, "maybe", "is_green", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "زار"
    assert len(words) >= 3
    assert words[2] == "الحديقة"


def test_generate_trigram_kb_no_allowed_falls_back():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد زار الساحة"]
        # لا نضع تعيينًا للحديقة حتى لو ظهرت بالتنعيم؛ نقيّد الخريطة على "الساحة" فقط
        tok_map = {"الساحة": "square"}
        s = gen.generate_trigram_kb_from_docs("سعد", "زار", docs, 1, 5, "maybe", "is_green", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "زار"
    assert len(words) >= 3
    # لا يوجد مرشح مسموح به حسب KB
    assert words[2] == "الساحة"



def test_generate_trigram_kb_entity_backoff_to_house():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        #
        # docs: KB/trigram backoff test
        docs = ["سعد زار المتحف"]
        tok_map = {"الطالب": "student", "البيت": "house"}
        s = gen.generate_trigram_kb_from_docs("الطالب", "ذهب", docs, 1, 5, "maybe", "is_green", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "الطالب" and words[1] == "ذهب"
    assert len(words) >= 3
    # بعد خطوة الصرف، نتوقع إدخال "الى" قبل المكان: "الطالب ذهب الى البيت"
    if len(words) >= 4 and words[2] == "الى":
        assert words[3] == "البيت"
    else:
        assert words[2] == "البيت"



def test_generate_trigram_kb_temp0_picks_top1():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        # نكرر "الحديقة" لرفع احتمالها مقابل "الساحة"
        docs = ["سعد زار الحديقة", "سعد زار الحديقة", "سعد زار الساحة"]
        tok_map = {"الحديقة": "garden", "الساحة": "square"}
        # temperature=0.0 يجب أن يختار أعلى مرشح (الحديقة)
        s = gen.generate_trigram_kb_from_docs("سعد", "زار", docs, 1, 2, "any", "x", tok_map, 0.0, 77)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "زار"
    assert len(words) >= 3
    assert words[2] == "الحديقة"


def test_generate_trigram_kb_sampling_reproducible_with_seed():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد زار الحديقة", "سعد زار الساحة"]
        tok_map = {"الحديقة": "garden", "الساحة": "square"}
        s1 = gen.generate_trigram_kb_from_docs("سعد", "زار", docs, 1, 2, "any", "x", tok_map, 1.0, 123)
        s2 = gen.generate_trigram_kb_from_docs("سعد", "زار", docs, 1, 2, "any", "x", tok_map, 1.0, 123)
        s3 = gen.generate_trigram_kb_from_docs("سعد", "زار", docs, 1, 2, "any", "x", tok_map, 1.0, 124)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s1 = env.get('s1')
    s2 = env.get('s2')
    s3 = env.get('s3')
    # نفس البذرة => نفس المخرجات
    assert s1 == s2
    # جميع المخرجات ضمن المجموعة المسموح بها
    w1 = s1.split()[2]
    w2 = s2.split()[2]
    w3 = s3.split()[2]
    assert w1 in {"الحديقة", "الساحة"}
    assert w2 in {"الحديقة", "الساحة"}
    assert w3 in {"الحديقة", "الساحة"}



def test_generate_trigram_kb_entity_backoff_student_prefers_school():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        # لا تُساعِد الوثائق على توليد الثلاثي مباشرةً لهذا السياق
        docs = ["سعد زار المتحف"]
        # نوفر المدرسـة والبيت كجهات محتملة؛ الكيان الطالب يملك المدرسة مباشرةً
        tok_map = {"الطالب": "student", "المدرسة": "school", "البيت": "house"}
        s = gen.generate_trigram_kb_from_docs("الطالب", "ذهب", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "الطالب" and words[1] == "ذهب"
    # يجب تفضيل الهدف المباشر (المدرسة) على الموروث (البيت)
    assert (len(words) >= 4 and words[2] == "الى" and words[3] == "المدرسة") or words[2] == "المدرسة"



def test_generate_trigram_kb_entity_backoff_teacher_prefers_school():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد زار المتحف"]
        tok_map = {"المعلم": "teacher", "المدرسة": "school", "البيت": "house"}
        s = gen.generate_trigram_kb_from_docs("المعلم", "ذهب", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "المعلم" and words[1] == "ذهب"
    # يُفضَّل الهدف المباشر (المدرسة) على الموروث (البيت)
    assert (len(words) >= 4 and words[2] == "الى" and words[3] == "المدرسة") or words[2] == "المدرسة"


def test_morpho_inserts_ila_for_mosque():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد": "person", "المسجد": "mosque"}
        s = gen.generate_trigram_kb_from_docs("سعد", "ذهب", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "ذهب"
    # ";الى" يجب إدراجها قبل "المسجد"
    assert len(words) >= 4 and words[2] == "الى" and words[3] == "المسجد"



def test_morpho_inserts_ila_for_dakhal():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد": "person", "المسجد": "mosque"}
        s = gen.generate_trigram_kb_from_docs("سعد", "دخل", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "دخل"
    assert len(words) >= 4 and words[2] == "الى" and words[3] == "المسجد"


def test_morpho_inserts_min_for_kharaja():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"الطالب": "person", "البيت": "house"}
        s = gen.generate_trigram_kb_from_docs("الطالب", "خرج", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "الطالب" and words[1] == "خرج"
    assert len(words) >= 4 and words[2] == "من" and words[3] == "البيت"


def test_morpho_inserts_ila_for_aada():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد": "person", "البيت": "house"}
        s = gen.generate_trigram_kb_from_docs("سعد", "عاد", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "عاد"
    assert len(words) >= 4 and words[2] == "الى" and words[3] == "البيت"


def test_morpho_inserts_fi_for_jalasa():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد": "person", "المسجد": "mosque"}
        s = gen.generate_trigram_kb_from_docs("سعد", "جلس", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "جلس"
    assert len(words) >= 4 and words[2] == "في" and words[3] == "المسجد"



def test_morpho_inserts_fi_for_jalasa_library():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد": "person", "المكتبة": "library"}
        s = gen.generate_trigram_kb_from_docs("سعد", "جلس", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "جلس"
    assert len(words) >= 4 and words[2] == "في" and words[3] == "المكتبة"



def test_enter_prefers_indoor_over_outdoor():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد": "person", "المسجد": "mosque", "السوق": "market"}
        s = gen.generate_trigram_kb_from_docs("سعد", "دخل", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "دخل"
    assert len(words) >= 4 and words[2] == "الى" and words[3] == "المسجد"


def test_exit_prefers_outdoor_over_indoor():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"الطالب": "person", "السوق": "market", "المكتبة": "library"}
        s = gen.generate_trigram_kb_from_docs("الطالب", "خرج", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "الطالب" and words[1] == "خرج"
    assert len(words) >= 4 and words[2] == "من" and words[3] == "السوق"


def test_return_prefers_house_over_others():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد": "person", "البيت": "house", "السوق": "market"}
        s = gen.generate_trigram_kb_from_docs("سعد", "عاد", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "عاد"
    assert len(words) >= 4 and words[2] == "الى" and words[3] == "البيت"



def test_morpho_and_kb_with_new_places_restaurant():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد": "person", "المطعم": "restaurant"}
        s = gen.generate_trigram_kb_from_docs("سعد", "جلس", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "جلس"
    assert len(words) >= 4 and words[2] == "في" and words[3] == "المطعم"



def test_top_p_limits_to_top1_even_with_temperature():
    # نبني توزيعًا مُنحازًا بقوة نحو "الحديقة" مقابل "الساحة"
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد زار الحديقة", "سعد زار الحديقة", "سعد زار الحديقة", "سعد زار الحديقة", "سعد زار الحديقة", "سعد زار الساحة"]
        tok_map = {"الحديقة": "garden", "الساحة": "square"}
        s = gen.generate_trigram_kb_from_docs("سعد", "زار", docs, 1, 2, "any", "x", tok_map, 1.0, 42, 0.5)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "زار"
    # nucleus صغير يجب أن يُلزِم الاختيار بـ "الحديقة" فقط
    assert len(words) >= 3 and words[2] == "الحديقة"



def test_enter_prefers_university_over_beach():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد":"person", "الجامعة":"university", "الشاطئ":"beach"}
        s = gen.generate_trigram_kb_from_docs("سعد", "دخل", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "دخل"
    assert len(words) >= 4 and words[2] == "الى" and words[3] == "الجامعة"


def test_sit_prefers_cafe():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد":"person", "المقهى":"cafe", "الشاطئ":"beach"}
        s = gen.generate_trigram_kb_from_docs("سعد", "جلس", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "جلس"
    assert len(words) >= 4 and words[2] == "في" and words[3] == "المقهى"


def test_exit_prefers_outdoor_beach_or_stadium():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"الطالب":"person", "الشاطئ":"beach", "الملعب":"stadium"}
        s = gen.generate_trigram_kb_from_docs("الطالب", "خرج", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "الطالب" and words[1] == "خرج"
    assert len(words) >= 4 and words[2] == "من" and words[3] in {"الشاطئ", "الملعب"}


def test_enter_hotel_indoor():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد":"person", "الفندق":"hotel", "الشاطئ":"beach"}
        s = gen.generate_trigram_kb_from_docs("سعد", "دخل", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "دخل"
    assert len(words) >= 4 and words[2] == "الى" and words[3] == "الفندق"



def test_morpho_inserts_ila_for_wasal():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد": "person", "المطار": "airport"}
        s = gen.generate_trigram_kb_from_docs("سعد", "وصل", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "وصل"
    assert len(words) >= 4 and words[2] == "الى" and words[3] == "المطار"


def test_morpho_inserts_ila_for_tawajja():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد": "person", "الجامعة": "university"}
        s = gen.generate_trigram_kb_from_docs("سعد", "توجه", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "توجه"
    assert len(words) >= 4 and words[2] == "الى" and words[3] == "الجامعة"


def test_morpho_inserts_ba_for_mar():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد": "person", "السوق": "market"}
        s = gen.generate_trigram_kb_from_docs("سعد", "مر", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "مر"
    assert len(words) >= 4 and words[2] == "ب" and words[3] == "السوق"


def test_morpho_inserts_min_for_iqtaraba():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد": "person", "السوق": "market"}
        s = gen.generate_trigram_kb_from_docs("سعد", "اقترب", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "اقترب"
    assert len(words) >= 4 and words[2] == "من" and words[3] == "السوق"


def test_morpho_inserts_an_for_ibtaada():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد": "person", "السوق": "market"}
        s = gen.generate_trigram_kb_from_docs("سعد", "ابتعد", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "ابتعد"
    assert len(words) >= 4 and words[2] == "عن" and words[3] == "السوق"


def test_morpho_inserts_ila_for_safara():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد": "person", "المطار": "airport"}
        s = gen.generate_trigram_kb_from_docs("سعد", "سافر", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "سافر"
    assert len(words) >= 4 and words[2] == "الى" and words[3] == "المطار"



def test_safara_prefers_travel_place_over_mall():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد سافر المتحف"]
        tok_map = {"سعد":"person", "المطار":"airport", "المول":"mall"}
        s = gen.generate_trigram_kb_from_docs("سعد", "سافر", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "سافر"
    assert len(words) >= 4 and words[2] == "الى" and words[3] == "المطار"


def test_zara_prefers_visitable_over_airport():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد زار المتحف", "سعد زار المطار"]
        tok_map = {"سعد":"person", "المتحف":"museum", "المطار":"airport"}
        s = gen.generate_trigram_kb_from_docs("سعد", "زار", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "زار"
    assert len(words) >= 3 and words[2] == "المتحف"


def test_mar_prefers_outdoor_beach_over_hotel():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد مر السوق"]
        tok_map = {"سعد":"person", "الشاطئ":"beach", "الفندق":"hotel"}
        s = gen.generate_trigram_kb_from_docs("سعد", "مر", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "مر"
    assert len(words) >= 4 and words[2] == "ب" and words[3] == "الشاطئ"


def test_kb_weighting_prefers_visitable_in_top_p():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        # نجعل احتمالات المتحف والفندق متقاربة في النماذج الإحصائية
        docs = ["سعد زار المتحف", "سعد زار الفندق"]
        tok_map = {"سعد":"person", "المتحف":"museum", "الفندق":"hotel"}
        # temperature=0 مع top_p>0 سيحترم ترتيب الاحتمالات بعد تعزيز KB
        s = gen.generate_trigram_kb_from_docs("سعد", "زار", docs, 1, 2, "any", "x", tok_map, 0.0, 123, 0.9)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "زار"
    # يجب أن يُفَضَّل المتحف (visitable) على الفندق
    assert len(words) >= 3 and words[2] == "المتحف"


def test_morpho_merges_ba_al_to_bal():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد مر السوق"]
        tok_map = {"سعد":"person", "السوق":"market"}
        s = gen.generate_trigram_kb_from_docs("سعد", "مر", docs, 1, 5, "any", "x", tok_map, 0.0, 7, 0.0, True)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "مر"
    # بعد الدمج، يجب أن تظهر "بالسوق" ككلمة واحدة
    assert any(w == "بالسوق" for w in words)



def test_morpho_merges_ba_al_to_bal_stadium():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد مر الملعب"]
        tok_map = {"سعد":"person", "الملعب":"stadium"}
        s = gen.generate_trigram_kb_from_docs("سعد", "مر", docs, 1, 5, "any", "x", tok_map, 0.0, 7, 0.0, True)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "مر"
    assert any(w == "بالملعب" for w in words)



def test_stop_tokens_break_after_min_length():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد جلس المقهى", "المقهى جميل"]
        tok_map = {"سعد":"person", "المقهى":"cafe"}
        # steps كبيرة لكن سنتوقف مبكرًا عند ظهور المقهى كرمز توقف بعد بلوغ الحد الأدنى
        s = gen.generate_trigram_kb_from_docs("سعد", "جلس", docs, 1, 10, "any", "x", tok_map, 0.0, 3, 0.0, True, ["المقهى"], 0, 1, 5)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "جلس"
    assert "المقهى" in words
    # يجب أن نتوقف مباشرة بعد إدراج "المقهى" (مع احتمال إدراج "في" قبلها صرفيًا)
    assert len(words) <= 4


def test_max_length_enforced_no_morpho_insert():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد زار المتحف", "سعد زار المكتبة"]
        tok_map = {"سعد":"person", "المتحف":"museum", "المكتبة":"library"}
        # نجعل الحد الأقصى لكلمات التوليد = 1، فلا يزيد الطول عن 3 كلمات (كلمتا البذرة + 1)
        s = gen.generate_trigram_kb_from_docs("سعد", "زار", docs, 1, 10, "any", "x", tok_map, 0.0, 5, 0.0, False, [], 0, 0, 1)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "زار"
    assert len(words) == 3


def test_min_length_overrides_stop_until_reached():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد جلس المقهى", "المقهى جميل"]
        tok_map = {"سعد":"person", "المقهى":"cafe"}
        # نطلب حدًا أدنى = 2، فلا يُسمح بالتوقف عند ظهور "المقهى" في أول خطوة
        s = gen.generate_trigram_kb_from_docs("سعد", "جلس", docs, 1, 10, "any", "x", tok_map, 0.0, 3, 0.0, True, ["المقهى"], 0, 2, 2)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "جلس"
    assert len(words) >= 4



def test_morpho_inserts_min_for_ghadara():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد":"person", "الشاطئ":"beach"}
        s = gen.generate_trigram_kb_from_docs("سعد", "غادر", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "غادر"
    assert len(words) >= 4 and words[2] == "من" and words[3] == "الشاطئ"


def test_istaqara_prefers_indoor_over_outdoor():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["محمد زار المتحف"]
        tok_map = {"سعد":"person", "الفندق":"hotel", "الشاطئ":"beach"}
        s = gen.generate_trigram_kb_from_docs("سعد", "استقر", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "استقر"
    assert len(words) >= 4 and words[2] == "في" and words[3] == "الفندق"



def test_haraba_prefers_outdoor_and_inserts_min():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد زار الشاطئ", "سعد زار الشاطئ", "سعد زار الفندق"]
        tok_map = {"سعد":"person", "الشاطئ":"beach", "الفندق":"hotel"}
        s = gen.generate_trigram_kb_from_docs("سعد", "هرب", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "هرب"
    assert len(words) >= 4 and words[2] == "من" and words[3] == "الشاطئ"


def test_tawajjaha_inserts_ila_prefers_high_prob_go_target():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["سعد زار الجامعة", "سعد زار الجامعة", "سعد زار السوق"]
        tok_map = {"سعد":"person", "الجامعة":"university", "السوق":"market"}
        s = gen.generate_trigram_kb_from_docs("سعد", "توجه", docs, 1, 5, "any", "x", tok_map, 0.0, 11)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "توجه"
    assert len(words) >= 4 and words[2] == "الى" and words[3] == "الجامعة"



def test_empty_docs_safe_generation_go_seeded():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = []
        tok_map = {"سعد":"person", "الجامعة":"university"}
        s = gen.generate_trigram_kb_from_docs("سعد", "توجه", docs, 3, 3, "any", "x", tok_map, 0.0, 7)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert len(words) >= 2
    assert words[0] == "سعد" and words[1] == "توجه"



def test_combined_controls_no_crash_and_respect_length():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = [
            "سعد ذهب الى الحديقة",
            "سعد ذهب الى السوق",
            "سعد ذهب الى المدرسة"
        ]
        tok_map = {"الحديقة":"garden","السوق":"market","المدرسة":"school"}
        s = gen.generate_trigram_kb_from_docs(
            "سعد", "ذهب", docs,
            4, 3,
            "any", "x", tok_map,
            0.8, 2025,
            0.8, False,
            ["."], 2,
            4, 7
        )
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "سعد" and words[1] == "ذهب"
    # احترام حدود الطول
    assert 4 <= len(words) <= 7
    # لا تكرار للثنائيات إذا طُلب ذلك
    bigrams = list(zip(words, words[1:]))
    assert len(bigrams) == len(set(bigrams))


def test_raja_morphology_inserts_ila_and_picks_house_by_docs():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = [
            "\u0633\u0639\u062f \u0631\u062c\u0639 \u0627\u0644\u0628\u064a\u062a",
            "\u0633\u0639\u062f \u0631\u062c\u0639 \u0627\u0644\u0628\u064a\u062a",
            "\u0633\u0639\u062f \u0631\u062c\u0639 \u0627\u0644\u0633\u0648\u0642"
        ]
        tok_map = {"\u0627\u0644\u0628\u064a\u062a":"house","\u0627\u0644\u0633\u0648\u0642":"market"}
        s = gen.generate_trigram_kb_from_docs("\u0633\u0639\u062f","\u0631\u062c\u0639",docs,1,5,"any","x",tok_map,0.0,77)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0]=="\u0633\u0639\u062f" and words[1]=="\u0631\u062c\u0639"
    assert len(words) >= 4 and words[2]=="\u0627\u0644\u0649" and words[3]=="\u0627\u0644\u0628\u064a\u062a"




def test_raja_prefers_house_over_others():
    code = """
    import nlp_bayan.core.generator_pipeline as gen
    hybrid {
        docs = ["\u0645\u062d\u0645\u062f \u0632\u0627\u0631 \u0627\u0644\u0645\u062a\u062d\u0641"]
        tok_map = {"\u0633\u0639\u062f": "person", "\u0627\u0644\u0628\u064a\u062a": "house", "\u0627\u0644\u0633\u0648\u0642": "market"}
        s = gen.generate_trigram_kb_from_docs("\u0633\u0639\u062f", "\u0631\u062c\u0639", docs, 1, 5, "any", "x", tok_map)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    s = env.get('s')
    words = s.split()
    assert words[0] == "\u0633\u0639\u062f" and words[1] == "\u0631\u062c\u0639"
    assert len(words) >= 4 and words[2] == "\u0627\u0644\u0649" and words[3] == "\u0627\u0644\u0628\u064a\u062a"
