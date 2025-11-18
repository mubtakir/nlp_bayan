"""
Abstract Syntax Tree (AST) nodes for Bayan Language
عقد شجرة التجريد للغة بيان
"""

class ASTNode:
    """Base class for all AST nodes with optional source position"""
    line = None
    column = None
    filename = None

    def with_pos(self, line=None, column=None, filename=None):
        self.line = line
        self.column = column
        self.filename = filename
        return self

# ============ Traditional Programming Nodes ============

class Program(ASTNode):
    """Root node of the program"""
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Program({len(self.statements)} statements)"

class Block(ASTNode):
    """A block of statements"""
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Block({len(self.statements)} statements)"

class Assignment(ASTNode):
    """Variable assignment: x = 5"""
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Assignment({self.name}, {self.value})"

class BinaryOp(ASTNode):
    """Binary operation: a + b"""
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return f"BinaryOp({self.operator}, {self.left}, {self.right})"

class UnaryOp(ASTNode):
    """Unary operation: -x, not x"""
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def __repr__(self):
        return f"UnaryOp({self.operator}, {self.operand})"

class Number(ASTNode):
    """Numeric literal"""
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"

class String(ASTNode):
    """String literal"""
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"String({repr(self.value)})"

class Boolean(ASTNode):
    """Boolean literal"""
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Boolean({self.value})"

class NoneLiteral(ASTNode):
    """None literal"""
    def __repr__(self):
        return "NoneLiteral()"


class Variable(ASTNode):
    """Variable reference"""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Variable({self.name})"

class List(ASTNode):
    """List literal: [1, 2, 3]"""
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return f"List({len(self.elements)} elements)"

class ListComprehension(ASTNode):
    """List comprehension: [expr for x in iterable if cond]"""
    def __init__(self, expr, var_name, iterable, condition=None):
        self.expr = expr
        self.var_name = var_name
        self.iterable = iterable
        self.condition = condition

    def __repr__(self):
        return f"ListComprehension({self.var_name} in ...)"

class ListPattern(ASTNode):
    """List pattern for Prolog-style matching: [H|T] or [H1, H2|T]
    Also used for regular pattern matching: [x, y, z]
    """
    def __init__(self, head_elements, tail=None):
        self.head_elements = head_elements  # List of head elements
        self.tail = tail  # Tail variable or expression (None for regular patterns)
        # For backward compatibility with match patterns
        self.elements = head_elements if tail is None else head_elements

    def __repr__(self):
        if self.tail is None:
            return f"ListPattern({len(self.head_elements)} elements)"
        return f"ListPattern({len(self.head_elements)} heads | tail)"

class Slice(ASTNode):
    """Slice expression: list[start:end:step]"""
    def __init__(self, start=None, end=None, step=None):
        self.start = start
        self.end = end
        self.step = step

    def __repr__(self):
        return f"Slice({self.start}:{self.end}:{self.step})"

class Tuple(ASTNode):
    """Tuple literal: (1, 2, 3)"""
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return f"Tuple({len(self.elements)} elements)"

class Set(ASTNode):
    """Set literal: {1, 2, 3}"""
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return f"Set({len(self.elements)} elements)"

class IsExpression(ASTNode):
    """Arithmetic evaluation in logic context: ?X is 5 + 3"""
    def __init__(self, variable, expression):
        self.variable = variable  # Variable to bind result to
        self.expression = expression  # Arithmetic expression to evaluate

    def __repr__(self):
        return f"IsExpression({self.variable} is {self.expression})"

class AsyncFunctionDef(ASTNode):
    """Async function definition: async def name(params): body"""
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def __repr__(self):
        return f"AsyncFunctionDef({self.name}, {len(self.params)} params)"

class AwaitExpr(ASTNode):
    """Await expression: await coroutine()"""
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"AwaitExpr({self.expression})"

class YieldExpr(ASTNode):
    """Yield expression: yield value"""
    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return f"YieldExpr({self.value})"

class WithStatement(ASTNode):
    """With statement: with expr as var: body"""
    def __init__(self, context_expr, target_var, body):
        self.context_expr = context_expr
        self.target_var = target_var  # Can be None
        self.body = body

    def __repr__(self):
        return f"WithStatement({self.context_expr} as {self.target_var})"

class Cut(ASTNode):
    """Cut operator: ! (prevents backtracking in logic programming)"""
    def __init__(self):
        pass

    def __repr__(self):
        return "Cut(!)"

class Decorator(ASTNode):
    """Decorator: @decorator_name or @decorator(args)"""
    def __init__(self, name, args=None):
        self.name = name
        self.args = args if args is not None else []

    def __repr__(self):
        if self.args:
            return f"Decorator(@{self.name}({len(self.args)} args))"
        return f"Decorator(@{self.name})"

class Dict(ASTNode):
    """Dictionary literal: {key: value}"""
    def __init__(self, pairs):
        self.pairs = pairs  # List of (key, value) tuples

    def __repr__(self):
        return f"Dict({len(self.pairs)} pairs)"

class PhraseStatement(ASTNode):
    """Nominal phrase sugar inside hybrid blocks: e.g., محمد الطبيب. or عصير العنب[of]."""
    def __init__(self, text, relation=None):
        self.text = text
        self.relation = relation

    def __repr__(self):
        return f"PhraseStatement({self.text!r}, relation={self.relation!r})"

class Parameter(ASTNode):
    """Function parameter with optional default value and support for *args/**kwargs"""
    def __init__(self, name, default_value=None, is_varargs=False, is_kwargs=False):
        self.name = name
        self.default_value = default_value
        self.is_varargs = is_varargs  # *args
        self.is_kwargs = is_kwargs    # **kwargs

    def has_default(self):
        """Check if this parameter has a default value"""
        return self.default_value is not None

    def __repr__(self):
        prefix = ""
        if self.is_kwargs:
            prefix = "**"
        elif self.is_varargs:
            prefix = "*"

        if self.has_default():
            return f"Parameter({prefix}{self.name}={self.default_value})"
        return f"Parameter({prefix}{self.name})"

