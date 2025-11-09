from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(ast)
    return interp


def test_vision_conv2d_valid_and_sobel():
    code = """
from ai.vision import conv2d_valid_3x3, sobel_x_kernel
hybrid {
  img = [[1,2,3],[4,5,6],[7,8,9]]
  k = [[0,0,0],[0,1,0],[0,0,0]]
  r = conv2d_valid_3x3(img, k)
  sx = sobel_x_kernel()
}
"""
    interp = run_interp(code)
    env = interp.traditional.global_env
    r = env["r"]
    assert r == [[5]]
    sx = env["sx"]
    assert sx == [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]

