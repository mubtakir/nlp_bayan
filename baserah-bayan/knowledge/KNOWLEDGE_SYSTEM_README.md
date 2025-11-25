# 📚 نظام المعرفة - Knowledge System

## 🎯 نظرة عامة

نظام المعرفة هو مكون أساسي في **بصيرة AI** يوفر قدرات شاملة لتغذية، تخزين، استعلام، وإدارة المعرفة. النظام مصمم ليكون مرناً وقابلاً للتوسع ومتكاملاً مع بقية مكونات النظام.

## 🏗️ البنية المعمارية

### المكونات الأساسية

```
knowledge/
├── knowledge-feeding-system.bn      # نظام تغذية المعرفة (592 سطر)
├── knowledge-base.bn                # قاعدة المعرفة (599 سطر)
├── knowledge-query-engine.bn        # محرك الاستعلام (542 سطر)
├── knowledge-integration.bn         # نظام التكامل (300 سطر)
├── knowledge-examples.bn            # أمثلة عملية (350 سطر)
├── knowledge-demo.html              # واجهة ويب (700 سطر)
└── KNOWLEDGE_SYSTEM_README.md       # هذا الملف
```

**الحجم الإجمالي:** ~3,083 سطر

---

## 📦 المكونات التفصيلية

### 1. نظام تغذية المعرفة (Knowledge Feeding System)

**الملف:** `knowledge-feeding-system.bn`

#### الوظائف الرئيسية:
- ✅ دعم أنواع ملفات متعددة (JSON, CSV, TXT, XML, XLSX, MD)
- ✅ تحويل تلقائي للبيانات إلى عناصر معرفية
- ✅ استخراج تلقائي للعلامات (Tags)
- ✅ تحديد تلقائي لمستوى المعرفة
- ✅ معالجة دفعية للملفات

#### الفئات الرئيسية:

**`KnowledgeItem`** - عنصر معرفي
```javascript
class KnowledgeItem {
    itemId: string
    title: string
    content: string
    category: KnowledgeCategory
    level: KnowledgeLevel
    tags: array<string>
    sourceFile: string
    sourceType: DataSource
    confidence: number
}
```

**`KnowledgeFeedingSystem`** - نظام التغذية
```javascript
class KnowledgeFeedingSystem {
    processFile(filePath, fileContent, category, metadata)
    detectFileType(filePath)
    search(query, category)
    getStatistics()
}
```

#### التعدادات (Enums):

**`FileType`** - أنواع الملفات المدعومة
- JSON, CSV, TXT, XML, XLSX, SQL, MD, PDF, DOCX

**`KnowledgeCategory`** - فئات المعرفة
- MATHEMATICAL (رياضيات)
- SCIENTIFIC (علوم)
- LINGUISTIC (لغويات)
- HISTORICAL (تاريخ)
- TECHNICAL (تقنية)
- PHILOSOPHICAL (فلسفة)
- CULTURAL (ثقافة)
- GENERAL (عام)

**`KnowledgeLevel`** - مستويات المعرفة
- BASIC (أساسي)
- INTERMEDIATE (متوسط)
- ADVANCED (متقدم)
- EXPERT (خبير)

**`DataSource`** - مصادر البيانات
- FILE_IMPORT (استيراد ملف)
- DATABASE_IMPORT (استيراد قاعدة بيانات)
- WEB_SCRAPING (استخراج من الويب)
- MANUAL_INPUT (إدخال يدوي)
- API_IMPORT (استيراد من API)
- BULK_UPLOAD (رفع دفعي)

---

### 2. قاعدة المعرفة (Knowledge Base)

**الملف:** `knowledge-base.bn`

#### الوظائف الرئيسية:
- ✅ تخزين منظم للعناصر المعرفية
- ✅ إدارة العلاقات بين العناصر
- ✅ تجميع العناصر في مجموعات (Clusters)
- ✅ فهرسة متقدمة (حسب الفئة، المستوى، العلامات)
- ✅ بحث متقدم متعدد المعايير

#### الفئات الرئيسية:

