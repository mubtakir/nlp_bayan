"""
Dual Brain System Extension
نظام الدماغ المزدوج

This extension provides the dual-brain architecture for Bayan:
- Left Brain (Logical): Facts, rules, inference
- Right Brain (Mathematical): Equations, calculations
- Integration Layer: Cross-validation and synthesis
"""

from .dual_brain import DualBrain, DualResult
from .left_brain import LeftBrain, LogicalAnalysis
from .right_brain import RightBrain, MathAnalysis
from .integration_layer import IntegrationLayer, ConsensusLevel

__all__ = [
    'DualBrain', 'DualResult',
    'LeftBrain', 'LogicalAnalysis',
    'RightBrain', 'MathAnalysis',
    'IntegrationLayer', 'ConsensusLevel'
]
