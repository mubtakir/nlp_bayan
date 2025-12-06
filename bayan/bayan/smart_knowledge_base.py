# -*- coding: utf-8 -*-
"""
قاعدة المعرفة الذكية (Smart Knowledge Base)
===========================================

قاعدة معرفة متطورة تجمع بين:
1. القواعد اليدوية (دقة عالية)
2. معجم الراموز (تغطية واسعة - 40,000+ كلمة)
3. سيميائية الحروف (استنباط لا نهائي للمعاني)

The Smart Knowledge Base integrates:
1. Manual Rules (High Precision)
2. Arramooz Dictionary (Broad Coverage)
3. Letter Semiotics (Infinite Inference)
"""

from typing import List, Dict, Any, Optional
from .linguistic_equation import KnowledgeBase, EntityState, EventType
from .unified_lexicon_system import UnifiedLexiconSystem
from .foundation_vocabulary import FoundationCategory
# Import Letter Semiotics components lazily to avoid circular imports if possible, 
# or import here if structure allows.
try:
    from .letter_semiotics import WordAnalyzer
except ImportError as e:
    print(f"⚠️ فشل استيراد WordAnalyzer: {e}")
    WordAnalyzer = None

class SmartKnowledgeBase(KnowledgeBase):
    """
    قاعدة معرفة ذكية تستخدم مصادر متعددة لاستنتاج نتائج الأحداث.
    Smart Knowledge Base using multiple sources to infer event results.
    """
    
    def __init__(self):
        super().__init__()
        print("🧠 جاري تهيئة قاعدة المعرفة الذكية...")
        
        # 1. تهيئة النظام المعجمي الموحد (الراموز)
        self.lexicon_system = UnifiedLexiconSystem()
        self.lexicon_system.initialize()
        
        # 2. تهيئة محلل سيميائية الحروف
        self.word_analyzer = WordAnalyzer(use_camel=False) if WordAnalyzer else None
        
        # 3. تحميل القواعد اليدوية (من الأب)
        # تم تحميلها تلقائياً عبر super().__init__()
        
    def infer_results(self, event: str, subject: Optional[str] = None, 
                     obj: Optional[str] = None) -> List[EntityState]:
        """
        استنتاج النتائج باستخدام الهرمية الذكية:
        1. القواعد اليدوية
        2. معجم الراموز
        3. سيميائية الحروف
        """
        results = []
        
        # ---------------------------------------------------------
        # المستوى 1: القواعد اليدوية (Manual Rules)
        # ---------------------------------------------------------
        if event in self.event_outcomes:
            print(f"   🎯 تم العثور على '{event}' في القواعد اليدوية.")
            return super().infer_results(event, subject, obj)
            
        # ---------------------------------------------------------
        # المستوى 2: معجم الراموز (Arramooz Dictionary)
        # ---------------------------------------------------------
        print(f"   🔍 البحث عن '{event}' في معجم الراموز...")
        lexicon_result = self.lexicon_system.lookup(event)
        
        if lexicon_result:
            print(f"   ℹ️ المصدر: {lexicon_result.source} | الأولوية: {lexicon_result.priority}")
            root = lexicon_result.word.root_word
            print(f"   ✅ تم العثور على '{event}' في الراموز (الجذر: {root}).")
            
            # محاولة استنتاج النتائج بناءً على فئة الجذر في القاموس التأسيسي
            foundation_word = self.lexicon_system.foundation_vocab.get_word(root) if root else None
            
            if foundation_word:
                category = foundation_word.category
                print(f"   🏷️ الفئة الدلالية: {category.value}")
                
                # تطبيق تأثيرات عامة بناءً على الفئة
                results = self._apply_category_effects(category, subject, obj)
                if results:
                    return results
            
            # إذا لم نجد فئة، نستخدم التعدي/اللزوم (Transitivity)
            # (يمكن إضافتها لاحقاً إذا توفرت بيانات التعدي في النتيجة)
            
        # ---------------------------------------------------------
        # المستوى 3: سيميائية الحروف (Letter Semiotics)
        # ---------------------------------------------------------
        if self.word_analyzer:
            print(f"   🔮 استنباط معنى '{event}' عبر سيميائية الحروف...")
            analysis = self.word_analyzer.analyze_word(event)
            
            if analysis:
                print(f"   ✨ الطاقة: {analysis.physical_score:.2f} (مادي) | {analysis.emotional_score:.2f} (نفسي)")
                results = self._infer_from_semiotics(analysis, subject, obj)
                if results:
                    return results
        
        # إذا فشل كل شيء
        print(f"   ⚠️ لم يتم استنتاج نتائج دقيقة للفعل '{event}'")
        return []

    def _apply_category_effects(self, category: FoundationCategory, 
                              subject: Optional[str], obj: Optional[str]) -> List[EntityState]:
        """تطبيق تأثيرات عامة بناءً على الفئة الدلالية"""
        results = []
        
        if category == FoundationCategory.BASIC_ACTIONS:
            # أفعال أساسية (أكل، شرب، نام...)
            if subject:
                results.append(EntityState(subject, {"طاقة": +0.2, "تعب": -0.1}, "قام بفعل أساسي"))
            if obj:
                results.append(EntityState(obj, {"تأثر": True}, "تأثر بالفعل"))
                
        elif category == FoundationCategory.PSYCHOLOGICAL:
            # أفعال نفسية (فرح، حزن، فكر...)
            if subject:
                results.append(EntityState(subject, {"شعور": "نشط", "تفكير": +0.5}, "تأثر نفسياً"))
                
        elif category == FoundationCategory.SOCIAL:
            # أفعال اجتماعية (تحدث، ساعد...)
            if subject:
                results.append(EntityState(subject, {"تواصل": +1.0}, "تفاعل اجتماعياً"))
            if obj:
                results.append(EntityState(obj, {"تواصل": +1.0}, "تم التواصل معه"))
                
        elif category == FoundationCategory.PHYSICAL:
             # أفعال فيزيائية (حركة، نقل...)
            if subject:
                results.append(EntityState(subject, {"حركة": True, "تعب": +0.1}, "تحرك فيزيائياً"))
            if obj:
                results.append(EntityState(obj, {"مكان": "تغير"}, "تغير مكانه"))
                
        return results

    def _infer_from_semiotics(self, analysis: Any, subject: Optional[str], obj: Optional[str]) -> List[EntityState]:
        """استنتاج النتائج من تحليل سيميائية الحروف"""
        results = []
        
        # 1. تحديد الطابع الغالب (مادي أم نفسي)
        is_physical = analysis.physical_score > analysis.emotional_score
        intensity = max(analysis.physical_score, analysis.emotional_score) / 10.0  # تطبيع 0-1
        
        # 2. تأثيرات الفاعل
        if subject:
            changes = {}
            if is_physical:
                changes["جهد_بدني"] = round(intensity * 0.5, 2)
                changes["طاقة"] = round(-intensity * 0.2, 2)
            else:
                changes["جهد_ذهني"] = round(intensity * 0.5, 2)
                changes["شعور"] = round(intensity * 0.3, 2)
            
            results.append(EntityState(subject, changes, "تأثير استنباطي (سيميائي)"))
            
        # 3. تأثيرات المفعول به (إذا كانت الطاقة عالية)
        if obj and intensity > 0.3:
            changes = {}
            if is_physical:
                changes["تأثر_مادي"] = round(intensity * 0.8, 2)
                changes["حالة"] = "تغيرت"
            else:
                changes["تأثر_نفسي"] = round(intensity * 0.6, 2)
                
            results.append(EntityState(obj, changes, "تأثير استنباطي (سيميائي)"))
            
        return results
