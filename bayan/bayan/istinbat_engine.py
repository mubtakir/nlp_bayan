from typing import List, Dict, Any, Optional
from .linguistic_equation import KnowledgeBase, LinguisticEquation, Role
from .advanced_arabic_parser import AdvancedArabicParser
from .entity_engine import EntityEngine
from .dynamic_builder import DynamicCircuitBuilder, Atom
from .logical_engine import LogicalEngine, Fact, Predicate, Term, Rule, ModalOperator, TemporalOperator
from .smart_knowledge_base import SmartKnowledgeBase
from .dialect_adapter import DialectAdapter, Dialect
from .balagha_engine import BalaghaEngine
from .hierarchy_engine import HierarchyEngine
from .neural.neural_engine import NeuralEngine
from .neural.tensor_bridge import TensorBridge
import copy

class DeductionResult:
    """Holds the result of a deep inference process."""
    def __init__(self, equation: LinguisticEquation, consequences: List[Any], circuit: Dict[str, Any],
                 original_text: str = None, dialect: str = None, converted_text: str = None,
                 logical_deductions: List[Any] = None, balagha_score: Any = None):
        self.equation = equation
        self.consequences = consequences
        self.circuit = circuit
        # معلومات اللهجة
        self.original_text = original_text
        self.dialect = dialect
        self.converted_text = converted_text
        self.logical_deductions = logical_deductions or []
        self.balagha_score = balagha_score

    def __repr__(self):
        dialect_info = f", Dialect={self.dialect}" if self.dialect else ""
        balagha_info = f", Eloquence={self.balagha_score.total:.2f}" if self.balagha_score else ""
        return f"DeductionResult(Event={self.equation.event}, Consequences={len(self.consequences)}{dialect_info}{balagha_info})"

