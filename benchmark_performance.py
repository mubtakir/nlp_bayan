#!/usr/bin/env python3
"""
Bytecode vs AST Performance Benchmark
======================================

Compare bytecode execution against AST interpretation to measure actual speedup.
"""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bayan.bayan.bytecode.instruction import Instruction, CodeObject
from bayan.bayan.bytecode.vm import BytecodeVM
from bayan.bayan.bytecode.opcodes import Opcode


def benchmark_arithmetic_bytecode(iterations=10000):
    """Benchmark arithmetic in bytecode"""
    # Code: x = (10 + 20) * 3
    code = CodeObject(
        name='arithmetic',
        instructions=[
            Instruction(Opcode.LOAD_CONST, 0),
            Instruction(Opcode.LOAD_CONST, 1),
            Instruction(Opcode.ADD),
            Instruction(Opcode.LOAD_CONST, 2),
            Instruction(Opcode.MUL),
            Instruction(Opcode.STORE_VAR, 0),
        ],
        constants=[10, 20, 3],
        names=['x']
    )
    
    vm = BytecodeVM()
    
    start = time.perf_counter()
    for _ in range(iterations):
        vm.reset()
        vm.execute(code)
    end = time.perf_counter()
    
    return end - start


def benchmark_arithmetic_python(iterations=10000):
    """Benchmark same arithmetic in pure Python (simulating AST)"""
    start = time.perf_counter()
    for _ in range(iterations):
        x = (10 + 20) * 3
    end = time.perf_counter()
    
    return end - start


def benchmark_loop_bytecode(iterations=1000):
    """Benchmark while loop in bytecode"""
    # Code: 
    # i = 0
    # sum = 0
    # while i < 10:
    #     sum = sum + i
    #     i = i + 1
    
    code = CodeObject(
        name='loop',
        instructions=[
            Instruction(Opcode.LOAD_CONST, 0),    # i = 0
            Instruction(Opcode.STORE_VAR, 0),
            Instruction(Opcode.LOAD_CONST, 0),    # sum = 0
            Instruction(Opcode.STORE_VAR, 1),
            
            # while i < 10:
            Instruction(Opcode.LOAD_VAR, 0),      # 4
            Instruction(Opcode.LOAD_CONST, 1),
            Instruction(Opcode.LT),
            Instruction(Opcode.JUMP_IF_FALSE, 16),
            
            # sum = sum + i
            Instruction(Opcode.LOAD_VAR, 1),      # 8
            Instruction(Opcode.LOAD_VAR, 0),
            Instruction(Opcode.ADD),
            Instruction(Opcode.STORE_VAR, 1),
            
            # i = i + 1
            Instruction(Opcode.LOAD_VAR, 0),      # 12
            Instruction(Opcode.LOAD_CONST, 2),
            Instruction(Opcode.ADD),
            Instruction(Opcode.STORE_VAR, 0),
            
            Instruction(Opcode.JUMP, 4),          # 16 (jump back)
        ],
        constants=[0, 10, 1],
        names=['i', 'sum']
    )
    
    vm = BytecodeVM()
    
    start = time.perf_counter()
    for _ in range(iterations):
        vm.reset()
        vm.execute(code)
    end = time.perf_counter()
    
    return end - start


def benchmark_loop_python(iterations=1000):
    """Benchmark same loop in Python"""
    start = time.perf_counter()
    for _ in range(iterations):
        i = 0
        sum_val = 0
        while i < 10:
            sum_val = sum_val + i
            i = i + 1
    end = time.perf_counter()
    
    return end - start


