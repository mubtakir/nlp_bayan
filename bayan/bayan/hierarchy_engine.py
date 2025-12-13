"""
Hierarchy Engine (Tarateeb & Shajara)
Handles generation of logical facts for sequences and tree structures.
"""

from typing import List, Dict, Any, Optional, Callable, Set
from .logical_engine import LogicalEngine, Fact, Rule, Predicate, Term, ModalOperator, TemporalOperator

class HierarchyEngine:
    def __init__(self, logic_engine: LogicalEngine):
        self.logic_engine = logic_engine
        self.stored_sequences: Dict[str, List[str]] = {}
        self.stored_cycles: Dict[str, List[str]] = {}
        self.stored_hierarchies: Dict[str, Any] = {} # {root: str, structure: dict}
        
        self.register_base_rules()

    def define_sequence(self, name: str, items: List[str]):
        """
        Define a linear sequence (Tarateeb/Sequence).
        """
        if not items:
            return
        self.stored_sequences[name] = items

        for index, item in enumerate(items):
            # member(SequenceName, Item)
            self.logic_engine.add_fact(Fact(Predicate("member", [Term(name), Term(item)])))

            # order(SequenceName, Item, Index) - 1-based index
            self.logic_engine.add_fact(Fact(Predicate("order", [Term(name), Term(item), Term(index + 1)])))

            # first/last
            if index == 0:
                self.logic_engine.add_fact(Fact(Predicate("first", [Term(name), Term(item)])))
            if index == len(items) - 1:
                self.logic_engine.add_fact(Fact(Predicate("last", [Term(name), Term(item)])))

            # next/prev
            if index < len(items) - 1:
                next_item = items[index + 1]
                self.logic_engine.add_fact(Fact(Predicate("next", [Term(name), Term(item), Term(next_item)])))
                self.logic_engine.add_fact(Fact(Predicate("prev", [Term(name), Term(next_item), Term(item)])))

    def define_cycle(self, name: str, items: List[str]):
        """
        Define a cyclic sequence (Dora/Cycle).
        """
        if not items:
            return
        self.stored_cycles[name] = items

        # Reuse sequence logic for linear parts
        self.define_sequence(name, items)

        # Add Cycle Close: Last -> First
        first = items[0]
        last = items[-1]

        self.logic_engine.add_fact(Fact(Predicate("next", [Term(name), Term(last), Term(first)])))
        self.logic_engine.add_fact(Fact(Predicate("prev", [Term(name), Term(first), Term(last)])))

        # Mark as cycle
        self.logic_engine.add_fact(Fact(Predicate("is_cycle", [Term(name)])))

        # --- Causal Integration ---
        # In a cycle, A -> B implies A causes/precedes B.
        cause_pred = "cause"
        for i, item in enumerate(items):
            if i < len(items) - 1:
                next_item = items[i + 1]
            else:
                next_item = items[0] # Wrap around

            # cause(Item, NextItem) [p=0.9, Next]
            self.logic_engine.add_fact(Fact(
                Predicate(cause_pred, [Term(item), Term(next_item)]),
                probability=0.9,
                temporal_op=TemporalOperator.NEXT
            ))

    def define_hierarchy(self, name: str, root: str, structure: Dict[str, List[str]]):
        """
        Define a tree hierarchy (Shajara/Hierarchy).
        """
        self.stored_hierarchies[name] = {'root': root, 'structure': structure}

        # Tag the root
        self.logic_engine.add_fact(Fact(Predicate("root", [Term(name), Term(root)])))

        # Process structure
        for parent, children in structure.items():
            for child in children:
                # parent(TreeName, Parent, Child)
                self.logic_engine.add_fact(Fact(Predicate("parent", [Term(name), Term(parent), Term(child)])))

                # child(TreeName, Child, Parent)
                self.logic_engine.add_fact(Fact(Predicate("child", [Term(name), Term(child), Term(parent)])))

    def register_base_rules(self):
        # 1. Ancestor Rule (Recursive)
        # ancestor(?tree, ?a, ?b) :- parent(?tree, ?a, ?b).
        r1 = Rule(
            Fact(Predicate("ancestor", [Term("?TREE", True), Term("?A", True), Term("?B", True)])).predicate,
            [Fact(Predicate("parent", [Term("?TREE", True), Term("?A", True), Term("?B", True)])).predicate]
        )
        self.logic_engine.add_rule(r1)

        # ancestor(?tree, ?a, ?c) :- parent(?tree, ?a, ?b), ancestor(?tree, ?b, ?c).
        r2 = Rule(
            Fact(Predicate("ancestor", [Term("?TREE", True), Term("?A", True), Term("?C", True)])).predicate,
            [
                Fact(Predicate("parent", [Term("?TREE", True), Term("?A", True), Term("?B", True)])).predicate,
                Fact(Predicate("ancestor", [Term("?TREE", True), Term("?B", True), Term("?C", True)])).predicate
            ]
        )
        self.logic_engine.add_rule(r2)

        # 2. Property Inheritance Rules
        # rule: property(?tree, ?child, ?k, ?v) :- ancestor(?tree, ?parent, ?child), property(?tree, ?parent, ?k, ?v).
        r_inherit = Rule(
            Fact(Predicate("property", [Term("?TREE", True), Term("?CHILD", True), Term("?K", True), Term("?V", True)])).predicate,
            [
                Fact(Predicate("ancestor", [Term("?TREE", True), Term("?PARENT", True), Term("?CHILD", True)])).predicate,
                Fact(Predicate("property", [Term("?TREE", True), Term("?PARENT", True), Term("?K", True), Term("?V", True)])).predicate
            ]
        )
        self.logic_engine.add_rule(r_inherit)

    def validate_sequence(self, name: str, type_resolver: Callable[[str], List[str]]) -> List[str]:
        """
        Validate a sequence or cycle for semantic consistency.
        """
        items = self.stored_sequences.get(name) or self.stored_cycles.get(name)
        if not items:
            return [f"Structure '{name}' not found."]

        warnings = []
        types_map = {}

        # 1. Resolve types
        for item in items:
            types_map[item] = type_resolver(item)

        # 2. Check consistency (Common type check)
        first_item = items[0]
        first_types = types_map.get(first_item, [])

        if first_types:
            common_types = set(first_types)
            for i in range(1, len(items)):
                item = items[i]
                item_types = types_map.get(item, [])
                
                # Intersect
                common_types = common_types.intersection(set(item_types))

            if not common_types:
                warnings.append(f"⚠️ Semantic Mismatch: Items in '{name}' do not share a common confirmed type. ({', '.join(items)})")
                for item in items:
                    t = types_map.get(item)
                    if not t:
                        warnings.append(f"   - '{item}' has no known type.")
                    else:
                        warnings.append(f"   - '{item}' is a [{', '.join(t)}]")
        else:
             warnings.append(f"ℹ️ Validation Skipped: First item '{first_item}' has no defined type.")

        return warnings
