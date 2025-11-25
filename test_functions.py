#!/usr/bin/env python3
"""
Test Functions in Bytecode Compiler
====================================

Tests function definitions and calls
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bayan.bayan.bytecode.instruction import Instruction, CodeObject
from bayan.bayan.bytecode.vm import BytecodeVM
from bayan.bayan.bytecode.opcodes import Opcode


def test_simple_function_call():
    """
    Test simple function call:
    def add_two(x):
        return x + 2
    
    result = add_two(5)
    Expected: result = 7
    """
    print("=" * 60)
    print("Test: Simple Function Call")
    print("=" * 60)
    
    # Function code: return arg0 + 2
    func_code = CodeObject(
        name='add_two',
        instructions=[
            Instruction(Opcode.LOAD_VAR, 0),      # Load arg0
            Instruction(Opcode.LOAD_CONST, 0),    # Load 2
            Instruction(Opcode.ADD),               # Add
            Instruction(Opcode.RETURN),            # Return (TOS = result)
        ],
        constants=[2],
        names=['arg0']
    )
    
    # Main code: result = add_two(5)
    instructions = [
        Instruction(Opcode.LOAD_CONST, 0),    # Load func_code
        Instruction(Opcode.LOAD_CONST, 1),    # Load argument 5
        Instruction(Opcode.CALL_FUNC, 1),     # Call with 1 arg
        Instruction(Opcode.STORE_VAR, 0),     # Store to 'result'
    ]
    
    main_code = CodeObject(
        name='<main>',
        instructions=instructions,
        constants=[func_code, 5],
        names=['result']
    )
    
    print("\nFunction code:")
    print(func_code.disassemble())
    print("\nMain code:")
    print(main_code.disassemble())
    
    vm = BytecodeVM()
    result = vm.execute(main_code)
    
    print("\nVariables:", vm.get_variables())
    print("Expected: {'result': 7}")
    
    passed = vm.get_variables().get('result') == 7
    print("✓ PASSED" if passed else "✗ FAILED")
    print()
    
    return passed


def test_function_with_two_args():
    """
    Test function with 2 arguments:
    def multiply(a, b):
        return a * b
    
    result = multiply(6, 7)
    Expected: result = 42
    """
    print("=" * 60)
    print("Test: Function with Two Arguments")
    print("=" * 60)
    
    # Function code: return arg0 * arg1
    func_code = CodeObject(
        name='multiply',
        instructions=[
            Instruction(Opcode.LOAD_VAR, 0),      # Load arg0
            Instruction(Opcode.LOAD_VAR, 1),      # Load arg1
            Instruction(Opcode.MUL),               # Multiply
            Instruction(Opcode.RETURN),
        ],
        constants=[],
        names=['arg0', 'arg1']
    )
    
    # Main code
    instructions = [
        Instruction(Opcode.LOAD_CONST, 0),    # Load func
        Instruction(Opcode.LOAD_CONST, 1),    # Load 6
        Instruction(Opcode.LOAD_CONST, 2),    # Load 7
        Instruction(Opcode.CALL_FUNC, 2),     # Call with 2 args
        Instruction(Opcode.STORE_VAR, 0),
    ]
    
    main_code = CodeObject(
        name='<main>',
        instructions=instructions,
        constants=[func_code, 6, 7],
        names=['result']
    )
    
    print("\nFunction code:")
    print(func_code.disassemble())
    print("\nMain code:")
    print(main_code.disassemble())
    
    vm = BytecodeVM()
    result = vm.execute(main_code)
    
    print("\nVariables:", vm.get_variables())
    print("Expected: {'result': 42}")
    
    passed = vm.get_variables().get('result') == 42
    print("✓ PASSED" if passed else "✗ FAILED")
    print()
    
    return passed


def test_nested_function_calls():
    """
    Test nested function calls:
    def double(x):
        return x * 2
    
    def add_one(x):
        return x + 1
    
    result = double(add_one(5))
    Expected: result = 12 (5+1=6, 6*2=12)
    """
    print("=" * 60)
    print("Test: Nested Function Calls")
    print("=" * 60)
    
    # double function
    double_code = CodeObject(
        name='double',
        instructions=[
            Instruction(Opcode.LOAD_VAR, 0),
            Instruction(Opcode.LOAD_CONST, 0),    # 2
            Instruction(Opcode.MUL),
            Instruction(Opcode.RETURN),
        ],
        constants=[2],
        names=['arg0']
    )
    
    # add_one function
    add_one_code = CodeObject(
        name='add_one',
        instructions=[
            Instruction(Opcode.LOAD_VAR, 0),
            Instruction(Opcode.LOAD_CONST, 0),    # 1
            Instruction(Opcode.ADD),
            Instruction(Opcode.RETURN),
        ],
        constants=[1],
        names=['arg0']
    )
    
    # Main: result = double(add_one(5))
    instructions = [
        # Call double
        Instruction(Opcode.LOAD_CONST, 0),    # Load double
        
        # Inner call: add_one(5)
        Instruction(Opcode.LOAD_CONST, 1),    # Load add_one
        Instruction(Opcode.LOAD_CONST, 2),    # Load 5
        Instruction(Opcode.CALL_FUNC, 1),     # Call add_one(5) -> pushes 6
        
        # Now stack has: [double, 6]
        Instruction(Opcode.CALL_FUNC, 1),     # Call double(6) -> pushes 12
        Instruction(Opcode.STORE_VAR, 0),     # Store result
    ]
    
    main_code = CodeObject(
        name='<main>',
        instructions=instructions,
        constants=[double_code, add_one_code, 5],
        names=['result']
    )
    
    print("\nDouble function:")
    print(double_code.disassemble())
    print("\nAdd_one function:")
    print(add_one_code.disassemble())
    print("\nMain code:")
    print(main_code.disassemble())
    
    vm = BytecodeVM()
    result = vm.execute(main_code)
    
    print("\nVariables:", vm.get_variables())
    print("Expected: {'result': 12}")
    
    passed = vm.get_variables().get('result') == 12
    print("✓ PASSED" if passed else "✗ FAILED")
    print()
    
    return passed


def main():
    print("\n" + "=" * 60)
    print("BYTECODE COMPILER - FUNCTION TESTS")
    print("=" * 60)
    print()
    
    results = []
    
    try:
        results.append(("Simple Function Call", test_simple_function_call()))
        results.append(("Two Arguments", test_function_with_two_args()))
        results.append(("Nested Calls", test_nested_function_calls()))
        
        print("=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        
        for name, passed in results:
            status = "✓ PASSED" if passed else "✗ FAILED"
            print(f"{name:30s} {status}")
        
        all_passed = all(r[1] for r in results)
        print()
        print("=" * 60)
        if all_passed:
            print("ALL TESTS PASSED ✓")
        else:
            print("SOME TESTS FAILED ✗")
        print("=" * 60)
        
        return 0 if all_passed else 1
        
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
