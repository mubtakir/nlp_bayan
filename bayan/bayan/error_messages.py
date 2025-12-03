"""
Bayan Error Messages - رسائل الأخطاء للبيان
Bilingual error messages with suggestions

This module provides clear, helpful error messages in both Arabic and English
with suggestions for fixing common errors.
"""

from typing import Dict, Optional, List, Tuple
from dataclasses import dataclass
from enum import Enum

class ErrorCategory(Enum):
    """Error categories / فئات الأخطاء"""
    SYNTAX = "syntax"
    RUNTIME = "runtime"
    TYPE = "type"
    NAME = "name"
    IMPORT = "import"
    LOGIC = "logic"
    VALUE = "value"
    INDEX = "index"
    KEY = "key"
    ATTRIBUTE = "attribute"
    DIVISION = "division"
    FILE = "file"
    ARGUMENT = "argument"

@dataclass
class BilingualMessage:
    """Bilingual error message with suggestion"""
    ar: str  # Arabic message
    en: str  # English message
    suggestion_ar: Optional[str] = None
    suggestion_en: Optional[str] = None
    
    def get(self, lang: str = "ar") -> str:
        """Get message in specified language"""
        return self.ar if lang == "ar" else self.en
    
    def get_suggestion(self, lang: str = "ar") -> Optional[str]:
        """Get suggestion in specified language"""
        if lang == "ar":
            return self.suggestion_ar
        return self.suggestion_en

# ============ Error Message Templates ============

