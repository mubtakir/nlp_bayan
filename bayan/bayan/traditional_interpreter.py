"""
Traditional Interpreter for Bayan Language
مفسر تقليدي للغة بيان
"""

import random
import re

from .ast_nodes import *
from .object_system import ClassSystem, BayanObject
from .import_system import ImportSystem

class ReturnValue(Exception):
    """Exception to handle return statements"""
    def __init__(self, value):
        self.value = value

class BreakException(Exception):
    """Exception to handle break statements"""
    pass

class ContinueException(Exception):
    """Exception to handle continue statements"""
    pass

class YieldValue(Exception):
    """Exception to handle yield expressions in generators"""
    def __init__(self, value):
        self.value = value

class BayanRuntimeError(Exception):
    """Runtime error that carries a Bayan stack trace"""
    pass

class BayanException(Exception):
    """Exception used for Bayan raise/try/except"""
    def __init__(self, value=None):
        self.value = value



class TraditionalInterpreter:
    """Interpreter for traditional programming constructs"""

    class BayanCoroutine:
        """Simple coroutine object for async function calls."""
        def __init__(self, interpreter, func_def, args, named_args):
            self.interpreter = interpreter
            self.func_def = func_def
            self.args = args
            self.named_args = named_args or {}

        def run(self):
            """Execute the coroutine synchronously"""
            interp = self.interpreter
            # Save and switch local environment
            old_local_env = interp.local_env
            interp.local_env = {}
            try:
                # Resolve parameters (support Parameter objects or raw names)
                parameters = getattr(self.func_def, 'parameters', getattr(self.func_def, 'params', []))
                param_names = []
                for p in parameters:
                    if isinstance(p, Parameter):
                        param_names.append(p.name)
                    else:
                        param_names.append(p)

                # Bind positional arguments
                for i, arg in enumerate(self.args):
                    if i < len(param_names):
                        interp.local_env[param_names[i]] = arg

                # Bind named arguments
                for name, value in self.named_args.items():
                    if name in param_names:
                        interp.local_env[name] = value

                # Bind defaults
                for p in parameters:
                    if isinstance(p, Parameter):
                        if p.name not in interp.local_env and p.has_default():
                            interp.local_env[p.name] = interp.interpret(p.default_value)
                        elif p.name not in interp.local_env and not p.has_default():
                            raise RuntimeError(f"Missing required parameter: {p.name}")

                # Execute body
                try:
                    result = interp.interpret(self.func_def.body)
                except ReturnValue as ret:
                    result = ret.value
                return result
            finally:
                interp.local_env = old_local_env

        def __await__(self):
            """Make this a proper awaitable"""
            result = self.run()
            if False:
                yield None
            return result

    def __init__(self):
        self.global_env = {}
        self.local_env = None
        self.functions = {}
        self.classes = {}
        self.class_system = ClassSystem(self)
        self.import_system = ImportSystem()
        self.logical_engine = None
        # Track current owner class for super() resolution in MRO
        self._owner_stack = []
        # Bayan runtime call stack of (node_type, line, column, filename)
        self._call_stack = []
        # Optional source buffer for code-frame rendering
        self._source_lines = None
        self._source_filename = None
        # Track async functions
        self._async_functions = set()
        # Reactive programming state
        self._reactive_vars = set()  # Set of reactive variable names
        self._watchers = []  # List of (variables, callback) tuples
        self._computed_props = {}  # Dict of {prop_name: (expression, dependencies)}

        # Cognitive-Semantic Model state
        self._cognitive_entities = {}  # Dict of {name: {properties}}
        self._cognitive_events = {}  # Dict of {name: event_config}
        self._linguistic_patterns = {}  # Dict of {name: pattern_config}
        self._ideas = {}  # Dict of {name: idea_config}
        self._conceptual_blueprints = {}  # Dict of {name: blueprint_config}

        # Semantic Programming & Knowledge Management state
        self._semantic_meanings = {}  # Dict of {name: {relationships}}
        self._knowledge_info = {}  # Dict of {name: {content, context}}
        self._inference_rules = {}  # Dict of {name: {if, then}}
        self._evolving_knowledge = {}  # Dict of {name: {current, history, future}}
        self._ontologies = {}  # Dict of {name: {root, taxonomy}}
        self._semantic_memory = []  # List of stored memories
        self._concepts = {}  # Dict of {name: properties}
        self._narratives = {}  # Dict of {name: {characters, events, structure}}
        self._current_context = {}  # Current context state

        # Existential Model state
        self._domains = {}  # Dict of {name: domain_config}
        self._environments = {}  # Dict of {name: environment_config}
        self._existential_beings = {}  # Dict of {name: being_config}
        self._domain_relations = {}  # Dict of {name: relation_config}
        self._domain_actions = {}  # Dict of {name: action_config}
        self._metaphorical_meanings = {}  # Dict of {name: meaning_config}
        self._domain_laws = {}  # Dict of {name: law_config}

        # RNG for sampling features
        self._rng = random.Random()

        # Error reporting configuration
        self._err_color = False
        self._err_context_lines = 1
        self._err_tabstop = 4

        # Register built-in types in global environment
        self.global_env['str'] = str
        self.global_env['int'] = int
        self.global_env['float'] = float
        self.global_env['bool'] = bool
        self.global_env['list'] = list
        self.global_env['dict'] = dict
        self.global_env['tuple'] = tuple
        self.global_env['set'] = set
        self.global_env['type'] = type
        self.global_env['object'] = object
        # Conceptual blueprint registry for conceptual LM tooling
        self.global_env['_conceptual_blueprints'] = self._conceptual_blueprints

        # Sampling helpers
        self.global_env['seed'] = self._rng.seed
        self.global_env['uniform'] = lambda a, b: self._rng.uniform(float(a), float(b))
        self.global_env['normal'] = lambda mu, sigma: self._rng.gauss(float(mu), float(sigma))
        self.global_env['bernoulli'] = lambda p: 1 if self._rng.random() < float(p) else 0

        def _categorical(mapping: dict):
            """Sample from categorical distribution: Categorical({"A": 0.6, "B": 0.3, "C": 0.1})"""
            items = list(mapping.items())
            if not items:
                return None
            # Normalize weights and sample
            values, weights = zip(*items)
            total = sum(float(w) for w in weights)
            if total <= 0:
                # fallback: uniform over items
                # Use data.rand() if available (for reproducibility with data.set_seed)
                try:
                    rand_fn = self.global_env.get('rand', self._rng.random)
                    idx = int(rand_fn() * len(values))
                except:
                    idx = int(self._rng.random() * len(values))
                return values[idx]
            # Use data.rand() if available (for reproducibility with data.set_seed)
            try:
                rand_fn = self.global_env.get('rand', self._rng.random)
                r = rand_fn() * total
            except:
                r = self._rng.random() * total
            acc = 0.0
            for v, w in zip(values, weights):
                acc += float(w)
                if r <= acc:
                    return v
            return values[-1]

        self.global_env['Categorical'] = _categorical
        self.global_env['categorical'] = _categorical
        def _choose_weighted(mapping: dict):
            items = list(mapping.items())
            if not items:
                return None
            # Normalize weights and sample
            values, weights = zip(*items)
            total = sum(float(w) for w in weights)
            if total <= 0:
                # fallback: uniform over items
                idx = int(self._rng.random() * len(values))
                return values[idx]
            r = self._rng.random() * total
            acc = 0.0
            for v, w in zip(values, weights):
                acc += float(w)
                if r <= acc:
                    return v
            return values[-1]
        self.global_env['choose_weighted'] = _choose_weighted

        # Approximate equality helper
        def _approx_eq(a, b, eps=None, kind=None):
            # Numeric approx
            def _is_number(x):
                return isinstance(x, (int, float))
            if eps is None:
                eps = self.global_env.get('approx_eps', 1e-6)
            if kind is None:
                kind = self.global_env.get('similarity_kind_default', 'syn')
            # If both are numeric or can be coerced
            if _is_number(a) and _is_number(b):
                return abs(float(a) - float(b)) <= float(eps)
            # String-like semantic approx via logical 'close/3'
            if (isinstance(a, str) or isinstance(a, (int, float))) and (isinstance(b, str) or isinstance(b, (int, float))):
                sa = str(a)
                sb = str(b)
                eng = self.logical_engine
                if eng is not None and 'close' in eng.knowledge_base:
                    # Try close/3 using default threshold for kind
                    from .logical_engine import Predicate, Term
                    goal = Predicate('close', [Term(sa), Term(sb), Term(str(kind))])
                    sols = eng.query(goal)
                    return len(sols) > 0
                # Fallback: plain equality
                return sa == sb
            # Fallback
            return a == b
        self.global_env['approx_eq'] = _approx_eq
        self.global_env['approx_eps'] = 1e-2
        self.global_env['similarity_kind_default'] = 'syn'

        # Template/Match helpers
        def _compile_template(tpl: str):
            if not isinstance(tpl, str):
                tpl = str(tpl)
            s = tpl
            parts = []
            fields = []
            i = 0
            last = 0
            while i < len(s):
                if s[i] == '{':
                    # flush preceding text
                    if i > last:
                        parts.append(re.escape(s[last:i]))
                    j = s.find('}', i + 1)
                    if j == -1:
                        # no closing brace; treat literally
                        parts.append(re.escape(s[i:]))
                        i = len(s)
                        break
                    content = s[i + 1:j]
                    # parse name[:regex]
                    if ':' in content:
                        name, rx = content.split(':', 1)
                        name = name.strip()
                        rx = rx.strip()
                        if not rx:
                            rx = '.+?'
                    else:
                        name = content.strip()
                        rx = '.+?'
                    if not name:
                        # anonymous hole: generate a name
                        name = f"_f{len(fields)}"
                    fields.append(name)
                    parts.append(f"(?P<{name}>{rx})")
                    i = j + 1
                    last = i
                else:
                    i += 1
            if last < len(s):
                parts.append(re.escape(s[last:]))
            pattern = '^' + ''.join(parts) + '$'
            try:
                regex = re.compile(pattern)
            except re.error:
                # fallback: match literally if user provided broken regex
                regex = re.compile('^' + re.escape(s) + '$')
                fields = []
            return {'__template__': True, 'src': tpl, 'fields': fields, 'regex': regex}

        def _is_template(obj):
            return isinstance(obj, dict) and obj.get('__template__') is True and 'regex' in obj

        def _match_template(tpl_or_str, text):
            tpl_obj = tpl_or_str if _is_template(tpl_or_str) else _compile_template(tpl_or_str)
            m = tpl_obj['regex'].match(str(text))
            if not m:
                return None
            return dict(m.groupdict())

        def _render_template(tpl_or_str, mapping: dict):
            tpl_obj = tpl_or_str if _is_template(tpl_or_str) else _compile_template(tpl_or_str)
            src = tpl_obj.get('src') if _is_template(tpl_or_str) else str(tpl_or_str)
            s = src
            out = []
            i = 0
            last = 0
            while i < len(s):
                if s[i] == '{':
                    if i > last:
                        out.append(s[last:i])
                    j = s.find('}', i + 1)
                    if j == -1:
                        out.append(s[i:])
                        i = len(s)
                        break
                    content = s[i + 1:j]
                    name = content.split(':', 1)[0].strip()
                    val = mapping.get(name)
                    if val is None:
                        # keep placeholder if missing
                        out.append(s[i:j + 1])
                    else:
                        out.append(str(val))
                    i = j + 1
                    last = i
                else:
                    i += 1
            if last < len(s):
                out.append(s[last:])
            return ''.join(out)

        self.global_env['template'] = _compile_template
        self.global_env['match'] = _match_template
        self.global_env['render'] = _render_template


    def set_source(self, code: str, filename: str | None = None):
        """Set current source buffer for error code-frames."""
        # Normalize line endings and keep lines including spaces
        self._source_lines = code.splitlines()
        self._source_filename = filename

    def set_error_formatting(self, *, colors: bool | None = None, context_lines: int | None = None, tabstop: int | None = None):
        """Configure error display options.
        - colors: enable ANSI color output
        - context_lines: number of lines before/after the error line to show
        - tabstop: tab width for caret alignment
        """
        if colors is not None:
            self._err_color = bool(colors)
        if context_lines is not None and context_lines >= 0:
            self._err_context_lines = int(context_lines)


        if tabstop is not None and tabstop >= 1:
            self._err_tabstop = int(tabstop)

    def _truthy(self, value):
        """Bayan truthiness: use __bool__ or __len__ on BayanObject if available."""
        if isinstance(value, BayanObject):
            if value.has_method('__bool__'):
                try:
                    res = value.call_method('__bool__', [])
                    return bool(res)
                except Exception:
                    return True
            if value.has_method('__len__'):
                try:
                    res = value.call_method('__len__', [])
                    return bool(res)
                except Exception:
                    return True
            return True
        return bool(value)

    def _to_iterable(self, obj):
        """Convert BayanObject with __iter__ into a Python iterable if possible."""
        if isinstance(obj, BayanObject):
            if obj.has_method('__iter__'):
                it = obj.call_method('__iter__', [])
                return self._to_iterable(it)
            else:
                raise TypeError("Object is not iterable")
        return obj

    def interpret(self, node):
        """Interpret an AST node with Bayan stack tracking"""
        # Push current frame (node type + optional position)
        self._call_stack.append((type(node).__name__, getattr(node, 'line', None), getattr(node, 'column', None), getattr(node, 'filename', None)))
        try:
            return self._interpret_core(node)
        except Exception as e:
            # Control-flow exceptions should not be wrapped
            if isinstance(e, (ReturnValue, BreakException, ContinueException, YieldValue, BayanException, BayanRuntimeError, ContractError)):
                raise
            frames = list(self._call_stack)
            trace = " -> ".join(
                (f"{name}@{fn}:{ln}:{col}" if fn else f"{name}@{ln}:{col}") if ln is not None else name
                for (name, ln, col, fn) in frames
            )
            # Try to add a code-frame for the most recent frame with position
            code_frame = ""
            try:
                for (name, ln, col, fn) in reversed(frames):
                    if ln is not None and col is not None:
                        # Only render frame if we have a matching source buffer
                        if self._source_lines is not None and (self._source_filename == fn or self._source_filename is None):
                            code_frame = self._build_code_frame(fn, int(ln), int(col))
                        break
            except Exception:
                # Never fail error reporting
                code_frame = ""
            raise BayanRuntimeError(f"{e.__class__.__name__}: {e}\nBayan stack: {trace}{code_frame}")
        finally:
            self._call_stack.pop()


    def _style(self, text: str, *kinds: str) -> str:
        if not self._err_color:
            return text
        code_map = {
            'dim': '2',
            'bold': '1',
            'red': '31',
            'cyan': '36',
        }
        codes = [code_map.get(k) for k in kinds if code_map.get(k)]
        if not codes:
            return text
        start = "\x1b[" + ";".join(codes) + "m"
        end = "\x1b[0m"
        return f"{start}{text}{end}"

    def _display_width(self, s: str, tabstop: int = 4) -> int:
        import unicodedata
        w = 0
        for ch in s:
            if ch == '\t':
                w += tabstop - (w % tabstop)
            elif unicodedata.combining(ch):
                continue
            else:
                ea = unicodedata.east_asian_width(ch)
                w += 2 if ea in ('W', 'F') else 1
        return w

    def _caret_indent_for(self, s: str, col_char_index_1based: int) -> str:
        # Compute display width up to character index col-1 (1-based char index)
        prefix = s[:max(0, col_char_index_1based - 1)]
        spaces = self._display_width(prefix, tabstop=self._err_tabstop)
        return ' ' * max(0, spaces)

    def _build_code_frame(self, filename: str | None, line: int, col: int) -> str:
        """Return a numbered code frame with caret.
        - Shows ±context_lines around the error
        - Highlights current line with '>' and optional ANSI colors
        """
        if self._source_lines is None:
            return ''
        file_label = filename if filename is not None else (self._source_filename if self._source_filename else '<memory>')
        start = max(1, line - self._err_context_lines)
        end = min(len(self._source_lines), line + self._err_context_lines)
        pad = len(str(end))
        header = f"\n\nFile {file_label}:{line}:{col}"
        if self._err_color:
            header = self._style(header, 'dim')
        lines_out = [header]
        for i in range(start, end + 1):
            text = self._source_lines[i - 1]
            prefix = '>' if i == line else ' '
            numbered = f"{prefix}{str(i).rjust(pad)} | {text}"
            if self._err_color:
                if i == line:
                    numbered = self._style(numbered, 'bold')
                else:
                    numbered = self._style(numbered, 'dim')
            lines_out.append(numbered)
            if i == line:
                caret_indent = self._caret_indent_for(text, col)
                caret = '^'
                if self._err_color:
                    caret = self._style(caret, 'red', 'bold')
                lines_out.append(' ' * (1 + pad + 3) + caret_indent + caret)
        return '\n'.join(lines_out)

    def _interpret_core(self, node):
        """Core interpret dispatch without stack handling"""
        if isinstance(node, Program):
            return self.visit_program(node)
        elif isinstance(node, Block):
            return self.visit_block(node)
        elif isinstance(node, Assignment):
            return self.visit_assignment(node)
        elif isinstance(node, BinaryOp):
            return self.visit_binary_op(node)
        elif isinstance(node, UnaryOp):
            return self.visit_unary_op(node)
        elif isinstance(node, Number):
            return node.value
        elif isinstance(node, String):
            return node.value
        elif isinstance(node, Boolean):
            return node.value
        elif isinstance(node, NoneLiteral):
            # Bayan None literal maps directly to Python None
            return None

        elif isinstance(node, CollectExpr):
            return self.visit_collect_expr(node)
        elif isinstance(node, TopkExpr):
            return self.visit_topk_expr(node)
        elif isinstance(node, ArgmaxExpr):
            return self.visit_argmax_expr(node)
        elif isinstance(node, ChooseExpr):
            return self.visit_choose_expr(node)
        elif isinstance(node, SampleAssign):
            return self.visit_sample_assign(node)
        elif isinstance(node, Variable):
            return self.visit_variable(node)
        elif isinstance(node, List):
            return self.visit_list(node)
        elif isinstance(node, ListComprehension):
            return self.visit_list_comprehension(node)
        elif isinstance(node, Dict):
            return self.visit_dict(node)
        elif isinstance(node, Tuple):
            return self.visit_tuple(node)
        elif isinstance(node, Set):
            return self.visit_set(node)
        elif isinstance(node, FunctionCall):
            return self.visit_function_call(node)
        elif isinstance(node, FunctionDef):
            return self.visit_function_def(node)
        elif isinstance(node, ClassDef):
            return self.visit_class_def(node)
        elif isinstance(node, IfStatement):
            return self.visit_if_statement(node)
        elif isinstance(node, ForLoop):
            return self.visit_for_loop(node)
        elif isinstance(node, WhileLoop):
            return self.visit_while_loop(node)
        elif isinstance(node, ReturnStatement):
            return self.visit_return_statement(node)
        elif isinstance(node, BreakStatement):
            raise BreakException()
        elif isinstance(node, ContinueStatement):
            raise ContinueException()
        elif isinstance(node, PrintStatement):
            return self.visit_print_statement(node)
        elif isinstance(node, SimilarityDecl):
            return self.visit_similarity_decl(node)
        elif isinstance(node, AttributeAccess):
            return self.visit_attribute_access(node)
        elif isinstance(node, SubscriptAccess):
            return self.visit_subscript_access(node)
        elif isinstance(node, AttributeAssignment):
            return self.visit_attribute_assignment(node)
        elif isinstance(node, SubscriptAssignment):
            return self.visit_subscript_assignment(node)
        elif isinstance(node, MethodCall):
            return self.visit_method_call(node)
        elif isinstance(node, SelfReference):
            return self.visit_self_reference(node)
        elif isinstance(node, SuperCall):
            return self.visit_super_call(node)
        elif isinstance(node, ImportStatement):
            return self.visit_import_statement(node)
        elif isinstance(node, FromImportStatement):
            return self.visit_from_import_statement(node)
        elif isinstance(node, RaiseStatement):
            return self.visit_raise_statement(node)
        elif isinstance(node, TryExceptFinally):
            return self.visit_try_except_finally(node)
        elif isinstance(node, AsyncFunctionDef):
            return self.visit_async_function_def(node)
        elif isinstance(node, AwaitExpr):
            return self.visit_await_expr(node)
        elif isinstance(node, YieldExpr):
            return self.visit_yield_expr(node)
        elif isinstance(node, WithStatement):
            return self.visit_with_statement(node)
        elif isinstance(node, OnceStatement):
            return self.visit_once_statement(node)
        elif isinstance(node, OnceGoal):
            return self.visit_once_goal(node)
        elif isinstance(node, LimitStatement):
            return self.visit_limit_statement(node)
        elif isinstance(node, LimitGoal):
            return self.visit_limit_goal(node)
        elif isinstance(node, MatchInAs):
            return self.visit_match_in_as(node)
        elif isinstance(node, MatchStatement):
            return self.visit_match_statement(node)
        elif isinstance(node, TemporalBlock):
            return self.visit_temporal_block(node)
        elif isinstance(node, WithinBlock):
            return self.visit_within_block(node)
        elif isinstance(node, ScheduleBlock):
            return self.visit_schedule_block(node)
        elif isinstance(node, ReactiveDeclaration):
            return self.visit_reactive_declaration(node)
        elif isinstance(node, WatchBlock):
            return self.visit_watch_block(node)
        elif isinstance(node, ComputedProperty):
            return self.visit_computed_property(node)
        elif isinstance(node, DelayStatement):
            return self.visit_delay_statement(node)
        elif isinstance(node, WhereClause):
            return self.visit_where_clause(node)
        elif isinstance(node, RequiresClause):
            return self.visit_requires_clause(node)
        elif isinstance(node, EnsuresClause):
            return self.visit_ensures_clause(node)
        elif isinstance(node, InvariantClause):
            return self.visit_invariant_clause(node)
        elif isinstance(node, PipelineOp):
            return self.visit_pipeline_op(node)
        elif isinstance(node, ComposeOp):
            return self.visit_compose_op(node)
        elif isinstance(node, CognitiveEntity):
            return self.visit_cognitive_entity(node)
        elif isinstance(node, CognitiveEvent):
            return self.visit_cognitive_event(node)
        elif isinstance(node, TriggerEvent):
            return self.visit_trigger_event(node)
        elif isinstance(node, ConcurrentEvents):
            return self.visit_concurrent_events(node)
        elif isinstance(node, LinguisticPattern):
            return self.visit_linguistic_pattern(node)
        elif isinstance(node, IdeaDef):
            return self.visit_idea_def(node)
        elif isinstance(node, ConceptualBlueprint):
            return self.visit_conceptual_blueprint(node)
        # Semantic Programming & Knowledge Management
        elif isinstance(node, SemanticMeaning):
            return self.visit_semantic_meaning(node)
        elif isinstance(node, SemanticQuery):
            return self.visit_semantic_query(node)
        elif isinstance(node, KnowledgeInfo):
            return self.visit_knowledge_info(node)
        elif isinstance(node, InferenceRule):
            return self.visit_inference_rule(node)
        elif isinstance(node, InferFrom):
            return self.visit_infer_from(node)
        elif isinstance(node, Contradiction):
            return self.visit_contradiction(node)
        elif isinstance(node, EvolvingKnowledge):
            return self.visit_evolving_knowledge(node)
        elif isinstance(node, Ontology):
            return self.visit_ontology(node)
        elif isinstance(node, SemanticMemory):
            return self.visit_semantic_memory(node)
        elif isinstance(node, SemanticSimilarity):
            return self.visit_semantic_similarity(node)
        elif isinstance(node, Concept):
            return self.visit_concept(node)
        elif isinstance(node, Narrative):
            return self.visit_narrative(node)
        elif isinstance(node, GenerateNarrative):
            return self.visit_generate_narrative(node)
        elif isinstance(node, CurrentContext):
            return self.visit_current_context(node)
        # Existential Model
        elif isinstance(node, Domain):
            return self.visit_domain(node)
        elif isinstance(node, GenericEnvironment):
            return self.visit_generic_environment(node)
        elif isinstance(node, ExistentialBeing):
            return self.visit_existential_being(node)
        elif isinstance(node, DomainRelation):
            return self.visit_domain_relation(node)
        elif isinstance(node, DomainAction):
            return self.visit_domain_action(node)
        elif isinstance(node, MetaphoricalMeaning):
            return self.visit_metaphorical_meaning(node)
        elif isinstance(node, DomainLaw):
            return self.visit_domain_law(node)
        elif isinstance(node, ExistentialQuery):
            return self.visit_existential_query(node)
        else:
            raise RuntimeError(f"Unknown node type: {type(node)}")

    def visit_program(self, node):
        """Visit a program node"""
        result = None
        for statement in node.statements:
            result = self.interpret(statement)
        return result

    def visit_block(self, node):
        """Visit a block node"""
        result = None
        for statement in node.statements:
            result = self.interpret(statement)
        return result

    def visit_assignment(self, node):
        """Visit an assignment node"""
        value = self.interpret(node.value)

        # Check if this is an attribute assignment (obj.attr = value)
        if '.' in node.name:
            parts = node.name.split('.')
            obj_name = parts[0]
            attr_name = parts[1]

            env = self.local_env if self.local_env is not None else self.global_env
            if obj_name in env:
                obj = env[obj_name]
                if isinstance(obj, BayanObject):
                    obj.set_attribute(attr_name, value)
                    return value
            elif obj_name in self.global_env:
                obj = self.global_env[obj_name]
                if isinstance(obj, BayanObject):
                    obj.set_attribute(attr_name, value)
                    return value

        # Use set_variable to trigger reactive updates
        self.set_variable(node.name, value)
        return value

    def visit_binary_op(self, node):
        """Visit a binary operation node"""
        left = self.interpret(node.left)
        right = self.interpret(node.right)

        # Helper to try dunder methods on BayanObject
        def _try_dunder(l, r, name, rname=None):
            if isinstance(l, BayanObject) and l.has_method(name):
                return l.call_method(name, [r])
            if rname and isinstance(r, BayanObject) and r.has_method(rname):
                return r.call_method(rname, [l])
            return None

        if node.operator == '+':
            res = _try_dunder(left, right, '__add__', '__radd__')
            return res if res is not None else (left + right)
        elif node.operator == '-':
            res = _try_dunder(left, right, '__sub__', '__rsub__')
            return res if res is not None else (left - right)
        elif node.operator == '*':
            res = _try_dunder(left, right, '__mul__', '__rmul__')
            return res if res is not None else (left * right)
        elif node.operator == '/':
            res = _try_dunder(left, right, '__truediv__', '__rtruediv__')
            return res if res is not None else (left / right)
        elif node.operator == '%':
            res = _try_dunder(left, right, '__mod__', '__rmod__')
            return res if res is not None else (left % right)
        elif node.operator == '==':
            res = _try_dunder(left, right, '__eq__')
            return res if res is not None else (left == right)
        elif node.operator == '!=':
            res = _try_dunder(left, right, '__ne__')
            if res is not None:
                return res
            # Fallback: negate __eq__ if provided
            eq_res = _try_dunder(left, right, '__eq__')
            return (not eq_res) if eq_res is not None else (left != right)
        elif node.operator == '<':
            res = _try_dunder(left, right, '__lt__')
            return res if res is not None else (left < right)
        elif node.operator == '>':
            res = _try_dunder(left, right, '__gt__')
            return res if res is not None else (left > right)
        elif node.operator == '<=':
            res = _try_dunder(left, right, '__le__')
            return res if res is not None else (left <= right)
        elif node.operator == '>=':
            res = _try_dunder(left, right, '__ge__')
            return res if res is not None else (left >= right)
        elif node.operator in ('~=','≈'):
            approx = self.global_env.get('approx_eq')
            if not callable(approx):
                raise RuntimeError("approx_eq runtime is not available")
            return approx(left, right)
        elif node.operator == 'in':
            # membership: left in right
            if isinstance(right, BayanObject) and right.has_method('__contains__'):
                return right.call_method('__contains__', [left])
            return left in right
        elif node.operator == 'and':
            # Preserve Python-like value return while using Bayan truthiness
            return right if self._truthy(left) else left
        elif node.operator == 'or':
            return left if self._truthy(left) else right
        else:
            raise RuntimeError(f"Unknown operator: {node.operator}")

    def visit_unary_op(self, node):
        """Visit a unary operation node"""
        operand = self.interpret(node.operand)

        if node.operator == '-':
            if isinstance(operand, BayanObject) and operand.has_method('__neg__'):
                return operand.call_method('__neg__', [])
            return -operand
        elif node.operator == 'not':
            return not self._truthy(operand)
        else:
            raise RuntimeError(f"Unknown unary operator: {node.operator}")

    def visit_variable(self, node):
        """Visit a variable node"""
        # Check if this is an attribute access (obj.attr)
        if '.' in node.name:
            parts = node.name.split('.')
            obj_name = parts[0]
            attr_name = parts[1]

            env = self.local_env if self.local_env is not None else self.global_env
            if obj_name in env:
                obj = env[obj_name]
                if isinstance(obj, BayanObject):
                    return obj.get_attribute(attr_name)
            elif obj_name in self.global_env:
                obj = self.global_env[obj_name]
                if isinstance(obj, BayanObject):
                    return obj.get_attribute(attr_name)

        env = self.local_env if self.local_env is not None else self.global_env

        if node.name in env:
            return env[node.name]
        elif node.name in self.global_env:
            return self.global_env[node.name]
        else:
            raise NameError(self._undefined_name_message(node.name))

    def _undefined_name_message(self, name: str) -> str:
        """Build a helpful undefined-name error message with suggestions."""
        # Collect candidate symbols from current scope
        candidates = set()
        if self.local_env:
            candidates.update(self.local_env.keys())
        candidates.update(self.global_env.keys())
        candidates.update(self.functions.keys())
        candidates.update(self.classes.keys())
        # Compute distances and keep best few
        scored = []
        for cand in candidates:
            try:
                d = self._levenshtein(name, str(cand), max_dist=3)
            except Exception:
                d = None
            if d is not None and d <= 3:
                scored.append((d, str(cand)))
        scored.sort(key=lambda x: (x[0], x[1]))
        suggestions = ", ".join(s for _, s in scored[:3])
        if suggestions:
            return f"Undefined variable: {name}. Did you mean: {suggestions}?"
        return f"Undefined variable: {name}"

    def _levenshtein(self, a: str, b: str, max_dist: int = 3) -> int | None:
        """Levenshtein distance with early exit; returns None if > max_dist."""
        if a == b:
            return 0
        # Ensure a is shorter
        if len(a) > len(b):
            a, b = b, a
        # If length diff already exceeds max_dist, skip
        if len(b) - len(a) > max_dist:
            return None
        previous = list(range(len(b) + 1))
        for i, ca in enumerate(a, start=1):
            current = [i]
            row_min = current[0]
            for j, cb in enumerate(b, start=1):
                ins = current[j-1] + 1
                dele = previous[j] + 1
                sub = previous[j-1] + (0 if ca == cb else 1)
                val = min(ins, dele, sub)
                current.append(val)
                if val < row_min:
                    row_min = val
            if row_min > max_dist:
                return None
            previous = current
        return previous[-1] if previous[-1] <= max_dist else None

    def _contains_yield(self, node):
        """Check if node contains yield expression"""
        from .ast_nodes import YieldExpr, Block, ForLoop, WhileLoop, IfStatement

        if isinstance(node, YieldExpr):
            return True
        if isinstance(node, Block):
            return any(self._contains_yield(stmt) for stmt in node.statements)
        if isinstance(node, ForLoop):
            return self._contains_yield(node.body)
        if isinstance(node, WhileLoop):
            return self._contains_yield(node.body)
        if isinstance(node, IfStatement):
            has_yield = self._contains_yield(node.then_block)
            if node.else_block:
                has_yield = has_yield or self._contains_yield(node.else_block)
            return has_yield
        if isinstance(node, list):
            return any(self._contains_yield(n) for n in node if hasattr(n, '__class__'))
        return False


    def visit_list(self, node):
        """Visit a list node"""
        return [self.interpret(elem) for elem in node.elements]

    def visit_tuple(self, node):
        """Visit a tuple node"""
        return tuple(self.interpret(elem) for elem in node.elements)

    def visit_set(self, node):
        """Visit a set node"""
        return set(self.interpret(elem) for elem in node.elements)

    def visit_list_pattern(self, node):
        """Visit a list pattern node [H|T]"""
        # Convert ListPattern to internal representation for logical engine
        head_elements = [self.interpret(elem) for elem in node.head_elements]
        tail = self.interpret(node.tail)

        # Return a special dict representation
        return {
            'list_pattern': True,
            'head': head_elements,
            'tail': tail
        }

    def visit_list_comprehension(self, node):
        """Evaluate a list comprehension."""
        iterable = self._to_iterable(self.interpret(node.iterable))
        result = []
        env = self.local_env if self.local_env is not None else self.global_env
        for value in iterable:
            env[node.var_name] = value
            if node.condition is not None:
                cond = self.interpret(node.condition)
                if not cond:
                    continue
            result.append(self.interpret(node.expr))
        return result

    def visit_dict(self, node):
        """Visit a dict node"""
        result = {}
        for key_node, value_node in node.pairs:
            key = self.interpret(key_node)
            value = self.interpret(value_node)
            result[key] = value
        return result

    def visit_function_call(self, node):
        """Visit a function call node"""
        # Check if this is a logical predicate call (contains logical variables)
        has_logical_vars = any(isinstance(arg, Variable) and arg.name.startswith('?') for arg in node.arguments)

        if has_logical_vars and hasattr(self, 'logical_engine'):
            # This is a logical query
            from .logical_engine import Predicate, Term

            # Convert arguments to logical terms
            logical_args = []
            for arg in node.arguments:
                if isinstance(arg, Variable):
                    if arg.name.startswith('?'):
                        # Logical variable
                        logical_args.append(Term(arg.name[1:], is_variable=True))
                    else:
                        # Regular variable - evaluate it
                        value = self.interpret(arg)
                        logical_args.append(Term(str(value), is_variable=False))
                else:
                    # Evaluate the argument
                    value = self.interpret(arg)
                    logical_args.append(Term(str(value), is_variable=False))

            # Create a logical predicate and query it
            predicate = Predicate(node.name, logical_args)
            solutions = self.logical_engine.query(predicate)

            # Return True if there are solutions, False otherwise
            return len(solutions) > 0

        # Check for semantic query functions
        if node.name in ['من_يدرس', 'who_studies', 'ما_هو', 'what_is']:
            args = [self.interpret(arg) for arg in node.arguments]
            return self._query_semantic_network(node.name, *args)
        elif node.name in ['تشابه', 'similarity']:
            if len(node.arguments) >= 2:
                concept1_name = self.interpret(node.arguments[0])
                concept2_name = self.interpret(node.arguments[1])

                # Get concepts from storage
                concept1 = self._concepts.get(concept1_name, concept1_name)
                concept2 = self._concepts.get(concept2_name, concept2_name)

                # Calculate similarity
                if isinstance(concept1, dict) and isinstance(concept2, dict):
                    # Count shared keys
                    keys1 = set(concept1.keys())
                    keys2 = set(concept2.keys())
                    shared = keys1.intersection(keys2)
                    total = keys1.union(keys2)

                    if len(total) == 0:
                        return 0.0

                    # Jaccard similarity
                    similarity = len(shared) / len(total)

                    # Also check value similarity for shared keys
                    value_matches = 0
                    for key in shared:
                        if concept1[key] == concept2[key]:
                            value_matches += 1

                    if len(shared) > 0:
                        value_similarity = value_matches / len(shared)
                        # Combine both similarities
                        similarity = (similarity + value_similarity) / 2

                    return similarity
                else:
                    # For non-dict concepts, just check equality
                    return 1.0 if concept1 == concept2 else 0.0
            else:
                raise RuntimeError(f"similarity() requires 2 arguments")
        elif node.name in ['بناءً_على', 'based_on']:
            # This is used in generate_narrative context
            if len(node.arguments) >= 1:
                return self.interpret(node.arguments[0])
            else:
                raise RuntimeError(f"based_on() requires 1 argument")

        # Check for built-in functions
        if node.name == 'len':
            arg = self.interpret(node.arguments[0])
            if isinstance(arg, BayanObject) and arg.has_method('__len__'):
                return arg.call_method('__len__', [])
            return len(arg)
        elif node.name == 'range':
            args = [self.interpret(arg) for arg in node.arguments]
            return list(range(*args))
        elif node.name == 'str':
            arg = self.interpret(node.arguments[0])
            if isinstance(arg, BayanObject) and arg.has_method('__str__'):
                return arg.call_method('__str__', [])
            return str(arg)
        elif node.name == 'repr':
            arg = self.interpret(node.arguments[0])
            if isinstance(arg, BayanObject) and arg.has_method('__repr__'):
                return arg.call_method('__repr__', [])
            return repr(arg)
        elif node.name == 'isinstance':
            args = [self.interpret(arg) for arg in node.arguments]
            return isinstance(*args)
        elif node.name == 'type':
            arg = self.interpret(node.arguments[0])
            return type(arg)
        elif node.name == 'callable':
            arg = self.interpret(node.arguments[0])
            return callable(arg)
        elif node.name == 'hasattr':
            args = [self.interpret(arg) for arg in node.arguments]
            return hasattr(*args)
        elif node.name == 'getattr':
            args = [self.interpret(arg) for arg in node.arguments]
            return getattr(*args)
        elif node.name == 'setattr':
            args = [self.interpret(arg) for arg in node.arguments]
            setattr(*args)
            return None
        elif node.name == 'bool':
            arg = self.interpret(node.arguments[0])
            return bool(self._truthy(arg))
        elif node.name == 'int':
            arg = self.interpret(node.arguments[0])
            return int(arg)
        elif node.name == 'float':
            arg = self.interpret(node.arguments[0])
            return float(arg)
        elif node.name == 'list':
            arg = self.interpret(node.arguments[0])
            # Check if it's a generator
            if hasattr(arg, '__iter__') and hasattr(arg, '__next__'):
                result = []
                try:
                    while True:
                        result.append(next(arg))
                except StopIteration:
                    pass
                return result
            return list(arg)
        elif node.name == 'dict':
            return {}
        elif node.name == 'sum':
            args = [self.interpret(arg) for arg in node.arguments]
            if len(args) == 1:
                return sum(args[0])
            elif len(args) == 2:
                return sum(args[0], args[1])  # sum(iterable, start)
            else:
                raise RuntimeError("sum() takes 1 or 2 arguments")
        elif node.name == 'min':
            args = [self.interpret(arg) for arg in node.arguments]
            if len(args) == 1 and hasattr(args[0], '__iter__'):
                return min(args[0])
            else:
                return min(*args)
        elif node.name == 'max':
            args = [self.interpret(arg) for arg in node.arguments]
            if len(args) == 1 and hasattr(args[0], '__iter__'):
                return max(args[0])
            else:
                return max(*args)
        elif node.name == 'sorted':
            args = [self.interpret(arg) for arg in node.arguments]
            if len(args) == 1:
                return sorted(args[0])
            elif len(args) == 2:
                # sorted(iterable, reverse=True/False)
                return sorted(args[0], reverse=args[1])
            else:
                raise RuntimeError("sorted() takes 1 or 2 arguments")
        elif node.name == 'enumerate':
            args = [self.interpret(arg) for arg in node.arguments]
            if len(args) == 1:
                return list(enumerate(args[0]))
            elif len(args) == 2:
                return list(enumerate(args[0], args[1]))  # enumerate(iterable, start)
            else:
                raise RuntimeError("enumerate() takes 1 or 2 arguments")
        elif node.name == 'zip':
            args = [self.interpret(arg) for arg in node.arguments]
            return list(zip(*args))
        elif node.name == 'map':
            # Special handling: first argument might be a function name (Variable node)
            if len(node.arguments) < 2:
                raise RuntimeError("map() requires at least 2 arguments")

            # Check if first argument is a Variable (function name)
            first_arg = node.arguments[0]
            if isinstance(first_arg, Variable) and first_arg.name in self.functions:
                func_name = first_arg.name
                func_def = self.functions[func_name]
                iterables = [self.interpret(arg) for arg in node.arguments[1:]]

                def wrapper(*items):
                    old_local = self.local_env
                    self.local_env = {}
                    try:
                        for i, param in enumerate(func_def.parameters):
                            param_name = param.name if isinstance(param, Parameter) else param
                            if i < len(items):
                                self.local_env[param_name] = items[i]
                        try:
                            result = self.interpret(func_def.body)
                        except ReturnValue as ret:
                            result = ret.value
                        return result
                    finally:
                        self.local_env = old_local
                return list(map(wrapper, *iterables))
            else:
                # Evaluate all arguments normally
                args = [self.interpret(arg) for arg in node.arguments]
                func = args[0]
                iterables = args[1:]
                return list(map(func, *iterables))
        elif node.name == 'filter':
            # Special handling: first argument might be a function name (Variable node)
            if len(node.arguments) != 2:
                raise RuntimeError("filter() requires exactly 2 arguments")

            # Check if first argument is a Variable (function name)
            first_arg = node.arguments[0]
            if isinstance(first_arg, Variable) and first_arg.name in self.functions:
                func_name = first_arg.name
                func_def = self.functions[func_name]
                iterable = self.interpret(node.arguments[1])

                def wrapper(item):
                    old_local = self.local_env
                    self.local_env = {}
                    try:
                        param_name = func_def.parameters[0].name if isinstance(func_def.parameters[0], Parameter) else func_def.parameters[0]
                        self.local_env[param_name] = item
                        try:
                            result = self.interpret(func_def.body)
                        except ReturnValue as ret:
                            result = ret.value
                        return self._truthy(result)
                    finally:
                        self.local_env = old_local
                return list(filter(wrapper, iterable))
            else:
                # Evaluate all arguments normally
                args = [self.interpret(arg) for arg in node.arguments]
                func = args[0]
                iterable = args[1]
                return list(filter(func, iterable))
        elif node.name == 'all':
            arg = self.interpret(node.arguments[0])
            return all(self._truthy(x) for x in arg)
        elif node.name == 'any':
            arg = self.interpret(node.arguments[0])
            return any(self._truthy(x) for x in arg)
        elif node.name == 'abs':
            arg = self.interpret(node.arguments[0])
            return abs(arg)
        elif node.name == 'round':
            args = [self.interpret(arg) for arg in node.arguments]
            if len(args) == 1:
                return round(args[0])
            elif len(args) == 2:
                return round(args[0], args[1])
            else:
                raise RuntimeError("round() takes 1 or 2 arguments")
        elif node.name == 'pow':
            args = [self.interpret(arg) for arg in node.arguments]
            if len(args) == 2:
                return pow(args[0], args[1])
            elif len(args) == 3:
                return pow(args[0], args[1], args[2])
            else:
                raise RuntimeError("pow() takes 2 or 3 arguments")
        elif node.name == 'reversed':
            arg = self.interpret(node.arguments[0])
            return list(reversed(arg))

        # Logical programming: assert/retract
        elif node.name == 'assertz' or node.name == 'asserta' or node.name == 'retract' or node.name == 'retractall':
            if self.logical_engine is None:
                raise RuntimeError(f"{node.name}() requires a logical engine")

            # These functions work with predicates/facts
            # For now, we'll support passing predicate objects
            arg = self.interpret(node.arguments[0])

            if node.name == 'assertz':
                self.logical_engine.assertz(arg)
                return True
            elif node.name == 'asserta':
                self.logical_engine.asserta(arg)
                return True
            elif node.name == 'retract':
                return self.logical_engine.retract(arg)
            elif node.name == 'retractall':
                return self.logical_engine.retractall(arg)

        # Check if this is a class (object instantiation)
        if node.name in self.classes:
            args = [self.interpret(arg) for arg in node.arguments]
            # Handle named arguments
            named_args = {}
            if hasattr(node, 'named_arguments') and node.named_arguments:
                for name, value in node.named_arguments.items():
                    named_args[name] = self.interpret(value)
            return self.class_system.create_object(node.name, args, named_args)

        # Check if function is decorated (stored in environment)
        env = self.local_env if self.local_env is not None else self.global_env
        # Fallback to global_env when symbol not found in local env (mirrors variable lookup behavior)
        if node.name in env or (self.local_env is not None and node.name in self.global_env):
            target = env[node.name] if node.name in env else self.global_env[node.name]
            # Check if it's a decorated function (callable)
            if callable(target) and not isinstance(target, type):
                args = [self.interpret(arg) for arg in node.arguments]
                kwargs = {}
                if hasattr(node, 'named_arguments') and node.named_arguments:
                    for name, value in node.named_arguments.items():
                        kwargs[name] = self.interpret(value)
                if isinstance(target, BayanObject) and target.has_method('__call__'):
                    # For Bayan objects, pass positional only
                    return target.call_method('__call__', args)
                return target(*args, **kwargs)

        # User-defined functions
        if node.name in self.functions:
            func_def = self.functions[node.name]
            args = [self.interpret(arg) for arg in node.arguments]

            # Check if function is async - return a coroutine
            if node.name in self._async_functions:
                named_args = {}
                if hasattr(node, 'named_arguments'):
                    for name, value in node.named_arguments.items():
                        named_args[name] = self.interpret(value)
                return self.BayanCoroutine(self, func_def, args, named_args)

            # Check if function contains yield (is a generator)
            if self._contains_yield(func_def.body):
                # Return a generator
                return self._create_generator(func_def, args, node.named_arguments if hasattr(node, 'named_arguments') else {})

            # Evaluate named arguments
            named_args = {}
            if hasattr(node, 'named_arguments'):
                for name, value in node.named_arguments.items():
                    named_args[name] = self.interpret(value)

            # Create new local environment
            old_local_env = self.local_env
            self.local_env = {}

            # Bind parameters with support for defaults, named arguments, *args, and **kwargs
            param_names = []
            varargs_param = None
            kwargs_param = None

            for param in func_def.parameters:
                if isinstance(param, Parameter):
                    if param.is_kwargs:
                        kwargs_param = param.name
                    elif param.is_varargs:
                        varargs_param = param.name
                    else:
                        param_names.append(param.name)
                else:
                    # Legacy format: parameter is just a string
                    param_names.append(param)

            # Bind positional arguments
            positional_count = 0
            for i, arg in enumerate(args):
                if i < len(param_names):
                    self.local_env[param_names[i]] = arg
                    positional_count += 1
                elif varargs_param:
                    # Extra positional arguments go to *args
                    if varargs_param not in self.local_env:
                        self.local_env[varargs_param] = []
                    self.local_env[varargs_param].append(arg)
                else:
                    raise RuntimeError(f"Too many positional arguments for function {node.name}")

            # Initialize *args if it exists and wasn't populated
            if varargs_param and varargs_param not in self.local_env:
                self.local_env[varargs_param] = []

            # Bind named arguments
            for name, value in named_args.items():
                if name in param_names:
                    self.local_env[name] = value
                elif kwargs_param:
                    # Extra named arguments go to **kwargs
                    if kwargs_param not in self.local_env:
                        self.local_env[kwargs_param] = {}
                    self.local_env[kwargs_param][name] = value
                else:
                    raise RuntimeError(f"Unexpected keyword argument: {name}")

            # Initialize **kwargs if it exists and wasn't populated
            if kwargs_param and kwargs_param not in self.local_env:
                self.local_env[kwargs_param] = {}

            # Bind default values for missing parameters
            for param in func_def.parameters:
                if isinstance(param, Parameter):
                    if not param.is_varargs and not param.is_kwargs:
                        if param.name not in self.local_env and param.has_default():
                            self.local_env[param.name] = self.interpret(param.default_value)
                        elif param.name not in self.local_env:
                            raise RuntimeError(f"Missing required parameter: {param.name}")

            try:
                # Check requires clauses (preconditions)
                if hasattr(func_def, 'requires') and func_def.requires:
                    for requires_clause in func_def.requires:
                        self.visit_requires_clause(requires_clause)

                # Execute function body
                result = self.interpret(func_def.body)

                # Check ensures clauses (postconditions)
                if hasattr(func_def, 'ensures') and func_def.ensures:
                    # Make result available as 'result' variable for ensures clauses
                    self.local_env['result'] = result
                    for ensures_clause in func_def.ensures:
                        self.visit_ensures_clause(ensures_clause)
            except ReturnValue as ret:
                result = ret.value

                # Check ensures clauses for early returns
                if hasattr(func_def, 'ensures') and func_def.ensures:
                    self.local_env['result'] = result
                    for ensures_clause in func_def.ensures:
                        self.visit_ensures_clause(ensures_clause)
            finally:
                self.local_env = old_local_env

            return result

        # Python/global environment callable or BayanObject __call__
        if node.name in env or (self.local_env is not None and node.name in self.global_env):
            target = env[node.name] if node.name in env else self.global_env[node.name]
            args = [self.interpret(arg) for arg in node.arguments]
            if isinstance(target, BayanObject) and target.has_method('__call__'):
                return target.call_method('__call__', args)
            if callable(target):
                # Support named arguments for Python callables as well
                kwargs = {}
                if hasattr(node, 'named_arguments') and node.named_arguments:
                    for name, value in node.named_arguments.items():
                        kwargs[name] = self.interpret(value)
                return target(*args, **kwargs)

        raise NameError(f"Undefined function or class: {node.name}")

    def visit_function_def(self, node):
        """Visit a function definition node with decorator support"""
        # Store the function
        self.functions[node.name] = node

        # Also store in local environment if we're inside a function
        if self.local_env is not None:
            # Create a callable for nested functions WITH CLOSURE SUPPORT
            # Capture the current local_env as closure
            closure_env = dict(self.local_env)  # Copy current local environment

            def make_nested_callable(fn_node, interp, closure):
                def nested_callable(*args):
                    return interp._execute_function(fn_node, list(args), closure)
                return nested_callable

            self.local_env[node.name] = make_nested_callable(node, self, closure_env)

        # Apply decorators if present (in reverse order, bottom to top)
        if node.decorators:
            # For Bayan decorators, we need to call the decorator function
            # with the original function as an argument

            env = self.local_env if self.local_env is not None else self.global_env

            # Start with the original function
            func_name = node.name
            func_node = self.functions[func_name]
            current_closure = dict(self.local_env) if self.local_env is not None else None

            def make_func_callable(fn_node, interp, closure):
                def func_callable(*args):
                    return interp._execute_function(fn_node, list(args), closure)
                return func_callable

            # Start with the base function
            current_func = make_func_callable(func_node, self, current_closure)

            # Apply decorators in reverse order (bottom decorator first)
            for decorator in reversed(node.decorators):
                # Check if decorator has arguments
                if hasattr(decorator, 'args') and decorator.args:
                    # Decorator with arguments: @decorator(arg1, arg2)
                    # First call the decorator with its arguments to get the actual decorator
                    decorator_args = [self.interpret(arg) for arg in decorator.args]

                    if decorator.name in self.functions:
                        # Call the decorator factory function
                        from .ast_nodes import FunctionCall, Number, String

                        # Create argument nodes for the decorator factory
                        arg_nodes = []
                        for arg in decorator_args:
                            if isinstance(arg, (int, float)):
                                arg_nodes.append(Number(arg))
                            elif isinstance(arg, str):
                                arg_nodes.append(String(arg))
                            else:
                                # For other types, we'll need to handle them differently
                                arg_nodes.append(Number(arg))  # Fallback
                        factory_call = FunctionCall(decorator.name, arg_nodes, {})

                        # This should return a decorator function
                        actual_decorator = self.interpret(factory_call)

                        # Call the decorator with the current function
                        if callable(actual_decorator):
                            current_func = actual_decorator(current_func)
                else:
                    # Simple decorator: @decorator
                    if decorator.name in self.functions:
                        # Call the decorator with the current function
                        decorator_result = self._execute_function(self.functions[decorator.name], [current_func])
                        current_func = decorator_result

            # Store the final decorated function
            env[node.name] = current_func

        return None

    def _execute_function(self, func_def, args, closure=None):
        """Helper method to execute a Bayan function with given arguments

        Args:
            func_def: The function definition AST node
            args: List of arguments to pass to the function
            closure: Optional dict containing closure variables from parent scope
        """
        # Create new local environment
        old_local_env = self.local_env

        # Start with closure if provided, otherwise empty dict
        if closure is not None:
            self.local_env = dict(closure)  # Copy closure to avoid mutation
        else:
            self.local_env = {}

        # Bind parameters
        param_names = []
        for param in func_def.parameters:
            if isinstance(param, Parameter):
                param_names.append(param.name)
            else:
                param_names.append(param)

        for i, arg in enumerate(args):
            if i < len(param_names):
                self.local_env[param_names[i]] = arg

                # If the argument is a callable (e.g., a decorated function),
                # also make it available for function calls
                if callable(arg) and not isinstance(arg, (int, float, str, bool, list, dict, type)):
                    # This allows calling the function from within Bayan code
                    pass  # Already stored in local_env

        try:
            # Check requires clauses (preconditions)
            if hasattr(func_def, 'requires') and func_def.requires:
                for requires_clause in func_def.requires:
                    self.visit_requires_clause(requires_clause)

            # Execute function body
            result = self.interpret(func_def.body)

            # Check ensures clauses (postconditions)
            if hasattr(func_def, 'ensures') and func_def.ensures:
                # Make result available as 'result' variable for ensures clauses
                self.local_env['result'] = result
                for ensures_clause in func_def.ensures:
                    self.visit_ensures_clause(ensures_clause)
        except ReturnValue as ret:
            result = ret.value

            # Check ensures clauses for early returns
            if hasattr(func_def, 'ensures') and func_def.ensures:
                self.local_env['result'] = result
                for ensures_clause in func_def.ensures:
                    self.visit_ensures_clause(ensures_clause)
        finally:
            self.local_env = old_local_env

        return result

    def visit_async_function_def(self, node):
        """Visit an async function definition node"""
        # Store async function with marker
        self.functions[node.name] = node
        # Mark as async in a separate registry
        self._async_functions.add(node.name)
        return None

    def visit_await_expr(self, node):
        """Visit an await expression node"""
        # Evaluate the expression being awaited
        result = self.interpret(node.expression)

        # If result is a BayanCoroutine, execute it synchronously
        if isinstance(result, self.BayanCoroutine):
            return result.run()

        # If result has __await__, call it
        if hasattr(result, '__await__'):
            return result.__await__()

        # Otherwise return the result as-is
        return result

    def visit_yield_expr(self, node):
        """Visit a yield expression node"""
        # Evaluate the value to yield
        value = None
        if node.value:
            value = self.interpret(node.value)

        # Raise YieldValue exception to signal yielding
        raise YieldValue(value)

    def visit_with_statement(self, node):
        """Visit a with statement node (context manager)"""
        # Evaluate the context expression
        context_obj = self.interpret(node.context_expr)

        # Call __enter__ method
        if isinstance(context_obj, BayanObject) and context_obj.has_method('__enter__'):
            enter_result = context_obj.call_method('__enter__', [])
        elif hasattr(context_obj, '__enter__'):
            enter_result = context_obj.__enter__()
        else:
            raise TypeError(f"Object does not support context manager protocol")

        # Bind the result to the target variable if specified
        env = self.local_env if self.local_env is not None else self.global_env
        if node.target_var:
            env[node.target_var] = enter_result

        # Execute the body
        result = None
        exception_occurred = None
        try:
            result = self.interpret(node.body)
        except Exception as e:
            exception_occurred = e

        # Call __exit__ method
        try:
            if isinstance(context_obj, BayanObject) and context_obj.has_method('__exit__'):
                context_obj.call_method('__exit__', [None, None, None])
            elif hasattr(context_obj, '__exit__'):
                context_obj.__exit__(None, None, None)
        except Exception:
            pass

        # Re-raise the exception if one occurred
        if exception_occurred:
            raise exception_occurred

        return result

    def visit_if_statement(self, node):
        """Visit an if statement node"""
        condition = self.interpret(node.condition)

        if self._truthy(condition):
            return self.interpret(node.then_branch)
        elif node.else_branch:
            return self.interpret(node.else_branch)

        return None

    def visit_for_loop(self, node):
        """Visit a for loop node (with optional invariants)"""
        iterable = self._to_iterable(self.interpret(node.iterable))
        result = None

        env = self.local_env if self.local_env is not None else self.global_env

        for value in iterable:
            env[node.variable] = value

            # Check invariants at start of each iteration
            if hasattr(node, 'invariants') and node.invariants:
                for invariant in node.invariants:
                    self.visit_invariant_clause(invariant)
            elif hasattr(node, 'invariant') and node.invariant:
                # Backward compatibility
                self.visit_invariant_clause(node.invariant)

            try:
                result = self.interpret(node.body)
            except BreakException:
                break
            except ContinueException:
                continue

            # Check invariants at end of each iteration
            if hasattr(node, 'invariants') and node.invariants:
                for invariant in node.invariants:
                    self.visit_invariant_clause(invariant)
            elif hasattr(node, 'invariant') and node.invariant:
                # Backward compatibility
                self.visit_invariant_clause(node.invariant)

        return result

    def visit_while_loop(self, node):
        """Visit a while loop node (with optional invariants)"""
        result = None
        while self._truthy(self.interpret(node.condition)):
            # Check invariants at start of each iteration
            if hasattr(node, 'invariants') and node.invariants:
                for invariant in node.invariants:
                    self.visit_invariant_clause(invariant)
            elif hasattr(node, 'invariant') and node.invariant:
                # Backward compatibility
                self.visit_invariant_clause(node.invariant)

            try:
                result = self.interpret(node.body)
            except BreakException:
                break
            except ContinueException:
                continue

            # Check invariants at end of each iteration
            if hasattr(node, 'invariants') and node.invariants:
                for invariant in node.invariants:
                    self.visit_invariant_clause(invariant)
            elif hasattr(node, 'invariant') and node.invariant:
                # Backward compatibility
                self.visit_invariant_clause(node.invariant)
        return result

    def visit_return_statement(self, node):
        """Visit a return statement node"""
        value = None
        if node.value:
            value = self.interpret(node.value)
        raise ReturnValue(value)

    def visit_raise_statement(self, node):
        """Visit a raise statement node"""
        value = self.interpret(node.value) if node.value is not None else None
        raise BayanException(value)

    def visit_try_except_finally(self, node):
        """Visit a try/except/finally node"""
        result = None
        try:
            result = self.interpret(node.try_block)
        except (BayanException, BayanRuntimeError, Exception) as e:
            # Don't catch control flow exceptions
            if isinstance(e, (ReturnValue, BreakException, ContinueException, YieldValue)):
                raise

            handled = False
            env = self.local_env if self.local_env is not None else self.global_env

            # Extract the actual exception value
            if isinstance(e, BayanException):
                exc_value = e.value
            elif isinstance(e, BayanRuntimeError):
                exc_value = str(e)
            else:
                exc_value = str(e)

            for handler in node.handlers:
                match = False
                if handler.type_name is None:
                    # Bare except: catches everything
                    match = True
                else:
                    # Determine exception class name if BayanObject
                    if isinstance(e, BayanException) and isinstance(e.value, BayanObject):
                        exc_class = e.value.class_def.name
                        if exc_class == handler.type_name or self.class_system.is_subclass(exc_class, handler.type_name):
                            match = True
                    else:
                        # Python exceptions or non-object Bayan exceptions match generic handlers
                        if handler.type_name in ('Exception', 'BaseException'):
                            match = True
                        # Also match specific Python exception types
                        elif handler.type_name == e.__class__.__name__:
                            match = True
                if match:
                    handled = True
                    if handler.alias:
                        env[handler.alias] = exc_value
                    result = self.interpret(handler.body)
                    break
            if not handled:
                # Propagate if not matched
                raise
        finally:
            if node.finally_block:
                self.interpret(node.finally_block)
        return result

    def visit_print_statement(self, node):
        """Visit a print statement node with support for multiple values"""
        # Check if node.value is a list (multiple arguments)
        if isinstance(node.value, list):
            # Multiple values - evaluate each and print with space separator
            values = [self.interpret(v) for v in node.value]
            # Convert all to strings and join with space
            output = ' '.join(str(v) for v in values)
            print(output)
        else:
            # Single value - old behavior
            value = self.interpret(node.value)
            print(value)
        return None

    def visit_similarity_decl(self, node):
        """Handle SimilarityDecl sugar by asserting similar facts (including reverse)."""
        # Prefer using the runtime helper assert_fact if available
        env = self.local_env if self.local_env is not None else self.global_env
        af = None
        try:
            cand = env.get('assert_fact') if isinstance(env, dict) else None
            if callable(cand):
                af = cand
            elif 'assert_fact' in self.global_env and callable(self.global_env['assert_fact']):
                af = self.global_env['assert_fact']
        except Exception:
            af = None

        head = str(getattr(node, 'head', ''))
        kind = str(node.kind) if getattr(node, 'kind', None) is not None else "syn"
        domain = str(node.domain) if getattr(node, 'domain', None) is not None else "lexicon"
        default = float(node.default) if getattr(node, 'default', None) is not None else 0.7

        for pair in getattr(node, 'pairs', []):
            key_val = self.interpret(pair.key)
            score_val = self.interpret(pair.value) if hasattr(pair, 'value') else default
            try:
                s = float(score_val)
            except Exception:
                raise RuntimeError(f"SimilarityDecl score must be numeric, got: {score_val}")
            y = str(key_val)
            if af is not None:
                af('similar', head, y, s, kind, domain)
                af('similar', y, head, s, kind, domain)
            else:
                # Fallback to direct logical assertion
                from .logical_engine import Predicate, Fact, Term, LogicalEngine
                if self.logical_engine is None:
                    self.logical_engine = LogicalEngine()
                pred1 = Predicate('similar', [Term(head), Term(y), Term(s), Term(kind), Term(domain)])
                pred2 = Predicate('similar', [Term(y), Term(head), Term(s), Term(kind), Term(domain)])
                self.logical_engine.assertz(Fact(pred1))
                self.logical_engine.assertz(Fact(pred2))
        return True

    # ---- Sugar visitors: collect/topk/argmax ----
    def _deref_value(self, term_or_val, subst=None):
        try:
            # Try logical deref if available
            if subst is not None and hasattr(self.logical_engine, '_deref'):
                resolved = self.logical_engine._deref(term_or_val, subst)
            else:
                resolved = term_or_val
        except Exception:
            resolved = term_or_val
        return getattr(resolved, 'value', resolved)

    def _query_solutions(self, goal, max_solutions=None):
        if self.logical_engine is None:
            raise RuntimeError("collect/topk/argmax require a logical engine (use inside hybrid)")
        solutions = self.logical_engine.query(goal)
        if max_solutions is not None:
            # Limit the number of solutions
            limited = []
            for i, sol in enumerate(solutions):
                if i >= max_solutions:
                    break
                limited.append(sol)
            return limited
        return solutions

    def visit_collect_expr(self, node):
        sols = self._query_solutions(node.goal)
        out = []
        seen = set()
        for subst in sols:
            if hasattr(subst, 'bindings'):
                val = subst.bindings.get(node.var_name)
                final = self._deref_value(val, subst)
                if node.unique:
                    key = str(final)
                    if key in seen:
                        continue
                    seen.add(key)
                out.append(final)
            if node.limit is not None and len(out) >= node.limit:
                break
        return out

    def visit_topk_expr(self, node):
        sols = self._query_solutions(node.goal)
        pairs = []
        for subst in sols:
            v = subst.bindings.get(node.var_name)
            s = subst.bindings.get(node.score_name)
            v_final = self._deref_value(v, subst)
            s_final = self._deref_value(s, subst)
            s_num = None
            try:
                s_num = float(s_final)
            except Exception:
                # If score var is unbound or non-numeric, fallback to solution probability
                try:
                    s_num = float(getattr(subst, 'probability', 1.0))
                except Exception:
                    s_num = None
            if s_num is None:
                continue
            pairs.append((v_final, s_num))
        pairs.sort(key=lambda x: x[1], reverse=True)
        return [v for (v, _) in pairs[:max(0, int(node.k))]]

    def visit_argmax_expr(self, node):
        lst = self.visit_topk_expr(type('Tmp', (), {
            'k': 1,
            'var_name': node.var_name,
            'score_name': node.score_name,
            'goal': node.goal
        }))
        return lst[0] if lst else None

    # ---- Sugar visitors: choose and sampling ----
    def visit_choose_expr(self, node):
        # node.mapping is a Dict AST node of choices->weights
        mapping = self.visit_dict(node.mapping)
        chooser = self.global_env.get('choose_weighted')
        if not callable(chooser):
            raise RuntimeError("choose_weighted runtime is not available")
        return chooser(mapping)

    def visit_sample_assign(self, node):
        # Evaluate distribution call (a function returning a sampled value)
        val = self.visit_function_call(node.dist_call) if isinstance(node.dist_call, FunctionCall) else self.interpret(node.dist_call)
        # Assign to variable in current env
        target_env = self.local_env if self.local_env is not None else self.global_env
        target_env[node.var_name] = val
        return val

    # ---- Once and Limit visitors ----
    def visit_once_statement(self, node):
        """Visit once { block } - execute block with max_solutions=1"""
        # Execute the block normally (traditional code)
        return self.interpret(node.body)

    def visit_once_goal(self, node):
        """Visit once goal. - single logical goal with limit 1"""
        # Query with limit 1
        sols = self._query_solutions(node.goal, max_solutions=1)
        return sols[0] if sols else None

    def visit_limit_statement(self, node):
        """Visit limit N { block }"""
        # Execute the block normally (traditional code)
        return self.interpret(node.body)

    def visit_limit_goal(self, node):
        """Visit limit N goal. - logical goal with limit N"""
        # Query with limit N
        sols = self._query_solutions(node.goal, max_solutions=node.limit)
        return sols

    def visit_match_in_as(self, node):
        """Visit match pattern in text as var_name
        Syntactic sugar for: var_name = match(pattern, text)
        """
        # Evaluate pattern and text
        pattern = self.interpret(node.pattern)
        text = self.interpret(node.text)

        # Call match function
        match_fn = self.global_env.get('match')
        if not callable(match_fn):
            raise RuntimeError("match runtime function is not available")

        result = match_fn(pattern, text)

        # Assign to variable
        target_env = self.local_env if self.local_env is not None else self.global_env
        target_env[node.var_name] = result

        return result

    def visit_class_def(self, node):
        """Visit a class definition node"""
        self.classes[node.name] = node
        self.class_system.register_class(node)
        return None

    def visit_super_call(self, node):
        """Visit a super(...) call inside a method using MRO"""
        # Ensure we are inside a method with self bound
        if not self.local_env or 'self' not in self.local_env:
            raise RuntimeError("'super' used outside of a method")
        self_obj = self.local_env['self']
        if not isinstance(self_obj, BayanObject):
            raise RuntimeError("'super' requires a BayanObject context")

        # Determine current owner class context for super
        if not self._owner_stack:
            raise RuntimeError("super() requires a current method context")
        current_owner = self._owner_stack[-1]

        # Resolve next method in MRO after current_owner
        start_after = current_owner
        owner, method = self.class_system.resolve_method(self_obj.class_def.name, node.method_name, start_after=start_after)
        if not method:
            raise AttributeError(f"No super method '{node.method_name}' found after {current_owner}")

        args = [self.interpret(arg) for arg in node.arguments]

        # Execute method body with self bound to the current instance; push new owner
        old_env = self.local_env
        self.local_env = {'self': self_obj}
        self._owner_stack.append(owner)
        try:
            # Bind parameters with support for Parameter objects and defaults
            from .ast_nodes import Parameter

            param_names = []
            for param in method.parameters:
                if isinstance(param, Parameter):
                    if param.name != 'self':
                        param_names.append(param.name)
                else:
                    # Legacy format: parameter is just a string
                    if param != 'self':
                        param_names.append(param)

            # Bind positional arguments
            for i, arg in enumerate(args):
                if i < len(param_names):
                    self.local_env[param_names[i]] = arg

            # Bind default values for missing parameters
            for param in method.parameters:
                if isinstance(param, Parameter):
                    if param.name != 'self' and param.name not in self.local_env and param.has_default():
                        self.local_env[param.name] = self.interpret(param.default_value)

            result = self.interpret(method.body)
            return result
        except ReturnValue as ret:
            return ret.value
        finally:
            self._owner_stack.pop()
            self.local_env = old_env

    def visit_attribute_access(self, node):
        """Visit an attribute access node (obj.attr)"""
        obj = self.interpret(node.object_expr)

        if isinstance(obj, BayanObject):
            return obj.get_attribute(node.attribute_name)
        elif isinstance(obj, dict):
            return obj.get(node.attribute_name)
        else:
            # Try Python attribute access
            if hasattr(obj, node.attribute_name):
                return getattr(obj, node.attribute_name)
            raise AttributeError(f"Object has no attribute '{node.attribute_name}'")

    def visit_subscript_access(self, node):
        """Visit a subscript access node (obj[index] or obj[start:end:step])"""
        from .ast_nodes import Slice

        obj = self.interpret(node.object_expr)
        index_expr = node.index_expr

        # Check if this is a slice operation
        if isinstance(index_expr, Slice):
            start = self.interpret(index_expr.start) if index_expr.start is not None else None
            end = self.interpret(index_expr.end) if index_expr.end is not None else None
            step = self.interpret(index_expr.step) if index_expr.step is not None else None

            # Create Python slice object
            slice_obj = slice(start, end, step)

            if isinstance(obj, BayanObject):
                if obj.has_method('__getitem__'):
                    return obj.call_method('__getitem__', [slice_obj])
                raise TypeError("Object does not support __getitem__")
            try:
                return obj[slice_obj]
            except Exception as e:
                raise TypeError(f"Slicing not supported: {e}")
        else:
            # Regular indexing
            index = self.interpret(index_expr)
            if isinstance(obj, BayanObject):
                if obj.has_method('__getitem__'):
                    return obj.call_method('__getitem__', [index])
                raise TypeError("Object does not support __getitem__")
            try:
                return obj[index]
            except Exception as e:
                raise TypeError(f"Indexing not supported: {e}")

    def visit_attribute_assignment(self, node):
        """Visit attribute assignment (obj.attr = value)"""
        obj = self.interpret(node.object_expr)
        value = self.interpret(node.value)
        if isinstance(obj, BayanObject):
            obj.set_attribute(node.attribute_name, value)
            return value
        # Fallback to Python setattr
        try:
            setattr(obj, node.attribute_name, value)
            return value
        except Exception as e:
            raise AttributeError(f"Cannot set attribute '{node.attribute_name}': {e}")

    def visit_subscript_assignment(self, node):
        """Visit subscript assignment (obj[index] = value)"""
        obj = self.interpret(node.object_expr)
        index = self.interpret(node.index_expr)
        value = self.interpret(node.value)
        if isinstance(obj, BayanObject):
            if obj.has_method('__setitem__'):
                obj.call_method('__setitem__', [index, value])
                return value
            raise TypeError("Object does not support __setitem__")
        # Python container assignment
        try:
            obj[index] = value
            return value
        except Exception as e:
            raise TypeError(f"Index assignment not supported: {e}")

    def visit_method_call(self, node):
        """Visit a method call node (obj.method()) with support for named arguments"""
        obj = self.interpret(node.object_expr)
        arguments = [self.interpret(arg) for arg in node.arguments]

        # Evaluate named arguments
        named_args = {}
        if hasattr(node, 'named_arguments'):
            for name, value in node.named_arguments.items():
                named_args[name] = self.interpret(value)

        if isinstance(obj, BayanObject):
            return obj.call_method(node.method_name, arguments, named_args)
        else:
            # Python object or module function call
            if hasattr(obj, node.method_name):
                func = getattr(obj, node.method_name)
                if callable(func):
                    return func(*arguments, **named_args)
            raise AttributeError(f"Object has no method '{node.method_name}'")

    def visit_self_reference(self, node):
        """Visit a self reference node"""
        if self.local_env and 'self' in self.local_env:
            return self.local_env['self']
        raise NameError("'self' is not defined")

    def visit_import_statement(self, node):
        """Visit an import statement"""
        module = self.import_system.import_module(node.module_name, node.alias)

        # Add to environment
        name = node.alias if node.alias else node.module_name
        env = self.local_env if self.local_env is not None else self.global_env
        env[name] = module

        return None

    def visit_from_import_statement(self, node):
        """Visit a from...import statement"""
        imported = self.import_system.import_from_module(
            node.module_name,
            node.names,
            node.aliases
        )

        # Add to environment
        env = self.local_env if self.local_env is not None else self.global_env
        for name, value in imported.items():
            env[name] = value

        return None

    def _contains_yield(self, node):
        """Check if a node or its children contain a yield expression"""
        if isinstance(node, YieldExpr):
            return True

        # Check all attributes that might contain child nodes
        if isinstance(node, Block):
            for statement in node.statements:
                if self._contains_yield(statement):
                    return True
        elif isinstance(node, IfStatement):
            if self._contains_yield(node.then_branch):
                return True
            if node.else_branch and self._contains_yield(node.else_branch):
                return True
        elif isinstance(node, WhileLoop):
            if self._contains_yield(node.body):
                return True
        elif isinstance(node, ForLoop):
            if self._contains_yield(node.body):
                return True
        elif isinstance(node, TryExceptFinally):
            if self._contains_yield(node.try_block):
                return True
            for handler in node.handlers:
                if self._contains_yield(handler.body):
                    return True
            if node.finally_block and self._contains_yield(node.finally_block):
                return True

        return False

    def _interpret_in_env(self, node, env):
        """Interpret a node with a specific local environment, restoring afterward."""
        old_env = self.local_env
        self.local_env = env
        try:
            return self.interpret(node)
        finally:
            self.local_env = old_env

    def _gen_run_block(self, block, env):
        """Execute a block as a Python generator, yielding values on YieldExpr."""
        for stmt in block.statements:
            # Yield statement
            if isinstance(stmt, YieldExpr):
                value = self._interpret_in_env(stmt.value, env) if stmt.value is not None else None
                yield value
                continue

            # Return ends the generator
            if isinstance(stmt, ReturnStatement):
                return

            # Simple assignment
            if isinstance(stmt, Assignment):
                value = self._interpret_in_env(stmt.value, env)
                env[stmt.name] = value
                continue

            # If statement (bodies may yield)
            if isinstance(stmt, IfStatement):
                cond = self._interpret_in_env(stmt.condition, env)
                if self._truthy(cond):
                    if isinstance(stmt.then_branch, Block):
                        yield from self._gen_run_block(stmt.then_branch, env)
                    else:
                        self._interpret_in_env(stmt.then_branch, env)
                elif stmt.else_branch:
                    if isinstance(stmt.else_branch, Block):
                        yield from self._gen_run_block(stmt.else_branch, env)
                    else:
                        self._interpret_in_env(stmt.else_branch, env)
                continue

            # For loop (body may yield)
            if isinstance(stmt, ForLoop):
                iterable = self._to_iterable(self._interpret_in_env(stmt.iterable, env))
                for value in iterable:
                    env[stmt.variable] = value
                    try:
                        yield from self._gen_run_block(stmt.body, env)
                    except BreakException:
                        break
                    except ContinueException:
                        continue
                continue

            # While loop (body may yield)
            if isinstance(stmt, WhileLoop):
                while self._truthy(self._interpret_in_env(stmt.condition, env)):
                    try:
                        yield from self._gen_run_block(stmt.body, env)
                    except BreakException:
                        break
                    except ContinueException:
                        continue
                continue

            # Try/except/finally (blocks may yield)
            if isinstance(stmt, TryExceptFinally):
                try:
                    # Execute try block as generator
                    yield from self._gen_run_block(stmt.try_block, env)
                except (BayanException, BayanRuntimeError, Exception) as e:
                    # Don't catch control flow exceptions
                    if isinstance(e, (ReturnValue, BreakException, ContinueException, YieldValue)):
                        raise

                    handled = False

                    # Extract the actual exception value
                    if isinstance(e, BayanException):
                        exc_value = e.value
                    elif isinstance(e, BayanRuntimeError):
                        exc_value = str(e)
                    else:
                        exc_value = str(e)

                    for handler in stmt.handlers:
                        match = False
                        if handler.type_name is None:
                            # Bare except: catches everything
                            match = True
                        else:
                            # Determine exception class name if BayanObject
                            if isinstance(e, BayanException) and isinstance(e.value, BayanObject):
                                exc_class = e.value.class_def.name
                                if exc_class == handler.type_name or self.class_system.is_subclass(exc_class, handler.type_name):
                                    match = True
                            else:
                                # Python exceptions or non-object Bayan exceptions match generic handlers
                                if handler.type_name in ('Exception', 'BaseException'):
                                    match = True
                                # Also match specific Python exception types
                                elif handler.type_name == e.__class__.__name__:
                                    match = True
                        if match:
                            handled = True
                            if handler.alias:
                                env[handler.alias] = exc_value
                            # Execute handler body as generator
                            yield from self._gen_run_block(handler.body, env)
                            break
                    if not handled:
                        # Propagate if not matched
                        raise
                finally:
                    if stmt.finally_block:
                        # Execute finally block as generator
                        yield from self._gen_run_block(stmt.finally_block, env)
                continue

            # With statement (body may yield)
            if isinstance(stmt, WithStatement):
                # Evaluate context manager
                context_manager = self._interpret_in_env(stmt.expression, env)

                # Call __enter__
                if isinstance(context_manager, BayanObject) and context_manager.has_method('__enter__'):
                    enter_result = context_manager.call_method('__enter__', [])
                elif hasattr(context_manager, '__enter__'):
                    enter_result = context_manager.__enter__()
                else:
                    raise RuntimeError(f"Context manager does not have __enter__ method")

                # Bind to alias if provided
                if stmt.alias:
                    env[stmt.alias] = enter_result

                # Execute body with proper cleanup
                try:
                    yield from self._gen_run_block(stmt.body, env)
                finally:
                    # Call __exit__
                    if isinstance(context_manager, BayanObject) and context_manager.has_method('__exit__'):
                        context_manager.call_method('__exit__', [None, None, None])
                    elif hasattr(context_manager, '__exit__'):
                        context_manager.__exit__(None, None, None)
                continue

            # Fallback: execute statement synchronously
            self._interpret_in_env(stmt, env)

    def _create_generator(self, func_def, args, named_args):
        """Return a native Python generator for a function containing yield."""
        # Prepare a fresh local environment for this generator invocation
        gen_env = {}

        # Parameter names (support Parameter objects or raw names)
        parameters = getattr(func_def, 'parameters', getattr(func_def, 'params', []))
        param_names = []
        for p in parameters:
            if isinstance(p, Parameter):
                param_names.append(p.name)
            else:
                param_names.append(p)

        # Bind positional arguments
        for i, arg in enumerate(args):
            if i < len(param_names):
                gen_env[param_names[i]] = arg

        # Bind named arguments (values are AST nodes; evaluate in caller env)
        if isinstance(named_args, dict):
            for name, value_node in named_args.items():
                if name in param_names:
                    gen_env[name] = self.interpret(value_node)

        # Apply default values for missing parameters
        for p in parameters:
            if isinstance(p, Parameter) and p.default_value is not None and p.name not in gen_env:
                gen_env[p.name] = self.interpret(p.default_value)

        def generator():
            # Drive the function body as a generator
            yield from self._gen_run_block(func_def.body, gen_env)

        return generator()

    # ============ Temporal Constructs Visitors ============

    def visit_temporal_block(self, node):
        """Visit temporal block: temporal { first: stmt, then: stmt, lastly: stmt }

        Executes steps in sequence. Each step is labeled (first, then, lastly).
        For now, we execute them sequentially without actual timing.
        Future enhancement: add actual timing/scheduling support.
        """
        import time

        results = []
        for label, stmt in node.steps:
            # Execute each step in sequence
            result = self.interpret(stmt)
            results.append((label, result))

            # Optional: add small delay between steps for demonstration
            # time.sleep(0.01)

        # Return the last result (or all results as a list)
        return results[-1][1] if results else None

    def visit_within_block(self, node):
        """Visit within block: within 5.0 seconds { ... }

        Executes block with a timeout constraint.
        If block takes longer than specified duration, raises TimeoutError.
        """
        import time
        import signal

        # Convert duration to seconds
        duration_seconds = self._convert_to_seconds(node.duration, node.unit)

        # For simplicity, we'll use a basic timeout mechanism
        # Note: signal.alarm only works on Unix systems and only with integer seconds
        # For production, consider using threading.Timer or asyncio

        start_time = time.time()

        try:
            result = self.interpret(node.body)

            elapsed = time.time() - start_time
            if elapsed > duration_seconds:
                raise TimeoutError(f"Block exceeded time limit of {node.duration} {node.unit}")

            return result
        except Exception as e:
            # Re-raise the exception
            raise

    def visit_schedule_block(self, node):
        """Visit schedule block: schedule every 2.0 seconds { ... }

        Schedules repeated execution of a block.
        Note: This is a simplified implementation that executes once.
        For actual scheduling, you would need a background scheduler.
        """
        import time

        # Convert interval to seconds
        interval_seconds = self._convert_to_seconds(node.interval, node.unit)

        # For now, we'll just execute once and return a message
        # In a real implementation, this would register a scheduled task
        result = self.interpret(node.body)

        # Store scheduling info for potential future use
        schedule_info = {
            'interval': interval_seconds,
            'unit': node.unit,
            'body': node.body,
            'last_result': result
        }

        # You could store this in a scheduler registry
        # self.scheduler.register(schedule_info)

        return result

    def visit_delay_statement(self, node):
        """Visit delay statement: delay 1.5 seconds

        Pauses execution for the specified duration.
        """
        import time

        # Convert duration to seconds
        duration_seconds = self._convert_to_seconds(node.duration, node.unit)

        # Sleep for the specified duration
        time.sleep(duration_seconds)

        return None

    def _convert_to_seconds(self, duration, unit):
        """Convert duration to seconds based on unit

        Args:
            duration: numeric value
            unit: 'seconds', 'minutes', 'hours' (or Arabic equivalents)

        Returns:
            float: duration in seconds
        """
        # Normalize unit to English
        unit_lower = unit.lower()

        if unit_lower in ['seconds', 'second', 'ثانية', 'ثواني']:
            return float(duration)
        elif unit_lower in ['minutes', 'minute', 'دقيقة', 'دقائق']:
            return float(duration) * 60
        elif unit_lower in ['hours', 'hour', 'ساعة', 'ساعات']:
            return float(duration) * 3600
        else:
            raise ValueError(f"Unknown time unit: {unit}")

    # ========================================================================
    # Constraint & Validation Visitors
    # ========================================================================

    def visit_where_clause(self, node):
        """Execute where clause (filter expression based on condition)

        Examples:
            x = [1, 2, 3, 4, 5] where item > 2  # Not implemented yet - needs special handling
            result = compute(x) where x > 0     # Evaluates compute(x) if x > 0, else raises error

        For now, we evaluate the expression and check the condition.
        If condition is false, we raise an error.
        """
        # Evaluate the main expression
        result = self.interpret(node.expression)

        # Evaluate the condition
        condition_result = self.interpret(node.condition)

        # Check if condition is true
        if not condition_result:
            raise ValueError(f"Where clause condition failed: {node.condition}")

        return result

    def visit_requires_clause(self, node):
        """Check requires clause (precondition)

        This is typically called at the start of a function.
        """
        condition_result = self.interpret(node.condition)

        if not condition_result:
            message = node.message if node.message else f"Precondition failed: {node.condition}"
            raise ContractError(f"Requires clause violated: {message}")

        return True

    def visit_ensures_clause(self, node):
        """Check ensures clause (postcondition)

        This is typically called at the end of a function.
        """
        condition_result = self.interpret(node.condition)

        if not condition_result:
            message = node.message if node.message else f"Postcondition failed: {node.condition}"
            raise ContractError(f"Ensures clause violated: {message}")

        return True

    def visit_invariant_clause(self, node):
        """Check invariant clause

        This is typically called in loops or class methods.
        """
        condition_result = self.interpret(node.condition)

        if not condition_result:
            message = node.message if node.message else f"Invariant failed: {node.condition}"
            raise ContractError(f"Invariant violated: {message}")

        return True

    def visit_match_statement(self, node):
        """Execute match statement for pattern matching

        Evaluates the value and tries to match it against each case.
        Executes the first matching case's body.
        """
        # Evaluate the value to match
        value = self.interpret(node.value)

        # Get current environment
        env = self.local_env if self.local_env is not None else self.global_env

        # Try each case
        for case in node.cases:
            if isinstance(case, DefaultClause):
                # Default case always matches
                return self.interpret(case.body)
            elif isinstance(case, CaseClause):
                # Try to match pattern
                bindings = self._match_pattern(case.pattern, value)

                if bindings is not None:
                    # Pattern matched, check guard if present
                    if case.guard:
                        # Add bindings to environment temporarily for guard evaluation
                        saved_values = {}
                        for var_name, var_value in bindings.items():
                            if var_name in env:
                                saved_values[var_name] = env[var_name]
                            env[var_name] = var_value

                        # Evaluate guard
                        guard_result = self.interpret(case.guard)

                        # Restore saved values
                        for var_name in bindings.keys():
                            if var_name in saved_values:
                                env[var_name] = saved_values[var_name]
                            else:
                                del env[var_name]

                        if not guard_result:
                            # Guard failed, try next case
                            continue

                    # Pattern matched (and guard passed if present)
                    # Add bindings to environment and execute body
                    for var_name, var_value in bindings.items():
                        env[var_name] = var_value

                    result = self.interpret(case.body)
                    return result

        # No case matched
        raise ValueError(f"No matching case for value: {value}")

    def _match_pattern(self, pattern, value):
        """Try to match a pattern against a value

        Returns a dictionary of variable bindings if match succeeds,
        or None if match fails.
        """
        if isinstance(pattern, ListPattern):
            # Match list pattern
            if not isinstance(value, list):
                return None

            if len(pattern.elements) != len(value):
                return None

            bindings = {}
            for i, elem_pattern in enumerate(pattern.elements):
                elem_bindings = self._match_pattern(elem_pattern, value[i])
                if elem_bindings is None:
                    return None
                bindings.update(elem_bindings)

            return bindings

        elif isinstance(pattern, DictPattern):
            # Match dict pattern
            if not isinstance(value, dict):
                return None

            bindings = {}
            for key, key_pattern in zip(pattern.keys, pattern.patterns):
                if key not in value:
                    return None

                key_bindings = self._match_pattern(key_pattern, value[key])
                if key_bindings is None:
                    return None
                bindings.update(key_bindings)

            return bindings

        elif isinstance(pattern, Variable):
            # Variable pattern - always matches and binds
            return {pattern.name: value}

        else:
            # Literal pattern - must equal value
            pattern_value = self.interpret(pattern)
            if pattern_value == value:
                return {}  # Match with no bindings
            else:
                return None  # No match

    def visit_case_clause(self, node):
        """Case clause should not be visited directly"""
        raise RuntimeError("CaseClause should not be visited directly")

    def visit_default_clause(self, node):
        """Default clause should not be visited directly"""
        raise RuntimeError("DefaultClause should not be visited directly")

    def visit_list_pattern(self, node):
        """List pattern should not be visited directly"""
        raise RuntimeError("ListPattern should not be visited directly")

    def visit_dict_pattern(self, node):
        """Dict pattern should not be visited directly"""
        raise RuntimeError("DictPattern should not be visited directly")
    # ========================================================================
    # Reactive Programming Visitors - زوار البرمجة التفاعلية
    # ========================================================================

    def visit_reactive_declaration(self, node):
        """Visit reactive variable declaration

        Declares a variable as reactive and sets up tracking.
        """
        # Evaluate initial value
        value = self.interpret(node.value)

        # Store in environment
        env = self.local_env if self.local_env is not None else self.global_env
        env[node.variable] = value

        # Mark as reactive
        self._reactive_vars.add(node.variable)

        return None

    def visit_watch_block(self, node):
        """Visit watch block

        Registers a watcher that executes when watched variables change.
        """
        # Store the watcher
        self._watchers.append((node.variables, node.body))

        return None

    def visit_computed_property(self, node):
        """Visit computed property

        Defines a computed property that auto-updates when dependencies change.
        """
        # Evaluate initial value
        value = self.interpret(node.expression)

        # Store in environment
        env = self.local_env if self.local_env is not None else self.global_env
        env[node.variable] = value

        # Store computed property info
        self._computed_props[node.variable] = (node.expression, node.dependencies)

        # Mark computed property as reactive so it can trigger watchers
        self._reactive_vars.add(node.variable)

        return None

    def set_variable(self, name, value):
        """Set a variable and trigger reactive updates if needed"""
        env = self.local_env if self.local_env is not None else self.global_env
        old_value = env.get(name)
        env[name] = value

        # If this is a reactive variable and value changed, trigger updates
        if name in self._reactive_vars and old_value != value:
            self._trigger_reactive_updates(name)

    def _trigger_reactive_updates(self, changed_var):
        """Trigger reactive updates when a variable changes

        1. Recompute all computed properties that depend on this variable
        2. Execute all watchers that watch this variable
        """
        # Recompute computed properties first
        for prop_name, (expression, dependencies) in self._computed_props.items():
            if changed_var in dependencies:
                new_value = self.interpret(expression)
                env = self.local_env if self.local_env is not None else self.global_env
                old_value = env.get(prop_name)
                env[prop_name] = new_value

                # If computed property changed, trigger its watchers
                if old_value != new_value:
                    for watched_vars, body in self._watchers:
                        if prop_name in watched_vars:
                            self.interpret(body)

        # Execute watchers for the changed variable
        for watched_vars, body in self._watchers:
            if changed_var in watched_vars:
                self.interpret(body)

    # ============================================
    # Pipeline and Composition Operators
    # ============================================

    def visit_pipeline_op(self, node):
        """Visit pipeline operator: value |> function

        Evaluates value and applies function to it.
        Examples:
            5 |> double        -> double(5)
            [1,2,3] |> sum     -> sum([1,2,3])
            x |> f |> g        -> g(f(x))
        """
        # Evaluate the value
        value = self.interpret(node.value)

        # Handle function reference
        # If node.function is a Variable, we need to look it up
        if isinstance(node.function, Variable):
            func_name = node.function.name

            # Try to find function in functions dict first
            if func_name in self.functions:
                func = self.functions[func_name]
            else:
                # Try local/global environment
                env = self.local_env if self.local_env is not None else self.global_env
                if func_name in env:
                    func = env[func_name]
                else:
                    # Try Python built-ins
                    import builtins
                    if hasattr(builtins, func_name):
                        func = getattr(builtins, func_name)
                    else:
                        raise NameError(f"Undefined function: {func_name}")
        else:
            # Otherwise evaluate it
            func = self.interpret(node.function)

        # Apply function to value
        if callable(func):
            return func(value)
        elif isinstance(func, FunctionDef):
            # Call user-defined function
            return self._execute_function(func, [value])
        else:
            raise RuntimeError(f"Pipeline operator |> requires a callable function, got {type(func)}")

    def visit_compose_op(self, node):
        """Visit composition operator: f >> g

        Creates a new function that applies f then g.
        Examples:
            double >> increment  -> λx. increment(double(x))
            f >> g >> h          -> λx. h(g(f(x)))
        """
        # Handle function references
        # If node.first is a Variable, look it up
        if isinstance(node.first, Variable):
            func_name = node.first.name

            # Try to find function in functions dict first
            if func_name in self.functions:
                first_func = self.functions[func_name]
            else:
                # Try local/global environment
                env = self.local_env if self.local_env is not None else self.global_env
                if func_name not in env:
                    raise NameError(f"Undefined function: {func_name}")
                first_func = env[func_name]
        else:
            first_func = self.interpret(node.first)

        # If node.second is a Variable, look it up
        if isinstance(node.second, Variable):
            func_name = node.second.name

            # Try to find function in functions dict first
            if func_name in self.functions:
                second_func = self.functions[func_name]
            else:
                # Try local/global environment
                env = self.local_env if self.local_env is not None else self.global_env
                if func_name not in env:
                    raise NameError(f"Undefined function: {func_name}")
                second_func = env[func_name]
        else:
            second_func = self.interpret(node.second)

        # Store reference to self for use in nested function
        interpreter = self

        # Create a composed function
        def composed(x):
            # Apply first function
            if callable(first_func):
                intermediate = first_func(x)
            elif isinstance(first_func, FunctionDef):
                intermediate = interpreter._execute_function(first_func, [x])
            else:
                raise RuntimeError(f"Composition operator >> requires callable functions")

            # Apply second function to result
            if callable(second_func):
                return second_func(intermediate)
            elif isinstance(second_func, FunctionDef):
                return interpreter._execute_function(second_func, [intermediate])
            else:
                raise RuntimeError(f"Composition operator >> requires callable functions")

        return composed

    # ============ Cognitive-Semantic Model Visitors ============

    def visit_cognitive_entity(self, node):
        """Visit cognitive entity definition

        Creates an entity with dynamic properties that can be modified by events.
        """
        # Evaluate properties dict
        properties = self.interpret(node.properties)

        if not isinstance(properties, dict):
            raise RuntimeError(f"Cognitive entity properties must be a dict, got {type(properties)}")

        # Store entity
        self._cognitive_entities[node.name] = properties

        # Also store in global environment for easy access
        self.global_env[node.name] = properties

        return None

    def visit_cognitive_event(self, node):
        """Visit cognitive event definition

        Defines an event with participants, strength, transformations, and reactions.
        """
        # Evaluate config dict
        config = self.interpret(node.config)

        if not isinstance(config, dict):
            raise RuntimeError(f"Cognitive event config must be a dict, got {type(config)}")

        # Store event definition
        self._cognitive_events[node.name] = config

        return None

    def visit_conceptual_blueprint(self, node):
        """Visit conceptual blueprint definition

        Stores the blueprint configuration in a registry accessible to conceptual LM tooling.
        """
        config = self.interpret(node.config)

        if not isinstance(config, dict):
            raise RuntimeError(f"Conceptual blueprint config must be a dict, got {type(config)}")

        # Remove quotes from name if present
        name = node.name.strip('"').strip("'") if isinstance(node.name, str) else node.name

        # Store blueprint definition
        self._conceptual_blueprints[name] = config

        # Also store in global environment for direct access
        self.global_env[name] = config

        return None

    def visit_trigger_event(self, node):
        """Visit trigger event statement

        Triggers a cognitive event, applying its transformations and reactions.
        """
        # Get event definition
        if node.event_name not in self._cognitive_events:
            raise RuntimeError(f"Undefined cognitive event: {node.event_name}")

        event_config = self._cognitive_events[node.event_name]

        # Evaluate params if provided
        params = {}
        if node.params:
            params = self.interpret(node.params)
            if not isinstance(params, dict):
                raise RuntimeError(f"Event params must be a dict, got {type(params)}")

        # Execute event
        self._execute_cognitive_event(node.event_name, event_config, params)

        return None

    def _execute_cognitive_event(self, event_name, config, params):
        """Execute a cognitive event

        Applies transformations to entities based on participants and their degrees.
        """
        # Get participants
        participants = config.get('participants', {}) or config.get('مشاركون', {})

        # Get strength (default 1.0 for actions, 0.5 for others)
        strength = config.get('strength', 1.0) or config.get('قوة', 1.0)

        # Get transformations
        transform = config.get('transform', {}) or config.get('تحويل', {})

        # Apply transformations
        if transform:
            # Save current environment
            old_local_env = self.local_env
            self.local_env = {}

            # Add participants to local environment
            for entity_name, participant_config in participants.items():
                if entity_name in self._cognitive_entities:
                    self.local_env[entity_name] = self._cognitive_entities[entity_name]

            # Add params to local environment
            self.local_env.update(params)

            # Execute transformations
            if isinstance(transform, dict):
                # Transform is a dict of property assignments
                for key, value in transform.items():
                    # Parse key as entity.property
                    if '.' in str(key):
                        entity_name, prop_name = str(key).split('.', 1)
                        if entity_name in self._cognitive_entities:
                            # Evaluate value (only if it's not already a primitive)
                            if isinstance(value, (str, int, float, bool, type(None))):
                                new_value = value
                            else:
                                new_value = self.interpret(value)
                            # Update entity property
                            self._cognitive_entities[entity_name][prop_name] = new_value
                            # Also update in global env
                            if entity_name in self.global_env:
                                self.global_env[entity_name][prop_name] = new_value
            else:
                # Transform is a block - execute it
                self.interpret(transform)

            # Restore environment
            self.local_env = old_local_env

        # Handle reactions
        reactions = config.get('reactions', []) or config.get('ردود_فعل', []) or config.get('ردود', [])
        if reactions:
            for reaction in reactions:
                if isinstance(reaction, dict):
                    reaction_event = reaction.get('event', None) or reaction.get('حدث', None)
                    probability = reaction.get('probability', 1.0) or reaction.get('احتمال', 1.0)

                    if reaction_event:
                        # Check probability
                        if self._rng.random() <= probability:
                            # Trigger reaction event
                            if reaction_event in self._cognitive_events:
                                self._execute_cognitive_event(
                                    reaction_event,
                                    self._cognitive_events[reaction_event],
                                    params
                                )

    def visit_concurrent_events(self, node):
        """Visit concurrent events block

        Executes multiple events concurrently and combines their effects.
        """
        # If node.events is empty, extract from effects (dict-based syntax)
        if not node.events and node.effects:
            config = self.interpret(node.effects)
            if isinstance(config, dict):
                events_list = config.get('events', []) or config.get('أحداث', [])
                if events_list:
                    for event_name, strength in events_list:
                        if event_name in self._cognitive_events:
                            event_config = self._cognitive_events[event_name].copy()
                            event_config['strength'] = strength
                            self._execute_cognitive_event(event_name, event_config, {})
                    return None

        # Statement-based syntax
        for event_name, strength in node.events:
            if event_name in self._cognitive_events:
                event_config = self._cognitive_events[event_name].copy()
                # Modify strength
                event_config['strength'] = strength
                # Execute event
                self._execute_cognitive_event(event_name, event_config, {})

        # Execute combined effects if provided
        if node.effects and node.events:  # Only if not dict-based
            self.interpret(node.effects)

        return None

    def visit_linguistic_pattern(self, node):
        """Visit linguistic pattern definition

        Defines a pattern for expressing ideas linguistically.
        """
        # Evaluate config dict
        config = self.interpret(node.config)

        if not isinstance(config, dict):
            raise RuntimeError(f"Linguistic pattern config must be a dict, got {type(config)}")

        # Store pattern
        self._linguistic_patterns[node.name] = config

        return None

    def visit_idea_def(self, node):
        """Visit idea definition

        Defines an idea (cognitive concept) with entities, events, and results.
        """
        # Evaluate config dict
        config = self.interpret(node.config)

        if not isinstance(config, dict):
            raise RuntimeError(f"Idea config must be a dict, got {type(config)}")

        # Store idea
        self._ideas[node.name] = config

        return None

    # ========================================================================
    # Semantic Programming & Knowledge Management Visitor Methods
    # ========================================================================

    def visit_semantic_meaning(self, node):
        """Visit semantic meaning definition"""
        relationships = self.interpret(node.relationships)
        if not isinstance(relationships, dict):
            raise RuntimeError(f"Semantic meaning relationships must be a dict")

        # Store meaning
        self._semantic_meanings[node.name] = relationships
        self.global_env[node.name] = relationships

        return None

    def visit_semantic_query(self, node):
        """Visit semantic query"""
        # Execute the query expression
        result = self.interpret(node.query_expr)
        return result

    def visit_knowledge_info(self, node):
        """Visit knowledge information"""
        config = self.interpret(node.config)
        if not isinstance(config, dict):
            raise RuntimeError(f"Knowledge information config must be a dict")

        # Remove quotes from name if present
        name = node.name.strip('"').strip("'") if isinstance(node.name, str) else node.name

        # Store information
        self._knowledge_info[name] = config
        self.global_env[name] = config

        return None

    def visit_inference_rule(self, node):
        """Visit inference rule"""
        config = self.interpret(node.config)
        if not isinstance(config, dict):
            raise RuntimeError(f"Inference rule config must be a dict")

        # Remove quotes from name if present
        name = node.name.strip('"').strip("'") if isinstance(node.name, str) else node.name

        # Store rule
        self._inference_rules[name] = config

        return None

    def visit_infer_from(self, node):
        """Visit infer from statement"""
        statement = self.interpret(node.statement)

        # Apply all inference rules to the statement
        inferred = []
        for rule_name, rule_config in self._inference_rules.items():
            if_conditions = rule_config.get('if') or rule_config.get('إذا')
            then_conclusion = rule_config.get('then') or rule_config.get('إذن')

            # Simple pattern matching (can be enhanced)
            # For now, just store the conclusion
            if then_conclusion:
                inferred.append(then_conclusion)

        return inferred

    def visit_contradiction(self, node):
        """Visit contradiction detection"""
        items = self.interpret(node.items)

        if not isinstance(items, list):
            raise RuntimeError(f"Contradiction items must be a list")

        # Detect contradictions by comparing certainty values
        contradictions = []
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                item1 = items[i]
                item2 = items[j]

                # Check if items contradict (simplified logic)
                if isinstance(item1, str) and isinstance(item2, str):
                    if item1 in self._knowledge_info and item2 in self._knowledge_info:
                        info1 = self._knowledge_info[item1]
                        info2 = self._knowledge_info[item2]

                        # Get certainty values
                        context1 = info1.get('context') or info1.get('سياق', {})
                        context2 = info2.get('context') or info2.get('سياق', {})

                        cert1 = context1.get('certainty') or context1.get('يقين', 0.5)
                        cert2 = context2.get('certainty') or context2.get('يقين', 0.5)

                        contradictions.append({
                            'items': [item1, item2],
                            'certainties': [cert1, cert2]
                        })

        # Apply resolution strategy if provided
        if node.resolution:
            strategy = self.interpret(node.resolution)
            if strategy == "choose_highest_certainty" or strategy == "اختر_الأعلى_يقين":
                # Keep only the item with highest certainty
                for contradiction in contradictions:
                    items_list = contradiction['items']
                    certs = contradiction['certainties']
                    max_idx = certs.index(max(certs))
                    # Remove the other item
                    for idx, item in enumerate(items_list):
                        if idx != max_idx and item in self._knowledge_info:
                            del self._knowledge_info[item]

        return contradictions

    def visit_evolving_knowledge(self, node):
        """Visit evolving knowledge"""
        config = self.interpret(node.config)
        if not isinstance(config, dict):
            raise RuntimeError(f"Evolving knowledge config must be a dict")

        # Remove quotes from name if present
        name = node.name.strip('"').strip("'") if isinstance(node.name, str) else node.name

        # Store evolving knowledge
        self._evolving_knowledge[name] = config
        self.global_env[name] = config

        return None

    def visit_ontology(self, node):
        """Visit ontology definition"""
        config = self.interpret(node.config)
        if not isinstance(config, dict):
            raise RuntimeError(f"Ontology config must be a dict")

        # Remove quotes from name if present
        name = node.name.strip('"').strip("'") if isinstance(node.name, str) else node.name

        # Store ontology
        self._ontologies[name] = config
        self.global_env[name] = config

        return None

    def visit_semantic_memory(self, node):
        """Visit semantic memory operation"""
        if node.operation == "store" or node.operation == "احفظ":
            data = self.interpret(node.data)
            self._semantic_memory.append(data)
            return None
        elif node.operation == "retrieve" or node.operation == "استرجع":
            query = self.interpret(node.data)
            # Simple retrieval by matching properties
            results = []
            for memory in self._semantic_memory:
                if isinstance(memory, dict) and isinstance(query, dict):
                    # Check if query properties match memory
                    match = True
                    for key, value in query.items():
                        if key not in memory or memory[key] != value:
                            match = False
                            break
                    if match:
                        results.append(memory)
            return results
        else:
            raise RuntimeError(f"Unknown memory operation: {node.operation}")

    def visit_semantic_similarity(self, node):
        """Visit semantic similarity calculation"""
        concept1 = self.interpret(node.concept1)
        concept2 = self.interpret(node.concept2)

        # Simple similarity calculation based on shared properties
        if isinstance(concept1, dict) and isinstance(concept2, dict):
            # Count shared keys
            keys1 = set(concept1.keys())
            keys2 = set(concept2.keys())
            shared = keys1.intersection(keys2)
            total = keys1.union(keys2)

            if len(total) == 0:
                return 0.0

            # Jaccard similarity
            similarity = len(shared) / len(total)

            # Also check value similarity for shared keys
            value_matches = 0
            for key in shared:
                if concept1[key] == concept2[key]:
                    value_matches += 1

            if len(shared) > 0:
                value_similarity = value_matches / len(shared)
                # Combine both similarities
                similarity = (similarity + value_similarity) / 2

            return similarity
        else:
            # For non-dict concepts, just check equality
            return 1.0 if concept1 == concept2 else 0.0

    def visit_concept(self, node):
        """Visit concept definition"""
        properties = self.interpret(node.properties)
        if not isinstance(properties, dict):
            raise RuntimeError(f"Concept properties must be a dict")

        # Remove quotes from name if present
        name = node.name.strip('"').strip("'") if isinstance(node.name, str) else node.name

        # Store concept
        self._concepts[name] = properties
        self.global_env[name] = properties

        return None

    def visit_narrative(self, node):
        """Visit narrative definition"""
        config = self.interpret(node.config)
        if not isinstance(config, dict):
            raise RuntimeError(f"Narrative config must be a dict")

        # Remove quotes from name if present
        name = node.name.strip('"').strip("'") if isinstance(node.name, str) else node.name

        # Store narrative
        self._narratives[name] = config
        self.global_env[name] = config

        return None

    def visit_generate_narrative(self, node):
        """Visit generate narrative statement"""
        template = self.interpret(node.template)

        # Generate narrative based on template
        # This is a simplified implementation
        if isinstance(template, str):
            # Look for narrative template
            if template in self._narratives:
                narrative = self._narratives[template]

                # Generate text based on narrative structure
                structure = narrative.get('structure') or narrative.get('بنية', '')
                characters = narrative.get('characters') or narrative.get('شخصيات', {})
                events = narrative.get('events') or narrative.get('أحداث', [])

                # Simple generation: combine structure with events
                generated = f"Structure: {structure}\n"
                generated += f"Characters: {', '.join(characters.keys())}\n"
                generated += f"Events: {len(events)} events\n"

                return generated

        return None

    def visit_current_context(self, node):
        """Visit current context definition"""
        context_data = self.interpret(node.context_data)
        if not isinstance(context_data, dict):
            raise RuntimeError(f"Current context must be a dict")

        # Update current context
        self._current_context.update(context_data)
        self.global_env['context'] = self._current_context
        self.global_env['سياق'] = self._current_context

        return None

    # ========================================================================
    # Helper Methods for Semantic Programming
    # ========================================================================

    def _query_semantic_network(self, query_name, *args):
        """Query the semantic network

        Supported queries:
        - من_يدرس(subject) / who_studies(subject)
        - ما_هو(entity) / what_is(entity)
        """
        if query_name in ['من_يدرس', 'who_studies']:
            if len(args) < 1:
                return None
            subject = args[0]

            # Find all entities that study this subject
            results = []
            for name, relationships in self._semantic_meanings.items():
                studies = relationships.get('يدرس') or relationships.get('studies')
                if studies == subject:
                    results.append(name)

            return results if len(results) > 1 else (results[0] if results else None)

        elif query_name in ['ما_هو', 'what_is']:
            if len(args) < 1:
                return None
            entity = args[0]

            # Find what this entity is
            if entity in self._semantic_meanings:
                relationships = self._semantic_meanings[entity]
                is_value = relationships.get('هو') or relationships.get('is')
                return is_value

            return None

        else:
            raise RuntimeError(f"Unknown semantic query: {query_name}")

    # ========================================================================
    # EXISTENTIAL MODEL VISITORS (النموذج الوجودي)
    # ========================================================================

    def visit_domain(self, node):
        """Visit domain definition"""
        config = self.interpret(node.config)
        if not isinstance(config, dict):
            raise RuntimeError(f"Domain config must be a dict")

        # Remove quotes from name if present
        name = node.name.strip('"').strip("'") if isinstance(node.name, str) else node.name

        # Store domain
        self._domains[name] = config
        self.global_env[name] = config

        return None

    def visit_generic_environment(self, node):
        """Visit generic environment definition"""
        config = self.interpret(node.config)
        if not isinstance(config, dict):
            raise RuntimeError(f"Environment config must be a dict")

        # Remove quotes from name and domain if present
        name = node.name.strip('"').strip("'") if isinstance(node.name, str) else node.name
        domain = node.domain.strip('"').strip("'") if isinstance(node.domain, str) else node.domain

        # Add domain reference to config
        config['_domain'] = domain

        # Store environment
        self._environments[name] = config
        self.global_env[name] = config

        return None

    def visit_existential_being(self, node):
        """Visit existential being definition"""
        config = self.interpret(node.config)
        if not isinstance(config, dict):
            raise RuntimeError(f"Existential being config must be a dict")

        # Remove quotes from name, type, and domain if present
        name = node.name.strip('"').strip("'") if isinstance(node.name, str) else node.name
        entity_type = node.entity_type.strip('"').strip("'") if isinstance(node.entity_type, str) else node.entity_type
        domain = node.domain.strip('"').strip("'") if isinstance(node.domain, str) else node.domain

        # Add type and domain references to config
        config['_type'] = entity_type
        config['_domain'] = domain

        # Get environment if specified
        env_name = config.get('بيئة') or config.get('environment')
        if env_name:
            env_name = env_name.strip('"').strip("'") if isinstance(env_name, str) else env_name
            environment = self._environments.get(env_name)
            if environment:
                # Inherit meanings from environment
                inherited = config.get('معانٍ_موروثة') or config.get('inherited_meanings') or []
                if isinstance(inherited, list):
                    # Add environment dimensions to inherited meanings
                    dimensions = environment.get('أبعاد') or environment.get('dimensions') or {}
                    for dim_type, dim_values in dimensions.items():
                        if isinstance(dim_values, list):
                            inherited.extend(dim_values)

        # Store being
        self._existential_beings[name] = config
        self.global_env[name] = config

        return None

    def visit_domain_relation(self, node):
        """Visit domain relation definition"""
        config = self.interpret(node.config)
        if not isinstance(config, dict):
            raise RuntimeError(f"Domain relation config must be a dict")

        # Remove quotes from name and domain if present
        name = node.name.strip('"').strip("'") if isinstance(node.name, str) else node.name
        domain = node.domain.strip('"').strip("'") if isinstance(node.domain, str) else node.domain

        # Add domain reference to config
        config['_domain'] = domain

        # Store relation
        self._domain_relations[name] = config
        self.global_env[name] = config

        return None

    def visit_domain_action(self, node):
        """Visit domain action definition"""
        config = self.interpret(node.config)
        if not isinstance(config, dict):
            raise RuntimeError(f"Domain action config must be a dict")

        # Remove quotes from name and domain if present
        name = node.name.strip('"').strip("'") if isinstance(node.name, str) else node.name
        domain = node.domain.strip('"').strip("'") if isinstance(node.domain, str) else node.domain

        # Add domain reference to config
        config['_domain'] = domain

        # Store action
        self._domain_actions[name] = config
        self.global_env[name] = config

        return None

    def visit_metaphorical_meaning(self, node):
        """Visit metaphorical meaning definition"""
        config = self.interpret(node.config)
        if not isinstance(config, dict):
            raise RuntimeError(f"Metaphorical meaning config must be a dict")

        # Remove quotes from name and domain if present
        name = node.name.strip('"').strip("'") if isinstance(node.name, str) else node.name
        domain = node.domain.strip('"').strip("'") if isinstance(node.domain, str) else node.domain

        # Add domain reference to config
        config['_domain'] = domain

        # Store metaphorical meaning
        self._metaphorical_meanings[name] = config
        self.global_env[name] = config

        return None

    def visit_domain_law(self, node):
        """Visit domain law definition"""
        config = self.interpret(node.config)
        if not isinstance(config, dict):
            raise RuntimeError(f"Domain law config must be a dict")

        # Remove quotes from name and domain if present
        name = node.name.strip('"').strip("'") if isinstance(node.name, str) else node.name
        domain = node.domain.strip('"').strip("'") if isinstance(node.domain, str) else node.domain

        # Add domain reference to config
        config['_domain'] = domain

        # Store law
        self._domain_laws[name] = config
        self.global_env[name] = config

        return None

    def visit_existential_query(self, node):
        """Visit existential query with enhanced features"""
        config = self.interpret(node.config)
        if not isinstance(config, dict):
            raise RuntimeError(f"Existential query config must be a dict")

        # Get query parameters
        domain = config.get('في_مجال') or config.get('in_domain')
        about = config.get('عن') or config.get('about')
        conditions = config.get('شروط') or config.get('conditions') or {}

        # Enhanced query parameters
        aggregate = config.get('تجميع') or config.get('aggregate')
        sort_by = config.get('ترتيب_حسب') or config.get('sort_by')
        ascending = config.get('تصاعدي') or config.get('ascending')
        limit = config.get('حد') or config.get('limit')
        offset = config.get('إزاحة') or config.get('offset')
        return_full = config.get('إرجاع_كامل') or config.get('return_full')

        if not domain or not about:
            raise RuntimeError(f"Existential query must specify domain and about")

        # Remove quotes if present
        domain = domain.strip('"').strip("'") if isinstance(domain, str) else domain
        about = about.strip('"').strip("'") if isinstance(about, str) else about

        # Search for matching beings
        results = []
        for being_name, being_config in self._existential_beings.items():
            # Check if being is in the specified domain
            being_domain = being_config.get('_domain')
            if being_domain != domain:
                continue

            # Check if being matches the type
            being_type = being_config.get('_type')
            if about != being_type and about != 'all' and about != 'كل':
                continue

            # Check conditions (enhanced with complex logic)
            if self._check_conditions(being_config, conditions):
                if return_full:
                    results.append({'name': being_name, 'config': being_config})
                else:
                    results.append(being_name)

        # Apply aggregation if specified
        if aggregate:
            return self._apply_aggregation(results, aggregate, config)

        # Apply sorting if specified
        if sort_by:
            results = self._apply_sorting(results, sort_by, ascending)

        # Apply limit and offset
        if offset:
            results = results[offset:]
        if limit:
            results = results[:limit]

        return results

    def _check_conditions(self, being_config, conditions):
        """Check if being matches conditions (supports complex logic)"""
        if not conditions:
            return True

        # Support for logical operators
        if 'و' in conditions or 'and' in conditions:
            # AND logic
            and_conditions = conditions.get('و') or conditions.get('and')
            return all(self._check_single_condition(being_config, k, v)
                      for k, v in and_conditions.items())

        if 'أو' in conditions or 'or' in conditions:
            # OR logic
            or_conditions = conditions.get('أو') or conditions.get('or')
            return any(self._check_single_condition(being_config, k, v)
                      for k, v in or_conditions.items())

        if 'ليس' in conditions or 'not' in conditions:
            # NOT logic
            not_conditions = conditions.get('ليس') or conditions.get('not')
            return not self._check_conditions(being_config, not_conditions)

        # Simple conditions (all must match - implicit AND)
        for cond_key, cond_value in conditions.items():
            if not self._check_single_condition(being_config, cond_key, cond_value):
                return False
        return True

    def _check_single_condition(self, being_config, cond_key, cond_value):
        """Check a single condition"""
        # Support for comparison operators
        if isinstance(cond_value, dict):
            # Complex condition like {"أكبر_من": 5, "أصغر_من": 10}
            for op, val in cond_value.items():
                actual_value = self._get_being_property(being_config, cond_key)
                if not self._compare_values(actual_value, op, val):
                    return False
            return True

        # Simple equality check
        actual_value = self._get_being_property(being_config, cond_key)

        # Handle list membership
        if isinstance(actual_value, list):
            return cond_value in actual_value

        return actual_value == cond_value

    def _get_being_property(self, being_config, prop_key):
        """Get property value from being config"""
        # Check in relations
        relations = being_config.get('علاقات') or being_config.get('relations') or {}
        if prop_key in relations:
            return relations[prop_key]

        # Check in intrinsic properties
        if prop_key in being_config:
            return being_config[prop_key]

        # Check in intrinsic_properties dict
        intrinsic_props = being_config.get('خصائص_ذاتية') or being_config.get('intrinsic_properties') or {}
        if prop_key in intrinsic_props:
            return intrinsic_props[prop_key]

        return None

    def _compare_values(self, actual, operator, expected):
        """Compare values using operator"""
        if actual is None:
            return False

        op_map = {
            'أكبر_من': lambda a, e: a > e,
            'greater_than': lambda a, e: a > e,
            '>': lambda a, e: a > e,
            'أصغر_من': lambda a, e: a < e,
            'less_than': lambda a, e: a < e,
            '<': lambda a, e: a < e,
            'أكبر_أو_يساوي': lambda a, e: a >= e,
            'greater_or_equal': lambda a, e: a >= e,
            '>=': lambda a, e: a >= e,
            'أصغر_أو_يساوي': lambda a, e: a <= e,
            'less_or_equal': lambda a, e: a <= e,
            '<=': lambda a, e: a <= e,
            'يساوي': lambda a, e: a == e,
            'equals': lambda a, e: a == e,
            '==': lambda a, e: a == e,
            'لا_يساوي': lambda a, e: a != e,
            'not_equals': lambda a, e: a != e,
            '!=': lambda a, e: a != e,
            'يحتوي': lambda a, e: e in a if isinstance(a, (list, str)) else False,
            'contains': lambda a, e: e in a if isinstance(a, (list, str)) else False,
        }

        compare_fn = op_map.get(operator)
        if compare_fn:
            return compare_fn(actual, expected)

        return False

    def _apply_aggregation(self, results, aggregate, config):
        """Apply aggregation function to results"""
        agg_type = aggregate.strip('"').strip("'") if isinstance(aggregate, str) else aggregate

        if agg_type in ['عدد', 'count']:
            return len(results)

        # For other aggregations, need a field to aggregate on
        field = config.get('حقل') or config.get('field')
        if not field:
            raise RuntimeError(f"Aggregation {agg_type} requires a field")

        field = field.strip('"').strip("'") if isinstance(field, str) else field

        # Extract values
        values = []
        for item in results:
            if isinstance(item, dict):
                being_config = item['config']
            else:
                being_config = self._existential_beings.get(item, {})

            value = self._get_being_property(being_config, field)
            if value is not None and isinstance(value, (int, float)):
                values.append(value)

        if not values:
            return None

        if agg_type in ['مجموع', 'sum']:
            return sum(values)
        elif agg_type in ['متوسط', 'average', 'avg']:
            return sum(values) / len(values)
        elif agg_type in ['أصغر', 'min']:
            return min(values)
        elif agg_type in ['أكبر', 'max']:
            return max(values)

        return None

    def _apply_sorting(self, results, sort_by, ascending=True):
        """Sort results by a field"""
        field = sort_by.strip('"').strip("'") if isinstance(sort_by, str) else sort_by

        # Default to ascending if not specified
        if ascending is None:
            ascending = True

        def get_sort_key(item):
            if isinstance(item, dict):
                being_config = item['config']
            else:
                being_config = self._existential_beings.get(item, {})

            value = self._get_being_property(being_config, field)
            # Handle None values by putting them at the end
            if value is None:
                return float('inf') if ascending else float('-inf')
            return value

        return sorted(results, key=get_sort_key, reverse=not ascending)

    # ========================================================================
    # Visualization Methods
    # ========================================================================

    def visualize_environment(self, env_name):
        """Visualize an environment - returns Mermaid diagram code"""
        from .visualization import ExistentialVisualizer
        visualizer = ExistentialVisualizer(self)
        return visualizer.visualize_environment(env_name)

    def visualize_relations(self, domain_name=None):
        """Visualize relations between beings - returns Mermaid diagram code"""
        from .visualization import ExistentialVisualizer
        visualizer = ExistentialVisualizer(self)
        return visualizer.visualize_relations(domain_name)

    def visualize_being(self, being_name):
        """Visualize a being with its context - returns Mermaid diagram code"""
        from .visualization import ExistentialVisualizer
        visualizer = ExistentialVisualizer(self)
        return visualizer.visualize_being(being_name)

    def visualize_domain(self, domain_name):
        """Visualize entire domain - returns Mermaid diagram code"""
        from .visualization import ExistentialVisualizer
        visualizer = ExistentialVisualizer(self)
        return visualizer.visualize_domain(domain_name)

    def save_visualization(self, mermaid_code, filename, title="Existential Model Visualization"):
        """Save visualization as HTML file"""
        from .visualization import ExistentialVisualizer
        visualizer = ExistentialVisualizer(self)
        html = visualizer.generate_html(mermaid_code, title)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

        return filename

