# 🌟 Bayan - Hybrid Programming Language | لغة البيان

**Last Updated**: 2025-11-25

<div align="center">

![Bayan Language](https://img.shields.io/badge/Bayan-Hybrid%20Language-blue?style=for-the-badge)
![Tests](https://img.shields.io/badge/tests-555%20passing-green?style=for-the-badge)
![Arabic Support](https://img.shields.io/badge/Arabic-Fully%20Supported-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
[![CI](https://github.com/mubtakir/nlp_bayan/actions/workflows/lint-and-test.yml/badge.svg?branch=main)](https://github.com/mubtakir/nlp_bayan/actions/workflows/lint-and-test.yml)
[![Tests Workflow](https://github.com/mubtakir/nlp_bayan/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/mubtakir/nlp_bayan/actions/workflows/tests.yml)


[![Developer Guide](https://img.shields.io/badge/Developer%20Guide-nlp__bayan-blue?style=for-the-badge)](docs/DEVELOPER_GUIDE.md)
[![Roadmap](https://img.shields.io/badge/Roadmap-Plan-orange?style=for-the-badge)](docs/ROADMAP.md)
[![Changelog](https://img.shields.io/badge/Changelog-Recent%20Changes-purple?style=for-the-badge)](CHANGELOG.md)


**The World's First True Hybrid Programming Language**
**أول لغة برمجة هجينة حقيقية في العالم**

[English](#english) | [العربية](#arabic)

</div>

---

> Status update (2025-11-24): Arabic Morphology System fully integrated with logic engine. AI stdlib Waves 1–20 complete (379 tests passing).



## 📘 Project Docs (nlp_bayan)
- Developer Guide: [docs/DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md)
- Roadmap: [docs/ROADMAP.md](docs/ROADMAP.md)
- Changelog: [CHANGELOG.md](CHANGELOG.md)

<a name="english"></a>

## 🎯 What is Bayan?

**Bayan** (البيان) is a revolutionary hybrid programming language that seamlessly combines **three programming paradigms** in one unified syntax:

1. **Imperative Programming** - Traditional procedural code
2. **Object-Oriented Programming (OOP)** - Classes, inheritance, polymorphism
3. **Logic Programming** - Prolog-style facts, rules, and queries

### 🌟 Key Features

- ✅ **Three Paradigms in One** - Switch between imperative, OOP, and logic programming seamlessly
- ✅ **Bilingual Keywords** - Full support for both Arabic and English keywords
- ✅ **Arabic Text Support** - Perfect handling of Arabic text without external libraries
- ✅ **Causal-Semantic System** ⭐ NEW - Express cause-effect relationships with physical/logical reasons
- ✅ **Adaptive GSE Engine** 🧠 NEW - Generalized Shape Equation for adaptive learning and function approximation
- ✅ **Mother Equation System** 🌟 NEW - Comprehensive object representation (properties, states, shapes)
- ✅ **Linguistic Equations** 💬 NEW - Convert natural language concepts to mathematical equations
- ✅ **Expert-Explorer System** 🎯 NEW - Dual decision-making combining expertise with exploration
- ✅ **Compiler Interface** 🔧 NEW - Advanced error classification and compilation analytics
- ✅ **Dual Brain Architecture** 🧠🧠 NEW - World's first true dual-brain programming language (logical + mathematical)
- ✅ **Modern Features** - Async/await, generators, decorators, context managers
- ✅ **AI/ML Ready** - Built-in functions for data science and machine learning
- ✅ **Dynamic Knowledge Base** - Assert and retract facts at runtime
- ✅ **Block Syntax** - Colon `:` + braces `{}`; indentation optional; no semicolons

- ✅ **High Test Coverage** - 555 passing tests (621 total)
- ✅ **Comprehensive Documentation** - 5,594+ lines of tutorials and guides
- ✅ **LLM Integration** - Ready-to-use prompts for ChatGPT, Claude, and other AI models

- ✅ Built-in Web IDE — run Bayan in your browser; great if you can't install dev tools

- ✅ Linguistic Templates — Multi-valued facts/rules/queries with Arabic nominal patterns (صفات/ألقاب/إضافة/ملكية)
- ✅ Grammar-level nominal phrases — Parser sugar inside hybrid: محمد الطبيب. عصير العنب[of]. مالك البيت[belongs].
- ✅ Programmable templates — define_nominal_template / define_head_template for custom phrase mappings
- ✅ Programmable templates — define_nominal_template / define_head_template for custom phrase mappings
- ✅ Built-in head hints — common heads auto-map to relations (e.g., مالك/owner → belongs, عصير/juice → of)

- ✅ **Generative Language Model (GLM)** ⭐ NEW - Full pipeline from abstract meaning to fluent text
    - **Lexicon**: Maps concepts to Arabic/English lemmas
    - **Morphology**: Conjugates verbs and declines nouns (Arabic/English)
    - **Realizer**: Generates coherent sentences from conceptual traces


---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/mubtakir/nlp_bayan.git
cd nlp_bayan
```

### Hello World

```bayan
hybrid {
    print("Hello, World!")
    print("مرحباً بالعالم!")
}
```

### Run it

```bash
python -m bayan examples/hello.by
```

Note: Both .by and .bayan extensions are supported for Bayan scripts and imports. Conventionally, .bayan is used for libraries/modules and .by for runnable scripts.


## 🧰 Built-in Web IDE (no install)

If you can’t install development tools, Bayan ships with a simple Web IDE you can run locally:

```bash
python web_ide/app.py
# then open your browser: http://127.0.0.1:5001/ide
```

- Create/rename/delete/save files (stored under web_ide/user_scripts)
- Run whole file or only the selected code
- Error messages with stack traces, RTL-friendly UI
- Theme and font controls, keyboard shortcuts (Ctrl/Cmd+S to save, Ctrl/Cmd+Enter to run)
- AI autocompletion (Arabic/English) with function docs; filter by language and domain (ai.ml / ai.nlp / ai.data / logic)
- Examples browser with search and domain filters (ai.ml / ai.nlp / ai.data / logic / mixed / unknown); hover tooltips and domain badges in the list
- Highlighted example in the IDE examples browser: `ar_مستشار_توازن_حياة_الطالب.md` — **Student Life Balance Advisor | مستشار توازن حياة الطالب** (advanced Arabic hybrid example combining entities, fuzzy states, semantic knowledge, and similarity/synonyms to propose an explained study plan)

- Graphics (gfx) domain + live SVG preview panel — SVG helpers (shapes/text/groups), waves (sine/square/triangle), and free pen drawing (Arabic/English)

## 🧩 Syntax: Blocks and Indentation

Unlike Python, Bayan does NOT require indentation. Blocks are defined by a colon `:` after control keywords and braces `{}`. No semicolons; each statement on its own line.

Formatted (readable):

```bayan
if (x > 0) {
  print("positive")
}
```

Unformatted (still valid):

```bayan
if (x > 0) {
print("positive")
}
```

---

---

## 💡 Examples

### 1. Imperative Programming

```bayan
hybrid {
    # Variables and operations
    x = 10
    y = 20
    sum = x + y
    print("Sum: " + str(sum))

    # Control flow
    if (sum > 25) {
        print("Large sum")
    }

    # Loops
    for i in (range(5)) {
        print("Number: " + str(i))
    }
}
```

### 2. Object-Oriented Programming

```bayan
hybrid {
    class Person: {
        def __init__(self, name, age): {
            self.name = name
            self.age = age
        }

        def greet(self): {
            return "Hello, I am " + self.name
        }
    }

    person = Person("أحمد", 25)
    print(person.greet())
}
```

### 3. Logic Programming

```bayan
hybrid {
    # Facts
    parent("أحمد", "محمد").
    parent("أحمد", "فاطمة").
    parent("علي", "سارة").

    # Rules
    sibling(?X, ?Y) :- parent(?P, ?X), parent(?P, ?Y), ?X != ?Y.

    # Query
    results = query sibling("محمد", ?S)?

    for result in (results) {
        print("Sibling: " + result["?S"])
    }
}
```

### 4. Hybrid Programming (All Three!)

```bayan
hybrid {
    # OOP: Define a Student class
    class Student: {
        def __init__(self, name, grade): {
            self.name = name
            self.grade = grade

            # Logic: Add to knowledge base
            assertz(student(name, grade))
        }
    }

    # Imperative: Create students
    students = [
        Student("أحمد", 85),
        Student("فاطمة", 95),
        Student("علي", 92)
    ]

    # Logic: Query excellent students
    results = query student(?N, ?G), ?G >= 90?

    # Imperative: Print results
    print("Excellent students:")
    for result in (results) {
        print("  - " + result["?N"] + ": " + str(result["?G"]))
    }
}
```

### 5. Causal-Semantic Knowledge ⭐ NEW

```bayan
hybrid {
    # Define causal laws with physical/logical reasons
    سبب_نتيجة("رفع_شيء_لفوق", "يسقط", "جاذبية", 1.0).
    سبب_نتيجة("دراسة_مجتهدة", "نجاح", "اكتساب_معرفة", 0.9).

    # Define semantic relations
    علاقة("الاستحمام", "في", "حمام", 0.9).
    علاقة("البيت", "فيه", "حمام", 0.95).
    علاقة("النهر", "هو", "ماء", 1.0).

    # Query: Why does something fall?
    print("Why does something fall when lifted?")
    query سبب_نتيجة("رفع_شيء_لفوق", ?result, ?cause, ?strength).
    # Returns: ?result="يسقط", ?cause="جاذبية", ?strength=1.0

    # Query: Where does bathing happen?
    print("Where does bathing happen?")
    query علاقة("الاستحمام", ?relation_type, ?place, ?strength).
    # Returns: ?relation_type="في", ?place="حمام", ?strength=0.9
}
```

**Benefits:**
- Goes beyond word embeddings by representing meanings through cause-effect relationships
- Explainable AI: Every relationship has a clear reason
- Context-aware prediction based on semantic distance
- Supports causal reasoning in physics, biology, social sciences, and more

---

### 6. Adaptive Learning with GSE 🧠 NEW

```bayan
hybrid {
    # Learn a model from data
    x_data = [0, 1, 2, 3, 4, 5]
    y_data = [0, 1, 4, 9, 16, 25]
    
    model = learn("square_function", x_data, y_data, max_components=3, verbose=True)
    
    # Infer new values
    prediction = infer("square_function", 2.5)
    print("f(2.5) = " + str(prediction))  # ≈ 6.25
}
```

**Benefits:**
- **Adaptive Function Approximation**: Learns complex functions from data
- **Explainable Structure**: Uses interpretable sigmoid components
- **Two-Stage Fitting**: Greedy build-up + global optimization
- **No Black Box**: Clear mathematical formula, not a neural network

---

### 7. Mother Equation System 🌟 NEW

```bayan
hybrid {
    # Create an object with comprehensive representation
    # Object = (id, Φ, Ψ(t), Γ)
    #   Φ: Fixed properties
    #   Ψ(t): Dynamic states (fuzzy 0..1)
    #   Γ: Shape equation (GSE)
    
    person = MotherEquation("P001", "سارة")
    
    # Add fixed properties
    person.add_property("العمر", 25, PropertyDomain("بيولوجي"), "سنة")
    person.add_property("المهنة", "طبيبة", PropertyDomain("اجتماعي"))
    
    # Add dynamic states (fuzzy values 0..1)
    person.add_state("السعادة", 0.7)
    person.add_state("الطاقة", 0.8)
    
    # Update states
    person.update_state("السعادة", 0.9)
    
    # Export/Import JSON
    json_str = person.to_json()
    restored = MotherEquation.from_json(json_str)
}
```

**Benefits:**
- **Comprehensive Modeling**: Combines fixed properties, dynamic states, and shapes
- **10 Property Domains**: Physical, Chemical, Psychological, Social, Biological, etc.
- **Fuzzy States**: All states are normalized (0..1) for consistency
- **Shape Equations**: Attach GSE models to represent object geometry

---

### 8. Linguistic Equations 💬 NEW

```bayan
hybrid {
    # Philosophy: Idea = (Objects + Event + Result)
    # الفكرة = (أشياء + حدث + نتيجة)
    
    kb = KnowledgeBase()
    
    # Parse natural language sentence
    eq = parse_sentence("محمد أكل تفاحة", kb)
    
    print(eq.to_natural_language())
    # → "محمد أكل تفاحة"
    
    print(eq.to_formal_notation())
    # → محمد(فاعل) + تفاحة(مفعول_به) + أكل = 
    #   [محمد: جوع↓, طاقة↑] + [تفاحة: موجود=False]
    
    # Create custom equation
    eq2 = create_simple_equation("أحمد", "ضرب", "الكرة", kb)
    
    # Add custom event to knowledge base
    kb.add_custom_event(
        event="درس",
        subject_changes={"تعب": +0.3, "معرفة": +0.6},
        object_changes={"مستوى_الفهم": +0.5}
    )
}
```

**Benefits:**
- **Natural Language → Math**: Converts Arabic sentences to equations
- **Causal Inference**: Automatically infers results from knowledge base
- **8 Roles**: Subject, Object, Location, Time, Instrument, etc.
- **9 Event Types**: Physical, Mental, Communication, Movement, etc.
- **Extensible**: Add custom events with their expected outcomes


---

### 9. Expert-Explorer System 🎯 NEW

```bayan
hybrid {
    # Create an intelligent decision-making system
    brain = BrainSystem(expert_weight=0.7, explorer_weight=0.3)
    
    # Expert: Add knowledge
    brain.expert.add_knowledge("كيف أتعلم Python؟", "ابدأ بالأساسيات", confidence=0.95)
    
    # Make a decision
    decision = brain.decide("كيف أتعلم البرمجة؟")
    print("Decision: " + decision.reasoning)
    print("Confidence: " + str(decision.final_confidence))
}
```

**Benefits:**
- **Dual Decision-Making**: Combines expert knowledge with exploration
- **Three Revolutionary Theories**: Zero Duality, Perpendicular Opposites, Filament Theory
- **Adaptive Learning**: Updates knowledge based on outcomes
- **Confidence Tracking**: Every decision has a confidence score

---

### 10. Compiler Interface 🔧 NEW

```bayan
hybrid {
    # Create compiler interface with advanced error classification
    compiler = BayanCompiler()
    
    # Compile code with detailed error analysis
    result = compiler.compile(source_code, "test.bayan")
    
    if result.success {
        print("✅ Compilation successful!")
    } else {
        print("❌ Errors found:")
        for error in result.errors {
            print(error.get_description("ar"))
        }
    }
    
    # Get compilation statistics
    stats = compiler.get_statistics()
    print("Success rate: " + stats['success_rate'])
}
```

**Benefits:**
- **10 Error Types**: Lexical, Syntax, Semantic, Runtime, Type, Logical, etc.
- **4 Severity Levels**: Error, Warning, Info, Hint
- **Automatic Suggestions**: Smart fix recommendations
- **Comprehensive Analytics**: Track compilation patterns and common errors

---

### 11. Dual Brain Architecture 🧠🧠 NEW - REVOLUTIONARY!

```bayan
hybrid {
    # Create the world's first dual-brain system
    brain = DualBrain()
    
    # Process with both logical and mathematical analysis
    result = brain.process("محمد أكل تفاحة", debug=True)
    
    # View the dual analysis
    result.print_summary()
    
    # Access individual brain analyses
    print("Logical confidence: " + str(result.logical.confidence))
    print("Mathematical confidence: " + str(result.mathematical.confidence))
    print("Final confidence: " + str(result.final_confidence))
    print("Consensus: " + str(result.validation.consensus))
}
```

**Output:**
```
🧩 Phase 1: Logical Analysis...
   ✓ Logical confidence: 70%
   ✓ Facts: 2, Entities: 1

🎨 Phase 2: Mathematical Analysis...
   ✓ Mathematical confidence: 57%
   ✓ Equations: 0, Numerical results: 0

🔍 Phase 3: Cross-Validation...
   ✓ Consensus: 100%

🤝 Phase 4: Negotiation...
   ✓ Logical contribution: 55% | Mathematical contribution: 45%

✨ Final confidence: 64%
```

**Benefits:**
- **Dual Perspective**: Combines logical reasoning with mathematical precision
- **Cross-Validation**: Each brain verifies the other's results
- **Conflict Resolution**: Automatically detects and resolves contradictions
- **Mutual Enhancement**: Weaknesses of one brain are compensated by the other
- **First of Its Kind**: The ONLY programming language with true dual-brain architecture!

**How It Works:**
1. **Left Brain (Logical)**: Extracts facts, entities, applies rules, checks consistency
2. **Right Brain (Mathematical)**: Creates equations, computes numerical values, makes decisions
3. **Integration Layer**: Cross-validates, negotiates, synthesizes final result
4. **Result**: More accurate and comprehensive than either brain alone



## 📚 Documentation

### 🤖 For AI Models (للنماذج اللغوية)
> **Complete project access for AI models with 632+ files organized by category**

- **AI Model Links (روابط للنماذج اللغوية):**
  - RAW: https://raw.githubusercontent.com/mubtakir/nlp_bayan/main/docs/AI_MODEL_LINKS.md
  - GitHub plain: https://github.com/mubtakir/nlp_bayan/blob/main/docs/AI_MODEL_LINKS.md?plain=1
  - **Contains:** Direct links to all essential files (README, keywords reference, guides, tutorials, examples, AI libraries, domain libraries, conceptual libraries, and more)

### 🗺️ Project Architecture Map (For LLMs)

Use this map to navigate the project's conceptual and linguistic layers:

#### 1. Conceptual Layer (The "Brain")
- **Blueprints** (`ai/conceptual_blueprints.bayan`): Defines abstract patterns (Events, States, Causality).
- **Circuits** (`ai/conceptual_circuits.bayan`): Reusable micro-scenarios built from blueprints.
- **Programs** (`ai/conceptual_programs.bayan`): High-level meaning programs that compose circuits.
- **Orchestrator** (`ai/conceptual_orchestrator.bayan`): Manages the execution of meaning programs.

#### 2. Generative Pipeline (The "Voice")
- **Architecture** (`docs/GENERATIVE_LM_ARCHITECTURE.md`): Overview of the GLM pipeline.
- **Lexicon** (`ai/lexicon.bayan`): Maps abstract concepts to Arabic/English lemmas.
- **Morphology** (`ai/morphology.bayan`): Handles conjugation and declension.
- **Surface Realizer** (`ai/conceptual_surface_realizer.bayan`): Converts conceptual traces into text.

#### 3. AI & NLP Libraries
- **NLP Core** (`ai/nlp.bayan`): Basic NLP tools (tokenization, phonetics, roots).
- **Machine Learning** (`ai/ml.bayan`): ML algorithms and data structures.


### Handoff (One-page)
- Quick handoff for the next model: [NEXT_MODEL_BRIEFING.md](NEXT_MODEL_BRIEFING.md)


### Tutorials (Arabic)
- [Part 1: Introduction](docs/01_INTRODUCTION_AR.md) - What is Bayan, features, installation
- [Part 2: Procedural & OOP](docs/02_PROCEDURAL_OOP_AR.md) - From beginner to expert
- [Part 3: Logic Programming](docs/03_LOGIC_PROGRAMMING_AR.md) - Prolog-style programming
- [Part 4: Probabilistic Reasoning](docs/04_PROBABILISTIC_REASONING_AR.md) - Expressing uncertainty 🎲 (NEW!)

### Tutorials (English)
- Procedural & OOP: [PART1](docs/02_PROCEDURAL_OOP_EN_PART1.md), [PART2](docs/02_PROCEDURAL_OOP_EN_PART2.md), [PART3](docs/02_PROCEDURAL_OOP_EN_PART3.md), [PART4](docs/02_PROCEDURAL_OOP_EN_PART4.md)
- Logic Programming: [PART1](docs/03_LOGIC_PROGRAMMING_EN_PART1.md), [PART2](docs/03_LOGIC_PROGRAMMING_EN_PART2.md), [PART3](docs/03_LOGIC_PROGRAMMING_EN_PART3.md), [PART4](docs/03_LOGIC_PROGRAMMING_EN_PART4.md)


### LLM Integration
- [LLM System Prompt](docs/LLM_SYSTEM_PROMPT.txt) - Ready-to-use prompt for AI models
- [LLM Quick Reference](docs/LLM_QUICK_REFERENCE.md) - Quick syntax reference
- [LLM Complete Guide](docs/LLM_REFERENCE_GUIDE.md) - Comprehensive guide with 10 examples
- [How to Use with LLMs](docs/HOW_TO_USE_WITH_LLMS.md) - Complete usage guide

- LLM‑friendly one‑pager (RAW links for models):
  - https://raw.githubusercontent.com/mubtakir/nlp_bayan/main/docs/AI_MODEL_LINKS.md
  - GitHub plain version: https://github.com/mubtakir/nlp_bayan/blob/main/docs/AI_MODEL_LINKS.md?plain=1

### Technical Documentation
- [Language Guide](docs/LANGUAGE_GUIDE.md) - Complete language reference
- [Architecture](docs/ARCHITECTURE.md) - Internal architecture
- [Examples](docs/EXAMPLES.md) - Advanced examples
- [Arabic Text Support](docs/ARABIC_TEXT_SUPPORT.md) - How Arabic text works


### ⚙️ Entity System (Quick Start)

Model dynamic actors, states (0..1), and interactions as facts you can query.

- Keywords: `entity`, `apply` (Arabic: `كيان`, `طبق`)
- Body keys: `states`, `properties`, `actions`, `reactions` (Arabic: "حالات", "خصائص", "أفعال", "ردود_أفعال")

```bayan
hybrid {
    entity Ahmed { "states": {"hunger": 0.6} }
    entity John  { "actions": {
        "feed": {"effects": [{"on": "hunger", "formula": "max(value - 0.4*action_value, 0.0)"}]}
    }}
    apply John.feed(Ahmed, action_value=1.0)
}

query state("Ahmed", "hunger", ?V).
```

- Full guide: docs/ENTITY_SYSTEM_GUIDE.md
- Examples: docs/EXAMPLES.md (see “Entity System Examples (English)”)

---

## ❓ FAQ

- Why use Bayan instead of Python?
  - Bayan unifies imperative, OOP, and logic programming in one syntax, with first-class fuzzy values (0..1) and a built-in Entity System to model interactions as facts you can query.

- How do I integrate Bayan with my current AI model?
  - Two options: (1) call the Bayan interpreter from Python and send code that defines entities and runs queries; (2) use Bayan to generate facts and export query results to your model. See docs/ENTITY_SYSTEM_GUIDE.md.

---


## 🧪 Testing

Run all tests:

```bash
python -m pytest tests/ -v
```

**Result**: 379 tests passing (100% success rate) ✅

## 📚 AI/ML Examples (Wave 20)
- Softmax Multiclass: examples/ai_softmax_multiclass.md
- Voting & Stacking: examples/ai_voting_stacking.md
- Soft TF-IDF Similarity: examples/ai_soft_tfidf_similarity.md
- PCA + Variance + Pipeline: examples/ai_pca_variance_pipeline.md

## 🖼️ Graphics & Visualization (SVG, gfx)
- English: examples/svg_basic_shapes.md, examples/svg_sine_wave.md, examples/svg_free_drawing.md, examples/svg_advanced_shapes.md, examples/img_basic_canvas.md, examples/svg_sawtooth_area.md, examples/wave_modulation.md
- Arabic: examples/ar_svg_أشكال_أساسية.md, examples/ar_svg_موجة_جيبية.md, examples/ar_svg_رسم_حر.md, examples/ar_svg_أشكال_متقدمة.md, examples/ar_img_لوحة_أساسية.md, examples/ar_svg_موجات_متقدمة.md, examples/ar_wave_تعديل.md


### Web IDE Preview Enhancements
- Multi-output rendering: shows all SVG and data:image/* outputs in order (navigate via Prev/Next).
- Toolbar: Download (SVG/PNG/JPEG) and Copy the current output.
- First output remains the default for quick iteration.


---

## 🌍 Use Cases

- **Education** - Teach multiple programming paradigms in one language
- **AI/ML** - Logic programming + imperative for expert systems
- **Arabic Software** - Build software with Arabic keywords and perfect text handling
- **Research** - Explore hybrid programming paradigms
- **Rapid Prototyping** - Use the best paradigm for each part of your code

---

## 📊 Statistics

- **154 files** in the repository
- **41,889 lines** of code and documentation
- **379 tests** (100% passing)
- **5,594+ lines** of tutorials and guides
- **10+ complete examples**
- **3 programming paradigms** in one language

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨💻 Author

**Developed by: Basel Yahya Abdullah (باسل يحيى عبدالله)**
**With assistance from: AI Language Models**

---

- ✅ محرر ويب مدمج — شغّل بيان في المتصفح؛ مناسب لمن لا يستطيع تثبيت بيئات عمل أخرى

## 🙏 Acknowledgments

- Thanks to the open-source community
- Inspired by Python, Prolog, and modern programming languages
- Built for the global programming competition

---

## 📞 Contact

- GitHub: [@mubtakir](https://github.com/mubtakir)
- Repository: [nlp_bayan](https://github.com/mubtakir/nlp_bayan)

---

<a name="arabic"></a>

<div dir="rtl">

## 🎯 ما هي لغة البيان؟

**البيان** هي لغة برمجة هجينة ثورية تجمع بسلاسة بين **ثلاثة أنماط برمجية** في صيغة موحدة:

1. **البرمجة الإجرائية** - الكود الإجرائي التقليدي
2. **البرمجة الكائنية (OOP)** - الأصناف، الوراثة، تعدد الأشكال
3. **البرمجة المنطقية** - الحقائق والقواعد والاستعلامات بأسلوب Prolog

### 🌟 المزايا الرئيسية

- ✅ **ثلاثة أنماط في واحد** - التبديل بين الإجرائية والكائنية والمنطقية بسلاسة
- ✅ **كلمات مفتاحية ثنائية اللغة** - دعم كامل للكلمات المفتاحية العربية والإنجليزية
- ✅ **دعم النصوص العربية** - معالجة مثالية للنصوص العربية بدون مكتبات خارجية
- ✅ **ميزات حديثة** - Async/await، Generators، Decorators، Context Managers
- ✅ **جاهزة للذكاء الاصطناعي** - دوال مدمجة لعلوم البيانات والتعلم الآلي
- ✅ **صيغة الكتل** - نقطتان `:` وأقواس `{}`؛ المسافات البادئة اختيارية؛ بلا فواصل منقوطة

- ✅ **قاعدة معرفة ديناميكية** - إضافة وحذف الحقائق أثناء التشغيل
- ✅ **تغطية اختبارات 100%** - 379 اختبار ناجح
- ✅ **وثائق شاملة** - 5,594+ سطر من الدروس والأدلة
- ✅ **تكامل مع النماذج اللغوية** - Prompts جاهزة لـ ChatGPT وClaude وغيرها

---

## 🚀 البدء السريع

### التثبيت

```bash
git clone https://github.com/mubtakir/nlp_bayan.git
cd nlp_bayan
```

### مرحباً بالعالم

```bayan
hybrid {
    print("مرحباً بالعالم!")
    print("Hello, World!")
}
```

### التشغيل

```bash
python -m bayan examples/hello.by
```


## 🧰 محرر ويب مدمج (لمن لا يمكنه تثبيت بيئات عمل أخرى)

```bash
python web_ide/app.py
# ثم افتح المتصفح: http://127.0.0.1:5001/ide
```

- إنشاء/إعادة تسمية/حذف/حفظ الملفات (web_ide/user_scripts)
- تشغيل الملف كله أو التحديد فقط
- رسائل أخطاء واضحة، واجهة مناسبة للاتجاه من اليمين لليسار
- تحكم بالثيم وحجم الخط، اختصارات لوحة المفاتيح
- إكمال ذكي ثنائي اللغة مع وصف للدوال، وتصفية حسب اللغة والمجال (ai.ml / ai.nlp / ai.data)
- مستعرض أمثلة مع بحث وتصفية حسب المجال (ai.ml / ai.nlp / ai.data / logic / mixed / unknown) ووصف عند المرور وشارة مجال بجانب الاسم


---

## 📚 الوثائق

### 🤖 للنماذج اللغوية (For AI Models)
> **وصول كامل للمشروع للنماذج اللغوية مع 632+ ملف منظم حسب الفئة**

- **روابط النماذج اللغوية (AI Model Links):**
  - RAW: https://raw.githubusercontent.com/mubtakir/nlp_bayan/main/docs/AI_MODEL_LINKS.md
  - GitHub plain: https://github.com/mubtakir/nlp_bayan/blob/main/docs/AI_MODEL_LINKS.md?plain=1
  - **يحتوي على:** روابط مباشرة لجميع الملفات الأساسية (README، مرجع الكلمات المفتاحية، الأدلة، الدروس، الأمثلة، مكتبات الذكاء الاصطناعي، مكتبات المجالات، المكتبات المفاهيمية، والمزيد)

### الدروس التعليمية
- [الجزء الأول: مقدمة](docs/01_INTRODUCTION_AR.md) - ما هي البيان، المزايا، التثبيت
- [الجزء الثاني: الإجرائية والكائنية](docs/02_PROCEDURAL_OOP_AR.md) - من المبتدئ إلى الخبير
- [الجزء الثالث: البرمجة المنطقية](docs/03_LOGIC_PROGRAMMING_AR.md) - البرمجة بأسلوب Prolog
- [الجزء الرابع: الاستدلال الاحتمالي والتشكيك](docs/04_PROBABILISTIC_REASONING_AR.md) - التعبير عن عدم اليقين 🎲 (جديد!)

### التكامل مع النماذج اللغوية
- [System Prompt للنماذج](docs/LLM_SYSTEM_PROMPT.txt) - Prompt جاهز للاستخدام
- [مرجع سريع](docs/LLM_QUICK_REFERENCE.md) - مرجع سريع للصيغة
- [دليل شامل](docs/LLM_REFERENCE_GUIDE.md) - دليل شامل مع 10 أمثلة
- [كيفية الاستخدام مع النماذج](docs/HOW_TO_USE_WITH_LLMS.md) - دليل الاستخدام الكامل

---

## 🧪 الاختبارات

تشغيل جميع الاختبارات:

```bash
python -m pytest tests/ -v
```

**النتيجة**: 379 اختبار ناجح (100% نجاح) ✅

---

## 👨💻 المطور

**تم التطوير بواسطة: باسل يحيى عبدالله**
**بمساعدة: نماذج الذكاء الاصطناعي اللغوية**

---

## 📞 التواصل

- GitHub: [@mubtakir](https://github.com/mubtakir)
- المستودع: [nlp_bayan](https://github.com/mubtakir/nlp_bayan)

---

**🌟 لغة البيان - اللغة الوحيدة التي تجمع ثلاثة أنماط برمجية! 🌟**

</div>

