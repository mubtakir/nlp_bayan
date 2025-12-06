/**
 * قاموس الكلمات الأساسية - Foundation Vocabulary
 * 
 * هذا القاموس يحتوي على الكلمات الأساس التي تُبنى عليها اللغة
 * كل كلمة هي جذر يتفرع منه كلمات أخرى تخصص المعنى
 * 
 * This vocabulary contains the foundation words upon which language is built
 * Each word is a root from which other words branch to specialize meaning
 */

/**
 * نوع الكلمة الأساسية
 * Foundation Word Type
 */
export enum FoundationWordType {
  // الكيانات الأساسية - Basic Entities
  ENTITY = 'كيان',
  
  // الخصائص - Properties
  PROPERTY = 'خاصية',
  
  // الأفعال - Actions
  ACTION = 'فعل',
  
  // الحالات - States
  STATE = 'حالة',
  
  // العلاقات - Relations
  RELATION = 'علاقة',
  
  // الاتجاهات - Directions
  DIRECTION = 'اتجاه',
  
  // الكميات - Quantities
  QUANTITY = 'كمية',
  
  // الزمن - Time
  TIME = 'زمن'
}

/**
 * فئة الكلمة الأساسية
 * Foundation Word Category
 */
export enum FoundationCategory {
  // البيئة الأولية - Initial Environment
  INITIAL_ENVIRONMENT = 'البيئة_الأولية',
  
  // الكيان والوجود - Entity & Existence
  ENTITY_EXISTENCE = 'الكيان_والوجود',
  
  // الخصائص الفيزيائية - Physical Properties
  PHYSICAL = 'فيزيائية',
  
  // الخصائص الحسية - Sensory Properties
  SENSORY = 'حسية',
  
  // الحالات النفسية - Psychological States
  PSYCHOLOGICAL = 'نفسية',
  
  // العلاقات الاجتماعية - Social Relations
  SOCIAL = 'اجتماعية',
  
  // الأفعال الأساسية - Basic Actions
  BASIC_ACTIONS = 'أفعال_أساسية',
  
  // التحولات - Transformations
  TRANSFORMATIONS = 'تحولات',
  
  // البيئة الطبيعية - Natural Environment
  NATURAL_ENVIRONMENT = 'بيئة_طبيعية'
}

/**
 * كلمة أساسية
 * Foundation Word
 */
export interface FoundationWord {
  // الكلمة العربية
  arabic: string;
  
  // الكلمة الإنجليزية (اختياري)
  english?: string;
  
  // نوع الكلمة
  type: FoundationWordType;
  
  // الفئة
  category: FoundationCategory;
  
  // المعنى الأساسي
  coreMeaning: string;
  
  // الكلمات المرتبطة (المتفرعة)
  relatedWords: string[];
  
  // الكلمة الأصل (إذا كانت متفرعة)
  rootWord?: string;
  
  // زاوية المعنى (كيف تخصص هذه الكلمة المعنى الأصلي)
  meaningAngle?: string;
  
  // أمثلة الاستخدام
  examples: string[];
  
  // الوزن/الأهمية (0-1)
  weight: number;
}

/**
 * قاموس الكلمات الأساسية
 * Foundation Vocabulary Dictionary
 */
export class FoundationVocabulary {
  private words: Map<string, FoundationWord> = new Map();
  private categories: Map<FoundationCategory, FoundationWord[]> = new Map();
  private types: Map<FoundationWordType, FoundationWord[]> = new Map();

  constructor() {
    this.initializeVocabulary();
  }

