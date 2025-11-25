/**
 * عرض تفاعلي لنظام بصيرة الذكي
 * يستخدم جميع الوحدات: الدماغ، الذاكرة، التفكير، الاستنباط، التعلم
 */

import { BaserahIntegratedExpertExplorer } from "./brain/integrated-expert-explorer";
import { ConversationalCore } from "./conversational-ai/conversational-core";
import { MemorySystem } from "./memory/memory-system";
import { ReasoningEngine } from "./reasoning/reasoning-engine";
import { ThinkingEngine } from "./thinking/thinking-engine";
import { KnowledgeBase } from "./knowledge/knowledge-base";
import { EmotionDetector, Emotion } from "./emotional-intelligence/emotion-detector";
import { LearningEngine } from "./learning/learning-engine";

class BaserahInteractiveSystem {
  brain: BaserahIntegratedExpertExplorer;
  conversation: ConversationalCore;
  memory: MemorySystem;
  reasoning: ReasoningEngine;
  thinking: ThinkingEngine;
  knowledge: KnowledgeBase;
  emotion: EmotionDetector;
  learning: LearningEngine;
  
  conversationCount: number = 0;
  
  constructor() {
    console.log("🚀 تهيئة نظام بصيرة التفاعلي الكامل...\n");
    
    this.brain = new BaserahIntegratedExpertExplorer("BaserahBrain", "conversation");
    this.conversation = new ConversationalCore("BaserahConversation");
    this.memory = new MemorySystem("BaserahMemory");
    this.reasoning = new ReasoningEngine("BaserahReasoning");
    this.thinking = new ThinkingEngine("BaserahThinking");
    this.knowledge = new KnowledgeBase("BaserahKnowledge");
    this.emotion = new EmotionDetector("BaserahEmotion");
    this.learning = new LearningEngine("BaserahLearning");
    
    this.initializeSystem();
    
    console.log("✅ النظام جاهز للتفاعل!\n");
  }
  
  private initializeSystem(): void {
    // قاعدة المعرفة
    this.knowledge.addFact("name", "بصيرة - Baserah AI");
    this.knowledge.addFact("creator", "Basel Yahya Abdullah - باسل يحيى عبدالله");
    this.knowledge.addFact("theory_1", "ثنائية الصفر - Zero Duality");
    this.knowledge.addFact("theory_2", "تعامد الأضداد - Perpendicular Opposites");
    this.knowledge.addFact("theory_3", "نظرية الفتائل - Filament Theory");
    this.knowledge.addFact("unique", "لا يستخدم شبكات عصبية، بل معادلات رياضية");
    
    // قواعد الاستنباط
    this.reasoning.addRule(
      { type: "greeting" },
      { response: "greeting_response", emotion: "friendly" }
    );
    
    this.reasoning.addRule(
      { type: "question", topic: "identity" },
      { response: "identity_response", useKnowledge: true }
    );
    
    this.reasoning.addRule(
      { type: "question", topic: "theories" },
      { response: "theories_response", useKnowledge: true }
    );
    
    // حفظ في الذاكرة طويلة المدى
    this.memory.store("system_purpose", "مساعدة المستخدمين بذكاء واستنباط", true);
    this.memory.store("conversation_style", "ودود ومفيد", true);
  }
  
  analyzeInput(input: string): any {
    const lower = input.toLowerCase();
    
    let type = "unknown";
    let topic = "general";
    let keywords: string[] = [];
    
    // تحليل النوع
    if (lower.includes("مرحبا") || lower.includes("أهلا") || lower.includes("السلام")) {
      type = "greeting";
    } else if (lower.includes("؟") || lower.includes("?") || 
               lower.includes("من") || lower.includes("ما") || lower.includes("كيف")) {
      type = "question";
      
      // تحديد الموضوع
      if (lower.includes("من أنت") || lower.includes("ما اسمك") || lower.includes("بصيرة")) {
        topic = "identity";
        keywords = ["identity", "name"];
      } else if (lower.includes("نظرية") || lower.includes("ثنائية") || 
                 lower.includes("تعامد") || lower.includes("فتائل")) {
        topic = "theories";
        keywords = ["theories", "revolutionary"];
      } else if (lower.includes("كيف تعمل") || lower.includes("آلية")) {
        topic = "mechanism";
        keywords = ["mechanism", "how"];
      } else if (lower.includes("تعلم") || lower.includes("تتعلم")) {
        topic = "learning";
        keywords = ["learning", "adaptive"];
      } else if (lower.includes("ذكاء") || lower.includes("فهم") || lower.includes("استنباط")) {
        topic = "intelligence";
        keywords = ["intelligence", "inference"];
      } else if (lower.includes("من صنعك") || lower.includes("مطور") || lower.includes("مبتكر")) {
        topic = "creator";
        keywords = ["creator"];
      }
    } else if (lower.includes("شكر") || lower.includes("ممتاز") || lower.includes("رائع")) {
      type = "gratitude";
    } else {
      type = "statement";
    }
    
    return { type, topic, keywords, originalInput: input };
  }
  
