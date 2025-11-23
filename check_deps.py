try:
    import transformers
    print("transformers: installed")
except ImportError:
    print("transformers: missing")

try:
    import numpy
    print("numpy: installed")
except ImportError:
    print("numpy: missing")
