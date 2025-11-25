// ========================================
// بصيرة AI - محرك الذكاء الحواري الحقيقي
// نظام توليد لغوي ذكي بدون شبكات عصبية
// ========================================

// ========================================
// 1. محلل النوايا (Intent Analyzer)
// ========================================
class IntentAnalyzer {
    constructor() {
        // قاعدة بيانات الكلمات المفتاحية للنوايا
        this.intentKeywords = {
            QUESTION: ['ما', 'من', 'متى', 'أين', 'لماذا', 'كيف', 'هل', 'كم', 'أي', 'ماذا', '؟'],
            GREETING: ['مرحبا', 'مرحباً', 'السلام', 'أهلا', 'أهلاً', 'صباح', 'مساء', 'هلا', 'هاي'],
            FAREWELL: ['وداع', 'وداعا', 'وداعاً', 'باي', 'مع السلامة', 'إلى اللقاء', 'سلام'],
            THANKS: ['شكرا', 'شكراً', 'ممتن', 'أشكرك', 'متشكر', 'جزاك الله'],
            APOLOGY: ['آسف', 'أعتذر', 'معذرة', 'عفوا', 'عفواً', 'سامحني'],
            CONFIRMATION: ['نعم', 'أجل', 'صحيح', 'بالتأكيد', 'طبعا', 'طبعاً', 'موافق', 'حسنا', 'حسناً'],
            DENIAL: ['لا', 'كلا', 'أبدا', 'أبداً', 'مستحيل', 'غير صحيح', 'خطأ'],
            REQUEST: ['أريد', 'أرجو', 'من فضلك', 'لو سمحت', 'ممكن', 'هل يمكن', 'أطلب'],
            COMPLAINT: ['مشكلة', 'خطأ', 'عطل', 'لا يعمل', 'سيء', 'سيئ', 'غير راض'],
            PRAISE: ['رائع', 'ممتاز', 'جيد', 'عظيم', 'مذهل', 'جميل', 'أحسنت'],
            SUGGESTION: ['أقترح', 'اقتراح', 'ما رأيك', 'يمكن', 'لو', 'أفضل'],
            COMMAND: ['افعل', 'قم', 'نفذ', 'اعمل', 'أنجز', 'اكتب', 'اشرح']
        };

        // أنواع الأسئلة
        this.questionTypes = {
            WHAT: ['ما', 'ماذا'],
            WHO: ['من'],
            WHEN: ['متى'],
            WHERE: ['أين'],
            WHY: ['لماذا', 'لم'],
            HOW: ['كيف'],
            YES_NO: ['هل'],
            HOW_MANY: ['كم'],
            WHICH: ['أي']
        };
    }

    analyze(text) {
        const normalizedText = text.toLowerCase().trim();
        
        // كشف النية
        let intent = 'OTHER';
        let maxScore = 0;
        
        for (const [intentType, keywords] of Object.entries(this.intentKeywords)) {
            let score = 0;
            for (const keyword of keywords) {
                if (normalizedText.includes(keyword)) {
                    score++;
                }
            }
            if (score > maxScore) {
                maxScore = score;
                intent = intentType;
            }
        }

        // كشف نوع السؤال
        let questionType = null;
        if (intent === 'QUESTION') {
            for (const [qType, keywords] of Object.entries(this.questionTypes)) {
                for (const keyword of keywords) {
                    if (normalizedText.includes(keyword)) {
                        questionType = qType;
                        break;
                    }
                }
                if (questionType) break;
            }
        }

        // استخراج الكيانات (بسيط)
        const entities = this.extractEntities(text);

        return {
            intent: intent,
            questionType: questionType,
            entities: entities,
            confidence: maxScore > 0 ? Math.min(maxScore * 0.3, 1.0) : 0.5
        };
    }

    extractEntities(text) {
        const entities = [];
        
        // كشف الأرقام
        const numbers = text.match(/\d+/g);
        if (numbers) {
            numbers.forEach(num => entities.push({ type: 'NUMBER', value: num }));
        }

        // كشف الكلمات المهمة (أسماء محتملة)
        const words = text.split(/\s+/);
        const capitalizedWords = words.filter(w => /^[A-Z]/.test(w) || /^[ا-ي]{3,}$/.test(w));
        capitalizedWords.forEach(word => {
            if (word.length > 2) {
                entities.push({ type: 'CONCEPT', value: word });
            }
        });

        return entities;
    }
}

