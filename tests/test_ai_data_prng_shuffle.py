from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    return interp


def test_data_prng_and_shuffle_split():
    code = """
from ai.data import random_permutation, train_test_split_shuffle
hybrid {
  perm = random_permutation(10, 123)
  X = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
  y = [0,1,2,3,4,5,6,7,8,9]
  res = train_test_split_shuffle(X, y, 0.3, 42)
  X_train = res[0]
  X_test = res[1]
  y_train = res[2]
  y_test = res[3]
}
"""
    interp = run_interp(code)
    env = interp.traditional.global_env
    perm = env["perm"]
    assert sorted(perm) == list(range(10))
    X_train = env["X_train"]
    X_test = env["X_test"]
    y_train = env["y_train"]
    y_test = env["y_test"]
    assert len(X_train) == 7
    assert len(X_test) == 3
    assert len(y_train) == 7
    assert len(y_test) == 3

