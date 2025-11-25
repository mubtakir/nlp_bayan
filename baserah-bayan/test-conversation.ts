/**
 * اختبار النظام الحواري الذكي - Intelligent Conversation Test
 */

import { BaserahIntegratedExpertExplorer } from "./brain/integrated-expert-explorer";
import { ConversationalCore } from "./conversational-ai/conversational-core";
import { MemorySystem } from "./memory/memory-system";
import { ReasoningEngine } from "./reasoning/reasoning-engine";
import { ThinkingEngine } from "./thinking/thinking-engine";
import { KnowledgeBase } from "./knowledge/knowledge-base";
import { EmotionDetector, Emotion } from "./emotional-intelligence/emotion-detector";
import { LearningEngine } from "./learning/learning-engine";

class IntelligentConversationalSystem {
  brain: BaserahIntegratedExpertExplorer;
  conversation: ConversationalCore;
  memory: MemorySystem;
  reasoning: ReasoningEngine;
  thinking: ThinkingEngine;
  knowledge: KnowledgeBase;
  emotion: EmotionDetector;
  learning: LearningEngine;
  
  constructor() {
    console.log("🧠 تهيئة نظام بصيرة الحواري الذكي...\n");
    
    this.brain = new BaserahIntegratedExpertExplorer("BaserahBrain", "conversation");
    this.conversation = new ConversationalCore("BaserahConversation");
    this.memory = new MemorySystem("BaserahMemory");
    this.reasoning = new ReasoningEngine("BaserahReasoning");
    this.thinking = new ThinkingEngine("BaserahThinking");
    this.knowledge = new KnowledgeBase("BaserahKnowledge");
    this.emotion = new EmotionDetector("BaserahEmotion");
    this.learning = new LearningEngine("BaserahLearning");
    
    this.initializeKnowledge();
    console.log("✅ النظام جاهز للحوار\n");
  }
  
  private initializeKnowledge(): void {
    // معرفة أساسية
    this.knowledge.addFact("creator", "Basel Yahya Abdullah");
    this.knowledge.addFact("system_name", "Baserah AI - بصيرة");
    this.knowledge.addFact("zero_duality", "كل قيمة لها نقيض والتوازن يساوي صفر");
    this.knowledge.addFact("perpendicular_opposites", "كل اتجاه له نقيض عمودي");
    this.knowledge.addFact("filament_theory", "النتائج المعقدة تُبنى من فتائل بسيطة");
    
    // قواعد استنباط
    this.reasoning.addRule(
      { type: "greeting" },
      { response: "أهلاً! أنا بصيرة، نظام ذكاء اصطناعي ثوري بدون شبكات عصبية" }
    );
    
    this.reasoning.addRule(
      { type: "question_about_creator" },
      { response: "أنا من تطوير المبتكر باسل يحيى عبدالله، مبني على نظريات رياضية ثورية" }
    );
    
    this.reasoning.addRule(
      { type: "question_about_theories" },
      { response: "أعتمد على ثلاث نظريات: ثنائية الصفر، تعامد الأضداد، ونظرية الفتائل" }
    );
  }
  
