#!/usr/bin/env python3
"""
Test Bytecode Optimizer
========================

Tests constant folding and peephole optimization.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bayan.bayan.bytecode.instruction import Instruction, CodeObject
from bayan.bayan.bytecode.opcodes import Opcode
from bayan.bayan.bytecode.optimizer import BytecodeOptimizer


def test_constant_folding():
    """
    Test: 10 + 20 -> 30
    """
    print("=" * 60)
    print("Test: Constant Folding")
    print("=" * 60)
    
    # Original: 10 + 20
    instructions = [
        Instruction(Opcode.LOAD_CONST, 0),   # 10
        Instruction(Opcode.LOAD_CONST, 1),   # 20
        Instruction(Opcode.ADD),
        Instruction(Opcode.STORE_VAR, 0),
    ]
    
    code = CodeObject(
        name='test_fold',
        instructions=instructions,
        constants=[10, 20],
        names=['x']
    )
    
    print("Before Optimization:")
    print(code.disassemble())
    
    optimizer = BytecodeOptimizer()
    optimized_code = optimizer.optimize(code)
    
    print("\nAfter Optimization:")
    print(optimized_code.disassemble())
    
    # Check results
    instrs = optimized_code.instructions
    # Should be: LOAD_CONST 30 (index 2), STORE_VAR x
    
    passed = (len(instrs) == 2 and 
              instrs[0].opcode == Opcode.LOAD_CONST and 
              optimized_code.constants[instrs[0].arg] == 30)
    
    print("\nResult:", "✓ PASSED" if passed else "✗ FAILED")
    return passed


def test_complex_folding():
    """
    Test: (10 + 20) * 3 -> 90
    """
    print("\n" + "=" * 60)
    print("Test: Complex Constant Folding")
    print("=" * 60)
    
    # Original: (10 + 20) * 3
    instructions = [
        Instruction(Opcode.LOAD_CONST, 0),   # 10
        Instruction(Opcode.LOAD_CONST, 1),   # 20
        Instruction(Opcode.ADD),              # -> 30
        Instruction(Opcode.LOAD_CONST, 2),   # 3
        Instruction(Opcode.MUL),              # -> 90
        Instruction(Opcode.STORE_VAR, 0),
    ]
    
    code = CodeObject(
        name='test_complex',
        instructions=instructions,
        constants=[10, 20, 3],
        names=['z']
    )
    
    print("Before Optimization:")
    print(code.disassemble())
    
    optimizer = BytecodeOptimizer()
    optimized_code = optimizer.optimize(code)
    
    print("\nAfter Optimization:")
    print(optimized_code.disassemble())
    
    # Check results
    instrs = optimized_code.instructions
    # Should be: LOAD_CONST 90, STORE_VAR z
    
    passed = (len(instrs) == 2 and 
              instrs[0].opcode == Opcode.LOAD_CONST and 
              optimized_code.constants[instrs[0].arg] == 90)
    
    print("\nResult:", "✓ PASSED" if passed else "✗ FAILED")
    return passed


def test_peephole_optimization():
    """
    Test: LOAD_CONST 10, POP -> Removed
    """
    print("\n" + "=" * 60)
    print("Test: Peephole Optimization")
    print("=" * 60)
    
    # Original: LOAD_CONST 10; POP; PRINT 42
    instructions = [
        Instruction(Opcode.LOAD_CONST, 0),   # 10
        Instruction(Opcode.POP),              # Useless
        Instruction(Opcode.LOAD_CONST, 1),   # 42
        Instruction(Opcode.PRINT),
    ]
    
    code = CodeObject(
        name='test_peephole',
        instructions=instructions,
        constants=[10, 42],
        names=[]
    )
    
    print("Before Optimization:")
    print(code.disassemble())
    
    optimizer = BytecodeOptimizer()
    optimized_code = optimizer.optimize(code)
    
    print("\nAfter Optimization:")
    print(optimized_code.disassemble())
    
    # Check results
    instrs = optimized_code.instructions
    # Should be: LOAD_CONST 42, PRINT
    
    passed = (len(instrs) == 2 and 
              instrs[0].opcode == Opcode.LOAD_CONST and 
              optimized_code.constants[instrs[0].arg] == 42)
    
    print("\nResult:", "✓ PASSED" if passed else "✗ FAILED")
    return passed


def main():
    results = [
        test_constant_folding(),
        test_complex_folding(),
        test_peephole_optimization()
    ]
    
    if all(results):
        print("\nALL TESTS PASSED ✓")
        return 0
    else:
        print("\nSOME TESTS FAILED ✗")
        return 1

if __name__ == "__main__":
    sys.exit(main())