class NamedArgument(ASTNode):
    """Named argument in function call: func(name=value)"""
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"NamedArgument({self.name}={self.value})"

class KeyValuePair(ASTNode):
    """Key-value pair sugar used in special call contexts: head(key: value)."""
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"KeyValuePair({self.key}: {self.value})"

class SimilarityDecl(ASTNode):
    """Syntactic sugar statement: Head(Key1:Score1, Key2:Score2, ...)
    Lowers at runtime to asserting similar(Head, Key, Score, Kind, Domain) facts.
    """
    def __init__(self, head, pairs, kind=None, domain=None, default=None):
        self.head = head  # string head name
        self.pairs = pairs  # list[KeyValuePair]
        self.kind = kind
        self.domain = domain
        self.default = default

    def __repr__(self):
        return f"SimilarityDecl({self.head}, {len(self.pairs)} pairs)"

class CollectExpr(ASTNode):
    """Sugar: collect ?Var from predicate(...) [limit N] [unique]
    Evaluates to a Python list of bound values for Var.
    """
    def __init__(self, var_name, goal, limit=None, unique=False):
        # var_name without leading '?'
        self.var_name = var_name
        self.goal = goal
        self.limit = limit
        self.unique = unique

    def __repr__(self):
        return f"CollectExpr({self.var_name} from {getattr(self.goal, 'name', '?')})"

class TopkExpr(ASTNode):
    """Sugar: topk K of ?Var by ?Score where predicate(...)
    Evaluates to list of top-k values of Var by descending Score.
    """
    def __init__(self, k, var_name, score_name, goal):
        self.k = k
        self.var_name = var_name  # without '?'
        self.score_name = score_name  # without '?'
        self.goal = goal

    def __repr__(self):
        return f"TopkExpr(k={self.k}, var={self.var_name}, by={self.score_name})"

class ArgmaxExpr(ASTNode):
    """Sugar: argmax ?Var by ?Score where predicate(...)
    Evaluates to the best value of Var by descending Score.
    """
    def __init__(self, var_name, score_name, goal):
        self.var_name = var_name
        self.score_name = score_name
        self.goal = goal

    def __repr__(self):
        return f"ArgmaxExpr(var={self.var_name}, by={self.score_name})"

class ChooseExpr(ASTNode):
    """Sugar: choose { key: weight, ... } / اختر { ... }
    Evaluates to one key sampled according to weights.
    """
    def __init__(self, mapping_dict):
        # mapping_dict is a Dict AST node
        self.mapping = mapping_dict

    def __repr__(self):
        try:
            n = len(self.mapping.pairs)
        except Exception:
            n = '?'
        return f"ChooseExpr({n} choices)"

class SampleAssign(ASTNode):
    """Sugar: x ~ Dist(args) assigns a sampled value to variable x."""
    def __init__(self, var_name, dist_call):
        self.var_name = var_name
        self.dist_call = dist_call  # FunctionCall AST

    def __repr__(self):
        return f"SampleAssign({self.var_name} ~ {getattr(self.dist_call, 'name', 'Dist')})"

class FunctionCall(ASTNode):
    """Function call: func(arg1, arg2, name=value)"""
    def __init__(self, name, arguments, named_arguments=None):
        self.name = name
        # Backward-compat: older parser/users expect .function_name
        self.function_name = name
        self.arguments = arguments
        self.named_arguments = named_arguments or {}

    def __repr__(self):
        return f"FunctionCall({self.name}, {len(self.arguments)} args, {len(self.named_arguments)} named)"

class FunctionDef(ASTNode):
    """Function definition with support for default parameters and decorators"""
    def __init__(self, name, parameters, body, decorators=None):
        self.name = name
        # parameters can be strings (old format) or Parameter objects (new format)
        self.parameters = parameters
        self.body = body
        self.decorators = decorators if decorators is not None else []

    def __repr__(self):
        dec_str = f", {len(self.decorators)} decorators" if self.decorators else ""
        return f"FunctionDef({self.name}, {len(self.parameters)} params{dec_str})"

class ClassDef(ASTNode):
    """Class definition with support for decorators"""
    def __init__(self, name, base_class, body, base_classes=None, decorators=None):
        self.name = name
        # Backward-compat single base
        self.base_class = base_class
        # New: support multiple bases
        self.base_classes = base_classes
        self.body = body
        self.decorators = decorators if decorators is not None else []

    def __repr__(self):
        dec_str = f", {len(self.decorators)} decorators" if self.decorators else ""
        return f"ClassDef({self.name}{dec_str})"

class ObjectInstance(ASTNode):
    """Object instance"""
    def __init__(self, class_name, arguments):
        self.class_name = class_name
        self.arguments = arguments

    def __repr__(self):
        return f"ObjectInstance({self.class_name})"

class AttributeAccess(ASTNode):
    """Attribute access (obj.attr)"""
    def __init__(self, object_expr, attribute_name):
        self.object_expr = object_expr
        self.attribute_name = attribute_name

    def __repr__(self):
        return f"AttributeAccess({self.attribute_name})"

class MethodCall(ASTNode):
    """Method call (obj.method()) with support for named arguments"""
    def __init__(self, object_expr, method_name, arguments, named_arguments=None):
        self.object_expr = object_expr
        self.method_name = method_name
        self.arguments = arguments
        self.named_arguments = named_arguments or {}

    def __repr__(self):
        return f"MethodCall({self.method_name})"

class SubscriptAccess(ASTNode):
    """Indexing access (obj[index])"""
    def __init__(self, object_expr, index_expr):
        self.object_expr = object_expr
        self.index_expr = index_expr

    def __repr__(self):
        return "SubscriptAccess([])"

