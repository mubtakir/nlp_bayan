"""
تكامل عقل بيان - Bayan Brain Integration
==========================================

الطبقة الرئيسية التي تدمج الفصين وتنسق بينهما.

المؤلف: باسل يحيى عبدالله
"""

from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
import numpy as np

# استيراد الفص المنطقي (سيميائية الحروف)
from ..letter_semiotics import (
    ArabicLetterDatabase,
    WordAnalyzer,
    WordGenerator,
    LetterAnalyzer,
    generate_word_from_meaning
)

from ..letter_semiotics.inference_engine import (
    MeaningInferenceEngine,
    ShapeInferenceEngine,
    SoundInferenceEngine,
    LexicalInferenceEngine,
    LetterNameInferenceEngine
)

# استيراد الفص الرياضي (بصيرة)
from ..baserah_ai import (
    AdaptiveEquation, AdaptationType,
    RevolutionaryLeadership,
    DrawingUnit, InferenceUnit, ShapeGenerator,
    GeneralizedSigmoid, SigmoidParameters,
    create_baserah_system
)

from ..baserah_ai.advanced import (
    ThinkingCore, LayerType,
    ConsciousnessSystem, AttentionLevel
)


class BrainHemisphere(Enum):
    """فصا الدماغ"""
    LOGICAL = "منطقي"      # الفص المنطقي/اللغوي
    MATHEMATICAL = "رياضي"  # الفص الرياضي


@dataclass
class ThoughtProcess:
    """عملية تفكير"""
    input_data: Any
    hemisphere: BrainHemisphere
    logical_result: Optional[Dict] = None
    mathematical_result: Optional[Dict] = None
    integrated_result: Optional[Dict] = None
    confidence: float = 0.0
    insights: List[str] = field(default_factory=list)


@dataclass
class BrainState:
    """حالة العقل"""
    active_hemisphere: BrainHemisphere = BrainHemisphere.LOGICAL
    cognitive_load: float = 0.0
    focus_target: Optional[str] = None
    processing: bool = False


