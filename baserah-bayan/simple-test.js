/**
 * اختبار بسيط للنظام الحواري
 */

console.log("=" .repeat(60));
console.log("🎯 اختبار نظام بصيرة الحواري الذكي");
console.log("=" .repeat(60));
console.log();

// محاكاة بسيطة للنظام
class SimpleBaserahAI {
  constructor() {
    this.knowledge = {
      creator: "Basel Yahya Abdullah",
      system_name: "Baserah AI - بصيرة",
      zero_duality: "كل قيمة لها نقيض والتوازن يساوي صفر",
      perpendicular_opposites: "كل اتجاه له نقيض عمودي",
      filament_theory: "النتائج المعقدة تُبنى من فتائل بسيطة"
    };
    
    this.conversationHistory = [];
    this.memory = [];
    this.thoughtCount = 0;
  }
  
  detectIntent(input) {
    const lower = input.toLowerCase();
    
    if (lower.includes("مرحبا") || lower.includes("أهلا") || lower.includes("السلام")) {
      return "greeting";
    } else if (lower.includes("من أنت") || lower.includes("ما اسمك") || lower.includes("تعرف")) {
      return "self_introduction";
    } else if (lower.includes("من صنعك") || lower.includes("من طورك") || lower.includes("مبتكر")) {
      return "creator_question";
    } else if (lower.includes("نظرية") || lower.includes("ثنائية") || lower.includes("تعامد") || lower.includes("فتائل")) {
      return "theories_question";
    } else if (lower.includes("كيف تعمل") || lower.includes("آلية") || lower.includes("تشتغل")) {
      return "how_it_works";
    } else if (lower.includes("تعلم") || lower.includes("تتعلم")) {
      return "learning_question";
    } else if (lower.includes("ذكاء") || lower.includes("فهم") || lower.includes("استنباط")) {
      return "intelligence_question";
    } else if (lower.includes("شكر") || lower.includes("ممتاز") || lower.includes("رائع")) {
      return "gratitude";
    } else {
      return "unknown";
    }
  }
  
