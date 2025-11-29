import dis
import sys
from bayan.bayan.bytecode_compiler import BytecodeCompiler
from bayan.bayan.ast_nodes import *

print(f"Python Version: {sys.version}")
print(f"END_FOR in opmap: {'END_FOR' in dis.opmap}")

if 'END_FOR' in dis.opmap:
    print(f"END_FOR opcode: {dis.opmap['END_FOR']}")

# 2. Compiler Bytecode
print("\n2. Compiler Bytecode")
compiler = BytecodeCompiler()
ast = Program([
    ForLoop(
        'i',
        FunctionCall('range', [Number(5)]),
        Assignment('x', Variable('i'))
    )
])

# Monkey patch emit to support END_FOR for testing
original_visit_ForLoop = BytecodeCompiler.visit_ForLoop

def new_visit_ForLoop(self, node):
    # Get iterator
    self.visit(node.iterable)
    self.emit('GET_ITER')
    
    # Create labels
    loop_start = self.create_label()
    loop_end = self.create_label()
    
    # Mark loop start
    self.mark_label(loop_start)
    
    # FOR_ITER
    self.emit_jump('FOR_ITER', loop_end)
    if sys.version_info >= (3, 11):
        self.emit('CACHE', 0)
    
    # Store loop variable
    idx = self.add_name(node.variable)
    self.emit('STORE_NAME', idx)
    
    # Loop body
    self.visit(node.body)
    
    # Jump back
    if sys.version_info >= (3, 11):
        self.emit_jump('JUMP_BACKWARD', loop_start)
    else:
        self.emit_jump('JUMP_ABSOLUTE', loop_start)
    
    # Mark loop end
    self.mark_label(loop_end)
    
    # Emit END_FOR if available
    if 'END_FOR' in dis.opmap:
        self.emit('END_FOR')

BytecodeCompiler.visit_ForLoop = new_visit_ForLoop

try:
    code = compiler.compile(ast)
    print("--- Bytecode ---")
    dis.dis(code)
    print("----------------")
    
    print("\n3. Executing Code...")
    loc = {}
    exec(code, {'range': range}, loc)
    print("Execution Successful!")
    print(f"x = {loc.get('x')}")
except Exception as e:
    print(f"Error: {e}")