ERROR_MESSAGES: Dict[str, BilingualMessage] = {
    # Syntax Errors - أخطاء نحوية
    "unknown_char": BilingualMessage(
        ar="حرف غير معروف '{char}' في السطر {line}:{col}",
        en="Unknown character '{char}' at line {line}:{col}",
        suggestion_ar="تأكد من استخدام أحرف صالحة في الكود",
        suggestion_en="Make sure to use valid characters in your code"
    ),
    "unterminated_string": BilingualMessage(
        ar="نص غير مغلق في السطر {line}:{col}",
        en="Unterminated string at line {line}:{col}",
        suggestion_ar="أضف علامة اقتباس مطابقة لإغلاق النص",
        suggestion_en="Add a matching quote to close the string"
    ),
    "unexpected_token": BilingualMessage(
        ar="رمز غير متوقع '{token}' في السطر {line}",
        en="Unexpected token '{token}' at line {line}",
        suggestion_ar="تحقق من بناء الجملة وترتيب الرموز",
        suggestion_en="Check the syntax and token order"
    ),
    "expected_token": BilingualMessage(
        ar="متوقع '{expected}' ولكن وجد '{found}' في السطر {line}",
        en="Expected '{expected}' but found '{found}' at line {line}",
        suggestion_ar="أضف '{expected}' في المكان المناسب",
        suggestion_en="Add '{expected}' in the appropriate place"
    ),
    "missing_colon": BilingualMessage(
        ar="نقطتان ':' مفقودة بعد '{construct}' في السطر {line}",
        en="Missing ':' after '{construct}' at line {line}",
        suggestion_ar="أضف ':' بعد {construct}",
        suggestion_en="Add ':' after {construct}"
    ),
    "unmatched_paren": BilingualMessage(
        ar="قوس '{paren}' غير مطابق في السطر {line}",
        en="Unmatched '{paren}' at line {line}",
        suggestion_ar="تأكد من إغلاق جميع الأقواس بشكل صحيح",
        suggestion_en="Make sure all parentheses are properly closed"
    ),
    "invalid_indent": BilingualMessage(
        ar="مسافة بادئة غير صالحة في السطر {line}",
        en="Invalid indentation at line {line}",
        suggestion_ar="استخدم مسافات أو tabs بشكل متسق",
        suggestion_en="Use spaces or tabs consistently"
    ),
    
    # Name Errors - أخطاء الأسماء
    "undefined_var": BilingualMessage(
        ar="متغير غير معرف: '{name}'",
        en="Undefined variable: '{name}'",
        suggestion_ar="تأكد من تعريف المتغير قبل استخدامه، أو تحقق من الإملاء",
        suggestion_en="Make sure the variable is defined before use, or check spelling"
    ),
    "undefined_func": BilingualMessage(
        ar="دالة غير معرفة: '{name}'",
        en="Undefined function: '{name}'",
        suggestion_ar="تأكد من تعريف الدالة قبل استدعائها",
        suggestion_en="Make sure the function is defined before calling it"
    ),
    "undefined_class": BilingualMessage(
        ar="صنف غير معرف: '{name}'",
        en="Undefined class: '{name}'",
        suggestion_ar="تأكد من تعريف الصنف قبل استخدامه",
        suggestion_en="Make sure the class is defined before using it"
    ),
    
    # Type Errors - أخطاء الأنواع
    "type_mismatch": BilingualMessage(
        ar="عدم تطابق الأنواع: متوقع '{expected}' ولكن وجد '{found}'",
        en="Type mismatch: expected '{expected}' but got '{found}'",
        suggestion_ar="تحقق من نوع القيمة المستخدمة",
        suggestion_en="Check the type of the value being used"
    ),
    "not_callable": BilingualMessage(
        ar="'{name}' ليس قابلاً للاستدعاء (ليس دالة)",
        en="'{name}' is not callable (not a function)",
        suggestion_ar="تأكد من أن '{name}' هو دالة أو صنف",
        suggestion_en="Make sure '{name}' is a function or class"
    ),
    "not_iterable": BilingualMessage(
        ar="'{type}' غير قابل للتكرار",
        en="'{type}' is not iterable",
        suggestion_ar="استخدم قائمة أو مجموعة أو نص للتكرار",
        suggestion_en="Use a list, set, or string for iteration"
    ),
    "not_subscriptable": BilingualMessage(
        ar="'{type}' لا يدعم الفهرسة",
        en="'{type}' is not subscriptable",
        suggestion_ar="استخدم قائمة أو قاموس للوصول بالفهرس",
        suggestion_en="Use a list or dictionary for index access"
    ),
    
    # Value Errors - أخطاء القيم
    "division_by_zero": BilingualMessage(
        ar="خطأ: القسمة على صفر",
        en="Error: Division by zero",
        suggestion_ar="تأكد من أن المقسوم عليه ليس صفراً",
        suggestion_en="Make sure the divisor is not zero"
    ),
    "invalid_value": BilingualMessage(
        ar="قيمة غير صالحة: {value}",
        en="Invalid value: {value}",
        suggestion_ar="تحقق من القيمة المدخلة",
        suggestion_en="Check the input value"
    ),
    "out_of_range": BilingualMessage(
        ar="القيمة خارج النطاق المسموح",
        en="Value out of allowed range",
        suggestion_ar="استخدم قيمة ضمن النطاق المحدد",
        suggestion_en="Use a value within the specified range"
    ),
    
    # Index/Key Errors - أخطاء الفهرسة
    "index_out_of_range": BilingualMessage(
        ar="الفهرس {index} خارج نطاق القائمة (الطول: {length})",
        en="Index {index} out of range (length: {length})",
        suggestion_ar="استخدم فهرساً بين 0 و {max_index}",
        suggestion_en="Use an index between 0 and {max_index}"
    ),
    "key_not_found": BilingualMessage(
        ar="المفتاح '{key}' غير موجود في القاموس",
        en="Key '{key}' not found in dictionary",
        suggestion_ar="تحقق من وجود المفتاح قبل الوصول إليه، أو استخدم .get()",
        suggestion_en="Check if key exists before accessing, or use .get()"
    ),
    
    # Attribute Errors - أخطاء الخصائص
    "no_attribute": BilingualMessage(
        ar="'{type}' لا يملك الخاصية '{attr}'",
        en="'{type}' has no attribute '{attr}'",
        suggestion_ar="تحقق من اسم الخاصية أو الدالة",
        suggestion_en="Check the attribute or method name"
    ),
    
    # Argument Errors - أخطاء المعاملات
    "wrong_arg_count": BilingualMessage(
        ar="الدالة '{name}' تتوقع {expected} معامل(ات) ولكن تم تمرير {got}",
        en="Function '{name}' expects {expected} argument(s) but got {got}",
        suggestion_ar="تحقق من عدد المعاملات المطلوبة",
        suggestion_en="Check the required number of arguments"
    ),
    "missing_required_arg": BilingualMessage(
        ar="المعامل المطلوب '{arg}' مفقود في الدالة '{func}'",
        en="Required argument '{arg}' missing in function '{func}'",
        suggestion_ar="أضف المعامل '{arg}' عند استدعاء الدالة",
        suggestion_en="Add argument '{arg}' when calling the function"
    ),
    "unexpected_keyword_arg": BilingualMessage(
        ar="معامل مسمى غير متوقع: '{arg}'",
        en="Unexpected keyword argument: '{arg}'",
        suggestion_ar="تحقق من أسماء المعاملات المسموحة",
        suggestion_en="Check the allowed parameter names"
    ),
    
    # Import Errors - أخطاء الاستيراد
    "module_not_found": BilingualMessage(
        ar="الوحدة '{module}' غير موجودة",
        en="Module '{module}' not found",
        suggestion_ar="تأكد من وجود الملف وصحة المسار",
        suggestion_en="Make sure the file exists and the path is correct"
    ),
    "import_error": BilingualMessage(
        ar="خطأ في استيراد '{name}' من '{module}'",
        en="Error importing '{name}' from '{module}'",
        suggestion_ar="تحقق من وجود '{name}' في الوحدة",
        suggestion_en="Check if '{name}' exists in the module"
    ),
    
    # Logic Errors - أخطاء منطقية
    "no_solution": BilingualMessage(
        ar="لا يوجد حل للاستعلام المنطقي",
        en="No solution found for logical query",
        suggestion_ar="تحقق من الحقائق والقواعد المعرفة",
        suggestion_en="Check the defined facts and rules"
    ),
    "infinite_loop": BilingualMessage(
        ar="تحذير: احتمال حلقة لا نهائية",
        en="Warning: Possible infinite loop detected",
        suggestion_ar="تحقق من شرط الخروج من الحلقة",
        suggestion_en="Check the loop exit condition"
    ),
    
    # File Errors - أخطاء الملفات
    "file_not_found": BilingualMessage(
        ar="الملف '{path}' غير موجود",
        en="File '{path}' not found",
        suggestion_ar="تحقق من مسار الملف وصحة الاسم",
        suggestion_en="Check the file path and name"
    ),
    "permission_denied": BilingualMessage(
        ar="لا توجد صلاحية للوصول إلى '{path}'",
        en="Permission denied for '{path}'",
        suggestion_ar="تحقق من صلاحيات الملف",
        suggestion_en="Check file permissions"
    ),
}

