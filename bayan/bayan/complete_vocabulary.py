# -*- coding: utf-8 -*-
"""
مدير قاموس الكلمات الأساسية الكامل
Complete Foundation Vocabulary Manager

المصدر الأصلي: TypeScript في /vocabulary/completeVocabulary.ts
Original source: TypeScript in /vocabulary/completeVocabulary.ts
"""

from typing import List, Dict
from .foundation_vocabulary import (
    FoundationVocabulary,
    FoundationWord,
    FoundationWordType,
    FoundationCategory
)
from .foundation_vocabulary_extended import add_extended_vocabulary
from .foundation_vocabulary_complete import add_complete_vocabulary


class CompleteFoundationVocabulary:
    """
    مدير قاموس الكلمات الأساسية الكامل
    Complete Foundation Vocabulary Manager
    """
    
    def __init__(self):
        self.vocab = FoundationVocabulary()
        self._load_all_vocabulary()
    
    def _load_all_vocabulary(self) -> None:
        """
        تحميل جميع الكلمات الأساسية
        Load all foundation words
        """
        # الكلمات الأساسية موجودة في FoundationVocabulary
        # Foundation words are already in FoundationVocabulary
        
        # تحميل الكلمات الموسعة
        # Load extended words
        add_extended_vocabulary(self.vocab)
        
        # تحميل الكلمات الكاملة
        # Load complete words
        add_complete_vocabulary(self.vocab)
    
    def get_vocabulary(self) -> FoundationVocabulary:
        """الحصول على القاموس / Get vocabulary"""
        return self.vocab
    
    def get_word(self, arabic: str) -> FoundationWord:
        """الحصول على كلمة / Get word"""
        return self.vocab.get_word(arabic)
    
    def get_words_by_category(self, category: FoundationCategory) -> List[FoundationWord]:
        """الحصول على كلمات حسب الفئة / Get words by category"""
        return self.vocab.get_words_by_category(category)
    
    def get_words_by_type(self, word_type: FoundationWordType) -> List[FoundationWord]:
        """الحصول على كلمات حسب النوع / Get words by type"""
        return self.vocab.get_words_by_type(word_type)
    
    def find_related_words(self, arabic: str) -> List[FoundationWord]:
        """إيجاد كلمات مرتبطة / Find related words"""
        return self.vocab.find_related_words(arabic)
    
    def get_all_words(self) -> List[FoundationWord]:
        """الحصول على جميع الكلمات / Get all words"""
        return self.vocab.get_all_words()
    
    def get_word_count(self) -> int:
        """عدد الكلمات / Word count"""
        return self.vocab.get_word_count()
    
    def get_statistics(self) -> Dict:
        """
        الحصول على إحصائيات
        Get statistics
        """
        all_words = self.vocab.get_all_words()
        by_type = {}
        by_category = {}
        
        for word in all_words:
            # Count by type
            type_key = word.word_type
            by_type[type_key] = by_type.get(type_key, 0) + 1
            
            # Count by category
            category_key = word.category
            by_category[category_key] = by_category.get(category_key, 0) + 1
        
        return {
            'total_words': len(all_words),
            'by_type': by_type,
            'by_category': by_category
        }
    
    def print_statistics(self) -> None:
        """طباعة الإحصائيات / Print statistics"""
        stats = self.get_statistics()
        
        print('\n📊 إحصائيات القاموس الأساسي / Foundation Vocabulary Statistics')
        print('=' * 60)
        print(f'\n📝 إجمالي الكلمات / Total Words: {stats["total_words"]}')
        
        print('\n📂 حسب النوع / By Type:')
        print('─' * 60)
        for word_type, count in stats['by_type'].items():
            print(f'   {word_type.value}: {count}')
        
        print('\n🏷️  حسب الفئة / By Category:')
        print('─' * 60)
        for category, count in stats['by_category'].items():
            print(f'   {category.value}: {count}')
        print('=' * 60)
    
    def show_examples(self) -> None:
        """عرض أمثلة / Show examples"""
        categories = [
            FoundationCategory.INITIAL_ENVIRONMENT,
            FoundationCategory.ENTITY_EXISTENCE,
            FoundationCategory.PHYSICAL,
            FoundationCategory.BASIC_ACTIONS
        ]
        
        print('\n📚 أمثلة من القاموس / Examples from Vocabulary')
        print('=' * 60)
        
        for category in categories:
            words = self.vocab.get_words_by_category(category)
            if words:
                print(f'\n🏷️  {category.value}:')
                example_words = words[:3]
                for word in example_words:
                    english = word.english or 'N/A'
                    print(f'   • {word.arabic} ({english}): {word.core_meaning}')
        print('=' * 60)
    
    def search_by_meaning(self, search_term: str) -> List[FoundationWord]:
        """
        البحث بالمعنى
        Search by meaning
        """
        all_words = self.vocab.get_all_words()
        return [
            word for word in all_words
            if search_term in word.core_meaning
            or search_term in word.arabic
            or (word.english and search_term in word.english)
        ]
    
    def get_related_words_tree(self, arabic: str, depth: int = 2) -> Dict[str, List[FoundationWord]]:
        """
        الحصول على شجرة الكلمات المرتبطة
        Get related words tree
        """
        tree = {}
        visited = set()
        
        def explore(word: str, current_depth: int):
            if current_depth > depth or word in visited:
                return
            
            visited.add(word)
            related = self.vocab.find_related_words(word)
            tree[word] = related
            
            if current_depth < depth:
                for related_word in related:
                    explore(related_word.arabic, current_depth + 1)
        
        explore(arabic, 0)
        return tree


# Singleton instance
_vocabulary_instance: CompleteFoundationVocabulary = None


def get_complete_vocabulary() -> CompleteFoundationVocabulary:
    """
    الحصول على نسخة واحدة من القاموس
    Get singleton vocabulary instance
    """
    global _vocabulary_instance
    if _vocabulary_instance is None:
        _vocabulary_instance = CompleteFoundationVocabulary()
    return _vocabulary_instance


def reset_vocabulary() -> None:
    """
    إعادة تعيين القاموس
    Reset vocabulary
    """
    global _vocabulary_instance
    _vocabulary_instance = None
