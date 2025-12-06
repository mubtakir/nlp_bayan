#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🤖 المساعد الذكي للبرمجة - AI Code Assistant
مساعد ذكي يساعد في كتابة الكود وإصلاح الأخطاء واقتراح التحسينات

المميزات:
- إكمال الكود الذكي
- شرح الأخطاء بالعربية
- اقتراح تحسينات الأداء والقراءة
- تحليل الكود وفهمه
- توليد الكود من وصف طبيعي
"""

import re
import ast
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

# ==================== الثوابت والإعدادات ====================

class CodeLanguage(Enum):
    """لغات البرمجة المدعومة"""
    BAYAN = "bayan"
    PYTHON = "python"
    HYBRID = "hybrid"

class SuggestionType(Enum):
    """أنواع الاقتراحات"""
    COMPLETION = "completion"
    ERROR_FIX = "error_fix"
    OPTIMIZATION = "optimization"
    REFACTORING = "refactoring"
    DOCUMENTATION = "documentation"

@dataclass
class CodeSuggestion:
    """اقتراح كود"""
    text: str
    suggestion_type: SuggestionType
    confidence: float
    description_ar: str
    description_en: str
    priority: int = 1

@dataclass
class CodeAnalysis:
    """نتيجة تحليل الكود"""
    language: CodeLanguage
    lines_count: int
    functions_count: int
    classes_count: int
    imports_count: int
    complexity_score: float
    issues: List[Dict[str, Any]] = field(default_factory=list)
    suggestions: List[CodeSuggestion] = field(default_factory=list)

@dataclass
class ErrorExplanation:
    """شرح الخطأ"""
    error_type: str
    error_message: str
    explanation_ar: str
    explanation_en: str
    fix_suggestion: str
    example_fix: str
    related_concepts: List[str] = field(default_factory=list)

# ==================== قاعدة معرفة الأخطاء ====================

ERROR_PATTERNS = {
    # أخطاء Python الشائعة
    r"NameError: name '(\w+)' is not defined": {
        "type": "NameError",
        "ar": "المتغير '{0}' غير معرّف. تأكد من تعريفه قبل استخدامه.",
        "en": "Variable '{0}' is not defined. Make sure to define it before use.",
        "fix": "قم بتعريف المتغير أولاً: {0} = قيمة",
        "concepts": ["المتغيرات", "نطاق المتغيرات"]
    },
    r"SyntaxError: invalid syntax": {
        "type": "SyntaxError",
        "ar": "خطأ في بناء الجملة. تحقق من الأقواس والنقطتين والمسافات.",
        "en": "Invalid syntax. Check parentheses, colons, and indentation.",
        "fix": "راجع الأقواس والنقطتين وتأكد من التنسيق الصحيح",
        "concepts": ["بناء الجملة", "الأقواس", "التنسيق"]
    },
    r"IndentationError: (.+)": {
        "type": "IndentationError",
        "ar": "خطأ في المسافات البادئة. استخدم 4 مسافات أو tab واحد بشكل متسق.",
        "en": "Indentation error. Use 4 spaces or 1 tab consistently.",
        "fix": "استخدم مسافات متساوية (4 مسافات لكل مستوى)",
        "concepts": ["المسافات البادئة", "هيكل الكود"]
    },
    r"TypeError: (.+)": {
        "type": "TypeError",
        "ar": "خطأ في نوع البيانات: {0}",
        "en": "Type error: {0}",
        "fix": "تحقق من توافق أنواع البيانات",
        "concepts": ["أنواع البيانات", "التحويل بين الأنواع"]
    },
    r"IndexError: (.+)": {
        "type": "IndexError",
        "ar": "خطأ في الفهرس: تحاول الوصول لعنصر خارج نطاق القائمة.",
        "en": "Index error: Trying to access element outside list range.",
        "fix": "تأكد من أن الفهرس أقل من طول القائمة",
        "concepts": ["القوائم", "الفهرسة"]
    },
    r"KeyError: (.+)": {
        "type": "KeyError",
        "ar": "المفتاح '{0}' غير موجود في القاموس.",
        "en": "Key '{0}' not found in dictionary.",
        "fix": "استخدم .get() للتحقق من وجود المفتاح أولاً",
        "concepts": ["القواميس", "المفاتيح"]
    },
    r"AttributeError: '(\w+)' object has no attribute '(\w+)'": {
        "type": "AttributeError",
        "ar": "الكائن من نوع '{0}' لا يملك الخاصية '{1}'.",
        "en": "Object of type '{0}' has no attribute '{1}'.",
        "fix": "تحقق من اسم الخاصية أو الدالة",
        "concepts": ["الكائنات", "الخصائص", "الدوال"]
    },
    r"ZeroDivisionError": {
        "type": "ZeroDivisionError",
        "ar": "لا يمكن القسمة على صفر!",
        "en": "Cannot divide by zero!",
        "fix": "تحقق من أن المقسوم عليه ليس صفراً قبل القسمة",
        "concepts": ["العمليات الحسابية", "معالجة الأخطاء"]
    },
    r"ImportError: No module named '(\w+)'": {
        "type": "ImportError",
        "ar": "المكتبة '{0}' غير موجودة. قم بتثبيتها أولاً.",
        "en": "Module '{0}' not found. Install it first.",
        "fix": "قم بتثبيت المكتبة: pip install {0}",
        "concepts": ["المكتبات", "الاستيراد"]
    },
    r"FileNotFoundError: (.+)": {
        "type": "FileNotFoundError",
        "ar": "الملف غير موجود. تحقق من المسار.",
        "en": "File not found. Check the path.",
        "fix": "تأكد من وجود الملف والمسار الصحيح",
        "concepts": ["الملفات", "المسارات"]
    }
}

# ==================== قوالب الكود ====================

CODE_TEMPLATES = {
    # قوالب بيان
    "دالة": '''def {name}({params}):
    """{description}"""
{body}
    return {return_value}
''',
    "صنف": '''class {name}:
    """{description}"""

    def __init__(self{params}):
        {init_body}

    def {method_name}(self):
        {method_body}
''',
    "حلقة": '''for {var} in {iterable}:
    {body}
''',
    "شرط": '''if {condition}:
    {if_body}
else:
    {else_body}
''',
    "محاولة": '''try:
    {try_body}
except {exception} as e:
    print(f"خطأ: {{e}}")
''',
    "hybrid": '''hybrid {{
    # الكود الهجين
    {body}
}}
''',
    "منطق": '''hybrid {{
    # حقائق
    fact {fact_name}({args}).

    # قواعد
    rule {rule_name}({rule_args}) :- {conditions}.

    # استعلام
    query {query}
}}
'''
}

# ==================== إكمالات الكود ====================

CODE_COMPLETIONS = {
    "def ": [
        ("def {name}():\n    pass", "دالة بسيطة"),
        ("def {name}(self):\n    pass", "دالة داخل صنف"),
        ("def {name}(*args, **kwargs):\n    pass", "دالة مع معاملات متغيرة"),
    ],
    "class ": [
        ("class {name}:\n    def __init__(self):\n        pass", "صنف بسيط"),
        ("class {name}(BaseClass):\n    def __init__(self):\n        super().__init__()", "صنف يرث"),
    ],
    "for ": [
        ("for i in range({n}):\n    ", "حلقة عددية"),
        ("for item in {list}:\n    ", "حلقة على قائمة"),
        ("for key, value in {dict}.items():\n    ", "حلقة على قاموس"),
    ],
    "if ": [
        ("if {condition}:\n    ", "شرط بسيط"),
        ("if {condition}:\n    \nelse:\n    ", "شرط مع بديل"),
        ("if {condition}:\n    \nelif {condition2}:\n    \nelse:\n    ", "شروط متعددة"),
    ],
    "try": [
        ("try:\n    \nexcept Exception as e:\n    print(e)", "معالجة خطأ بسيطة"),
        ("try:\n    \nexcept Exception as e:\n    \nfinally:\n    ", "معالجة مع finally"),
    ],
    "print": [
        ('print("{message}")', "طباعة نص"),
        ('print(f"{var}={{{var}}}")', "طباعة متغير"),
        ('print("{}", end="")', "طباعة بدون سطر جديد"),
    ],
    "import": [
        ("import {module}", "استيراد مكتبة"),
        ("from {module} import {item}", "استيراد عنصر محدد"),
        ("import {module} as {alias}", "استيراد مع اسم مختصر"),
    ],
    "hybrid": [
        ("hybrid {\n    \n}", "كتلة هجينة"),
        ("hybrid {\n    fact {name}({args}).\n}", "حقيقة منطقية"),
        ("hybrid {\n    rule {name}({args}) :- {body}.\n}", "قاعدة منطقية"),
    ],
    "with": [
        ('with open("{file}", "r") as f:\n    content = f.read()', "قراءة ملف"),
        ('with open("{file}", "w") as f:\n    f.write({content})', "كتابة ملف"),
    ],
    "lambda": [
        ("lambda x: x", "دالة مجهولة بسيطة"),
        ("lambda x, y: x + y", "دالة مجهولة مع معاملين"),
    ],
    "list": [
        ("[{expr} for {var} in {iterable}]", "list comprehension"),
        ("[{expr} for {var} in {iterable} if {condition}]", "list comprehension مع شرط"),
    ],
    "dict": [
        ("{{key: value for key, value in {items}}}", "dict comprehension"),
    ]
}

# ==================== الصنف الرئيسي ====================

class AICodeAssistant:
    """
    🤖 المساعد الذكي للبرمجة

    يوفر:
    - إكمال الكود الذكي
    - شرح الأخطاء بالعربية
    - اقتراح تحسينات
    - تحليل الكود
    - توليد الكود من وصف
    """

    def __init__(self, language: str = "ar"):
        self.language = language  # ar أو en
        self.history: List[Dict] = []
        self.learning_data: Dict[str, int] = {}  # تتبع الاستخدام للتعلم

    # ==================== إكمال الكود ====================

    def suggest_completion(self, partial_code: str, cursor_position: int = -1) -> List[CodeSuggestion]:
        """
        اقتراح إكمال للكود

        Args:
            partial_code: الكود الجزئي
            cursor_position: موقع المؤشر

        Returns:
            قائمة باقتراحات الإكمال
        """
        suggestions = []

        # الحصول على السطر الحالي
        lines = partial_code.split('\n')
        current_line = lines[-1] if lines else ""
        current_line_stripped = current_line.strip()

        # البحث عن إكمالات مطابقة
        for prefix, completions in CODE_COMPLETIONS.items():
            if current_line_stripped.startswith(prefix) or current_line_stripped == prefix.strip():
                for template, desc in completions:
                    suggestions.append(CodeSuggestion(
                        text=template,
                        suggestion_type=SuggestionType.COMPLETION,
                        confidence=0.9,
                        description_ar=desc,
                        description_en=desc,
                        priority=1
                    ))

        # اقتراحات سياقية
        context_suggestions = self._get_context_suggestions(partial_code, current_line)
        suggestions.extend(context_suggestions)

        # ترتيب حسب الأولوية والثقة
        suggestions.sort(key=lambda s: (-s.priority, -s.confidence))

        return suggestions[:10]  # أعلى 10 اقتراحات

    def _get_context_suggestions(self, code: str, current_line: str) -> List[CodeSuggestion]:
        """اقتراحات سياقية بناءً على الكود"""
        suggestions = []

        # إذا كان داخل صنف، اقترح دوال
        if "class " in code and current_line.strip() == "":
            suggestions.append(CodeSuggestion(
                text="    def method(self):\n        pass",
                suggestion_type=SuggestionType.COMPLETION,
                confidence=0.8,
                description_ar="إضافة دالة للصنف",
                description_en="Add method to class",
                priority=2
            ))

        # إذا كان بعد try، اقترح except
        if "try:" in code and "except" not in code:
            suggestions.append(CodeSuggestion(
                text="except Exception as e:\n    print(f'خطأ: {e}')",
                suggestion_type=SuggestionType.COMPLETION,
                confidence=0.95,
                description_ar="إضافة معالجة الخطأ",
                description_en="Add error handling",
                priority=3
            ))

        return suggestions

    # ==================== شرح الأخطاء ====================

    def explain_error(self, error_message: str, code_context: str = "") -> ErrorExplanation:
        """
        شرح الخطأ بطريقة مفهومة

        Args:
            error_message: رسالة الخطأ
            code_context: سياق الكود (اختياري)

        Returns:
            شرح مفصل للخطأ
        """
        # البحث عن نمط مطابق
        for pattern, info in ERROR_PATTERNS.items():
            match = re.search(pattern, error_message)
            if match:
                groups = match.groups()

                # تنسيق الرسائل مع المتغيرات
                ar_msg = info["ar"].format(*groups) if groups else info["ar"]
                en_msg = info["en"].format(*groups) if groups else info["en"]
                fix_msg = info["fix"].format(*groups) if groups else info["fix"]

                # إنشاء مثال للإصلاح
                example_fix = self._generate_fix_example(info["type"], groups, code_context)

                return ErrorExplanation(
                    error_type=info["type"],
                    error_message=error_message,
                    explanation_ar=ar_msg,
                    explanation_en=en_msg,
                    fix_suggestion=fix_msg,
                    example_fix=example_fix,
                    related_concepts=info.get("concepts", [])
                )

        # خطأ غير معروف
        return ErrorExplanation(
            error_type="Unknown",
            error_message=error_message,
            explanation_ar="خطأ غير معروف. راجع رسالة الخطأ الأصلية.",
            explanation_en="Unknown error. Check the original error message.",
            fix_suggestion="راجع الوثائق أو ابحث عن الخطأ",
            example_fix="",
            related_concepts=["معالجة الأخطاء"]
        )

    def _generate_fix_example(self, error_type: str, groups: tuple, code_context: str) -> str:
        """توليد مثال للإصلاح"""
        if error_type == "NameError" and groups:
            var_name = groups[0]
            return f'{var_name} = None  # أو القيمة المناسبة\n# ثم استخدم {var_name}'
        elif error_type == "IndentationError":
            return "# استخدم 4 مسافات لكل مستوى:\nif condition:\n    statement  # ← 4 مسافات"
        elif error_type == "ZeroDivisionError":
            return "if divisor != 0:\n    result = number / divisor\nelse:\n    result = 0  # أو معالجة أخرى"
        elif error_type == "KeyError" and groups:
            key = groups[0]
            return f'# استخدم get للتحقق:\nvalue = my_dict.get({key}, default_value)'
        return ""

    # ==================== اقتراح التحسينات ====================

    def suggest_optimization(self, code: str) -> List[CodeSuggestion]:
        """
        اقتراح تحسينات للكود

        Args:
            code: الكود المراد تحسينه

        Returns:
            قائمة باقتراحات التحسين
        """
        suggestions = []

        # 1. تحسين الحلقات
        if "for i in range(len(" in code:
            suggestions.append(CodeSuggestion(
                text="استخدم enumerate() بدلاً من range(len())",
                suggestion_type=SuggestionType.OPTIMIZATION,
                confidence=0.95,
                description_ar="enumerate أسرع وأوضح: for i, item in enumerate(list)",
                description_en="enumerate is faster and clearer",
                priority=2
            ))

        # 2. استخدام list comprehension
        if re.search(r'for .+ in .+:\s*\n\s+\w+\.append\(', code):
            suggestions.append(CodeSuggestion(
                text="استخدم List Comprehension",
                suggestion_type=SuggestionType.OPTIMIZATION,
                confidence=0.9,
                description_ar="List comprehension أسرع: [x for x in items]",
                description_en="List comprehension is faster",
                priority=2
            ))

        # 3. تحسين التعامل مع الملفات
        if "open(" in code and "with " not in code:
            suggestions.append(CodeSuggestion(
                text="استخدم with للتعامل مع الملفات",
                suggestion_type=SuggestionType.OPTIMIZATION,
                confidence=0.98,
                description_ar="with يضمن إغلاق الملف تلقائياً",
                description_en="with ensures file is closed automatically",
                priority=3
            ))

        # 4. تحسين الشروط
        if "== True" in code or "== False" in code:
            suggestions.append(CodeSuggestion(
                text="لا حاجة للمقارنة مع True/False",
                suggestion_type=SuggestionType.OPTIMIZATION,
                confidence=0.9,
                description_ar="استخدم if condition: بدلاً من if condition == True:",
                description_en="Use if condition: instead of if condition == True:",
                priority=1
            ))

        # 5. تحسين السلاسل النصية
        if re.search(r'"\s*\+\s*str\(', code) or re.search(r"'\s*\+\s*str\(", code):
            suggestions.append(CodeSuggestion(
                text="استخدم f-strings",
                suggestion_type=SuggestionType.OPTIMIZATION,
                confidence=0.9,
                description_ar="f-strings أسرع وأوضح: f'{variable}'",
                description_en="f-strings are faster and clearer",
                priority=2
            ))

        # 6. تجنب المتغيرات العامة
        if re.search(r'^[a-zA-Z_]\w*\s*=', code, re.MULTILINE) and "def " in code:
            if code.index("=") < code.index("def "):
                suggestions.append(CodeSuggestion(
                    text="تجنب المتغيرات العامة",
                    suggestion_type=SuggestionType.REFACTORING,
                    confidence=0.7,
                    description_ar="استخدم المتغيرات داخل الدوال أو الأصناف",
                    description_en="Use variables inside functions or classes",
                    priority=1
                ))

        # 7. إضافة توثيق
        if "def " in code and '"""' not in code and "'''" not in code:
            suggestions.append(CodeSuggestion(
                text="أضف توثيقاً للدوال",
                suggestion_type=SuggestionType.DOCUMENTATION,
                confidence=0.85,
                description_ar='أضف docstring: def func():\n    """وصف الدالة"""',
                description_en="Add docstring to functions",
                priority=1
            ))

        return suggestions

    # ==================== تحليل الكود ====================

    def analyze_code(self, code: str) -> CodeAnalysis:
        """
        تحليل الكود وفهمه

        Args:
            code: الكود المراد تحليله

        Returns:
            نتيجة التحليل
        """
        # تحديد اللغة
        language = self._detect_language(code)

        # إحصائيات أساسية
        lines = code.split('\n')
        lines_count = len(lines)

        # عد العناصر
        functions_count = len(re.findall(r'\bdef\s+\w+', code))
        classes_count = len(re.findall(r'\bclass\s+\w+', code))
        imports_count = len(re.findall(r'\b(import|from)\s+', code))

        # حساب التعقيد
        complexity_score = self._calculate_complexity(code)

        # جمع المشاكل
        issues = self._find_issues(code)

        # جمع الاقتراحات
        suggestions = self.suggest_optimization(code)

        return CodeAnalysis(
            language=language,
            lines_count=lines_count,
            functions_count=functions_count,
            classes_count=classes_count,
            imports_count=imports_count,
            complexity_score=complexity_score,
            issues=issues,
            suggestions=suggestions
        )

    def _detect_language(self, code: str) -> CodeLanguage:
        """تحديد لغة الكود"""
        if "hybrid {" in code or "hybrid{" in code:
            return CodeLanguage.HYBRID
        elif "fact " in code or "rule " in code or "query " in code:
            return CodeLanguage.BAYAN
        return CodeLanguage.PYTHON

    def _calculate_complexity(self, code: str) -> float:
        """حساب تعقيد الكود (مبسط)"""
        complexity = 1.0

        # زيادة التعقيد بناءً على العناصر
        complexity += len(re.findall(r'\bif\b', code)) * 0.1
        complexity += len(re.findall(r'\bfor\b', code)) * 0.15
        complexity += len(re.findall(r'\bwhile\b', code)) * 0.15
        complexity += len(re.findall(r'\btry\b', code)) * 0.1
        complexity += len(re.findall(r'\bdef\b', code)) * 0.05
        complexity += len(re.findall(r'\bclass\b', code)) * 0.1

        # التعقيد المتداخل
        max_indent = max([len(line) - len(line.lstrip()) for line in code.split('\n') if line.strip()], default=0)
        complexity += max_indent * 0.02

        return min(complexity, 10.0)  # حد أقصى 10

    def _find_issues(self, code: str) -> List[Dict[str, Any]]:
        """البحث عن مشاكل في الكود"""
        issues = []
        lines = code.split('\n')

        for i, line in enumerate(lines, 1):
            # سطر طويل جداً
            if len(line) > 120:
                issues.append({
                    "line": i,
                    "type": "style",
                    "message_ar": "السطر طويل جداً (أكثر من 120 حرف)",
                    "message_en": "Line too long (>120 chars)"
                })

            # TODO غير مكتمل
            if "TODO" in line or "FIXME" in line:
                issues.append({
                    "line": i,
                    "type": "todo",
                    "message_ar": "يوجد عمل غير مكتمل",
                    "message_en": "Incomplete work"
                })

            # print للتصحيح
            if "print(" in line and "#" not in line.split("print")[0]:
                issues.append({
                    "line": i,
                    "type": "debug",
                    "message_ar": "تأكد من إزالة print للتصحيح",
                    "message_en": "Consider removing debug print"
                })

        return issues

    # ==================== توليد الكود ====================

    def generate_code(self, description: str, template_type: str = None) -> str:
        """
        توليد كود من وصف طبيعي

        Args:
            description: وصف ما تريد إنشاءه
            template_type: نوع القالب (اختياري)

        Returns:
            الكود المولّد
        """
        description_lower = description.lower()

        # تحديد نوع القالب من الوصف
        if template_type is None:
            if any(w in description_lower for w in ["دالة", "function", "def"]):
                template_type = "دالة"
            elif any(w in description_lower for w in ["صنف", "class", "كلاس"]):
                template_type = "صنف"
            elif any(w in description_lower for w in ["حلقة", "loop", "for"]):
                template_type = "حلقة"
            elif any(w in description_lower for w in ["شرط", "if", "إذا"]):
                template_type = "شرط"
            elif any(w in description_lower for w in ["hybrid", "هجين", "منطق"]):
                template_type = "hybrid"
            elif any(w in description_lower for w in ["fact", "rule", "حقيقة", "قاعدة"]):
                template_type = "منطق"

        # الحصول على القالب
        if template_type and template_type in CODE_TEMPLATES:
            template = CODE_TEMPLATES[template_type]

            # استخراج الأسماء من الوصف
            name = self._extract_name(description) or "my_function"

            # ملء القالب
            code = template.format(
                name=name,
                params="",
                description=description,
                body="    pass  # أضف الكود هنا",
                return_value="None",
                init_body="pass",
                method_name="do_something",
                method_body="pass",
                var="item",
                iterable="items",
                condition="True",
                if_body="pass",
                else_body="pass",
                try_body="pass",
                exception="Exception",
                fact_name="my_fact",
                args="X",
                rule_name="my_rule",
                rule_args="X",
                conditions="condition(X)",
                query="my_fact(?X)"
            )

            return code

        # توليد عام
        return self._generate_from_description(description)

    def _extract_name(self, description: str) -> Optional[str]:
        """استخراج اسم من الوصف"""
        # البحث عن اسم بين علامات اقتباس
        match = re.search(r'["\'](\w+)["\']', description)
        if match:
            return match.group(1)

        # البحث عن اسم بعد "اسمه" أو "called"
        match = re.search(r'(?:اسم[هـ]ا?|called|named)\s+(\w+)', description)
        if match:
            return match.group(1)

        return None

    def _generate_from_description(self, description: str) -> str:
        """توليد كود من وصف عام"""
        lines = []
        lines.append(f'# {description}')
        lines.append('')

        # تحليل الوصف وتوليد كود مناسب
        desc_lower = description.lower()

        if "جمع" in desc_lower or "sum" in desc_lower or "مجموع" in desc_lower:
            lines.append('def calculate_sum(numbers):')
            lines.append('    """حساب المجموع"""')
            lines.append('    return sum(numbers)')
        elif "ضرب" in desc_lower or "multiply" in desc_lower:
            lines.append('def multiply(a, b):')
            lines.append('    """الضرب"""')
            lines.append('    return a * b')
        elif "قسمة" in desc_lower or "divide" in desc_lower:
            lines.append('def divide(a, b):')
            lines.append('    """القسمة مع معالجة القسمة على صفر"""')
            lines.append('    if b == 0:')
            lines.append('        raise ValueError("لا يمكن القسمة على صفر")')
            lines.append('    return a / b')
        elif "قراءة" in desc_lower or "read" in desc_lower or "ملف" in desc_lower:
            lines.append('def read_file(path):')
            lines.append('    """قراءة ملف"""')
            lines.append('    with open(path, "r", encoding="utf-8") as f:')
            lines.append('        return f.read()')
        elif "كتابة" in desc_lower or "write" in desc_lower:
            lines.append('def write_file(path, content):')
            lines.append('    """كتابة ملف"""')
            lines.append('    with open(path, "w", encoding="utf-8") as f:')
            lines.append('        f.write(content)')
        elif "ترتيب" in desc_lower or "sort" in desc_lower:
            lines.append('def sort_list(items, reverse=False):')
            lines.append('    """ترتيب قائمة"""')
            lines.append('    return sorted(items, reverse=reverse)')
        elif "بحث" in desc_lower or "search" in desc_lower or "find" in desc_lower:
            lines.append('def search(items, target):')
            lines.append('    """البحث عن عنصر في قائمة"""')
            lines.append('    for i, item in enumerate(items):')
            lines.append('        if item == target:')
            lines.append('            return i')
            lines.append('    return -1')
        elif "عكس" in desc_lower or "reverse" in desc_lower:
            lines.append('def reverse_list(items):')
            lines.append('    """عكس قائمة"""')
            lines.append('    return items[::-1]')
        elif "فلترة" in desc_lower or "filter" in desc_lower or "تصفية" in desc_lower:
            lines.append('def filter_items(items, condition):')
            lines.append('    """تصفية قائمة حسب شرط"""')
            lines.append('    return [item for item in items if condition(item)]')
        elif "عداد" in desc_lower or "count" in desc_lower or "إحصاء" in desc_lower:
            lines.append('def count_items(items):')
            lines.append('    """إحصاء العناصر"""')
            lines.append('    from collections import Counter')
            lines.append('    return dict(Counter(items))')
        elif "متوسط" in desc_lower or "average" in desc_lower or "mean" in desc_lower:
            lines.append('def calculate_average(numbers):')
            lines.append('    """حساب المتوسط"""')
            lines.append('    if not numbers:')
            lines.append('        return 0')
            lines.append('    return sum(numbers) / len(numbers)')
        elif "أكبر" in desc_lower or "max" in desc_lower or "أعلى" in desc_lower:
            lines.append('def find_max(numbers):')
            lines.append('    """إيجاد أكبر قيمة"""')
            lines.append('    return max(numbers) if numbers else None')
        elif "أصغر" in desc_lower or "min" in desc_lower or "أدنى" in desc_lower:
            lines.append('def find_min(numbers):')
            lines.append('    """إيجاد أصغر قيمة"""')
            lines.append('    return min(numbers) if numbers else None')
        else:
            lines.append('def my_function():')
            lines.append(f'    """{description}"""')
            lines.append('    # أضف الكود هنا')
            lines.append('    pass')

        return '\n'.join(lines)

    # ==================== واجهة تفاعلية ====================

    def chat(self, user_input: str) -> str:
        """
        محادثة مع المساعد

        Args:
            user_input: رسالة المستخدم

        Returns:
            رد المساعد
        """
        user_input_lower = user_input.lower()

        # تحديد نوع الطلب
        if any(w in user_input_lower for w in ["خطأ", "error", "مشكلة", "problem"]):
            # البحث عن رسالة خطأ في الإدخال
            explanation = self.explain_error(user_input)
            if self.language == "ar":
                return f"🔍 **شرح الخطأ:**\n{explanation.explanation_ar}\n\n💡 **الحل:**\n{explanation.fix_suggestion}\n\n📝 **مثال:**\n```python\n{explanation.example_fix}\n```"
            else:
                return f"🔍 **Error Explanation:**\n{explanation.explanation_en}\n\n💡 **Fix:**\n{explanation.fix_suggestion}\n\n📝 **Example:**\n```python\n{explanation.example_fix}\n```"

        elif any(w in user_input_lower for w in ["أنشئ", "اكتب", "create", "write", "generate"]):
            code = self.generate_code(user_input)
            return f"✨ **الكود المولّد:**\n```python\n{code}\n```"

        elif any(w in user_input_lower for w in ["حلل", "analyze", "تحليل"]):
            # البحث عن كود في الإدخال
            code_match = re.search(r'```(?:python)?\n?(.*?)\n?```', user_input, re.DOTALL)
            if code_match:
                code = code_match.group(1)
                analysis = self.analyze_code(code)
                return self._format_analysis(analysis)
            else:
                return "❓ أرسل الكود للتحليل داخل ``` ```"

        elif any(w in user_input_lower for w in ["حسّن", "optimize", "تحسين", "improve"]):
            code_match = re.search(r'```(?:python)?\n?(.*?)\n?```', user_input, re.DOTALL)
            if code_match:
                code = code_match.group(1)
                suggestions = self.suggest_optimization(code)
                return self._format_suggestions(suggestions)
            else:
                return "❓ أرسل الكود للتحسين داخل ``` ```"

        elif any(w in user_input_lower for w in ["أكمل", "complete", "إكمال"]):
            suggestions = self.suggest_completion(user_input)
            if suggestions:
                result = "💡 **اقتراحات الإكمال:**\n"
                for i, s in enumerate(suggestions[:5], 1):
                    result += f"\n{i}. {s.description_ar}\n```python\n{s.text}\n```\n"
                return result
            return "❓ لم أجد اقتراحات مناسبة"

        else:
            return """🤖 **المساعد الذكي للبرمجة**

أستطيع مساعدتك في:
• **شرح الأخطاء**: أرسل رسالة الخطأ
• **توليد كود**: قل "أنشئ دالة لـ..."
• **تحليل كود**: قل "حلل" مع الكود
• **تحسين كود**: قل "حسّن" مع الكود
• **إكمال كود**: قل "أكمل" مع بداية الكود

مثال: "أنشئ دالة لحساب مجموع قائمة أرقام"
"""

    def _format_analysis(self, analysis: CodeAnalysis) -> str:
        """تنسيق نتيجة التحليل"""
        result = f"""📊 **تحليل الكود:**

• **اللغة**: {analysis.language.value}
• **عدد الأسطر**: {analysis.lines_count}
• **الدوال**: {analysis.functions_count}
• **الأصناف**: {analysis.classes_count}
• **الاستيرادات**: {analysis.imports_count}
• **التعقيد**: {analysis.complexity_score:.1f}/10
"""

        if analysis.issues:
            result += "\n⚠️ **المشاكل:**\n"
            for issue in analysis.issues[:5]:
                msg = issue["message_ar"] if self.language == "ar" else issue["message_en"]
                result += f"• سطر {issue['line']}: {msg}\n"

        if analysis.suggestions:
            result += "\n💡 **اقتراحات:**\n"
            for s in analysis.suggestions[:3]:
                desc = s.description_ar if self.language == "ar" else s.description_en
                result += f"• {desc}\n"

        return result

    def _format_suggestions(self, suggestions: List[CodeSuggestion]) -> str:
        """تنسيق الاقتراحات"""
        if not suggestions:
            return "✅ الكود جيد! لا توجد اقتراحات للتحسين."

        result = "💡 **اقتراحات التحسين:**\n\n"
        for i, s in enumerate(suggestions, 1):
            desc = s.description_ar if self.language == "ar" else s.description_en
            result += f"{i}. **{s.text}**\n   {desc}\n\n"

        return result


