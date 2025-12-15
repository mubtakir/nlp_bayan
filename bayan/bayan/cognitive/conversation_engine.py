"""
محرك الحوار الذكي - Conversation Engine
========================================

نظام محادثة متقدم يحتفظ بالسياق ويستخدم الذاكرة قصيرة وطويلة المدى.

المكونات:
- ConversationMemory: ذاكرة المحادثة
- DialogueManager: إدارة أدوار الحوار
- ContextTracker: تتبع السياق
- ConversationEngine: المحرك الرئيسي

المطور: باسل يحيى عبدالله
"""

import sys
import os
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import json

# Ensure we can import bayan packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from bayan.bayan.istinbat_engine import IstinbatEngine


class MessageRole(Enum):
    """أدوار المحادثة"""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


@dataclass
class Message:
    """رسالة واحدة في المحادثة"""
    role: MessageRole
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "role": self.role.value,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
            "metadata": self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Message':
        return cls(
            role=MessageRole(data["role"]),
            content=data["content"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            metadata=data.get("metadata", {})
        )


@dataclass
class ConversationTurn:
    """دور واحد في المحادثة (سؤال + إجابة)"""
    user_message: Message
    assistant_message: Optional[Message] = None
    context_snapshot: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def is_complete(self) -> bool:
        return self.assistant_message is not None


class ConversationMemory:
    """
    ذاكرة المحادثة - قصيرة وطويلة المدى
    
    - الذاكرة القصيرة: آخر N دور
    - الذاكرة الطويلة: ملخصات وحقائق مستخرجة
    """
    
    def __init__(self, short_term_limit: int = 10):
        self.short_term_limit = short_term_limit
        self.short_term: List[ConversationTurn] = []
        self.long_term: Dict[str, Any] = {
            "summaries": [],      # ملخصات المحادثات السابقة
            "facts": [],          # حقائق مستخرجة
            "user_profile": {},   # معلومات عن المستخدم
            "topics": []          # المواضيع التي نوقشت
        }
        self.conversation_id: str = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def add_turn(self, turn: ConversationTurn):
        """إضافة دور جديد"""
        self.short_term.append(turn)
        
        # نقل للذاكرة الطويلة إذا تجاوزنا الحد
        if len(self.short_term) > self.short_term_limit:
            old_turn = self.short_term.pop(0)
            self._consolidate_to_long_term(old_turn)
    
    def _consolidate_to_long_term(self, turn: ConversationTurn):
        """تحويل دور قديم لملخص في الذاكرة الطويلة"""
        if turn.is_complete:
            summary = {
                "user_said": turn.user_message.content[:100],
                "assistant_said": turn.assistant_message.content[:100] if turn.assistant_message else "",
                "timestamp": turn.user_message.timestamp.isoformat()
            }
            self.long_term["summaries"].append(summary)
    
    def add_fact(self, fact: str, source: str = "conversation"):
        """إضافة حقيقة مستخرجة"""
        self.long_term["facts"].append({
            "fact": fact,
            "source": source,
            "timestamp": datetime.now().isoformat()
        })
    
    def add_topic(self, topic: str):
        """إضافة موضوع"""
        if topic not in self.long_term["topics"]:
            self.long_term["topics"].append(topic)
    
    def update_user_profile(self, key: str, value: Any):
        """تحديث ملف المستخدم"""
        self.long_term["user_profile"][key] = value
    
    def get_context_window(self, n: int = 5) -> List[Dict[str, str]]:
        """الحصول على آخر n دور للسياق"""
        context = []
        for turn in self.short_term[-n:]:
            context.append({"role": "user", "content": turn.user_message.content})
            if turn.assistant_message:
                context.append({"role": "assistant", "content": turn.assistant_message.content})
        return context
    
    def get_relevant_facts(self, query: str) -> List[str]:
        """الحصول على الحقائق ذات الصلة"""
        # بحث بسيط بالكلمات المفتاحية
        query_words = set(query.lower().split())
        relevant = []
        for fact_entry in self.long_term["facts"]:
            fact_words = set(fact_entry["fact"].lower().split())
            if query_words & fact_words:
                relevant.append(fact_entry["fact"])
        return relevant
    
    def save(self, filepath: str):
        """حفظ الذاكرة"""
        data = {
            "conversation_id": self.conversation_id,
            "short_term": [
                {
                    "user": t.user_message.to_dict(),
                    "assistant": t.assistant_message.to_dict() if t.assistant_message else None,
                    "context": t.context_snapshot
                }
                for t in self.short_term
            ],
            "long_term": self.long_term
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load(self, filepath: str):
        """تحميل الذاكرة"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        self.conversation_id = data["conversation_id"]
        self.long_term = data["long_term"]
        self.short_term = []
        
        for turn_data in data["short_term"]:
            user_msg = Message.from_dict(turn_data["user"])
            asst_msg = Message.from_dict(turn_data["assistant"]) if turn_data["assistant"] else None
            turn = ConversationTurn(user_msg, asst_msg, turn_data.get("context", {}))
            self.short_term.append(turn)


class ContextTracker:
    """
    تتبع السياق الحالي للمحادثة
    
    يحلل المحادثة لتحديد:
    - الموضوع الحالي
    - الكيانات المذكورة
    - نية المستخدم
    """
    
    def __init__(self):
        self.current_topic: Optional[str] = None
        self.entities: Dict[str, str] = {}  # اسم -> نوع
        self.intent_history: List[str] = []
        self.mood: str = "neutral"
    
    def analyze(self, message: str) -> Dict[str, Any]:
        """تحليل رسالة لاستخراج السياق"""
        analysis = {
            "topic": self._detect_topic(message),
            "intent": self._detect_intent(message),
            "entities": self._extract_entities(message),
            "mood": self._detect_mood(message)
        }
        
        # تحديث الحالة
        if analysis["topic"]:
            self.current_topic = analysis["topic"]
        self.entities.update(analysis["entities"])
        self.intent_history.append(analysis["intent"])
        self.mood = analysis["mood"]
        
        return analysis
    
    def _detect_topic(self, message: str) -> Optional[str]:
        """اكتشاف الموضوع"""
        topics = {
            "تقنية": ["برمجة", "كود", "تطوير", "ذكاء", "اصطناعي", "حاسوب"],
            "علوم": ["رياضيات", "فيزياء", "كيمياء", "أحياء", "علم"],
            "هندسة": ["تصميم", "ترس", "محرك", "آلة", "ميكانيكي"],
            "لغة": ["عربي", "كلمة", "جملة", "نحو", "صرف", "بلاغة"],
            "عام": []
        }
        
        message_lower = message.lower()
        for topic, keywords in topics.items():
            if any(kw in message_lower for kw in keywords):
                return topic
        return self.current_topic or "عام"
    
    def _detect_intent(self, message: str) -> str:
        """اكتشاف نية المستخدم"""
        intents = {
            "question": ["ما", "من", "أين", "كيف", "لماذا", "متى", "هل", "؟"],
            "command": ["اعمل", "أنشئ", "صمم", "احسب", "افعل", "نفذ"],
            "greeting": ["مرحبا", "السلام", "أهلا", "صباح", "مساء"],
            "farewell": ["وداعا", "إلى اللقاء", "مع السلامة"],
            "thanks": ["شكرا", "شكر", "ممتن"],
            "statement": []
        }
        
        message_lower = message.lower()
        for intent, markers in intents.items():
            if any(marker in message_lower for marker in markers):
                return intent
        return "statement"
    
    def _extract_entities(self, message: str) -> Dict[str, str]:
        """استخراج الكيانات"""
        entities = {}
        
        # أرقام
        import re
        numbers = re.findall(r'\d+(?:\.\d+)?', message)
        if numbers:
            entities["numbers"] = numbers
        
        # كلمات بين علامات تنصيص
        quoted = re.findall(r'"([^"]+)"', message)
        if quoted:
            entities["quoted"] = quoted
        
        return entities
    
    def _detect_mood(self, message: str) -> str:
        """اكتشاف المزاج"""
        positive = ["رائع", "ممتاز", "جميل", "شكرا", "أحب"]
        negative = ["سيء", "مشكلة", "خطأ", "لا يعمل", "فشل"]
        
        message_lower = message.lower()
        if any(w in message_lower for w in positive):
            return "positive"
        elif any(w in message_lower for w in negative):
            return "negative"
        return "neutral"
    
    def get_context_summary(self) -> Dict[str, Any]:
        """ملخص السياق الحالي"""
        return {
            "topic": self.current_topic,
            "entities": self.entities,
            "recent_intents": self.intent_history[-3:] if self.intent_history else [],
            "mood": self.mood
        }


class DialogueManager:
    """
    إدارة أدوار الحوار
    
    يحدد:
    - كيفية الرد على أنواع مختلفة من الرسائل
    - متى يطرح أسئلة توضيحية
    - كيفية إدارة تدفق الحوار
    """
    
    def __init__(self, engine: IstinbatEngine):
        self.engine = engine
        self.dialogue_state: str = "idle"  # idle, questioning, responding, clarifying
        self.pending_clarification: Optional[str] = None
    
    def process_intent(self, intent: str, context: Dict[str, Any]) -> Tuple[str, str]:
        """
        معالجة النية وتحديد نوع الاستجابة
        
        Returns:
            (action_type, action_data)
        """
        if intent == "greeting":
            self.dialogue_state = "responding"
            return ("greet", "")
        
        elif intent == "farewell":
            self.dialogue_state = "idle"
            return ("farewell", "")
        
        elif intent == "thanks":
            return ("acknowledge", "")
        
        elif intent == "question":
            self.dialogue_state = "responding"
            return ("answer", "")
        
        elif intent == "command":
            self.dialogue_state = "responding"
            return ("execute", "")
        
        else:
            return ("discuss", "")
    
    def needs_clarification(self, message: str, context: Dict[str, Any]) -> Optional[str]:
        """تحديد إذا كانت الرسالة تحتاج توضيح"""
        # رسالة قصيرة جداً
        if len(message.split()) < 2:
            return "هل يمكنك توضيح ما تقصده أكثر؟"
        
        # ضمائر بدون مرجع
        pronouns = ["هذا", "ذلك", "هو", "هي", "هم"]
        if any(p in message for p in pronouns) and not context.get("entities"):
            return "عن أي شيء تتحدث بالتحديد؟"
        
        return None
    
    def generate_response_structure(self, action_type: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """توليد هيكل الاستجابة"""
        structures = {
            "greet": {
                "template": "greeting",
                "include_context": False,
                "tone": "friendly"
            },
            "farewell": {
                "template": "farewell",
                "include_context": False,
                "tone": "warm"
            },
            "acknowledge": {
                "template": "thanks_response",
                "include_context": False,
                "tone": "humble"
            },
            "answer": {
                "template": "answer",
                "include_context": True,
                "use_engine": True,
                "tone": "informative"
            },
            "execute": {
                "template": "execution_result",
                "include_context": True,
                "use_engine": True,
                "tone": "professional"
            },
            "discuss": {
                "template": "discussion",
                "include_context": True,
                "tone": "conversational"
            }
        }
        return structures.get(action_type, structures["discuss"])


class ConversationEngine:
    """
    المحرك الرئيسي للمحادثة
    
    يجمع كل المكونات لتقديم تجربة حوار ذكية.
    """
    
    def __init__(self, engine: Optional[IstinbatEngine] = None):
        self.engine = engine or IstinbatEngine(enable_dialect_support=True)
        self.memory = ConversationMemory()
        self.context_tracker = ContextTracker()
        self.dialogue_manager = DialogueManager(self.engine)
        
        # قوالب الاستجابة
        self.response_templates = {
            "greeting": [
                "مرحباً! كيف يمكنني مساعدتك اليوم؟",
                "أهلاً وسهلاً! أنا هنا للمساعدة.",
                "مرحباً بك! ما الذي تود معرفته؟"
            ],
            "farewell": [
                "إلى اللقاء! سعدت بالحديث معك.",
                "مع السلامة! لا تتردد في العودة."
            ],
            "thanks_response": [
                "العفو! سعيد بمساعدتك.",
                "لا شكر على واجب!"
            ],
            "clarification": [
                "لم أفهم تماماً. هل يمكنك التوضيح؟",
                "أحتاج مزيداً من التفاصيل لمساعدتك."
            ]
        }
    
    def chat(self, user_input: str) -> str:
        """
        نقطة الدخول الرئيسية للمحادثة
        
        Args:
            user_input: رسالة المستخدم
            
        Returns:
            رد المساعد
        """
        # 1. إنشاء رسالة المستخدم
        user_message = Message(
            role=MessageRole.USER,
            content=user_input
        )
        
        # 2. تحليل السياق
        context_analysis = self.context_tracker.analyze(user_input)
        
        # 3. فحص الحاجة للتوضيح
        clarification = self.dialogue_manager.needs_clarification(
            user_input, 
            self.context_tracker.get_context_summary()
        )
        
        if clarification:
            response_text = clarification
        else:
            # 4. تحديد نوع الاستجابة
            action_type, action_data = self.dialogue_manager.process_intent(
                context_analysis["intent"],
                context_analysis
            )
            
            # 5. توليد الاستجابة
            response_text = self._generate_response(
                action_type, 
                user_input, 
                context_analysis
            )
        
        # 6. إنشاء رسالة المساعد
        assistant_message = Message(
            role=MessageRole.ASSISTANT,
            content=response_text,
            metadata={"context": context_analysis}
        )
        
        # 7. حفظ في الذاكرة
        turn = ConversationTurn(
            user_message=user_message,
            assistant_message=assistant_message,
            context_snapshot=context_analysis
        )
        self.memory.add_turn(turn)
        
        # 8. تحديث الموضوعات
        if context_analysis.get("topic"):
            self.memory.add_topic(context_analysis["topic"])
        
        return response_text
    
    def _generate_response(self, action_type: str, user_input: str, context: Dict[str, Any]) -> str:
        """توليد الاستجابة بناءً على نوع الإجراء"""
        import random
        
        if action_type == "greet":
            return random.choice(self.response_templates["greeting"])
        
        elif action_type == "farewell":
            return random.choice(self.response_templates["farewell"])
        
        elif action_type == "acknowledge":
            return random.choice(self.response_templates["thanks_response"])
        
        elif action_type in ["answer", "execute"]:
            # استخدام محرك الاستنباط
            return self._process_with_engine(user_input, context)
        
        else:
            # مناقشة عامة
            return self._generate_discussion_response(user_input, context)
    
    def _process_with_engine(self, user_input: str, context: Dict[str, Any]) -> str:
        """معالجة مع محرك الاستنباط"""
        try:
            result = self.engine.process(user_input)
            
            if result and result.equation:
                # استخراج معلومات من المعادلة
                entities = list(result.equation.entities.keys())
                event = result.equation.event
                
                # بناء استجابة
                if event:
                    response = f"فهمت أنك تتحدث عن '{event}'."
                    if entities:
                        response += f" الكيانات المذكورة: {', '.join(entities)}."
                    
                    # إضافة نتائج منطقية إن وجدت
                    if result.logical_deductions:
                        response += f" واستنتجت: {result.logical_deductions[0]}"
                    
                    return response
                else:
                    return f"فهمت رسالتك. الكيانات المذكورة: {', '.join(entities) if entities else 'لم أجد كيانات محددة'}."
            else:
                return "فهمت ما قلته، لكن لم أستطع تحليله بعمق. هل يمكنك إعادة الصياغة؟"
                
        except Exception as e:
            return f"واجهت صعوبة في الفهم. هل يمكنك توضيح ما تقصده؟"
    
    def _generate_discussion_response(self, user_input: str, context: Dict[str, Any]) -> str:
        """توليد استجابة نقاشية"""
        topic = context.get("topic", "عام")
        
        # الحصول على حقائق ذات صلة من الذاكرة
        relevant_facts = self.memory.get_relevant_facts(user_input)
        
        if relevant_facts:
            return f"بناءً على ما ناقشناه سابقاً: {relevant_facts[0]}. هل تريد المزيد من التفاصيل؟"
        else:
            return f"هذا موضوع مثير للاهتمام في مجال {topic}. هل تريد أن أوضح أكثر؟"
    
    def add_fact(self, fact: str):
        """إضافة حقيقة للذاكرة"""
        self.memory.add_fact(fact, source="manual")
    
    def get_conversation_summary(self) -> Dict[str, Any]:
        """الحصول على ملخص المحادثة"""
        return {
            "turns_count": len(self.memory.short_term),
            "topics_discussed": self.memory.long_term["topics"],
            "facts_learned": len(self.memory.long_term["facts"]),
            "current_context": self.context_tracker.get_context_summary()
        }
    
    def save_conversation(self, filepath: str):
        """حفظ المحادثة"""
        self.memory.save(filepath)
    
    def load_conversation(self, filepath: str):
        """تحميل محادثة سابقة"""
        self.memory.load(filepath)


# ============ اختبار ============
if __name__ == "__main__":
    print("=" * 50)
    print("اختبار محرك الحوار الذكي")
    print("=" * 50)
    
    engine = ConversationEngine()
    
    # اختبار التحيات
    print("\n1. اختبار التحية:")
    print(f"   المستخدم: مرحبا")
    print(f"   المساعد: {engine.chat('مرحبا')}")
    
    # اختبار سؤال
    print("\n2. اختبار سؤال:")
    print(f"   المستخدم: ما هو الذكاء الاصطناعي؟")
    print(f"   المساعد: {engine.chat('ما هو الذكاء الاصطناعي؟')}")
    
    # اختبار أمر
    print("\n3. اختبار أمر:")
    print(f"   المستخدم: صمم لي ترس بقطر 50")
    print(f"   المساعد: {engine.chat('صمم لي ترس بقطر 50')}")
    
    # اختبار الوداع
    print("\n4. اختبار الوداع:")
    print(f"   المستخدم: شكراً، إلى اللقاء")
    print(f"   المساعد: {engine.chat('شكراً، إلى اللقاء')}")
    
    # ملخص
    print("\n5. ملخص المحادثة:")
    summary = engine.get_conversation_summary()
    print(f"   عدد الأدوار: {summary['turns_count']}")
    print(f"   المواضيع: {summary['topics_discussed']}")
    
    print("\n✅ اكتمل الاختبار بنجاح!")
