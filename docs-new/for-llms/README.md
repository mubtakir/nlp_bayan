# 🤖 For LLMs

Documentation specifically designed for Large Language Models.

**Last Updated**: 2025-12-05 | **Version**: 0.4.0

---

## 📋 Contents

- [System Prompt](system-prompt.txt) - System prompt for LLMs
- [Quick Reference](quick-reference.md) - Fast lookup reference
- [Reference Guide](reference-guide.md) - Complete language reference
- [Model Links](model-links.md) - Links to documentation
- [Test Prompts](test-prompts.md) - Testing prompts
- **[Advanced Features 2025](../../docs/ADVANCED_FEATURES_2025.md)** - New features reference
- **[Extensions Layer](../../دليل_الطبقة_الوسيطة.md)** - 🆕 New middleware layer (v0.4.0)

---

## 🆕 Extensions Layer (v0.4.0)

New middleware features without modifying core files:

| Module | Description | Example |
|--------|-------------|---------|
| `DialectAdapter` | Arabic dialect → MSA | `adapter.convert_to_standard("عايز أكل")` |
| `EquationVisualizer` | SVG equation visualization | `viz.visualize_equation("أحمد", "أكل", "تفاحة")` |
| `BayanTutor` | Interactive learning | `tutor.start_lesson("intro")` |
| `IntelligentDialogueSystem` | Smart chat with memory | `system.chat("مرحباً")` |
| `ExtendedIstinbatEngine` | Dialect-aware inference | `engine.process("عايز أفهم")` |

```python
from extensions import DialectAdapter, IntelligentDialogueSystem

# Convert Egyptian dialect
adapter = DialectAdapter()
result = adapter.convert_to_standard("أحمد عايز ياكل")
# → "أحمد يريد ياكل"

# Smart dialogue
system = IntelligentDialogueSystem()
response = system.chat("مرحباً أنا محمد")
# → "مرحباً! سعيد بالتحدث معك."
```

---

## 🎯 How to Use

When working with Bayan code:

1. Read [Quick Reference](quick-reference.md) for syntax overview
2. Consult [Reference Guide](reference-guide.md) for details
3. Check [Advanced Features 2025](../../docs/ADVANCED_FEATURES_2025.md) for new features
4. Check [Model Links](model-links.md) for external docs

---

## 📝 Key Syntax (Quick)

### Basic Syntax
```bayan
if (condition) { body }
for var in (iterable) { body }
while (condition) { body }
else { body }
```

### Paradigms
```bayan
# Traditional
def func(x) { return x * 2 }

# Logic
logic {
    fact(data).
    rule(?x) :- condition(?x).
}

# Hybrid
hybrid {
    fact data(value).
    def process() { ... }
}
```

---

## 🚀 New Features (2025)

### Pattern Matching
```bayan
match x: {
    case 1: { print("one") }
    case 2: { print("two") }
    case _: { print("other") }
}
```

### Enums
```bayan
enum Color: { RED = 1; GREEN = 2; BLUE = 3 }
```

### Ternary
```bayan
result = "big" if x > 5 else "small"
```

### Spread Operators
```bayan
merged = [*list1, *list2]
merged_dict = {**dict1, **dict2}
```

### Tuple Unpacking
```bayan
a, b, c = 1, 2, 3
a, b = b, a  # Swap
```

### F-Strings
```bayan
print(f"Name: {name}, Age: {age}")
```

### Nullish Coalescing
```bayan
value = x ?? default_value
```

### Enhanced Exceptions
```bayan
try: {
    raise ValueError("message")
} except ValueError as e: {
    print(str(e))
}
```

---

## 📚 Full Documentation

For complete documentation of all features:
- [ADVANCED_FEATURES_2025.md](../../docs/ADVANCED_FEATURES_2025.md) - All new features
- [LLM_REFERENCE_GUIDE.md](../../docs/LLM_REFERENCE_GUIDE.md) - Complete LLM guide

---

[← Back to Index](../README.md)

**Last Updated**: 2025-12-05 | **Version**: 0.4.0
