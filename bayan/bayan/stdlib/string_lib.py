"""
Bayan String Library - مكتبة النصوص للبيان
string / نص

Provides string manipulation functions with bilingual names.
"""

# ============ Basic String Operations - العمليات النصية الأساسية ============

def length(s):
    """Get string length - طول النص"""
    return len(s)
طول = length

def upper(s):
    """Convert to uppercase - تحويل للأحرف الكبيرة"""
    return s.upper()
أحرف_كبيرة = upper

def lower(s):
    """Convert to lowercase - تحويل للأحرف الصغيرة"""
    return s.lower()
أحرف_صغيرة = lower

def capitalize(s):
    """Capitalize first letter - تكبير الحرف الأول"""
    return s.capitalize()
تكبير_أول = capitalize

def title(s):
    """Title case - تكبير أوائل الكلمات"""
    return s.title()
عنوان = title

def strip(s, chars=None):
    """Strip whitespace or chars - إزالة المسافات"""
    return s.strip(chars)
تجريد = إزالة_مسافات = strip

def lstrip(s, chars=None):
    """Strip from left"""
    return s.lstrip(chars)
تجريد_يسار = lstrip

def rstrip(s, chars=None):
    """Strip from right"""
    return s.rstrip(chars)
تجريد_يمين = rstrip

# ============ Search and Replace - البحث والاستبدال ============

def find(s, sub, start=0, end=None):
    """Find substring - البحث عن نص فرعي"""
    if end is None:
        return s.find(sub, start)
    return s.find(sub, start, end)
بحث = إيجاد = find

def rfind(s, sub, start=0, end=None):
    """Find from right"""
    if end is None:
        return s.rfind(sub, start)
    return s.rfind(sub, start, end)
بحث_يمين = rfind

def index(s, sub, start=0, end=None):
    """Find substring or raise error"""
    if end is None:
        return s.index(sub, start)
    return s.index(sub, start, end)
فهرس = index

def count(s, sub, start=0, end=None):
    """Count occurrences - عد التكرارات"""
    if end is None:
        return s.count(sub, start)
    return s.count(sub, start, end)
عد = count

def replace(s, old, new, count=-1):
    """Replace substring - استبدال"""
    if count == -1:
        return s.replace(old, new)
    return s.replace(old, new, count)
استبدال = replace

# ============ Testing - الاختبارات ============

def startswith(s, prefix, start=0, end=None):
    """Check if starts with prefix"""
    if end is None:
        return s.startswith(prefix, start)
    return s.startswith(prefix, start, end)
يبدأ_بـ = startswith

def endswith(s, suffix, start=0, end=None):
    """Check if ends with suffix"""
    if end is None:
        return s.endswith(suffix, start)
    return s.endswith(suffix, start, end)
ينتهي_بـ = endswith

def contains(s, sub):
    """Check if contains substring"""
    return sub in s
يحتوي = contains

def isalpha(s):
    """Check if all alphabetic"""
    return s.isalpha()
هل_أحرف = isalpha

def isdigit(s):
    """Check if all digits"""
    return s.isdigit()
هل_أرقام = isdigit

def isalnum(s):
    """Check if alphanumeric"""
    return s.isalnum()
هل_حروف_أرقام = isalnum

def isspace(s):
    """Check if all whitespace"""
    return s.isspace()
هل_مسافات = isspace

def isupper(s):
    """Check if all uppercase"""
    return s.isupper()
هل_كبيرة = isupper

def islower(s):
    """Check if all lowercase"""
    return s.islower()
هل_صغيرة = islower

# ============ Split and Join - التقسيم والربط ============

def split(s, sep=None, maxsplit=-1):
    """Split string - تقسيم النص"""
    return s.split(sep, maxsplit)
تقسيم = split

def rsplit(s, sep=None, maxsplit=-1):
    """Split from right"""
    return s.rsplit(sep, maxsplit)
تقسيم_يمين = rsplit

def splitlines(s, keepends=False):
    """Split by lines"""
    return s.splitlines(keepends)
تقسيم_أسطر = splitlines

def join(sep, iterable):
    """Join strings - ربط النصوص"""
    return sep.join(iterable)
ربط = join

# ============ Formatting - التنسيق ============

def center(s, width, fillchar=' '):
    """Center string"""
    return s.center(width, fillchar)
توسيط = center

def ljust(s, width, fillchar=' '):
    """Left justify"""
    return s.ljust(width, fillchar)
محاذاة_يسار = ljust

def rjust(s, width, fillchar=' '):
    """Right justify"""
    return s.rjust(width, fillchar)
محاذاة_يمين = rjust

def zfill(s, width):
    """Pad with zeros"""
    return s.zfill(width)
ملء_أصفار = zfill

def reverse(s):
    """Reverse string - عكس النص"""
    return s[::-1]
عكس = reverse

def repeat(s, n):
    """Repeat string n times - تكرار النص"""
    return s * n
تكرار = repeat

def slice(s, start=None, end=None, step=None):
    """Slice string - قطع النص"""
    return s[start:end:step]
قطع = slice

