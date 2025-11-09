"""
Hybrid Interpreter for Bayan Language
مفسر هجين للغة بيان
"""

from .ast_nodes import *
from .traditional_interpreter import TraditionalInterpreter
from .logical_engine import LogicalEngine, Fact, Rule, Predicate, Term
from .entity_engine import EntityEngine

class HybridInterpreter:
    """Hybrid interpreter combining traditional and logical programming"""

    def __init__(self):
        self.traditional = TraditionalInterpreter()
        self.logical = LogicalEngine()
        self.shared_env = {}
        # Share the logical engine with the traditional interpreter
        self.traditional.logical_engine = self.logical
        # Expose useful runtime objects/types in Bayan global env
        env = self.traditional.global_env
        env['EntityEngine'] = EntityEngine
        env['Fact'] = Fact
        env['Rule'] = Rule
        env['Predicate'] = Predicate
        env['Term'] = Term
        env['logical'] = self.logical
        # Share the class system and import system
        self.class_system = self.traditional.class_system
        self.import_system = self.traditional.import_system
        # Bayan module cache and search paths
        import os
        self._bayan_module_cache = {}
        cwd = os.getcwd()
        self._bayan_module_paths = [cwd, os.path.join(cwd, 'tests'), os.path.join(cwd, 'tests', 'bayan_modules')]

        # Action-centric helper API (no grammar changes needed)
        def _perform_api(action_name, participants, states=None, properties=None, action_value=1.0):
            engine = self._get_or_create_engine()
            return engine.perform_action(action_name, participants, states=states, properties=properties, action_value=float(action_value))
        # English/Arabic aliases
        env['perform'] = _perform_api
        env['perform_action'] = _perform_api
        env['do'] = _perform_api
        env['execute'] = _perform_api
        env['نفذ'] = _perform_api
        env['افعل'] = _perform_api

        # Groups helpers
        def _define_group(name, members):
            engine = self._get_or_create_engine()
            engine.define_group(name, members)
        def _add_to_group(name, members):
            engine = self._get_or_create_engine()
            engine.add_to_group(name, members)
        env['define_group'] = _define_group
        env['add_to_group'] = _add_to_group
        env['عرّف_مجموعة'] = _define_group
        env['أضف_إلى_مجموعة'] = _add_to_group

        # Quick setters for states/properties
        def _set_state(entity, key, value):
            engine = self._get_or_create_engine()
            return engine.set_state(entity, key, float(value))
        def _set_property(entity, key, value):
            engine = self._get_or_create_engine()
            return engine.set_property(entity, key, float(value))
        env['set_state'] = _set_state
        env['set_property'] = _set_property
        env['عين_حالة'] = _set_state
        env['عين_خاصية'] = _set_property

    def interpret(self, node):
        """Interpret an AST node"""
        if isinstance(node, Program):
            return self.visit_program(node)
        elif isinstance(node, HybridBlock):
            return self.visit_hybrid_block(node)
        elif isinstance(node, LogicalFact):
            return self.visit_logical_fact(node)
        elif isinstance(node, LogicalRule):
            return self.visit_logical_rule(node)
        elif isinstance(node, LogicalQuery):
            return self.visit_logical_query(node)
        elif isinstance(node, LogicalIfStatement):
            return self.visit_logical_if_statement(node)
        elif isinstance(node, QueryExpression):
            return self.visit_query_expression(node)
        elif isinstance(node, EntityDef):
            return self.visit_entity_def(node)
        elif isinstance(node, ApplyActionStmt):
            return self.visit_apply_action_stmt(node)
        elif isinstance(node, ImportStatement):
            return self.visit_import_statement(node)
        elif isinstance(node, FromImportStatement):
            return self.visit_from_import_statement(node)
        else:
            # Delegate to traditional interpreter
            return self.traditional.interpret(node)
    class _BayanModuleProxy:
        def __init__(self, module_interpreter):
            self._mod = module_interpreter.traditional

        def __getattr__(self, name):
            # Classes
            if name in self._mod.classes:
                def _ctor(*args):
                    return self._mod.class_system.create_object(name, list(args))
                return _ctor
            # Functions
            if name in self._mod.functions:
                func_def = self._mod.functions[name]
                def _fn(*args):
                    old_local = self._mod.local_env
                    self._mod.local_env = {}
                    try:
                        # Bind params with support for Parameter objects
                        from .ast_nodes import Parameter

                        param_names = []
                        for param in func_def.parameters:
                            if isinstance(param, Parameter):
                                param_names.append(param.name)
                            else:
                                # Legacy format: parameter is just a string
                                param_names.append(param)

                        # Bind positional arguments
                        for i, arg in enumerate(args):
                            if i < len(param_names):
                                self._mod.local_env[param_names[i]] = arg

                        # Bind default values for missing parameters
                        for param in func_def.parameters:
                            if isinstance(param, Parameter):
                                if param.name not in self._mod.local_env and param.has_default():
                                    self._mod.local_env[param.name] = self._mod.interpret(param.default_value)

                        res = self._mod.interpret(func_def.body)
                        return res
                    except Exception as e:
                        if e.__class__.__name__ == 'ReturnValue':
                            return getattr(e, 'value', None)
                        raise
                    finally:
                        self._mod.local_env = old_local
                return _fn
            # Variables in global env
            if name in self._mod.global_env:
                return self._mod.global_env[name]
            raise AttributeError(f"Module has no attribute '{name}'")

    def _find_bayan_module_path(self, module_name):
        import os
        rel_path = module_name.replace('.', os.sep) + '.bayan'
        for base in self._bayan_module_paths:
            candidate = os.path.join(base, rel_path)
            if os.path.isfile(candidate):
                return candidate
        return None

    def _load_bayan_module(self, module_name):
        # Cache
        if module_name in self._bayan_module_cache:
            return self._bayan_module_cache[module_name]
        path = self._find_bayan_module_path(module_name)
        if not path:
            return None
        # Lazy imports to avoid cycles
        from .lexer import HybridLexer
        from .parser import HybridParser
        from .hybrid_interpreter import HybridInterpreter
        with open(path, 'r', encoding='utf-8') as f:
            code = f.read()
        lexer = HybridLexer(code)
        tokens = lexer.tokenize()
        parser = HybridParser(tokens)
        ast = parser.parse()
        mod_interp = HybridInterpreter()
        mod_interp.interpret(ast)
        proxy = self._BayanModuleProxy(mod_interp)
        self._bayan_module_cache[module_name] = (mod_interp, proxy)
        return (mod_interp, proxy)

    def visit_import_statement(self, node):
        # Try Bayan module first
        loaded = self._load_bayan_module(node.module_name)
        if loaded:
            _, proxy = loaded
            name = node.alias if node.alias else node.module_name
            env = self.traditional.local_env if self.traditional.local_env is not None else self.traditional.global_env
            env[name] = proxy
            return None
        # Fallback to Python import via traditional interpreter
        return self.traditional.visit_import_statement(node)

    def visit_from_import_statement(self, node):
        loaded = self._load_bayan_module(node.module_name)
        if loaded:
            mod_interp, _ = loaded
            env = self.traditional.local_env if self.traditional.local_env is not None else self.traditional.global_env
            for name in node.names:
                if name in mod_interp.traditional.classes:
                    # Copy class definition and register
                    cls_def = mod_interp.traditional.classes[name]
                    self.traditional.classes[name] = cls_def
                    self.class_system.register_class(cls_def)
                elif name in mod_interp.traditional.functions:
                    func_def = mod_interp.traditional.functions[name]
                    self.traditional.functions[name] = func_def
                elif name in mod_interp.traditional.global_env:
                    env[name] = mod_interp.traditional.global_env[name]
                else:
                    raise ImportError(f"Cannot import name '{name}' from '{node.module_name}'")
            return None
        return self.traditional.visit_from_import_statement(node)


    def visit_program(self, node):
        """Visit a program node"""
        result = None
        for statement in node.statements:
            result = self.interpret(statement)
        return result

    def visit_hybrid_block(self, node):
        """Visit a hybrid block"""
        # First, execute traditional statements
        traditional_result = None
        for stmt in node.traditional_stmts:
            traditional_result = self.interpret(stmt)

        # Then, add logical rules and facts
        for stmt in node.logical_stmts:
            self.interpret(stmt)

        return traditional_result

    def visit_logical_fact(self, node):
        """Visit a logical fact"""
        fact = Fact(node.predicate)
        self.logical.add_fact(fact)
        return None

    def visit_logical_rule(self, node):
        """Visit a logical rule"""
        rule = Rule(node.head, node.body)
        self.logical.add_rule(rule)
        return None

    def visit_logical_query(self, node):
        """Visit a logical query"""
        solutions = self.logical.query(node.goal)

        # Convert solutions to dictionaries
        results = []
        for substitution in solutions:
            result_dict = {}
            for var_name, value in substitution.bindings.items():
                result_dict[var_name] = value
            results.append(result_dict)

        return results

    def visit_logical_if_statement(self, node):
        """Visit a logical if statement"""
        # Try to solve the condition as a logical query
        if isinstance(node.condition, LogicalQuery):
            solutions = self.logical.query(node.condition.goal)

            if solutions:
                # If solutions found, execute then branch
                return self.interpret(node.then_branch)
            elif node.else_branch:
                # Otherwise, execute else branch
                return self.interpret(node.else_branch)
        else:
            # Traditional if statement
            condition_result = self.interpret(node.condition)

            if condition_result:
                return self.interpret(node.then_branch)
            elif node.else_branch:
                return self.interpret(node.else_branch)

        return None

    def visit_query_expression(self, node):
        """Visit a query expression"""
        solutions = self.logical.query(node.goal)

        # Convert solutions to dictionaries
        results = []
        for substitution in solutions:
            result_dict = {}
            for var_name, value in substitution.bindings.items():
                result_dict[var_name] = value
            results.append(result_dict)
        return results

    def _get_or_create_engine(self):
        env = self.traditional.global_env
        if 'entity_engine' not in env:
            env['entity_engine'] = EntityEngine(self.logical)
        return env['entity_engine']

    def visit_entity_def(self, node):
        """Create/extend an entity from an EntityDef node."""
        engine = self._get_or_create_engine()
        # Evaluate body dict (keys likely strings)
        body = self.traditional.interpret(node.body)
        if not isinstance(body, dict):
            raise TypeError("Entity body must be a dict-like structure")
        # Bilingual keys support
        def k(*names):
            for n in names:
                if n in body:
                    return n
            return None
        name = node.name
        states = body.get(k('states', 'حالات')) or {}
        properties = body.get(k('properties', 'خصائص')) or {}
        reactions = body.get(k('reactions', 'ردود_أفعال')) or {}
        actions = body.get(k('actions', 'أفعال')) or {}
        # Create the entity with initial states/properties/reactions
        engine.create_entity(name, states=states, properties=properties, reactions=reactions)
        # Define actions for this actor, if any
        if isinstance(actions, dict):
            for act_name, spec in actions.items():
                if not isinstance(spec, dict):
                    continue
                power = spec.get('power')
                if power is None:
                    power = spec.get('قوة', 1.0)
                effects = spec.get('effects') or spec.get('تأثيرات') or []
                engine.define_action(name, act_name, power=float(power), effects=effects)
        return None

    def visit_apply_action_stmt(self, node):
        """Apply an action defined on an actor to a target entity."""
        engine = self._get_or_create_engine()
        actor = node.actor_name
        action = node.action_name
        # Resolve target name. Accept string literal, or identifier fallback to its name.
        from .ast_nodes import Variable, String
        target_name = None
        if isinstance(node.target_expr, String):
            target_name = node.target_expr.value
        elif isinstance(node.target_expr, Variable):
            # Try to resolve variable from env; fallback to its symbol
            if self.traditional.local_env and node.target_expr.name in self.traditional.local_env:
                target_name = self.traditional.local_env[node.target_expr.name]
            elif node.target_expr.name in self.traditional.global_env:
                target_name = self.traditional.global_env[node.target_expr.name]
            else:
                target_name = node.target_expr.name
        else:
            # Evaluate to a value and stringify
            val = self.traditional.interpret(node.target_expr)
            target_name = str(val)
        # Named args
        action_value = 1.0
        if node.named_args:
            if 'action_value' in node.named_args:
                action_value = float(self.traditional.interpret(node.named_args['action_value']))
            elif 'قيمة_الفعل' in node.named_args:
                action_value = float(self.traditional.interpret(node.named_args['قيمة_الفعل']))
        engine.apply_action(actor, action, target_name, action_value=action_value)
        return None


