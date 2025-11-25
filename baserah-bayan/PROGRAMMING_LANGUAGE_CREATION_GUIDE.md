# 📚 الدليل الشامل لصناعة لغة برمجية من الصفر
## How to Create a Programming Language from Scratch

**نموذج عملي: لغة البيان (Bayan Programming Language)**

---

## 📖 جدول المحتويات

1. [المقدمة والأساسيات](#المقدمة-والأساسيات)
2. [المرحلة الأولى: التخطيط والتصميم](#المرحلة-الأولى-التخطيط-والتصميم)
3. [المرحلة الثانية: التحليل المعجمي (Lexical Analysis)](#المرحلة-الثانية-التحليل-المعجمي)
4. [المرحلة الثالثة: التحليل النحوي (Syntax Analysis)](#المرحلة-الثالثة-التحليل-النحوي)
5. [المرحلة الرابعة: التحليل الدلالي (Semantic Analysis)](#المرحلة-الرابعة-التحليل-الدلالي)
6. [المرحلة الخامسة: توليد الكود (Code Generation)](#المرحلة-الخامسة-توليد-الكود)
7. [المرحلة السادسة: التحسين والتطوير](#المرحلة-السادسة-التحسين-والتطوير)
8. [الملفات المطلوبة والبنية](#الملفات-المطلوبة-والبنية)
9. [أدوات وتقنيات متقدمة](#أدوات-وتقنيات-متقدمة)
10. [الخلاصة والموارد](#الخلاصة-والموارد)

---

## 🎯 المقدمة والأساسيات

### ما هي لغة البرمجة؟

لغة البرمجة هي **نظام رسمي** يتكون من:
- **بناء الجملة (Syntax)**: القواعد التي تحدد كيفية كتابة الكود
- **الدلالات (Semantics)**: المعنى والسلوك لكل تعليمة
- **المترجم/المفسر (Compiler/Interpreter)**: الأداة التي تحول الكود إلى تعليمات قابلة للتنفيذ

### لماذا نصنع لغة برمجية جديدة؟

1. **حل مشكلة محددة**: لغة متخصصة لمجال معين
2. **دعم لغة طبيعية**: مثل العربية في لغة البيان
3. **نموذج برمجي جديد**: paradigm جديد
4. **التعليم والبحث**: فهم عميق لكيفية عمل اللغات

### نموذجنا: لغة البيان

**لغة البيان** هي لغة برمجية:
- ✅ **ثنائية اللغة**: تدعم العربية والإنجليزية
- ✅ **هجينة**: تجمع بين البرمجة الإجرائية والكائنية والمنطقية
- ✅ **تُترجم إلى JavaScript**: تستفيد من نظام JavaScript البيئي
- ✅ **امتداد الملف**: `.bn`

---

## 🎨 المرحلة الأولى: التخطيط والتصميم

### 1.1 تحديد الأهداف

قبل البدء، يجب الإجابة على:

**أسئلة أساسية:**
```
❓ ما هو الهدف من اللغة؟
   → لغة البيان: دعم العربية + نموذج هجين

❓ من هو الجمهور المستهدف؟
   → لغة البيان: المبرمجون العرب + الباحثون

❓ ما هو نموذج البرمجة (Paradigm)؟
   → لغة البيان: إجرائي + كائني + منطقي

❓ هل ستكون مترجمة أم مفسرة؟
   → لغة البيان: مترجمة إلى JavaScript

❓ ما هي اللغة المستهدفة (Target)?
   → لغة البيان: JavaScript (ES2020)
```

### 1.2 تصميم بناء الجملة (Syntax Design)

**خطوات التصميم:**

#### أ) تحديد الكلمات المفتاحية (Keywords)

```javascript
// لغة البيان - نسخة ثنائية اللغة
const KEYWORDS = {
    // التحكم في التدفق
    'if': 'إذا',
    'else': 'وإلا',
    'while': 'بينما',
    'for': 'لكل',
    
    // التعريفات
    'let': 'متغير',
    'const': 'ثابت',
    'function': 'دالة',
    'class': 'صنف',
    
    // القيم
    'true': 'صحيح',
    'false': 'خطأ',
    'null': 'عدم',
    
    // العمليات
    'return': 'أرجع',
    'break': 'اكسر',
    'continue': 'تابع'
};
```

#### ب) تحديد العمليات (Operators)

```javascript
const OPERATORS = {
    // حسابية
    '+': 'جمع',
    '-': 'طرح',
    '*': 'ضرب',
    '/': 'قسمة',
    
    // مقارنة
    '==': 'يساوي',
    '!=': 'لا يساوي',
    '>': 'أكبر من',
    '<': 'أصغر من',
    
    // منطقية
    '&&': 'و',
    '||': 'أو',
    '!': 'ليس'
};
```

#### ج) تصميم البنية النحوية

**مثال: جملة if في لغة البيان**

```bayan
// النسخة الإنجليزية
if (x > 5) {
    print("Greater");
}

// النسخة العربية
إذا (x > 5) {
    اطبع("أكبر");
}
```

### 1.3 تحديد أنواع البيانات (Data Types)

```javascript
const DATA_TYPES = {
    // أنواع أساسية
    NUMBER: 'رقم',
    STRING: 'نص',
    BOOLEAN: 'منطقي',
    NULL: 'عدم',
    
    // أنواع مركبة
    ARRAY: 'مصفوفة',
    OBJECT: 'كائن',
    FUNCTION: 'دالة'
};
```

### 1.4 كتابة المواصفات (Specification Document)

**ملف: `BAYAN_SPECIFICATION.md`**

يجب أن يحتوي على:
- ✅ قواعد بناء الجملة الكاملة (Full Grammar)
- ✅ أمثلة لكل ميزة
- ✅ الدلالات (Semantics) لكل تعليمة
- ✅ معالجة الأخطاء

---

## 🔍 المرحلة الثانية: التحليل المعجمي (Lexical Analysis)

### 2.1 ما هو التحليل المعجمي؟

**التحليل المعجمي (Lexer/Tokenizer)** هو المرحلة الأولى من المترجم:
- يقرأ الكود المصدري كنص
- يقسمه إلى **رموز (Tokens)**
- يتجاهل المسافات والتعليقات

**مثال:**

```bayan
متغير x = 10;
```

**يتحول إلى:**

```javascript
[
    { type: 'KEYWORD', value: 'متغير' },
    { type: 'IDENTIFIER', value: 'x' },
    { type: 'OPERATOR', value: '=' },
    { type: 'NUMBER', value: '10' },
    { type: 'SEMICOLON', value: ';' }
]
```

### 2.2 أنواع الرموز (Token Types)

```javascript
const TOKEN_TYPES = {
    // الكلمات المفتاحية
    KEYWORD: 'KEYWORD',
    
    // المعرفات (أسماء المتغيرات والدوال)
    IDENTIFIER: 'IDENTIFIER',
    
    // القيم الثابتة
    NUMBER: 'NUMBER',
    STRING: 'STRING',
    BOOLEAN: 'BOOLEAN',
    NULL: 'NULL',
    
    // العمليات
    OPERATOR: 'OPERATOR',
    
    // الرموز الخاصة
    LPAREN: '(',      // (
    RPAREN: ')',      // )
    LBRACE: '{',      // {
    RBRACE: '}',      // }
    LBRACKET: '[',    // [
    RBRACKET: ']',    // ]
    SEMICOLON: ';',
    COMMA: ',',
    DOT: '.',
    COLON: ':',
    
    // نهاية الملف
    EOF: 'EOF'
};
```

### 2.3 بناء المحلل المعجمي (Lexer Implementation)

**ملف: `lexer.js`**

```javascript
class Lexer {
    constructor(sourceCode) {
        this.source = sourceCode;
        this.position = 0;
        this.currentChar = this.source[0];
        this.line = 1;
        this.column = 1;
    }

    // تقدم إلى الحرف التالي
    advance() {
        this.position++;
        this.column++;
        
        if (this.position >= this.source.length) {
            this.currentChar = null; // نهاية الملف
        } else {
            this.currentChar = this.source[this.position];
            
            // تتبع رقم السطر
            if (this.currentChar === '\n') {
                this.line++;
                this.column = 1;
            }
        }
    }

    // تجاوز المسافات البيضاء
    skipWhitespace() {
        while (this.currentChar && /\s/.test(this.currentChar)) {
            this.advance();
        }
    }

    // تجاوز التعليقات
    skipComment() {
        if (this.currentChar === '/' && this.peek() === '/') {
            // تعليق سطر واحد
            while (this.currentChar && this.currentChar !== '\n') {
                this.advance();
            }
        } else if (this.currentChar === '/' && this.peek() === '*') {
            // تعليق متعدد الأسطر
            this.advance(); // /
            this.advance(); // *
            
            while (this.currentChar) {
                if (this.currentChar === '*' && this.peek() === '/') {
                    this.advance(); // *
                    this.advance(); // /
                    break;
                }
                this.advance();
            }
        }
    }

    // النظر إلى الحرف التالي بدون التقدم
    peek(offset = 1) {
        const peekPos = this.position + offset;
        if (peekPos >= this.source.length) {
            return null;
        }
        return this.source[peekPos];
    }

    // قراءة رقم
    readNumber() {
        let numStr = '';
        let hasDot = false;
        
        while (this.currentChar && (/\d/.test(this.currentChar) || this.currentChar === '.')) {
            if (this.currentChar === '.') {
                if (hasDot) break; // رقم عشري واحد فقط
                hasDot = true;
            }
            numStr += this.currentChar;
            this.advance();
        }
        
        return {
            type: TOKEN_TYPES.NUMBER,
            value: parseFloat(numStr),
            line: this.line,
            column: this.column
        };
    }

    // قراءة نص (string)
    readString(quote) {
        let str = '';
        this.advance(); // تجاوز علامة الاقتباس الأولى
        
        while (this.currentChar && this.currentChar !== quote) {
            if (this.currentChar === '\\') {
                // معالجة الأحرف الخاصة
                this.advance();
                const escapeChars = {
                    'n': '\n',
                    't': '\t',
                    'r': '\r',
                    '\\': '\\',
                    '"': '"',
                    "'": "'"
                };
                str += escapeChars[this.currentChar] || this.currentChar;
            } else {
                str += this.currentChar;
            }
            this.advance();
        }
        
        this.advance(); // تجاوز علامة الاقتباس الأخيرة
        
        return {
            type: TOKEN_TYPES.STRING,
            value: str,
            line: this.line,
            column: this.column
        };
    }

    // قراءة معرف أو كلمة مفتاحية
    readIdentifier() {
        let id = '';
        
        // المعرف يبدأ بحرف أو _ ويحتوي على حروف وأرقام و_
        while (this.currentChar && /[\w\u0600-\u06FF_]/.test(this.currentChar)) {
            id += this.currentChar;
            this.advance();
        }
        
        // التحقق إذا كانت كلمة مفتاحية
        const keywords = {
            // إنجليزي
            'if': 'KEYWORD',
            'else': 'KEYWORD',
            'while': 'KEYWORD',
            'for': 'KEYWORD',
            'function': 'KEYWORD',
            'return': 'KEYWORD',
            'let': 'KEYWORD',
            'const': 'KEYWORD',
            'class': 'KEYWORD',
            'true': 'BOOLEAN',
            'false': 'BOOLEAN',
            'null': 'NULL',
            
            // عربي
            'إذا': 'KEYWORD',
            'وإلا': 'KEYWORD',
            'بينما': 'KEYWORD',
            'لكل': 'KEYWORD',
            'دالة': 'KEYWORD',
            'أرجع': 'KEYWORD',
            'متغير': 'KEYWORD',
            'ثابت': 'KEYWORD',
            'صنف': 'KEYWORD',
            'صحيح': 'BOOLEAN',
            'خطأ': 'BOOLEAN',
            'عدم': 'NULL'
        };
        
        const type = keywords[id] || TOKEN_TYPES.IDENTIFIER;
        
        return {
            type: type,
            value: id,
            line: this.line,
            column: this.column
        };
    }

    // الحصول على الرمز التالي
    getNextToken() {
        while (this.currentChar) {
            // تجاوز المسافات
            if (/\s/.test(this.currentChar)) {
                this.skipWhitespace();
                continue;
            }
            
            // تجاوز التعليقات
            if (this.currentChar === '/' && (this.peek() === '/' || this.peek() === '*')) {
                this.skipComment();
                continue;
            }
            
            // أرقام
            if (/\d/.test(this.currentChar)) {
                return this.readNumber();
            }
            
            // نصوص
            if (this.currentChar === '"' || this.currentChar === "'") {
                return this.readString(this.currentChar);
            }
            
            // معرفات وكلمات مفتاحية
            if (/[a-zA-Z\u0600-\u06FF_]/.test(this.currentChar)) {
                return this.readIdentifier();
            }
            
            // عمليات ورموز خاصة
            const char = this.currentChar;
            this.advance();
            
            // عمليات مركبة
            if (char === '=' && this.currentChar === '=') {
                this.advance();
                return { type: TOKEN_TYPES.OPERATOR, value: '==', line: this.line, column: this.column };
            }
            if (char === '!' && this.currentChar === '=') {
                this.advance();
                return { type: TOKEN_TYPES.OPERATOR, value: '!=', line: this.line, column: this.column };
            }
            if (char === '>' && this.currentChar === '=') {
                this.advance();
                return { type: TOKEN_TYPES.OPERATOR, value: '>=', line: this.line, column: this.column };
            }
            if (char === '<' && this.currentChar === '=') {
                this.advance();
                return { type: TOKEN_TYPES.OPERATOR, value: '<=', line: this.line, column: this.column };
            }
            if (char === '&' && this.currentChar === '&') {
                this.advance();
                return { type: TOKEN_TYPES.OPERATOR, value: '&&', line: this.line, column: this.column };
            }
            if (char === '|' && this.currentChar === '|') {
                this.advance();
                return { type: TOKEN_TYPES.OPERATOR, value: '||', line: this.line, column: this.column };
            }
            
            // رموز مفردة
            const singleTokens = {
                '(': TOKEN_TYPES.LPAREN,
                ')': TOKEN_TYPES.RPAREN,
                '{': TOKEN_TYPES.LBRACE,
                '}': TOKEN_TYPES.RBRACE,
                '[': TOKEN_TYPES.LBRACKET,
                ']': TOKEN_TYPES.RBRACKET,
                ';': TOKEN_TYPES.SEMICOLON,
                ',': TOKEN_TYPES.COMMA,
                '.': TOKEN_TYPES.DOT,
                ':': TOKEN_TYPES.COLON,
                '+': TOKEN_TYPES.OPERATOR,
                '-': TOKEN_TYPES.OPERATOR,
                '*': TOKEN_TYPES.OPERATOR,
                '/': TOKEN_TYPES.OPERATOR,
                '=': TOKEN_TYPES.OPERATOR,
                '>': TOKEN_TYPES.OPERATOR,
                '<': TOKEN_TYPES.OPERATOR,
                '!': TOKEN_TYPES.OPERATOR
            };
            
            if (singleTokens[char]) {
                return { type: singleTokens[char], value: char, line: this.line, column: this.column };
            }
            
            // رمز غير معروف
            throw new Error(`Unexpected character '${char}' at line ${this.line}, column ${this.column}`);
        }
        
        // نهاية الملف
        return { type: TOKEN_TYPES.EOF, value: null, line: this.line, column: this.column };
    }

    // الحصول على جميع الرموز
    tokenize() {
        const tokens = [];
        let token = this.getNextToken();
        
        while (token.type !== TOKEN_TYPES.EOF) {
            tokens.push(token);
            token = this.getNextToken();
        }
        
        tokens.push(token); // إضافة EOF
        return tokens;
    }
}

module.exports = { Lexer, TOKEN_TYPES };
```

### 2.4 اختبار المحلل المعجمي

**ملف: `test-lexer.js`**

```javascript
const { Lexer } = require('./lexer');

// كود بيان للاختبار
const code = `
متغير x = 10;
إذا (x > 5) {
    اطبع("أكبر من خمسة");
}
`;

const lexer = new Lexer(code);
const tokens = lexer.tokenize();

console.log('Tokens:');
tokens.forEach(token => {
    console.log(`  ${token.type}: ${token.value} (Line ${token.line})`);
});
```

---

## 🌳 المرحلة الثالثة: التحليل النحوي (Syntax Analysis)

### 3.1 ما هو التحليل النحوي؟

**التحليل النحوي (Parser)** يأخذ الرموز من المحلل المعجمي ويبني **شجرة بناء الجملة المجردة (Abstract Syntax Tree - AST)**.

**مثال:**

```bayan
متغير x = 5 + 3;
```

**AST:**

```
VariableDeclaration
├── name: "x"
└── value: BinaryExpression
    ├── operator: "+"
    ├── left: NumberLiteral(5)
    └── right: NumberLiteral(3)
```

### 3.2 تعريف القواعد النحوية (Grammar Definition)

**ملف: `grammar.bnf`** (Backus-Naur Form)

```bnf
Program         ::= Statement*

Statement       ::= VariableDecl
                  | FunctionDecl
                  | ClassDecl
                  | IfStatement
                  | WhileStatement
                  | ForStatement
                  | ReturnStatement
                  | ExpressionStatement

VariableDecl    ::= ('let' | 'متغير' | 'const' | 'ثابت') Identifier '=' Expression ';'

FunctionDecl    ::= ('function' | 'دالة') Identifier '(' Parameters? ')' Block

IfStatement     ::= ('if' | 'إذا') '(' Expression ')' Block ('else' | 'وإلا' Block)?

WhileStatement  ::= ('while' | 'بينما') '(' Expression ')' Block

Expression      ::= Assignment

Assignment      ::= LogicalOr ('=' Assignment)?

LogicalOr       ::= LogicalAnd (('||' | 'أو') LogicalAnd)*

LogicalAnd      ::= Equality (('&&' | 'و') Equality)*

Equality        ::= Comparison (('==' | '!=') Comparison)*

Comparison      ::= Addition (('>' | '<' | '>=' | '<=') Addition)*

Addition        ::= Multiplication (('+' | '-') Multiplication)*

Multiplication  ::= Unary (('*' | '/') Unary)*

Unary           ::= ('!' | '-') Unary | Primary

Primary         ::= Number
                  | String
                  | Boolean
                  | Null
                  | Identifier
                  | '(' Expression ')'
                  | FunctionCall
                  | ArrayLiteral
                  | ObjectLiteral

FunctionCall    ::= Identifier '(' Arguments? ')'

Block           ::= '{' Statement* '}'
```

### 3.3 بناء المحلل النحوي (Parser Implementation)

**ملف: `parser.js`**

```javascript
class Parser {
    constructor(tokens) {
        this.tokens = tokens;
        this.position = 0;
        this.currentToken = this.tokens[0];
    }

    // التقدم إلى الرمز التالي
    advance() {
        this.position++;
        if (this.position < this.tokens.length) {
            this.currentToken = this.tokens[this.position];
        }
    }

    // التحقق من نوع الرمز الحالي
    check(type) {
        return this.currentToken.type === type;
    }

    // استهلاك رمز من نوع معين
    consume(type, errorMessage) {
        if (this.check(type)) {
            const token = this.currentToken;
            this.advance();
            return token;
        }
        throw new Error(`${errorMessage} at line ${this.currentToken.line}`);
    }

    // تحليل البرنامج الكامل
    parse() {
        const statements = [];

        while (!this.check(TOKEN_TYPES.EOF)) {
            statements.push(this.parseStatement());
        }

        return {
            type: 'Program',
            body: statements
        };
    }

    // تحليل جملة
    parseStatement() {
        // تعريف متغير
        if (this.currentToken.value === 'let' || this.currentToken.value === 'متغير' ||
            this.currentToken.value === 'const' || this.currentToken.value === 'ثابت') {
            return this.parseVariableDeclaration();
        }

        // تعريف دالة
        if (this.currentToken.value === 'function' || this.currentToken.value === 'دالة') {
            return this.parseFunctionDeclaration();
        }

        // جملة if
        if (this.currentToken.value === 'if' || this.currentToken.value === 'إذا') {
            return this.parseIfStatement();
        }

        // جملة while
        if (this.currentToken.value === 'while' || this.currentToken.value === 'بينما') {
            return this.parseWhileStatement();
        }

        // جملة return
        if (this.currentToken.value === 'return' || this.currentToken.value === 'أرجع') {
            return this.parseReturnStatement();
        }

        // جملة تعبير
        return this.parseExpressionStatement();
    }

    // تحليل تعريف متغير
    parseVariableDeclaration() {
        const kind = this.currentToken.value;
        this.advance();

        const name = this.consume(TOKEN_TYPES.IDENTIFIER, 'Expected variable name').value;

        this.consume(TOKEN_TYPES.OPERATOR, 'Expected =');

        const value = this.parseExpression();

        this.consume(TOKEN_TYPES.SEMICOLON, 'Expected ;');

        return {
            type: 'VariableDeclaration',
            kind: kind,
            name: name,
            value: value
        };
    }

    // تحليل تعريف دالة
    parseFunctionDeclaration() {
        this.advance(); // تجاوز 'function' أو 'دالة'

        const name = this.consume(TOKEN_TYPES.IDENTIFIER, 'Expected function name').value;

        this.consume(TOKEN_TYPES.LPAREN, 'Expected (');

        const params = [];
        if (!this.check(TOKEN_TYPES.RPAREN)) {
            do {
                if (this.check(TOKEN_TYPES.COMMA)) {
                    this.advance();
                }
                params.push(this.consume(TOKEN_TYPES.IDENTIFIER, 'Expected parameter name').value);
            } while (this.check(TOKEN_TYPES.COMMA));
        }

        this.consume(TOKEN_TYPES.RPAREN, 'Expected )');

        const body = this.parseBlock();

        return {
            type: 'FunctionDeclaration',
            name: name,
            params: params,
            body: body
        };
    }

    // تحليل جملة if
    parseIfStatement() {
        this.advance(); // تجاوز 'if' أو 'إذا'

        this.consume(TOKEN_TYPES.LPAREN, 'Expected (');
        const condition = this.parseExpression();
        this.consume(TOKEN_TYPES.RPAREN, 'Expected )');

        const thenBranch = this.parseBlock();

        let elseBranch = null;
        if (this.currentToken.value === 'else' || this.currentToken.value === 'وإلا') {
            this.advance();
            elseBranch = this.parseBlock();
        }

        return {
            type: 'IfStatement',
            condition: condition,
            thenBranch: thenBranch,
            elseBranch: elseBranch
        };
    }

    // تحليل كتلة
    parseBlock() {
        this.consume(TOKEN_TYPES.LBRACE, 'Expected {');

        const statements = [];
        while (!this.check(TOKEN_TYPES.RBRACE) && !this.check(TOKEN_TYPES.EOF)) {
            statements.push(this.parseStatement());
        }

        this.consume(TOKEN_TYPES.RBRACE, 'Expected }');

        return {
            type: 'BlockStatement',
            body: statements
        };
    }

    // تحليل تعبير
    parseExpression() {
        return this.parseAssignment();
    }

    // تحليل إسناد
    parseAssignment() {
        let expr = this.parseLogicalOr();

        if (this.currentToken.value === '=') {
            this.advance();
            const value = this.parseAssignment();
            return {
                type: 'AssignmentExpression',
                left: expr,
                right: value
            };
        }

        return expr;
    }

    // تحليل OR منطقي
    parseLogicalOr() {
        let left = this.parseLogicalAnd();

        while (this.currentToken.value === '||' || this.currentToken.value === 'أو') {
            const operator = this.currentToken.value;
            this.advance();
            const right = this.parseLogicalAnd();
            left = {
                type: 'BinaryExpression',
                operator: operator,
                left: left,
                right: right
            };
        }

        return left;
    }

    // تحليل AND منطقي
    parseLogicalAnd() {
        let left = this.parseEquality();

        while (this.currentToken.value === '&&' || this.currentToken.value === 'و') {
            const operator = this.currentToken.value;
            this.advance();
            const right = this.parseEquality();
            left = {
                type: 'BinaryExpression',
                operator: operator,
                left: left,
                right: right
            };
        }

        return left;
    }

    // تحليل مساواة
    parseEquality() {
        let left = this.parseComparison();

        while (this.currentToken.value === '==' || this.currentToken.value === '!=') {
            const operator = this.currentToken.value;
            this.advance();
            const right = this.parseComparison();
            left = {
                type: 'BinaryExpression',
                operator: operator,
                left: left,
                right: right
            };
        }

        return left;
    }

    // تحليل مقارنة
    parseComparison() {
        let left = this.parseAddition();

        while (['>', '<', '>=', '<='].includes(this.currentToken.value)) {
            const operator = this.currentToken.value;
            this.advance();
            const right = this.parseAddition();
            left = {
                type: 'BinaryExpression',
                operator: operator,
                left: left,
                right: right
            };
        }

        return left;
    }

    // تحليل جمع وطرح
    parseAddition() {
        let left = this.parseMultiplication();

        while (this.currentToken.value === '+' || this.currentToken.value === '-') {
            const operator = this.currentToken.value;
            this.advance();
            const right = this.parseMultiplication();
            left = {
                type: 'BinaryExpression',
                operator: operator,
                left: left,
                right: right
            };
        }

        return left;
    }

    // تحليل ضرب وقسمة
    parseMultiplication() {
        let left = this.parseUnary();

        while (this.currentToken.value === '*' || this.currentToken.value === '/') {
            const operator = this.currentToken.value;
            this.advance();
            const right = this.parseUnary();
            left = {
                type: 'BinaryExpression',
                operator: operator,
                left: left,
                right: right
            };
        }

        return left;
    }

    // تحليل عملية أحادية
    parseUnary() {
        if (this.currentToken.value === '!' || this.currentToken.value === '-') {
            const operator = this.currentToken.value;
            this.advance();
            const operand = this.parseUnary();
            return {
                type: 'UnaryExpression',
                operator: operator,
                operand: operand
            };
        }

        return this.parsePrimary();
    }

    // تحليل قيمة أساسية
    parsePrimary() {
        // رقم
        if (this.check(TOKEN_TYPES.NUMBER)) {
            const value = this.currentToken.value;
            this.advance();
            return { type: 'NumberLiteral', value: value };
        }

        // نص
        if (this.check(TOKEN_TYPES.STRING)) {
            const value = this.currentToken.value;
            this.advance();
            return { type: 'StringLiteral', value: value };
        }

        // قيمة منطقية
        if (this.check(TOKEN_TYPES.BOOLEAN)) {
            const value = this.currentToken.value === 'true' || this.currentToken.value === 'صحيح';
            this.advance();
            return { type: 'BooleanLiteral', value: value };
        }

        // null
        if (this.check(TOKEN_TYPES.NULL)) {
            this.advance();
            return { type: 'NullLiteral', value: null };
        }

        // معرف أو استدعاء دالة
        if (this.check(TOKEN_TYPES.IDENTIFIER)) {
            const name = this.currentToken.value;
            this.advance();

            // استدعاء دالة
            if (this.check(TOKEN_TYPES.LPAREN)) {
                this.advance();

                const args = [];
                if (!this.check(TOKEN_TYPES.RPAREN)) {
                    do {
                        if (this.check(TOKEN_TYPES.COMMA)) {
                            this.advance();
                        }
                        args.push(this.parseExpression());
                    } while (this.check(TOKEN_TYPES.COMMA));
                }

                this.consume(TOKEN_TYPES.RPAREN, 'Expected )');

                return {
                    type: 'CallExpression',
                    callee: name,
                    arguments: args
                };
            }

            // مجرد معرف
            return { type: 'Identifier', name: name };
        }

        // تعبير بين أقواس
        if (this.check(TOKEN_TYPES.LPAREN)) {
            this.advance();
            const expr = this.parseExpression();
            this.consume(TOKEN_TYPES.RPAREN, 'Expected )');
            return expr;
        }

        throw new Error(`Unexpected token ${this.currentToken.value} at line ${this.currentToken.line}`);
    }

    // تحليل جملة return
    parseReturnStatement() {
        this.advance(); // تجاوز 'return' أو 'أرجع'

        let value = null;
        if (!this.check(TOKEN_TYPES.SEMICOLON)) {
            value = this.parseExpression();
        }

        this.consume(TOKEN_TYPES.SEMICOLON, 'Expected ;');

        return {
            type: 'ReturnStatement',
            value: value
        };
    }

    // تحليل جملة تعبير
    parseExpressionStatement() {
        const expr = this.parseExpression();
        this.consume(TOKEN_TYPES.SEMICOLON, 'Expected ;');
        return {
            type: 'ExpressionStatement',
            expression: expr
        };
    }

    // تحليل جملة while
    parseWhileStatement() {
        this.advance(); // تجاوز 'while' أو 'بينما'

        this.consume(TOKEN_TYPES.LPAREN, 'Expected (');
        const condition = this.parseExpression();
        this.consume(TOKEN_TYPES.RPAREN, 'Expected )');

        const body = this.parseBlock();

        return {
            type: 'WhileStatement',
            condition: condition,
            body: body
        };
    }
}

module.exports = { Parser };
```

### 3.4 اختبار المحلل النحوي

**ملف: `test-parser.js`**

```javascript
const { Lexer } = require('./lexer');
const { Parser } = require('./parser');

const code = `
متغير x = 10;
إذا (x > 5) {
    اطبع("أكبر");
}
`;

const lexer = new Lexer(code);
const tokens = lexer.tokenize();

const parser = new Parser(tokens);
const ast = parser.parse();

console.log('AST:');
console.log(JSON.stringify(ast, null, 2));
```

---

## 🔬 المرحلة الرابعة: التحليل الدلالي (Semantic Analysis)

### 4.1 ما هو التحليل الدلالي؟

**التحليل الدلالي** يتحقق من:
- ✅ **التحقق من الأنواع (Type Checking)**: هل العمليات صحيحة؟
- ✅ **التحقق من النطاق (Scope Checking)**: هل المتغيرات معرفة؟
- ✅ **التحقق من الدلالات**: هل الكود منطقي؟

### 4.2 بناء محلل دلالي

**ملف: `semantic-analyzer.js`**

```javascript
class SemanticAnalyzer {
    constructor() {
        this.scopes = [{}]; // مكدس النطاقات
        this.errors = [];
    }

    // دخول نطاق جديد
    enterScope() {
        this.scopes.push({});
    }

    // الخروج من النطاق
    exitScope() {
        this.scopes.pop();
    }

    // تعريف متغير في النطاق الحالي
    defineVariable(name, type) {
        const currentScope = this.scopes[this.scopes.length - 1];

        if (currentScope[name]) {
            this.errors.push(`Variable '${name}' already defined in this scope`);
            return false;
        }

        currentScope[name] = { type: type };
        return true;
    }

    // البحث عن متغير في جميع النطاقات
    lookupVariable(name) {
        for (let i = this.scopes.length - 1; i >= 0; i--) {
            if (this.scopes[i][name]) {
                return this.scopes[i][name];
            }
        }
        return null;
    }

    // تحليل البرنامج
    analyze(ast) {
        this.visit(ast);
        return {
            success: this.errors.length === 0,
            errors: this.errors
        };
    }

    // زيارة عقدة في AST
    visit(node) {
        const methodName = `visit${node.type}`;
        if (this[methodName]) {
            return this[methodName](node);
        }
        throw new Error(`No visit method for ${node.type}`);
    }

    // زيارة البرنامج
    visitProgram(node) {
        node.body.forEach(statement => this.visit(statement));
    }

    // زيارة تعريف متغير
    visitVariableDeclaration(node) {
        const valueType = this.visit(node.value);
        this.defineVariable(node.name, valueType);
    }

    // زيارة تعريف دالة
    visitFunctionDeclaration(node) {
        this.defineVariable(node.name, 'function');

        this.enterScope();
        node.params.forEach(param => {
            this.defineVariable(param, 'any');
        });
        this.visit(node.body);
        this.exitScope();
    }

    // زيارة جملة if
    visitIfStatement(node) {
        const conditionType = this.visit(node.condition);

        if (conditionType !== 'boolean' && conditionType !== 'any') {
            this.errors.push('If condition must be boolean');
        }

        this.enterScope();
        this.visit(node.thenBranch);
        this.exitScope();

        if (node.elseBranch) {
            this.enterScope();
            this.visit(node.elseBranch);
            this.exitScope();
        }
    }

    // زيارة كتلة
    visitBlockStatement(node) {
        node.body.forEach(statement => this.visit(statement));
    }

    // زيارة تعبير ثنائي
    visitBinaryExpression(node) {
        const leftType = this.visit(node.left);
        const rightType = this.visit(node.right);

        // عمليات حسابية
        if (['+', '-', '*', '/'].includes(node.operator)) {
            if (leftType === 'number' && rightType === 'number') {
                return 'number';
            }
            if (node.operator === '+' && (leftType === 'string' || rightType === 'string')) {
                return 'string';
            }
            this.errors.push(`Invalid operands for ${node.operator}`);
            return 'any';
        }

        // عمليات مقارنة
        if (['>', '<', '>=', '<=', '==', '!='].includes(node.operator)) {
            return 'boolean';
        }

        // عمليات منطقية
        if (['&&', '||', 'و', 'أو'].includes(node.operator)) {
            return 'boolean';
        }

        return 'any';
    }

    // زيارة معرف
    visitIdentifier(node) {
        const variable = this.lookupVariable(node.name);

        if (!variable) {
            this.errors.push(`Undefined variable '${node.name}'`);
            return 'any';
        }

        return variable.type;
    }

    // زيارة قيم ثابتة
    visitNumberLiteral(node) { return 'number'; }
    visitStringLiteral(node) { return 'string'; }
    visitBooleanLiteral(node) { return 'boolean'; }
    visitNullLiteral(node) { return 'null'; }

    // زيارة استدعاء دالة
    visitCallExpression(node) {
        const func = this.lookupVariable(node.callee);

        if (!func) {
            this.errors.push(`Undefined function '${node.callee}'`);
        }

        node.arguments.forEach(arg => this.visit(arg));

        return 'any';
    }

    // زيارة جملة return
    visitReturnStatement(node) {
        if (node.value) {
            this.visit(node.value);
        }
    }

    // زيارة جملة تعبير
    visitExpressionStatement(node) {
        this.visit(node.expression);
    }

    // زيارة جملة while
    visitWhileStatement(node) {
        const conditionType = this.visit(node.condition);

        if (conditionType !== 'boolean' && conditionType !== 'any') {
            this.errors.push('While condition must be boolean');
        }

        this.enterScope();
        this.visit(node.body);
        this.exitScope();
    }

    // زيارة تعبير إسناد
    visitAssignmentExpression(node) {
        const rightType = this.visit(node.right);

        if (node.left.type === 'Identifier') {
            const variable = this.lookupVariable(node.left.name);
            if (!variable) {
                this.errors.push(`Cannot assign to undefined variable '${node.left.name}'`);
            }
        }

        return rightType;
    }

    // زيارة تعبير أحادي
    visitUnaryExpression(node) {
        const operandType = this.visit(node.operand);

        if (node.operator === '!') {
            return 'boolean';
        }
        if (node.operator === '-') {
            if (operandType !== 'number' && operandType !== 'any') {
                this.errors.push('Unary minus requires number');
            }
            return 'number';
        }

        return 'any';
    }
}

module.exports = { SemanticAnalyzer };
```

---

## ⚙️ المرحلة الخامسة: توليد الكود (Code Generation)

### 5.1 ما هو توليد الكود؟

**مولد الكود (Code Generator)** يحول AST إلى كود في اللغة المستهدفة (JavaScript في حالة لغة البيان).

### 5.2 بناء مولد الكود

**ملف: `code-generator.js`**

```javascript
class CodeGenerator {
    constructor() {
        this.output = '';
        this.indentLevel = 0;
        this.indentString = '    '; // 4 مسافات
    }

    // إضافة سطر مع المسافة البادئة
    emit(code) {
        const indent = this.indentString.repeat(this.indentLevel);
        this.output += indent + code + '\n';
    }

    // زيادة المسافة البادئة
    indent() {
        this.indentLevel++;
    }

    // تقليل المسافة البادئة
    dedent() {
        this.indentLevel--;
    }

    // توليد الكود من AST
    generate(ast) {
        this.output = '';
        this.indentLevel = 0;

        // إضافة تعليق في البداية
        this.emit('// Generated by Bayan Compiler');
        this.emit('// Target: JavaScript ES2020');
        this.emit('');

        this.visit(ast);

        return this.output;
    }

    // زيارة عقدة
    visit(node) {
        const methodName = `visit${node.type}`;
        if (this[methodName]) {
            return this[methodName](node);
        }
        throw new Error(`No visit method for ${node.type}`);
    }

    // زيارة البرنامج
    visitProgram(node) {
        node.body.forEach(statement => {
            this.visit(statement);
        });
    }

    // زيارة تعريف متغير
    visitVariableDeclaration(node) {
        // تحويل الكلمات العربية إلى إنجليزية
        const keyword = (node.kind === 'متغير' || node.kind === 'let') ? 'let' : 'const';

        const value = this.visitExpression(node.value);
        this.emit(`${keyword} ${node.name} = ${value};`);
    }

    // زيارة تعريف دالة
    visitFunctionDeclaration(node) {
        const params = node.params.join(', ');
        this.emit(`function ${node.name}(${params}) {`);
        this.indent();
        this.visit(node.body);
        this.dedent();
        this.emit('}');
        this.emit('');
    }

    // زيارة جملة if
    visitIfStatement(node) {
        const condition = this.visitExpression(node.condition);
        this.emit(`if (${condition}) {`);
        this.indent();
        this.visit(node.thenBranch);
        this.dedent();

        if (node.elseBranch) {
            this.emit('} else {');
            this.indent();
            this.visit(node.elseBranch);
            this.dedent();
        }

        this.emit('}');
    }

    // زيارة جملة while
    visitWhileStatement(node) {
        const condition = this.visitExpression(node.condition);
        this.emit(`while (${condition}) {`);
        this.indent();
        this.visit(node.body);
        this.dedent();
        this.emit('}');
    }

    // زيارة كتلة
    visitBlockStatement(node) {
        node.body.forEach(statement => {
            this.visit(statement);
        });
    }

    // زيارة جملة return
    visitReturnStatement(node) {
        if (node.value) {
            const value = this.visitExpression(node.value);
            this.emit(`return ${value};`);
        } else {
            this.emit('return;');
        }
    }

    // زيارة جملة تعبير
    visitExpressionStatement(node) {
        const expr = this.visitExpression(node.expression);
        this.emit(`${expr};`);
    }

    // زيارة تعبير (بدون إضافة سطر جديد)
    visitExpression(node) {
        const methodName = `visit${node.type}`;
        if (this[methodName]) {
            return this[methodName](node);
        }
        throw new Error(`No visit method for ${node.type}`);
    }

    // زيارة تعبير ثنائي
    visitBinaryExpression(node) {
        const left = this.visitExpression(node.left);
        const right = this.visitExpression(node.right);

        // تحويل العمليات العربية إلى إنجليزية
        let operator = node.operator;
        if (operator === 'و') operator = '&&';
        if (operator === 'أو') operator = '||';

        return `(${left} ${operator} ${right})`;
    }

    // زيارة تعبير أحادي
    visitUnaryExpression(node) {
        const operand = this.visitExpression(node.operand);
        return `(${node.operator}${operand})`;
    }

    // زيارة تعبير إسناد
    visitAssignmentExpression(node) {
        const left = this.visitExpression(node.left);
        const right = this.visitExpression(node.right);
        return `${left} = ${right}`;
    }

    // زيارة استدعاء دالة
    visitCallExpression(node) {
        // تحويل أسماء الدوال العربية إلى إنجليزية
        let callee = node.callee;
        const functionMap = {
            'اطبع': 'console.log',
            'اقرأ': 'prompt',
            'طول': 'length'
        };
        callee = functionMap[callee] || callee;

        const args = node.arguments.map(arg => this.visitExpression(arg)).join(', ');
        return `${callee}(${args})`;
    }

    // زيارة معرف
    visitIdentifier(node) {
        return node.name;
    }

    // زيارة قيم ثابتة
    visitNumberLiteral(node) {
        return node.value.toString();
    }

    visitStringLiteral(node) {
        // معالجة الأحرف الخاصة
        const escaped = node.value
            .replace(/\\/g, '\\\\')
            .replace(/"/g, '\\"')
            .replace(/\n/g, '\\n')
            .replace(/\t/g, '\\t');
        return `"${escaped}"`;
    }

    visitBooleanLiteral(node) {
        return node.value ? 'true' : 'false';
    }

    visitNullLiteral(node) {
        return 'null';
    }
}

module.exports = { CodeGenerator };
```

### 5.3 المترجم الكامل

**ملف: `compiler.js`**

```javascript
const { Lexer } = require('./lexer');
const { Parser } = require('./parser');
const { SemanticAnalyzer } = require('./semantic-analyzer');
const { CodeGenerator } = require('./code-generator');
const fs = require('fs');
const path = require('path');

class BayanCompiler {
    constructor() {
        this.errors = [];
        this.warnings = [];
    }

    // ترجمة ملف
    compileFile(inputPath, outputPath) {
        try {
            // قراءة الملف المصدري
            const sourceCode = fs.readFileSync(inputPath, 'utf-8');

            // الترجمة
            const result = this.compile(sourceCode);

            if (result.success) {
                // كتابة الملف المترجم
                fs.writeFileSync(outputPath, result.code, 'utf-8');
                console.log(`✅ Compilation successful: ${outputPath}`);
                return true;
            } else {
                console.error('❌ Compilation failed:');
                result.errors.forEach(error => console.error(`  - ${error}`));
                return false;
            }
        } catch (error) {
            console.error(`❌ Error: ${error.message}`);
            return false;
        }
    }

    // ترجمة كود
    compile(sourceCode) {
        this.errors = [];
        this.warnings = [];

        try {
            // 1. التحليل المعجمي
            console.log('🔍 Lexical Analysis...');
            const lexer = new Lexer(sourceCode);
            const tokens = lexer.tokenize();
            console.log(`   Found ${tokens.length} tokens`);

            // 2. التحليل النحوي
            console.log('🌳 Syntax Analysis...');
            const parser = new Parser(tokens);
            const ast = parser.parse();
            console.log(`   AST generated with ${ast.body.length} statements`);

            // 3. التحليل الدلالي
            console.log('🔬 Semantic Analysis...');
            const analyzer = new SemanticAnalyzer();
            const semanticResult = analyzer.analyze(ast);

            if (!semanticResult.success) {
                return {
                    success: false,
                    errors: semanticResult.errors,
                    code: null
                };
            }
            console.log('   ✅ No semantic errors');

            // 4. توليد الكود
            console.log('⚙️  Code Generation...');
            const generator = new CodeGenerator();
            const code = generator.generate(ast);
            console.log(`   Generated ${code.split('\n').length} lines of JavaScript`);

            return {
                success: true,
                errors: [],
                code: code,
                ast: ast,
                tokens: tokens
            };

        } catch (error) {
            return {
                success: false,
                errors: [error.message],
                code: null
            };
        }
    }

    // ترجمة مجلد كامل
    compileDirectory(inputDir, outputDir) {
        if (!fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        const files = fs.readdirSync(inputDir);
        let successCount = 0;
        let failCount = 0;

        files.forEach(file => {
            if (path.extname(file) === '.bn') {
                const inputPath = path.join(inputDir, file);
                const outputFile = path.basename(file, '.bn') + '.js';
                const outputPath = path.join(outputDir, outputFile);

                console.log(`\n📄 Compiling ${file}...`);
                if (this.compileFile(inputPath, outputPath)) {
                    successCount++;
                } else {
                    failCount++;
                }
            }
        });

        console.log(`\n📊 Summary: ${successCount} succeeded, ${failCount} failed`);
    }
}

// واجهة سطر الأوامر
if (require.main === module) {
    const args = process.argv.slice(2);

    if (args.length < 2) {
        console.log('Usage: node compiler.js <input.bn> <output.js>');
        console.log('   or: node compiler.js <input-dir> <output-dir> --dir');
        process.exit(1);
    }

    const compiler = new BayanCompiler();

    if (args[2] === '--dir') {
        compiler.compileDirectory(args[0], args[1]);
    } else {
        compiler.compileFile(args[0], args[1]);
    }
}

module.exports = { BayanCompiler };
```

### 5.4 اختبار المترجم الكامل

**ملف: `example.bn`**

```bayan
// مثال بسيط بلغة البيان

متغير x = 10;
متغير y = 20;

دالة جمع(a, b) {
    أرجع a + b;
}

متغير نتيجة = جمع(x, y);
اطبع("النتيجة: " + نتيجة);

إذا (نتيجة > 25) {
    اطبع("أكبر من 25");
} وإلا {
    اطبع("أصغر من أو يساوي 25");
}
```

**تشغيل المترجم:**

```bash
node compiler.js example.bn example.js
```

**الناتج: `example.js`**

```javascript
// Generated by Bayan Compiler
// Target: JavaScript ES2020

let x = 10;
let y = 20;

function جمع(a, b) {
    return (a + b);
}

let نتيجة = جمع(x, y);
console.log(("النتيجة: " + نتيجة));

if ((نتيجة > 25)) {
    console.log("أكبر من 25");
} else {
    console.log("أصغر من أو يساوي 25");
}
```

---

## 🚀 المرحلة السادسة: التحسين والتطوير

### 6.1 تحسينات الأداء

#### أ) تحسين الكود المولد (Optimization)

**ملف: `optimizer.js`**

```javascript
class Optimizer {
    optimize(ast) {
        return this.visit(ast);
    }

    visit(node) {
        const methodName = `visit${node.type}`;
        if (this[methodName]) {
            return this[methodName](node);
        }
        return node;
    }

    // طي الثوابت (Constant Folding)
    visitBinaryExpression(node) {
        const left = this.visit(node.left);
        const right = this.visit(node.right);

        // إذا كان الطرفان أرقام ثابتة، احسب النتيجة مباشرة
        if (left.type === 'NumberLiteral' && right.type === 'NumberLiteral') {
            let result;
            switch (node.operator) {
                case '+': result = left.value + right.value; break;
                case '-': result = left.value - right.value; break;
                case '*': result = left.value * right.value; break;
                case '/': result = left.value / right.value; break;
                default: return { ...node, left, right };
            }
            return { type: 'NumberLiteral', value: result };
        }

        return { ...node, left, right };
    }

    // إزالة الكود الميت (Dead Code Elimination)
    visitIfStatement(node) {
        const condition = this.visit(node.condition);

        // إذا كان الشرط ثابت
        if (condition.type === 'BooleanLiteral') {
            if (condition.value) {
                // الشرط دائماً صحيح، نرجع فقط thenBranch
                return this.visit(node.thenBranch);
            } else if (node.elseBranch) {
                // الشرط دائماً خطأ، نرجع فقط elseBranch
                return this.visit(node.elseBranch);
            } else {
                // الشرط دائماً خطأ ولا يوجد else، نحذف الجملة
                return null;
            }
        }

        return {
            ...node,
            condition,
            thenBranch: this.visit(node.thenBranch),
            elseBranch: node.elseBranch ? this.visit(node.elseBranch) : null
        };
    }
}

module.exports = { Optimizer };
```

### 6.2 رسائل الأخطاء المحسنة

**ملف: `error-reporter.js`**

```javascript
class ErrorReporter {
    constructor(sourceCode) {
        this.sourceCode = sourceCode;
        this.lines = sourceCode.split('\n');
    }

    // تقرير خطأ مع السياق
    reportError(message, line, column) {
        console.error(`\n❌ Error at line ${line}, column ${column}:`);
        console.error(`   ${message}\n`);

        // إظهار السطر الذي فيه الخطأ
        if (line > 0 && line <= this.lines.length) {
            const errorLine = this.lines[line - 1];
            console.error(`${line} | ${errorLine}`);

            // إظهار مؤشر للموقع
            const pointer = ' '.repeat(String(line).length + 3 + column - 1) + '^';
            console.error(pointer);
        }
    }

    // تقرير تحذير
    reportWarning(message, line, column) {
        console.warn(`\n⚠️  Warning at line ${line}, column ${column}:`);
        console.warn(`   ${message}`);
    }
}

module.exports = { ErrorReporter };
```

### 6.3 دعم الوحدات (Modules)

**إضافة import/export:**

```bayan
// ملف: math.bn
تصدير دالة جمع(a, b) {
    أرجع a + b;
}

تصدير دالة ضرب(a, b) {
    أرجع a * b;
}

// ملف: main.bn
استيراد { جمع، ضرب } من "./math.bn";

متغير نتيجة = جمع(5, 3);
اطبع(نتيجة);
```

### 6.4 دعم الأصناف (Classes)

```bayan
صنف شخص {
    بناء(اسم، عمر) {
        هذا.اسم = اسم;
        هذا.عمر = عمر;
    }

    دالة تحية() {
        اطبع("مرحباً، أنا " + هذا.اسم);
    }
}

متغير أحمد = جديد شخص("أحمد", 25);
أحمد.تحية();
```

---

## 📂 الملفات المطلوبة والبنية

### 7.1 هيكل المشروع الكامل

```
bayan-language/
│
├── src/                          # الكود المصدري للمترجم
│   ├── lexer.js                  # المحلل المعجمي
│   ├── parser.js                 # المحلل النحوي
│   ├── semantic-analyzer.js      # المحلل الدلالي
│   ├── code-generator.js         # مولد الكود
│   ├── optimizer.js              # محسن الكود
│   ├── error-reporter.js         # مُبلغ الأخطاء
│   └── compiler.js               # المترجم الرئيسي
│
├── grammar/                      # ملفات القواعد النحوية
│   ├── bayan.grammar             # القواعد النحوية الكاملة
│   ├── tokens.def                # تعريفات الرموز
│   └── operators.def             # تعريفات العمليات
│
├── stdlib/                       # المكتبة القياسية
│   ├── core.bn                   # الدوال الأساسية
│   ├── math.bn                   # دوال رياضية
│   ├── string.bn                 # دوال النصوص
│   ├── array.bn                  # دوال المصفوفات
│   └── io.bn                     # دوال الإدخال/الإخراج
│
├── tools/                        # أدوات التطوير
│   ├── formatter/                # أداة التنسيق
│   │   ├── formatter.js
│   │   └── rules.json
│   ├── linter/                   # أداة الفحص
│   │   ├── linter.js
│   │   └── rules.json
│   └── repl/                     # بيئة تفاعلية
│       └── repl.js
│
├── vscode-extension/             # امتداد VS Code
│   ├── package.json
│   ├── syntaxes/
│   │   └── bayan.tmLanguage.json # تلوين الكود
│   ├── language-configuration.json
│   └── src/
│       └── extension.js          # Language Server Protocol
│
├── tests/                        # الاختبارات
│   ├── lexer.test.js
│   ├── parser.test.js
│   ├── semantic.test.js
│   ├── codegen.test.js
│   └── examples/                 # أمثلة للاختبار
│       ├── hello.bn
│       ├── fibonacci.bn
│       └── classes.bn
│
├── docs/                         # التوثيق
│   ├── SPECIFICATION.md          # المواصفات الكاملة
│   ├── TUTORIAL.md               # دليل المبتدئين
│   ├── API.md                    # واجهة برمجية
│   └── EXAMPLES.md               # أمثلة متقدمة
│
├── package.json                  # معلومات المشروع
├── README.md                     # ملف تعريفي
├── LICENSE                       # الترخيص
└── .gitignore                    # ملفات مستبعدة من Git
```

### 7.2 ملفات القواعد النحوية

#### **ملف: `grammar/bayan.grammar`**

```ebnf
(* Bayan Language Grammar - EBNF Format *)

(* البرنامج *)
Program = { Statement } ;

(* الجمل *)
Statement = VariableDeclaration
          | FunctionDeclaration
          | ClassDeclaration
          | IfStatement
          | WhileStatement
          | ForStatement
          | ReturnStatement
          | BreakStatement
          | ContinueStatement
          | ImportStatement
          | ExportStatement
          | ExpressionStatement
          ;

(* تعريف المتغيرات *)
VariableDeclaration = ( "let" | "متغير" | "const" | "ثابت" )
                      Identifier
                      [ "=" Expression ]
                      ";"
                      ;

(* تعريف الدوال *)
FunctionDeclaration = ( "function" | "دالة" )
                      Identifier
                      "(" [ ParameterList ] ")"
                      Block
                      ;

ParameterList = Identifier { "," Identifier } ;

(* تعريف الأصناف *)
ClassDeclaration = ( "class" | "صنف" )
                   Identifier
                   [ ( "extends" | "يمتد" ) Identifier ]
                   "{"
                   { ClassMember }
                   "}"
                   ;

ClassMember = ConstructorDeclaration
            | MethodDeclaration
            | PropertyDeclaration
            ;

ConstructorDeclaration = ( "constructor" | "بناء" )
                         "(" [ ParameterList ] ")"
                         Block
                         ;

MethodDeclaration = Identifier
                    "(" [ ParameterList ] ")"
                    Block
                    ;

(* جملة if *)
IfStatement = ( "if" | "إذا" )
              "(" Expression ")"
              Block
              [ ( "else" | "وإلا" ) ( Block | IfStatement ) ]
              ;

(* جملة while *)
WhileStatement = ( "while" | "بينما" )
                 "(" Expression ")"
                 Block
                 ;

(* جملة for *)
ForStatement = ( "for" | "لكل" )
               "("
               ( VariableDeclaration | ExpressionStatement | ";" )
               [ Expression ] ";"
               [ Expression ]
               ")"
               Block
               ;

(* جملة return *)
ReturnStatement = ( "return" | "أرجع" ) [ Expression ] ";" ;

(* جملة break *)
BreakStatement = ( "break" | "اكسر" ) ";" ;

(* جملة continue *)
ContinueStatement = ( "continue" | "تابع" ) ";" ;

(* الاستيراد والتصدير *)
ImportStatement = ( "import" | "استيراد" )
                  ( Identifier | "{" Identifier { "," Identifier } "}" )
                  ( "from" | "من" )
                  StringLiteral
                  ";"
                  ;

ExportStatement = ( "export" | "تصدير" )
                  ( VariableDeclaration | FunctionDeclaration | ClassDeclaration )
                  ;

(* كتلة *)
Block = "{" { Statement } "}" ;

(* التعبيرات *)
Expression = Assignment ;

Assignment = LogicalOr [ "=" Assignment ] ;

LogicalOr = LogicalAnd { ( "||" | "أو" ) LogicalAnd } ;

LogicalAnd = Equality { ( "&&" | "و" ) Equality } ;

Equality = Comparison { ( "==" | "!=" ) Comparison } ;

Comparison = Addition { ( ">" | "<" | ">=" | "<=" ) Addition } ;

Addition = Multiplication { ( "+" | "-" ) Multiplication } ;

Multiplication = Unary { ( "*" | "/" | "%" ) Unary } ;

Unary = ( "!" | "-" | "++" | "--" ) Unary
      | Postfix
      ;

Postfix = Primary { ( "++" | "--" | MemberAccess | FunctionCall | ArrayAccess ) } ;

MemberAccess = "." Identifier ;

FunctionCall = "(" [ ArgumentList ] ")" ;

ArgumentList = Expression { "," Expression } ;

ArrayAccess = "[" Expression "]" ;

Primary = NumberLiteral
        | StringLiteral
        | BooleanLiteral
        | NullLiteral
        | Identifier
        | ArrayLiteral
        | ObjectLiteral
        | "(" Expression ")"
        | ( "new" | "جديد" ) Identifier "(" [ ArgumentList ] ")"
        | ( "this" | "هذا" )
        ;

ArrayLiteral = "[" [ Expression { "," Expression } ] "]" ;

ObjectLiteral = "{" [ PropertyAssignment { "," PropertyAssignment } ] "}" ;

PropertyAssignment = ( Identifier | StringLiteral ) ":" Expression ;

(* القيم الثابتة *)
NumberLiteral = Digit { Digit } [ "." Digit { Digit } ] ;

StringLiteral = '"' { Character } '"'
              | "'" { Character } "'"
              ;

BooleanLiteral = "true" | "false" | "صحيح" | "خطأ" ;

NullLiteral = "null" | "عدم" ;

Identifier = Letter { Letter | Digit | "_" } ;

(* الأحرف الأساسية *)
Letter = "a" | "b" | ... | "z"
       | "A" | "B" | ... | "Z"
       | ArabicLetter
       ;

ArabicLetter = "ا" | "ب" | "ت" | ... | "ي" ;

Digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

Character = (* أي حرف Unicode *) ;
```

#### **ملف: `grammar/tokens.def`**

```json
{
  "keywords": {
    "control": {
      "if": ["if", "إذا"],
      "else": ["else", "وإلا"],
      "while": ["while", "بينما"],
      "for": ["for", "لكل"],
      "break": ["break", "اكسر"],
      "continue": ["continue", "تابع"],
      "return": ["return", "أرجع"]
    },
    "declarations": {
      "let": ["let", "متغير"],
      "const": ["const", "ثابت"],
      "function": ["function", "دالة"],
      "class": ["class", "صنف"],
      "constructor": ["constructor", "بناء"],
      "extends": ["extends", "يمتد"]
    },
    "modules": {
      "import": ["import", "استيراد"],
      "export": ["export", "تصدير"],
      "from": ["from", "من"]
    },
    "literals": {
      "true": ["true", "صحيح"],
      "false": ["false", "خطأ"],
      "null": ["null", "عدم"]
    },
    "special": {
      "this": ["this", "هذا"],
      "new": ["new", "جديد"]
    }
  },
  "operators": {
    "arithmetic": ["+", "-", "*", "/", "%"],
    "comparison": [">", "<", ">=", "<=", "==", "!="],
    "logical": {
      "and": ["&&", "و"],
      "or": ["||", "أو"],
      "not": ["!", "ليس"]
    },
    "assignment": ["=", "+=", "-=", "*=", "/="],
    "increment": ["++", "--"]
  },
  "delimiters": {
    "parentheses": ["(", ")"],
    "braces": ["{", "}"],
    "brackets": ["[", "]"],
    "semicolon": ";",
    "comma": ",",
    "dot": ".",
    "colon": ":"
  }
}
```

### 7.3 ملف package.json

```json
{
  "name": "bayan-lang",
  "version": "1.0.0",
  "description": "Bayan Programming Language - Bilingual (Arabic/English) Compiler",
  "main": "src/compiler.js",
  "bin": {
    "bayan": "./bin/bayan.js"
  },
  "scripts": {
    "test": "jest",
    "build": "node src/compiler.js",
    "repl": "node tools/repl/repl.js",
    "format": "node tools/formatter/formatter.js",
    "lint": "node tools/linter/linter.js"
  },
  "keywords": [
    "programming-language",
    "compiler",
    "arabic",
    "bilingual",
    "transpiler",
    "javascript"
  ],
  "author": "Baserah AI Team",
  "license": "MIT",
  "dependencies": {},
  "devDependencies": {
    "jest": "^29.0.0"
  },
  "engines": {
    "node": ">=14.0.0"
  }
}
```

### 7.4 ملف CLI التنفيذي

**ملف: `bin/bayan.js`**

```javascript
#!/usr/bin/env node

const { BayanCompiler } = require('../src/compiler');
const fs = require('fs');
const path = require('path');

// تحليل الأوامر
const args = process.argv.slice(2);

function showHelp() {
    console.log(`
🌙 Bayan Programming Language Compiler

Usage:
  bayan <command> [options]

Commands:
  compile <file.bn>              Compile a Bayan file to JavaScript
  compile <dir> -o <outdir>      Compile all .bn files in directory
  run <file.bn>                  Compile and run a Bayan file
  repl                           Start interactive REPL
  format <file.bn>               Format a Bayan file
  lint <file.bn>                 Lint a Bayan file
  help                           Show this help message
  version                        Show version

Examples:
  bayan compile example.bn
  bayan run hello.bn
  bayan compile src/ -o dist/
  bayan repl

Options:
  -o, --output <path>            Output file or directory
  -w, --watch                    Watch for changes
  -v, --verbose                  Verbose output
  --ast                          Print AST
  --tokens                       Print tokens
  --no-optimize                  Disable optimizations
    `);
}

function showVersion() {
    const pkg = require('../package.json');
    console.log(`Bayan v${pkg.version}`);
}

// معالجة الأوامر
const command = args[0];

switch (command) {
    case 'compile': {
        const inputPath = args[1];
        const outputIndex = args.indexOf('-o') || args.indexOf('--output');
        const outputPath = outputIndex !== -1 ? args[outputIndex + 1] : null;

        if (!inputPath) {
            console.error('❌ Error: No input file specified');
            process.exit(1);
        }

        const compiler = new BayanCompiler();

        if (fs.statSync(inputPath).isDirectory()) {
            const outDir = outputPath || path.join(inputPath, '../dist');
            compiler.compileDirectory(inputPath, outDir);
        } else {
            const outFile = outputPath || inputPath.replace('.bn', '.js');
            compiler.compileFile(inputPath, outFile);
        }
        break;
    }

    case 'run': {
        const inputPath = args[1];
        if (!inputPath) {
            console.error('❌ Error: No input file specified');
            process.exit(1);
        }

        const compiler = new BayanCompiler();
        const sourceCode = fs.readFileSync(inputPath, 'utf-8');
        const result = compiler.compile(sourceCode);

        if (result.success) {
            // تنفيذ الكود المولد
            eval(result.code);
        } else {
            console.error('❌ Compilation failed');
            result.errors.forEach(err => console.error(`  - ${err}`));
            process.exit(1);
        }
        break;
    }

    case 'repl': {
        require('../tools/repl/repl.js');
        break;
    }

    case 'format': {
        const formatter = require('../tools/formatter/formatter.js');
        const inputPath = args[1];
        formatter.formatFile(inputPath);
        break;
    }

    case 'lint': {
        const linter = require('../tools/linter/linter.js');
        const inputPath = args[1];
        linter.lintFile(inputPath);
        break;
    }

    case 'version':
        showVersion();
        break;

    case 'help':
    default:
        showHelp();
        break;
}
```

---

## 🛠️ أدوات وتقنيات متقدمة

### 8.1 بيئة تفاعلية (REPL)

**ملف: `tools/repl/repl.js`**

```javascript
const readline = require('readline');
const { BayanCompiler } = require('../../src/compiler');

class BayanREPL {
    constructor() {
        this.compiler = new BayanCompiler();
        this.context = {}; // سياق التنفيذ
        this.rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout,
            prompt: 'بيان> '
        });
    }

    start() {
        console.log('🌙 Bayan REPL v1.0.0');
        console.log('اكتب .help للمساعدة، .exit للخروج\n');

        this.rl.prompt();

        this.rl.on('line', (line) => {
            const trimmed = line.trim();

            // أوامر خاصة
            if (trimmed === '.exit' || trimmed === '.خروج') {
                console.log('وداعاً! 👋');
                process.exit(0);
            }

            if (trimmed === '.help' || trimmed === '.مساعدة') {
                this.showHelp();
                this.rl.prompt();
                return;
            }

            if (trimmed === '.clear' || trimmed === '.مسح') {
                console.clear();
                this.rl.prompt();
                return;
            }

            if (trimmed === '') {
                this.rl.prompt();
                return;
            }

            // تنفيذ الكود
            try {
                const result = this.compiler.compile(trimmed);

                if (result.success) {
                    // تنفيذ الكود في السياق
                    const func = new Function('context', result.code + '\nreturn context;');
                    this.context = func(this.context);
                    console.log('✅');
                } else {
                    result.errors.forEach(err => console.error(`❌ ${err}`));
                }
            } catch (error) {
                console.error(`❌ ${error.message}`);
            }

            this.rl.prompt();
        });

        this.rl.on('close', () => {
            console.log('\nوداعاً! 👋');
            process.exit(0);
        });
    }

    showHelp() {
        console.log(`
الأوامر المتاحة:
  .help, .مساعدة     عرض هذه المساعدة
  .exit, .خروج       الخروج من REPL
  .clear, .مسح       مسح الشاشة

أمثلة:
  متغير x = 10;
  دالة جمع(a, b) { أرجع a + b; }
  اطبع(جمع(5, 3));
        `);
    }
}

// تشغيل REPL
if (require.main === module) {
    const repl = new BayanREPL();
    repl.start();
}

module.exports = { BayanREPL };
```

### 8.2 أداة التنسيق (Formatter)

**ملف: `tools/formatter/formatter.js`**

```javascript
const fs = require('fs');
const { Lexer } = require('../../src/lexer');
const { Parser } = require('../../src/parser');

class BayanFormatter {
    constructor() {
        this.indentSize = 4;
        this.indentLevel = 0;
    }

    formatFile(filePath) {
        const sourceCode = fs.readFileSync(filePath, 'utf-8');
        const formatted = this.format(sourceCode);
        fs.writeFileSync(filePath, formatted, 'utf-8');
        console.log(`✅ Formatted: ${filePath}`);
    }

    format(sourceCode) {
        try {
            const lexer = new Lexer(sourceCode);
            const tokens = lexer.tokenize();
            const parser = new Parser(tokens);
            const ast = parser.parse();

            return this.formatAST(ast);
        } catch (error) {
            console.error(`❌ Formatting error: ${error.message}`);
            return sourceCode; // إرجاع الكود الأصلي في حالة الخطأ
        }
    }

    formatAST(ast) {
        let output = '';
        this.indentLevel = 0;

        ast.body.forEach((statement, index) => {
            output += this.formatStatement(statement);
            if (index < ast.body.length - 1) {
                output += '\n';
            }
        });

        return output;
    }

    formatStatement(node) {
        const indent = ' '.repeat(this.indentLevel * this.indentSize);

        switch (node.type) {
            case 'VariableDeclaration':
                return `${indent}${node.kind} ${node.name} = ${this.formatExpression(node.value)};\n`;

            case 'FunctionDeclaration':
                const params = node.params.join(', ');
                let func = `${indent}${node.kind || 'دالة'} ${node.name}(${params}) {\n`;
                this.indentLevel++;
                node.body.body.forEach(stmt => {
                    func += this.formatStatement(stmt);
                });
                this.indentLevel--;
                func += `${indent}}\n`;
                return func;

            case 'IfStatement':
                let ifStmt = `${indent}إذا (${this.formatExpression(node.condition)}) {\n`;
                this.indentLevel++;
                node.thenBranch.body.forEach(stmt => {
                    ifStmt += this.formatStatement(stmt);
                });
                this.indentLevel--;
                ifStmt += `${indent}}`;

                if (node.elseBranch) {
                    ifStmt += ' وإلا {\n';
                    this.indentLevel++;
                    node.elseBranch.body.forEach(stmt => {
                        ifStmt += this.formatStatement(stmt);
                    });
                    this.indentLevel--;
                    ifStmt += `${indent}}`;
                }
                ifStmt += '\n';
                return ifStmt;

            case 'ReturnStatement':
                return `${indent}أرجع ${node.value ? this.formatExpression(node.value) : ''};\n`;

            case 'ExpressionStatement':
                return `${indent}${this.formatExpression(node.expression)};\n`;

            default:
                return `${indent}/* Unknown statement type: ${node.type} */\n`;
        }
    }

    formatExpression(node) {
        switch (node.type) {
            case 'BinaryExpression':
                return `${this.formatExpression(node.left)} ${node.operator} ${this.formatExpression(node.right)}`;

            case 'CallExpression':
                const args = node.arguments.map(arg => this.formatExpression(arg)).join(', ');
                return `${node.callee}(${args})`;

            case 'Identifier':
                return node.name;

            case 'NumberLiteral':
                return node.value.toString();

            case 'StringLiteral':
                return `"${node.value}"`;

            case 'BooleanLiteral':
                return node.value ? 'صحيح' : 'خطأ';

            default:
                return '/* unknown */';
        }
    }
}

module.exports = new BayanFormatter();
```

### 8.3 أداة الفحص (Linter)

**ملف: `tools/linter/linter.js`**

```javascript
const fs = require('fs');
const { Lexer } = require('../../src/lexer');
const { Parser } = require('../../src/parser');

class BayanLinter {
    constructor() {
        this.warnings = [];
        this.errors = [];
    }

    lintFile(filePath) {
        const sourceCode = fs.readFileSync(filePath, 'utf-8');
        const result = this.lint(sourceCode);

        console.log(`\n📋 Linting: ${filePath}\n`);

        if (result.errors.length > 0) {
            console.log('❌ Errors:');
            result.errors.forEach(err => console.log(`  - ${err}`));
        }

        if (result.warnings.length > 0) {
            console.log('\n⚠️  Warnings:');
            result.warnings.forEach(warn => console.log(`  - ${warn}`));
        }

        if (result.errors.length === 0 && result.warnings.length === 0) {
            console.log('✅ No issues found!');
        }

        return result;
    }

    lint(sourceCode) {
        this.warnings = [];
        this.errors = [];

        try {
            const lexer = new Lexer(sourceCode);
            const tokens = lexer.tokenize();
            const parser = new Parser(tokens);
            const ast = parser.parse();

            this.checkAST(ast);
        } catch (error) {
            this.errors.push(error.message);
        }

        return {
            errors: this.errors,
            warnings: this.warnings
        };
    }

    checkAST(ast) {
        ast.body.forEach(statement => this.checkStatement(statement));
    }

    checkStatement(node) {
        switch (node.type) {
            case 'VariableDeclaration':
                // تحذير: استخدام let بدلاً من const للقيم الثابتة
                if (node.kind === 'متغير' || node.kind === 'let') {
                    if (node.value && node.value.type.includes('Literal')) {
                        this.warnings.push(`Consider using 'const' for '${node.name}' since it's initialized with a literal`);
                    }
                }
                break;

            case 'FunctionDeclaration':
                // تحذير: دالة بدون return
                const hasReturn = this.hasReturnStatement(node.body);
                if (!hasReturn) {
                    this.warnings.push(`Function '${node.name}' has no return statement`);
                }
                break;

            case 'IfStatement':
                // تحذير: شرط ثابت
                if (node.condition.type === 'BooleanLiteral') {
                    this.warnings.push('If statement has constant condition');
                }
                break;
        }
    }

    hasReturnStatement(block) {
        return block.body.some(stmt => {
            if (stmt.type === 'ReturnStatement') {
                return true;
            }
            if (stmt.type === 'IfStatement') {
                return this.hasReturnStatement(stmt.thenBranch) ||
                       (stmt.elseBranch && this.hasReturnStatement(stmt.elseBranch));
            }
            return false;
        });
    }
}

module.exports = new BayanLinter();
```

### 8.4 امتداد VS Code

**ملف: `vscode-extension/syntaxes/bayan.tmLanguage.json`**

```json
{
  "name": "Bayan",
  "scopeName": "source.bayan",
  "fileTypes": ["bn"],
  "patterns": [
    {
      "include": "#comments"
    },
    {
      "include": "#keywords"
    },
    {
      "include": "#strings"
    },
    {
      "include": "#numbers"
    },
    {
      "include": "#operators"
    },
    {
      "include": "#functions"
    }
  ],
  "repository": {
    "comments": {
      "patterns": [
        {
          "name": "comment.line.double-slash.bayan",
          "match": "//.*$"
        },
        {
          "name": "comment.block.bayan",
          "begin": "/\\*",
          "end": "\\*/"
        }
      ]
    },
    "keywords": {
      "patterns": [
        {
          "name": "keyword.control.bayan",
          "match": "\\b(if|else|while|for|return|break|continue|إذا|وإلا|بينما|لكل|أرجع|اكسر|تابع)\\b"
        },
        {
          "name": "keyword.declaration.bayan",
          "match": "\\b(let|const|function|class|متغير|ثابت|دالة|صنف)\\b"
        },
        {
          "name": "keyword.other.bayan",
          "match": "\\b(import|export|from|new|this|استيراد|تصدير|من|جديد|هذا)\\b"
        }
      ]
    },
    "strings": {
      "patterns": [
        {
          "name": "string.quoted.double.bayan",
          "begin": "\"",
          "end": "\"",
          "patterns": [
            {
              "name": "constant.character.escape.bayan",
              "match": "\\\\."
            }
          ]
        },
        {
          "name": "string.quoted.single.bayan",
          "begin": "'",
          "end": "'",
          "patterns": [
            {
              "name": "constant.character.escape.bayan",
              "match": "\\\\."
            }
          ]
        }
      ]
    },
    "numbers": {
      "patterns": [
        {
          "name": "constant.numeric.bayan",
          "match": "\\b\\d+(\\.\\d+)?\\b"
        }
      ]
    },
    "operators": {
      "patterns": [
        {
          "name": "keyword.operator.bayan",
          "match": "(\\+|\\-|\\*|\\/|%|==|!=|>|<|>=|<=|&&|\\|\\||!|=|و|أو|ليس)"
        }
      ]
    },
    "functions": {
      "patterns": [
        {
          "name": "entity.name.function.bayan",
          "match": "\\b([a-zA-Z_\\u0600-\\u06FF][a-zA-Z0-9_\\u0600-\\u06FF]*)\\s*(?=\\()"
        }
      ]
    }
  }
}
```

**ملف: `vscode-extension/package.json`**

```json
{
  "name": "bayan-language",
  "displayName": "Bayan Language Support",
  "description": "Syntax highlighting and language support for Bayan programming language",
  "version": "1.0.0",
  "publisher": "baserah-ai",
  "engines": {
    "vscode": "^1.60.0"
  },
  "categories": ["Programming Languages"],
  "contributes": {
    "languages": [
      {
        "id": "bayan",
        "aliases": ["Bayan", "bayan"],
        "extensions": [".bn"],
        "configuration": "./language-configuration.json"
      }
    ],
    "grammars": [
      {
        "language": "bayan",
        "scopeName": "source.bayan",
        "path": "./syntaxes/bayan.tmLanguage.json"
      }
    ],
    "snippets": [
      {
        "language": "bayan",
        "path": "./snippets/bayan.json"
      }
    ]
  }
}
```

### 8.5 اختبارات شاملة

**ملف: `tests/compiler.test.js`**

```javascript
const { BayanCompiler } = require('../src/compiler');

describe('Bayan Compiler', () => {
    let compiler;

    beforeEach(() => {
        compiler = new BayanCompiler();
    });

    test('should compile variable declaration', () => {
        const code = 'متغير x = 10;';
        const result = compiler.compile(code);

        expect(result.success).toBe(true);
        expect(result.code).toContain('let x = 10');
    });

    test('should compile function declaration', () => {
        const code = `
            دالة جمع(a, b) {
                أرجع a + b;
            }
        `;
        const result = compiler.compile(code);

        expect(result.success).toBe(true);
        expect(result.code).toContain('function جمع');
        expect(result.code).toContain('return');
    });

    test('should compile if statement', () => {
        const code = `
            إذا (x > 5) {
                اطبع("أكبر");
            }
        `;
        const result = compiler.compile(code);

        expect(result.success).toBe(true);
        expect(result.code).toContain('if');
    });

    test('should detect undefined variable', () => {
        const code = 'اطبع(y);'; // y غير معرف
        const result = compiler.compile(code);

        expect(result.success).toBe(false);
        expect(result.errors.length).toBeGreaterThan(0);
    });

    test('should compile Arabic and English mixed code', () => {
        const code = `
            let x = 10;
            متغير y = 20;
            function add(a, b) {
                return a + b;
            }
            دالة multiply(a, b) {
                أرجع a * b;
            }
        `;
        const result = compiler.compile(code);

        expect(result.success).toBe(true);
    });
});
```

---

## 🎓 الخلاصة والموارد

### 9.1 ملخص المراحل

لصناعة لغة برمجية كاملة، تحتاج إلى:

#### **1️⃣ التخطيط والتصميم**
- ✅ تحديد الأهداف والجمهور
- ✅ تصميم بناء الجملة (Syntax)
- ✅ تحديد الكلمات المفتاحية والعمليات
- ✅ كتابة المواصفات الكاملة

#### **2️⃣ التحليل المعجمي (Lexer)**
- ✅ تقسيم الكود إلى رموز (Tokens)
- ✅ التعرف على الكلمات المفتاحية
- ✅ معالجة الأرقام والنصوص
- ✅ تجاهل المسافات والتعليقات

#### **3️⃣ التحليل النحوي (Parser)**
- ✅ بناء شجرة AST من الرموز
- ✅ التحقق من صحة بناء الجملة
- ✅ معالجة الأولويات والترابط

#### **4️⃣ التحليل الدلالي (Semantic Analyzer)**
- ✅ التحقق من الأنواع
- ✅ التحقق من النطاقات
- ✅ كشف الأخطاء المنطقية

#### **5️⃣ توليد الكود (Code Generator)**
- ✅ تحويل AST إلى كود مستهدف
- ✅ تحسين الكود المولد
- ✅ إضافة تعليقات وتوثيق

#### **6️⃣ الأدوات والتطوير**
- ✅ REPL تفاعلي
- ✅ أداة تنسيق (Formatter)
- ✅ أداة فحص (Linter)
- ✅ امتداد محرر (VS Code Extension)
- ✅ اختبارات شاملة

### 9.2 الملفات الأساسية المطلوبة

| الملف | الوصف | الأهمية |
|------|-------|---------|
| `lexer.js` | المحلل المعجمي | ⭐⭐⭐⭐⭐ |
| `parser.js` | المحلل النحوي | ⭐⭐⭐⭐⭐ |
| `semantic-analyzer.js` | المحلل الدلالي | ⭐⭐⭐⭐ |
| `code-generator.js` | مولد الكود | ⭐⭐⭐⭐⭐ |
| `compiler.js` | المترجم الرئيسي | ⭐⭐⭐⭐⭐ |
| `grammar.bnf` | القواعد النحوية | ⭐⭐⭐⭐ |
| `tokens.def` | تعريفات الرموز | ⭐⭐⭐ |
| `optimizer.js` | محسن الكود | ⭐⭐⭐ |
| `error-reporter.js` | مُبلغ الأخطاء | ⭐⭐⭐ |
| `repl.js` | بيئة تفاعلية | ⭐⭐ |
| `formatter.js` | أداة التنسيق | ⭐⭐ |
| `linter.js` | أداة الفحص | ⭐⭐ |

### 9.3 المفاهيم الأساسية

**مصطلحات مهمة:**

- **Token (رمز)**: أصغر وحدة ذات معنى في اللغة
- **AST (شجرة البناء المجردة)**: تمثيل هيكلي للكود
- **Grammar (القواعد النحوية)**: القواعد التي تحدد بناء الجملة
- **Lexer (المحلل المعجمي)**: يحول النص إلى رموز
- **Parser (المحلل النحوي)**: يبني AST من الرموز
- **Semantic Analysis (التحليل الدلالي)**: يتحقق من المعنى والمنطق
- **Code Generation (توليد الكود)**: يحول AST إلى كود مستهدف
- **Transpiler (المترجم العابر)**: يترجم من لغة إلى لغة أخرى
- **Compiler (المترجم)**: يحول الكود إلى لغة آلة أو وسيطة

### 9.4 موارد إضافية

#### كتب موصى بها:
1. **"Crafting Interpreters"** by Robert Nystrom
2. **"Writing An Interpreter In Go"** by Thorsten Ball
3. **"Modern Compiler Implementation"** by Andrew Appel
4. **"Engineering a Compiler"** by Keith Cooper

#### أدوات مفيدة:
- **ANTLR**: مولد محللات نحوية
- **PEG.js**: محلل نحوي لـ JavaScript
- **Ohm**: مكتبة لبناء المحللات
- **Nearley**: محلل نحوي سريع

#### مواقع تعليمية:
- [Compiler Explorer](https://godbolt.org/)
- [AST Explorer](https://astexplorer.net/)
- [The Super Tiny Compiler](https://github.com/jamiebuilds/the-super-tiny-compiler)

### 9.5 نصائح نهائية

1. **ابدأ صغيراً**: لا تحاول بناء كل شيء دفعة واحدة
2. **اختبر باستمرار**: اكتب اختبارات لكل مكون
3. **وثق جيداً**: اكتب مواصفات واضحة
4. **تعلم من الآخرين**: ادرس لغات موجودة
5. **كن صبوراً**: بناء لغة برمجية يستغرق وقتاً
6. **استمع للمستخدمين**: خذ ملاحظاتهم بعين الاعتبار
7. **حسّن تدريجياً**: لا تسعى للكمال من البداية

### 9.6 الخطوات التالية للغة البيان

**ما تم إنجازه:**
- ✅ التحليل المعجمي الكامل
- ✅ التحليل النحوي الأساسي
- ✅ التحليل الدلالي
- ✅ توليد كود JavaScript
- ✅ دعم ثنائي اللغة (عربي/إنجليزي)

**ما يمكن تطويره:**
- 🔲 دعم الوحدات (Modules) الكامل
- 🔲 نظام أنواع متقدم (Type System)
- 🔲 دعم البرمجة غير المتزامنة (Async/Await)
- 🔲 مكتبة قياسية شاملة
- 🔲 أدوات تصحيح (Debugger)
- 🔲 توليد Source Maps
- 🔲 تحسينات الأداء المتقدمة
- 🔲 دعم WebAssembly كهدف بديل

---

## 🎯 الخاتمة

صناعة لغة برمجية هي رحلة تعليمية رائعة تجمع بين:
- 📐 **الرياضيات**: نظرية اللغات والأوتوماتا
- 💻 **البرمجة**: تطبيق عملي للخوارزميات
- 🎨 **التصميم**: ابتكار بناء جملة جميل وعملي
- 🧠 **المنطق**: فهم عميق لكيفية عمل الحواسيب

**لغة البيان** هي مثال عملي يوضح كل هذه المفاهيم، وتُظهر كيف يمكن دمج اللغة العربية في البرمجة بشكل طبيعي وفعال.

نتمنى أن يكون هذا الدليل مرجعاً مفيداً لكل من يريد فهم أو بناء لغة برمجية! 🚀

---

**تم بحمد الله ✨**

**فريق بصيرة AI**
*نحو ذكاء اصطناعي عربي متقدم*


