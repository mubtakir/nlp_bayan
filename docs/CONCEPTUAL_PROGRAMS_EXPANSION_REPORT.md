# Conceptual Programs Expansion Report

## تقرير توسعة برامج المعاني التصورية

**Date / التاريخ:** 2025-11-16

---

## 1. Executive Summary / الملخص التنفيذي

This report documents the expansion of the Conceptual Circuits and Meaning Programs layer in the Bayan programming language. Two new meaning programs have been added to demonstrate the reusability and composability of the six canonical circuits across different domains.

تم توسيع طبقة الدوائر التصورية وبرامج المعاني في لغة البيان البرمجية. تمت إضافة برنامجي معاني جديدين لإثبات قابلية إعادة الاستخدام والتركيب للدوائر الستة الأساسية عبر مجالات مختلفة.

---

## 2. New Meaning Programs / برامج المعاني الجديدة

### 2.1 Social Relationship Building Program
**برنامج بناء العلاقات الاجتماعية**

- **File:** `ai/conceptual_programs.bayan`
- **Function:** `build_social_relationship_program(settings)`
- **Domain:** Social relationships, friendship, trust building
- **المجال:** العلاقات الاجتماعية، الصداقة، بناء الثقة

**Circuits Used / الدوائر المستخدمة:**
1. Action → StateChange → Evaluation (Interaction builds trust)
2. Causal Link (Interaction causes trust building)
3. Temporal Sequence (Meeting before friendship develops)
4. Contextualized Event (Shared activities in social context)
5. Uncertain Cause-Effect (Trust may/may not lead to lasting friendship)

**Key Entities / الكيانات الرئيسية:**
- `الشخص_أ` (Person A)
- `الشخص_ب` (Person B)

**Key Events / الأحداث الرئيسية:**
- `تفاعل_اجتماعي` (Social interaction)
- `بناء_الثقة` (Trust building)
- `اللقاء_الأول` (First meeting)
- `تطور_الصداقة` (Friendship development)
- `صداقة_دائمة` (Lasting friendship)

---

### 2.2 Daily Decision-Making Program
**برنامج اتخاذ القرارات اليومية**

- **File:** `ai/conceptual_programs.bayan`
- **Function:** `build_daily_decision_program(settings)`
- **Domain:** Daily life, personal decisions, choice evaluation
- **المجال:** الحياة اليومية، القرارات الشخصية، تقييم الخيارات

**Circuits Used / الدوائر المستخدمة:**
1. Action → StateChange → Evaluation (Evaluating options changes certainty level)
2. Causal Link (Evaluation causes decision)
3. Temporal Sequence (Thinking before deciding)
4. Contextualized Event (Decision in life context)
5. Uncertain Cause-Effect (Decision may/may not lead to positive outcome)

**Key Entities / الكيانات الرئيسية:**
- `الشخص` (The person)

**Key Events / الأحداث الرئيسية:**
- `تقييم_الخيارات` (Evaluating options)
- `التفكير` (Thinking)
- `اتخاذ_القرار` (Making decision)
- `نتيجة_إيجابية` (Positive outcome)

---

## 3. Orchestrator Integration / التكامل مع المنسق

### 3.1 Registry Updates / تحديثات السجل

**File:** `ai/conceptual_orchestrator.bayan`

Two new entries added to `get_program_registry()`:

```bayan
{
    "id": "social_relationship",
    "description": "Social relationship building narrative meaning program",
    "domains": ["social", "friendship", "relationships"],
    "intents": ["relationship_scenario", "friendship_scenario"],
    "builder": programs.build_social_relationship_program
}

{
    "id": "daily_decision",
    "description": "Daily decision-making narrative meaning program",
    "domains": ["daily_life", "personal", "decision"],
    "intents": ["decision_scenario", "choice_scenario"],
    "builder": programs.build_daily_decision_program
}
```

---

## 4. NL Mapper Expansion / توسعة محول اللغة الطبيعية

### 4.1 New Domain Detection / كشف المجالات الجديدة

**File:** `ai/conceptual_nl_mapper.bayan`

**Social Domain Keywords:**
- Arabic: `صداقة، صديق، علاقة، تفاعل اجتماعي، ثقة، لقاء`
- English: `friendship, friend, relationship, social, trust, meeting, interaction`

