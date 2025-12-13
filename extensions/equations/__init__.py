"""
Equations Extension
نظام المعادلات

This extension provides equation systems:
- Linguistic Equations (الفكرة = أشياء + حدث + نتيجة)
- Mother Equation (Object = id + Φ + Ψ(t) + Γ)
- GSE (Generalized Shape Equation)
"""

from .linguistic_equation import (
    LinguisticEquation, EntityState, Role, EventType,
    KnowledgeBase, LinguisticEquationParser, create_simple_equation
)
from .mother_equation import (
    MotherEquation, Property, State, PropertyDomain,
    create_example_human, create_example_tree, create_example_building
)
from .gse import GSEModel, generalized_sigmoid

__all__ = [
    'LinguisticEquation', 'EntityState', 'Role', 'EventType',
    'KnowledgeBase', 'LinguisticEquationParser', 'create_simple_equation',
    'MotherEquation', 'Property', 'State', 'PropertyDomain',
    'create_example_human', 'create_example_tree', 'create_example_building',
    'GSEModel', 'generalized_sigmoid'
]