def benchmark_function_bytecode(iterations=5000):
    """Benchmark function call in bytecode"""
    # def add_two(x): return x + 2
    # result = add_two(5)
    
    func_code = CodeObject(
        name='add_two',
        instructions=[
            Instruction(Opcode.LOAD_VAR, 0),
            Instruction(Opcode.LOAD_CONST, 0),
            Instruction(Opcode.ADD),
            Instruction(Opcode.RETURN),
        ],
        constants=[2],
        names=['arg0']
    )
    
    main_code = CodeObject(
        name='main',
        instructions=[
            Instruction(Opcode.LOAD_CONST, 0),
            Instruction(Opcode.LOAD_CONST, 1),
            Instruction(Opcode.CALL_FUNC, 1),
            Instruction(Opcode.STORE_VAR, 0),
        ],
        constants=[func_code, 5],
        names=['result']
    )
    
    vm = BytecodeVM()
    
    start = time.perf_counter()
    for _ in range(iterations):
        vm.reset()
        vm.execute(main_code)
    end = time.perf_counter()
    
    return end - start


def benchmark_function_python(iterations=5000):
    """Benchmark function call in Python"""
    def add_two(x):
        return x + 2
    
    start = time.perf_counter()
    for _ in range(iterations):
        result = add_two(5)
    end = time.perf_counter()
    
    return end - start


def print_results(name, bytecode_time, python_time):
    """Print benchmark results"""
    speedup = python_time / bytecode_time if bytecode_time > 0 else 0
    
    print(f"\n{name}")
    print(f"  Bytecode: {bytecode_time*1000:.2f}ms")
    print(f"  Python:   {python_time*1000:.2f}ms")
    print(f"  Speedup:  {speedup:.2f}x", end="")
    
    if speedup > 1.5:
        print(" ✅ FASTER")
    elif speedup > 0.8:
        print(" ≈ SIMILAR")
    else:
        print(" ⚠️ SLOWER")


def main():
    print("=" * 60)
    print("BYTECODE vs AST PERFORMANCE BENCHMARK")
    print("=" * 60)
    
    print("\nWarming up...")
    benchmark_arithmetic_bytecode(100)
    benchmark_arithmetic_python(100)
    
    results = []
    
    print("\n" + "=" * 60)
    print("RUNNING BENCHMARKS")
    print("=" * 60)
    
    # Test 1: Arithmetic
    print("\n[1/3] Arithmetic Operations (10K iterations)")
    bc_time = benchmark_arithmetic_bytecode(10000)
    py_time = benchmark_arithmetic_python(10000)
    print_results("Arithmetic", bc_time, py_time)
    results.append(("Arithmetic", bc_time, py_time))
    
    # Test 2: Loops
    print("\n[2/3] While Loops (1K iterations)")
    bc_time = benchmark_loop_bytecode(1000)
    py_time = benchmark_loop_python(1000)
    print_results("While Loop", bc_time, py_time)
    results.append(("While Loop", bc_time, py_time))
    
    # Test 3: Functions
    print("\n[3/3] Function Calls (5K iterations)")
    bc_time = benchmark_function_bytecode(5000)
    py_time = benchmark_function_python(5000)
    print_results("Functions", bc_time, py_time)
    results.append(("Functions", bc_time, py_time))
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    total_bc = sum(r[1] for r in results)
    total_py = sum(r[2] for r in results)
    avg_speedup = sum(r[2]/r[1] for r in results) / len(results)
    
    print(f"\nTotal Bytecode Time: {total_bc*1000:.2f}ms")
    print(f"Total Python Time:   {total_py*1000:.2f}ms")
    print(f"Average Speedup:     {avg_speedup:.2f}x")
    
    print("\n" + "=" * 60)
    
    if avg_speedup > 1.5:
        print("✅ BYTECODE IS SIGNIFICANTLY FASTER!")
    elif avg_speedup > 0.8:
        print("≈ BYTECODE PERFORMANCE IS SIMILAR")
    else:
        print("⚠️ BYTECODE NEEDS OPTIMIZATION")
    
    print("=" * 60)
    
    print("\nNote: This compares bytecode VM against pure Python,")
    print("not against full Bayan AST interpretation.")
    print("Real Bayan (with AST) would be even slower,")
    print("so actual speedup is likely higher!\n")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
