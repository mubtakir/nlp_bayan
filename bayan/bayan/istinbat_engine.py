from typing import List, Dict, Any, Optional
from .linguistic_equation import LinguisticEquationParser, KnowledgeBase, LinguisticEquation, Role
from .entity_engine import EntityEngine
from .dynamic_builder import DynamicCircuitBuilder, Atom
from .logical_engine import LogicalEngine

class DeductionResult:
    """Holds the result of a deep inference process."""
    def __init__(self, equation: LinguisticEquation, consequences: List[Any], circuit: Dict[str, Any]):
        self.equation = equation
        self.consequences = consequences
        self.circuit = circuit

    def __repr__(self):
        return f"DeductionResult(Event={self.equation.event}, Consequences={len(self.consequences)})"

class IstinbatEngine:
    """
    The Unified Brain (محرك الاستنباط).
    Orchestrates the flow from Text -> Equation -> Causal Inference -> Entity State -> Logical Thought.
    """
    def __init__(self):
        self.logical_engine = LogicalEngine()
        self.entity_engine = EntityEngine(self.logical_engine)
        self.kb = KnowledgeBase()
        self.parser = LinguisticEquationParser(self.kb)
        self.circuit_builder = DynamicCircuitBuilder()

    def process(self, text: str) -> Optional[DeductionResult]:
        """
        Main entry point: Text -> Deep Deduction.
        """
        # 1. Parse Text into Linguistic Equation
        equation = self._parse_equation(text)
        if not equation:
            return None

        # 2. Hydrate Entities (Ensure they exist in EntityEngine)
        self._hydrate_entities(equation)

        # 3. Infer Consequences (Causal Logic)
        consequences = self._infer_consequences(equation)

        # 4. Synthesize Final Thought (Dynamic Circuit)
        circuit = self._synthesize_thought(equation, consequences)

        return DeductionResult(equation, consequences, circuit)

    def _parse_equation(self, text: str) -> Optional[LinguisticEquation]:
        return self.parser.parse(text)

    def _hydrate_entities(self, equation: LinguisticEquation):
        """
        Ensures entities mentioned in the equation exist in the EntityEngine.
        """
        for name, role in equation.entities.items():
            # Create entity if not exists (idempotent)
            # We could infer initial state from the role (e.g., Subject might be Active)
            self.entity_engine.create_entity(name)

    def _infer_consequences(self, equation: LinguisticEquation) -> List[Any]:
        """
        Uses the KnowledgeBase to predict results and applies them to the EntityEngine.
        """
        # The equation already contains results inferred during parsing by the KB
        # But we can also apply them to the EntityEngine here to update the "World State"
        
        applied_changes = []
        
        subject = equation._get_entity_by_role(Role.SUBJECT)
        obj = equation._get_entity_by_role(Role.OBJECT)
        
        # Apply the event to the EntityEngine to get concrete state changes
        if subject and equation.event:
            # If there is an object, it's a directed action
            if obj:
                # Define action on the fly if needed (simplified for demo)
                # In a real system, we'd look up the action definition
                self.entity_engine.define_action(subject, equation.event, effects=[]) 
                
                # We assume the KB results are the "effects"
                # For this prototype, we just log that we *would* apply them
                pass
            else:
                # Intransitive action
                pass
                
        return equation.results

    def _synthesize_thought(self, equation: LinguisticEquation, consequences: List[Any]) -> Dict[str, Any]:
        """
        Converts the equation and its consequences into a Conceptual Circuit.
        """
        atoms = []
        
        # Convert Entities
        for name, role in equation.entities.items():
            atoms.append(Atom("Entity", name, {"role": role.value}))
            
        # Convert Event
        atoms.append(Atom("Action", equation.event, {"type": equation.event_type.value}))
        
        # Convert Context
        if equation.location:
            atoms.append(Atom("Context", equation.location, {"type": "Location"}))
        if equation.time:
            atoms.append(Atom("Context", equation.time, {"type": "Time"}))
            
        # Convert Consequences into Atoms (e.g., StateChange atoms)
        for result in consequences:
            for key, value in result.state_changes.items():
                atoms.append(Atom("StateChange", f"{result.entity_name}.{key}={value}"))

        # Build Circuit
        return self.circuit_builder.assemble(atoms)