// ========================================
// 2. نظام الفهم العميق (Deep Understanding)
// ========================================
class DeepUnderstanding {
    constructor() {
        // قاعدة بيانات المشاعر
        this.emotionKeywords = {
            JOY: ['سعيد', 'فرح', 'مسرور', 'رائع', 'ممتاز', 'جميل', '😊', '😃', '🎉'],
            SADNESS: ['حزين', 'كئيب', 'مكتئب', 'أسف', 'حزن', '😢', '😞'],
            ANGER: ['غاضب', 'غضب', 'منزعج', 'مستاء', 'غضبان', '😠', '😡'],
            FEAR: ['خائف', 'خوف', 'قلق', 'مرعوب', 'متوتر', '😨', '😰'],
            SURPRISE: ['مفاجأة', 'مندهش', 'متفاجئ', 'عجيب', '😲', '😮'],
            LOVE: ['حب', 'أحب', 'عشق', 'محبة', '❤️', '😍'],
            HOPE: ['أمل', 'آمل', 'متفائل', 'تفاؤل', '🌟'],
            ANXIETY: ['قلق', 'قلقان', 'متوتر', 'توتر', 'مضطرب']
        };

        // قاعدة بيانات النبرات
        this.toneKeywords = {
            POLITE: ['من فضلك', 'لو سمحت', 'أرجو', 'تكرماً', 'شكراً'],
            FRIENDLY: ['صديقي', 'حبيبي', 'عزيزي', '😊', '🙂'],
            FORMAL: ['سيدي', 'حضرتك', 'سيادتك', 'المحترم'],
            INFORMAL: ['يا زلمة', 'يا رجل', 'يا أخي'],
            SARCASTIC: ['طبعاً', 'أكيد', 'واضح', 'بالتأكيد'],
            SERIOUS: ['مهم', 'خطير', 'جاد', 'ضروري'],
            ENTHUSIASTIC: ['رائع', 'مذهل', 'عظيم', '!', '🔥'],
            CALM: ['هادئ', 'بهدوء', 'بروية', 'بتأني']
        };
    }

    analyze(text, intentAnalysis) {
        const normalizedText = text.toLowerCase();

        // تحليل المشاعر
        const emotion = this.detectEmotion(normalizedText);
        
        // تحليل النبرة
        const tone = this.detectTone(normalizedText);

        // استخراج السياق
        const context = this.extractContext(text, intentAnalysis);

        // كشف النوايا الضمنية
        const implicitIntent = this.detectImplicitIntent(text, intentAnalysis);

        return {
            emotion: emotion,
            tone: tone,
            context: context,
            implicitIntent: implicitIntent
        };
    }

    detectEmotion(text) {
        let maxScore = 0;
        let detectedEmotion = 'NEUTRAL';

        for (const [emotion, keywords] of Object.entries(this.emotionKeywords)) {
            let score = 0;
            for (const keyword of keywords) {
                if (text.includes(keyword)) {
                    score++;
                }
            }
            if (score > maxScore) {
                maxScore = score;
                detectedEmotion = emotion;
            }
        }

        return {
            type: detectedEmotion,
            intensity: Math.min(maxScore * 0.4, 1.0)
        };
    }

    detectTone(text) {
        let maxScore = 0;
        let detectedTone = 'NEUTRAL';

        for (const [tone, keywords] of Object.entries(this.toneKeywords)) {
            let score = 0;
            for (const keyword of keywords) {
                if (text.includes(keyword)) {
                    score++;
                }
            }
            if (score > maxScore) {
                maxScore = score;
                detectedTone = tone;
            }
        }

        return detectedTone;
    }

    extractContext(text, intentAnalysis) {
        // استخراج الموضوع الرئيسي
        const topics = [];
        
        if (text.includes('بصيرة') || text.includes('النظام')) {
            topics.push('SYSTEM');
        }
        if (text.includes('معادلة') || text.includes('رياضيات')) {
            topics.push('MATHEMATICS');
        }
        if (text.includes('ذكاء') || text.includes('AI')) {
            topics.push('AI');
        }
        if (text.includes('لغة') || text.includes('كلام')) {
            topics.push('LANGUAGE');
        }

        return {
            mainTopic: topics[0] || 'GENERAL',
            relatedTopics: topics.slice(1)
        };
    }

    detectImplicitIntent(text, intentAnalysis) {
        // كشف النوايا الضمنية
        const implicit = [];

        if (intentAnalysis.intent === 'QUESTION' && text.includes('كيف')) {
            implicit.push('SEEKING_EXPLANATION');
        }
        if (intentAnalysis.intent === 'COMPLAINT') {
            implicit.push('SEEKING_HELP');
        }
        if (text.includes('أريد') || text.includes('أحتاج')) {
            implicit.push('HAS_NEED');
        }

        return implicit;
    }
}

