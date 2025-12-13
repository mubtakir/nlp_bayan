"""
طبقات التفكير المتعددة - Multi-Layer Thinking Core
===================================================

نظام التفكير متعدد الطبقات:
1. الطبقة الرياضية (Mathematical Layer)
2. الطبقة اللغوية (Linguistic Layer)
3. الطبقة المنطقية (Logical Layer)
4. الطبقة الفيزيائية (Physical Layer)
5. الطبقة التفسيرية (Interpretive Layer)

المؤلف: باسل يحيى عبدالله
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum
import numpy as np


class LayerType(Enum):
    """أنواع طبقات التفكير"""
    MATHEMATICAL = "رياضية"
    LINGUISTIC = "لغوية"
    LOGICAL = "منطقية"
    PHYSICAL = "فيزيائية"
    INTERPRETIVE = "تفسيرية"


@dataclass
class LayerResult:
    """نتيجة معالجة طبقة"""
    layer_type: LayerType
    input_data: Any
    output: Any
    confidence: float = 1.0
    processing_time: float = 0.0
    insights: List[str] = field(default_factory=list)


@dataclass
class ThinkingLayer:
    """طبقة تفكير واحدة"""
    layer_type: LayerType
    active: bool = True
    weight: float = 1.0
    history: List[LayerResult] = field(default_factory=list)
    
    def process(self, data: Any) -> LayerResult:
        """معالجة البيانات في الطبقة"""
        # التنفيذ الافتراضي
        return LayerResult(
            layer_type=self.layer_type,
            input_data=data,
            output=data,
            insights=[f"تمت المعالجة في الطبقة {self.layer_type.value}"]
        )


class ThinkingCore:
    """
    نواة التفكير متعددة الطبقات
    
    تنسق بين الطبقات المختلفة للوصول إلى فهم شامل
    """
    
    def __init__(self):
        self.layers: Dict[LayerType, ThinkingLayer] = {}
        self._init_layers()
        self.processing_history: List[Dict] = []
    
    def _init_layers(self):
        """تهيئة الطبقات"""
        for layer_type in LayerType:
            self.layers[layer_type] = ThinkingLayer(layer_type=layer_type)
    
    def process(self, data: Any, active_layers: List[LayerType] = None) -> Dict[LayerType, LayerResult]:
        """
        معالجة البيانات عبر الطبقات
        """
        if active_layers is None:
            active_layers = list(LayerType)
        
        results = {}
        
        for layer_type in active_layers:
            if layer_type in self.layers and self.layers[layer_type].active:
                layer = self.layers[layer_type]
                result = self._process_in_layer(layer, data)
                results[layer_type] = result
                layer.history.append(result)
        
        # دمج النتائج
        combined = self._combine_results(results)
        self.processing_history.append({
            "input": data,
            "results": results,
            "combined": combined
        })
        
        return results
    
    def _process_in_layer(self, layer: ThinkingLayer, data: Any) -> LayerResult:
        """معالجة في طبقة معينة"""
        processors = {
            LayerType.MATHEMATICAL: self._mathematical_process,
            LayerType.LINGUISTIC: self._linguistic_process,
            LayerType.LOGICAL: self._logical_process,
            LayerType.PHYSICAL: self._physical_process,
            LayerType.INTERPRETIVE: self._interpretive_process,
        }
        
        processor = processors.get(layer.layer_type, layer.process)
        return processor(data)
    
    def _mathematical_process(self, data: Any) -> LayerResult:
        """المعالجة الرياضية"""
        insights = []
        output = data
        
        if isinstance(data, (int, float)):
            output = {"القيمة": data, "المربع": data**2, "الجذر": np.sqrt(abs(data))}
            insights.append(f"تحليل رياضي: {data}")
        elif isinstance(data, str):
            output = {"الطول": len(data), "عدد_الكلمات": len(data.split())}
            insights.append("تحليل إحصائي للنص")
        
        return LayerResult(LayerType.MATHEMATICAL, data, output, insights=insights)
    
    def _linguistic_process(self, data: Any) -> LayerResult:
        """المعالجة اللغوية"""
        insights = []
        output = data
        
        if isinstance(data, str):
            output = {
                "النص": data,
                "الحروف": list(data.replace(" ", "")),
                "الكلمات": data.split()
            }
            insights.append("تحليل لغوي للنص")
        
        return LayerResult(LayerType.LINGUISTIC, data, output, insights=insights)
    
    def _logical_process(self, data: Any) -> LayerResult:
        """المعالجة المنطقية"""
        return LayerResult(LayerType.LOGICAL, data, {"صحة": bool(data)}, 
                          insights=["فحص منطقي"])
    
    def _physical_process(self, data: Any) -> LayerResult:
        """المعالجة الفيزيائية"""
        return LayerResult(LayerType.PHYSICAL, data, data, 
                          insights=["معالجة فيزيائية"])
    
    def _interpretive_process(self, data: Any) -> LayerResult:
        """المعالجة التفسيرية"""
        return LayerResult(LayerType.INTERPRETIVE, data, 
                          {"التفسير": f"تفسير: {data}"}, 
                          insights=["تفسير شامل"])
    
    def _combine_results(self, results: Dict[LayerType, LayerResult]) -> Dict:
        """دمج نتائج الطبقات"""
        combined = {
            "عدد_الطبقات": len(results),
            "الثقة_الإجمالية": np.mean([r.confidence for r in results.values()]),
            "الرؤى": []
        }
        
        for result in results.values():
            combined["الرؤى"].extend(result.insights)
        
        return combined

