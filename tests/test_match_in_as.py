"""
Tests for match ... in ... as syntax
اختبارات لصيغة match ... in ... as
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


def test_match_in_as_basic():
    """Test basic match ... in ... as syntax"""
    code = """
hybrid {
    text = "سافر خالد إلى مكة"
    match "سافر {اسم} إلى {مدينة}" in text as m
    
    if m:
    {
        who = m["اسم"]
        where = m["مدينة"]
    }
    print(who)
    print(where)
}
"""
    interp = run_code(code)
    env = interp.traditional.global_env
    assert env.get('who') == "خالد"
    assert env.get('where') == "مكة"


def test_match_in_as_with_template():
    """Test match ... in ... as with template() function"""
    code = """
hybrid {
    line = "User Ali scored 42"
    tpl = template("User {name} scored {score:\\d+}")
    match tpl in line as m
    
    if m:
    {
        uname = m["name"]
        uscore = m["score"]
    }
    print(uname)
    print(uscore)
}
"""
    interp = run_code(code)
    env = interp.traditional.global_env
    assert env.get('uname') == "Ali"
    assert env.get('uscore') == "42"


def test_match_in_as_no_match():
    """Test match ... in ... as when pattern doesn't match"""
    code = """
hybrid {
    text = "hello world"
    match "goodbye {name}" in text as m
    
    if m:
    {
        result = "matched"
    }
    else:
    {
        result = "no match"
    }
    print(result)
}
"""
    interp = run_code(code)
    env = interp.traditional.global_env
    assert env.get('result') == "no match"
    assert env.get('m') is None


def test_match_in_as_arabic_keywords():
    """Test match ... in ... as with Arabic keywords"""
    code = """
hybrid {
    النص = "مرحبا سارة"
    طابق "مرحبا {اسم}" في النص كـ م
    
    if م:
    {
        من = م["اسم"]
    }
    print(من)
}
"""
    interp = run_code(code)
    env = interp.traditional.global_env
    assert env.get('من') == "سارة"


def test_match_in_as_english():
    """Test match ... in ... as with English text"""
    code = """
hybrid {
    sentence = "The cat sat on the mat"
    match "The {animal} sat on the {object}" in sentence as result
    
    if result:
    {
        a = result["animal"]
        o = result["object"]
    }
    print(a)
    print(o)
}
"""
    interp = run_code(code)
    env = interp.traditional.global_env
    assert env.get('a') == "cat"
    assert env.get('o') == "mat"


def test_match_in_as_with_regex():
    """Test match ... in ... as with regex patterns"""
    code = """
hybrid {
    data = "Temperature: 25.5 degrees"
    match "Temperature: {temp:\\d+\\.\\d+} degrees" in data as m
    
    if m:
    {
        temperature = m["temp"]
    }
    print(temperature)
}
"""
    interp = run_code(code)
    env = interp.traditional.global_env
    assert env.get('temperature') == "25.5"

