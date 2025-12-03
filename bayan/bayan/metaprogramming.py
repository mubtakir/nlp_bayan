"""
Bayan Metaprogramming Module
وحدة البرمجة الوصفية للغة بيان

This module provides metaprogramming capabilities for self-modifying code:
- eval/قيّم: Evaluate expressions dynamically
- exec/نفّذ: Execute code dynamically  
- compile/ترجم: Compile code to AST
- source_code/كود_المصدر: Get source code of functions
- modify_function/عدّل_دالة: Modify existing functions
- create_function/أنشئ_دالة: Create new functions dynamically
- introspect/تأمل: Inspect code structure

Author: Bayan Development Team
"""

import inspect
import textwrap
from typing import Any, Dict, List, Optional, Callable, Union
from dataclasses import dataclass


@dataclass
class CompiledCode:
    """Represents compiled Bayan code
    يمثل كود بيان مترجم
    """
    source: str
    ast: Any
    filename: str = "<dynamic>"
    
    def __repr__(self):
        lines = self.source.count('\n') + 1
        return f"<CompiledCode: {lines} lines from '{self.filename}'>"


@dataclass 
class FunctionInfo:
    """Information about a function
    معلومات عن دالة
    """
    name: str
    parameters: List[str]
    source: Optional[str]
    ast_node: Any
    is_generator: bool = False
    is_async: bool = False
    decorators: List[str] = None
    
    def __post_init__(self):
        if self.decorators is None:
            self.decorators = []


