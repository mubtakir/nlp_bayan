from bayan.bayan.ast_nodes import *
from bayan.bayan.bytecode_compiler import BytecodeCompiler
import dis

# Test while loop
compiler = BytecodeCompiler()

# x = 0
# while x < 5: x = x + 1
ast = Program([
    Assignment('x', Number(0)),
    WhileLoop(
        BinaryOp('<', Variable('x'), Number(5)),
        Assignment('x', BinaryOp('+', Variable('x'), Number(1)))
    )
])

try:
    code = compiler.compile(ast)
    print("Compilation successful!")
    print(f"\nLabels: {compiler.labels}")
    print(f"Jumps: {compiler.jumps}")
    print(f"\nDisassembly:")
    dis.dis(code)
    
    print(f"\nExecution:")
    loc = {}
    exec(code, {}, loc)
    print(f"Result: x = {loc.get('x')}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
