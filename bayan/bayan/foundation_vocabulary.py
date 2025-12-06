# -*- coding: utf-8 -*-
"""
قاموس الكلمات الأساسية - Foundation Vocabulary

هذا القاموس يحتوي على الكلمات الأساس التي تُبنى عليها اللغة
كل كلمة هي جذر يتفرع منه كلمات أخرى تخصص المعنى

This vocabulary contains the foundation words upon which language is built
Each word is a root from which other words branch to specialize meaning

المصدر الأصلي: TypeScript في /vocabulary/foundationVocabulary.ts
Original source: TypeScript in /vocabulary/foundationVocabulary.ts
"""

from enum import Enum
from typing import List, Optional, Dict
from dataclasses import dataclass, field


class FoundationWordType(Enum):
    """نوع الكلمة الأساسية / Foundation Word Type"""
    ENTITY = 'كيان'
    PROPERTY = 'خاصية'
    ACTION = 'فعل'
    STATE = 'حالة'
    RELATION = 'علاقة'
    DIRECTION = 'اتجاه'
    QUANTITY = 'كمية'
    TIME = 'زمن'


class FoundationCategory(Enum):
    """فئة الكلمة الأساسية / Foundation Word Category"""
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
    """كلمة أساسية / Foundation Word"""
    arabic: str
    word_type: FoundationWordType
    category: FoundationCategory
    core_meaning: str
    related_words: List[str] = field(default_factory=list)
    english: Optional[str] = None
    root_word: Optional[str] = None
    meaning_angle: Optional[str] = None
    examples: List[str] = field(default_factory=list)
    weight: float = 0.5


