/**
 * النظام المعجمي الموحد
 * Unified Lexicon System
 * 
 * يدمج جميع مصادر المفردات في نظام واحد:
 * - CompleteFoundationVocabulary (105 كلمة أساسية - أولوية عالية)
 * - ArramoozDictionaryAdapter (40,850 كلمة - أولوية متوسطة)
 * - CharacterMeaningExtractor (معاني الحروف - أولوية منخفضة)
 * 
 * Merges all vocabulary sources into one system:
 * - CompleteFoundationVocabulary (105 foundation words - high priority)
 * - ArramoozDictionaryAdapter (40,850 words - medium priority)
 * - CharacterMeaningExtractor (character meanings - low priority)
 */

import { FoundationWord, FoundationWordType, FoundationCategory } from './foundationVocabulary';
import { CompleteFoundationVocabulary } from './completeVocabulary';
import { ArramoozDictionaryAdapter } from './arramoozDictionaryAdapter';
import { LinguisticNormalizer } from './linguisticNormalizer';

/**
 * مستوى الأولوية
 * Priority Level
 */
export enum PriorityLevel {
  HIGH = 3,      // الكلمات الأساسية
  MEDIUM = 2,    // قاموس Arramooz
  LOW = 1        // معاني الحروف
}

/**
 * نتيجة البحث مع معلومات إضافية
 * Search result with additional info
 */
export interface LexiconSearchResult {
  word: FoundationWord;
  source: 'foundation' | 'arramooz' | 'character';
  priority: PriorityLevel;
  confidence: number;
}

/**
 * إحصائيات النظام المعجمي
 * Lexicon system statistics
 */
export interface LexiconStatistics {
  foundationWords: number;
  arramoozWords: number;
  totalWords: number;
  cacheSize: number;
  cacheHitRate: number;
}

/**
 * النظام المعجمي الموحد
 * Unified Lexicon System
 */
export class UnifiedLexiconSystem {
  private foundationVocab: CompleteFoundationVocabulary;
  private arramoozAdapter: ArramoozDictionaryAdapter;
  
  // التخزين المؤقت متعدد المستويات
  private cache: Map<string, LexiconSearchResult> = new Map();
  private rootCache: Map<string, FoundationWord[]> = new Map();
  
  // إحصائيات
  private cacheHits: number = 0;
  private cacheMisses: number = 0;
  
  private isInitialized: boolean = false;

  constructor() {
    this.foundationVocab = new CompleteFoundationVocabulary();
    this.arramoozAdapter = new ArramoozDictionaryAdapter();
  }

  /**
   * تهيئة النظام
   * Initialize the system
   */
  async initialize(): Promise<void> {
    if (this.isInitialized) {
      return;
    }

    console.log('🔄 جاري تهيئة النظام المعجمي الموحد...');
    
    // تحميل قاعدة بيانات Arramooz
    await this.arramoozAdapter.loadDatabase();
    
    this.isInitialized = true;
    
    const stats = this.getStatistics();
    console.log(`✅ تم تهيئة النظام المعجمي الموحد بنجاح!`);
    console.log(`   📚 الكلمات الأساسية: ${stats.foundationWords}`);
    console.log(`   📖 قاموس Arramooz: ${stats.arramoozWords}`);
    console.log(`   📊 الإجمالي: ${stats.totalWords} كلمة`);
  }

  /**
   * البحث عن كلمة (مع نظام الأولويات)
   * Search for a word (with priority system)
   */
  lookup(word: string): LexiconSearchResult | undefined {
    if (!this.isInitialized) {
      throw new Error('النظام غير مهيأ. استخدم initialize() أولاً.');
    }

    // تطبيع الكلمة
    const normalizedResult = LinguisticNormalizer.removeDefiniteArticle(word);
    const normalized = normalizedResult.clean;

    // 1. البحث في الذاكرة المؤقتة
    if (this.cache.has(normalized)) {
      this.cacheHits++;
      return this.cache.get(normalized);
    }

    this.cacheMisses++;

    // 2. البحث في الكلمات الأساسية (أولوية عالية)
    const foundationWord = this.foundationVocab.getWord(normalized);
    if (foundationWord) {
      const result: LexiconSearchResult = {
        word: foundationWord,
        source: 'foundation',
        priority: PriorityLevel.HIGH,
        confidence: 1.0
      };
      this.cache.set(normalized, result);
      return result;
    }

    // 3. البحث في قاموس Arramooz (أولوية متوسطة)
    const arramoozWord = this.arramoozAdapter.searchWord(normalized);
    if (arramoozWord) {
      const result: LexiconSearchResult = {
        word: arramoozWord,
        source: 'arramooz',
        priority: PriorityLevel.MEDIUM,
        confidence: 0.8
      };
      this.cache.set(normalized, result);
      return result;
    }

    // 4. لم يتم العثور على الكلمة
    return undefined;
  }