class AttributeAssignment(ASTNode):
    """Attribute assignment: obj.attr = value"""
    def __init__(self, object_expr, attribute_name, value):
        self.object_expr = object_expr
        self.attribute_name = attribute_name
        self.value = value

    def __repr__(self):
        return f"AttributeAssignment({self.attribute_name})"

class SubscriptAssignment(ASTNode):
    """Subscript assignment: obj[index] = value"""
    def __init__(self, object_expr, index_expr, value):
        self.object_expr = object_expr
        self.index_expr = index_expr
        self.value = value

    def __repr__(self):
        return "SubscriptAssignment([])"

class SelfReference(ASTNode):
    """Self reference"""
    def __init__(self):
        pass

    def __repr__(self):
        return "SelfReference()"

class SuperCall(ASTNode):
    """Super call for parent class with support for named arguments"""
    def __init__(self, method_name, arguments, named_arguments=None):
        self.method_name = method_name
        self.arguments = arguments
        self.named_arguments = named_arguments or {}

    def __repr__(self):
        return f"SuperCall({self.method_name})"

class ImportStatement(ASTNode):
    """Import statement"""
    def __init__(self, module_name, alias=None):
        self.module_name = module_name
        self.alias = alias

    def __repr__(self):
        return f"ImportStatement({self.module_name})"

class FromImportStatement(ASTNode):
    """From ... import statement"""
    def __init__(self, module_name, names, aliases=None):
        self.module_name = module_name
        self.names = names
        self.aliases = aliases or []

    def __repr__(self):
        return f"FromImportStatement({self.module_name})"

class IfStatement(ASTNode):
    """If statement"""
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

    def __repr__(self):
        return f"IfStatement(condition, then, else={self.else_branch is not None})"

class ForLoop(ASTNode):
    """For loop"""
    def __init__(self, variable, iterable, body):
        self.variable = variable
        self.iterable = iterable
        self.body = body

    def __repr__(self):
        return f"ForLoop({self.variable}, iterable, body)"

class WhileLoop(ASTNode):
    """While loop"""
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"WhileLoop(condition, body)"

class ReturnStatement(ASTNode):
    """Return statement"""
    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return f"ReturnStatement({self.value})"

class BreakStatement(ASTNode):
    """Break statement"""
    def __repr__(self):
        return "BreakStatement()"

class ContinueStatement(ASTNode):
    """Continue statement"""
    def __repr__(self):
        return "ContinueStatement()"

class PrintStatement(ASTNode):
    """Print statement"""
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"PrintStatement({self.value})"

# ============ Logical Programming Nodes ============

class RaiseStatement(ASTNode):
    """Raise statement"""
    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return f"RaiseStatement({self.value})"

class ExceptHandler(ASTNode):
    """Except handler: except [Type] [as alias]: body"""
    def __init__(self, type_name=None, alias=None, body=None):
        self.type_name = type_name
        self.alias = alias
        self.body = body

    def __repr__(self):
        return f"ExceptHandler({self.type_name}, alias={self.alias})"

class TryExceptFinally(ASTNode):
    """Try/Except/Finally statement"""
    def __init__(self, try_block, handlers=None, finally_block=None):
        self.try_block = try_block
        self.handlers = handlers or []
        self.finally_block = finally_block

    def __repr__(self):
        return f"TryExceptFinally(handlers={len(self.handlers)}, finally={self.finally_block is not None})"


class LogicalFact(ASTNode):
    """Logical fact: parent(john, mary). Optionally with probability via fact[0.8]."""
    def __init__(self, predicate, probability=None):
        self.predicate = predicate
        self.probability = probability  # Optional float in [0,1]

    def __repr__(self):
        if self.probability is not None:
            return f"LogicalFact({self.predicate}, p={self.probability})"
        return f"LogicalFact({self.predicate})"

class LogicalRule(ASTNode):
    """Logical rule: grandparent(X, Z) :- parent(X, Y), parent(Y, Z)."""
    def __init__(self, head, body):
        self.head = head
        self.body = body  # List of predicates

    def __repr__(self):
        return f"LogicalRule({self.head} :- ...)"

class LogicalQuery(ASTNode):
    """Logical query: ?- parent(X, john)."""
    def __init__(self, goal):
        self.goal = goal

    def __repr__(self):
        return f"LogicalQuery({self.goal})"

class LogicalPredicate(ASTNode):
    """Logical predicate: parent(X, Y)"""
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

    def __repr__(self):
        return f"LogicalPredicate({self.name}/{len(self.arguments)})"

class LogicalVariable(ASTNode):
    """Logical variable: ?X, ?Y"""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"LogicalVariable(?{self.name})"

class LogicalConstant(ASTNode):
    """Logical constant: atom, number, string"""
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"LogicalConstant({self.value})"

class LogicalConjunction(ASTNode):
    """Logical AND: goal1, goal2"""
    def __init__(self, goals):
        self.goals = goals

    def __repr__(self):
        return f"LogicalConjunction({len(self.goals)} goals)"

class LogicalDisjunction(ASTNode):
    """Logical OR: goal1; goal2"""
    def __init__(self, goals):
        self.goals = goals

    def __repr__(self):
        return f"LogicalDisjunction({len(self.goals)} goals)"

class LogicalNegation(ASTNode):
    """Logical NOT: \\+ goal"""
    def __init__(self, goal):
        self.goal = goal

    def __repr__(self):
        return f"LogicalNegation({self.goal})"

# ============ Hybrid Nodes ============

class HybridBlock(ASTNode):
    """Hybrid block combining traditional and logical code"""
    def __init__(self, traditional_stmts, logical_stmts):
        self.traditional_stmts = traditional_stmts
        self.logical_stmts = logical_stmts

    def __repr__(self):
        return f"HybridBlock({len(self.traditional_stmts)} trad, {len(self.logical_stmts)} logical)"

