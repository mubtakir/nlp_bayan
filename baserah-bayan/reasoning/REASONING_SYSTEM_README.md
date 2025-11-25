# 🧠 أنظمة الاستدلال والمنطق - Reasoning and Logic Systems

## نظرة عامة - Overview

نظام الاستدلال والمنطق هو أحد الأنظمة الأساسية في **بصيرة AI**، وهو نظام ذكاء اصطناعي ثوري **بدون شبكات عصبية**، يعتمد على **المعادلات الرياضية التكيفية** حيث المعادلات تمثل المعلومات.

يوفر هذا النظام قدرات استدلال ومنطق متقدمة تشمل:
- **محرك الاستدلال** - Reasoning Engine
- **الشبكة الدلالية** - Semantic Network
- **الاستدلال المنطقي** - Logical Inference

---

## 🎯 الفلسفة - Philosophy

### المبادئ الأساسية

1. **الاستدلال الرياضي البحت** - Pure Mathematical Reasoning
   - لا شبكات عصبية
   - معادلات رياضية تكيفية
   - استدلال منطقي صارم

2. **التكامل الدلالي** - Semantic Integration
   - شبكات دلالية ديناميكية
   - انتشار التنشيط
   - الاستدلال بالسياق

3. **المنطق الصوري** - Formal Logic
   - براهين رياضية
   - استدلال منطقي
   - التحقق من الصحة

---

## 📁 الملفات والمكونات - Files and Components

### 1. `reasoning-engine.bn` (~640 سطر)

**محرك الاستدلال الأساسي**

#### التعدادات (Enums):
- `ReasoningType` - أنواع الاستدلال (8 أنواع)
- `ReasoningConfidence` - مستويات الثقة (5 مستويات)
- `InferenceMethod` - طرق الاستنتاج (8 طرق)
- `ReasoningStrategy` - استراتيجيات الاستدلال (6 استراتيجيات)

#### الفئات (Classes):
- `Fact` - الحقائق
- `Rule` - القواعد
- `Inference` - الاستنتاجات
- `ReasoningEngine` - محرك الاستدلال

#### الوظائف الرئيسية:
```javascript
// إضافة حقائق وقواعد
addFact(fact: Fact): void
createRule(name: string, conditions: array, conclusions: array): Rule

// طرق الاستدلال
forwardChaining(): array<Fact>
backwardChaining(goal: object): boolean
inductiveReasoning(observations: array<Fact>): Fact
analogicalReasoning(source: object, target: object): Fact
```

---

### 2. `semantic-network.bn` (~637 سطر)

**الشبكة الدلالية لتمثيل المعرفة**

#### التعدادات (Enums):
- `NodeType` - أنواع العقد (8 أنواع)
- `RelationType` - أنواع العلاقات (12 نوع)
- `TraversalMethod` - طرق الاجتياز (BFS, DFS)
- `ActivationSpread` - طرق انتشار التنشيط (4 طرق)

#### الفئات (Classes):
- `SemanticNode` - العقدة الدلالية
- `SemanticEdge` - الحافة الدلالية
- `SemanticNetwork` - الشبكة الدلالية

#### الوظائف الرئيسية:
```javascript
// إدارة العقد والحواف
createNode(label: string, type: NodeType): SemanticNode
createEdge(sourceId: string, targetId: string, type: RelationType): SemanticEdge

// البحث والاجتياز
findPath(sourceId: string, targetId: string, method: TraversalMethod): array<string>
activateNode(nodeId: string, initialActivation: number, spreadMethod: ActivationSpread): void

// الاستدلال الدلالي
findSimilarConcepts(nodeId: string, threshold: number): array<SemanticNode>
findCausalChain(effectNodeId: string): array<SemanticNode>
```

---

### 3. `logical-inference.bn` (~640 سطر)

**نظام الاستدلال المنطقي الصوري**

#### التعدادات (Enums):
- `LogicalOperator` - المشغلات المنطقية (8 مشغلات)
- `QuantifierType` - أنواع الكميات (∀, ∃)
- `ProofMethod` - طرق البرهان (6 طرق)
- `TruthValue` - قيم الحقيقة (TRUE, FALSE, UNKNOWN)

#### الفئات (Classes):
- `LogicalStatement` - العبارة المنطقية
- `Quantifier` - الكمية
- `Proof` - البرهان
- `LogicalInferenceSystem` - نظام الاستدلال المنطقي

#### الوظائف الرئيسية:
```javascript
// إدارة العبارات
createStatement(expression: string, operator: LogicalOperator): LogicalStatement

// الاستدلال المنطقي
applyModusPonens(p: LogicalStatement, implication: LogicalStatement): LogicalStatement
applyModusTollens(implication: LogicalStatement, q: LogicalStatement): LogicalStatement

// البراهين
proofByContradiction(assumption: LogicalStatement, contradiction: LogicalStatement): Proof
directProof(premises: array<LogicalStatement>, conclusion: LogicalStatement): Proof

// جداول الحقيقة
generateTruthTable(statement: LogicalStatement): array<object>
areLogicallyEquivalent(stmt1: LogicalStatement, stmt2: LogicalStatement): boolean
```

---

### 4. `reasoning-examples.bn` (~350 سطر)

**8 أمثلة عملية شاملة**