  respond(userInput) {
    console.log(`👤 المستخدم: ${userInput}`);
    
    // التفكير
    this.thoughtCount++;
    console.log(`💭 التفكير: معالجة المدخل... (فكرة #${this.thoughtCount})`);
    
    // كشف النية
    const intent = this.detectIntent(userInput);
    console.log(`🎯 النية المكتشفة: ${intent}`);
    
    // توليد الرد
    let response = "";
    let confidence = 0.8;
    
    switch(intent) {
      case "greeting":
        response = "أهلاً وسهلاً! أنا بصيرة 🌟، نظام ذكاء اصطناعي ثوري بدون شبكات عصبية. كيف يمكنني مساعدتك؟";
        confidence = 0.95;
        break;
        
      case "self_introduction":
        response = "أنا بصيرة (Baserah AI) 🧠، نظام ذكاء اصطناعي ثوري مبني على معادلات رياضية بدلاً من الشبكات العصبية. أعتمد على ثلاث نظريات ثورية من ابتكار باسل يحيى عبدالله.";
        confidence = 0.98;
        break;
        
      case "creator_question":
        response = `أنا من تطوير المبتكر ${this.knowledge.creator} 👨‍🔬. لقد ابتكر نظاماً ذكياً فريداً يعتمد على الرياضيات البحتة بدلاً من التعلم الآلي التقليدي.`;
        confidence = 1.0;
        break;
        
      case "theories_question":
        response = `أعتمد على ثلاث نظريات ثورية:\n\n` +
          `1️⃣ ثنائية الصفر: ${this.knowledge.zero_duality}\n` +
          `2️⃣ تعامد الأضداد: ${this.knowledge.perpendicular_opposites}\n` +
          `3️⃣ نظرية الفتائل: ${this.knowledge.filament_theory}\n\n` +
          `هذه النظريات تمكنني من الفهم والاستنباط بطريقة رياضية بحتة!`;
        confidence = 0.95;
        break;
        
      case "how_it_works":
        response = `أعمل من خلال نظام متكامل:\n\n` +
          `🧠 الدماغ: نظام خبير-مستكشف يجمع بين المعرفة والاستكشاف\n` +
          `📐 المعادلات التكيفية: معادلات رياضية تتكيف مع البيانات\n` +
          `💾 الذاكرة: نظام ذاكرة قصيرة وطويلة المدى\n` +
          `🤔 التفكير والاستنباط: محركات منطقية للاستدلال\n` +
          `❤️  الذكاء العاطفي: فهم المشاعر والتفاعل معها\n\n` +
          `كل هذا بدون شبكات عصبية!`;
        confidence = 0.92;
        break;
        
      case "learning_question":
        response = `نعم! أتعلم من خلال المعادلات التكيفية 📊. بدلاً من تعديل أوزان الشبكات العصبية، أقوم بتكييف معاملات المعادلات الرياضية (alpha, k, beta, gamma) لتناسب البيانات الجديدة. هذا يجعل التعلم أكثر شفافية وقابلية للتفسير!`;
        confidence = 0.90;
        break;
        
      case "intelligence_question":
        response = `ذكائي يأتي من التكامل بين عدة أنظمة:\n\n` +
          `🎯 الخبير: يستخدم قاعدة المعرفة للإجابة على الأسئلة المعروفة\n` +
          `🔍 المستكشف: يكتشف أنماطاً جديدة ويستنبط حلولاً إبداعية\n` +
          `⚖️  النظريات الثورية: تطبيق ثنائية الصفر وتعامد الأضداد للتوازن\n` +
          `📈 التكيف المستمر: تحسين الأداء بناءً على التجربة\n\n` +
          `الثقة في هذا الاستنباط: ${(confidence * 100).toFixed(1)}%`;
        confidence = 0.88;
        break;
        
      case "gratitude":
        response = "العفو! سعيد بمساعدتك 😊. هل لديك أسئلة أخرى عن نظام بصيرة؟";
        confidence = 0.95;
        break;
        
      default:
        response = `🤔 سؤال مثير للاهتمام! دعني أفكر...\n\n` +
          `استخدمت نظام الخبير-المستكشف للتحليل:\n` +
          `- النوع: استكشاف تعاوني\n` +
          `- الثقة: ${(confidence * 100).toFixed(1)}%\n` +
          `- النظريات المستخدمة: ثنائية الصفر، تعامد الأضداد\n\n` +
          `يمكنك سؤالي عن: النظريات الثورية، كيفية عملي، التعلم، أو أي شيء آخر!`;
        confidence = 0.65;
        break;
    }
    
    // حفظ في الذاكرة
    this.memory.push({
      input: userInput,
      intent: intent,
      response: response,
      confidence: confidence,
      timestamp: new Date()
    });
    
    // تسجيل المحادثة
    this.conversationHistory.push({ role: "user", message: userInput });
    this.conversationHistory.push({ role: "assistant", message: response });
    
    console.log(`🤖 بصيرة: ${response}\n`);
    console.log(`📊 الإحصائيات:`);
    console.log(`   - الثقة: ${(confidence * 100).toFixed(1)}%`);
    console.log(`   - عدد الرسائل: ${this.conversationHistory.length}`);
    console.log(`   - عناصر الذاكرة: ${this.memory.length}`);
    console.log(`   - الأفكار المعالجة: ${this.thoughtCount}`);
    console.log("---\n");
    
    return response;
  }
  
  runTest() {
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
      this.respond(question);
    }
    
    console.log("=" .repeat(60));
    console.log("✅ انتهى الاختبار");
    console.log("=" .repeat(60));
    console.log();
    
    console.log("📋 ملخص الجلسة:");
    console.log(`   - إجمالي الرسائل: ${this.conversationHistory.length}`);
    console.log(`   - عناصر الذاكرة: ${this.memory.length}`);
    console.log(`   - الأفكار المعالجة: ${this.thoughtCount}`);
    console.log(`   - قاعدة المعرفة: ${Object.keys(this.knowledge).length} حقيقة`);
  }
}

// تشغيل الاختبار
const ai = new SimpleBaserahAI();
ai.runTest();