**Daily Life Domain Keywords:**
- Arabic: `قرار، اختيار، خيار، تفكير، حياة يومية`
- English: `decision, choice, option, decide, choose, daily, everyday`

---

## 5. Demo Files / ملفات العرض التوضيحي

### 5.1 Social Relationship Demo
**File:** `examples/conceptual_program_social_relationship_demo.bayan`

Demonstrates:
- Building the social relationship program
- Extracting merged conceptual trace
- Generating LM examples for each component
- Full pipeline from circuits to symbolic text

### 5.2 Orchestrator Social Demo
**File:** `examples/conceptual_orchestrator_social_demo.bayan`

Demonstrates:
- NL mapper converting Arabic/English text to control messages
- Orchestrator dispatching to correct program
- Settings affecting program behavior (scenario_variant, time_horizon)
- Full end-to-end pipeline

**Test Cases:**
1. Arabic input: `"أريد قصة عن صداقة بين شخصين"`
2. English input: `"Tell me about friendship and trust between two people"`
3. Programmatic control with optimistic scenario variant

---

## 6. Testing Results / نتائج الاختبار

### 6.1 Social Relationship Program
✅ Successfully generates merged trace with:
- 7 entities
- 8 events
- 2 causal links
- 1 transform

✅ LM examples generated successfully for both English and Arabic

### 6.2 Orchestrator Integration
✅ NL mapper correctly identifies social domain from Arabic keywords
✅ NL mapper correctly identifies social domain from English keywords
✅ Orchestrator successfully dispatches to `social_relationship` program
✅ Settings (scenario_variant, time_horizon) correctly passed to program

---

## 7. Architecture Validation / التحقق من البنية المعمارية

### 7.1 Design Principles Confirmed / تأكيد مبادئ التصميم

✅ **Language Neutrality:** All programs work with conceptual structures only
✅ **Compositionality:** Programs built entirely from existing circuits
✅ **Reusability:** Same 6 circuits used across 5 different domains
✅ **Typed Roles:** Clear role definitions maintained
✅ **Deterministic:** Same inputs produce same outputs
✅ **Settings-Driven:** scenario_variant and time_horizon affect values

### 7.2 Domains Covered / المجالات المغطاة

1. ✅ Education (Student study narrative)
2. ✅ Health (Medical treatment with uncertainty)
3. ✅ Economy (Investment with risk)
4. ✅ **Social** (Relationship building) - **NEW**
5. ✅ **Daily Life** (Decision making) - **NEW**

---

## 8. Next Steps / الخطوات التالية

### 8.1 Completed Tasks / المهام المنجزة
- ✅ Add new meaning programs to different domains (Task 4.5.1)
- ✅ Expand NL mapper vocabulary for new domains (Task 4.5.3)
- ✅ Add educational examples documenting real scenarios (Task 4.5.5)

### 8.2 Remaining Tasks / المهام المتبقية
- ⏳ Use `detail_level` and `focus` settings to control circuit inclusion (Task 4.5.2)
- ⏳ Support multiple programs per domain with selection policy (Task 4.5.4)
- ⏳ Design actual linguistic generation layer (Task 4.2)
- ⏳ Clearer link with LM layer in ai/nlp (Task 4.4)

---

## 9. Conclusion / الخلاصة

The expansion successfully demonstrates the power and flexibility of the Conceptual Circuits architecture. The same six canonical circuits can be composed in different ways to create meaningful narratives across diverse domains, from education to social relationships to daily decision-making.

نجحت التوسعة في إثبات قوة ومرونة بنية الدوائر التصورية. يمكن تركيب نفس الدوائر الستة الأساسية بطرق مختلفة لإنشاء سرديات ذات معنى عبر مجالات متنوعة، من التعليم إلى العلاقات الاجتماعية إلى اتخاذ القرارات اليومية.

The architecture maintains language neutrality, compositionality, and reusability while allowing settings to control behavior. This validates the conceptual LM approach as a viable foundation for symbolic AI reasoning.

تحافظ البنية على الحياد اللغوي والتركيبية وقابلية إعادة الاستخدام مع السماح للإعدادات بالتحكم في السلوك. هذا يؤكد صحة نهج النموذج اللغوي التصوري كأساس قابل للتطبيق للاستدلال الرمزي في الذكاء الاصطناعي.

---

**Report Generated By:** Augment Agent  
**Date:** 2025-11-16

