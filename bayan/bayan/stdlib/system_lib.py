"""
Bayan System Library - مكتبة النظام للبيان
system / نظام

Provides interaction with the operating system and environment.
Wraps sys and subprocess modules.
"""

import sys as _sys
import os as _os
import subprocess as _subprocess
import platform as _platform

# ============ Process Management - إدارة العمليات ============

def exit(code=0):
    """Exit the program - الخروج من البرنامج"""
    _sys.exit(code)
خروج = انهاء = exit

def execute(command, capture_output=True):
    """
    Execute a shell command - تنفيذ أمر
    Returns a dict with 'stdout', 'stderr', and 'returncode'.
    """
    try:
        result = _subprocess.run(
            command, 
            shell=True, 
            text=True, 
            capture_output=capture_output
        )
        return {
            'stdout': result.stdout,
            'stderr': result.stderr,
            'code': result.returncode,
            'success': result.returncode == 0
        }
    except Exception as e:
        return {
            'stdout': '',
            'stderr': str(e),
            'code': -1,
            'success': False
        }
نفذ = تنفيذ = execute

# ============ Environment - البيئة ============

def get_env(key, default=None):
    """Get environment variable - الحصول على متغير بيئة"""
    return _os.environ.get(key, default)
متغير_بيئة = get_env

def set_env(key, value):
    """Set environment variable - تعيين متغير بيئة"""
    _os.environ[key] = str(value)
    return True
عين_بيئة = set_env

def get_args():
    """Get command line arguments - معاملات سطر الأوامر"""
    return _sys.argv
معاملات = وسائط = get_args

def get_platform():
    """Get platform name (e.g. Linux, Windows) - اسم النظام"""
    return _platform.system()
نظام_تشغيل = get_platform

def get_python_version():
    """Get Python version - إصدار بايثون"""
    return _platform.python_version()
إصدار_بايثون = get_python_version

# ============ Standard Streams - المجاري القياسية ============

def stdin_read():
    """Read from stdin - قراءة من المدخل القياسي"""
    return _sys.stdin.read()
اقرأ_مدخل = stdin_read

def stdout_write(text):
    """Write to stdout - كتابة للمخرج القياسي"""
    _sys.stdout.write(str(text))
    return True
اكتب_مخرج = stdout_write

def stderr_write(text):
    """Write to stderr - كتابة لمخرج الأخطاء"""
    _sys.stderr.write(str(text))
    return True
اكتب_خطأ = stderr_write

# ============ System Info - معلومات النظام ============

def cpu_count():
    """Get number of CPUs - عدد المعالجات"""
    return _os.cpu_count()
عدد_المعالجات = cpu_count

def get_login():
    """Get current user login name - اسم المستخدم"""
    try:
        return _os.getlogin()
    except:
        return _os.environ.get('USER', 'unknown')
مستخدم = get_login
