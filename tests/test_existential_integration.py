"""
Tests for Existential Model Integration with Other Features
اختبارات تكامل النموذج الوجودي مع الميزات الأخرى
"""

import pytest
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
from bayan.bayan.traditional_interpreter import TraditionalInterpreter


def test_existential_to_logical_facts():
    """Test that existential beings can be queried and used as data"""
    code = '''
مجال "test":
{
    "كائن_أساسي": "عنصر",
    "بيئة": "محلول",
    "معانٍ_أساسية": ["تفاعل"],
    "علاقات": ["يتفاعل_مع"],
    "خصائص": ["نشاط"]
}

كائن_وجودي "صوديوم" من_نوع "عنصر" في_مجال "test":
{
    "بيئة": "محلول",
    "خصائص_ذاتية": {
        "نشاط": "عالي"
    },
    "علاقات": {
        "يتفاعل_مع": ["كلور"]
    }
}

كائن_وجودي "ذهب" من_نوع "عنصر" في_مجال "test":
{
    "بيئة": "محلول",
    "خصائص_ذاتية": {
        "نشاط": "منخفض"
    },
    "علاقات": {
        "يتفاعل_مع": []
    }
}

# Query active elements
active = استعلام_وجودي:
{
    "في_مجال": "test",
    "عن": "عنصر",
    "شروط": {"نشاط": "عالي"}
}

# Query inactive elements
inactive = استعلام_وجودي:
{
    "في_مجال": "test",
    "عن": "عنصر",
    "شروط": {"نشاط": "منخفض"}
}
'''

    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interpreter = TraditionalInterpreter()
    interpreter.interpret(ast)

    # Check that queries work correctly
    active = interpreter.global_env['active']
    inactive = interpreter.global_env['inactive']

    assert len(active) == 1
    assert "صوديوم" in active

    assert len(inactive) == 1
    assert "ذهب" in inactive


def test_existential_query_with_logical_conditions():
    """Test existential queries combined with logical reasoning"""
    code = '''
مجال "test":
{
    "كائن_أساسي": "عنصر",
    "بيئة": "محلول",
    "معانٍ_أساسية": ["تفاعل"],
    "علاقات": ["يتفاعل_مع"],
    "خصائص": ["نشاط"]
}

كائن_وجودي "عنصر1" من_نوع "عنصر" في_مجال "test":
{
    "بيئة": "محلول",
    "خصائص_ذاتية": {
        "نشاط": "عالي",
        "قيمة": 10
    }
}

كائن_وجودي "عنصر2" من_نوع "عنصر" في_مجال "test":
{
    "بيئة": "محلول",
    "خصائص_ذاتية": {
        "نشاط": "منخفض",
        "قيمة": 5
    }
}

# Query with complex conditions
result = استعلام_وجودي:
{
    "في_مجال": "test",
    "عن": "عنصر",
    "شروط": {
        "و": {
            "نشاط": "عالي",
            "قيمة": {"أكبر_من": 5}
        }
    }
}
'''
    
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interpreter = TraditionalInterpreter()
    interpreter.interpret(ast)
    
    result = interpreter.global_env['result']
    assert len(result) == 1
    assert "عنصر1" in result


def test_multiple_domain_queries():
    """Test querying multiple domains"""
    code = '''
مجال "كيمياء":
{
    "كائن_أساسي": "عنصر",
    "بيئة": "محلول",
    "معانٍ_أساسية": ["تفاعل"],
    "علاقات": [],
    "خصائص": ["نشاط"]
}

مجال "فيزياء":
{
    "كائن_أساسي": "جسيم",
    "بيئة": "فضاء",
    "معانٍ_أساسية": ["حركة"],
    "علاقات": [],
    "خصائص": ["كتلة"]
}

كائن_وجودي "صوديوم" من_نوع "عنصر" في_مجال "كيمياء":
{
    "بيئة": "محلول",
    "خصائص_ذاتية": {"نشاط": "عالي"}
}

كائن_وجودي "إلكترون" من_نوع "جسيم" في_مجال "فيزياء":
{
    "بيئة": "فضاء",
    "خصائص_ذاتية": {"كتلة": 0.0005}
}

# Query chemistry domain
chem_result = استعلام_وجودي:
{
    "في_مجال": "كيمياء",
    "عن": "عنصر"
}

# Query physics domain
phys_result = استعلام_وجودي:
{
    "في_مجال": "فيزياء",
    "عن": "جسيم"
}
'''
    
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interpreter = TraditionalInterpreter()
    interpreter.interpret(ast)
    
    chem_result = interpreter.global_env['chem_result']
    phys_result = interpreter.global_env['phys_result']
    
    assert len(chem_result) == 1
    assert "صوديوم" in chem_result
    
    assert len(phys_result) == 1
    assert "إلكترون" in phys_result

