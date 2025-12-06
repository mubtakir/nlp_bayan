/**
 * إكمال قاموس الكلمات الأساسية - Complete Foundation Vocabulary
 * 
 * هذا الملف يحتوي على باقي الكلمات الأساسية
 */

import { FoundationWord, FoundationWordType, FoundationCategory, FoundationVocabulary } from './foundationVocabulary';

/**
 * إضافة الكلمات الأساسية المتبقية
 * Add remaining foundation words
 */
export function addCompleteVocabulary(vocab: FoundationVocabulary): void {
  // 15. المعرفة والشك - Knowledge & Doubt
  vocab.addWord({
    arabic: 'شك',
    english: 'doubt',
    type: FoundationWordType.STATE,
    category: FoundationCategory.PSYCHOLOGICAL,
    coreMeaning: 'عدم اليقين',
    relatedWords: ['شكوك', 'مشكوك', 'ارتياب'],
    examples: ['لديه شك', 'شك في الأمر'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'يقين',
    english: 'certainty',
    type: FoundationWordType.STATE,
    category: FoundationCategory.PSYCHOLOGICAL,
    coreMeaning: 'العلم الثابت',
    relatedWords: ['متيقن', 'تيقن', 'قطع'],
    examples: ['لديه يقين', 'على يقين'],
    weight: 0.9
  });

  // 16. الأنشطة - Activities
  vocab.addWord({
    arabic: 'ممارسة',
    english: 'practice',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'القيام بعمل بانتظام',
    relatedWords: ['مارس', 'ممارس', 'مران'],
    examples: ['ممارسة الرياضة', 'يمارس العمل'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'لعب',
    english: 'play',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'النشاط للمتعة',
    relatedWords: ['لعبة', 'لاعب', 'ملعب'],
    examples: ['لعب الكرة', 'لعبة ممتعة'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'مشي',
    english: 'walk',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'الحركة على القدمين',
    relatedWords: ['مشى', 'ماشي', 'مشاء'],
    examples: ['مشى في الطريق', 'المشي مفيد'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'ركض',
    english: 'run',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'الحركة السريعة على القدمين',
    relatedWords: ['ركض', 'راكض', 'عدو'],
    examples: ['ركض بسرعة', 'ركض في السباق'],
    weight: 1.0
  });

  // 17. أعضاء الجسم - Body Parts
  vocab.addWord({
    arabic: 'يد',
    english: 'hand',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.PHYSICAL,
    coreMeaning: 'العضو للإمساك',
    relatedWords: ['أيدي', 'كف', 'أصابع'],
    examples: ['رفع يده', 'يد قوية'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'رجل',
    english: 'leg',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.PHYSICAL,
    coreMeaning: 'العضو للمشي',
    relatedWords: ['أرجل', 'ساق', 'فخذ'],
    examples: ['كسرت رجله', 'رجل طويلة'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'قدم',
    english: 'foot',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.PHYSICAL,
    coreMeaning: 'نهاية الرجل',
    relatedWords: ['أقدام', 'قدمان', 'كعب'],
    examples: ['غسل قدميه', 'قدم كبيرة'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'وجه',
    english: 'face',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.PHYSICAL,
    coreMeaning: 'مقدمة الرأس',
    relatedWords: ['وجوه', 'محيا', 'سحنة'],
    examples: ['وجه جميل', 'غسل وجهه'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'عين',
    english: 'eye',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.PHYSICAL,
    coreMeaning: 'العضو للرؤية',
    relatedWords: ['عيون', 'أعين', 'بصر'],
    examples: ['عين زرقاء', 'فتح عينيه'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'أنف',
    english: 'nose',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.PHYSICAL,
    coreMeaning: 'العضو للشم',
    relatedWords: ['أنوف', 'منخر', 'خيشوم'],
    examples: ['أنف طويل', 'شم بأنفه'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'أذن',
    english: 'ear',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.PHYSICAL,
    coreMeaning: 'العضو للسمع',
    relatedWords: ['آذان', 'أذنان', 'سمع'],
    examples: ['أذن كبيرة', 'سمع بأذنيه'],
    weight: 1.0
  });

  // 18. البيئة الطبيعية - Natural Environment
  vocab.addWord({
    arabic: 'مطر',
    english: 'rain',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.NATURAL_ENVIRONMENT,
    coreMeaning: 'الماء النازل من السماء',
    relatedWords: ['قطر', 'أمطار', 'ممطر'],
    examples: ['نزل المطر', 'مطر غزير'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'قطر',
    english: 'drip',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.NATURAL_ENVIRONMENT,
    coreMeaning: 'نزول الماء قطرة قطرة',
    relatedWords: ['قطرة', 'تقطير', 'قاطر'],
    examples: ['قطر الماء', 'قطرة ماء'],
    weight: 0.8
  });

  vocab.addWord({
    arabic: 'زرع',
    english: 'plant',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.NATURAL_ENVIRONMENT,
    coreMeaning: 'وضع البذور في الأرض',
    relatedWords: ['زراعة', 'زارع', 'مزروع'],
    examples: ['زرع الحقل', 'زراعة القمح'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'شجر',
    english: 'tree',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.NATURAL_ENVIRONMENT,
    coreMeaning: 'النبات الكبير ذو الجذع',
    relatedWords: ['شجرة', 'أشجار', 'شجيرة'],
    examples: ['شجرة كبيرة', 'غابة أشجار'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'نبات',
    english: 'vegetation',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.NATURAL_ENVIRONMENT,
    coreMeaning: 'ما ينبت من الأرض',
    relatedWords: ['نبت', 'نباتات', 'نابت'],
    examples: ['نبات أخضر', 'نباتات الحديقة'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'نما',
    english: 'grow',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.TRANSFORMATIONS,
    coreMeaning: 'الزيادة في الحجم',
    relatedWords: ['نمو', 'نامي', 'منمي'],
    examples: ['نما الطفل', 'نمو سريع'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'حيا',
    english: 'live',
    type: FoundationWordType.STATE,
    category: FoundationCategory.TRANSFORMATIONS,
    coreMeaning: 'الوجود بالحياة',
    relatedWords: ['حياة', 'حي', 'أحياء'],
    examples: ['حيا سنوات', 'حياة طويلة'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'مات',
    english: 'die',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.TRANSFORMATIONS,
    coreMeaning: 'انتهاء الحياة',
    relatedWords: ['موت', 'ميت', 'أموات'],
    examples: ['مات الرجل', 'موت مفاجئ'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'ازدهر',
    english: 'flourish',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.TRANSFORMATIONS,
    coreMeaning: 'النمو والتقدم',
    relatedWords: ['ازدهار', 'مزدهر', 'زهر'],
    examples: ['ازدهرت الحضارة', 'ازدهار اقتصادي'],
    weight: 0.8
  });

  vocab.addWord({
    arabic: 'بحر',
    english: 'sea',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.NATURAL_ENVIRONMENT,
    coreMeaning: 'الماء الكثير المالح',
    relatedWords: ['بحار', 'بحري', 'محيط'],
    examples: ['البحر واسع', 'سافر في البحر'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'نهر',
    english: 'river',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.NATURAL_ENVIRONMENT,
    coreMeaning: 'الماء الجاري العذب',
    relatedWords: ['أنهار', 'نهري', 'جدول'],
    examples: ['نهر النيل', 'عبر النهر'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'شاطئ',
    english: 'shore',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.NATURAL_ENVIRONMENT,
    coreMeaning: 'حافة البحر أو النهر',
    relatedWords: ['شواطئ', 'ساحل', 'ضفة'],
    examples: ['شاطئ البحر', 'جلس على الشاطئ'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'سبح',
    english: 'swim',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'الحركة في الماء',
    relatedWords: ['سباحة', 'سابح', 'سبّاح'],
    examples: ['سبح في البحر', 'سباحة ماهرة'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'غاص',
    english: 'dive',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'النزول تحت الماء',
    relatedWords: ['غوص', 'غواص', 'غائص'],
    examples: ['غاص في البحر', 'غوص عميق'],
    weight: 0.8
  });

  vocab.addWord({
    arabic: 'غرق',
    english: 'drown',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.TRANSFORMATIONS,
    coreMeaning: 'الموت في الماء',
    relatedWords: ['غريق', 'إغراق', 'مغرق'],
    examples: ['غرق في البحر', 'غريق البحر'],
    weight: 0.8
  });

  vocab.addWord({
    arabic: 'نجا',
    english: 'survive',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.TRANSFORMATIONS,
    coreMeaning: 'الخلاص من الخطر',
    relatedWords: ['نجاة', 'ناجي', 'منجي'],
    examples: ['نجا من الغرق', 'نجاة معجزة'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'استحم',
    english: 'bathe',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'غسل الجسم بالماء',
    relatedWords: ['استحمام', 'حمام', 'محتم'],
    examples: ['استحم بالماء', 'استحمام منعش'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'نشف',
    english: 'dry',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.TRANSFORMATIONS,
    coreMeaning: 'إزالة الماء',
    relatedWords: ['تنشيف', 'ناشف', 'جفاف'],
    examples: ['نشف الملابس', 'تنشيف الشعر'],
    weight: 0.8
  });

  vocab.addWord({
    arabic: 'جف',
    english: 'become dry',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.TRANSFORMATIONS,
    coreMeaning: 'ذهاب الماء',
    relatedWords: ['جفاف', 'جاف', 'يابس'],
    examples: ['جف الماء', 'جفاف الأرض'],
    weight: 0.9
  });

  // 19. الحركة والانتقال - Movement & Transition
  vocab.addWord({
    arabic: 'غاب',
    english: 'disappear',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.TRANSFORMATIONS,
    coreMeaning: 'الاختفاء عن النظر',
    relatedWords: ['غياب', 'غائب', 'مغيب'],
    examples: ['غاب عن الأنظار', 'غياب طويل'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'حضر',
    english: 'attend',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'الوجود في المكان',
    relatedWords: ['حضور', 'حاضر', 'محضر'],
    examples: ['حضر الاجتماع', 'حضور قوي'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'ذهب',
    english: 'go',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'الانتقال من مكان',
    relatedWords: ['ذهاب', 'ذاهب', 'مذهب'],
    examples: ['ذهب إلى المدرسة', 'ذهاب وإياب'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'رجع',
    english: 'return',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'العودة إلى المكان',
    relatedWords: ['رجوع', 'راجع', 'مرجع'],
    examples: ['رجع إلى البيت', 'رجوع سريع'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'عاد',
    english: 'come back',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'الرجوع مرة أخرى',
    relatedWords: ['عودة', 'عائد', 'معاد'],
    examples: ['عاد من السفر', 'عودة ميمونة'],
    weight: 1.0
  });
}

