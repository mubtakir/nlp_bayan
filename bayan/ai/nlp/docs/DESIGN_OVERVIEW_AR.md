# تصميم النموذج التوليدي (nlp_bayan)

## خريطة الترحيل من الأنظمة القديمة (bayan_python)
- bayan_solutions/linguistic_equations.by → core/linguistic_equations.bayan (مفاهيم ومعادلات + قواعد استخراج).
- bayan_solutions/probabilistic_reasoning.by → core/probabilistic.bayan (prob/ربما/محتمل/غير_محتمل/…)
- bayan_solutions/semantic_networks.by → core/semantic_network.bayan (عُقد/علاقات واستعلامات أساسية).
- bayan_solutions/operator_definitions.by → core/operators.bayan (أنواع المشغّلات وإمكانية التطبيق).
- bayan_solutions/object_definitions.by → core/entities.bayan (تبسيط لنمذجة الكيانات وحالاتها).
- bayan/core/causal_network_engine.by → core/causal_network.bayan (واجهة مبسطة أولية).

- bayan_solutions/information_equations.by → core/information_equations.bayan (نمذجة I=Ω(S,E,R) مبسطة).
- bayan_solutions/morphosyntactic_rules.by → core/morphosyntactic_rules.bayan (جذور/أنماط أساسية).
- bayan_solutions/event_processing.by → core/event_processing.bayan (تسلسل زماني مبسط).
- bayan_solutions/expert_knowledge_base.by → core/expert_knowledge_base.bayan (عينات معرفة خبيرة).
- bayan_solutions/logical_inference.by → core/logical_inference.bayan (سلاسل أسلاف/أجداد …).
- bayan_solutions/shape_equations.by → core/shape_equations.bayan (أنواع ومعادلات أشكال).
- bayan_solutions/knowledge_management.by → core/knowledge_management.bayan (عناصر معرفة وروابط).
- bayan_solutions/object_definitions.by → core/object_definitions.bayan (تفكيك Φ/Ψ/Γ إلى حقائق).

### ملاحظات نحوية/تنفيذية
- تم تأجيل استخدام retract/assert و findall المركّب داخل القواعد لحين تثبيت الصياغة المدعومة.
- يُفضّل إجراء التحديثات الإجرائية خارج القواعد، أو عبر دوال منفصلة تستدعي قواعد مبسطة.

## طبقات النموذج
1) Representation: كيانات، علاقات، احتمالات، معادلات لغوية.
2) Inference: استعلامات منطقية، شبكات سببية/دلالية، قواعد اختيار.
3) Realization: توليد جملة عربية وفق قوالب بسيطة قابلة للتوسّع.

## حدود النطاق في الإصدار الأولي
- قواعد/حقائق مختصرة لتثبيت الهيكل.
- لا توجد تبعيات خارجية؛ كل شيء بيان-فقط.
- أمثلة وتشغيل سريع؛ لاحقاً نضيف اختبارات أدق واستدلال أعمق.

## كيفية الاستخدام
- استورد الوحدات داخل ملفات .bayan كما في المثال.
- استخدم الدالة generator_pipeline.generate_simple_ar(subject, verb, object) كبداية.

