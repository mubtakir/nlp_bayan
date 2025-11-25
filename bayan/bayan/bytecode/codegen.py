"""
Code Generator - AST to Bytecode Compiler
==========================================

Compiles Bayan AST nodes to bytecode instructions.

This is a Proof of Concept focusing on simple expressions and arithmetic.
"""

from ..ast_nodes import *
from .opcodes import Opcode
from .instruction import Instruction, CodeObject


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
    
    def _emit(self, opcode, arg=None):
        """Emit an instruction"""
        instr = Instruction(opcode, arg)
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
    
    def _visit_Literal(self, node):
        """Compile literal value"""
        idx = self._add_constant(node.value)
        self._emit(Opcode.LOAD_CONST, idx)
    
    def _visit_Identifier(self, node):
        """Compile variable load"""
        idx = self._add_name(node.name)
        self._emit(Opcode.LOAD_VAR, idx)
    
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
        }
        
        if node.op in op_map:
            self._emit(op_map[node.op])
        else:
            raise NotImplementedError(f"Binary operator '{node.op}' not supported")
    
    def _visit_UnaryOp(self, node):
        """Compile unary operation"""
        self._visit(node.operand)
        
        if node.op == '-':
            self._emit(Opcode.NEG)
        elif node.op == 'not':
            self._emit(Opcode.NOT)
        else:
            raise NotImplementedError(f"Unary operator '{node.op}' not supported")
    
    def _visit_Assignment(self, node):
        """Compile assignment"""
        # Compile value expression
        self._visit(node.value)
        
        # Store to variable
        idx = self._add_name(node.target)
        self._emit(Opcode.STORE_VAR, idx)
    
    def _visit_FunctionCall(self, node):
        """Compile function call (limited support for PoC)"""
        if node.name == 'print':
            # Special handling for print()
            if node.args:
                self._visit(node.args[0])
            self._emit(Opcode.PRINT)
        else:
            raise NotImplementedError(f"Function '{node.name}' not supported in PoC")
    
    def _visit_ExpressionStatement(self, node):
        """Compile expression statement"""
        self._visit(node.expression)
        # Pop result if not used
        self._emit(Opcode.POP)


def compile_to_bytecode(ast):
    """
    Convenience function to compile AST to bytecode.
    
    Args:
        ast: AST node or list
    
    Returns:
        CodeObject: Compiled bytecode
    """
    generator = CodeGenerator()
    return generator.generate(ast)
