from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_data_json_text_array_and_object():
    code = """
    import ai.data as data
    hybrid {
      txt_arr = '["a","b","c"]'
      arr = data.read_json_string(txt_arr)
      out_arr = data.write_json_array_string(arr)

      obj = {"x": "one", "y": "two"}
      out_obj = data.write_json_object_string(obj)

      # Arabic wrappers
      arr2 = data.قراءة_JSON_نص(txt_arr)
      out_arr2 = data.كتابة_JSON_قائمة(arr)
      out_obj2 = data.كتابة_JSON_كائن(obj)

      txt_obj = '{"a":"1","b":"2"}'
      obj2 = data.read_json_string(txt_obj)
      out_obj3 = data.write_json_object_string(obj2)
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    arr = env.get('arr'); arr2 = env.get('arr2')
    out_arr = env.get('out_arr'); out_arr2 = env.get('out_arr2')
    out_obj = env.get('out_obj'); out_obj2 = env.get('out_obj2'); out_obj3 = env.get('out_obj3')

    assert arr == ["a", "b", "c"]
    assert arr2 == arr
    assert out_arr == '["a","b","c"]'
    assert out_arr2 == out_arr

    # object writer sorts keys lexicographically; here already sorted
    assert out_obj == '{"x":"one","y":"two"}'
    assert out_obj2 == out_obj
    # round-trip for parsed object
    assert out_obj3 == '{"a":"1","b":"2"}'

