from typing import List, Dict, Any, Optional

class Atom:
    """Represents a semantic atom (Entity, Action, Context, etc.)"""
    def __init__(self, kind: str, value: str, properties: Dict[str, Any] = None):
        self.kind = kind  # "Entity", "Action", "Context"
        self.value = value
        self.properties = properties or {}

    def __repr__(self):
        return f"Atom({self.kind}, {self.value})"

class DynamicCircuitBuilder:
    """
    Assembles conceptual circuits dynamically from a bag of atoms.
    Does not rely on pre-defined blueprints.
    """
    def __init__(self):
        pass

    def assemble(self, atoms: List[Atom]) -> Dict[str, Any]:
        """
        Main entry point. Takes a list of atoms and tries to build a valid circuit.
        """
        entities = [a for a in atoms if a.kind == "Entity"]
        actions = [a for a in atoms if a.kind == "Action"]
        contexts = [a for a in atoms if a.kind == "Context"]
        
        # Heuristic: If we have at least 1 Entity and 1 Action, we can build an Event.
        if entities and actions:
            return self._build_event_circuit(entities, actions, contexts)
        
        # Fallback: Just return a collection of entities
        return self._build_entity_collection_circuit(entities)

    def _build_event_circuit(self, entities: List[Atom], actions: List[Atom], contexts: List[Atom]) -> Dict[str, Any]:
        """
        Builds a generic event circuit.
        """
        # Assign roles heuristically
        actor = entities[0]
        target = entities[1] if len(entities) > 1 else None
        action = actions[0]
        context = contexts[0] if contexts else Atom("Context", "GenericContext")
        
        # Construct the trace
        trace_entities = [{"id": e.value, "kind": "dynamic_entity"} for e in entities]
        
        event_id = f"DynamicEvent_{action.value}"
        event = {
            "id": event_id,
            "action": action.value,
            "actors": [actor.value],
            "targets": [target.value] if target else [],
            "context": context.value,
            "probability": 1.0
        }
        
        trace = {
            "entities": trace_entities,
            "events": [event],
            "meta": {
                "source": "dynamic_circuit_builder",
                "mode": "generative",
                "confidence": 0.8  # Lower confidence than blueprints
            }
        }
        
        # Construct generic roles
        roles = {
            "DynamicEventPattern": {
                "Actor": actor.value,
                "Action": action.value,
                "Target": target.value if target else "None",
                "Context": context.value
            }
        }
        
        return {"trace": trace, "roles": roles}

    def _build_entity_collection_circuit(self, entities: List[Atom]) -> Dict[str, Any]:
        """
        Builds a simple circuit just listing entities (e.g. "Cars and trucks").
        """
        trace_entities = [{"id": e.value, "kind": "dynamic_entity"} for e in entities]
        
        trace = {
            "entities": trace_entities,
            "meta": {
                "source": "dynamic_circuit_builder",
                "mode": "descriptive",
                "confidence": 0.9
            }
        }
        
        roles = {
            "EntityCollectionPattern": {
                "Entities": [e.value for e in entities]
            }
        }
        
        return {"trace": trace, "roles": roles}
