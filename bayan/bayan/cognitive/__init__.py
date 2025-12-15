"""
Bayan Cognitive Package
حزمة بيان الإدراكية
========================

Implements the Neuro-Symbolic Cognitive Bridge.
تنفيذ الجسر العصبي-الرمزي.

المكونات:
- CognitiveBridge: الجسر الإدراكي
- LLMInterface: واجهة النماذج اللغوية
- ConversationEngine: محرك الحوار الذكي
- LearningAgent: وكيل التعلم التفاعلي
- AbductionEngine: محرك الاستنباط العكسي
- CausalStoriesEngine: محرك القصص السببية
- KnowledgeExporter: مصدّر المعرفة
- BayanAgent: الوكيل الذكي الموحد
"""

from .cognitive_bridge import CognitiveBridge
from .llm_interface import LLMInterface

# New capabilities
try:
    from .conversation_engine import ConversationEngine, ConversationMemory
    from .interactive_learning import LearningAgent, FactExtractor
    from .abduction_engine import AbductionEngine, HypothesisGenerator
    from .causal_stories import CausalStoriesEngine, StorySimulator
    from .knowledge_export import KnowledgeExporter
    from .intelligent_agent import BayanAgent, TaskPlanner, ToolExecutor
except ImportError as e:
    pass  # Some modules may not be available in all environments

__all__ = [
    'CognitiveBridge',
    'LLMInterface', 
    'ConversationEngine',
    'ConversationMemory',
    'LearningAgent',
    'FactExtractor',
    'AbductionEngine',
    'HypothesisGenerator',
    'CausalStoriesEngine',
    'StorySimulator',
    'KnowledgeExporter',
    'BayanAgent',
    'TaskPlanner',
    'ToolExecutor'
]
