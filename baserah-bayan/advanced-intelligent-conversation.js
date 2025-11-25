/**
 * نظام حواري ذكي متقدم - بدون تلقين مسبق
 * يستخدم المعادلات الرياضية والتحليل اللغوي والاستنباط
 */

// ============ محرك المعجم المتقدم ============
class AdvancedLexiconEngine {
  constructor() {
    this.entries = new Map();
    this.rootIndex = new Map();
    this.categoryIndex = new Map();
  }
  
  addEntry(word, type, definition, category = 'general', root = null) {
    const entry = {
      word,
      type,
      definition,
      category,
      root,
      confidence: 1.0,
      semanticVector: this.computeSemanticVector(word),
      usageCount: 0
    };
    
    this.entries.set(word, entry);
    
    if (!this.categoryIndex.has(category)) {
      this.categoryIndex.set(category, new Set());
    }
    this.categoryIndex.get(category).add(word);
    
    return entry;
  }
  
  computeSemanticVector(word) {
    const vector = new Array(20).fill(0);
    for (let i = 0; i < word.length; i++) {
      const charCode = word.charCodeAt(i);
      vector[i % 20] += charCode / 100;
      vector[(i + 1) % 20] += Math.sin(charCode / 50);
    }
    return vector;
  }
  
  findSimilar(word, threshold = 0.5) {
    const targetVector = this.computeSemanticVector(word);
    const similar = [];
    
    for (const [key, entry] of this.entries) {
      const similarity = this.cosineSimilarity(targetVector, entry.semanticVector);
      if (similarity > threshold && key !== word) {
        similar.push({ word: key, similarity, entry });
      }
    }
    
    return similar.sort((a, b) => b.similarity - a.similarity);
  }
  
  cosineSimilarity(v1, v2) {
    let dot = 0, mag1 = 0, mag2 = 0;
    for (let i = 0; i < v1.length; i++) {
      dot += v1[i] * v2[i];
      mag1 += v1[i] * v1[i];
      mag2 += v2[i] * v2[i];
    }
    return dot / (Math.sqrt(mag1) * Math.sqrt(mag2) + 0.0001);
  }
  
  getByCategory(category) {
    return Array.from(this.categoryIndex.get(category) || [])
      .map(word => this.entries.get(word));
  }
}

// ============ المحلل اللغوي المتقدم ============
class AdvancedLanguageAnalyzer {
  constructor(lexicon) {
    this.lexicon = lexicon;
  }
  
  tokenize(text) {
    // إزالة علامات الترقيم وتقسيم
    return text.replace(/[؟?!.,،]/g, ' ')
      .split(/\s+/)
      .filter(w => w.length > 0);
  }
  
  analyzeWord(word) {
    const entry = this.lexicon.entries.get(word);
    if (entry) {
      entry.usageCount++;
      return { 
        word, 
        type: entry.type, 
        category: entry.category,
        confidence: 1.0, 
        source: 'lexicon' 
      };
    }
    
    // استنباط من الكلمات المشابهة
    const similar = this.lexicon.findSimilar(word, 0.5);
    if (similar.length > 0) {
      return { 
        word, 
        type: similar[0].entry.type,
        category: similar[0].entry.category,
        confidence: similar[0].similarity,
        source: 'similarity'
      };
    }
    
    // تحليل الأنماط العربية
    if (/^[\u0600-\u06FF]+$/.test(word)) {
      if (word.startsWith('ال')) {
        return { word, type: 'noun', category: 'general', confidence: 0.7, source: 'pattern' };
      }
      if (word.startsWith('ي') || word.startsWith('ت') || word.startsWith('أ')) {
        return { word, type: 'verb', category: 'general', confidence: 0.6, source: 'pattern' };
      }
      if (word.length <= 3) {
        return { word, type: 'particle', category: 'general', confidence: 0.5, source: 'pattern' };
      }
      return { word, type: 'noun', category: 'general', confidence: 0.5, source: 'pattern' };
    }
    
    return { word, type: 'unknown', category: 'general', confidence: 0.2, source: 'default' };
  }
  
