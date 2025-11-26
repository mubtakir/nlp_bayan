"""
Tests for constraint and validation features in Bayan
"""

import pytest
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
from bayan.bayan.hybrid_interpreter import HybridInterpreter
from bayan.bayan.ast_nodes import ContractError
from bayan.bayan.traditional_interpreter import BayanRuntimeError


def test_where_clause_success():
    """Test where clause that succeeds"""
    code = """
x = 10
y = x * 2 where x > 0
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)
    
    assert interp.traditional.global_env.get('y') == 20


def test_where_clause_failure():
    """Test where clause that fails"""
    code = """
x = -5
y = x * 2 where x > 0
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()

    with pytest.raises((ValueError, BayanRuntimeError)):
        interp.interpret(ast)


def test_where_clause_arabic():
    """Test where clause with Arabic keyword"""
    code = """
س = 15
ص = س + 5 حيث س > 10
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)
    
    assert interp.traditional.global_env.get('ص') == 20


def test_requires_clause_success():
    """Test requires clause that succeeds"""
    code = """
def divide(a, b):
    requires b != 0
    {
        return a / b
    }

result = divide(10, 2)
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)
    
    assert interp.traditional.global_env.get('result') == 5.0


def test_requires_clause_failure():
    """Test requires clause that fails"""
    code = """
def divide(a, b):
    requires b != 0
    {
        return a / b
    }

result = divide(10, 0)
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()

    with pytest.raises((ContractError, BayanRuntimeError)):
        interp.interpret(ast)


def test_requires_clause_arabic():
    """Test requires clause with Arabic keyword"""
    code = """
def قسمة(أ, ب):
    يتطلب ب != 0
    {
        return أ / ب
    }

نتيجة = قسمة(20, 4)
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)
    
    assert interp.traditional.global_env.get('نتيجة') == 5.0


def test_ensures_clause_success():
    """Test ensures clause that succeeds"""
    code = """
def sqrt_approx(x):
    requires x >= 0
    ensures result >= 0
    {
        return pow(x, 0.5)
    }

result = sqrt_approx(16)
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)

    assert interp.traditional.global_env.get('result') == 4.0


def test_ensures_clause_failure():
    """Test ensures clause that fails"""
    code = """
def bad_func(x):
    requires x > 0
    ensures result > 100
    {
        return x + 1
    }

result = bad_func(5)
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()

    with pytest.raises((ContractError, BayanRuntimeError)):
        interp.interpret(ast)


def test_invariant_for_loop_success():
    """Test invariant in for loop that succeeds"""
    code = """
total = 0
for i in (range(5))
    invariant total >= 0
{
        total = total + i
    }
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)

    assert interp.traditional.global_env.get('total') == 10


def test_invariant_for_loop_failure():
    """Test invariant in for loop that fails"""
    code = """
total = 0
for i in (range(5))
    invariant total < 5
{
        total = total + i
    }
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()

    with pytest.raises((ContractError, BayanRuntimeError)):
        interp.interpret(ast)


def test_invariant_while_loop_success():
    """Test invariant in while loop that succeeds"""
    code = """
counter = 0
while (counter < 5)
    invariant counter >= 0
{
        counter = counter + 1
    }
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)

    assert interp.traditional.global_env.get('counter') == 5


def test_invariant_arabic():
    """Test invariant with Arabic keyword"""
    code = """
مجموع = 0
for عدد in (range(3))
    ثابت مجموع >= 0
{
        مجموع = مجموع + عدد
    }
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)

    assert interp.traditional.global_env.get('مجموع') == 3


def test_combined_contracts():
    """Test function with both requires and ensures"""
    code = """
def safe_divide(a, b):
    requires b != 0
    requires a >= 0
    ensures result >= 0
    {
        return a / b
    }

result = safe_divide(10, 2)
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)

    assert interp.traditional.global_env.get('result') == 5.0

