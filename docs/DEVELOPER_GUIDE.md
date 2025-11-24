# Bayan Developer Guide
# دليل المطور - لغة البيان

Welcome to the Bayan development community! This guide will help you get started contributing to the world's first true hybrid programming language.

---

## 📑 Table of Contents

- [Getting Started](#-getting-started)
- [Architecture Overview](#-architecture-overview)
- [Development Guidelines](#-development-guidelines)
- [Recent Features & Integration](#-recent-features--integration)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
- [Quick Reference](#-quick-reference)

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** (Python 3.11 recommended)
- **Git** for version control
- Basic understanding of:
  - Python programming
  - Object-oriented concepts
  - Logic programming (Prolog) - helpful but not required

### Quick Setup (5 minutes)

#### 1. Clone the repository
```bash
git clone https://github.com/mubtakir/nlp_bayan.git
cd bayan_python_ide14
```

#### 2. Set up virtual environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate        # Linux/macOS
# OR
venv\Scripts\activate           # Windows
```

#### 3. Install dependencies
```bash
pip install -r requirements.txt
pip install pytest              # For testing
```

#### 4. Verify installation
```bash
# Run test suite
python -m pytest tests/ -v

# Should see: 379 tests passing ✅
```

#### 5. Run your first Bayan program
```bash
# Try the hello world example
python -m bayan examples/hello.by

# Try the Web IDE
python web_ide/app.py
# Then open: http://127.0.0.1:5001/ide
```

### Your First Contribution

**Step 1: Find a good first issue**
- Browse [GitHub Issues](https://github.com/mubtakir/nlp_bayan/issues)
- Look for `good-first-issue` or `help-wanted` labels
- Check [DEVELOPER_FEEDBACK_SUMMARY.md](../DEVELOPER_FEEDBACK_SUMMARY.md) for ideas

**Step 2: Set up your development environment**
```bash
# Enable pre-commit hooks (one-time setup)
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit

# Verify hooks work
git add .
git commit -m "test"  # Should run linter
```

**Step 3: Create a feature branch**
```bash
git checkout -b feature/your-feature-name
# OR
git checkout -b fix/bug-description
```

**Step 4: Make your changes**
- Follow the [code style guidelines](#code-style-guidelines)
- Add tests for new features
- Update documentation as needed
- Run linter: `python scripts/bayan_lint_identifiers.py nlp_bayan`

**Step 5: Commit and push**
```bash
git add .
git commit -m "descriptive message"
git push origin your-branch-name
```

**Step 6: Create a pull request**
- Go to GitHub and create a PR
- Fill in the PR template with:
  - What changed
  - Why it changed
  - How to test it
- Wait for review from maintainers

### Development Workflow

```
┌─────────────────────────────────────────┐
│  1. Pick an Issue/Feature               │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  2. Create Branch (feature/fix)         │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  3. Code + Write Tests                  │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  4. Run Linter & Tests Locally          │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  5. Commit (pre-commit hook runs)       │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  6. Push to GitHub                      │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  7. Create Pull Request                 │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  8. CI Runs (linter + tests)            │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  9. Code Review + Feedback              │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  10. Merge! 🎉                          │
└─────────────────────────────────────────┘
```

---

## 🏗️ Architecture Overview

### Project Structure

```
bayan_python_ide14/
├── bayan/                    # Core language implementation
│   ├── bayan/               # Main interpreter package
│   │   ├── lexer.py        # Tokenization
│   │   ├── parser.py       # AST generation
│   │   ├── interpreter.py  # Execution engine
│   │   ├── logical_engine.py  # Prolog-style logic
│   │   └── visualization.py   # Graph export
│   └── core/
│       └── similarity.py   # Similarity engine
│
├── nlp_bayan/               # NLP-specific modules (English-only identifiers)
│   ├── core/               # Core NLP functionality
│   │   └── integrated_kb.bayan  # Knowledge base
│   └── examples/           # NLP demo files
│
├── ai/                      # AI/ML/NLP libraries (Bayan code)
│   ├── morphology.bayan    # Arabic morphology system ⭐ NEW
│   ├── lexicon.bayan       # Concept-to-word mapping
│   ├── nlp.bayan           # NLP tools (tokenization, roots)
│   ├── ml.bayan            # Machine learning algorithms
│   ├── conceptual_*.bayan  # Conceptual LM pipeline
│   └── data.bayan          # Data manipulation
│
├── web_ide/                 # Web-based IDE
│   ├── app.py              # Flask server
│   ├── templates/          # HTML templates
│   │   ├── ide.html       # Main IDE
│   │   └── logic_graph.html  # Graph visualization ⭐ NEW
│   └── static/             # CSS/JS
│
├── docs/                    # Documentation
│   ├── DEVELOPER_GUIDE.md  # This file
│   ├── ARABIC_MORPHOLOGY.md  # Morphology docs ⭐ NEW
│   ├── LOGIC_GRAPH_COMPLETE_GUIDE.md  # Visualization guide
│   └── تعليمية/            # Tutorials (Arabic/English)
│
├── examples/                # Language examples
│   ├── hello.by            # Hello world
│   ├── demo_morphology_logic.bayan  # Morphology demo ⭐ NEW
│   └── *.bayan             # 139+ examples
│
├── tests/                   # Test suite (379 tests)
│   ├── test_*.py           # Python tests
│   └── test_*.bayan        # Bayan tests
│
└── scripts/                 # Utility scripts
    └── bayan_lint_identifiers.py  # Linter
```

### Core Components

#### 1. Language Core (`bayan/bayan/`)

**Lexer (`lexer.py`)**
- Tokenizes Bayan source code
- Supports Arabic and English keywords
- Handles strings, numbers, operators, identifiers

**Parser (`parser.py`)**
- Builds Abstract Syntax Tree (AST)
- Enforces syntax: `:` + `{}` for blocks
- Supports hybrid paradigm mixing

**Interpreter (`interpreter.py`)**
- Executes the AST
- Manages variable scopes
- Handles function calls and class instantiation

**Logical Engine (`logical_engine.py`)**
- Prolog-style inference engine
- Facts, rules, and queries
- Unification and backtracking
- Proof trace export ⭐

#### 2. AI/ML Libraries (`ai/`)

**Morphology System (`morphology.bayan`)** ⭐ NEW
- Pattern application (فاعل، مفعول، etc.)
- Verb conjugation (past, present, imperative)
- Root extraction

**NLP Tools (`nlp.bayan`)**
- Tokenization (Arabic/English)
- Root extraction
- Phonetic analysis
- Naive Bayes classifier

**Machine Learning (`ml.bayan`)**
- KNN, Decision Trees, Random Forest
- Clustering (K-Means, Hierarchical)
- Dimensionality reduction (PCA)
- Neural networks (basic)

**Conceptual LM Pipeline (`conceptual_*.bayan`)**
- Conceptual blueprints
- Circuits (reusable patterns)
- Programs (high-level compositions)
- Surface realization

#### 3. Web IDE (`web_ide/`)

**Flask Application (`app.py`)**
- `/ide` - Main IDE interface
- `/logic_graph` - Graph visualization ⭐ NEW
- `/api/ide/run_logic` - Execute code endpoint

**Logic Graph (`templates/logic_graph.html`)** ⭐ NEW
- D3.js interactive visualization
- Entity/Fact/Event/Rule visualization
- Probability representation
- Contradiction detection

### Data Flow

```
┌──────────────────┐
│  Bayan Source    │ (.by or .bayan file)
│    Code          │
└────────┬─────────┘
         │
         │ 1. Tokenize
         ▼
┌──────────────────┐
│     Lexer        │ → Tokens (IDENTIFIER, NUMBER, KEYWORD, etc.)
└────────┬─────────┘
         │
         │ 2. Parse
         ▼
┌──────────────────┐
│     Parser       │ → AST (HybridBlock, FunctionDef, ClassDef, etc.)
└────────┬─────────┘
         │
         │ 3. Interpret
         ▼
┌──────────────────┐
│  Interpreter     │
└────────┬─────────┘
         │
         ├──────────────┬────────────────┐
         │              │                │
         ▼              ▼                ▼
   ┌──────────┐  ┌────────────┐  ┌────────────┐
   │ Traditional│  │   Logic    │  │  Hybrid    │
   │   Code     │  │  Engine    │  │  Features  │
   │ (Python-   │  │ (Facts,    │  │ (Combined) │
   │  style)    │  │  Rules,    │  │            │
   │            │  │  Queries)  │  │            │
   └──────────┘  └────────────┘  └────────────┘
         │              │                │
         └──────────────┴────────────────┘
                        │
                        ▼
                 ┌──────────────┐
                 │   Output     │
                 └──────────────┘
```

### Key Concepts

#### Hybrid Blocks
All Bayan code runs inside `hybrid { }` blocks:

```bayan
hybrid {
    # Imperative: variables, loops, conditions
    x = 10
    if (x > 5) {
        print("x is large")
    }
    
    # OOP: classes and objects
    class Person: {
        def __init__(self, name): {
            self.name = name
        }
    }
    
    # Logic: facts, rules, queries
    parent("أحمد", "محمد").
    grandparent(?X, ?Z) :- parent(?X, ?Y), parent(?Y, ?Z).
    
    results = query grandparent(?GP, "علي")?
}
```

#### Triple-Paradigm Integration
Bayan seamlessly mixes three programming paradigms:
1. **Imperative**: Variables, functions, loops, conditions
2. **Object-Oriented**: Classes, inheritance, polymorphism
3. **Logic**: Facts, rules, queries, unification

**Example**:
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
        Student("فاطمة", 95)
    ]
    
    # Logic: Query excellent students
    results = query student(?N, ?G), ?G >= 90?
    
    # Imperative: Print results
    for result in (results) {
        print(result["?N"])
    }
}
```

---

## 💡 Recent Features & Integration

### Arabic Morphology System (2025-11-24) ⭐ NEW

**Location**: `ai/morphology.bayan`  
**Documentation**: [docs/ARABIC_MORPHOLOGY.md](ARABIC_MORPHOLOGY.md)  
**Demo**: [examples/demo_morphology_logic.bayan](../examples/demo_morphology_logic.bayan)

**Key Functions**:

1. **`apply_pattern(root, pattern)`** - Generate words from trilateral roots
   ```bayan
   word = apply_pattern("كتب", "فاعل")  # Returns: "كاتب"
   ```

2. **`conjugate_arabic_verb(verb, tense, person)`** - Conjugate verbs
   ```bayan
   past = conjugate_arabic_verb("درس", "past", "3ms")      # "درس"
   present = conjugate_arabic_verb("درس", "present", "3ms") # "يدرس"
   ```

3. **`extract_root(word)`** - Extract trilateral roots
   ```bayan
   root = extract_root("كاتب")  # Returns: "كتب"
   ```

**Integration with Logic**:
```bayan
include("ai/morphology.bayan")

hybrid {
    # Define morphological facts
    fact root_of("كتب", "ك", "ت", "ب").
    fact pattern_meaning("فاعل", "active_participle").
    
    # Use morphology in logic
    word = apply_pattern("كتب", "فاعل")
    assertz(word_form(word, "كتب", "فاعل"))
}
```

### Logic Graph Visualization (2025-11-22) ⭐

**Location**: `web_ide/templates/logic_graph.html`  
**Guide**: [LOGIC_GRAPH_COMPLETE_GUIDE.md](../LOGIC_GRAPH_COMPLETE_GUIDE.md)

**Features**:
- Interactive D3.js visualization
- Entity (green), Event (blue), Rule (purple) nodes
- Probability visualization (opacity/dashing)
- Causal network display
- Contradiction detection

**Usage**:
```bash
# Start the web server
python web_ide/app.py

# Open in browser
http://127.0.0.1:5001/logic_graph
```

**Example Code**:
```bayan
hybrid {
    # Facts with probabilities
    color(sky, blue) [0.9].
    color(grass, green) [1.0].
    
    # Causal rules
    writes_code(?X) :- programmer(?X).
    
    # Query and visualize
    results = query color(?Thing, ?Color)?
}
```

The graph will show:
- Entities as green nodes
- Facts as links
- Rules as purple nodes
- Probabilities as visual styles

### Conceptual LM Pipeline

**Location**: `ai/conceptual_*.bayan`  
**Documentation**: [docs/CONCEPTUAL_CIRCUITS_AND_PROGRAMS.md](CONCEPTUAL_CIRCUITS_AND_PROGRAMS.md)

**Components**:
1. **Conceptual Blueprints** (`conceptual_blueprints.bayan`)
   - Abstract patterns: Action, StateChange, Causal, etc.

2. **Conceptual Circuits** (`conceptual_circuits.bayan`)
   - Reusable micro-scenarios
   - 6 canonical circuits

3. **Meaning Programs** (`conceptual_programs.bayan`)
   - High-level compositions
   - 5 domain-specific programs

4. **Orchestrator** (`conceptual_orchestrator.bayan`)
   - Program selection and dispatch

**Example Usage**:
```bayan
include("ai/conceptual_circuits.bayan")

hybrid {
    # Use a circuit
    result = build_action_state_eval_circuit(
        actor_id="أحمد",
        patient_id="الكتاب",
        action_kind="قراءة",
        state_axis="معرفة",
        before_value=0.3,
        after_value=0.8,
        evaluation_degree="high",
        context_label="تعليم",
        action_intensity=0.9,
        action_probability=1.0
    )
}
```

---

## 📚 Development Guidelines

### English-only Identifiers Policy (scoped to `nlp_bayan/`)

**Why**: Ensure portability and universal collaboration for the NLP model.

**Scope**: Only applies to `nlp_bayan/` directory.

**What's enforced**:
- ✅ Predicate/function/class/variable names must use English characters
- ✅ Arabic is allowed in:
  - String literals (data values)
  - Comments
  - Documentation

**Manual check**:
```bash
python scripts/bayan_lint_identifiers.py nlp_bayan
```

**Example**:
```bayan
# ✅ Correct
def process_text(arabic_text): {
    result = "معالجة: " + arabic_text
    return result
}

# ❌ Wrong (Arabic identifier)
def معالجة_نص(نص): {
    ...
}
```

### Pre-commit Hooks

**Purpose**: Automatically run linter before each commit.

**One-time setup**:
```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
```

**What it does**:
- Runs linter on staged `.bayan`/`.by` files in `nlp_bayan/`
- Blocks commit if violations found
- Shows clear error messages with file:line:col

### CI/CD Workflow

**Location**: `.github/workflows/lint-and-test.yml`

**Triggers**: 
- Push to main
- Pull requests

**Steps**:
1. Checkout code
2. Setup Python 3.11
3. Install dependencies
4. Run linter on `nlp_bayan/`
5. Run full test suite (379 tests)

**View results**: 
- GitHub Actions tab in repository
- Green checkmark = all passed ✅
- Red X = failures (click for details) ❌

### Code Style Guidelines

**Python-like Code**:
- Use 4 spaces for indentation (in blocks)
- Colon `:` followed by braces `{}`
- No semicolons
- Clear variable names

**Logic Code**:
- Predicates in lowercase: `parent(X, Y)`
- Variables start with `?`: `?Name`, `?Age`
- Facts end with `.`
- Rules use `:-`

**Example**:
```bayan
hybrid {
    # Good style
    def calculate_sum(numbers): {
        total = 0
        for num in (numbers) {
            total = total + num
        }
        return total
    }
    
    # Good logic style
    parent("أحمد", "محمد").
    ancestor(?X, ?Y) :- parent(?X, ?Y).
    ancestor(?X, ?Z) :- parent(?X, ?Y), ancestor(?Y, ?Z).
}
```

---

## 🧪 Testing

### Running Tests

**Run all tests**:
```bash
python -m pytest tests/ -v
```

**Run specific test file**:
```bash
python -m pytest tests/test_lexer.py -v
```

**Run with coverage**:
```bash
pytest --cov=bayan --cov-report=html tests/
```

### Test Structure

```
tests/
├── test_lexer.py           # Lexer tests
├── test_parser.py          # Parser tests
├── test_interpreter.py     # Interpreter tests
├── test_logical_engine.py  # Logic tests
├── test_morphology.bayan   # Morphology tests ⭐
└── ...                     # 162 test files total
```

### Writing Tests

**Python tests** (using pytest):
```python
def test_simple_assignment():
    code = """
    hybrid {
        x = 10
    }
    """
    interpreter = run_bayan_code(code)
    assert interpreter.get_variable('x') == 10
```

**Bayan tests** (hybrid blocks):
```bayan
hybrid {
    # Test morphology
    result = apply_pattern("كتب", "فاعل")
    assert result == "كاتب", "Pattern application failed"
    
    print("✅ Test passed")
}
```

### Test Results

Current status: **379 tests passing (100%)** ✅

---

## 🐛 Troubleshooting

### Pre-commit hook not working

**Problem**: Hook doesn't run on commit.

**Solution**:
```bash
# Ensure hooks path is configured
git config core.hooksPath .githooks

# Make hook executable
chmod +x .githooks/pre-commit

# Verify
ls -la .githooks/pre-commit
```

### Linter flags Arabic in code

**Problem**: Linter shows violations for Arabic.

**Check**:
- Is the Arabic in a string literal? ✅ OK
- Is the Arabic in a comment? ✅ OK
- Is the Arabic in an identifier? ❌ Change to English

**Example**:
```bayan
# ❌ Wrong
def معالجة(نص): {
    ...
}

# ✅ Correct
def process(text): {
    message = "معالجة النص"  # Arabic in string is OK
    ...
}
```

### Import errors

**Problem**: `ModuleNotFoundError` when running code.

**Solution**:
```bash
# Make sure you're in project root
cd bayan_python_ide14

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Try again
python -m bayan your_file.by
```

### Web IDE doesn't start

**Problem**: Flask app won't start.

**Solution**:
```bash
# Check if port 5001 is in use
lsof -i :5001

# Kill process if needed
pkill -f "web_ide/app.py"

# Start fresh
python web_ide/app.py
```

### Tests failing

**Problem**: Some tests fail locally.

**Steps**:
1. Update dependencies: `pip install -r requirements.txt`
2. Clear pytest cache: `rm -rf .pytest_cache`
3. Run specific failing test with verbose: `pytest tests/test_name.py -vv`
4. Check for environment issues (Python version, etc.)

---

## 📝 Quick Reference

### Essential Commands

```bash
# Development
python -m bayan file.by                    # Run Bayan file
python web_ide/app.py                      # Start Web IDE
python scripts/bayan_lint_identifiers.py nlp_bayan  # Run linter

# Testing
python -m pytest tests/ -v                 # Run all tests
python -m pytest tests/test_file.py        # Run specific test
pytest --cov=bayan tests/                  # With coverage

# Git workflow
git config core.hooksPath .githooks        # Enable pre-commit hooks
chmod +x .githooks/pre-commit              # Make executable
git checkout -b feature/my-feature         # Create branch
git add .                                  # Stage changes
git commit -m "message"                    # Commit (runs hooks)
git push origin feature/my-feature         # Push branch

# Documentation
python -m http.server 8000                 # Serve docs locally
# Then open http://localhost:8000/docs/
```

### Important Links

- **Repository**: https://github.com/mubtakir/nlp_bayan
- **Issues**: https://github.com/mubtakir/nlp_bayan/issues
- **Roadmap**: [docs/ROADMAP.md](ROADMAP.md)
- **Changelog**: [CHANGELOG.md](../CHANGELOG.md)
- **Developer Feedback**: [DEVELOPER_FEEDBACK_SUMMARY.md](../DEVELOPER_FEEDBACK_SUMMARY.md)

### Key Files

- `README.md` - Project overview and features
- `DEVELOPER_GUIDE.md` - This file (developer reference)
- `LOGIC_GRAPH_COMPLETE_GUIDE.md` - Graph visualization guide
- `ARABIC_MORPHOLOGY.md` - Morphology system documentation
- `CONCEPTUAL_CIRCUITS_AND_PROGRAMS.md` - Conceptual LM architecture

### Quick Tests

```bash
# Test installation
python -c "from bayan import HybridLexer; print('✅ Bayan installed')"

# Test morphology
python -c "import sys; sys.path.insert(0, 'bayan'); from bayan.main import run_file; run_file('examples/demo_morphology_logic.bayan')"

# Test Web IDE
curl http://127.0.0.1:5001/ide
```

---

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

1. **Start small**: Look for `good-first-issue` labels
2. **Ask questions**: Open an issue or discussion
3. **Read the docs**: Familiarize yourself with the codebase
4. **Write tests**: All new features should have tests
5. **Update docs**: Documentation is as important as code

### Ways to Contribute

- 🐛 Report bugs
- ✨ Suggest new features
- 📝 Improve documentation
- 🧪 Write tests
- 💻 Submit code
- 🎨 Design examples
- 🌍 Translate docs
- 📣 Spread the word!

---

## 📞 Getting Help

- **GitHub Issues**: Report bugs or request features
- **Documentation**: Check `docs/` directory
- **Examples**: Browse `examples/` for inspiration
- **Tests**: Look at `tests/` for usage patterns

---

**Last Updated**: 2025-11-24  
**Version**: 2.0  
**Maintainer**: Bayan Development Team

---

*Happy coding!    البرمجة العربية! 🚀*
