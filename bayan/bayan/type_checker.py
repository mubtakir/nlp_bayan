"""
Type Checker for Bayan Language
محلل الأنواع للغة بيان

This module provides static type checking capabilities for Bayan programs.
يوفر هذا الوحدة إمكانيات فحص الأنواع الثابتة لبرامج بيان.
"""

from .ast_nodes import *
from .lexer import TokenType


class BayanType:
    """Base class for all Bayan types"""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"BayanType({self.name})"

    def __eq__(self, other):
        if isinstance(other, BayanType):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

    def is_compatible_with(self, other):
        """Check if this type is compatible with another type"""
        if self == other:
            return True
        if isinstance(other, AnyType):
            return True
        if isinstance(self, AnyType):
            return True
        return False


class PrimitiveType(BayanType):
    """Primitive types: int, float, str, bool"""
    pass


class AnyType(BayanType):
    """Any type - compatible with all types"""
    def __init__(self):
        super().__init__("Any")

    def is_compatible_with(self, other):
        return True


class NoneType(BayanType):
    """None type"""
    def __init__(self):
        super().__init__("None")


class GenericTypeInstance(BayanType):
    """Generic type instance: List[int], Dict[str, int]"""
    def __init__(self, base_type, type_args):
        super().__init__(f"{base_type.name}[{', '.join(str(t) for t in type_args)}]")
        self.base_type = base_type
        self.type_args = type_args

    def is_compatible_with(self, other):
        if isinstance(other, AnyType):
            return True
        if isinstance(other, GenericTypeInstance):
            if self.base_type != other.base_type:
                return False
            if len(self.type_args) != len(other.type_args):
                return False
            return all(a.is_compatible_with(b) for a, b in zip(self.type_args, other.type_args))
        return False


class UnionTypeInstance(BayanType):
    """Union type: int | str"""
    def __init__(self, types):
        super().__init__(" | ".join(t.name for t in types))
        self.types = types

    def is_compatible_with(self, other):
        if isinstance(other, AnyType):
            return True
        if isinstance(other, UnionTypeInstance):
            return all(any(t1.is_compatible_with(t2) for t2 in other.types) for t1 in self.types)
        return any(t.is_compatible_with(other) for t in self.types)


class OptionalTypeInstance(BayanType):
    """Optional type: Optional[int] or int?"""
    def __init__(self, inner_type):
        super().__init__(f"Optional[{inner_type.name}]")
        self.inner_type = inner_type

    def is_compatible_with(self, other):
        if isinstance(other, AnyType):
            return True
        if isinstance(other, NoneType):
            return True
        if isinstance(other, OptionalTypeInstance):
            return self.inner_type.is_compatible_with(other.inner_type)
        return self.inner_type.is_compatible_with(other)


class CallableTypeInstance(BayanType):
    """Callable type: Callable[[int, str], bool]"""
    def __init__(self, param_types, return_type):
        params_str = ", ".join(t.name for t in param_types)
        super().__init__(f"Callable[({params_str}) -> {return_type.name}]")
        self.param_types = param_types
        self.return_type = return_type


class FunctionType(BayanType):
    """Function type with parameter and return types"""
    def __init__(self, name, param_types, return_type):
        super().__init__(f"Function[{name}]")
        self.func_name = name
        self.param_types = param_types
        self.return_type = return_type


class ClassType(BayanType):
    """Class type"""
    def __init__(self, name, parent=None, methods=None, attributes=None):
        super().__init__(name)
        self.parent = parent
        self.methods = methods or {}
        self.attributes = attributes or {}

    def is_compatible_with(self, other):
        if super().is_compatible_with(other):
            return True
        # Check inheritance
        if self.parent and self.parent.is_compatible_with(other):
            return True
        return False


class EnumType(BayanType):
    """Enum type"""
    def __init__(self, name, members):
        super().__init__(name)
        self.members = members


class InterfaceType(BayanType):
    """Interface type"""
    def __init__(self, name, methods, extends=None):
        super().__init__(name)
        self.methods = methods
        self.extends = extends or []


# Built-in types
INT_TYPE = PrimitiveType("int")
FLOAT_TYPE = PrimitiveType("float")
STR_TYPE = PrimitiveType("str")
BOOL_TYPE = PrimitiveType("bool")
ANY_TYPE = AnyType()
NONE_TYPE = NoneType()
LIST_TYPE = PrimitiveType("list")
DICT_TYPE = PrimitiveType("dict")
SET_TYPE = PrimitiveType("set")
TUPLE_TYPE = PrimitiveType("tuple")


