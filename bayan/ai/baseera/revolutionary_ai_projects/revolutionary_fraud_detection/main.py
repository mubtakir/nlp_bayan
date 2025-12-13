#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🛡️ نظام كشف الاحتيال الثوري
Revolutionary Fraud Detection System

مبني على نظام بصيرة الثوري - بدون تعلم آلة تقليدي
Built on Basera Revolutionary System - No traditional ML

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداعه الشخصي
"""

import numpy as np
import json
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Any
import math
import random

class RevolutionaryFraudDetection:
    """
    🛡️ نظام كشف الاحتيال الثوري
    يستخدم النظريات الثلاث الثورية لكشف الأنماط المشبوهة
    """
    
    def __init__(self, system_name: str = "RevolutionaryFraudDetector"):
        """تهيئة النظام"""
        self.system_name = system_name
        self.normal_patterns = {}
        self.fraud_indicators = {}
        self.behavioral_baselines = {}
        self.detection_history = []
        
        print(f"🛡️ تهيئة {self.system_name}")
        print("🧬 نظام كشف احتيال ثوري بدون تعلم آلة تقليدي")
    
    def establish_baseline(self, user_id: str, transactions: List[Dict]):
        """
        📊 إنشاء خط أساس للسلوك الطبيعي
        باستخدام النظريات الثلاث الثورية
        """
        print(f"📊 إنشاء خط أساس للمستخدم: {user_id}")
        
        # تطبيق النظريات الثلاث على المعاملات
        zero_duality = self.apply_zero_duality_to_transactions(transactions)
        perpendicular = self.apply_perpendicular_opposites_to_transactions(transactions)
        filaments = self.apply_filament_theory_to_transactions(transactions)
        
        # حفظ خط الأساس
        self.behavioral_baselines[user_id] = {
            "zero_duality_baseline": zero_duality,
            "perpendicular_baseline": perpendicular,
            "filament_baseline": filaments,
            "transaction_count": len(transactions),
            "established_at": datetime.now().isoformat()
        }
        
        print(f"✅ تم إنشاء خط أساس من {len(transactions)} معاملة")
    
    def apply_zero_duality_to_transactions(self, transactions: List[Dict]) -> Dict:
        """
        🔄 تطبيق نظرية ثنائية الصفر على المعاملات
        تحليل التوازن بين الإنفاق والادخار
        """
        spending_transactions = []
        saving_transactions = []
        
        for transaction in transactions:
            amount = transaction.get("amount", 0)
            transaction_type = transaction.get("type", "unknown")
            
            if transaction_type in ["purchase", "withdrawal", "payment"]:
                spending_transactions.append(transaction)
            elif transaction_type in ["deposit", "transfer_in", "refund"]:
                saving_transactions.append(transaction)
        
        # حساب التوازن المالي
        total_spending = sum(t.get("amount", 0) for t in spending_transactions)
        total_saving = sum(t.get("amount", 0) for t in saving_transactions)
        
        balance_ratio = total_saving / (total_spending + total_saving) if (total_spending + total_saving) > 0 else 0.5
        
        return {
            "spending_pattern": self._analyze_spending_pattern(spending_transactions),
            "saving_pattern": self._analyze_saving_pattern(saving_transactions),
            "financial_balance": balance_ratio,
            "duality_insight": self._generate_financial_insight(balance_ratio)
        }
    
    def apply_perpendicular_opposites_to_transactions(self, transactions: List[Dict]) -> Dict:
        """
        ⊥ تطبيق نظرية الأضداد المتعامدة على المعاملات
        إنشاء أبعاد جديدة من الأنماط المتضادة
        """
        # تحديد أزواج السلوك المتضاد
        opposite_behaviors = self._identify_opposite_behaviors(transactions)
        
        # إنشاء أبعاد متعامدة
        orthogonal_dimensions = []
        for behavior_pair in opposite_behaviors:
            dimension = self._create_behavioral_dimension(behavior_pair)
            orthogonal_dimensions.append(dimension)
        
        return {
            "opposite_behaviors": opposite_behaviors,
            "behavioral_dimensions": orthogonal_dimensions,
            "complexity_score": len(orthogonal_dimensions) * 0.2
        }
    
    def apply_filament_theory_to_transactions(self, transactions: List[Dict]) -> Dict:
        """
        🧵 تطبيق نظرية الخيوط على المعاملات
        ربط المعاملات بخيوط سلوكية خفية
        """
        transaction_connections = {}
        
        for i, transaction in enumerate(transactions):
            # البحث عن المعاملات المرتبطة
            connected_transactions = self._find_connected_transactions(
                transaction, transactions[i+1:]
            )
            transaction_connections[i] = connected_transactions
        
        # اكتشاف الأنماط السلوكية
        behavioral_patterns = self._discover_behavioral_patterns(transaction_connections)
        
        return {
            "transaction_connections": transaction_connections,
            "behavioral_patterns": behavioral_patterns,
            "connection_density": self._calculate_behavioral_density(transaction_connections)
        }
    
    def detect_fraud(self, user_id: str, new_transaction: Dict) -> Dict:
        """
        🚨 كشف الاحتيال في معاملة جديدة
        """
        print(f"\n🚨 فحص معاملة للمستخدم: {user_id}")
        
        if user_id not in self.behavioral_baselines:
            return {
                "fraud_probability": 0.5,
                "risk_level": "unknown",
                "reason": "لا يوجد خط أساس للمستخدم"
            }
        
        baseline = self.behavioral_baselines[user_id]
        
        # تحليل المعاملة الجديدة
        transaction_analysis = self._analyze_single_transaction(new_transaction)
        
        # حساب الانحراف عن خط الأساس
        deviation_score = self._calculate_baseline_deviation(
            transaction_analysis, baseline
        )
        
        # تطبيق النظريات الثلاث للكشف
        fraud_indicators = self._apply_revolutionary_fraud_detection(
            new_transaction, baseline, deviation_score
        )
        
        # حساب احتمالية الاحتيال
        fraud_probability = self._calculate_fraud_probability(fraud_indicators)
        
        # تحديد مستوى المخاطر
        risk_level = self._determine_risk_level(fraud_probability)
        
        # توليد التفسير
        explanation = self._generate_fraud_explanation(fraud_indicators)
        
        # حفظ نتيجة الكشف
        detection_result = {
            "user_id": user_id,
            "transaction": new_transaction,
            "fraud_probability": fraud_probability,
            "risk_level": risk_level,
            "explanation": explanation,
            "fraud_indicators": fraud_indicators,
            "detected_at": datetime.now().isoformat()
        }
        
        self.detection_history.append(detection_result)
        
        return detection_result
    
    def _analyze_spending_pattern(self, spending_transactions: List[Dict]) -> Dict:
        """تحليل نمط الإنفاق"""
        if not spending_transactions:
            return {"average_amount": 0, "frequency": 0, "variance": 0}
        
        amounts = [t.get("amount", 0) for t in spending_transactions]
        
        return {
            "average_amount": np.mean(amounts),
            "frequency": len(spending_transactions),
            "variance": np.var(amounts),
            "max_amount": max(amounts),
            "min_amount": min(amounts)
        }
    
    def _analyze_saving_pattern(self, saving_transactions: List[Dict]) -> Dict:
        """تحليل نمط الادخار"""
        if not saving_transactions:
            return {"average_amount": 0, "frequency": 0, "variance": 0}
        
        amounts = [t.get("amount", 0) for t in saving_transactions]
        
        return {
            "average_amount": np.mean(amounts),
            "frequency": len(saving_transactions),
            "variance": np.var(amounts),
            "max_amount": max(amounts),
            "min_amount": min(amounts)
        }
    
    def _generate_financial_insight(self, balance_ratio: float) -> str:
        """توليد رؤية مالية"""
        if balance_ratio > 0.7:
            return "مدخر - يميل للادخار أكثر من الإنفاق"
        elif balance_ratio < 0.3:
            return "منفق - يميل للإنفاق أكثر من الادخار"
        else:
            return "متوازن - توازن بين الإنفاق والادخار"
    
    def _identify_opposite_behaviors(self, transactions: List[Dict]) -> List[Tuple]:
        """تحديد السلوكيات المتضادة"""
        behaviors = []
        
        # تجميع المعاملات حسب النوع
        by_type = {}
        for transaction in transactions:
            t_type = transaction.get("type", "unknown")
            if t_type not in by_type:
                by_type[t_type] = []
            by_type[t_type].append(transaction)
        
        # البحث عن الأضداد
        types = list(by_type.keys())
        for i in range(len(types)):
            for j in range(i+1, len(types)):
                type1, type2 = types[i], types[j]
                
                # تحديد إذا كانا متضادين
                if self._are_opposite_behaviors(type1, type2):
                    behaviors.append((type1, type2))
        
        return behaviors
    
    def _are_opposite_behaviors(self, behavior1: str, behavior2: str) -> bool:
        """تحديد إذا كان السلوكان متضادين"""
        opposite_pairs = [
            ("purchase", "refund"),
            ("withdrawal", "deposit"),
            ("payment", "transfer_in"),
            ("spending", "saving")
        ]
        
        for pair in opposite_pairs:
            if (behavior1 in pair and behavior2 in pair):
                return True
        
        return False
    
    def _create_behavioral_dimension(self, behavior_pair: Tuple) -> Dict:
        """إنشاء بُعد سلوكي من زوج أضداد"""
        behavior1, behavior2 = behavior_pair
        
        dimension = {
            "axis_name": f"{behavior1}_vs_{behavior2}",
            "behavioral_tension": self._calculate_behavioral_tension(behavior1, behavior2),
            "resolution_strategy": "balanced_monitoring"
        }
        
        return dimension
    
    def _calculate_behavioral_tension(self, behavior1: str, behavior2: str) -> float:
        """حساب التوتر السلوكي"""
        # خوارزمية بسيطة لحساب التوتر
        hash1 = hash(behavior1) % 100
        hash2 = hash(behavior2) % 100
        
        tension = abs(hash1 - hash2) / 100
        return tension
    
    def _find_connected_transactions(self, transaction: Dict, other_transactions: List[Dict]) -> List[int]:
        """البحث عن المعاملات المرتبطة"""
        connections = []
        
        t_amount = transaction.get("amount", 0)
        t_type = transaction.get("type", "")
        t_time = transaction.get("timestamp", "")
        
        for i, other_t in enumerate(other_transactions):
            # حساب قوة الاتصال
            connection_strength = self._calculate_transaction_connection(
                transaction, other_t
            )
            
            if connection_strength > 0.6:
                connections.append(i)
        
        return connections
    
    def _calculate_transaction_connection(self, t1: Dict, t2: Dict) -> float:
        """حساب قوة الاتصال بين معاملتين"""
        # التشابه في المبلغ
        amount1 = t1.get("amount", 0)
        amount2 = t2.get("amount", 0)
        amount_similarity = 1.0 - abs(amount1 - amount2) / max(amount1, amount2, 1)
        
        # التشابه في النوع
        type1 = t1.get("type", "")
        type2 = t2.get("type", "")
        type_similarity = 1.0 if type1 == type2 else 0.0
        
        # قوة الاتصال الإجمالية
        connection_strength = (amount_similarity + type_similarity) / 2
        
        return connection_strength
    
    def _discover_behavioral_patterns(self, connections: Dict) -> List[str]:
        """اكتشاف الأنماط السلوكية"""
        patterns = []
        
        # البحث عن أنماط التكرار
        for transaction_id, connected_ids in connections.items():
            if len(connected_ids) >= 2:
                patterns.append(f"نمط متكرر: معاملة {transaction_id} مرتبطة بـ {len(connected_ids)} معاملات")
        
        return patterns
    
    def _calculate_behavioral_density(self, connections: Dict) -> float:
        """حساب كثافة السلوك"""
        total_connections = sum(len(conns) for conns in connections.values())
        total_transactions = len(connections)
        
        if total_transactions == 0:
            return 0.0
        
        return total_connections / total_transactions
    
    def _analyze_single_transaction(self, transaction: Dict) -> Dict:
        """تحليل معاملة واحدة"""
        return {
            "amount": transaction.get("amount", 0),
            "type": transaction.get("type", "unknown"),
            "timestamp": transaction.get("timestamp", ""),
            "location": transaction.get("location", "unknown"),
            "merchant": transaction.get("merchant", "unknown")
        }
    
    def _calculate_baseline_deviation(self, transaction_analysis: Dict, baseline: Dict) -> float:
        """حساب الانحراف عن خط الأساس"""
        # انحراف المبلغ
        baseline_avg = baseline["zero_duality_baseline"]["spending_pattern"]["average_amount"]
        transaction_amount = transaction_analysis["amount"]
        
        if baseline_avg > 0:
            amount_deviation = abs(transaction_amount - baseline_avg) / baseline_avg
        else:
            amount_deviation = 1.0 if transaction_amount > 0 else 0.0
        
        # انحراف التعقيد
        baseline_complexity = baseline["perpendicular_baseline"]["complexity_score"]
        complexity_deviation = abs(0.2 - baseline_complexity)  # افتراض تعقيد متوسط للمعاملة الجديدة
        
        # الانحراف الإجمالي
        total_deviation = (amount_deviation + complexity_deviation) / 2
        
        return min(total_deviation, 1.0)
    
    def _apply_revolutionary_fraud_detection(self, transaction: Dict, baseline: Dict, deviation: float) -> Dict:
        """تطبيق الكشف الثوري للاحتيال"""
        indicators = {}
        
        # مؤشر ثنائية الصفر
        indicators["duality_anomaly"] = self._detect_duality_anomaly(transaction, baseline)
        
        # مؤشر الأضداد المتعامدة
        indicators["perpendicular_anomaly"] = self._detect_perpendicular_anomaly(transaction, baseline)
        
        # مؤشر الخيوط
        indicators["filament_anomaly"] = self._detect_filament_anomaly(transaction, baseline)
        
        # مؤشر الانحراف العام
        indicators["baseline_deviation"] = deviation
        
        return indicators
    
    def _detect_duality_anomaly(self, transaction: Dict, baseline: Dict) -> float:
        """كشف شذوذ ثنائية الصفر"""
        transaction_amount = transaction.get("amount", 0)
        baseline_avg = baseline["zero_duality_baseline"]["spending_pattern"]["average_amount"]
        
        if baseline_avg > 0:
            anomaly_score = abs(transaction_amount - baseline_avg) / baseline_avg
        else:
            anomaly_score = 1.0 if transaction_amount > 100 else 0.0
        
        return min(anomaly_score, 1.0)
    
    def _detect_perpendicular_anomaly(self, transaction: Dict, baseline: Dict) -> float:
        """كشف شذوذ الأضداد المتعامدة"""
        # تحليل بسيط للشذوذ في النوع
        transaction_type = transaction.get("type", "unknown")
        baseline_behaviors = baseline["perpendicular_baseline"]["opposite_behaviors"]
        
        # إذا كان النوع غير مألوف، فهو شاذ
        known_types = set()
        for behavior_pair in baseline_behaviors:
            known_types.update(behavior_pair)
        
        if transaction_type not in known_types:
            return 0.8  # نوع غير مألوف
        else:
            return 0.1  # نوع مألوف
    
    def _detect_filament_anomaly(self, transaction: Dict, baseline: Dict) -> float:
        """كشف شذوذ الخيوط"""
        # تحليل بسيط للشذوذ في الاتصالات
        baseline_density = baseline["filament_baseline"]["connection_density"]
        
        # إذا كانت المعاملة معزولة (لا اتصالات)، فقد تكون شاذة
        if baseline_density > 0.5:
            return 0.6  # المستخدم عادة لديه معاملات مترابطة
        else:
            return 0.2  # المستخدم عادة لديه معاملات منفصلة
    
    def _calculate_fraud_probability(self, indicators: Dict) -> float:
        """حساب احتمالية الاحتيال"""
        weights = {
            "duality_anomaly": 0.3,
            "perpendicular_anomaly": 0.25,
            "filament_anomaly": 0.25,
            "baseline_deviation": 0.2
        }
        
        fraud_probability = sum(
            indicators[key] * weights[key] 
            for key in weights.keys()
        )
        
        return min(fraud_probability, 1.0)
    
    def _determine_risk_level(self, fraud_probability: float) -> str:
        """تحديد مستوى المخاطر"""
        if fraud_probability >= 0.8:
            return "عالي جداً"
        elif fraud_probability >= 0.6:
            return "عالي"
        elif fraud_probability >= 0.4:
            return "متوسط"
        elif fraud_probability >= 0.2:
            return "منخفض"
        else:
            return "آمن"
    
    def _generate_fraud_explanation(self, indicators: Dict) -> str:
        """توليد تفسير للاحتيال"""
        explanations = []
        
        if indicators["duality_anomaly"] > 0.5:
            explanations.append("انحراف في نمط الإنفاق")
        
        if indicators["perpendicular_anomaly"] > 0.5:
            explanations.append("سلوك غير مألوف")
        
        if indicators["filament_anomaly"] > 0.5:
            explanations.append("معاملة معزولة")
        
        if indicators["baseline_deviation"] > 0.5:
            explanations.append("انحراف عن السلوك المعتاد")
        
        if not explanations:
            return "المعاملة تبدو طبيعية"
        
        return "، ".join(explanations)

def main():
    """مثال على الاستخدام"""
    print("🛡️ نظام كشف الاحتيال الثوري - مثال تطبيقي")
    print("=" * 60)
    
    # إنشاء نظام كشف الاحتيال
    fraud_detector = RevolutionaryFraudDetection("BankFraudDetector")
    
    # معاملات طبيعية لإنشاء خط الأساس
    normal_transactions = [
        {"amount": 50, "type": "purchase", "timestamp": "2025-01-01", "merchant": "grocery"},
        {"amount": 100, "type": "withdrawal", "timestamp": "2025-01-02", "location": "atm_1"},
        {"amount": 30, "type": "purchase", "timestamp": "2025-01-03", "merchant": "cafe"},
        {"amount": 200, "type": "deposit", "timestamp": "2025-01-04", "location": "bank"},
        {"amount": 75, "type": "purchase", "timestamp": "2025-01-05", "merchant": "pharmacy"}
    ]
    
    # إنشاء خط أساس للمستخدم
    fraud_detector.establish_baseline("user_123", normal_transactions)
    
    # معاملات للاختبار
    test_transactions = [
        {"amount": 60, "type": "purchase", "timestamp": "2025-01-06", "merchant": "grocery"},  # طبيعية
        {"amount": 5000, "type": "withdrawal", "timestamp": "2025-01-07", "location": "atm_unknown"},  # مشبوهة
        {"amount": 25, "type": "purchase", "timestamp": "2025-01-08", "merchant": "cafe"},  # طبيعية
        {"amount": 1000, "type": "transfer", "timestamp": "2025-01-09", "location": "online"}  # مشبوهة
    ]
    
    # اختبار كشف الاحتيال
    for i, transaction in enumerate(test_transactions, 1):
        result = fraud_detector.detect_fraud("user_123", transaction)
        
        print(f"\n🔍 اختبار المعاملة {i}:")
        print(f"   💰 المبلغ: {transaction['amount']}")
        print(f"   📝 النوع: {transaction['type']}")
        print(f"   🚨 احتمالية الاحتيال: {result['fraud_probability']:.3f}")
        print(f"   ⚠️ مستوى المخاطر: {result['risk_level']}")
        print(f"   💡 التفسير: {result['explanation']}")
        
        if result['fraud_probability'] > 0.6:
            print("   🚨 تحذير: معاملة مشبوهة!")
        else:
            print("   ✅ معاملة آمنة")
    
    print("\n✅ تم إنجاز اختبار كشف الاحتيال بنجاح!")

if __name__ == "__main__":
    main()
