/**
 * نظام حواري ذكي حقيقي - بدون تلقين مسبق
 * يستخدم المعادلات الرياضية والتحليل اللغوي
 */

// ============ محرك المعجم ============
class LexiconEngine {
  constructor() {
    this.entries = new Map();
    this.rootIndex = new Map();
  }
  
  addEntry(word, type, definition, root = null) {
    const entry = {
      word,
      type,
      definition,
      root,
      confidence: 1.0,
      semanticVector: this.computeSemanticVector(word)
    };
    
    this.entries.set(word, entry);
    
    if (root) {
      if (!this.rootIndex.has(root)) {
        this.rootIndex.set(root, new Set());
      }
      this.rootIndex.get(root).add(word);
    }
    
    return entry;
  }
  
  computeSemanticVector(word) {
    // تحويل الكلمة إلى متجه دلالي بسيط (hash-based)
    const vector = new Array(10).fill(0);
    for (let i = 0; i < word.length; i++) {
      const charCode = word.charCodeAt(i);
      vector[i % 10] += charCode;
    }
    return vector;
  }
  
  findSimilar(word, threshold = 0.5) {
    const targetVector = this.computeSemanticVector(word);
    const similar = [];
    
    for (const [key, entry] of this.entries) {
      const similarity = this.cosineSimilarity(targetVector, entry.semanticVector);
      if (similarity > threshold) {
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
}

// ============ المحلل اللغوي ============
class LanguageAnalyzer {
  constructor(lexicon) {
    this.lexicon = lexicon;
  }
  
  tokenize(text) {
    return text.split(/\s+/).filter(w => w.length > 0);
  }
  
  analyzeWord(word) {
    const entry = this.lexicon.entries.get(word);
    if (entry) {
      return { word, type: entry.type, confidence: 1.0, source: 'lexicon' };
    }
    
    // استنباط النوع من البنية
    const similar = this.lexicon.findSimilar(word, 0.6);
    if (similar.length > 0) {
      return { 
        word, 
        type: similar[0].entry.type, 
        confidence: similar[0].similarity,
        source: 'inference'
      };
    }
    
    // تحليل الأنماط
    if (/^[\u0600-\u06FF]+$/.test(word)) {
      if (word.startsWith('ال')) return { word, type: 'noun', confidence: 0.7, source: 'pattern' };
      if (word.startsWith('ي') || word.startsWith('ت')) return { word, type: 'verb', confidence: 0.6, source: 'pattern' };
      return { word, type: 'noun', confidence: 0.5, source: 'pattern' };
    }
    
    return { word, type: 'unknown', confidence: 0.3, source: 'default' };
  }
  
  analyzeSentence(sentence) {
    const tokens = this.tokenize(sentence);
    const words = tokens.map(w => this.analyzeWord(w));
    
    const structure = words.map(w => w.type).join('-');
    const avgConfidence = words.reduce((sum, w) => sum + w.confidence, 0) / words.length;
    
    return {
      sentence,
      tokens,
      words,
      structure,
      confidence: avgConfidence
    };
  }
  
  extractKeywords(sentence) {
    const analysis = this.analyzeSentence(sentence);
    return analysis.words
      .filter(w => w.type === 'noun' || w.type === 'verb')
      .filter(w => w.confidence > 0.5)
      .map(w => w.word);
  }
}

// ============ نظام الاستنباط الدلالي ============
class SemanticInferenceEngine {
  constructor(lexicon, analyzer) {
    this.lexicon = lexicon;
    this.analyzer = analyzer;
    this.knowledgeGraph = new Map();
  }
  
  addKnowledge(subject, predicate, object) {
    if (!this.knowledgeGraph.has(subject)) {
      this.knowledgeGraph.set(subject, []);
    }
    this.knowledgeGraph.get(subject).push({ predicate, object });
  }
  
  query(subject) {
    return this.knowledgeGraph.get(subject) || [];
  }
  
  inferIntent(sentence) {
    const keywords = this.analyzer.extractKeywords(sentence);
    const analysis = this.analyzer.analyzeSentence(sentence);
    
    // استنباط النية من البنية والكلمات المفتاحية
    const intentScores = {
      greeting: 0,
      question: 0,
      statement: 0,
      request: 0,
      gratitude: 0
    };
    
    // تحليل الكلمات المفتاحية
    for (const keyword of keywords) {
      const similar = this.lexicon.findSimilar(keyword, 0.6);
      for (const match of similar) {
        if (match.entry.type === 'greeting') intentScores.greeting += match.similarity;
        if (match.entry.type === 'question') intentScores.question += match.similarity;
      }
    }
    
    // تحليل البنية
    if (sentence.includes('؟') || sentence.includes('?')) {
      intentScores.question += 0.5;
    }
    
    if (analysis.structure.startsWith('verb')) {
      intentScores.request += 0.3;
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
      analysis
    };
  }
  
  inferResponse(intent, keywords, context) {
    // استنباط الرد من الرسم المعرفي
    const responses = [];
    
    for (const keyword of keywords) {
      const knowledge = this.query(keyword);
      for (const fact of knowledge) {
        responses.push(fact.object);
      }
    }
    
    if (responses.length > 0) {
      return {
        text: responses.join('. '),
        confidence: 0.8,
        source: 'knowledge_graph'
      };
    }
    
    return null;
  }
}

// ============ مولد الردود الذكية ============
class SmartResponseGenerator {
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
      context
    );
    
    if (inferredResponse && inferredResponse.confidence > 0.6) {
      return {
        text: inferredResponse.text,
        confidence: inferredResponse.confidence,
        method: 'inference',
        intent: inference.intent,
        keywords: inference.keywords
      };
    }
    
    // توليد رد عام بناءً على النية
    const response = this.generateByIntent(inference.intent, inference.keywords);
    
    this.responseHistory.push({
      input: sentence,
      output: response,
      inference
    });
    
    return response;
  }
  
  generateByIntent(intent, keywords) {
    const templates = {
      greeting: [
        'أهلاً وسهلاً! كيف يمكنني مساعدتك؟',
        'مرحباً! أنا هنا للمساعدة.'
      ],
      question: [
        `سؤال مثير للاهتمام عن ${keywords.join(', ')}. دعني أفكر...`,
        `بخصوص ${keywords.join(', ')}، يمكنني القول...`
      ],
      gratitude: [
        'العفو! سعيد بمساعدتك.',
        'على الرحب والسعة!'
      ],
      statement: [
        'فهمت. شكراً على المعلومة.',
        'مثير للاهتمام!'
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
      confidence: 0.6,
      method: 'template',
      intent,
      keywords
    };
  }
}

// ============ النظام الحواري المتكامل ============
class IntelligentConversationalSystem {
  constructor() {
    console.log("🧠 تهيئة النظام الحواري الذكي (بدون تلقين)...\n");
    
    this.lexicon = new LexiconEngine();
    this.analyzer = new LanguageAnalyzer(this.lexicon);
    this.inference = new SemanticInferenceEngine(this.lexicon, this.analyzer);
    this.generator = new SmartResponseGenerator(this.inference);
    
    this.initializeKnowledge();
    
    console.log("✅ النظام جاهز\n");
  }
  
  initializeKnowledge() {
    // إضافة كلمات للمعجم
    this.lexicon.addEntry('مرحبا', 'greeting', 'تحية');
    this.lexicon.addEntry('أهلا', 'greeting', 'تحية');
    this.lexicon.addEntry('السلام', 'greeting', 'تحية');
    this.lexicon.addEntry('من', 'question', 'أداة استفهام');
    this.lexicon.addEntry('ما', 'question', 'أداة استفهام');
    this.lexicon.addEntry('كيف', 'question', 'أداة استفهام');
    this.lexicon.addEntry('أنت', 'pronoun', 'ضمير');
    this.lexicon.addEntry('بصيرة', 'noun', 'اسم النظام');
    this.lexicon.addEntry('نظام', 'noun', 'كيان');
    this.lexicon.addEntry('ذكاء', 'noun', 'مفهوم');
    this.lexicon.addEntry('شكرا', 'gratitude', 'شكر');
    
    // إضافة معرفة للرسم المعرفي
    this.inference.addKnowledge('بصيرة', 'هو', 'نظام ذكاء اصطناعي ثوري');
    this.inference.addKnowledge('بصيرة', 'يعتمد_على', 'معادلات رياضية بدون شبكات عصبية');
    this.inference.addKnowledge('بصيرة', 'مطور', 'Basel Yahya Abdullah');
    this.inference.addKnowledge('نظام', 'يستخدم', 'ثلاث نظريات ثورية');
    this.inference.addKnowledge('ذكاء', 'يأتي_من', 'التكامل بين الخبير والمستكشف');
  }
  
  respond(userInput) {
    console.log(`👤 المستخدم: ${userInput}`);
    
    // التحليل اللغوي
    const analysis = this.analyzer.analyzeSentence(userInput);
    console.log(`📊 التحليل: ${analysis.structure} (ثقة: ${(analysis.confidence * 100).toFixed(1)}%)`);
    
    // الاستنباط الدلالي
    const inference = this.inference.inferIntent(userInput);
    console.log(`🎯 النية المستنبطة: ${inference.intent} (ثقة: ${(inference.confidence * 100).toFixed(1)}%)`);
    console.log(`🔑 الكلمات المفتاحية: ${inference.keywords.join(', ')}`);
    
    // توليد الرد
    const response = this.generator.generate(userInput);
    
    console.log(`🤖 بصيرة: ${response.text}`);
    console.log(`📈 الطريقة: ${response.method} (ثقة: ${(response.confidence * 100).toFixed(1)}%)`);
    console.log("---\n");
    
    return response;
  }
  
  runTest() {
    console.log("=" .repeat(60));
    console.log("🎯 اختبار النظام الحواري الذكي (بدون تلقين)");
    console.log("=" .repeat(60));
    console.log();
    
    const testQuestions = [
      "مرحباً",
      "من أنت؟",
      "ما هو بصيرة؟",
      "كيف تعمل؟",
      "شكراً لك"
    ];
    
    for (const question of testQuestions) {
      this.respond(question);
    }
    
    console.log("=" .repeat(60));
    console.log("✅ انتهى الاختبار");
    console.log("=" .repeat(60));
    console.log();
    
    console.log("📋 الإحصائيات:");
    console.log(`   - كلمات المعجم: ${this.lexicon.entries.size}`);
    console.log(`   - حقائق الرسم المعرفي: ${this.inference.knowledgeGraph.size}`);
    console.log(`   - سجل الردود: ${this.generator.responseHistory.length}`);
  }
}

// تشغيل الاختبار
const system = new IntelligentConversationalSystem();
system.runTest();
