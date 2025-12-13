# خارطة طريق "بيان" نحو العبقرية
# Bayan Roadmap to Genius AI

هذه الوثيقة تحدد المسار المستقبلي لتحويل "بيان" من نظام منطقي متقدم إلى **عقل اصطناعي عبقري** (Genius AI) يجمع بين المنطق الصارم والطلاقة اللغوية والوعي الذاتي.

This document outlines the future path to transform Bayan from an advanced logical system into a **Genius AI** that combines strict logic, linguistic fluency, and self-awareness.

---

## الرؤية: العقل الهجين
## Vision: The Hybrid Mind

الهدف هو بناء نظام لا "يحفظ" الإجابات، بل "يفكر" فيها.
The goal is to build a system that doesn't just "memorize" answers, but "thinks" about them.

يتم ذلك عبر دمج ثلاث ركائز مفقودة حالياً:
This is achieved by bridging three currently missing pillars:

1.  **المترجم (The Translator):** جسر بين اللغة الطبيعية ومنطق بيان.
2.  **الصوت (The Voice):** قدرة التوليد اللغوي الطليق.
3.  **الذات (The Self):** حلقة تفكير واعية ومستقلة.

---

## المراحل المستقبلية
## Future Phases

### المرحلة 5: الجسر المعرفي (The Cognitive Bridge)
**الهدف:** جعل النظام يفهم الأسئلة البشرية ويحولها إلى منطق.
**Goal:** Enable the system to understand human questions and translate them into logic.

*   [ ] **تكامل نموذج لغوي (LLM Integration):** دمج نموذج محلي صغير (مثل Llama/GPT-2) ليعمل كمترجم.
*   [ ] **هندسة التلقين المنطقي (Logical Prompt Engineering):** تدريب النموذج على تحويل "لماذا الشمس حارة؟" إلى `query why(is_hot(Sun))`.
*   [ ] **المترجم العكسي (Reverse Translator):** تحويل نتائج المنطق `[Fact(burning)]` إلى جملة "لأن الظواهر تشير إلى احتراق".

### المرحلة 6: الصوت المولد (The Generative Voice)
**الهدف:** التخلص من الردود المعلبة والقوالب الجامدة.
**Goal:** Eliminate canned responses and rigid templates.

*   [ ] **محرك التوليد (Generation Engine):** استبدال `generative_model.py` المعتمد على القواعد بنموذج توليدي كامل.
*   [ ] **تطعيم النص بالحقائق (Fact-Informed Generation):** تلقيم الحقائق المستنبطة من `IstinbatEngine` إلى النموذج اللغوي لصياغة الجواب النهائي.
    *   *Prompt: "Given facts [X, Y], answer the user's question elegantly in Arabic."*

### المرحلة 7: الحلقة الذاتية (The Agentic Component)
**الهدف:** الاستقلال والقدرة على تصحيح الذات.
**Goal:** Autonomy and Self-Correction.

*   [ ] **حلقة التفكير (Thought Loop):** (ملاحظة -> تفكير -> قرار -> فعل).
*   [ ] **نقد الذات (Self-Reflection):** قبل الرد، يسأل النظام نفسه: "هل هذا الجواب منطقي؟" باستخدام `check_contradictions`.
*   [ ] **البحث النشط (Active Search):** إذا لم يجد المعلومة، يقرر البحث عنها (في الويب أو الكتب).

---

## البنية التقنية المقترحة
## Proposed Technical Architecture

```mermaid
graph TD
    User[المستخدم] -->|Language| Translator[المترجم (LLM)]
    Translator -->|Logical Query| LogicEngine[محرك الاستنباط]
    Translator -->|Neural Search| NeuralEngine[المحرك العصبي]
    
    LogicEngine -->|Facts| Synthesizer[المصيغ (Generator)]
    NeuralEngine -->|Context| Synthesizer
    
    Synthesizer -->|Fluent Response| User
    
    subgraph "Deep Mind / العقل العميق"
        LogicEngine
        NeuralEngine
    end
    
    subgraph "Cognitive Interface / الواجهة الإدراكية"
        Translator
        Synthesizer
    end
```

---

## سجل التغييرات
## Change Log

| التاريخ | المرحلة | الحالة | الملاحظات |
| :--- | :--- | :--- | :--- |
| 2025-12-13 | Neural Integration | ✅ Done | تم دمج البحث العصبي. |
| 2025-12-13 | Stdlib Expansion | ✅ Done | تم توسيع المكتبة القياسية. |
| ... | Cognitive Bridge | ⏳ Pending | الخطوة القادمة. |