  generateResponse(analysis: any, brainDecision: any): string {
    const { type, topic, keywords } = analysis;
    
    // استخدام قواعد الاستنباط
    const inference = this.reasoning.infer({ type, topic });
    
    let response = "";
    
    if (type === "greeting") {
      response = "أهلاً وسهلاً! 🌟 أنا بصيرة، نظام ذكاء اصطناعي ثوري. كيف يمكنني مساعدتك؟";
    } else if (type === "question") {
      if (topic === "identity") {
        const name = this.knowledge.query("name");
        const unique = this.knowledge.query("unique");
        response = `أنا ${name}، نظام ذكاء اصطناعي فريد. ${unique}. أعتمد على ثلاث نظريات رياضية ثورية.`;
      } else if (topic === "creator") {
        const creator = this.knowledge.query("creator");
        response = `أنا من تطوير المبتكر ${creator}. لقد ابتكر نظاماً ذكياً يعتمد على الرياضيات البحتة بدلاً من الشبكات العصبية.`;
      } else if (topic === "theories") {
        const t1 = this.knowledge.query("theory_1");
        const t2 = this.knowledge.query("theory_2");
        const t3 = this.knowledge.query("theory_3");
        response = `أعتمد على ثلاث نظريات ثورية:\n\n` +
          `1️⃣ ${t1}: كل قيمة لها نقيض والتوازن يساوي صفر\n` +
          `2️⃣ ${t2}: كل اتجاه له نقيض عمودي\n` +
          `3️⃣ ${t3}: النتائج المعقدة تُبنى من فتائل بسيطة\n\n` +
          `هذه النظريات تمكنني من الفهم والاستنباط الرياضي!`;
      } else if (topic === "mechanism") {
        response = `أعمل من خلال نظام متكامل:\n\n` +
          `🧠 الدماغ: نظام خبير-مستكشف (Expert-Explorer)\n` +
          `📐 المعادلات التكيفية: معادلات رياضية تتكيف مع البيانات\n` +
          `💾 الذاكرة: قصيرة وطويلة المدى\n` +
          `🤔 التفكير: معالجة الأفكار والاستنباط\n` +
          `📚 قاعدة المعرفة: حقائق وقواعد\n` +
          `❤️  الذكاء العاطفي: فهم المشاعر\n` +
          `📊 التعلم: تكيف مستمر\n\n` +
          `الثقة في هذا القرار: ${(brainDecision.confidence * 100).toFixed(1)}%`;
      } else if (topic === "learning") {
        response = `نعم! أتعلم من خلال المعادلات التكيفية 📊.\n\n` +
          `بدلاً من تعديل أوزان الشبكات العصبية، أقوم بتكييف معاملات المعادلات الرياضية:\n` +
          `- Alpha (α): معاملات السيجمويد\n` +
          `- K: حدة الانحناء\n` +
          `- Beta (β): الميل الخطي\n` +
          `- Gamma (γ): الإزاحة\n\n` +
          `هذا يجعل التعلم شفافاً وقابلاً للتفسير!`;
      } else if (topic === "intelligence") {
        response = `ذكائي يأتي من التكامل بين:\n\n` +
          `🎯 الخبير: يستخدم المعرفة المخزنة\n` +
          `🔍 المستكشف: يكتشف أنماطاً جديدة\n` +
          `⚖️  النظريات الثورية: للتوازن والاستنباط\n` +
          `🧮 المعادلات الرياضية: للحسابات الدقيقة\n` +
          `📈 التعلم التكيفي: للتحسين المستمر\n\n` +
          `استخدمت نظام الخبير-المستكشف:\n` +
          `- النوع: ${brainDecision.decisionType}\n` +
          `- الثقة: ${(brainDecision.confidence * 100).toFixed(1)}%\n` +
          `- النظريات: ${brainDecision.revolutionaryTheoriesUsed?.join(', ') || 'متعددة'}`;
      } else {
        response = `سؤال مثير للاهتمام! 🤔\n\n` +
          `استخدمت نظام الخبير-المستكشف للتحليل:\n` +
          `- النوع: ${brainDecision.decisionType}\n` +
          `- الثقة: ${(brainDecision.confidence * 100).toFixed(1)}%\n` +
          `- الكلمات المفتاحية: ${keywords.join(', ') || 'لا يوجد'}\n\n` +
          `يمكنك سؤالي عن: هويتي، مطوري، النظريات، كيفية عملي، التعلم، أو الذكاء.`;
      }
    } else if (type === "gratitude") {
      response = "العفو! 😊 سعيد بمساعدتك. هل لديك أسئلة أخرى؟";
    } else {
      response = "فهمت. شكراً على المعلومة! هل يمكنني مساعدتك في شيء آخر؟";
    }
    
    return response;
  }
  