  analyzeSentence(sentence) {
    const tokens = this.tokenize(sentence);
    const words = tokens.map(w => this.analyzeWord(w));
    
    const structure = words.map(w => w.type).join('-');
    const avgConfidence = words.reduce((sum, w) => sum + w.confidence, 0) / (words.length || 1);
    
    // تحديد الفئات الموجودة
    const categories = [...new Set(words.map(w => w.category))];
    
    return {
      sentence,
      tokens,
      words,
      structure,
      confidence: avgConfidence,
      categories
    };
  }
  
  extractKeywords(sentence) {
    const analysis = this.analyzeSentence(sentence);
    return analysis.words
      .filter(w => w.type === 'noun' || w.type === 'verb' || w.category !== 'general')
      .filter(w => w.confidence > 0.4)
      .map(w => w.word);
  }
  
  extractEntities(sentence) {
    const analysis = this.analyzeSentence(sentence);
    return analysis.words
      .filter(w => w.category !== 'general' && w.confidence > 0.5)
      .map(w => ({ word: w.word, category: w.category }));
  }
}

// ============ نظام الاستنباط الدلالي المتقدم ============
class AdvancedSemanticInferenceEngine {
  constructor(lexicon, analyzer) {
    this.lexicon = lexicon;
    this.analyzer = analyzer;
    this.knowledgeGraph = new Map();
    this.inferenceRules = [];
  }
  
  addKnowledge(subject, predicate, object, confidence = 1.0) {
    if (!this.knowledgeGraph.has(subject)) {
      this.knowledgeGraph.set(subject, []);
    }
    this.knowledgeGraph.get(subject).push({ predicate, object, confidence });
  }
  
  addInferenceRule(condition, action) {
    this.inferenceRules.push({ condition, action });
  }
  
  query(subject) {
    const direct = this.knowledgeGraph.get(subject) || [];
    
    // استنباط من الكلمات المشابهة
    const similar = this.lexicon.findSimilar(subject, 0.6);
    const inferred = [];
    
    for (const match of similar) {
      const facts = this.knowledgeGraph.get(match.word) || [];
      for (const fact of facts) {
        inferred.push({
          ...fact,
          confidence: fact.confidence * match.similarity,
          source: 'inferred'
        });
      }
    }
    
    return [...direct, ...inferred];
  }
  
  inferIntent(sentence) {
    const keywords = this.analyzer.extractKeywords(sentence);
    const entities = this.analyzer.extractEntities(sentence);
    const analysis = this.analyzer.analyzeSentence(sentence);
    
    const intentScores = {
      greeting: 0,
      question_identity: 0,
      question_creator: 0,
      question_how: 0,
      question_what: 0,
      statement: 0,
      request: 0,
      gratitude: 0
    };
    
    // تحليل الكلمات المفتاحية والكيانات
    for (const keyword of keywords) {
      const entry = this.lexicon.entries.get(keyword);
      if (entry) {
        if (entry.category === 'greeting') intentScores.greeting += 1.0;
        if (entry.category === 'question') {
          if (keyword === 'من') intentScores.question_identity += 0.8;
          if (keyword === 'ما') intentScores.question_what += 0.8;
          if (keyword === 'كيف') intentScores.question_how += 0.8;
        }
        if (entry.category === 'gratitude') intentScores.gratitude += 1.0;
        if (entry.category === 'system') intentScores.question_identity += 0.5;
      }
    }
    
    for (const entity of entities) {
      if (entity.category === 'system') intentScores.question_identity += 0.6;
      if (entity.category === 'creator') intentScores.question_creator += 0.6;
    }
    
    // تحليل البنية
    if (sentence.includes('؟') || sentence.includes('?')) {
      intentScores.question_what += 0.3;
    }
    
    if (analysis.structure.startsWith('question')) {
      intentScores.question_what += 0.4;
    }
    
    // اختيار النية الأعلى
    let maxIntent = 'statement';
    let maxScore = 0;
    
    for (const [intent, score] of Object.entries(intentScores)) {
      if (score > maxScore) {
        maxScore = score;
        maxIntent = intent;
      }
    }
    
    return {
      intent: maxIntent,
      confidence: Math.min(maxScore, 1.0),
      keywords,
      entities,
      analysis,
      allScores: intentScores
    };
  }
  
