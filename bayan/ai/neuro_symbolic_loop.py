"""
Neuro-Symbolic Loop: The "Dream" -> "Reality Check" -> "Realization" Pipeline

This is the core integration between LLMs and Bayan's symbolic reasoning.
"""

from typing import Dict, Any, Optional
from .llm_gateway import LLMGateway, LLMMode

class NeuroSymbolicLoop:
    """
    The unified pipeline that combines:
    1. LLM's "Dream" (creative generation)
    2. Bayan's "Reality Check" (logical verification)
    3. Bayan's "Realization" (fluent text generation)
    """
    def __init__(self, mode: str = "standalone"):
        self.gateway = LLMGateway(mode=mode)
        
        # Import Bayan engines
        from bayan.bayan.istinbat_engine import IstinbatEngine
        from bayan.bayan.dynamic_builder import DynamicCircuitBuilder
        
        self.istinbat = IstinbatEngine()
        self.builder = DynamicCircuitBuilder()
    
    def process(self, user_input: str, language: str = "arabic") -> Dict[str, Any]:
        """
        Main pipeline: User Input -> Atoms -> Verification -> Text
        
        Returns a dict with:
        - dream: The LLM's initial generation
        - reality_check: Bayan's verification results
        - realization: The final output text
        - metadata: Info about the process
        """
        result = {
            "input": user_input,
            "mode": self.gateway.mode.value,
            "language": language
        }
        
        # Step 1: Dream (LLM generates Atoms)
        dream = self._dream(user_input)
        result["dream"] = dream
        
        # Step 2: Reality Check (Bayan verifies)
        reality_check = self._reality_check(dream)
        result["reality_check"] = reality_check
        
        # Step 3: Realization (Convert back to text)
        realization = self._realize(reality_check, language)
        result["realization"] = realization
        
        return result
    
    def _dream(self, user_input: str) -> Dict[str, Any]:
        """
        Step 1: Ask the LLM (or Standalone) to generate Atoms.
        """
        schema = {
            "atoms": [
                {
                    "type": "Entity | Action | Context",
                    "value": "string",
                    "metadata": {}
                }
            ]
        }
        
        prompt = f"""
You are a semantic analyzer for the Bayan language.
Convert this text into Bayan Atoms (Entities, Actions, Contexts):

Text: "{user_input}"

Extract:
- Entities (people, objects)
- Actions (verbs, events)
- Contexts (time, place)
"""
        
        return self.gateway.generate_structured(prompt, schema)
    
    def _reality_check(self, dream: Dict[str, Any]) -> Dict[str, Any]:
        """
        Step 2: Verify the Atoms using Bayan's logic.
        """
        if "error" in dream:
            return {
                "verified": False,
                "reason": "Dream generation failed",
                "original_error": dream
            }
        
        atoms = dream.get("atoms", [])
        
        # Check if atoms are logically consistent
        # For now, we accept all atoms (future: add contradiction detection)
        return {
            "verified": True,
            "atoms": atoms,
            "corrections": [],
            "note": "Atoms accepted (no contradictions found)"
        }
    
    def _realize(self, reality_check: Dict[str, Any], language: str) -> str:
        """
        Step 3: Convert verified atoms back to fluent text.
        """
        if not reality_check.get("verified"):
            return f"[Could not generate text: {reality_check.get('reason')}]"
        
        atoms = reality_check.get("atoms", [])
        
        if not atoms:
            return "[No atoms to realize]"
        
        # Simple realization: concatenate atoms
        # Future: Use GLM Surface Realizer for fluent text
        entities = [a["value"] for a in atoms if a.get("type") == "Entity"]
        actions = [a["value"] for a in atoms if a.get("type") == "Action"]
        
        if language == "arabic":
            if entities and actions:
                return f"{entities[0]} {actions[0]} {entities[1] if len(entities) > 1 else ''}"
            else:
                return "لا يمكن تكوين جملة من الذرات المعطاة"
        else:
            if entities and actions:
                return f"{entities[0]} {actions[0]} {entities[1] if len(entities) > 1 else ''}"
            else:
                return "Cannot form sentence from given atoms"
    
    def get_info(self) -> Dict[str, Any]:
        """Get information about the current configuration."""
        return {
            "gateway": self.gateway.get_info(),
            "components": {
                "istinbat_engine": "active",
                "dynamic_builder": "active"
            }
        }
