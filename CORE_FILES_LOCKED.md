# 🔒 ملفات نواة لغة البيان المقفلة
# Bayan Language Core Files - Locked (Read-Only)

---

## ⚠️ تحذير مهم | Important Warning

هذه الملفات مقفلة للقراءة فقط (Read-Only) لحماية نواة اللغة من التعديلات العرضية.
These files are locked (read-only) to protect the language core from accidental modifications.

---

## 🔒 الملفات المقفلة | Locked Files (15 ملف - Core Only)

### 📁 النواة الرئيسية | Core (bayan/bayan/)

| الملف | الوصف | Description | الحجم |
|-------|-------|-------------|-------|
| `__init__.py` | تهيئة الوحدة | Module init | 1.4KB |
| `lexer.py` | المحلل المعجمي | Lexical Analyzer | 42KB |
| `parser.py` | المحلل النحوي | Parser | 205KB |
| `ast_nodes.py` | عقد الشجرة التركيبية | AST Nodes | 69KB |
| `traditional_interpreter.py` | المفسر التقليدي | Traditional Interpreter | 267KB |
| `hybrid_interpreter.py` | المفسر الهجين | Hybrid Interpreter | 48KB |
| `logical_engine.py` | المحرك المنطقي | Logic Engine | 46KB |
| `builtins.py` | الدوال المدمجة | Built-in Functions | 34KB |
| `type_checker.py` | مدقق الأنواع | Type Checker | 21KB |
| `object_system.py` | نظام الكائنات | Object System | 14KB |
| `import_system.py` | نظام الاستيراد | Import System | 12KB |
| `metaprogramming.py` | البرمجة الوصفية | Metaprogramming | 12KB |
| `error_messages.py` | رسائل الأخطاء | Error Messages | 16KB |
| `entity_engine.py` | محرك الكيانات | Entity Engine | 35KB |
| `compiler_interface.py` | واجهة المترجم | Compiler Interface | 14KB |

### 📁 الآلة الافتراضية | Bytecode VM (bayan/bayan/bytecode/)

| الملف | الوصف | Description |
|-------|-------|-------------|
| `__init__.py` | تهيئة الوحدة | Module init |
| `opcodes.py` | تعريفات العمليات | Opcode Definitions |
| `instruction.py` | التعليمات | Instructions |
| `codegen.py` | مولد الكود | Code Generator |
| `optimizer.py` | محسن الكود | Optimizer |
| `vm.py` | الآلة الافتراضية | Virtual Machine |

---

## 📂 الملفات المنقولة للطبقات الوسيطة | Migrated to Extensions

### ✅ تم النقل في 2025-12-07

| المجموعة | الملفات | الموقع الجديد |
|----------|---------|---------------|
| **Dual Brain** | `dual_brain.py`, `left_brain.py`, `right_brain.py`, `integration_layer.py` | `extensions/dual_brain/` |
| **GLM** | `generative_model.py`, `word_energy_matrix.py`, `reverse_glm.py`, `letter_semiotics/` | `extensions/glm/` |
| **Equations** | `linguistic_equation.py`, `mother_equation.py`, `gse.py`, `gse_fitting.py`, `gse_visualization.py` | `extensions/equations/` |
| **Arabic NLP** | `arabic_adapter.py`, `arramooz_adapter.py`, `advanced_arabic_parser.py` | `extensions/arabic_nlp/` |
| **Vocabulary** | `foundation_vocabulary*.py`, `vocabulary_extension.py`, `complete_vocabulary.py` | `extensions/vocabulary/` |
| **Networks** | `causal_semantic_network.py` | `extensions/networks/` |
| **Knowledge** | `smart_knowledge_base.py`, `smart_lexicon.py`, `unified_lexicon_system.py` | `extensions/knowledge/` |
| **Visualization** | `visualization.py` | `extensions/visualization/` |
| **Baserah** | `baserah_ai/`, `baserah_extension.py` | `extensions/baserah/` |
| **Other** | `expert_explorer.py`, `istinbat_engine.py`, `dynamic_builder.py`, `brain_extension.py` | `extensions/` |

---

