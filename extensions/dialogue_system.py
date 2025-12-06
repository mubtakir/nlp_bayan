"""
🤖 نظام الحوار الذكي
Intelligent Dialogue System

نظام محادثة ذكي يفهم السياق ويحافظ على الذاكرة:
- فهم النوايا (Intents)
- كشف المشاعر (Emotions)
- ذاكرة قصيرة وطويلة المدى
- توليد ردود ذكية
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum
from datetime import datetime
import re


class Intent(Enum):
    """أنواع النوايا"""
    GREETING = "تحية"
    QUESTION = "سؤال"
    REQUEST = "طلب"
    STATEMENT = "تصريح"
    GRATITUDE = "شكر"
    FAREWELL = "وداع"
    LEARNING = "تعلم"
    HELP = "مساعدة"
    UNKNOWN = "غير محدد"


class Emotion(Enum):
    """المشاعر"""
    NEUTRAL = "محايد"
    HAPPY = "سعيد"
    SAD = "حزين"
    ANGRY = "غاضب"
    CURIOUS = "فضولي"
    CONFUSED = "مرتبك"


@dataclass
class Understanding:
    """فهم الرسالة"""
    text: str
    intent: Intent
    entities: Dict[str, str] = field(default_factory=dict)
    emotion: Emotion = Emotion.NEUTRAL
    keywords: List[str] = field(default_factory=list)


@dataclass
class DialogueTurn:
    """دورة حوارية"""
    user_input: str
    bot_response: str
    understanding: Understanding
    timestamp: datetime = field(default_factory=datetime.now)


class IntelligentDialogueSystem:
    """
    🤖 نظام الحوار الذكي
    
    يفهم السياق ويحافظ على الذاكرة ويولد ردود ذكية
    """
    
    # أنماط كشف النوايا (مرتبة حسب الأولوية)
    INTENT_PATTERNS = {
        # الوداع أولاً (لأن "مع السلامة" تحتوي على "السلام")
        Intent.FAREWELL: [
            r"مع السلامة", r"وداعا", r"إلى اللقاء", r"باي", r"سلام$"
        ],
        Intent.GREETING: [
            r"^مرحبا", r"^السلام عليكم", r"^أهلا", r"صباح الخير", r"مساء الخير", r"^هلا", r"^هاي"
        ],
        Intent.QUESTION: [
            r"ما هو", r"ما هي", r"كيف", r"لماذا", r"متى", r"أين", r"من هو", r"هل", r"\?"
        ],
        Intent.REQUEST: [
            r"أريد", r"أحتاج", r"ساعدني", r"أعطني", r"علمني", r"اشرح"
        ],
        Intent.GRATITUDE: [
            r"شكرا", r"ممتن", r"جزاك", r"بارك"
        ],
        Intent.LEARNING: [
            r"أتعلم", r"تعلم", r"درس", r"فهم", r"اشرح لي"
        ],
        Intent.HELP: [
            r"مساعدة", r"ساعد", r"لا أفهم", r"صعب"
        ],
    }
    
    # أنماط كشف المشاعر
    EMOTION_PATTERNS = {
        Emotion.HAPPY: [r"سعيد", r"فرحان", r"رائع", r"ممتاز", r"جميل"],
        Emotion.SAD: [r"حزين", r"مؤلم", r"صعب", r"للأسف"],
        Emotion.ANGRY: [r"غاضب", r"مزعج", r"سيء"],
        Emotion.CURIOUS: [r"أتساءل", r"غريب", r"مثير"],
        Emotion.CONFUSED: [r"لا أفهم", r"محير", r"مربك"],
    }
    
    # قوالب الردود
    RESPONSE_TEMPLATES = {
        Intent.GREETING: [
            "أهلاً وسهلاً! كيف يمكنني مساعدتك اليوم؟",
            "مرحباً! سعيد بالتحدث معك.",
            "أهلاً! أنا بيان، مساعدك الذكي.",
        ],
        Intent.QUESTION: [
            "سؤال جيد! دعني أفكر...",
            "هذا سؤال مهم.",
        ],
        Intent.REQUEST: [
            "بالتأكيد! سأساعدك في ذلك.",
            "حسناً، دعني أساعدك.",
        ],
        Intent.GRATITUDE: [
            "عفواً! سعيد بمساعدتك.",
            "لا شكر على واجب!",
        ],
        Intent.FAREWELL: [
            "مع السلامة! أتمنى لك يوماً سعيداً.",
            "إلى اللقاء! كان من دواعي سروري التحدث معك.",
        ],
        Intent.LEARNING: [
            "رائع! التعلم رحلة ممتعة. من أين تريد أن نبدأ؟",
            "ممتاز! سأكون معلمك. ما الموضوع الذي يهمك؟",
        ],
        Intent.HELP: [
            "أنا هنا للمساعدة! ما الذي تحتاجه؟",
            "لا تقلق، سأساعدك خطوة بخطوة.",
        ],
        Intent.UNKNOWN: [
            "أفهم. هل يمكنك توضيح المزيد؟",
            "مثير للاهتمام! أخبرني المزيد.",
        ],
    }
    
    def __init__(self):
        self.context: List[DialogueTurn] = []  # سياق المحادثة
        self.memory: Dict[str, any] = {}  # ذاكرة طويلة المدى
        self.user_name: Optional[str] = None
        self.session_start = datetime.now()

    def chat(self, user_input: str) -> str:
        """
        المحادثة الرئيسية

        Args:
            user_input: رسالة المستخدم

        Returns:
            رد النظام
        """
        # 1. فهم المدخل
        understanding = self._understand(user_input)

        # 2. استخراج اسم المستخدم إذا ذُكر
        self._extract_user_name(user_input)

        # 3. استرجاع السياق المناسب
        relevant_context = self._retrieve_context(understanding)

        # 4. توليد الرد
        response = self._generate_response(understanding, relevant_context)

        # 5. تحديث السياق
        turn = DialogueTurn(
            user_input=user_input,
            bot_response=response,
            understanding=understanding
        )
        self.context.append(turn)

        # 6. تحديث الذاكرة
        self._update_memory(understanding)

        return response

    def _understand(self, text: str) -> Understanding:
        """فهم النص"""
        intent = self._detect_intent(text)
        emotion = self._detect_emotion(text)
        entities = self._extract_entities(text)
        keywords = self._extract_keywords(text)

        return Understanding(
            text=text,
            intent=intent,
            entities=entities,
            emotion=emotion,
            keywords=keywords
        )

    def _detect_intent(self, text: str) -> Intent:
        """كشف النية"""
        for intent, patterns in self.INTENT_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    return intent
        return Intent.UNKNOWN

    def _detect_emotion(self, text: str) -> Emotion:
        """كشف المشاعر"""
        for emotion, patterns in self.EMOTION_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    return emotion
        return Emotion.NEUTRAL

    def _extract_entities(self, text: str) -> Dict[str, str]:
        """استخراج الكيانات"""
        entities = {}

        # استخراج الأسماء (كلمات تبدأ بأحرف عربية كبيرة أو بعد "أنا")
        name_match = re.search(r"(?:أنا|اسمي)\s+(\w+)", text)
        if name_match:
            entities["name"] = name_match.group(1)

        return entities

    def _extract_keywords(self, text: str) -> List[str]:
        """استخراج الكلمات المفتاحية"""
        # كلمات بسيطة: تقسيم وتصفية
        words = text.split()
        # تصفية الكلمات القصيرة جداً
        keywords = [w for w in words if len(w) > 2]
        return keywords[:5]  # أول 5 كلمات

    def _extract_user_name(self, text: str):
        """استخراج اسم المستخدم"""
        patterns = [
            r"أنا\s+(\w+)",
            r"اسمي\s+(\w+)",
            r"أدعى\s+(\w+)",
        ]
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                self.user_name = match.group(1)
                self.memory["user_name"] = self.user_name
                break

    def _retrieve_context(self, understanding: Understanding) -> List[DialogueTurn]:
        """استرجاع السياق المناسب"""
        # آخر 3 محادثات
        return self.context[-3:] if len(self.context) >= 3 else self.context

    def _generate_response(self, understanding: Understanding,
                          context: List[DialogueTurn]) -> str:
        """توليد الرد"""
        import random

        intent = understanding.intent
        templates = self.RESPONSE_TEMPLATES.get(intent, self.RESPONSE_TEMPLATES[Intent.UNKNOWN])

        # اختيار قالب عشوائي
        base_response = random.choice(templates)

        # تخصيص الرد
        response = self._personalize_response(base_response, understanding, context)

        return response

    def _personalize_response(self, response: str,
                             understanding: Understanding,
                             context: List[DialogueTurn]) -> str:
        """تخصيص الرد"""
        # تخصيص حسب النية أولاً
        if understanding.intent == Intent.FAREWELL:
            if self.user_name:
                return f"مع السلامة {self.user_name}! أتمنى لك يوماً سعيداً."
            return response

        if understanding.intent == Intent.GREETING:
            if self.user_name:
                return f"أهلاً {self.user_name}! كيف يمكنني مساعدتك؟"
            return response

        # إضافة رد عاطفي للردود الأخرى
        if understanding.emotion == Emotion.SAD:
            response = "أتمنى أن تشعر بتحسن قريباً. " + response
        elif understanding.emotion == Emotion.HAPPY:
            response = "سعيد أنك سعيد! " + response
        elif understanding.emotion == Emotion.CONFUSED:
            response = "لا تقلق، سأوضح لك. " + response

        return response

    def _update_memory(self, understanding: Understanding):
        """تحديث الذاكرة"""
        # حفظ الكلمات المفتاحية
        if "keywords" not in self.memory:
            self.memory["keywords"] = []
        self.memory["keywords"].extend(understanding.keywords)

        # حفظ النوايا المتكررة
        if "intents" not in self.memory:
            self.memory["intents"] = {}
        intent_name = understanding.intent.name
        self.memory["intents"][intent_name] = self.memory["intents"].get(intent_name, 0) + 1

    def get_context_summary(self) -> Dict:
        """ملخص السياق"""
        return {
            "turns_count": len(self.context),
            "user_name": self.user_name,
            "session_duration": str(datetime.now() - self.session_start),
            "memory_keys": list(self.memory.keys()),
        }

    def reset(self):
        """إعادة تعيين المحادثة"""
        self.context = []
        self.session_start = datetime.now()
        # الاحتفاظ بالذاكرة طويلة المدى


# دالة مساعدة للمحادثة السريعة
def chat(message: str, system: IntelligentDialogueSystem = None) -> str:
    """محادثة سريعة"""
    if system is None:
        system = IntelligentDialogueSystem()
    return system.chat(message)

