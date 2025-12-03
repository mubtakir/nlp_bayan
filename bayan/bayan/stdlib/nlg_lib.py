"""
Natural Language Generation Library for Bayan
مكتبة توليد النص الطبيعي للغة بيان

Provides bilingual (Arabic/English) text generation capabilities.
"""

from typing import List, Dict, Any, Optional
import random

# ═══════════════════════════════════════════════════════════════════════════════
# Arabic Sentence Templates - قوالب الجمل العربية
# ═══════════════════════════════════════════════════════════════════════════════

ARABIC_TEMPLATES = {
    'simple': [
        "{subject} {verb} {object}",
        "{verb} {subject} {object}",
        "{subject} {verb}",
    ],
    'conditional': [
        "إذا {condition}، فإن {result}",
        "لو {condition}، لـ{result}",
        "عندما {condition}، {result}",
    ],
    'causal': [
        "{cause} لذلك {effect}",
        "بسبب {cause}، {effect}",
        "{effect} نتيجة {cause}",
    ],
    'temporal': [
        "أولاً {first}، ثم {second}",
        "بعد {first}، {second}",
        "قبل {second}، {first}",
    ],
    'descriptive': [
        "{subject} {adjective}",
        "{subject} الـ{adjective}",
        "إن {subject} {adjective} جداً",
    ],
}

ENGLISH_TEMPLATES = {
    'simple': [
        "{subject} {verb} {object}",
        "{subject} {verb}",
    ],
    'conditional': [
        "If {condition}, then {result}",
        "When {condition}, {result}",
    ],
    'causal': [
        "{cause}, therefore {effect}",
        "Because of {cause}, {effect}",
    ],
    'temporal': [
        "First {first}, then {second}",
        "After {first}, {second}",
    ],
    'descriptive': [
        "{subject} is {adjective}",
        "The {adjective} {subject}",
    ],
}

# ═══════════════════════════════════════════════════════════════════════════════
# Connectors - الروابط
# ═══════════════════════════════════════════════════════════════════════════════

CONNECTORS = {
    'ar': {
        'addition': ['و', 'كما', 'أيضاً', 'بالإضافة إلى ذلك'],
        'contrast': ['لكن', 'ولكن', 'غير أن', 'إلا أن'],
        'cause': ['لأن', 'بسبب', 'نظراً لـ', 'إذ'],
        'result': ['لذلك', 'وبالتالي', 'ومن ثم', 'فـ'],
        'time': ['ثم', 'بعد ذلك', 'قبل ذلك', 'في النهاية'],
    },
    'en': {
        'addition': ['and', 'also', 'moreover', 'furthermore'],
        'contrast': ['but', 'however', 'yet', 'although'],
        'cause': ['because', 'since', 'as', 'due to'],
        'result': ['therefore', 'thus', 'hence', 'so'],
        'time': ['then', 'afterwards', 'before', 'finally'],
    }
}


class NLGEngine:
    """Natural Language Generation Engine - محرك توليد النص الطبيعي"""
    
    def __init__(self, lang: str = 'ar'):
        self.lang = lang
        self.templates = ARABIC_TEMPLATES if lang == 'ar' else ENGLISH_TEMPLATES
        self.connectors = CONNECTORS.get(lang, CONNECTORS['en'])
        self._rng = random.Random()
        
    def generate_sentence(self, template_type: str, **kwargs) -> str:
        """Generate a sentence from template. توليد جملة من قالب."""
        templates = self.templates.get(template_type, self.templates['simple'])
        template = self._rng.choice(templates)
        try:
            return template.format(**kwargs)
        except KeyError as e:
            return f"Missing: {e}"
    
    def generate_paragraph(self, sentences: List[str], 
                          connector_type: str = 'addition') -> str:
        """Generate a paragraph by connecting sentences. توليد فقرة بربط الجمل."""
        if not sentences:
            return ""
        if len(sentences) == 1:
            return sentences[0]
            
        connectors = self.connectors.get(connector_type, self.connectors['addition'])
        result = [sentences[0]]
        
        for i, sentence in enumerate(sentences[1:], 1):
            connector = self._rng.choice(connectors)
            if self.lang == 'ar':
                result.append(f"{connector} {sentence}")
            else:
                result.append(f"{connector}, {sentence}")
                
        return ' '.join(result) if self.lang == 'en' else ' '.join(result)
    
    def generate_list(self, items: List[str], ordered: bool = False) -> str:
        """Generate a formatted list. توليد قائمة منسقة."""
        if not items:
            return ""
        if ordered:
            if self.lang == 'ar':
                return '\n'.join(f"{i+1}. {item}" for i, item in enumerate(items))
            return '\n'.join(f"{i+1}. {item}" for i, item in enumerate(items))
        else:
            marker = '•' if self.lang == 'ar' else '-'
            return '\n'.join(f"{marker} {item}" for item in items)

    def generate_question(self, question_type: str, **kwargs) -> str:
        """Generate a question. توليد سؤال."""
        if self.lang == 'ar':
            patterns = {
                'what': "ما {topic}؟",
                'why': "لماذا {topic}؟",
                'how': "كيف {topic}؟",
                'when': "متى {topic}؟",
                'where': "أين {topic}؟",
                'who': "من {topic}؟",
                'yes_no': "هل {topic}؟",
            }
        else:
            patterns = {
                'what': "What is {topic}?",
                'why': "Why {topic}?",
                'how': "How {topic}?",
                'when': "When {topic}?",
                'where': "Where {topic}?",
                'who': "Who {topic}?",
                'yes_no': "Is {topic}?",
            }
        pattern = patterns.get(question_type, patterns['what'])
        return pattern.format(**kwargs)


# ═══════════════════════════════════════════════════════════════════════════════
# Standalone Functions - الدوال المستقلة
# ═══════════════════════════════════════════════════════════════════════════════

_ar_engine = NLGEngine('ar')
_en_engine = NLGEngine('en')

def generate_sentence(template_type: str, lang: str = 'ar', **kwargs) -> str:
    """Generate a sentence. توليد جملة."""
    engine = _ar_engine if lang == 'ar' else _en_engine
    return engine.generate_sentence(template_type, **kwargs)

def generate_paragraph(sentences: List[str], connector_type: str = 'addition',
                       lang: str = 'ar') -> str:
    """Generate a paragraph. توليد فقرة."""
    engine = _ar_engine if lang == 'ar' else _en_engine
    return engine.generate_paragraph(sentences, connector_type)

def generate_list(items: List[str], ordered: bool = False, lang: str = 'ar') -> str:
    """Generate a list. توليد قائمة."""
    engine = _ar_engine if lang == 'ar' else _en_engine
    return engine.generate_list(items, ordered)

def generate_question(question_type: str, lang: str = 'ar', **kwargs) -> str:
    """Generate a question. توليد سؤال."""
    engine = _ar_engine if lang == 'ar' else _en_engine
    return engine.generate_question(question_type, **kwargs)

def get_connector(connector_type: str, lang: str = 'ar') -> str:
    """Get a random connector. الحصول على رابط عشوائي."""
    connectors = CONNECTORS.get(lang, CONNECTORS['en'])
    conn_list = connectors.get(connector_type, connectors['addition'])
    return random.choice(conn_list)


# Arabic aliases - الأسماء العربية
ولّد_جملة = generate_sentence
ولّد_فقرة = generate_paragraph
ولّد_قائمة = generate_list
ولّد_سؤال = generate_question
احصل_على_رابط = get_connector
محرك_توليد = NLGEngine