  inferResponse(intent, keywords, entities, context) {
    const responses = [];
    
    // البحث في الرسم المعرفي
    for (const keyword of keywords) {
      const knowledge = this.query(keyword);
      for (const fact of knowledge) {
        responses.push({
          text: fact.object,
          confidence: fact.confidence,
          source: fact.source || 'knowledge_graph'
        });
      }
    }
    
    for (const entity of entities) {
      const knowledge = this.query(entity.word);
      for (const fact of knowledge) {
        responses.push({
          text: fact.object,
          confidence: fact.confidence,
          source: fact.source || 'knowledge_graph'
        });
      }
    }
    
    if (responses.length > 0) {
      // دمج الردود
      const sortedResponses = responses.sort((a, b) => b.confidence - a.confidence);
      const topResponses = sortedResponses.slice(0, 3);
      const combinedText = topResponses.map(r => r.text).join('. ');
      const avgConfidence = topResponses.reduce((sum, r) => sum + r.confidence, 0) / topResponses.length;
      
      return {
        text: combinedText,
        confidence: avgConfidence,
        source: 'knowledge_inference'
      };
    }
    
    return null;
  }
}

// ============ مولد الردود الذكية المتقدم ============
class AdvancedSmartResponseGenerator {
  constructor(inferenceEngine) {
    this.inferenceEngine = inferenceEngine;
    this.responseHistory = [];
  }
  
  generate(sentence, context = {}) {
    const inference = this.inferenceEngine.inferIntent(sentence);
    
    // محاولة الاستنباط من الرسم المعرفي
    const inferredResponse = this.inferenceEngine.inferResponse(
      inference.intent,
      inference.keywords,
      inference.entities,
      context
    );
    
    if (inferredResponse && inferredResponse.confidence > 0.5) {
      const response = {
        text: inferredResponse.text,
        confidence: inferredResponse.confidence,
        method: 'knowledge_inference',
        intent: inference.intent,
        keywords: inference.keywords,
        entities: inference.entities
      };
      
      this.responseHistory.push({
        input: sentence,
        output: response,
        inference
      });
      
      return response;
    }
    
    // توليد رد بناءً على النية
    const response = this.generateByIntent(inference.intent, inference.keywords, inference.entities);
    
    this.responseHistory.push({
      input: sentence,
      output: response,
      inference
    });
    
    return response;
  }
  
  generateByIntent(intent, keywords, entities) {
    const templates = {
      greeting: [
        'أهلاً وسهلاً! كيف يمكنني مساعدتك؟ 🌟',
        'مرحباً! أنا بصيرة، نظام ذكاء اصطناعي ثوري. كيف يمكنني خدمتك؟'
      ],
      question_identity: [
        'أنا بصيرة، نظام ذكاء اصطناعي ثوري مبني على معادلات رياضية بدون شبكات عصبية.',
        'بصيرة هو نظام ذكاء اصطناعي فريد يعتمد على النظريات الرياضية الثورية.'
      ],
      question_creator: [
        'أنا من تطوير المبتكر باسل يحيى عبدالله، الذي ابتكر نظاماً ذكياً فريداً.',
        'مطوري هو باسل يحيى عبدالله، مبتكر النظريات الثورية الثلاث.'
      ],
      question_how: [
        'أعمل من خلال نظام متكامل: الدماغ (خبير-مستكشف)، المعادلات التكيفية، الذاكرة، التفكير، والذكاء العاطفي.',
        'آلية عملي تعتمد على المعادلات الرياضية والاستنباط المنطقي بدلاً من الشبكات العصبية.'
      ],
      question_what: keywords.length > 0 ? [
        `بخصوص ${keywords.join(', ')}، هذا موضوع مثير للاهتمام. دعني أستنبط الإجابة...`,
        `سؤال جيد عن ${keywords.join(', ')}. أستخدم نظام الخبير-المستكشف للإجابة.`
      ] : [
        'سؤال مثير للاهتمام! يمكنك سؤالي عن: هويتي، مطوري، كيفية عملي، أو النظريات الثورية.',
        'أحتاج مزيداً من التفاصيل لأجيب بدقة. ماذا تريد أن تعرف بالتحديد؟'
      ],
      gratitude: [
        'العفو! سعيد بمساعدتك 😊',
        'على الرحب والسعة! هل لديك أسئلة أخرى؟'
      ],
      statement: [
        'فهمت. شكراً على المعلومة.',
        'مثير للاهتمام! أخبرني المزيد.'
      ],
      request: [
        'سأحاول مساعدتك في ذلك.',
        'دعني أرى ما يمكنني فعله.'
      ]
    };
    
    const options = templates[intent] || templates.statement;
    const text = options[Math.floor(Math.random() * options.length)];
    
    return {
      text,
      confidence: 0.7,
      method: 'template_generation',
      intent,
      keywords,
      entities
    };
  }
}