class BayanBrain:
    """
    عقل بيان الموحد

    يدمج الفص المنطقي (سيميائية الحروف) مع الفص الرياضي (بصيرة)
    لتحقيق فهم عميق ومتكامل للغة والمفاهيم.
    """

    def __init__(self, name: str = "عقل_بيان"):
        self.name = name
        self.state = BrainState()

        # الفص المنطقي
        self.letter_db = ArabicLetterDatabase()
        self.word_analyzer = WordAnalyzer(use_camel=False)
        self.word_generator = WordGenerator()
        self.letter_analyzer = LetterAnalyzer()
        self.inference_engines = {
            "شكلي": ShapeInferenceEngine(),
            "صوتي": SoundInferenceEngine(),
            "معجمي": LexicalInferenceEngine(),
            "اسمي": LetterNameInferenceEngine()
        }

        # الفص الرياضي
        self.baserah = create_baserah_system(name)
        self.thinking_core = ThinkingCore()
        self.consciousness = ConsciousnessSystem()
        self.leadership = RevolutionaryLeadership()

        # تاريخ العمليات
        self.thought_history: List[ThoughtProcess] = []
    
    def think(self, input_data: Any, use_both: bool = True) -> ThoughtProcess:
        """
        التفكير في مدخل معين باستخدام الفصين
        """
        self.state.processing = True
        process = ThoughtProcess(input_data=input_data, hemisphere=self.state.active_hemisphere)
        
        # التركيز على المدخل
        self.consciousness.focus_on(str(input_data), 1.0)
        
        # المعالجة اللغوية (الفص المنطقي)
        if use_both or self.state.active_hemisphere == BrainHemisphere.LOGICAL:
            process.logical_result = self._logical_process(input_data)
            process.insights.append("تحليل لغوي مكتمل")
        
        # المعالجة الرياضية (الفص الرياضي)
        if use_both or self.state.active_hemisphere == BrainHemisphere.MATHEMATICAL:
            process.mathematical_result = self._mathematical_process(input_data)
            process.insights.append("تحليل رياضي مكتمل")
        
        # دمج النتائج
        if process.logical_result and process.mathematical_result:
            process.integrated_result = self._integrate_results(
                process.logical_result,
                process.mathematical_result
            )
            process.confidence = 0.9
        else:
            process.confidence = 0.6
        
        self.thought_history.append(process)
        self.state.processing = False
        
        return process
    
    def _logical_process(self, data: Any) -> Dict:
        """المعالجة في الفص المنطقي"""
        result = {"النوع": "تحليل_لغوي"}

        if isinstance(data, str):
            # تحليل الكلمة
            try:
                word_analysis = self.word_analyzer.analyze_word(data)
                result["تحليل_الكلمة"] = {
                    "الكلمة": data,
                    "المعنى": word_analysis.combined_meaning if word_analysis else None,
                    "الجذر": word_analysis.root_analysis.root if word_analysis and word_analysis.root_analysis else None
                }
            except:
                result["تحليل_الكلمة"] = {"الكلمة": data}

            # تحليل الحروف
            letters_info = []
            for char in data:
                if char.strip():
                    try:
                        info = self.letter_db.get_letter(char)
                        if info:
                            letters_info.append({
                                "الحرف": char,
                                "المعاني": info.meanings[:3] if hasattr(info, 'meanings') else []
                            })
                    except:
                        pass
            result["الحروف"] = letters_info

            # استنباط المعاني
            inferences = {}
            for name, engine in self.inference_engines.items():
                try:
                    inf = engine.infer(data)
                    if inf:
                        inferences[name] = [{"المعنى": m.meaning, "الثقة": m.confidence}
                                           for m in inf[:3]]
                except:
                    pass
            result["الاستنباطات"] = inferences

        return result

    def _mathematical_process(self, data: Any) -> Dict:
        """المعالجة في الفص الرياضي"""
        result = {"النوع": "تحليل_رياضي"}

        # المعالجة عبر طبقات التفكير
        layer_results = self.thinking_core.process(data)
        result["طبقات_التفكير"] = {
            lt.value: {
                "المخرج": str(lr.output)[:100],
                "الرؤى": lr.insights
            }
            for lt, lr in layer_results.items()
        }

        # تطبيق النظريات الثورية
        if isinstance(data, (int, float)):
            zero_result = self.leadership.apply_zero_duality(data)
            result["ثنائية_الصفر"] = zero_result.output
        elif isinstance(data, str) and len(data) > 1:
            # تحويل الكلمة إلى قيم رقمية
            numeric_values = [ord(c) for c in data]
            result["القيم_الرقمية"] = numeric_values[:10]
            result["المجموع"] = sum(numeric_values)
            result["المتوسط"] = np.mean(numeric_values)

        return result

    def _integrate_results(self, logical: Dict, mathematical: Dict) -> Dict:
        """دمج نتائج الفصين"""
        integrated = {
            "النوع": "تحليل_متكامل",
            "التحليل_اللغوي": logical,
            "التحليل_الرياضي": mathematical
        }

        # استخراج الرؤى المشتركة
        insights = []

        if "تحليل_الكلمة" in logical:
            insights.append(f"كلمة ذات {len(logical.get('الحروف', []))} حرف")

        if "المجموع" in mathematical:
            insights.append(f"القيمة العددية: {mathematical['المجموع']}")

        integrated["الرؤى_المتكاملة"] = insights

        return integrated

    def analyze_word_deeply(self, word: str) -> Dict:
        """تحليل عميق لكلمة باستخدام الفصين"""
        process = self.think(word, use_both=True)

        result = {
            "الكلمة": word,
            "التحليل_اللغوي": process.logical_result,
            "التحليل_الرياضي": process.mathematical_result,
            "التكامل": process.integrated_result,
            "الثقة": process.confidence
        }

        # إضافة التحليل المتقدم
        if process.logical_result and "الحروف" in process.logical_result:
            letters = process.logical_result["الحروف"]
            if letters:
                # تحويل معاني الحروف إلى معادلة
                meanings = []
                for letter in letters:
                    if isinstance(letter, dict) and "المعاني" in letter:
                        meanings.extend(letter["المعاني"][:2])
                result["المعاني_المستخلصة"] = meanings[:10]

        return result

    def generate_word(self, meaning: str) -> Dict:
        """توليد كلمة من معنى"""
        # استخدام الفص المنطقي للتوليد
        word = generate_word_from_meaning(meaning)

        # تحليل النتيجة
        if word:
            analysis = self.analyze_word_deeply(word)
            return {
                "المعنى_المطلوب": meaning,
                "الكلمة_المولدة": word,
                "التحليل": analysis
            }

        return {"المعنى_المطلوب": meaning, "الكلمة_المولدة": None}

    def switch_hemisphere(self, hemisphere: BrainHemisphere):
        """تبديل الفص النشط"""
        self.state.active_hemisphere = hemisphere

    def get_status(self) -> Dict:
        """حالة العقل"""
        consciousness_status = self.consciousness.get_status()

        return {
            "الاسم": self.name,
            "الفص_النشط": self.state.active_hemisphere.value,
            "قيد_المعالجة": self.state.processing,
            "عدد_العمليات": len(self.thought_history),
            "الحمل_المعرفي": consciousness_status["الحمل_المعرفي"],
            "نقاط_التركيز": consciousness_status["نقاط_التركيز"],
            "محركات_الاستنباط": list(self.inference_engines.keys()),
            "مكونات_بصيرة": list(self.baserah.keys())
        }

