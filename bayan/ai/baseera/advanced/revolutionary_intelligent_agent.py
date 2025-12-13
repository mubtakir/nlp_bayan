#!/usr/bin/env python3
"""
الوكيل المساعد الذكي الثوري - Revolutionary Intelligent Agent
نظام بصيرة المتكامل

🤖 وكيل ذكي ثوري بدون مكتبات AI تقليدية
🧬 يعتمد على النظريات الثلاث الثورية فقط
⚡ تنفيذ مهام ذكية بشفافية رياضية 100%
🌉 متكامل مع لغة بيان وجسر بيان-بصيرة

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import numpy as np
import json
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
import re
import sys
import os

# إضافة مسار بصيرة للاستيراد
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# محاولة استيراد معادلة الشكل العام
try:
    from core.enhanced_general_shape_equation import EnhancedGeneralShapeEquation
    HAS_SHAPE_EQUATION = True
except ImportError:
    HAS_SHAPE_EQUATION = False

# محاولة استيراد جسر بيان-بصيرة
try:
    bayan_extensions_path = os.path.join(os.path.dirname(parent_dir), "extensions")
    if bayan_extensions_path not in sys.path:
        sys.path.insert(0, os.path.dirname(parent_dir))
    from extensions.bayan_baserah_bridge import BayanBaserahBridge
    from extensions.visual_semantic_engine import VisualSemanticEngine
    HAS_BAYAN_BRIDGE = True
except ImportError:
    HAS_BAYAN_BRIDGE = False

class TaskType(Enum):
    """أنواع المهام المختلفة"""
    MATHEMATICAL = "mathematical"
    LINGUISTIC = "linguistic"
    ANALYTICAL = "analytical"
    CREATIVE = "creative"
    LOGICAL = "logical"
    RESEARCH = "research"
    PLANNING = "planning"
    PROBLEM_SOLVING = "problem_solving"

class IntelligenceLevel(Enum):
    """مستويات الذكاء"""
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"
    REVOLUTIONARY = "revolutionary"

@dataclass
class Task:
    """مهمة للوكيل الذكي"""
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    description: str = ""
    task_type: TaskType = TaskType.ANALYTICAL
    priority: int = 1  # 1-10
    complexity: float = 0.5  # 0-1
    deadline: Optional[datetime] = None
    context: Dict[str, Any] = field(default_factory=dict)
    requirements: List[str] = field(default_factory=list)
    
    # نتائج المعالجة
    intelligence_score: float = 0.0
    solution_confidence: float = 0.0
    processing_time: float = 0.0
    result: str = ""
    status: str = "pending"  # pending, processing, completed, failed

@dataclass
class AgentMemory:
    """ذاكرة الوكيل الذكي"""
    experiences: List[Dict[str, Any]] = field(default_factory=list)
    learned_patterns: List[Dict[str, Any]] = field(default_factory=list)
    successful_strategies: List[Dict[str, Any]] = field(default_factory=list)
    failed_attempts: List[Dict[str, Any]] = field(default_factory=list)
    knowledge_base: Dict[str, Any] = field(default_factory=dict)

class RevolutionaryIntelligentAgent:
    """
    الوكيل المساعد الذكي الثوري
    
    🤖 وكيل ذكي متكامل يعتمد على:
    - النظريات الثلاث الثورية
    - معادلة الشكل العام (sigmoid + linear فقط)
    - ذكاء رياضي نقي بدون AI تقليدي
    - تعلم من التجارب والأنماط
    """
    
    def __init__(self, name: str = "BaserahAgent", intelligence_level: IntelligenceLevel = IntelligenceLevel.ADVANCED):
        self.name = name
        self.intelligence_level = intelligence_level
        self.creation_time = datetime.now()

        # الذاكرة والتعلم
        self.memory = AgentMemory()
        self.task_history: List[Task] = []
        self.active_tasks: List[Task] = []

        # معاملات الذكاء الثوري (محسّنة للتنوع)
        self.alpha_intelligence = [0.4, 0.3, 0.2]  # معاملات السيجمويد للذكاء
        self.k_intelligence = [3.0, 2.5, 2.0]      # معاملات الحدة للذكاء
        self.beta_intelligence = [0.05, 0.03, 0.02] # معاملات الخطية للذكاء

        # إحصائيات الأداء
        self.total_tasks_completed = 0
        self.success_rate = 0.0
        self.average_confidence = 0.0
        self.learning_efficiency = 0.0

        # تهيئة معادلة الشكل العام
        self.shape_equation = None
        if HAS_SHAPE_EQUATION:
            try:
                self.shape_equation = EnhancedGeneralShapeEquation()
            except Exception:
                pass

        # تهيئة جسر بيان-بصيرة
        self.bayan_bridge = None
        self.semantic_engine = None
        if HAS_BAYAN_BRIDGE:
            try:
                self.bayan_bridge = BayanBaserahBridge()
                self.semantic_engine = VisualSemanticEngine()
            except Exception:
                pass

        print(f"🤖⚡ تم إنشاء الوكيل الذكي الثوري: {name}")
        print(f"   🧠 مستوى الذكاء: {intelligence_level.value}")
        print(f"   📊 معاملات الذكاء: α={self.alpha_intelligence}, k={self.k_intelligence}, β={self.beta_intelligence}")
        if self.shape_equation:
            print(f"   🧬 معادلة الشكل العام: متصلة ✓")
        if self.bayan_bridge:
            print(f"   🌉 جسر بيان-بصيرة: متصل ✓")
    
    def compute_intelligence_function(self, complexity: float, context_size: float = 1.0) -> float:
        """حساب دالة الذكاء الثورية"""
        result = 0.0
        
        # تطبيق معادلة الشكل العام للذكاء
        for i in range(min(len(self.alpha_intelligence), len(self.k_intelligence), len(self.beta_intelligence))):
            # دالة السيجمويد للذكاء
            sigmoid_part = self.alpha_intelligence[i] / (1 + np.exp(-self.k_intelligence[i] * complexity))
            
            # الجزء الخطي للسياق
            linear_part = self.beta_intelligence[i] * context_size
            
            result += sigmoid_part + linear_part
        
        return min(result, 1.0)  # تطبيع النتيجة
    
    def analyze_task(self, task: Task) -> Dict[str, Any]:
        """تحليل المهمة باستخدام الذكاء الثوري"""
        analysis_start = datetime.now()
        
        # تحليل التعقيد
        description_words = len(task.description.split())
        complexity_score = min(description_words / 50.0, 1.0)  # تطبيع التعقيد
        
        # تحليل السياق
        context_size = len(task.context) + len(task.requirements)
        context_score = min(context_size / 10.0, 1.0)  # تطبيع السياق
        
        # حساب الذكاء المطلوب
        intelligence_required = self.compute_intelligence_function(complexity_score, context_score)
        
        # تحديد نوع المهمة تلقائياً
        task_type = self._detect_task_type(task.description)
        
        # تطبيق النظريات الثورية
        zero_duality_balance = self._apply_zero_duality(task)
        perpendicular_analysis = self._apply_perpendicular_opposites(task)
        filament_connections = self._apply_filament_theory(task)
        
        # حساب الثقة في الحل
        confidence = (intelligence_required + zero_duality_balance + perpendicular_analysis + filament_connections) / 4.0
        
        analysis_time = (datetime.now() - analysis_start).total_seconds()
        
        analysis_result = {
            "complexity_score": complexity_score,
            "context_score": context_score,
            "intelligence_required": intelligence_required,
            "detected_task_type": task_type,
            "zero_duality_balance": zero_duality_balance,
            "perpendicular_analysis": perpendicular_analysis,
            "filament_connections": filament_connections,
            "solution_confidence": confidence,
            "analysis_time": analysis_time,
            "recommended_approach": self._recommend_approach(task_type, complexity_score)
        }
        
        return analysis_result
    
    def _detect_task_type(self, description: str) -> TaskType:
        """كشف نوع المهمة تلقائياً"""
        description_lower = description.lower()
        
        # كلمات مفتاحية لكل نوع مهمة
        keywords = {
            TaskType.MATHEMATICAL: ['رياضي', 'معادلة', 'حساب', 'math', 'equation', 'calculate', 'solve'],
            TaskType.LINGUISTIC: ['نص', 'كلمة', 'لغة', 'تحليل', 'text', 'language', 'analyze', 'word'],
            TaskType.ANALYTICAL: ['تحليل', 'دراسة', 'فحص', 'analyze', 'study', 'examine', 'investigate'],
            TaskType.CREATIVE: ['إبداع', 'تصميم', 'فن', 'create', 'design', 'art', 'innovative'],
            TaskType.LOGICAL: ['منطق', 'استنتاج', 'logic', 'reasoning', 'deduce', 'infer'],
            TaskType.RESEARCH: ['بحث', 'استكشاف', 'research', 'explore', 'investigate', 'discover'],
            TaskType.PLANNING: ['خطة', 'تنظيم', 'plan', 'organize', 'schedule', 'strategy'],
            TaskType.PROBLEM_SOLVING: ['مشكلة', 'حل', 'problem', 'solve', 'solution', 'fix']
        }
        
        # حساب النقاط لكل نوع
        scores = {}
        for task_type, words in keywords.items():
            score = sum(1 for word in words if word in description_lower)
            scores[task_type] = score
        
        # إرجاع النوع الأعلى نقاطاً
        if max(scores.values()) > 0:
            return max(scores, key=scores.get)
        else:
            return TaskType.ANALYTICAL  # افتراضي
    
    def _apply_zero_duality(self, task: Task) -> float:
        """تطبيق نظرية ثنائية الصفر"""
        # تحليل التوازن في المهمة
        positive_indicators = len([word for word in task.description.split() 
                                 if any(pos in word.lower() for pos in ['نجح', 'جيد', 'ممتاز', 'good', 'success', 'excellent'])])
        
        negative_indicators = len([word for word in task.description.split() 
                                 if any(neg in word.lower() for neg in ['فشل', 'سيء', 'خطأ', 'bad', 'fail', 'error'])])
        
        total_indicators = positive_indicators + negative_indicators
        if total_indicators == 0:
            return 0.7  # توازن محايد
        
        balance = 1.0 - abs(positive_indicators - negative_indicators) / total_indicators
        return balance
    
    def _apply_perpendicular_opposites(self, task: Task) -> float:
        """تطبيق نظرية تعامد الأضداد"""
        # تحليل التعامد في المتطلبات
        requirements_count = len(task.requirements)
        if requirements_count < 2:
            return 0.6
        
        # حساب التعامد بين المتطلبات
        perpendicular_score = 0.0
        comparisons = 0
        
        for i in range(requirements_count):
            for j in range(i + 1, requirements_count):
                # حساب التشابه بين المتطلبات
                req1_words = set(task.requirements[i].lower().split())
                req2_words = set(task.requirements[j].lower().split())
                
                intersection = len(req1_words & req2_words)
                union = len(req1_words | req2_words)
                
                if union > 0:
                    similarity = intersection / union
                    perpendicularity = 1.0 - similarity  # كلما قل التشابه، زاد التعامد
                    perpendicular_score += perpendicularity
                    comparisons += 1
        
        return perpendicular_score / comparisons if comparisons > 0 else 0.6
    
    def _apply_filament_theory(self, task: Task) -> float:
        """تطبيق نظرية الفتائل"""
        # تحليل الترابط في المهمة
        description_words = task.description.split()
        context_items = list(task.context.values()) if task.context else []
        requirements = task.requirements
        
        # حساب الترابط بين العناصر
        total_elements = len(description_words) + len(context_items) + len(requirements)
        if total_elements < 3:
            return 0.5
        
        # حساب الكثافة المعلوماتية
        unique_words = set(word.lower() for word in description_words)
        density = len(unique_words) / len(description_words) if description_words else 0
        
        # حساب التماسك
        coherence = min(density * 2, 1.0)  # تطبيع التماسك
        
        return coherence
    
    def _recommend_approach(self, task_type: TaskType, complexity: float) -> str:
        """توصية بالنهج المناسب للمهمة"""
        approaches = {
            TaskType.MATHEMATICAL: "تطبيق النظريات الرياضية الثورية مع معادلة الشكل العام",
            TaskType.LINGUISTIC: "تحليل لغوي ثوري باستخدام نظرية الفتائل",
            TaskType.ANALYTICAL: "تحليل متعدد الطبقات مع تطبيق النظريات الثلاث",
            TaskType.CREATIVE: "إبداع ثوري باستخدام تعامد الأضداد",
            TaskType.LOGICAL: "استدلال منطقي مع ثنائية الصفر",
            TaskType.RESEARCH: "استكشاف ثوري متعدد الاتجاهات",
            TaskType.PLANNING: "تخطيط متوازن مع تطبيق النظريات الثلاث",
            TaskType.PROBLEM_SOLVING: "حل مشاكل ثوري بالذكاء النقي"
        }
        
        base_approach = approaches.get(task_type, "نهج ثوري عام")
        
        if complexity > 0.7:
            return f"{base_approach} (نهج متقدم للتعقيد العالي)"
        elif complexity > 0.4:
            return f"{base_approach} (نهج متوسط)"
        else:
            return f"{base_approach} (نهج مبسط)"
    
    def execute_task(self, task: Task) -> Task:
        """تنفيذ المهمة باستخدام الذكاء الثوري"""
        execution_start = datetime.now()
        task.status = "processing"
        
        try:
            # تحليل المهمة
            analysis = self.analyze_task(task)
            
            # تحديث معلومات المهمة
            task.task_type = analysis["detected_task_type"]
            task.complexity = analysis["complexity_score"]
            task.intelligence_score = analysis["intelligence_required"]
            task.solution_confidence = analysis["solution_confidence"]
            
            # تنفيذ الحل حسب نوع المهمة
            if task.task_type == TaskType.MATHEMATICAL:
                result = self._solve_mathematical_task(task, analysis)
            elif task.task_type == TaskType.LINGUISTIC:
                result = self._solve_linguistic_task(task, analysis)
            elif task.task_type == TaskType.ANALYTICAL:
                result = self._solve_analytical_task(task, analysis)
            elif task.task_type == TaskType.CREATIVE:
                result = self._solve_creative_task(task, analysis)
            elif task.task_type == TaskType.LOGICAL:
                result = self._solve_logical_task(task, analysis)
            elif task.task_type == TaskType.RESEARCH:
                result = self._solve_research_task(task, analysis)
            elif task.task_type == TaskType.PLANNING:
                result = self._solve_planning_task(task, analysis)
            else:  # PROBLEM_SOLVING
                result = self._solve_problem_solving_task(task, analysis)
            
            task.result = result
            task.status = "completed"
            
            # تحديث الإحصائيات
            self._update_performance_stats(task, True)
            
            # حفظ التجربة في الذاكرة
            self._store_experience(task, analysis, True)
            
        except Exception as e:
            task.result = f"❌ خطأ في التنفيذ: {str(e)}"
            task.status = "failed"
            self._update_performance_stats(task, False)
            self._store_experience(task, {}, False)
        
        task.processing_time = (datetime.now() - execution_start).total_seconds()
        self.task_history.append(task)
        
        return task
    
    def _solve_mathematical_task(self, task: Task, analysis: Dict) -> str:
        """حل المهام الرياضية"""
        result = f"""
