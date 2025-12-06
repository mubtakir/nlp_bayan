/**
 * مدير قاموس الكلمات الأساسية الكامل
 * Complete Foundation Vocabulary Manager
 * 
 * @author Basel Yahya Abdullah
 */

import { 
  FoundationVocabulary, 
  FoundationWord, 
  FoundationWordType, 
  FoundationCategory 
} from './foundationVocabulary';
import { addExtendedVocabulary } from './foundationVocabularyExtended';
import { addCompleteVocabulary } from './foundationVocabularyComplete';

/**
 * مدير قاموس الكلمات الأساسية الكامل
 * Complete Foundation Vocabulary Manager
 */
export class CompleteFoundationVocabulary {
  private vocab: FoundationVocabulary;

  constructor() {
    this.vocab = new FoundationVocabulary();
    this.loadAllVocabulary();
  }

  /**
   * تحميل جميع الكلمات الأساسية
   * Load all foundation words
   */
  private loadAllVocabulary(): void {
    // الكلمات الأساسية موجودة في FoundationVocabulary
    // Foundation words are already in FoundationVocabulary
    
    // تحميل الكلمات الموسعة
    // Load extended words
    addExtendedVocabulary(this.vocab);
    
    // تحميل الكلمات الكاملة
    // Load complete words
    addCompleteVocabulary(this.vocab);
  }

  /**
   * الحصول على القاموس
   * Get vocabulary
   */
  getVocabulary(): FoundationVocabulary {
    return this.vocab;
  }

  /**
   * الحصول على كلمة
   * Get word
   */
  getWord(arabic: string): FoundationWord | undefined {
    return this.vocab.getWord(arabic);
  }

  /**
   * الحصول على كلمات حسب الفئة
   * Get words by category
   */
  getWordsByCategory(category: FoundationCategory): FoundationWord[] {
    return this.vocab.getWordsByCategory(category);
  }

  /**
   * الحصول على كلمات حسب النوع
   * Get words by type
   */
  getWordsByType(type: FoundationWordType): FoundationWord[] {
    return this.vocab.getWordsByType(type);
  }

  /**
   * إيجاد كلمات مرتبطة
   * Find related words
   */
  findRelatedWords(arabic: string): FoundationWord[] {
    return this.vocab.findRelatedWords(arabic);
  }

  /**
   * الحصول على جميع الكلمات
   * Get all words
   */
  getAllWords(): FoundationWord[] {
    return this.vocab.getAllWords();
  }

  /**
   * عدد الكلمات
   * Word count
   */
  getWordCount(): number {
    return this.vocab.getWordCount();
  }

  /**
   * الحصول على إحصائيات
   * Get statistics
   */
  getStatistics(): {
    totalWords: number;
    byType: Map<FoundationWordType, number>;
    byCategory: Map<FoundationCategory, number>;
  } {
    const allWords = this.vocab.getAllWords();
    const byType = new Map<FoundationWordType, number>();
    const byCategory = new Map<FoundationCategory, number>();

    for (const word of allWords) {
      // Count by type
      const typeCount = byType.get(word.type) || 0;
      byType.set(word.type, typeCount + 1);

      // Count by category
      const categoryCount = byCategory.get(word.category) || 0;
      byCategory.set(word.category, categoryCount + 1);
    }

    return {
      totalWords: allWords.length,
      byType,
      byCategory
    };
  }

  /**
   * طباعة الإحصائيات
   * Print statistics
   */
  printStatistics(): void {
    const stats = this.getStatistics();
    
    console.log('\n📊 إحصائيات القاموس الأساسي / Foundation Vocabulary Statistics');
    console.log('═'.repeat(60));
    console.log(`\n📝 إجمالي الكلمات / Total Words: ${stats.totalWords}`);
    
    console.log('\n📂 حسب النوع / By Type:');
    console.log('─'.repeat(60));
    for (const [type, count] of stats.byType.entries()) {
      console.log(`   ${type}: ${count}`);
    }
    
    console.log('\n🏷️  حسب الفئة / By Category:');
    console.log('─'.repeat(60));
    for (const [category, count] of stats.byCategory.entries()) {
      console.log(`   ${category}: ${count}`);
    }
    console.log('═'.repeat(60));
  }

  /**
   * عرض أمثلة
   * Show examples
   */
  showExamples(): void {
    const categories = [
      FoundationCategory.INITIAL_ENVIRONMENT,
      FoundationCategory.ENTITY_EXISTENCE,
      FoundationCategory.PHYSICAL,
      FoundationCategory.BASIC_ACTIONS
    ];

    console.log('\n📚 أمثلة من القاموس / Examples from Vocabulary');
    console.log('═'.repeat(60));

    for (const category of categories) {
      const words = this.vocab.getWordsByCategory(category);
      if (words.length > 0) {
        console.log(`\n🏷️  ${category}:`);
        const exampleWords = words.slice(0, 3);
        for (const word of exampleWords) {
          console.log(`   • ${word.arabic} (${word.english || 'N/A'}): ${word.coreMeaning}`);
        }
      }
    }
    console.log('═'.repeat(60));
  }

  /**
   * البحث بالمعنى
   * Search by meaning
   */
  searchByMeaning(searchTerm: string): FoundationWord[] {
    const allWords = this.vocab.getAllWords();
    return allWords.filter(word => 
      word.coreMeaning.includes(searchTerm) ||
      word.arabic.includes(searchTerm) ||
      (word.english && word.english.includes(searchTerm))
    );
  }

  /**
   * الحصول على شجرة الكلمات المرتبطة
   * Get related words tree
   */
  getRelatedWordsTree(arabic: string, depth: number = 2): Map<string, FoundationWord[]> {
    const tree = new Map<string, FoundationWord[]>();
    const visited = new Set<string>();
    
    const explore = (word: string, currentDepth: number) => {
      if (currentDepth > depth || visited.has(word)) return;
      
      visited.add(word);
      const related = this.vocab.findRelatedWords(word);
      tree.set(word, related);
      
      if (currentDepth < depth) {
        for (const relatedWord of related) {
          explore(relatedWord.arabic, currentDepth + 1);
        }
      }
    };
    
    explore(arabic, 0);
    return tree;
  }
}

/**
 * Singleton instance
 */
let vocabularyInstance: CompleteFoundationVocabulary | null = null;

/**
 * الحصول على نسخة واحدة من القاموس
 * Get singleton vocabulary instance
 */
export function getCompleteVocabulary(): CompleteFoundationVocabulary {
  if (!vocabularyInstance) {
    vocabularyInstance = new CompleteFoundationVocabulary();
  }
  return vocabularyInstance;
}

/**
 * إعادة تعيين القاموس
 * Reset vocabulary
 */
export function resetVocabulary(): void {
  vocabularyInstance = null;
}

