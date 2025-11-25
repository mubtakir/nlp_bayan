# Bayan Language Support for Visual Studio Code

<p align="center">
  <img src="https://raw.githubusercontent.com/mubtakir/nlp_bayan/main/gfx/logo_light.svg" alt="Bayan Logo" width="200"/>
</p>

**Bayan** (البيان) is a hybrid programming language that combines traditional programming with logic programming, featuring full bilingual support for Arabic and English.

This extension provides syntax highlighting and code snippets for the Bayan programming language.

## Features

✨ **Comprehensive Syntax Highlighting**
- 200+ keywords (English and Arabic)
- Logical variables (`?X`, `?variable`)
- Multiple keyword categories with distinct colors:
  - Control flow (`if`, `for`, `while`)
  - Logic programming (`hybrid`, `fact`, `rule`, `query`)
  - Entity system (`entity`, `apply`)
  - Temporal operations (`temporal`, `schedule`, `every`)
  - Semantic programming (`meaning`, `knowledge`, `similarity`)
  - Cognitive semantics (`cognitive_entity`, `event`)
  - And many more!

📝 **Code Snippets**
- Function and class definitions
- Control flow structures
- Hybrid logic blocks
- Entity definitions
- Fact and rule declarations
- Medical expert system template
- Arabic snippets support

🌍 **Bilingual Support**
- Full Arabic keyword support: `كيان`, `قاعدة`, `حقيقة`, `دالة`
- Seamless mixing of Arabic and English code
- RTL text rendering support

## Installation

### From VSCode Marketplace (Coming Soon)
1. Open VSCode
2. Go to Extensions (`Ctrl+Shift+X`)
3. Search for "Bayan"
4. Click Install

### From VSIX File
1. Download the `.vsix` file from releases
2. Open VSCode
3. Press `Ctrl+Shift+P` and type "Extensions: Install from VSIX"
4. Select the downloaded file

## Quick Start

### Create a new Bayan file

Create a file with `.bayan` extension and start coding!

### Example: Hello World

```bayan
print("Hello from Bayan!")
print("مرحباً من لغة البيان!")
```

### Example: Hybrid Programming

```bayan
# Object-Oriented Programming
class Person: {
}
{
    def __init__(self, name) {
        self.name = name
    }
    
    def greet() {
        print(f"Hello, {self.name}!")
    }
}

# Logic Programming
hybrid {
    fact parent("Ali", "Ahmed").
    fact parent("Ahmed", "Sara").
    
    rule grandparent(?X, ?Z) :- 
        parent(?X, ?Y), 
        parent(?Y, ?Z).
    
    query grandparent("Ali", ?grandchild).
}
```

### Example: Medical Expert System

```bayan
hybrid {
    # Knowledge base
    fact symptom("حمى", "انفلونزا", 0.8).
    fact symptom("سعال", "انفلونزا", 0.7).
    
    rule possible_disease(?disease) :-
        symptom(?s, ?disease, ?conf),
        has_symptom(?s).
    
    def diagnose(symptoms) {
        for s in (symptoms) {
            assertz(has_symptom(s))
        }
        return query possible_disease(?disease)
    }
}
```

## Code Snippets

Type these prefixes and press `Tab` to expand:

| Prefix | Description |
|--------|-------------|
| `def` | Function definition |
| `class` | Class definition |
| `if` / `ifelse` | If / If-else statement |
| `for` | For loop |
| `while` | While loop |
| `hybrid` | Hybrid logic block |
| `entity` | Entity definition |
| `fact` | Fact declaration |
| `rule` | Rule declaration |
| `query` | Query statement |
| `medical-expert` | Medical expert system template |
| `دالة` | Arabic function definition |
| `كيان` | Arabic entity definition |
| `حقيقة` | Arabic fact declaration |

## Syntax Highlighting Preview

The extension provides rich syntax highlighting with distinct colors for:

- **Keywords**: Control flow, logic, entities, temporal, semantic
- **Strings**: Single, double, and triple-quoted
- **Comments**: Line comments starting with `#`
- **Numbers**: Integer and floating-point
- **Logical Variables**: `?X`, `?variable`
- **Operators**: Arithmetic, comparison, logical, pipeline (`|>`)

## Language Features

- File extensions: `.bayan`, `.by`
- Comment syntax: `# This is a comment`
- Bracket matching: `()`, `{}`, `[]`
- Auto-closing pairs for quotes and brackets
- Code folding support

## Resources

- 📚 [Official Documentation](https://github.com/mubtakir/nlp_bayan#readme)
- 🐛 [Report Issues](https://github.com/mubtakir/nlp_bayan/issues)
- 💻 [Source Code](https://github.com/mubtakir/nlp_bayan)
- 📖 [Language Guide](https://github.com/mubtakir/nlp_bayan/tree/main/docs)
- 📝 [Examples](https://github.com/mubtakir/nlp_bayan/tree/main/examples)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This extension is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Developed with ❤️ for the Bayan programming language community.

---

**Enjoy coding in Bayan! 🚀**

**استمتع بالبرمجة بلغة البيان! 🚀**
