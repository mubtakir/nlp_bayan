#!/bin/bash

# سكريبت لتشغيل خادم ويب محلي لواجهات بصيرة

echo "🌐 تشغيل خادم ويب محلي لواجهات بصيرة..."
echo ""

# الانتقال إلى مجلد المشروع
cd "$(dirname "$0")"

# التحقق من وجود Node.js
if command -v node &> /dev/null; then
    echo "✅ Node.js موجود"
    
    # التحقق من وجود http-server
    if command -v http-server &> /dev/null; then
        echo "✅ http-server موجود"
        echo ""
        echo "🚀 تشغيل الخادم على المنفذ 8000..."
        echo ""
        echo "📱 افتح المتصفح على:"
        echo "   http://localhost:8000"
        echo "   http://localhost:8000/index.html"
        echo "   http://localhost:8000/interactive-chat.html"
        echo ""
        echo "⏹️  للإيقاف: اضغط Ctrl+C"
        echo ""
        http-server -p 8000 -o
    else
        echo "⚠️  http-server غير موجود، جاري التثبيت..."
        npm install -g http-server
        echo ""
        echo "🚀 تشغيل الخادم..."
        http-server -p 8000 -o
    fi
    
# التحقق من وجود Python
elif command -v python3 &> /dev/null; then
    echo "✅ Python 3 موجود"
    echo ""
    echo "🚀 تشغيل الخادم على المنفذ 8000..."
    echo ""
    echo "📱 افتح المتصفح على:"
    echo "   http://localhost:8000"
    echo "   http://localhost:8000/index.html"
    echo "   http://localhost:8000/interactive-chat.html"
    echo ""
    echo "⏹️  للإيقاف: اضغط Ctrl+C"
    echo ""
    python3 -m http.server 8000

elif command -v python &> /dev/null; then
    echo "✅ Python موجود"
    echo ""
    echo "🚀 تشغيل الخادم على المنفذ 8000..."
    echo ""
    echo "📱 افتح المتصفح على:"
    echo "   http://localhost:8000"
    echo ""
    echo "⏹️  للإيقاف: اضغط Ctrl+C"
    echo ""
    python -m SimpleHTTPServer 8000

else
    echo "❌ لم يتم العثور على Node.js أو Python"
    echo ""
    echo "الحلول البديلة:"
    echo "1. ثبت Node.js: sudo apt install nodejs npm"
    echo "2. ثبت Python: sudo apt install python3"
    echo "3. افتح الملفات مباشرة في المتصفح:"
    echo "   firefox index.html"
    echo ""
fi