// ========================================
// 3. مخطط الاستجابة (Response Planner)
// ========================================
class ResponsePlanner {
    constructor() {
        this.strategies = {
            DIRECT: 'مباشر',
            DETAILED: 'تفصيلي',
            BRIEF: 'موجز',
            INTERACTIVE: 'تفاعلي',
            EDUCATIONAL: 'تعليمي',
            EMPATHETIC: 'تعاطفي'
        };
    }

    plan(intentAnalysis, understanding, settings) {
        // تحديد نوع الاستجابة
        const responseType = this.determineResponseType(intentAnalysis);
        
        // اختيار الاستراتيجية
        const strategy = this.selectStrategy(intentAnalysis, understanding, settings);
        
        // بناء مكونات الاستجابة
        const components = this.buildComponents(intentAnalysis, understanding, responseType);

        return {
            responseType: responseType,
            strategy: strategy,
            components: components
        };
    }

    determineResponseType(intentAnalysis) {
        const intentToResponse = {
            QUESTION: 'ANSWER',
            GREETING: 'GREETING',
            FAREWELL: 'FAREWELL',
            THANKS: 'ACKNOWLEDGMENT',
            APOLOGY: 'ACCEPTANCE',
            REQUEST: 'SUGGESTION',
            COMPLAINT: 'APOLOGY',
            PRAISE: 'THANKS',
            CONFIRMATION: 'CONFIRMATION',
            DENIAL: 'CLARIFICATION'
        };

        return intentToResponse[intentAnalysis.intent] || 'INFORMATION';
    }

    selectStrategy(intentAnalysis, understanding, settings) {
        // اختيار الاستراتيجية بناءً على السياق
        if (understanding.emotion.type === 'SADNESS' || understanding.emotion.type === 'ANGER') {
            return 'EMPATHETIC';
        }
        if (intentAnalysis.intent === 'QUESTION') {
            return settings.detailLevel === 'DETAILED' ? 'DETAILED' : 'EDUCATIONAL';
        }
        if (understanding.tone === 'FORMAL') {
            return 'DIRECT';
        }
        
        return 'INTERACTIVE';
    }

    buildComponents(intentAnalysis, understanding, responseType) {
        const components = {
            greeting: null,
            mainContent: null,
            details: null,
            examples: null,
            closing: null
        };

        // إضافة تحية إذا كانت النبرة ودية
        if (understanding.tone === 'FRIENDLY' || understanding.tone === 'POLITE') {
            components.greeting = this.generateGreeting(understanding.emotion);
        }

        // المحتوى الرئيسي (سيتم ملؤه بواسطة مولد النصوص)
        components.mainContent = { type: responseType };

        return components;
    }

    generateGreeting(emotion) {
        const greetings = {
            JOY: 'يسعدني حماسك! 😊',
            SADNESS: 'أتفهم شعورك...',
            NEUTRAL: 'بالتأكيد،'
        };
        return greetings[emotion.type] || greetings.NEUTRAL;
    }
}