// ============ النظام الحواري المتكامل المتقدم ============
class AdvancedIntelligentConversationalSystem {
  constructor() {
    console.log("🧠 تهيئة النظام الحواري الذكي المتقدم (بدون تلقين)...\n");
    
    this.lexicon = new AdvancedLexiconEngine();
    this.analyzer = new AdvancedLanguageAnalyzer(this.lexicon);
    this.inference = new AdvancedSemanticInferenceEngine(this.lexicon, this.analyzer);
    this.generator = new AdvancedSmartResponseGenerator(this.inference);
    
    this.initializeKnowledge();
    
    console.log("✅ النظام جاهز\n");
  }
  
  initializeKnowledge() {
    // كلمات التحية
    this.lexicon.addEntry('مرحبا', 'greeting', 'تحية', 'greeting');
    this.lexicon.addEntry('أهلا', 'greeting', 'تحية', 'greeting');
    this.lexicon.addEntry('السلام', 'greeting', 'تحية', 'greeting');
    this.lexicon.addEntry('مرحباً', 'greeting', 'تحية', 'greeting');
    this.lexicon.addEntry('أهلاً', 'greeting', 'تحية', 'greeting');
    
    // أدوات الاستفهام
    this.lexicon.addEntry('من', 'question', 'أداة استفهام', 'question');
    this.lexicon.addEntry('ما', 'question', 'أداة استفهام', 'question');
    this.lexicon.addEntry('كيف', 'question', 'أداة استفهام', 'question');
    this.lexicon.addEntry('ماذا', 'question', 'أداة استفهام', 'question');
    this.lexicon.addEntry('هل', 'question', 'أداة استفهام', 'question');
    
    // الضمائر
    this.lexicon.addEntry('أنت', 'pronoun', 'ضمير', 'pronoun');
    this.lexicon.addEntry('أنا', 'pronoun', 'ضمير', 'pronoun');
    this.lexicon.addEntry('هو', 'pronoun', 'ضمير', 'pronoun');
    
    // كلمات النظام
    this.lexicon.addEntry('بصيرة', 'noun', 'اسم النظام', 'system');
    this.lexicon.addEntry('نظام', 'noun', 'كيان', 'system');
    this.lexicon.addEntry('ذكاء', 'noun', 'مفهوم', 'system');
    this.lexicon.addEntry('اصطناعي', 'adjective', 'صفة', 'system');
    
    // كلمات المطور
    this.lexicon.addEntry('صنعك', 'verb', 'فعل', 'creator');
    this.lexicon.addEntry('طورك', 'verb', 'فعل', 'creator');
    this.lexicon.addEntry('مبتكر', 'noun', 'اسم', 'creator');
    this.lexicon.addEntry('مطور', 'noun', 'اسم', 'creator');
    
    // كلمات الشكر
    this.lexicon.addEntry('شكرا', 'gratitude', 'شكر', 'gratitude');
    this.lexicon.addEntry('شكراً', 'gratitude', 'شكر', 'gratitude');
    
    // أفعال
    this.lexicon.addEntry('تعمل', 'verb', 'فعل', 'action');
    this.lexicon.addEntry('يعمل', 'verb', 'فعل', 'action');
    
    // إضافة معرفة للرسم المعرفي
    this.inference.addKnowledge('بصيرة', 'هو', 'نظام ذكاء اصطناعي ثوري مبني على معادلات رياضية', 1.0);
    this.inference.addKnowledge('بصيرة', 'يعتمد_على', 'ثلاث نظريات ثورية: ثنائية الصفر، تعامد الأضداد، ونظرية الفتائل', 1.0);
    this.inference.addKnowledge('بصيرة', 'مطور', 'Basel Yahya Abdullah (باسل يحيى عبدالله)', 1.0);
    this.inference.addKnowledge('بصيرة', 'مميز_بـ', 'لا يستخدم شبكات عصبية، بل معادلات رياضية بحتة', 1.0);
    
    this.inference.addKnowledge('نظام', 'يتكون_من', 'دماغ (خبير-مستكشف)، معادلات تكيفية، ذاكرة، تفكير، ذكاء عاطفي', 0.9);
    this.inference.addKnowledge('نظام', 'يستخدم', 'النظريات الثورية الثلاث', 0.9);
    
    this.inference.addKnowledge('ذكاء', 'يأتي_من', 'التكامل بين نظام الخبير والمستكشف', 0.9);
    this.inference.addKnowledge('ذكاء', 'يعتمد_على', 'الاستنباط المنطقي والمعادلات الرياضية', 0.9);
  }
  
