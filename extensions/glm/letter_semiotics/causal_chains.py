# -*- coding: utf-8 -*-
"""
محرك السلاسل السببية
Causal Chain Engine

يقوم ببناء وتحليل العلاقات السببية بين معاني الحروف
"""

from typing import List, Dict, Optional, Tuple, Set
from dataclasses import dataclass, field


@dataclass
class CausalRelation:
    """علاقة سببية بين معنيين"""
    from_meaning: str
    to_meaning: str
    relation_type: str  # causes, requires, enables, leads_to
    weight: float = 1.0


@dataclass
class CausalPath:
    """مسار سببي كامل"""
    start: str
    end: str
    path: List[str]
    total_weight: float
    relations: List[CausalRelation]


class CausalChainEngine:
    """محرك السلاسل السببية"""
    
    def __init__(self):
        self._relations: Dict[str, List[CausalRelation]] = {}
        self._load_default_relations()
    
    def _load_default_relations(self):
        """تحميل العلاقات السببية الافتراضية"""
        # علاقات حرف الباء
        self.add_relation("دك", "امتلاء", "causes", 0.9)
        self.add_relation("امتلاء", "بلع", "causes", 0.8)
        self.add_relation("بلع", "حمل", "requires", 0.85)
        self.add_relation("حمل", "نقل", "enables", 0.9)
        self.add_relation("امتلاء", "تشبع", "causes", 0.9)
        
        # علاقات حرف الشين
        self.add_relation("تشتت", "تشعب", "causes", 0.9)
        self.add_relation("تشعب", "انتشار", "leads_to", 0.85)
        
        # علاقات حرف الجيم
        self.add_relation("التحام", "تجمع", "causes", 0.9)
        self.add_relation("تجمع", "وتد", "enables", 0.8)
        
        # علاقات حرف الراء
        self.add_relation("تدفق", "انطلاق", "causes", 0.85)
        self.add_relation("انطلاق", "انسيابية", "leads_to", 0.8)
        self.add_relation("انسيابية", "تكرار", "enables", 0.75)
    
    def add_relation(self, from_meaning: str, to_meaning: str, 
                     relation_type: str, weight: float = 1.0):
        """إضافة علاقة سببية"""
        relation = CausalRelation(from_meaning, to_meaning, relation_type, weight)
        if from_meaning not in self._relations:
            self._relations[from_meaning] = []
        self._relations[from_meaning].append(relation)
    
    def get_direct_effects(self, meaning: str) -> List[CausalRelation]:
        """الحصول على التأثيرات المباشرة لمعنى"""
        return self._relations.get(meaning, [])
    
    def find_path(self, start: str, end: str, max_depth: int = 5) -> Optional[CausalPath]:
        """إيجاد مسار سببي بين معنيين"""
        visited: Set[str] = set()
        path: List[str] = []
        relations: List[CausalRelation] = []
        
        def dfs(current: str, depth: int) -> bool:
            if depth > max_depth:
                return False
            if current == end:
                return True
            if current in visited:
                return False
            
            visited.add(current)
            path.append(current)
            
            for relation in self._relations.get(current, []):
                relations.append(relation)
                if dfs(relation.to_meaning, depth + 1):
                    return True
                relations.pop()
            
            path.pop()
            return False
        
        if dfs(start, 0):
            path.append(end)
            total_weight = 1.0
            for r in relations:
                total_weight *= r.weight
            return CausalPath(start, end, path, total_weight, relations)
        return None
    
    def get_all_effects(self, meaning: str, max_depth: int = 3) -> List[Tuple[str, float]]:
        """الحصول على جميع التأثيرات المباشرة وغير المباشرة"""
        effects: List[Tuple[str, float]] = []
        visited: Set[str] = set()
        
        def explore(current: str, weight: float, depth: int):
            if depth > max_depth or current in visited:
                return
            visited.add(current)
            
            for relation in self._relations.get(current, []):
                new_weight = weight * relation.weight
                effects.append((relation.to_meaning, new_weight))
                explore(relation.to_meaning, new_weight, depth + 1)
        
        explore(meaning, 1.0, 0)
        return sorted(effects, key=lambda x: x[1], reverse=True)
    
    def get_root_causes(self) -> List[str]:
        """الحصول على الأسباب الجذرية (التي ليس لها أسباب)"""
        all_effects = set()
        for relations in self._relations.values():
            for r in relations:
                all_effects.add(r.to_meaning)
        
        return [m for m in self._relations.keys() if m not in all_effects]
    
    def get_final_effects(self) -> List[str]:
        """الحصول على النتائج النهائية (التي ليس لها تأثيرات)"""
        all_causes = set(self._relations.keys())
        all_effects = set()
        for relations in self._relations.values():
            for r in relations:
                all_effects.add(r.to_meaning)
        
        return [e for e in all_effects if e not in all_causes]