class LogicalIfStatement(ASTNode):
    """If statement with logical condition"""
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition  # Can be a logical query
        self.then_branch = then_branch
        self.else_branch = else_branch

    def __repr__(self):
        return f"LogicalIfStatement(condition, then, else={self.else_branch is not None})"

class QueryExpression(ASTNode):
    """Query expression in traditional code: query parent(?X, john)"""
    def __init__(self, goal):
        self.goal = goal

    def __repr__(self):
        return f"QueryExpression({self.goal})"


# ============ Entity System Nodes ============

class EntityDef(ASTNode):
    """Entity definition: entity <name> { ... } where body is a dict-like structure"""
    def __init__(self, name, body):
        self.name = name
        self.body = body  # AST node (Dict) to be evaluated later

    def __repr__(self):
        return f"EntityDef({self.name})"


class ConceptDef(ASTNode):
    """Concept definition: concept Name = {elements}
    Holds a set literal to be evaluated and installed as both runtime set and logical facts in_concept(Name, Elem).
    """
    def __init__(self, name, set_node):
        self.name = name
        self.set_node = set_node  # Set AST node

    def __repr__(self):
        return f"ConceptDef({self.name})"

class ApplyActionStmt(ASTNode):
    """Apply action: apply <actor>.<action>(<target>, [action_value=...])"""
    def __init__(self, actor_name, action_name, target_expr, named_args=None):
        self.actor_name = actor_name
        self.action_name = action_name
        self.target_expr = target_expr
        self.named_args = named_args or {}

    def __repr__(self):
        return f"ApplyActionStmt({self.actor_name}.{self.action_name}(...))"


# ============ Once and Limit Nodes ============

class OnceStatement(ASTNode):
    """Once statement: once { block } - execute block with max_solutions=1"""
    def __init__(self, body):
        self.body = body  # Block node

    def __repr__(self):
        return f"OnceStatement({self.body})"

class OnceGoal(ASTNode):
    """Once goal: once goal. - single logical goal with limit 1"""
    def __init__(self, goal):
        self.goal = goal  # Predicate node

    def __repr__(self):
        return f"OnceGoal({self.goal})"

class LimitStatement(ASTNode):
    """Limit statement: limit N { block }"""
    def __init__(self, limit, body):
        self.limit = limit  # int
        self.body = body  # Block node

    def __repr__(self):
        return f"LimitStatement({self.limit}, {self.body})"

class LimitGoal(ASTNode):
    """Limit goal: limit N goal."""
    def __init__(self, limit, goal):
        self.limit = limit  # int
        self.goal = goal  # Predicate node

    def __repr__(self):
        return f"LimitGoal({self.limit}, {self.goal})"


class MatchInAs(ASTNode):
    """Match statement: match pattern in text as var_name
    Syntactic sugar for: var_name = match(pattern, text)
    """
    def __init__(self, pattern, text, var_name):
        self.pattern = pattern  # Expression (string or template)
        self.text = text  # Expression (string to match against)
        self.var_name = var_name  # Variable name to bind result

    def __repr__(self):
        return f"MatchInAs(pattern, text, as={self.var_name})"


# ============ Temporal Constructs ============

class TemporalBlock(ASTNode):
    """Temporal block: temporal { first: action1, then: action2, lastly: action3 }
    Executes actions in sequence with optional timing constraints
    """
    def __init__(self, steps):
        self.steps = steps  # List of (label, statement) tuples: [('first', stmt), ('then', stmt), ...]

    def __repr__(self):
        return f"TemporalBlock({len(self.steps)} steps)"


class WithinBlock(ASTNode):
    """Within block: within 5.0 seconds { ... }
    Executes block with a time constraint (timeout)
    """
    def __init__(self, duration, unit, body):
        self.duration = duration  # Number (float or int)
        self.unit = unit  # 'seconds', 'minutes', 'hours' (or Arabic equivalents)
        self.body = body  # Block or statement

    def __repr__(self):
        return f"WithinBlock({self.duration} {self.unit})"


class ScheduleBlock(ASTNode):
    """Schedule block: schedule every 2.0 seconds { ... }
    Schedules repeated execution of a block
    """
    def __init__(self, interval, unit, body):
        self.interval = interval  # Number (float or int)
        self.unit = unit  # 'seconds', 'minutes', 'hours' (or Arabic equivalents)
        self.body = body  # Block or statement

    def __repr__(self):
        return f"ScheduleBlock(every {self.interval} {self.unit})"


class DelayStatement(ASTNode):
    """Delay statement: delay 1.5 seconds
    Pauses execution for specified duration
    """
    def __init__(self, duration, unit):
        self.duration = duration  # Number (float or int)
        self.unit = unit  # 'seconds', 'minutes', 'hours' (or Arabic equivalents)

    def __repr__(self):
        return f"DelayStatement({self.duration} {self.unit})"


# ============================================================================
# Constraint & Validation Nodes
# ============================================================================

class WhereClause(ASTNode):
    """Where clause for filtering/constraints

    Examples:
        x = [1, 2, 3, 4, 5] where item > 2
        result = compute(x) where x > 0
    """
    def __init__(self, expression, condition):
        self.expression = expression  # The main expression
        self.condition = condition    # The where condition

    def __repr__(self):
        return f"WhereClause({self.expression} where {self.condition})"


class RequiresClause(ASTNode):
    """Requires clause (precondition contract)

    Example:
        def divide(a, b):
            requires b != 0
            { return a / b }
    """
    def __init__(self, condition, message=None):
        self.condition = condition  # Boolean expression
        self.message = message      # Optional error message

    def __repr__(self):
        return f"RequiresClause({self.condition})"


