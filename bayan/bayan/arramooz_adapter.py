# -*- coding: utf-8 -*-
"""
محول قاعدة بيانات Arramooz إلى Python
Arramooz Dictionary Adapter for Python

يحول بيانات قاعدة بيانات Arramooz (40,850 كلمة) للاستخدام في بيان
Converts Arramooz database data (40,850 words) for use in Bayan

المصدر الأصلي: TypeScript في /vocabulary/arramoozDictionaryAdapter.ts
Original source: TypeScript in /vocabulary/arramoozDictionaryAdapter.ts
"""

import sqlite3
import os
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class FoundationWordType(Enum):
    """نوع الكلمة الأساسية"""
    ENTITY = 'كيان'
    PROPERTY = 'خاصية'
    ACTION = 'فعل'
    STATE = 'حالة'
    RELATION = 'علاقة'
    DIRECTION = 'اتجاه'
    QUANTITY = 'كمية'
    TIME = 'زمن'


class FoundationCategory(Enum):
    """فئة الكلمة الأساسية"""
    INITIAL_ENVIRONMENT = 'البيئة_الأولية'
    ENTITY_EXISTENCE = 'الكيان_والوجود'
    PHYSICAL = 'فيزيائية'
    SENSORY = 'حسية'
    PSYCHOLOGICAL = 'نفسية'
    SOCIAL = 'اجتماعية'
    BASIC_ACTIONS = 'أفعال_أساسية'
    TRANSFORMATIONS = 'تحولات'
    NATURAL_ENVIRONMENT = 'بيئة_طبيعية'


@dataclass
class FoundationWord:
    """كلمة أساسية"""
    arabic: str
    english: Optional[str] = None
    word_type: FoundationWordType = FoundationWordType.ENTITY
    category: FoundationCategory = FoundationCategory.ENTITY_EXISTENCE
    core_meaning: str = ""
    related_words: List[str] = None
    root_word: Optional[str] = None
    meaning_angle: Optional[str] = None
    examples: List[str] = None
    weight: float = 0.5
    
    def __post_init__(self):
        if self.related_words is None:
            self.related_words = []
        if self.examples is None:
            self.examples = []


