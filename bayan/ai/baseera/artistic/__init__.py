"""
🎨 الوحدات الفنية لنظام بصيرة الثوري
Artistic Components of Revolutionary Basera System

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله

هذا المجلد يحتوي على الوحدات الفنية:
- الوحدة الفنية للنشر والإخراج
- واجهة الاستنباط الفني
- الوحدة الفنية المحسنة
- نظام التصور الثوري
"""

from .artistic_publishing_unit import ArtisticPublishingUnit
from .artistic_inference_interface import create_gradio_interface
from .enhanced_artistic_unit_fixed import BaserahIntegratedSystem as EnhancedArtisticUnit
from .revolutionary_visualization import RevolutionaryVisualizer

__all__ = [
    'ArtisticPublishingUnit',
    'create_gradio_interface',
    'EnhancedArtisticUnit', 
    'RevolutionaryVisualizer'
]

__version__ = "1.0.0"
__author__ = "باسل يحيى عبدالله"
