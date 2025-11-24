# 🔧 Internals

للمطورين الذين يريدون المساهمة في تطوير Bayan.

---

## 📖 للمساهمين

- [Developer Guide](developer-guide.md) - دليل شامل للمطورين
- [Contributing](contributing.md) - كيف تساهم في المشروع
- [Architecture](architecture.md) - البنية المعمارية
- [Testing](testing.md) - كتابة وتشغيل الاختبارات
- [Roadmap](roadmap.md) - خارطة طريق المشروع

---

## 🏗️ البنية الداخلية

```
bayan/
├── bayan/
│   ├── lexer.py          # المحلل اللفظي
│   ├── parser.py         # المحلل النحوي
│   ├── interpreter.py    # المفسر
│   └── ...
├── libraries/            # المكتبات
├── web_ide/             # Web IDE
└── tests/               # الاختبارات
```

---

## 🚀 البداية السريعة للمساهمين

```bash
# 1. Fork المشروع على GitHub
# 2. استنسخ fork الخاص بك
git clone https://github.com/YOUR_USERNAME/nlp_bayan.git
cd nlp_bayan

# 3. أنشئ branch جديد
git checkout -b feature/my-feature

# 4. اعمل تغييراتك
# ...

# 5. شغّل الاختبارات
pytest tests/

# 6. Commit و Push
git add .
git commit -m "Add: my feature"
git push origin feature/my-feature

# 7. افتح Pull Request على GitHub
```

---

[← العودة للفهرس](../README.md)
