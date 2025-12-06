/**
 * محول قاعدة بيانات Arramooz
 * Arramooz Dictionary Adapter
 * 
 * يحول بيانات قاعدة بيانات Arramooz (40,850 كلمة) إلى صيغة FoundationWord
 * Converts Arramooz database data (40,850 words) to FoundationWord format
 */

import initSqlJs, { Database } from 'sql.js';
import * as fs from 'fs';
import * as path from 'path';
import { FoundationWord, FoundationWordType, FoundationCategory } from './foundationVocabulary';
import { LinguisticNormalizer } from './linguisticNormalizer';

/**
 * كلمة من قاعدة بيانات Arramooz (اسم)
 * Arramooz Noun Entry
 */
interface ArramoozNoun {
  id: number;
  vocalized: string;
  unvocalized: string;
  normalized: string;
  stamped: string;
  wordtype: string;
  root: string;
  wazn: string;
  category: string;
  original: string;
  gender: string;
  feminin: string;
  masculin: string;
  number: string;
  single: string;
  broken_plural: string;
  defined: number;
  mankous: number;
  feminable: number;
  dualable: number;
  masculin_plural: number;
  feminin_plural: number;
  mamnou3_sarf: number;
  relative: number;
  w_suffix: number;
  hm_suffix: number;
  kal_prefix: number;
  ha_suffix: number;
  k_prefix: number;
  annex: number;
  definition: string;
  note: string;
}

/**
 * كلمة من قاعدة بيانات Arramooz (فعل)
 * Arramooz Verb Entry
 */
interface ArramoozVerb {
  id: number;
  vocalized: string;
  unvocalized: string;
  root: string;
  normalized: string;
  stamped: string;
  future_type: string;
  triliteral: number;
  transitive: number;
  double_trans: number;
  think_trans: number;
  unthink_trans: number;
  reflexive_trans: number;
  past: number;
  future: number;
  imperative: number;
  passive: number;
  future_moode: number;
  confirmed: number;
}

/**
 * محول قاعدة بيانات Arramooz
 * Arramooz Dictionary Adapter
 */
export class ArramoozDictionaryAdapter {
  private db: Database | null = null;
  private cache: Map<string, FoundationWord> = new Map();
  private rootCache: Map<string, FoundationWord[]> = new Map();
  private isLoaded: boolean = false;
  
  private readonly DB_PATH = 'src/baserah/lexicon/databases/arramooz_dictionary.db';

  /**
   * تحميل قاعدة البيانات
   * Load the database
   */
  async loadDatabase(): Promise<void> {
    if (this.isLoaded) {
      return;
    }

    try {
      const SQL = await initSqlJs();
      const buffer = fs.readFileSync(this.DB_PATH);
      this.db = new SQL.Database(buffer);
      this.isLoaded = true;
      console.log('✅ تم تحميل قاعدة بيانات Arramooz بنجاح (40,850 كلمة)');
    } catch (error) {
      console.error('❌ خطأ في تحميل قاعدة بيانات Arramooz:', error);
      throw error;
    }
  }

  /**
   * البحث عن كلمة
   * Search for a word
   */
  searchWord(word: string): FoundationWord | undefined {
    if (!this.isLoaded || !this.db) {
      throw new Error('قاعدة البيانات غير محملة. استخدم loadDatabase() أولاً.');
    }

    // تطبيع الكلمة
    const normalizedResult = LinguisticNormalizer.removeDefiniteArticle(word);
    const normalized = normalizedResult.clean;

    // البحث في الذاكرة المؤقتة
    if (this.cache.has(normalized)) {
      return this.cache.get(normalized);
    }

    // البحث في جدول الأسماء
    let result = this.searchInNouns(normalized);
    if (result) {
      this.cache.set(normalized, result);
      return result;
    }

    // البحث في جدول الأفعال
    result = this.searchInVerbs(normalized);
    if (result) {
      this.cache.set(normalized, result);
      return result;
    }

    return undefined;
  }

  /**
   * البحث في جدول الأسماء
   * Search in nouns table
   */
  private searchInNouns(word: string): FoundationWord | undefined {
    if (!this.db) return undefined;

    try {
      const query = `
        SELECT * FROM nouns 
        WHERE unvocalized = ? OR normalized = ? OR stamped = ?
        LIMIT 1
      `;
      
      const result = this.db.exec(query, [word, word, word]);
      
      if (!result.length || !result[0].values.length) {
        return undefined;
      }

      const row = result[0].values[0];
      const columns = result[0].columns;
      const noun = this.rowToNoun(row, columns);
      
      return this.convertNounToFoundationWord(noun);
    } catch (error) {
      console.error('خطأ في البحث في جدول الأسماء:', error);
      return undefined;
    }
  }

  /**
   * البحث في جدول الأفعال
   * Search in verbs table
   */
  private searchInVerbs(word: string): FoundationWord | undefined {
    if (!this.db) return undefined;

    try {
      const query = `
        SELECT * FROM verbs 
        WHERE unvocalized = ? OR normalized = ? OR stamped = ?
        LIMIT 1
      `;
      
      const result = this.db.exec(query, [word, word, word]);
      
      if (!result.length || !result[0].values.length) {
        return undefined;
      }

      const row = result[0].values[0];
      const columns = result[0].columns;
      const verb = this.rowToVerb(row, columns);
      
      return this.convertVerbToFoundationWord(verb);
    } catch (error) {
      console.error('خطأ في البحث في جدول الأفعال:', error);
      return undefined;
    }
  }

