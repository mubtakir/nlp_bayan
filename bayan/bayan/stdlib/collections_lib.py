"""
Bayan Collections Library - مكتبة المجموعات للبيان
collections / مجموعات

Provides collection utilities with bilingual names.
"""

from collections import OrderedDict as _OrderedDict
from collections import Counter as _Counter
from collections import defaultdict as _defaultdict
from collections import deque as _deque

# ============ Counter - العداد ============

class Counter(_Counter):
    """Counter class - فئة العداد"""
    pass

عداد = Counter

def count_elements(iterable):
    """Count elements in iterable - عد العناصر"""
    return Counter(iterable)
عد_عناصر = count_elements

def most_common(counter, n=None):
    """Get most common elements - الأكثر شيوعاً"""
    return counter.most_common(n)
الأكثر_شيوعاً = most_common

# ============ OrderedDict - القاموس المرتب ============

class OrderedDict(_OrderedDict):
    """Ordered dictionary - قاموس مرتب"""
    pass

قاموس_مرتب = OrderedDict

# ============ DefaultDict - القاموس الافتراضي ============

def defaultdict(default_factory, *args, **kwargs):
    """Create a defaultdict - قاموس افتراضي"""
    return _defaultdict(default_factory, *args, **kwargs)
قاموس_افتراضي = defaultdict

# ============ Deque - الطابور المزدوج ============

class Deque(_deque):
    """Double-ended queue - طابور مزدوج"""
    pass

طابور = طابور_مزدوج = Deque

# ============ Stack - المكدس ============

class Stack:
    """Stack (LIFO) - مكدس"""
    def __init__(self, items=None):
        self._items = list(items) if items else []
    
    def push(self, item):
        """Push item - إضافة عنصر"""
        self._items.append(item)
    ادفع = push
    
    def pop(self):
        """Pop item - إزالة عنصر"""
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items.pop()
    أخرج = pop
    
    def peek(self):
        """Peek at top - النظر للقمة"""
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items[-1]
    قمة = peek
    
    def is_empty(self):
        """Check if empty - هل فارغ"""
        return len(self._items) == 0
    فارغ = is_empty
    
    def size(self):
        """Get size - الحجم"""
        return len(self._items)
    حجم = size
    
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return f"Stack({self._items})"

مكدس = Stack

# ============ Queue - الطابور ============

class Queue:
    """Queue (FIFO) - طابور"""
    def __init__(self, items=None):
        self._items = _deque(items) if items else _deque()
    
    def enqueue(self, item):
        """Add to queue - إضافة للطابور"""
        self._items.append(item)
    أضف = enqueue
    
    def dequeue(self):
        """Remove from queue - إزالة من الطابور"""
        if not self._items:
            raise IndexError("Queue is empty")
        return self._items.popleft()
    أخرج = dequeue
    
    def peek(self):
        """Peek at front - النظر للمقدمة"""
        if not self._items:
            raise IndexError("Queue is empty")
        return self._items[0]
    مقدمة = peek
    
    def is_empty(self):
        return len(self._items) == 0
    فارغ = is_empty
    
    def size(self):
        return len(self._items)
    حجم = size
    
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return f"Queue({list(self._items)})"

صف = Queue

# ============ Utility Functions - دوال مساعدة ============

def flatten(nested_list):
    """Flatten nested list - تسطيح القائمة"""
    result = []
    for item in nested_list:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
تسطيح = flatten

def unique(iterable):
    """Get unique elements preserving order - العناصر الفريدة"""
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
فريدة = unique

def group_by(iterable, key_func):
    """Group elements by key - تجميع حسب مفتاح"""
    result = {}
    for item in iterable:
        key = key_func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result
تجميع = group_by

def chunk(iterable, size):
    """Split into chunks - تقسيم لأجزاء"""
    lst = list(iterable)
    return [lst[i:i+size] for i in range(0, len(lst), size)]
تقسيم_أجزاء = chunk

