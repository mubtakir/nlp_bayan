"""
Tests for Semantic Programming & Knowledge Management features
اختبارات لميزات البرمجة المعانية وإدارة المعرفة
"""

import pytest
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
from bayan.bayan.hybrid_interpreter import HybridInterpreter


def test_semantic_meaning_english():
    """Test semantic meaning with English keywords"""
    code = """
meaning محمد:
{
    is: "طالب",
    studies: "الرياضيات",
    age: 20
}

meaning الرياضيات:
{
    is: "علم",
    part_of: "العلوم",
    difficulty: 0.7
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    assert "محمد" in interp.traditional._semantic_meanings
    assert interp.traditional._semantic_meanings["محمد"]["is"] == "طالب"
    assert interp.traditional._semantic_meanings["محمد"]["studies"] == "الرياضيات"
    assert interp.traditional._semantic_meanings["الرياضيات"]["is"] == "علم"


def test_semantic_query():
    """Test semantic query"""
    code = """
معنى محمد:
{
    هو: "طالب",
    يدرس: "الرياضيات"
}

معنى فاطمة:
{
    هو: "طالبة",
    يدرس: "الفيزياء"
}

معنى علي:
{
    هو: "طالب",
    يدرس: "الرياضيات"
}

result1 = من_يدرس("الرياضيات")
result2 = ما_هو("محمد")
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    # من_يدرس should return list of students studying math
    result1 = interp.traditional.global_env["result1"]
    assert isinstance(result1, list)
    assert "محمد" in result1
    assert "علي" in result1
    
    # ما_هو should return what محمد is
    result2 = interp.traditional.global_env["result2"]
    assert result2 == "طالب"


def test_knowledge_info():
    """Test knowledge information with context"""
    code = """
information "الأرض كروية":
{
    "content": {"shape": "sphere"},
    "context": {
        "time": "2024",
        "place": "Earth",
        "source": "Science",
        "certainty": 1.0
    }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert "الأرض كروية" in interp.traditional._knowledge_info
    info = interp.traditional._knowledge_info["الأرض كروية"]
    assert info["context"]["certainty"] == 1.0
    assert info["context"]["source"] == "Science"


def test_inference_rule():
    """Test inference rule"""
    code = """
inference_rule "إذا كان طالب يدرس الرياضيات فهو ذكي":
{
    "if": ["يدرس", "الرياضيات"],
    "then": {"ذكي": 1}
}

infer_from: "محمد يدرس الرياضيات"
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)

    assert "إذا كان طالب يدرس الرياضيات فهو ذكي" in interp.traditional._inference_rules


def test_contradiction():
    """Test contradiction detection"""
    code = """
معلومة "الأرض مسطحة":
{
    "محتوى": {"شكل": "مسطح"},
    "سياق": {
        "يقين": 0.1
    }
}

معلومة "الأرض كروية":
{
    "محتوى": {"شكل": "كروي"},
    "سياق": {
        "يقين": 1.0
    }
}

تناقض بين: ["الأرض مسطحة", "الأرض كروية"]
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)

    # Should detect contradiction
    # The contradiction statement returns the list of contradictions
    # We can check if any contradictions were detected
    assert "الأرض مسطحة" in interp.traditional._knowledge_info
    assert "الأرض كروية" in interp.traditional._knowledge_info


def test_evolving_knowledge():
    """Test evolving knowledge"""
    code = """
knowledge "سعر البيتكوين":
{
    current_value: 50000,
    history: [30000, 40000, 45000],
    future_prediction: {"next_month": 55000}
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert "سعر البيتكوين" in interp.traditional._evolving_knowledge
    knowledge = interp.traditional._evolving_knowledge["سعر البيتكوين"]
    assert knowledge["current_value"] == 50000
    assert len(knowledge["history"]) == 3


def test_ontology():
    """Test ontology definition"""
    code = """
ontology "الكائنات الحية":
{
    root: "كائن حي",
    taxonomy: {
        "حيوان": {
            "ثدييات": ["إنسان", "قط", "كلب"],
            "طيور": ["عصفور", "نسر"]
        },
        "نبات": {
            "أشجار": ["نخلة", "زيتون"],
            "أزهار": ["وردة", "ياسمين"]
        }
    }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert "الكائنات الحية" in interp.traditional._ontologies
    ontology = interp.traditional._ontologies["الكائنات الحية"]
    assert ontology["root"] == "كائن حي"
    assert "حيوان" in ontology["taxonomy"]


def test_semantic_similarity():
    """Test semantic similarity calculation"""
    code = """
concept "قط":
{
    type: "حيوان",
    legs: 4,
    sound: "مواء"
}

concept "كلب":
{
    type: "حيوان",
    legs: 4,
    sound: "نباح"
}

concept "عصفور":
{
    type: "حيوان",
    legs: 2,
    sound: "تغريد"
}

sim1 = تشابه("قط", "كلب")
sim2 = تشابه("قط", "عصفور")
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    sim1 = interp.traditional.global_env["sim1"]
    sim2 = interp.traditional.global_env["sim2"]

    # قط and كلب should be more similar than قط and عصفور
    assert sim1 > sim2
    assert 0 <= sim1 <= 1
    assert 0 <= sim2 <= 1


def test_narrative():
    """Test narrative definition"""
    code = """
narrative "رحلة البطل":
{
    characters: {
        "البطل": {"role": "protagonist"},
        "الشرير": {"role": "antagonist"}
    },
    events: [
        "البداية",
        "المغامرة",
        "الصراع",
        "النصر"
    ],
    structure: "رحلة_البطل_الكلاسيكية"
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert "رحلة البطل" in interp.traditional._narratives
    narrative = interp.traditional._narratives["رحلة البطل"]
    assert "البطل" in narrative["characters"]
    assert len(narrative["events"]) == 4


def test_current_context():
    """Test current context"""
    code = """
current_context:
{
    time: "ليل",
    place: "منزل",
    mood: "متعب"
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert "context" in interp.traditional.global_env
    context = interp.traditional.global_env["context"]
    assert context["time"] == "ليل"
    assert context["place"] == "منزل"


