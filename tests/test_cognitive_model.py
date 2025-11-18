"""
Tests for Cognitive-Semantic Model
اختبارات للنموذج المعرفي-الدلالي
"""

from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
from bayan.bayan.traditional_interpreter import TraditionalInterpreter


def test_cognitive_entity_english():
    """Test cognitive entity definition in English"""
    code = """
cognitive_entity أرض:
{
    لون: "بني"
    حالة: "جافة"
    خصوبة: 0.2
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    
    interp = TraditionalInterpreter()
    interp.interpret(ast)
    
    # Check entity was created
    assert "أرض" in interp._cognitive_entities
    assert interp._cognitive_entities["أرض"]["لون"] == "بني"
    assert interp._cognitive_entities["أرض"]["حالة"] == "جافة"
    assert interp._cognitive_entities["أرض"]["خصوبة"] == 0.2


def test_cognitive_entity_arabic():
    """Test cognitive entity definition in Arabic"""
    code = """
كيان_معرفي شخص:
{
    اسم: "محمد"
    عمر: 25
    مهنة: "مهندس"
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    
    interp = TraditionalInterpreter()
    interp.interpret(ast)
    
    # Check entity was created
    assert "شخص" in interp._cognitive_entities
    assert interp._cognitive_entities["شخص"]["اسم"] == "محمد"
    assert interp._cognitive_entities["شخص"]["عمر"] == 25


def test_cognitive_event_simple():
    """Test simple cognitive event"""
    code = """
cognitive_entity أرض:
{
    لون: "بني"
    حالة: "جافة"
}

cognitive_event نزول_المطر:
{
    participants: {
        "أرض": {"role": "متأثر", "degree": 1.0}
    },
    strength: 0.8,
    transform: {
        "أرض.لون": "أخضر",
        "أرض.حالة": "رطبة"
    }
}

trigger نزول_المطر
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    
    interp = TraditionalInterpreter()
    interp.interpret(ast)
    
    # Check entity state was transformed
    assert interp._cognitive_entities["أرض"]["لون"] == "أخضر"
    assert interp._cognitive_entities["أرض"]["حالة"] == "رطبة"


def test_cognitive_event_arabic():
    """Test cognitive event in Arabic"""
    code = """
كيان_معرفي محمد:
{
    حالة: "طالب"
    معرفة: 0.5
}

حدث_معرفي دراسة:
{
    مشاركون: {
        "محمد": {"دور": "فاعل", "درجة": 1.0}
    },
    قوة: 0.9,
    تحويل: {
        "محمد.معرفة": 0.9,
        "محمد.حالة": "متعلم"
    }
}

أطلق دراسة
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    
    interp = TraditionalInterpreter()
    interp.interpret(ast)
    
    # Check entity state was transformed
    assert interp._cognitive_entities["محمد"]["معرفة"] == 0.9
    assert interp._cognitive_entities["محمد"]["حالة"] == "متعلم"


def test_idea_definition():
    """Test idea definition"""
    code = """
idea "الأرض الخضراء":
{
    entities: {
        "أرض": {"state": "جافة"},
        "ماء": {"state": "متوفر"}
    },
    event: "نزول_المطر",
    result: {
        "state_changes": {
            "أرض.لون": "أخضر"
        }
    }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    
    interp = TraditionalInterpreter()
    interp.interpret(ast)
    
    # Check idea was stored (name is stored with quotes from string literal)
    idea_name = list(interp._ideas.keys())[0]
    assert "الأرض الخضراء" in idea_name
    assert "entities" in interp._ideas[idea_name]


def test_reaction_system():
    """Test reaction system (cascading events)"""
    code = """
كيان_معرفي طالب:
{
    حالة: "مبتدئ"
    معرفة: 0.3
}

حدث_معرفي دراسة:
{
    مشاركون: {
        "طالب": {"دور": "فاعل", "درجة": 1.0}
    },
    قوة: 0.8,
    تحويل: {
        "طالب.معرفة": 0.7
    },
    ردود_فعل: [
        {"حدث": "تخرج", "احتمال": 1.0}
    ]
}

حدث_معرفي تخرج:
{
    مشاركون: {
        "طالب": {"دور": "فاعل", "درجة": 1.0}
    },
    قوة: 1.0,
    تحويل: {
        "طالب.حالة": "خريج"
    }
}

أطلق دراسة
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()

    interp = TraditionalInterpreter()
    interp.interpret(ast)

    # Check that both events were triggered
    assert interp._cognitive_entities["طالب"]["معرفة"] == 0.7
    assert interp._cognitive_entities["طالب"]["حالة"] == "خريج"


def test_concurrent_events():
    """Test concurrent events"""
    code = """
كيان_معرفي شخص:
{
    طاقة: 100
    سعادة: 50
}

حدث_معرفي عمل:
{
    مشاركون: {
        "شخص": {"دور": "فاعل", "درجة": 1.0}
    },
    قوة: 0.8,
    تحويل: {
        "شخص.طاقة": 60
    }
}

حدث_معرفي لعب:
{
    مشاركون: {
        "شخص": {"دور": "فاعل", "درجة": 1.0}
    },
    قوة: 0.6,
    تحويل: {
        "شخص.سعادة": 80
    }
}

concurrent يوم_عادي:
{
    events: [
        ("عمل", 0.8),
        ("لعب", 0.6)
    ]
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()

    interp = TraditionalInterpreter()
    interp.interpret(ast)

    # Check that both events affected the entity
    assert interp._cognitive_entities["شخص"]["طاقة"] == 60
    assert interp._cognitive_entities["شخص"]["سعادة"] == 80


def test_linguistic_pattern():
    """Test linguistic pattern definition"""
    code = """
pattern فعل_ونتيجة:
{
    structure: ["فاعل", "فعل", "مفعول"],
    express: "قام {فاعل} بـ {فعل} {مفعول}"
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()

    interp = TraditionalInterpreter()
    interp.interpret(ast)

    # Check pattern was stored
    assert "فعل_ونتيجة" in interp._linguistic_patterns
    assert "structure" in interp._linguistic_patterns["فعل_ونتيجة"]

