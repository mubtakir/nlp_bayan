# -*- coding: utf-8 -*-
"""
النظام المعجمي الموحد
Unified Lexicon System

يدمج جميع مصادر المفردات في نظام واحد:
- CompleteFoundationVocabulary (105 كلمة أساسية - أولوية عالية)
- ArramoozDictionaryAdapter (40,850 كلمة - أولوية متوسطة)

Merges all vocabulary sources into one system:
- CompleteFoundationVocabulary (105 foundation words - high priority)
- ArramoozDictionaryAdapter (40,850 words - medium priority)

المصدر الأصلي: TypeScript في /vocabulary/unifiedLexiconSystem.ts
Original source: TypeScript in /vocabulary/unifiedLexiconSystem.ts
"""

from enum import Enum
from typing import Dict, List, Optional
from dataclasses import dataclass

from .foundation_vocabulary import FoundationWord, FoundationWordType, FoundationCategory
from .complete_vocabulary import CompleteFoundationVocabulary
from .arramooz_adapter import ArramoozAdapter


class PriorityLevel(Enum):
    """مستوى الأولوية / Priority Level"""
    HIGH = 3      # الكلمات الأساسية
    MEDIUM = 2    # قاموس Arramooz
    LOW = 1       # معاني الحروف


@dataclass
class LexiconSearchResult:
    """
    نتيجة البحث مع معلومات إضافية
    Search result with additional info
    """
    word: FoundationWord
    source: str  # 'foundation' | 'arramooz' | 'character'
    priority: PriorityLevel
    confidence: float


class LexiconStatistics:
    """إحصائيات النظام المعجمي / Lexicon system statistics"""
    
    def __init__(self, foundation_words: int, arramooz_words: int, 
                 total_words: int, cache_size: int, cache_hit_rate: float):
        self.foundation_words = foundation_words
        self.arramooz_words = arramooz_words
        self.total_words = total_words
        self.cache_size = cache_size
        self.cache_hit_rate = cache_hit_rate


