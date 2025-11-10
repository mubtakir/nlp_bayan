# دليل لغة البيان - الجزء الثالث: البرمجة المنطقية
# Bayan Language Guide - Part 3: Logic Programming

<div dir="rtl">
> Note: This tutorial is large and will be split into multiple parts (Part 1/2/3). See docs/ENTITY_SYSTEM_GUIDE.md for the new Entity System (0..1).



> الأجزاء: [PART1](03_LOGIC_PROGRAMMING_AR_PART1.md) | [PART2](03_LOGIC_PROGRAMMING_AR_PART2.md) | [PART3](03_LOGIC_PROGRAMMING_AR_PART3.md) | [PART4](03_LOGIC_PROGRAMMING_AR_PART4.md)


## 📚 جدول المحتويات

### القسم الأول: الأساسيات (للمبتدئين)
1. [مقدمة في البرمجة المنطقية](#1-مقدمة-في-البرمجة-المنطقية)
2. [الحقائق (Facts)](#2-الحقائق-facts)
3. [الاستعلامات (Queries)](#3-الاستعلامات-queries)
4. [المتغيرات المنطقية](#4-المتغيرات-المنطقية)
5. [القواعد البسيطة (Rules)](#5-القواعد-البسيطة-rules)

### القسم الثاني: المستوى المتوسط
6. [القواعد المركبة](#6-القواعد-المركبة)
7. [العودية (Recursion)](#7-العودية-recursion)
8. [القوائم في البرمجة المنطقية](#8-القوائم-في-البرمجة-المنطقية)
9. [العمليات المنطقية](#9-العمليات-المنطقية)

### القسم الثالث: المستوى المتقدم
10. [Meta-predicates](#10-meta-predicates)
11. [قاعدة المعرفة الديناميكية](#11-قاعدة-المعرفة-الديناميكية)
12. [البرمجة الهجينة](#12-البرمجة-الهجينة)
13. [أمثلة متقدمة](#13-أمثلة-متقدمة)
14. [الاستدلال الاحتمالي والتشكيك](#14-الاستدلال-الاحتمالي-والتشكيك-جديد-) 🎲 **(جديد!)**
15. [محرك الشبكات السببية](#15-محرك-الشبكات-السببية-جديد-) 🎯 **(جديد!)**

---

# القسم الأول: الأساسيات

## 1. مقدمة في البرمجة المنطقية

### 1.1 ما هي البرمجة المنطقية؟

البرمجة المنطقية هي نمط برمجي يعتمد على:
- **الحقائق** (Facts): معلومات صحيحة
- **القواعد** (Rules): علاقات منطقية
- **الاستعلامات** (Queries): أسئلة نطرحها

### 1.2 الفرق بين البرمجة الإجرائية والمنطقية

**البرمجة الإجرائية:**
```bayan
hybrid {
    # نخبر الحاسوب "كيف" يفعل الشيء
    def is_parent(person1, person2): {
        if person1 == "أحمد" and person2 == "محمد": {
            return True
        }
        return False
    }
}
```

**البرمجة المنطقية:**
```bayan
hybrid {
    # نخبر الحاسوب "ماذا" نريد
    parent("أحمد", "محمد").

    # الحاسوب يستنتج الإجابة
    results = query parent("أحمد", ?X)?
}
```

---

## 2. الحقائق (Facts)

### 2.1 حقيقة بسيطة

```bayan
hybrid {
    # حقيقة: أحمد هو أب محمد
    parent("أحمد", "محمد").

    # حقيقة: محمد هو أب علي
    parent("محمد", "علي").
}
```

### 2.2 حقائق متعددة

```bayan
hybrid {
    # علاقات الأبوة
    parent("أحمد", "محمد").
    parent("أحمد", "فاطمة").
    parent("محمد", "علي").
    parent("محمد", "سارة").

    # الأعمار
    age("أحمد", 50).
    age("محمد", 25).
    age("علي", 5).
}
```

### 2.3 حقائق بأنواع مختلفة

```bayan
hybrid {
    # نصوص
    city("الرياض").
    city("جدة").

    # أرقام
    temperature("الرياض", 35).
    temperature("جدة", 32).

    # قيم منطقية
    is_capital("الرياض", True).
    is_capital("جدة", False).
}
```

---

## 3. الاستعلامات (Queries)

### 3.1 استعلام بسيط

```bayan
hybrid {
    # حقائق
    parent("أحمد", "محمد").
    parent("محمد", "علي").

    # استعلام: هل أحمد أب محمد؟
    results = query parent("أحمد", "محمد")?

    if len(results) > 0: {
        print("نعم، أحمد أب محمد")
    }
}
```

### 3.2 استعلام مع متغير

```bayan
hybrid {
    # حقائق
    parent("أحمد", "محمد").
    parent("أحمد", "فاطمة").

    # استعلام: من هم أبناء أحمد؟
    results = query parent("أحمد", ?Child)?

    for result in results: {
        child = result["?Child"]
        print(child)  # محمد، فاطمة
    }
}
```

### 3.3 استعلام مع متغيرات متعددة

```bayan
hybrid {
    # حقائق
    parent("أحمد", "محمد").
    parent("فاطمة", "سارة").

    # استعلام: من هم جميع الآباء والأبناء؟
    results = query parent(?Parent, ?Child)?

    for result in results: {
        parent_name = result["?Parent"]
        child_name = result["?Child"]
        print(parent_name)
        print(child_name)
    }
}
```

---

## 4. المتغيرات المنطقية

### 4.1 تعريف المتغيرات

في البرمجة المنطقية، المتغيرات تبدأ بـ `?`:

```bayan
hybrid {
    # ?X متغير
    # "أحمد" ثابت

    parent("أحمد", "محمد").

    results = query parent(?X, "محمد")?
    # ?X سيكون "أحمد"
}
```

### 4.2 متغيرات متعددة

```bayan
hybrid {
    likes("أحمد", "برمجة").
    likes("فاطمة", "رياضيات").
    likes("علي", "برمجة").

    # من يحب ماذا؟
    results = query likes(?Person, ?Thing)?

    for result in results: {
        person = result["?Person"]
        thing = result["?Thing"]
        print(person + " يحب " + thing)
    }
}
```

### 4.3 نفس المتغير في أماكن متعددة

```bayan
hybrid {
    likes("أحمد", "برمجة").
    likes("أحمد", "رياضيات").
    likes("فاطمة", "برمجة").

    # من يحب البرمجة؟
    results = query likes(?Person, "برمجة")?

    for result in results: {
        print(result["?Person"])  # أحمد، فاطمة
    }
}
```

---

## 5. القواعد البسيطة (Rules)

### 5.1 قاعدة بسيطة

```bayan
hybrid {
    # حقائق
    parent("أحمد", "محمد").
    parent("محمد", "علي").

    # قاعدة: X جد Z إذا كان X أب Y و Y أب Z
    grandparent(?X, ?Z) :- parent(?X, ?Y), parent(?Y, ?Z).

    # استعلام
    results = query grandparent(?GP, "علي")?

    for result in results: {
        print(result["?GP"])  # أحمد
    }
}
```

### 5.2 قاعدة مع شرط واحد

```bayan
hybrid {
    # حقائق
    male("أحمد").
    male("محمد").
    female("فاطمة").

    parent("أحمد", "محمد").
    parent("أحمد", "فاطمة").

    # قاعدة: X أب Y إذا كان X ذكر و X والد Y
    father(?X, ?Y) :- male(?X), parent(?X, ?Y).

    # استعلام
    results = query father(?F, "محمد")?

    for result in results: {
        print(result["?F"])  # أحمد
    }
}
```

### 5.3 قواعد متعددة

```bayan
hybrid {
    # حقائق
    male("أحمد").
    male("محمد").
    female("فاطمة").
    female("سارة").

    parent("أحمد", "محمد").
    parent("أحمد", "فاطمة").

    # قواعد
    father(?X, ?Y) :- male(?X), parent(?X, ?Y).
    mother(?X, ?Y) :- female(?X), parent(?X, ?Y).

    # استعلامات
    fathers = query father(?F, ?C)?
    mothers = query mother(?M, ?C)?

    print("الآباء:")
    for result in fathers: {
        print(result["?F"])
    }

    print("الأمهات:")
    for result in mothers: {
        print(result["?M"])
    }
}
```

---

# القسم الثاني: المستوى المتوسط

## 6. القواعد المركبة

### 6.1 قاعدة بشروط متعددة

```bayan
hybrid {
    # حقائق
    parent("أحمد", "محمد").
    parent("فاطمة", "محمد").
    parent("محمد", "علي").

    male("أحمد").
    male("محمد").
    female("فاطمة").

    # قاعدة: X جد Y إذا كان X ذكر و X جد Y
    grandfather(?X, ?Z) :- male(?X), parent(?X, ?Y), parent(?Y, ?Z).

    results = query grandfather(?GF, "علي")?

    for result in results: {
        print(result["?GF"])  # أحمد
    }
}
```

### 6.2 قواعد متداخلة

```bayan
hybrid {
    # حقائق
    parent("أحمد", "محمد").
    parent("محمد", "علي").
    parent("علي", "حسن").

    # قواعد
    grandparent(?X, ?Z) :- parent(?X, ?Y), parent(?Y, ?Z).
    great_grandparent(?X, ?W) :- parent(?X, ?Y), grandparent(?Y, ?W).

    # استعلام
    results = query great_grandparent(?GGP, "حسن")?

    for result in results: {
        print(result["?GGP"])  # أحمد
    }
}
```

### 6.3 قواعد مع OR

```bayan
hybrid {
    # حقائق
    parent("أحمد", "محمد").
    parent("فاطمة", "سارة").

    # قاعدة: X قريب Y إذا كان X والد Y أو Y والد X
    related(?X, ?Y) :- parent(?X, ?Y).
    related(?X, ?Y) :- parent(?Y, ?X).

    results = query related("أحمد", ?R)?

    for result in results: {
        print(result["?R"])
    }
}
```

---

## 7. العودية (Recursion)

### 7.1 عودية بسيطة - الأسلاف

```bayan
hybrid {
    # حقائق
    parent("أحمد", "محمد").
    parent("محمد", "علي").
    parent("علي", "حسن").

    # قاعدة عودية: X سلف Y
    ancestor(?X, ?Y) :- parent(?X, ?Y).
    ancestor(?X, ?Z) :- parent(?X, ?Y), ancestor(?Y, ?Z).

    # استعلام: من هم أسلاف حسن؟
    results = query ancestor(?A, "حسن")?

    for result in results: {
        print(result["?A"])  # علي، محمد، أحمد
    }
}
```

### 7.2 عودية - حساب العدد

```bayan
hybrid {
    # حقيقة: 0 عدد
    number(0).

    # قاعدة عودية: إذا كان N عدد، فإن N+1 عدد
    number(?N1) :- number(?N), ?N1 = ?N + 1, ?N < 10.

    # استعلام
    results = query number(?N)?

    for result in results: {
        print(result["?N"])  # 0, 1, 2, ..., 10
    }
}
```

---

## 8. القوائم في البرمجة المنطقية

### 8.1 قوائم بسيطة

```bayan
hybrid {
    # حقيقة بقائمة
    scores("أحمد", [85, 90, 88]).
    scores("فاطمة", [92, 95, 89]).

    # استعلام
    results = query scores("أحمد", ?Scores)?

    for result in results: {
        scores_list = result["?Scores"]
        print(scores_list)  # [85, 90, 88]
    }
}
```

### 8.2 عضو في قائمة

```bayan
hybrid {
    # قاعدة: X عضو في قائمة
    member(?X, [?X | ?Tail]).
    member(?X, [?Head | ?Tail]) :- member(?X, ?Tail).

    # استعلام
    results = query member(2, [1, 2, 3])?

    if len(results) > 0: {
        print("2 موجود في القائمة")
    }
}
```

### 8.3 طول القائمة

```bayan
hybrid {
    # قاعدة: طول قائمة فارغة = 0
    list_length([], 0).

    # قاعدة عودية: طول قائمة = 1 + طول الباقي
    list_length([?H | ?T], ?N) :- list_length(?T, ?N1), ?N = ?N1 + 1.

    # استعلام
    results = query list_length([1, 2, 3, 4], ?Len)?

    for result in results: {
        print(result["?Len"])  # 4
    }
}
```

---

## 9. العمليات المنطقية

### 9.1 AND (,)

```bayan
hybrid {
    # حقائق
    student("أحمد").
    student("فاطمة").

    grade("أحمد", 85).
    grade("فاطمة", 92).

    # استعلام: طلاب بدرجة أكبر من 80
    results = query student(?S), grade(?S, ?G), ?G > 80?

    for result in results: {
        print(result["?S"])
    }
}
```

### 9.2 OR (;)

```bayan
hybrid {
    # حقائق
    likes("أحمد", "برمجة").
    likes("فاطمة", "رياضيات").

    # قاعدة: X يحب علوم إذا كان يحب برمجة أو رياضيات
    likes_science(?X) :- likes(?X, "برمجة"); likes(?X, "رياضيات").

    results = query likes_science(?Person)?

    for result in results: {
        print(result["?Person"])
    }
}
```

### 9.3 NOT

```bayan
hybrid {
    # حقائق
    student("أحمد").
    student("فاطمة").
    student("علي").

    passed("أحمد").
    passed("فاطمة").

    # قاعدة: X راسب إذا كان طالب ولم ينجح
    failed(?X) :- student(?X), not(passed(?X)).

    results = query failed(?S)?

    for result in results: {
        print(result["?S"])  # علي
    }
}
```

---

# القسم الثالث: المستوى المتقدم

## 10. Meta-predicates

### 10.1 findall/3

`findall/3` يجمع جميع الحلول في قائمة:

```bayan
hybrid {
    # حقائق
    score("أحمد", 85).
    score("فاطمة", 92).
    score("علي", 78).
    score("سارة", 95).

    # جمع جميع الدرجات
    results = query findall(?Score, score(?Name, ?Score), ?AllScores)?

    for result in results: {
        all_scores = result["?AllScores"]
        print(all_scores)  # [85, 92, 78, 95]
    }
}
```

### 10.2 findall مع شرط

```bayan
hybrid {
    # حقائق
    score("أحمد", 85).
    score("فاطمة", 92).
    score("علي", 78).
    score("سارة", 95).

    # جمع الدرجات الأكبر من 80
    goal = score(?Name, ?Score), ?Score > 80
    results = query findall(?Score, goal, ?HighScores)?

    for result in results: {
        high_scores = result["?HighScores"]
        print(high_scores)  # [85, 92, 95]
    }
}
```

### 10.3 bagof/3

`bagof/3` مثل `findall` لكنه يفشل إذا لم توجد حلول:

```bayan
hybrid {
    # حقائق
    class_member("أحمد", "class_a").
    class_member("فاطمة", "class_a").
    class_member("علي", "class_b").

    score("أحمد", 85).
    score("فاطمة", 92).
    score("علي", 78).

    # جمع درجات class_a
    goal = class_member(?Name, "class_a"), score(?Name, ?Score)
    results = query bagof(?Score, goal, ?Scores)?

    for result in results: {
        scores = result["?Scores"]
        print(scores)  # [85, 92]
    }
}
```

### 10.4 setof/3

`setof/3` يجمع حلول فريدة ومرتبة:

```bayan
hybrid {
    # حقائق
    likes("أحمد", "برمجة").
    likes("فاطمة", "برمجة").
    likes("علي", "رياضيات").
    likes("سارة", "برمجة").

    # جمع المواد المحبوبة (بدون تكرار)
    results = query setof(?Subject, likes(?Person, ?Subject), ?Subjects)?

    for result in results: {
        subjects = result["?Subjects"]
        print(subjects)  # ["برمجة", "رياضيات"]
    }
}
```

---

## 11. قاعدة المعرفة الديناميكية

### 11.1 assertz - إضافة حقيقة في النهاية

```bayan
hybrid {
    # حقائق أولية
    student("أحمد").
    student("فاطمة").

    # إضافة طالب جديد
    assertz(student("علي"))

    # استعلام
    results = query student(?S)?

    for result in results: {
        print(result["?S"])  # أحمد، فاطمة، علي
    }
}
```

### 11.2 asserta - إضافة حقيقة في البداية

```bayan
hybrid {
    # حقائق أولية
    priority("task2", 2).
    priority("task3", 3).

    # إضافة مهمة ذات أولوية عالية
    asserta(priority("task1", 1))

    # استعلام
    results = query priority(?Task, ?P)?

    for result in results: {
        print(result["?Task"])  # task1، task2، task3
    }
}
```

### 11.3 retract - حذف حقيقة

```bayan
hybrid {
    # حقائق
    student("أحمد").
    student("فاطمة").
    student("علي").

    # حذف طالب
    retract(student("فاطمة"))

    # استعلام
    results = query student(?S)?

    for result in results: {
        print(result["?S"])  # أحمد، علي
    }
}
```

### 11.4 retractall - حذف جميع الحقائق المطابقة

```bayan
hybrid {
    # حقائق
    temp_data("item1", 100).
    temp_data("item2", 200).
    temp_data("item3", 300).

    # حذف جميع البيانات المؤقتة
    retractall(temp_data(?X, ?Y))

    # استعلام
    results = query temp_data(?Item, ?Value)?

    print(len(results))  # 0
}
```

---

## 12. البرمجة الهجينة

### 12.1 دمج البرمجة الإجرائية والمنطقية

```bayan
hybrid {
    # الجزء المنطقي: قاعدة المعرفة
    parent("أحمد", "محمد").
    parent("محمد", "علي").

    grandparent(?X, ?Z) :- parent(?X, ?Y), parent(?Y, ?Z).

    # الجزء الإجرائي: معالجة النتائج
    results = query grandparent(?GP, "علي")?

    for result in results: {
        gp_name = result["?GP"]
        message = "الجد هو: " + gp_name
        print(message)
    }
}
```

### 12.2 استخدام OOP مع البرمجة المنطقية

```bayan
hybrid {
    # صنف لتمثيل شخص
    class Person: {
        def __init__(self, name, age): {
            self.name = name
            self.age = age
        }

        def display(self): {
            print(self.name + " - " + str(self.age))
        }
    }

    # إنشاء كائنات
    ahmad = Person("أحمد", 50)
    mohamed = Person("محمد", 25)

    # حقائق منطقية
    parent("أحمد", "محمد").

    # استعلام ودمج النتائج
    results = query parent(?P, "محمد")?

    for result in results: {
        parent_name = result["?P"]
        if parent_name == "أحمد": {
            ahmad.display()
        }
    }
}
```

### 12.3 قاعدة معرفة ديناميكية مع دوال

```bayan
hybrid {
    # دالة لإضافة طالب
    def add_student(name, grade): {
        assertz(student(name, grade))
    }

    # دالة للبحث عن الطلاب المتفوقين
    def find_excellent_students(): {
        results = query student(?Name, ?Grade), ?Grade >= 90?

        excellent = []
        for result in results: {
            excellent.append(result["?Name"])
        }

        return excellent
    }

    # استخدام الدوال
    add_student("أحمد", 85)
    add_student("فاطمة", 95)
    add_student("علي", 92)

    top_students = find_excellent_students()

    for student in top_students: {
        print(student)  # فاطمة، علي
    }
}
```

---

## 13. أمثلة متقدمة

### 13.1 نظام خبير طبي بسيط

```bayan
hybrid {
    # الأعراض
    symptom("patient1", "fever").
    symptom("patient1", "cough").
    symptom("patient2", "headache").
    symptom("patient2", "fever").

    # قواعد التشخيص
    diagnosis(?Patient, "flu") :-
        symptom(?Patient, "fever"),
        symptom(?Patient, "cough").

    diagnosis(?Patient, "migraine") :-
        symptom(?Patient, "headache").

    # دالة للتشخيص
    def diagnose_patient(patient_name): {
        results = query diagnosis(patient_name, ?Disease)?

        if len(results) > 0: {
            disease = results[0]["?Disease"]
            return disease
        }

        return "غير معروف"
    }

    # استخدام النظام
    diagnosis1 = diagnose_patient("patient1")
    print("Patient 1: " + diagnosis1)  # flu

    diagnosis2 = diagnose_patient("patient2")
    print("Patient 2: " + diagnosis2)  # migraine
}
```

### 13.2 نظام توصيات

```bayan
hybrid {
    # تفضيلات المستخدمين
    likes("أحمد", "برمجة").
    likes("أحمد", "رياضيات").
    likes("فاطمة", "برمجة").
    likes("فاطمة", "فيزياء").
    likes("علي", "رياضيات").

    # قاعدة: مستخدمان متشابهان إذا أحبا نفس الشيء
    similar(?User1, ?User2) :-
        likes(?User1, ?Thing),
        likes(?User2, ?Thing),
        ?User1 != ?User2.

    # دالة للحصول على توصيات
    def get_recommendations(user): {
        # البحث عن مستخدمين متشابهين
        similar_users = query similar(user, ?Other)?

        recommendations = []

        for result in similar_users: {
            other_user = result["?Other"]

            # البحث عن ما يحبه المستخدم المشابه
            likes_results = query likes(other_user, ?Thing)?

            for like_result in likes_results: {
                thing = like_result["?Thing"]

                # التحقق من أن المستخدم الحالي لا يحبه بالفعل
                already_likes = query likes(user, thing)?

                if len(already_likes) == 0: {
                    if thing not in recommendations: {
                        recommendations.append(thing)
                    }
                }
            }
        }

        return recommendations
    }

    # الحصول على توصيات لأحمد
    recs = get_recommendations("أحمد")

    print("توصيات لأحمد:")
    for rec in recs: {
        print(rec)  # فيزياء
    }
}
```

### 13.3 معالجة بيانات ML

```bayan
hybrid {
    # بيانات تدريب
    training_sample("sample1", "class_a", 0.8).
    training_sample("sample2", "class_a", 0.9).
    training_sample("sample3", "class_b", 0.3).
    training_sample("sample4", "class_b", 0.2).

    # دالة لحساب متوسط درجات صنف
    def calculate_class_average(class_name): {
        # جمع جميع الدرجات للصنف
        goal = training_sample(?ID, class_name, ?Score)
        results = query findall(?Score, goal, ?Scores)?

        if len(results) > 0: {
            scores = results[0]["?Scores"]

            # حساب المتوسط
            total = sum(scores)
            average = total / len(scores)

            return average
        }

        return 0
    }

    # حساب المتوسطات
    avg_a = calculate_class_average("class_a")
    avg_b = calculate_class_average("class_b")

    print("Class A average: " + str(avg_a))  # 0.85
    print("Class B average: " + str(avg_b))  # 0.25
}
```

### 13.4 رسم بياني للمعرفة (Knowledge Graph)

```bayan
hybrid {
    # علاقات في رسم بياني
    connected("الرياض", "جدة").
    connected("جدة", "مكة").
    connected("مكة", "المدينة").
    connected("الرياض", "الدمام").

    distance("الرياض", "جدة", 950).
    distance("جدة", "مكة", 80).
    distance("مكة", "المدينة", 400).
    distance("الرياض", "الدمام", 400).

    # قاعدة: يمكن الوصول من A إلى B
    reachable(?A, ?B) :- connected(?A, ?B).
    reachable(?A, ?C) :- connected(?A, ?B), reachable(?B, ?C).

    # دالة للبحث عن مسار
    def find_path(start, end): {
        results = query reachable(start, end)?

        if len(results) > 0: {
            return True
        }

        return False
    }

    # دالة لحساب المسافة الكلية
    def calculate_distance(city1, city2): {
        results = query distance(city1, city2, ?Dist)?

        if len(results) > 0: {
            return results[0]["?Dist"]
        }

        return 0
    }

    # استخدام النظام
    can_reach = find_path("الرياض", "المدينة")
    print("Can reach: " + str(can_reach))  # True

    dist = calculate_distance("الرياض", "جدة")
    print("Distance: " + str(dist))  # 950
}
```

### 13.5 نظام قواعد الأعمال

```bayan
hybrid {
    # حقائق عن الموظفين
    employee("أحمد", "مهندس", 5).
    employee("فاطمة", "مدير", 10).
    employee("علي", "مبرمج", 2).

    salary("مهندس", 8000).
    salary("مدير", 15000).
    salary("مبرمج", 6000).

    # قواعد الترقية
    eligible_for_promotion(?Name) :-
        employee(?Name, ?Position, ?Years),
        ?Years >= 5.

    # قواعد المكافأة
    bonus_percentage(?Name, 20) :-
        employee(?Name, ?Position, ?Years),
        ?Years >= 10.

    bonus_percentage(?Name, 10) :-
        employee(?Name, ?Position, ?Years),
        ?Years >= 5,
        ?Years < 10.

    bonus_percentage(?Name, 5) :-
        employee(?Name, ?Position, ?Years),
        ?Years < 5.

    # دالة لحساب الراتب الكلي
    def calculate_total_salary(name): {
        # الحصول على الراتب الأساسي
        emp_results = query employee(name, ?Position, ?Years)?

        if len(emp_results) == 0: {
            return 0
        }

        position = emp_results[0]["?Position"]

        salary_results = query salary(position, ?BaseSalary)?
        base_salary = salary_results[0]["?BaseSalary"]

        # الحصول على نسبة المكافأة
        bonus_results = query bonus_percentage(name, ?Bonus)?
        bonus_percent = bonus_results[0]["?Bonus"]

        # حساب الراتب الكلي
        bonus_amount = base_salary * bonus_percent / 100
        total = base_salary + bonus_amount

        return total
    }

    # حساب الرواتب
    ahmad_salary = calculate_total_salary("أحمد")
    print("أحمد: " + str(ahmad_salary))  # 8800

    fatima_salary = calculate_total_salary("فاطمة")
    print("فاطمة: " + str(fatima_salary))  # 18000

    # البحث عن المؤهلين للترقية
    promotion_results = query eligible_for_promotion(?Name)?

    print("مؤهلون للترقية:")
    for result in promotion_results: {
        print(result["?Name"])  # أحمد، فاطمة
    }
}
```

---

## 🎓 خاتمة

الآن أصبحت تعرف البرمجة المنطقية في لغة البيان من المبتدئ إلى المحترف!

### 📚 ما تعلمته:

#### المستوى الأساسي:
- ✅ الحقائق والاستعلامات
- ✅ المتغيرات المنطقية
- ✅ القواعد البسيطة

#### المستوى المتوسط:
- ✅ القواعد المركبة
- ✅ العودية (Recursion)
- ✅ القوائم في البرمجة المنطقية
- ✅ العمليات المنطقية (AND, OR, NOT)

#### المستوى المتقدم:
- ✅ Meta-predicates (findall, bagof, setof)
- ✅ قاعدة المعرفة الديناميكية (assert, retract)
- ✅ البرمجة الهجينة (دمج الأنماط الثلاثة)
- ✅ أمثلة متقدمة (أنظمة خبيرة، توصيات، ML، Knowledge Graphs)

### 💡 نصائح للإتقان:

1. **ابدأ بسيطاً**: ابدأ بحقائق واستعلامات بسيطة
2. **فكر منطقياً**: البرمجة المنطقية تعتمد على "ماذا" وليس "كيف"
3. **استخدم العودية**: العودية قوية جداً في البرمجة المنطقية
4. **جرب الهجين**: دمج الأنماط الثلاثة يعطيك قوة هائلة
5. **اكتب أمثلة**: الممارسة هي المفتاح

### 🚀 التطبيقات العملية:

البرمجة المنطقية مثالية لـ:
- 🧠 **الأنظمة الخبيرة** (Expert Systems)
- 🤖 **الذكاء الاصطناعي** (AI Reasoning)
- 📊 **تحليل البيانات** (Data Analysis)
- 🔍 **محركات البحث** (Search Engines)
- 💼 **قواعد الأعمال** (Business Rules)
- 🌐 **رسوم المعرفة** (Knowledge Graphs)

### 📖 المراجع:

- **[الجزء الأول: مقدمة](01_INTRODUCTION_AR.md)** - تعريف بلغة البيان
- **[الجزء الثاني: البرمجة الإجرائية والكائنية](02_PROCEDURAL_OOP_AR.md)** - دليل شامل للـ OOP

---

<a id="probabilities"></a>

## 14. الاستدلال الاحتمالي والتشكيك (جديد! 🎲)

### 14.1 مقدمة

**الاستدلال الاحتمالي** هو قدرة جديدة في لغة البيان تتيح لك:
- التعبير عن الحقائق غير المؤكدة باحتمالات رقمية
- استخدام أدوات تشكيك ثنائية اللغة (عربي + إنجليزي)
- حساب احتمالات الحالات المتعددة
- الاستدلال الشرطي المبني على الاحتمالات

**الميزة الفريدة:** شفافية كاملة - كل احتمال قابل للتفسير والتتبع!

---

### 14.2 الحقائق الاحتمالية

#### الصيغة الأساسية:

```bayan
hybrid {
    prob("fact_name", "entity", probability).
}
```

- `fact_name`: اسم الحقيقة (string)
- `entity`: الكيان المعني (string)
- `probability`: الاحتمال (رقم بين 0.0 و 1.0)

#### مثال بسيط:

```bayan
hybrid {
    # حقائق احتمالية عن الطقس
    prob("is_sunny", "tomorrow", 0.8).
    prob("is_rainy", "tomorrow", 0.2).
    prob("is_hot", "tomorrow", 0.6).

    # استعلام
    query prob("is_sunny", "tomorrow", ?p).
    # النتيجة: ?p = 0.8
}
```

---

### 14.3 أدوات التشكيك (ثنائية اللغة)

لغة البيان توفر 5 أدوات تشكيك بالعربية والإنجليزية:

| العربية | English | الشرط | المعنى |
|---------|---------|-------|--------|
| `ربما` | `maybe` | `p > 0.5` | احتمال أكثر من 50% |
| `محتمل` | `likely` | `p > 0.7` | احتمال أكثر من 70% |
| `غير_محتمل` | `unlikely` | `p < 0.3` | احتمال أقل من 30% |
| `ممكن` | `possible` | `0.2 < p < 0.8` | احتمال بين 20% و 80% |
| `مؤكد` | `certain` | `p > 0.95` | احتمال أكثر من 95% |

#### مثال الاستخدام:

```bayan
hybrid {
    # حقائق احتمالية
    prob("will_rain", "tomorrow", 0.75).
    prob("will_snow", "tomorrow", 0.15).

    # أدوات التشكيك بالعربية
    query ربما("will_rain", "tomorrow").      # نعم (75% > 50%)
    query محتمل("will_rain", "tomorrow").     # نعم (75% > 70%)
    query غير_محتمل("will_snow", "tomorrow"). # نعم (15% < 30%)

    # أدوات التشكيك بالإنجليزية
    query maybe("will_rain", "tomorrow").      # نعم
    query likely("will_rain", "tomorrow").     # نعم
    query unlikely("will_snow", "tomorrow").   # نعم
}
```

---

### 14.4 الحالات المتعددة

عندما يكون لديك متغيران A و B، هناك 4 حالات ممكنة:
1. A و B معاً
2. A بدون B
3. B بدون A
4. لا A ولا B

#### مثال: الحديقة

```bayan
hybrid {
    # الحقائق
    prob("is_green", "garden", 0.7).
    prob("has_trees", "garden", 0.6).

    # الحالة 1: خضراء وفيها أشجار
    state_green_with_trees("garden", ?prob) :-
        prob("is_green", "garden", ?p1),
        prob("has_trees", "garden", ?p2),
        ?prob is ?p1 * ?p2.  # 0.7 × 0.6 = 0.42 (42%)

    # الحالة 2: خضراء بلا أشجار
    state_green_no_trees("garden", ?prob) :-
        prob("is_green", "garden", ?p1),
        prob("has_trees", "garden", ?p2),
        ?not_p2 is 1 - ?p2,  # 1 - 0.6 = 0.4
        ?prob is ?p1 * ?not_p2.  # 0.7 × 0.4 = 0.28 (28%)

    # الحالة 3: غير خضراء مع أشجار
    state_not_green_with_trees("garden", ?prob) :-
        prob("is_green", "garden", ?p1),
        prob("has_trees", "garden", ?p2),
        ?not_p1 is 1 - ?p1,  # 1 - 0.7 = 0.3
        ?prob is ?not_p1 * ?p2.  # 0.3 × 0.6 = 0.18 (18%)

    # الحالة 4: غير خضراء بلا أشجار
    state_not_green_no_trees("garden", ?prob) :-
        prob("is_green", "garden", ?p1),
        prob("has_trees", "garden", ?p2),
        ?not_p1 is 1 - ?p1,
        ?not_p2 is 1 - ?p2,
        ?prob is ?not_p1 * ?not_p2.  # 0.3 × 0.4 = 0.12 (12%)

    # الاستعلامات
    print("جميع الحالات الممكنة:")
    query state_green_with_trees("garden", ?p1).      # 42%
    query state_green_no_trees("garden", ?p2).        # 28%
    query state_not_green_with_trees("garden", ?p3).  # 18%
    query state_not_green_no_trees("garden", ?p4).    # 12%

    # المجموع = 42% + 28% + 18% + 12% = 100% ✅
}
```

---

### 14.5 الاستدلال الشرطي

الاستدلال الشرطي يعتمد على شروط:
```
إذا كان الشرط صحيح → النتيجة X باحتمال P1
إذا كان الشرط خاطئ → النتيجة Y باحتمال P2
```

#### مثال: المركب الكيميائي

```bayan
hybrid {
    # الحقائق
    prob("compound_exists", "compound_A", 0.9).
    prob("has_element_X", "compound_A", 0.85).
    prob("has_element_Y", "compound_A", 0.75).
    prob("factor_present", "factor_Z", 0.6).

    # القاعدة 1: المركب يؤثر إذا توفر العامل
    compound_affects_if_factor("compound_A", ?prob) :-
        prob("compound_exists", "compound_A", ?p1),
        prob("factor_present", "factor_Z", ?p2),
        ?p1 > 0.8,  # المركب موجود بنسبة عالية
        ?p2 > 0.5,  # العامل متوفر
        ?prob is 0.9.  # احتمال التأثير 90%

    # القاعدة 2: المركب لا يؤثر إذا لم يتوفر العامل
    compound_no_affect_if_no_factor("compound_A", ?prob) :-
        prob("compound_exists", "compound_A", ?p1),
        prob("factor_present", "factor_Z", ?p2),
        ?p1 > 0.8,  # المركب موجود بنسبة عالية
        ?p2 < 0.5,  # العامل غير متوفر
        ?prob is 0.2.  # احتمال التأثير 20% فقط

    # الاستعلام
    print("هل المركب يؤثر؟")
    query compound_affects_if_factor("compound_A", ?prob).
    # النتيجة: نعم، باحتمال 90% (لأن العامل Z متوفر بنسبة 60%)
}
```

---

### 14.6 العمليات الاحتمالية

#### 1. عملية AND (الاحتمال المشترك):
```
P(A ∧ B) = P(A) × P(B)
```

```bayan
hybrid {
    prob("event_A", "scenario", 0.7).
    prob("event_B", "scenario", 0.6).

    # احتمال حدوث A و B معاً
    both_events(?prob) :-
        prob("event_A", "scenario", ?pA),
        prob("event_B", "scenario", ?pB),
        ?prob is ?pA * ?pB.  # 0.7 × 0.6 = 0.42
}
```

#### 2. عملية NOT (النفي):
```
P(¬A) = 1 - P(A)
```

```bayan
hybrid {
    prob("event_happens", "scenario", 0.7).

    # احتمال عدم حدوث الحدث
    event_not_happens(?prob) :-
        prob("event_happens", "scenario", ?p),
        ?prob is 1 - ?p.  # 1 - 0.7 = 0.3
}
```

---

### 14.7 أمثلة عملية

#### مثال 1: التشخيص الطبي

```bayan
hybrid {
    # أعراض المريض
    prob("has_fever", "patient", 0.9).
    prob("has_cough", "patient", 0.7).
    prob("has_headache", "patient", 0.5).

    # التشخيص
    prob("has_flu", "patient", 0.8).
    prob("has_cold", "patient", 0.6).

    # الاستعلامات
    print("هل من المحتمل أن المريض مصاب بالإنفلونزا؟")
    query محتمل("has_flu", "patient").  # نعم (80% > 70%)

    print("هل من المؤكد أن المريض لديه حمى؟")
    query مؤكد("has_fever", "patient").  # لا (90% < 95%)
}
```

#### مثال 2: التنبؤ بالمبيعات

```bayan
hybrid {
    # عوامل السوق
    prob("economy_good", "market", 0.7).
    prob("competition_low", "market", 0.5).
    prob("product_quality_high", "product", 0.8).

    # التنبؤ بالمبيعات
    sales_high(?prob) :-
        prob("economy_good", "market", ?p1),
        prob("competition_low", "market", ?p2),
        prob("product_quality_high", "product", ?p3),
        ?p1 > 0.6,
        ?p3 > 0.7,
        ?prob is ?p1 * ?p2 * ?p3.

    query sales_high(?p).
    # النتيجة: 0.7 × 0.5 × 0.8 = 0.28 (28%)
}
```

---

### 14.8 التطبيقات

الاستدلال الاحتمالي مثالي لـ:

1. **الذكاء الاصطناعي:**
   - أنظمة الخبراء الاحتمالية
   - التعلم الآلي البايزي
   - معالجة اللغة الطبيعية مع عدم اليقين

2. **الطب:**
   - التشخيص الطبي
   - تقييم المخاطر الصحية
   - التنبؤ بنتائج العلاج

3. **الأعمال:**
   - التنبؤ بالمبيعات
   - تقييم المخاطر المالية
   - اتخاذ القرارات الاستراتيجية

4. **العلوم:**
   - النمذجة الإحصائية
   - التجارب العلمية
   - تحليل البيانات

---

### 14.9 ملاحظات مهمة

#### 1. الاستقلالية
العمليات الاحتمالية تفترض استقلالية الأحداث:
```
P(A ∧ B) = P(A) × P(B)  # صحيح فقط إذا كانت A و B مستقلتين
```

#### 2. الدقة
الاحتمالات يجب أن تكون بين 0.0 و 1.0:
```bayan
prob("event", "entity", 0.5).   # ✅ صحيح
prob("event", "entity", 1.5).   # ❌ خطأ
prob("event", "entity", -0.2).  # ❌ خطأ
```

#### 3. الشفافية
كل احتمال قابل للتتبع والتفسير - هذه ميزة فريدة مقارنة بالنماذج الإحصائية الأخرى!

---

<a id="causal-networks"></a>

---

## 15. محرك الشبكات السببية (جديد! 🎯)

### 15.1 مقدمة

**محرك الشبكات السببية** هو نظام متقدم مدمج في **نواة لغة البيان** يتيح لك:
- بناء شبكات سببية في أي مجال (علمي، اجتماعي، نفسي، فلسفي، إلخ)
- تعريف 12 نوع من العلاقات السببية
- الاستدلال السببي المتقدم
- بناء نظريات ديناميكية

**الميزة الفريدة:** المحرك جزء من اللغة نفسها - أي مبرمج يمكنه استخدامه!

---

### 15.2 المفاهيم الأساسية

#### العقدة (Node)
وحدة أساسية تمثل مفهوم، كيان، حالة، قانون، إلخ.

```bayan
hybrid {
    # إضافة عقدة
    add_node(network_id, node_id, node_type, properties)
}
```

#### العلاقة السببية (Causal Relation)
علاقة بين عقدتين توضح كيف تؤثر إحداهما على الأخرى.

```bayan
hybrid {
    # إضافة علاقة سببية
    add_causal_relation(network_id, from_node, to_node, relation_type, strength)
}
```

#### الشبكة (Network)
مجموعة من العقد والعلاقات في مجال محدد.

```bayan
hybrid {
    # إنشاء شبكة
    create_network(network_id, network_name, domain)
}
```

---

### 15.3 أنواع العلاقات السببية (12 نوع)

| النوع | المعنى | القوة النموذجية |
|-------|--------|------------------|
| `causes` | A يسبب B | 0.9-1.0 |
| `enables` | A يمكّن B | 0.8-0.95 |
| `prevents` | A يمنع B | 0.8-0.95 |
| `requires` | A يتطلب B | 0.8-0.95 |
| `leads_to` | A يؤدي إلى B | 0.7-0.9 |
| `results_from` | A ينتج عن B | 0.7-0.9 |
| `enhances` | A يعزز B | 0.7-0.9 |
| `weakens` | A يضعف B | 0.7-0.9 |
| `correlates_with` | A يتزامن مع B | 0.6-0.9 |
| `contradicts` | A يتناقض مع B | 0.9-1.0 |
| `complements` | A يكمل B | 0.5-0.8 |
| `depends_on` | A يعتمد على B | 0.8-1.0 |

---

### 15.4 مثال بسيط: شبكة مهنية

```bayan
hybrid {
    # إنشاء شبكة
    create_network("prof_net", "شبكة المهن", "professional")

    # إضافة عقد
    add_node("prof_net", "نجار", "profession", "مهنة")
    add_node("prof_net", "خشب", "material", "مادة")
    add_node("prof_net", "منشار", "tool", "أداة")
    add_node("prof_net", "طاولة", "product", "منتج")
    add_node("prof_net", "طعام", "object", "شيء")

    # إضافة علاقات سببية
    add_causal_relation("prof_net", "نجار", "خشب", "requires", "0.9")
    add_causal_relation("prof_net", "نجار", "منشار", "requires", "0.9")
    add_causal_relation("prof_net", "خشب", "طاولة", "enables", "0.9")
    add_causal_relation("prof_net", "منشار", "طاولة", "enables", "0.8")
    add_causal_relation("prof_net", "طاولة", "طعام", "enables", "0.7")

    # استدلال سببي: ما العلاقة بين النجار والطعام؟
    infer_causal_chain("prof_net", "نجار", "طعام", "5")
    # النتيجة: نجار → خشب → طاولة → طعام
}
```

---

### 15.5 مثال متقدم: شبكة علمية (الفيزياء)

```bayan
hybrid {
    # إنشاء شبكة علمية
    create_network("physics_net", "قوانين نيوتن", "scientific")

    # إضافة مفاهيم فيزيائية
    add_node("physics_net", "قوة", "concept", "مفهوم فيزيائي")
    add_node("physics_net", "كتلة", "property", "خاصية")
    add_node("physics_net", "تسارع", "concept", "مفهوم فيزيائي")
    add_node("physics_net", "سرعة", "state", "حالة")
    add_node("physics_net", "حركة", "state", "حالة")
    add_node("physics_net", "طاقة_حركية", "concept", "مفهوم فيزيائي")

    # قوانين نيوتن
    add_causal_relation("physics_net", "قوة", "تسارع", "causes", "0.95")
    add_causal_relation("physics_net", "كتلة", "تسارع", "affects", "0.9")
    add_causal_relation("physics_net", "تسارع", "سرعة", "leads_to", "0.9")
    add_causal_relation("physics_net", "سرعة", "حركة", "causes", "0.95")
    add_causal_relation("physics_net", "حركة", "طاقة_حركية", "results_in", "0.9")

    # استدلال: كيف تؤدي القوة إلى الطاقة الحركية؟
    infer_causal_chain("physics_net", "قوة", "طاقة_حركية", "5")
    # النتيجة: قوة → تسارع → سرعة → حركة → طاقة_حركية

    # إيجاد جميع تأثيرات القوة
    find_all_effects("physics_net", "قوة", "3")
    # النتيجة: تسارع، سرعة، حركة، طاقة_حركية
}
```

---

### 15.6 مثال: شبكة نفسية

```bayan
hybrid {
    # إنشاء شبكة نفسية
    create_network("psych_net", "الحالات النفسية", "psychological")

    # إضافة حالات نفسية
    add_node("psych_net", "ضغط_نفسي", "state", "حالة نفسية")
    add_node("psych_net", "قلق", "emotion", "عاطفة")
    add_node("psych_net", "أرق", "state", "حالة")
    add_node("psych_net", "تعب", "state", "حالة")
    add_node("psych_net", "استرخاء", "state", "حالة")
    add_node("psych_net", "راحة", "state", "حالة")
    add_node("psych_net", "سعادة", "emotion", "عاطفة")

    # علاقات سببية سلبية
    add_causal_relation("psych_net", "ضغط_نفسي", "قلق", "causes", "0.9")
    add_causal_relation("psych_net", "قلق", "أرق", "leads_to", "0.8")
    add_causal_relation("psych_net", "أرق", "تعب", "causes", "0.95")

    # علاقات سببية إيجابية
    add_causal_relation("psych_net", "استرخاء", "راحة", "leads_to", "0.9")
    add_causal_relation("psych_net", "راحة", "سعادة", "enhances", "0.8")

    # علاقات عكسية
    add_causal_relation("psych_net", "استرخاء", "قلق", "weakens", "0.85")

    # استعلام: كيف أتخلص من القلق؟
    # نبحث عن ما يضعف القلق
    results = query causal_relation(?From, "قلق", "weakens", ?Strength)?

    for result in results: {
        solution = result["?From"]
        print("الحل: " + solution)  # استرخاء
    }
}
```

---

### 15.7 المجالات المدعومة

المحرك يدعم 7 مجالات رئيسية:

1. **`professional`** - المهن والحياة اليومية
2. **`social`** - العلاقات الاجتماعية
3. **`psychological`** - الحالات النفسية
4. **`scientific`** - القوانين العلمية
5. **`philosophical`** - النظريات الفلسفية
6. **`historical`** - الأحداث التاريخية
7. **`custom`** - أي مجال مخصص

---

### 15.8 الأوامر المتقدمة

#### 1. دمج شبكتين
```bayan
hybrid {
    merge_networks("network1", "network2", "merged_network")
}
```

#### 2. استخراج شبكة فرعية
```bayan
hybrid {
    nodes = ["node1", "node2", "node3"]
    extract_subnetwork("main_network", nodes, "sub_network")
}
```

#### 3. تحليل الشبكة
```bayan
hybrid {
    analyze_network("my_network")
    # يعرض: عدد العقد، عدد العلاقات، العقد الأكثر ارتباطاً، إلخ
}
```

#### 4. التنبؤ بالنتيجة
```bayan
hybrid {
    initial_state = ["condition1", "condition2"]
    actions = ["action1", "action2"]
    predict_outcome("my_network", initial_state, actions)
}
```

---

### 15.9 التطبيقات العملية

#### 1. الذكاء الاصطناعي
- بناء أنظمة خبيرة سببية
- الاستدلال المنطقي المتقدم
- التعلم من الأمثلة

#### 2. العلوم
- نمذجة القوانين الفيزيائية
- تحليل التفاعلات الكيميائية
- دراسة الأنظمة البيولوجية

#### 3. الطب
- التشخيص الطبي
- تحليل الأعراض والأمراض
- التنبؤ بنتائج العلاج

#### 4. الأعمال
- تحليل العلاقات السببية في السوق
- التنبؤ بالمبيعات
- تقييم المخاطر

#### 5. الفلسفة
- بناء نظريات فلسفية
- تحليل الحجج المنطقية
- دراسة العلاقات المفاهيمية

---

### 15.10 مثال كامل: نظام توصيات ذكي

```bayan
hybrid {
    # إنشاء شبكة اجتماعية
    create_network("social_net", "العلاقات الاجتماعية", "social")

    # بناء الشبكة
    add_node("social_net", "صدق", "behavior", "سلوك")
    add_node("social_net", "ثقة", "emotion", "عاطفة")
    add_node("social_net", "احترام", "emotion", "عاطفة")
    add_node("social_net", "تعاون", "behavior", "سلوك")
    add_node("social_net", "نجاح_مشترك", "state", "حالة")

    add_causal_relation("social_net", "صدق", "ثقة", "causes", "0.9")
    add_causal_relation("social_net", "ثقة", "احترام", "leads_to", "0.85")
    add_causal_relation("social_net", "احترام", "تعاون", "enables", "0.8")
    add_causal_relation("social_net", "تعاون", "نجاح_مشترك", "leads_to", "0.9")

    # دالة للحصول على توصيات
    def get_relationship_advice(goal): {
        print("=== كيف أصل إلى: " + goal + "؟ ===")

        # إيجاد جميع الأسباب
        causes = find_all_causes("social_net", goal, "4")

        print("الخطوات المقترحة:")
        for cause in causes: {
            print("  - " + cause)
        }

        # إيجاد المسار السببي
        infer_causal_chain("social_net", "صدق", goal, "5")
    }

    # استخدام النظام
    get_relationship_advice("نجاح_مشترك")
    # النتيجة: ابدأ بالصدق → ثقة → احترام → تعاون → نجاح مشترك
}
```

---

## 🌟 الخلاصة النهائية

**لغة البيان** هي اللغة الوحيدة في العالم التي تجمع:
- ✅ البرمجة الإجرائية
- ✅ البرمجة الكائنية
- ✅ البرمجة المنطقية
- ✅ **الاستدلال الاحتمالي والتشكيك** (جديد! 🎲)
- ✅ **محرك الشبكات السببية** (جديد! 🎯)

في لغة واحدة مع دعم كامل للعربية والإنجليزية!

**بالتوفيق في رحلتك البرمجية مع لغة البيان! 🎉🚀**

</div>

