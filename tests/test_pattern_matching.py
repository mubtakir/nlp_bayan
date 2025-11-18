"""
Tests for Pattern Matching features
اختبارات لميزات مطابقة الأنماط
"""

import pytest
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
from bayan.bayan.hybrid_interpreter import HybridInterpreter
from bayan.bayan.traditional_interpreter import BayanRuntimeError


def test_match_literal_english():
    """Test match with literal patterns in English"""
    code = """
x = 2
result = ""
match x:
{
    case 1: { result = "one" }
    case 2: { result = "two" }
    case 3: { result = "three" }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert interp.traditional.global_env.get('result') == "two"


def test_match_literal_arabic():
    """Test match with literal patterns in Arabic"""
    code = """
س = 1
نتيجة = ""
طابق س:
{
    حالة 1: { نتيجة = "واحد" }
    حالة 2: { نتيجة = "اثنان" }
    حالة 3: { نتيجة = "ثلاثة" }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert interp.traditional.global_env.get('نتيجة') == "واحد"


def test_match_with_default():
    """Test match with default case"""
    code = """
x = 99
result = ""
match x:
{
    case 1: { result = "one" }
    case 2: { result = "two" }
    default: { result = "other" }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    assert interp.traditional.global_env.get('result') == "other"


def test_match_list_destructuring():
    """Test match with list destructuring"""
    code = """
point = [10, 20]
result = 0
match point:
{
    case [x, y]: { result = x + y }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    assert interp.traditional.global_env.get('result') == 30
    assert interp.traditional.global_env.get('x') == 10
    assert interp.traditional.global_env.get('y') == 20


def test_match_dict_destructuring():
    """Test match with dict destructuring"""
    code = """
person = {"name": "Ali", "age": 25}
result = ""
match person:
{
    case {"name": n, "age": a}: { result = n }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    assert interp.traditional.global_env.get('result') == "Ali"
    assert interp.traditional.global_env.get('n') == "Ali"
    assert interp.traditional.global_env.get('a') == 25


def test_match_with_guard():
    """Test match with guard (when clause)"""
    code = """
x = 15
result = ""
match x:
{
    case n when n < 10: { result = "small" }
    case n when n >= 10: { result = "large" }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    assert interp.traditional.global_env.get('result') == "large"


def test_match_with_guard_arabic():
    """Test match with guard in Arabic"""
    code = """
س = 5
نتيجة = ""
طابق س:
{
    حالة ع عندما ع < 10: { نتيجة = "صغير" }
    حالة ع عندما ع >= 10: { نتيجة = "كبير" }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    assert interp.traditional.global_env.get('نتيجة') == "صغير"


def test_match_complex_pattern():
    """Test match with complex nested patterns"""
    code = """
data = {"type": "point", "coords": [5, 10]}
result = 0
match data:
{
    case {"type": t, "coords": [x, y]}: { result = x + y }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert interp.traditional.global_env.get('result') == 15
    assert interp.traditional.global_env.get('t') == "point"
    assert interp.traditional.global_env.get('x') == 5
    assert interp.traditional.global_env.get('y') == 10


def test_match_multiple_cases_with_guards():
    """Test match with multiple cases and guards"""
    code = """
def classify(n):
{
    result = ""
    match n:
    {
        case x when x < 0: { result = "negative" }
        case x when x == 0: { result = "zero" }
        case x when x > 0 and x < 10: { result = "small positive" }
        case x when x >= 10: { result = "large positive" }
    }
    return result
}

r1 = classify(-5)
r2 = classify(0)
r3 = classify(5)
r4 = classify(15)
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert interp.traditional.global_env.get('r1') == "negative"
    assert interp.traditional.global_env.get('r2') == "zero"
    assert interp.traditional.global_env.get('r3') == "small positive"
    assert interp.traditional.global_env.get('r4') == "large positive"


def test_match_no_match_error():
    """Test that match raises error when no case matches"""
    code = """
x = 99
match x:
{
    case 1: { result = "one" }
    case 2: { result = "two" }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()

    with pytest.raises(BayanRuntimeError, match="No matching case"):
        interp.interpret(ast)


def test_match_list_length_mismatch():
    """Test that list pattern fails when length doesn't match"""
    code = """
point = [10, 20, 30]
result = 0
match point:
{
    case [x, y]: { result = x + y }
    default: { result = -1 }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert interp.traditional.global_env.get('result') == -1


def test_match_dict_missing_key():
    """Test that dict pattern fails when key is missing"""
    code = """
person = {"name": "Ali"}
result = ""
match person:
{
    case {"name": n, "age": a}: { result = "has age" }
    default: { result = "no age" }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert interp.traditional.global_env.get('result') == "no age"


def test_match_variable_pattern():
    """Test match with variable pattern (always matches)"""
    code = """
x = 42
result = 0
match x:
{
    case n: { result = n * 2 }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert interp.traditional.global_env.get('result') == 84
    assert interp.traditional.global_env.get('n') == 42


def test_match_string_patterns():
    """Test match with string patterns"""
    code = """
command = "start"
result = ""
match command:
{
    case "start": { result = "starting" }
    case "stop": { result = "stopping" }
    case "pause": { result = "pausing" }
    default: { result = "unknown" }
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    assert interp.traditional.global_env.get('result') == "starting"