class IstinbatEngine:
    """
    The Unified Brain (محرك الاستنباط).
    Orchestrates the flow from Text -> Equation -> Causal Inference -> Entity State -> Logical Thought.
    Now with Neuro-Symbolic Integration! 🧠✨
    
    الميزات الجديدة:
    - دعم العوالم المتوازية (Parallel Universes)
    - المنطق الموجه والزمني (Modal & Temporal Logic)
    - البلاغة (Balagha)
    - التراتيب (Hierarchy)
    - المحرك العصبي (Neural Engine)
    """
    def __init__(self, enable_dialect_support: bool = True):
        # World Management
        self.worlds: Dict[str, LogicalEngine] = {}
        self.current_world_name = "Reality"
        
        # Initialize Base Reality
        self.logical_engine = LogicalEngine()
        self.worlds[self.current_world_name] = self.logical_engine
        
        self.entity_engine = EntityEngine(self.logical_engine)
        self.kb = SmartKnowledgeBase()
        self.parser = AdvancedArabicParser(self.kb)
        self.circuit_builder = DynamicCircuitBuilder()

        # Intelligence Engines
        self.balagha_engine = BalaghaEngine()
        self.hierarchy_engine = HierarchyEngine(self.logical_engine)
        
        # Neural Integration
        self.neural_engine = NeuralEngine()
        self.tensor_bridge = TensorBridge(self.neural_engine)

        # دعم اللهجات
        self.enable_dialect_support = enable_dialect_support
        self.dialect_adapter = DialectAdapter() if enable_dialect_support else None
        
        # Dynamic Context (Maqam)
        self.active_context: List[str] = []

    def set_context(self, tags: List[str]):
        """Set the current semantic context (Maqam)."""
        self.active_context = tags

    # --- Parallel Universes API ---

    def create_world(self, name: str, from_world: str = None) -> bool:
        """Create a new possible world (clone of an existing one)."""
        if from_world is None:
            from_world = self.current_world_name
            
        parent_world = self.worlds.get(from_world)
        if not parent_world:
            return False
            
        # Deep copy the logical engine state
        # Note: Shallow copy might suffice if Fact lists are copied, but deep copy is checks
        self.worlds[name] = copy.deepcopy(parent_world)
        return True

    def switch_world(self, name: str) -> bool:
        """Switch the active logical reference frame."""
        world = self.worlds.get(name)
        if not world:
            return False
            
        self.current_world_name = name
        self.logical_engine = world
        # Also update hierarchy engine to point to new world
        self.hierarchy_engine.logic_engine = world 
        
        return True

    def compare_worlds(self, world1_name: str, world2_name: str) -> List[str]:
        """Compare two worlds and return differences."""
        w1 = self.worlds.get(world1_name)
        w2 = self.worlds.get(world2_name)
        if not w1 or not w2:
            return ["Error: World not found"]

        diffs = []
        
        # Get all facts as strings for comparison
        w1_facts = {str(item.predicate): item for sublist in w1.knowledge_base.values() for item in sublist if isinstance(item, Fact)}
        w2_facts = {str(item.predicate): item for sublist in w2.knowledge_base.values() for item in sublist if isinstance(item, Fact)}

        # Check for removed/changed facts
        for pred_str in w1_facts:
            if pred_str not in w2_facts:
                diffs.append(f"[- REMOVED] {pred_str}")
        
        # Check for added facts
        for pred_str in w2_facts:
            if pred_str not in w1_facts:
                diffs.append(f"[+ ADDED] {pred_str}")

        return diffs

    # --- Modal Logic API ---

    def must(self, predicate: str, args: List[str]):
        """Assert Necessity (يجب)."""
        terms = [Term(a, False) for a in args]
        fact = Fact(Predicate(predicate, terms), modal_op=ModalOperator.NECESSITY)
        self.logical_engine.add_fact(fact)

    def can(self, predicate: str, args: List[str]):
        """Assert Possibility (يمكن)."""
        terms = [Term(a, False) for a in args]
        fact = Fact(Predicate(predicate, terms), modal_op=ModalOperator.POSSIBILITY)
        self.logical_engine.add_fact(fact)

    def is_necessary(self, predicate: str, args: List[str]) -> bool:
        """Check if P is Necessary in the current world."""
        terms = [Term(a, False) for a in args]
        goal = Predicate(predicate, terms)
        
        # Query for matching fact with NECESSITY operator
        # This requires more complex query logic in LogicalEngine to filter by op
        # For prototype, we iterate:
        facts = self.logical_engine.knowledge_base.get(predicate, [])
        for item in facts:
            if isinstance(item, Fact) and item.modal_op == ModalOperator.NECESSITY:
                if item.predicate.args == terms:
                    return True
        return False

    def is_possible(self, predicate: str, args: List[str]) -> bool:
        """Check if P is Possible."""
        terms = [Term(a, False) for a in args]
        
        # 1. Explicit Possibility
        facts = self.logical_engine.knowledge_base.get(predicate, [])
        for item in facts:
            if isinstance(item, Fact) and item.modal_op == ModalOperator.POSSIBILITY:
                 if item.predicate.args == terms:
                    return True
        
        # 2. Necessity implies Possibility
        if self.is_necessary(predicate, args):
            return True
            
        # 3. Actuality implies Possibility
        for item in facts:
            if isinstance(item, Fact) and item.modal_op == ModalOperator.NONE:
                 if item.predicate.args == terms:
                    return True
        
        return False

    # --- Temporal Logic API ---

    def always(self, predicate: str, args: List[str]):
        """Assert Always (دائماً)."""
        terms = [Term(a, False) for a in args]
        fact = Fact(Predicate(predicate, terms), temporal_op=TemporalOperator.ALWAYS)
        self.logical_engine.add_fact(fact)

    def eventually(self, predicate: str, args: List[str]):
        """Assert Eventually (يوماً ما)."""
        terms = [Term(a, False) for a in args]
        fact = Fact(Predicate(predicate, terms), temporal_op=TemporalOperator.EVENTUALLY)
        self.logical_engine.add_fact(fact)


    # --- Processing ---

    # --- Neural API ---
        
    def neural_search(self, query: str, top_k: int = 3):
        """
        Search the active world's knowledge base using semantic similarity.
        This allows finding facts that mean the same thing but use different words.
        """
        # Collect all facts from the active logical engine
        all_facts = []
        for facts_list in self.logical_engine.knowledge_base.values():
            for item in facts_list:
                # IMPORTANT: Filter only Facts, ignore Rules
                if isinstance(item, Fact):
                    all_facts.append(item)
            
        return self.tensor_bridge.find_similar_facts(query, all_facts, top_k)

    def process(self, text: str, dialect: Optional[str] = None) -> Optional[DeductionResult]:
        """
        Main entry point: Text -> Deep Deduction.
        """
        original_text = text
        detected_dialect = None
        converted_text = None

        # 0. Dialect Support
        if self.enable_dialect_support and self.dialect_adapter:
            conversion = self.dialect_adapter.convert_to_standard(text, dialect)
            if conversion.dialect != Dialect.STANDARD and conversion.changes:
                detected_dialect = conversion.dialect.value
                converted_text = conversion.converted
                text = converted_text
        
        # Eloquence Check
        balagha_score = self.balagha_engine.evaluate(text, self.active_context)

        # 1. Parse Text
        equation = self._parse_equation(text)
        if not equation:
            return None

        # 2. Hydrate Entities
        self._hydrate_entities(equation)

        # 3. Infer Consequences
        consequences = self._infer_consequences(equation)

        # 4. Synthesize Thought
        circuit = self._synthesize_thought(equation, consequences)
        
        # 5. Logical Deductions (Sample Query)
        logical_deductions = []
        if equation.entities:
            # Try to find if the subject has any properties in the logic engine
            subject = next((k for k, v in equation.entities.items() if v == Role.SUBJECT), None)
            if subject:
                # Query something simple just to populate result
                pass

        return DeductionResult(
            equation, consequences, circuit,
            original_text=original_text,
            dialect=detected_dialect,
            converted_text=converted_text,
            logical_deductions=logical_deductions,
            balagha_score=balagha_score
        )

    def _parse_equation(self, text: str) -> Optional[LinguisticEquation]:
        return self.parser.parse(text)

    def _hydrate_entities(self, equation: LinguisticEquation):
        for name, role in equation.entities.items():
            self.entity_engine.create_entity(name)

    def _infer_consequences(self, equation: LinguisticEquation) -> List[Any]:
        return equation.results

    def _synthesize_thought(self, equation: LinguisticEquation, consequences: List[Any]) -> Dict[str, Any]:
        atoms = []
        for name, role in equation.entities.items():
            atoms.append(Atom("Entity", name, {"role": role.value}))
        atoms.append(Atom("Action", equation.event, {"type": equation.event_type.value}))
        
        if equation.location:
             atoms.append(Atom("Context", equation.location, {"type": "Location"}))
        if equation.time:
             atoms.append(Atom("Context", equation.time, {"type": "Time"}))

        for result in consequences:
            for key, value in result.state_changes.items():
                atoms.append(Atom("StateChange", f"{result.entity_name}.{key}={value}"))

        return self.circuit_builder.assemble(atoms)

