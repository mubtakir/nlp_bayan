"""
LLM Gateway: Unified interface for AI models with 3 modes.

Modes:
1. Cloud (Gemini 1.5 Pro via API) - Requires internet + API key
2. Local (Ollama with Qwen/Llama) - Open source, runs locally
3. Standalone (Bayan only) - No external LLM, pure symbolic reasoning

Default: Standalone (to prove Bayan's independence)
"""

import os
import json
from typing import Dict, List, Any, Optional
from enum import Enum

class LLMMode(Enum):
    CLOUD = "cloud"
    LOCAL = "local"
    STANDALONE = "standalone"

class LLMGateway:
    """
    Unified gateway for LLM communication.
    Automatically selects the best available backend.
    """
    def __init__(self, mode: str = "standalone", model: str = None):
        self.mode = LLMMode(mode.lower())
        self.model = model
        self.backend = self._initialize_backend()
        
    def _initialize_backend(self):
        """Initialize the appropriate backend based on mode."""
        if self.mode == LLMMode.CLOUD:
            return CloudBackend(self.model or "gemini-1.5-pro")
        elif self.mode == LLMMode.LOCAL:
            return LocalBackend(self.model or "qwen2.5-coder:7b")
        else:  # STANDALONE
            return StandaloneBackend()
    
    def generate(self, prompt: str, system_instruction: str = None) -> str:
        """
        Generate text from prompt.
        """
        return self.backend.generate(prompt, system_instruction)
    
    def generate_structured(self, prompt: str, schema: Dict) -> Dict:
        """
        Generate structured output (JSON) matching the schema.
        This is crucial for Bayan Atoms.
        """
        return self.backend.generate_structured(prompt, schema)
    
    def get_info(self) -> Dict[str, Any]:
        """Get information about the current backend."""
        return {
            "mode": self.mode.value,
            "model": self.model,
            "backend": self.backend.__class__.__name__,
            "available": self.backend.is_available()
        }


class CloudBackend:
    """Gemini API backend."""
    def __init__(self, model: str):
        self.model = model
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.client = None
        
        if self.api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self.client = genai.GenerativeModel(model)
            except ImportError:
                print("⚠️  google-generativeai not installed. Run: pip install google-generativeai")
    
    def is_available(self) -> bool:
        return self.client is not None
    
    def generate(self, prompt: str, system_instruction: str = None) -> str:
        if not self.is_available():
            return "[ERROR: Gemini API not configured]"
        
        try:
            response = self.client.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"[ERROR: {str(e)}]"
    
    def generate_structured(self, prompt: str, schema: Dict) -> Dict:
        """Force JSON output."""
        json_prompt = f"{prompt}\n\nRespond ONLY with valid JSON matching this schema:\n{json.dumps(schema, indent=2)}"
        response = self.generate(json_prompt)
        
        try:
            # Extract JSON from markdown code blocks if present
            if "```json" in response:
                response = response.split("```json")[1].split("```")[0].strip()
            elif "```" in response:
                response = response.split("```")[1].split("```")[0].strip()
            
            return json.loads(response)
        except:
            return {"error": "Failed to parse JSON", "raw": response}


class LocalBackend:
    """Ollama backend for local models."""
    def __init__(self, model: str):
        self.model = model
        self.client = None
        
        try:
            import ollama
            self.client = ollama
        except ImportError:
            print("⚠️  ollama not installed. Run: pip install ollama")
    
    def is_available(self) -> bool:
        if not self.client:
            return False
        try:
            # Check if Ollama server is running
            self.client.list()
            return True
        except:
            return False
    
    def generate(self, prompt: str, system_instruction: str = None) -> str:
        if not self.is_available():
            return "[ERROR: Ollama not running. Start with: ollama serve]"
        
        try:
            messages = []
            if system_instruction:
                messages.append({"role": "system", "content": system_instruction})
            messages.append({"role": "user", "content": prompt})
            
            response = self.client.chat(model=self.model, messages=messages)
            return response['message']['content']
        except Exception as e:
            return f"[ERROR: {str(e)}]"
    
    def generate_structured(self, prompt: str, schema: Dict) -> Dict:
        """Force JSON output."""
        json_prompt = f"{prompt}\n\nRespond ONLY with valid JSON matching this schema:\n{json.dumps(schema, indent=2)}"
        response = self.generate(json_prompt)
        
        try:
            if "```json" in response:
                response = response.split("```json")[1].split("```")[0].strip()
            elif "```" in response:
                response = response.split("```")[1].split("```")[0].strip()
            
            return json.loads(response)
        except:
            return {"error": "Failed to parse JSON", "raw": response}


class StandaloneBackend:
    """
    Pure Bayan backend - No external LLM.
    Uses only IstinbatEngine and DynamicCircuitBuilder.
    
    This proves that Bayan is CAPABLE on its own.
    The limitation is DATA, not DESIGN.
    """
    def __init__(self):
        # Import here to avoid circular dependencies
        from bayan.bayan.istinbat_engine import IstinbatEngine
        from bayan.bayan.dynamic_builder import DynamicCircuitBuilder, Atom
        
        self.istinbat = IstinbatEngine()
        self.builder = DynamicCircuitBuilder()
    
    def is_available(self) -> bool:
        return True  # Always available
    
    def generate(self, prompt: str, system_instruction: str = None) -> str:
        """
        Process using pure Bayan logic.
        """
        # Try to deduce using Istinbat
        result = self.istinbat.process(prompt)
        
        if result:
            # Convert the deduction to natural language
            summary = f"Based on logical deduction:\n"
            summary += f"- Event: {result.equation.event}\n"
            summary += f"- Entities: {list(result.equation.entities.keys())}\n"
            summary += f"- Consequences: {len(result.consequences)} state changes\n"
            return summary
        else:
            return "[INFO: Could not process with current knowledge base. Add more rules to expand capabilities.]"
    
    def generate_structured(self, prompt: str, schema: Dict) -> Dict:
        """
        Generate structured output using Bayan's symbolic reasoning.
        """
        result = self.istinbat.process(prompt)
        
        if result:
            # Convert to Atoms format
            atoms = []
            for name, role in result.equation.entities.items():
                atoms.append({
                    "type": "Entity",
                    "value": name,
                    "metadata": {"role": role.value}
                })
            
            atoms.append({
                "type": "Action",
                "value": result.equation.event,
                "metadata": {"event_type": result.equation.event_type.value}
            })
            
            return {
                "atoms": atoms,
                "consequences": [
                    {
                        "entity": c.entity_name,
                        "changes": c.state_changes
                    } for c in result.consequences
                ],
                "mode": "standalone",
                "note": "Generated using pure symbolic reasoning (no external LLM)"
            }
        else:
            return {
                "error": "Insufficient knowledge",
                "suggestion": "Add more causal rules to the knowledge base",
                "mode": "standalone"
            }
