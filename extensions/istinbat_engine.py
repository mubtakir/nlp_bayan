from typing import List, Dict, Any, Optional
from .linguistic_equation import KnowledgeBase, LinguisticEquation, Role
from .advanced_arabic_parser import AdvancedArabicParser
from .entity_engine import EntityEngine
from .dynamic_builder import DynamicCircuitBuilder, Atom
from .logical_engine import LogicalEngine
from .smart_knowledge_base import SmartKnowledgeBase
from .dialect_adapter import DialectAdapter, Dialect

class DeductionResult:
    """Holds the result of a deep inference process."""
    def __init__(self, equation: LinguisticEquation, consequences: List[Any], circuit: Dict[str, Any],
                 original_text: str = None, dialect: str = None, converted_text: str = None):
        self.equation = equation
        self.consequences = consequences
        self.circuit = circuit
        # معلومات اللهجة
        self.original_text = original_text
        self.dialect = dialect
        self.converted_text = converted_text

    def __repr__(self):
        dialect_info = f", Dialect={self.dialect}" if self.dialect else ""
        return f"DeductionResult(Event={self.equation.event}, Consequences={len(self.consequences)}{dialect_info})"

class IstinbatEngine:
    """
    The Unified Brain (محرك الاستنباط).
    Orchestrates the flow from Text -> Equation -> Causal Inference -> Entity State -> Logical Thought.

    الميزات الجديدة:
    - دعم اللهجات العربية (مصرية، خليجية، شامية، مغربية)
    - تحويل تلقائي من اللهجة إلى الفصحى
    """
    def __init__(self, enable_dialect_support: bool = True):
        self.logical_engine = LogicalEngine()
        self.entity_engine = EntityEngine(self.logical_engine)
        self.kb = SmartKnowledgeBase()
        self.parser = AdvancedArabicParser(self.kb)
        self.circuit_builder = DynamicCircuitBuilder()

        # دعم اللهجات
        self.enable_dialect_support = enable_dialect_support
        self.dialect_adapter = DialectAdapter() if enable_dialect_support else None

    def process(self, text: str, dialect: Optional[str] = None) -> Optional[DeductionResult]:
        """
        Main entry point: Text -> Deep Deduction.

        Args:
            text: النص المراد تحليله (يمكن أن يكون بأي لهجة)
            dialect: اللهجة (اختياري - None = اكتشاف تلقائي)

        Returns:
            نتيجة الاستنباط أو None
        """
        original_text = text
        detected_dialect = None
        converted_text = None

        # 0. تحويل من اللهجة إلى الفصحى (إذا مفعّل)
        if self.enable_dialect_support and self.dialect_adapter:
            conversion = self.dialect_adapter.convert_to_standard(text, dialect)
            if conversion.dialect != Dialect.STANDARD and conversion.changes:
                detected_dialect = conversion.dialect.value
                converted_text = conversion.converted
                text = converted_text
                print(f"   🌍 اللهجة المكتشفة: {detected_dialect}")
                print(f"   📝 النص الأصلي: {original_text}")
                print(f"   ✨ النص المحول: {converted_text}")

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

        return DeductionResult(
            equation, consequences, circuit,
            original_text=original_text,
            dialect=detected_dialect,
            converted_text=converted_text
        )

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
