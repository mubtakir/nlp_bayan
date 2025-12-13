#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌐 REST API Server للنظام الذكي المتكامل
Intelligent System REST API Server

يوفر واجهة REST API للتفاعل مع النظام الذكي
Provides REST API interface to interact with the intelligent system
"""

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import subprocess
import json
import os
import tempfile
from datetime import datetime

app = Flask(__name__)
CORS(app)  # للسماح بالطلبات من مصادر مختلفة

# مسار المفسر
BAYAN_INTERPRETER = "bayan/main.py"

# ============================================
# HTML Template للواجهة
# ============================================

HTML_TEMPLATE = """
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>النظام الذكي المتكامل - Intelligent System</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        .header h1 { font-size: 2em; margin-bottom: 10px; }
        .header p { opacity: 0.9; }
        .chat-container {
            height: 500px;
            overflow-y: auto;
            padding: 20px;
            background: #f8f9fa;
        }
        .message {
            margin: 15px 0;
            padding: 15px 20px;
            border-radius: 15px;
            max-width: 80%;
            animation: slideIn 0.3s ease;
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .user-message {
            background: #e3f2fd;
            margin-left: auto;
            text-align: right;
            border-bottom-right-radius: 5px;
        }
        .ai-message {
            background: #f1f8e9;
            margin-right: auto;
            text-align: left;
            border-bottom-left-radius: 5px;
        }
        .input-container {
            padding: 20px;
            background: white;
            border-top: 1px solid #e0e0e0;
            display: flex;
            gap: 10px;
        }
        input[type="text"] {
            flex: 1;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 25px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        input[type="text"]:focus {
            outline: none;
            border-color: #667eea;
        }
        button {
            padding: 15px 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            cursor: pointer;
            transition: transform 0.2s;
        }
        button:hover { transform: scale(1.05); }
        button:active { transform: scale(0.95); }
        .stats {
            padding: 20px;
            background: #f8f9fa;
            border-top: 1px solid #e0e0e0;
            display: flex;
            justify-content: space-around;
            text-align: center;
        }
        .stat-item { flex: 1; }
        .stat-value { font-size: 24px; font-weight: bold; color: #667eea; }
        .stat-label { font-size: 12px; color: #666; margin-top: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 النظام الذكي المتكامل</h1>
            <p>Intelligent Integrated System - Powered by Bayan Language</p>
        </div>
        
        <div class="chat-container" id="chatContainer">
            <div class="message ai-message">
                مرحباً! أنا نظام ذكي متكامل. اطرح علي أي سؤال! 🚀
            </div>
        </div>
        
        <div class="input-container">
            <input type="text" id="questionInput" placeholder="اطرح سؤالك هنا..." 
                   onkeypress="if(event.key==='Enter') askQuestion()">
            <button onclick="askQuestion()">إرسال 📤</button>
        </div>
        
        <div class="stats">
            <div class="stat-item">
                <div class="stat-value" id="totalQuestions">0</div>
                <div class="stat-label">إجمالي الأسئلة</div>
            </div>
            <div class="stat-item">
                <div class="stat-value" id="avgConfidence">0%</div>
                <div class="stat-label">متوسط الثقة</div>
            </div>
            <div class="stat-item">
                <div class="stat-value" id="responseTime">0ms</div>
                <div class="stat-label">وقت الاستجابة</div>
            </div>
        </div>
    </div>

    <script>
        let questionCount = 0;
        let totalConfidence = 0;
        
        function addMessage(text, type) {
            const container = document.getElementById('chatContainer');
            const message = document.createElement('div');
            message.className = `message ${type}-message`;
            message.textContent = text;
            container.appendChild(message);
            container.scrollTop = container.scrollHeight;
        }
        
        async function askQuestion() {
            const input = document.getElementById('questionInput');
            const question = input.value.trim();
            if (!question) return;
            
            addMessage(question, 'user');
            input.value = '';
            
            const startTime = Date.now();
            
            try {
                const response = await fetch('/api/ask', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({question: question})
                });
                
                const data = await response.json();
                const endTime = Date.now();
                
                addMessage(data.answer || data.message, 'ai');
                
                // تحديث الإحصائيات
                questionCount++;
                document.getElementById('totalQuestions').textContent = questionCount;
                document.getElementById('responseTime').textContent = (endTime - startTime) + 'ms';
                
            } catch (error) {
                addMessage('عذراً، حدث خطأ: ' + error.message, 'ai');
            }
        }
    </script>
</body>
</html>
"""

# ============================================
# API Endpoints
# ============================================

@app.route('/')
def index():
    """الصفحة الرئيسية"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/ask', methods=['POST'])
def ask_question():
    """
    طرح سؤال على النظام
    POST /api/ask
    Body: {"question": "ما هو الذكاء الاصطناعي؟"}
    """
    try:
        data = request.json
        question = data.get('question', '')
        
        if not question:
            return jsonify({'error': 'السؤال مطلوب'}), 400
        
        # إنشاء ملف مؤقت
        with tempfile.NamedTemporaryFile(mode='w', suffix='.bayan', delete=False, encoding='utf-8') as f:
            f.write(f'print("معالجة السؤال: {question}")\n')
            f.write(f'print("الإجابة: النظام قيد التطوير")\n')
            temp_file = f.name
        
        try:
            # تشغيل المفسر
            result = subprocess.run(
                ['python3', BAYAN_INTERPRETER, temp_file],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            return jsonify({
                'question': question,
                'answer': result.stdout.strip() if result.stdout else 'لا توجد إجابة',
                'confidence': 0.85,
                'timestamp': datetime.now().isoformat()
            })
            
        finally:
            # حذف الملف المؤقت
            if os.path.exists(temp_file):
                os.unlink(temp_file)
                
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/status', methods=['GET'])
def get_status():
    """الحصول على حالة النظام"""
    return jsonify({
        'status': 'active',
        'system': 'Intelligent Integrated System',
        'version': '1.0.0',
        'language': 'Bayan',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """فحص صحة النظام"""
    return jsonify({'status': 'healthy'})

# ============================================
# Main
# ============================================

if __name__ == '__main__':
    print("=" * 70)
    print("🌐 بدء خادم REST API للنظام الذكي")
    print("=" * 70)
    print("")
    print("📡 الخادم يعمل على: http://localhost:5000")
    print("🌍 الواجهة: http://localhost:5000")
    print("🔌 API: http://localhost:5000/api/ask")
    print("")
    print("✅ اضغط Ctrl+C للإيقاف")
    print("")
    
    app.run(host='0.0.0.0', port=5000, debug=True)

