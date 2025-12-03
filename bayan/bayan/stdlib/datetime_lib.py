"""
Bayan DateTime Library - مكتبة التاريخ والوقت للبيان
datetime / تاريخ_وقت

Provides date/time functions with bilingual names.
"""

from datetime import datetime as _datetime
from datetime import date as _date
from datetime import time as _time
from datetime import timedelta as _timedelta
import time as _time_module

# ============ Current Time - الوقت الحالي ============

def now():
    """Get current datetime - الوقت الحالي"""
    return _datetime.now()
الآن = now

def today():
    """Get today's date - تاريخ اليوم"""
    return _date.today()
اليوم = today

def utcnow():
    """Get current UTC datetime"""
    return _datetime.utcnow()
الآن_عالمي = utcnow

def timestamp():
    """Get current Unix timestamp"""
    return _time_module.time()
طابع_زمني = timestamp

# ============ Date Creation - إنشاء التاريخ ============

def date(year, month, day):
    """Create a date - إنشاء تاريخ"""
    return _date(year, month, day)
تاريخ = date

def time(hour=0, minute=0, second=0, microsecond=0):
    """Create a time - إنشاء وقت"""
    return _time(hour, minute, second, microsecond)
وقت = time

def datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0):
    """Create a datetime - إنشاء تاريخ ووقت"""
    return _datetime(year, month, day, hour, minute, second, microsecond)
تاريخ_وقت = datetime

# ============ Duration - المدة الزمنية ============

def days(n):
    """Create timedelta of n days - أيام"""
    return _timedelta(days=n)
أيام = days

def hours(n):
    """Create timedelta of n hours - ساعات"""
    return _timedelta(hours=n)
ساعات = hours

def minutes(n):
    """Create timedelta of n minutes - دقائق"""
    return _timedelta(minutes=n)
دقائق = minutes

def seconds(n):
    """Create timedelta of n seconds - ثواني"""
    return _timedelta(seconds=n)
ثواني = seconds

def weeks(n):
    """Create timedelta of n weeks - أسابيع"""
    return _timedelta(weeks=n)
أسابيع = weeks

def timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, 
              minutes=0, hours=0, weeks=0):
    """Create a timedelta - فترة زمنية"""
    return _timedelta(days=days, seconds=seconds, microseconds=microseconds,
                     milliseconds=milliseconds, minutes=minutes, 
                     hours=hours, weeks=weeks)
فترة = مدة = timedelta

# ============ Formatting - التنسيق ============

def format_date(dt, fmt="%Y-%m-%d"):
    """Format date/datetime - تنسيق التاريخ"""
    return dt.strftime(fmt)
تنسيق_تاريخ = format_date

def format_time(t, fmt="%H:%M:%S"):
    """Format time - تنسيق الوقت"""
    return t.strftime(fmt)
تنسيق_وقت = format_time

def format_datetime(dt, fmt="%Y-%m-%d %H:%M:%S"):
    """Format datetime - تنسيق التاريخ والوقت"""
    return dt.strftime(fmt)
تنسيق_تاريخ_وقت = format_datetime

# ============ Parsing - التحليل ============

def parse_date(s, fmt="%Y-%m-%d"):
    """Parse date string - تحليل نص التاريخ"""
    return _datetime.strptime(s, fmt).date()
تحليل_تاريخ = parse_date

def parse_time(s, fmt="%H:%M:%S"):
    """Parse time string - تحليل نص الوقت"""
    return _datetime.strptime(s, fmt).time()
تحليل_وقت = parse_time

def parse_datetime(s, fmt="%Y-%m-%d %H:%M:%S"):
    """Parse datetime string - تحليل نص التاريخ والوقت"""
    return _datetime.strptime(s, fmt)
تحليل_تاريخ_وقت = parse_datetime

# ============ Components - المكونات ============

def year(dt):
    """Get year - السنة"""
    return dt.year
سنة = year

def month(dt):
    """Get month - الشهر"""
    return dt.month
شهر = month

def day(dt):
    """Get day - اليوم"""
    return dt.day
يوم = day

def hour(dt):
    """Get hour - الساعة"""
    return dt.hour
ساعة = hour

def minute(dt):
    """Get minute - الدقيقة"""
    return dt.minute
دقيقة = minute

def second(dt):
    """Get second - الثانية"""
    return dt.second
ثانية = second

def weekday(dt):
    """Get weekday (0=Monday) - يوم الأسبوع"""
    return dt.weekday()
يوم_أسبوع = weekday

# ============ Arabic Day Names - أسماء الأيام بالعربية ============

WEEKDAYS_AR = أيام_الأسبوع = [
    "الاثنين", "الثلاثاء", "الأربعاء", "الخميس",
    "الجمعة", "السبت", "الأحد"
]

MONTHS_AR = أشهر_السنة = [
    "يناير", "فبراير", "مارس", "أبريل",
    "مايو", "يونيو", "يوليو", "أغسطس",
    "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"
]

def weekday_name_ar(dt):
    """Get Arabic weekday name - اسم يوم الأسبوع بالعربية"""
    return WEEKDAYS_AR[dt.weekday()]
اسم_يوم = weekday_name_ar

def month_name_ar(dt):
    """Get Arabic month name - اسم الشهر بالعربية"""
    return MONTHS_AR[dt.month - 1]
اسم_شهر = month_name_ar

# ============ Calculations - الحسابات ============

def add_days(dt, n):
    """Add days to date/datetime - إضافة أيام"""
    return dt + _timedelta(days=n)
أضف_أيام = add_days

def subtract_days(dt, n):
    """Subtract days - طرح أيام"""
    return dt - _timedelta(days=n)
اطرح_أيام = subtract_days

def diff_days(dt1, dt2):
    """Difference in days - الفرق بالأيام"""
    return (dt1 - dt2).days
فرق_أيام = diff_days

def is_leap_year(year):
    """Check if leap year - سنة كبيسة"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
سنة_كبيسة = is_leap_year

