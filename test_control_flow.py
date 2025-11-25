#!/usr/bin/env python3
"""
Test Control Flow in Bytecode Compiler
========================================

Tests if/while/for statements
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bayan.bayan.bytecode.instruction import Instruction, CodeObject
from bayan.bayan.bytecode.vm import BytecodeVM
from bayan.bayan.bytecode.opcodes import Opcode


def test_if_statement():
    """
    Test: if (x > 5) { y = 10 } else { y = 20 }
    with x = 7
    Expected: y = 10
    """
    print("=" * 60)
    print("Test: If Statement")
    print("=" * 60)
    
    # Bytecode for:
    # x = 7
    # if (x > 5) { y = 10 } else { y = 20 }
    
    instructions = [
        # x = 7
        Instruction(Opcode.LOAD_CONST, 0),   # 0: Load 7
        Instruction(Opcode.STORE_VAR, 0),    # 2: Store to 'x'
        
        # if (x > 5)
        Instruction(Opcode.LOAD_VAR, 0),     # 4: Load 'x'
        Instruction(Opcode.LOAD_CONST, 1),   # 6: Load 5
        Instruction(Opcode.GT),               # 8: x > 5
        Instruction(Opcode.JUMP_IF_FALSE, 14), # 9: Jump to else if false
        
        # then block: y = 10
        Instruction(Opcode.LOAD_CONST, 2),   # 11: Load 10
        Instruction(Opcode.STORE_VAR, 1),    # 13: Store to 'y'
        Instruction(Opcode.JUMP, 17),        # 15: Jump to end
        
        # else block: y = 20
        Instruction(Opcode.LOAD_CONST, 3),   # 17: Load 20 (offset 14 in list)
        Instruction(Opcode.STORE_VAR, 1),    # 19: Store to 'y'
        
        # end (offset 17 in list)
    ]
    
    code = CodeObject(
        name='<test_if>',
        instructions=instructions,
        constants=[7, 5, 10, 20],
        names=['x', 'y']
    )
    
    print("\nDisassembly:")
    print(code.disassemble())
    
    vm = BytecodeVM()
    result = vm.execute(code)
    
    print("\nVariables:", vm.get_variables())
    print("Expected: {'x': 7, 'y': 10}")
    
    vars = vm.get_variables()
    passed = vars.get('x') == 7 and vars.get('y') == 10
    print("✓ PASSED" if passed else "✗ FAILED")
    print()
    
    return passed


def test_if_false_branch():
    """Test if statement with false condition"""
    print("=" * 60)
    print("Test: If Statement (False Branch)")
    print("=" * 60)
    
    # x = 3
    # if (x > 5) { y = 10 } else { y = 20 }
    # Expected: y = 20
    
    instructions = [
        Instruction(Opcode.LOAD_CONST, 0),   # x = 3
        Instruction(Opcode.STORE_VAR, 0),
        
        Instruction(Opcode.LOAD_VAR, 0),     # if (x > 5)
        Instruction(Opcode.LOAD_CONST, 1),
        Instruction(Opcode.GT),
        Instruction(Opcode.JUMP_IF_FALSE, 9),
        
        Instruction(Opcode.LOAD_CONST, 2),   # y = 10
        Instruction(Opcode.STORE_VAR, 1),
        Instruction(Opcode.JUMP, 11),
        
        Instruction(Opcode.LOAD_CONST, 3),   # y = 20
        Instruction(Opcode.STORE_VAR, 1),
    ]
    
    code = CodeObject(
        name='<test_if_false>',
        instructions=instructions,
        constants=[3, 5, 10, 20],
        names=['x', 'y']
    )
    
    print("\nDisassembly:")
    print(code.disassemble())
    
    vm = BytecodeVM()
    result = vm.execute(code)
    
    print("\nVariables:", vm.get_variables())
    print("Expected: {'x': 3, 'y': 20}")
    
    vars = vm.get_variables()
    passed = vars.get('x') == 3 and vars.get('y') == 20
    print("✓ PASSED" if passed else "✗ FAILED")
    print()
    
    return passed


def test_while_loop():
    """
    Test: 
    i = 0
    sum = 0
    while (i < 5) {
        sum = sum + i
        i = i + 1
    }
    Expected: sum = 0+1+2+3+4 = 10
    """
    print("=" * 60)
    print("Test: While Loop")
    print("=" * 60)
    
    instructions = [
        # i = 0
        Instruction(Opcode.LOAD_CONST, 0),   # 0
        Instruction(Opcode.STORE_VAR, 0),
        
        # sum = 0
        Instruction(Opcode.LOAD_CONST, 0),   # 0
        Instruction(Opcode.STORE_VAR, 1),
        
        # while (i < 5): (loop start at instruction 4)
        Instruction(Opcode.LOAD_VAR, 0),     # 4: Load i
        Instruction(Opcode.LOAD_CONST, 1),   # 6: Load 5
        Instruction(Opcode.LT),               # 8: i < 5
        Instruction(Opcode.JUMP_IF_FALSE, 20), # 9: Exit loop if false
        
        # sum = sum + i
        Instruction(Opcode.LOAD_VAR, 1),     # 11: Load sum
        Instruction(Opcode.LOAD_VAR, 0),     # 13: Load i
        Instruction(Opcode.ADD),              # 15: sum + i
        Instruction(Opcode.STORE_VAR, 1),    # 16: Store to sum
        
        # i = i + 1
        Instruction(Opcode.LOAD_VAR, 0),     # 18: Load i
        Instruction(Opcode.LOAD_CONST, 2),   # 20: Load 1
        Instruction(Opcode.ADD),              # 22: i + 1
        Instruction(Opcode.STORE_VAR, 0),    # 23: Store to i
        
        # Jump back to loop start
        Instruction(Opcode.JUMP, 4),         # 25: Jump to condition
        
        # Loop end (instruction 20)
    ]
    
    code = CodeObject(
        name='<test_while>',
        instructions=instructions,
        constants=[0, 5, 1],
        names=['i', 'sum']
    )
    
    print("\nDisassembly:")
    print(code.disassemble())
    
    vm = BytecodeVM()
    result = vm.execute(code)
    
    print("\nVariables:", vm.get_variables())
    print("Expected: {'i': 5, 'sum': 10}")
    
    vars = vm.get_variables()
    passed = vars.get('i') == 5 and vars.get('sum') == 10
    print("✓ PASSED" if passed else "✗ FAILED")
    print()
    
    return passed


def main():
    print("\n" + "=" * 60)
    print("BYTECODE COMPILER - CONTROL FLOW TESTS")
    print("=" * 60)
    print()
    
    results = []
    
    try:
        results.append(("If Statement (True)", test_if_statement()))
        results.append(("If Statement (False)", test_if_false_branch()))
        results.append(("While Loop", test_while_loop()))
        
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
