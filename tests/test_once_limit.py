"""
Tests for once and limit statements
اختبارات لبنى once و limit
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


def test_once_goal_basic():
    """Test once with a single logical goal"""
    code = """
hybrid {
    parent("أحمد", "محمد").
    parent("أحمد", "علي").
    parent("أحمد", "فاطمة").
    
    once parent("أحمد", ?X).
}
"""
    interp = run_code(code)
    # once should return only one solution
    # We can't directly test the return value here, but we can verify no errors


def test_once_goal_arabic():
    """Test once with Arabic keyword مرة"""
    code = """
hybrid {
    color("red").
    color("blue").
    color("green").
    
    مرة color(?C).
}
"""
    interp = run_code(code)
    # Should execute without errors


def test_limit_goal_basic():
    """Test limit N goal."""
    code = """
hybrid {
    number(1).
    number(2).
    number(3).
    number(4).
    number(5).
    
    limit 3 number(?N).
}
"""
    interp = run_code(code)
    # Should execute without errors


def test_limit_goal_arabic():
    """Test limit with Arabic keyword حد"""
    code = """
hybrid {
    fruit("تفاح").
    fruit("موز").
    fruit("برتقال").
    fruit("عنب").
    
    حد 2 fruit(?F).
}
"""
    interp = run_code(code)
    # Should execute without errors


def test_once_statement_block():
    """Test once { block } - simplified version without query"""
    code = """
hybrid {
    parent("أحمد", "محمد").
    parent("أحمد", "علي").
}

x = 0
once {
    x = x + 1
}
print(x)
"""
    interp = run_code(code)
    # Should execute without errors
    assert interp.traditional.global_env.get('x') == 1


def test_limit_statement_block():
    """Test limit N { block } - simplified version without query"""
    code = """
hybrid {
    number(1).
    number(2).
    number(3).
}

x = 0
limit 2 {
    x = x + 1
}
print(x)
"""
    interp = run_code(code)
    # Should execute without errors
    assert interp.traditional.global_env.get('x') == 1


def test_once_with_collect():
    """Test once combined with collect"""
    code = """
hybrid {
    parent("أحمد", "محمد").
    parent("أحمد", "علي").
    parent("أحمد", "فاطمة").
}

x = collect ?X from parent("أحمد", ?X) limit 1
print(len(x))
"""
    interp = run_code(code)
    # Should have collected only 1 solution
    assert interp.traditional.global_env.get('x') is not None
    assert len(interp.traditional.global_env['x']) == 1


def test_limit_with_collect():
    """Test limit combined with collect"""
    code = """
hybrid {
    number(1).
    number(2).
    number(3).
    number(4).
    number(5).
}

nums = collect ?N from number(?N) limit 3
print(len(nums))
"""
    interp = run_code(code)
    # Should have collected only 3 solutions
    assert interp.traditional.global_env.get('nums') is not None
    assert len(interp.traditional.global_env['nums']) == 3

