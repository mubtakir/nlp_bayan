"""
نظام الوعي والانتباه - Consciousness & Attention System
========================================================

نظام يحاكي آلية الانتباه والوعي:
- التركيز على المعلومات المهمة
- تجاهل المشتتات
- إدارة الموارد المعرفية

المؤلف: باسل يحيى عبدالله
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum
import numpy as np
from datetime import datetime


class AttentionLevel(Enum):
    """مستويات الانتباه"""
    FOCUSED = "مركز"
    DIFFUSE = "منتشر"
    ALERT = "منتبه"
    RELAXED = "مسترخ"


@dataclass
class AttentionFocus:
    """نقطة تركيز الانتباه"""
    target: Any
    priority: float = 1.0
    duration: float = 0.0
    start_time: datetime = field(default_factory=datetime.now)
    metadata: Dict = field(default_factory=dict)
    
    def get_age(self) -> float:
        """عمر التركيز بالثواني"""
        return (datetime.now() - self.start_time).total_seconds()


@dataclass
class ConsciousnessState:
    """حالة الوعي"""
    level: AttentionLevel = AttentionLevel.ALERT
    active_focuses: List[AttentionFocus] = field(default_factory=list)
    awareness_score: float = 1.0
    cognitive_load: float = 0.0


class ConsciousnessSystem:
    """
    نظام الوعي والانتباه
    
    يدير:
    - نقاط التركيز والانتباه
    - مستوى الوعي العام
    - الحمل المعرفي
    """
    
    def __init__(self, max_focuses: int = 7):
        self.max_focuses = max_focuses  # السعة المعرفية
        self.state = ConsciousnessState()
        self.history: List[Dict] = []
    
    def focus_on(self, target: Any, priority: float = 1.0) -> AttentionFocus:
        """
        التركيز على هدف جديد
        """
        focus = AttentionFocus(target=target, priority=priority)
        
        # إدارة السعة
        if len(self.state.active_focuses) >= self.max_focuses:
            # إزالة أقل الأهداف أولوية
            self.state.active_focuses.sort(key=lambda f: f.priority)
            self.state.active_focuses.pop(0)
        
        self.state.active_focuses.append(focus)
        self._update_cognitive_load()
        
        self.history.append({
            "action": "focus",
            "target": str(target),
            "priority": priority,
            "time": datetime.now()
        })
        
        return focus
    
    def defocus(self, target: Any = None):
        """
        إزالة التركيز
        """
        if target is None:
            # إزالة جميع نقاط التركيز
            self.state.active_focuses.clear()
        else:
            # إزالة تركيز معين
            self.state.active_focuses = [
                f for f in self.state.active_focuses 
                if f.target != target
            ]
        
        self._update_cognitive_load()
    
    def get_main_focus(self) -> Optional[AttentionFocus]:
        """
        الحصول على نقطة التركيز الرئيسية
        """
        if not self.state.active_focuses:
            return None
        
        # الأعلى أولوية
        return max(self.state.active_focuses, key=lambda f: f.priority)
    
    def set_attention_level(self, level: AttentionLevel):
        """تعيين مستوى الانتباه"""
        self.state.level = level
        
        # تعديل الوعي بناءً على المستوى
        level_scores = {
            AttentionLevel.FOCUSED: 1.0,
            AttentionLevel.ALERT: 0.8,
            AttentionLevel.DIFFUSE: 0.5,
            AttentionLevel.RELAXED: 0.3
        }
        self.state.awareness_score = level_scores.get(level, 0.5)
    
    def _update_cognitive_load(self):
        """تحديث الحمل المعرفي"""
        if not self.state.active_focuses:
            self.state.cognitive_load = 0.0
            return
        
        # الحمل = مجموع الأولويات / السعة القصوى
        total_priority = sum(f.priority for f in self.state.active_focuses)
        self.state.cognitive_load = min(total_priority / self.max_focuses, 1.0)
    
    def is_overloaded(self) -> bool:
        """هل النظام مثقل؟"""
        return self.state.cognitive_load > 0.8
    
    def get_status(self) -> Dict:
        """حالة النظام"""
        main_focus = self.get_main_focus()
        return {
            "مستوى_الانتباه": self.state.level.value,
            "درجة_الوعي": f"{self.state.awareness_score:.2%}",
            "الحمل_المعرفي": f"{self.state.cognitive_load:.2%}",
            "نقاط_التركيز": len(self.state.active_focuses),
            "التركيز_الرئيسي": str(main_focus.target) if main_focus else "لا يوجد",
            "مثقل": self.is_overloaded()
        }

