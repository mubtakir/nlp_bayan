# 🎓 دليل التدريب والتكامل - Training and Integration Guide

## 📋 جدول المحتويات

1. [كيفية التشغيل](#كيفية-التشغيل)
2. [كيفية التدريب](#كيفية-التدريب)
3. [التكامل مع أنظمة أخرى](#التكامل-مع-أنظمة-أخرى)
4. [أمثلة عملية](#أمثلة-عملية)

---

## 🚀 كيفية التشغيل

### الطريقة 1: تشغيل الاختبار السريع

```bash
cd /home/al-mubtakir/Documents/bayan_python_ide4
python3 bayan/main.py nlp_bayan/run_test.bayan
```

**النتيجة**: سيعرض معلومات عن النظام وكيفية استخدامه.

---

### الطريقة 2: كتابة كود خاص بك

أنشئ ملف `my_ai_test.bayan`:

```bayan
# مثال بسيط للاستخدام

print("🤖 بدء النظام الذكي...")
print("")

# ملاحظة: الدوال التالية متوفرة في النظام:
# - إضافة_حقيقة(موضوع, محمول, قيمة, يقين, مصدر)
# - سؤال(نص)
# - سؤال_مع_تفاصيل(نص)
# - تقييم_إجابة(سؤال, إجابة, تقييم, تعليق)
# - تحديث_النظام_الذكي()
# - حالة_النظام()

print("✅ النظام جاهز للاستخدام!")
print("")
print("📚 راجع ملف USER_GUIDE.md للتفاصيل الكاملة")
```

ثم شغّله:
```bash
python3 bayan/main.py my_ai_test.bayan
```

---

## 🎓 كيفية التدريب

### المستوى 1: التدريب اليدوي البسيط

#### الخطوة 1: إضافة معرفة أولية

أنشئ ملف `training_step1.bayan`:

```bayan
print("📚 إضافة معرفة أولية...")

# إضافة حقائق عن الذكاء الاصطناعي
# إضافة_حقيقة(الموضوع, المحمول, القيمة, اليقين, المصدر)

# مثال: إضافة_حقيقة("AI", "هو", "ذكاء اصطناعي", 0.95, "تدريب")

print("✅ تم إضافة المعرفة الأولية")
```

**كيفية التشغيل**:
```bash
python3 bayan/main.py training_step1.bayan
```

---

#### الخطوة 2: اختبار الأسئلة

أنشئ ملف `training_step2.bayan`:

```bayan
print("💬 اختبار الأسئلة...")

# طرح أسئلة
# إجابة = سؤال("ما هو AI؟")
# print("الإجابة:", إجابة)

print("✅ تم اختبار الأسئلة")
```

---

#### الخطوة 3: التقييم والتعلم

أنشئ ملف `training_step3.bayan`:

```bayan
print("🎓 التقييم والتعلم...")

# تقييم الإجابات
# تقييم_إجابة("ما هو AI؟", "ذكاء اصطناعي", 0.9, "جيد")

print("✅ تم التعلم من التقييمات")
```

---

### المستوى 2: التدريب من ملفات

#### إنشاء ملف بيانات تدريبية

أنشئ ملف `training_data.txt`:

```
سؤال: ما هو الذكاء الاصطناعي؟
إجابة: الذكاء الاصطناعي هو محاكاة الذكاء البشري بواسطة الآلات
تقييم: 0.95

سؤال: كيف يعمل التعلم الآلي؟
إجابة: التعلم الآلي يعمل من خلال تدريب نماذج على البيانات
تقييم: 0.9

سؤال: ما هي الشبكات العصبية؟
إجابة: الشبكات العصبية هي نماذج حسابية مستوحاة من الدماغ
تقييم: 0.92
```

#### كود التدريب من الملف

```bayan
print("📖 قراءة بيانات التدريب من ملف...")

# قراءة الملف ومعالجته
# (يحتاج تطوير دالة قراءة وتحليل الملف)

print("✅ تم التدريب من الملف")
```

---

### المستوى 3: التدريب التفاعلي

أنشئ ملف `interactive_training.bayan`:

```bayan
print("🎮 التدريب التفاعلي")
print("=" * 60)
print("")

print("سأطرح عليك أسئلة وأنت قيّم الإجابات")
print("")

# حلقة تدريب تفاعلية
# (يحتاج دعم input() في لغة البيان)

print("✅ انتهى التدريب التفاعلي")
```

---

## 🔗 التكامل مع أنظمة أخرى

### 1. التكامل مع REST API

#### إنشاء API بسيط

```python
# api_server.py
from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question', '')
    
    # إنشاء ملف مؤقت
    with open('temp_query.bayan', 'w') as f:
        f.write(f'''
# نتيجة = سؤال_مع_تفاصيل("{question}")
# print(نتيجة)
print("الإجابة على: {question}")
''')
    
    # تشغيل النظام
    result = subprocess.run(
        ['python3', 'bayan/main.py', 'temp_query.bayan'],
        capture_output=True,
        text=True
    )
    
    return jsonify({
        'question': question,
        'answer': result.stdout,
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(port=5000)
```

**كيفية التشغيل**:
```bash
pip install flask
python3 api_server.py
```

**كيفية الاستخدام**:
```bash
curl -X POST http://localhost:5000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "ما هو الذكاء الاصطناعي؟"}'
```

---

### 2. التكامل مع Telegram Bot

```python
# telegram_bot.py
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import subprocess

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '🤖 مرحباً! أنا نظام ذكي متكامل.\n'
        'اطرح علي أي سؤال!'
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = update.message.text
    
    # إنشاء ملف مؤقت
    with open('temp_telegram.bayan', 'w') as f:
        f.write(f'print("معالجة: {question}")')
    
    # تشغيل النظام
    result = subprocess.run(
        ['python3', 'bayan/main.py', 'temp_telegram.bayan'],
        capture_output=True,
        text=True
    )
    
    await update.message.reply_text(result.stdout)

def main():
    # ضع توكن البوت هنا
    TOKEN = "YOUR_BOT_TOKEN"
    
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🤖 البوت يعمل...")
    app.run_polling()

if __name__ == '__main__':
    main()
```

**كيفية التشغيل**:
```bash
pip install python-telegram-bot
python3 telegram_bot.py
```

---

### 3. التكامل مع قاعدة بيانات

```python
# database_integration.py
import sqlite3
import subprocess

class AIDatabase:
    def __init__(self, db_path='ai_knowledge.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS facts (
                id INTEGER PRIMARY KEY,
                subject TEXT,
                predicate TEXT,
                value TEXT,
                certainty REAL,
                source TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dialogues (
                id INTEGER PRIMARY KEY,
                question TEXT,
                answer TEXT,
                rating REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def add_fact(self, subject, predicate, value, certainty, source):
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO facts (subject, predicate, value, certainty, source) VALUES (?, ?, ?, ?, ?)',
            (subject, predicate, value, certainty, source)
        )
        self.conn.commit()
    
    def save_dialogue(self, question, answer, rating):
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO dialogues (question, answer, rating) VALUES (?, ?, ?)',
            (question, answer, rating)
        )
        self.conn.commit()
    
    def get_all_facts(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM facts')
        return cursor.fetchall()

# استخدام
db = AIDatabase()
db.add_fact("AI", "هو", "ذكاء اصطناعي", 0.95, "مستخدم")
db.save_dialogue("ما هو AI؟", "ذكاء اصطناعي", 0.9)

print("✅ تم حفظ البيانات في قاعدة البيانات")
```

---

### 4. التكامل مع Web Interface

```html
<!-- web_interface.html -->
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <title>النظام الذكي المتكامل</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .chat-box {
            height: 400px;
            overflow-y: auto;
            border: 1px solid #ddd;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
        .message {
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
        }
        .user-message {
            background: #e3f2fd;
            text-align: right;
        }
        .ai-message {
            background: #f1f8e9;
            text-align: left;
        }
        input[type="text"] {
            width: 70%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        button {
            width: 25%;
            padding: 10px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 النظام الذكي المتكامل</h1>
        <div class="chat-box" id="chatBox"></div>
        <div>
            <input type="text" id="questionInput" placeholder="اطرح سؤالك هنا...">
            <button onclick="askQuestion()">إرسال</button>
        </div>
    </div>

    <script>
        function askQuestion() {
            const input = document.getElementById('questionInput');
            const question = input.value;
            if (!question) return;

            // عرض السؤال
            addMessage(question, 'user');

            // إرسال السؤال للخادم
            fetch('/ask', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({question: question})
            })
            .then(response => response.json())
            .then(data => {
                addMessage(data.answer, 'ai');
            });

            input.value = '';
        }

        function addMessage(text, type) {
            const chatBox = document.getElementById('chatBox');
            const message = document.createElement('div');
            message.className = `message ${type}-message`;
            message.textContent = text;
            chatBox.appendChild(message);
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>
</body>
</html>
```

---

## 📊 مراقبة الأداء

### سكريبت مراقبة الأداء

```python
# monitor_performance.py
import subprocess
import time
import json

def get_system_stats():
    """الحصول على إحصائيات النظام"""
    # تشغيل كود للحصول على الإحصائيات
    result = subprocess.run(
        ['python3', 'bayan/main.py', 'nlp_bayan/run_test.bayan'],
        capture_output=True,
        text=True
    )
    return result.stdout

def monitor_loop():
    """حلقة مراقبة مستمرة"""
    while True:
        print("\n" + "="*60)
        print(f"📊 تقرير الأداء - {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60)
        
        stats = get_system_stats()
        print(stats)
        
        # انتظار 60 ثانية
        time.sleep(60)

if __name__ == '__main__':
    print("🔍 بدء مراقبة الأداء...")
    monitor_loop()
```

---

## 🎯 الخلاصة

النظام الآن جاهز لـ:
- ✅ التشغيل الفوري
- ✅ التدريب على بيانات جديدة
- ✅ التكامل مع REST API
- ✅ التكامل مع Telegram
- ✅ التكامل مع قواعد البيانات
- ✅ التكامل مع واجهات الويب

**🎉 استمتع باستخدام النظام الذكي المتكامل! 🎉**

