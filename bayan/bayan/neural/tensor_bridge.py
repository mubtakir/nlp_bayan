"""
Tensor Bridge for Bayan
جسر التواصل بين المنطق والأعصاب
"""
from typing import Any, List
from ..logical_engine import Fact
from .neural_engine import NeuralEngine

class TensorBridge:
    """
    Bridges the gap between Symbolic Logic (Facts/Concepts) and Neural Tensors (Vectors).
    """
    def __init__(self, neural_engine: NeuralEngine):
        self.neural = neural_engine

    def fact_to_text(self, fact: Fact) -> str:
        """Convert a logical Fact into a natural language sentence."""
        pred = fact.predicate.name
        args = [str(arg) for arg in fact.predicate.args]
        
        # Simple heuristic for converting predicate(arg1, arg2) to text
        # Improve this with a proper template system later
        if len(args) == 1:
            return f"{args[0]} is {pred}"
        elif len(args) == 2:
            return f"{args[0]} {pred} {args[1]}"
        else:
            return f"{pred} involving {', '.join(args)}"

    def embed_fact(self, fact: Fact):
        """Get the vector embedding of a fact."""
        text = self.fact_to_text(fact)
        return self.neural.embed(text)

    def embed_concept(self, concept_name: str):
        """Get the vector embedding of a concept."""
        return self.neural.embed(concept_name)

    def find_similar_facts(self, query_text: str, facts: List[Fact], top_k: int = 3) -> List[Any]:
        """
        Semantic Search: Find facts semantically similar to the query text.
        Structure: List of (Fact, score)
        """
        if not self.neural.initialized:
            return []

        query_vec = self.neural.embed(query_text)
        if query_vec is None:
            return []

        results = []
        for fact in facts:
            fact_text = self.fact_to_text(fact)
            score = self.neural.compute_similarity(query_text, fact_text)
            results.append((fact, score, fact_text))

        # Sort by score descending
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_k]
