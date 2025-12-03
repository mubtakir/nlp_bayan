"""
Entity Engine for Bayan Language
محرك الكيانات للغة بيان

Purpose
- Maintain entities with fuzzy states/properties [0..1]
- Define actions with effects and optional conditions
- Apply actions (actor -> action -> target) and update states
- Mirror states/properties as logical facts so they are queryable:
    - entity(Name).
    - state(Entity, Key, Value).
    - property(Entity, Key, Value).
    - event(Actor, Action, Target, Value).

This is a conservative library layer (no syntax changes). You can use it from
traditional Bayan code and query results in logic blocks or query expressions.

Example (inside a Bayan program):
    engine = EntityEngine(logical)
    engine.create_entity("أحمد", states={"جوع": 0.6})
    engine.create_entity("محمد")
    engine.define_action("محمد", "تقديم_وجبة", effects=[{"on": "جوع", "formula": "value - 0.4*action_value"}])
    engine.apply_action("محمد", "تقديم_وجبة", "أحمد", action_value=1.0)
    # Then you can query: result = query state("أحمد", "جوع", ?V)?
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple
import ast as _ast
import math as _math
import random as _random

from .logical_engine import Term, Predicate, Fact


# ----------------------------- Utilities ---------------------------------

def _clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, float(x)))


class _SafeExpr:
    """Very small safe arithmetic evaluator for effect formulas.
    Allowed:
      - Numbers, + - * / **, parentheses, unary +/-, names: value, action_value, power, sensitivity
      - Functions: min, max, clamp, sqrt, rand() (uniform 0..1)
    """

    ALLOWED_FUNCS = {
        'min': min,
        'max': max,
        'clamp': _clamp,
        'sqrt': _math.sqrt,
        'abs': abs,
        'sin': _math.sin,
        'cos': _math.cos,
        'tan': _math.tan,
        'exp': _math.exp,
        'log': _math.log,
        'rand': lambda: _random.random(),
    }

    @classmethod
    def eval(cls, expr: str, variables: Dict[str, Any]) -> float:
        node = _ast.parse(expr, mode='eval')
        return float(cls._eval_node(node.body, variables))

    @classmethod
    def _eval_node(cls, node, vars):
        if isinstance(node, _ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Only numeric constants allowed")
        if isinstance(node, _ast.Name):
            if node.id in vars:
                return vars[node.id]
            if node.id in cls.ALLOWED_FUNCS and callable(cls.ALLOWED_FUNCS[node.id]):
                # zero-arg call form like rand used without () is not allowed
                raise ValueError("Function name used without call")
            raise ValueError(f"Unknown name: {node.id}")
        if isinstance(node, _ast.BinOp):
            left = cls._eval_node(node.left, vars)
            right = cls._eval_node(node.right, vars)
            if isinstance(node.op, _ast.Add):
                return left + right
            if isinstance(node.op, _ast.Sub):
                return left - right
            if isinstance(node.op, _ast.Mult):
                return left * right
            if isinstance(node.op, _ast.Div):
                return left / right
            if isinstance(node.op, _ast.Pow):
                return left ** right
            raise ValueError("Operator not allowed")
        if isinstance(node, _ast.UnaryOp) and isinstance(node.op, (_ast.UAdd, _ast.USub)):
            val = cls._eval_node(node.operand, vars)
            return +val if isinstance(node.op, _ast.UAdd) else -val
        if isinstance(node, _ast.Call):
            if not isinstance(node.func, _ast.Name):
                raise ValueError("Only simple function calls allowed")
            fname = node.func.id
            if fname not in cls.ALLOWED_FUNCS:
                raise ValueError(f"Function not allowed: {fname}")
            if node.keywords:
                raise ValueError("No keyword args allowed in formulas")
            args = [cls._eval_node(a, vars) for a in node.args]
            func = cls.ALLOWED_FUNCS[fname]
            return func(*args)
        if isinstance(node, _ast.Expr):
            return cls._eval_node(node.value, vars)
        raise ValueError("Unsupported expression in formula")


# ------------------------------ Data -------------------------------------

@dataclass
class _ActionEffect:
    on: str  # state key to affect
    formula: str  # expression string using names: value, action_value, power, sensitivity
    condition: Optional[str] = None  # optional expression returning truthy

@dataclass
class _Reaction:
    sensitivity: float = 1.0
    response: Optional[str] = None  # e.g., "غضب += 0.5" or "ثقة += sensitivity*action_value"

@dataclass
class _Entity:
    name: str
    states: Dict[str, float] = field(default_factory=dict)
    properties: Dict[str, float] = field(default_factory=dict)
    actions: Dict[str, Dict[str, Any]] = field(default_factory=dict)  # action_name -> {power, effects: List[_ActionEffect]}
    reactions: Dict[str, _Reaction] = field(default_factory=dict)     # action_name -> Reaction on receiving
    # Optional type metadata per key
    state_types: Dict[str, Dict[str, Any]] = field(default_factory=dict)      # key -> {kind: fuzzy|numeric|bounded, min, max}
    property_types: Dict[str, Dict[str, Any]] = field(default_factory=dict)   # key -> {kind: ...}
    # Optional equations/constraints applied after updates: list of {scope: 'state'|'property', key: str, expr: str}
    constraints: List[Dict[str, Any]] = field(default_factory=list)


# --------------------------- Entity Engine --------------------------------

class EntityEngine:
    def __init__(self, logical_engine):
        if logical_engine is None:
            raise ValueError("EntityEngine requires a logical engine (pass 'logical')")
        self.logical = logical_engine
        self.entities: Dict[str, _Entity] = {}
        # Groups and discourse helpers
        self.groups: Dict[str, List[str]] = {}
        self._last_participants: List[str] = []
        # Event log for downstream analysis/training data
        self.events: List[Dict[str, Any]] = []
        # Constraint enforcement guard to avoid recursion
        self._in_enforce: bool = False

    # --------- Type handling (optional) ---------
    def _default_typeinfo(self, kind: str = 'fuzzy') -> Dict[str, Any]:
        if kind == 'numeric':
            return {'kind': 'numeric'}
        if kind == 'bounded':
            # caller should override min/max
            return {'kind': 'bounded', 'min': 0.0, 'max': 1.0}
        # default fuzzy 0..1
        return {'kind': 'fuzzy', 'min': 0.0, 'max': 1.0}

    def _parse_type_spec(self, spec: Any) -> Dict[str, Any]:
        """Parse a type spec from strings or dicts (bilingual keys supported).
        Accepted forms:
          - 'fuzzy' / 'ضبابي'
          - 'numeric' / 'عددي'
          - {'bounded': [min, max]} / {'نطاق': [min, max]}
          - {'type': 'bounded', 'min': x, 'max': y} (or Arabic min/max)
        Returns a normalized dict: {'kind': 'fuzzy'|'numeric'|'bounded', 'min'?, 'max'?}
        """
        # direct strings
        if isinstance(spec, str):
            s = spec.strip().lower()
            if s in ('fuzzy', 'ضبابي'):
                return self._default_typeinfo('fuzzy')
            if s in ('numeric', 'عددي'):
                return self._default_typeinfo('numeric')
            if s in ('bounded', 'محدود'):
                return self._default_typeinfo('bounded')
        # dict forms
        if isinstance(spec, dict):
            # nested bounded list: {'bounded': [min, max]} or Arabic
            for key in ('bounded', 'نطاق', 'range', 'bounds'):
                if key in spec:
                    arr = spec[key]
                    if isinstance(arr, (list, tuple)) and len(arr) == 2:
                        return {'kind': 'bounded', 'min': float(arr[0]), 'max': float(arr[1])}
            # flat: {'type': 'bounded', 'min': x, 'max': y}
            tval = spec.get('type') or spec.get('نوع')
            if tval:
                tinfo = self._parse_type_spec(tval)
                if tinfo['kind'] == 'bounded':
                    mn = spec.get('min') or spec.get('حد_أدنى')
                    mx = spec.get('max') or spec.get('حد_أقصى')
                    if mn is not None and mx is not None:
                        tinfo['min'] = float(mn)
                        tinfo['max'] = float(mx)
                return tinfo
        # fallback
        return self._default_typeinfo('fuzzy')

    def _coerce_value_and_type(self, raw: Any, default_kind: str = 'fuzzy') -> Tuple[Any, Dict[str, Any]]:
        """Accept numeric or typed-dict like {'type': 'numeric'|'fuzzy'|{'bounded':[a,b]}, 'value': x}
        Also accepts Arabic keys: 'نوع', 'قيمة'.
        Also accepts string values for non-numeric properties.
        Returns (value, typeinfo)
        """
        if isinstance(raw, dict):
            # value field
            val = raw.get('value')
            if val is None and 'قيمة' in raw:
                val = raw.get('قيمة')
            # type field (may be string or dict)
            tspec = raw.get('type')
            if tspec is None and 'نوع' in raw:
                tspec = raw.get('نوع')
            # allow putting bounds at top-level too
            tinfo = self._parse_type_spec(tspec if tspec is not None else raw)
            if val is None:
                # If dict had no value, but was actually a bounds dict, default value 0.0
                val = 0.0
            # Try to convert to float, but keep as-is if it's a string
            try:
                return float(val), tinfo
            except (ValueError, TypeError):
                # Keep string values as-is with 'string' type
                return val, {'kind': 'string'}
        # Handle string values (non-numeric properties)
        if isinstance(raw, str):
            # Try to convert to float first
            try:
                tinfo = self._default_typeinfo(default_kind)
                return float(raw), tinfo
            except ValueError:
                # Keep as string
                return raw, {'kind': 'string'}
        # plain number: default to fuzzy (to preserve existing semantics)
        tinfo = self._default_typeinfo(default_kind)
        return float(raw), tinfo

    def _get_typemap(self, ent: _Entity, is_state: bool) -> Dict[str, Dict[str, Any]]:
        return ent.state_types if is_state else ent.property_types

    def _apply_bounds(self, ent: _Entity, is_state: bool, key: str, value: Any) -> Any:
        tmap = self._get_typemap(ent, is_state)
        tinfo = tmap.get(key)
        if not tinfo:
            # Check if value is a string - don't try to clamp strings
            if isinstance(value, str):
                return value
            # default semantics: fuzzy clamp
            return _clamp(value)
        kind = tinfo.get('kind', 'fuzzy')
        if kind == 'string':
            # String values are returned as-is
            return value
        if kind == 'numeric':
            return float(value)
        # fuzzy or bounded
        mn = float(tinfo.get('min', 0.0))
        mx = float(tinfo.get('max', 1.0))
        return max(mn, min(mx, float(value)))

    def _normalize_initial_map(self, ent: _Entity, src: Optional[Dict[str, Any]], *, is_state: bool, default_kind: str = 'fuzzy') -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if not src:
            return result
        tmap = self._get_typemap(ent, is_state)
        for k, raw in src.items():
            val, tinfo = self._coerce_value_and_type(raw, default_kind=default_kind)
            tmap[k] = tinfo
            result[k] = self._apply_bounds(ent, is_state, k, val)
        return result

    # --------- Logical KB helpers ---------
    def _assert_fact(self, name: str, *args: Any) -> None:
        terms = [Term(a, is_variable=False) for a in args]
        self.logical.add_fact(Fact(Predicate(name, terms)))

    def _retractall(self, name: str, *args: Any) -> None:
        # Replace any wildcard with a fresh variable; concrete constants keep as-is
        subterms = []
        for a in args:
            if a is None:
                # variable to match anything
                subterms.append(Term('X', is_variable=True))
            else:
                subterms.append(Term(a, is_variable=False))
        self.logical.retractall(Predicate(name, subterms))

    def _sync_entity_facts(self, ent: _Entity) -> None:
        # entity(Name).
        self._retractall('entity', ent.name)
        self._assert_fact('entity', ent.name)
        # states
        for k, v in ent.states.items():
            self._retractall('state', ent.name, k, None)
            # Handle both numeric and string values
            try:
                self._assert_fact('state', ent.name, k, float(v))
            except (ValueError, TypeError):
                self._assert_fact('state', ent.name, k, v)
        # properties
        for k, v in ent.properties.items():
            self._retractall('property', ent.name, k, None)
            # Handle both numeric and string values
            try:
                self._assert_fact('property', ent.name, k, float(v))
            except (ValueError, TypeError):
                self._assert_fact('property', ent.name, k, v)

    # ------------- API -------------
    def create_entity(self, name: str, *, states: Optional[Dict[str, Any]] = None,
                      properties: Optional[Dict[str, Any]] = None,
                      reactions: Optional[Dict[str, Dict[str, Any]]] = None) -> None:
        ent = _Entity(name=name)
        # Normalize maps (support typed entries)
        ent.states = self._normalize_initial_map(ent, states, is_state=True, default_kind='fuzzy')
        ent.properties = self._normalize_initial_map(ent, properties, is_state=False, default_kind='fuzzy')
        if reactions:
            for act_name, spec in reactions.items():
                sens = float(spec.get('sensitivity', 1.0))
                resp = spec.get('response')
                ent.reactions[act_name] = _Reaction(sensitivity=_clamp(sens), response=resp)
        self.entities[name] = ent
        self._sync_entity_facts(ent)

    def set_state(self, name: str, key: str, value: float) -> float:
        ent = self.entities.setdefault(name, _Entity(name=name))
        # Ensure type info exists (default fuzzy)
        if key not in ent.state_types:
            ent.state_types[key] = self._default_typeinfo('fuzzy')
        val = self._apply_bounds(ent, True, key, value)
        ent.states[key] = val
        self._retractall('state', name, key, None)
        self._assert_fact('state', name, key, ent.states[key])
        # Enforce equations/constraints if defined
        if not self._in_enforce:
            self._enforce_constraints_for(ent)
        return ent.states[key]

    def get_state(self, name: str, key: str, default: float = 0.5) -> float:
        ent = self.entities.get(name)
        if not ent:
            return _clamp(default)
        return float(ent.states.get(key, _clamp(default)))

    def get_property(self, name: str, key: str, default: float = 0.5) -> float:
        ent = self.entities.get(name)
        if not ent:
            return _clamp(default)
        return float(ent.properties.get(key, _clamp(default)))


    def set_property(self, name: str, key: str, value: float) -> float:
        ent = self.entities.setdefault(name, _Entity(name=name))
        # Ensure type info exists (default fuzzy to preserve previous semantics)
        if key not in ent.property_types:
            ent.property_types[key] = self._default_typeinfo('fuzzy')
        val = self._apply_bounds(ent, False, key, value)
        ent.properties[key] = val
        self._retractall('property', name, key, None)
        self._assert_fact('property', name, key, ent.properties[key])
        # Enforce equations/constraints if defined
        if not self._in_enforce:
            self._enforce_constraints_for(ent)
        return ent.properties[key]

    def define_action(self, actor_name: str, action_name: str, *, power: float = 1.0,
                      effects: List[Dict[str, Any]] | List[_ActionEffect]) -> None:
        ent = self.entities.setdefault(actor_name, _Entity(name=actor_name))
        eff_list: List[_ActionEffect] = []
        for e in effects:
            if isinstance(e, _ActionEffect):
                eff_list.append(e)
            else:
                eff_list.append(_ActionEffect(on=e['on'], formula=e['formula'], condition=e.get('condition')))
        ent.actions[action_name] = {"power": _clamp(power), "effects": eff_list}
        # No facts asserted for actions for now (could add action/2 later)

    def apply_action(self, actor_name: str, action_name: str, target_name: str, *, action_value: float = 1.0, override_sensitivity: float | None = None) -> Dict[str, float]:
        actor = self.entities.setdefault(actor_name, _Entity(name=actor_name))
        target = self.entities.setdefault(target_name, _Entity(name=target_name))
        spec = actor.actions.get(action_name)
        if not spec:
            raise ValueError(f"Unknown action '{action_name}' for actor '{actor_name}'")

        power = float(spec.get('power', 1.0))
        results: Dict[str, float] = {}
        changes: List[Dict[str, float]] = []

        # Reaction sensitivity on receiver (allow override for single application)
        reaction = target.reactions.get(action_name, _Reaction())
        sensitivity = float(override_sensitivity if override_sensitivity is not None else reaction.sensitivity)

        for eff in spec['effects']:
            # Evaluate condition if present
            if eff.condition:
                cond_val = _SafeExpr.eval(eff.condition, {
                    'value': self.get_state(target_name, eff.on, 0.5),
                    'action_value': action_value,
                    'power': power,
                    'sensitivity': sensitivity,
                })
                if not cond_val:
                    continue

            # Determine whether this key is a state or a property on target
            if eff.on in target.states or eff.on not in target.properties:
                old = self.get_state(target_name, eff.on, 0.5)
                new_val = _SafeExpr.eval(eff.formula, {
                    'value': old,
                    'action_value': action_value,
                    'power': power,
                    'sensitivity': sensitivity,
                })
                new_val = self.set_state(target_name, eff.on, new_val)
            else:
                old = self.get_property(target_name, eff.on, 0.0)
                new_val = _SafeExpr.eval(eff.formula, {
                    'value': old,
                    'action_value': action_value,
                    'power': power,
                    'sensitivity': sensitivity,
                })
                new_val = self.set_property(target_name, eff.on, new_val)
            results[eff.on] = new_val
            changes.append({'key': eff.on, 'old': float(old), 'new': float(new_val)})
            # Record change as fact: changed(Target, Key, Old, New)
            self._assert_fact('changed', target_name, eff.on, float(old), float(new_val))

        # Apply simple reaction response if specified (STATE += expr or STATE -= expr)
        if reaction.response:
            key, op, expr = self._parse_response(reaction.response)
            base = self.get_state(target_name, key, 0.5)
            delta = _SafeExpr.eval(expr, {
                'action_value': action_value,
                'power': power,
                'sensitivity': sensitivity,
                'value': base,
            })
            if op == '+=':
                newv = self.set_state(target_name, key, base + delta)
                results[key] = newv
                changes.append({'key': key, 'old': float(base), 'new': float(newv)})
            elif op == '-=':
                newv = self.set_state(target_name, key, base - delta)
                results[key] = newv
                changes.append({'key': key, 'old': float(base), 'new': float(newv)})

        # Record event (logical fact + in-memory log)
        self._assert_fact('event', actor_name, action_name, target_name, float(action_value))
        # Build short textual summaries (EN/AR)
        try:
            _val = float(action_value)
            _pow = float(power)
            _sen = float(sensitivity)
        except Exception:
            _val, _pow, _sen = float(action_value), float(power), float(sensitivity)
        summary_en = f"{actor_name} -> {action_name} -> {target_name} (value={_val}, power={_pow}, sensitivity={_sen})"
        summary_ar = f"{actor_name} -> {action_name} -> {target_name} (قيمة={_val}، قدرة={_pow}، حساسية={_sen})"
        self.events.append({
            'actor': actor_name,
            'action': action_name,
            'target': target_name,
            'value': float(action_value),
            'power': float(power),
            'sensitivity': float(sensitivity),
            'changes': changes,
            'summary_en': summary_en,
            'summary_ar': summary_ar,
        })
        return results

    # --------- Action-centric API (perform) ---------
    def _normalize_participants(self, participants: Any) -> List[Tuple[str, float]]:
        out: List[Tuple[str, float]] = []
        if participants is None:
            return out

        def _add(name: str, deg: float):
            out.append((str(name), float(deg)))

        def _expand_group_spec(spec: str) -> Tuple[List[str], Optional[float]]:
            s = spec.strip()
            if s.startswith('group:'):
                rest = s[len('group:'):]
            elif s.startswith('مجموعة:'):
                rest = s[len('مجموعة:'):]
            else:
                rest = s
            deg = None
            # Prefer explicit ':' separator for degree if present
            idx = rest.rfind(':')
            name_part = rest
            if idx != -1:
                name_part = rest[:idx].strip()
                try:
                    deg = float(rest[idx+1:].strip())
                except Exception:
                    deg = None
            else:
                # Fall back to using the FIRST '.' as separator (so 'Team.0.5' -> name 'Team', deg '0.5')
                dot_idx = rest.find('.')
                if dot_idx != -1:
                    cand_name = rest[:dot_idx].strip()
                    cand_deg = rest[dot_idx+1:].strip()
                    try:
                        deg = float(cand_deg)
                        name_part = cand_name
                    except Exception:
                        # Not a degree; treat as name only
                        name_part = rest
                        deg = None
            members = self.groups.get(name_part, [])
            return (list(members), deg)

        def _parse_degree_suffix(s: str) -> Optional[float]:
            idx = s.rfind(':')
            if idx != -1:
                try:
                    return float(s[idx+1:].strip())
                except Exception:
                    return None
            dot_idx = s.find('.')
            if dot_idx != -1:
                try:
                    return float(s[dot_idx+1:].strip())
                except Exception:
                    return None
            return None

        pronouns_en = {'last', 'they', 'them', 'he', 'she', 'it'}
        pronouns_ar = {'هم', 'هو', 'هي', 'هما', 'هن'}

        # dict form
        if isinstance(participants, dict):
            for k, v in participants.items():
                if k in ('group', 'مجموعة'):
                    members, gdeg = _expand_group_spec(f'group:{v}')
                    for m in members:
                        _add(m, gdeg if gdeg is not None else 1.0)
                else:
                    try:
                        _add(k, float(v))
                    except Exception:
                        _add(k, 1.0)
            return out

        # list/tuple form
        if isinstance(participants, (list, tuple)):
            for item in participants:
                if isinstance(item, (list, tuple)) and len(item) == 2:
                    name, deg = item[0], item[1]
                    if isinstance(name, str) and (name.startswith('group:') or name.startswith('مجموعة:')):
                        members, _gdeg = _expand_group_spec(name)
                        for m in members:
                            _add(m, float(deg))
                    elif isinstance(name, str) and (name.lower() in pronouns_en or name in pronouns_ar):
                        for m in self._last_participants:
                            _add(m, float(deg))
                    else:
                        _add(name, deg)
                elif isinstance(item, str):
                    s = item.strip()
                    # group specs
                    if s.startswith('group:') or s.startswith('مجموعة:'):
                        members, gdeg = _expand_group_spec(s)
                        for m in members:
                            _add(m, gdeg if gdeg is not None else 1.0)
                        continue
                    # pronoun / last reference (supports ':deg' or first '.' suffix)
                    low = s.lower()
                    base = low.split(':', 1)[0]
                    if '.' in base:
                        base = base.split('.', 1)[0]
                    if (base in pronouns_en) or (base == 'last') or (base in pronouns_ar) or (s in pronouns_ar):
                        deg = _parse_degree_suffix(s)
                        for m in self._last_participants:
                            _add(m, deg if deg is not None else 1.0)
                        continue
                    # Default: "Name:1.0" or "Name.1.0"
                    sep_idx = s.rfind(':')
                    if sep_idx == -1:
                        # prefer first '.' that yields a valid float suffix
                        dot_idx = s.find('.')
                        if dot_idx != -1:
                            candidate = s[dot_idx+1:]
                            try:
                                deg_val = float(candidate)
                                _add(s[:dot_idx].strip(), deg_val)
                                continue
                            except Exception:
                                sep_idx = -1
                    if sep_idx != -1:
                        try:
                            _add(s[:sep_idx].strip(), float(s[sep_idx+1:]))
                        except Exception:
                            _add(s, 1.0)
                    else:
                        _add(s, 1.0)
        return out

    def _normalize_assignments(self, items: Any) -> List[Tuple[str, str, float]]:
        out: List[Tuple[str, str, float]] = []
        if not items:
            return out
        if isinstance(items, dict):
            # { entity: {key: value} }
            for ent, inner in items.items():
                if isinstance(inner, dict):
                    for k, v in inner.items():
                        out.append((str(ent), str(k), float(v)))
            return out
        if isinstance(items, (list, tuple)):
            for it in items:
                if isinstance(it, (list, tuple)) and len(it) == 3:
                    out.append((str(it[0]), str(it[1]), float(it[2])))
                elif isinstance(it, str):
                    s = it.strip()
                    if '=' in s and '.' in s:
                        # Entity.key=value
                        left, val = s.split('=', 1)
                        ent, key = left.split('.', 1)
                        out.append((ent.strip(), key.strip(), float(val)))
        return out

    def perform_action(self, action_name: str, participants: Any, *, states: Any = None, properties: Any = None, action_value: float = 1.0) -> Dict[str, Dict[str, float]]:
        """Action-first API:
        - participants: list/dict of (entity, responsiveness)
        - states/properties: pre-assignments before applying the action
        Semantics:
          * Identify actors as those who define the action; if none, use first participant as the sole actor.
          * If there are no non-actor participants, each actor acts on self (self-target) using its own responsiveness.
          * If there are non-actor participants, each actor applies the action to each non-actor target using that target's responsiveness.
        Returns dict: target_name -> {key: new_value}
        """
        ptcs = self._normalize_participants(participants)
        if not ptcs:
            return {}
        # Pre-assign states/properties
        for ent, key, val in self._normalize_assignments(states):
            self.set_state(ent, key, val)
        for ent, key, val in self._normalize_assignments(properties):
            self.set_property(ent, key, val)

        # Identify actors
        actors: List[str] = [n for (n, _deg) in ptcs if action_name in self.entities.setdefault(n, _Entity(name=n)).actions]
        if not actors:
            actors = [ptcs[0][0]]
        actor_set = set(actors)
        # Map degrees and ordered unique names
        deg_map = {n: d for (n, d) in ptcs}
        ordered_names: List[str] = []
        _seen = set()
        for n, _d in ptcs:
            if n not in _seen:
                _seen.add(n)
                ordered_names.append(n)
        # Targets follow the ordered unique names
        all_targets = [(n, deg_map.get(n, 1.0)) for n in ordered_names]

        all_results: Dict[str, Dict[str, float]] = {}
        if len(actor_set) == len(ordered_names):
            # Everyone is an actor -> each acts on self only
            for a in actors:
                res = self.apply_action(a, action_name, a, action_value=action_value, override_sensitivity=deg_map.get(a, 1.0))
                all_results[a] = res
        else:
            # There are non-actors -> each actor applies to all participants (including self)
            for a in actors:
                for (t, s) in all_targets:
                    res = self.apply_action(a, action_name, t, action_value=action_value, override_sensitivity=s)
                    # Merge
                    exist = all_results.setdefault(t, {})
                    exist.update(res)
        # Remember last participants (ordered unique) for pronoun-like references
        self._last_participants = ordered_names
        return all_results


    # --------- Groups API ---------
    def define_group(self, name: str, members: List[str]) -> None:
        self.groups[str(name)] = [str(m) for m in members]

    def add_to_group(self, name: str, members: List[str] | str) -> None:
        nm = str(name)
        existing = self.groups.setdefault(nm, [])
        if isinstance(members, str):
            members = [members]
        for m in members:
            sm = str(m)
            if sm not in existing:
                existing.append(sm)

    def get_group_members(self, name: str) -> List[str]:
        return list(self.groups.get(str(name), []))


    # --------- Equations / Constraints API ---------
    def _gather_vars(self, ent: _Entity) -> Dict[str, float]:
        vars_map: Dict[str, float] = {}
        # expose all states and properties as variables by their keys
        for k, v in ent.states.items():
            try:
                vars_map[str(k)] = float(v)
            except Exception:
                pass
        for k, v in ent.properties.items():
            try:
                vars_map[str(k)] = float(v)
            except Exception:
                pass
        return vars_map

    def _enforce_constraints_for(self, ent: _Entity) -> None:
        if not ent or not getattr(ent, 'constraints', None):
            return
        # Prevent recursive re-entry while we are enforcing
        if self._in_enforce:
            return
        self._in_enforce = True
        try:
            vars_map = self._gather_vars(ent)
            for c in list(ent.constraints):
                scope = c.get('scope', 'state')
                key = c.get('key')
                expr = c.get('expr')
                if not key or not isinstance(expr, str):
                    continue
                try:
                    val = float(_SafeExpr.eval(expr, vars_map))
                except Exception:
                    continue
                if scope == 'property':
                    self.set_property(ent.name, key, val)
                else:
                    self.set_state(ent.name, key, val)
                # refresh vars map for subsequent constraints
                vars_map[key] = val
        finally:
            self._in_enforce = False

    def add_equation(self, entity_name: str, *, scope: str, key: str, expr: str) -> None:
        ent = self.entities.setdefault(entity_name, _Entity(name=entity_name))
        scope_norm = 'property' if scope in ('property', 'خاصية') else 'state'
        ent.constraints.append({'scope': scope_norm, 'key': str(key), 'expr': str(expr)})
        # enforce once to synchronize
        self._enforce_constraints_for(ent)

    def add_state_equation(self, entity_name: str, key: str, expr: str) -> None:
        self.add_equation(entity_name, scope='state', key=key, expr=expr)

    def add_property_equation(self, entity_name: str, key: str, expr: str) -> None:
        self.add_equation(entity_name, scope='property', key=key, expr=expr)

    def define_complement(self, entity_name: str, *, scope: str, base_key: str, complement_key: str, total: float = 1.0) -> None:
        # complement_key = total - base_key
        expr = f"{float(total)} - {base_key}"
        self.add_equation(entity_name, scope=scope, key=complement_key, expr=expr)

    def define_opposites(self, entity_name: str, *, scope: str, key_a: str, key_b: str, total: float = 1.0) -> None:
        # Define symmetric complements: A = total - B and B = total - A
        total_f = float(total)
        self.add_equation(entity_name, scope=scope, key=str(key_a), expr=f"{total_f} - {key_b}")
        self.add_equation(entity_name, scope=scope, key=str(key_b), expr=f"{total_f} - {key_a}")


    @staticmethod
    def _parse_response(s: str) -> (str, str, str):
        # Very small parser for forms: "NAME += EXPR" or "NAME -= EXPR"
        if '+=' in s:
            parts = s.split('+=', 1)
            return parts[0].strip(), '+=', parts[1].strip()
        if '-=' in s:
            parts = s.split('-=', 1)
            return parts[0].strip(), '-=', parts[1].strip()
        # Fallback: treat as absolute assignment NAME = EXPR
        if '=' in s:
            parts = s.split('=', 1)
            return parts[0].strip(), '+=', parts[1].strip()  # emulate set by += expr-base in apply
        raise ValueError("Unsupported reaction response format")