// ========================================
// 4. مولد النصوص (Text Generator)
// ========================================
class TextGenerator {
    constructor() {
        // قاعدة بيانات القوالب النصية
        this.templates = {
            ANSWER: {
                WHAT: [
                    '{topic} هو {explanation}',
                    'يمكن تعريف {topic} على أنه {explanation}',
                    'ببساطة، {topic} يعني {explanation}'
                ],
                HOW: [
                    'يعمل {topic} من خلال {explanation}',
                    'الطريقة هي: {explanation}',
                    'يمكنك القيام بذلك عبر {explanation}'
                ],
                WHY: [
                    'السبب هو {explanation}',
                    'ذلك لأن {explanation}',
                    'يحدث هذا بسبب {explanation}'
                ],
                GENERAL: [
                    'الإجابة هي: {explanation}',
                    'دعني أوضح لك: {explanation}',
                    'بكل سرور! {explanation}'
                ]
            },
            GREETING: [
                'مرحباً! يسعدني التحدث معك 😊',
                'أهلاً وسهلاً! كيف يمكنني مساعدتك؟',
                'السلام عليكم! أنا هنا لخدمتك',
                'مرحباً بك! ما الذي تود معرفته؟'
            ],
            FAREWELL: [
                'وداعاً! كان من دواعي سروري مساعدتك 👋',
                'إلى اللقاء! أتمنى لك يوماً سعيداً',
                'مع السلامة! لا تتردد في العودة',
                'وداعاً! سعدت بالحديث معك'
            ],
            THANKS: [
                'العفو! سعيد بمساعدتك 😊',
                'لا شكر على واجب!',
                'تشرفت بخدمتك!',
                'دائماً في الخدمة!'
            ],
            APOLOGY: [
                'أعتذر عن ذلك. دعني أساعدك بشكل أفضل',
                'آسف على الإزعاج. كيف يمكنني تحسين الأمر؟',
                'أعتذر. سأحاول تقديم خدمة أفضل'
            ],
            CONFIRMATION: [
                'ممتاز! أنا معك',
                'رائع! لنتابع',
                'حسناً، فهمت'
            ],
            CLARIFICATION: [
                'دعني أوضح الأمر بشكل أفضل',
                'ربما لم أكن واضحاً. المقصود هو',
                'لأكون أكثر دقة'
            ],
            SUGGESTION: [
                'أقترح عليك {suggestion}',
                'يمكنك تجربة {suggestion}',
                'ما رأيك في {suggestion}؟'
            ]
        };

        // قاعدة معرفة عن بصيرة AI
        this.knowledgeBase = {
            'بصيرة': 'نظام ذكاء اصطناعي ثوري يعمل بالمعادلات الرياضية المتكيفة بدون استخدام الشبكات العصبية',
            'المعادلة الأم': 'المعادلة الأساسية O = (id, Φ, Ψ(t), Γ) التي تمثل أي كائن أو معلومة في النظام',
            'الذكاء الاصطناعي': 'علم يهدف لجعل الآلات تحاكي الذكاء البشري في التفكير والتعلم واتخاذ القرارات',
            'المعادلات المتكيفة': 'معادلات رياضية تتغير وتتطور تلقائياً مع تغير المعلومات',
            'نظرية الفتائل': 'نظرية ثورية تقول أن النتائج المعقدة تُبنى من فتائل بسيطة متشابكة',
            'ثنائية الصفر': 'نظرية تقول أن لكل قيمة نقيضاً ومجموعهما يساوي صفراً في التوازن المثالي',
            'تعامد الأضداد': 'نظرية تقول أن لكل اتجاه نقيضاً متعامداً عليه',
            'الخبير': 'وحدة في بصيرة AI مسؤولة عن استخدام المعرفة المكتسبة',
            'المستكشف': 'وحدة في بصيرة AI مسؤولة عن اكتشاف معرفة جديدة والابتكار',
            'طبقات التفكير': '11 طبقة تفكير في بصيرة: رياضية، منطقية، تفسيرية، فيزيائية، لغوية، رمزية، بصرية، دلالية، أحداث، عاطفية، خصائص'
        };
    }

    generate(plan, intentAnalysis, understanding, settings) {
        let text = '';

        // إضافة التحية إن وجدت
        if (plan.components.greeting) {
            text += plan.components.greeting + ' ';
        }

        // توليد المحتوى الرئيسي
        const mainContent = this.generateMainContent(
            plan.responseType,
            intentAnalysis,
            understanding,
            settings
        );
        text += mainContent;

        // إضافة أمثلة إذا كان المستوى تفصيلي
        if (settings.detailLevel === 'DETAILED' || settings.detailLevel === 'COMPREHENSIVE') {
            const example = this.generateExample(understanding.context);
            if (example) {
                text += ' ' + example;
            }
        }

        return {
            text: text,
            alternatives: this.generateAlternatives(text, settings),
            metadata: {
                length: text.length,
                style: settings.writingStyle,
                detailLevel: settings.detailLevel
            }
        };
    }

    generateMainContent(responseType, intentAnalysis, understanding, settings) {
        // اختيار القالب المناسب
        const templates = this.templates[responseType];

        if (!templates) {
            return this.generateGenericResponse(intentAnalysis, understanding);
        }

        // إذا كان سؤال، نستخدم نوع السؤال
        if (responseType === 'ANSWER' && intentAnalysis.questionType) {
            const questionTemplates = templates[intentAnalysis.questionType] || templates.GENERAL;
            const template = this.selectTemplate(questionTemplates, settings);
            return this.fillTemplate(template, intentAnalysis, understanding);
        }

        // للأنواع الأخرى
        if (Array.isArray(templates)) {
            return this.selectTemplate(templates, settings);
        }

        return this.generateGenericResponse(intentAnalysis, understanding);
    }

    selectTemplate(templates, settings) {
        // اختيار قالب بناءً على الأسلوب
        if (settings.writingStyle === 'FORMAL') {
            return templates[0];
        } else if (settings.writingStyle === 'FRIENDLY') {
            return templates[templates.length - 1];
        }
        // اختيار عشوائي
        return templates[Math.floor(Math.random() * templates.length)];
    }