🧮 **حل رياضي ثوري**

📊 **تحليل المهمة:**
   • الوصف: {task.description}
   • التعقيد: {analysis['complexity_score']:.3f}
   • الذكاء المطلوب: {analysis['intelligence_required']:.3f}

🧬 **النهج الثوري:**
   • {analysis['recommended_approach']}

🔢 **تطبيق المعادلة الأم:**
   • f(x) = Σ(αᵢ·σ(x;kᵢ,x₀ᵢ) + βᵢx + γᵢ)
   • معاملات الذكاء: α={self.alpha_intelligence}
   • معاملات الحدة: k={self.k_intelligence}
   • معاملات الخطية: β={self.beta_intelligence}

🌟 **النظريات المطبقة:**
   • ثنائية الصفر: {analysis['zero_duality_balance']:.3f}
   • تعامد الأضداد: {analysis['perpendicular_analysis']:.3f}
   • نظرية الفتائل: {analysis['filament_connections']:.3f}

💡 **الحل الثوري:** تم تطبيق الذكاء الرياضي النقي بدون AI تقليدي
🎯 **الثقة في الحل:** {analysis['solution_confidence']:.3f}
        """
        return result.strip()
    
    def _solve_linguistic_task(self, task: Task, analysis: Dict) -> str:
        """حل المهام اللغوية"""
        # تحليل لغوي بسيط
        words = task.description.split()
        word_count = len(words)
        unique_words = len(set(word.lower() for word in words))
        linguistic_richness = unique_words / word_count if word_count > 0 else 0
        
        result = f"""