class EnsuresClause(ASTNode):
    """Ensures clause (postcondition contract)

    Example:
        def sqrt(x):
            requires x >= 0
            ensures result >= 0
            { result = x ** 0.5 }
    """
    def __init__(self, condition, message=None):
        self.condition = condition  # Boolean expression
        self.message = message      # Optional error message

    def __repr__(self):
        return f"EnsuresClause({self.condition})"


class InvariantClause(ASTNode):
    """Invariant clause (loop/class invariant)

    Examples:
        # Loop invariant
        for i in range(10):
            invariant i >= 0
            { ... }

        # Class invariant
        class BankAccount:
            invariant balance >= 0
            { ... }
    """
    def __init__(self, condition, message=None):
        self.condition = condition  # Boolean expression
        self.message = message      # Optional error message

    def __repr__(self):
        return f"InvariantClause({self.condition})"


class ContractError(Exception):
    """Exception raised when a contract is violated"""
    pass


# ============================================================================
# Pattern Matching Nodes
# ============================================================================

class MatchStatement(ASTNode):
    """Match statement for pattern matching

    Example:
        match value:
            case 1: { print("one") }
            case 2: { print("two") }
            default: { print("other") }
    """
    def __init__(self, value, cases):
        self.value = value          # Expression to match
        self.cases = cases          # List of CaseClause nodes

    def __repr__(self):
        return f"MatchStatement({self.value}, {len(self.cases)} cases)"


class CaseClause(ASTNode):
    """Case clause in a match statement

    Example:
        case [x, y]: { print(x + y) }
        case {"name": n} when n != "": { print(n) }
    """
    def __init__(self, pattern, body, guard=None):
        self.pattern = pattern      # Pattern to match (can be literal, list, dict, or variable)
        self.body = body            # Block to execute if matched
        self.guard = guard          # Optional guard condition (when clause)

    def __repr__(self):
        guard_str = f" when {self.guard}" if self.guard else ""
        return f"CaseClause({self.pattern}{guard_str})"


class DefaultClause(ASTNode):
    """Default clause in a match statement

    Example:
        default: { print("no match") }
    """
    def __init__(self, body):
        self.body = body            # Block to execute if no case matches

    def __repr__(self):
        return "DefaultClause()"


class DictPattern(ASTNode):
    """Dictionary pattern for destructuring

    Example:
        {"name": n, "age": a}
    """
    def __init__(self, keys, patterns):
        self.keys = keys            # List of dictionary keys
        self.patterns = patterns    # List of patterns for each key

    def __repr__(self):
        return f"DictPattern({dict(zip(self.keys, self.patterns))})"


# ============================================================================
# Reactive Programming Nodes - عقد البرمجة التفاعلية
# ============================================================================

class ReactiveDeclaration(ASTNode):
    """Reactive variable declaration

    Declares a variable as reactive, meaning changes to it will trigger
    watchers and update computed properties.

    Example:
        reactive x = 10
        تفاعلي س = 10
    """
    def __init__(self, variable, value):
        self.variable = variable    # Variable name
        self.value = value          # Initial value expression

    def __repr__(self):
        return f"ReactiveDeclaration({self.variable}, {self.value})"


class WatchBlock(ASTNode):
    """Watch block for monitoring variable changes

    Executes a block of code whenever watched variables change.

    Example:
        watch x, y: { print("x or y changed") }
        راقب س, ص: { print("س أو ص تغيرت") }
    """
    def __init__(self, variables, body):
        self.variables = variables  # List of variable names to watch
        self.body = body            # Block to execute on change

    def __repr__(self):
        return f"WatchBlock({self.variables}, {self.body})"


class ComputedProperty(ASTNode):
    """Computed property that auto-updates when dependencies change

    Defines a property that is automatically recomputed when any of its
    dependencies (reactive variables) change.

    Example:
        computed sum = x + y
        محسوب مجموع = س + ص
    """
    def __init__(self, variable, expression, dependencies=None):
        self.variable = variable        # Property name
        self.expression = expression    # Expression to compute
        self.dependencies = dependencies or []  # List of dependent variables

    def __repr__(self):
        return f"ComputedProperty({self.variable}, {self.expression})"


# ============================================
# Pipeline and Composition Nodes
# ============================================

class PipelineOp(ASTNode):
    """Pipeline operation: value |> function

    Applies function to value: value |> f means f(value)
    """
    def __init__(self, value, function):
        self.value = value          # Expression to pipe
        self.function = function    # Function to apply

    def __repr__(self):
        return f"PipelineOp({self.value} |> {self.function})"


class ComposeOp(ASTNode):
    """Function composition: f >> g

    Creates a new function that applies f then g: (f >> g)(x) means g(f(x))
    """
    def __init__(self, first, second):
        self.first = first      # First function
        self.second = second    # Second function

    def __repr__(self):
        return f"ComposeOp({self.first} >> {self.second})"


# ============ Cognitive-Semantic Model Nodes ============
# النموذج المعرفي-الدلالي (Idea-Event-Result Model)

class CognitiveEntity(ASTNode):
    """Cognitive entity with dynamic properties

    Syntax:
        cognitive_entity <name>:
        {
            property1: value1
            property2: value2
            ...
        }

    Arabic:
        كيان_معرفي <اسم>:
        {
            خاصية1: قيمة1
            خاصية2: قيمة2
            ...
        }
    """
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties  # Dict node with property: value pairs

    def __repr__(self):
        return f"CognitiveEntity({self.name})"


