import unittest
import types
from bayan.bayan.ast_nodes import *
from bayan.bayan.bytecode_compiler import BytecodeCompiler

class TestBytecodeCompiler(unittest.TestCase):
    def setUp(self):
        self.compiler = BytecodeCompiler()

    def test_compile_number(self):
        # Program: 42
        ast = Program([Number(42)])
        code = self.compiler.compile(ast)
        self.assertIsInstance(code, types.CodeType)
        # Should execute without error (though it does nothing visible)
        exec(code)

    def test_compile_arithmetic(self):
        # Program: 1 + 2
        ast = Program([BinaryOp('+', Number(1), Number(2))])
        code = self.compiler.compile(ast)
        exec(code)

    def test_compile_assignment(self):
        # Program: x = 10
        ast = Program([Assignment('x', Number(10))])
        code = self.compiler.compile(ast)
        
        # Capture locals
        loc = {}
        exec(code, {}, loc)
        self.assertEqual(loc['x'], 10)

    def test_compile_complex_expression(self):
        # Program: y = (10 + 5) * 2
        ast = Program([
            Assignment('y', BinaryOp('*', 
                                     BinaryOp('+', Number(10), Number(5)), 
                                     Number(2)))
        ])
        code = self.compiler.compile(ast)
        loc = {}
        exec(code, {}, loc)
        self.assertEqual(loc['y'], 30)

if __name__ == '__main__':
    unittest.main()