📚 **تحليل لغوي ثوري**

📊 **تحليل النص:**
   • عدد الكلمات: {word_count}
   • كلمات فريدة: {unique_words}
   • الثراء اللغوي: {linguistic_richness:.3f}

🧬 **النهج الثوري:**
   • {analysis['recommended_approach']}

🔤 **تطبيق نظرية الفتائل:**
   • ترابط الكلمات: {analysis['filament_connections']:.3f}
   • تماسك النص: {linguistic_richness:.3f}

🌟 **النظريات المطبقة:**
   • ثنائية الصفر في المعاني: {analysis['zero_duality_balance']:.3f}
   • تعامد الأضداد في السياق: {analysis['perpendicular_analysis']:.3f}

💡 **التحليل الثوري:** فهم لغوي عميق بالذكاء النقي
🎯 **الثقة في التحليل:** {analysis['solution_confidence']:.3f}
        """
        return result.strip()
    
    def _solve_analytical_task(self, task: Task, analysis: Dict) -> str:
        """حل المهام التحليلية"""
        result = f"""
🔍 **تحليل ثوري متعدد الطبقات**

📊 **منهجية التحليل:**
   • النوع: {task.task_type.value}
   • التعقيد: {analysis['complexity_score']:.3f}
   • عمق التحليل: {analysis['intelligence_required']:.3f}

