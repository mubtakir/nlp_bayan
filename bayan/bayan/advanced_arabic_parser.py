# -*- coding: utf-8 -*-
"""
المحلل النحوي العربي المتقدم (Advanced Arabic Parser)
=====================================================

يستخدم التعابير النمطية (Regex) لتحليل الجمل العربية المعقدة
واستخراج المكونات اللغوية بدقة أعلى من التقسيم البسيط.

الميزات:
- دعم الجمل الفعلية والاسمية
- استخراج حروف الجر والمجرور
- استخراج الظروف (الزمان والمكان)
- استخراج الصفات
- دعم الجمل الشرطية

المؤلف: باسل يحيى عبد الله
التاريخ: 2025-12-05
"""

import re
from typing import Dict, Any, Optional, List, Tuple
from .linguistic_equation import LinguisticEquation, Role, EventType, EntityState, KnowledgeBase

class AdvancedArabicParser:
    """
    محلل نحوي متقدم يعتمد على الأنماط (Patterns)
    """
    
    def __init__(self, knowledge_base: KnowledgeBase):
        self.kb = knowledge_base
        
        # تعريف الأنماط النحوية (Regex Patterns)
        # ملاحظة: \w+ في بايثون 3 تدعم الحروف العربية (Unicode)
        
        self.patterns = {
            # 1. الجملة الشرطية: إذا [شرط] فإن [نتيجة]
            # مثال: "إذا درس الطالب فإن الطالب ينجح"
            "conditional": r"إذا\s+(.+?)\s+فإن\s+(.+)",
            
            # 2. جملة مع حرف جر: فاعل + فعل + حرف جر + مفعول به
            # مثال: "محمد ذهب إلى المدرسة"
            "prepositional": r"(\w+)\s+(\w+)\s+(في|إلى|على|من|عن|بـ|لـ)\s+(\w+)",
            
            # 3. جملة مع ظرف زمان/مكان: فاعل + فعل + مفعول به + ظرف
            # مثال: "أحمد أكل التفاحة صباحاً"
            "adverbial": r"(\w+)\s+(\w+)\s+(\w+)\s+(صباحاً|مساءً|ليلاً|نهاراً|اليوم|غداً|أمس|هنا|هناك)",
            
            # 4. جملة مع صفة: فاعل + فعل + مفعول به + صفة
            # مثال: "الرجل ضرب الكرة الكبيرة"
            "descriptive": r"(\w+)\s+(\w+)\s+(\w+)\s+([\w\u0600-\u06FF]+)",
            
            # 5. جملة بسيطة (فاعل + فعل + مفعول به)
            # مثال: "محمد أكل تفاحة"
            "simple_svo": r"(\w+)\s+(\w+)\s+(\w+)",
            
            # 6. جملة بسيطة (فاعل + فعل)
            # مثال: "محمد نام"
            "simple_sv": r"(\w+)\s+(\w+)"
        }

    def parse(self, sentence: str) -> Optional[LinguisticEquation]:
        """
        تحليل الجملة واستخراج المعادلة اللغوية المناسبة.
        """
        sentence = sentence.strip()
        
        # 1. محاولة مطابقة الجمل الشرطية أولاً (لأنها الأعقد)
        match = re.match(self.patterns["conditional"], sentence)
        if match:
            return self._parse_conditional(match)
            
        # 2. محاولة مطابقة الجمل مع حروف الجر
        match = re.match(self.patterns["prepositional"], sentence)
        if match:
            return self._parse_prepositional(match)
            
        # 3. محاولة مطابقة الجمل الظرفية
        match = re.match(self.patterns["adverbial"], sentence)
        if match:
            return self._parse_adverbial(match)
            
        # 4. محاولة مطابقة الجمل الوصفية (الصفات)
        # نحتاج للتأكد أن الكلمة الأخيرة ليست ظرفاً أو حرف جر
        # هذا النمط عام جداً، لذا نضعه بعد الأنماط المحددة
        match = re.match(self.patterns["descriptive"], sentence)
        if match:
            # تحقق إضافي: هل الكلمة الأخيرة صفة محتملة؟
            # (يمكن تحسين هذا باستخدام قاموس الصفات)
            return self._parse_descriptive(match)
            
        # 5. الجمل البسيطة (SVO)
        match = re.match(self.patterns["simple_svo"], sentence)
        if match:
            return self._parse_simple_svo(match)
            
        # 6. الجمل البسيطة (SV)
        match = re.match(self.patterns["simple_sv"], sentence)
        if match:
            return self._parse_simple_sv(match)
            
        return None

    def _parse_conditional(self, match) -> LinguisticEquation:
        """تحليل الجملة الشرطية"""
        condition_part = match.group(1)  # "درس الطالب"
        result_part = match.group(2)     # "الطالب ينجح"
        
        # تحليل جزئي الشرط والنتيجة (يمكن أن يكونا جملاً بسيطة)
        # للتبسيط هنا، سنعتبرهما نصاً وصفياً
        
        return LinguisticEquation(
            entities={}, # كيانات مجردة في الشرط
            event="شرط",
            event_type=EventType.MENTAL_ACTION, # تصنيف مجازي
            condition=condition_part,
            results=[
                EntityState("النتيجة", {"تحقق": True}, f"بشرط: {condition_part}")
            ],
            source="advanced_parser_conditional"
        )

    def _parse_prepositional(self, match) -> LinguisticEquation:
        """تحليل جملة الجار والمجرور"""
        subject = match.group(1)
        event = match.group(2)
        prep = match.group(3)
        obj = match.group(4)
        
        entities = {
            subject: Role.SUBJECT,
            obj: Role.LOCATION if prep in ["إلى", "في"] else Role.OBJECT
        }
        
        # استنتاج النتائج
        results = self.kb.infer_results(event, subject, obj)
        
        # إضافة تأثير حرف الجر (يمكن توسيعه لاحقاً)
        if prep == "إلى":
            # تأكيد الانتقال
            pass
            
        return LinguisticEquation(
            entities=entities,
            event=event,
            event_type=self._infer_event_type(event),
            preposition=prep,
            results=results,
            source="advanced_parser_prepositional"
        )

    def _parse_adverbial(self, match) -> LinguisticEquation:
        """تحليل الجملة الظرفية"""
        subject = match.group(1)
        event = match.group(2)
        obj = match.group(3)
        adverb = match.group(4)
        
        entities = {
            subject: Role.SUBJECT,
            obj: Role.OBJECT
        }
        
        results = self.kb.infer_results(event, subject, obj)
        
        return LinguisticEquation(
            entities=entities,
            event=event,
            event_type=self._infer_event_type(event),
            time=adverb, # نفترض أنه ظرف زمان حالياً
            adverb=adverb,
            results=results,
            source="advanced_parser_adverbial"
        )

    def _parse_descriptive(self, match) -> LinguisticEquation:
        """تحليل الجملة الوصفية"""
        subject = match.group(1)
        event = match.group(2)
        obj = match.group(3)
        adjective = match.group(4)
        
        entities = {
            subject: Role.SUBJECT,
            obj: Role.OBJECT
        }
        
        results = self.kb.infer_results(event, subject, obj)
        
        return LinguisticEquation(
            entities=entities,
            event=event,
            event_type=self._infer_event_type(event),
            adjective=adjective,
            results=results,
            source="advanced_parser_descriptive"
        )

    def _parse_simple_svo(self, match) -> LinguisticEquation:
        """تحليل جملة فاعل فعل مفعول"""
        subject = match.group(1)
        event = match.group(2)
        obj = match.group(3)
        
        entities = {
            subject: Role.SUBJECT,
            obj: Role.OBJECT
        }
        
        results = self.kb.infer_results(event, subject, obj)
        
        return LinguisticEquation(
            entities=entities,
            event=event,
            event_type=self._infer_event_type(event),
            results=results,
            source="advanced_parser_simple"
        )

    def _parse_simple_sv(self, match) -> LinguisticEquation:
        """تحليل جملة فاعل فعل"""
        subject = match.group(1)
        event = match.group(2)
        
        entities = {
            subject: Role.SUBJECT
        }
        
        results = self.kb.infer_results(event, subject, None)
        
        return LinguisticEquation(
            entities=entities,
            event=event,
            event_type=self._infer_event_type(event),
            results=results,
            source="advanced_parser_simple"
        )

    def _infer_event_type(self, event: str) -> EventType:
        """
        (نسخة من الدالة الموجودة في LinguisticEquationParser)
        استنتاج نوع الحدث من اسمه.
        """
        # يمكن تحسين هذا باستخدام SmartKnowledgeBase لاحقاً
        physical_verbs = ["أكل", "ضرب", "كسر", "بنى", "شرب", "لعب"]
        mental_verbs = ["فكر", "تذكر", "نسي", "فهم", "درس"]
        communication_verbs = ["قال", "كتب", "سأل", "أجاب", "تحدث"]
        movement_verbs = ["ذهب", "جاء", "رجع", "ركض", "مشى", "سافر"]
        
        if event in physical_verbs:
            return EventType.PHYSICAL_ACTION
        elif event in mental_verbs:
            return EventType.MENTAL_ACTION
        elif event in communication_verbs:
            return EventType.COMMUNICATION
        elif event in movement_verbs:
            return EventType.MOVEMENT
        else:
            return EventType.PHYSICAL_ACTION  # افتراضي