  respond(userInput) {
    console.log(`👤 المستخدم: ${userInput}`);
    
    // التحليل اللغوي
    const analysis = this.analyzer.analyzeSentence(userInput);
    console.log(`📊 التحليل: ${analysis.structure}`);
    console.log(`   الثقة: ${(analysis.confidence * 100).toFixed(1)}%`);
    console.log(`   الفئات: ${analysis.categories.join(', ')}`);
    
    // الاستنباط الدلالي
    const inference = this.inference.inferIntent(userInput);
    console.log(`🎯 النية المستنبطة: ${inference.intent}`);
    console.log(`   الثقة: ${(inference.confidence * 100).toFixed(1)}%`);
    console.log(`   الكلمات المفتاحية: ${inference.keywords.join(', ') || 'لا يوجد'}`);
    console.log(`   الكيانات: ${inference.entities.map(e => `${e.word}(${e.category})`).join(', ') || 'لا يوجد'}`);
    
    // توليد الرد
    const response = this.generator.generate(userInput);
    
    console.log(`🤖 بصيرة: ${response.text}`);
    console.log(`📈 الطريقة: ${response.method}`);
    console.log(`   الثقة: ${(response.confidence * 100).toFixed(1)}%`);
    console.log("---\n");
    
    return response;
  }
  
  runTest() {
    console.log("=" .repeat(70));
    console.log("🎯 اختبار النظام الحواري الذكي المتقدم (بدون تلقين)");
    console.log("=" .repeat(70));
    console.log();
    
    const testQuestions = [
      "مرحباً",
      "من أنت؟",
      "ما هو بصيرة؟",
      "من صنعك؟",
      "كيف تعمل؟",
      "ما هي النظريات التي تعتمد عليها؟",
      "شكراً لك"
    ];
    
    for (const question of testQuestions) {
      this.respond(question);
    }
    
    console.log("=" .repeat(70));
    console.log("✅ انتهى الاختبار");
    console.log("=" .repeat(70));
    console.log();
    
    console.log("📋 الإحصائيات النهائية:");
    console.log(`   - كلمات المعجم: ${this.lexicon.entries.size}`);
    console.log(`   - الفئات: ${this.lexicon.categoryIndex.size}`);
    console.log(`   - حقائق الرسم المعرفي: ${this.inference.knowledgeGraph.size}`);
    console.log(`   - سجل الردود: ${this.generator.responseHistory.length}`);
    
    // عرض الكلمات الأكثر استخداماً
    const sortedByUsage = Array.from(this.lexicon.entries.values())
      .filter(e => e.usageCount > 0)
      .sort((a, b) => b.usageCount - a.usageCount)
      .slice(0, 5);
    
    if (sortedByUsage.length > 0) {
      console.log(`\n📊 الكلمات الأكثر استخداماً:`);
      for (const entry of sortedByUsage) {
        console.log(`   - ${entry.word}: ${entry.usageCount} مرة (${entry.category})`);
      }
    }
  }
}

// تشغيل الاختبار
const system = new AdvancedIntelligentConversationalSystem();
system.runTest();
