# 🔒 ملفات نواة لغة البيان المقفلة
# Bayan Language Core Files - Locked (Read-Only)

---

## ⚠️ تحذير مهم | Important Warning

هذه الملفات مقفلة للقراءة فقط (Read-Only) لحماية نواة اللغة من التعديلات العرضية.
These files are locked (read-only) to protect the language core from accidental modifications.

---

## 🔒 الملفات المقفلة | Locked Files

### 📁 النواة الرئيسية | Core (bayan/bayan/)

| الملف | الوصف | Description |
|-------|-------|-------------|
| `__init__.py` | تهيئة الوحدة | Module init |
| `lexer.py` | المحلل المعجمي | Lexical Analyzer |
| `parser.py` | المحلل النحوي | Parser |
| `ast_nodes.py` | عقد الشجرة التركيبية | AST Nodes |
| `traditional_interpreter.py` | المفسر التقليدي | Traditional Interpreter |
| `hybrid_interpreter.py` | المفسر الهجين | Hybrid Interpreter |
| `logical_engine.py` | المحرك المنطقي | Logic Engine |
| `builtins.py` | الدوال المدمجة | Built-in Functions |
| `type_checker.py` | مدقق الأنواع | Type Checker |
| `object_system.py` | نظام الكائنات | Object System |
| `import_system.py` | نظام الاستيراد | Import System |
| `metaprogramming.py` | البرمجة الوصفية | Metaprogramming |
| `error_messages.py` | رسائل الأخطاء | Error Messages |

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

## 📝 الملفات غير المقفلة | Unlocked Files

### ✅ المكتبات القياسية | Standard Library (bayan/bayan/stdlib/)
- يمكن التعديل والإضافة
- Can be modified and extended

### ✅ الأمثلة | Examples (examples/)
- يمكن التعديل والإضافة
- Can be modified and extended

### ✅ نماذج NLP/AI | NLP/AI Models (nlp_bayan/, ai_bayan/)
- يمكن التعديل والإضافة
- Can be modified and extended

---

## 🔓 لفك القفل | To Unlock

إذا كنت بحاجة لتعديل ملفات النواة:
If you need to modify core files:

```bash
# فك قفل ملف واحد
chmod 644 bayan/bayan/lexer.py

# فك قفل كل ملفات النواة
chmod 644 bayan/bayan/*.py bayan/bayan/bytecode/*.py

# إعادة القفل
chmod 444 bayan/bayan/lexer.py bayan/bayan/parser.py bayan/bayan/ast_nodes.py \
    bayan/bayan/traditional_interpreter.py bayan/bayan/hybrid_interpreter.py \
    bayan/bayan/logical_engine.py bayan/bayan/builtins.py bayan/bayan/type_checker.py \
    bayan/bayan/object_system.py bayan/bayan/import_system.py \
    bayan/bayan/metaprogramming.py bayan/bayan/error_messages.py \
    bayan/bayan/__init__.py bayan/bayan/bytecode/*.py
```

---

## 📅 تاريخ القفل | Lock Date
- **التاريخ:** 2025-12-02
- **السبب:** حماية نواة اللغة من التعديلات العرضية

---

## 📊 الإحصائيات | Statistics

| المقياس | القيمة |
|---------|--------|
| ملفات النواة المقفلة | 19 ملف |
| ملفات المكتبات (غير مقفلة) | 10 ملفات |
| إجمالي سطور النواة | ~15,000+ سطر |

