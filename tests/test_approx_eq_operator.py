"""
Tests for ~= (approximate equality) operator
اختبارات لعامل ~= (المساواة التقريبية)
"""

import pytest
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
from bayan.bayan.hybrid_interpreter import HybridInterpreter


def run_code(code):
    """Helper to run Bayan code and return interpreter"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    
    interpreter = HybridInterpreter()
    interpreter.interpret(ast)
    return interpreter


def test_approx_eq_numbers():
    """Test ~= with numbers"""
    code = """
hybrid {
    approx_eps = 0.01
    x = 1.0001
    y = 1.0002
    result = x ~= y
    print(result)
}
"""
    interp = run_code(code)
    # Should be True because difference is < 0.01
    assert interp.traditional.global_env.get('result') == True


def test_approx_eq_numbers_false():
    """Test ~= with numbers that are not approximately equal"""
    code = """
hybrid {
    approx_eps = 0.001
    x = 1.0
    y = 1.1
    result = x ~= y
    print(result)
}
"""
    interp = run_code(code)
    # Should be False because difference is > 0.001
    assert interp.traditional.global_env.get('result') == False


def test_approx_eq_unicode():
    """Test ~= with Unicode symbol ≈"""
    code = """
hybrid {
    approx_eps = 0.1
    a = 5.05
    b = 5.08
    result = a ≈ b
    print(result)
}
"""
    interp = run_code(code)
    # Should be True because difference is < 0.1
    assert interp.traditional.global_env.get('result') == True


def test_approx_eq_strings():
    """Test ~= with strings (exact equality fallback)"""
    code = """
hybrid {
    s1 = "hello"
    s2 = "hello"
    s3 = "world"
    r1 = s1 ~= s2
    r2 = s1 ~= s3
    print(r1)
    print(r2)
}
"""
    interp = run_code(code)
    # Strings should use exact equality
    assert interp.traditional.global_env.get('r1') == True
    assert interp.traditional.global_env.get('r2') == False


def test_approx_eq_in_condition():
    """Test ~= in if condition"""
    code = """
hybrid {
    approx_eps = 0.01
    x = 3.14159
    y = 3.14160

    if x ~= y:
    {
        result = "approximately equal"
    }
    else:
    {
        result = "not equal"
    }
    print(result)
}
"""
    interp = run_code(code)
    assert interp.traditional.global_env.get('result') == "approximately equal"


def test_approx_eq_default_epsilon():
    """Test ~= with default epsilon"""
    code = """
hybrid {
    # Default approx_eps is 0.01
    x = 1.005
    y = 1.006
    result = x ~= y
    print(result)
}
"""
    interp = run_code(code)
    # Should be True with default epsilon
    assert interp.traditional.global_env.get('result') == True


def test_approx_eq_arabic_context():
    """Test ~= in Arabic context"""
    code = """
hybrid {
    approx_eps = 0.1
    قيمة1 = 10.05
    قيمة2 = 10.08
    نتيجة = قيمة1 ~= قيمة2
    print(نتيجة)
}
"""
    interp = run_code(code)
    assert interp.traditional.global_env.get('نتيجة') == True