class UnifiedLexiconSystem:
    """
    النظام المعجمي الموحد
    Unified Lexicon System
    """
    
    def __init__(self, arramooz_db_path: Optional[str] = None):
        self.foundation_vocab = CompleteFoundationVocabulary()
        self.arramooz_adapter = ArramoozAdapter(arramooz_db_path)
        
        # التخزين المؤقت متعدد المستويات
        self.cache: Dict[str, LexiconSearchResult] = {}
        self.root_cache: Dict[str, List[FoundationWord]] = {}
        
        # إحصائيات
        self.cache_hits = 0
        self.cache_misses = 0
        
        self.is_initialized = False
    
    def initialize(self) -> bool:
        """
        تهيئة النظام
        Initialize the system
        
        Returns:
            True إذا نجحت التهيئة
        """
        if self.is_initialized:
            return True
        
        print('🔄 جاري تهيئة النظام المعجمي الموحد...')
        
        # تحميل قاعدة بيانات Arramooz
        arramooz_loaded = self.arramooz_adapter.load_database()
        
        self.is_initialized = True
        
        stats = self.get_statistics()
        print(f'✅ تم تهيئة النظام المعجمي الموحد بنجاح!')
        print(f'   📚 الكلمات الأساسية: {stats.foundation_words}')
        print(f'   📖 قاموس Arramooz: {stats.arramooz_words}')
        print(f'   📊 الإجمالي: {stats.total_words} كلمة')
        
        return True
    
    def lookup(self, word: str) -> Optional[LexiconSearchResult]:
        """
        البحث عن كلمة (مع نظام الأولويات)
        Search for a word (with priority system)
        """
        if not self.is_initialized:
            raise RuntimeError('النظام غير مهيأ. استخدم initialize() أولاً.')
        
        # تطبيع الكلمة
        normalized = self._normalize_word(word)
        
        # 1. البحث في الذاكرة المؤقتة
        if normalized in self.cache:
            self.cache_hits += 1
            return self.cache[normalized]
        
        self.cache_misses += 1
        
        # 2. البحث في الكلمات الأساسية (أولوية عالية)
        foundation_word = self.foundation_vocab.get_word(normalized)
        if foundation_word:
            result = LexiconSearchResult(
                word=foundation_word,
                source='foundation',
                priority=PriorityLevel.HIGH,
                confidence=1.0
            )
            self.cache[normalized] = result
            return result
        
        # 3. البحث في قاموس Arramooz (أولوية متوسطة)
        if self.arramooz_adapter.is_loaded:
            arramooz_word = self.arramooz_adapter.search_word(normalized)
            if arramooz_word:
                result = LexiconSearchResult(
                    word=arramooz_word,
                    source='arramooz',
                    priority=PriorityLevel.MEDIUM,
                    confidence=0.8
                )
                self.cache[normalized] = result
                return result
        
        # 4. لم يتم العثور على الكلمة
        return None
    
    def search_by_root(self, root: str) -> List[FoundationWord]:
        """
        البحث بالجذر
        Search by root
        """
        if not self.is_initialized:
            raise RuntimeError('النظام غير مهيأ. استخدم initialize() أولاً.')
        
        # البحث في الذاكرة المؤقتة
        if root in self.root_cache:
            return self.root_cache[root]
        
        results = []
        
        # البحث في الكلمات الأساسية
        foundation_words = self.foundation_vocab.get_all_words()
        for word in foundation_words:
            if word.root_word == root:
                results.append(word)
        
        # البحث في Arramooz
        if self.arramooz_adapter.is_loaded:
            arramooz_words = self.arramooz_adapter.search_by_root(root)
            results.extend(arramooz_words)
        
        # حفظ في الذاكرة المؤقتة
        self.root_cache[root] = results
        
        return results
    
    def advanced_search(self, word: str) -> List[LexiconSearchResult]:
        """
        البحث المتقدم (يرجع جميع التطابقات مع الأولويات)
        Advanced search (returns all matches with priorities)
        """
        if not self.is_initialized:
            raise RuntimeError('النظام غير مهيأ. استخدم initialize() أولاً.')
        
        results = []
        normalized = self._normalize_word(word)
        
        # البحث في الكلمات الأساسية
        foundation_word = self.foundation_vocab.get_word(normalized)
        if foundation_word:
            results.append(LexiconSearchResult(
                word=foundation_word,
                source='foundation',
                priority=PriorityLevel.HIGH,
                confidence=1.0
            ))
        
        # البحث في Arramooz
        if self.arramooz_adapter.is_loaded:
            arramooz_word = self.arramooz_adapter.search_word(normalized)
            if arramooz_word:
                results.append(LexiconSearchResult(
                    word=arramooz_word,
                    source='arramooz',
                    priority=PriorityLevel.MEDIUM,
                    confidence=0.8
                ))
        
        # ترتيب حسب الأولوية
        results.sort(key=lambda x: x.priority.value, reverse=True)
        
        return results
    
    def get_best_match(self, word: str) -> Optional[FoundationWord]:
        """
        الحصول على الكلمة الأفضل (أعلى أولوية)
        Get the best word (highest priority)
        """
        result = self.lookup(word)
        return result.word if result else None
    
    def has_word(self, word: str) -> bool:
        """التحقق من وجود كلمة / Check if word exists"""
        return self.lookup(word) is not None
    
    def get_words_by_source(self, source: str) -> List[FoundationWord]:
        """
        الحصول على جميع الكلمات من مصدر معين
        Get all words from a specific source
        """
        if not self.is_initialized:
            raise RuntimeError('النظام غير مهيأ. استخدم initialize() أولاً.')
        
        if source == 'foundation':
            return self.foundation_vocab.get_all_words()
        
        # لا يمكن الحصول على جميع كلمات Arramooz (40,850 كلمة)
        # يجب استخدام البحث بدلاً من ذلك
        return []
    
    def clear_cache(self) -> None:
        """مسح الذاكرة المؤقتة / Clear cache"""
        self.cache.clear()
        self.root_cache.clear()
        self.cache_hits = 0
        self.cache_misses = 0
    
    def get_statistics(self) -> LexiconStatistics:
        """الحصول على إحصائيات / Get statistics"""
        foundation_words = len(self.foundation_vocab.get_all_words())
        
        if self.arramooz_adapter.is_loaded:
            arramooz_stats = self.arramooz_adapter.get_statistics()
            arramooz_count = arramooz_stats['total']
        else:
            arramooz_count = 0
        
        total_requests = self.cache_hits + self.cache_misses
        cache_hit_rate = self.cache_hits / total_requests if total_requests > 0 else 0
        
        return LexiconStatistics(
            foundation_words=foundation_words,
            arramooz_words=arramooz_count,
            total_words=foundation_words + arramooz_count,
            cache_size=len(self.cache),
            cache_hit_rate=cache_hit_rate
        )
    
    def close(self) -> None:
        """إغلاق النظام / Close the system"""
        self.arramooz_adapter.close()
        self.clear_cache()
        self.is_initialized = False
    
    def get_word_details(self, word: str) -> Dict:
        """
        الحصول على معلومات تفصيلية عن كلمة
        Get detailed information about a word
        """
        results = self.advanced_search(word)
        
        if not results:
            return {
                'exists': False,
                'sources': [],
                'priority': None,
                'related_words': []
            }
        
        best_result = results[0]
        
        return {
            'exists': True,
            'sources': [r.source for r in results],
            'priority': best_result.priority,
            'root': best_result.word.root_word,
            'related_words': best_result.word.related_words
        }
    
    def _normalize_word(self, word: str) -> str:
        """تطبيع الكلمة (إزالة ال التعريف) / Normalize word"""
        if word.startswith('ال'):
            return word[2:]
        return word
    
    def __enter__(self):
        """دعم context manager"""
        self.initialize()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """إغلاق تلقائي"""
        self.close()


