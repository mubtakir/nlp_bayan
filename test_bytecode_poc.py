#!/usr/bin/env python3
"""
Bytecode Compiler PoC Test
===========================

Test the bytecode compiler proof of concept with simple expressions.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bayan.bayan.bytecode.instruction import Instruction, CodeObject
from bayan.bayan.bytecode.vm import BytecodeVM
from bayan.bayan.bytecode.opcodes import Opcode


def test_simple_arithmetic():
    """Test: x = 10 + 20"""
    print("=" * 60)
    print("Test 1: Simple Arithmetic (x = 10 + 20)")
    print("=" * 60)
    
    # Manually create bytecode for: x = 10 + 20
    instructions = [
        Instruction(Opcode.LOAD_CONST, 0),  # Load 10
        Instruction(Opcode.LOAD_CONST, 1),  # Load 20
        Instruction(Opcode.ADD),             # Add
        Instruction(Opcode.STORE_VAR, 0),   # Store to 'x'
    ]
    
    code = CodeObject(
        name='<test>',
        instructions=instructions,
        constants=[10, 20],
        names=['x']
    )
    
    print("\nDisassembly:")
    print(code.disassemble())
    
    # Execute
    vm = BytecodeVM()
    result = vm.execute(code)
    
    print("\nVariables:", vm.get_variables())
    print("Expected: {'x': 30}")
    print("✓ PASSED" if vm.get_variables().get('x') == 30 else "✗ FAILED")
    print()


def test_complex_expression():
    """Test: z = (10 + 20) * 3"""
    print("=" * 60)
    print("Test 2: Complex Expression (z = (10 + 20) * 3)")
    print("=" * 60)
    
    instructions = [
        Instruction(Opcode.LOAD_CONST, 0),  # Load 10
        Instruction(Opcode.LOAD_CONST, 1),  # Load 20
        Instruction(Opcode.ADD),             # Add -> 30
        Instruction(Opcode.LOAD_CONST, 2),  # Load 3
        Instruction(Opcode.MUL),             # Multiply -> 90
        Instruction(Opcode.STORE_VAR, 0),   # Store to 'z'
    ]
    
    code = CodeObject(
        name='<test>',
        instructions=instructions,
        constants=[10, 20, 3],
        names=['z']
    )
    
    print("\nDisassembly:")
    print(code.disassemble())
    
    vm = BytecodeVM()
    result = vm.execute(code)
    
    print("\nVariables:", vm.get_variables())
    print("Expected: {'z': 90}")
    print("✓ PASSED" if vm.get_variables().get('z') == 90 else "✗ FAILED")
    print()


def test_multiple_variables():
    """Test: a = 5, b = 10, c = a + b"""
    print("=" * 60)
    print("Test 3: Multiple Variables (a=5, b=10, c=a+b)")
    print("=" * 60)
    
    instructions = [
        # a = 5
        Instruction(Opcode.LOAD_CONST, 0),
        Instruction(Opcode.STORE_VAR, 0),
        
        # b = 10
        Instruction(Opcode.LOAD_CONST, 1),
        Instruction(Opcode.STORE_VAR, 1),
        
        # c = a + b
        Instruction(Opcode.LOAD_VAR, 0),   # Load 'a'
        Instruction(Opcode.LOAD_VAR, 1),   # Load 'b'
        Instruction(Opcode.ADD),
        Instruction(Opcode.STORE_VAR, 2),   # Store to 'c'
    ]
    
    code = CodeObject(
        name='<test>',
        instructions=instructions,
        constants=[5, 10],
        names=['a', 'b', 'c']
    )
    
    print("\nDisassembly:")
    print(code.disassemble())
    
    vm = BytecodeVM()
    result = vm.execute(code)
    
    print("\nVariables:", vm.get_variables())
    print("Expected: {'a': 5, 'b': 10, 'c': 15}")
    
    vars = vm.get_variables()
    passed = (vars.get('a') == 5 and 
              vars.get('b') == 10 and 
              vars.get('c') == 15)
    print("✓ PASSED" if passed else "✗ FAILED")
    print()


def test_comparison():
    """Test: result = 10 > 5"""
    print("=" * 60)
    print("Test 4: Comparison (result = 10 > 5)")
    print("=" * 60)
    
    instructions = [
        Instruction(Opcode.LOAD_CONST, 0),  # Load 10
        Instruction(Opcode.LOAD_CONST, 1),  # Load 5
        Instruction(Opcode.GT),              # Greater than
        Instruction(Opcode.STORE_VAR, 0),   # Store to 'result'
    ]
    
    code = CodeObject(
        name='<test>',
        instructions=instructions,
        constants=[10, 5],
        names=['result']
    )
    
    print("\nDisassembly:")
    print(code.disassemble())
    
    vm = BytecodeVM()
    result = vm.execute(code)
    
    print("\nVariables:", vm.get_variables())
    print("Expected: {'result': True}")
    print("✓ PASSED" if vm.get_variables().get('result') == True else "✗ FAILED")
    print()


def test_print():
    """Test: print(42)"""
    print("=" * 60)
    print("Test 5: Print Statement")
    print("=" * 60)
    
    instructions = [
        Instruction(Opcode.LOAD_CONST, 0),  # Load 42
        Instruction(Opcode.PRINT),           # Print
    ]
    
    code = CodeObject(
        name='<test>',
        instructions=instructions,
        constants=[42],
        names=[]
    )
    
    print("\nDisassembly:")
    print(code.disassemble())
    
    print("\nOutput:")
    vm = BytecodeVM()
    result = vm.execute(code)
    
    print("✓ PASSED (visual check)")
    print()


def main():
    print("\n" + "=" * 60)
    print("BAYAN BYTECODE COMPILER - PROOF OF CONCEPT")
    print("=" * 60)
    print()
    
    try:
        test_simple_arithmetic()
        test_complex_expression()
        test_multiple_variables()
        test_comparison()
        test_print()
        
        print("=" * 60)
        print("ALL TESTS COMPLETED")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
