#!/usr/bin/env python3
"""
محرك الدلالات البصرية - Visual Semantic Engine
==============================================

🧬 يطبق نظريات بصيرة على سيميائية الحروف في بيان:
   - ثنائية الصفر: كل حرف له ضد
   - تعامد الأضداد: الأضداد تتعامد في الفضاء الدلالي
   - نظرية الخيوط: الحروف مرتبطة بخيوط معنوية

المطور: باسل يحيى عبدالله
"""

import sys
import os
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from extensions.bayan_baserah_bridge import (
    BayanBaserahBridge, LetterShapeType, 
    LETTER_SHAPE_EQUATIONS, SHAPE_MEANING_BRIDGE
)

# استيراد من بيان
try:
    from bayan.bayan.letter_semiotics.inference_engine import ARABIC_SHAPE_MEANINGS
    BAYAN_AVAILABLE = True
except ImportError:
    BAYAN_AVAILABLE = False
    ARABIC_SHAPE_MEANINGS = {}


@dataclass
class SemanticVector:
    """متجه دلالي للحرف في الفضاء المعنوي"""
    letter: str
    x: float = 0.0  # البعد الأفقي (مادي ← نفسي)
    y: float = 0.0  # البعد العمودي (سلبي ← إيجابي)
    z: float = 0.0  # البعد العمقي (سطحي ← عميق)
    magnitude: float = 0.0
    meanings: List[str] = field(default_factory=list)