  /**
   * البحث بالجذر
   * Search by root
   */
  searchByRoot(root: string): FoundationWord[] {
    if (!this.isInitialized) {
      throw new Error('النظام غير مهيأ. استخدم initialize() أولاً.');
    }

    // البحث في الذاكرة المؤقتة
    if (this.rootCache.has(root)) {
      return this.rootCache.get(root)!;
    }

    const results: FoundationWord[] = [];

    // البحث في الكلمات الأساسية
    const foundationWords = this.foundationVocab.getAllWords();
    for (const word of foundationWords) {
      if (word.rootWord === root) {
        results.push(word);
      }
    }

    // البحث في Arramooz
    const arramoozWords = this.arramoozAdapter.searchByRoot(root);
    results.push(...arramoozWords);

    // حفظ في الذاكرة المؤقتة
    this.rootCache.set(root, results);

    return results;
  }

  /**
   * البحث المتقدم (يرجع جميع التطابقات مع الأولويات)
   * Advanced search (returns all matches with priorities)
   */
  advancedSearch(word: string): LexiconSearchResult[] {
    if (!this.isInitialized) {
      throw new Error('النظام غير مهيأ. استخدم initialize() أولاً.');
    }

    const results: LexiconSearchResult[] = [];
    const normalizedResult = LinguisticNormalizer.removeDefiniteArticle(word);
    const normalized = normalizedResult.clean;

    // البحث في الكلمات الأساسية
    const foundationWord = this.foundationVocab.getWord(normalized);
    if (foundationWord) {
      results.push({
        word: foundationWord,
        source: 'foundation',
        priority: PriorityLevel.HIGH,
        confidence: 1.0
      });
    }

    // البحث في Arramooz
    const arramoozWord = this.arramoozAdapter.searchWord(normalized);
    if (arramoozWord) {
      results.push({
        word: arramoozWord,
        source: 'arramooz',
        priority: PriorityLevel.MEDIUM,
        confidence: 0.8
      });
    }

    // ترتيب حسب الأولوية
    results.sort((a, b) => b.priority - a.priority);

    return results;
  }

  /**
   * الحصول على الكلمة الأفضل (أعلى أولوية)
   * Get the best word (highest priority)
   */
  getBestMatch(word: string): FoundationWord | undefined {
    const result = this.lookup(word);
    return result?.word;
  }

  /**
   * التحقق من وجود كلمة
   * Check if word exists
   */
  hasWord(word: string): boolean {
    return this.lookup(word) !== undefined;
  }

  /**
   * الحصول على جميع الكلمات من مصدر معين
   * Get all words from a specific source
   */
  getWordsBySource(source: 'foundation' | 'arramooz'): FoundationWord[] {
    if (!this.isInitialized) {
      throw new Error('النظام غير مهيأ. استخدم initialize() أولاً.');
    }

    if (source === 'foundation') {
      return this.foundationVocab.getAllWords();
    }

    // لا يمكن الحصول على جميع كلمات Arramooz (40,850 كلمة)
    // يجب استخدام البحث بدلاً من ذلك
    return [];
  }

  /**
   * مسح الذاكرة المؤقتة
   * Clear cache
   */
  clearCache(): void {
    this.cache.clear();
    this.rootCache.clear();
    this.cacheHits = 0;
    this.cacheMisses = 0;
  }

  /**
   * الحصول على إحصائيات
   * Get statistics
   */
  getStatistics(): LexiconStatistics {
    const foundationWords = this.foundationVocab.getAllWords().length;
    const arramoozStats = this.arramoozAdapter.getStatistics();
    
    const totalRequests = this.cacheHits + this.cacheMisses;
    const cacheHitRate = totalRequests > 0 ? this.cacheHits / totalRequests : 0;

    return {
      foundationWords: foundationWords,
      arramoozWords: arramoozStats.total,
      totalWords: foundationWords + arramoozStats.total,
      cacheSize: this.cache.size,
      cacheHitRate: cacheHitRate
    };
  }

  /**
   * إغلاق النظام
   * Close the system
   */
  close(): void {
    this.arramoozAdapter.close();
    this.clearCache();
    this.isInitialized = false;
  }

  /**
   * الحصول على معلومات تفصيلية عن كلمة
   * Get detailed information about a word
   */
  getWordDetails(word: string): {
    exists: boolean;
    sources: string[];
    priority: PriorityLevel | null;
    root?: string;
    relatedWords: string[];
  } {
    const results = this.advancedSearch(word);
    
    if (results.length === 0) {
      return {
        exists: false,
        sources: [],
        priority: null,
        relatedWords: []
      };
    }

    const bestResult = results[0];
    
    return {
      exists: true,
      sources: results.map(r => r.source),
      priority: bestResult.priority,
      root: bestResult.word.rootWord,
      relatedWords: bestResult.word.relatedWords
    };
  }
}