# Similar variable name suggestions
COMMON_TYPOS: Dict[str, List[str]] = {
    "pirnt": ["print", "اطبع"],
    "prnit": ["print", "اطبع"],
    "pritn": ["print", "اطبع"],
    "retrun": ["return", "أرجع"],
    "reutrn": ["return", "أرجع"],
    "ture": ["True", "صحيح"],
    "flase": ["False", "خطأ"],
    "fasle": ["False", "خطأ"],
    "noen": ["None", "لاشيء"],
    "defn": ["def", "دالة"],
    "calss": ["class", "صنف"],
    "slef": ["self", "ذاتي"],
    "sefl": ["self", "ذاتي"],
}

def get_error_message(error_key: str, lang: str = "ar", **kwargs) -> str:
    """
    Get formatted error message.
    
    Args:
        error_key: Key for the error message
        lang: Language ('ar' or 'en')
        **kwargs: Format arguments
    
    Returns:
        Formatted error message
    """
    if error_key not in ERROR_MESSAGES:
        return f"Unknown error: {error_key}" if lang == "en" else f"خطأ غير معروف: {error_key}"
    
    msg = ERROR_MESSAGES[error_key]
    text = msg.get(lang)
    
    try:
        return text.format(**kwargs)
    except KeyError:
        return text

def get_suggestion(error_key: str, lang: str = "ar", **kwargs) -> Optional[str]:
    """Get suggestion for fixing the error."""
    if error_key not in ERROR_MESSAGES:
        return None
    
    msg = ERROR_MESSAGES[error_key]
    suggestion = msg.get_suggestion(lang)
    
    if suggestion:
        try:
            return suggestion.format(**kwargs)
        except KeyError:
            return suggestion
    return None

def suggest_similar_name(name: str, available_names: List[str]) -> Optional[str]:
    """Suggest similar variable/function name."""
    # Check common typos first
    if name.lower() in COMMON_TYPOS:
        return COMMON_TYPOS[name.lower()][0]
    
    # Simple Levenshtein-like similarity
    def similarity(a: str, b: str) -> float:
        if len(a) == 0 or len(b) == 0:
            return 0.0
        matches = sum(1 for i, c in enumerate(a) if i < len(b) and b[i] == c)
        return matches / max(len(a), len(b))
    
    best_match = None
    best_score = 0.6  # Minimum threshold
    
    for available in available_names:
        score = similarity(name.lower(), available.lower())
        if score > best_score:
            best_score = score
            best_match = available
    
    return best_match

def format_error_with_context(
    error_msg: str,
    source_code: str,
    line: int,
    column: int = 0,
    context_lines: int = 2,
    lang: str = "ar"
) -> str:
    """
    Format error message with source code context.
    
    Args:
        error_msg: The error message
        source_code: Full source code
        line: Error line number (1-indexed)
        column: Error column (1-indexed)
        context_lines: Number of context lines before/after
        lang: Language for labels
    
    Returns:
        Formatted error with context
    """
    lines = source_code.split('\n')
    
    # Build context
    start = max(0, line - context_lines - 1)
    end = min(len(lines), line + context_lines)
    
    result = [error_msg, ""]
    
    for i in range(start, end):
        line_num = i + 1
        prefix = "→ " if line_num == line else "  "
        result.append(f"{prefix}{line_num:4d} | {lines[i]}")
        
        # Add column indicator
        if line_num == line and column > 0:
            indicator = " " * (7 + column) + "^"
            result.append(indicator)
    
    return "\n".join(result)

class BayanError(Exception):
    """Enhanced Bayan error with bilingual support."""
    
    def __init__(
        self,
        error_key: str,
        lang: str = "ar",
        line: int = 0,
        column: int = 0,
        source_code: str = "",
        **kwargs
    ):
        self.error_key = error_key
        self.lang = lang
        self.line = line
        self.column = column
        self.source_code = source_code
        self.kwargs = kwargs
        
        message = get_error_message(error_key, lang, **kwargs)
        suggestion = get_suggestion(error_key, lang, **kwargs)
        
        if source_code and line > 0:
            message = format_error_with_context(
                message, source_code, line, column, lang=lang
            )
        
        if suggestion:
            hint_label = "💡 اقتراح:" if lang == "ar" else "💡 Suggestion:"
            message = f"{message}\n{hint_label} {suggestion}"
        
        super().__init__(message)

