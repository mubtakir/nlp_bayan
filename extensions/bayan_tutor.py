"""
🎓 نظام بيان التعليمي التفاعلي
Bayan Interactive Learning System

نظام تعليمي لتعليم:
- المعادلات اللغوية
- تحليل الجمل العربية
- البرمجة بلغة بيان
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from enum import Enum


class LessonLevel(Enum):
    """مستويات الدروس"""
    BEGINNER = "مبتدئ"
    INTERMEDIATE = "متوسط"
    ADVANCED = "متقدم"


@dataclass
class Exercise:
    """تمرين تفاعلي"""
    question: str
    expected: Dict[str, Any]
    hint: str
    explanation: str = ""
    points: int = 10


@dataclass
class Lesson:
    """درس تعليمي"""
    id: str
    title: str
    description: str
    level: LessonLevel
    exercises: List[Exercise] = field(default_factory=list)
    

@dataclass
class StudentProgress:
    """تقدم الطالب"""
    completed_lessons: List[str] = field(default_factory=list)
    total_points: int = 0
    current_lesson: Optional[str] = None
    

class BayanTutor:
    """
    🎓 معلم بيان التفاعلي
    
    نظام تعليمي شامل يقدم دروساً تفاعلية لتعليم:
    - تحليل الجمل العربية
    - المعادلات اللغوية
    - البرمجة المنطقية
    """
    
    def __init__(self):
        self.lessons = self._create_lessons()
        self.progress = StudentProgress()
    
    def _create_lessons(self) -> Dict[str, Lesson]:
        """إنشاء الدروس"""
        return {
            "intro": Lesson(
                id="intro",
                title="🌟 مقدمة في المعادلات اللغوية",
                description="تعلم أساسيات تحليل الجمل العربية",
                level=LessonLevel.BEGINNER,
                exercises=[
                    Exercise(
                        question="حلل الجملة: 'أحمد أكل تفاحة'\nما هو الفاعل؟",
                        expected={"answer": "أحمد"},
                        hint="الفاعل هو من يقوم بالفعل",
                        explanation="أحمد هو الفاعل لأنه من قام بفعل الأكل",
                        points=10
                    ),
                    Exercise(
                        question="في نفس الجملة 'أحمد أكل تفاحة'\nما هو الفعل؟",
                        expected={"answer": "أكل"},
                        hint="الفعل يدل على حدث",
                        explanation="أكل هو الفعل (الحدث) الذي قام به الفاعل",
                        points=10
                    ),
                    Exercise(
                        question="ما هو المفعول به في 'أحمد أكل تفاحة'؟",
                        expected={"answer": "تفاحة"},
                        hint="المفعول به هو ما وقع عليه الفعل",
                        explanation="تفاحة هي المفعول به لأنها ما أُكلت",
                        points=10
                    ),
                ]
            ),
            "equations": Lesson(
                id="equations",
                title="📐 صياغة المعادلات اللغوية",
                description="تعلم كيف تصوغ المعادلة: فاعل + فعل → مفعول به",
                level=LessonLevel.BEGINNER,
                exercises=[
                    Exercise(
                        question="اكتب المعادلة اللغوية للجملة: 'محمد كتب رسالة'",
                        expected={"answer": "محمد + كتب → رسالة"},
                        hint="الصيغة: فاعل + فعل → مفعول به",
                        explanation="المعادلة: محمد (فاعل) + كتب (فعل) → رسالة (مفعول به)",
                        points=15
                    ),
                    Exercise(
                        question="ما نتيجة الفعل 'شرب' على الفاعل؟",
                        expected={"answer": "عطش"},
                        hint="فكر: ماذا يحدث عندما يشرب الإنسان؟",
                        explanation="الشرب يقلل العطش ويزيد الطاقة",
                        points=15
                    ),
                ]
            ),
            "dialects": Lesson(
                id="dialects",
                title="🌍 اللهجات العربية",
                description="تعرف على تحويل اللهجات للفصحى",
                level=LessonLevel.INTERMEDIATE,
                exercises=[
                    Exercise(
                        question="ما معنى 'عايز' بالفصحى؟ (لهجة مصرية)",
                        expected={"answer": "يريد"},
                        hint="فكر: ماذا يعني أن شخصاً 'عايز' شيئاً؟",
                        explanation="عايز = يريد في اللهجة المصرية",
                        points=10
                    ),
                    Exercise(
                        question="ما معنى 'الحين' بالفصحى؟ (لهجة خليجية)",
                        expected={"answer": "الآن"},
                        hint="تستخدم للإشارة للزمن الحاضر",
                        explanation="الحين = الآن في اللهجة الخليجية",
                        points=10
                    ),
                    Exercise(
                        question="ما اللهجة التي تستخدم كلمة 'بدي'؟",
                        expected={"answer": "شامية"},
                        hint="لهجة بلاد الشام (سوريا، لبنان، فلسطين، الأردن)",
                        explanation="بدي = أريد، وهي من اللهجة الشامية",
                        points=15
                    ),
                ]
            ),
        }

    def list_lessons(self) -> List[Dict]:
        """عرض قائمة الدروس"""
        result = []
        for lesson_id, lesson in self.lessons.items():
            completed = lesson_id in self.progress.completed_lessons
            result.append({
                "id": lesson_id,
                "title": lesson.title,
                "level": lesson.level.value,
                "exercises_count": len(lesson.exercises),
                "completed": completed,
                "status": "✅" if completed else "📖"
            })
        return result

    def start_lesson(self, lesson_id: str) -> Optional[Dict]:
        """بدء درس"""
        if lesson_id not in self.lessons:
            return None

        self.progress.current_lesson = lesson_id
        lesson = self.lessons[lesson_id]

        return {
            "id": lesson.id,
            "title": lesson.title,
            "description": lesson.description,
            "level": lesson.level.value,
            "total_exercises": len(lesson.exercises),
        }

    def get_exercise(self, lesson_id: str, exercise_index: int) -> Optional[Dict]:
        """الحصول على تمرين محدد"""
        if lesson_id not in self.lessons:
            return None

        lesson = self.lessons[lesson_id]
        if exercise_index < 0 or exercise_index >= len(lesson.exercises):
            return None

        ex = lesson.exercises[exercise_index]
        return {
            "index": exercise_index + 1,
            "total": len(lesson.exercises),
            "question": ex.question,
            "hint": ex.hint,
            "points": ex.points,
        }

    def check_answer(self, lesson_id: str, exercise_index: int, answer: str) -> Dict:
        """التحقق من إجابة"""
        if lesson_id not in self.lessons:
            return {"correct": False, "message": "الدرس غير موجود"}

        lesson = self.lessons[lesson_id]
        if exercise_index < 0 or exercise_index >= len(lesson.exercises):
            return {"correct": False, "message": "التمرين غير موجود"}

        ex = lesson.exercises[exercise_index]
        expected = ex.expected.get("answer", "").strip()
        user_answer = answer.strip()

        # مقارنة مرنة
        is_correct = (
            user_answer == expected or
            user_answer in expected or
            expected in user_answer
        )

        if is_correct:
            self.progress.total_points += ex.points
            return {
                "correct": True,
                "message": "✅ إجابة صحيحة!",
                "explanation": ex.explanation,
                "points_earned": ex.points,
                "total_points": self.progress.total_points,
            }
        else:
            return {
                "correct": False,
                "message": "❌ إجابة خاطئة",
                "hint": ex.hint,
                "try_again": True,
            }

    def complete_lesson(self, lesson_id: str) -> Dict:
        """إكمال درس"""
        if lesson_id not in self.progress.completed_lessons:
            self.progress.completed_lessons.append(lesson_id)

        return {
            "message": f"🎉 أحسنت! أكملت الدرس",
            "total_points": self.progress.total_points,
            "completed_lessons": len(self.progress.completed_lessons),
            "total_lessons": len(self.lessons),
        }

    def get_progress(self) -> Dict:
        """عرض التقدم"""
        return {
            "total_points": self.progress.total_points,
            "completed_lessons": len(self.progress.completed_lessons),
            "total_lessons": len(self.lessons),
            "percentage": int(len(self.progress.completed_lessons) / len(self.lessons) * 100),
            "current_lesson": self.progress.current_lesson,
        }

    def run_interactive(self, lesson_id: str = "intro"):
        """تشغيل الدرس بشكل تفاعلي في الطرفية"""
        lesson_info = self.start_lesson(lesson_id)
        if not lesson_info:
            print(f"❌ الدرس '{lesson_id}' غير موجود")
            return

        print("\n" + "=" * 50)
        print(f"📚 {lesson_info['title']}")
        print(f"   {lesson_info['description']}")
        print(f"   المستوى: {lesson_info['level']}")
        print("=" * 50 + "\n")

        lesson = self.lessons[lesson_id]
        for i, ex in enumerate(lesson.exercises):
            print(f"\n📝 تمرين {i+1}/{len(lesson.exercises)}")
            print(f"   {ex.question}")
            print(f"   💡 تلميح: {ex.hint}")

            while True:
                answer = input("\n   إجابتك: ").strip()
                result = self.check_answer(lesson_id, i, answer)

                if result["correct"]:
                    print(f"   {result['message']}")
                    print(f"   📖 {result['explanation']}")
                    print(f"   ⭐ النقاط: +{result['points_earned']} (المجموع: {result['total_points']})")
                    break
                else:
                    print(f"   {result['message']}")
                    print(f"   💡 {result['hint']}")
                    retry = input("   حاول مرة أخرى؟ (نعم/لا): ")
                    if retry != "نعم":
                        print(f"   📖 الإجابة الصحيحة: {ex.expected['answer']}")
                        break

        # إكمال الدرس
        completion = self.complete_lesson(lesson_id)
        print("\n" + "=" * 50)
        print(f"🎉 {completion['message']}")
        print(f"⭐ مجموع النقاط: {completion['total_points']}")
        print(f"📊 التقدم: {completion['completed_lessons']}/{completion['total_lessons']} دروس")
        print("=" * 50)


# دالة مساعدة
def start_tutorial(lesson_id: str = "intro"):
    """بدء درس تفاعلي"""
    tutor = BayanTutor()
    tutor.run_interactive(lesson_id)