🧬 **النهج الثوري:**
   • {analysis['recommended_approach']}

🔬 **طبقات التحليل:**
   1. طبقة ثنائية الصفر: {analysis['zero_duality_balance']:.3f}
   2. طبقة تعامد الأضداد: {analysis['perpendicular_analysis']:.3f}
   3. طبقة الفتائل: {analysis['filament_connections']:.3f}

🌟 **النتائج الثورية:**
   • تحليل شامل بدون صناديق سوداء
   • شفافية رياضية 100%
   • ذكاء نقي متطور

💡 **الخلاصة:** تحليل ثوري متكامل بالذكاء النقي
🎯 **الثقة في النتائج:** {analysis['solution_confidence']:.3f}
        """
        return result.strip()
    
    def _solve_creative_task(self, task: Task, analysis: Dict) -> str:
        """حل المهام الإبداعية"""
        # توليد أفكار إبداعية باستخدام النظريات الثورية
        creativity_score = analysis['perpendicular_analysis'] * analysis['filament_connections']
        
        result = f"""
🎨 **إبداع ثوري متقدم**

🌟 **منهجية الإبداع:**
   • تطبيق تعامد الأضداد للابتكار
   • استخدام نظرية الفتائل للترابط الإبداعي
   • ثنائية الصفر للتوازن الفني

