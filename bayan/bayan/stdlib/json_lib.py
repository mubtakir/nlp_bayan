"""
Bayan JSON Library - مكتبة JSON للبيان
json / جيسون

Provides JSON operations with bilingual (Arabic/English) names.
"""

import json as _json

# ============ JSON Parsing - تحليل JSON ============

def parse_json(text):
    """Parse JSON string to object - تحليل نص JSON إلى كائن"""
    return _json.loads(text)
حلل_جيسون = تحليل_جيسون = parse_json

def to_json(obj, indent=None, ensure_ascii=False):
    """Convert object to JSON string - تحويل كائن إلى نص JSON"""
    return _json.dumps(obj, indent=indent, ensure_ascii=ensure_ascii)
إلى_جيسون = الى_جيسون = to_json

def pretty_json(obj, indent=2):
    """Convert to pretty-printed JSON - تحويل إلى JSON منسق"""
    return _json.dumps(obj, indent=indent, ensure_ascii=False)
جيسون_منسق = تنسيق_جيسون = pretty_json

# ============ File Operations - عمليات الملفات ============

def read_json(path, encoding='utf-8'):
    """Read JSON from file - قراءة JSON من ملف"""
    with open(path, 'r', encoding=encoding) as f:
        return _json.load(f)
اقرأ_جيسون = قراءة_جيسون = read_json

def write_json(path, obj, indent=2, encoding='utf-8'):
    """Write JSON to file - كتابة JSON إلى ملف"""
    with open(path, 'w', encoding=encoding) as f:
        _json.dump(obj, f, indent=indent, ensure_ascii=False)
    return True
اكتب_جيسون = كتابة_جيسون = write_json

# ============ Validation - التحقق ============

def is_valid_json(text):
    """Check if string is valid JSON - هل النص JSON صالح"""
    try:
        _json.loads(text)
        return True
    except (ValueError, TypeError):
        return False
هل_جيسون_صالح = جيسون_صالح = is_valid_json

# ============ Utility Functions - دوال مساعدة ============

def get_value(obj, path, default=None):
    """Get nested value using dot notation - الحصول على قيمة متداخلة"""
    keys = path.split('.')
    current = obj
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list):
            try:
                current = current[int(key)]
            except (ValueError, IndexError):
                return default
        else:
            return default
    return current
احصل_على_قيمة = قيمة = get_value

def set_value(obj, path, value):
    """Set nested value using dot notation - تعيين قيمة متداخلة"""
    keys = path.split('.')
    current = obj
    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]
    current[keys[-1]] = value
    return obj
عين_قيمة = تعيين_قيمة = set_value

def merge_json(obj1, obj2):
    """Merge two JSON objects - دمج كائنين JSON"""
    result = dict(obj1)
    for key, value in obj2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_json(result[key], value)
        else:
            result[key] = value
    return result
ادمج_جيسون = دمج_جيسون = merge_json

def flatten_json(obj, separator='.', prefix=''):
    """Flatten nested JSON to single level - تسطيح JSON متداخل"""
    result = {}
    for key, value in obj.items():
        new_key = f"{prefix}{separator}{key}" if prefix else key
        if isinstance(value, dict):
            result.update(flatten_json(value, separator, new_key))
        else:
            result[new_key] = value
    return result
سطح_جيسون = تسطيح_جيسون = flatten_json

def unflatten_json(obj, separator='.'):
    """Unflatten single-level JSON to nested - إلغاء تسطيح JSON"""
    result = {}
    for key, value in obj.items():
        keys = key.split(separator)
        current = result
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        current[keys[-1]] = value
    return result
ألغ_تسطيح = إلغاء_تسطيح = unflatten_json

