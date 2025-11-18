"""
Tests for Enhanced Existential Queries
اختبارات الاستعلامات الوجودية المحسّنة
"""

import pytest
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
from bayan.bayan.traditional_interpreter import TraditionalInterpreter


def test_complex_and_conditions():
    """Test AND conditions in queries"""
    code = '''
مجال "test":
{
    "كائن_أساسي": "شيء",
    "بيئة": "مكان",
    "معانٍ_أساسية": ["موجود"],
    "علاقات": [],
    "خصائص": ["قيمة"]
}

كائن_وجودي "شيء1" من_نوع "شيء" في_مجال "test":
{
    "بيئة": "مكان",
    "خصائص_ذاتية": {
        "قيمة": 10,
        "نوع": "أ"
    }
}

كائن_وجودي "شيء2" من_نوع "شيء" في_مجال "test":
{
    "بيئة": "مكان",
    "خصائص_ذاتية": {
        "قيمة": 20,
        "نوع": "أ"
    }
}

كائن_وجودي "شيء3" من_نوع "شيء" في_مجال "test":
{
    "بيئة": "مكان",
    "خصائص_ذاتية": {
        "قيمة": 15,
        "نوع": "ب"
    }
}

result = استعلام_وجودي:
{
    "في_مجال": "test",
    "عن": "شيء",
    "شروط": {
        "و": {
            "قيمة": {"أكبر_من": 5},
            "نوع": "أ"
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
    assert len(result) == 2
    assert "شيء1" in result
    assert "شيء2" in result


def test_complex_or_conditions():
    """Test OR conditions in queries"""
    code = '''
مجال "test":
{
    "كائن_أساسي": "شيء",
    "بيئة": "مكان",
    "معانٍ_أساسية": ["موجود"],
    "علاقات": [],
    "خصائص": ["قيمة"]
}

كائن_وجودي "شيء1" من_نوع "شيء" في_مجال "test":
{
    "بيئة": "مكان",
    "خصائص_ذاتية": {
        "قيمة": 10
    }
}

كائن_وجودي "شيء2" من_نوع "شيء" في_مجال "test":
{
    "بيئة": "مكان",
    "خصائص_ذاتية": {
        "قيمة": 100
    }
}

كائن_وجودي "شيء3" من_نوع "شيء" في_مجال "test":
{
    "بيئة": "مكان",
    "خصائص_ذاتية": {
        "قيمة": 50
    }
}

result = استعلام_وجودي:
{
    "في_مجال": "test",
    "عن": "شيء",
    "شروط": {
        "أو": {
            "قيمة": 10,
            "قيمة": 100
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
    # OR should match at least one condition
    assert len(result) >= 1


def test_comparison_operators():
    """Test comparison operators in queries"""
    code = '''
مجال "test":
{
    "كائن_أساسي": "عدد",
    "بيئة": "خط",
    "معانٍ_أساسية": ["قيمة"],
    "علاقات": [],
    "خصائص": ["قيمة"]
}

كائن_وجودي "عدد1" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 5}
}

كائن_وجودي "عدد2" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 15}
}

كائن_وجودي "عدد3" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 25}
}

result = استعلام_وجودي:
{
    "في_مجال": "test",
    "عن": "عدد",
    "شروط": {
        "قيمة": {"أكبر_من": 10}
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
    assert len(result) == 2
    assert "عدد2" in result
    assert "عدد3" in result


def test_range_conditions():
    """Test range conditions (between)"""
    code = '''
مجال "test":
{
    "كائن_أساسي": "عدد",
    "بيئة": "خط",
    "معانٍ_أساسية": ["قيمة"],
    "علاقات": [],
    "خصائص": ["قيمة"]
}

كائن_وجودي "عدد1" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 5}
}

كائن_وجودي "عدد2" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 15}
}

كائن_وجودي "عدد3" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 25}
}