class FoundationVocabulary:
    """
    قاموس الكلمات الأساسية
    Foundation Vocabulary Dictionary
    """
    
    def __init__(self):
        self.words: Dict[str, FoundationWord] = {}
        self.categories: Dict[FoundationCategory, List[FoundationWord]] = {}
        self.types: Dict[FoundationWordType, List[FoundationWord]] = {}
        self._initialize_vocabulary()
    
    def _initialize_vocabulary(self):
        """تهيئة القاموس بالكلمات الأساسية"""
        
        # 1. البيئة الأولية - Initial Environment
        self.add_word(FoundationWord(
            arabic='أرض',
            english='ground',
            word_type=FoundationWordType.ENTITY,
            category=FoundationCategory.INITIAL_ENVIRONMENT,
            core_meaning='السطح الذي نقف عليه',
            related_words=['تراب', 'أرضية', 'قاع', 'قعر'],
            examples=['الأرض صلبة', 'سقط على الأرض'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='سماء',
            english='sky',
            word_type=FoundationWordType.ENTITY,
            category=FoundationCategory.INITIAL_ENVIRONMENT,
            core_meaning='الفضاء فوقنا',
            related_words=['سقف', 'علو', 'فضاء'],
            examples=['السماء زرقاء', 'نظر إلى السماء'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='شمس',
            english='sun',
            word_type=FoundationWordType.ENTITY,
            category=FoundationCategory.INITIAL_ENVIRONMENT,
            core_meaning='مصدر الضوء والحرارة في النهار',
            related_words=['ضوء', 'نهار', 'شروق', 'غروب'],
            examples=['الشمس ساطعة', 'طلعت الشمس'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='قمر',
            english='moon',
            word_type=FoundationWordType.ENTITY,
            category=FoundationCategory.INITIAL_ENVIRONMENT,
            core_meaning='مصدر النور في الليل',
            related_words=['نور', 'ليل', 'هلال', 'بدر'],
            examples=['القمر منير', 'ظهر القمر'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='ضوء',
            english='light',
            word_type=FoundationWordType.PROPERTY,
            category=FoundationCategory.INITIAL_ENVIRONMENT,
            core_meaning='ما يجعلنا نرى',
            related_words=['إضاءة', 'نور', 'إشراق', 'لمعان'],
            examples=['الضوء ساطع', 'أضاء المكان'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='نور',
            english='illumination',
            word_type=FoundationWordType.PROPERTY,
            category=FoundationCategory.INITIAL_ENVIRONMENT,
            core_meaning='ضوء خفيف',
            related_words=['إنارة', 'ضياء', 'بريق'],
            examples=['نور القمر', 'أنار الطريق'],
            weight=0.9
        ))
        
        self.add_word(FoundationWord(
            arabic='ليل',
            english='night',
            word_type=FoundationWordType.TIME,
            category=FoundationCategory.INITIAL_ENVIRONMENT,
            core_meaning='وقت الظلام',
            related_words=['ظلام', 'ظلمة', 'عتمة'],
            examples=['الليل مظلم', 'جاء الليل'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='نهار',
            english='day',
            word_type=FoundationWordType.TIME,
            category=FoundationCategory.INITIAL_ENVIRONMENT,
            core_meaning='وقت الضوء',
            related_words=['يوم', 'صباح', 'نهارا'],
            examples=['النهار طويل', 'في النهار'],
            weight=1.0
        ))
        
        # 2. الكيان والوجود - Entity & Existence
        self.add_word(FoundationWord(
            arabic='شيء',
            english='thing',
            word_type=FoundationWordType.ENTITY,
            category=FoundationCategory.ENTITY_EXISTENCE,
            core_meaning='كيان موجود',
            related_words=['كائن', 'موجود', 'جسم', 'كيان'],
            examples=['هذا شيء غريب', 'رأيت شيئا'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='بيئة',
            english='environment',
            word_type=FoundationWordType.ENTITY,
            category=FoundationCategory.ENTITY_EXISTENCE,
            core_meaning='المحيط الذي يعيش فيه الشيء',
            related_words=['محيط', 'وسط', 'مكان'],
            examples=['البيئة نظيفة', 'يعيش في بيئة'],
            weight=0.9
        ))
        
        self.add_word(FoundationWord(
            arabic='محيط',
            english='surroundings',
            word_type=FoundationWordType.ENTITY,
            category=FoundationCategory.ENTITY_EXISTENCE,
            core_meaning='ما يحيط بالشيء',
            related_words=['جوار', 'حول', 'دائرة'],
            examples=['المحيط الهادئ', 'في محيطه'],
            weight=0.8
        ))
        
        # 3. الاتجاهات - Directions
        for direction_data in [
            ('يمين', 'right', 'الجهة اليمنى', ['يميني', 'أيمن']),
            ('يسار', 'left', 'الجهة اليسرى', ['يساري', 'أيسر', 'شمال']),
            ('أمام', 'front', 'الجهة الأمامية', ['قدام', 'وجه', 'مواجهة']),
            ('خلف', 'behind', 'الجهة الخلفية', ['وراء', 'ظهر', 'خلفي']),
            ('فوق', 'above', 'الجهة العلوية', ['علو', 'أعلى', 'سماء']),
            ('تحت', 'below', 'الجهة السفلية', ['أسفل', 'قاع', 'أرض']),
        ]:
            self.add_word(FoundationWord(
                arabic=direction_data[0],
                english=direction_data[1],
                word_type=FoundationWordType.DIRECTION,
                category=FoundationCategory.ENTITY_EXISTENCE,
                core_meaning=direction_data[2],
                related_words=direction_data[3],
                examples=[f'اتجه {direction_data[0]}', f'على {direction_data[0]}'],
                weight=1.0
            ))
        
        # 4. الخصائص الفيزيائية - Physical Properties
        self.add_word(FoundationWord(
            arabic='أجوف',
            english='hollow',
            word_type=FoundationWordType.PROPERTY,
            category=FoundationCategory.PHYSICAL,
            core_meaning='له جوف من الداخل',
            related_words=['جوف', 'فراغ', 'تجويف'],
            examples=['إناء أجوف', 'شيء أجوف'],
            weight=0.9
        ))
        
        self.add_word(FoundationWord(
            arabic='صلد',
            english='solid',
            word_type=FoundationWordType.PROPERTY,
            category=FoundationCategory.PHYSICAL,
            core_meaning='لا جوف له، صلب',
            related_words=['صلب', 'متين', 'قاسي'],
            examples=['حجر صلد', 'جسم صلد'],
            weight=0.9
        ))
        
        self.add_word(FoundationWord(
            arabic='ممتلئ',
            english='full',
            word_type=FoundationWordType.STATE,
            category=FoundationCategory.PHYSICAL,
            core_meaning='في جوفه شيء',
            related_words=['امتلاء', 'ملء', 'مليء'],
            examples=['الكأس ممتلئ', 'امتلأ الإناء'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='فارغ',
            english='empty',
            word_type=FoundationWordType.STATE,
            category=FoundationCategory.PHYSICAL,
            core_meaning='لا شيء في جوفه',
            related_words=['فراغ', 'خلاء', 'خالي'],
            examples=['الكأس فارغ', 'فرغ الإناء'],
            weight=1.0
        ))
        
        # 5. العلاقات المكانية - Spatial Relations
        self.add_word(FoundationWord(
            arabic='قرب',
            english='nearness',
            word_type=FoundationWordType.RELATION,
            category=FoundationCategory.PHYSICAL,
            core_meaning='المسافة قليلة',
            related_words=['قريب', 'دنو', 'جوار'],
            examples=['قرب منه', 'على مقربة'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='بعد',
            english='distance',
            word_type=FoundationWordType.RELATION,
            category=FoundationCategory.PHYSICAL,
            core_meaning='المسافة كبيرة',
            related_words=['بعيد', 'بُعد', 'نأي'],
            examples=['بعد عنه', 'على بُعد'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='تماس',
            english='contact',
            word_type=FoundationWordType.RELATION,
            category=FoundationCategory.PHYSICAL,
            core_meaning='التصاق شيئين',
            related_words=['لمس', 'مس', 'التصاق'],
            examples=['تماس الجسمين', 'في تماس'],
            weight=0.9
        ))
        
        # 6. الحاجات الأساسية - Basic Needs
        self.add_word(FoundationWord(
            arabic='جائع',
            english='hungry',
            word_type=FoundationWordType.STATE,
            category=FoundationCategory.PHYSICAL,
            core_meaning='يحتاج إلى طعام',
            related_words=['جوع', 'مجاعة', 'جياع'],
            examples=['أنا جائع', 'شعر بالجوع'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='شبع',
            english='satiation',
            word_type=FoundationWordType.STATE,
            category=FoundationCategory.PHYSICAL,
            core_meaning='امتلأ من الطعام',
            related_words=['شبعان', 'تشبع', 'شباع'],
            examples=['شبع من الطعام', 'أنا شبعان'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='حاجة',
            english='need',
            word_type=FoundationWordType.STATE,
            category=FoundationCategory.PHYSICAL,
            core_meaning='نقص يحتاج إلى سد',
            related_words=['احتياج', 'ضرورة', 'لزوم'],
            examples=['لديه حاجة', 'يحتاج إلى'],
            weight=1.0
        ))
        
        # 7. الأفعال الأساسية - Basic Actions
        self.add_word(FoundationWord(
            arabic='أكل',
            english='eat',
            word_type=FoundationWordType.ACTION,
            category=FoundationCategory.BASIC_ACTIONS,
            core_meaning='إدخال الطعام إلى الجوف',
            related_words=['طعام', 'أكلة', 'آكل'],
            examples=['أكل الطعام', 'يأكل التفاحة'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='ابتلع',
            english='swallow',
            word_type=FoundationWordType.ACTION,
            category=FoundationCategory.BASIC_ACTIONS,
            core_meaning='إدخال شيء إلى الجوف دفعة واحدة',
            related_words=['بلع', 'ابتلاع', 'بالع'],
            examples=['ابتلع الدواء', 'بلع اللقمة'],
            weight=0.9
        ))
        
        # 8. العلاقات الاجتماعية - Social Relations
        self.add_word(FoundationWord(
            arabic='ود',
            english='affection',
            word_type=FoundationWordType.RELATION,
            category=FoundationCategory.SOCIAL,
            core_meaning='محبة وقرب',
            related_words=['مودة', 'حب', 'ألفة'],
            examples=['بينهما ود', 'ود صادق'],
            weight=0.9
        ))
        
        self.add_word(FoundationWord(
            arabic='نفور',
            english='aversion',
            word_type=FoundationWordType.RELATION,
            category=FoundationCategory.SOCIAL,
            core_meaning='كراهة وابتعاد',
            related_words=['كره', 'بغض', 'نافر'],
            examples=['نفور منه', 'ينفر من'],
            weight=0.9
        ))
        
        self.add_word(FoundationWord(
            arabic='اعتداء',
            english='aggression',
            word_type=FoundationWordType.ACTION,
            category=FoundationCategory.SOCIAL,
            core_meaning='تجاوز الحد والإيذاء',
            related_words=['تجاوز', 'ظلم', 'معتدي'],
            examples=['اعتداء على حقه', 'اعتدى عليه'],
            weight=0.9
        ))
        
        self.add_word(FoundationWord(
            arabic='شر',
            english='evil',
            word_type=FoundationWordType.PROPERTY,
            category=FoundationCategory.PSYCHOLOGICAL,
            core_meaning='سوء وإيذاء',
            related_words=['شرير', 'خبث', 'سوء'],
            examples=['فعل الشر', 'شرير القلب'],
            weight=0.9
        ))
        
        self.add_word(FoundationWord(
            arabic='طيب',
            english='good',
            word_type=FoundationWordType.PROPERTY,
            category=FoundationCategory.PSYCHOLOGICAL,
            core_meaning='حسن وخير',
            related_words=['خير', 'حسن', 'طيبة'],
            examples=['رجل طيب', 'قلب طيب'],
            weight=0.9
        ))
        
        self.add_word(FoundationWord(
            arabic='مسكين',
            english='poor',
            word_type=FoundationWordType.STATE,
            category=FoundationCategory.SOCIAL,
            core_meaning='ضعيف محتاج',
            related_words=['فقير', 'ضعيف', 'مسكنة'],
            examples=['رجل مسكين', 'حال مسكين'],
            weight=0.8
        ))
        
        self.add_word(FoundationWord(
            arabic='متسامح',
            english='forgiving',
            word_type=FoundationWordType.PROPERTY,
            category=FoundationCategory.PSYCHOLOGICAL,
            core_meaning='يعفو ولا ينتقم',
            related_words=['تسامح', 'عفو', 'صفح'],
            examples=['رجل متسامح', 'تسامح معه'],
            weight=0.8
        ))
        
        # 9. الإحساس والشعور - Sensation & Feeling
        self.add_word(FoundationWord(
            arabic='ألم',
            english='pain',
            word_type=FoundationWordType.STATE,
            category=FoundationCategory.PSYCHOLOGICAL,
            core_meaning='إحساس بالوجع',
            related_words=['وجع', 'توجع', 'مؤلم'],
            examples=['شعر بالألم', 'ألم شديد'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='إحساس',
            english='sensation',
            word_type=FoundationWordType.STATE,
            category=FoundationCategory.PSYCHOLOGICAL,
            core_meaning='الشعور بشيء',
            related_words=['حس', 'شعور', 'إدراك'],
            examples=['لديه إحساس', 'أحس بالبرد'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='شعور',
            english='feeling',
            word_type=FoundationWordType.STATE,
            category=FoundationCategory.PSYCHOLOGICAL,
            core_meaning='إدراك داخلي',
            related_words=['شعر', 'إحساس', 'وجدان'],
            examples=['شعور بالفرح', 'يشعر بالحزن'],
            weight=1.0
        ))
        
        self.add_word(FoundationWord(
            arabic='خدش',
            english='scratch',
            word_type=FoundationWordType.ACTION,
            category=FoundationCategory.BASIC_ACTIONS,
            core_meaning='جرح سطحي',
            related_words=['خدشة', 'جرح', 'كشط'],
            examples=['خدش الجلد', 'خدشة بسيطة'],
            weight=0.8
        ))

        self.add_word(FoundationWord(
            arabic='فرح',
            english='happiness',
            word_type=FoundationWordType.STATE,
            category=FoundationCategory.PSYCHOLOGICAL,
            core_meaning='شعور بالسعادة والسرور',
            related_words=['سعادة', 'سرور', 'بهجة'],
            root_word='فرح',
            examples=['شعر بالفرح', 'فرح بالخبر'],
            weight=1.0
        ))

        self.add_word(FoundationWord(
            arabic='ركض',
            english='run',
            word_type=FoundationWordType.ACTION,
            category=FoundationCategory.PHYSICAL,
            core_meaning='المشي بسرعة شديدة',
            related_words=['جري', 'عدو', 'هرولة'],
            root_word='ركض',
            examples=['ركض بسرعة', 'يركض في الملعب'],
            weight=1.0
        ))
    
    def add_word(self, word: FoundationWord) -> None:
        """إضافة كلمة أساسية / Add foundation word"""
        self.words[word.arabic] = word
        
        # إضافة إلى الفئة
        if word.category not in self.categories:
            self.categories[word.category] = []
        self.categories[word.category].append(word)
        
        # إضافة إلى النوع
        if word.word_type not in self.types:
            self.types[word.word_type] = []
        self.types[word.word_type].append(word)
    
    def get_word(self, arabic: str) -> Optional[FoundationWord]:
        """الحصول على كلمة / Get word"""
        return self.words.get(arabic)
    
    def get_words_by_category(self, category: FoundationCategory) -> List[FoundationWord]:
        """الحصول على كلمات حسب الفئة / Get words by category"""
        return self.categories.get(category, [])
    
    def get_words_by_type(self, word_type: FoundationWordType) -> List[FoundationWord]:
        """الحصول على كلمات حسب النوع / Get words by type"""
        return self.types.get(word_type, [])
    
    def find_related_words(self, arabic: str) -> List[FoundationWord]:
        """البحث عن كلمات مرتبطة / Find related words"""
        word = self.get_word(arabic)
        if not word:
            return []
        
        related = []
        for related_arabic in word.related_words:
            related_word = self.get_word(related_arabic)
            if related_word:
                related.append(related_word)
        
        return related
    
    def get_all_words(self) -> List[FoundationWord]:
        """الحصول على جميع الكلمات / Get all words"""
        return list(self.words.values())
    
    def get_word_count(self) -> int:
        """عدد الكلمات / Word count"""
        return len(self.words)