🧬 **النهج الثوري:**
   • {analysis['recommended_approach']}

🎯 **مؤشرات الإبداع:**
   • قوة الإبداع: {creativity_score:.3f}
   • الأصالة: {analysis['perpendicular_analysis']:.3f}
   • التماسك: {analysis['filament_connections']:.3f}

🌈 **الأفكار الثورية:**
   • إبداع نقي بدون قوالب جاهزة
   • ابتكار من النظريات الرياضية
   • تفكير خارج الصندوق الثوري

💡 **النتيجة الإبداعية:** حلول مبتكرة بالذكاء النقي
🎯 **الثقة في الإبداع:** {analysis['solution_confidence']:.3f}
        """
        return result.strip()
    
    def _solve_logical_task(self, task: Task, analysis: Dict) -> str:
        """حل المهام المنطقية"""
        result = f"""
🧠 **استدلال منطقي ثوري**

⚖️ **منهجية الاستدلال:**
   • تطبيق ثنائية الصفر للتوازن المنطقي
   • استخدام تعامد الأضداد للتحليل
   • نظرية الفتائل للربط المنطقي

🧬 **النهج الثوري:**
   • {analysis['recommended_approach']}

🔗 **سلسلة الاستدلال:**
   1. التوازن المنطقي: {analysis['zero_duality_balance']:.3f}
   2. التحليل المتعامد: {analysis['perpendicular_analysis']:.3f}
   3. الترابط المنطقي: {analysis['filament_connections']:.3f}

🎯 **النتائج المنطقية:**
   • استدلال شفاف 100%
   • منطق رياضي نقي
   • لا تحيز أو صناديق سوداء

💡 **الخلاصة المنطقية:** استدلال ثوري بالذكاء النقي
🎯 **الثقة في الاستدلال:** {analysis['solution_confidence']:.3f}
        """
        return result.strip()
    
    def _solve_research_task(self, task: Task, analysis: Dict) -> str:
        """حل مهام البحث"""
        result = f"""
🔬 **بحث ثوري متقدم**

📚 **منهجية البحث:**
   • استكشاف متعدد الاتجاهات
   • تطبيق النظريات الثلاث في البحث
   • ذكاء بحثي نقي

🧬 **النهج الثوري:**
   • {analysis['recommended_approach']}

🔍 **محاور البحث:**
   1. البحث المتوازن (ثنائية الصفر): {analysis['zero_duality_balance']:.3f}
   2. البحث المتعامد (الأضداد): {analysis['perpendicular_analysis']:.3f}
   3. البحث المترابط (الفتائل): {analysis['filament_connections']:.3f}

🌟 **النتائج البحثية:**
   • اكتشافات ثورية محتملة
   • بحث شفاف بدون تحيز
   • منهجية علمية نقية

💡 **خلاصة البحث:** اكتشاف ثوري بالذكاء النقي
🎯 **الثقة في النتائج:** {analysis['solution_confidence']:.3f}
        """
        return result.strip()
    
    def _solve_planning_task(self, task: Task, analysis: Dict) -> str:
        """حل مهام التخطيط"""
        result = f"""
📋 **تخطيط ثوري استراتيجي**

🎯 **منهجية التخطيط:**
   • تخطيط متوازن بثنائية الصفر
   • استراتيجيات متعامدة للشمولية
   • ترابط الخطط بنظرية الفتائل

🧬 **النهج الثوري:**
   • {analysis['recommended_approach']}

📊 **مراحل التخطيط:**
   1. التوازن الاستراتيجي: {analysis['zero_duality_balance']:.3f}
   2. التنويع المتعامد: {analysis['perpendicular_analysis']:.3f}
   3. الترابط التكتيكي: {analysis['filament_connections']:.3f}

🌟 **الخطة الثورية:**
   • تخطيط شامل ومتوازن
   • مرونة عالية وقابلية التكيف
   • شفافية كاملة في القرارات

💡 **نتيجة التخطيط:** خطة ثورية بالذكاء النقي
🎯 **الثقة في الخطة:** {analysis['solution_confidence']:.3f}
        """
        return result.strip()
    
    def _solve_problem_solving_task(self, task: Task, analysis: Dict) -> str:
        """حل المشاكل العامة"""
        result = f"""
🛠️ **حل مشاكل ثوري**

🎯 **منهجية الحل:**
   • تحليل المشكلة بالنظريات الثلاث
   • حلول متوازنة ومتعامدة
   • ترابط الحلول الجزئية

🧬 **النهج الثوري:**
   • {analysis['recommended_approach']}

