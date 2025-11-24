# 🤖 Chatbot بسيط

بناء بوت محادثة ذكي بالعربية باستخدام البرمجة الهجينة.

---

## 📋 نظرة عامة

Chatbot بسيط يستخدم:
- **البرمجة المنطقية** لقاعدة المعرفة
- **Pattern matching** للفهم
- **البرمجة الإجرائية** للتفاعل

---

## 💻 الكود الكامل

```bayan
# chatbot.bayan
# بوت محادثة ذكي بالعربية

hybrid {
    # ===== قاعدة المعرفة =====
    
    # تحيات
    fact greeting("مرحبا", "أهلاً وسهلاً! كيف يمكنني مساعدتك؟").
    fact greeting("السلام عليكم", "وعليكم السلام ورحمة الله وبركاته!").
    fact greeting("صباح الخير", "صباح النور! كيف حالك؟").
    fact greeting("مساء الخير", "مساء النور! تشرفنا").
    fact greeting("هلا", "هلا فيك! أهلاً بك").
    
    # معلومات عن البوت
    fact info("ما اسمك", "اسمي بيان، مساعد ذكي مبرمج بلغة Bayan").
    fact info("من أنت", "أنا بوت محادثة ذكي. أستطيع الإجابة على أسئلتك ومساعدتك").
    fact info("ماذا تفعل", "أنا أساعدك في الإجابة على الأسئلة وتقديم المعلومات").
    
    # أسئلة شائعة
    fact faq("ما هي بيان", "بيان لغة برمجة هجينة تجمع البرمجة الإجرائية والكائنية والمنطقية").
    fact faq("كيف أتعلم بيان", "يمكنك البدء من docs/getting-started/ أو تجربة Web IDE").
    fact faq("ما هي اللغات المدعومة", "بيان تدعم الكلمات المفتاحية بالعربية والإنجليزية").
    
    # شكر ووداع
    fact thanks("شكرا", "العفو! سعيد بخدمتك").
    fact thanks("شكراً", "العفو! دائماً في الخدمة").
    fact bye("مع السلامة", "مع السلامة! كان من دواعي سروري مساعدتك").
    fact bye("خروج", "إلى اللقاء! أتمنى لك يوماً سعيداً").
    
    # ===== القواعد المنطقية =====
    
    rule respond_to_greeting(?input, ?output) :-
        greeting(?keyword, ?output),
        contains_word(?input, ?keyword).
    
    rule respond_to_info(?input, ?output) :-
        info(?keyword, ?output),
        contains_word(?input, ?keyword).
    
    rule respond_to_faq(?input, ?output) :-
        faq(?keyword, ?output),
        contains_phrase(?input, ?keyword).
    
    rule respond_to_thanks(?input, ?output) :-
        thanks(?keyword, ?output),
        contains_word(?input, ?keyword).
    
    rule respond_to_bye(?input, ?output) :-
        bye(?keyword, ?output),
        contains_word(?input, ?keyword).
    
    # ===== الدوال الإجرائية =====
    
    def normalize_text(text) {
        """تطبيع النص للمطابقة"""
        # إزالة علامات الترقيم
        normalized = text.replace("؟", "").replace("!", "").replace(".", "")
        normalized = normalized.replace("،", "").replace(":", "")
        # تحويل لـ lowercase
        return normalized.strip().lower()
    }
    
    def contains_word_check(text, word) {
        """التحقق من وجود كلمة في النص"""
        normalized_text = normalize_text(text)
        normalized_word = normalize_text(word)
        
        words = normalized_text.split()
        return normalized_word in words
    }
    
    def contains_phrase_check(text, phrase) {
        """التحقق من وجود عبارة في النص"""
        normalized_text = normalize_text(text)
        normalized_phrase = normalize_text(phrase)
        
        return normalized_phrase in normalized_text
    }
    
    def find_response(user_input) {
        """البحث عن رد مناسب"""
        
        # تسجيل الدوال المساعدة كحقائق مؤقتة
        for word in (user_input.split()) {
            assertz(contains_word(user_input, word))
        }
        assertz(contains_phrase(user_input, user_input))
        
        # محاولة الأنماط المختلفة
        responses = []
        
        # تحية
        greeting_results = query respond_to_greeting(user_input, ?resp)
        for r in (greeting_results) {
            responses.append(r["?resp"])
        }
        
        # معلومات
        if (len(responses) == 0) {
            info_results = query respond_to_info(user_input, ?resp)
            for r in (info_results) {
                responses.append(r["?resp"])
            }
        }
        
        # أسئلة شائعة
        if (len(responses) == 0) {
            faq_results = query respond_to_faq(user_input, ?resp)
            for r in (faq_results) {
                responses.append(r["?resp"])
            }
        }
        
        # شكر
        if (len(responses) == 0) {
            thanks_results = query respond_to_thanks(user_input, ?resp)
            for r in (thanks_results) {
                responses.append(r["?resp"])
            }
        }
        
        # وداع
        if (len(responses) == 0) {
            bye_results = query respond_to_bye(user_input, ?resp)
            for r in (bye_results) {
                responses.append(r["?resp"])
            }
        }
        
        # تنظيف
        retractall(contains_word(?, ?)).
        retractall(contains_phrase(?, ?)).
        
        if (len(responses) > 0) {
            return responses[0]
        }
        
        return None
    }
    
    def chat() {
        """حلقة المحادثة الرئيسية"""
        
        print("🤖 بوت بيان الذكي")
        print("="*50)
        print("اكتب رسالتك (اكتب 'خروج' للإنهاء)\n")
        
        conversation_count = 0
        
        while (True) {
            # قراءة المدخل
            user_input = input("أنت: ").strip()
            
            if (user_input == "") {
                continue
            }
            
            # التحقق من الخروج
            if (user_input == "خروج" or user_input == "exit") {
                print("بيان: مع السلامة! 👋")
                break
            }
            
            # البحث عن رد
            response = find_response(user_input)
            
            if (response) {
                print(f"بيان: {response}\n")
            } else {
                # رد افتراضي
                default_responses = [
                    "عذراً، لم أفهم سؤالك. يمكنك إعادة صياغته؟",
                    "لست متأكداً من فهمي. هل يمكنك توضيح أكثر؟",
                    "أنا أتعلم باستمرار. حاول سؤال آخر من فضلك."
                ]
                
                import random
                response_idx = conversation_count % len(default_responses)
                print(f"بيان: {default_responses[response_idx]}\n")
            }
            
            conversation_count = conversation_count + 1
        }
        
        print("\n✨ شكراً لاستخدامك بوت بيان!")
    }
    
    # تشغيل البوت
    chat()
}
```

