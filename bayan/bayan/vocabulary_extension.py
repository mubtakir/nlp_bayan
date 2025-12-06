# -*- coding: utf-8 -*-
"""
إضافة نظام المعجم الموحد للمفسر
Unified Lexicon Extension for Bayan Interpreter
================================================

هذا الملف يضيف دوال نظام المعجم الموحد للمفسر بدون تعديل المفسر الأصلي.
يدمج القاموس الأساسي (105 كلمة) + معجم الرموز (40,850 كلمة)

الاستخدام:
    from bayan.vocabulary_extension import register_vocabulary_functions
    register_vocabulary_functions(interpreter)

أو تلقائياً عند إنشاء المفسر:
    from bayan.vocabulary_extension import create_vocabulary_enhanced_interpreter
    interpreter = create_vocabulary_enhanced_interpreter()

المطور: مشروع لغة بيان
التاريخ: 2025-12-05
"""

from typing import Dict, Any, List, Optional


def register_vocabulary_functions(interpreter) -> bool:
    """
    تسجيل دوال نظام المعجم الموحد في المفسر
    
    Args:
        interpreter: المفسر (TraditionalInterpreter أو HybridInterpreter)
    
    Returns:
        True إذا نجح التسجيل، False إذا فشل
    """
    
    # ═══════════════════════════════════════════════════════════════
    # 1. الحصول على global_env
    # ═══════════════════════════════════════════════════════════════
    
    if hasattr(interpreter, 'global_env'):
        env = interpreter.global_env
    elif hasattr(interpreter, 'traditional') and hasattr(interpreter.traditional, 'global_env'):
        env = interpreter.traditional.global_env
    else:
        print("⚠️ تحذير: لا يمكن العثور على global_env في المفسر")
        return False
    
    # ═══════════════════════════════════════════════════════════════
    # 2. استيراد المكتبات المطلوبة
    # ═══════════════════════════════════════════════════════════════
    
    try:
        from .unified_lexicon_system import UnifiedLexiconSystem, PriorityLevel
        from .complete_vocabulary import get_complete_vocabulary
        from .foundation_vocabulary import FoundationWordType, FoundationCategory
    except ImportError as e:
        print(f"⚠️ تحذير: لم يتم تحميل نظام المعجم: {e}")
        return False
    
    # ═══════════════════════════════════════════════════════════════
    # 3. تهيئة كسولة (Lazy Initialization)
    # ═══════════════════════════════════════════════════════════════
    
    _cache = {}
    
    def _get_unified_lexicon():
        """الحصول على النظام الموحد (مع تهيئة كسولة)"""
        if 'lexicon' not in _cache:
            lexicon = UnifiedLexiconSystem()
            lexicon.initialize()
            _cache['lexicon'] = lexicon
        return _cache['lexicon']
    
    def _get_foundation_vocab():
        """الحصول على القاموس الأساسي"""
        if 'foundation' not in _cache:
            _cache['foundation'] = get_complete_vocabulary()
        return _cache['foundation']
    
    # ═══════════════════════════════════════════════════════════════
    # 4. دوال البحث في المعجم
    # ═══════════════════════════════════════════════════════════════
    
    def lookup_word(word: str) -> Dict[str, Any]:
        """
        البحث عن كلمة في المعجم الموحد
        Search for a word in the unified lexicon
        
        مثال: ابحث_كلمة("مدرسة")
        """
        lexicon = _get_unified_lexicon()
        result = lexicon.lookup(word)
        
        if result:
            return {
                'word': word,
                'الكلمة': word,
                'found': True,
                'موجودة': True,
                'source': result.source,
                'المصدر': result.source,
                'priority': result.priority.name,
                'الأولوية': result.priority.name,
                'confidence': result.confidence,
                'الثقة': result.confidence,
                'type': result.word.word_type.value,
                'النوع': result.word.word_type.value,
                'category': result.word.category.value,
                'الفئة': result.word.category.value,
                'meaning': result.word.core_meaning,
                'المعنى': result.word.core_meaning,
                'root': result.word.root_word,
                'الجذر': result.word.root_word,
                'related_words': result.word.related_words,
                'كلمات_مرتبطة': result.word.related_words
            }
        else:
            return {
                'word': word,
                'الكلمة': word,
                'found': False,
                'موجودة': False,
                'message': 'الكلمة غير موجودة في المعجم',
                'الرسالة': 'الكلمة غير موجودة في المعجم'
            }
    
    env['lookup_word'] = lookup_word
    env['ابحث_كلمة'] = lookup_word
    env['ابحث_في_المعجم'] = lookup_word
    
    def search_by_root(root: str, limit: int = 10) -> List[Dict]:
        """
        البحث بالجذر
        Search by root
        
        مثال: ابحث_بالجذر("درس")
        """
        lexicon = _get_unified_lexicon()
        results = lexicon.search_by_root(root)
        
        return [
            {
                'word': w.arabic,
                'الكلمة': w.arabic,
                'type': w.word_type.value,
                'النوع': w.word_type.value,
                'meaning': w.core_meaning[:50] + '...' if len(w.core_meaning) > 50 else w.core_meaning,
                'المعنى': w.core_meaning[:50] + '...' if len(w.core_meaning) > 50 else w.core_meaning
            }
            for w in results[:limit]
        ]
    
    env['search_by_root'] = search_by_root
    env['ابحث_بالجذر'] = search_by_root
    
    def advanced_search(word: str) -> List[Dict]:
        """
        البحث المتقدم (يرجع جميع المصادر)
        Advanced search (returns all sources)
        
        مثال: بحث_متقدم("كتاب")
        """
        lexicon = _get_unified_lexicon()
        results = lexicon.advanced_search(word)
        
        return [
            {
                'source': r.source,
                'المصدر': r.source,
                'priority': r.priority.name,
                'الأولوية': r.priority.name,
                'confidence': r.confidence,
                'الثقة': r.confidence,
                'word': r.word.arabic,
                'الكلمة': r.word.arabic,
                'meaning': r.word.core_meaning[:50] + '...' if len(r.word.core_meaning) > 50 else r.word.core_meaning,
                'المعنى': r.word.core_meaning[:50] + '...' if len(r.word.core_meaning) > 50 else r.word.core_meaning
            }
            for r in results
        ]
    
    env['advanced_search'] = advanced_search
    env['بحث_متقدم'] = advanced_search
    
    def word_exists(word: str) -> bool:
        """
        التحقق من وجود كلمة
        Check if word exists
        
        مثال: كلمة_موجودة("أرض")
        """
        lexicon = _get_unified_lexicon()
        return lexicon.has_word(word)
    
    env['word_exists'] = word_exists
    env['كلمة_موجودة'] = word_exists
    
    # ═══════════════════════════════════════════════════════════════
    # 5. دوال القاموس الأساسي
    # ═══════════════════════════════════════════════════════════════
    
    def get_words_by_type(word_type: str) -> List[Dict]:
        """
        الحصول على كلمات حسب النوع
        Get words by type
        
        الأنواع المتاحة: كيان، خاصية، فعل، حالة، علاقة، اتجاه، كمية، زمن
        
        مثال: كلمات_حسب_النوع("فعل")
        """
        vocab = _get_foundation_vocab()
        
        # تحويل النص إلى Enum
        type_map = {
            'كيان': FoundationWordType.ENTITY,
            'خاصية': FoundationWordType.PROPERTY,
            'فعل': FoundationWordType.ACTION,
            'حالة': FoundationWordType.STATE,
            'علاقة': FoundationWordType.RELATION,
            'اتجاه': FoundationWordType.DIRECTION,
            'كمية': FoundationWordType.QUANTITY,
            'زمن': FoundationWordType.TIME
        }
        
        word_type_enum = type_map.get(word_type)
        if not word_type_enum:
            return []
        
        words = vocab.get_words_by_type(word_type_enum)
        return [
            {
                'word': w.arabic,
                'الكلمة': w.arabic,
                'english': w.english,
                'الإنجليزية': w.english,
                'meaning': w.core_meaning,
                'المعنى': w.core_meaning
            }
            for w in words[:20]  # أول 20 كلمة
        ]
    
    env['get_words_by_type'] = get_words_by_type
    env['كلمات_حسب_النوع'] = get_words_by_type
    
    def get_words_by_category(category: str) -> List[Dict]:
        """
        الحصول على كلمات حسب الفئة
        Get words by category
        
        الفئات المتاحة: البيئة_الأولية، الكيان_والوجود، فيزيائية، حسية، نفسية، 
                        اجتماعية، أفعال_أساسية، تحولات، بيئة_طبيعية
        
        مثال: كلمات_حسب_الفئة("أفعال_أساسية")
        """
        vocab = _get_foundation_vocab()
        
        # تحويل النص إلى Enum
        category_map = {
            'البيئة_الأولية': FoundationCategory.INITIAL_ENVIRONMENT,
            'الكيان_والوجود': FoundationCategory.ENTITY_EXISTENCE,
            'فيزيائية': FoundationCategory.PHYSICAL,
            'حسية': FoundationCategory.SENSORY,
            'نفسية': FoundationCategory.PSYCHOLOGICAL,
            'اجتماعية': FoundationCategory.SOCIAL,
            'أفعال_أساسية': FoundationCategory.BASIC_ACTIONS,
            'تحولات': FoundationCategory.TRANSFORMATIONS,
            'بيئة_طبيعية': FoundationCategory.NATURAL_ENVIRONMENT
        }
        
        category_enum = category_map.get(category)
        if not category_enum:
            return []
        
        words = vocab.get_words_by_category(category_enum)
        return [
            {
                'word': w.arabic,
                'الكلمة': w.arabic,
                'english': w.english,
                'الإنجليزية': w.english,
                'meaning': w.core_meaning,
                'المعنى': w.core_meaning
            }
            for w in words[:20]  # أول 20 كلمة
        ]
    
    env['get_words_by_category'] = get_words_by_category
    env['كلمات_حسب_الفئة'] = get_words_by_category
    
    def find_related_words(word: str) -> List[str]:
        """
        إيجاد كلمات مرتبطة
        Find related words
        
        مثال: كلمات_مرتبطة("أرض")
        """
        vocab = _get_foundation_vocab()
        related = vocab.find_related_words(word)
        return [w.arabic for w in related]
    
    env['find_related_words'] = find_related_words
    env['كلمات_مرتبطة'] = find_related_words
    
    def search_by_meaning(meaning: str) -> List[Dict]:
        """
        البحث بالمعنى
        Search by meaning
        
        مثال: ابحث_بالمعنى("ماء")
        """
        vocab = _get_foundation_vocab()
        results = vocab.search_by_meaning(meaning)
        return [
            {
                'word': w.arabic,
                'الكلمة': w.arabic,
                'meaning': w.core_meaning,
                'المعنى': w.core_meaning,
                'type': w.word_type.value,
                'النوع': w.word_type.value
            }
            for w in results[:10]  # أول 10 نتائج
        ]
    
    env['search_by_meaning'] = search_by_meaning
    env['ابحث_بالمعنى'] = search_by_meaning
    
    # ═══════════════════════════════════════════════════════════════
    # 6. دوال الإحصائيات
    # ═══════════════════════════════════════════════════════════════
    
    def lexicon_statistics() -> Dict[str, Any]:
        """
        الحصول على إحصائيات المعجم
        Get lexicon statistics
        
        مثال: إحصائيات_المعجم()
        """
        lexicon = _get_unified_lexicon()
        stats = lexicon.get_statistics()
        
        return {
            'foundation_words': stats.foundation_words,
            'كلمات_أساسية': stats.foundation_words,
            'arramooz_words': stats.arramooz_words,
            'كلمات_الرموز': stats.arramooz_words,
            'total_words': stats.total_words,
            'المجموع': stats.total_words,
            'cache_size': stats.cache_size,
            'حجم_الذاكرة': stats.cache_size,
            'cache_hit_rate': f"{stats.cache_hit_rate:.2%}",
            'معدل_الإصابة': f"{stats.cache_hit_rate:.2%}"
        }
    
    env['lexicon_statistics'] = lexicon_statistics
    env['إحصائيات_المعجم'] = lexicon_statistics
    
    def foundation_statistics() -> Dict[str, Any]:
        """
        الحصول على إحصائيات القاموس الأساسي
        Get foundation vocabulary statistics
        
        مثال: إحصائيات_القاموس()
        """
        vocab = _get_foundation_vocab()
        stats = vocab.get_statistics()
        
        # تحويل Enum إلى نص
        by_type = {k.value: v for k, v in stats['by_type'].items()}
        by_category = {k.value: v for k, v in stats['by_category'].items()}
        
        return {
            'total_words': stats['total_words'],
            'المجموع': stats['total_words'],
            'by_type': by_type,
            'حسب_النوع': by_type,
            'by_category': by_category,
            'حسب_الفئة': by_category
        }
    
    env['foundation_statistics'] = foundation_statistics
    env['إحصائيات_القاموس'] = foundation_statistics
    
    # ═══════════════════════════════════════════════════════════════
    # 7. رسالة نجاح
    # ═══════════════════════════════════════════════════════════════
    
    print("✅ تم تسجيل دوال نظام المعجم الموحد بنجاح")
    print("   📚 105 كلمة أساسية + 40,850 كلمة من معجم الرموز")
    return True


def create_vocabulary_enhanced_interpreter(use_hybrid: bool = True):
    """
    إنشاء مفسر محسّن مع دوال نظام المعجم
    
    Args:
        use_hybrid: استخدام المفسر الهجين (True) أو التقليدي (False)
    
    Returns:
        المفسر مع الدوال المضافة
    """
    if use_hybrid:
        from .hybrid_interpreter import HybridInterpreter
        interpreter = HybridInterpreter()
    else:
        from .traditional_interpreter import TraditionalInterpreter
        interpreter = TraditionalInterpreter()
    
    register_vocabulary_functions(interpreter)
    return interpreter
