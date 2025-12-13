#!/bin/bash
# -*- coding: utf-8 -*-
"""
🔧 الصيانة اليومية - نظام بصيرة الثوري
========================================

سكريبت الصيانة اليومية لنظام بصيرة الثوري
يقوم بفحص النظام وإضافة معرفة جديدة وإنتاج التقارير

الاستخدام:
    ./daily_maintenance.sh

المطور: باسل يحيى عبدالله
"""

# ألوان للعرض
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# دالة طباعة ملونة
print_colored() {
    echo -e "${2}${1}${NC}"
}

# دالة طباعة العنوان
print_header() {
    echo
    print_colored "🔧 $1" $CYAN
    echo "=================================================="
}

# دالة فحص النجاح
check_success() {
    if [ $? -eq 0 ]; then
        print_colored "✅ $1" $GREEN
    else
        print_colored "❌ $1" $RED
        return 1
    fi
}

# بداية السكريبت
print_colored "🧬 بدء الصيانة اليومية لنظام بصيرة الثوري" $PURPLE
print_colored "📅 التاريخ: $(date '+%Y-%m-%d %H:%M:%S')" $BLUE
echo

# التحقق من المجلد الحالي
if [ ! -f "revolutionary_knowledge_system.py" ]; then
    print_colored "❌ خطأ: لم يتم العثور على ملفات النظام في المجلد الحالي" $RED
    print_colored "تأكد من تشغيل السكريپت من مجلد المشروع" $YELLOW
    exit 1
fi

# 1. تفعيل البيئة الافتراضية
print_header "تفعيل البيئة الافتراضية"

# البحث عن البيئة الافتراضية
if [ -d "myenv" ]; then
    ENV_PATH="myenv"
elif [ -d "../myenv" ]; then
    ENV_PATH="../myenv"
elif [ -d "/home/al-mubtakir/Desktop/myenv" ]; then
    ENV_PATH="/home/al-mubtakir/Desktop/myenv"
else
    print_colored "❌ لم يتم العثور على البيئة الافتراضية" $RED
    print_colored "تأكد من وجود مجلد myenv" $YELLOW
    exit 1
fi

source $ENV_PATH/bin/activate
check_success "تم تفعيل البيئة الافتراضية"

# التحقق من Python
python3 --version > /dev/null 2>&1
check_success "Python متاح"

# 2. فحص حالة Ollama
print_header "فحص حالة Ollama"

if ollama list > /dev/null 2>&1; then
    check_success "Ollama يعمل بشكل طبيعي"
    
    # عرض النماذج المتاحة
    print_colored "📋 النماذج المتاحة:" $BLUE
    ollama list | grep -v "NAME" | while read line; do
        if [ ! -z "$line" ]; then
            echo "  🦙 $line"
        fi
    done
else
    print_colored "❌ مشكلة في Ollama - محاولة إعادة التشغيل..." $YELLOW
    
    # محاولة إعادة تشغيل Ollama
    sudo systemctl restart ollama 2>/dev/null
    sleep 5
    
    if ollama list > /dev/null 2>&1; then
        check_success "تم إعادة تشغيل Ollama بنجاح"
    else
        print_colored "❌ فشل في إعادة تشغيل Ollama" $RED
        print_colored "قد تحتاج إلى تدخل يدوي" $YELLOW
    fi
fi

# 3. فحص قواعد البيانات
print_header "فحص قواعد البيانات"

if [ -d "databases" ]; then
    check_success "مجلد قواعد البيانات موجود"
    
    if [ -f "databases/revolutionary_knowledge_system.db" ]; then
        check_success "قاعدة البيانات الرئيسية موجودة"
        
        # فحص حجم قاعدة البيانات
        db_size=$(du -h databases/revolutionary_knowledge_system.db | cut -f1)
        print_colored "📊 حجم قاعدة البيانات: $db_size" $BLUE
    else
        print_colored "❌ قاعدة البيانات الرئيسية مفقودة - إعادة إنشاء..." $YELLOW
        python3 -c "from revolutionary_knowledge_system import RevolutionaryKnowledgeSystem; RevolutionaryKnowledgeSystem()" 2>/dev/null
        check_success "تم إعادة إنشاء قاعدة البيانات"
    fi
else
    print_colored "❌ مجلد قواعد البيانات مفقود - إنشاء..." $YELLOW
    mkdir -p databases
    python3 -c "from revolutionary_knowledge_system import RevolutionaryKnowledgeSystem; RevolutionaryKnowledgeSystem()" 2>/dev/null
    check_success "تم إنشاء مجلد قواعد البيانات"
fi

# 4. تشغيل تقرير النمو
print_header "إنتاج تقرير النمو"

if [ -f "monitor_growth.py" ]; then
    python3 monitor_growth.py 2>/dev/null
    check_success "تم إنتاج تقرير النمو"
else
    print_colored "❌ ملف مراقب النمو غير موجود" $RED
fi

# 5. إضافة معرفة يومية
print_header "إضافة معرفة يومية"