    fillTemplate(template, intentAnalysis, understanding) {
        let filled = template;

        // استخراج الموضوع من الكيانات
        const topic = intentAnalysis.entities.find(e => e.type === 'CONCEPT')?.value || 'الموضوع';

        // البحث في قاعدة المعرفة
        let explanation = 'معلومة مفيدة ومهمة';
        for (const [key, value] of Object.entries(this.knowledgeBase)) {
            if (topic.includes(key) || key.includes(topic)) {
                explanation = value;
                break;
            }
        }

        filled = filled.replace('{topic}', topic);
        filled = filled.replace('{explanation}', explanation);
        filled = filled.replace('{suggestion}', 'استكشاف المزيد عن هذا الموضوع');

        return filled;
    }

    generateGenericResponse(intentAnalysis, understanding) {
        // استجابة عامة ذكية
        const responses = {
            QUESTION: 'هذا سؤال مثير للاهتمام! بناءً على فهمي، يمكنني القول أن الموضوع يتعلق بمجال مهم يستحق الاستكشاف.',
            REQUEST: 'بالتأكيد! سأكون سعيداً بمساعدتك في ذلك.',
            COMPLAINT: 'أعتذر عن أي إزعاج. دعني أحاول مساعدتك بشكل أفضل.',
            PRAISE: 'شكراً جزيلاً! يسعدني أن الخدمة نالت إعجابك 😊',
            SUGGESTION: 'اقتراح رائع! سأأخذه بعين الاعتبار.',
            OTHER: 'فهمت. هل يمكنك توضيح المزيد؟'
        };

        return responses[intentAnalysis.intent] || responses.OTHER;
    }

    generateExample(context) {
        const examples = {
            SYSTEM: 'على سبيل المثال، يمكن لبصيرة AI معالجة المعلومات بسرعة فائقة.',
            MATHEMATICS: 'مثلاً، المعادلة الأم يمكنها تمثيل أي كائن رياضي.',
            AI: 'كمثال، الذكاء الاصطناعي يستخدم في التعرف على الصور والنصوص.',
            LANGUAGE: 'على سبيل المثال، معالجة اللغة الطبيعية تساعد في فهم النصوص.'
        };

        return examples[context.mainTopic] || null;
    }

    generateAlternatives(text, settings) {
        // توليد نسخ بديلة من النص
        const alternatives = [];

        // نسخة أقصر
        const brief = text.split('.')[0] + '.';
        if (brief !== text) {
            alternatives.push(brief);
        }

        // نسخة أطول
        const detailed = text + ' هل تريد معرفة المزيد؟';
        alternatives.push(detailed);

        return alternatives;
    }
}

// ========================================
// 5. محسن الطلاقة (Fluency Enhancer)
// ========================================
class FluencyEnhancer {
    constructor() {
        this.connectors = {
            ADDITION: ['أيضاً', 'كذلك', 'بالإضافة إلى ذلك', 'علاوة على ذلك'],
            CONTRAST: ['لكن', 'ومع ذلك', 'على الرغم من ذلك', 'بالمقابل'],
            CAUSALITY: ['لذلك', 'وبالتالي', 'نتيجة لذلك', 'من هنا'],
            TEMPORAL: ['ثم', 'بعد ذلك', 'في البداية', 'أخيراً'],
            CLARIFICATION: ['أي', 'بمعنى آخر', 'بعبارة أخرى', 'وهذا يعني'],
            SUMMARY: ['باختصار', 'في الختام', 'إجمالاً', 'خلاصة القول']
        };
    }

    enhance(generatedText, settings) {
        let enhanced = generatedText.text;

        // إضافة روابط لغوية
        enhanced = this.addConnectors(enhanced);

        // إزالة التكرار
        enhanced = this.removeRedundancy(enhanced);

        // تحسين الوضوح
        enhanced = this.improveClarity(enhanced);

        // ضبط النبرة حسب الأسلوب
        enhanced = this.adjustTone(enhanced, settings.writingStyle);

        return {
            original: generatedText.text,
            enhanced: enhanced,
            improvements: this.calculateImprovements(generatedText.text, enhanced)
        };
    }

    addConnectors(text) {
        // إضافة روابط بين الجمل
        const sentences = text.split('.');
        if (sentences.length > 2) {
            // إضافة رابط في الجملة الثانية
            sentences[1] = ' ' + this.connectors.ADDITION[0] + '، ' + sentences[1].trim();
        }
        return sentences.join('.');
    }

    removeRedundancy(text) {
        // إزالة الكلمات المكررة المتتالية
        return text.replace(/\b(\w+)\s+\1\b/g, '$1');
    }

