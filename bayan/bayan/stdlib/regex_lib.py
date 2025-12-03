"""
Bayan Regex Library - مكتبة التعبيرات النمطية للبيان
regex / تعبيرات_نمطية

Provides regular expression operations with bilingual (Arabic/English) names.
"""

import re as _re

# ============ Basic Matching - المطابقة الأساسية ============

def match(pattern, text, flags=0):
    """Match pattern at start of text - مطابقة النمط في بداية النص"""
    result = _re.match(pattern, text, flags)
    return result.group() if result else None
طابق = مطابقة = match

def search(pattern, text, flags=0):
    """Search for pattern in text - البحث عن نمط في النص"""
    result = _re.search(pattern, text, flags)
    return result.group() if result else None
ابحث = بحث = search

def find_all(pattern, text, flags=0):
    """Find all matches - إيجاد جميع المطابقات"""
    return _re.findall(pattern, text, flags)
جد_الكل = إيجاد_الكل = find_all

def find_iter(pattern, text, flags=0):
    """Find all matches as iterator - إيجاد المطابقات كمكرر"""
    return [m.group() for m in _re.finditer(pattern, text, flags)]
جد_تكراري = إيجاد_تكراري = find_iter

# ============ Replacement - الاستبدال ============

def replace(pattern, replacement, text, count=0, flags=0):
    """Replace pattern with replacement - استبدال النمط"""
    return _re.sub(pattern, replacement, text, count, flags)
استبدل = استبدال = replace

def replace_all(pattern, replacement, text, flags=0):
    """Replace all occurrences - استبدال جميع التكرارات"""
    return _re.sub(pattern, replacement, text, 0, flags)
استبدل_الكل = استبدال_الكل = replace_all

def replace_first(pattern, replacement, text, flags=0):
    """Replace first occurrence - استبدال أول تكرار"""
    return _re.sub(pattern, replacement, text, 1, flags)
استبدل_الأول = استبدال_الأول = replace_first

# ============ Splitting - التقسيم ============

def split(pattern, text, maxsplit=0, flags=0):
    """Split text by pattern - تقسيم النص بالنمط"""
    return _re.split(pattern, text, maxsplit, flags)
قسم = تقسيم = split

# ============ Validation - التحقق ============

def is_match(pattern, text, flags=0):
    """Check if pattern matches entire text - هل النمط يطابق النص بالكامل"""
    return bool(_re.fullmatch(pattern, text, flags))
هل_يطابق = يطابق = is_match

def contains(pattern, text, flags=0):
    """Check if text contains pattern - هل النص يحتوي على النمط"""
    return bool(_re.search(pattern, text, flags))
يحتوي = هل_يحتوي = contains

# ============ Groups - المجموعات ============

def groups(pattern, text, flags=0):
    """Get all groups from match - الحصول على جميع المجموعات"""
    result = _re.search(pattern, text, flags)
    return result.groups() if result else ()
مجموعات = المجموعات = groups

def named_groups(pattern, text, flags=0):
    """Get named groups as dict - الحصول على المجموعات المسماة"""
    result = _re.search(pattern, text, flags)
    return result.groupdict() if result else {}
مجموعات_مسماة = المجموعات_المسماة = named_groups

# ============ Utility - أدوات مساعدة ============

def escape(text):
    """Escape special regex characters - تهريب الأحرف الخاصة"""
    return _re.escape(text)
هرب = تهريب = escape

def compile_pattern(pattern, flags=0):
    """Compile pattern for reuse - تجميع النمط لإعادة الاستخدام"""
    return _re.compile(pattern, flags)
جمع_نمط = تجميع_نمط = compile_pattern

# ============ Common Patterns - أنماط شائعة ============

# Email pattern - نمط البريد الإلكتروني
EMAIL_PATTERN = نمط_بريد = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Phone pattern - نمط الهاتف
PHONE_PATTERN = نمط_هاتف = r'[\+]?[(]?[0-9]{1,3}[)]?[-\s\.]?[0-9]{1,4}[-\s\.]?[0-9]{1,4}[-\s\.]?[0-9]{1,9}'

# URL pattern - نمط الرابط
URL_PATTERN = نمط_رابط = r'https?://[^\s<>"{}|\\^`\[\]]+'

# Arabic text pattern - نمط النص العربي
ARABIC_PATTERN = نمط_عربي = r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+'

# Number pattern - نمط الأرقام
NUMBER_PATTERN = نمط_رقم = r'-?\d+\.?\d*'

# Integer pattern - نمط الأعداد الصحيحة
INTEGER_PATTERN = نمط_صحيح = r'-?\d+'

# ============ Validation Functions - دوال التحقق ============

def is_email(text):
    """Check if text is valid email - هل النص بريد إلكتروني صالح"""
    return is_match(EMAIL_PATTERN, text)
هل_بريد = بريد_صالح = is_email

def is_url(text):
    """Check if text is valid URL - هل النص رابط صالح"""
    return is_match(URL_PATTERN, text)
هل_رابط = رابط_صالح = is_url

def is_arabic(text):
    """Check if text contains Arabic - هل النص يحتوي على عربي"""
    return contains(ARABIC_PATTERN, text)
هل_عربي = يحتوي_عربي = is_arabic

def is_number(text):
    """Check if text is a number - هل النص رقم"""
    return is_match(NUMBER_PATTERN, text.strip())
هل_رقم = رقم_صالح = is_number

def extract_emails(text):
    """Extract all emails from text - استخراج جميع البريد الإلكتروني"""
    return find_all(EMAIL_PATTERN, text)
استخرج_بريد = استخراج_بريد = extract_emails

def extract_urls(text):
    """Extract all URLs from text - استخراج جميع الروابط"""
    return find_all(URL_PATTERN, text)
استخرج_روابط = استخراج_روابط = extract_urls

def extract_numbers(text):
    """Extract all numbers from text - استخراج جميع الأرقام"""
    return [float(n) if '.' in n else int(n) for n in find_all(NUMBER_PATTERN, text)]
استخرج_أرقام = استخراج_أرقام = extract_numbers

def extract_arabic(text):
    """Extract Arabic words from text - استخراج الكلمات العربية"""
    return find_all(ARABIC_PATTERN, text)
استخرج_عربي = استخراج_عربي = extract_arabic

