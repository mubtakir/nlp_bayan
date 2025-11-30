"""
Causal and Semantic Networks for Bayan
======================================

Manages the relationships between concepts, enabling causal reasoning
and semantic associations.

Key Features:
- Causal Chains: A causes B causes C
- Semantic Relations: Synonyms, Opposites, Is-A
- Graph Traversal: Finding paths and related concepts
"""

from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, field
from enum import Enum
import collections

class RelationType(Enum):
    CAUSES = "causes"       # يسبب
    REQUIRES = "requires"   # يتطلب
    ENABLES = "enables"     # يمكن
    LEADS_TO = "leads_to"   # يؤدي إلى
    OPPOSITE = "opposite"   # ضد
    SIMILAR = "similar"     # مشابه
    IS_A = "is_a"           # نوع من
    PART_OF = "part_of"     # جزء من

@dataclass
class Relation:
    source: str
    target: str
    type: RelationType
    weight: float = 1.0
    metadata: Dict[str, Any] = field(default_factory=dict)

class CausalSemanticNetwork:
    """
    A graph-based network for storing and querying causal and semantic knowledge.
    """
    def __init__(self):
        self.nodes: Set[str] = set()
        self.edges: Dict[str, List[Relation]] = collections.defaultdict(list)
        self.reverse_edges: Dict[str, List[Relation]] = collections.defaultdict(list)

    def add_node(self, concept: str):
        """Add a concept node to the network."""
        self.nodes.add(concept)

    def add_relation(self, source: str, target: str, rel_type: RelationType, weight: float = 1.0, **metadata):
        """Add a relationship between two concepts."""
        self.add_node(source)
        self.add_node(target)
        
        relation = Relation(source, target, rel_type, weight, metadata)
        self.edges[source].append(relation)
        
        # For undirected relations (like SIMILAR, OPPOSITE), add reverse edge automatically
        # For directed, we store reverse specifically for backward traversal
        if rel_type in [RelationType.SIMILAR, RelationType.OPPOSITE]:
            rev_relation = Relation(target, source, rel_type, weight, metadata)
            self.edges[target].append(rev_relation)
        
        self.reverse_edges[target].append(relation)

    def get_relations(self, concept: str, rel_type: Optional[RelationType] = None) -> List[Relation]:
        """Get outgoing relations from a concept."""
        if rel_type:
            return [r for r in self.edges[concept] if r.type == rel_type]
        return self.edges[concept]

    def find_causal_chain(self, start: str, end: str, max_depth: int = 5) -> List[List[str]]:
        """
        Find all causal paths from start to end.
        Uses BFS to find paths.
        """
        paths = []
        queue = [(start, [start])]
        
        while queue:
            current, path = queue.pop(0)
            
            if len(path) > max_depth:
                continue
                
            if current == end:
                paths.append(path)
                continue
            
            # Explore neighbors linked by causal relations
            for rel in self.edges[current]:
                if rel.type in [RelationType.CAUSES, RelationType.LEADS_TO, RelationType.ENABLES]:
                    if rel.target not in path: # Avoid cycles
                        queue.append((rel.target, path + [rel.target]))
                        
        return paths

    def infer_consequences(self, event: str, depth: int = 2) -> List[Tuple[str, float]]:
        """
        Infer what happens after an event (forward chaining).
        Returns list of (consequence, confidence).
        """
        results = []
        queue = [(event, 1.0, 0)] # (current, confidence, current_depth)
        visited = set()

        while queue:
            curr, conf, d = queue.pop(0)
            if d >= depth:
                continue
            
            visited.add(curr)
            
            for rel in self.edges[curr]:
                if rel.type in [RelationType.CAUSES, RelationType.LEADS_TO]:
                    new_conf = conf * rel.weight
                    if rel.target not in visited:
                        results.append((rel.target, new_conf))
                        queue.append((rel.target, new_conf, d + 1))
                        
        return sorted(results, key=lambda x: x[1], reverse=True)

    def infer_causes(self, result: str, depth: int = 2) -> List[Tuple[str, float]]:
        """
        Infer what caused a result (backward chaining).
        """
        results = []
        queue = [(result, 1.0, 0)]
        visited = set()

        while queue:
            curr, conf, d = queue.pop(0)
            if d >= depth:
                continue
            
            visited.add(curr)
            
            # Look at incoming edges
            for rel in self.reverse_edges[curr]:
                if rel.type in [RelationType.CAUSES, RelationType.LEADS_TO]:
                    new_conf = conf * rel.weight
                    if rel.source not in visited:
                        results.append((rel.source, new_conf))
                        queue.append((rel.source, new_conf, d + 1))
                        
        return sorted(results, key=lambda x: x[1], reverse=True)

    def suggest_scenario_completion(self, start: str) -> Dict[str, List[str]]:
        """
        Suggest possible Events and Results given a Start concept.
        """
        suggestions = {"events": [], "results": []}
        
        # Find direct consequences (Events)
        events = self.infer_consequences(start, depth=1)
        for evt, _ in events:
            suggestions["events"].append(evt)
            
            # Find consequences of events (Results)
            results = self.infer_consequences(evt, depth=1)
            for res, _ in results:
                suggestions["results"].append(res)
                
        return suggestions