  interact(userInput: string): void {
    this.conversationCount++;
    
    console.log(`\n${"=".repeat(70)}`);
    console.log(`💬 محادثة #${this.conversationCount}`);
    console.log(`${"=".repeat(70)}\n`);
    
    console.log(`👤 المستخدم: ${userInput}\n`);
    
    // 1. التفكير
    const thought = this.thinking.think({ input: userInput, timestamp: new Date() });
    console.log(`💭 التفكير: معالجة المدخل... (فكرة #${this.thinking.thoughts.length})`);
    
    // 2. كشف المشاعر
    const emotion = this.emotion.detect(userInput);
    console.log(`❤️  المشاعر: ${emotion}`);
    
    // 3. التحليل
    const analysis = this.analyzeInput(userInput);
    console.log(`📊 التحليل:`);
    console.log(`   - النوع: ${analysis.type}`);
    console.log(`   - الموضوع: ${analysis.topic}`);
    console.log(`   - الكلمات المفتاحية: ${analysis.keywords.join(', ') || 'لا يوجد'}`);
    
    // 4. استخدام الدماغ (خبير-مستكشف)
    const brainDecision = this.brain.solve({
      input: userInput,
      analysis: analysis,
      emotion: emotion
    });
    console.log(`�� قرار الدماغ:`);
    console.log(`   - النوع: ${brainDecision.decisionType}`);
    console.log(`   - الثقة: ${(brainDecision.confidence * 100).toFixed(1)}%`);
    console.log(`   - النظريات المستخدمة: ${brainDecision.revolutionaryTheoriesUsed?.join(', ') || 'لا يوجد'}`);
    
    // 5. توليد الرد
    const response = this.generateResponse(analysis, brainDecision);
    
    console.log(`\n🤖 بصيرة:\n${response}\n`);
    
    // 6. حفظ في الذاكرة
    this.memory.store(`conversation_${this.conversationCount}`, {
      input: userInput,
      analysis: analysis,
      emotion: emotion,
      brainDecision: brainDecision,
      response: response,
      timestamp: new Date()
    }, false);
    
    // 7. التعلم
    this.learning.learn([{
      input: { text: userInput, analysis: analysis },
      output: { response: response, confidence: brainDecision.confidence }
    }]);
    
    // 8. تسجيل المحادثة
    this.conversation.addMessage("user", userInput);
    this.conversation.addMessage("assistant", response);
    
    // 9. الإحصائيات
    console.log(`📈 الإحصائيات:`);
    console.log(`   - إجمالي المحادثات: ${this.conversationCount}`);
    console.log(`   - الرسائل: ${this.conversation.conversationHistory.length}`);
    console.log(`   - الذاكرة القصيرة: ${this.memory.shortTermMemory.length} عنصر`);
    console.log(`   - الأفكار: ${this.thinking.thoughts.length}`);
    console.log(`   - بيانات التعلم: ${this.learning.trainingData.length}`);
  }
  
  runDemo(): void {
    console.log("╔" + "═".repeat(68) + "╗");
    console.log("║" + " ".repeat(15) + "🌟 عرض تفاعلي لنظام بصيرة الذكي 🌟" + " ".repeat(15) + "║");
    console.log("╚" + "═".repeat(68) + "╝\n");
    
    const demoQuestions = [
      "مرحباً",
      "من أنت؟",
      "من صنعك؟",
      "ما هي النظريات التي تعتمد عليها؟",
      "كيف تعمل؟",
      "هل تتعلم؟",
      "كيف تفهم وتستنبط؟",
      "شكراً لك"
    ];
    
    for (const question of demoQuestions) {
      this.interact(question);
    }
    
    console.log("\n" + "╔" + "═".repeat(68) + "╗");
    console.log("║" + " ".repeat(25) + "✅ انتهى العرض" + " ".repeat(25) + "║");
    console.log("╚" + "═".repeat(68) + "╝\n");
    
    this.showFinalStats();
  }
  
  showFinalStats(): void {
    console.log("📊 الإحصائيات النهائية:\n");
    console.log(`   🔢 إجمالي المحادثات: ${this.conversationCount}`);
    console.log(`   💬 إجمالي الرسائل: ${this.conversation.conversationHistory.length}`);
    console.log(`   💾 الذاكرة القصيرة: ${this.memory.shortTermMemory.length} عنصر`);
    console.log(`   💾 الذاكرة الطويلة: ${this.memory.longTermMemory.length} عنصر`);
    console.log(`   🤔 الأفكار المعالجة: ${this.thinking.thoughts.length}`);
    console.log(`   📚 قاعدة المعرفة: ${this.knowledge.facts.size} حقيقة`);
    console.log(`   📏 قواعد الاستنباط: ${this.reasoning.rules.length} قاعدة`);
    console.log(`   📊 بيانات التعلم: ${this.learning.trainingData.length} عينة`);
    
    console.log("\n🎯 الوحدات المستخدمة:");
    console.log("   ✅ الدماغ (خبير-مستكشف)");
    console.log("   ✅ المحادثة");
    console.log("   ✅ الذاكرة");
    console.log("   ✅ التفكير");
    console.log("   ✅ الاستنباط");
    console.log("   ✅ قاعدة المعرفة");
    console.log("   ✅ الذكاء العاطفي");
    console.log("   ✅ التعلم");
  }
}

// تشغيل العرض
const system = new BaserahInteractiveSystem();
system.runDemo();