# ==================== اختبار ====================

if __name__ == "__main__":
    print("=" * 60)
    print("🤖 اختبار المساعد الذكي للبرمجة")
    print("=" * 60)

    assistant = AICodeAssistant(language="ar")

    # اختبار 1: شرح خطأ
    print("\n📋 اختبار 1: شرح الأخطاء")
    print("-" * 40)
    error = "NameError: name 'x' is not defined"
    explanation = assistant.explain_error(error)
    print(f"الخطأ: {error}")
    print(f"الشرح: {explanation.explanation_ar}")
    print(f"الحل: {explanation.fix_suggestion}")

    # اختبار 2: إكمال الكود
    print("\n📋 اختبار 2: إكمال الكود")
    print("-" * 40)
    partial = "def "
    suggestions = assistant.suggest_completion(partial)
    print(f"الكود الجزئي: '{partial}'")
    print(f"الاقتراحات: {len(suggestions)}")
    for s in suggestions[:3]:
        print(f"  • {s.description_ar}")

    # اختبار 3: توليد كود
    print("\n📋 اختبار 3: توليد الكود")
    print("-" * 40)
    desc = "أنشئ دالة لحساب مجموع رقمين"
    code = assistant.generate_code(desc)
    print(f"الوصف: {desc}")
    print(f"الكود:\n{code}")

    # اختبار 4: تحليل كود
    print("\n📋 اختبار 4: تحليل الكود")
    print("-" * 40)
    sample_code = '''
def calculate(x, y):
    result = x + y
    print(result)
    return result

for i in range(len(items)):
    process(items[i])
'''
    analysis = assistant.analyze_code(sample_code)
    print(f"الأسطر: {analysis.lines_count}")
    print(f"الدوال: {analysis.functions_count}")
    print(f"التعقيد: {analysis.complexity_score:.1f}")
    print(f"الاقتراحات: {len(analysis.suggestions)}")
    for s in analysis.suggestions:
        print(f"  • {s.description_ar}")

    # اختبار 5: المحادثة
    print("\n📋 اختبار 5: المحادثة")
    print("-" * 40)
    response = assistant.chat("أنشئ دالة للقسمة مع معالجة القسمة على صفر")
    print(response)

    print("\n" + "=" * 60)
    print("✅ اكتمل الاختبار!")
    print("=" * 60)

