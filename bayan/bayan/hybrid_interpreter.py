"""
Hybrid Interpreter for Bayan Language
مفسر هجين للغة بيان
"""

from .ast_nodes import *
from .traditional_interpreter import TraditionalInterpreter
from .logical_engine import LogicalEngine, Fact, Rule, Predicate, Term
from .entity_engine import EntityEngine
from .gse import GSEModel, generalized_sigmoid, linear_component, approximate_gate

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
        
        # Expose GSE Model
        env['GSEModel'] = GSEModel
        env['generalized_sigmoid'] = generalized_sigmoid
        env['linear_component'] = linear_component
        env['approximate_gate'] = approximate_gate
        
        # Arabic Aliases for GSE
        env['نموذج_الشكل_العام'] = GSEModel
        env['سيغمويد_معمم'] = generalized_sigmoid
        env['مكون_خطي'] = linear_component
        env['بوابة_تقريبية'] = approximate_gate
        # Share the class system and import system
        self.class_system = self.traditional.class_system
        self.import_system = self.traditional.import_system
        # Bayan module cache and search paths
        import os
        self._bayan_module_cache = {}
        cwd = os.getcwd()
        self._bayan_module_paths = [
            cwd,
            os.path.join(cwd, 'tests'),
            os.path.join(cwd, 'tests', 'bayan_modules'),
            os.path.join(cwd, 'nlp_bayan'),  # Add nlp_bayan directory
            os.path.join(cwd, 'bayan', 'libraries'),  # Add libraries directory
            os.path.join(cwd, 'ai'),  # Add ai directory for morphology
        ]

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

        # Equations / constraints helpers
        def _define_equation(entity, scope, key, expr):
            engine = self._get_or_create_engine()
            return engine.add_equation(str(entity), scope=str(scope), key=str(key), expr=str(expr))
        def _equation_state(entity, key, expr):
            engine = self._get_or_create_engine()
            return engine.add_state_equation(str(entity), str(key), str(expr))
        def _equation_property(entity, key, expr):
            engine = self._get_or_create_engine()
            return engine.add_property_equation(str(entity), str(key), str(expr))
        def _define_complement(entity, scope, base_key, complement_key, total: float = 1.0):
            engine = self._get_or_create_engine()
            return engine.define_complement(str(entity), scope=str(scope), base_key=str(base_key), complement_key=str(complement_key), total=float(total))
        def _define_opposites(entity, scope, key_a, key_b, total: float = 1.0):
            engine = self._get_or_create_engine()
            return engine.define_opposites(str(entity), scope=str(scope), key_a=str(key_a), key_b=str(key_b), total=float(total))
        env['define_equation'] = _define_equation
        env['equation_state'] = _equation_state
        env['equation_property'] = _equation_property
        env['define_complement'] = _define_complement
        env['define_opposites'] = _define_opposites
        env['عرّف_معادلة'] = _define_equation
        env['معادلة_حالة'] = _equation_state
        env['معادلة_خاصية'] = _equation_property
        env['عرّف_متمم'] = _define_complement
        env['عرّف_أضداد'] = _define_opposites

        # Concept comparison helper (utility only)
        def _compare_concepts(before: dict, after: dict, tolerance: float = 0.1):
            def _num(v):
                try:
                    return float(v)
                except Exception:
                    return None
            changes = {}
            keys = set(before.keys()) | set(after.keys())
            for k in keys:
                b = before.get(k)
                a = after.get(k)
                bn = _num(b)
                an = _num(a)
                if bn is not None and an is not None:
                    if abs(an - bn) > tolerance:
                        changes[k] = {'before': bn, 'after': an, 'delta': an - bn}
                else:
                    if a != b:
                        changes[k] = {'before': b, 'after': a}
            return changes
        env['compare_concepts'] = _compare_concepts
        env['قارن_المفاهيم'] = _compare_concepts


        # Linguistic Operators (thin wrappers over perform)
        def _make_action_wrapper(_action_name: str):
            def _fn(participants, states=None, properties=None, value: float = 1.0):
                engine = self._get_or_create_engine()
                return engine.perform_action(_action_name, participants, states=states, properties=properties, action_value=float(value))
            return _fn
        # English operators
        env['Go'] = _make_action_wrapper('go')
        env['Affect'] = _make_action_wrapper('affect')
        env['Consume'] = _make_action_wrapper('consume')
        env['Bond'] = _make_action_wrapper('bond')
        env['Transform'] = _make_action_wrapper('transform')
        # Arabic operators
        env['اذهب'] = _make_action_wrapper('اذهب')
        env['أثّر'] = _make_action_wrapper('أثر')
        env['اثر'] = env['أثّر']
        env['أكل'] = _make_action_wrapper('أكل')
        env['اكل'] = env['أكل']
        env['اربط'] = _make_action_wrapper('اربط')
        env['حوّل'] = _make_action_wrapper('حوّل')
        env['حول'] = env['حوّل']

        # Dynamic operator definition (user-defined wrappers)
        def _define_operator(name: str, action: str | None = None, alias: str | None = None):
            act = str(action) if action is not None else str(name)
            def _dyn_op(participants, states=None, properties=None, value: float = 1.0):
                engine = self._get_or_create_engine()
                return engine.perform_action(act, participants, states=states, properties=properties, action_value=float(value))
            env[str(name)] = _dyn_op
            if alias:
                env[str(alias)] = _dyn_op
            return True
        env['define_operator'] = _define_operator
        env['عرّف_مشغل'] = _define_operator

        # Event/history helpers
        def _events(actor=None, action=None, target=None):
            engine = self._get_or_create_engine()
            def _ok(evt):
                if actor is not None and evt.get('actor') != actor: return False
                if action is not None and evt.get('action') != action: return False
                if target is not None and evt.get('target') != target: return False
                return True
            return [e for e in engine.events if _ok(e)]
        def _clear_events():
            engine = self._get_or_create_engine()
            engine.events.clear()
        def _last_participants():
            engine = self._get_or_create_engine()
            return list(getattr(engine, '_last_participants', []))
        def _event_texts(lang='en'):
            engine = self._get_or_create_engine()
            key = 'summary_en' if str(lang).lower().startswith('e') else 'summary_ar'
            out = []
            for evt in engine.events:
                if key in evt:
                    out.append(evt[key])
                else:
                    # Back-compat if summaries missing
                    out.append(f"{evt.get('actor')} -> {evt.get('action')} -> {evt.get('target')}")
            return out
        env['events'] = _events
        env['get_events'] = _events
        env['clear_events'] = _clear_events
        env['last_participants'] = _last_participants
        env['event_texts'] = _event_texts
        env['describe_events'] = _event_texts
        env['الأحداث'] = _events
        env['سجل_الأحداث'] = _events
        env['امسح_الأحداث'] = _clear_events
        env['آخر_مشاركين'] = _last_participants
        env['نص_الأحداث'] = _event_texts
        env['وصف_الأحداث'] = _event_texts

        # --- Linguistic logic helpers (facts/rules sugar) ---
        def _assert_fact(_name: str, *args):
            """Assert a fact predicate(args). Accepts numbers/strings."""
            pred = Predicate(str(_name), [Term(a, is_variable=False) if not isinstance(a, Term) else a for a in args])
            self.logical.assertz(Fact(pred))
            return True

        def _assert_is(subject, klass):
            # isa(subject, klass) and unary klass(subject)
            _assert_fact('isa', str(subject), str(klass))
            _assert_fact(str(klass), str(subject))
            return True

        def _parse_attr_items(attrs):
            # attrs: list like ["كريم", "شجاع:0.7"] or comma-separated string
            items = []
            if attrs is None:
                return items
            if isinstance(attrs, str):
                parts = [p.strip() for p in attrs.split(',') if p.strip()]
            else:
                parts = list(attrs)
            for it in parts:
                name = str(it)
                deg = None
                if isinstance(it, (int, float)):
                    name = str(it)
                else:
                    # parse suffix :0.7 or .0.7
                    if ':' in name:
                        base, d = name.split(':', 1)
                        try:
                            deg = float(d)
                            name = base
                        except Exception:
                            deg = None
                    elif '.' in name:
                        base, d = name.split('.', 1)
                        try:
                            deg = float(d)
                            name = base
                        except Exception:
                            deg = None
                items.append((name, deg))
            return items

        def _assert_attrs(subject, attrs):
            # attribute(subject, a) [+ attribute(subject,a,deg)] and unary a(subject)
            for (adj, deg) in _parse_attr_items(attrs):
                _assert_fact('attribute', str(subject), str(adj))
                _assert_fact(str(adj), str(subject))
                if deg is not None:
                    _assert_fact('attribute', str(subject), str(adj), float(deg))
            return True

        def _assert_of(head, genitive):
            # of(head, genitive) and synonyms: genitive(head, genitive), from(head, genitive)
            _assert_fact('of', str(head), str(genitive))
            _assert_fact('genitive', str(head), str(genitive))
            _assert_fact('from', str(head), str(genitive))
            return True

        def _assert_belongs(owned, owner):
            # belongs_to(owned, owner) and owner_of(owner, owned)
            _assert_fact('belongs_to', str(owned), str(owner))
            _assert_fact('owner_of', str(owner), str(owned))
            return True

        # English bindings
        env['assert_fact'] = _assert_fact
        env['assert_is'] = _assert_is
        env['assert_attrs'] = _assert_attrs
        env['assert_of'] = _assert_of
        env['assert_belongs'] = _assert_belongs
        env['isa'] = lambda s, c: _assert_is(s, c)
        env['of'] = lambda h, g: _assert_of(h, g)
        env['belongs_to'] = lambda t, o: _assert_belongs(t, o)
        env['owner_of'] = lambda o, t: _assert_belongs(t, o)

        # Arabic bindings
        env['أثبت_حقيقة'] = _assert_fact
        env['أثبت_يكون'] = _assert_is
        env['أثبت_صفات'] = _assert_attrs
        env['أثبت_إضافة'] = _assert_of
        env['أثبت_يعود'] = _assert_belongs
        env['يكون'] = lambda s, c: _assert_is(s, c)
        env['إضافة'] = lambda h, g: _assert_of(h, g)
        env['يعود'] = lambda t, o: _assert_belongs(t, o)
        # --- Phrase helpers for nominal templates (EN/AR) ---
        def _strip_al_ar(s: str) -> str:
            try:
                if isinstance(s, str) and s.startswith("ال"):
                    return s[2:]
            except Exception:
                pass
            return s

        # --- Nominal templates registry and helpers ---
        env['_nominal_templates'] = env.get('_nominal_templates', {})
        env['_nominal_head_hints'] = env.get('_nominal_head_hints', {})

        # Built-in head hints (safe defaults) for common nominal heads (AR/EN)
        _default_head_hints = {
            # belongs: "X الY" → belongs_to(Y, X)
            "مالك": {"relation": "belongs", "order": "BA", "strip_definite": True},
            "صاحب": {"relation": "belongs", "order": "BA", "strip_definite": True},
            "owner": {"relation": "belongs", "order": "BA", "strip_definite": True},
            # of/genitive: "Head Genitive"
            "عصير": {"relation": "of", "order": "AB", "strip_definite": True},
            "juice": {"relation": "of", "order": "AB", "strip_definite": True},
            "باب": {"relation": "of", "order": "AB", "strip_definite": True},
            "door": {"relation": "of", "order": "AB", "strip_definite": True},
            "صورة": {"relation": "of", "order": "AB", "strip_definite": True},
            "picture": {"relation": "of", "order": "AB", "strip_definite": True},
            # professional/role heads → of
            "كاتب": {"relation": "of", "order": "AB", "strip_definite": True},
            "writer": {"relation": "of", "order": "AB", "strip_definite": True},
            "مدير": {"relation": "of", "order": "AB", "strip_definite": True},
            "manager": {"relation": "of", "order": "AB", "strip_definite": True},
            "رئيس": {"relation": "of", "order": "AB", "strip_definite": True},
            # additional heads → of
            "مؤلف": {"relation": "of", "order": "AB", "strip_definite": True},
            "author": {"relation": "of", "order": "AB", "strip_definite": True},
            "كتاب": {"relation": "of", "order": "AB", "strip_definite": True},
            "book": {"relation": "of", "order": "AB", "strip_definite": True},
            "photo": {"relation": "of", "order": "AB", "strip_definite": True},
            "صورة فوتوغرافية": {"relation": "of", "order": "AB", "strip_definite": True},
        }
        for _k, _v in _default_head_hints.items():
            if _k not in env['_nominal_head_hints']:
                env['_nominal_head_hints'][_k] = _v

        def _normalize_relation(name: str) -> str:
            s = str(name)
            if s in ('يكون',):
                return 'isa'
            if s in ('إضافة', 'genitive', 'من'):
                return 'of'
            if s in ('يعود', 'ملكية', 'ملك'):
                return 'belongs'
            return s.lower()

        def _define_nominal_template(name, relation='isa', order='AB', strip_definite=True):
            env['_nominal_templates'][str(name)] = {
                'relation': _normalize_relation(relation),
                'order': 'BA' if str(order).upper() == 'BA' else 'AB',
                'strip_definite': bool(strip_definite),
            }
            return True

        def _apply_nominal_template(name, a, b):
            tpl = env['_nominal_templates'].get(str(name))
            if not tpl:
                return False
            rel = tpl['relation']; order = tpl['order']
            sa, sb = (a, b) if order == 'AB' else (b, a)
            if rel in ('isa', 'is', 'class'):
                return _assert_is(sa, sb)
            if rel in ('of', 'genitive', 'from'):
                return _assert_of(sa, sb)
            if rel in ('belongs', 'belongs_to', 'owner', 'owner_of'):
                return _assert_belongs(sa, sb)
            return _assert_is(sa, sb)

        def _define_head_template(head, template_or_relation, order=None, strip_definite=None):
            # Resolve possibly by template name
            tpl = env['_nominal_templates'].get(str(template_or_relation))
            if tpl:
                rel = tpl['relation']
                ordv = tpl['order']
                sd = tpl.get('strip_definite', True)
            else:
                rel = _normalize_relation(template_or_relation)
                ordv = 'BA' if (str(order).upper() == 'BA') else 'AB' if order else 'AB'
                sd = True if strip_definite is None else bool(strip_definite)
            env['_nominal_head_hints'][str(head)] = {'relation': rel, 'order': ordv, 'strip_definite': sd}
            return True

        def _assert_phrase(text, relation=None, strip_definite=True):
            """Assert a nominal phrase into facts.
            Examples:
              - phrase("محمد الطبيب", relation="isa")
              - phrase("عصير العنب", relation="of")
              - phrase("مالك البيت", relation="belongs")
            """
            if text is None:
                return False
            if not isinstance(text, str):
                text = str(text)
            parts = [p for p in text.strip().split() if p]
            if len(parts) < 2:
                return False
            a, b = parts[0], parts[1]

            rel_l = None
            order = 'AB'

            # Relation from explicit argument or template name
            if relation is not None:
                # If refers to a registered template, use it
                tpl = env['_nominal_templates'].get(str(relation))
                if tpl:
                    rel_l = tpl['relation']
                    order = tpl['order']
                    # keep strip_definite as passed by caller
                else:
                    rel_l = _normalize_relation(relation)
                    if rel_l == 'belongs':
                        order = 'BA'
            else:
                # Try head hint
                hint = env['_nominal_head_hints'].get(a)
                if hint:
                    rel_l = hint.get('relation')
                    order = hint.get('order', 'AB')
                    sd_hint = hint.get('strip_definite')
                    if sd_hint is not None:
                        strip_definite = sd_hint

            if strip_definite:
                a = _strip_al_ar(a)
                b = _strip_al_ar(b)

            # Default if still unknown
            if not rel_l:
                rel_l = 'isa'

            # Apply ordering
            sa, sb = (a, b) if order == 'AB' else (b, a)

            if rel_l in ('isa', 'is', 'class'):
                return _assert_is(sa, sb)
            elif rel_l in ('of', 'genitive', 'from'):
                return _assert_of(sa, sb)
            elif rel_l in ('belongs', 'belongs_to', 'owner', 'owner_of'):
                return _assert_belongs(sa, sb)
            else:
                return _assert_is(sa, sb)

        def _assert_phrases(items, relation=None, strip_definite=True):
            if items is None:
                return False
            seq = []
            if isinstance(items, str):
                if ('\n' in items) or (',' in items):
                    tmp = []
                    for line in items.splitlines():
                        tmp += [p.strip() for p in line.split(',') if p.strip()]
                    seq = tmp
                else:
                    seq = [items]
            else:
                seq = list(items)
            ok = True
            for it in seq:
                ok = _assert_phrase(it, relation=relation, strip_definite=strip_definite) and ok
            return ok

        # English bindings
        env['assert_phrase'] = _assert_phrase
        env['phrase'] = _assert_phrase
        env['assert_phrases'] = _assert_phrases
        env['phrases'] = _assert_phrases
        env['define_nominal_template'] = _define_nominal_template
        env['apply_template'] = _apply_nominal_template
        env['define_head_template'] = _define_head_template

        # Arabic bindings
        env['أثبت_عبارة'] = _assert_phrase
        env['عبارة'] = _assert_phrase
        env['أثبت_عبارات'] = _assert_phrases
        env['عبارات'] = _assert_phrases
        env['عرّف_قالب_عبارة'] = _define_nominal_template
        env['طبق_قالب'] = _apply_nominal_template
        env['عرّف_قالب_رأس'] = _define_head_template


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
        elif isinstance(node, PhraseStatement):
            return self.visit_phrase_statement(node)
        elif isinstance(node, CauseEffectStatement):
            return self.visit_cause_effect_statement(node)
        elif isinstance(node, RelationStatement):
            return self.visit_relation_statement(node)
        elif isinstance(node, EntityDef):
            return self.visit_entity_def(node)
        elif isinstance(node, ConceptDef):
            return self.visit_concept_def(node)
        elif isinstance(node, ApplyActionStmt):
            return self.visit_apply_action_stmt(node)
        elif isinstance(node, ImportStatement):
            return self.visit_import_statement(node)
        elif isinstance(node, FromImportStatement):
            return self.visit_from_import_statement(node)
        else:
            # Delegate to traditional interpreter
            return self.traditional.interpret(node)

    def visit_phrase_statement(self, node):
        """Evaluate grammar-sugar nominal phrase by delegating to phrase/عبارة env function."""
        env = self.traditional.global_env
        fn = env.get('phrase') or env.get('عبارة')
        if fn:
            if getattr(node, 'relation', None) is not None:
                return fn(node.text, relation=node.relation)
            return fn(node.text)
        return None
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
        rel_base = module_name.replace('.', os.sep)
        for base in self._bayan_module_paths:
            for ext in ('.bayan', '.by'):
                candidate = os.path.join(base, rel_base + ext)
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
            # If module name contains slashes or dots, use the last part as default alias
            if not node.alias and ('/' in name or '.' in name):
                name = name.replace('/', '.').split('.')[-1]
            
            env = self.traditional.local_env if self.traditional.local_env is not None else self.traditional.global_env
            env[name] = proxy
            
            # Also register functions directly if it's a simple import (optional, but helpful for 'include' style)
            # Actually, 'include' is different. 'import' should namespace.
            # But wait, the test uses `apply_pattern` directly without namespace.
            # The test uses `include "ai/morphology.bayan"`.
            # `include` is handled by TraditionalInterpreter._include which executes in current scope.
            # So why did it fail?
            # Ah, `include` in TraditionalInterpreter uses `self.interpret(ast)`.
            # `self` is TraditionalInterpreter.
            # But `ast` contains `FunctionDef`.
            # `TraditionalInterpreter.visit_function_def` registers function in `self.functions`.
            # So it should work.
            
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
        """Visit a logical fact (supports optional probability via fact[prob])"""
        # Convert AST LogicalPredicate to logical_engine Predicate
        print(f"DEBUG: Visiting LogicalFact: {node.predicate} (Type: {type(node.predicate)})")
        predicate = self.traditional._convert_to_predicate(node.predicate)
        print(f"DEBUG: Converted predicate: {predicate}")
        if not predicate:
            return None
            
        prob = None
        if getattr(node, 'probability', None) is not None:
            prob = self.traditional.interpret(node.probability)
        
        fact = Fact(predicate, probability=prob)
        self.logical.add_fact(fact)
        return None
    def visit_concept_def(self, node):
        """Install a concept as a runtime set and assert logical in_concept(Name, Elem) facts."""
        # Evaluate set literal to a Python set
        members = self.traditional.interpret(node.set_node)
        if not isinstance(members, (set, list, tuple)):
            raise TypeError("concept expects a set literal or set-like value")
        # Store as a runtime variable for membership tests (x in Animal)
        env = self.traditional.local_env if self.traditional.local_env is not None else self.traditional.global_env
        env[node.name] = set(members)
        # Assert logical facts
        for m in members:
            pred = Predicate('in_concept', [Term(str(node.name)), Term(str(m))])
            self.logical.add_fact(Fact(pred))
        return None

    def visit_logical_rule(self, node):
        """Visit a logical rule"""
        from .logical_engine import Predicate, Term
        
        # Convert AST nodes to logical_engine objects
        # Check if head is already a Predicate
        if isinstance(node.head, Predicate):
            head = node.head
        else:
            head = self.traditional._convert_to_predicate(node.head)
            if not head:
                return None
            
        body = []
        for goal in node.body:
            # Check if goal is already a Predicate (from parser)
            if isinstance(goal, Predicate):
                # Fix: Parser creates Terms without proper is_variable flag
                # Rebuild the predicate with corrected Terms
                fixed_args = []
                for arg in goal.args:
                    if isinstance(arg, Term):
                        # Check if this should be a variable (starts with uppercase or ? or already flagged)
                        val = str(arg.value)
                        is_var = getattr(arg, 'is_variable', False) or val.startswith('?') or (val and val[0].isupper())
                        fixed_args.append(Term(arg.value, is_variable=is_var))
                    else:
                        fixed_args.append(arg)
                fixed_pred = Predicate(goal.name, fixed_args)
                body.append(fixed_pred)
            else:
                pred = self.traditional._convert_to_predicate(goal)
                if pred:
                    body.append(pred)
        
        rule = Rule(head, body)
        self.logical.add_rule(rule)
        return None

    def visit_cause_effect_statement(self, node):
        """Visit a cause-effect statement: سبب_نتيجة(condition, result, cause, strength).

        Stores it as a logical fact: سبب_نتيجة(condition, result, cause, strength).
        """
        # The parser already returns Term objects, so use them directly
        args = [node.condition, node.result, node.cause]

        # Add strength if provided
        if node.strength is not None:
            args.append(node.strength)

        # Create predicate and fact
        predicate = Predicate('سبب_نتيجة', args)
        fact = Fact(predicate)
        self.logical.add_fact(fact)
        return None

    def visit_relation_statement(self, node):
        """Visit a relation statement: علاقة(from, relation_type, to, strength).

        Stores it as a logical fact: علاقة(from, relation_type, to, strength).
        """
        # The parser already returns Term objects, so use them directly
        args = [node.from_concept, node.relation_type, node.to_concept]

        # Add strength if provided
        if node.strength is not None:
            args.append(node.strength)

        # Create predicate and fact
        predicate = Predicate('علاقة', args)
        fact = Fact(predicate)
        self.logical.add_fact(fact)
        return None

    def visit_logical_query(self, node):
        """Visit a logical query"""
        from .logical_engine import Predicate
        
        # Check if goal is already a Predicate (from parser) or needs conversion
        if isinstance(node.goal, Predicate):
            goal = node.goal
        else:
            # Convert AST goal to logical_engine Predicate
            goal = self.traditional._convert_to_predicate(node.goal)
            if not goal:
                return []
            
        solutions = self.logical.query(goal)

        # Convert solutions to dictionaries (include '__prob')
        results = []
        for substitution in solutions:
            result_dict = {}
            for var_name, value in substitution.bindings.items():
                # Dereference to get the final bound value (if any)
                try:
                    resolved = self.logical._deref(value, substitution)
                except Exception:
                    resolved = value
                # Extract underlying value for Terms; otherwise keep as is
                final_val = getattr(resolved, 'value', resolved)
                result_dict[var_name] = final_val
            # Attach aggregated probability if available
            result_dict['__prob'] = float(getattr(substitution, 'probability', 1.0))
            results.append(result_dict)

        # Best-effort console display for interactive use inside hybrid blocks
        try:
            # Collect only variables that appear in the original query goal
            goal_vars = set()
            if goal is not None and hasattr(goal, 'args'):
                for arg in goal.args:
                    # arg is a Term from logical_engine with .is_variable and .value
                    if hasattr(arg, 'is_variable') and getattr(arg, 'is_variable', False):
                        name = getattr(arg, 'value', None)
                        if name is not None:
                            goal_vars.add(name)

            if results:
                # If variable bindings exist, print only goal vars; else print a generic confirmation
                printed_any = False
                for r in results:
                    parts = []
                    for k, v in r.items():
                        if goal_vars and k not in goal_vars:
                            continue
                        val = getattr(v, 'value', v)
                        parts.append(f"?{k}={val}")
                    if parts:
                        print(", ".join(parts))
                        printed_any = True
                if not printed_any:
                    # No goal variables or no bindings to show
                    print("(true)")
            else:
                print("(no solutions)")
        except Exception:
            # Do not fail execution because of display issues
            pass

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

        # Convert solutions to dictionaries (include '__prob')
        results = []
        for substitution in solutions:
            result_dict = {}
            for var_name, value in substitution.bindings.items():
                result_dict[var_name] = value
            result_dict['__prob'] = float(getattr(substitution, 'probability', 1.0))
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