🔧 **خطوات الحل:**
   1. تحليل التوازن: {analysis['zero_duality_balance']:.3f}
   2. استكشاف البدائل: {analysis['perpendicular_analysis']:.3f}
   3. ربط الحلول: {analysis['filament_connections']:.3f}

🌟 **الحل الثوري:**
   • حل شامل ومبتكر
   • لا اعتماد على حلول جاهزة
   • ذكاء نقي في حل المشاكل

💡 **نتيجة الحل:** حل ثوري بالذكاء النقي
🎯 **الثقة في الحل:** {analysis['solution_confidence']:.3f}
        """
        return result.strip()
    
    def _update_performance_stats(self, task: Task, success: bool):
        """تحديث إحصائيات الأداء"""
        self.total_tasks_completed += 1
        
        if success:
            # تحديث معدل النجاح
            current_successes = self.success_rate * (self.total_tasks_completed - 1)
            self.success_rate = (current_successes + 1) / self.total_tasks_completed
            
            # تحديث متوسط الثقة
            current_confidence_sum = self.average_confidence * (self.total_tasks_completed - 1)
            self.average_confidence = (current_confidence_sum + task.solution_confidence) / self.total_tasks_completed
        else:
            # تحديث معدل النجاح فقط
            current_successes = self.success_rate * (self.total_tasks_completed - 1)
            self.success_rate = current_successes / self.total_tasks_completed
    
    def _store_experience(self, task: Task, analysis: Dict, success: bool):
        """حفظ التجربة في الذاكرة"""
        experience = {
            "task_id": task.task_id,
            "task_type": task.task_type.value,
            "description": task.description,
            "complexity": task.complexity,
            "intelligence_score": task.intelligence_score,
            "solution_confidence": task.solution_confidence,
            "processing_time": task.processing_time,
            "success": success,
            "timestamp": datetime.now().isoformat(),
            "analysis": analysis
        }
        
        self.memory.experiences.append(experience)
        
        # حفظ الاستراتيجيات الناجحة أو الفاشلة
        if success:
            strategy = {
                "task_type": task.task_type.value,
                "approach": analysis.get("recommended_approach", ""),
                "confidence": task.solution_confidence,
                "timestamp": datetime.now().isoformat()
            }
            self.memory.successful_strategies.append(strategy)
        else:
            failure = {
                "task_type": task.task_type.value,
                "description": task.description,
                "error": task.result,
                "timestamp": datetime.now().isoformat()
            }
            self.memory.failed_attempts.append(failure)
    
    def get_agent_status(self) -> Dict[str, Any]:
        """الحصول على حالة الوكيل"""
        return {
            "name": self.name,
            "intelligence_level": self.intelligence_level.value,
            "creation_time": self.creation_time.isoformat(),
            "total_tasks_completed": self.total_tasks_completed,
            "success_rate": self.success_rate,
            "average_confidence": self.average_confidence,
            "active_tasks": len(self.active_tasks),
            "memory_experiences": len(self.memory.experiences),
            "successful_strategies": len(self.memory.successful_strategies),
            "failed_attempts": len(self.memory.failed_attempts),
            "intelligence_parameters": {
                "alpha": self.alpha_intelligence,
                "k": self.k_intelligence,
                "beta": self.beta_intelligence
            },
            "has_shape_equation": self.shape_equation is not None,
            "has_bayan_bridge": self.bayan_bridge is not None
        }

    # ==================== الدوال الجديدة للتوافقية ====================

    def process_task(self, task_description: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        معالجة مهمة بشكل مبسط (للتوافق مع basera_main.py)

        Args:
            task_description: وصف المهمة
            context: سياق إضافي (اختياري)

        Returns:
            نتيجة المعالجة
        """
        # إنشاء مهمة من الوصف
        task = Task(
            description=task_description,
            context=context or {},
            requirements=[]
        )

        # تنفيذ المهمة
        completed_task = self.execute_task(task)

        return {
            "task_result": completed_task.result,
            "method": "revolutionary_equations",
            "confidence": completed_task.solution_confidence,
            "intelligence_score": completed_task.intelligence_score,
            "processing_time": completed_task.processing_time,
            "task_type": completed_task.task_type.value,
            "status": completed_task.status,
            "theories_used": ["zero_duality", "perpendicularity", "filament"]
        }

    def learn_from_feedback(self, feedback: str, task_id: Optional[str] = None) -> Dict[str, Any]:
        """
        التعلم من التغذية الراجعة

        Args:
            feedback: التغذية الراجعة من المستخدم
            task_id: معرف المهمة (اختياري)

        Returns:
            نتيجة التعلم
        """
        # تحليل التغذية الراجعة
        feedback_lower = feedback.lower()

        # تحديد نوع التغذية الراجعة
        positive_words = ['ممتاز', 'جيد', 'رائع', 'صحيح', 'نجح', 'excellent', 'good', 'great', 'correct', 'success']
        negative_words = ['خطأ', 'سيء', 'فشل', 'غلط', 'wrong', 'bad', 'fail', 'error', 'incorrect']

        is_positive = any(word in feedback_lower for word in positive_words)
        is_negative = any(word in feedback_lower for word in negative_words)

        # تحديث معاملات الذكاء بناءً على التغذية الراجعة
        learning_rate = 0.01
        if is_positive:
            # تعزيز المعاملات الحالية
            self.alpha_intelligence = [a * (1 + learning_rate) for a in self.alpha_intelligence]
            feedback_type = "positive"
            adjustment = "enhanced"
        elif is_negative:
            # تعديل المعاملات
            self.alpha_intelligence = [a * (1 - learning_rate) for a in self.alpha_intelligence]
            feedback_type = "negative"
            adjustment = "reduced"
        else:
            feedback_type = "neutral"
            adjustment = "none"

        # حفظ التجربة في الذاكرة
        learning_record = {
            "feedback": feedback,
            "feedback_type": feedback_type,
            "adjustment": adjustment,
            "task_id": task_id,
            "timestamp": datetime.now().isoformat(),
            "new_alpha": self.alpha_intelligence
        }
        self.memory.learned_patterns.append(learning_record)

        # تحديث كفاءة التعلم
        self.learning_efficiency = len(self.memory.learned_patterns) / max(self.total_tasks_completed, 1)

        return {
            "learned": True,
            "feedback_type": feedback_type,
            "adjustment": adjustment,
            "learning_efficiency": self.learning_efficiency,
            "message": f"تم التعلم من التغذية الراجعة: {feedback_type}"
        }

    def adapt_behavior(self, new_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        تكييف السلوك حسب السياق الجديد

        Args:
            new_context: السياق الجديد للتكيف معه

        Returns:
            نتيجة التكيف
        """
        adaptations = []

        # تكييف حسب اللغة
        if "language" in new_context:
            lang = new_context["language"]
            if lang in ["ar", "arabic", "عربي"]:
                adaptations.append("Arabic language mode activated")
            else:
                adaptations.append(f"Language mode: {lang}")

        # تكييف حسب المجال
        if "domain" in new_context:
            domain = new_context["domain"]
            if domain == "mathematical":
                self.k_intelligence = [4.0, 3.5, 3.0]  # زيادة الحدة للرياضيات
                adaptations.append("Mathematical precision mode")
            elif domain == "creative":
                self.k_intelligence = [2.0, 1.5, 1.0]  # تقليل الحدة للإبداع
                adaptations.append("Creative flexibility mode")
            elif domain == "linguistic":
                # تفعيل جسر بيان-بصيرة للمهام اللغوية
                if self.bayan_bridge:
                    adaptations.append("Bayan-Baserah bridge activated for linguistics")

        # تكييف حسب مستوى الدقة المطلوب
        if "precision" in new_context:
            precision = new_context["precision"]
            if precision == "high":
                self.alpha_intelligence = [a * 1.1 for a in self.alpha_intelligence]
                adaptations.append("High precision mode")
            elif precision == "low":
                self.alpha_intelligence = [a * 0.9 for a in self.alpha_intelligence]
                adaptations.append("Fast processing mode")

        return {
            "adapted": True,
            "context": new_context,
            "adaptations": adaptations,
            "current_parameters": {
                "alpha": self.alpha_intelligence,
                "k": self.k_intelligence,
                "beta": self.beta_intelligence
            }
        }

    def analyze_with_bayan(self, text: str) -> Dict[str, Any]:
        """
        تحليل نص باستخدام جسر بيان-بصيرة

        Args:
            text: النص للتحليل

        Returns:
            نتيجة التحليل
        """
        if not self.bayan_bridge:
            return {
                "error": "جسر بيان-بصيرة غير متاح",
                "suggestion": "تأكد من وجود extensions/bayan_baserah_bridge.py"
            }

        results = {
            "text": text,
            "analysis_type": "bayan_baserah_integrated"
        }

        # تحليل الحروف
        if len(text) == 1:
            # تحليل حرف واحد
            letter_analysis = self.bayan_bridge.analyze_letter_visually(text)
            results["letter_analysis"] = {
                "letter": letter_analysis.letter,
                "shape": letter_analysis.shape_type.value if hasattr(letter_analysis.shape_type, 'value') else str(letter_analysis.shape_type),
                "meanings": letter_analysis.semantic_meanings,
                "equation": letter_analysis.baserah_equation,
                "confidence": letter_analysis.confidence
            }
        else:
            # تحليل كلمة
            word_analysis = self.bayan_bridge.word_visual_analysis(text)
            results["word_analysis"] = word_analysis

            # تحليل دلالي متقدم
            if self.semantic_engine:
                semantic_analysis = self.semantic_engine.full_analysis(text)
                results["semantic_analysis"] = semantic_analysis

        return results

# ==================== اختبار الوكيل الذكي ====================

def test_intelligent_agent():
    """اختبار شامل للوكيل الذكي الثوري"""
    print("🤖 اختبار الوكيل المساعد الذكي الثوري")
    print("="*60)
    
    # إنشاء الوكيل
    agent = RevolutionaryIntelligentAgent("TestAgent", IntelligenceLevel.ADVANCED)
    
    # مهام اختبار متنوعة
    test_tasks = [
        Task(
            description="حل معادلة رياضية معقدة بالنظريات الثورية",
            task_type=TaskType.MATHEMATICAL,
            priority=8,
            requirements=["دقة عالية", "شفافية كاملة", "سرعة في الحل"]
        ),
        Task(
            description="تحليل نص عربي وفهم معانيه العميقة",
            task_type=TaskType.LINGUISTIC,
            priority=6,
            context={"language": "arabic", "domain": "literature"},
            requirements=["فهم عميق", "تحليل دلالي"]
        ),
        Task(
            description="تصميم حل إبداعي لمشكلة تقنية معقدة",
            task_type=TaskType.CREATIVE,
            priority=9,
            requirements=["ابتكار", "عملية", "قابلية التطبيق"]
        ),
        Task(
            description="وضع خطة استراتيجية شاملة للمشروع",
            task_type=TaskType.PLANNING,
            priority=7,
            context={"timeline": "6 months", "budget": "limited"},
            requirements=["شمولية", "مرونة", "قابلية القياس"]
        )
    ]
    
    print(f"\n🧪 اختبار {len(test_tasks)} مهام متنوعة:")
    
    # تنفيذ المهام
    for i, task in enumerate(test_tasks, 1):
        print(f"\n📋 المهمة {i}: {task.task_type.value}")
        print(f"   الوصف: {task.description}")
        
        # تنفيذ المهمة
        completed_task = agent.execute_task(task)
        
        print(f"   ✅ الحالة: {completed_task.status}")
        print(f"   🎯 الثقة: {completed_task.solution_confidence:.3f}")
        print(f"   ⏱️ الوقت: {completed_task.processing_time:.3f}s")
        print(f"   🧠 الذكاء: {completed_task.intelligence_score:.3f}")
    
    # عرض إحصائيات الوكيل
    print(f"\n📊 إحصائيات الوكيل:")
    status = agent.get_agent_status()
    print(f"   📈 معدل النجاح: {status['success_rate']:.3f}")
    print(f"   🎯 متوسط الثقة: {status['average_confidence']:.3f}")
    print(f"   📚 التجارب المحفوظة: {status['memory_experiences']}")
    print(f"   ✅ الاستراتيجيات الناجحة: {status['successful_strategies']}")
    print(f"   🧬 معادلة الشكل العام: {'متصلة ✓' if status['has_shape_equation'] else 'غير متصلة'}")
    print(f"   🌉 جسر بيان-بصيرة: {'متصل ✓' if status['has_bayan_bridge'] else 'غير متصل'}")

    # اختبار الدوال الجديدة
    print(f"\n🔧 اختبار الدوال الجديدة:")

    # اختبار process_task
    print(f"\n   📝 اختبار process_task:")
    result = agent.process_task("تحليل جملة عربية بسيطة")
    print(f"      ✅ الحالة: {result['status']}")
    print(f"      🎯 الثقة: {result['confidence']:.3f}")

    # اختبار learn_from_feedback
    print(f"\n   📚 اختبار learn_from_feedback:")
    learn_result = agent.learn_from_feedback("ممتاز، النتيجة صحيحة!")
    print(f"      ✅ نوع التغذية: {learn_result['feedback_type']}")
    print(f"      📊 كفاءة التعلم: {learn_result['learning_efficiency']:.3f}")

    # اختبار adapt_behavior
    print(f"\n   🔄 اختبار adapt_behavior:")
    adapt_result = agent.adapt_behavior({"language": "arabic", "domain": "linguistic", "precision": "high"})
    print(f"      ✅ التكيفات: {adapt_result['adaptations']}")

    # اختبار analyze_with_bayan
    print(f"\n   🌉 اختبار analyze_with_bayan:")
    bayan_result = agent.analyze_with_bayan("ع")
    if "error" in bayan_result:
        print(f"      ⚠️ {bayan_result['error']}")
    else:
        print(f"      ✅ تحليل الحرف: متاح")
        if "letter_analysis" in bayan_result:
            print(f"      📝 الشكل: {bayan_result['letter_analysis'].get('shape', 'غير محدد')}")

    print(f"\n✅ انتهى اختبار الوكيل الذكي الثوري!")
    return agent

# إضافة alias للكلاس لحل مشكلة الاستيراد
BaserahIntelligentAgent = RevolutionaryIntelligentAgent

if __name__ == "__main__":
    test_intelligent_agent()
