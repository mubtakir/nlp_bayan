# Bayan Programming Language - LLM Reference Guide
# دليل مرجعي للنماذج اللغوية - لغة البيان

> **Purpose**: This guide is designed for Large Language Models (LLMs) to understand and generate code in the Bayan programming language.

---

## Quick Overview

**Bayan** is a unique hybrid programming language that combines three paradigms:
1. **Imperative Programming** (like Python)
2. **Object-Oriented Programming** (like Python/Java)
3. **Logic Programming** (like Prolog)
4. **Causal Network Engine** (NEW! 🎯) - Build causal networks in any domain

**Key Features**:
- Supports both Arabic and English keywords
- Brace-based syntax with `:` before blocks
- All code must be wrapped in `hybrid { ... }`
- Full Unicode support for Arabic text
- **Built-in Causal Network Engine** for building causal reasoning systems

---

## Syntax Rules

### 1. Basic Structure

```bayan
hybrid {
    # All code goes inside hybrid block
    # Comments start with #
    
    # Statements
    x = 10
    print(x)
}
```

### 2. Block Syntax

**IMPORTANT**: Use `{` and `}` for blocks, with `:` before the opening brace:

```bayan
# Correct ✓
if (condition) {
    statement
}

# Wrong ✗
if condition {  # Missing :
    statement
}

# Wrong ✗
if condition:
    statement  # Missing braces
```

### 3. Keywords

**English Keywords** (recommended for universal code):
- Control: `if`, `elif`, `else`, `for`, `in`, `while`
- Functions: `def`, `return`, `yield`, `lambda`
- Classes: `class`, `self`, `new`
- Logic: `and`, `or`, `not`
- Values: `True`, `False`, `None`
- Exceptions: `try`, `except`, `finally`, `raise`
- Async: `async`, `await`
- Context: `with`
- Other: `import`, `from`, `global`, `del`, `pass`, `break`, `continue`, `assert`

**Arabic Keywords** (alternative):
- `اذا` (if), `والا_اذا` (elif), `والا` (else)
- `لكل` (for), `في` (in), `بينما` (while)
- `دالة` (def), `ارجع` (return)
- `صنف` (class), `الذات` (self)
- `صحيح` (True), `خطأ` (False), `لاشيء` (None)

---

## Data Types

### Primitives
```bayan
hybrid {
    # Integer
    age = 25
    
    # Float
    price = 99.99
    
    # String (supports Arabic)
    name = "أحمد"
    city = "Riyadh"
    
    # Boolean
    is_active = True
    
    # None
    result = None
}
```

### Collections
```bayan
hybrid {
    # List
    numbers = [1, 2, 3, 4, 5]
    names = ["أحمد", "فاطمة", "علي"]
    
    # Dictionary
    person = {
        "name": "أحمد",
        "age": 25,
        "city": "الرياض"
    }
    
    # Set
    unique_numbers = {1, 2, 3, 4, 5}
}
```

---

## Control Flow

### If-Elif-Else
```bayan
hybrid {
    score = 85
    
    if (score >= 90) {
        print("Excellent")
    }
    elif (score >= 80) {
        print("Very Good")
    }
    elif (score >= 70) {
        print("Good")
    }
    else: {
        print("Pass")
    }
}
```

### For Loop
```bayan
hybrid {
    # Iterate over list
    fruits = ["apple", "banana", "orange"]
    for fruit in (fruits) {
        print(fruit)
    }
    
    # Range
    for i in (range(5)) {
        print(i)  # 0, 1, 2, 3, 4
    }
    
    # Enumerate
    for item in (enumerate(fruits)) {
        index = item[0]
        value = item[1]
        print(index)
        print(value)
    }
}
```

### While Loop
```bayan
hybrid {
    count = 0
    while (count < 5) {
        print(count)
        count = count + 1
    }
}
```

---

## Functions

### Basic Function
```bayan
hybrid {
    def greet(name): {
        return "Hello, " + name
    }
    
    message = greet("أحمد")
    print(message)
}
```

### Default Parameters
```bayan
hybrid {
    def greet(name, greeting="Hello"): {
        return greeting + ", " + name
    }
    
    msg1 = greet("أحمد")  # "Hello, أحمد"
    msg2 = greet("فاطمة", "مرحباً")  # "مرحباً, فاطمة"
}
```

