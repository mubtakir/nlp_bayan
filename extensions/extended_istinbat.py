"""
🧠 محرك الاستنباط الموسع - Extended Istinbat Engine
طبقة وسيطية تضيف دعم اللهجات لمحرك الاستنباط الأصلي

This is a wrapper layer that adds dialect support to the original IstinbatEngine
without modifying the locked core files.
"""

import sys
import os

# إضافة مسار المشروع
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import Optional
from dataclasses import dataclass
from .dialect_adapter import DialectAdapter, Dialect, ConversionResult

# استيراد المحرك الأصلي
from bayan.bayan.istinbat_engine import IstinbatEngine, DeductionResult


@dataclass
class ExtendedDeductionResult:
    """نتيجة الاستنباط الموسعة مع معلومات اللهجة"""
    original_result: DeductionResult  # النتيجة الأصلية
    original_text: Optional[str] = None  # النص الأصلي قبل التحويل
    dialect: Optional[str] = None  # اللهجة المكتشفة
    converted_text: Optional[str] = None  # النص بعد التحويل للفصحى
    conversion_changes: list = None  # التغييرات التي تمت
    
    def __post_init__(self):
        if self.conversion_changes is None:
            self.conversion_changes = []
    
    # تمرير الخصائص للنتيجة الأصلية
    @property
    def equation(self):
        return self.original_result.equation
    
    @property
    def consequences(self):
        return self.original_result.consequences


class ExtendedIstinbatEngine:
    """
    محرك استنباط موسع يدعم اللهجات العربية
    
    يعمل كطبقة وسيطية فوق IstinbatEngine الأصلي
    """
    
    def __init__(self, enable_dialect_support: bool = True, **kwargs):
        """
        تهيئة المحرك الموسع
        
        Args:
            enable_dialect_support: تفعيل دعم اللهجات
            **kwargs: معاملات إضافية للمحرك الأصلي
        """
        # المحرك الأصلي
        self.engine = IstinbatEngine(**kwargs)
        
        # دعم اللهجات
        self.enable_dialect_support = enable_dialect_support
        self.dialect_adapter = DialectAdapter() if enable_dialect_support else None
    
    def process(self, text: str, dialect: Optional[str] = None) -> Optional[ExtendedDeductionResult]:
        """
        معالجة النص مع دعم اللهجات
        
        Args:
            text: النص المراد تحليله (فصحى أو لهجة)
            dialect: اللهجة (اختياري - يتم اكتشافها تلقائياً)
            
        Returns:
            نتيجة الاستنباط الموسعة أو None
        """
        original_text = text
        detected_dialect = None
        converted_text = None
        changes = []
        
        # تحويل من اللهجة للفصحى إذا مفعّل
        if self.enable_dialect_support and self.dialect_adapter:
            conversion = self.dialect_adapter.convert_to_standard(text, dialect)
            
            if conversion.dialect != Dialect.STANDARD and conversion.changes:
                detected_dialect = conversion.dialect.value
                converted_text = conversion.converted
                changes = conversion.changes
                text = converted_text
                print(f"   🌍 اللهجة المكتشفة: {detected_dialect}")
                print(f"   📝 النص الأصلي: {original_text}")
                print(f"   ✨ النص المحول: {converted_text}")
        
        # استدعاء المحرك الأصلي
        result = self.engine.process(text)
        
        if result:
            return ExtendedDeductionResult(
                original_result=result,
                original_text=original_text if detected_dialect else None,
                dialect=detected_dialect,
                converted_text=converted_text,
                conversion_changes=changes
            )
        
        return None
    
    # تمرير الخصائص للمحرك الأصلي
    @property
    def kb(self):
        return self.engine.kb
    
    @property
    def parser(self):
        return self.engine.parser


# دالة مساعدة لإنشاء المحرك
def create_engine(enable_dialects: bool = True) -> ExtendedIstinbatEngine:
    """إنشاء محرك استنباط موسع"""
    return ExtendedIstinbatEngine(enable_dialect_support=enable_dialects)