## 📝 الملفات غير المقفلة في النواة | Unlocked Core Files

> ⚠️ هذه الملفات لا تزال في النواة لأسباب التوافق العكسي، لكن النسخ الرسمية في extensions/

| الملف | السبب |
|-------|-------|
| `dual_brain.py` | تبعيات داخلية |
| `left_brain.py` | تبعيات داخلية |
| `right_brain.py` | تبعيات داخلية |
| `gse.py` | مستخدم في builtins.py |
| `mother_equation.py` | مستخدم في builtins.py |
| وغيرها... | توافق عكسي |

---

## 🔓 لفك القفل | To Unlock

إذا كنت بحاجة لتعديل ملفات النواة:
If you need to modify core files:

```bash
# فك قفل ملف واحد
chmod 644 bayan/bayan/lexer.py

# فك قفل كل ملفات النواة
chmod 644 bayan/bayan/lexer.py bayan/bayan/parser.py bayan/bayan/ast_nodes.py \
    bayan/bayan/traditional_interpreter.py bayan/bayan/hybrid_interpreter.py \
    bayan/bayan/logical_engine.py bayan/bayan/builtins.py bayan/bayan/type_checker.py \
    bayan/bayan/object_system.py bayan/bayan/import_system.py \
    bayan/bayan/metaprogramming.py bayan/bayan/error_messages.py \
    bayan/bayan/entity_engine.py bayan/bayan/compiler_interface.py \
    bayan/bayan/__init__.py bayan/bayan/bytecode/*.py

# إعادة القفل
chmod 444 bayan/bayan/lexer.py bayan/bayan/parser.py bayan/bayan/ast_nodes.py \
    bayan/bayan/traditional_interpreter.py bayan/bayan/hybrid_interpreter.py \
    bayan/bayan/logical_engine.py bayan/bayan/builtins.py bayan/bayan/type_checker.py \
    bayan/bayan/object_system.py bayan/bayan/import_system.py \
    bayan/bayan/metaprogramming.py bayan/bayan/error_messages.py \
    bayan/bayan/entity_engine.py bayan/bayan/compiler_interface.py \
    bayan/bayan/__init__.py bayan/bayan/bytecode/*.py
```

---

## 📅 تاريخ التحديثات | Update History

| التاريخ | الإجراء |
|---------|---------|
| 2025-12-02 | القفل الأولي (19 ملف) |
| **2025-12-07** | **إعادة الهيكلة: نقل ~30 ملف إلى extensions/** |

---

## 📊 الإحصائيات | Statistics

| المقياس | القيمة |
|---------|--------|
| ملفات النواة المقفلة | 15 ملف |
| ملفات bytecode المقفلة | 6 ملفات |
| ملفات منقولة للـ extensions | ~30 ملف |
| إجمالي سطور النواة المقفلة | ~600,000+ سطر |

---

## 🏗️ الهيكل الجديد | New Structure

```
bayan/bayan/                    # النواة النقية (15 ملف مقفل)
├── 🔒 __init__.py
├── 🔒 lexer.py
├── 🔒 parser.py
├── 🔒 ast_nodes.py
├── 🔒 traditional_interpreter.py
├── 🔒 hybrid_interpreter.py
├── 🔒 logical_engine.py
├── 🔒 builtins.py
├── 🔒 object_system.py
├── 🔒 type_checker.py
├── 🔒 import_system.py
├── 🔒 metaprogramming.py
├── 🔒 error_messages.py
├── 🔒 entity_engine.py
├── 🔒 compiler_interface.py
├── 🔒 bytecode/
│   ├── 🔒 __init__.py
│   ├── 🔒 opcodes.py
│   ├── 🔒 instruction.py
│   ├── 🔒 codegen.py
│   ├── 🔒 optimizer.py
│   └── 🔒 vm.py
│
└── (unlocked files for backward compatibility)

extensions/                      # الأنظمة المتقدمة
├── dual_brain/
├── glm/
├── equations/
├── arabic_nlp/
├── vocabulary/
├── networks/
├── knowledge/
├── visualization/
├── baserah/
└── (existing extensions)
```