  intelligentRespond(userInput: string): string {
    console.log(`👤 المستخدم: ${userInput}`);
    
    // 1. التفكير في المدخل
    const thought = this.thinking.think({ input: userInput });
    console.log(`💭 التفكير: معالجة المدخل...`);
    
    // 2. كشف المشاعر
    const detectedEmotion = this.emotion.detect(userInput);
    console.log(`❤️  المشاعر المكتشفة: ${detectedEmotion}`);
    
    // 3. تحليل النية والاستنباط
    let intent = "general";
    let response = "";
    
    const lowerInput = userInput.toLowerCase();
    
    if (lowerInput.includes("مرحبا") || lowerInput.includes("أهلا") || lowerInput.includes("السلام")) {
      intent = "greeting";
      response = "أهلاً وسهلاً! أنا بصيرة 🌟، نظام ذكاء اصطناعي ثوري بدون شبكات عصبية. كيف يمكنني مساعدتك؟";
    }
    else if (lowerInput.includes("من أنت") || lowerInput.includes("ما اسمك") || lowerInput.includes("تعرف")) {
      intent = "self_introduction";
      response = "أنا بصيرة (Baserah AI) 🧠، نظام ذكاء اصطناعي ثوري مبني على معادلات رياضية بدلاً من الشبكات العصبية. أعتمد على ثلاث نظريات ثورية من ابتكار باسل يحيى عبدالله.";
    }
    else if (lowerInput.includes("من صنعك") || lowerInput.includes("من طورك") || lowerInput.includes("مبتكر")) {
      intent = "creator_question";
      const creator = this.knowledge.query("creator");
      response = `أنا من تطوير المبتكر ${creator} 👨‍🔬. لقد ابتكر نظاماً ذكياً فريداً يعتمد على الرياضيات البحتة بدلاً من التعلم الآلي التقليدي.`;
    }
    else if (lowerInput.includes("نظرية") || lowerInput.includes("ثنائية") || lowerInput.includes("تعامد") || lowerInput.includes("فتائل")) {
      intent = "theories_question";
      response = `أعتمد على ثلاث نظريات ثورية:\n\n` +
        `1️⃣ ثنائية الصفر: ${this.knowledge.query("zero_duality")}\n` +
        `2️⃣ تعامد الأضداد: ${this.knowledge.query("perpendicular_opposites")}\n` +
        `3️⃣ نظرية الفتائل: ${this.knowledge.query("filament_theory")}\n\n` +
        `هذه النظريات تمكنني من الفهم والاستنباط بطريقة رياضية بحتة!`;
    }
    else if (lowerInput.includes("كيف تعمل") || lowerInput.includes("آلية") || lowerInput.includes("تشتغل")) {
      intent = "how_it_works";
      response = `أعمل من خلال نظام متكامل:\n\n` +
        `🧠 الدماغ: نظام خبير-مستكشف يجمع بين المعرفة والاستكشاف\n` +
        `📐 المعادلات التكيفية: معادلات رياضية تتكيف مع البيانات\n` +
        `💾 الذاكرة: نظام ذاكرة قصيرة وطويلة المدى\n` +
        `🤔 التفكير والاستنباط: محركات منطقية للاستدلال\n` +
        `❤️  الذكاء العاطفي: فهم المشاعر والتفاعل معها\n\n` +
        `كل هذا بدون شبكات عصبية!`;
    }
    else if (lowerInput.includes("تعلم") || lowerInput.includes("تتعلم") || lowerInput.includes("learning")) {
      intent = "learning_question";
      response = `نعم! أتعلم من خلال المعادلات التكيفية 📊. بدلاً من تعديل أوزان الشبكات العصبية، أقوم بتكييف معاملات المعادلات الرياضية (alpha, k, beta, gamma) لتناسب البيانات الجديدة. هذا يجعل التعلم أكثر شفافية وقابلية للتفسير!`;
    }
    else if (lowerInput.includes("ذكاء") || lowerInput.includes("فهم") || lowerInput.includes("استنباط")) {
      intent = "intelligence_question";
      
      // استخدام نظام الخبير-المستكشف للاستنباط
      const decision = this.brain.solve({ question: userInput });
      
      response = `ذكائي يأتي من التكامل بين عدة أنظمة:\n\n` +
        `🎯 الخبير: يستخدم قاعدة المعرفة للإجابة على الأسئلة المعروفة\n` +
        `🔍 المستكشف: يكتشف أنماطاً جديدة ويستنبط حلولاً إبداعية\n` +
        `⚖️  النظريات الثورية: تطبيق ثنائية الصفر وتعامد الأضداد للتوازن\n` +
        `📈 التكيف المستمر: تحسين الأداء بناءً على التجربة\n\n` +
        `الثقة في هذا الاستنباط: ${(decision.confidence * 100).toFixed(1)}%`;
    }
    else if (lowerInput.includes("شكر") || lowerInput.includes("ممتاز") || lowerInput.includes("رائع")) {
      intent = "gratitude";
      response = "العفو! سعيد بمساعدتك 😊. هل لديك أسئلة أخرى عن نظام بصيرة؟";
    }
    else {
      // استخدام نظام الخبير-المستكشف للحالات غير المعروفة
      intent = "unknown";
      const decision = this.brain.solve({ question: userInput, context: "conversation" });
      
      response = `🤔 سؤال مثير للاهتمام! دعني أفكر...\n\n` +
        `استخدمت نظام الخبير-المستكشف للتحليل:\n` +
        `- النوع: ${decision.decisionType}\n` +
        `- الثقة: ${(decision.confidence * 100).toFixed(1)}%\n` +
        `- النظريات المستخدمة: ${decision.revolutionaryTheoriesUsed?.join(', ') || 'لا يوجد'}\n\n` +
        `يمكنك سؤالي عن: النظريات الثورية، كيفية عملي، التعلم، أو أي شيء آخر!`;
    }
    
    // 4. حفظ في الذاكرة
    this.memory.store(`conversation_${Date.now()}`, {
      input: userInput,
      intent: intent,
      response: response,
      emotion: detectedEmotion
    }, false);
    
    // 5. التعلم من التفاعل
    this.learning.learn([{
      input: { text: userInput, intent: intent },
      output: { response: response }
    }]);
    
    // 6. تسجيل في سجل المحادثة
    this.conversation.addMessage("user", userInput);
    this.conversation.addMessage("assistant", response);
    
    console.log(`🤖 بصيرة: ${response}\n`);
    console.log(`�� الإحصائيات:`);
    console.log(`   - النية المكتشفة: ${intent}`);
    console.log(`   - عدد الرسائل في الذاكرة: ${this.conversation.conversationHistory.length}`);
    console.log(`   - عناصر الذاكرة القصيرة: ${this.memory.shortTermMemory.length}`);
    console.log(`---\n`);
    
    return response;
  }
  
  runConversationTest(): void {
    console.log("=" .repeat(60));
    console.log("🎯 اختبار النظام الحواري الذكي لبصيرة");
    console.log("=" .repeat(60));
    console.log();
    
    const testQuestions = [
      "مرحباً",
      "من أنت؟",
      "من صنعك؟",
      "ما هي النظريات التي تعتمد عليها؟",
      "كيف تعمل؟",
      "هل تتعلم؟",
      "كيف تفهم وتستنبط؟",
      "شكراً لك"
    ];
    
    for (const question of testQuestions) {
      this.intelligentRespond(question);
    }
    
    console.log("=" .repeat(60));
    console.log("✅ انتهى الاختبار");
    console.log("=" .repeat(60));
    console.log();
    
    // عرض ملخص
    console.log("📋 ملخص الجلسة:");
    console.log(`   - إجمالي الرسائل: ${this.conversation.conversationHistory.length}`);
    console.log(`   - الذاكرة القصيرة: ${this.memory.shortTermMemory.length} عنصر`);
    console.log(`   - قاعدة المعرفة: ${this.knowledge.facts.size} حقيقة`);
    console.log(`   - قواعد الاستنباط: ${this.reasoning.rules.length} قاعدة`);
    console.log(`   - الأفكار المعالجة: ${this.thinking.thoughts.length} فكرة`);
  }
}

// تشغيل الاختبار
const system = new IntelligentConversationalSystem();
system.runConversationTest();
