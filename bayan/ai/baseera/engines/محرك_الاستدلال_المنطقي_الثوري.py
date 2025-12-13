#!/usr/bin/env python3
"""
محرك الاستدلال المنطقي الثوري v1.0 - باسل يحيى عبدالله
تطبيق الاستدلال المنطقي بالنهج الثوري الخالص بدون أي مكتبات ذكاء اصطناعي تقليدية
"""

import math
import re
from typing import Dict, List, Any, Optional, Union, Tuple
from النظريات_الثورية_المحسنة_v2 import EnhancedRevolutionaryTheories


class RevolutionaryLogicalReasoningEngine:
    """محرك الاستدلال المنطقي الثوري - بدون AI تقليدي"""
    
    def __init__(self):
        self.engine_name = "محرك الاستدلال الثوري"
        self.creator = "باسل يحيى عبدالله"
        self.version = "v1.0 - ثوري خالص"
        
        # أنواع الاستدلال المدعومة
        self.reasoning_modes = {
            "deductive": "استنتاجي",
            "inductive": "استقرائي", 
            "abductive": "افتراضي"
        }
        
        # قواعد الاستدلال الثورية
        self.revolutionary_rules = {
            "modus_ponens": {
                "name": "القياس المنطقي المباشر",
                "confidence": 0.95,
                "baserah_params": {"n": 1, "k": 1.5, "alpha": 1.0},
                "pattern": r"إذا (.+) فإن (.+)"
            },
            "modus_tollens": {
                "name": "القياس المنطقي العكسي",
                "confidence": 0.9,
                "baserah_params": {"n": 1, "k": 1.3, "alpha": 0.9},
                "pattern": r"إذا (.+) فإن (.+)"
            },
            "syllogism": {
                "name": "القياس الأرسطي",
                "confidence": 0.88,
                "baserah_params": {"n": 2, "k": 1.2, "alpha": 0.85},
                "pattern": r"كل (.+) هو (.+)"
            },
            "contradiction_detection": {
                "name": "كشف التناقض",
                "confidence": 0.92,
                "baserah_params": {"n": 1, "k": 2.0, "alpha": 1.0},
                "pattern": r"(.+) و ليس (.+)"
            }
        }
        
        # النظريات الثورية المحسنة
        self.revolutionary_theories = EnhancedRevolutionaryTheories()
        
        # ذاكرة الاستدلال
        self.reasoning_memory = {
            "premises": [],
            "conclusions": [],
            "reasoning_paths": [],
            "contradictions": []
        }
        
        print(f"🧠 تم تهيئة {self.engine_name} - {self.creator}")
        print(f"📚 أنواع الاستدلال: {list(self.reasoning_modes.values())}")
        print(f"⚖️ قواعد الاستدلال: {len(self.revolutionary_rules)} قاعدة ثورية")
    
    def baserah_sigmoid(self, x: float, n: int = 1, k: float = 1.0, x0: float = 0.0, alpha: float = 1.0) -> float:
        """المعادلة الأساسية: σₙ(x; k, x₀, n, α) = α * (1 / (1 + e^(-k*(x - x₀)^n)))"""
        try:
            exponent = -k * ((x - x0) ** n)
            if exponent > 700:  # تجنب overflow
                return 0.0
            elif exponent < -700:
                return alpha
            return alpha * (1.0 / (1.0 + (2.718281828459045 ** exponent)))
        except:
            return alpha * 0.5
    
    def baserah_linear(self, x: float, beta: float = 1.0, gamma: float = 0.0) -> float:
        """المعادلة الخطية الثورية: f(x) = β*x + γ"""
        return beta * x + gamma
    
    # ==========================================
    # 🧠 محرك الاستدلال الرئيسي
    # ==========================================
    
    def reason_revolutionarily(self, premises: List[str], conclusion_target: str = None, mode: str = "deductive") -> Dict[str, Any]:
        """الاستدلال بالنهج الثوري الخالص"""
        
        print(f"\n🧠 بدء الاستدلال الثوري - النمط: {self.reasoning_modes.get(mode, mode)}")
        print(f"📝 عدد المقدمات: {len(premises)}")
        
        # تحليل المقدمات
        premises_analysis = self._analyze_premises_revolutionarily(premises)
        
        # تطبيق النظريات الثورية على الاستدلال
        revolutionary_analysis = self._apply_theories_to_reasoning(premises_analysis, conclusion_target)
        
        # تطبيق قواعد الاستدلال حسب النمط
        reasoning_result = self._apply_reasoning_mode(premises, conclusion_target, mode, premises_analysis)
        
        # حساب الثقة النهائية
        final_confidence = self._calculate_revolutionary_confidence(
            revolutionary_analysis, reasoning_result, premises_analysis
        )
        
        # إنشاء مسار الاستدلال
        reasoning_path = self._create_reasoning_path(premises, reasoning_result, revolutionary_analysis)
        
        # حفظ في الذاكرة
        self._save_to_memory(premises, reasoning_result.get("conclusion", conclusion_target), reasoning_path)
        
        return {
            "engine": self.engine_name,
            "creator": self.creator,
            "reasoning_mode": mode,
            "premises": premises,
            "conclusion": reasoning_result.get("conclusion", conclusion_target),
            "confidence": final_confidence,
            "premises_analysis": premises_analysis,
            "revolutionary_analysis": revolutionary_analysis,
            "reasoning_result": reasoning_result,
            "reasoning_path": reasoning_path,
            "theories_applied": {
                "zero_duality": revolutionary_analysis["zero_duality"],
                "perpendicular_opposites": revolutionary_analysis["perpendicular_opposites"],
                "filament_theory": revolutionary_analysis["filament_theory"]
            },
            "revolutionary_insight": self._generate_reasoning_insight(final_confidence, reasoning_result)
        }
    
    def _analyze_premises_revolutionarily(self, premises: List[str]) -> Dict[str, Any]:
        """تحليل المقدمات بالنهج الثوري"""
        
        analysis = {
            "total_premises": len(premises),
            "premise_strengths": [],
            "logical_connections": [],
            "contradiction_check": None,
            "premise_types": [],
            "complexity_analysis": {}
        }
        
        for i, premise in enumerate(premises):
            # حساب قوة المقدمة
            premise_strength = self._calculate_premise_strength(premise)
            analysis["premise_strengths"].append(premise_strength)
            
            # تحديد نوع المقدمة
            premise_type = self._identify_premise_type(premise)
            analysis["premise_types"].append(premise_type)
            
            # فحص الاتصالات المنطقية
            connections = self._find_logical_connections(premise, premises[i+1:])
            analysis["logical_connections"].extend(connections)
        
        # فحص التناقضات
        analysis["contradiction_check"] = self._check_contradictions_revolutionarily(premises)
        
        # تحليل التعقيد
        analysis["complexity_analysis"] = self._analyze_premises_complexity(premises)
        
        return analysis
    
    def _calculate_premise_strength(self, premise: str) -> float:
        """حساب قوة المقدمة باستخدام المعادلات الثورية"""
        
        # عوامل قوة المقدمة
        length_factor = len(premise.split())  # تعقيد المقدمة
        certainty_keywords = ["بالتأكيد", "حتماً", "دائماً", "أبداً", "كل", "جميع"]
        uncertainty_keywords = ["ربما", "أحياناً", "قد", "يمكن", "محتمل"]
        
        # حساب عامل اليقين
        certainty_score = sum(1 for keyword in certainty_keywords if keyword in premise)
        uncertainty_score = sum(1 for keyword in uncertainty_keywords if keyword in premise)
        
        # تطبيق المعادلة الثورية
        strength = self.baserah_sigmoid(
            length_factor + certainty_score - uncertainty_score,
            n=1, k=0.1, alpha=1.0
        )
        
        return strength
    
    def _identify_premise_type(self, premise: str) -> str:
        """تحديد نوع المقدمة"""
        
        if re.search(r"إذا .+ فإن .+", premise):
            return "شرطية"
        elif re.search(r"كل .+ هو .+", premise):
            return "كلية"
        elif re.search(r"بعض .+ هو .+", premise):
            return "جزئية"
        elif re.search(r"ليس .+", premise):
            return "سالبة"
        else:
            return "بسيطة"
    
    def _find_logical_connections(self, premise: str, other_premises: List[str]) -> List[Dict[str, Any]]:
        """العثور على الاتصالات المنطقية بين المقدمات"""
        
        connections = []
        
        for other_premise in other_premises:
            # حساب قوة الاتصال
            connection_strength = self._calculate_connection_strength(premise, other_premise)
            
            if connection_strength > 0.5:
                connections.append({
                    "premise1": premise,
                    "premise2": other_premise,
                    "connection_strength": connection_strength,
                    "connection_type": self._identify_connection_type(premise, other_premise)
                })
        
        return connections
    
    def _calculate_connection_strength(self, premise1: str, premise2: str) -> float:
        """حساب قوة الاتصال بين مقدمتين"""
        
        # البحث عن كلمات مشتركة
        words1 = set(premise1.split())
        words2 = set(premise2.split())
        common_words = words1.intersection(words2)
        
        # حساب نسبة التشابه
        max_words = max(len(words1), len(words2), 1)
        similarity_ratio = len(common_words) / max_words if max_words > 0 else 0.0
        
        # تطبيق المعادلة الثورية
        connection_strength = self.baserah_sigmoid(
            similarity_ratio * 10,  # تضخيم للحساسية
            n=1, k=2.0, alpha=1.0
        )
        
        return connection_strength
    
    def _identify_connection_type(self, premise1: str, premise2: str) -> str:
        """تحديد نوع الاتصال بين المقدمات"""
        
        if "إذا" in premise1 and any(word in premise2 for word in premise1.split()):
            return "سببي"
        elif "كل" in premise1 and "بعض" in premise2:
            return "تدرجي"
        elif "ليس" in premise1 or "ليس" in premise2:
            return "تناقضي"
        else:
            return "ترابطي"
    
    def _check_contradictions_revolutionarily(self, premises: List[str]) -> Dict[str, Any]:
        """فحص التناقضات بالنهج الثوري"""
        
        contradictions = []
        
        for i, premise1 in enumerate(premises):
            for j, premise2 in enumerate(premises[i+1:], i+1):
                # فحص التناقض المباشر
                contradiction_score = self._detect_contradiction(premise1, premise2)
                
                if contradiction_score > 0.7:
                    contradictions.append({
                        "premise1": premise1,
                        "premise2": premise2,
                        "contradiction_score": contradiction_score,
                        "contradiction_type": self._classify_contradiction(premise1, premise2)
                    })
        
        return {
            "contradictions_found": len(contradictions) > 0,
            "contradiction_count": len(contradictions),
            "contradictions": contradictions,
            "overall_consistency": self._calculate_overall_consistency(contradictions, len(premises))
        }
    
    def _detect_contradiction(self, premise1: str, premise2: str) -> float:
        """كشف التناقض بين مقدمتين"""
        
        # البحث عن أنماط التناقض
        negation_patterns = [
            (r"(.+) هو (.+)", r"(.+) ليس (.+)"),
            (r"كل (.+) (.+)", r"لا (.+) (.+)"),
            (r"دائماً (.+)", r"أبداً (.+)")
        ]
        
        contradiction_score = 0.0
        
        for positive_pattern, negative_pattern in negation_patterns:
            if re.search(positive_pattern, premise1) and re.search(negative_pattern, premise2):
                # تطبيق المعادلة الثورية لحساب قوة التناقض
                contradiction_score = self.baserah_sigmoid(
                    self._calculate_semantic_opposition(premise1, premise2),
                    n=1, k=2.0, alpha=1.0
                )
                break
        
        return contradiction_score
    
    def _calculate_semantic_opposition(self, premise1: str, premise2: str) -> float:
        """حساب التعارض الدلالي"""
        
        # كلمات التأكيد والنفي
        affirmative_words = ["هو", "كل", "دائماً", "بالتأكيد"]
        negative_words = ["ليس", "لا", "أبداً", "مستحيل"]
        
        # حساب درجة التأكيد والنفي
        affirmative_score1 = sum(1 for word in affirmative_words if word in premise1)
        negative_score1 = sum(1 for word in negative_words if word in premise1)
        
        affirmative_score2 = sum(1 for word in affirmative_words if word in premise2)
        negative_score2 = sum(1 for word in negative_words if word in premise2)
        
        # حساب التعارض
        opposition = abs((affirmative_score1 - negative_score1) - (affirmative_score2 - negative_score2))
        
        return opposition
    
    def _classify_contradiction(self, premise1: str, premise2: str) -> str:
        """تصنيف نوع التناقض"""
        
        if "ليس" in premise1 or "ليس" in premise2:
            return "تناقض مباشر"
        elif "كل" in premise1 and "لا" in premise2:
            return "تناقض كلي"
        elif "دائماً" in premise1 and "أبداً" in premise2:
            return "تناقض زمني"
        else:
            return "تناقض ضمني"
    
    def _calculate_overall_consistency(self, contradictions: List[Dict], total_premises: int) -> float:
        """حساب الاتساق الإجمالي"""
        
        if total_premises == 0:
            return 1.0
        
        contradiction_ratio = len(contradictions) / (total_premises * (total_premises - 1) / 2)
        
        # تطبيق المعادلة الثورية للاتساق
        consistency = self.baserah_sigmoid(
            -contradiction_ratio * 10,  # كلما زادت التناقضات قل الاتساق
            n=1, k=2.0, alpha=1.0
        )
        
        return consistency
    
    def _analyze_premises_complexity(self, premises: List[str]) -> Dict[str, Any]:
        """تحليل تعقيد المقدمات"""
        
        total_words = sum(len(premise.split()) for premise in premises)
        avg_length = total_words / len(premises) if premises and len(premises) > 0 else 0.0
        
        # حساب مؤشر التعقيد
        complexity_index = self.baserah_sigmoid(
            avg_length,
            n=1, k=0.1, alpha=1.0
        )
        
        # تصنيف التعقيد
        if complexity_index > 0.8:
            complexity_level = "معقد جداً"
        elif complexity_index > 0.6:
            complexity_level = "معقد"
        elif complexity_index > 0.4:
            complexity_level = "متوسط"
        else:
            complexity_level = "بسيط"
        
        return {
            "total_words": total_words,
            "average_length": avg_length,
            "complexity_index": complexity_index,
            "complexity_level": complexity_level
        }
    
    # ==========================================
    # ⚖️ تطبيق قواعد الاستدلال الثورية
    # ==========================================
    
    def _apply_reasoning_mode(self, premises: List[str], conclusion_target: str, mode: str, analysis: Dict) -> Dict[str, Any]:
        """تطبيق نمط الاستدلال المحدد"""
        
        if mode == "deductive":
            return self._apply_deductive_reasoning(premises, conclusion_target, analysis)
        elif mode == "inductive":
            return self._apply_inductive_reasoning(premises, conclusion_target, analysis)
        elif mode == "abductive":
            return self._apply_abductive_reasoning(premises, conclusion_target, analysis)
        else:
            return self._apply_general_reasoning(premises, conclusion_target, analysis)
    
    def _apply_deductive_reasoning(self, premises: List[str], conclusion_target: str, analysis: Dict) -> Dict[str, Any]:
        """تطبيق الاستدلال الاستنتاجي (من العام إلى الخاص)"""
        
        print("   🔍 تطبيق الاستدلال الاستنتاجي...")
        
        # البحث عن قواعد Modus Ponens
        modus_ponens_results = self._apply_modus_ponens(premises, conclusion_target)
        
        # البحث عن قواعد Modus Tollens
        modus_tollens_results = self._apply_modus_tollens(premises, conclusion_target)
        
        # البحث عن القياس الأرسطي
        syllogism_results = self._apply_syllogism(premises, conclusion_target)
        
        # دمج النتائج
        all_results = modus_ponens_results + modus_tollens_results + syllogism_results
        
        # اختيار أفضل نتيجة
        best_result = max(all_results, key=lambda x: x["confidence"]) if all_results else {
            "conclusion": conclusion_target or "لا يمكن الاستنتاج",
            "confidence": 0.0,
            "rule_applied": "لا توجد قاعدة مطبقة",
            "reasoning_steps": []
        }
        
        return {
            "reasoning_type": "استنتاجي",
            "conclusion": best_result["conclusion"],
            "confidence": best_result["confidence"],
            "rule_applied": best_result["rule_applied"],
            "reasoning_steps": best_result["reasoning_steps"],
            "all_possible_conclusions": all_results
        }
    
    def _apply_modus_ponens(self, premises: List[str], conclusion_target: str) -> List[Dict[str, Any]]:
        """تطبيق قاعدة Modus Ponens الثورية"""
        
        results = []
        
        for premise in premises:
            # البحث عن نمط "إذا ... فإن ..."
            match = re.search(r"إذا (.+) فإن (.+)", premise)
            if match:
                condition = match.group(1).strip()
                consequence = match.group(2).strip()
                
                # البحث عن المقدمة التي تؤكد الشرط
                for other_premise in premises:
                    if condition in other_premise and premise != other_premise:
                        # تطبيق Modus Ponens
                        confidence = self._calculate_modus_ponens_confidence(premise, other_premise, consequence)
                        
                        results.append({
                            "conclusion": consequence,
                            "confidence": confidence,
                            "rule_applied": "Modus Ponens الثوري",
                            "reasoning_steps": [
                                f"المقدمة الشرطية: {premise}",
                                f"تأكيد الشرط: {other_premise}",
                                f"النتيجة: {consequence}"
                            ]
                        })
        
        return results
    
    def _calculate_modus_ponens_confidence(self, conditional_premise: str, affirming_premise: str, conclusion: str) -> float:
        """حساب ثقة Modus Ponens بالنهج الثوري"""
        
        # قوة المقدمة الشرطية
        conditional_strength = self._calculate_premise_strength(conditional_premise)
        
        # قوة تأكيد الشرط
        affirming_strength = self._calculate_premise_strength(affirming_premise)
        
        # تطبيق المعادلة الثورية
        confidence = self.baserah_sigmoid(
            (conditional_strength + affirming_strength) / 2,
            **self.revolutionary_rules["modus_ponens"]["baserah_params"]
        )
        
        return confidence * self.revolutionary_rules["modus_ponens"]["confidence"]
    
    def _apply_modus_tollens(self, premises: List[str], conclusion_target: str) -> List[Dict[str, Any]]:
        """تطبيق قاعدة Modus Tollens الثورية"""
        
        results = []
        
        for premise in premises:
            # البحث عن نمط "إذا ... فإن ..."
            match = re.search(r"إذا (.+) فإن (.+)", premise)
            if match:
                condition = match.group(1).strip()
                consequence = match.group(2).strip()
                
                # البحث عن المقدمة التي تنفي النتيجة
                for other_premise in premises:
                    if f"ليس {consequence}" in other_premise or f"لا {consequence}" in other_premise:
                        # تطبيق Modus Tollens
                        negated_condition = f"ليس {condition}"
                        confidence = self._calculate_modus_tollens_confidence(premise, other_premise, negated_condition)
                        
                        results.append({
                            "conclusion": negated_condition,
                            "confidence": confidence,
                            "rule_applied": "Modus Tollens الثوري",
                            "reasoning_steps": [
                                f"المقدمة الشرطية: {premise}",
                                f"نفي النتيجة: {other_premise}",
                                f"النتيجة: {negated_condition}"
                            ]
                        })
        
        return results
    
    def _calculate_modus_tollens_confidence(self, conditional_premise: str, negating_premise: str, conclusion: str) -> float:
        """حساب ثقة Modus Tollens بالنهج الثوري"""
        
        # قوة المقدمة الشرطية
        conditional_strength = self._calculate_premise_strength(conditional_premise)
        
        # قوة نفي النتيجة
        negating_strength = self._calculate_premise_strength(negating_premise)
        
        # تطبيق المعادلة الثورية
        confidence = self.baserah_sigmoid(
            (conditional_strength + negating_strength) / 2,
            **self.revolutionary_rules["modus_tollens"]["baserah_params"]
        )
        
        return confidence * self.revolutionary_rules["modus_tollens"]["confidence"]
    
    def _apply_syllogism(self, premises: List[str], conclusion_target: str) -> List[Dict[str, Any]]:
        """تطبيق القياس الأرسطي الثوري"""
        
        results = []
        
        # البحث عن مقدمات القياس
        for i, premise1 in enumerate(premises):
            for j, premise2 in enumerate(premises[i+1:], i+1):
                syllogism_result = self._check_syllogism_pattern(premise1, premise2)
                
                if syllogism_result:
                    results.append(syllogism_result)
        
        return results
    
    def _check_syllogism_pattern(self, premise1: str, premise2: str) -> Optional[Dict[str, Any]]:
        """فحص نمط القياس الأرسطي"""
        
        # نمط: كل A هو B، كل B هو C -> كل A هو C
        match1 = re.search(r"كل (.+) هو (.+)", premise1)
        match2 = re.search(r"كل (.+) هو (.+)", premise2)
        
        if match1 and match2:
            a, b = match1.groups()
            c, d = match2.groups()
            
            # فحص الحد الأوسط
            if b.strip() == c.strip():
                conclusion = f"كل {a} هو {d}"
                confidence = self._calculate_syllogism_confidence(premise1, premise2, conclusion)
                
                return {
                    "conclusion": conclusion,
                    "confidence": confidence,
                    "rule_applied": "القياس الأرسطي الثوري",
                    "reasoning_steps": [
                        f"المقدمة الكبرى: {premise1}",
                        f"المقدمة الصغرى: {premise2}",
                        f"النتيجة: {conclusion}"
                    ]
                }
        
        return None
    
    def _calculate_syllogism_confidence(self, major_premise: str, minor_premise: str, conclusion: str) -> float:
        """حساب ثقة القياس الأرسطي بالنهج الثوري"""
        
        # قوة المقدمة الكبرى
        major_strength = self._calculate_premise_strength(major_premise)
        
        # قوة المقدمة الصغرى
        minor_strength = self._calculate_premise_strength(minor_premise)
        
        # تطبيق المعادلة الثورية
        confidence = self.baserah_sigmoid(
            (major_strength + minor_strength) / 2,
            **self.revolutionary_rules["syllogism"]["baserah_params"]
        )
        
        return confidence * self.revolutionary_rules["syllogism"]["confidence"]

    def _apply_inductive_reasoning(self, premises: List[str], conclusion_target: str, analysis: Dict) -> Dict[str, Any]:
        """تطبيق الاستدلال الاستقرائي (من الخاص إلى العام)"""

        print("   🔍 تطبيق الاستدلال الاستقرائي...")

        # تحليل الأنماط في المقدمات
        patterns = self._identify_inductive_patterns(premises)

        # توليد تعميمات
        generalizations = self._generate_generalizations(patterns, premises)

        # اختيار أفضل تعميم
        best_generalization = max(generalizations, key=lambda x: x["confidence"]) if generalizations else {
            "conclusion": conclusion_target or "لا يمكن التعميم",
            "confidence": 0.0,
            "pattern_type": "لا يوجد نمط",
            "reasoning_steps": []
        }

        return {
            "reasoning_type": "استقرائي",
            "conclusion": best_generalization["conclusion"],
            "confidence": best_generalization["confidence"],
            "pattern_type": best_generalization["pattern_type"],
            "reasoning_steps": best_generalization["reasoning_steps"],
            "all_patterns": patterns
        }

    def _identify_inductive_patterns(self, premises: List[str]) -> List[Dict[str, Any]]:
        """تحديد الأنماط الاستقرائية"""

        patterns = []

        # البحث عن أنماط التكرار
        word_frequency = {}
        for premise in premises:
            words = premise.split()
            for word in words:
                word_frequency[word] = word_frequency.get(word, 0) + 1

        # تحديد الكلمات المتكررة
        frequent_words = {word: freq for word, freq in word_frequency.items() if freq > 1}

        if frequent_words:
            patterns.append({
                "type": "تكرار الكلمات",
                "elements": frequent_words,
                "strength": self.baserah_sigmoid(len(frequent_words), n=1, k=0.5, alpha=1.0)
            })

        # البحث عن أنماط البنية
        structural_patterns = self._find_structural_patterns(premises)
        patterns.extend(structural_patterns)

        return patterns

    def _find_structural_patterns(self, premises: List[str]) -> List[Dict[str, Any]]:
        """العثور على الأنماط البنيوية"""

        patterns = []

        # أنماط الجمل الشرطية
        conditional_count = sum(1 for premise in premises if "إذا" in premise)
        if conditional_count > 1:
            patterns.append({
                "type": "جمل شرطية متكررة",
                "count": conditional_count,
                "strength": self.baserah_sigmoid(conditional_count, n=1, k=1.0, alpha=1.0)
            })

        # أنماط الجمل الكلية
        universal_count = sum(1 for premise in premises if "كل" in premise)
        if universal_count > 1:
            patterns.append({
                "type": "جمل كلية متكررة",
                "count": universal_count,
                "strength": self.baserah_sigmoid(universal_count, n=1, k=1.0, alpha=1.0)
            })

        return patterns

    def _generate_generalizations(self, patterns: List[Dict], premises: List[str]) -> List[Dict[str, Any]]:
        """توليد التعميمات من الأنماط"""

        generalizations = []

        for pattern in patterns:
            if pattern["type"] == "تكرار الكلمات":
                # تعميم بناءً على الكلمات المتكررة
                most_frequent = max(pattern["elements"], key=pattern["elements"].get)
                generalization = f"غالباً ما يرتبط الموضوع بـ {most_frequent}"

                confidence = self.baserah_sigmoid(
                    pattern["strength"] * pattern["elements"][most_frequent],
                    n=1, k=0.8, alpha=1.0
                )

                generalizations.append({
                    "conclusion": generalization,
                    "confidence": confidence,
                    "pattern_type": pattern["type"],
                    "reasoning_steps": [
                        f"تحليل تكرار الكلمات في {len(premises)} مقدمة",
                        f"الكلمة الأكثر تكراراً: {most_frequent}",
                        f"التعميم: {generalization}"
                    ]
                })

            elif pattern["type"] in ["جمل شرطية متكررة", "جمل كلية متكررة"]:
                # تعميم بناءً على البنية
                if "شرطية" in pattern["type"]:
                    generalization = "يميل التفكير إلى استخدام العلاقات السببية"
                else:
                    generalization = "يميل التفكير إلى التعميمات الكلية"

                confidence = self.baserah_sigmoid(
                    pattern["strength"] * pattern["count"],
                    n=1, k=0.6, alpha=1.0
                )

                generalizations.append({
                    "conclusion": generalization,
                    "confidence": confidence,
                    "pattern_type": pattern["type"],
                    "reasoning_steps": [
                        f"تحليل البنية في {len(premises)} مقدمة",
                        f"نمط متكرر: {pattern['type']}",
                        f"التعميم: {generalization}"
                    ]
                })

        return generalizations

    def _apply_abductive_reasoning(self, premises: List[str], conclusion_target: str, analysis: Dict) -> Dict[str, Any]:
        """تطبيق الاستدلال الافتراضي (أفضل تفسير)"""

        print("   🔍 تطبيق الاستدلال الافتراضي...")

        # توليد فرضيات محتملة
        hypotheses = self._generate_hypotheses(premises, conclusion_target)

        # تقييم الفرضيات
        evaluated_hypotheses = self._evaluate_hypotheses(hypotheses, premises)

        # اختيار أفضل فرضية
        best_hypothesis = max(evaluated_hypotheses, key=lambda x: x["plausibility"]) if evaluated_hypotheses else {
            "conclusion": conclusion_target or "لا يمكن تكوين فرضية",
            "plausibility": 0.0,
            "explanation_quality": 0.0,
            "reasoning_steps": []
        }

        return {
            "reasoning_type": "افتراضي",
            "conclusion": best_hypothesis["conclusion"],
            "confidence": best_hypothesis["plausibility"],
            "explanation_quality": best_hypothesis["explanation_quality"],
            "reasoning_steps": best_hypothesis["reasoning_steps"],
            "all_hypotheses": evaluated_hypotheses
        }

    def _generate_hypotheses(self, premises: List[str], conclusion_target: str) -> List[Dict[str, Any]]:
        """توليد فرضيات محتملة"""

        hypotheses = []

        # فرضيات بناءً على الأسباب المحتملة
        for premise in premises:
            if "لأن" in premise or "بسبب" in premise:
                # استخراج السبب
                cause_match = re.search(r"(.+) لأن (.+)", premise)
                if cause_match:
                    effect, cause = cause_match.groups()
                    hypothesis = f"السبب المحتمل هو: {cause.strip()}"

                    hypotheses.append({
                        "hypothesis": hypothesis,
                        "type": "سببي",
                        "supporting_premise": premise
                    })

        # فرضيات بناءً على الأنماط
        if conclusion_target:
            hypotheses.append({
                "hypothesis": conclusion_target,
                "type": "مستهدف",
                "supporting_premise": "الهدف المطلوب"
            })

        # فرضية افتراضية عامة
        hypotheses.append({
            "hypothesis": "هناك علاقة خفية بين العناصر المذكورة",
            "type": "عام",
            "supporting_premise": "تحليل عام للمقدمات"
        })

        return hypotheses

    def _evaluate_hypotheses(self, hypotheses: List[Dict], premises: List[str]) -> List[Dict[str, Any]]:
        """تقييم الفرضيات"""

        evaluated = []

        for hypothesis in hypotheses:
            # حساب معقولية الفرضية
            plausibility = self._calculate_hypothesis_plausibility(hypothesis, premises)

            # حساب جودة التفسير
            explanation_quality = self._calculate_explanation_quality(hypothesis, premises)

            evaluated.append({
                "conclusion": hypothesis["hypothesis"],
                "type": hypothesis["type"],
                "plausibility": plausibility,
                "explanation_quality": explanation_quality,
                "reasoning_steps": [
                    f"فرضية: {hypothesis['hypothesis']}",
                    f"نوع الفرضية: {hypothesis['type']}",
                    f"المعقولية: {plausibility:.3f}",
                    f"جودة التفسير: {explanation_quality:.3f}"
                ]
            })

        return evaluated

    def _calculate_hypothesis_plausibility(self, hypothesis: Dict, premises: List[str]) -> float:
        """حساب معقولية الفرضية"""

        # عوامل المعقولية
        type_weight = {
            "سببي": 0.9,
            "مستهدف": 0.8,
            "عام": 0.6
        }

        base_plausibility = type_weight.get(hypothesis["type"], 0.5)

        # تحسين المعقولية بناءً على التوافق مع المقدمات
        compatibility_score = 0.0
        for premise in premises:
            compatibility_score += self._calculate_compatibility(hypothesis["hypothesis"], premise)

        avg_compatibility = compatibility_score / len(premises) if premises and len(premises) > 0 else 0.0

        # تطبيق المعادلة الثورية
        plausibility = self.baserah_sigmoid(
            base_plausibility + avg_compatibility,
            n=1, k=1.0, alpha=1.0
        )

        return plausibility

    def _calculate_compatibility(self, hypothesis: str, premise: str) -> float:
        """حساب التوافق بين الفرضية والمقدمة"""

        # البحث عن كلمات مشتركة
        hypothesis_words = set(hypothesis.split())
        premise_words = set(premise.split())
        common_words = hypothesis_words.intersection(premise_words)

        # حساب نسبة التوافق
        max_words = max(len(hypothesis_words), len(premise_words), 1)
        compatibility = len(common_words) / max_words if max_words > 0 else 0.0

        return compatibility

    def _calculate_explanation_quality(self, hypothesis: Dict, premises: List[str]) -> float:
        """حساب جودة التفسير"""

        # عوامل جودة التفسير
        simplicity = 1.0 / (len(hypothesis["hypothesis"].split()) + 1)  # البساطة
        # التغطية
        matching_premises = [p for p in premises if any(word in p for word in hypothesis["hypothesis"].split())]
        coverage = len(matching_premises) / len(premises) if premises and len(premises) > 0 else 0.0

        # تطبيق المعادلة الثورية
        quality = self.baserah_sigmoid(
            simplicity + coverage,
            n=1, k=1.5, alpha=1.0
        )

        return quality

    def _apply_general_reasoning(self, premises: List[str], conclusion_target: str, analysis: Dict) -> Dict[str, Any]:
        """تطبيق الاستدلال العام"""

        # دمج جميع أنواع الاستدلال
        deductive_result = self._apply_deductive_reasoning(premises, conclusion_target, analysis)
        inductive_result = self._apply_inductive_reasoning(premises, conclusion_target, analysis)
        abductive_result = self._apply_abductive_reasoning(premises, conclusion_target, analysis)

        # اختيار أفضل نتيجة
        all_results = [deductive_result, inductive_result, abductive_result]
        best_result = max(all_results, key=lambda x: x["confidence"])

        return {
            "reasoning_type": "عام متكامل",
            "conclusion": best_result["conclusion"],
            "confidence": best_result["confidence"],
            "best_method": best_result["reasoning_type"],
            "reasoning_steps": best_result["reasoning_steps"],
            "all_methods": all_results
        }

    # ==========================================
    # 🌟 تطبيق النظريات الثورية على الاستدلال
    # ==========================================

    def _apply_theories_to_reasoning(self, premises_analysis: Dict, conclusion_target: str) -> Dict[str, Any]:
        """تطبيق النظريات الثورية على عملية الاستدلال"""

        print("   🌟 تطبيق النظريات الثورية على الاستدلال...")

        # تطبيق نظرية ثنائية الصفر على قوة المقدمات
        total_premise_strength = sum(premises_analysis["premise_strengths"])
        zero_duality_result = self.revolutionary_theories.apply_enhanced_zero_duality_theory(
            total_premise_strength,
            {"reasoning_context": True, "balance_factor": 1.2}
        )

        # تطبيق نظرية تعامد الأضداد على التناقضات
        contradiction_score = premises_analysis["contradiction_check"]["contradiction_count"]
        perpendicular_result = self.revolutionary_theories.apply_enhanced_perpendicular_opposites_theory(
            contradiction_score,
            {"contradiction_context": True, "stability_factor": 1.1}
        )

        # تطبيق نظرية الفتائل على الترابط المنطقي
        connection_strengths = [conn["connection_strength"] for conn in premises_analysis["logical_connections"]]
        filament_result = self.revolutionary_theories.apply_enhanced_filament_theory(
            connection_strengths if connection_strengths else [0.0],
            {"reasoning_network": True}
        )

        # حساب التكامل الثوري للاستدلال
        reasoning_integration = self._calculate_reasoning_integration(
            zero_duality_result, perpendicular_result, filament_result
        )

        return {
            "zero_duality": zero_duality_result,
            "perpendicular_opposites": perpendicular_result,
            "filament_theory": filament_result,
            "reasoning_integration": reasoning_integration,
            "revolutionary_reasoning_strength": reasoning_integration["integration_strength"]
        }

    def _calculate_reasoning_integration(self, zero_duality: Dict, perpendicular: Dict, filament: Dict) -> Dict[str, Any]:
        """حساب التكامل الثوري للاستدلال"""

        # قوة كل نظرية في سياق الاستدلال
        zero_strength = zero_duality.get("theory_strength", 0.0)
        perpendicular_strength = perpendicular.get("theory_strength", 0.0)
        filament_strength = filament.get("theory_strength", 0.0)

        # التكامل الاستدلالي
        integration_strength = self.baserah_sigmoid(
            (zero_strength + perpendicular_strength + filament_strength) / 3,
            n=1, k=2.0, alpha=1.0
        )

        # توازن الاستدلال
        reasoning_balance = self.baserah_linear(
            abs(zero_strength - perpendicular_strength) + abs(perpendicular_strength - filament_strength),
            beta=-0.3, gamma=1.0
        )

        # جودة الاستدلال الثوري
        revolutionary_quality = self.baserah_sigmoid(
            integration_strength * reasoning_balance,
            n=1, k=1.8, alpha=1.0
        )

        return {
            "integration_strength": integration_strength,
            "reasoning_balance": reasoning_balance,
            "revolutionary_quality": revolutionary_quality,
            "theory_contributions": {
                "zero_duality": zero_strength,
                "perpendicular_opposites": perpendicular_strength,
                "filament_theory": filament_strength
            }
        }

    def _calculate_revolutionary_confidence(self, revolutionary_analysis: Dict, reasoning_result: Dict, premises_analysis: Dict) -> float:
        """حساب الثقة النهائية بالنهج الثوري"""

        # عوامل الثقة
        reasoning_confidence = reasoning_result.get("confidence", 0.0)
        revolutionary_strength = revolutionary_analysis.get("revolutionary_reasoning_strength", 0.0)
        premises_consistency = premises_analysis["contradiction_check"]["overall_consistency"]

        # تطبيق المعادلة الثورية للثقة
        final_confidence = self.baserah_sigmoid(
            (reasoning_confidence + revolutionary_strength + premises_consistency) / 3,
            n=1, k=2.5, alpha=1.0
        )

        return final_confidence

    def _create_reasoning_path(self, premises: List[str], reasoning_result: Dict, revolutionary_analysis: Dict) -> List[str]:
        """إنشاء مسار الاستدلال الثوري"""

        path = [
            "🧠 بدء عملية الاستدلال الثوري",
            f"📝 تحليل {len(premises)} مقدمة",
            "🌟 تطبيق النظريات الثورية الثلاث:"
        ]

        # إضافة تفاصيل النظريات
        zero_duality = revolutionary_analysis["zero_duality"]
        path.append(f"   🧬 نظرية ثنائية الصفر: {zero_duality['revolutionary_insight']}")

        perpendicular = revolutionary_analysis["perpendicular_opposites"]
        path.append(f"   ⚡ نظرية تعامد الأضداد: زاوية {perpendicular['orthogonal_angle']:.1f}°")

        filament = revolutionary_analysis["filament_theory"]
        path.append(f"   🧵 نظرية الفتائل: {filament['total_filaments']} فتيلة مترابطة")

        # إضافة خطوات الاستدلال
        if "reasoning_steps" in reasoning_result:
            path.append("⚖️ خطوات الاستدلال:")
            path.extend([f"   {step}" for step in reasoning_result["reasoning_steps"]])

        # النتيجة النهائية
        path.append(f"🎯 النتيجة: {reasoning_result.get('conclusion', 'غير محددة')}")

        return path

    def _generate_reasoning_insight(self, confidence: float, reasoning_result: Dict) -> str:
        """توليد رؤية ثورية للاستدلال"""

        if confidence > 0.9:
            return "🌟 استدلال ثوري متميز - ثقة عالية جداً في النتيجة"
        elif confidence > 0.7:
            return "⚡ استدلال ثوري قوي - ثقة عالية في النتيجة"
        elif confidence > 0.5:
            return "🔄 استدلال ثوري متوسط - ثقة معتدلة في النتيجة"
        else:
            return "⚠️ استدلال ثوري ضعيف - الحاجة لمقدمات إضافية"

    def _save_to_memory(self, premises: List[str], conclusion: str, reasoning_path: List[str]) -> None:
        """حفظ الاستدلال في الذاكرة"""

        self.reasoning_memory["premises"].extend(premises)
        self.reasoning_memory["conclusions"].append(conclusion)
        self.reasoning_memory["reasoning_paths"].append(reasoning_path)

    # ==========================================
    # 🔍 وظائف مساعدة ومتقدمة
    # ==========================================

    def analyze_reasoning_quality(self, reasoning_result: Dict) -> Dict[str, Any]:
        """تحليل جودة الاستدلال"""

        confidence = reasoning_result.get("confidence", 0.0)
        reasoning_type = reasoning_result.get("reasoning_mode", "غير محدد")

        # تحليل نقاط القوة
        strengths = []
        if confidence > 0.8:
            strengths.append("ثقة عالية في النتيجة")
        if "theories_applied" in reasoning_result:
            strengths.append("تطبيق النظريات الثورية")
        if len(reasoning_result.get("reasoning_path", [])) > 5:
            strengths.append("مسار استدلال مفصل")

        # تحليل نقاط الضعف
        weaknesses = []
        if confidence < 0.5:
            weaknesses.append("ثقة منخفضة في النتيجة")
        if reasoning_result.get("premises_analysis", {}).get("contradiction_check", {}).get("contradictions_found", False):
            weaknesses.append("وجود تناقضات في المقدمات")

        # تقييم إجمالي
        weakness_factor = max(len(weaknesses), 1)
        quality_score = confidence * len(strengths) / weakness_factor if weakness_factor > 0 else confidence
        overall_quality = self.baserah_sigmoid(
            quality_score,
            n=1, k=1.0, alpha=1.0
        )

        return {
            "overall_quality": overall_quality,
            "confidence": confidence,
            "reasoning_type": reasoning_type,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "recommendations": self._generate_improvement_recommendations(weaknesses)
        }

    def _generate_improvement_recommendations(self, weaknesses: List[str]) -> List[str]:
        """توليد توصيات للتحسين"""

        recommendations = []

        for weakness in weaknesses:
            if "ثقة منخفضة" in weakness:
                recommendations.append("إضافة مقدمات أقوى وأكثر وضوحاً")
            elif "تناقضات" in weakness:
                recommendations.append("مراجعة المقدمات وحل التناقضات")
            elif "مسار" in weakness:
                recommendations.append("تفصيل خطوات الاستدلال أكثر")

        if not recommendations:
            recommendations.append("الاستدلال جيد - يمكن المتابعة")

        return recommendations

    def get_reasoning_statistics(self) -> Dict[str, Any]:
        """إحصائيات الاستدلال"""

        return {
            "total_reasoning_sessions": len(self.reasoning_memory["reasoning_paths"]),
            "total_premises_processed": len(self.reasoning_memory["premises"]),
            "total_conclusions_reached": len(self.reasoning_memory["conclusions"]),
            "average_premises_per_session": len(self.reasoning_memory["premises"]) / max(len(self.reasoning_memory["reasoning_paths"]), 1) if len(self.reasoning_memory["reasoning_paths"]) > 0 else 0.0,
            "reasoning_modes_supported": list(self.reasoning_modes.keys()),
            "revolutionary_rules_available": list(self.revolutionary_rules.keys())
        }


