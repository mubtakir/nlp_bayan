from bayan.bayan.ast_nodes import *
from bayan.bayan.bytecode_compiler import BytecodeCompiler

# Simple test
compiler = BytecodeCompiler()

# Test: if True: x = 10
ast = Program([
    IfStatement(
        Boolean(True),
        Assignment('x', Number(10)),
        None
    )
])

try:
    code = compiler.compile(ast)
    print("Compilation successful!")
    print(f"Bytecode length: {len(compiler.bytecode)}")
    print(f"Labels: {compiler.labels}")
    print(f"Jumps: {compiler.jumps}")
    
    loc = {}
    exec(code, {}, loc)
    print(f"Result: x = {loc.get('x')}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