class CognitiveEvent(ASTNode):
    """Cognitive event with participants and their degrees

    Syntax:
        cognitive_event <name>:
        {
            participants: {
                entity1: {role: "...", degree: 0.8},
                entity2: {role: "...", degree: 1.0}
            },
            strength: 0.9,
            transform: {
                entity1.property = new_value
                ...
            },
            reactions: [
                {event: "event_name", probability: 0.8, delay: "1s"}
            ]
        }

    Arabic:
        حدث_معرفي <اسم>:
        {
            مشاركون: {...},
            قوة: 0.9,
            تحويل: {...},
            ردود_فعل: [...]
        }
    """
    def __init__(self, name, config):
        self.name = name
        self.config = config  # Dict node with event configuration

    def __repr__(self):
        return f"CognitiveEvent({self.name})"



class ConceptualBlueprint(ASTNode):
    """Conceptual blueprint pattern definition.

    Syntax:
        conceptual_blueprint <name> { ... }
        تصور_عام <name> { ... }
    """

    def __init__(self, name, config):
        self.name = name
        self.config = config  # Dict node with blueprint configuration

    def __repr__(self):
        return f"ConceptualBlueprint({self.name})"


class TriggerEvent(ASTNode):
    """Trigger a cognitive event

    Syntax:
        trigger <event_name>
        trigger <event_name> with {param: value}

    Arabic:
        أطلق <اسم_الحدث>
        أطلق <اسم_الحدث> مع {معامل: قيمة}
    """
    def __init__(self, event_name, params=None):
        self.event_name = event_name
        self.params = params  # Optional dict node

    def __repr__(self):
        return f"TriggerEvent({self.event_name})"


class ConcurrentEvents(ASTNode):
    """Execute multiple events concurrently

    Syntax:
        concurrent:
        {
            event event1 with strength 0.8
            event event2 with strength 0.6
            ...
        }
        => {
            # Combined effects
        }

    Arabic:
        متزامن:
        {
            حدث حدث1 بقوة 0.8
            حدث حدث2 بقوة 0.6
            ...
        }
        => {
            # التأثيرات المدمجة
        }
    """
    def __init__(self, events, effects):
        self.events = events  # List of (event_name, strength) tuples
        self.effects = effects  # Block node with combined effects

    def __repr__(self):
        return f"ConcurrentEvents({len(self.events)} events)"


class LinguisticPattern(ASTNode):
    """Define a linguistic pattern for expressing ideas

    Syntax:
        pattern <name>:
        {
            structure: [component1, component2, ...]
            express: function(idea) { ... }
        }

    Arabic:
        قالب <اسم>:
        {
            بنية: [مكون1، مكون2، ...]
            تعبير: دالة(فكرة) { ... }
        }
    """
    def __init__(self, name, config):
        self.name = name
        self.config = config  # Dict node with pattern configuration

    def __repr__(self):
        return f"LinguisticPattern({self.name})"


class IdeaDef(ASTNode):
    """Define an idea (cognitive concept)

    Syntax:
        idea "<name>":
        {
            entities: {entity1: {...}, entity2: {...}},
            event: "event_name",
            result: {
                state_changes: {...},
                reactions: [...],
                linguistic_forms: [...]
            }
        }

    Arabic:
        فكرة "<اسم>":
        {
            كيانات: {...},
            حدث: "اسم_الحدث",
            نتيجة: {
                تغييرات_الحالة: {...},
                ردود_فعل: [...],
                أشكال_لغوية: [...]
            }
        }
    """
    def __init__(self, name, config):
        self.name = name
        self.config = config  # Dict node with idea configuration

    def __repr__(self):
        return f"IdeaDef({self.name})"


# ============================================================================
# Semantic Programming & Knowledge Management Nodes
# عقد البرمجة المعانية وإدارة المعرفة
# ============================================================================

class SemanticMeaning(ASTNode):
    """Define semantic meaning with relationships

    Syntax:
        meaning <name>:
        {
            relationship1: value1,
            relationship2: value2
        }

        معنى <اسم>:
        {
            علاقة1: قيمة1,
            علاقة2: قيمة2
        }
    """
    def __init__(self, name, relationships):
        self.name = name
        self.relationships = relationships  # Dict node with relationships

    def __repr__(self):
        return f"SemanticMeaning({self.name})"


class SemanticQuery(ASTNode):
    """Query semantic network

    Syntax:
        query: function_name(args)
        استعلام: اسم_الدالة(معاملات)
    """
    def __init__(self, query_expr):
        self.query_expr = query_expr  # Function call or expression

    def __repr__(self):
        return f"SemanticQuery({self.query_expr})"


class KnowledgeInfo(ASTNode):
    """Information with context (time, place, source, certainty)

    Syntax:
        information "<name>":
        {
            content: {...},
            context: {
                time: "...",
                place: "...",
                source: "...",
                certainty: 0.9
            }
        }

        معلومة "<اسم>":
        {
            محتوى: {...},
            سياق: {
                زمان: "...",
                مكان: "...",
                مصدر: "...",
                يقين: 0.9
            }
        }
    """
    def __init__(self, name, config):
        self.name = name
        self.config = config  # Dict node with content and context

    def __repr__(self):
        return f"KnowledgeInfo({self.name})"


class InferenceRule(ASTNode):
    """Define inference rule for knowledge deduction

    Syntax:
        inference_rule "<name>":
        {
            if: [...conditions...],
            then: {...conclusion...}
        }

        قاعدة_استدلال "<اسم>":
        {
            إذا: [...شروط...],
            إذن: {...نتيجة...}
        }
    """
    def __init__(self, name, config):
        self.name = name
        self.config = config  # Dict node with if/then

    def __repr__(self):
        return f"InferenceRule({self.name})"


class InferFrom(ASTNode):
    """Apply inference from given information

    Syntax:
        infer_from: "statement"
        استنتج من: "عبارة"
    """
    def __init__(self, statement):
        self.statement = statement

    def __repr__(self):
        return f"InferFrom({self.statement})"