# ═══════════════════════════════════════════════════════════════
# مثال الاستخدام / Usage Example
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║              🔍 النظام المعجمي الموحد                           ║
║              Unified Lexicon System                             ║
║                                                                  ║
║              105 كلمة أساسية + 40,850 كلمة من Arramooz         ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
""")
    
    try:
        with UnifiedLexiconSystem() as lexicon:
            # عرض الإحصائيات
            stats = lexicon.get_statistics()
            print(f"\n📊 إحصائيات النظام:")
            print(f"   ├─ الكلمات الأساسية: {stats.foundation_words:,}")
            print(f"   ├─ قاموس Arramooz: {stats.arramooz_words:,}")
            print(f"   └─ المجموع: {stats.total_words:,}")
            
            # اختبار البحث
            print(f"\n🔍 اختبار البحث:")
            test_words = ["أرض", "مدرسة", "كتاب", "يدرس"]
            
            for word in test_words:
                result = lexicon.lookup(word)
                if result:
                    print(f"\n   الكلمة: {word}")
                    print(f"   ├─ المصدر: {result.source}")
                    print(f"   ├─ الأولوية: {result.priority.name}")
                    print(f"   ├─ الثقة: {result.confidence}")
                    print(f"   └─ المعنى: {result.word.core_meaning[:50]}...")
                else:
                    print(f"\n   الكلمة: {word} - ❌ غير موجودة")
            
            # اختبار البحث بالجذر
            print(f"\n📚 البحث بالجذر 'درس':")
            root_results = lexicon.search_by_root('درس')
            for i, word in enumerate(root_results[:5], 1):
                print(f"   {i}. {word.arabic} ({word.word_type.value})")
            
            # إحصائيات الذاكرة المؤقتة
            print(f"\n💾 إحصائيات الذاكرة المؤقتة:")
            print(f"   ├─ الحجم: {stats.cache_size}")
            print(f"   └─ معدل الإصابة: {stats.cache_hit_rate:.2%}")
            
    except Exception as e:
        print(f"\n❌ خطأ: {e}")
        print("\n💡 تأكد من وجود قاعدة البيانات في:")
        print("   src/baserah/lexicon/databases/arramooz_dictionary.db")
