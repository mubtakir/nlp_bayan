"""
Tests for Categorical distribution
اختبارات لتوزيع Categorical
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


def test_categorical_basic():
    """Test basic Categorical distribution"""
    code = """
hybrid {
    seed(42)
    x ~ Categorical({"A": 0.0, "B": 1.0, "C": 0.0})
    print(x)
}
"""
    interp = run_code(code)
    # With weight 1.0 for "B", should always return "B"
    assert interp.traditional.global_env.get('x') == "B"


def test_categorical_arabic():
    """Test Categorical with Arabic values"""
    code = """
hybrid {
    seed(123)
    فعل ~ Categorical({"انطلق": 0.5, "سار": 0.3, "ذهب": 0.2})
    print(فعل)
}
"""
    interp = run_code(code)
    # Should return one of the three values
    result = interp.traditional.global_env.get('فعل')
    assert result in ["انطلق", "سار", "ذهب"]


def test_categorical_lowercase():
    """Test categorical (lowercase) distribution"""
    code = """
hybrid {
    seed(7)
    y ~ categorical({"red": 0.4, "green": 0.4, "blue": 0.2})
    print(y)
}
"""
    interp = run_code(code)
    # Should return one of the three colors
    result = interp.traditional.global_env.get('y')
    assert result in ["red", "green", "blue"]


def test_categorical_reproducible():
    """Test Categorical reproducibility with same seed"""
    code = """
hybrid {
    seed(999)
    x1 ~ Categorical({"A": 0.3, "B": 0.5, "C": 0.2})
    seed(999)
    x2 ~ Categorical({"A": 0.3, "B": 0.5, "C": 0.2})
    print(x1)
    print(x2)
}
"""
    interp = run_code(code)
    x1 = interp.traditional.global_env.get('x1')
    x2 = interp.traditional.global_env.get('x2')
    # Same seed should give same result
    assert x1 == x2


def test_categorical_uniform_fallback():
    """Test Categorical with zero/negative weights falls back to uniform"""
    code = """
hybrid {
    seed(555)
    x ~ Categorical({"A": 0.0, "B": 0.0, "C": 0.0})
    print(x)
}
"""
    interp = run_code(code)
    # Should still return one of the values (uniform fallback)
    result = interp.traditional.global_env.get('x')
    assert result in ["A", "B", "C"]


def test_categorical_with_numbers():
    """Test Categorical with numeric values"""
    code = """
hybrid {
    seed(111)
    n ~ Categorical({1: 0.5, 2: 0.3, 3: 0.2})
    print(n)
}
"""
    interp = run_code(code)
    # Should return one of the numbers
    result = interp.traditional.global_env.get('n')
    assert result in [1, 2, 3]

