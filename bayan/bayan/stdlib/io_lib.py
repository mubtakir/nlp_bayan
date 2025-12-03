"""
Bayan IO Library - مكتبة الإدخال والإخراج للبيان
io / إدخال_إخراج

Provides file and I/O operations with bilingual (Arabic/English) names.
"""

import os as _os
import sys as _sys

# ============ File Operations - عمليات الملفات ============

def read_file(path, encoding='utf-8'):
    """Read entire file content - قراءة محتوى الملف"""
    with open(path, 'r', encoding=encoding) as f:
        return f.read()
اقرأ_ملف = قراءة_ملف = read_file

def write_file(path, content, encoding='utf-8'):
    """Write content to file - كتابة محتوى إلى ملف"""
    with open(path, 'w', encoding=encoding) as f:
        f.write(str(content))
    return True
اكتب_ملف = كتابة_ملف = write_file

def append_file(path, content, encoding='utf-8'):
    """Append content to file - إلحاق محتوى بملف"""
    with open(path, 'a', encoding=encoding) as f:
        f.write(str(content))
    return True
ألحق_بملف = إلحاق_ملف = append_file

def read_lines(path, encoding='utf-8'):
    """Read file as list of lines - قراءة الملف كقائمة أسطر"""
    with open(path, 'r', encoding=encoding) as f:
        return f.readlines()
اقرأ_أسطر = قراءة_أسطر = read_lines

def write_lines(path, lines, encoding='utf-8'):
    """Write list of lines to file - كتابة قائمة أسطر إلى ملف"""
    with open(path, 'w', encoding=encoding) as f:
        for line in lines:
            f.write(str(line) + '\n')
    return True
اكتب_أسطر = كتابة_أسطر = write_lines

# ============ File Checks - فحص الملفات ============

def file_exists(path):
    """Check if file exists - هل الملف موجود"""
    return _os.path.isfile(path)
ملف_موجود = هل_ملف_موجود = file_exists

def dir_exists(path):
    """Check if directory exists - هل المجلد موجود"""
    return _os.path.isdir(path)
مجلد_موجود = هل_مجلد_موجود = dir_exists

def path_exists(path):
    """Check if path exists - هل المسار موجود"""
    return _os.path.exists(path)
مسار_موجود = هل_مسار_موجود = path_exists

def file_size(path):
    """Get file size in bytes - حجم الملف بالبايت"""
    return _os.path.getsize(path)
حجم_ملف = file_size

# ============ Directory Operations - عمليات المجلدات ============

def list_dir(path='.'):
    """List directory contents - قائمة محتويات المجلد"""
    return _os.listdir(path)
قائمة_مجلد = محتويات_مجلد = list_dir

def make_dir(path):
    """Create directory - إنشاء مجلد"""
    _os.makedirs(path, exist_ok=True)
    return True
أنشئ_مجلد = إنشاء_مجلد = make_dir

def remove_file(path):
    """Remove file - حذف ملف"""
    _os.remove(path)
    return True
احذف_ملف = حذف_ملف = remove_file

def remove_dir(path):
    """Remove empty directory - حذف مجلد فارغ"""
    _os.rmdir(path)
    return True
احذف_مجلد = حذف_مجلد = remove_dir

def rename(old_path, new_path):
    """Rename file or directory - إعادة تسمية"""
    _os.rename(old_path, new_path)
    return True
أعد_تسمية = إعادة_تسمية = rename

def current_dir():
    """Get current working directory - المجلد الحالي"""
    return _os.getcwd()
المجلد_الحالي = مجلد_العمل = current_dir

def change_dir(path):
    """Change current directory - تغيير المجلد الحالي"""
    _os.chdir(path)
    return True
غير_المجلد = تغيير_مجلد = change_dir

# ============ Path Operations - عمليات المسارات ============

def join_path(*parts):
    """Join path components - دمج أجزاء المسار"""
    return _os.path.join(*parts)
ادمج_مسار = دمج_مسار = join_path

def split_path(path):
    """Split path into directory and filename - تقسيم المسار"""
    return _os.path.split(path)
قسم_مسار = تقسيم_مسار = split_path

def get_extension(path):
    """Get file extension - امتداد الملف"""
    return _os.path.splitext(path)[1]
امتداد_ملف = الامتداد = get_extension

def get_filename(path):
    """Get filename from path - اسم الملف من المسار"""
    return _os.path.basename(path)
اسم_ملف = الاسم = get_filename

def get_dirname(path):
    """Get directory name from path - اسم المجلد من المسار"""
    return _os.path.dirname(path)
اسم_مجلد = المجلد = get_dirname

def absolute_path(path):
    """Get absolute path - المسار المطلق"""
    return _os.path.abspath(path)
مسار_مطلق = المسار_المطلق = absolute_path

# ============ Console I/O - إدخال/إخراج الطرفية ============

def input_text(prompt=''):
    """Read input from user - قراءة إدخال من المستخدم"""
    return input(prompt)
أدخل = إدخال = ادخال = input_text

def print_text(*args, sep=' ', end='\n'):
    """Print to console - طباعة على الطرفية"""
    print(*args, sep=sep, end=end)
اطبع = طباعة = print_text

def print_error(*args):
    """Print to stderr - طباعة خطأ"""
    print(*args, file=_sys.stderr)
اطبع_خطأ = طباعة_خطأ = print_error