class VisualSemanticEngine:
    """
    محرك الدلالات البصرية
    
    🧬 يطبق النظريات الثلاث من بصيرة:
       1. ثنائية الصفر - انبثاق الأضداد
       2. تعامد الأضداد - 90° في الفضاء
       3. الخيوط - الروابط المعنوية
    """
    
    def __init__(self):
        self.bridge = BayanBaserahBridge()
        self.semantic_space: Dict[str, SemanticVector] = {}
        self._build_semantic_space()
        print("🧬 محرك الدلالات البصرية: تم التهيئة")
    
    def _build_semantic_space(self):
        """بناء الفضاء الدلالي للحروف"""
        # تحديد موقع كل حرف في الفضاء ثلاثي الأبعاد
        letter_positions = {
            # الحروف الحلقية (عميقة، نفسية)
            "ا": (0.0, 0.9, 0.9), "ه": (0.1, 0.5, 0.8), "ع": (0.2, 0.7, 0.9),
            "ح": (-0.1, 0.6, 0.7), "غ": (0.3, 0.4, 0.8), "خ": (-0.2, 0.3, 0.7),
            
            # الحروف الشفهية (سطحية، مادية)
            "ب": (-0.8, 0.5, 0.1), "م": (-0.7, 0.8, 0.2), "و": (-0.6, 0.4, 0.1),
            "ف": (-0.9, 0.3, 0.2),
            
            # الحروف اللسانية (متوسطة)
            "ت": (-0.4, 0.4, 0.4), "ث": (-0.3, 0.3, 0.4), "د": (-0.5, 0.5, 0.5),
            "ذ": (-0.4, 0.4, 0.5), "ر": (-0.3, 0.6, 0.4), "ز": (-0.2, 0.5, 0.4),
            "س": (-0.5, 0.4, 0.5), "ش": (-0.4, 0.5, 0.5), "ص": (-0.6, 0.6, 0.6),
            "ض": (-0.5, 0.5, 0.6), "ط": (-0.6, 0.7, 0.6), "ظ": (-0.5, 0.6, 0.6),
            "ل": (-0.2, 0.7, 0.3), "ن": (-0.3, 0.6, 0.3),
            
            # الحروف الحنجرية
            "ق": (0.5, 0.5, 0.7), "ك": (0.4, 0.6, 0.6),
            
            # حروف أخرى
            "ج": (0.3, 0.5, 0.6), "ي": (-0.1, 0.5, 0.3),
        }
        
        for letter, (x, y, z) in letter_positions.items():
            meanings = ARABIC_SHAPE_MEANINGS.get(letter, {}).get("meanings", [])
            magnitude = math.sqrt(x**2 + y**2 + z**2)
            
            self.semantic_space[letter] = SemanticVector(
                letter=letter, x=x, y=y, z=z,
                magnitude=magnitude, meanings=meanings
            )
    
    def apply_zero_duality(self, letter: str) -> Dict[str, Any]:
        """
        تطبيق نظرية ثنائية الصفر
        
        🎯 الحرف ينبثق من الصفر مع ضده
        Σ(+) + Σ(-) = 0
        """
        if letter not in self.semantic_space:
            return {"error": f"الحرف '{letter}' غير موجود في الفضاء الدلالي"}
        
        vec = self.semantic_space[letter]
        
        # إيجاد النقطة المقابلة (الضد)
        opposite_vec = SemanticVector(
            letter=f"ضد_{letter}",
            x=-vec.x, y=-vec.y, z=-vec.z,
            magnitude=vec.magnitude
        )
        
        # التحقق من التوازن الكوني
        balance = (vec.x + opposite_vec.x, vec.y + opposite_vec.y, vec.z + opposite_vec.z)
        
        # البحث عن أقرب حرف للضد
        closest_opposite = self._find_closest_letter(opposite_vec)
        
        return {
            "letter": letter,
            "position": (vec.x, vec.y, vec.z),
            "opposite_position": (opposite_vec.x, opposite_vec.y, opposite_vec.z),
            "balance": balance,
            "balance_sum": sum(balance),
            "closest_opposite_letter": closest_opposite,
            "theory": "ثنائية الصفر: كل شيء ينبثق من الصفر إلى ضدين متوازنين"
        }
    
    def _find_closest_letter(self, target: SemanticVector) -> str:
        """إيجاد أقرب حرف للموقع المحدد"""
        min_distance = float('inf')
        closest = ""
        
        for letter, vec in self.semantic_space.items():
            distance = math.sqrt(
                (vec.x - target.x)**2 + 
                (vec.y - target.y)**2 + 
                (vec.z - target.z)**2
            )
            if distance < min_distance:
                min_distance = distance
                closest = letter
        
        return closest
    
    def apply_perpendicularity(self, letter1: str, letter2: str) -> Dict[str, Any]:
        """
        تطبيق نظرية تعامد الأضداد
        
        🎯 الأضداد تتعامد (90°) لمنع الفناء المتبادل
        A ⊥ B ⟺ A·B = 0
        """
        if letter1 not in self.semantic_space or letter2 not in self.semantic_space:
            return {"error": "أحد الحرفين غير موجود"}
        
        vec1 = self.semantic_space[letter1]
        vec2 = self.semantic_space[letter2]
        
        # حساب الضرب النقطي (dot product)
        dot_product = vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z
        
        # حساب الزاوية بين المتجهين
        mag1 = vec1.magnitude if vec1.magnitude > 0 else 1
        mag2 = vec2.magnitude if vec2.magnitude > 0 else 1
        cos_angle = dot_product / (mag1 * mag2)
        cos_angle = max(-1, min(1, cos_angle))  # clamp
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)
        
        # هل هما متعامدان؟
        is_perpendicular = 80 <= angle_deg <= 100
        
        return {
            "letter1": letter1,
            "letter2": letter2,
            "dot_product": round(dot_product, 4),
            "angle_degrees": round(angle_deg, 2),
            "is_perpendicular": is_perpendicular,
            "relationship": "متعامدان (أضداد)" if is_perpendicular else "غير متعامدين",
            "theory": "تعامد الأضداد: الأضداد تتعامد بزاوية 90°"
        }

    def apply_filament_theory(self, word: str) -> Dict[str, Any]:
        """
        تطبيق نظرية الخيوط

        🎯 الحروف مرتبطة بخيوط معنوية غير مرئية
        System = Σ(Filaments) + Connections + Evolution
        """
        if not word:
            return {"error": "الكلمة فارغة"}

        letters = [l for l in word if l in self.semantic_space]
        if not letters:
            return {"error": "لا توجد حروف معروفة في الكلمة"}

        # بناء الخيوط بين الحروف المتتالية
        filaments = []
        total_tension = 0.0

        for i in range(len(letters) - 1):
            vec1 = self.semantic_space[letters[i]]
            vec2 = self.semantic_space[letters[i + 1]]

            # حساب طول الخيط (المسافة)
            distance = math.sqrt(
                (vec2.x - vec1.x)**2 +
                (vec2.y - vec1.y)**2 +
                (vec2.z - vec1.z)**2
            )

            # حساب التوتر (كلما زادت المسافة زاد التوتر)
            tension = distance
            total_tension += tension

            filaments.append({
                "from": letters[i],
                "to": letters[i + 1],
                "length": round(distance, 3),
                "tension": round(tension, 3)
            })

        # حساب التماسك الكلي (عكسي مع التوتر)
        cohesion = 1.0 / (1.0 + total_tension) if total_tension > 0 else 1.0

        return {
            "word": word,
            "letters": letters,
            "filaments": filaments,
            "total_tension": round(total_tension, 3),
            "cohesion": round(cohesion, 3),
            "interpretation": self._interpret_cohesion(cohesion),
            "theory": "نظرية الخيوط: الكيانات مرتبطة بخيوط غير مرئية"
        }

    def _interpret_cohesion(self, cohesion: float) -> str:
        """تفسير مستوى التماسك"""
        if cohesion > 0.7:
            return "تماسك عالي - الحروف متقاربة معنوياً"
        elif cohesion > 0.4:
            return "تماسك متوسط - توازن معنوي"
        else:
            return "تماسك منخفض - تباين معنوي (قد يكون مقصوداً)"

    def visualize_word_in_space(self, word: str) -> Dict[str, Any]:
        """
        تصور الكلمة في الفضاء الدلالي ثلاثي الأبعاد
        """
        letters = [l for l in word if l in self.semantic_space]

        points = []
        for letter in letters:
            vec = self.semantic_space[letter]
            points.append({
                "letter": letter,
                "x": vec.x,
                "y": vec.y,
                "z": vec.z,
                "meanings": vec.meanings[:2]
            })

        # حساب مركز الثقل
        if points:
            center_x = sum(p["x"] for p in points) / len(points)
            center_y = sum(p["y"] for p in points) / len(points)
            center_z = sum(p["z"] for p in points) / len(points)
        else:
            center_x = center_y = center_z = 0

        return {
            "word": word,
            "points": points,
            "center_of_gravity": {
                "x": round(center_x, 3),
                "y": round(center_y, 3),
                "z": round(center_z, 3)
            },
            "interpretation": self._interpret_center(center_x, center_y, center_z)
        }

    def _interpret_center(self, x: float, y: float, z: float) -> str:
        """تفسير مركز الثقل"""
        parts = []

        if x < -0.3:
            parts.append("مادي/شفهي")
        elif x > 0.3:
            parts.append("نفسي/حلقي")
        else:
            parts.append("متوازن")

        if y > 0.5:
            parts.append("إيجابي")
        elif y < 0.3:
            parts.append("محايد/سلبي")

        if z > 0.5:
            parts.append("عميق")
        else:
            parts.append("سطحي")

        return " - ".join(parts)

    def full_analysis(self, word: str) -> Dict[str, Any]:
        """
        تحليل شامل للكلمة باستخدام النظريات الثلاث
        """
        # تحليل الجسر الأساسي
        bridge_analysis = self.bridge.word_visual_analysis(word)

        # تطبيق نظرية الخيوط
        filament_analysis = self.apply_filament_theory(word)

        # تصور في الفضاء
        space_analysis = self.visualize_word_in_space(word)

        # تحليل ثنائية الصفر لكل حرف
        duality_results = []
        for letter in word:
            if letter in self.semantic_space:
                result = self.apply_zero_duality(letter)
                if "error" not in result:
                    duality_results.append({
                        "letter": letter,
                        "opposite": result["closest_opposite_letter"]
                    })

        return {
            "word": word,
            "visual_analysis": {
                "meanings": bridge_analysis.get("combined_meanings", [])[:5],
                "harmony": bridge_analysis.get("visual_harmony", 0)
            },
            "filament_theory": {
                "cohesion": filament_analysis.get("cohesion", 0),
                "interpretation": filament_analysis.get("interpretation", "")
            },
            "space_position": space_analysis.get("center_of_gravity", {}),
            "space_interpretation": space_analysis.get("interpretation", ""),
            "dualities": duality_results,
            "summary": self._generate_summary(bridge_analysis, filament_analysis, space_analysis)
        }

    def _generate_summary(self, bridge: Dict, filament: Dict, space: Dict) -> str:
        """توليد ملخص التحليل"""
        parts = []

        harmony = bridge.get("visual_harmony", 0)
        if harmony > 0.7:
            parts.append("تناغم بصري عالي")

        cohesion = filament.get("cohesion", 0)
        if cohesion > 0.5:
            parts.append("تماسك معنوي قوي")

        interpretation = space.get("interpretation", "")
        if interpretation:
            parts.append(interpretation)

        return " | ".join(parts) if parts else "تحليل متوازن"