**`KnowledgeRelation`** - علاقة معرفية
```javascript
class KnowledgeRelation {
    relationId: string
    sourceItemId: string
    targetItemId: string
    relationType: RelationType
    strength: number  // 0.0 - 1.0
    bidirectional: boolean
}
```

**`KnowledgeCluster`** - مجموعة معرفية
```javascript
class KnowledgeCluster {
    clusterId: string
    name: string
    itemIds: Set<string>
    category: KnowledgeCategory
    tags: array<string>
}
```

**`KnowledgeBase`** - قاعدة المعرفة
```javascript
class KnowledgeBase {
    addItem(item)
    getItem(itemId)
    removeItem(itemId)
    addRelation(relation)
    getItemRelations(itemId)
    createCluster(name, category)
    search(query)
    searchByCategory(category)
    searchByLevel(level)
    searchByTag(tag)
    advancedSearch(criteria)
    getRelatedItems(itemId, maxDepth)
    getStatistics()
    exportToJSON()
}
```

#### التعدادات:

**`RelationType`** - أنواع العلاقات
- IS_A (هو نوع من)
- PART_OF (جزء من)
- RELATED_TO (مرتبط بـ)
- DEPENDS_ON (يعتمد على)
- CONTRADICTS (يناقض)
- SUPPORTS (يدعم)
- EXAMPLE_OF (مثال على)
- DERIVED_FROM (مشتق من)

---

### 3. محرك الاستعلام (Knowledge Query Engine)

**الملف:** `knowledge-query-engine.bn`

#### الوظائف الرئيسية:
- ✅ بحث بسيط (Simple Search)
- ✅ بحث دلالي (Semantic Search)
- ✅ بحث علائقي (Relational Search)
- ✅ بحث غامض (Fuzzy Search)
- ✅ بحث متقدم (Advanced Search)
- ✅ ترتيب ذكي للنتائج
- ✅ حساب الصلة (Relevance Scoring)

#### الفئات الرئيسية:

**`QueryResult`** - نتيجة استعلام
```javascript
class QueryResult {
    item: KnowledgeItem
    relevanceScore: number  // 0.0 - 1.0
    matchedFields: array<string>
    snippet: string
}
```

**`KnowledgeQueryEngine`** - محرك الاستعلام
```javascript
class KnowledgeQueryEngine {
    simpleQuery(query, maxResults)
    semanticQuery(query, maxResults)
    relationalQuery(itemId, relationType, maxDepth)
    fuzzyQuery(query, maxResults, threshold)
    advancedQuery(criteria)
    queryByCategory(category, maxResults)
    queryByTag(tag, maxResults)
    getStatistics()
}
```

#### خوارزميات البحث:

**1. البحث البسيط:**
- تطابق العنوان (وزن 40%)
- تطابق المحتوى (وزن 30%)
- تطابق العلامات (وزن 20%)
- الثقة (وزن 10%)

**2. البحث الدلالي:**
- استخراج الكلمات المفتاحية
- إزالة كلمات التوقف
- بحث متعدد الكلمات
- مكافأة التطابقات المتعددة

**3. البحث الغامض:**
- خوارزمية Levenshtein Distance
- حساب التشابه النصي
- عتبة قابلة للتخصيص

#### التعدادات:

**`QueryType`** - أنواع الاستعلامات
- SIMPLE (بسيط)
- SEMANTIC (دلالي)
- RELATIONAL (علائقي)
- FUZZY (غامض)
- ADVANCED (متقدم)

**`SortMethod`** - طرق الترتيب
- RELEVANCE (حسب الصلة)
- DATE (حسب التاريخ)
- CONFIDENCE (حسب الثقة)
- LEVEL (حسب المستوى)
- ALPHABETICAL (أبجدي)

---

### 4. نظام التكامل (Integrated Knowledge System)

**الملف:** `knowledge-integration.bn`

#### الوظائف الرئيسية:
- ✅ واجهة موحدة لجميع المكونات
- ✅ تكامل سلس بين التغذية والاستعلام
- ✅ إدارة شاملة للعلاقات والمجموعات
- ✅ إحصائيات موحدة

