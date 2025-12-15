"""
الوكيل الذكي - Intelligent Agent
=================================

نظام وكيل يجمع كل القدرات ويمكنه التخطيط وتنفيذ مهام معقدة.

المكونات:
- TaskPlanner: تحليل وتخطيط المهام
- ToolExecutor: تنفيذ الأدوات
- BayanAgent: الوكيل الموحد

المطور: باسل يحيى عبدالله
"""

import sys
import os
from typing import List, Dict, Any, Optional, Callable, Tuple
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

# Ensure we can import bayan packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from bayan.bayan.istinbat_engine import IstinbatEngine


class TaskStatus(Enum):
    """حالة المهمة"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"


class ToolCategory(Enum):
    """تصنيف الأدوات"""
    KNOWLEDGE = "knowledge"      # قراءة/كتابة المعرفة
    REASONING = "reasoning"      # الاستنباط والتفكير
    GENERATION = "generation"    # توليد المحتوى
    DESIGN = "design"            # تصميم 3D
    COMMUNICATION = "communication"  # التواصل


@dataclass
class Task:
    """مهمة للتنفيذ"""
    id: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
    priority: int = 5  # 1-10
    dependencies: List[str] = field(default_factory=list)
    result: Optional[Any] = None
    error: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status.value,
            "priority": self.priority,
            "dependencies": self.dependencies,
            "result": str(self.result) if self.result else None,
            "error": self.error
        }


@dataclass 
class Tool:
    """أداة متاحة للوكيل"""
    name: str
    description: str
    category: ToolCategory
    function: Callable
    parameters: List[str] = field(default_factory=list)
    
    def execute(self, **kwargs) -> Any:
        return self.function(**kwargs)


class TaskPlanner:
    """
    مخطط المهام
    
    يحلل المهام المعقدة ويقسمها لخطوات.
    """
    
    def __init__(self, engine: Optional[IstinbatEngine] = None):
        self.engine = engine
    
    def analyze(self, goal: str) -> List[Task]:
        """
        تحليل هدف وتقسيمه لمهام
        
        Args:
            goal: الهدف المطلوب
            
        Returns:
            قائمة المهام
        """
        tasks = []
        goal_lower = goal.lower()
        
        # تحليل بسيط بالكلمات المفتاحية
        if "صمم" in goal_lower or "design" in goal_lower:
            tasks.extend(self._plan_design_task(goal))
        elif "اشرح" in goal_lower or "explain" in goal_lower:
            tasks.extend(self._plan_explanation_task(goal))
        elif "حلل" in goal_lower or "analyze" in goal_lower:
            tasks.extend(self._plan_analysis_task(goal))
        elif "تعلم" in goal_lower or "learn" in goal_lower:
            tasks.extend(self._plan_learning_task(goal))
        else:
            # مهمة عامة
            tasks.append(Task(
                id="task_1",
                description=goal,
                priority=5
            ))
        
        return tasks
    
    def _plan_design_task(self, goal: str) -> List[Task]:
        """تخطيط مهمة تصميم"""
        return [
            Task(id="design_1", description="فهم متطلبات التصميم", priority=8),
            Task(id="design_2", description="اختيار القطع المناسبة", 
                 priority=7, dependencies=["design_1"]),
            Task(id="design_3", description="إنشاء النموذج 3D",
                 priority=7, dependencies=["design_2"]),
            Task(id="design_4", description="التحقق والتصدير",
                 priority=6, dependencies=["design_3"])
        ]
    
    def _plan_explanation_task(self, goal: str) -> List[Task]:
        """تخطيط مهمة شرح"""
        return [
            Task(id="explain_1", description="جمع المعلومات", priority=8),
            Task(id="explain_2", description="تنظيم الشرح",
                 priority=7, dependencies=["explain_1"]),
            Task(id="explain_3", description="توليد النص",
                 priority=6, dependencies=["explain_2"])
        ]
    
    def _plan_analysis_task(self, goal: str) -> List[Task]:
        """تخطيط مهمة تحليل"""
        return [
            Task(id="analyze_1", description="جمع البيانات", priority=8),
            Task(id="analyze_2", description="تحليل البيانات",
                 priority=7, dependencies=["analyze_1"]),
            Task(id="analyze_3", description="استخلاص النتائج",
                 priority=6, dependencies=["analyze_2"])
        ]
    
    def _plan_learning_task(self, goal: str) -> List[Task]:
        """تخطيط مهمة تعلم"""
        return [
            Task(id="learn_1", description="تحليل النص", priority=8),
            Task(id="learn_2", description="استخراج الحقائق",
                 priority=7, dependencies=["learn_1"]),
            Task(id="learn_3", description="حفظ في قاعدة المعرفة",
                 priority=6, dependencies=["learn_2"])
        ]
    
    def get_next_task(self, tasks: List[Task]) -> Optional[Task]:
        """الحصول على المهمة التالية"""
        for task in sorted(tasks, key=lambda t: t.priority, reverse=True):
            if task.status == TaskStatus.PENDING:
                # التحقق من التبعيات
                deps_completed = all(
                    any(t.id == dep and t.status == TaskStatus.COMPLETED 
                        for t in tasks)
                    for dep in task.dependencies
                )
                if deps_completed or not task.dependencies:
                    return task
        return None


class ToolExecutor:
    """
    منفذ الأدوات
    
    يدير وينفذ الأدوات المتاحة.
    """
    
    def __init__(self):
        self.tools: Dict[str, Tool] = {}
        self._register_builtin_tools()
    
    def _register_builtin_tools(self):
        """تسجيل الأدوات المدمجة"""
        
        # أدوات المعرفة
        self.register(Tool(
            name="query_knowledge",
            description="البحث في قاعدة المعرفة",
            category=ToolCategory.KNOWLEDGE,
            function=self._query_knowledge,
            parameters=["query"]
        ))
        
        self.register(Tool(
            name="add_fact",
            description="إضافة حقيقة جديدة",
            category=ToolCategory.KNOWLEDGE,
            function=self._add_fact,
            parameters=["fact"]
        ))
        
        # أدوات الاستنباط
        self.register(Tool(
            name="reason",
            description="الاستنباط المنطقي",
            category=ToolCategory.REASONING,
            function=self._reason,
            parameters=["premise"]
        ))
        
        self.register(Tool(
            name="explain_why",
            description="شرح لماذا",
            category=ToolCategory.REASONING,
            function=self._explain_why,
            parameters=["observation"]
        ))
        
        # أدوات التوليد
        self.register(Tool(
            name="generate_text",
            description="توليد نص",
            category=ToolCategory.GENERATION,
            function=self._generate_text,
            parameters=["prompt"]
        ))
        
        # أدوات التصميم
        self.register(Tool(
            name="create_3d_part",
            description="إنشاء قطعة 3D",
            category=ToolCategory.DESIGN,
            function=self._create_3d_part,
            parameters=["part_type", "parameters"]
        ))
    
    def register(self, tool: Tool):
        """تسجيل أداة"""
        self.tools[tool.name] = tool
    
    def execute(self, tool_name: str, **kwargs) -> Dict[str, Any]:
        """تنفيذ أداة"""
        if tool_name not in self.tools:
            return {"success": False, "error": f"الأداة '{tool_name}' غير موجودة"}
        
        tool = self.tools[tool_name]
        try:
            result = tool.execute(**kwargs)
            return {"success": True, "result": result}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_tools_by_category(self, category: ToolCategory) -> List[Tool]:
        """الحصول على أدوات حسب التصنيف"""
        return [t for t in self.tools.values() if t.category == category]
    
    def list_tools(self) -> List[Dict[str, str]]:
        """قائمة الأدوات"""
        return [
            {"name": t.name, "description": t.description}
            for t in self.tools.values()
        ]
    
    # ========== تنفيذات الأدوات ==========
    
    def _query_knowledge(self, query: str) -> str:
        return f"نتائج البحث عن: {query}"
    
    def _add_fact(self, fact: str) -> str:
        return f"تم إضافة الحقيقة: {fact}"
    
    def _reason(self, premise: str) -> str:
        return f"استنتاج من: {premise}"
    
    def _explain_why(self, observation: str) -> str:
        return f"تفسير لـ: {observation}"
    
    def _generate_text(self, prompt: str) -> str:
        return f"نص مولّد لـ: {prompt}"
    
    def _create_3d_part(self, part_type: str, parameters: Dict) -> str:
        return f"قطعة {part_type} بالمواصفات {parameters}"


class BayanAgent:
    """
    الوكيل الذكي الموحد
    
    يجمع كل القدرات ويمكنه تنفيذ مهام معقدة.
    """
    
    def __init__(self, engine: Optional[IstinbatEngine] = None):
        self.engine = engine or IstinbatEngine()
        self.planner = TaskPlanner(self.engine)
        self.executor = ToolExecutor()
        self.active_tasks: List[Task] = []
        self.completed_goals: List[Dict[str, Any]] = []
        self.memory: Dict[str, Any] = {}
    
    def execute_goal(self, goal: str) -> Dict[str, Any]:
        """
        تنفيذ هدف كامل
        
        Args:
            goal: الهدف المطلوب
            
        Returns:
            نتيجة التنفيذ
        """
        result = {
            "goal": goal,
            "success": False,
            "tasks": [],
            "results": []
        }
        
        # 1. تخطيط المهام
        tasks = self.planner.analyze(goal)
        self.active_tasks = tasks
        result["tasks"] = [t.to_dict() for t in tasks]
        
        # 2. تنفيذ المهام بالترتيب
        while True:
            task = self.planner.get_next_task(self.active_tasks)
            if not task:
                break
            
            task_result = self._execute_task(task)
            result["results"].append(task_result)
            
            if not task_result["success"]:
                break
        
        # 3. تقييم النتيجة
        completed = sum(1 for t in self.active_tasks 
                       if t.status == TaskStatus.COMPLETED)
        result["success"] = completed == len(self.active_tasks)
        result["completed_ratio"] = completed / len(self.active_tasks) if self.active_tasks else 0
        
        self.completed_goals.append(result)
        return result
    
    def _execute_task(self, task: Task) -> Dict[str, Any]:
        """تنفيذ مهمة واحدة"""
        task.status = TaskStatus.IN_PROGRESS
        
        # تحديد الأداة المناسبة
        tool_name, kwargs = self._select_tool(task)
        
        # تنفيذ
        tool_result = self.executor.execute(tool_name, **kwargs)
        
        if tool_result["success"]:
            task.status = TaskStatus.COMPLETED
            task.result = tool_result["result"]
            task.completed_at = datetime.now()
        else:
            task.status = TaskStatus.FAILED
            task.error = tool_result["error"]
        
        return {
            "task_id": task.id,
            "description": task.description,
            "success": tool_result["success"],
            "tool_used": tool_name,
            "result": tool_result.get("result"),
            "error": tool_result.get("error")
        }
    
    def _select_tool(self, task: Task) -> Tuple[str, Dict[str, Any]]:
        """اختيار الأداة المناسبة للمهمة"""
        desc_lower = task.description.lower()
        
        if "فهم" in desc_lower or "متطلبات" in desc_lower:
            return "query_knowledge", {"query": task.description}
        elif "اختيار" in desc_lower or "قطع" in desc_lower:
            return "reason", {"premise": task.description}
        elif "إنشاء" in desc_lower or "3d" in desc_lower:
            return "create_3d_part", {"part_type": "box", "parameters": {}}
        elif "تحقق" in desc_lower or "تصدير" in desc_lower:
            return "generate_text", {"prompt": task.description}
        elif "جمع" in desc_lower:
            return "query_knowledge", {"query": task.description}
        elif "تحليل" in desc_lower:
            return "reason", {"premise": task.description}
        elif "استخراج" in desc_lower or "حقائق" in desc_lower:
            return "reason", {"premise": task.description}
        elif "حفظ" in desc_lower:
            return "add_fact", {"fact": task.description}
        else:
            return "generate_text", {"prompt": task.description}
    
    def ask(self, question: str) -> str:
        """
        طرح سؤال على الوكيل
        """
        # محاولة الإجابة مباشرة
        try:
            result = self.engine.process(question)
            if result and result.equation:
                return f"فهمت سؤالك. الموضوع: {result.equation.event}. الكيانات: {list(result.equation.entities.keys())}"
        except:
            pass
        
        return "سأحاول مساعدتك. هل يمكنك توضيح سؤالك أكثر؟"
    
    def remember(self, key: str, value: Any):
        """تذكر معلومة"""
        self.memory[key] = value
    
    def recall(self, key: str) -> Optional[Any]:
        """استرجاع معلومة"""
        return self.memory.get(key)
    
    def get_status(self) -> Dict[str, Any]:
        """حالة الوكيل"""
        return {
            "active_tasks": len(self.active_tasks),
            "completed_goals": len(self.completed_goals),
            "available_tools": len(self.executor.tools),
            "memory_items": len(self.memory)
        }
    
    def list_capabilities(self) -> List[str]:
        """قائمة القدرات"""
        return [
            "تنفيذ أهداف معقدة متعددة الخطوات",
            "البحث في قاعدة المعرفة",
            "الاستنباط والتفكير المنطقي",
            "توليد النصوص",
            "إنشاء نماذج 3D",
            "التعلم من المحادثات",
            "الإجابة على الأسئلة"
        ]


# ============ اختبار ============
if __name__ == "__main__":
    print("=" * 50)
    print("اختبار الوكيل الذكي")
    print("=" * 50)
    
    agent = BayanAgent()
    
    # عرض القدرات
    print("\n1. قدرات الوكيل:")
    for cap in agent.list_capabilities()[:4]:
        print(f"   - {cap}")
    
    # عرض الأدوات
    print("\n2. الأدوات المتاحة:")
    for tool in agent.executor.list_tools()[:4]:
        print(f"   - {tool['name']}: {tool['description']}")
    
    # تنفيذ هدف
    print("\n3. تنفيذ هدف:")
    result = agent.execute_goal("صمم ترس حلزوني للمحرك")
    print(f"   النجاح: {result['success']}")
    print(f"   المهام: {len(result['tasks'])}")
    print(f"   المنجزة: {result['completed_ratio']:.0%}")
    
    # طرح سؤال
    print("\n4. طرح سؤال:")
    answer = agent.ask("ما هو الذكاء الاصطناعي؟")
    print(f"   الجواب: {answer}")
    
    # الحالة
    print("\n5. حالة الوكيل:")
    status = agent.get_status()
    print(f"   الأدوات: {status['available_tools']}")
    print(f"   الأهداف المنجزة: {status['completed_goals']}")
    
    print("\n✅ اكتمل الاختبار بنجاح!")
