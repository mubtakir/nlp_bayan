"""
Tests for Pipeline and Composition Operators
اختبارات لعوامل الأنابيب والتركيب
"""

from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
from bayan.bayan.hybrid_interpreter import HybridInterpreter


def test_pipeline_basic():
    """Test basic pipeline operator"""
    code = """
def double(x):
{
    return x * 2
}

result = 5 |> double
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    assert interp.traditional.global_env.get('result') == 10


def test_pipeline_chain():
    """Test chained pipeline operations"""
    code = """
def double(x):
{
    return x * 2
}

def increment(x):
{
    return x + 1
}

result = 5 |> double |> increment
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    # 5 |> double = 10, 10 |> increment = 11
    assert interp.traditional.global_env.get('result') == 11


def test_pipeline_with_builtin():
    """Test pipeline with built-in functions"""
    code = """
result = [1, 2, 3, 4, 5] |> len
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    assert interp.traditional.global_env.get('result') == 5


def test_composition_basic():
    """Test basic function composition"""
    code = """
def double(x):
{
    return x * 2
}

def increment(x):
{
    return x + 1
}

composed = double >> increment
result = composed(5)
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    # double(5) = 10, increment(10) = 11
    assert interp.traditional.global_env.get('result') == 11


def test_composition_chain():
    """Test chained function composition"""
    code = """
def double(x):
{
    return x * 2
}

def increment(x):
{
    return x + 1
}

def square(x):
{
    return x * x
}

composed = double >> increment >> square
result = composed(3)
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    # double(3) = 6, increment(6) = 7, square(7) = 49
    assert interp.traditional.global_env.get('result') == 49


def test_pipeline_and_composition_combined():
    """Test combining pipeline and composition"""
    code = """
def double(x):
{
    return x * 2
}

def increment(x):
{
    return x + 1
}

composed = double >> increment
result = 5 |> composed
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    # composed(5) = increment(double(5)) = increment(10) = 11
    assert interp.traditional.global_env.get('result') == 11


def test_pipeline_with_list_operations():
    """Test pipeline with list operations"""
    code = """
def sum_list(lst):
{
    total = 0
    for item in lst:
    {
        total = total + item
    }
    return total
}

result = [1, 2, 3, 4, 5] |> sum_list
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert interp.traditional.global_env.get('result') == 15


def test_pipeline_with_string():
    """Test pipeline with string operations"""
    code = """
def add_exclamation(s):
{
    return s + "!"
}

result = "Hello" |> add_exclamation
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert interp.traditional.global_env.get('result') == "Hello!"


def test_composition_with_multiple_params():
    """Test composition with functions that take single parameter"""
    code = """
def add_ten(x):
{
    return x + 10
}

def multiply_by_three(x):
{
    return x * 3
}

composed = add_ten >> multiply_by_three
result = composed(5)
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    # add_ten(5) = 15, multiply_by_three(15) = 45
    assert interp.traditional.global_env.get('result') == 45


def test_pipeline_complex_expression():
    """Test pipeline with complex expressions"""
    code = """
def double(x):
{
    return x * 2
}

x = 3
y = 7
result = (x + y) |> double
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    # (3 + 7) |> double = 10 |> double = 20
    assert interp.traditional.global_env.get('result') == 20


def test_pipeline_with_method_call():
    """Test pipeline with method-like operations"""
    code = """
def get_length(s):
{
    return len(s)
}

result = "Hello World" |> get_length
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert interp.traditional.global_env.get('result') == 11


def test_composition_reusable():
    """Test that composed functions are reusable"""
    code = """
def double(x):
{
    return x * 2
}

def increment(x):
{
    return x + 1
}

composed = double >> increment
result1 = composed(5)
result2 = composed(10)
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert interp.traditional.global_env.get('result1') == 11
    assert interp.traditional.global_env.get('result2') == 21