class ArramoozAdapter:
    """
    محول قاعدة بيانات Arramooz
    Arramooz Dictionary Adapter
    
    يوفر الوصول إلى 40,850 كلمة عربية من قاعدة بيانات Arramooz
    Provides access to 40,850 Arabic words from Arramooz database
    """
    
    def __init__(self, db_path: str = None):
        """
        تهيئة المحول
        
        Args:
            db_path: مسار قاعدة البيانات (اختياري)
        """
        self.db_path = db_path
        self.conn: Optional[sqlite3.Connection] = None
        self.cache: Dict[str, FoundationWord] = {}
        self.root_cache: Dict[str, List[FoundationWord]] = {}
        self.is_loaded = False
    
    def _find_database(self) -> Optional[str]:
        """البحث عن ملف قاعدة البيانات في مسارات متعددة"""
        if self.db_path and os.path.exists(self.db_path):
            return self.db_path
            
        # المسارات المحتملة
        possible_paths = [
            # المسار الافتراضي المحدد في الكود الأصلي
            'src/baserah/lexicon/databases/arramooz_dictionary.db',
            # في نفس المجلد
            os.path.join(os.path.dirname(__file__), 'arramooz_dictionary.db'),
            # في مجلد databases المجاور
            os.path.join(os.path.dirname(__file__), 'databases', 'arramooz_dictionary.db'),
            # في مجلد databases في الجذر
            'databases/arramooz_dictionary.db',
            # في المسار الحالي
            'arramooz_dictionary.db'
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
                
        return None

    def load_database(self) -> bool:
        """
        تحميل قاعدة البيانات
        Load the database
        
        Returns:
            True إذا نجح التحميل، False إذا فشل
        """
        if self.is_loaded:
            return True
            
        # البحث عن قاعدة البيانات
        found_path = self._find_database()
        if not found_path:
            print(f'❌ لم يتم العثور على ملف قاعدة البيانات arramooz_dictionary.db')
            print(f'   يرجى وضعه في أحد المسارات التالية:')
            print(f'   - src/baserah/lexicon/databases/')
            print(f'   - {os.path.dirname(__file__)}/')
            return False
        
        self.db_path = found_path
        
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
            self.is_loaded = True
            print('✅ تم تحميل قاعدة بيانات Arramooz بنجاح (40,850 كلمة)')
            return True
        except Exception as e:
            print(f'❌ خطأ في تحميل قاعدة بيانات Arramooz: {e}')
            print(f'   المسار المتوقع: {self.db_path}')
            return False
    
    def search_word(self, word: str) -> Optional[FoundationWord]:
        """
        البحث عن كلمة
        Search for a word
        
        Args:
            word: الكلمة المراد البحث عنها
        
        Returns:
            FoundationWord أو None إذا لم توجد
        """
        if not self.is_loaded or not self.conn:
            raise RuntimeError('قاعدة البيانات غير محملة. استخدم load_database() أولاً.')
        
        # تطبيع الكلمة (إزالة ال التعريف)
        normalized = self._normalize_word(word)
        
        # البحث في الذاكرة المؤقتة
        if normalized in self.cache:
            return self.cache[normalized]
        
        # البحث في جدول الأسماء
        result = self._search_in_nouns(normalized)
        if result:
            self.cache[normalized] = result
            return result
        
        # البحث في جدول الأفعال
        result = self._search_in_verbs(normalized)
        if result:
            self.cache[normalized] = result
            return result
        
        return None
    
    def search_by_root(self, root: str, limit: int = 20) -> List[FoundationWord]:
        """
        البحث بالجذر
        Search by root
        
        Args:
            root: الجذر
            limit: الحد الأقصى للنتائج
        
        Returns:
            قائمة الكلمات المشتقة من الجذر
        """
        if not self.is_loaded or not self.conn:
            raise RuntimeError('قاعدة البيانات غير محملة. استخدم load_database() أولاً.')
        
        # البحث في الذاكرة المؤقتة
        if root in self.root_cache:
            return self.root_cache[root]
        
        results = []
        
        # البحث في الأسماء
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM nouns WHERE root = ? LIMIT ?', (root, limit))
            for row in cursor.fetchall():
                word = self._convert_noun_to_foundation_word(dict(row))
                if word:
                    results.append(word)
        except Exception as e:
            print(f'خطأ في البحث بالجذر في الأسماء: {e}')
        
        # البحث في الأفعال
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM verbs WHERE root = ? LIMIT ?', (root, limit))
            for row in cursor.fetchall():
                word = self._convert_verb_to_foundation_word(dict(row))
                if word:
                    results.append(word)
        except Exception as e:
            print(f'خطأ في البحث بالجذر في الأفعال: {e}')
        
        # حفظ في الذاكرة المؤقتة
        self.root_cache[root] = results
        
        return results
    
    def get_statistics(self) -> Dict[str, int]:
        """
        الحصول على إحصائيات قاعدة البيانات
        Get database statistics
        
        Returns:
            قاموس بالإحصائيات
        """
        if not self.is_loaded or not self.conn:
            return {'nouns': 0, 'verbs': 0, 'total': 0}
        
        try:
            cursor = self.conn.cursor()
            
            cursor.execute('SELECT COUNT(*) FROM nouns')
            noun_count = cursor.fetchone()[0]
            
            cursor.execute('SELECT COUNT(*) FROM verbs')
            verb_count = cursor.fetchone()[0]
            
            return {
                'nouns': noun_count,
                'verbs': verb_count,
                'total': noun_count + verb_count
            }
        except Exception as e:
            print(f'خطأ في الحصول على الإحصائيات: {e}')
            return {'nouns': 0, 'verbs': 0, 'total': 0}
    
    def close(self):
        """إغلاق قاعدة البيانات"""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.is_loaded = False
    
    # ═══════════════════════════════════════════════════════════════
    # دوال مساعدة خاصة
    # ═══════════════════════════════════════════════════════════════
    
    def _normalize_word(self, word: str) -> str:
        """تطبيع الكلمة (إزالة ال التعريف)"""
        if word.startswith('ال'):
            return word[2:]
        return word
    
    def _search_in_nouns(self, word: str) -> Optional[FoundationWord]:
        """البحث في جدول الأسماء"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT * FROM nouns 
                WHERE unvocalized = ? OR normalized = ? OR stamped = ?
                LIMIT 1
            ''', (word, word, word))
            
            row = cursor.fetchone()
            if row:
                return self._convert_noun_to_foundation_word(dict(row))
        except Exception as e:
            print(f'خطأ في البحث في جدول الأسماء: {e}')
        
        return None
    
    def _search_in_verbs(self, word: str) -> Optional[FoundationWord]:
        """البحث في جدول الأفعال"""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT * FROM verbs 
                WHERE unvocalized = ? OR normalized = ? OR stamped = ?
                LIMIT 1
            ''', (word, word, word))
            
            row = cursor.fetchone()
            if row:
                return self._convert_verb_to_foundation_word(dict(row))
        except Exception as e:
            print(f'خطأ في البحث في جدول الأفعال: {e}')
        
        return None
    
    def _convert_noun_to_foundation_word(self, noun: Dict) -> Optional[FoundationWord]:
        """تحويل اسم Arramooz إلى FoundationWord"""
        if not noun.get('unvocalized'):
            return None
        
        # تحديد النوع
        word_type = self._determine_noun_type(
            noun.get('wordtype', ''),
            noun.get('category', '')
        )
        
        # استخراج الكلمات المرتبطة
        related = []
        for field in ['feminin', 'masculin', 'single', 'broken_plural']:
            value = noun.get(field)
            if value and value.strip():
                related.append(value)
        
        return FoundationWord(
            arabic=noun['unvocalized'],
            english=None,
            word_type=word_type,
            category=FoundationCategory.ENTITY_EXISTENCE,
            core_meaning=noun.get('definition', f"{noun.get('wordtype', '')} من {noun.get('root', '')}"),
            related_words=related,
            root_word=noun.get('root'),
            meaning_angle=noun.get('wazn'),
            examples=[],
            weight=0.5
        )
    
    def _convert_verb_to_foundation_word(self, verb: Dict) -> Optional[FoundationWord]:
        """تحويل فعل Arramooz إلى FoundationWord"""
        if not verb.get('unvocalized'):
            return None
        
        return FoundationWord(
            arabic=verb['unvocalized'],
            english=None,
            word_type=FoundationWordType.ACTION,
            category=FoundationCategory.BASIC_ACTIONS,
            core_meaning=f"فعل من الجذر {verb.get('root', '')}",
            related_words=[],
            root_word=verb.get('root'),
            meaning_angle=verb.get('future_type'),
            examples=[],
            weight=0.5
        )
    
    def _determine_noun_type(self, wordtype: str, category: str) -> FoundationWordType:
        """تحديد نوع الاسم"""
        if 'فاعل' in wordtype or 'مفعول' in wordtype:
            return FoundationWordType.ENTITY
        if 'صفة' in wordtype:
            return FoundationWordType.PROPERTY
        if category == 'حالة':
            return FoundationWordType.STATE
        return FoundationWordType.ENTITY
    
    def __enter__(self):
        """دعم context manager"""
        self.load_database()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """إغلاق تلقائي"""
        self.close()


# ═══════════════════════════════════════════════════════════════
# مثال الاستخدام
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║              🔍 محول قاعدة بيانات Arramooz                      ║
║              Arramooz Dictionary Adapter                        ║
║                                                                  ║
║              40,850 كلمة عربية                                  ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
""")
    
    # استخدام context manager
    try:
        with ArramoozAdapter() as adapter:
            # عرض الإحصائيات
            stats = adapter.get_statistics()
            print(f"\n📊 إحصائيات قاعدة البيانات:")
            print(f"   ├─ الأسماء: {stats['nouns']:,}")
            print(f"   ├─ الأفعال: {stats['verbs']:,}")
            print(f"   └─ المجموع: {stats['total']:,}")
            
            # اختبار البحث
            print(f"\n🔍 اختبار البحث:")
            test_words = ["مدرسة", "كتاب", "يدرس", "كتب"]
            
            for word in test_words:
                result = adapter.search_word(word)
                if result:
                    print(f"\n   الكلمة: {word}")
                    print(f"   ├─ النوع: {result.word_type.value}")
                    print(f"   ├─ الجذر: {result.root_word}")
                    print(f"   └─ المعنى: {result.core_meaning[:50]}...")
            
            # اختبار البحث بالجذر
            print(f"\n📚 البحث بالجذر 'درس':")
            root_results = adapter.search_by_root('درس', limit=5)
            for i, word in enumerate(root_results, 1):
                print(f"   {i}. {word.arabic} ({word.word_type.value})")
            
    except Exception as e:
        print(f"\n❌ خطأ: {e}")
        print("\n💡 تأكد من وجود قاعدة البيانات في:")
        print("   src/baserah/lexicon/databases/arramooz_dictionary.db")
