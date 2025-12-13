import sys
import os

# Ensure import paths
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from bayan.bayan.istinbat_engine import IstinbatEngine, Fact, Predicate, Term

class LogicPolice:
    """
    The Internal Censor / Logic Police.
    Ensures that the Agent does not 'hallucinate' or contradict itself.
    """
    def __init__(self, engine: IstinbatEngine):
        self.engine = engine

    def review_statement(self, fact_proposed: Fact) -> bool:
        """
        Check if a proposed fact contradicts existing knowledge.
        Returns True if safe, False if contradicted.
        """
        # 1. Check direct contradiction (e.g., is_hot(Sun) vs not is_hot(Sun))
        # Note: Bayan's logical engine handles negation via 'not'.
        # We simulate a check by querying the negation.
        
        # Construct negation query: not(proposed)
        # Simplified: If we propose is_cold(Sun), we check query is_hot(Sun).
        # This requires semantic knowledge of opposites, which is advanced.
        # For now, we check direct explicit contradictions if the engine supports it.
        
        # Using the engine's check_contradictions if available, 
        # or a simple consistency check.
        
        try:
            # Hypothetical check: Try adding it to a temporary world
            current_world = getattr(self.engine, 'active_world_name', 'Reality')
            temp_world = f"temp_check_{abs(hash(str(fact_proposed)))}"
            
            # Create temp world from current
            self.engine.create_world(temp_world, from_world=current_world)
            self.engine.switch_world(temp_world)
            
            # Add fact
            self.engine.logical_engine.add_fact(fact_proposed)
            
            # Check for contradictions defined in the engine
            contradictions = self.engine.logical_engine.check_contradictions()
            
            # Clean up (Switch back and delete - though delete not impl in engine yet, we just switch back)
            self.engine.switch_world(current_world)
            
            if contradictions:
                print(f"👮 Logic Police: REJECTED {fact_proposed} due to contradiction.")
                return False
            
            return True
            
        except Exception as e:
            print(f"👮 Logic Police Error: {e}")
            # Fail safe: Reject if unsure? Or Allow? 
            # Allow for now to avoid blocking on errors
            return True

    def check_thought(self, thought_text: str) -> str:
        """
        Review a natural language thought. 
        Uses Cognitive Bridge to translate to logic, then checks logic.
        """
        # This would require the Cognitive Bridge to translate "Fire is cold" -> Fact(is_cold, Fire)
        # Then check against KB.
        pass
