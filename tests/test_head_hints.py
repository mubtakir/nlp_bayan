from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter
from bayan.bayan.logical_engine import Predicate, Term


def run(code: str):
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp.logical


def test_default_head_hints_ar():
    code = """
    hybrid {
      محمد الطبيب.
      عصير البرتقال.
      مالك السيارة.
      صاحب الدار.
      باب الغرفة.
      كاتب الرواية.
      مدير الشركة.
      رئيس القسم.
      مؤلف القصيدة.
      كتاب الفيزياء.
    }
    """
    logical = run(code)
    # isa
    sols_isa = logical.query(Predicate("isa", [Term("محمد", False), Term("طبيب", False)]))
    assert len(sols_isa) == 1
    # of
    sols_of1 = logical.query(Predicate("of", [Term("عصير", False), Term("X", True)]))
    assert len(sols_of1) == 1
    xv1 = sols_of1[0].lookup("X"); xv1 = getattr(xv1, 'value', xv1)
    assert xv1 == "برتقال"
    sols_of2 = logical.query(Predicate("of", [Term("باب", False), Term("Y", True)]))
    assert len(sols_of2) == 1
    yv = sols_of2[0].lookup("Y"); yv = getattr(yv, 'value', yv)
    assert yv == "غرفة"
    # belongs
    sols_b1 = logical.query(Predicate("belongs_to", [Term("سيارة", False), Term("مالك", False)]))
    # professional heads (AR)
    for head, gen in [("كاتب", "رواية"), ("مدير", "شركة"), ("رئيس", "قسم"), ("مؤلف", "قصيدة")]:
        sols = logical.query(Predicate("of", [Term(head, False), Term("X", True)]))
        assert len(sols) == 1
        xv = sols[0].lookup("X"); xv = getattr(xv, 'value', xv)
        assert xv == gen
    # object heads (AR)
    for head, gen in [("كتاب", "فيزياء")]:
        sols = logical.query(Predicate("of", [Term(head, False), Term("X", True)]))
        assert len(sols) == 1
        xv = sols[0].lookup("X"); xv = getattr(xv, 'value', xv)
        assert xv == gen

    assert len(sols_b1) == 1
    sols_b2 = logical.query(Predicate("belongs_to", [Term("دار", False), Term("صاحب", False)]))
    assert len(sols_b2) == 1


def test_default_head_hints_en():
    code = """
    hybrid {
      owner house.
      juice orange.
      door room.
      picture moon.
      photo cat.
      book physics.
      writer novel.
      manager company.
      author paper.
    }
    """
    logical = run(code)
    # belongs
    sols_b = logical.query(Predicate("belongs_to", [Term("house", False), Term("owner", False)]))
    assert len(sols_b) == 1
    # of (objects)
    for head, gen in [("juice", "orange"), ("door", "room"), ("picture", "moon"), ("photo", "cat"), ("book", "physics")]:
        sols = logical.query(Predicate("of", [Term(head, False), Term("X", True)]))
        assert len(sols) == 1
        xv = sols[0].lookup("X"); xv = getattr(xv, 'value', xv)
        assert xv == gen

    # of (professional heads)
    for head, gen in [("writer", "novel"), ("manager", "company"), ("author", "paper")]:
        sols = logical.query(Predicate("of", [Term(head, False), Term("X", True)]))
        assert len(sols) == 1
        xv = sols[0].lookup("X"); xv = getattr(xv, 'value', xv)
        assert xv == gen

