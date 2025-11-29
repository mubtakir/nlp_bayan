import dis
import sys
from bayan.bayan.bytecode_compiler import BytecodeCompiler
from bayan.bayan.ast_nodes import *

print(f"Python Version: {sys.version}")
if sys.version_info >= (3, 11):
    opcode = dis.opmap['POP_JUMP_IF_FALSE']
    print(f"POP_JUMP_IF_FALSE cache entries: {dis._inline_cache_entries[opcode]}")


compiler = BytecodeCompiler()

# While Loop Test Case
# x = 0
# while x < 5: x = x + 1
ast = Program([
    Assignment('x', Number(0)),
    WhileLoop(
        BinaryOp('<', Variable('x'), Number(5)),
        Assignment('x', BinaryOp('+', Variable('x'), Number(1)))
    )
])

print("\n--- Compiling While Loop ---")
try:
    code = compiler.compile(ast)
    print("--- Bytecode ---")
    dis.dis(code)
    print("----------------")
    
    print("\n--- Executing ---")
    loc = {}
    exec(code, {}, loc)
    print(f"Result: x = {loc.get('x')}")
    if loc.get('x') == 5:
        print("SUCCESS")
    else:
        print(f"FAILURE: Expected 5, got {loc.get('x')}")

except Exception as e:
    print(f"Error: {e}")