  /**
   * البحث بالجذر
   * Search by root
   */
  searchByRoot(root: string): FoundationWord[] {
    if (!this.isLoaded || !this.db) {
      throw new Error('قاعدة البيانات غير محملة. استخدم loadDatabase() أولاً.');
    }

    // البحث في الذاكرة المؤقتة
    if (this.rootCache.has(root)) {
      return this.rootCache.get(root)!;
    }

    const results: FoundationWord[] = [];

    // البحث في الأسماء
    try {
      const nounQuery = `SELECT * FROM nouns WHERE root = ? LIMIT 20`;
      const nounResult = this.db.exec(nounQuery, [root]);
      
      if (nounResult.length && nounResult[0].values.length) {
        for (const row of nounResult[0].values) {
          const noun = this.rowToNoun(row, nounResult[0].columns);
          const foundationWord = this.convertNounToFoundationWord(noun);
          if (foundationWord) {
            results.push(foundationWord);
          }
        }
      }
    } catch (error) {
      console.error('خطأ في البحث بالجذر في الأسماء:', error);
    }

    // البحث في الأفعال
    try {
      const verbQuery = `SELECT * FROM verbs WHERE root = ? LIMIT 20`;
      const verbResult = this.db.exec(verbQuery, [root]);
      
      if (verbResult.length && verbResult[0].values.length) {
        for (const row of verbResult[0].values) {
          const verb = this.rowToVerb(row, verbResult[0].columns);
          const foundationWord = this.convertVerbToFoundationWord(verb);
          if (foundationWord) {
            results.push(foundationWord);
          }
        }
      }
    } catch (error) {
      console.error('خطأ في البحث بالجذر في الأفعال:', error);
    }

    // حفظ في الذاكرة المؤقتة
    this.rootCache.set(root, results);
    
    return results;
  }

  /**
   * تحويل صف إلى كائن اسم
   * Convert row to noun object
   */
  private rowToNoun(row: any[], columns: string[]): ArramoozNoun {
    const noun: any = {};
    columns.forEach((col, index) => {
      noun[col] = row[index];
    });
    return noun as ArramoozNoun;
  }

  /**
   * تحويل صف إلى كائن فعل
   * Convert row to verb object
   */
  private rowToVerb(row: any[], columns: string[]): ArramoozVerb {
    const verb: any = {};
    columns.forEach((col, index) => {
      verb[col] = row[index];
    });
    return verb as ArramoozVerb;
  }

  /**
   * تحويل اسم Arramooz إلى FoundationWord
   * Convert Arramooz noun to FoundationWord
   */
  private convertNounToFoundationWord(noun: ArramoozNoun): FoundationWord | undefined {
    if (!noun.unvocalized) return undefined;

    // تحديد النوع بناءً على wordtype
    const type = this.determineNounType(noun.wordtype, noun.category);
    
    // تحديد الفئة
    const category = FoundationCategory.ENTITY_EXISTENCE; // افتراضي

    return {
      arabic: noun.unvocalized,
      english: undefined,
      type: type,
      category: category,
      coreMeaning: noun.definition || `${noun.wordtype} من ${noun.original || noun.root}`,
      relatedWords: this.extractRelatedWords(noun),
      rootWord: noun.root || undefined,
      meaningAngle: noun.wazn || undefined,
      examples: [],
      weight: 0.5 // وزن متوسط للكلمات من Arramooz
    };
  }

  /**
   * تحويل فعل Arramooz إلى FoundationWord
   * Convert Arramooz verb to FoundationWord
   */
  private convertVerbToFoundationWord(verb: ArramoozVerb): FoundationWord | undefined {
    if (!verb.unvocalized) return undefined;

    return {
      arabic: verb.unvocalized,
      english: undefined,
      type: FoundationWordType.ACTION,
      category: FoundationCategory.BASIC_ACTIONS,
      coreMeaning: `فعل من الجذر ${verb.root}`,
      relatedWords: [],
      rootWord: verb.root || undefined,
      meaningAngle: verb.future_type || undefined,
      examples: [],
      weight: 0.5
    };
  }

  /**
   * تحديد نوع الاسم
   * Determine noun type
   */
  private determineNounType(wordtype: string, category: string): FoundationWordType {
    if (wordtype.includes('فاعل') || wordtype.includes('مفعول')) {
      return FoundationWordType.ENTITY;
    }
    if (wordtype.includes('صفة')) {
      return FoundationWordType.PROPERTY;
    }
    if (category === 'حالة') {
      return FoundationWordType.STATE;
    }
    return FoundationWordType.ENTITY; // افتراضي
  }

  /**
   * استخراج الكلمات المرتبطة
   * Extract related words
   */
  private extractRelatedWords(noun: ArramoozNoun): string[] {
    const related: string[] = [];
    
    if (noun.feminin) related.push(noun.feminin);
    if (noun.masculin) related.push(noun.masculin);
    if (noun.single) related.push(noun.single);
    if (noun.broken_plural) related.push(noun.broken_plural);
    
    return related.filter(w => w && w.trim().length > 0);
  }

  /**
   * إغلاق قاعدة البيانات
   * Close the database
   */
  close(): void {
    if (this.db) {
      this.db.close();
      this.db = null;
      this.isLoaded = false;
    }
  }

  /**
   * الحصول على إحصائيات
   * Get statistics
   */
  getStatistics(): { nouns: number; verbs: number; total: number } {
    if (!this.isLoaded || !this.db) {
      return { nouns: 0, verbs: 0, total: 0 };
    }

    try {
      const nounCount = this.db.exec('SELECT COUNT(*) FROM nouns')[0].values[0][0] as number;
      const verbCount = this.db.exec('SELECT COUNT(*) FROM verbs')[0].values[0][0] as number;
      
      return {
        nouns: nounCount,
        verbs: verbCount,
        total: nounCount + verbCount
      };
    } catch (error) {
      console.error('خطأ في الحصول على الإحصائيات:', error);
      return { nouns: 0, verbs: 0, total: 0 };
    }
  }
}

