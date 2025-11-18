"""
Tests for Existential Model (النموذج الوجودي)
"""

from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
from bayan.bayan.hybrid_interpreter import HybridInterpreter


def test_domain_definition():
    """Test domain definition"""
    code = """
مجال "الكيمياء":
{
    "كائن_أساسي": "عنصر",
    "بيئة": "محلول",
    "معانٍ_أساسية": ["تفاعل", "ذوبان"],
    "علاقات": ["يتفاعل_مع", "يذوب_في"],
    "خصائص": ["عدد_ذري", "كتلة_ذرية"]
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    
    result = interp.interpret(ast)
    
    # Check that domain was stored
    assert "الكيمياء" in interp.traditional._domains
    domain = interp.traditional._domains["الكيمياء"]
    assert domain["كائن_أساسي"] == "عنصر"
    assert domain["بيئة"] == "محلول"
    assert "تفاعل" in domain["معانٍ_أساسية"]


def test_generic_environment():
    """Test generic environment definition"""
    code = """
بيئة "محلول_حمضي" في_مجال "الكيمياء":
{
    "أبعاد": {
        "مكاني": ["سطح", "قاع", "وسط"],
        "زماني": ["قبل_التفاعل", "أثناء_التفاعل", "بعد_التفاعل"],
        "مجالي": ["تركيز", "حرارة", "ضغط"]
    },
    "خصائص": {"pH": 3, "حرارة": 25},
    "قوانين": ["قانون_الكتلة", "قانون_الطاقة"]
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    
    result = interp.interpret(ast)
    
    # Check that environment was stored
    assert "محلول_حمضي" in interp.traditional._environments
    env = interp.traditional._environments["محلول_حمضي"]
    assert env["_domain"] == "الكيمياء"
    assert env["خصائص"]["pH"] == 3
    assert "سطح" in env["أبعاد"]["مكاني"]


def test_existential_being():
    """Test existential being definition"""
    code = """
بيئة "محلول" في_مجال "الكيمياء":
{
    "أبعاد": {
        "مكاني": ["سطح", "قاع"],
        "زماني": ["قبل", "بعد"]
    }
}

كائن_وجودي "صوديوم" من_نوع "عنصر" في_مجال "الكيمياء":
{
    "بيئة": "محلول",
    "خصائص_ذاتية": {"عدد_ذري": 11, "رمز": "Na"},
    "معانٍ_موروثة": ["موقع_في_المحلول"],
    "معانٍ_ذاتية": ["نشاط_كيميائي"],
    "علاقات": {"يتفاعل_مع": ["كلور", "ماء"]},
    "أفعال": {"تفاعل": "ينتج_ملح"},
    "حالات": ["صلب", "منحل"]
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    
    result = interp.interpret(ast)
    
    # Check that being was stored
    assert "صوديوم" in interp.traditional._existential_beings
    being = interp.traditional._existential_beings["صوديوم"]
    assert being["_type"] == "عنصر"
    assert being["_domain"] == "الكيمياء"
    assert being["خصائص_ذاتية"]["عدد_ذري"] == 11
    assert "كلور" in being["علاقات"]["يتفاعل_مع"]


def test_domain_relation():
    """Test domain relation definition"""
    code = """
علاقة_مجالية "يتفاعل_مع" في_مجال "الكيمياء":
{
    "نوع": "ثنائية",
    "متماثلة": 0,
    "شروط": {"نشاط": "عالي"},
    "نتيجة": "مركب_جديد"
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    
    result = interp.interpret(ast)
    
    # Check that relation was stored
    assert "يتفاعل_مع" in interp.traditional._domain_relations
    relation = interp.traditional._domain_relations["يتفاعل_مع"]
    assert relation["_domain"] == "الكيمياء"
    assert relation["نوع"] == "ثنائية"
    assert relation["نتيجة"] == "مركب_جديد"


def test_domain_action():
    """Test domain action definition"""
    code = """
فعل_مجالي "تفاعل" في_مجال "الكيمياء":
{
    "فاعل": "عنصر",
    "مفعول": "عنصر",
    "شروط": {"طاقة": "كافية"},
    "نتيجة": {"مركب": "جديد", "طاقة": "محررة"}
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    
    result = interp.interpret(ast)
    
    # Check that action was stored
    assert "تفاعل" in interp.traditional._domain_actions
    action = interp.traditional._domain_actions["تفاعل"]
    assert action["_domain"] == "الكيمياء"
    assert action["فاعل"] == "عنصر"


def test_metaphorical_meaning():
    """Test metaphorical meaning definition"""
    code = """
معنى_مجازي "عدالة" في_مجال "عام":
{
    "تعريف": "كل كائن يأخذ ما يكفيه حسب طبيعته",
    "يُبنى_على": ["احتياج", "طبيعة", "توزيع"],
    "يُطبق_على": ["كل_الكائنات"],
    "شروط": {
        "لكل": "كائن",
        "يوجد": "احتياج"
    }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()

    result = interp.interpret(ast)

    # Check that metaphorical meaning was stored
    assert "عدالة" in interp.traditional._metaphorical_meanings
    meaning = interp.traditional._metaphorical_meanings["عدالة"]
    assert meaning["_domain"] == "عام"
    assert "احتياج" in meaning["يُبنى_على"]


def test_domain_law():
    """Test domain law definition"""
    code = """
قانون_مجالي "قانون_الكتلة" في_مجال "الكيمياء":
{
    "صيغة": "كتلة_المتفاعلات = كتلة_النواتج",
    "ينطبق_على": ["كل_التفاعلات"],
    "استثناءات": []
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()

    result = interp.interpret(ast)

    # Check that law was stored
    assert "قانون_الكتلة" in interp.traditional._domain_laws
    law = interp.traditional._domain_laws["قانون_الكتلة"]
    assert law["_domain"] == "الكيمياء"
    assert law["صيغة"] == "كتلة_المتفاعلات = كتلة_النواتج"


def test_existential_query():
    """Test existential query"""
    code = """
كائن_وجودي "صوديوم" من_نوع "عنصر" في_مجال "الكيمياء":
{
    "بيئة": "محلول",
    "خصائص_ذاتية": {"عدد_ذري": 11},
    "علاقات": {"يتفاعل_مع": ["ماء"], "نشاط": "عالي"}
}

كائن_وجودي "كلور" من_نوع "عنصر" في_مجال "الكيمياء":
{
    "بيئة": "محلول",
    "خصائص_ذاتية": {"عدد_ذري": 17},
    "علاقات": {"يتفاعل_مع": ["ماء"], "نشاط": "عالي"}
}

كائن_وجودي "ذهب" من_نوع "عنصر" في_مجال "الكيمياء":
{
    "بيئة": "محلول",
    "خصائص_ذاتية": {"عدد_ذري": 79},
    "علاقات": {"نشاط": "منخفض"}
}

نتيجة = استعلام_وجودي:
{
    "في_مجال": "الكيمياء",
    "عن": "عنصر",
    "شروط": {"يتفاعل_مع": "ماء", "نشاط": "عالي"}
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()

    result = interp.interpret(ast)

    # Check that query returned correct results
    query_result = interp.traditional.global_env.get('نتيجة')
    assert query_result is not None
    assert isinstance(query_result, list)
    assert "صوديوم" in query_result
    assert "كلور" in query_result
    assert "ذهب" not in query_result  # Doesn't react with water


def test_existential_model_english():
    """Test existential model with English keywords"""
    code = """
domain "Electronics":
{
    "basic_entity": "transistor",
    "environment": "circuit",
    "basic_meanings": ["amplify", "switch"],
    "relations": ["connected_to", "controls"],
    "properties": ["type", "beta", "Vbe"]
}

environment "circuit" in_domain "Electronics":
{
    "dimensions": {
        "spatial": ["input", "output", "ground"],
        "temporal": ["t0", "t1", "t2"],
        "domain_specific": ["voltage", "current", "resistance"]
    },
    "properties": {"voltage_source": 5, "frequency": 1000}
}

existential_being "Q1" of_type "transistor" in_domain "Electronics":
{
    "environment": "circuit",
    "intrinsic_properties": {"type": "NPN", "beta": 100, "Vbe": 0.7},
    "inherited_meanings": ["position_in_circuit"],
    "intrinsic_meanings": ["amplification", "switching"],
    "relations": {"connected_to": ["R1", "C1"]},
    "actions": {"amplify": "increases_current"},
    "states": ["cutoff", "saturation", "active"]
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()

    result = interp.interpret(ast)

    # Check that all were stored
    assert "Electronics" in interp.traditional._domains
    assert "circuit" in interp.traditional._environments
    assert "Q1" in interp.traditional._existential_beings

    being = interp.traditional._existential_beings["Q1"]
    assert being["_type"] == "transistor"
    assert being["_domain"] == "Electronics"
    assert being["intrinsic_properties"]["beta"] == 100