class Contradiction(ASTNode):
    """Detect contradiction between information

    Syntax:
        contradiction between: [info1, info2]
        resolve: "strategy"

        تناقض بين: [معلومة1, معلومة2]
        حل: "استراتيجية"
    """
    def __init__(self, items, resolution=None):
        self.items = items  # List of information items
        self.resolution = resolution  # Resolution strategy

    def __repr__(self):
        return f"Contradiction({len(self.items)} items)"


class EvolvingKnowledge(ASTNode):
    """Knowledge that evolves over time

    Syntax:
        evolving_knowledge "<name>":
        {
            current_value: ...,
            history: [...],
            future_prediction: {...}
        }

        معرفة "<اسم>":
        {
            قيمة_حالية: ...,
            تاريخ: [...],
            توقع_مستقبلي: {...}
        }
    """
    def __init__(self, name, config):
        self.name = name
        self.config = config

    def __repr__(self):
        return f"EvolvingKnowledge({self.name})"


class Ontology(ASTNode):
    """Define ontology (concept hierarchy)

    Syntax:
        ontology "<name>":
        {
            root: "concept",
            taxonomy: {...}
        }

        أنطولوجيا "<اسم>":
        {
            جذر: "مفهوم",
            تصنيف: {...}
        }
    """
    def __init__(self, name, config):
        self.name = name
        self.config = config

    def __repr__(self):
        return f"Ontology({self.name})"


class SemanticMemory(ASTNode):
    """Semantic memory operations

    Syntax:
        memory.store({...})
        memory.retrieve(query)

        ذاكرة.احفظ({...})
        ذاكرة.استرجع(استعلام)
    """
    def __init__(self, operation, data):
        self.operation = operation  # "store" or "retrieve"
        self.data = data  # Data to store or query

    def __repr__(self):
        return f"SemanticMemory({self.operation})"


class SemanticSimilarity(ASTNode):
    """Calculate semantic similarity between concepts

    Syntax:
        similarity(concept1, concept2)
        تشابه(مفهوم1, مفهوم2)
    """
    def __init__(self, concept1, concept2):
        self.concept1 = concept1
        self.concept2 = concept2

    def __repr__(self):
        return f"SemanticSimilarity({self.concept1}, {self.concept2})"


class Concept(ASTNode):
    """Define a concept with properties

    Syntax:
        concept "<name>": {...properties...}
        مفهوم "<اسم>": {...خصائص...}
    """
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties

    def __repr__(self):
        return f"Concept({self.name})"


class Narrative(ASTNode):
    """Define a narrative/story

    Syntax:
        narrative "<name>":
        {
            characters: {...},
            events: [...],
            structure: "..."
        }

        سرد "<اسم>":
        {
            شخصيات: {...},
            أحداث: [...],
            بنية: "..."
        }
    """
    def __init__(self, name, config):
        self.name = name
        self.config = config

    def __repr__(self):
        return f"Narrative({self.name})"


class GenerateNarrative(ASTNode):
    """Generate narrative based on template

    Syntax:
        generate_narrative: based_on("template")
        ولّد_سرد: بناءً_على("قالب")
    """
    def __init__(self, template):
        self.template = template

    def __repr__(self):
        return f"GenerateNarrative({self.template})"


class CurrentContext(ASTNode):
    """Define or access current context

    Syntax:
        current_context: {...}
        سياق_حالي: {...}
    """
    def __init__(self, context_data):
        self.context_data = context_data

    def __repr__(self):
        return f"CurrentContext()"


class ContextAwareBlock(ASTNode):
    """Context-aware conditional block

    Syntax:
        if context.property == value:
        {
            ...
        }
    """
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"ContextAwareBlock()"


# ============================================================================
# EXISTENTIAL MODEL NODES (النموذج الوجودي)
# ============================================================================

class Domain(ASTNode):
    """
    Define a knowledge domain with its basic entities, environment, and rules.

    Arabic:
        مجال "الكيمياء":
        {
            "كائن_أساسي": "عنصر",
            "بيئة": "محلول",
            "معانٍ_أساسية": ["تفاعل", "ذوبان"],
            "علاقات": ["يتفاعل_مع", "يذوب_في"],
            "خصائص": ["عدد_ذري", "كتلة_ذرية"]
        }

    English:
        domain "Chemistry":
        {
            "basic_entity": "element",
            "environment": "solution",
            "basic_meanings": ["reaction", "dissolution"],
            "relations": ["reacts_with", "dissolves_in"],
            "properties": ["atomic_number", "atomic_mass"]
        }
    """
    def __init__(self, name, config):
        self.name = name
        self.config = config  # Dict node with domain configuration

    def __repr__(self):
        return f"Domain({self.name})"


class GenericEnvironment(ASTNode):
    """
    Define a generic environment with spatial, temporal, and domain-specific dimensions.

    Arabic:
        بيئة "محلول_حمضي" في_مجال "الكيمياء":
        {
            "أبعاد": {
                "مكاني": ["سطح", "قاع", "وسط"],
                "زماني": ["قبل_التفاعل", "أثناء_التفاعل", "بعد_التفاعل"],
                "مجالي": ["تركيز", "حرارة", "ضغط"]
            },
            "خصائص": {"pH": 3, "حرارة": 25},
            "قوانين": ["قانون_الكتلة", "قانون_الطاقة"]
        }

    English:
        environment "acidic_solution" in_domain "Chemistry":
        {
            "dimensions": {
                "spatial": ["surface", "bottom", "middle"],
                "temporal": ["before_reaction", "during_reaction", "after_reaction"],
                "domain_specific": ["concentration", "temperature", "pressure"]
            },
            "properties": {"pH": 3, "temperature": 25},
            "laws": ["mass_law", "energy_law"]
        }
    """
    def __init__(self, name, domain, config):
        self.name = name
        self.domain = domain
        self.config = config  # Dict node with environment configuration

    def __repr__(self):
        return f"GenericEnvironment({self.name}, domain={self.domain})"