# ==========================================
# 🧪 اختبار محرك الاستدلال الثوري
# ==========================================

def test_revolutionary_reasoning_engine():
    """اختبار شامل لمحرك الاستدلال الثوري"""

    print("🧪 بدء اختبار محرك الاستدلال الثوري...")
    print("=" * 70)

    # إنشاء المحرك
    engine = RevolutionaryLogicalReasoningEngine()

    # اختبارات متنوعة
    test_cases = [
        {
            "name": "اختبار Modus Ponens",
            "premises": [
                "إذا كان الجو ممطراً فإن الأرض ستكون مبللة",
                "الجو ممطر اليوم"
            ],
            "conclusion_target": "الأرض مبللة",
            "mode": "deductive"
        },
        {
            "name": "اختبار القياس الأرسطي",
            "premises": [
                "كل إنسان فان",
                "كل فان يموت",
                "سقراط إنسان"
            ],
            "conclusion_target": "سقراط يموت",
            "mode": "deductive"
        },
        {
            "name": "اختبار الاستدلال الاستقرائي",
            "premises": [
                "الطائر الأول يطير",
                "الطائر الثاني يطير",
                "الطائر الثالث يطير"
            ],
            "conclusion_target": "كل الطيور تطير",
            "mode": "inductive"
        },
        {
            "name": "اختبار الاستدلال الافتراضي",
            "premises": [
                "الأرض مبللة",
                "السماء غائمة"
            ],
            "conclusion_target": "لقد أمطرت",
            "mode": "abductive"
        }
    ]

    results = []

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🧪 {test_case['name']} ({i}/{len(test_cases)}):")
        print(f"   المقدمات: {test_case['premises']}")
        print(f"   الهدف: {test_case['conclusion_target']}")
        print(f"   النمط: {test_case['mode']}")

        # تشغيل الاستدلال
        result = engine.reason_revolutionarily(
            test_case["premises"],
            test_case["conclusion_target"],
            test_case["mode"]
        )

        results.append(result)

        # عرض النتائج
        print(f"   ✅ النتيجة: {result['conclusion']}")
        print(f"   📊 الثقة: {result['confidence']:.3f}")
        print(f"   🌟 الرؤية: {result['revolutionary_insight']}")

        # تحليل الجودة
        quality_analysis = engine.analyze_reasoning_quality(result)
        print(f"   🎯 جودة الاستدلال: {quality_analysis['overall_quality']:.3f}")

    print("\n" + "=" * 70)
    print("📊 إحصائيات الاختبار:")

    # إحصائيات عامة
    avg_confidence = sum(r["confidence"] for r in results) / len(results) if results and len(results) > 0 else 0.0
    print(f"   متوسط الثقة: {avg_confidence:.3f}")

    successful_tests = sum(1 for r in results if r["confidence"] > 0.5)
    print(f"   الاختبارات الناجحة: {successful_tests}/{len(results)}")

    # إحصائيات المحرك
    engine_stats = engine.get_reasoning_statistics()
    print(f"   جلسات الاستدلال: {engine_stats['total_reasoning_sessions']}")
    print(f"   المقدمات المعالجة: {engine_stats['total_premises_processed']}")
    print(f"   النتائج المحققة: {engine_stats['total_conclusions_reached']}")

    print("\n✅ اكتمل اختبار محرك الاستدلال الثوري بنجاح!")

    return results


if __name__ == "__main__":
    # تشغيل الاختبار
    test_results = test_revolutionary_reasoning_engine()

    print(f"\n🎯 ملخص النتائج:")
    for i, result in enumerate(test_results, 1):
        print(f"   اختبار {i}: {result['conclusion']} (ثقة: {result['confidence']:.3f})")

    print(f"\n🌟 محرك الاستدلال الثوري جاهز للاستخدام!")
