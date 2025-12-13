# -*- coding: utf-8 -*-
"""
إضافة سيميائية الحروف للمفسر
Letter Semiotics Extension for Bayan Interpreter
================================================

هذا الملف يضيف دوال سيميائية الحروف للمفسر بدون تعديل المفسر الأصلي.

الاستخدام:
    from bayan.letter_semiotics_extension import register_letter_semiotics
    register_letter_semiotics(interpreter)

أو تلقائياً عند إنشاء المفسر:
    from bayan.letter_semiotics_extension import create_enhanced_interpreter
    interpreter = create_enhanced_interpreter()

المطور: باسل يحيى عبدالله - العراق/الموصل
"""

from typing import Union, List, Dict, Any, Optional


def register_letter_semiotics(interpreter) -> bool:
    """
    تسجيل دوال سيميائية الحروف في المفسر
    
    Args:
        interpreter: المفسر (TraditionalInterpreter أو HybridInterpreter)
    
    Returns:
        True إذا نجح التسجيل، False إذا فشل
    """
    try:
        from .letter_semiotics import (
            ArabicLetterDatabase,
            WordAnalyzer,
            WordGenerator,
            LetterAnalyzer
        )
        from .letter_semiotics.inference_engine import EnhancedMeaningInferenceEngine
    except ImportError as e:
        print(f"⚠️ تحذير: لم يتم تحميل سيميائية الحروف: {e}")
        return False
    
    # الحصول على global_env
    if hasattr(interpreter, 'global_env'):
        env = interpreter.global_env
    elif hasattr(interpreter, 'traditional') and hasattr(interpreter.traditional, 'global_env'):
        env = interpreter.traditional.global_env
    else:
        print("⚠️ تحذير: لا يمكن العثور على global_env في المفسر")
        return False
    
    # تهيئة كسولة للمكتبات
    _cache = {}
    
    def _get_letter_db():
        if 'db' not in _cache:
            _cache['db'] = ArabicLetterDatabase()
        return _cache['db']
    
    def _get_word_analyzer():
        if 'analyzer' not in _cache:
            _cache['analyzer'] = WordAnalyzer(use_camel=True)
        return _cache['analyzer']
    
    def _get_word_generator():
        if 'generator' not in _cache:
            _cache['generator'] = WordGenerator()
        return _cache['generator']

    def _get_inference_engine():
        if 'inference' not in _cache:
            _cache['inference'] = EnhancedMeaningInferenceEngine()
        return _cache['inference']
    
    # ═══════════════════════════════════════════════════════════════
    # الدوال المدمجة
    # ═══════════════════════════════════════════════════════════════
    
    def analyze_word(word: str) -> Dict[str, Any]:
        """
        تحليل كلمة واستخراج دلالاتها
        Analyze a word and extract its meanings

        مثال: حلل_كلمة("بيان")
        """
        analyzer = _get_word_analyzer()
        result = analyzer.analyze_word(word)
        return {
            'word': word,
            'الكلمة': word,
            'root': result.root_analysis.root if result.root_analysis else None,
            'الجذر': result.root_analysis.root if result.root_analysis else None,
            'pattern': result.morphological_pattern or None,
            'الوزن': result.morphological_pattern or None,
            'meaning': result.combined_meaning,
            'المعنى': result.combined_meaning,
            'emotional_score': result.emotional_score,
            'القوة_النفسية': result.emotional_score,
            'physical_score': result.physical_score,
            'القوة_المادية': result.physical_score,
            'letters': [
                {
                    'letter': la.letter,
                    'الحرف': la.letter,
                    'meanings': la.meanings[:3],
                    'المعاني': la.meanings[:3]
                }
                for la in result.letters
            ]
        }
    
    env['analyze_word'] = analyze_word
    env['حلل_كلمة'] = analyze_word
    
    def letter_meanings(letter: str) -> Dict[str, Any]:
        """
        الحصول على معاني حرف معين
        Get meanings of a specific letter
        
        مثال: معاني_حرف("ب")
        """
        db = _get_letter_db()
        data = db.get_letter(letter)
        if not data:
            return {'error': f'الحرف "{letter}" غير موجود', 'letter': letter}
        
        return {
            'letter': letter,
            'الحرف': letter,
            'meanings': [m.meaning for m in data.developer_meanings],
            'المعاني': [m.meaning for m in data.developer_meanings],
            'opposites': data.developer_meanings[0].opposite if data.developer_meanings else [],
            'الأضداد': data.developer_meanings[0].opposite if data.developer_meanings else [],
            'emotional_strength': data.emotional_strength,
            'القوة_النفسية': data.emotional_strength,
            'physical_strength': data.physical_strength,
            'القوة_المادية': data.physical_strength
        }
    
    env['letter_meanings'] = letter_meanings
    env['معاني_حرف'] = letter_meanings
    
    def generate_word(meanings: Union[str, List[str]], min_letters: int = 3, max_letters: int = 5) -> List[Dict]:
        """
        توليد كلمة جديدة من معاني معينة
        Generate a new word from given meanings
        
        مثال: ابنِ_كلمة(["القوة", "الشدة"])
        """
        generator = _get_word_generator()
        if isinstance(meanings, str):
            meanings = [meanings]
        
        results = generator.generate_word(meanings, min_letters, max_letters)
        return [
            {
                'word': r.word,
                'الكلمة': r.word,
                'confidence': r.confidence,
                'الثقة': r.confidence,
                'explanation': r.explanation,
                'التفسير': r.explanation,
                'emotional_score': r.emotional_score,
                'physical_score': r.physical_score
            }
            for r in results[:5]
        ]
    
    env['generate_word'] = generate_word
    env['ابنِ_كلمة'] = generate_word
    env['ولّد_كلمة'] = generate_word

    def word_root(word: str) -> Dict[str, Any]:
        """
        استخراج جذر الكلمة
        Extract the root of a word

        مثال: جذر_كلمة("مكتبة")
        """
        analyzer = _get_word_analyzer()
        result = analyzer.analyze_word(word)
        if result.root_analysis:
            return {
                'word': word,
                'الكلمة': word,
                'root': result.root_analysis.root,
                'الجذر': result.root_analysis.root,
                'pattern': result.morphological_pattern or None,
                'الوزن': result.morphological_pattern or None,
                'method': result.root_analysis.method,
                'الطريقة': result.root_analysis.method
            }
        return {'word': word, 'الكلمة': word, 'root': None, 'الجذر': None}

    env['word_root'] = word_root
    env['جذر_كلمة'] = word_root

    def suggest_name(concept: str, style: str = "متوازن") -> List[Dict]:
        """
        اقتراح اسم لمفهوم معين
        Suggest a name for a concept

        مثال: اقترح_اسم("ذكاء", "قوي")
        """
        generator = _get_word_generator()
        results = generator.suggest_name(concept, style)
        return [
            {
                'word': r.word,
                'الكلمة': r.word,
                'confidence': r.confidence,
                'emotional_score': r.emotional_score,
                'physical_score': r.physical_score
            }
            for r in results[:5]
        ]

    env['suggest_name'] = suggest_name
    env['اقترح_اسم'] = suggest_name

    def compare_words(word1: str, word2: str) -> Dict[str, Any]:
        """
        مقارنة كلمتين من حيث الدلالة
        Compare two words semantically

        مثال: قارن_كلمتين("حب", "كره")
        """
        analyzer = _get_word_analyzer()
        result1 = analyzer.analyze_word(word1)
        result2 = analyzer.analyze_word(word2)

        return {
            'word1': word1,
            'word2': word2,
            'الكلمة1': word1,
            'الكلمة2': word2,
            'emotional_diff': abs(result1.emotional_score - result2.emotional_score),
            'فرق_النفسي': abs(result1.emotional_score - result2.emotional_score),
            'physical_diff': abs(result1.physical_score - result2.physical_score),
            'فرق_المادي': abs(result1.physical_score - result2.physical_score),
            'word1_meaning': result1.combined_meaning[:100],
            'word2_meaning': result2.combined_meaning[:100]
        }

    env['compare_words'] = compare_words
    env['قارن_كلمتين'] = compare_words

    # ═══════════════════════════════════════════════════════════════
    # دوال الاستنباط الذكي (من محرك الاستنباط الجديد)
    # ═══════════════════════════════════════════════════════════════

    def infer_word(word: str) -> Dict[str, Any]:
        """
        استنباط معنى كلمة جديدة من حروفها
        Infer meaning of a new word from its letters

        هذه الدالة تستنبط المعاني حتى لكلمات لم يرها النظام من قبل!

        مثال: استنبط_كلمة("برمجة")
        """
        engine = _get_inference_engine()
        result = engine.infer_word_meaning(word)
        return {
            'word': word,
            'الكلمة': word,
            'combined_meaning': result['combined_meaning'],
            'المعنى_المركب': result['combined_meaning'],
            'top_meanings': result['top_meanings'],
            'أهم_المعاني': result['top_meanings'],
            'meaning_type': result['meaning_type'],
            'نوع_المعنى': result['meaning_type'],
            'emotional_score': result['emotional_score'],
            'القوة_النفسية': result['emotional_score'],
            'physical_score': result['physical_score'],
            'القوة_المادية': result['physical_score'],
            'pair_patterns': result.get('pair_patterns', []),
            'أنماط_الحروف': result.get('pair_patterns', [])
        }

    env['infer_word'] = infer_word
    env['استنبط_كلمة'] = infer_word
    env['استنبط_معنى'] = infer_word

    def infer_letter(letter: str) -> List[Dict]:
        """
        استنباط معاني حرف واحد من كل المصادر
        Infer meanings of a single letter from all sources

        مثال: استنبط_حرف("ب")
        """
        engine = _get_inference_engine()
        meanings = engine.infer_letter_meanings(letter)
        return [
            {
                'meaning': m.meaning,
                'المعنى': m.meaning,
                'method': m.method.value,
                'الطريقة': m.method.value,
                'confidence': m.confidence,
                'الثقة': m.confidence,
                'evidence': m.evidence,
                'الأدلة': m.evidence
            }
            for m in meanings
        ]

    env['infer_letter'] = infer_letter
    env['استنبط_حرف'] = infer_letter

    def full_letter_analysis(letter: str) -> Dict[str, Any]:
        """
        تحليل كامل لحرف (شكلي + صوتي + اسمي + معجمي)
        Full analysis of a letter (shape + sound + name + lexical)

        مثال: حلل_حرف_كامل("ب")
        """
        engine = _get_inference_engine()
        return engine.get_full_letter_analysis(letter)

    env['full_letter_analysis'] = full_letter_analysis
    env['حلل_حرف_كامل'] = full_letter_analysis

    print("✅ تم تسجيل دوال سيميائية الحروف والاستنباط بنجاح")
    return True


def create_enhanced_interpreter(use_hybrid: bool = True):
    """
    إنشاء مفسر محسّن مع دوال سيميائية الحروف

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

    register_letter_semiotics(interpreter)
    return interpreter

