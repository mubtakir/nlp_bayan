"""
Bayan CSV Library - مكتبة ملفات CSV للبيان
csv / ملفات_csv

Provides simplified CSV reading and writing with bilingual names.
"""

import csv as _csv

def read_csv(path, encoding='utf-8', delimiter=','):
    """
    Read CSV file into a list of dictionaries.
    اقرأ ملف CSV كقائمة من القواميس
    """
    results = []
    try:
        with open(path, 'r', encoding=encoding, newline='') as f:
            reader = _csv.DictReader(f, delimiter=delimiter)
            for row in reader:
                results.append(dict(row))
        return results
    except Exception as e:
        return {'error': str(e)}
اقرأ_csv = قراءة_csv = read_csv

def write_csv(path, data, fieldnames=None, encoding='utf-8', delimiter=','):
    """
    Write a list of dictionaries to a CSV file.
    اكتب قائمة من القواميس إلى ملف CSV
    """
    if not data:
        return False
        
    try:
        if fieldnames is None:
            # Infer fieldnames from the first item keys
            fieldnames = list(data[0].keys())
            
        with open(path, 'w', encoding=encoding, newline='') as f:
            writer = _csv.DictWriter(f, fieldnames=fieldnames, delimiter=delimiter)
            writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as e:
        return {'error': str(e)}
اكتب_csv = كتابة_csv = write_csv

def read_csv_list(path, encoding='utf-8', delimiter=','):
    """
    Read CSV file into a list of lists (no headers assumption).
    اقرأ ملف CSV كقائمة من القوائم
    """
    results = []
    try:
        with open(path, 'r', encoding=encoding, newline='') as f:
            reader = _csv.reader(f, delimiter=delimiter)
            for row in reader:
                results.append(row)
        return results
    except Exception as e:
        return {'error': str(e)}
اقرأ_csv_قائمة = read_csv_list