    improveClarity(text) {
        // تحسين الوضوح بإضافة علامات ترقيم
        let improved = text;

        // التأكد من وجود نقطة في النهاية
        if (!improved.endsWith('.') && !improved.endsWith('!') && !improved.endsWith('?')) {
            improved += '.';
        }

        return improved;
    }

    adjustTone(text, style) {
        let adjusted = text;

        // ضبط النبرة حسب الأسلوب
        if (style === 'FORMAL') {
            // إزالة الإيموجي في الأسلوب الرسمي
            adjusted = adjusted.replace(/[\u{1F600}-\u{1F64F}]/gu, '');
        } else if (style === 'FRIENDLY') {
            // إضافة إيموجي إذا لم يكن موجوداً
            if (!adjusted.match(/[\u{1F600}-\u{1F64F}]/gu)) {
                adjusted += ' 😊';
            }
        }

        return adjusted;
    }

    calculateImprovements(original, enhanced) {
        return {
            lengthChange: enhanced.length - original.length,
            clarityScore: this.calculateClarityScore(enhanced),
            fluencyScore: this.calculateFluencyScore(enhanced)
        };
    }

    calculateClarityScore(text) {
        let score = 0.5;

        // زيادة النقاط للجمل الواضحة
        if (text.includes('.')) score += 0.1;
        if (text.length > 20 && text.length < 200) score += 0.2;
        if (!text.match(/\b(\w+)\s+\1\b/)) score += 0.2;

        return Math.min(score, 1.0);
    }

    calculateFluencyScore(text) {
        let score = 0.5;

        // زيادة النقاط للنص الطليق
        const connectorWords = Object.values(this.connectors).flat();
        for (const connector of connectorWords) {
            if (text.includes(connector)) {
                score += 0.1;
                break;
            }
        }

        return Math.min(score, 1.0);
    }
}

// ========================================
// 6. نظام التعلم (Learning System)
// ========================================
class ConversationalLearning {
    constructor() {
        this.conversations = [];
        this.patterns = {
            successfulResponses: [],
            failedResponses: [],
            commonQuestions: {}
        };
    }

    logConversation(userInput, systemResponse, analysis) {
        this.conversations.push({
            timestamp: new Date(),
            userInput: userInput,
            systemResponse: systemResponse,
            analysis: analysis
        });

        // تحديث الأنماط
        this.updatePatterns(userInput, analysis);
    }

    updatePatterns(userInput, analysis) {
        // تسجيل الأسئلة الشائعة
        const intent = analysis.intent.intent;
        if (!this.patterns.commonQuestions[intent]) {
            this.patterns.commonQuestions[intent] = 0;
        }
        this.patterns.commonQuestions[intent]++;
    }

    getStatistics() {
        return {
            totalConversations: this.conversations.length,
            commonIntents: this.patterns.commonQuestions,
            averageResponseLength: this.calculateAverageResponseLength()
        };
    }

    calculateAverageResponseLength() {
        if (this.conversations.length === 0) return 0;

        const total = this.conversations.reduce((sum, conv) => {
            return sum + (conv.systemResponse?.length || 0);
        }, 0);

        return Math.round(total / this.conversations.length);
    }
}

// ========================================
// 7. النظام المتكامل (Integrated System)
// ========================================
class IntegratedConversationalAI {
    constructor() {
        this.intentAnalyzer = new IntentAnalyzer();
        this.deepUnderstanding = new DeepUnderstanding();
        this.responsePlanner = new ResponsePlanner();
        this.textGenerator = new TextGenerator();
        this.fluencyEnhancer = new FluencyEnhancer();
        this.learningSystem = new ConversationalLearning();

        this.settings = {
            writingStyle: 'FRIENDLY',
            detailLevel: 'MEDIUM',
            enabledComponents: {
                intent: true,
                understanding: true,
                planner: true,
                generator: true,
                fluency: true,
                learning: true
            }
        };

        this.statistics = {
            totalProcessed: 0,
            totalTime: 0,
            componentStats: {}
        };
    }

    updateSettings(newSettings) {
        this.settings = { ...this.settings, ...newSettings };
    }