result = استعلام_وجودي:
{
    "في_مجال": "test",
    "عن": "عدد",
    "شروط": {
        "قيمة": {
            "أكبر_أو_يساوي": 10,
            "أصغر_أو_يساوي": 20
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
    assert "عدد2" in result


def test_aggregation_count():
    """Test count aggregation"""
    code = '''
مجال "test":
{
    "كائن_أساسي": "شيء",
    "بيئة": "مكان",
    "معانٍ_أساسية": ["موجود"],
    "علاقات": [],
    "خصائص": []
}

كائن_وجودي "شيء1" من_نوع "شيء" في_مجال "test":
{
    "بيئة": "مكان",
    "خصائص_ذاتية": {}
}

كائن_وجودي "شيء2" من_نوع "شيء" في_مجال "test":
{
    "بيئة": "مكان",
    "خصائص_ذاتية": {}
}

كائن_وجودي "شيء3" من_نوع "شيء" في_مجال "test":
{
    "بيئة": "مكان",
    "خصائص_ذاتية": {}
}

count = استعلام_وجودي:
{
    "في_مجال": "test",
    "عن": "شيء",
    "تجميع": "عدد"
}
'''

    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interpreter = TraditionalInterpreter()
    interpreter.interpret(ast)

    count = interpreter.global_env['count']
    assert count == 3


def test_aggregation_sum():
    """Test sum aggregation"""
    code = '''
مجال "test":
{
    "كائن_أساسي": "عدد",
    "بيئة": "خط",
    "معانٍ_أساسية": ["قيمة"],
    "علاقات": [],
    "خصائص": ["قيمة"]
}

كائن_وجودي "عدد1" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 10}
}

كائن_وجودي "عدد2" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 20}
}

كائن_وجودي "عدد3" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 30}
}

total = استعلام_وجودي:
{
    "في_مجال": "test",
    "عن": "عدد",
    "تجميع": "مجموع",
    "حقل": "قيمة"
}
'''

    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interpreter = TraditionalInterpreter()
    interpreter.interpret(ast)

    total = interpreter.global_env['total']
    assert total == 60


def test_aggregation_average():
    """Test average aggregation"""
    code = '''
مجال "test":
{
    "كائن_أساسي": "عدد",
    "بيئة": "خط",
    "معانٍ_أساسية": ["قيمة"],
    "علاقات": [],
    "خصائص": ["قيمة"]
}

كائن_وجودي "عدد1" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 10}
}

كائن_وجودي "عدد2" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 20}
}

كائن_وجودي "عدد3" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 30}
}

avg = استعلام_وجودي:
{
    "في_مجال": "test",
    "عن": "عدد",
    "تجميع": "متوسط",
    "حقل": "قيمة"
}
'''

    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interpreter = TraditionalInterpreter()
    interpreter.interpret(ast)

    avg = interpreter.global_env['avg']
    assert avg == 20


def test_sorting_ascending():
    """Test sorting in ascending order"""
    code = '''
مجال "test":
{
    "كائن_أساسي": "عدد",
    "بيئة": "خط",
    "معانٍ_أساسية": ["قيمة"],
    "علاقات": [],
    "خصائص": ["قيمة"]
}

كائن_وجودي "عدد1" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 30}
}

كائن_وجودي "عدد2" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 10}
}

كائن_وجودي "عدد3" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 20}
}

sorted_result = استعلام_وجودي:
{
    "في_مجال": "test",
    "عن": "عدد",
    "ترتيب_حسب": "قيمة",
    "تصاعدي": 1
}
'''

    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interpreter = TraditionalInterpreter()
    interpreter.interpret(ast)

    sorted_result = interpreter.global_env['sorted_result']
    assert sorted_result == ["عدد2", "عدد3", "عدد1"]


def test_limit_and_offset():
    """Test limit and offset"""
    code = '''
مجال "test":
{
    "كائن_أساسي": "عدد",
    "بيئة": "خط",
    "معانٍ_أساسية": ["قيمة"],
    "علاقات": [],
    "خصائص": ["قيمة"]
}

كائن_وجودي "عدد1" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 10}
}

كائن_وجودي "عدد2" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 20}
}

كائن_وجودي "عدد3" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 30}
}

كائن_وجودي "عدد4" من_نوع "عدد" في_مجال "test":
{
    "بيئة": "خط",
    "خصائص_ذاتية": {"قيمة": 40}
}

limited = استعلام_وجودي:
{
    "في_مجال": "test",
    "عن": "عدد",
    "ترتيب_حسب": "قيمة",
    "إزاحة": 1,
    "حد": 2
}
'''

    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interpreter = TraditionalInterpreter()
    interpreter.interpret(ast)

    limited = interpreter.global_env['limited']
    assert len(limited) == 2
    assert "عدد2" in limited
    assert "عدد3" in limited


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

