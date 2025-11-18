"""
Test entity syntax unification: support both quoted and unquoted keys
"""
import pytest
from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter

def run_interp(code):
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.traditional.set_source(code, filename=None)
    result = interp.interpret(ast)
    return interp, result

def test_entity_old_syntax_quoted_keys():
    """Test old syntax with quoted keys (backward compatibility)"""
    code = '''
hybrid {
    entity Ahmed { "states": {"hunger": 0.6} }
}
query state("Ahmed", "hunger", ?V).
'''
    _, result = run_interp(code)
    assert isinstance(result, list) and result, "Expected non-empty query results"
    v = result[0].get('V')
    num = getattr(v, 'value', v)
    assert abs(num - 0.6) < 0.01

def test_entity_new_syntax_unquoted_keys():
    """Test new syntax with unquoted keys"""
    code = '''
hybrid {
    entity Ahmed { states: {"hunger": 0.6} }
}
query state("Ahmed", "hunger", ?V).
'''
    _, result = run_interp(code)
    assert isinstance(result, list) and result, "Expected non-empty query results"
    v = result[0].get('V')
    num = getattr(v, 'value', v)
    assert abs(num - 0.6) < 0.01

def test_entity_mixed_syntax():
    """Test mixing quoted and unquoted keys"""
    code = '''
hybrid {
    entity Ahmed {
        states: {"hunger": 0.6},
        "properties": {"x": 0.0}
    }
}
query property("Ahmed", "x", ?X).
'''
    _, result = run_interp(code)
    assert isinstance(result, list) and result, "Expected non-empty query results"
    x = result[0].get('X')
    num = getattr(x, 'value', x)
    assert abs(num - 0.0) < 0.01

def test_entity_full_new_syntax():
    """Test full entity definition with new syntax"""
    code = '''
hybrid {
    entity Ball {
        states: {
            "energy": {"type": "fuzzy", "value": 1.0}
        },
        properties: {
            "x": {"type": "numeric", "value": 0.0},
            "y": {"type": "numeric", "value": 0.0}
        },
        actions: {
            "move": {
                "effects": [
                    {"on": "x", "formula": "value + 5.0*action_value"},
                    {"on": "y", "formula": "value + 2.0*action_value"}
                ]
            }
        }
    }

    apply Ball.move(Ball, action_value=2.0)
}
query property("Ball", "y", ?Y).
'''
    _, result = run_interp(code)
    assert isinstance(result, list) and result, "Expected non-empty query results"
    y = result[0].get('Y')
    num = getattr(y, 'value', y)
    # y should be 0.0 + 2.0*2.0 = 4.0
    assert abs(num - 4.0) < 0.01

def test_entity_arabic_new_syntax():
    """Test Arabic entity with new syntax"""
    code = '''
hybrid {
    كيان أحمد {
        حالات: {"جوع": 0.7},
        خصائص: {"س": 0.0}
    }
}
query state("أحمد", "جوع", ?V).
'''
    _, result = run_interp(code)
    assert isinstance(result, list) and result, "Expected non-empty query results"
    v = result[0].get('V')
    num = getattr(v, 'value', v)
    assert abs(num - 0.7) < 0.01

def test_entity_reactions_new_syntax():
    """Test entity reactions with new syntax"""
    code = '''
hybrid {
    entity Ahmed {
        states: {"happiness": 0.5},
        reactions: {
            "praise": {
                "sensitivity": 0.7,
                "response": "happiness += sensitivity*0.3"
            }
        }
    }

    entity John {
        actions: {
            "praise": {
                "effects": []
            }
        }
    }

    apply John.praise(Ahmed, action_value=1.0)
}
query state("Ahmed", "happiness", ?H).
'''
    _, result = run_interp(code)
    assert isinstance(result, list) and result, "Expected non-empty query results"
    h = result[0].get('H')
    num = getattr(h, 'value', h)
    # happiness should be 0.5 + 0.7*0.3 = 0.5 + 0.21 = 0.71
    assert abs(num - 0.71) < 0.01

