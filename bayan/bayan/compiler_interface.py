"""
واجهة المترجم - Compiler Interface
==================================

نظام موحد لتصنيف وإدارة أخطاء الترجمة في لغة البيان.
مستوحى من: baserah-bayan/bayan-baserah-integration/bayan-compiler-interface.bn

المؤلف: باسل يحيى عبدالله
التاريخ: 2025-11-25
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional, Any
from datetime import datetime
import time


# ═══════════════════════════════════════════════════════════════
# التعدادات (Enums)
# ═══════════════════════════════════════════════════════════════

class ErrorType(Enum):
    """أنواع الأخطاء في الترجمة"""
    LEXICAL = "معجمي"           # خطأ في التحليل المعجمي (tokenization)
    SYNTAX = "نحوي"             # خطأ في بناء الجملة
    SEMANTIC = "دلالي"          # خطأ في المعنى/السياق
    RUNTIME = "تنفيذي"          # خطأ أثناء التنفيذ
    TYPE = "أنواع"              # خطأ في الأنواع (type mismatch)
    LOGICAL = "منطقي"           # خطأ منطقي (contradiction)
    REFERENCE = "مرجعي"         # متغير/دالة غير معرفة
    IMPORT = "استيراد"          # خطأ في الاستيراد
    INDENTATION = "مسافات"      # خطأ في المسافات البادئة
    UNKNOWN = "غير_معروف"       # خطأ غير مصنف


class ErrorSeverity(Enum):
    """شدة الخطأ"""
    ERROR = ("خطأ", 3)          # خطأ - يمنع التنفيذ
    WARNING = ("تحذير", 2)     # تحذير - لا يمنع التنفيذ
    INFO = ("معلومة", 1)       # معلومة
    HINT = ("تلميح", 0)        # تلميح لتحسين الكود
    
    def __init__(self, arabic_name, level):
        self.arabic_name = arabic_name
        self.level = level


class OptimizationLevel(Enum):
    """مستويات التحسين"""
    NONE = 0        # بدون تحسين
    BASIC = 1       # تحسينات أساسية
    MEDIUM = 2      # تحسينات متوسطة
    AGGRESSIVE = 3  # تحسينات قوية


# ═══════════════════════════════════════════════════════════════
# الفئات (Classes)
# ═══════════════════════════════════════════════════════════════

@dataclass
class CompilationError:
    """
    يمثل خطأ في عملية الترجمة.
    
    Attributes:
        error_type: نوع الخطأ
        severity: شدة الخطأ
        message: رسالة الخطأ
        line: رقم السطر (1-indexed)
        column: رقم العمود (1-indexed)
        file_name: اسم الملف
        source_snippet: مقتطف من الكود المصدري
        suggestion: اقتراح لإصلاح الخطأ
    """
    error_type: ErrorType
    severity: ErrorSeverity
    message: str
    line: int
    column: int = 0
    file_name: str = "unknown"
    source_snippet: Optional[str] = None
    suggestion: Optional[str] = None
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
    
    def get_description(self, language: str = "ar") -> str:
        """
        الحصول على وصف كامل للخطأ.
        
        Args:
            language: اللغة ('ar' أو 'en')
        
        Returns:
            وصف نصي للخطأ
        """
        if language == "ar":
            severity_name = self.severity.arabic_name
            type_name = self.error_type.value
            
            desc = f"[{severity_name}] {type_name} في السطر {self.line}"
            if self.column > 0:
                desc += f":{self.column}"
            desc += f": {self.message}"
            
            if self.source_snippet:
                desc += f"\n  الكود: {self.source_snippet}"
            
            if self.suggestion:
                desc += f"\n  💡 اقتراح: {self.suggestion}"
        else:
            desc = f"[{self.severity.name}] {self.error_type.name} at line {self.line}"
            if self.column > 0:
                desc += f":{self.column}"
            desc += f": {self.message}"
            
            if self.source_snippet:
                desc += f"\n  Code: {self.source_snippet}"
            
            if self.suggestion:
                desc += f"\n  💡 Suggestion: {self.suggestion}"
        
        return desc
    
    def to_dict(self) -> Dict[str, Any]:
        """تحويل إلى قاموس"""
        return {
            'type': self.error_type.name,
            'type_ar': self.error_type.value,
            'severity': self.severity.name,
            'severity_ar': self.severity.arabic_name,
            'severity_level': self.severity.level,
            'message': self.message,
            'line': self.line,
            'column': self.column,
            'file': self.file_name,
            'snippet': self.source_snippet,
            'suggestion': self.suggestion,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }


@dataclass
class CompilationResult:
    """
    نتيجة عملية الترجمة.
    
    Attributes:
        success: هل نجحت الترجمة؟
        errors: قائمة الأخطاء
        warnings: قائمة التحذيرات
        hints: قائمة التلميحات
        compiled_code: الكود المترجم (إن وُجد)
        execution_time: وقت التنفيذ (ثواني)
        optimization_level: مستوى التحسين المستخدم
    """
    success: bool
    errors: List[CompilationError]
    warnings: List[CompilationError]
    hints: List[CompilationError]
    compiled_code: Optional[str] = None
    execution_time: float = 0.0
   optimization_level: OptimizationLevel = OptimizationLevel.BASIC
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
    
    def has_errors(self) -> bool:
        """هل يوجد أخطاء؟"""
        return len(self.errors) > 0
    
    def has_warnings(self) -> bool:
        """هل يوجد تحذيرات؟"""
        return len(self.warnings) > 0
    
    def get_summary(self, language: str = "ar") -> str:
        """ملخص النتيجة"""
        if language == "ar":
            status = "نجحت ✅" if self.success else "فشلت ❌"
            summary = f"الترجمة {status}\n"
            summary += f"  - أخطاء: {len(self.errors)}\n"
            summary += f"  - تحذيرات: {len(self.warnings)}\n"
            summary += f"  - تلميحات: {len(self.hints)}\n"
            summary += f"  - الوقت: {self.execution_time*1000:.2f} ms"
        else:
            status = "succeeded ✅" if self.success else "failed ❌"
            summary = f"Compilation {status}\n"
            summary += f"  - Errors: {len(self.errors)}\n"
            summary += f"  - Warnings: {len(self.warnings)}\n"
            summary += f"  - Hints: {len(self.hints)}\n"
            summary += f"  - Time: {self.execution_time*1000:.2f} ms"
        
        return summary
    
    def to_dict(self) -> Dict[str, Any]:
        """تحويل إلى قاموس"""
        return {
            'success': self.success,
            'errors': [e.to_dict() for e in self.errors],
            'warnings': [w.to_dict() for w in self.warnings],
            'hints': [h.to_dict() for h in self.hints],
            'compiled_code': self.compiled_code,
            'execution_time': self.execution_time,
            'optimization_level': self.optimization_level.name,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }


class BayanCompilerInterface:
    """
    واجهة موحدة للتفاعل مع مترجم لغة البيان.
    
    يوفر:
    - تصنيف الأخطاء
    - إحصائيات الترجمة
    - تتبع الأخطاء الشائعة
    - اقتراحات الإصلاح
    """
    
    def __init__(self):
        self.compilation_history: List[CompilationResult] = []
        self.error_statistics: Dict[ErrorType, int] = {et: 0 for et in ErrorType}
        self.total_compilations = 0
        self.successful_compilations = 0
        
    def compile(
        self,
        source_code: str,
        file_name: str = "unknown.bayan",
        optimization_level: OptimizationLevel = OptimizationLevel.BASIC
    ) -> CompilationResult:
        """
        ترجمة كود بيان.
        
        Args:
            source_code: الكود المصدري
            file_name: اسم الملف
            optimization_level: مستوى التحسين
        
        Returns:
            CompilationResult
        """
        start_time = time.time()
        
        errors: List[CompilationError] = []
        warnings: List[CompilationError] = []
        hints: List[CompilationError] = []
        
        # محاكاة عملية الترجمة (سيتم استبداله بالمترجم الحقيقي)
        # هنا نفحص الكود بحثاً عن أخطاء شائعة
        
        lines = source_code.split('\n')
        for i, line in enumerate(lines, 1):
            # فحص أساسي
            if line.strip() and not line.strip().startswith('#'):
                # مثال: فحص الأقواس
                if '(' in line and ')' not in line:
                    errors.append(CompilationError(
                        error_type=ErrorType.SYNTAX,
                        severity=ErrorSeverity.ERROR,
                        message="قوس مفتوح بدون إغلاق",
                        line=i,
                        file_name=file_name,
                        source_snippet=line.strip(),
                        suggestion="أضف ')' في نهاية السطر"
                    ))
        
        execution_time = time.time() - start_time
        success = len(errors) == 0
        
        result = CompilationResult(
            success=success,
            errors=errors,
            warnings=warnings,
            hints=hints,
            compiled_code=source_code if success else None,
            execution_time=execution_time,
            optimization_level=optimization_level
        )
        
        # تحديث الإحصائيات
        self.compilation_history.append(result)
        self.total_compilations += 1
        if success:
            self.successful_compilations += 1
        
        for error in errors:
            self.error_statistics[error.error_type] += 1
        
        return result
    
    def get_statistics(self) -> Dict[str, Any]:
        """الحصول على إحصائيات الترجمة"""
        success_rate = (self.successful_compilations / self.total_compilations * 100
                       if self.total_compilations > 0 else 0)
        
        return {
            'total_compilations': self.total_compilations,
            'successful': self.successful_compilations,
            'failed': self.total_compilations - self.successful_compilations,
            'success_rate': f"{success_rate:.1f}%",
            'error_statistics': {
                et.value: count 
                for et, count in self.error_statistics.items()
                if count > 0
            },
            'average_time': (
                sum(r.execution_time for r in self.compilation_history) / len(self.compilation_history)
                if self.compilation_history else 0
            )
        }
    
    def get_common_errors(self, limit: int = 5) -> List[tuple]:
        """
        الحصول على الأخطاء الأكثر شيوعاً.
        
        Args:
            limit: عدد الأخطاء المطلوبة
        
        Returns:
            قائمة من (ErrorType, count)
        """
        sorted_errors = sorted(
            self.error_statistics.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return [(et.value, count) for et, count in sorted_errors[:limit] if count > 0]
    
    def suggest_fix(self, error: CompilationError) -> Optional[str]:
        """
        اقتراح إصلاح للخطأ.
        
        Args:
            error: الخطأ
        
        Returns:
            نص الاقتراح أو None
        """
        # يمكن توسيع هذا النظام ليكون أكثر ذكاءً
        if error.suggestion:
            return error.suggestion
        
        # اقتراحات افتراضية بناءً على نوع الخطأ
        suggestions = {
            ErrorType.SYNTAX: "تحقق من بناء الجملة وتطابق الأقواس",
            ErrorType.REFERENCE: "تأكد من تعريف المتغير قبل استخدامه",
            ErrorType.TYPE: "تحقق من توافق الأنواع",
            ErrorType.INDENTATION: "استخدم مسافات متساوية",
        }
        
        return suggestions.get(error.error_type, "راجع الوثائق")
    
    def clear_history(self):
        """مسح سجل الترجمة"""
        self.compilation_history.clear()
        self.error_statistics = {et: 0 for et in ErrorType}
        self.total_compilations = 0
        self.successful_compilations = 0