### *args and **kwargs
```bayan
hybrid {
    # Variable positional arguments
    def sum_all(*numbers): {
        total = 0
        for num in (numbers) {
            total = total + num
        }
        return total
    }
    
    result = sum_all(1, 2, 3, 4, 5)  # 15
    
    # Variable keyword arguments
    def print_info(**info): {
        for key in (info) {
            print(key)
            print(info[key])
        }
    }
    
    print_info(name="أحمد", age=25, city="الرياض")
}
```

### Lambda Functions
```bayan
hybrid {
    square = lambda x: x * x
    result = square(5)  # 25
    
    # With filter
    numbers = [1, 2, 3, 4, 5, 6]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
}
```

---

## Object-Oriented Programming

### Class Definition
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
        
        def get_age(self): {
            return self.age
        }
    }
    
    # Create object
    person = Person("أحمد", 25)
    print(person.greet())
    print(person.get_age())
}
```

### Inheritance
```bayan
hybrid {
    class Animal: {
        def __init__(self, name): {
            self.name = name
        }
        
        def speak(self): {
            print("Animal speaks")
        }
    }
    
    class Dog: {
        def __init__(self, name, breed): {
            self.name = name
            self.breed = breed
        }
        
        def speak(self): {
            print("Dog barks")
        }
    }
    
    dog = Dog("Rex", "German Shepherd")
    dog.speak()
}
```

---

## Logic Programming

### Facts
```bayan
hybrid {
    # Define facts (end with .)
    parent("أحمد", "محمد").
    parent("محمد", "علي").
    
    age("أحمد", 50).
    age("محمد", 25).
}
```

### Rules
```bayan
hybrid {
    # Facts
    parent("أحمد", "محمد").
    parent("محمد", "علي").
    
    # Rule: X is grandparent of Z if X is parent of Y and Y is parent of Z
    grandparent(?X, ?Z) :- parent(?X, ?Y), parent(?Y, ?Z).
}
```

### Queries
```bayan
hybrid {
    # Facts
    parent("أحمد", "محمد").
    parent("أحمد", "فاطمة").
    
    # Query: Who are the children of أحمد?
    results = query parent("أحمد", ?Child)?
    
    for result in (results) {
        child = result["?Child"]
        print(child)  # محمد, فاطمة
    }
}
```

### Meta-predicates
```bayan
hybrid {
    # Facts
    score("أحمد", 85).
    score("فاطمة", 92).
    score("علي", 78).
    
    # findall: collect all solutions
    results = query findall(?Score, score(?Name, ?Score), ?AllScores)?
    
    for result in (results) {
        all_scores = result["?AllScores"]
        print(all_scores)  # [85, 92, 78]
    }
}
```

### Dynamic Knowledge Base
```bayan
hybrid {
    # Initial facts
    student("أحمد").
    student("فاطمة").
    
    # Add new fact
    assertz(student("علي"))
    
    # Remove fact
    retract(student("فاطمة"))
    
    # Query
    results = query student(?S)?
    # Results: أحمد, علي
}
```

---

## Advanced Features

### Generators
```bayan
hybrid {
    def count_up_to(n): {
        i = 1
        while (i <= n) {
            yield i
            i = i + 1
        }
    }
    
    for num in (count_up_to(5)) {
        print(num)  # 1, 2, 3, 4, 5
    }
}
```

### Decorators
```bayan
hybrid {
    def my_decorator(func): {
        def wrapper(): {
            print("Before function")
            func()
            print("After function")
        }
        return wrapper
    }
    
    @my_decorator
    def say_hello(): {
        print("Hello!")
    }
    
    say_hello()
}
```

### Exception Handling
```bayan
hybrid {
    try: {
        x = 10 / 0
    }
    except ZeroDivisionError: {
        print("Cannot divide by zero!")
    }
    finally: {
        print("Cleanup")
    }
}
```

### Context Managers
```bayan
hybrid {
    class FileManager: {
        def __init__(self, filename): {
            self.filename = filename
        }
        
        def __enter__(self): {
            print("Opening file")
            return self
        }
        
        def __exit__(self): {
            print("Closing file")
        }
    }
    
    with FileManager("data.txt"): {
        print("Working with file")
    }
}
```

---

## Built-in Functions

### Common Functions
```bayan
hybrid {
    # Type conversion
    x = int("123")
    y = float("3.14")
    z = str(456)
    
    # String operations
    text = "hello world"
    upper_text = upper(text)
    lower_text = lower(text)
    
    # List operations
    numbers = [3, 1, 4, 1, 5]
    length = len(numbers)
    sorted_nums = sorted(numbers)
    
    # Math operations
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    
    # Functional
    squared = list(map(lambda x: x * x, numbers))
    evens = list(filter(lambda x: x % 2 == 0, numbers))
}
```

---

## Common Patterns

### Pattern 1: Hybrid OOP + Logic
```bayan
hybrid {
    # Class definition
    class Student: {
        def __init__(self, name, grade): {
            self.name = name
            self.grade = grade
            
            # Add to logic knowledge base
            assertz(student(name, grade))
        }
    }
    
    # Create students
    s1 = Student("أحمد", 85)
    s2 = Student("فاطمة", 95)
    
    # Query using logic
    results = query student(?N, ?G), ?G >= 90?
    
    for result in (results) {
        print(result["?N"])  # فاطمة
    }
}
```

### Pattern 2: Expert System
```bayan
hybrid {
    # Symptoms
    symptom("patient1", "fever").
    symptom("patient1", "cough").
    
    # Diagnosis rules
    diagnosis(?Patient, "flu") :- 
        symptom(?Patient, "fever"),
        symptom(?Patient, "cough").
    
    # Query
    results = query diagnosis("patient1", ?Disease)?
    
    for result in (results) {
        print(result["?Disease"])  # flu
    }
}
```

### Pattern 3: Data Processing
```bayan
hybrid {
    # Data
    scores = [85, 92, 78, 95, 88]
    
    # Processing
    average = sum(scores) / len(scores)
    high_scores = list(filter(lambda x: x >= 90, scores))
    sorted_scores = sorted(scores)
    
    print("Average: " + str(average))
    print("High scores: " + str(high_scores))
}
```

---

## Important Notes for LLMs

### ✅ DO:
1. **Always wrap code in `hybrid { ... }`**
2. **Use `:` before opening brace `{`** in control structures and functions
3. **Use braces `{ }` for all blocks** (if, for, while, def, class)
4. **End logic facts and rules with `.`**
5. **Use `?Variable` for logic variables**
6. **Support Arabic text in strings and identifiers**
7. **Use English keywords** for universal code (unless user requests Arabic)
8. **Use Causal Network Engine** for building causal reasoning systems (NEW! 🎯)

### ❌ DON'T:
1. Don't forget the `hybrid { }` wrapper
2. Don't use Python-style indentation without braces
3. Don't forget `:` before `{` in function/class/control definitions
4. Don't use `print()` with multiple arguments - use string concatenation instead
5. Don't forget `.` at the end of logic facts/rules
6. Don't confuse causal network commands with regular functions

---

## Example: Complete Program

```bayan
hybrid {
    # Imperative: Variables and data
    students_data = [
        {"name": "أحمد", "score": 85},
        {"name": "فاطمة", "score": 95},
        {"name": "علي", "score": 78}
    ]
    
    # OOP: Student class
    class Student: {
        def __init__(self, name, score): {
            self.name = name
            self.score = score
        }
        
        def is_excellent(self): {
            return self.score >= 90
        }
    }
    
    # Create objects and add to logic KB
    for data in (students_data) {
        student = Student(data["name"], data["score"])
        
        # Add to logic knowledge base
        assertz(student_record(data["name"], data["score"]))
        
        if (student.is_excellent()) {
            print(student.name + " is excellent!")
        }
    }
    
    # Logic: Query high performers
    results = query student_record(?Name, ?Score), ?Score >= 85?
    
    print("High performers:")
    for result in (results) {
        print(result["?Name"])
    }
}
```

---

## Quick Reference Card

| Feature | Syntax |
|---------|--------|
| Variable | `x = 10` |
| String | `name = "أحمد"` |
| List | `nums = [1, 2, 3]` |
| Dict | `d = {"key": "value"}` |
| If | `if x > 0: { ... }` |
| For | `for i in range(5): { ... }` |
| While | `while x < 10: { ... }` |
| Function | `def f(x): { return x * 2 }` |
| Class | `class C: { def __init__(self): { ... } }` |
| Fact | `parent("a", "b").` |
| Rule | `grandparent(?X, ?Z) :- parent(?X, ?Y), parent(?Y, ?Z).` |
| Query | `results = query parent(?X, "b")?` |
| Assert | `assertz(fact("data"))` |
| Retract | `retract(fact("data"))` |
| **Causal Network** 🎯 | |
| Create Network | `create_network("id", "name", "domain")` |
| Add Node | `add_node("net_id", "node_id", "type", "props")` |
| Add Relation | `add_causal_relation("net_id", "from", "to", "type", "strength")` |
| Infer Chain | `infer_causal_chain("net_id", "start", "end", "depth")` |
| Find Effects | `find_all_effects("net_id", "node_id", "depth")` |
| Find Causes | `find_all_causes("net_id", "node_id", "depth")` |

---

**When generating Bayan code, always follow this structure and syntax. The language is powerful and unique - use it correctly!**

---

## Complete Examples Library

### Example 1: Calculator with OOP
```bayan
hybrid {
    class Calculator: {
        def __init__(self): {
            self.history = []
        }

        def add(self, a, b): {
            result = a + b
            self.history.append("add: " + str(a) + " + " + str(b) + " = " + str(result))
            return result
        }

        def subtract(self, a, b): {
            result = a - b
            self.history.append("subtract: " + str(a) + " - " + str(b) + " = " + str(result))
            return result
        }

        def multiply(self, a, b): {
            result = a * b
            self.history.append("multiply: " + str(a) + " * " + str(b) + " = " + str(result))
            return result
        }

        def get_history(self): {
            return self.history
        }
    }

    calc = Calculator()
    r1 = calc.add(10, 5)
    r2 = calc.multiply(r1, 2)

    print("Result: " + str(r2))

    for entry in (calc.get_history()) {
        print(entry)
    }
}
```

### Example 2: Student Management System
```bayan
hybrid {
    class Student: {
        def __init__(self, name, student_id, grades): {
            self.name = name
            self.student_id = student_id
            self.grades = grades
        }

        def get_average(self): {
            if (len(self.grades) == 0) {
                return 0
            }
            return sum(self.grades) / len(self.grades)
        }

        def add_grade(self, grade): {
            self.grades.append(grade)
        }

        def get_status(self): {
            avg = self.get_average()
            if (avg >= 90) {
                return "Excellent"
            }
            elif (avg >= 80) {
                return "Very Good"
            }
            elif (avg >= 70) {
                return "Good"
            }
            elif (avg >= 60) {
                return "Pass"
            }
            else: {
                return "Fail"
            }
        }
    }

    students = [
        Student("أحمد", "S001", [85, 90, 88]),
        Student("فاطمة", "S002", [95, 92, 98]),
        Student("علي", "S003", [70, 75, 72])
    ]

    for student in (students) {
        avg = student.get_average()
        status = student.get_status()
        print(student.name + ": " + str(avg) + " - " + status)
    }
}
```

### Example 3: Family Tree with Logic Programming
```bayan
hybrid {
    # Facts: parent relationships
    parent("إبراهيم", "أحمد").
    parent("إبراهيم", "فاطمة").
    parent("أحمد", "محمد").
    parent("أحمد", "علي").
    parent("فاطمة", "سارة").

    # Facts: gender
    male("إبراهيم").
    male("أحمد").
    male("محمد").
    male("علي").
    female("فاطمة").
    female("سارة").

    # Rules
    father(?F, ?C) :- parent(?F, ?C), male(?F).
    mother(?M, ?C) :- parent(?M, ?C), female(?M).
    grandparent(?GP, ?GC) :- parent(?GP, ?P), parent(?P, ?GC).
    grandfather(?GF, ?GC) :- grandparent(?GF, ?GC), male(?GF).
    grandmother(?GM, ?GC) :- grandparent(?GM, ?GC), female(?GM).
    sibling(?X, ?Y) :- parent(?P, ?X), parent(?P, ?Y), not(?X == ?Y).

    # Queries
    print("=== Fathers ===")
    fathers = query father(?F, ?C)?
    for result in (fathers) {
        print(result["?F"] + " is father of " + result["?C"])
    }

    print("=== Grandparents ===")
    grandparents = query grandparent(?GP, ?GC)?
    for result in (grandparents) {
        print(result["?GP"] + " is grandparent of " + result["?GC"])
    }

    print("=== Siblings ===")
    siblings = query sibling(?X, ?Y)?
    for result in (siblings) {
        print(result["?X"] + " and " + result["?Y"] + " are siblings")
    }
}
```

### Example 4: Medical Expert System
```bayan
hybrid {
    # Symptoms database
    symptom("patient1", "fever").
    symptom("patient1", "cough").
    symptom("patient1", "fatigue").

    symptom("patient2", "headache").
    symptom("patient2", "nausea").

    symptom("patient3", "fever").
    symptom("patient3", "rash").
    symptom("patient3", "sore_throat").

    # Diagnosis rules
    diagnosis(?P, "flu") :-
        symptom(?P, "fever"),
        symptom(?P, "cough"),
        symptom(?P, "fatigue").

    diagnosis(?P, "migraine") :-
        symptom(?P, "headache"),
        symptom(?P, "nausea").

    diagnosis(?P, "measles") :-
        symptom(?P, "fever"),
        symptom(?P, "rash").

    # Treatment recommendations
    treatment("flu", "rest_and_fluids").
    treatment("flu", "antiviral_medication").
    treatment("migraine", "pain_relievers").
    treatment("migraine", "rest_in_dark_room").
    treatment("measles", "rest_and_isolation").
    treatment("measles", "fever_reducers").

    # Function to diagnose and recommend treatment
    def diagnose_patient(patient_id): {
        print("=== Diagnosis for " + patient_id + " ===")

        # Get diagnosis
        diag_results = query diagnosis(patient_id, ?Disease)?

        if (len(diag_results) == 0) {
            print("No diagnosis found")
            return
        }

        for diag in (diag_results) {
            disease = diag["?Disease"]
            print("Diagnosed with: " + disease)

            # Get treatments
            treat_results = query treatment(disease, ?Treatment)?
            print("Recommended treatments:")
            for treat in (treat_results) {
                print("  - " + treat["?Treatment"])
            }
        }
    }

    # Diagnose all patients
    diagnose_patient("patient1")
    diagnose_patient("patient2")
    diagnose_patient("patient3")
}
```

### Example 5: Recommendation System
```bayan
hybrid {
    # User preferences
    likes("أحمد", "programming").
    likes("أحمد", "math").
    likes("أحمد", "science").

    likes("فاطمة", "programming").
    likes("فاطمة", "art").
    likes("فاطمة", "music").

    likes("علي", "math").
    likes("علي", "science").
    likes("علي", "sports").

    likes("سارة", "programming").
    likes("سارة", "math").
    likes("سارة", "reading").

    # Rule: users are similar if they share interests
    similar_users(?U1, ?U2) :-
        likes(?U1, ?Interest),
        likes(?U2, ?Interest),
        not(?U1 == ?U2).

    # Function to get recommendations
    def get_recommendations(user): {
        print("=== Recommendations for " + user + " ===")

        # Find similar users
        similar = query similar_users(user, ?SimilarUser)?

        if (len(similar) == 0) {
            print("No similar users found")
            return
        }

        # Get unique similar users
        similar_users_list = []
        for result in (similar) {
            similar_user = result["?SimilarUser"]
            if (similar_user not in similar_users_list) {
                similar_users_list.append(similar_user)
            }
        }

        print("Similar users: " + str(similar_users_list))

        # Get interests of similar users that current user doesn't have
        user_interests_results = query likes(user, ?Interest)?
        user_interests = []
        for result in (user_interests_results) {
            user_interests.append(result["?Interest"])
        }

        recommendations = []
        for similar_user in (similar_users_list) {
            interests = query likes(similar_user, ?Interest)?
            for result in (interests) {
                interest = result["?Interest"]
                if (interest not in user_interests and interest not in recommendations) {
                    recommendations.append(interest)
                }
            }
        }

        print("Recommended interests: " + str(recommendations))
    }

    get_recommendations("أحمد")
    get_recommendations("علي")
}
```

### Example 6: Data Analysis with ML Functions
```bayan
hybrid {
    # Sample data: student scores
    data = [
        {"name": "أحمد", "math": 85, "science": 90, "english": 88},
        {"name": "فاطمة", "math": 95, "science": 92, "english": 98},
        {"name": "علي", "math": 70, "science": 75, "english": 72},
        {"name": "سارة", "math": 88, "science": 85, "english": 90},
        {"name": "محمد", "math": 92, "science": 88, "english": 85}
    ]

    # Extract scores for each subject
    math_scores = list(map(lambda x: x["math"], data))
    science_scores = list(map(lambda x: x["science"], data))
    english_scores = list(map(lambda x: x["english"], data))

    # Calculate statistics
    def calculate_stats(scores, subject): {
        avg = sum(scores) / len(scores)
        minimum = min(scores)
        maximum = max(scores)

        print("=== " + subject + " Statistics ===")
        print("Average: " + str(avg))
        print("Minimum: " + str(minimum))
        print("Maximum: " + str(maximum))
        print("Sorted: " + str(sorted(scores)))
    }

    calculate_stats(math_scores, "Math")
    calculate_stats(science_scores, "Science")
    calculate_stats(english_scores, "English")

    # Find top performers (average >= 90)
    print("=== Top Performers ===")
    for student in (data) {
        avg = (student["math"] + student["science"] + student["english"]) / 3
        if (avg >= 90) {
            print(student["name"] + ": " + str(avg))
        }
    }

    # Find students who need help (any score < 75)
    print("=== Students Needing Help ===")
    for student in (data) {
        needs_help = False
        subjects = []

        if (student["math"] < 75) {
            needs_help = True
            subjects.append("Math")
        }
        if (student["science"] < 75) {
            needs_help = True
            subjects.append("Science")
        }
        if (student["english"] < 75) {
            needs_help = True
            subjects.append("English")
        }

        if (needs_help) {
            print(student["name"] + " needs help in: " + str(subjects))
        }
    }
}
```

### Example 7: Async/Await Example
```bayan
hybrid {
    async def fetch_data(source): {
        print("Fetching from " + source + "...")
        await asyncio.sleep(1)
        return "Data from " + source
    }

    async def process_data(data): {
        print("Processing: " + data)
        await asyncio.sleep(1)
        return "Processed: " + data
    }

    async def main(): {
        # Fetch data
        data1 = await fetch_data("Database")
        data2 = await fetch_data("API")

        # Process data
        result1 = await process_data(data1)
        result2 = await process_data(data2)

        print(result1)
        print(result2)
    }

    # Run async function
    asyncio.run(main())
}
```

### Example 8: Generator Example
```bayan
hybrid {
    def fibonacci(n): {
        a = 0
        b = 1
        count = 0

        while (count < n) {
            yield a
            temp = a
            a = b
            b = temp + b
            count = count + 1
        }
    }

    print("First 10 Fibonacci numbers:")
    for num in (fibonacci(10)) {
        print(str(num))
    }

    # Generator with filter
    def even_numbers(max_num): {
        num = 0
        while (num <= max_num) {
            if (num % 2 == 0) {
                yield num
            }
            num = num + 1
        }
    }

    print("Even numbers up to 20:")
    for num in (even_numbers(20)) {
        print(str(num))
    }
}
```

### Example 9: Decorator Example
```bayan
hybrid {
    def timer_decorator(func): {
        def wrapper(*args, **kwargs): {
            print("Function " + func.__name__ + " started")
            result = func(*args, **kwargs)
            print("Function " + func.__name__ + " finished")
            return result
        }
        return wrapper
    }

    @timer_decorator
    def calculate_sum(numbers): {
        total = 0
        for num in (numbers) {
            total = total + num
        }
        return total
    }

    result = calculate_sum([1, 2, 3, 4, 5])
    print("Sum: " + str(result))
}
```

### Example 10: Complete Hybrid Application
```bayan
hybrid {
    # OOP: Define classes
    class Product: {
        def __init__(self, name, price, category): {
            self.name = name
            self.price = price
            self.category = category

            # Add to logic KB
            assertz(product(name, price, category))
        }

        def get_info(self): {
            return self.name + " - $" + str(self.price) + " (" + self.category + ")"
        }
    }

    # Create products
    products = [
        Product("Laptop", 999.99, "Electronics"),
        Product("Mouse", 29.99, "Electronics"),
        Product("Desk", 299.99, "Furniture"),
        Product("Chair", 199.99, "Furniture"),
        Product("Book", 19.99, "Books")
    ]

    # Logic: Define discount rules
    discount(?Product, 0.2) :- product(?Product, ?Price, "Electronics"), ?Price > 500.
    discount(?Product, 0.1) :- product(?Product, ?Price, "Furniture"), ?Price > 100.
    discount(?Product, 0.05) :- product(?Product, ?Price, "Books").

    # Function: Calculate final price
    def get_final_price(product_name): {
        # Get product price
        price_results = query product(product_name, ?Price, ?Category)?

        if (len(price_results) == 0) {
            return 0
        }

        price = price_results[0]["?Price"]

        # Get discount
        discount_results = query discount(product_name, ?Discount)?

        if (len(discount_results) > 0) {
            discount = discount_results[0]["?Discount"]
            final_price = price * (1 - discount)
            return final_price
        }

        return price
    }

    # Display products with prices
    print("=== Product Catalog ===")
    for product in (products) {
        original_price = product.price
        final_price = get_final_price(product.name)

        print(product.get_info())

        if (final_price < original_price) {
            discount_percent = ((original_price - final_price) / original_price) * 100
            print("  Discount: " + str(discount_percent) + "%")
            print("  Final Price: $" + str(final_price))
        }
        else: {
            print("  No discount")
        }
    }
}
```

---

### Example 11: Probabilistic Reasoning - Medical Diagnosis (NEW! 🎲)

```bayan
hybrid {
    # Patient symptoms (probabilistic facts)
    prob("has_fever", "patient1", 0.9).
    prob("has_cough", "patient1", 0.7).
    prob("has_headache", "patient1", 0.5).
    prob("has_fatigue", "patient1", 0.8).

    # Disease probabilities
    prob("has_flu", "patient1", 0.8).
    prob("has_cold", "patient1", 0.6).
    prob("has_covid", "patient1", 0.3).

    # Uncertainty tools (bilingual)
    print("=== Medical Diagnosis ===")

    # Check if flu is likely
    print("Is flu likely?")
    flu_likely = query محتمل("has_flu", "patient1")?
    if (len(flu_likely) > 0) {
        print("  Yes, flu is likely (80% > 70%)")
    }
    else: {
        print("  No, flu is not likely")
    }

    # Check if COVID is unlikely
    print("Is COVID unlikely?")
    covid_unlikely = query غير_محتمل("has_covid", "patient1")?
    if (len(covid_unlikely) > 0) {
        print("  Yes, COVID is unlikely (30% < 30%)")
    }

    # Calculate combined probability of fever AND cough
    fever_and_cough(?prob) :-
        prob("has_fever", "patient1", ?p1),
        prob("has_cough", "patient1", ?p2),
        ?prob is ?p1 * ?p2.

    print("Probability of fever AND cough:")
    result = query fever_and_cough(?p)?
    if (len(result) > 0) {
        prob_value = result[0]["?p"]
        print("  " + str(prob_value) + " (90% × 70% = 63%)")
    }

    # Conditional inference: Treatment recommendation
    recommend_antiviral("patient1", ?confidence) :-
        prob("has_flu", "patient1", ?p_flu),
        prob("has_fever", "patient1", ?p_fever),
        ?p_flu > 0.7,
        ?p_fever > 0.8,
        ?confidence is 0.9.

    print("Should we recommend antiviral treatment?")
    treatment = query recommend_antiviral("patient1", ?conf)?
    if (len(treatment) > 0) {
        confidence = treatment[0]["?conf"]
        print("  Yes, with " + str(confidence * 100) + "% confidence")
    }
    else: {
        print("  No, conditions not met")
    }
}
```

**Probabilistic Keywords:**
- `prob(fact, entity, probability)` - Define probabilistic fact
- `ربما/maybe` - probability > 50%
- `محتمل/likely` - probability > 70%
- `غير_محتمل/unlikely` - probability < 30%
- `ممكن/possible` - probability between 20% and 80%
- `مؤكد/certain` - probability > 95%

**Probabilistic Operations:**
- AND: `P(A ∧ B) = P(A) × P(B)`
- NOT: `P(¬A) = 1 - P(A)`

---

## Example 12: Causal Network Engine (NEW! 🎯)

### Building a Scientific Theory Network

```bayan
hybrid {
    # Create a physics network
    create_network("physics", "قوانين نيوتن", "scientific")

    # Add physics concepts
    add_node("physics", "قوة", "concept", "مفهوم فيزيائي")
    add_node("physics", "كتلة", "property", "خاصية")
    add_node("physics", "تسارع", "concept", "مفهوم فيزيائي")
    add_node("physics", "سرعة", "state", "حالة")
    add_node("physics", "حركة", "state", "حالة")
    add_node("physics", "طاقة_حركية", "concept", "مفهوم فيزيائي")

    # Newton's laws as causal relations
    add_causal_relation("physics", "قوة", "تسارع", "causes", "0.95")
    add_causal_relation("physics", "كتلة", "تسارع", "affects", "0.9")
    add_causal_relation("physics", "تسارع", "سرعة", "leads_to", "0.9")
    add_causal_relation("physics", "سرعة", "حركة", "causes", "0.95")
    add_causal_relation("physics", "حركة", "طاقة_حركية", "results_in", "0.9")

    # Causal inference: How does force lead to kinetic energy?
    print("=== السلسلة السببية: من القوة إلى الطاقة الحركية ===")
    infer_causal_chain("physics", "قوة", "طاقة_حركية", "5")
    # Result: قوة → تسارع → سرعة → حركة → طاقة_حركية

    # Find all effects of force
    print("\n=== جميع تأثيرات القوة ===")
    find_all_effects("physics", "قوة", "3")
    # Result: تسارع، سرعة، حركة، طاقة_حركية

    # Analyze the network
    print("\n=== تحليل الشبكة ===")
    analyze_network("physics")
}
```

### Building a Psychological Network

```bayan
hybrid {
    # Create psychological network
    create_network("psych", "الحالات النفسية", "psychological")

    # Add psychological states
    add_node("psych", "ضغط_نفسي", "state", "حالة نفسية")
    add_node("psych", "قلق", "emotion", "عاطفة")
    add_node("psych", "أرق", "state", "حالة")
    add_node("psych", "تعب", "state", "حالة")
    add_node("psych", "استرخاء", "state", "حالة")
    add_node("psych", "راحة", "state", "حالة")

    # Negative causal chain
    add_causal_relation("psych", "ضغط_نفسي", "قلق", "causes", "0.9")
    add_causal_relation("psych", "قلق", "أرق", "leads_to", "0.8")
    add_causal_relation("psych", "أرق", "تعب", "causes", "0.95")

    # Positive causal chain
    add_causal_relation("psych", "استرخاء", "راحة", "leads_to", "0.9")

    # Inverse relation
    add_causal_relation("psych", "استرخاء", "قلق", "weakens", "0.85")

    # Query: How to reduce anxiety?
    print("=== كيف أتخلص من القلق؟ ===")
    results = query causal_relation(?From, "قلق", "weakens", ?Strength)?

    for result in (results) {
        solution = result["?From"]
        strength = result["?Strength"]
        print("الحل: " + solution + " (قوة: " + strength + ")")
    }

    # Find causes of fatigue
    print("\n=== أسباب التعب ===")
    find_all_causes("psych", "تعب", "3")
    # Result: أرق، قلق، ضغط_نفسي
}
```

### Building a Social Network

```bayan
hybrid {
    # Create social network
    create_network("social", "العلاقات الاجتماعية", "social")

    # Add social behaviors and emotions
    add_node("social", "صدق", "behavior", "سلوك")
    add_node("social", "ثقة", "emotion", "عاطفة")
    add_node("social", "احترام", "emotion", "عاطفة")
    add_node("social", "تعاون", "behavior", "سلوك")
    add_node("social", "نجاح_مشترك", "state", "حالة")

    # Build causal chain
    add_causal_relation("social", "صدق", "ثقة", "causes", "0.9")
    add_causal_relation("social", "ثقة", "احترام", "leads_to", "0.85")
    add_causal_relation("social", "احترام", "تعاون", "enables", "0.8")
    add_causal_relation("social", "تعاون", "نجاح_مشترك", "leads_to", "0.9")

    # Function to get relationship advice
    def get_advice(goal): {
        print("=== كيف أصل إلى: " + goal + "؟ ===")

        # Find all causes
        causes = find_all_causes("social", goal, "4")

        print("الخطوات المقترحة:")
        for cause in (causes) {
            print("  - " + cause)
        }

        # Find causal path
        print("\nالمسار السببي:")
        infer_causal_chain("social", "صدق", goal, "5")
    }

    # Use the system
    get_advice("نجاح_مشترك")
    # Result: ابدأ بالصدق → ثقة → احترام → تعاون → نجاح مشترك
}
```

**Key Causal Network Commands:**
- `create_network(id, name, domain)` - Create new network
- `add_node(net_id, node_id, type, properties)` - Add node
- `add_causal_relation(net_id, from, to, type, strength)` - Add causal relation
- `infer_causal_chain(net_id, start, end, depth)` - Find causal path
- `find_all_effects(net_id, node_id, depth)` - Find all effects
- `find_all_causes(net_id, node_id, depth)` - Find all causes
- `analyze_network(net_id)` - Analyze network structure

**Supported Domains:**
- `professional` - المهن والحياة اليومية
- `social` - العلاقات الاجتماعية
- `psychological` - الحالات النفسية
- `scientific` - القوانين العلمية
- `philosophical` - النظريات الفلسفية
- `historical` - الأحداث التاريخية
- `custom` - أي مجال مخصص

**12 Causal Relation Types:**
- `causes`, `enables`, `prevents`, `requires`, `leads_to`, `results_from`
- `enhances`, `weakens`, `correlates_with`, `contradicts`, `complements`, `depends_on`

---

## Tips for Writing Clean Bayan Code

1. **Always use meaningful variable names** (Arabic or English)
2. **Add comments** to explain complex logic
3. **Use functions** to organize code
4. **Combine paradigms** when it makes sense
5. **Use logic programming** for rules and queries
6. **Use OOP** for data structures and encapsulation
7. **Use imperative** for sequential operations
8. **Use probabilistic reasoning** for uncertainty and decision-making
9. **Use causal networks** for building theories and reasoning systems (NEW! 🎯)
10. **Test your code** with different inputs

---

**These examples demonstrate the full power of Bayan. Use them as templates when generating code!**