---

## 🎮 كيفية التشغيل

```bash
python -m bayan.bayan.cli chatbot.bayan
```

---

## 📖 مثال على الحوار

```
🤖 بوت بيان الذكي
==================================================
اكتب رسالتك (اكتب 'خروج' للإنهاء)

أنت: مرحبا
بيان: أهلاً وسهلاً! كيف يمكنني مساعدتك؟

أنت: ما اسمك؟
بيان: اسمي بيان، مساعد ذكي مبرمج بلغة Bayan

أنت: ما هي بيان؟
بيان: بيان لغة برمجة هجينة تجمع البرمجة الإجرائية والكائنية والمنطقية

أنت: كيف أتعلم بيان؟
بيان: يمكنك البدء من docs/getting-started/ أو تجربة Web IDE

أنت: شكراً
بيان: العفو! سعيد بخدمتك

أنت: خروج
بيان: مع السلامة! 👋

✨ شكراً لاستخدامك بوت بيان!
```

---

## 🎯 التوسعات الممكنة

### 1. NLP متقدم
```bayan
import ai.nlp as nlp

# تحليل المشاعر
sentiment = nlp.sentiment_analysis(user_input)

# استخراج الكيانات
entities = nlp.extract_entities(user_input)
```

### 2. تعلم من المحادثات
```bayan
# حفظ المحادثات
fact conversation(user_input, bot_response, timestamp).

# تحليل الأنماط المتكررة
rule frequent_question(?q) :-
    conversation(?q, ?, ?),
    count(?q) > 5.
```

### 3. ذاكرة سياقية
```bayan
# تذكر السياق
fact context("user_name", "أحمد").
fact last_topic("learning").

# استخدامه في الردود
rule personalized_response(?name, ?resp) :-
    context("user_name", ?name),
    ?resp = "مرحباً " + ?name.
```

### 4. API خارجية
```python
#  استدعاء ChatGPT API
import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": user_input}]
)
```

---

## 🎓 ما تعلمناه

✅ **Pattern matching**: مطابقة الأنماط  
✅ **قواعد منطقية**: للاستجابة  
✅ **معالجة نصوص**: تطبيع وبحث  
✅ **حلقة تفاعل**: REPL-style  
✅ **بناء المعرفة**: قاعدة بيانات منطقية  

---

[← العودة لـ Cookbook](../README.md)
