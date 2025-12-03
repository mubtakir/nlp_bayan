"""
Bytecode Optimizer
===================

Optimizes Bayan bytecode to improve runtime performance.

Strategies:
1. Constant Folding: Evaluate constant expressions at compile time.
2. Peephole Optimization: Replace inefficient instruction sequences.
"""

from .opcodes import Opcode
from .instruction import Instruction, CodeObject


class BytecodeOptimizer:
    """
    Optimizes bytecode instructions.
    """
    
    def __init__(self):
        self.changed = False
    
    def optimize(self, code_object):
        """
        Optimize a CodeObject.
        Returns a new, optimized CodeObject.
        """
        instructions = list(code_object.instructions)
        constants = list(code_object.constants)
        names = list(code_object.names)
        
        # Run optimization passes until no more changes
        max_passes = 5
        for _ in range(max_passes):
            self.changed = False
            
            # Pass 1: Constant Folding
            instructions = self._fold_constants(instructions, constants)
            
            # Pass 2: Peephole Optimization
            instructions = self._peephole_optimize(instructions)
            
            if not self.changed:
                break
        
        return CodeObject(code_object.name, instructions, constants, names)
    
    def _fold_constants(self, instructions, constants):
        """
        Fold constant expressions.
        Example: LOAD_CONST 1, LOAD_CONST 2, ADD -> LOAD_CONST 3
        """
        new_instrs = []
        i = 0
        
        while i < len(instructions):
            # Check for pattern: LOAD_CONST a, LOAD_CONST b, BINARY_OP
            if i + 2 < len(instructions):
                instr1 = instructions[i]
                instr2 = instructions[i+1]
                instr3 = instructions[i+2]
                
                if (instr1.opcode == Opcode.LOAD_CONST and
                    instr2.opcode == Opcode.LOAD_CONST and
                    instr3.opcode in (Opcode.ADD, Opcode.SUB, Opcode.MUL, Opcode.DIV, Opcode.POW)):
                    
                    # Found pattern! Calculate result
                    val1 = constants[instr1.arg]
                    val2 = constants[instr2.arg]
                    
                    try:
                        result = None
                        if instr3.opcode == Opcode.ADD:
                            result = val1 + val2
                        elif instr3.opcode == Opcode.SUB:
                            result = val1 - val2
                        elif instr3.opcode == Opcode.MUL:
                            result = val1 * val2
                        elif instr3.opcode == Opcode.DIV:
                            result = val1 / val2
                        elif instr3.opcode == Opcode.POW:
                            result = val1 ** val2
                        
                        if result is not None:
                            # Add new constant
                            if result in constants:
                                const_idx = constants.index(result)
                            else:
                                constants.append(result)
                                const_idx = len(constants) - 1
                            
                            # Emit single LOAD_CONST
                            new_instrs.append(Instruction(Opcode.LOAD_CONST, const_idx))
                            
                            # Skip consumed instructions
                            i += 3
                            self.changed = True
                            continue
                            
                    except Exception:
                        # If calculation fails (e.g. div by zero), skip optimization
                        pass
            
            # No optimization applied, keep instruction
            new_instrs.append(instructions[i])
            i += 1
            
        return new_instrs

    def _peephole_optimize(self, instructions):
        """
        Apply peephole optimizations.
        Example: LOAD_CONST x, POP -> NOP (removed)
        """
        new_instrs = []
        i = 0

        while i < len(instructions):
            instr = instructions[i]

            # Pattern 1: LOAD_CONST + POP -> Remove both
            if instr.opcode == Opcode.LOAD_CONST and i + 1 < len(instructions):
                next_instr = instructions[i+1]
                if next_instr.opcode == Opcode.POP:
                    # Skip both
                    i += 2
                    self.changed = True
                    continue

            # Pattern 2: LOAD_VAR + POP -> Remove both
            if instr.opcode == Opcode.LOAD_VAR and i + 1 < len(instructions):
                next_instr = instructions[i+1]
                if next_instr.opcode == Opcode.POP:
                    i += 2
                    self.changed = True
                    continue

            # Pattern 3: Double negation NOT NOT -> Remove both
            if instr.opcode == Opcode.NOT and i + 1 < len(instructions):
                next_instr = instructions[i+1]
                if next_instr.opcode == Opcode.NOT:
                    i += 2
                    self.changed = True
                    continue

            # Pattern 4: STORE_VAR followed by LOAD_VAR of same var -> DUP + STORE
            if instr.opcode == Opcode.STORE_VAR and i + 1 < len(instructions):
                next_instr = instructions[i+1]
                if next_instr.opcode == Opcode.LOAD_VAR and next_instr.arg == instr.arg:
                    # Replace with DUP + STORE_NAME
                    new_instrs.append(Instruction(Opcode.DUP, None))
                    new_instrs.append(instr)
                    i += 2
                    self.changed = True
                    continue

            # Pattern 5: Multiply by 1 -> Remove
            if i + 2 < len(instructions):
                if (instr.opcode == Opcode.LOAD_CONST and
                    instructions[i+1].opcode == Opcode.MUL):
                    # Check if constant is 1
                    pass  # Would need access to constants

            new_instrs.append(instr)
            i += 1

        return new_instrs

    def _dead_code_elimination(self, instructions):
        """
        Remove unreachable code after unconditional jumps.
        """
        new_instrs = []
        i = 0

        while i < len(instructions):
            instr = instructions[i]
            new_instrs.append(instr)

            # After RETURN, skip until next jump target
            if instr.opcode == Opcode.RETURN:
                i += 1
                # Skip until we find a jump target or end
                while i < len(instructions):
                    # Check if this is a jump target
                    is_target = False
                    for j, check_instr in enumerate(instructions):
                        if check_instr.opcode in (Opcode.JUMP, Opcode.JUMP_IF_FALSE, Opcode.JUMP_IF_TRUE):
                            if check_instr.arg == i:
                                is_target = True
                                break
                    if is_target:
                        break
                    i += 1
                    self.changed = True
                continue

            i += 1

        return new_instrs
