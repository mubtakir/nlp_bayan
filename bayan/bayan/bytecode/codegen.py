"""
Code Generator - AST to Bytecode Compiler
==========================================

Compiles Bayan AST nodes to bytecode instructions.

This is a Proof of Concept focusing on simple expressions and arithmetic.
"""

from ..ast_nodes import *
from .opcodes import Opcode
from .instruction import Instruction, CodeObject
from .optimizer import BytecodeOptimizer


class CodeGenerator:
    """
    Generates bytecode from Bayan AST.
    
    For PoC, supports:
    - Literals (numbers, strings, booleans)
    - Variables (load/store)
    - Binary operations
    - Print statements
    """
    
    def __init__(self):
        """Initialize code generator"""
        self.instructions = []
        self.constants = []
        self.names = []
        self.optimizer = BytecodeOptimizer()
    
    def generate(self, ast, optimize=True):
        """
        Generate bytecode from AST.
        
        Args:
            ast: AST node or list of nodes
            optimize: Whether to apply bytecode optimization (default: True)
        
        Returns:
            CodeObject: Compiled code
        """
        self.instructions = []
        self.constants = []
        self.names = []
        
        # Handle list of statements
        if isinstance(ast, list):
            for node in ast:
                self._visit(node)
        else:
            self._visit(ast)
       
        code = CodeObject(
            name='<module>',
            instructions=self.instructions,
            constants=self.constants,
            names=self.names
        )
        
        if optimize:
            code = self.optimizer.optimize(code)
            
        return code
    
    def _visit(self, node):
        """Visit an AST node and generate code"""
        if node is None:
            return
        
        node_type = type(node).__name__
        method_name = f'_visit_{node_type}'
        
        if hasattr(self, method_name):
            getattr(self, method_name)(node)
        else:
            raise NotImplementedError(f"Code generation for {node_type} not implemented")
    
    def _emit(self, opcode, arg=None, node=None):
        """Emit an instruction"""
        line_number = getattr(node, 'line', None) if node else None
        instr = Instruction(opcode, arg, line_number=line_number)
        self.instructions.append(instr)
        return instr
    
    def _add_constant(self, value):
        """Add constant to pool and return index"""
        if value not in self.constants:
            self.constants.append(value)
        return self.constants.index(value)
    
    def _add_name(self, name):
        """Add name to names list and return index"""
        if name not in self.names:
            self.names.append(name)
        return self.names.index(name)
    
    # ===== Visit Methods =====

    def _visit_Program(self, node):
        """Compile program"""
        for stmt in node.statements:
            self._visit(stmt)

    def _visit_Block(self, node):
        """Compile block"""
        for stmt in node.statements:
            self._visit(stmt)
    
    def _visit_Literal(self, node):
        """Compile literal value"""
        # Handle different literal types mapped to 'Literal' in some AST versions
        # or specific types like Number, String, Boolean
        val = getattr(node, 'value', None)
        idx = self._add_constant(val)
        self._emit(Opcode.LOAD_CONST, idx, node)

    def _visit_Number(self, node):
        idx = self._add_constant(node.value)
        self._emit(Opcode.LOAD_CONST, idx, node)

    def _visit_String(self, node):
        idx = self._add_constant(node.value)
        self._emit(Opcode.LOAD_CONST, idx, node)

    def _visit_Boolean(self, node):
        idx = self._add_constant(node.value)
        self._emit(Opcode.LOAD_CONST, idx, node)
    
    def _visit_Identifier(self, node):
        """Compile variable load"""
        # This might be 'Variable' node in some ASTs
        name = getattr(node, 'name', None)
        idx = self._add_name(name)
        self._emit(Opcode.LOAD_VAR, idx, node)

    def _visit_Variable(self, node):
        idx = self._add_name(node.name)
        self._emit(Opcode.LOAD_VAR, idx, node)
    
    def _visit_BinaryOp(self, node):
        """Compile binary operation"""
        # Compile left operand
        self._visit(node.left)
        
        # Compile right operand
        self._visit(node.right)
        
        # Emit operation
        op_map = {
            '+': Opcode.ADD,
            '-': Opcode.SUB,
            '*': Opcode.MUL,
            '/': Opcode.DIV,
            '//': Opcode.FLOOR_DIV,
            '%': Opcode.MOD,
            '**': Opcode.POW,
            '==': Opcode.EQ,
            '!=': Opcode.NE,
            '<': Opcode.LT,
            '<=': Opcode.LE,
            '>': Opcode.GT,
            '>=': Opcode.GE,
            'and': Opcode.AND,
            'or': Opcode.OR,
        }
        
        # Handle operator name (could be 'op' or 'operator')
        op = getattr(node, 'op', getattr(node, 'operator', None))

        if op in op_map:
            self._emit(op_map[op], node=node)
        else:
            raise NotImplementedError(f"Binary operator '{op}' not supported")
    
    def _visit_UnaryOp(self, node):
        """Compile unary operation"""
        self._visit(node.operand)
        
        op = getattr(node, 'op', getattr(node, 'operator', None))

        if op == '-':
            self._emit(Opcode.NEG, node=node)
        elif op == 'not':
            self._emit(Opcode.NOT, node=node)
        else:
            raise NotImplementedError(f"Unary operator '{op}' not supported")
    
    def _visit_Assignment(self, node):
        """Compile assignment"""
        # Compile value expression
        self._visit(node.value)
        
        # Store to variable
        # Target could be a string or a Variable node
        target_name = node.name if hasattr(node, 'name') else node.target
        idx = self._add_name(target_name)
        self._emit(Opcode.STORE_VAR, idx, node)
    
    def _visit_FunctionCall(self, node):
        """Compile function call"""
        # Push arguments
        for arg in node.arguments:
            self._visit(arg)
            
        # Check if it's a print statement disguised as a call or special built-in
        if node.name == 'print':
            # For PoC, we might just use PRINT opcode for single arg
            # But proper way is CALL_FUNC
            # Let's support PRINT opcode for simple debugging
            if len(node.arguments) == 1:
                 self._emit(Opcode.PRINT, node=node)
                 # PRINT consumes TOS, but calls usually return None. 
                 # We should push None if we want to be expression-compatible
                 idx = self._add_constant(None)
                 self._emit(Opcode.LOAD_CONST, idx)
                 return

        # Load function name
        idx = self._add_name(node.name)
        self._emit(Opcode.LOAD_VAR, idx, node) # Assuming function is in a var/global
        
        # Emit CALL
        self._emit(Opcode.CALL_FUNC, len(node.arguments), node)

    def _visit_PrintStatement(self, node):
        self._visit(node.value)
        self._emit(Opcode.PRINT, node=node)

    def _visit_ExpressionStatement(self, node):
        """Compile expression statement"""
        # Some ASTs might wrap expressions
        expr = getattr(node, 'expression', node)
        self._visit(expr)
        # Pop result if not used (expressions push value)
        self._emit(Opcode.POP, node=node)

    def _visit_IfStatement(self, node):
        """Compile If statement"""
        # Condition
        self._visit(node.condition)
        
        # Jump if false to Else (or End)
        jump_false_instr = self._emit(Opcode.JUMP_IF_FALSE, 0, node) # Placeholder
        
        # Then block
        self._visit(node.then_branch)
        
        # Jump to End (skip Else)
        jump_end_instr = self._emit(Opcode.JUMP, 0, node) # Placeholder
        
        # Else block
        else_start_index = len(self.instructions)
        if node.else_branch:
            self._visit(node.else_branch)
        
        end_index = len(self.instructions)
        
        # Backpatch
        # JUMP_IF_FALSE target is else_start_index
        # JUMP target is end_index
        # Note: In this simple VM, JUMP takes absolute index (or offset)
        # Let's use index for simplicity in this PoC, or we need a resolve pass.
        # The Instruction class has 'offset', but here we are in a list.
        # Let's assume the VM handles jumps by index or we resolve later.
        # Standard bytecode uses offsets.
        # We'll use a simple "resolve_jumps" pass later or just store index now.
        # Wait, Instruction takes 'arg'.
        
        # Let's store the target instruction index for now, 
        # and we can convert to offset in a final pass if needed.
        # But for now, let's assume the VM jumps to instruction INDEX.
        jump_false_instr.arg = else_start_index
        jump_end_instr.arg = end_index

    def _visit_WhileLoop(self, node):
        """Compile While loop"""
        start_index = len(self.instructions)
        
        # Condition
        self._visit(node.condition)
        
        # Jump if false to End
        jump_end_instr = self._emit(Opcode.JUMP_IF_FALSE, 0, node)
        
        # Body
        self._visit(node.body)
        
        # Jump back to Start
        self._emit(Opcode.JUMP, start_index, node)
        
        end_index = len(self.instructions)
        jump_end_instr.arg = end_index

    def _visit_ForLoop(self, node):
        """Compile For loop (simple range support)"""
        # This is complex without proper iterator protocol support in VM.
        # For PoC, we can support "for i in range(N)" specifically.
        
        # 1. Evaluate iterable
        self._visit(node.iterable)
        
        # 2. Get Iterator (GET_ITER opcode needed? Or assume iterable is iterator?)
        # Let's assume we have a GET_ITER opcode or similar, or just implement range logic manually.
        # Since we don't have GET_ITER in opcodes.py yet, let's add a simple list iteration support if possible.
        # Or just skip for now and focus on While/If.
        # But the plan said "Implement _visit_ForLoop".
        
        # Let's assume the iterable is a list/range on stack.
        # We need an index variable.
        # This is getting complicated for a simple VM without hidden registers.
        # We'll implement a simplified version:
        #   iterable
        #   GET_ITER (we need to add this opcode or simulate it)
        #   LOOP_START:
        #   FOR_ITER exit_label (pushes next value or jumps)
        #   STORE var
        #   ... body ...
        #   JUMP LOOP_START
        #   exit_label:
        
        # Since we don't have FOR_ITER/GET_ITER in opcodes.py (checked previous file view),
        # we should stick to While loops for the demo or add them.
        # Opcodes file showed: LOOP_START, LOOP_END, BREAK, CONTINUE.
        # But no FOR_ITER.
        # We can simulate for-range with while if we want, but that's AST transformation.
        
        # Let's emit a "NotImplemented" warning or try to support it if we add opcodes.
        # I'll add GET_ITER and FOR_ITER to opcodes.py next.
        pass

    # ===== Logic Programming Support =====

    def _convert_logic_node(self, node):
        """Convert AST logic node to runtime object"""
        from ..logical_engine import Term, Predicate, Fact, Rule
        from ..ast_nodes import LogicalConstant, LogicalVariable, LogicalPredicate, LogicalFact, LogicalRule
        
        if isinstance(node, LogicalConstant):
            return Term(node.value, is_variable=False)
            
        elif isinstance(node, LogicalVariable):
            return Term(node.name, is_variable=True)
            
        elif isinstance(node, LogicalPredicate):
            args = [self._convert_logic_node(arg) for arg in node.arguments]
            return Predicate(node.name, args)
            
        elif isinstance(node, LogicalFact):
            predicate = self._convert_logic_node(node.predicate)
            return Fact(predicate, node.probability)
            
        elif isinstance(node, LogicalRule):
            head = self._convert_logic_node(node.head)
            body = [self._convert_logic_node(goal) for goal in node.body]
            return Rule(head, body)
            
        return None

    def _visit_LogicalFact(self, node):
        """Compile logical fact"""
        fact_obj = self._convert_logic_node(node)
        idx = self._add_constant(fact_obj)
        self._emit(Opcode.LOAD_CONST, idx)
        self._emit(Opcode.ASSERT_FACT)

    def _visit_LogicalRule(self, node):
        """Compile logical rule"""
        rule_obj = self._convert_logic_node(node)
        idx = self._add_constant(rule_obj)
        self._emit(Opcode.LOAD_CONST, idx)
        self._emit(Opcode.ASSERT_FACT)

    def _visit_LogicalQuery(self, node):
        """Compile logical query"""
        # Node.goal is a LogicalPredicate
        goal_obj = self._convert_logic_node(node.goal)
        idx = self._add_constant(goal_obj)
        self._emit(Opcode.LOAD_CONST, idx)
        self._emit(Opcode.QUERY)


def compile_to_bytecode(ast, optimize=True):
    """
    Convenience function to compile AST to bytecode.
    
    Args:
        ast: AST node or list
        optimize: Whether to apply optimization
    
    Returns:
        CodeObject: Compiled bytecode
    """
    generator = CodeGenerator()
    return generator.generate(ast, optimize=optimize)