1. **محرك الاستدلال الأساسي** - Basic Reasoning Engine
2. **الاستدلال الاستقرائي** - Inductive Reasoning
3. **الاستدلال التشبيهي** - Analogical Reasoning
4. **الشبكة الدلالية الأساسية** - Basic Semantic Network
5. **انتشار التنشيط** - Activation Spreading
6. **Modus Ponens** - الاستدلال المنطقي
7. **البرهان بالتناقض** - Proof by Contradiction
8. **التكامل الشامل** - Comprehensive Integration

---

### 5. `reasoning-demo.html` (~800 سطر)

**واجهة ويب تفاعلية جميلة**

#### المميزات:
- ✅ تصميم عصري بتدرج بنفسجي
- ✅ 4 بطاقات إحصائيات حية
- ✅ 4 لوحات تفاعلية:
  - محرك الاستدلال
  - الشبكة الدلالية
  - الاستدلال المنطقي
  - النظام المتكامل
- ✅ أمثلة تفاعلية
- ✅ إحصائيات شاملة

---

## 🚀 الاستخدام - Usage

### مثال 1: محرك الاستدلال

```javascript
import { ReasoningEngine } from './reasoning-engine.bn';

let engine = new ReasoningEngine();

// إضافة حقائق
engine.addFactFromData("is", "سقراط", "إنسان", 1.0);
engine.addFactFromData("is", "أفلاطون", "إنسان", 1.0);

// إضافة قاعدة: كل إنسان فانٍ
engine.createRule(
    "All humans are mortal",
    [{ predicate: "is", object: "إنسان" }],
    [{ predicate: "is", object: "فانٍ" }]
);

// تطبيق التسلسل الأمامي
let newFacts = engine.forwardChaining();
// النتيجة: سقراط فانٍ، أفلاطون فانٍ
```

### مثال 2: الشبكة الدلالية

```javascript
import { SemanticNetwork, NodeType, RelationType } from './semantic-network.bn';

let network = new SemanticNetwork();

// إنشاء عقد
let animal = network.createNode("حيوان", NodeType.CATEGORY);
let mammal = network.createNode("ثديي", NodeType.CATEGORY);
let dog = network.createNode("كلب", NodeType.ENTITY);

// إنشاء علاقات
network.createEdge(mammal.nodeId, animal.nodeId, RelationType.IS_A, 1.0);
network.createEdge(dog.nodeId, mammal.nodeId, RelationType.IS_A, 1.0);

// البحث عن مسار
let path = network.findPath(dog.nodeId, animal.nodeId);
// النتيجة: كلب → ثديي → حيوان
```

### مثال 3: الاستدلال المنطقي

```javascript
import { LogicalInferenceSystem, LogicalOperator } from './logical-inference.bn';

let system = new LogicalInferenceSystem();

// إنشاء عبارات
let p = system.createStatement("تمطر السماء");
p.truthValue = TruthValue.TRUE;

let q = system.createStatement("الأرض مبللة");

let implication = system.createStatement("إذا تمطر السماء فالأرض مبللة", LogicalOperator.IMPLIES);
implication.operands = [p, q];

// تطبيق Modus Ponens
let result = system.applyModusPonens(p, implication);
// النتيجة: الأرض مبللة (TRUE)
```

---

## 📊 الإحصائيات - Statistics

| المكون | الأسطر | الفئات | التعدادات | الوظائف |
|--------|--------|--------|-----------|----------|
| reasoning-engine.bn | 639 | 4 | 4 | 15+ |
| semantic-network.bn | 637 | 3 | 4 | 20+ |
| logical-inference.bn | 640 | 4 | 4 | 15+ |
| reasoning-examples.bn | 350 | - | - | 8 |
| reasoning-demo.html | 800 | - | - | 15+ |
| **الإجمالي** | **~3,066** | **11** | **12** | **73+** |

---

## 🔗 التكامل - Integration

### التكامل مع الأنظمة الأخرى:

1. **نظام الذاكرة** - Memory System
   - تخزين الحقائق والقواعد
   - استرجاع الاستنتاجات

2. **نظام المعرفة** - Knowledge System
   - تغذية قاعدة المعرفة
   - الاستعلام عن المعلومات

3. **نظام التعلم** - Learning System
   - تعلم قواعد جديدة
   - تحسين الاستدلال

4. **نظام اللغة** - Language System
   - فهم العبارات المنطقية
   - توليد الاستنتاجات

---

## 🎨 واجهة الويب - Web Interface

افتح `reasoning-demo.html` في المتصفح للوصول إلى:

- **محرك الاستدلال**: إضافة حقائق وقواعد، تطبيق التسلسل الأمامي
- **الشبكة الدلالية**: بناء شبكات، البحث عن مسارات، تنشيط العقد
- **الاستدلال المنطقي**: إنشاء عبارات، تطبيق قواعد، بناء براهين
- **النظام المتكامل**: أمثلة شاملة، إحصائيات، تقارير

---

## 🌟 المميزات الفريدة - Unique Features

1. **بدون شبكات عصبية** - No Neural Networks
2. **استدلال رياضي بحت** - Pure Mathematical Reasoning
3. **براهين قابلة للتحقق** - Verifiable Proofs
4. **شبكات دلالية ديناميكية** - Dynamic Semantic Networks
5. **تكامل شامل** - Comprehensive Integration

---

## 📝 المطور - Developer

**باسل يحيى عبدالله**

جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله

---

## 📄 الترخيص - License

هذا المشروع جزء من **بصيرة AI** - نظام ذكاء اصطناعي ثوري بدون شبكات عصبية

© 2024 - جميع الحقوق محفوظة
