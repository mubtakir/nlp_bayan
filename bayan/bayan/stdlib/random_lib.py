"""
Bayan Random Library - مكتبة العشوائية للبيان
random / عشوائي

Provides random number generation and selection utilities with bilingual names.
Wraps Python's random module.
"""

import random as _random

# ============ Random Number Generation - توليد الأرقام ============

def random_float():
    """Return a random float between 0.0 and 1.0 - رقم عشري عشوائي"""
    return _random.random()
عشوائي = رقم_عشوائي = random_float

def randint(a, b):
    """Return a random integer N such that a <= N <= b - رقم صحيح عشوائي"""
    return _random.randint(a, b)
رقم_صحيح = عدد_صحيح = randint

def uniform(a, b):
    """Return a random floating point number N such that a <= N <= b"""
    return _random.uniform(a, b)
عشوائي_متجانس = uniform

def randrange(start, stop=None, step=1):
    """Choose a random item from range(start, stop[, step])"""
    return _random.randrange(start, stop, step)
رقم_نطاق = randrange

# ============ Selection - الاختيار ============

def choice(seq):
    """Choose a random element from a non-empty sequence - اختر عنصر"""
    return _random.choice(seq)
اختر = اختيار = choice

def choices(population, weights=None, k=1):
    """Return a k sized list of elements chosen from the population with replacement"""
    return _random.choices(population, weights=weights, k=k)
اختر_مجموعة = choices

def sample(population, k):
    """Return a k length list of unique elements chosen from the population sequence"""
    return _random.sample(population, k)
عينة = sample

# ============ Shuffling - الخلط ============

def shuffle(x):
    """Shuffle list x in place, and return None - خلط القائمة"""
    _random.shuffle(x)
    return x # Return x for convenience in Bayan, though Python returns None
اخلط = خلط = shuffle

# ============ Seeding - التأسيس ============

def seed(a=None):
    """Initialize internal state of the random number generator - بذرة العشوائية"""
    _random.seed(a)
    return True
بذرة = تأسيس = seed