class MetaprogrammingEngine:
    """
    Engine for metaprogramming operations
    محرك عمليات البرمجة الوصفية
    """
    
    def __init__(self, interpreter=None):
        self.interpreter = interpreter
        self._compiled_cache: Dict[str, CompiledCode] = {}
        self._function_sources: Dict[str, str] = {}
        
    def set_interpreter(self, interpreter):
        """Set the interpreter reference"""
        self.interpreter = interpreter
        
    def eval(self, expression: str, local_vars: Dict = None) -> Any:
        """
        Evaluate a Bayan expression and return its value.
        تقييم تعبير بيان وإرجاع قيمته.
        
        Args:
            expression: The expression to evaluate (string)
            local_vars: Optional local variables dict
            
        Returns:
            The result of evaluating the expression
            
        Example:
            >>> engine.eval("1 + 2 * 3")
            7
            >>> engine.eval("x + y", {"x": 10, "y": 5})
            15
        """
        if self.interpreter is None:
            raise RuntimeError("Interpreter not set / المفسر غير محدد")
            
        from .lexer import HybridLexer
        from .parser import HybridParser
        
        # Parse as expression
        lexer = HybridLexer(expression)
        tokens = lexer.tokenize()
        parser = HybridParser(tokens)
        
        # Try to parse as single expression
        try:
            ast = parser.parse_expression()
        except:
            # Fallback: wrap in program and extract result
            lexer = HybridLexer(expression)
            tokens = lexer.tokenize()
            parser = HybridParser(tokens)
            ast = parser.parse()
        
        # Set up local variables if provided
        old_local = self.interpreter.local_env
        if local_vars:
            if self.interpreter.local_env is None:
                self.interpreter.local_env = {}
            self.interpreter.local_env.update(local_vars)
        
        try:
            result = self.interpreter.interpret(ast)
            return result
        finally:
            self.interpreter.local_env = old_local
            
    def exec(self, code: str, local_vars: Dict = None, 
             filename: str = "<exec>") -> Any:
        """
        Execute Bayan code dynamically.
        تنفيذ كود بيان ديناميكياً.
        
        Args:
            code: The code to execute (string)
            local_vars: Optional local variables dict
            filename: Optional filename for error messages
            
        Returns:
            The result of the last statement
            
        Example:
            >>> engine.exec("x = 5\\ny = x * 2\\nprint(y)")
            10
        """
        if self.interpreter is None:
            raise RuntimeError("Interpreter not set / المفسر غير محدد")
            
        from .lexer import HybridLexer
        from .parser import HybridParser
        
        lexer = HybridLexer(code)
        tokens = lexer.tokenize()
        parser = HybridParser(tokens)
        ast = parser.parse()
        
        # Set up local variables if provided
        old_local = self.interpreter.local_env
        if local_vars:
            if self.interpreter.local_env is None:
                self.interpreter.local_env = {}
            self.interpreter.local_env.update(local_vars)
        
        try:
            result = self.interpreter.interpret(ast)
            return result
        finally:
            self.interpreter.local_env = old_local

    def compile(self, code: str, filename: str = "<compile>") -> CompiledCode:
        """
        Compile Bayan code to AST without executing.
        ترجمة كود بيان إلى AST بدون تنفيذ.

        Args:
            code: The code to compile
            filename: Optional filename for error messages

        Returns:
            CompiledCode object that can be executed later
        """
        from .lexer import HybridLexer
        from .parser import HybridParser

        lexer = HybridLexer(code)
        tokens = lexer.tokenize()
        parser = HybridParser(tokens)
        ast = parser.parse()

        compiled = CompiledCode(source=code, ast=ast, filename=filename)
        cache_key = f"{filename}:{hash(code)}"
        self._compiled_cache[cache_key] = compiled

        return compiled

    def exec_compiled(self, compiled: CompiledCode,
                      local_vars: Dict = None) -> Any:
        """Execute pre-compiled code. تنفيذ كود مترجم مسبقاً."""
        if self.interpreter is None:
            raise RuntimeError("Interpreter not set / المفسر غير محدد")

        old_local = self.interpreter.local_env
        if local_vars:
            if self.interpreter.local_env is None:
                self.interpreter.local_env = {}
            self.interpreter.local_env.update(local_vars)

        try:
            return self.interpreter.interpret(compiled.ast)
        finally:
            self.interpreter.local_env = old_local

    def get_function_info(self, func_name: str) -> Optional[FunctionInfo]:
        """Get information about a function. الحصول على معلومات عن دالة."""
        if self.interpreter is None:
            return None

        func_def = self.interpreter.functions.get(func_name)
        if func_def is None:
            return None

        params = []
        if hasattr(func_def, 'parameters'):
            for p in func_def.parameters:
                params.append(p.name if hasattr(p, 'name') else str(p))

        is_gen = hasattr(func_def, 'is_generator') and func_def.is_generator
        is_async = hasattr(func_def, 'is_async') and func_def.is_async

        decorators = []
        if hasattr(func_def, 'decorators'):
            for d in func_def.decorators:
                if hasattr(d, 'name'):
                    decorators.append(d.name)

        source = self._function_sources.get(func_name)

        return FunctionInfo(
            name=func_name, parameters=params, source=source,
            ast_node=func_def, is_generator=is_gen, is_async=is_async,
            decorators=decorators
        )

    def create_function(self, name: str, params: List[str],
                        body: str, decorators: List[str] = None) -> Any:
        """
        Create a new function dynamically.
        إنشاء دالة جديدة ديناميكياً.

        Args:
            name: Function name
            params: List of parameter names
            body: Function body code
            decorators: Optional list of decorator names

        Returns:
            The created function
        """
        dec_str = ""
        if decorators:
            dec_str = "\n".join(f"@{d}" for d in decorators) + "\n"

        params_str = ", ".join(params)
        body_lines = body.strip().split('\n')
        indented_body = "\n".join("    " + line for line in body_lines)

        func_code = f"{dec_str}def {name}({params_str}): {{\n{indented_body}\n}}"
        self._function_sources[name] = func_code
        self.exec(func_code)

        if self.interpreter:
            return self.interpreter.functions.get(name) or \
                   self.interpreter.global_env.get(name)
        return None

    def modify_function(self, name: str, new_body: str = None,
                        new_params: List[str] = None) -> Any:
        """
        Modify an existing function.
        تعديل دالة موجودة.
        """
        info = self.get_function_info(name)
        if info is None:
            raise NameError(f"Function '{name}' not found / الدالة '{name}' غير موجودة")

        params = new_params if new_params is not None else info.parameters
        body = new_body if new_body is not None else "pass"

        return self.create_function(name, params, body, info.decorators)

    def delete_function(self, name: str) -> bool:
        """Delete a function. حذف دالة."""
        if self.interpreter is None:
            return False

        deleted = False
        if name in self.interpreter.functions:
            del self.interpreter.functions[name]
            deleted = True
        if name in self.interpreter.global_env:
            del self.interpreter.global_env[name]
            deleted = True
        if name in self._function_sources:
            del self._function_sources[name]

        return deleted

    def list_functions(self) -> List[str]:
        """List all defined functions. قائمة بجميع الدوال المعرفة."""
        if self.interpreter is None:
            return []
        return list(self.interpreter.functions.keys())

    def introspect(self, obj: Any) -> Dict[str, Any]:
        """
        Introspect an object and return its structure.
        تأمل كائن وإرجاع بنيته.
        """
        result = {
            'type': type(obj).__name__,
            'type_ar': self._get_arabic_type(type(obj).__name__),
        }

        if callable(obj):
            result['callable'] = True
            if hasattr(obj, '__name__'):
                result['name'] = obj.__name__

        if hasattr(obj, '__dict__'):
            result['attributes'] = list(obj.__dict__.keys())

        if hasattr(obj, '__doc__') and obj.__doc__:
            result['doc'] = obj.__doc__

        return result

    def _get_arabic_type(self, type_name: str) -> str:
        """Get Arabic name for type."""
        types_ar = {
            'int': 'عدد_صحيح', 'float': 'عدد_عشري', 'str': 'نص',
            'list': 'قائمة', 'dict': 'قاموس', 'bool': 'منطقي',
            'function': 'دالة', 'NoneType': 'فارغ', 'tuple': 'صف',
            'set': 'مجموعة', 'FunctionInfo': 'معلومات_دالة',
            'CompiledCode': 'كود_مترجم'
        }
        return types_ar.get(type_name, type_name)


# Global engine instance
_global_engine: Optional[MetaprogrammingEngine] = None

def get_engine() -> MetaprogrammingEngine:
    """Get the global metaprogramming engine."""
    global _global_engine
    if _global_engine is None:
        _global_engine = MetaprogrammingEngine()
    return _global_engine

def set_interpreter(interpreter):
    """Set interpreter for global engine."""
    get_engine().set_interpreter(interpreter)
