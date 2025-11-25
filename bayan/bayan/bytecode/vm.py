"""
Bytecode Virtual Machine
=========================

Stack-based virtual machine for executing Bayan bytecode.

Supports:
- Basic operations (Phase 1)
- Control flow (Phase 2)  
- Functions (Phase 3)
"""

from .opcodes import Opcode
from .instruction import Instruction, CodeObject


class CallFrame:
    """
    Represents a function call frame.
    
    Contains:
    - Code object being executed
    - Local variables for this frame
    - Return address (instruction pointer to return to)
    """
    
    def __init__(self, code_object, return_ip=None, locals=None):
        self.code = code_object
        self.locals = locals or {}
        self.return_ip = return_ip
        self.ip = 0  # Instruction pointer within this frame
    
    def __repr__(self):
        return f"CallFrame({self.code.name}, ip={self.ip})"


class BytecodeVM:
    """
    Stack-based virtual machine for Bayan bytecode.
    
    Architecture:
    - Value stack for computation
    - Call stack for function calls
    - Global variables (module level)
    """
    
    def __init__(self):
        """Initialize the VM"""
        self.stack = []              # Value stack
        self.globals = {}            # Global variables
        self.call_stack = []         # Call frames
        self.current_frame = None    # Current execution frame
        self.ip = 0                  # Instruction pointer (in current frame)
        self.code = None             # Current code object
        self.running = False         # Execution state
        
    def reset(self):
        """Reset VM state"""
        self.stack.clear()
        self.globals.clear()
        self.call_stack.clear()
        self.current_frame = None
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
        # Create initial frame
        self.current_frame = CallFrame(code_object)
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
    
    @property
    def locals(self):
        """Get current frame's local variables"""
        if self.current_frame:
            return self.current_frame.locals
        return {}
    
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
        
        # ===== Function Operations =====
        elif opcode == Opcode.CALL_FUNC:
            # Call function with N arguments
            # Stack: [..., func, arg1, arg2, ..., argN]
            nargs = arg
            
            # Pop arguments
            args = []
            for _ in range(nargs):
                args.insert(0, self.stack.pop())
            
            # Pop function object (code object)
            func_code = self.stack.pop()
            
            if not isinstance(func_code, CodeObject):
                raise TypeError(f"Expected CodeObject, got {type(func_code)}")
            
            # Save current state
            saved_ip = self.ip
            saved_code = self.code
            saved_instructions = self.code.instructions if self.code else []
            
            # Create new frame
            new_frame = CallFrame(func_code, return_ip=saved_ip, locals={})
            
            # Set up arguments as local variables (simple approach: arg0, arg1, ...)
            for i, arg_val in enumerate(args):
                new_frame.locals[f'arg{i}'] = arg_val
            
            # Push frame to call stack
            self.call_stack.append(self.current_frame)
            self.current_frame = new_frame
            
            # Execute function
            self.code = func_code
            self.ip = 0
            
            # Run until RETURN
            while self.ip < len(func_code.instructions):
                instr = func_code.instructions[self.ip]
                self.ip += 1
                
                if instr.opcode == Opcode.RETURN:
                    # Function finished, restore state
                    break
                    
                self._execute_instruction(instr)
            
            # Restore previous frame
            self.current_frame = self.call_stack.pop() if self.call_stack else None
            self.code = saved_code
            self.ip = saved_ip
        
        # ===== Special =====
        elif opcode == Opcode.PRINT:
            # Print top of stack (for debugging)
            value = self.stack.pop()
            print(value)
        
        elif opcode == Opcode.RETURN:
            # Return from function
            # TOS should contain return value (if any)
            # In nested calls, this will be handled by CALL_FUNC
            # In top-level, it just stops execution
            if not self.call_stack:
                # Top-level return, stop execution
                self.running = False
        
        else:
            raise NotImplementedError(f"Opcode {opcode} not implemented yet")
    
    def get_stack(self):
        """Get current stack state (for debugging)"""
        return list(self.stack)
    
    def get_variables(self):
        """Get all variables (for debugging)"""
        return {**self.globals, **self.locals}
