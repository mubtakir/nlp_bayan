/**
 * امتداد قاموس الكلمات الأساسية - Extended Foundation Vocabulary
 * 
 * هذا الملف يحتوي على المزيد من الكلمات الأساسية
 */

import { FoundationWord, FoundationWordType, FoundationCategory, FoundationVocabulary } from './foundationVocabulary';

/**
 * إضافة الكلمات الأساسية الممتدة
 * Add extended foundation words
 */
export function addExtendedVocabulary(vocab: FoundationVocabulary): void {
  // 10. الأفعال الاجتماعية - Social Actions
  vocab.addWord({
    arabic: 'ثأر',
    english: 'revenge',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.SOCIAL,
    coreMeaning: 'الانتقام من الظالم',
    relatedWords: ['انتقام', 'ثائر', 'مثاورة'],
    examples: ['أخذ ثأره', 'ثأر لأخيه'],
    weight: 0.8
  });

  vocab.addWord({
    arabic: 'فعل',
    english: 'action',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'القيام بعمل',
    relatedWords: ['عمل', 'فاعل', 'مفعول'],
    examples: ['فعل الخير', 'يفعل شيئا'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'شارك',
    english: 'participate',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.SOCIAL,
    coreMeaning: 'الدخول مع آخرين في عمل',
    relatedWords: ['مشاركة', 'شريك', 'اشتراك'],
    examples: ['شارك في العمل', 'مشاركة فعالة'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'أصلح',
    english: 'fix',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'إزالة الفساد والعيب',
    relatedWords: ['صلح', 'إصلاح', 'صالح'],
    examples: ['أصلح الخطأ', 'إصلاح الأمر'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'أثار',
    english: 'provoke',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.SOCIAL,
    coreMeaning: 'تحريك الشيء وإظهاره',
    relatedWords: ['إثارة', 'مثير', 'استثارة'],
    examples: ['أثار المشكلة', 'إثارة الفتنة'],
    weight: 0.8
  });

  vocab.addWord({
    arabic: 'أشعل',
    english: 'ignite',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'إيقاد النار',
    relatedWords: ['شعلة', 'اشتعال', 'مشتعل'],
    examples: ['أشعل النار', 'اشتعلت النار'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'مشكلة',
    english: 'problem',
    type: FoundationWordType.STATE,
    category: FoundationCategory.SOCIAL,
    coreMeaning: 'أمر معقد يحتاج حل',
    relatedWords: ['إشكال', 'معضلة', 'مأزق'],
    examples: ['واجه مشكلة', 'حل المشكلة'],
    weight: 0.9
  });

  // 11. الخصائص البصرية - Visual Properties
  vocab.addWord({
    arabic: 'ظل',
    english: 'shadow',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.PHYSICAL,
    coreMeaning: 'الظلام الذي يصنعه الشيء',
    relatedWords: ['ظلال', 'ظليل', 'تظليل'],
    examples: ['ظل الشجرة', 'في الظل'],
    weight: 0.9
  });

  // 12. النتائج والتحولات - Results & Transformations
  vocab.addWord({
    arabic: 'انتصر',
    english: 'win',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.TRANSFORMATIONS,
    coreMeaning: 'الغلبة في الصراع',
    relatedWords: ['نصر', 'منتصر', 'انتصار'],
    examples: ['انتصر في المعركة', 'نصر عظيم'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'هزم',
    english: 'defeat',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.TRANSFORMATIONS,
    coreMeaning: 'الخسارة في الصراع',
    relatedWords: ['هزيمة', 'مهزوم', 'انهزام'],
    examples: ['هُزم في المعركة', 'هزيمة ساحقة'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'تحول',
    english: 'transform',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.TRANSFORMATIONS,
    coreMeaning: 'التغير من حال إلى حال',
    relatedWords: ['صيرورة', 'تغير', 'تبدل'],
    examples: ['تحول الماء إلى بخار', 'تحول كبير'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'صار',
    english: 'become',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.TRANSFORMATIONS,
    coreMeaning: 'الانتقال إلى حالة جديدة',
    relatedWords: ['صيرورة', 'مصير', 'أصبح'],
    examples: ['صار قويا', 'صار غنيا'],
    weight: 1.0
  });

  // 13. الحركة - Movement
  vocab.addWord({
    arabic: 'هرب',
    english: 'flee',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'الفرار من الخطر',
    relatedWords: ['فرار', 'هارب', 'هروب'],
    examples: ['هرب من العدو', 'هروب سريع'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'لحق',
    english: 'chase',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'السعي خلف شيء للإمساك به',
    relatedWords: ['لحاق', 'ملاحقة', 'لاحق'],
    examples: ['لحق به', 'ملاحقة حثيثة'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'طارد',
    english: 'pursue',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'السعي خلف شيء لإبعاده',
    relatedWords: ['طرد', 'مطاردة', 'طارد'],
    examples: ['طارد العدو', 'مطاردة شديدة'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'أمسك',
    english: 'grab',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'القبض على شيء باليد',
    relatedWords: ['مسك', 'إمساك', 'ماسك'],
    examples: ['أمسك الكرة', 'إمساك قوي'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'أوقع',
    english: 'drop',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'إسقاط شيء على الأرض',
    relatedWords: ['وقع', 'إيقاع', 'سقوط'],
    examples: ['أوقعه أرضا', 'وقع على الأرض'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'طرح',
    english: 'throw down',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'رمي شيء بقوة',
    relatedWords: ['طرحة', 'مطروح', 'طارح'],
    examples: ['طرحه أرضا', 'طرح السؤال'],
    weight: 0.8
  });

  vocab.addWord({
    arabic: 'صرع',
    english: 'knock down',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'إسقاط شيء بقوة',
    relatedWords: ['صراع', 'مصروع', 'صريع'],
    examples: ['صرعه في المصارعة', 'صريع المرض'],
    weight: 0.8
  });

  // 14. الحاجات الأساسية - Basic Needs
  vocab.addWord({
    arabic: 'زاد',
    english: 'provisions',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.PHYSICAL,
    coreMeaning: 'الطعام والشراب للسفر',
    relatedWords: ['طعام', 'غذاء', 'قوت'],
    examples: ['حمل الزاد', 'زاد السفر'],
    weight: 0.8
  });

  vocab.addWord({
    arabic: 'طعام',
    english: 'food',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.PHYSICAL,
    coreMeaning: 'ما يؤكل',
    relatedWords: ['أكل', 'غذاء', 'طعم'],
    examples: ['أكل الطعام', 'طعام لذيذ'],
    weight: 1.0
  });

  vocab.addWord({
    arabic: 'غسل',
    english: 'wash',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'إزالة الوسخ بالماء',
    relatedWords: ['غسيل', 'مغسول', 'غاسل'],
    examples: ['غسل يديه', 'غسيل الملابس'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'نظافة',
    english: 'cleanliness',
    type: FoundationWordType.PROPERTY,
    category: FoundationCategory.PHYSICAL,
    coreMeaning: 'خلو من الوسخ',
    relatedWords: ['نظيف', 'تنظيف', 'نظف'],
    examples: ['نظافة المكان', 'مكان نظيف'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'رعاية',
    english: 'care',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.SOCIAL,
    coreMeaning: 'الاهتمام والحفظ',
    relatedWords: ['رعى', 'راعي', 'مرعي'],
    examples: ['رعاية الأطفال', 'يرعى الغنم'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'رقيب',
    english: 'watcher',
    type: FoundationWordType.ENTITY,
    category: FoundationCategory.SOCIAL,
    coreMeaning: 'من يراقب ويحرس',
    relatedWords: ['رقابة', 'مراقب', 'رقب'],
    examples: ['رقيب على العمل', 'رقابة صارمة'],
    weight: 0.8
  });

  vocab.addWord({
    arabic: 'حرص',
    english: 'carefulness',
    type: FoundationWordType.PROPERTY,
    category: FoundationCategory.PSYCHOLOGICAL,
    coreMeaning: 'الاهتمام الشديد',
    relatedWords: ['حريص', 'احتراس', 'محترس'],
    examples: ['حرص على الأمر', 'حريص جدا'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'حذر',
    english: 'caution',
    type: FoundationWordType.PROPERTY,
    category: FoundationCategory.PSYCHOLOGICAL,
    coreMeaning: 'التوقي من الخطر',
    relatedWords: ['حذر', 'تحذير', 'محذور'],
    examples: ['حذر من الخطر', 'توخي الحذر'],
    weight: 0.9
  });

  vocab.addWord({
    arabic: 'توخي',
    english: 'seek carefully',
    type: FoundationWordType.ACTION,
    category: FoundationCategory.BASIC_ACTIONS,
    coreMeaning: 'القصد بحذر',
    relatedWords: ['توخى', 'متوخي'],
    examples: ['توخى الحذر', 'توخي الدقة'],
    weight: 0.7
  });
}