class ExistentialBeing(ASTNode):
    """
    Define an existential being in a domain with inherited and intrinsic meanings.

    Arabic:
        كائن_وجودي "صوديوم" من_نوع "عنصر" في_مجال "الكيمياء":
        {
            "بيئة": "محلول_حمضي",
            "خصائص_ذاتية": {"عدد_ذري": 11, "رمز": "Na"},
            "معانٍ_موروثة": ["موقع_في_المحلول", "زمن_الإضافة"],
            "معانٍ_ذاتية": ["نشاط_كيميائي", "قابلية_للتفاعل"],
            "علاقات": {"يتفاعل_مع": ["كلور", "ماء"]},
            "أفعال": {"تفاعل": "ينتج_ملح"},
            "حالات": ["صلب", "منحل", "متفاعل"]
        }

    English:
        existential_being "sodium" of_type "element" in_domain "Chemistry":
        {
            "environment": "acidic_solution",
            "intrinsic_properties": {"atomic_number": 11, "symbol": "Na"},
            "inherited_meanings": ["position_in_solution", "addition_time"],
            "intrinsic_meanings": ["chemical_activity", "reactivity"],
            "relations": {"reacts_with": ["chlorine", "water"]},
            "actions": {"react": "produces_salt"},
            "states": ["solid", "dissolved", "reacting"]
        }
    """
    def __init__(self, name, entity_type, domain, config):
        self.name = name
        self.entity_type = entity_type
        self.domain = domain
        self.config = config  # Dict node with being configuration

    def __repr__(self):
        return f"ExistentialBeing({self.name}, type={self.entity_type}, domain={self.domain})"


class DomainRelation(ASTNode):
    """
    Define a relation between entities in a domain.

    Arabic:
        علاقة_مجالية "يتفاعل_مع" في_مجال "الكيمياء":
        {
            "نوع": "ثنائية",
            "متماثلة": 0,
            "شروط": {"نشاط": "عالي"},
            "نتيجة": "مركب_جديد"
        }

    English:
        domain_relation "reacts_with" in_domain "Chemistry":
        {
            "type": "binary",
            "symmetric": 0,
            "conditions": {"activity": "high"},
            "result": "new_compound"
        }
    """
    def __init__(self, name, domain, config):
        self.name = name
        self.domain = domain
        self.config = config  # Dict node with relation configuration

    def __repr__(self):
        return f"DomainRelation({self.name}, domain={self.domain})"


class DomainAction(ASTNode):
    """
    Define an action that entities can perform in a domain.

    Arabic:
        فعل_مجالي "تفاعل" في_مجال "الكيمياء":
        {
            "فاعل": "عنصر",
            "مفعول": "عنصر",
            "شروط": {"طاقة": "كافية"},
            "نتيجة": {"مركب": "جديد", "طاقة": "محررة"}
        }

    English:
        domain_action "react" in_domain "Chemistry":
        {
            "actor": "element",
            "object": "element",
            "conditions": {"energy": "sufficient"},
            "result": {"compound": "new", "energy": "released"}
        }
    """
    def __init__(self, name, domain, config):
        self.name = name
        self.domain = domain
        self.config = config  # Dict node with action configuration

    def __repr__(self):
        return f"DomainAction({self.name}, domain={self.domain})"


class MetaphoricalMeaning(ASTNode):
    """
    Define a metaphorical meaning built on basic meanings.

    Arabic:
        معنى_مجازي "عدالة" في_مجال "عام":
        {
            "تعريف": "كل كائن يأخذ ما يكفيه حسب طبيعته",
            "يُبنى_على": ["احتياج", "طبيعة", "توزيع"],
            "يُطبق_على": ["كل_الكائنات"],
            "شروط": {
                "لكل": "كائن",
                "يوجد": "احتياج",
                "يُعطى": "ما_يكفي_الاحتياج"
            }
        }

    English:
        metaphorical_meaning "justice" in_domain "general":
        {
            "definition": "each being gets what suffices according to its nature",
            "built_on": ["need", "nature", "distribution"],
            "applies_to": ["all_beings"],
            "conditions": {
                "for_each": "being",
                "exists": "need",
                "given": "what_suffices_need"
            }
        }
    """
    def __init__(self, name, domain, config):
        self.name = name
        self.domain = domain
        self.config = config  # Dict node with metaphorical meaning configuration

    def __repr__(self):
        return f"MetaphoricalMeaning({self.name}, domain={self.domain})"


class DomainLaw(ASTNode):
    """
    Define a law that governs a domain.

    Arabic:
        قانون_مجالي "قانون_الكتلة" في_مجال "الكيمياء":
        {
            "صيغة": "كتلة_المتفاعلات = كتلة_النواتج",
            "ينطبق_على": ["كل_التفاعلات"],
            "استثناءات": []
        }

    English:
        domain_law "mass_law" in_domain "Chemistry":
        {
            "formula": "mass_reactants = mass_products",
            "applies_to": ["all_reactions"],
            "exceptions": []
        }
    """
    def __init__(self, name, domain, config):
        self.name = name
        self.domain = domain
        self.config = config  # Dict node with law configuration

    def __repr__(self):
        return f"DomainLaw({self.name}, domain={self.domain})"


class ExistentialQuery(ASTNode):
    """
    Query existential beings in a domain.

    Arabic:
        استعلام_وجودي:
        {
            "في_مجال": "الكيمياء",
            "عن": "عناصر",
            "شروط": {"يتفاعل_مع": "ماء", "نشاط": "عالي"}
        }

    English:
        existential_query:
        {
            "in_domain": "Chemistry",
            "about": "elements",
            "conditions": {"reacts_with": "water", "activity": "high"}
        }
    """
    def __init__(self, config):
        self.config = config  # Dict node with query configuration

    def __repr__(self):
        return f"ExistentialQuery()"


