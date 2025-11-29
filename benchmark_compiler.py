import time
import sys
from bayan.bayan.ast_nodes import *
from bayan.bayan.bytecode_compiler import BytecodeCompiler
from bayan.bayan.traditional_interpreter import TraditionalInterpreter

def benchmark():
    # Create a large AST: x = 0; x = x + 1; ... (100,000 times)
    stmts = [Assignment('x', Number(0))]
    for _ in range(100000):
        stmts.append(Assignment('x', BinaryOp('+', Variable('x'), Number(1))))
    
    ast = Program(stmts)
    
    print(f"Benchmarking {len(stmts)} statements...")
    
    # 1. Traditional Interpreter
    interpreter = TraditionalInterpreter()
    start_time = time.time()
    interpreter.interpret(ast)
    end_time = time.time()
    interp_time = end_time - start_time
    print(f"Interpreter Time: {interp_time:.4f}s")
    print(f"Interpreter Result: {interpreter.global_env.get('x')}")
    
    # 2. Bytecode Compiler
    compiler = BytecodeCompiler()
    # Compilation time
    start_compile = time.time()
    code = compiler.compile(ast)
    end_compile = time.time()
    compile_time = end_compile - start_compile
    print(f"Compilation Time: {compile_time:.4f}s")
    
    # Execution time
    start_exec = time.time()
    loc = {}
    exec(code, {}, loc)
    end_exec = time.time()
    exec_time = end_exec - start_exec
    print(f"Bytecode Exec Time: {exec_time:.4f}s")
    print(f"Bytecode Result: {loc.get('x')}")
    
    # Comparison
    total_bytecode_time = compile_time + exec_time
    print(f"\nSpeedup (Exec only): {interp_time / exec_time:.2f}x")
    print(f"Speedup (Total): {interp_time / total_bytecode_time:.2f}x")

if __name__ == '__main__':
    benchmark()
