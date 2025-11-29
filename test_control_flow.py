import unittest
import types
from bayan.bayan.ast_nodes import *
from bayan.bayan.bytecode_compiler import BytecodeCompiler

class TestControlFlow(unittest.TestCase):
    def setUp(self):
        self.compiler = BytecodeCompiler()

    def test_if_statement_true(self):
        # if True: x = 10
        ast = Program([
            IfStatement(
                Boolean(True),
                Assignment('x', Number(10)),
                None
            )
        ])
        code = self.compiler.compile(ast)
        loc = {}
        exec(code, {}, loc)
        self.assertEqual(loc['x'], 10)

    def test_if_else_statement_false(self):
        # if False: x = 10 else: x = 20
        ast = Program([
            IfStatement(
                Boolean(False),
                Assignment('x', Number(10)),
                Assignment('x', Number(20))
            )
        ])
        code = self.compiler.compile(ast)
        loc = {}
        exec(code, {}, loc)
        self.assertEqual(loc['x'], 20)

    def test_while_loop(self):
        # x = 0
        # while x < 5: x = x + 1
        ast = Program([
            Assignment('x', Number(0)),
            WhileLoop(
                BinaryOp('<', Variable('x'), Number(5)),
                Assignment('x', BinaryOp('+', Variable('x'), Number(1)))
            )
        ])
        code = self.compiler.compile(ast)
        loc = {}
        exec(code, {}, loc)
        self.assertEqual(loc['x'], 5)

    def test_for_loop_range(self):
        # sum = 0
        # for i in range(5): sum = sum + i
        ast = Program([
            Assignment('sum', Number(0)),
            ForLoop(
                'i',
                FunctionCall('range', [Number(5)]),
                Assignment('sum', BinaryOp('+', Variable('sum'), Variable('i')))
            )
        ])
        code = self.compiler.compile(ast)
        loc = {}
        exec(code, {'range': range}, loc)
        self.assertEqual(loc['sum'], 10)  # 0+1+2+3+4 = 10

    def test_nested_if(self):
        # x = 5
        # if x > 0:
        #     if x > 3:
        #         y = 100
        #     else:
        #         y = 50
        # else:
        #     y = 0
        ast = Program([
            Assignment('x', Number(5)),
            IfStatement(
                BinaryOp('>', Variable('x'), Number(0)),
                IfStatement(
                    BinaryOp('>', Variable('x'), Number(3)),
                    Assignment('y', Number(100)),
                    Assignment('y', Number(50))
                ),
                Assignment('y', Number(0))
            )
        ])
        code = self.compiler.compile(ast)
        loc = {}
        exec(code, {}, loc)
        self.assertEqual(loc['y'], 100)

if __name__ == '__main__':
    unittest.main()