#### الفئة الرئيسية:

**`IntegratedKnowledgeSystem`** - النظام المتكامل
```javascript
class IntegratedKnowledgeSystem {
    // تغذية المعرفة
    feedFromFile(filePath, fileContent, category, metadata)
    feedFromText(title, content, category, level)
    feedFromJSON(data, category)
    
    // البحث والاستعلام
    search(query, maxResults)
    semanticSearch(query, maxResults)
    advancedSearch(criteria)
    searchByCategory(category, maxResults)
    searchByTag(tag, maxResults)
    fuzzySearch(query, maxResults, threshold)
    
    // إدارة العلاقات
    linkItems(sourceId, targetId, relationType, strength, bidirectional)
    getRelatedItems(itemId, maxDepth)
    relationalSearch(itemId, relationType, maxDepth)
    
    // إدارة المجموعات
    createCluster(name, category)
    addToCluster(itemId, clusterId)
    getClusterItems(clusterId)
    
    // الإحصائيات
    getStatistics()
    exportKnowledgeBase()
    clearAll()
}
```

---

## 🎯 أمثلة الاستخدام

### مثال 1: تغذية المعرفة من نص

```javascript
import { IntegratedKnowledgeSystem } from "./knowledge-integration.bn";
import { KnowledgeCategory, KnowledgeLevel } from "./knowledge-feeding-system.bn";

let system = new IntegratedKnowledgeSystem();

let itemId = system.feedFromText(
    "نظرية فيثاغورس",
    "في المثلث القائم الزاوية، مربع طول الوتر يساوي مجموع مربعي طولي الضلعين الآخرين.",
    KnowledgeCategory.MATHEMATICAL,
    KnowledgeLevel.INTERMEDIATE
);
```

### مثال 2: البحث البسيط

```javascript
let results = system.search("فيثاغورس", 10);

for (let result of results) {
    console.log(`${result.item.title} - الصلة: ${result.relevanceScore}`);
}
```

### مثال 3: ربط العناصر المعرفية

```javascript
import { RelationType } from "./knowledge-base.bn";

let aiId = system.feedFromText("الذكاء الاصطناعي", "...", ...);
let mlId = system.feedFromText("التعلم الآلي", "...", ...);

system.linkItems(mlId, aiId, RelationType.PART_OF, 1.0, false);
```

---

## 🌐 واجهة الويب

**الملف:** `knowledge-demo.html`

### الميزات:
- ✅ إضافة معرفة جديدة
- ✅ بحث متعدد الأنواع
- ✅ عرض النتائج مع الصلة
- ✅ إحصائيات حية
- ✅ تصدير قاعدة المعرفة
- ✅ واجهة عربية جميلة

### فتح الواجهة:
```bash
file:///path/to/baserah-bayan/knowledge/knowledge-demo.html
```

---

## 📊 الإحصائيات

- **إجمالي الأسطر:** ~3,083 سطر
- **عدد الفئات:** 10 فئات رئيسية
- **عدد الدوال:** 80+ دالة
- **أنواع الملفات المدعومة:** 9 أنواع
- **أنواع البحث:** 5 أنواع
- **أنواع العلاقات:** 8 أنواع

---

## 🔄 التكامل مع المكونات الأخرى

### التكامل مع نظام الذاكرة:
- الذاكرة الدلالية تستخدم قاعدة المعرفة لتخزين الحقائق
- الذاكرة العرضية تستخدم نظام التغذية لتخزين الأحداث

### التكامل مع طبقات التفكير:
- الطبقة المنطقية تستخدم محرك الاستعلام للاستدلال
- الطبقة اللغوية تستخدم قاعدة المعرفة للمعاني

---

## 🚀 الخطوات التالية

1. ✅ نظام المعرفة (مكتمل)
2. ⏳ نظام التعلم (الأسبوع 3)
3. ⏳ التكامل اللغوي (الأسبوع 4)
4. ⏳ الأنظمة المتقدمة (الأسابيع 5-8)

---

**تم بناء نظام المعرفة بنجاح! 🎉**

*باسل يحيى عبدالله - 2025-10-27*
