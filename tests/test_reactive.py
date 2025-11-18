"""
Tests for Reactive Programming features
اختبارات لميزات البرمجة التفاعلية
"""

import pytest
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
from bayan.bayan.hybrid_interpreter import HybridInterpreter


def test_reactive_declaration_english():
    """Test reactive variable declaration in English"""
    code = """
reactive x = 10
x = 20
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    assert interp.traditional.global_env.get('x') == 20
    assert 'x' in interp.traditional._reactive_vars


def test_reactive_declaration_arabic():
    """Test reactive variable declaration in Arabic"""
    code = """
تفاعلي س = 5
س = 15
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    assert interp.traditional.global_env.get('س') == 15
    assert 'س' in interp.traditional._reactive_vars


def test_watch_block_english():
    """Test watch block in English"""
    code = """
reactive x = 10
result = 0
watch x:
{
    result = x * 2
}
x = 20
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    # result should be updated when x changes
    assert interp.traditional.global_env.get('result') == 40


def test_watch_block_arabic():
    """Test watch block in Arabic"""
    code = """
تفاعلي س = 5
نتيجة = 0
راقب س:
{
    نتيجة = س + 10
}
س = 15
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    assert interp.traditional.global_env.get('نتيجة') == 25


def test_watch_multiple_variables():
    """Test watching multiple variables"""
    code = """
reactive x = 10
reactive y = 20
result = 0
watch x, y:
{
    result = x + y
}
x = 30
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    assert interp.traditional.global_env.get('result') == 50


def test_computed_property_english():
    """Test computed property in English"""
    code = """
reactive x = 10
reactive y = 20
computed sum = x + y
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    assert interp.traditional.global_env.get('sum') == 30


def test_computed_property_arabic():
    """Test computed property in Arabic"""
    code = """
تفاعلي س = 5
تفاعلي ص = 15
محسوب مجموع = س + ص
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    assert interp.traditional.global_env.get('مجموع') == 20


def test_computed_property_auto_update():
    """Test that computed property auto-updates when dependencies change"""
    code = """
reactive x = 10
reactive y = 20
computed sum = x + y
x = 30
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    
    # sum should auto-update to 30 + 20 = 50
    assert interp.traditional.global_env.get('sum') == 50


def test_computed_property_multiple_updates():
    """Test computed property with multiple dependency updates"""
    code = """
reactive x = 10
reactive y = 20
computed sum = x + y
x = 30
y = 40
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    # sum should auto-update to 30 + 40 = 70
    assert interp.traditional.global_env.get('sum') == 70


def test_combined_watch_and_computed():
    """Test combining watch blocks and computed properties"""
    code = """
reactive x = 10
reactive y = 20
computed sum = x + y
log = []
watch sum:
{
    log = log + [sum]
}
x = 30
y = 40
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    # log should contain updates: [50, 70]
    log = interp.traditional.global_env.get('log')
    assert 50 in log
    assert 70 in log


def test_reactive_with_complex_expression():
    """Test reactive with complex expressions"""
    code = """
reactive x = 5
reactive y = 10
computed result = (x * 2) + (y / 2)
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    # result = (5 * 2) + (10 / 2) = 10 + 5 = 15
    assert interp.traditional.global_env.get('result') == 15.0


def test_non_reactive_variable_no_trigger():
    """Test that non-reactive variables don't trigger watchers"""
    code = """
x = 10
result = 0
watch x:
{
    result = x * 2
}
x = 20
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    # result should still be 0 because x is not reactive
    assert interp.traditional.global_env.get('result') == 0


def test_reactive_in_function():
    """Test reactive variables updated outside functions"""
    code = """
reactive counter = 0
log = []

watch counter:
{
    log = log + [counter]
}

counter = 1
counter = 2
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)

    # counter should be 2
    assert interp.traditional.global_env.get('counter') == 2
    # log should contain [1, 2]
    log = interp.traditional.global_env.get('log')
    assert 1 in log
    assert 2 in log

