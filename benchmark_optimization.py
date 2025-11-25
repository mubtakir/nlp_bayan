#!/usr/bin/env python3
"""
Bytecode Optimization Benchmark
================================

Compare optimized vs unoptimized bytecode performance.
"""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bayan.bayan.bytecode.instruction import Instruction, CodeObject
from bayan.bayan.bytecode.vm import BytecodeVM
from bayan.bayan.bytecode.opcodes import Opcode
from bayan.bayan.bytecode.optimizer import BytecodeOptimizer


def benchmark_optimization(iterations=10000):
    """
    Benchmark: (10 + 20) * 3
    Unoptimized: 6 instructions (LOAD, LOAD, ADD, LOAD, MUL, STORE)
    Optimized: 2 instructions (LOAD, STORE)
    """
    print("=" * 60)
    print("OPTIMIZATION BENCHMARK")
    print("=" * 60)
    
    # Unoptimized Code
    unopt_code = CodeObject(
        name='unoptimized',
        instructions=[
            Instruction(Opcode.LOAD_CONST, 0),   # 10
            Instruction(Opcode.LOAD_CONST, 1),   # 20
            Instruction(Opcode.ADD),
            Instruction(Opcode.LOAD_CONST, 2),   # 3
            Instruction(Opcode.MUL),
            Instruction(Opcode.STORE_VAR, 0),
        ],
        constants=[10, 20, 3],
        names=['x']
    )
    
    # Optimize it
    optimizer = BytecodeOptimizer()
    opt_code = optimizer.optimize(unopt_code)
    
    print("\nUnoptimized Code:")
    print(unopt_code.disassemble())
    print("\nOptimized Code:")
    print(opt_code.disassemble())
    
    vm = BytecodeVM()
    
    # Run Unoptimized
    start = time.perf_counter()
    for _ in range(iterations):
        vm.reset()
        vm.execute(unopt_code)
    end = time.perf_counter()
    unopt_time = end - start
    
    # Run Optimized
    start = time.perf_counter()
    for _ in range(iterations):
        vm.reset()
        vm.execute(opt_code)
    end = time.perf_counter()
    opt_time = end - start
    
    # Results
    print("\n" + "=" * 60)
    print(f"Iterations: {iterations}")
    print(f"Unoptimized: {unopt_time*1000:.2f}ms")
    print(f"Optimized:   {opt_time*1000:.2f}ms")
    
    speedup = unopt_time / opt_time if opt_time > 0 else 0
    print(f"Speedup:     {speedup:.2f}x")
    print("=" * 60)
    
    if speedup > 1.5:
        print("✅ SIGNIFICANT IMPROVEMENT")
    else:
        print("⚠️ MINOR IMPROVEMENT")
        
    return speedup

if __name__ == "__main__":
    benchmark_optimization()