# قائمة مواضيع يومية متنوعة
daily_topics=(
    "تطورات جديدة في التكنولوجيا"
    "اكتشافات علمية حديثة"
    "تقنيات البرمجة المتقدمة"
    "نظريات رياضية مهمة"
    "مفاهيم فيزيائية أساسية"
    "تطبيقات الذكاء الاصطناعي"
    "علوم الحاسوب الحديثة"
    "الابتكارات في الطب"
    "التقنيات البيئية المستدامة"
    "تطوير البرمجيات الحديث"
)

# اختيار موضوع عشوائي
topic_index=$((RANDOM % ${#daily_topics[@]}))
selected_topic="${daily_topics[$topic_index]}"

print_colored "📖 موضوع اليوم: $selected_topic" $BLUE

# محاولة إضافة المعرفة
python3 -c "
from revolutionary_knowledge_system import RevolutionaryKnowledgeSystem
import sys

try:
    system = RevolutionaryKnowledgeSystem()
    topic = '$selected_topic'
    
    print(f'🔍 استخراج معرفة حول: {topic}')
    result = system.extract_from_external_source('ollama', topic)
    
    if result and len(result.strip()) > 50:
        print(f'✅ تم إضافة معرفة جديدة ({len(result)} حرف)')
        sys.exit(0)
    else:
        print('❌ فشل في إضافة المعرفة أو محتوى ضعيف')
        sys.exit(1)
        
except Exception as e:
    print(f'❌ خطأ: {str(e)[:100]}')
    sys.exit(1)
" 2>/dev/null

if [ $? -eq 0 ]; then
    check_success "تم إضافة معرفة يومية جديدة"
else
    print_colored "❌ فشل في إضافة المعرفة اليومية" $RED
    print_colored "قد يكون بسبب مشكلة في الاتصال أو Ollama" $YELLOW
fi

# 6. فحص مساحة القرص
print_header "فحص مساحة القرص"

disk_usage=$(df -h . | tail -1 | awk '{print $5}' | sed 's/%//')
if [ $disk_usage -gt 90 ]; then
    print_colored "⚠️ تحذير: مساحة القرص ممتلئة ($disk_usage%)" $YELLOW
    print_colored "فكر في تنظيف الملفات غير المهمة" $YELLOW
else
    print_colored "✅ مساحة القرص مناسبة ($disk_usage%)" $GREEN
fi

# 7. إنشاء نسخة احتياطية (اختياري)
print_header "النسخ الاحتياطي"

backup_dir="backups"
if [ ! -d "$backup_dir" ]; then
    mkdir -p "$backup_dir"
fi

# نسخ احتياطية أسبوعية فقط (يوم الأحد)
if [ $(date +%u) -eq 7 ]; then
    backup_file="$backup_dir/backup_$(date +%Y%m%d).tar.gz"
    tar -czf "$backup_file" databases/ *.py 2>/dev/null
    
    if [ $? -eq 0 ]; then
        check_success "تم إنشاء نسخة احتياطية أسبوعية"
        print_colored "📁 الملف: $backup_file" $BLUE
    else
        print_colored "❌ فشل في إنشاء النسخة الاحتياطية" $RED
    fi
else
    print_colored "ℹ️ النسخ الاحتياطي يتم أسبوعياً (الأحد)" $BLUE
fi

# 8. تنظيف الملفات المؤقتة
print_header "تنظيف الملفات المؤقتة"

# حذف ملفات Python المؤقتة
find . -name "*.pyc" -delete 2>/dev/null
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null

# حذف السجلات القديمة (أكثر من 30 يوم)
if [ -d "logs" ]; then
    find logs/ -name "*.log" -mtime +30 -delete 2>/dev/null
fi

check_success "تم تنظيف الملفات المؤقتة"

# 9. التقرير النهائي
print_header "التقرير النهائي"

end_time=$(date '+%Y-%m-%d %H:%M:%S')
print_colored "⏰ وقت الانتهاء: $end_time" $BLUE

# فحص حالة النظام العامة
python3 -c "
from revolutionary_knowledge_system import RevolutionaryKnowledgeSystem
try:
    system = RevolutionaryKnowledgeSystem()
    print('✅ النظام يعمل بشكل صحيح')
    print(f'📚 عدد العناصر المعرفية: {system.internal_knowledge_count}')
except Exception as e:
    print(f'❌ مشكلة في النظام: {str(e)[:100]}')
" 2>/dev/null

print_colored "🎉 انتهت الصيانة اليومية بنجاح!" $GREEN
print_colored "💡 نصيحة: شغل هذا السكريپت يومياً للحفاظ على صحة النظام" $YELLOW

echo
print_colored "📋 الخطوات التالية المقترحة:" $CYAN
echo "  1. راجع تقرير النمو للتحقق من التقدم"
echo "  2. أضف مواضيع إضافية حسب اهتماماتك"
echo "  3. اختبر البحث في المعرفة الجديدة"
echo "  4. راقب أداء النظام وجودة المعرفة"

# إلغاء تفعيل البيئة الافتراضية
deactivate 2>/dev/null

exit 0