class TypeEnvironment:
    """Type environment for tracking variable and function types"""
    def __init__(self, parent=None):
        self.parent = parent
        self.variables = {}
        self.functions = {}
        self.classes = {}
        self.enums = {}
        self.interfaces = {}

    def define_variable(self, name, type_):
        self.variables[name] = type_

    def lookup_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        if self.parent:
            return self.parent.lookup_variable(name)
        return None

    def define_function(self, name, func_type):
        self.functions[name] = func_type

    def lookup_function(self, name):
        if name in self.functions:
            return self.functions[name]
        if self.parent:
            return self.parent.lookup_function(name)
        return None

    def define_class(self, name, class_type):
        self.classes[name] = class_type

    def lookup_class(self, name):
        if name in self.classes:
            return self.classes[name]
        if self.parent:
            return self.parent.lookup_class(name)
        return None

    def child_scope(self):
        return TypeEnvironment(parent=self)


class TypeChecker:
    """Type checker for Bayan programs"""

    def __init__(self):
        self.env = TypeEnvironment()
        self.errors = []
        self.warnings = []
        self._init_builtins()

    def _init_builtins(self):
        """Initialize built-in functions and types"""
        # Built-in functions
        self.env.define_function("print", FunctionType("print", [ANY_TYPE], NONE_TYPE))
        self.env.define_function("len", FunctionType("len", [ANY_TYPE], INT_TYPE))
        self.env.define_function("str", FunctionType("str", [ANY_TYPE], STR_TYPE))
        self.env.define_function("int", FunctionType("int", [ANY_TYPE], INT_TYPE))
        self.env.define_function("float", FunctionType("float", [ANY_TYPE], FLOAT_TYPE))
        self.env.define_function("bool", FunctionType("bool", [ANY_TYPE], BOOL_TYPE))
        self.env.define_function("range", FunctionType("range", [INT_TYPE], GenericTypeInstance(LIST_TYPE, [INT_TYPE])))
        self.env.define_function("sum", FunctionType("sum", [GenericTypeInstance(LIST_TYPE, [INT_TYPE])], INT_TYPE))
        self.env.define_function("min", FunctionType("min", [ANY_TYPE], ANY_TYPE))
        self.env.define_function("max", FunctionType("max", [ANY_TYPE], ANY_TYPE))
        self.env.define_function("abs", FunctionType("abs", [INT_TYPE], INT_TYPE))
        self.env.define_function("input", FunctionType("input", [STR_TYPE], STR_TYPE))
        self.env.define_function("type", FunctionType("type", [ANY_TYPE], STR_TYPE))

    def check(self, program):
        """Check types in a program"""
        self.errors = []
        self.warnings = []
        for stmt in program.statements:
            self._check_statement(stmt)
        return self.errors, self.warnings

    def _error(self, message, node=None):
        line = getattr(node, 'line', '?') if node else '?'
        self.errors.append(f"Type Error (line {line}): {message}")

    def _warning(self, message, node=None):
        line = getattr(node, 'line', '?') if node else '?'
        self.warnings.append(f"Type Warning (line {line}): {message}")

    def _resolve_type_annotation(self, annotation):
        """Convert TypeAnnotation AST node to BayanType"""
        if annotation is None:
            return ANY_TYPE

        if isinstance(annotation, TypeAnnotation):
            base = annotation.base_type.lower()
            type_map = {
                'int': INT_TYPE, 'صحيح': INT_TYPE, 'عدد_صحيح': INT_TYPE,
                'float': FLOAT_TYPE, 'عشري': FLOAT_TYPE, 'عدد_عشري': FLOAT_TYPE,
                'str': STR_TYPE, 'نص': STR_TYPE, 'سلسلة': STR_TYPE,
                'bool': BOOL_TYPE, 'منطقي': BOOL_TYPE,
                'list': LIST_TYPE, 'قائمة': LIST_TYPE,
                'dict': DICT_TYPE, 'قاموس': DICT_TYPE,
                'set': SET_TYPE, 'مجموعة': SET_TYPE,
                'tuple': TUPLE_TYPE, 'صف': TUPLE_TYPE,
                'any': ANY_TYPE, 'أي': ANY_TYPE,
                'none': NONE_TYPE, 'لاشيء': NONE_TYPE,
                'self': ANY_TYPE, 'ذاتي': ANY_TYPE,
            }
            base_type = type_map.get(base)
            if base_type is None:
                # Could be a class or custom type
                class_type = self.env.lookup_class(annotation.base_type)
                if class_type:
                    return class_type
                return ANY_TYPE

            if annotation.type_params:
                type_args = [self._resolve_type_annotation(p) for p in annotation.type_params]
                return GenericTypeInstance(base_type, type_args)
            return base_type

        if isinstance(annotation, UnionType):
            types = [self._resolve_type_annotation(t) for t in annotation.types]
            return UnionTypeInstance(types)

        if isinstance(annotation, OptionalType):
            inner = self._resolve_type_annotation(annotation.inner_type)
            return OptionalTypeInstance(inner)

        return ANY_TYPE

    def _check_statement(self, stmt):
        """Check types in a statement"""
        if isinstance(stmt, FunctionDef):
            self._check_function_def(stmt)
        elif isinstance(stmt, ClassDef):
            self._check_class_def(stmt)
        elif isinstance(stmt, Assignment):
            self._check_assignment(stmt)
        elif isinstance(stmt, TypedVariable):
            self._check_typed_variable(stmt)
        elif isinstance(stmt, IfStatement):
            self._check_if_statement(stmt)
        elif isinstance(stmt, ForLoop):
            self._check_for_loop(stmt)
        elif isinstance(stmt, WhileLoop):
            self._check_while_loop(stmt)
        elif isinstance(stmt, ReturnStatement):
            self._check_return_statement(stmt)
        elif isinstance(stmt, EnumDef):
            self._check_enum_def(stmt)
        elif isinstance(stmt, InterfaceDef):
            self._check_interface_def(stmt)
        elif isinstance(stmt, Block):
            for s in stmt.statements:
                self._check_statement(s)
        # Skip other statement types silently

    def _check_function_def(self, func):
        """Check types in a function definition"""
        # Get return type
        return_type = self._resolve_type_annotation(getattr(func, 'return_type', None))

        # Get parameter types
        param_types = []
        for param in func.parameters:
            param_type = self._resolve_type_annotation(getattr(param, 'type_annotation', None))
            param_types.append(param_type)

        # Register function
        func_type = FunctionType(func.name, param_types, return_type)
        self.env.define_function(func.name, func_type)

        # Check body in new scope
        old_env = self.env
        self.env = self.env.child_scope()

        # Add parameters to scope
        for i, param in enumerate(func.parameters):
            self.env.define_variable(param.name, param_types[i])

        # Check body
        if isinstance(func.body, Block):
            for stmt in func.body.statements:
                self._check_statement(stmt)

        self.env = old_env

    def _check_class_def(self, cls):
        """Check types in a class definition"""
        parent_type = None
        if cls.parent:
            parent_type = self.env.lookup_class(cls.parent)

        class_type = ClassType(cls.name, parent_type)
        self.env.define_class(cls.name, class_type)

        # Check methods
        old_env = self.env
        self.env = self.env.child_scope()
        self.env.define_variable("self", class_type)

        if isinstance(cls.body, Block):
            for stmt in cls.body.statements:
                self._check_statement(stmt)

        self.env = old_env

    def _check_typed_variable(self, typed_var):
        """Check types in a typed variable declaration"""
        declared_type = self._resolve_type_annotation(typed_var.type_annotation)
        self.env.define_variable(typed_var.name, declared_type)

        if typed_var.value:
            value_type = self._infer_type(typed_var.value)
            if not value_type.is_compatible_with(declared_type):
                self._error(f"Cannot assign {value_type.name} to variable '{typed_var.name}' of type {declared_type.name}", typed_var)

    def _check_assignment(self, assign):
        """Check types in an assignment"""
        value_type = self._infer_type(assign.value)

        # Assignment has 'name' attribute (string) not 'target'
        name = assign.name
        if isinstance(name, str):
            existing_type = self.env.lookup_variable(name)
            if existing_type and not value_type.is_compatible_with(existing_type):
                self._warning(f"Variable '{name}' was {existing_type.name}, now assigned {value_type.name}", assign)
            self.env.define_variable(name, value_type)
        elif isinstance(name, Variable):
            existing_type = self.env.lookup_variable(name.name)
            if existing_type and not value_type.is_compatible_with(existing_type):
                self._warning(f"Variable '{name.name}' was {existing_type.name}, now assigned {value_type.name}", assign)
            self.env.define_variable(name.name, value_type)

    def _check_if_statement(self, stmt):
        """Check types in an if statement"""
        cond_type = self._infer_type(stmt.condition)
        if not cond_type.is_compatible_with(BOOL_TYPE) and not isinstance(cond_type, AnyType):
            self._warning(f"Condition should be bool, got {cond_type.name}", stmt)

        if isinstance(stmt.then_block, Block):
            for s in stmt.then_block.statements:
                self._check_statement(s)

        if stmt.else_block:
            if isinstance(stmt.else_block, Block):
                for s in stmt.else_block.statements:
                    self._check_statement(s)
            else:
                self._check_statement(stmt.else_block)

    def _check_for_loop(self, stmt):
        """Check types in a for loop"""
        iterable_type = self._infer_type(stmt.iterable)

        old_env = self.env
        self.env = self.env.child_scope()

        # Infer loop variable type from iterable
        if isinstance(iterable_type, GenericTypeInstance):
            self.env.define_variable(stmt.variable, iterable_type.type_args[0] if iterable_type.type_args else ANY_TYPE)
        else:
            self.env.define_variable(stmt.variable, ANY_TYPE)

        if isinstance(stmt.body, Block):
            for s in stmt.body.statements:
                self._check_statement(s)

        self.env = old_env

    def _check_while_loop(self, stmt):
        """Check types in a while loop"""
        cond_type = self._infer_type(stmt.condition)
        if not cond_type.is_compatible_with(BOOL_TYPE) and not isinstance(cond_type, AnyType):
            self._warning(f"Condition should be bool, got {cond_type.name}", stmt)

        if isinstance(stmt.body, Block):
            for s in stmt.body.statements:
                self._check_statement(s)

    def _check_return_statement(self, stmt):
        """Check types in a return statement"""
        if stmt.value:
            self._infer_type(stmt.value)

    def _check_enum_def(self, enum):
        """Check types in an enum definition"""
        members = {name: value for name, value in enum.members}
        enum_type = EnumType(enum.name, members)
        self.env.define_class(enum.name, enum_type)

    def _check_interface_def(self, interface):
        """Check types in an interface definition"""
        methods = {}
        for method in interface.methods:
            param_types = [self._resolve_type_annotation(t) for _, t in method.params]
            return_type = self._resolve_type_annotation(method.return_type)
            methods[method.name] = FunctionType(method.name, param_types, return_type)

        interface_type = InterfaceType(interface.name, methods, interface.extends)
        self.env.define_class(interface.name, interface_type)

    def _infer_type(self, expr):
        """Infer the type of an expression"""
        if expr is None:
            return NONE_TYPE

        if isinstance(expr, Number):
            if '.' in str(expr.value):
                return FLOAT_TYPE
            return INT_TYPE

        if isinstance(expr, String):
            return STR_TYPE

        if isinstance(expr, Boolean):
            return BOOL_TYPE

        if isinstance(expr, NoneLiteral):
            return NONE_TYPE

        if isinstance(expr, Variable):
            var_type = self.env.lookup_variable(expr.name)
            if var_type:
                return var_type
            return ANY_TYPE

        if isinstance(expr, List):
            if expr.elements:
                elem_type = self._infer_type(expr.elements[0])
                return GenericTypeInstance(LIST_TYPE, [elem_type])
            return GenericTypeInstance(LIST_TYPE, [ANY_TYPE])

        if isinstance(expr, Dict):
            if expr.pairs:
                key_type = self._infer_type(expr.pairs[0][0])
                val_type = self._infer_type(expr.pairs[0][1])
                return GenericTypeInstance(DICT_TYPE, [key_type, val_type])
            return GenericTypeInstance(DICT_TYPE, [ANY_TYPE, ANY_TYPE])

        if isinstance(expr, BinaryOp):
            left_type = self._infer_type(expr.left)
            right_type = self._infer_type(expr.right)

            if expr.operator in ('+', '-', '*', '/', '//', '%', '**'):
                if left_type == FLOAT_TYPE or right_type == FLOAT_TYPE:
                    return FLOAT_TYPE
                if left_type == INT_TYPE and right_type == INT_TYPE:
                    return INT_TYPE
                if left_type == STR_TYPE and expr.operator == '+':
                    return STR_TYPE
                return ANY_TYPE

            if expr.operator in ('==', '!=', '<', '>', '<=', '>=', 'and', 'or', 'in', 'not in'):
                return BOOL_TYPE

            return ANY_TYPE

        if isinstance(expr, UnaryOp):
            operand_type = self._infer_type(expr.operand)
            if expr.operator == 'not':
                return BOOL_TYPE
            if expr.operator == '-':
                return operand_type
            return ANY_TYPE

        if isinstance(expr, FunctionCall):
            func_type = self.env.lookup_function(expr.name)
            if func_type:
                return func_type.return_type
            return ANY_TYPE

        if isinstance(expr, MethodCall):
            return ANY_TYPE

        if isinstance(expr, AttributeAccess):
            return ANY_TYPE

        if isinstance(expr, IndexAccess):
            container_type = self._infer_type(expr.container)
            if isinstance(container_type, GenericTypeInstance):
                if container_type.type_args:
                    return container_type.type_args[0]
            return ANY_TYPE

        if isinstance(expr, TernaryOp):
            then_type = self._infer_type(expr.then_expr)
            else_type = self._infer_type(expr.else_expr)
            if then_type == else_type:
                return then_type
            return UnionTypeInstance([then_type, else_type])

        if isinstance(expr, LambdaExpression):
            return CallableTypeInstance([], ANY_TYPE)

        return ANY_TYPE

