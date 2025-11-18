"""
Tests for Temporal Constructs in Bayan Language
اختبارات للصيغ الزمنية في لغة البيان
"""

import pytest
import time
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
from bayan.bayan.hybrid_interpreter import HybridInterpreter


def test_temporal_block_english():
    """Test temporal block with English keywords"""
    code = """
temporal {
    first: x = 1,
    then: y = x + 1,
    lastly: z = y + 1
}
print(z)
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)

    # Check that z = 3
    assert interp.traditional.global_env.get('z') == 3


def test_temporal_block_arabic():
    """Test temporal block with Arabic keywords"""
    code = """
زمنيا {
    أولا: س = 10,
    ثم: ص = س * 2,
    أخيرا: ع = ص + 5
}
print(ع)
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)

    # Check that ع = 25
    assert interp.traditional.global_env.get('ع') == 25


def test_delay_statement_english():
    """Test delay statement with English keywords"""
    code = """
start = time.time()
delay 0.1 seconds
end = time.time()
elapsed = end - start
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()

    # Add time module to environment
    import time as time_module
    interp.traditional.global_env['time'] = time_module

    result = interp.interpret(ast)

    # Check that elapsed time is at least 0.1 seconds
    elapsed = interp.traditional.global_env.get('elapsed')
    assert elapsed >= 0.1


def test_delay_statement_arabic():
    """Test delay statement with Arabic keywords"""
    code = """
بداية = time.time()
تأخير 0.05 ثانية
نهاية = time.time()
مضى = نهاية - بداية
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()

    # Add time module to environment
    import time as time_module
    interp.traditional.global_env['time'] = time_module

    result = interp.interpret(ast)

    # Check that elapsed time is at least 0.05 seconds
    elapsed = interp.traditional.global_env.get('مضى')
    assert elapsed >= 0.05


def test_within_block_success():
    """Test within block that completes in time"""
    code = """
within 1.0 seconds {
    x = 42
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)

    # Should complete successfully
    assert interp.traditional.global_env.get('x') == 42


def test_within_block_arabic():
    """Test within block with Arabic keywords"""
    code = """
خلال 2.0 ثواني {
    س = 100
    ص = س * 2
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)

    # Should complete successfully
    assert interp.traditional.global_env.get('ص') == 200


def test_schedule_block_english():
    """Test schedule block with English keywords"""
    code = """
counter = 0
schedule every 0.5 seconds {
    counter = counter + 1
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)

    # Should execute once (simplified implementation)
    assert interp.traditional.global_env.get('counter') == 1


def test_schedule_block_arabic():
    """Test schedule block with Arabic keywords"""
    code = """
عداد = 0
جدولة كل 1.0 ثانية {
    عداد = عداد + 5
}
"""
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    result = interp.interpret(ast)

    # Should execute once (simplified implementation)
    assert interp.traditional.global_env.get('عداد') == 5

