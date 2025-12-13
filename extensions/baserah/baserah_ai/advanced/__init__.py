"""
الوحدات المتقدمة - Advanced Units
==================================

المكونات المتقدمة لنظام بصيرة:
- طبقات التفكير المتعددة
- نظام الوعي والانتباه
- التكامل اللغوي-الرياضي

المؤلف: باسل يحيى عبدالله
"""

from .thinking_layers import ThinkingCore, ThinkingLayer, LayerType, LayerResult
from .consciousness import (
    ConsciousnessSystem,
    AttentionFocus,
    AttentionLevel,
    ConsciousnessState
)

__all__ = [
    # طبقات التفكير
    'ThinkingCore',
    'ThinkingLayer',
    'LayerType',
    'LayerResult',

    # نظام الوعي
    'ConsciousnessSystem',
    'AttentionFocus',
    'AttentionLevel',
    'ConsciousnessState',
]

