import dis
import types
import sys
from .ast_nodes import *

class BytecodeCompiler:
    """
    Compiles Bayan AST to Python Bytecode.
    This is a Proof-of-Concept implementation.
    """
    def __init__(self):
        self.code_object = None
        self.bytecode = []
        self.consts = [None] # First const is usually None
        self.names = []
        self.varnames = []
        self.stack_size = 0
        self.max_stack_size = 0
        # Jump handling
        self.labels = {}  # label_name -> bytecode offset
        self.jumps = []   # List of (offset, label_name, instruction) for backpatching
        self.label_counter = 0
        
    def compile(self, node, filename="<string>"):
        """Compiles an AST node into a code object."""
        self.bytecode = []
        self.consts = [None]
        self.names = []
        self.varnames = []
        self.stack_size = 0
        self.max_stack_size = 0
        self.labels = {}
        self.jumps = []
        self.label_counter = 0
        
        # Python 3.11+ requires RESUME at the start
        if sys.version_info >= (3, 11):
            self.emit('RESUME', 0)
        
        self.visit(node)
        
        # Add RETURN_VALUE (always return None by default for now)
        self.emit('LOAD_CONST', 0) # Load None
        self.emit('RETURN_VALUE')
        
        # Backpatch all jumps
        self.backpatch_jumps()
        
        # Create code object
        # Python 3.11+ code object creation
        if sys.version_info >= (3, 11):
             # co_argcount, co_posonlyargcount, co_kwonlyargcount, co_nlocals, co_stacksize, co_flags, 
             # co_code, co_consts, co_names, co_varnames, co_filename, co_name, co_qualname, 
             # co_firstlineno, co_linetable, co_exceptiontable, co_freevars, co_cellvars
            code = types.CodeType(
                0, 0, 0, len(self.varnames), self.max_stack_size + 10, 64, # 64 = CO_OPTIMIZED | CO_NEWLOCALS
                bytes(self.bytecode), tuple(self.consts), tuple(self.names), tuple(self.varnames),
                filename, "<module>", "<module>", 1, b'', b'', (), ()
            )
        elif sys.version_info >= (3, 8):
             # Python 3.8 - 3.10
            code = types.CodeType(
                0, 0, 0, len(self.varnames), self.max_stack_size + 5, 64,
                bytes(self.bytecode), tuple(self.consts), tuple(self.names), tuple(self.varnames),
                filename, "<module>", 1, b'', (), ()
            )
        else:
             raise NotImplementedError("Python < 3.8 not supported")
             
        return code

    def emit(self, opname, arg=None):
        """Emit a bytecode instruction."""
        try:
            opcode = dis.opmap[opname]
        except KeyError:
            # Fallback for Python 3.11+ where BINARY_* are merged into BINARY_OP
            if opname.startswith('BINARY_') and 'BINARY_OP' in dis.opmap:
                opcode = dis.opmap['BINARY_OP']
            elif opname == 'CALL_FUNCTION' and 'CALL' in dis.opmap:
                opcode = dis.opmap['CALL']
            else:
                raise

        self.bytecode.append(opcode)
        
        if arg is not None:
            if isinstance(arg, int):
                val = arg
            else:
                val = 0 
            self.bytecode.append(val)
        else:
             self.bytecode.append(0) 

    def create_label(self):
        """Create a new unique label"""
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return label
    
    def mark_label(self, label):
        """Mark the current position with a label"""
        self.labels[label] = len(self.bytecode)
    
    def emit_jump(self, opname, label):
        """Emit a jump instruction with a label (to be backpatched)"""
        try:
            opcode = dis.opmap[opname]
        except KeyError:
            raise ValueError(f"Unknown jump opcode: {opname}")
        
        # Record this jump for backpatching
        jump_offset = len(self.bytecode)
        self.jumps.append((jump_offset, label, opname))
        
        # Emit placeholder
        self.bytecode.append(opcode)
        self.bytecode.append(0)  # Placeholder for jump target
    
    def backpatch_jumps(self):
        """Resolve all jump targets after code generation"""
        for jump_offset, label, opname in self.jumps:
            if label not in self.labels:
                raise ValueError(f"Undefined label: {label}")
            
            target_offset = self.labels[label]
            
            # Calculate relative jump (in code units for 3.11+)
            # In Python 3.11+, jumps are in 2-byte instruction units
            if sys.version_info >= (3, 11):
                # Calculate instruction size including cache
                # Python 3.11+ instructions may have inline cache entries
                opcode = dis.opmap[opname]
                cache_entries = dis._inline_cache_entries[opcode]
                instr_size = 2 + (cache_entries * 2)
                
                # Jump is relative to the next instruction (after cache)
                base_offset = jump_offset + instr_size

                # For forward jumps: target - base
                # For backward jumps: base - target (must be positive)
                if 'BACKWARD' in opname:
                    # JUMP_BACKWARD arg is the number of instructions to jump back
                    delta = (base_offset - target_offset) // 2
                    if delta < 0:
                        raise ValueError(f"JUMP_BACKWARD delta is negative: {delta}")
                else:
                    delta = (target_offset - base_offset) // 2
                    if delta < 0:
                        raise ValueError(f"Forward jump delta is negative: {delta}")
            else:
                # Python 3.8-3.10 uses byte offsets
                if 'BACKWARD' in opname or 'ABSOLUTE' in opname:
                    delta = target_offset
                else:
                    delta = target_offset - (jump_offset + 2)
            
            # Update the placeholder
            if delta < 0 or delta > 255:
                # Need extended arg (not implemented in POC)
                raise NotImplementedError(f"Jump distance {delta} requires EXTENDED_ARG")
            
            self.bytecode[jump_offset + 1] = delta 

    def add_const(self, value):
        if value in self.consts:
            return self.consts.index(value)
        self.consts.append(value)
        return len(self.consts) - 1
        
    def add_name(self, name):
        if name not in self.names:
            self.names.append(name)
        return self.names.index(name)
        
    def add_varname(self, name):
        if name not in self.varnames:
            self.varnames.append(name)
        return self.varnames.index(name)

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise NotImplementedError(f"Compilation not implemented for {type(node).__name__}")

    def visit_Program(self, node):
        for stmt in node.statements:
            self.visit(stmt)
            # If statement is an expression, pop result
            if isinstance(stmt, (BinaryOp, Number, String, Variable)):
                 self.emit('POP_TOP')

    def visit_Block(self, node):
        for stmt in node.statements:
            self.visit(stmt)

    def visit_Number(self, node):
        idx = self.add_const(node.value)
        self.emit('LOAD_CONST', idx)
        
    def visit_String(self, node):
        idx = self.add_const(node.value)
        self.emit('LOAD_CONST', idx)

    def visit_BinaryOp(self, node):
        self.visit(node.left)
        self.visit(node.right)
        
        # Check if it's a comparison operator
        comparison_ops = {'==', '!=', '<', '>', '<=', '>='}
        
        if node.operator in comparison_ops:
            # Use COMPARE_OP
            if sys.version_info >= (3, 12):
                # Python 3.12 COMPARE_OP values
                compare_map_312 = {
                    '<': 2,
                    '<=': 26,
                    '==': 40,
                    '!=': 55,
                    '>': 68,
                    '>=': 92,
                }
                self.emit('COMPARE_OP', compare_map_312[node.operator])
                # COMPARE_OP in 3.12 has 1 CACHE entry (2 bytes)
                self.emit('CACHE', 0)
            elif sys.version_info >= (3, 11):
                # Python 3.11 COMPARE_OP values (same as map below but with cache)
                compare_map = {
                    '<': 0,   # Py_LT
                    '<=': 1,  # Py_LE
                    '==': 2,  # Py_EQ
                    '!=': 3,  # Py_NE
                    '>': 4,   # Py_GT
                    '>=': 5,  # Py_GE
                }
                self.emit('COMPARE_OP', compare_map[node.operator])
                # COMPARE_OP has 1 CACHE in 3.11+
                self.emit('CACHE', 0)
            else:
                # Python 3.10-
                compare_map = {
                    '<': 0,   # Py_LT
                    '<=': 1,  # Py_LE
                    '==': 2,  # Py_EQ
                    '!=': 3,  # Py_NE
                    '>': 4,   # Py_GT
                    '>=': 5,  # Py_GE
                }
                self.emit('COMPARE_OP', compare_map[node.operator])
            return
        
        # Python 3.11+ uses BINARY_OP with an argument indicating the operation
        if sys.version_info >= (3, 11):
            # Indices from dis._nb_ops
            op_map_311 = {
                '+': 0,  # NB_ADD
                '-': 10, # NB_SUBTRACT
                '*': 5,  # NB_MULTIPLY
                '/': 11, # NB_TRUE_DIVIDE
            }
            if node.operator in op_map_311:
                self.emit('BINARY_OP', op_map_311[node.operator])
                # BINARY_OP has 1 CACHE entry (2 bytes)
                self.emit('CACHE', 0)
            else:
                raise NotImplementedError(f"Operator {node.operator} not supported")
        else:
            op_map = {
                '+': 'BINARY_ADD',
                '-': 'BINARY_SUBTRACT',
                '*': 'BINARY_MULTIPLY',
                '/': 'BINARY_TRUE_DIVIDE',
            }
            if node.operator in op_map:
                self.emit(op_map[node.operator])
            else:
                raise NotImplementedError(f"Operator {node.operator} not supported")

    def visit_Assignment(self, node):
        self.visit(node.value)
        # Use add_name for STORE_NAME (module level)
        idx = self.add_name(node.name)
        self.emit('STORE_NAME', idx)
        
    def visit_Variable(self, node):
        # Use LOAD_NAME for module level variables
        idx = self.add_name(node.name)
        self.emit('LOAD_NAME', idx)

    def visit_PrintStatement(self, node):
        idx = self.add_name('print')
        
        if sys.version_info >= (3, 11):
             # Push NULL to support CALL (which expects NULL + Callable + Args)
             # LOAD_GLOBAL arg: index << 1 | 1 (push_null=1)
             # But here we can use LOAD_NAME for print too if it's in builtins
             # However, LOAD_NAME searches locals then globals then builtins.
             # So LOAD_NAME is safe.
             self.emit('LOAD_NAME', idx)
             # LOAD_NAME has no cache? Let's verify.
             # dis output for 'print(x)' showed LOAD_NAME for print.
             # 4 LOAD_NAME 0 (print)
             # 6 LOAD_NAME 1 (x)
             # So LOAD_NAME has no cache.
        else:
             self.emit('LOAD_NAME', idx)
             
        self.visit(node.value)
        
        if sys.version_info >= (3, 11):
            self.emit('CALL', 1)
            # CALL has 3 CACHE entries
            self.emit('CACHE', 0)
            self.emit('CACHE', 0)
            self.emit('CACHE', 0)
        else:
            self.emit('CALL_FUNCTION', 1)
            
        self.emit('POP_TOP') 

    def visit_IfStatement(self, node):
        """Compile if/else statement"""
        # Evaluate condition
        self.visit(node.condition)
        
        # Create labels
        else_label = self.create_label()
        end_label = self.create_label()
        
        # Jump to else if condition is false
        if sys.version_info >= (3, 11):
            self.emit_jump('POP_JUMP_IF_FALSE', else_label)
        else:
            self.emit_jump('POP_JUMP_IF_FALSE', else_label)
        
        # Then branch
        self.visit(node.then_branch)
        
        # Jump to end (skip else)
        if node.else_branch:
            self.emit_jump('JUMP_FORWARD', end_label)
        
        # Else branch
        self.mark_label(else_label)
        if node.else_branch:
            self.visit(node.else_branch)
        
        # End
        self.mark_label(end_label)

    def visit_WhileLoop(self, node):
        """Compile while loop"""
        # Standard While Loop Compilation
        # loop_start:
        #     condition
        #     POP_JUMP_IF_FALSE loop_end
        #     body
        #     JUMP_BACKWARD loop_start
        # loop_end:
        
        # Create labels
        loop_start = self.create_label()
        loop_end = self.create_label()
        
        # Mark loop start
        self.mark_label(loop_start)
        
        # Evaluate condition
        self.visit(node.condition)
        
        # Jump to end if false
        if sys.version_info >= (3, 11):
            self.emit_jump('POP_JUMP_IF_FALSE', loop_end)
        else:
            self.emit_jump('POP_JUMP_IF_FALSE', loop_end)
            
        # Body
        self.visit(node.body)
        
        # Jump back to start
        if sys.version_info >= (3, 11):
            self.emit_jump('JUMP_BACKWARD', loop_start)
        else:
            self.emit_jump('JUMP_ABSOLUTE', loop_start)
            
        # Mark loop end
        self.mark_label(loop_end)

    def visit_ForLoop(self, node):
        """Compile for loop"""
        # Get iterator
        self.visit(node.iterable)
        self.emit('GET_ITER')
        
        # Create labels
        loop_start = self.create_label()
        loop_end = self.create_label()
        
        # Mark loop start
        self.mark_label(loop_start)
        
        # FOR_ITER: get next item or jump to end
        if sys.version_info >= (3, 11):
            self.emit_jump('FOR_ITER', loop_end)
            # FOR_ITER in 3.11+ has 1 CACHE
            self.emit('CACHE', 0)
        else:
            self.emit_jump('FOR_ITER', loop_end)
        
        # Store loop variable
        idx = self.add_name(node.variable)
        self.emit('STORE_NAME', idx)
        
        # Loop body
        self.visit(node.body)
        
        # Jump back to start
        if sys.version_info >= (3, 11):
            self.emit_jump('JUMP_BACKWARD', loop_start)
        else:
            self.emit_jump('JUMP_ABSOLUTE', loop_start)
        
        # Mark loop end
        self.mark_label(loop_end)
        
        # Clean up iterator (FOR_ITER leaves it on stack when done)
        # Actually, FOR_ITER pops the iterator when exhausted in 3.11+
        # But Python 3.12 requires END_FOR to clean up the stack properly
        if 'END_FOR' in dis.opmap:
            self.emit('END_FOR')

    def visit_Boolean(self, node):
        """Compile boolean literal"""
        idx = self.add_const(node.value)
        self.emit('LOAD_CONST', idx)

    def visit_FunctionCall(self, node):
        """Compile function call (basic support for range, etc)"""
        # Load function
        idx = self.add_name(node.name)
        
        if sys.version_info >= (3, 11):
            # LOAD_GLOBAL with push_null for CALL
            self.emit('LOAD_GLOBAL', (idx << 1) | 1)
            self.emit('CACHE', 0)
            self.emit('CACHE', 0)
            self.emit('CACHE', 0)
            self.emit('CACHE', 0)
        else:
            self.emit('LOAD_GLOBAL', idx)
        
        # Load arguments
        for arg in node.arguments:
            self.visit(arg)
        
        # Call
        if sys.version_info >= (3, 11):
            self.emit('CALL', len(node.arguments))
            self.emit('CACHE', 0)
            self.emit('CACHE', 0)
            self.emit('CACHE', 0)
        else:
            self.emit('CALL_FUNCTION', len(node.arguments))
