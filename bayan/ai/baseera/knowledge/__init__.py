"""
📚 نظام المعرفة الخارجية لنظام بصيرة الثوري
External Knowledge System for Revolutionary Basera System

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله

هذا المجلد يحتوي على نظام المعرفة الخارجية:
- النظام الشامل للمعرفة الثورية
- حاصد المعرفة من المصادر المحلية
- تكامل Ollama للنماذج اللغوية
- جسر المعرفة الخارجية
- محول المعرفة الثوري
- واجهات تغذية المعرفة
"""

from .revolutionary_knowledge_system import RevolutionaryKnowledgeSystem
from .knowledge_harvester import KnowledgeHarvester
from .external_knowledge_bridge import ExternalKnowledgeBridge
from .revolutionary_knowledge_converter import RevolutionaryKnowledgeConverter
from .knowledge_feeding_interface import KnowledgeFeedingInterface
from .knowledge_feeding_system import KnowledgeFeedingSystem

__all__ = [
    'RevolutionaryKnowledgeSystem',
    'KnowledgeHarvester',
    'ExternalKnowledgeBridge',
    'RevolutionaryKnowledgeConverter',
    'KnowledgeFeedingInterface',
    'KnowledgeFeedingSystem'
]

__version__ = "1.0.0"
__author__ = "باسل يحيى عبدالله"
