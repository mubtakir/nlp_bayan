# -*- coding: utf-8 -*-
"""
إكمال قاموس الكلمات الأساسية - Complete Foundation Vocabulary

هذا الملف يحتوي على باقي الكلمات الأساسية

المصدر الأصلي: TypeScript في /vocabulary/foundationVocabularyComplete.ts
Original source: TypeScript in /vocabulary/foundationVocabularyComplete.ts
"""

from .foundation_vocabulary import (
    FoundationVocabulary,
    FoundationWord,
    FoundationWordType,
    FoundationCategory
)


def add_complete_vocabulary(vocab: FoundationVocabulary) -> None:
    """
    إضافة الكلمات الأساسية المتبقية
    Add remaining foundation words
    """
    
    # 15. المعرفة والشك - Knowledge & Doubt
    vocab.add_word(FoundationWord(
        arabic='شك',
        english='doubt',
        word_type=FoundationWordType.STATE,
        category=FoundationCategory.PSYCHOLOGICAL,
        core_meaning='عدم اليقين',
        related_words=['شكوك', 'مشكوك', 'ارتياب'],
        examples=['لديه شك', 'شك في الأمر'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='يقين',
        english='certainty',
        word_type=FoundationWordType.STATE,
        category=FoundationCategory.PSYCHOLOGICAL,
        core_meaning='العلم الثابت',
        related_words=['متيقن', 'تيقن', 'قطع'],
        examples=['لديه يقين', 'على يقين'],
        weight=0.9
    ))
    
    # 16. الأنشطة - Activities
    vocab.add_word(FoundationWord(
        arabic='ممارسة',
        english='practice',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='القيام بعمل بانتظام',
        related_words=['مارس', 'ممارس', 'مران'],
        examples=['ممارسة الرياضة', 'يمارس العمل'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='لعب',
        english='play',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='النشاط للمتعة',
        related_words=['لعبة', 'لاعب', 'ملعب'],
        examples=['لعب الكرة', 'لعبة ممتعة'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='مشي',
        english='walk',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='الحركة على القدمين',
        related_words=['مشى', 'ماشي', 'مشاء'],
        examples=['مشى في الطريق', 'المشي مفيد'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='ركض',
        english='run',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='الحركة السريعة على القدمين',
        related_words=['ركض', 'راكض', 'عدو'],
        root_word='ركض',
        examples=['ركض بسرعة', 'ركض في السباق'],
        weight=1.0
    ))
    
    # 17. أعضاء الجسم - Body Parts
    body_parts = [
        ('يد', 'hand', 'العضو للإمساك', ['أيدي', 'كف', 'أصابع'], ['رفع يده', 'يد قوية']),
        ('رجل', 'leg', 'العضو للمشي', ['أرجل', 'ساق', 'فخذ'], ['كسرت رجله', 'رجل طويلة']),
        ('قدم', 'foot', 'نهاية الرجل', ['أقدام', 'قدمان', 'كعب'], ['غسل قدميه', 'قدم كبيرة']),
        ('وجه', 'face', 'مقدمة الرأس', ['وجوه', 'محيا', 'سحنة'], ['وجه جميل', 'غسل وجهه']),
        ('عين', 'eye', 'العضو للرؤية', ['عيون', 'أعين', 'بصر'], ['عين زرقاء', 'فتح عينيه']),
        ('أنف', 'nose', 'العضو للشم', ['أنوف', 'منخر', 'خيشوم'], ['أنف طويل', 'شم بأنفه']),
        ('أذن', 'ear', 'العضو للسمع', ['آذان', 'أذنان', 'سمع'], ['أذن كبيرة', 'سمع بأذنيه']),
    ]
    
    for arabic, english, meaning, related, examples in body_parts:
        vocab.add_word(FoundationWord(
            arabic=arabic,
            english=english,
            word_type=FoundationWordType.ENTITY,
            category=FoundationCategory.PHYSICAL,
            core_meaning=meaning,
            related_words=related,
            examples=examples,
            weight=1.0
        ))
    
    # 18. البيئة الطبيعية - Natural Environment
    vocab.add_word(FoundationWord(
        arabic='مطر',
        english='rain',
        word_type=FoundationWordType.ENTITY,
        category=FoundationCategory.NATURAL_ENVIRONMENT,
        core_meaning='الماء النازل من السماء',
        related_words=['قطر', 'أمطار', 'ممطر'],
        examples=['نزل المطر', 'مطر غزير'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='قطر',
        english='drip',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.NATURAL_ENVIRONMENT,
        core_meaning='نزول الماء قطرة قطرة',
        related_words=['قطرة', 'تقطير', 'قاطر'],
        examples=['قطر الماء', 'قطرة ماء'],
        weight=0.8
    ))
    
    vocab.add_word(FoundationWord(
        arabic='زرع',
        english='plant',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.NATURAL_ENVIRONMENT,
        core_meaning='وضع البذور في الأرض',
        related_words=['زراعة', 'زارع', 'مزروع'],
        examples=['زرع الحقل', 'زراعة القمح'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='شجر',
        english='tree',
        word_type=FoundationWordType.ENTITY,
        category=FoundationCategory.NATURAL_ENVIRONMENT,
        core_meaning='النبات الكبير ذو الجذع',
        related_words=['شجرة', 'أشجار', 'شجيرة'],
        examples=['شجرة كبيرة', 'غابة أشجار'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='نبات',
        english='vegetation',
        word_type=FoundationWordType.ENTITY,
        category=FoundationCategory.NATURAL_ENVIRONMENT,
        core_meaning='ما ينبت من الأرض',
        related_words=['نبت', 'نباتات', 'نابت'],
        examples=['نبات أخضر', 'نباتات الحديقة'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='نما',
        english='grow',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.TRANSFORMATIONS,
        core_meaning='الزيادة في الحجم',
        related_words=['نمو', 'نامي', 'منمي'],
        examples=['نما الطفل', 'نمو سريع'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='حيا',
        english='live',
        word_type=FoundationWordType.STATE,
        category=FoundationCategory.TRANSFORMATIONS,
        core_meaning='الوجود بالحياة',
        related_words=['حياة', 'حي', 'أحياء'],
        examples=['حيا سنوات', 'حياة طويلة'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='مات',
        english='die',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.TRANSFORMATIONS,
        core_meaning='انتهاء الحياة',
        related_words=['موت', 'ميت', 'أموات'],
        examples=['مات الرجل', 'موت مفاجئ'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='ازدهر',
        english='flourish',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.TRANSFORMATIONS,
        core_meaning='النمو والتقدم',
        related_words=['ازدهار', 'مزدهر', 'زهر'],
        examples=['ازدهرت الحضارة', 'ازدهار اقتصادي'],
        weight=0.8
    ))
    
    vocab.add_word(FoundationWord(
        arabic='بحر',
        english='sea',
        word_type=FoundationWordType.ENTITY,
        category=FoundationCategory.NATURAL_ENVIRONMENT,
        core_meaning='الماء الكثير المالح',
        related_words=['بحار', 'بحري', 'محيط'],
        examples=['البحر واسع', 'سافر في البحر'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='نهر',
        english='river',
        word_type=FoundationWordType.ENTITY,
        category=FoundationCategory.NATURAL_ENVIRONMENT,
        core_meaning='الماء الجاري العذب',
        related_words=['أنهار', 'نهري', 'جدول'],
        examples=['نهر النيل', 'عبر النهر'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='شاطئ',
        english='shore',
        word_type=FoundationWordType.ENTITY,
        category=FoundationCategory.NATURAL_ENVIRONMENT,
        core_meaning='حافة البحر أو النهر',
        related_words=['شواطئ', 'ساحل', 'ضفة'],
        examples=['شاطئ البحر', 'جلس على الشاطئ'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='سبح',
        english='swim',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='الحركة في الماء',
        related_words=['سباحة', 'سابح', 'سبّاح'],
        examples=['سبح في البحر', 'سباحة ماهرة'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='غاص',
        english='dive',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='النزول تحت الماء',
        related_words=['غوص', 'غواص', 'غائص'],
        examples=['غاص في البحر', 'غوص عميق'],
        weight=0.8
    ))
    
    vocab.add_word(FoundationWord(
        arabic='غرق',
        english='drown',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.TRANSFORMATIONS,
        core_meaning='الموت في الماء',
        related_words=['غريق', 'إغراق', 'مغرق'],
        examples=['غرق في البحر', 'غريق البحر'],
        weight=0.8
    ))
    
    vocab.add_word(FoundationWord(
        arabic='نجا',
        english='survive',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.TRANSFORMATIONS,
        core_meaning='الخلاص من الخطر',
        related_words=['نجاة', 'ناجي', 'منجي'],
        examples=['نجا من الغرق', 'نجاة معجزة'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='استحم',
        english='bathe',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='غسل الجسم بالماء',
        related_words=['استحمام', 'حمام', 'محتم'],
        examples=['استحم بالماء', 'استحمام منعش'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='نشف',
        english='dry',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.TRANSFORMATIONS,
        core_meaning='إزالة الماء',
        related_words=['تنشيف', 'ناشف', 'جفاف'],
        examples=['نشف الملابس', 'تنشيف الشعر'],
        weight=0.8
    ))
    
    vocab.add_word(FoundationWord(
        arabic='جف',
        english='become dry',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.TRANSFORMATIONS,
        core_meaning='ذهاب الماء',
        related_words=['جفاف', 'جاف', 'يابس'],
        examples=['جف الماء', 'جفاف الأرض'],
        weight=0.9
    ))
    
    # 19. الحركة والانتقال - Movement & Transition
    vocab.add_word(FoundationWord(
        arabic='غاب',
        english='disappear',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.TRANSFORMATIONS,
        core_meaning='الاختفاء عن النظر',
        related_words=['غياب', 'غائب', 'مغيب'],
        examples=['غاب عن الأنظار', 'غياب طويل'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='حضر',
        english='attend',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='الوجود في المكان',
        related_words=['حضور', 'حاضر', 'محضر'],
        examples=['حضر الاجتماع', 'حضور قوي'],
        weight=0.9
    ))
    
    vocab.add_word(FoundationWord(
        arabic='ذهب',
        english='go',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='الانتقال من مكان',
        related_words=['ذهاب', 'ذاهب', 'مذهب'],
        examples=['ذهب إلى المدرسة', 'ذهاب وإياب'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='رجع',
        english='return',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='العودة إلى المكان',
        related_words=['رجوع', 'راجع', 'مرجع'],
        examples=['رجع إلى البيت', 'رجوع سريع'],
        weight=1.0
    ))
    
    vocab.add_word(FoundationWord(
        arabic='عاد',
        english='come back',
        word_type=FoundationWordType.ACTION,
        category=FoundationCategory.BASIC_ACTIONS,
        core_meaning='الرجوع مرة أخرى',
        related_words=['عودة', 'عائد', 'معاد'],
        examples=['عاد من السفر', 'عودة ميمونة'],
        weight=1.0
    ))