# للاختبار
if __name__ == "__main__":
    engine = VisualSemanticEngine()

    print("\n" + "=" * 60)
    print("🧬 اختبار محرك الدلالات البصرية")
    print("=" * 60)

    # اختبار ثنائية الصفر
    print("\n⚡ نظرية ثنائية الصفر - حرف 'ع':")
    result = engine.apply_zero_duality("ع")
    print(f"   الموقع: {result['position']}")
    print(f"   الضد: {result['closest_opposite_letter']}")
    print(f"   التوازن: {result['balance_sum']}")

    # اختبار التعامد
    print("\n📐 نظرية تعامد الأضداد - 'ا' و 'ب':")
    result = engine.apply_perpendicularity("ا", "ب")
    print(f"   الزاوية: {result['angle_degrees']}°")
    print(f"   العلاقة: {result['relationship']}")

    # اختبار الخيوط
    print("\n🧵 نظرية الخيوط - كلمة 'بيان':")
    result = engine.apply_filament_theory("بيان")
    print(f"   التماسك: {result['cohesion']}")
    print(f"   التفسير: {result['interpretation']}")

    # تحليل شامل
    print("\n📊 تحليل شامل - كلمة 'عقل':")
    result = engine.full_analysis("عقل")
    print(f"   المعاني: {result['visual_analysis']['meanings']}")
    print(f"   التماسك: {result['filament_theory']['cohesion']}")
    print(f"   الموقع: {result['space_interpretation']}")
    print(f"   الملخص: {result['summary']}")

    print("\n" + "=" * 60)
    print("✅ اكتمل الاختبار!")
    print("=" * 60)