    async processMessage(userInput) {
        const startTime = Date.now();
        const processingLog = [];

        try {
            // 1. تحليل النية
            let intentAnalysis = null;
            if (this.settings.enabledComponents.intent) {
                intentAnalysis = this.intentAnalyzer.analyze(userInput);
                processingLog.push({ step: 'Intent Analysis', result: intentAnalysis });
            }

            // 2. الفهم العميق
            let understanding = null;
            if (this.settings.enabledComponents.understanding && intentAnalysis) {
                understanding = this.deepUnderstanding.analyze(userInput, intentAnalysis);
                processingLog.push({ step: 'Deep Understanding', result: understanding });
            }

            // 3. تخطيط الاستجابة
            let plan = null;
            if (this.settings.enabledComponents.planner && intentAnalysis && understanding) {
                plan = this.responsePlanner.plan(intentAnalysis, understanding, this.settings);
                processingLog.push({ step: 'Response Planning', result: plan });
            }

            // 4. توليد النص
            let generatedText = null;
            if (this.settings.enabledComponents.generator && plan) {
                generatedText = this.textGenerator.generate(plan, intentAnalysis, understanding, this.settings);
                processingLog.push({ step: 'Text Generation', result: generatedText });
            }

            // 5. تحسين الطلاقة
            let finalResponse = null;
            if (this.settings.enabledComponents.fluency && generatedText) {
                finalResponse = this.fluencyEnhancer.enhance(generatedText, this.settings);
                processingLog.push({ step: 'Fluency Enhancement', result: finalResponse });
            } else if (generatedText) {
                finalResponse = { enhanced: generatedText.text, original: generatedText.text };
            }

            // 6. التعلم
            if (this.settings.enabledComponents.learning && finalResponse) {
                this.learningSystem.logConversation(userInput, finalResponse.enhanced, {
                    intent: intentAnalysis,
                    understanding: understanding
                });
            }

            // تحديث الإحصائيات
            const processingTime = Date.now() - startTime;
            this.updateStatistics(processingTime);

            return {
                response: finalResponse?.enhanced || 'عذراً، لم أتمكن من معالجة الرسالة.',
                analysis: {
                    intent: intentAnalysis,
                    understanding: understanding,
                    plan: plan,
                    processingTime: processingTime
                },
                processingLog: processingLog
            };

        } catch (error) {
            console.error('Error processing message:', error);
            return {
                response: 'عذراً، حدث خطأ أثناء معالجة رسالتك. يرجى المحاولة مرة أخرى.',
                analysis: null,
                processingLog: processingLog,
                error: error.message
            };
        }
    }

    updateStatistics(processingTime) {
        this.statistics.totalProcessed++;
        this.statistics.totalTime += processingTime;
    }

    getStatistics() {
        return {
            general: {
                totalProcessed: this.statistics.totalProcessed,
                averageTime: this.statistics.totalProcessed > 0
                    ? (this.statistics.totalTime / this.statistics.totalProcessed).toFixed(2)
                    : 0
            },
            learning: this.learningSystem.getStatistics()
        };
    }
}

// ========================================
// 8. واجهة التطبيق (Application Interface)
// ========================================

// إنشاء نسخة من النظام
const conversationalAI = new IntegratedConversationalAI();

// متغيرات عامة
let messageCount = 0;
let totalTime = 0;

// دالة إرسال الرسالة
window.sendMessage = async function() {
    const input = document.getElementById('userInput');
    const text = input.value.trim();

    if (!text) return;

    // إضافة رسالة المستخدم
    addMessage(text, 'user');
    input.value = '';

    // إظهار مؤشر المعالجة
    const indicator = document.getElementById('processingIndicator');
    indicator.classList.add('active');

    // تحديث الإعدادات من الواجهة
    updateAISettings();

    // معالجة الرسالة
    const result = await conversationalAI.processMessage(text);

    // إخفاء مؤشر المعالجة
    indicator.classList.remove('active');

    // إضافة رسالة النظام
    addMessage(result.response, 'system');

    // تحديث التحليل
    updateAnalysis(result.analysis);

    // تحديث الإحصائيات
    updateStats(result.analysis.processingTime);
};

