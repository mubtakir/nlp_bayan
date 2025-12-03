"""
Bayan Math Library - مكتبة الرياضيات للبيان
math / رياضيات

Provides mathematical functions with bilingual (Arabic/English) names.
"""

import math as _math

# ============ Constants - الثوابت ============
PI = باي = _math.pi
E = هـ = _math.e
TAU = تاو = _math.tau
INF = لانهاية = _math.inf
NAN = غير_رقم = _math.nan

# ============ Basic Functions - الدوال الأساسية ============

def sqrt(x):
    """Square root - الجذر التربيعي"""
    return _math.sqrt(x)
جذر = جذر_تربيعي = sqrt

def cbrt(x):
    """Cube root - الجذر التكعيبي"""
    return x ** (1/3) if x >= 0 else -(-x) ** (1/3)
جذر_تكعيبي = cbrt

def pow(x, y):
    """Power - الأس"""
    return _math.pow(x, y)
أس = قوة = pow

def abs(x):
    """Absolute value - القيمة المطلقة"""
    return _math.fabs(x)
مطلق = قيمة_مطلقة = abs

def ceil(x):
    """Ceiling - السقف"""
    return _math.ceil(x)
سقف = ceil

def floor(x):
    """Floor - الأرضية"""
    return _math.floor(x)
أرضية = floor

def round(x, digits=0):
    """Round - التقريب"""
    if digits == 0:
        return _math.floor(x + 0.5)
    factor = 10 ** digits
    return _math.floor(x * factor + 0.5) / factor
تقريب = round

def trunc(x):
    """Truncate - القطع"""
    return _math.trunc(x)
قطع = trunc

# ============ Trigonometric Functions - الدوال المثلثية ============

def sin(x):
    """Sine - الجيب"""
    return _math.sin(x)
جيب = جا = sin

def cos(x):
    """Cosine - جيب التمام"""
    return _math.cos(x)
جيب_تمام = جتا = cos

def tan(x):
    """Tangent - الظل"""
    return _math.tan(x)
ظل = ظا = tan

def asin(x):
    """Arc sine - معكوس الجيب"""
    return _math.asin(x)
معكوس_جيب = asin

def acos(x):
    """Arc cosine - معكوس جيب التمام"""
    return _math.acos(x)
معكوس_جيب_تمام = acos

def atan(x):
    """Arc tangent - معكوس الظل"""
    return _math.atan(x)
معكوس_ظل = atan

def atan2(y, x):
    """Arc tangent of y/x"""
    return _math.atan2(y, x)

def degrees(x):
    """Radians to degrees - تحويل إلى درجات"""
    return _math.degrees(x)
درجات = degrees

def radians(x):
    """Degrees to radians - تحويل إلى راديان"""
    return _math.radians(x)
راديان = radians

# ============ Logarithmic Functions - الدوال اللوغاريتمية ============

def log(x, base=None):
    """Logarithm - اللوغاريتم"""
    if base is None:
        return _math.log(x)
    return _math.log(x, base)
لوغاريتم = log

def log10(x):
    """Base-10 logarithm"""
    return _math.log10(x)
لوغاريتم10 = log10

def log2(x):
    """Base-2 logarithm"""
    return _math.log2(x)
لوغاريتم2 = log2

def exp(x):
    """e raised to power x"""
    return _math.exp(x)
أسي = exp

# ============ Hyperbolic Functions - الدوال الزائدية ============

def sinh(x):
    """Hyperbolic sine"""
    return _math.sinh(x)
جيب_زائدي = sinh

def cosh(x):
    """Hyperbolic cosine"""
    return _math.cosh(x)
جيب_تمام_زائدي = cosh

def tanh(x):
    """Hyperbolic tangent"""
    return _math.tanh(x)
ظل_زائدي = tanh

# ============ Special Functions - دوال خاصة ============

def factorial(n):
    """Factorial - المضروب"""
    return _math.factorial(n)
مضروب = factorial

def gcd(a, b):
    """Greatest common divisor - القاسم المشترك الأكبر"""
    return _math.gcd(a, b)
قاسم_مشترك = gcd

def lcm(a, b):
    """Least common multiple - المضاعف المشترك الأصغر"""
    return (a * b) // _math.gcd(a, b)
مضاعف_مشترك = lcm

def isnan(x):
    """Check if NaN"""
    return _math.isnan(x)
هل_غير_رقم = isnan

def isinf(x):
    """Check if infinite"""
    return _math.isinf(x)
هل_لانهائي = isinf

