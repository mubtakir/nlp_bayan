"""
Bytecode Virtual Machine
=========================

Stack-based virtual machine for executing Bayan bytecode.

This is a Proof of Concept implementation focusing on basic operations.
"""

from .opcodes import Opcode
from .instruction import Instruction, CodeObject


class BytecodeVM:
    """
    Stack-based virtual machine for Bayan bytecode.
    
    Architecture:
    - Value stack for computation
    - Global and local variable dictionaries
    - Instruction pointer for execution
    """
    
    def __init__(self):
        """Initialize the VM"""
        self.stack = []              # Value stack
        self.globals = {}            # Global variables
        self.locals = {}             # Local variables (current frame)
        self.ip = 0                  # Instruction pointer
        self.code = None             # Current code object
        self.running = False         # Execution state
        
    def reset(self):
        """Reset VM state"""
        self.stack.clear()
        self.globals.clear()
        self.locals.clear()
        self.ip = 0
        self.running = False
    
    def execute(self, code_object):
        """
        Execute a code object.
        
        Args:
            code_object (CodeObject): Code to execute
        
        Returns:
            Value at top of stack (or None)
        """
        self.code = code_object
        self.ip = 0
        self.running = True
        
        instructions = code_object.instructions
        
        while self.running and self.ip < len(instructions):
            instr = instructions[self.ip]
            self.ip += 1
            
            # Execute instruction
            self._execute_instruction(instr)
        
        # Return value at top of stack (if any)
        if self.stack:
            return self.stack[-1]
        return None
    
    def _execute_instruction(self, instr):
        """Execute a single instruction"""
        opcode = instr.opcode
        arg = instr.arg
        
        # ===== Stack Operations =====
        if opcode == Opcode.NOP:
            pass
        
        elif opcode == Opcode.LOAD_CONST:
            # Push constant from constant pool
            self.stack.append(self.code.constants[arg])
        
        elif opcode == Opcode.LOAD_VAR:
            # Load variable (check locals first, then globals)
            name = self.code.names[arg] if isinstance(arg, int) else arg
            if name in self.locals:
                self.stack.append(self.locals[name])
            elif name in self.globals:
                self.stack.append(self.globals[name])
            else:
                raise NameError(f"Variable '{name}' not defined")
        
        elif opcode == Opcode.STORE_VAR:
            # Store to variable
            name = self.code.names[arg] if isinstance(arg, int) else arg
            value = self.stack.pop()
            self.locals[name] = value
        
        elif opcode == Opcode.POP:
            self.stack.pop()
        
        elif opcode == Opcode.DUP:
            self.stack.append(self.stack[-1])
        
        # ===== Arithmetic Operations =====
        elif opcode == Opcode.ADD:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a + b)
        
        elif opcode == Opcode.SUB:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a - b)
        
        elif opcode == Opcode.MUL:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a * b)
        
        elif opcode == Opcode.DIV:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a / b)
        
        elif opcode == Opcode.FLOOR_DIV:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a // b)
        
        elif opcode == Opcode.MOD:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a % b)
        
        elif opcode == Opcode.POW:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a ** b)
        
        elif opcode == Opcode.NEG:
            a = self.stack.pop()
            self.stack.append(-a)
        
        elif opcode == Opcode.NOT:
            a = self.stack.pop()
            self.stack.append(not a)
        
        # ===== Comparison Operations =====
        elif opcode == Opcode.EQ:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a == b)
        
        elif opcode == Opcode.NE:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a != b)
        
        elif opcode == Opcode.LT:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a < b)
        
        elif opcode == Opcode.LE:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a <= b)
        
        elif opcode == Opcode.GT:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a > b)
        
        elif opcode == Opcode.GE:
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a >= b)
        
        # ===== Control Flow =====
        elif opcode == Opcode.JUMP:
            # Unconditional jump to target instruction
            self.ip = arg
        
        elif opcode == Opcode.JUMP_IF_TRUE:
            # Jump if TOS is truthy
            condition = self.stack.pop()
            if condition:
                self.ip = arg
        
        elif opcode == Opcode.JUMP_IF_FALSE:
            # Jump if TOS is falsy
            condition = self.stack.pop()
            if not condition:
                self.ip = arg
        
        # ===== Special =====
        elif opcode == Opcode.PRINT:
            # Print top of stack (for debugging)
            value = self.stack.pop()
            print(value)
        
        elif opcode == Opcode.RETURN:
            # Return from function (stop execution for PoC)
            self.running = False
        
        else:
            raise NotImplementedError(f"Opcode {opcode} not implemented yet")
    
    def get_stack(self):
        """Get current stack state (for debugging)"""
        return list(self.stack)
    
    def get_variables(self):
        """Get all variables (for debugging)"""
        return {**self.globals, **self.locals}
