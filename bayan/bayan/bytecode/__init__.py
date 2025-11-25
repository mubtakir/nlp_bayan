"""
Bayan Bytecode Module
=====================

This module implements a bytecode compiler and virtual machine for Bayan language.

Design Goals:
- 2-4x performance improvement over AST interpretation
- Stack-based VM architecture
- Compatible with existing Bayan features
- Incremental compilation support

Components:
- opcodes.py: Bytecode instruction definitions
- instruction.py: Instruction class
- vm.py: Virtual machine
- codegen.py: AST to bytecode compiler
- optimizer.py: Bytecode optimizer
- serializer.py: .byc file format

Author: Bayan Development Team
"""

from .opcodes import Opcode, OpcodeName
from .instruction import Instruction
from .vm import BytecodeVM
from .codegen import CodeGenerator

__all__ = [
    'Opcode',
    'OpcodeName',
    'Instruction',
    'BytecodeVM',
    'CodeGenerator',
]

__version__ = '0.1.0'
