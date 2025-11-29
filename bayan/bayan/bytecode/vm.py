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
from ..logical_engine import LogicalEngine


class CallFrame:
    def __init__(self, code, locals_map=None, return_ip=None):
        self.code = code
        self.locals = locals_map or {}
        self.return_ip = return_ip
        self.ip = 0


class BytecodeVM:
    """
    Stack-based virtual machine for Bayan bytecode.
    
    Architecture:
    - Value stack for computation
    - Call stack for function calls
    - Global variables (module level)
    """
    
    def __init__(self, debug_mode=False):
        """Initialize VM"""
        self.stack = []
        self.frames = [] # This will replace call_stack and current_frame conceptually
        self.globals = {}
        self.ip = 0  # Instruction Pointer
        self.running = False
        
        # Debugging
        self.debug_mode = debug_mode
        self.breakpoints = set()  # Set of instruction indices
        self.paused = False
        self.current_code = None # The top-level code object being executed
        
        # Note: The original code had self.logical_engine. This change removes it.
        # If logical_engine is still needed, it should be re-added here.
        self.reset()
        
    def reset(self):
        """Reset VM state"""
        self.stack = []
        self.frames = []
        self.globals = {}
        self.ip = 0
        self.running = False
        self.paused = False
        self.current_code = None
    
    def execute(self, code_object):
        """
        Execute code object.
        
        Args:
            code_object (CodeObject): Code to execute
        
        Returns:
            Result of execution (TOS)
        """
        self.current_code = code_object
        self.running = True
        self.paused = False
        
        # Create initial frame (module level)
        # For PoC, we just use global state + ip
        self.ip = 0
        
        instructions = code_object.instructions
        
        while self.running and self.ip < len(instructions):
            # Check breakpoints
            if self.debug_mode and self.ip in self.breakpoints:
                self.paused = True
                return "PAUSED"
            
            if self.debug_mode and self.paused:
                return "PAUSED"

            instr = instructions[self.ip]
            self.ip += 1
            
            # Execute instruction
            self._execute_instruction(instr)
        
        self.running = False
        
        # Return value at top of stack (if any)
        if self.stack:
            return self.stack[-1]
        return None

    def step(self):
        """Execute single instruction (Debug Mode)"""
        if not self.running or not self.current_code:
            return "NOT_RUNNING"
            
        instructions = self.current_code.instructions
        if self.ip >= len(instructions):
            self.running = False
            return "FINISHED"
            
        instr = instructions[self.ip]
        self.ip += 1
        self._execute_instruction(instr)
        
        if self.ip >= len(instructions):
            self.running = False
            return "FINISHED"
            
        return "STEPPED"

    def resume(self):
        """Resume execution until breakpoint or end"""
        self.paused = False
        return self.execute(self.current_code)

    def get_state(self):
        """Get current VM state for debugger"""
        current_instr = None
        if self.current_code and 0 <= self.ip < len(self.current_code.instructions):
            current_instr = self.current_code.instructions[self.ip]
            
        return {
            'ip': self.ip,
            'stack': [str(x) for x in self.stack],
            'globals': {k: str(v) for k, v in self.globals.items()},
            'running': self.running,
            'paused': self.paused,
            'current_instruction': str(current_instr) if current_instr else None,
            'line_number': current_instr.line_number if current_instr else None
        }

    def set_breakpoint(self, line_number):
        """Set breakpoint at line number"""
        if not self.current_code:
            return False
            
        # Find first instruction at or after line_number
        for i, instr in enumerate(self.current_code.instructions):
            if instr.line_number == line_number:
                self.breakpoints.add(i)
                return True
        return False
        
    def clear_breakpoint(self, line_number):
        """Clear breakpoint at line number"""
        if not self.current_code:
            return False
            
        for i, instr in enumerate(self.current_code.instructions):
            if instr.line_number == line_number:
                self.breakpoints.discard(i)
                return True
        return False
    
    @property
    def locals(self):
        """Get current frame's local variables"""
        # For simple PoC without call frames, use globals
        # If frames are implemented later, use frames[-1].locals
        if self.frames:
            return self.frames[-1].locals if hasattr(self.frames[-1], 'locals') else {}
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
            self.stack.append(self.current_code.constants[arg])
        
        elif opcode == Opcode.LOAD_VAR:
            # Load variable (check locals first, then globals)
            name = self.current_code.names[arg] if isinstance(arg, int) else arg
            if name in self.locals:
                self.stack.append(self.locals[name])
            elif name in self.globals:
                self.stack.append(self.globals[name])
            else:
                raise NameError(f"Variable '{name}' not defined")
        
        elif opcode == Opcode.STORE_VAR:
            # Store to variable
            name = self.current_code.names[arg] if isinstance(arg, int) else arg
            value = self.stack.pop()
            # For module-level code, store in globals
            # For function calls, would store in current frame's locals
            if self.frames:
                self.frames[-1].locals[name] = value
            else:
                self.globals[name] = value
        
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
            saved_code = self.current_code
            saved_instructions = self.current_code.instructions if self.current_code else []
            
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
                
        # ===== Logic Programming =====
        elif opcode == Opcode.ASSERT_FACT:
            # Assert fact or rule: TOS is a Fact or Rule object
            item = self.stack.pop()
            self.logical_engine.assertz(item)
            
        elif opcode == Opcode.QUERY:
            # Query: TOS is a Predicate (goal)
            goal = self.stack.pop()
            solutions = self.logical_engine.query(goal)
            self.stack.append(solutions)
        
        else:
            raise NotImplementedError(f"Opcode {opcode} not implemented yet")
    
    def get_stack(self):
        """Get current stack state (for debugging)"""
        return list(self.stack)
    
    def get_variables(self):
        """Get all variables (for debugging)"""
        return {**self.globals, **self.locals}