// دالة إضافة رسالة
function addMessage(text, sender) {
    const messagesDiv = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;

    const time = new Date().toLocaleTimeString('ar-EG', {
        hour: '2-digit',
        minute: '2-digit'
    });

    messageDiv.innerHTML = `
        <div>${text}</div>
        <div class="message-meta">${sender === 'user' ? 'أنت' : 'بصيرة AI'} • ${time}</div>
    `;

    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

// دالة تحديث التحليل
function updateAnalysis(analysis) {
    if (!analysis) return;

    const analysisDiv = document.getElementById('lastAnalysis');

    const intentLabel = getIntentLabel(analysis.intent?.intent);
    const emotionLabel = getEmotionLabel(analysis.understanding?.emotion?.type);
    const toneLabel = getToneLabel(analysis.understanding?.tone);

    analysisDiv.innerHTML = `
        <div class="analysis-item">
            <strong>النية:</strong> <span class="badge">${intentLabel}</span>
        </div>
        <div class="analysis-item">
            <strong>المشاعر:</strong> <span class="badge">${emotionLabel}</span>
        </div>
        <div class="analysis-item">
            <strong>النبرة:</strong> <span class="badge">${toneLabel}</span>
        </div>
        <div class="analysis-item">
            <strong>وقت المعالجة:</strong> ${analysis.processingTime}ms
        </div>
        <div class="analysis-item">
            <strong>الثقة:</strong> ${(analysis.intent?.confidence * 100).toFixed(0)}%
        </div>
    `;
}

// دوال الترجمة
function getIntentLabel(intent) {
    const labels = {
        QUESTION: 'سؤال',
        GREETING: 'تحية',
        FAREWELL: 'وداع',
        THANKS: 'شكر',
        APOLOGY: 'اعتذار',
        CONFIRMATION: 'تأكيد',
        DENIAL: 'رفض',
        REQUEST: 'طلب',
        COMPLAINT: 'شكوى',
        PRAISE: 'مدح',
        SUGGESTION: 'اقتراح',
        COMMAND: 'أمر',
        OTHER: 'أخرى'
    };
    return labels[intent] || intent;
}

function getEmotionLabel(emotion) {
    const labels = {
        JOY: 'فرح',
        SADNESS: 'حزن',
        ANGER: 'غضب',
        FEAR: 'خوف',
        SURPRISE: 'مفاجأة',
        LOVE: 'حب',
        HOPE: 'أمل',
        ANXIETY: 'قلق',
        NEUTRAL: 'محايد'
    };
    return labels[emotion] || emotion;
}

function getToneLabel(tone) {
    const labels = {
        POLITE: 'مهذب',
        FRIENDLY: 'ودي',
        FORMAL: 'رسمي',
        INFORMAL: 'غير رسمي',
        SARCASTIC: 'ساخر',
        SERIOUS: 'جاد',
        ENTHUSIASTIC: 'متحمس',
        CALM: 'هادئ',
        NEUTRAL: 'محايد'
    };
    return labels[tone] || tone;
}

// دالة تحديث الإحصائيات
function updateStats(processingTime) {
    messageCount++;
    totalTime += processingTime;

    document.getElementById('totalMessages').textContent = messageCount;
    document.getElementById('avgTime').textContent =
        Math.round(totalTime / messageCount) + 'ms';
}

// دالة تحديث إعدادات الذكاء الاصطناعي
function updateAISettings() {
    const writingStyle = document.getElementById('writingStyle').value;
    const detailLevel = document.getElementById('detailLevel').value;

    conversationalAI.updateSettings({
        writingStyle: writingStyle,
        detailLevel: detailLevel,
        enabledComponents: {
            intent: document.getElementById('enableIntent').checked,
            understanding: document.getElementById('enableUnderstanding').checked,
            planner: document.getElementById('enablePlanner').checked,
            generator: document.getElementById('enableGenerator').checked,
            fluency: document.getElementById('enableFluency').checked,
            learning: document.getElementById('enableLearning').checked
        }
    });
}

// دالة معالجة ضغط Enter
window.handleKeyPress = function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
};

// دالة بدء محادثة جديدة
window.startConversation = function() {
    addMessage("تم بدء محادثة جديدة! 🎉 أنا جاهز للإجابة على أسئلتك.", 'system');
};

// دالة مسح المحادثة
window.clearChat = function() {
    const messagesDiv = document.getElementById('chatMessages');
    messagesDiv.innerHTML = `
        <div class="message system">
            <div>مرحباً! أنا بصيرة AI، نظام ذكاء اصطناعي متقدم يعمل بالمعادلات الرياضية المتكيفة بدون شبكات عصبية. كيف يمكنني مساعدتك اليوم؟ 😊</div>
            <div class="message-meta">بصيرة AI • الآن</div>
        </div>
    `;
    messageCount = 0;
    totalTime = 0;
    document.getElementById('totalMessages').textContent = '0';
    document.getElementById('avgTime').textContent = '0ms';
    document.getElementById('lastAnalysis').innerHTML = '<p style="color: #999; text-align: center; font-size: 14px;">لا يوجد تحليل بعد</p>';
};

// رسالة ترحيبية عند تحميل الصفحة
console.log('🤖 بصيرة AI - نظام الذكاء الحواري الحقيقي');
console.log('✅ النظام جاهز للعمل!');
console.log('📊 المكونات: محلل النوايا، الفهم العميق، مخطط الاستجابة، مولد النصوص، محسن الطلاقة، نظام التعلم');

