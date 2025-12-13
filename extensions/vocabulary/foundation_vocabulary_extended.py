# -*- coding: utf-8 -*-
"""
امتداد قاموس الكلمات الأساسية - Extended Foundation Vocabulary

هذا الملف يحتوي على المزيد من الكلمات الأساسية

المصدر الأصلي: TypeScript في /vocabulary/foundationVocabularyExtended.ts
Original source: TypeScript in /vocabulary/foundationVocabularyExtended.ts
"""

from .foundation_vocabulary import (
    FoundationVocabulary,
    FoundationWord,
    FoundationWordType,
    FoundationCategory
)


def add_extended_vocabulary(vocab: FoundationVocabulary) -> None:
    """
    إضافة الكلمات الأساسية الممتدة
    Add extended foundation words
    """
    
    # 10. الأفعال الاجتماعية - Social Actions
    vocab.add_word(FoundationWord(
        arabic='ثأر',
        english='revenge',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.SOCIAL,
        core_meaning='الانتقام من الظالم',
        related_words=['انتقام', 'ثائر', 'مثاورة'],
        examples=['أخذ ثأره', 'ثأر لأخيه'],
        weight=0.8
    ))
    
    vocab.add_word(FoundationWord(
        arabic='فعل',
        english='action',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='القيام بعمل',
        related_words=['عمل', 'فاعل', 'مفعول'],
        examples=['فعل الخير', 'يفعل شيئا'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='شارك',
        english='participate',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.SOCIAL,
        core_meaning='الدخول مع آخرين في عمل',
        related_words=['مشاركة', 'شريك', 'اشتراك'],
        examples=['شارك في العمل', 'مشاركة فعالة'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='أصلح',
        english='fix',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='إزالة الفساد والعيب',
        related_words=['صلح', 'إصلاح', 'صالح'],
        examples=['أصلح الخطأ', 'إصلاح الأمر'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='أثار',
        english='provoke',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.SOCIAL,
        core_meaning='تحريك الشيء وإظهاره',
        related_words=['إثارة', 'مثير', 'استثارة'],
        examples=['أثار المشكلة', 'إثارة الفتنة'],
        weight=0.8
    ))
    
    vocab.add_word(FoundationWord(
        arabic='أشعل',
        english='ignite',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='إيقاد النار',
        related_words=['شعلة', 'اشتعال', 'مشتعل'],
        examples=['أشعل النار', 'اشتعلت النار'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='مشكلة',
        english='problem',
        word_type=FoundationWordType.STATE,
        category=FoundationCategory.SOCIAL,
        core_meaning='أمر معقد يحتاج حل',
        related_words=['إشكال', 'معضلة', 'مأزق'],
        examples=['واجه مشكلة', 'حل المشكلة'],
        weight=0.9
    ))
    
    # 11. الخصائص البصرية - Visual Properties
    vocab.add_word(FoundationWord(
        arabic='ظل',
        english='shadow',
        word_type=FoundationWordType.ENTITY,
        category=FoundationCategory.PHYSICAL,
        core_meaning='الظلام الذي يصنعه الشيء',
        related_words=['ظلال', 'ظليل', 'تظليل'],
        examples=['ظل الشجرة', 'في الظل'],
        weight=0.9
    ))
    
    # 12. النتائج والتحولات - Results & Transformations
    vocab.add_word(FoundationWord(
        arabic='انتصر',
        english='win',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.TRANSFORMATIONS,
        core_meaning='الغلبة في الصراع',
        related_words=['نصر', 'منتصر', 'انتصار'],
        examples=['انتصر في المعركة', 'نصر عظيم'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='هزم',
        english='defeat',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.TRANSFORMATIONS,
        core_meaning='الخسارة في الصراع',
        related_words=['هزيمة', 'مهزوم', 'انهزام'],
        examples=['هُزم في المعركة', 'هزيمة ساحقة'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='تحول',
        english='transform',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.TRANSFORMATIONS,
        core_meaning='التغير من حال إلى حال',
        related_words=['صيرورة', 'تغير', 'تبدل'],
        examples=['تحول الماء إلى بخار', 'تحول كبير'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='صار',
        english='become',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.TRANSFORMATIONS,
        core_meaning='الانتقال إلى حالة جديدة',
        related_words=['صيرورة', 'مصير', 'أصبح'],
        examples=['صار قويا', 'صار غنيا'],
        weight=1.0
    ))
    
    # 13. الحركة - Movement
    vocab.add_word(FoundationWord(
        arabic='هرب',
        english='flee',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='الفرار من الخطر',
        related_words=['فرار', 'هارب', 'هروب'],
        examples=['هرب من العدو', 'هروب سريع'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='لحق',
        english='chase',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='السعي خلف شيء للإمساك به',
        related_words=['لحاق', 'ملاحقة', 'لاحق'],
        examples=['لحق به', 'ملاحقة حثيثة'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='طارد',
        english='pursue',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='السعي خلف شيء لإبعاده',
        related_words=['طرد', 'مطاردة', 'طارد'],
        examples=['طارد العدو', 'مطاردة شديدة'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='أمسك',
        english='grab',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='القبض على شيء باليد',
        related_words=['مسك', 'إمساك', 'ماسك'],
        examples=['أمسك الكرة', 'إمساك قوي'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='أوقع',
        english='drop',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='إسقاط شيء على الأرض',
        related_words=['وقع', 'إيقاع', 'سقوط'],
        examples=['أوقعه أرضا', 'وقع على الأرض'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='طرح',
        english='throw down',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='رمي شيء بقوة',
        related_words=['طرحة', 'مطروح', 'طارح'],
        examples=['طرحه أرضا', 'طرح السؤال'],
        weight=0.8
    ))
    
    vocab.add_word(FoundationWord(
        arabic='صرع',
        english='knock down',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='إسقاط شيء بقوة',
        related_words=['صراع', 'مصروع', 'صريع'],
        examples=['صرعه في المصارعة', 'صريع المرض'],
        weight=0.8
    ))
    
    # 14. الحاجات الأساسية - Basic Needs
    vocab.add_word(FoundationWord(
        arabic='زاد',
        english='provisions',
        word_type=FoundationWordType.ENTITY,
        category=FoundationCategory.PHYSICAL,
        core_meaning='الطعام والشراب للسفر',
        related_words=['طعام', 'غذاء', 'قوت'],
        examples=['حمل الزاد', 'زاد السفر'],
        weight=0.8
    ))
    
    vocab.add_word(FoundationWord(
        arabic='طعام',
        english='food',
        word_type=FoundationWordType.ENTITY,
        category=FoundationCategory.PHYSICAL,
        core_meaning='ما يؤكل',
        related_words=['أكل', 'غذاء', 'طعم'],
        examples=['أكل الطعام', 'طعام لذيذ'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='غسل',
        english='wash',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='إزالة الوسخ بالماء',
        related_words=['غسيل', 'مغسول', 'غاسل'],
        examples=['غسل يديه', 'غسيل الملابس'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='نظافة',
        english='cleanliness',
        word_type=FoundationWordType.PROPERTY,
        category=FoundationCategory.PHYSICAL,
        core_meaning='خلو من الوسخ',
        related_words=['نظيف', 'تنظيف', 'نظف'],
        examples=['نظافة المكان', 'مكان نظيف'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='رعاية',
        english='care',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.SOCIAL,
        core_meaning='الاهتمام والحفظ',
        related_words=['رعى', 'راعي', 'مرعي'],
        examples=['رعاية الأطفال', 'يرعى الغنم'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='رقيب',
        english='watcher',
        word_type=FoundationWordType.ENTITY,
        category=FoundationCategory.SOCIAL,
        core_meaning='من يراقب ويحرس',
        related_words=['رقابة', 'مراقب', 'رقب'],
        examples=['رقيب على العمل', 'رقابة صارمة'],
        weight=0.8
    ))
    
    vocab.add_word(FoundationWord(
        arabic='حرص',
        english='carefulness',
        word_type=FoundationWordType.PROPERTY,
        category=FoundationCategory.PSYCHOLOGICAL,
        core_meaning='الاهتمام الشديد',
        related_words=['حريص', 'احتراس', 'محترس'],
        examples=['حرص على الأمر', 'حريص جدا'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='حذر',
        english='caution',
        word_type=FoundationWordType.PROPERTY,
        category=FoundationCategory.PSYCHOLOGICAL,
        core_meaning='التوقي من الخطر',
        related_words=['حذر', 'تحذير', 'محذور'],
        examples=['حذر من الخطر', 'توخي الحذر'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='توخي',
        english='seek carefully',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='القصد بحذر',
        related_words=['توخى', 'متوخي'],
        examples=['توخى الحذر', 'توخي الدقة'],
        weight=0.7
    ))
