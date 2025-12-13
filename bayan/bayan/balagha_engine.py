"""
Balagha Engine (مقياس البلاغة)
Evaluates the "eloquence" of text based on logical and aesthetic criteria.

Criteria:
1. Conciseness (الإيجاز): High meaningful content in few words.
2. Relevance (مقتضى الحال): Alignment with the current context.
"""

from typing import List, Dict, Any
from dataclasses import dataclass

@dataclass
class BalaghaScore:
    conciseness: float  # 0.0 - 1.0 (Higher is better)
    relevance: float    # 0.0 - 1.0 (Higher is better)
    total: float        # Weighted average
    feedback: List[str]

class BalaghaEngine:
    """
    Engine for evaluating text eloquence (Balagha).
    """

    def evaluate(self, text: str, context_keywords: List[str]) -> BalaghaScore:
        """
        Evaluate the eloquence of a text given a context.
        
        Args:
            text: The input text to evaluate.
            context_keywords: Keywords defining the current "Maqam" (Context).
            
        Returns:
            BalaghaScore object containing detailed metrics.
        """
        words = [w for w in text.split() if w.strip()]
        word_count = len(words)

        if word_count == 0:
            return BalaghaScore(0.0, 0.0, 0.0, ["Text is empty."])

        # 1. Calculate Relevance (Mutaabaqa)
        match_count = 0
        for word in words:
            # Check if word contains any context keyword (simple substring check for now)
            if any(k in word for k in context_keywords):
                match_count += 1
        
        # Relevance = Ratio of context-relevant words to total words
        # We boost it slightly because not every word needs to be a keyword (stop words etc)
        # Using min(ratio * 2.0, 1.0) as in JS version
        relevance_raw = match_count / word_count
        relevance = min(relevance_raw * 2.0, 1.0)

        # 2. Calculate Conciseness (Ijaz)
        # Heuristic: Shorter is better IF it conveys meaning.
        # Penalty for excessive length.
        # Ideal length for a simple statement might be 3-7 words.
        conciseness = 1.0
        if word_count > 7:
            # Drop score by 0.05 for every word over 7
            conciseness = max(0.1, 1.0 - ((word_count - 7) * 0.05))

        # 3. Total Score
        # Relevance is weighted higher (0.6) than conciseness (0.4)
        total = (relevance * 0.6) + (conciseness * 0.4)

        feedback = []
        if relevance < 0.5:
            feedback.append("Text has low relevance to context.")
        if conciseness < 0.5:
            feedback.append("Text is too verbose.")
        if total > 0.8:
            feedback.append("Highly eloquent!")

        return BalaghaScore(conciseness, relevance, total, feedback)