  /**
   * تهيئة القاموس بالكلمات الأساسية
   * Initialize vocabulary with foundation words
   */
  private initializeVocabulary(): void {
    // 1. البيئة الأولية - Initial Environment
    this.addWord({
      arabic: 'أرض',
      english: 'ground',
      type: FoundationWordType.ENTITY,
      category: FoundationCategory.INITIAL_ENVIRONMENT,
      coreMeaning: 'السطح الذي نقف عليه',
      relatedWords: ['تراب', 'أرضية', 'قاع', 'قعر'],
      examples: ['الأرض صلبة', 'سقط على الأرض'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'سماء',
      english: 'sky',
      type: FoundationWordType.ENTITY,
      category: FoundationCategory.INITIAL_ENVIRONMENT,
      coreMeaning: 'الفضاء فوقنا',
      relatedWords: ['سقف', 'علو', 'فضاء'],
      examples: ['السماء زرقاء', 'نظر إلى السماء'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'شمس',
      english: 'sun',
      type: FoundationWordType.ENTITY,
      category: FoundationCategory.INITIAL_ENVIRONMENT,
      coreMeaning: 'مصدر الضوء والحرارة في النهار',
      relatedWords: ['ضوء', 'نهار', 'شروق', 'غروب'],
      examples: ['الشمس ساطعة', 'طلعت الشمس'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'قمر',
      english: 'moon',
      type: FoundationWordType.ENTITY,
      category: FoundationCategory.INITIAL_ENVIRONMENT,
      coreMeaning: 'مصدر النور في الليل',
      relatedWords: ['نور', 'ليل', 'هلال', 'بدر'],
      examples: ['القمر منير', 'ظهر القمر'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'ضوء',
      english: 'light',
      type: FoundationWordType.PROPERTY,
      category: FoundationCategory.INITIAL_ENVIRONMENT,
      coreMeaning: 'ما يجعلنا نرى',
      relatedWords: ['إضاءة', 'نور', 'إشراق', 'لمعان'],
      examples: ['الضوء ساطع', 'أضاء المكان'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'نور',
      english: 'illumination',
      type: FoundationWordType.PROPERTY,
      category: FoundationCategory.INITIAL_ENVIRONMENT,
      coreMeaning: 'ضوء خفيف',
      relatedWords: ['إنارة', 'ضياء', 'بريق'],
      examples: ['نور القمر', 'أنار الطريق'],
      weight: 0.9
    });

    this.addWord({
      arabic: 'ليل',
      english: 'night',
      type: FoundationWordType.TIME,
      category: FoundationCategory.INITIAL_ENVIRONMENT,
      coreMeaning: 'وقت الظلام',
      relatedWords: ['ظلام', 'ظلمة', 'عتمة'],
      examples: ['الليل مظلم', 'جاء الليل'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'نهار',
      english: 'day',
      type: FoundationWordType.TIME,
      category: FoundationCategory.INITIAL_ENVIRONMENT,
      coreMeaning: 'وقت الضوء',
      relatedWords: ['يوم', 'صباح', 'نهارا'],
      examples: ['النهار طويل', 'في النهار'],
      weight: 1.0
    });

    // 2. الكيان والوجود - Entity & Existence
    this.addWord({
      arabic: 'شيء',
      english: 'thing',
      type: FoundationWordType.ENTITY,
      category: FoundationCategory.ENTITY_EXISTENCE,
      coreMeaning: 'كيان موجود',
      relatedWords: ['كائن', 'موجود', 'جسم', 'كيان'],
      examples: ['هذا شيء غريب', 'رأيت شيئا'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'بيئة',
      english: 'environment',
      type: FoundationWordType.ENTITY,
      category: FoundationCategory.ENTITY_EXISTENCE,
      coreMeaning: 'المحيط الذي يعيش فيه الشيء',
      relatedWords: ['محيط', 'وسط', 'مكان'],
      examples: ['البيئة نظيفة', 'يعيش في بيئة'],
      weight: 0.9
    });

    this.addWord({
      arabic: 'محيط',
      english: 'surroundings',
      type: FoundationWordType.ENTITY,
      category: FoundationCategory.ENTITY_EXISTENCE,
      coreMeaning: 'ما يحيط بالشيء',
      relatedWords: ['جوار', 'حول', 'دائرة'],
      examples: ['المحيط الهادئ', 'في محيطه'],
      weight: 0.8
    });

    // 3. الاتجاهات - Directions
    this.addWord({
      arabic: 'يمين',
      english: 'right',
      type: FoundationWordType.DIRECTION,
      category: FoundationCategory.ENTITY_EXISTENCE,
      coreMeaning: 'الجهة اليمنى',
      relatedWords: ['يميني', 'أيمن'],
      examples: ['اتجه يمينا', 'على اليمين'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'يسار',
      english: 'left',
      type: FoundationWordType.DIRECTION,
      category: FoundationCategory.ENTITY_EXISTENCE,
      coreMeaning: 'الجهة اليسرى',
      relatedWords: ['يساري', 'أيسر', 'شمال'],
      examples: ['اتجه يسارا', 'على اليسار'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'أمام',
      english: 'front',
      type: FoundationWordType.DIRECTION,
      category: FoundationCategory.ENTITY_EXISTENCE,
      coreMeaning: 'الجهة الأمامية',
      relatedWords: ['قدام', 'وجه', 'مواجهة'],
      examples: ['أمامك', 'في الأمام'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'خلف',
      english: 'behind',
      type: FoundationWordType.DIRECTION,
      category: FoundationCategory.ENTITY_EXISTENCE,
      coreMeaning: 'الجهة الخلفية',
      relatedWords: ['وراء', 'ظهر', 'خلفي'],
      examples: ['خلفك', 'من الخلف'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'فوق',
      english: 'above',
      type: FoundationWordType.DIRECTION,
      category: FoundationCategory.ENTITY_EXISTENCE,
      coreMeaning: 'الجهة العلوية',
      relatedWords: ['علو', 'أعلى', 'سماء'],
      examples: ['فوق الطاولة', 'في الأعلى'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'تحت',
      english: 'below',
      type: FoundationWordType.DIRECTION,
      category: FoundationCategory.ENTITY_EXISTENCE,
      coreMeaning: 'الجهة السفلية',
      relatedWords: ['أسفل', 'قاع', 'أرض'],
      examples: ['تحت الطاولة', 'في الأسفل'],
      weight: 1.0
    });

    // 4. الخصائص الفيزيائية - Physical Properties
    this.addWord({
      arabic: 'أجوف',
      english: 'hollow',
      type: FoundationWordType.PROPERTY,
      category: FoundationCategory.PHYSICAL,
      coreMeaning: 'له جوف من الداخل',
      relatedWords: ['جوف', 'فراغ', 'تجويف'],
      examples: ['إناء أجوف', 'شيء أجوف'],
      weight: 0.9
    });

    this.addWord({
      arabic: 'صلد',
      english: 'solid',
      type: FoundationWordType.PROPERTY,
      category: FoundationCategory.PHYSICAL,
      coreMeaning: 'لا جوف له، صلب',
      relatedWords: ['صلب', 'متين', 'قاسي'],
      examples: ['حجر صلد', 'جسم صلد'],
      weight: 0.9
    });

    this.addWord({
      arabic: 'ممتلئ',
      english: 'full',
      type: FoundationWordType.STATE,
      category: FoundationCategory.PHYSICAL,
      coreMeaning: 'في جوفه شيء',
      relatedWords: ['امتلاء', 'ملء', 'مليء'],
      examples: ['الكأس ممتلئ', 'امتلأ الإناء'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'فارغ',
      english: 'empty',
      type: FoundationWordType.STATE,
      category: FoundationCategory.PHYSICAL,
      coreMeaning: 'لا شيء في جوفه',
      relatedWords: ['فراغ', 'خلاء', 'خالي'],
      examples: ['الكأس فارغ', 'فرغ الإناء'],
      weight: 1.0
    });

    // 5. العلاقات المكانية - Spatial Relations
    this.addWord({
      arabic: 'قرب',
      english: 'nearness',
      type: FoundationWordType.RELATION,
      category: FoundationCategory.PHYSICAL,
      coreMeaning: 'المسافة قليلة',
      relatedWords: ['قريب', 'دنو', 'جوار'],
      examples: ['قرب منه', 'على مقربة'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'بعد',
      english: 'distance',
      type: FoundationWordType.RELATION,
      category: FoundationCategory.PHYSICAL,
      coreMeaning: 'المسافة كبيرة',
      relatedWords: ['بعيد', 'بُعد', 'نأي'],
      examples: ['بعد عنه', 'على بُعد'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'تماس',
      english: 'contact',
      type: FoundationWordType.RELATION,
      category: FoundationCategory.PHYSICAL,
      coreMeaning: 'التصاق شيئين',
      relatedWords: ['لمس', 'مس', 'التصاق'],
      examples: ['تماس الجسمين', 'في تماس'],
      weight: 0.9
    });

    // 6. الحاجات الأساسية - Basic Needs
    this.addWord({
      arabic: 'جائع',
      english: 'hungry',
      type: FoundationWordType.STATE,
      category: FoundationCategory.PHYSICAL,
      coreMeaning: 'يحتاج إلى طعام',
      relatedWords: ['جوع', 'مجاعة', 'جياع'],
      examples: ['أنا جائع', 'شعر بالجوع'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'شبع',
      english: 'satiation',
      type: FoundationWordType.STATE,
      category: FoundationCategory.PHYSICAL,
      coreMeaning: 'امتلأ من الطعام',
      relatedWords: ['شبعان', 'تشبع', 'شباع'],
      examples: ['شبع من الطعام', 'أنا شبعان'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'حاجة',
      english: 'need',
      type: FoundationWordType.STATE,
      category: FoundationCategory.PHYSICAL,
      coreMeaning: 'نقص يحتاج إلى سد',
      relatedWords: ['احتياج', 'ضرورة', 'لزوم'],
      examples: ['لديه حاجة', 'يحتاج إلى'],
      weight: 1.0
    });

    // 7. الأفعال الأساسية - Basic Actions
    this.addWord({
      arabic: 'أكل',
      english: 'eat',
      type: FoundationWordType.ACTION,
      category: FoundationCategory.BASIC_ACTIONS,
      coreMeaning: 'إدخال الطعام إلى الجوف',
      relatedWords: ['طعام', 'أكلة', 'آكل'],
      examples: ['أكل الطعام', 'يأكل التفاحة'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'ابتلع',
      english: 'swallow',
      type: FoundationWordType.ACTION,
      category: FoundationCategory.BASIC_ACTIONS,
      coreMeaning: 'إدخال شيء إلى الجوف دفعة واحدة',
      relatedWords: ['بلع', 'ابتلاع', 'بالع'],
      examples: ['ابتلع الدواء', 'بلع اللقمة'],
      weight: 0.9
    });

    // 8. العلاقات الاجتماعية - Social Relations
    this.addWord({
      arabic: 'ود',
      english: 'affection',
      type: FoundationWordType.RELATION,
      category: FoundationCategory.SOCIAL,
      coreMeaning: 'محبة وقرب',
      relatedWords: ['مودة', 'حب', 'ألفة'],
      examples: ['بينهما ود', 'ود صادق'],
      weight: 0.9
    });

    this.addWord({
      arabic: 'نفور',
      english: 'aversion',
      type: FoundationWordType.RELATION,
      category: FoundationCategory.SOCIAL,
      coreMeaning: 'كراهة وابتعاد',
      relatedWords: ['كره', 'بغض', 'نافر'],
      examples: ['نفور منه', 'ينفر من'],
      weight: 0.9
    });

    this.addWord({
      arabic: 'اعتداء',
      english: 'aggression',
      type: FoundationWordType.ACTION,
      category: FoundationCategory.SOCIAL,
      coreMeaning: 'تجاوز الحد والإيذاء',
      relatedWords: ['تجاوز', 'ظلم', 'معتدي'],
      examples: ['اعتداء على حقه', 'اعتدى عليه'],
      weight: 0.9
    });

    this.addWord({
      arabic: 'شر',
      english: 'evil',
      type: FoundationWordType.PROPERTY,
      category: FoundationCategory.PSYCHOLOGICAL,
      coreMeaning: 'سوء وإيذاء',
      relatedWords: ['شرير', 'خبث', 'سوء'],
      examples: ['فعل الشر', 'شرير القلب'],
      weight: 0.9
    });

    this.addWord({
      arabic: 'طيب',
      english: 'good',
      type: FoundationWordType.PROPERTY,
      category: FoundationCategory.PSYCHOLOGICAL,
      coreMeaning: 'حسن وخير',
      relatedWords: ['خير', 'حسن', 'طيبة'],
      examples: ['رجل طيب', 'قلب طيب'],
      weight: 0.9
    });

    this.addWord({
      arabic: 'مسكين',
      english: 'poor',
      type: FoundationWordType.STATE,
      category: FoundationCategory.SOCIAL,
      coreMeaning: 'ضعيف محتاج',
      relatedWords: ['فقير', 'ضعيف', 'مسكنة'],
      examples: ['رجل مسكين', 'حال مسكين'],
      weight: 0.8
    });

    this.addWord({
      arabic: 'متسامح',
      english: 'forgiving',
      type: FoundationWordType.PROPERTY,
      category: FoundationCategory.PSYCHOLOGICAL,
      coreMeaning: 'يعفو ولا ينتقم',
      relatedWords: ['تسامح', 'عفو', 'صفح'],
      examples: ['رجل متسامح', 'تسامح معه'],
      weight: 0.8
    });

    // 9. الإحساس والشعور - Sensation & Feeling
    this.addWord({
      arabic: 'ألم',
      english: 'pain',
      type: FoundationWordType.STATE,
      category: FoundationCategory.PSYCHOLOGICAL,
      coreMeaning: 'إحساس بالوجع',
      relatedWords: ['وجع', 'توجع', 'مؤلم'],
      examples: ['شعر بالألم', 'ألم شديد'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'إحساس',
      english: 'sensation',
      type: FoundationWordType.STATE,
      category: FoundationCategory.PSYCHOLOGICAL,
      coreMeaning: 'الشعور بشيء',
      relatedWords: ['حس', 'شعور', 'إدراك'],
      examples: ['لديه إحساس', 'أحس بالبرد'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'شعور',
      english: 'feeling',
      type: FoundationWordType.STATE,
      category: FoundationCategory.PSYCHOLOGICAL,
      coreMeaning: 'إدراك داخلي',
      relatedWords: ['شعر', 'إحساس', 'وجدان'],
      examples: ['شعور بالفرح', 'يشعر بالحزن'],
      weight: 1.0
    });

    this.addWord({
      arabic: 'خدش',
      english: 'scratch',
      type: FoundationWordType.ACTION,
      category: FoundationCategory.BASIC_ACTIONS,
      coreMeaning: 'جرح سطحي',
      relatedWords: ['خدشة', 'جرح', 'كشط'],
      examples: ['خدش الجلد', 'خدشة بسيطة'],
      weight: 0.8
    });
  }

  /**
   * إضافة كلمة أساسية
   * Add foundation word
   */
  addWord(word: FoundationWord): void {
    this.words.set(word.arabic, word);

    // إضافة إلى الفئة
    if (!this.categories.has(word.category)) {
      this.categories.set(word.category, []);
    }
    this.categories.get(word.category)!.push(word);

    // إضافة إلى النوع
    if (!this.types.has(word.type)) {
      this.types.set(word.type, []);
    }
    this.types.get(word.type)!.push(word);
  }

  /**
   * الحصول على كلمة
   * Get word
   */
  getWord(arabic: string): FoundationWord | undefined {
    return this.words.get(arabic);
  }

  /**
   * الحصول على كلمات حسب الفئة
   * Get words by category
   */
  getWordsByCategory(category: FoundationCategory): FoundationWord[] {
    return this.categories.get(category) || [];
  }

  /**
   * الحصول على كلمات حسب النوع
   * Get words by type
   */
  getWordsByType(type: FoundationWordType): FoundationWord[] {
    return this.types.get(type) || [];
  }

  /**
   * البحث عن كلمات مرتبطة
   * Find related words
   */
  findRelatedWords(arabic: string): FoundationWord[] {
    const word = this.getWord(arabic);
    if (!word) return [];

    const related: FoundationWord[] = [];
    for (const relatedArabic of word.relatedWords) {
      const relatedWord = this.getWord(relatedArabic);
      if (relatedWord) {
        related.push(relatedWord);
      }
    }

    return related;
  }

  /**
   * الحصول على جميع الكلمات
   * Get all words
   */
  getAllWords(): FoundationWord[] {
    return Array.from(this.words.values());
  }

  /**
   * عدد الكلمات
   * Word count
   */
  getWordCount(): number {
    return this.words.size;
  }
}

