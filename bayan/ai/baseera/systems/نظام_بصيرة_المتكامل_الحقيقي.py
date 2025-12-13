#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
نظام بصيرة المتكامل الحقيقي - الاتصال بالنظام الأساسي
Real Integrated Basera System - Connected to Core System

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله

هذا النظام يربط بين:
- النظام الأساسي لبصيرة (المعادلة الأم، النواة التفكيرية، الخبير/المستكشف)
- النظام الثوري الجديد (التفاعل الذكي، قاعدة المعرفة، Ollama)
"""

import sys
import os
import math
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple

# إضافة المسارات للنظام الأساسي
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'core'))
sys.path.append(os.path.join(current_dir, 'advanced'))
sys.path.append(os.path.join(current_dir, 'artistic'))

class IntegratedBaseraSystem:
    """
    نظام بصيرة المتكامل الحقيقي
    يربط بين النظام الأساسي والمكونات الجديدة
    """
    
    def __init__(self):
        self.system_name = "نظام بصيرة المتكامل الحقيقي"
        self.creator = "باسل يحيى عبدالله"
        self.version = "v1.0 - متكامل مع النظام الأساسي"
        self.creation_date = datetime.now().isoformat()
        
        print(f"🧬 تهيئة {self.system_name}")
        print(f"👨‍💻 المطور: {self.creator}")
        print("=" * 60)
        
        # تهيئة النظام الأساسي
        self.core_system = None
        self.thinking_core = None
        self.expert_explorer = None
        self.mother_equation = None
        self.adaptive_equations = None
        self.shape_equation = None
        
        # تهيئة النظام الجديد
        self.intelligent_interaction = None
        self.knowledge_base = None
        self.response_generator = None
        self.ollama_integration = None
        
        self._initialize_core_basera_system()
        self._initialize_new_components()
        
    def _initialize_core_basera_system(self):
        """تهيئة النظام الأساسي لبصيرة"""
        print("🧬 تهيئة النظام الأساسي لبصيرة...")

        # تحميل المكونات واحداً تلو الآخر لتجنب الاستيراد الدائري

        # 1. المعادلة الأم
        try:
            from core.revolutionary_mother_equation import RevolutionaryMotherEquation
            self.mother_equation = RevolutionaryMotherEquation("نظام_بصيرة_المتكامل")
            print("   ✅ تم تحميل المعادلة الأم")
        except Exception as e:
            print(f"   ⚠️ فشل تحميل المعادلة الأم: {e}")
            self.mother_equation = None

        # 2. المعادلات المتكيفة (قبل النواة التفكيرية)
        try:
            from core.adaptive_revolutionary_equations_fixed import AdaptiveRevolutionaryEquation
            self.adaptive_equations = AdaptiveRevolutionaryEquation("نظام_بصيرة_المتكامل")
            print("   ✅ تم تحميل المعادلات المتكيفة")
        except Exception as e:
            print(f"   ⚠️ فشل تحميل المعادلات المتكيفة: {e}")
            self.adaptive_equations = None

        # 3. معادلة الشكل العام
        try:
            from core.enhanced_general_shape_equation import EnhancedGeneralShapeEquation
            self.shape_equation = EnhancedGeneralShapeEquation(
                shape_name="نظام_بصيرة_المتكامل",
                shape_state="نشط",
                shape_color="ذهبي"
            )
            print("   ✅ تم تحميل معادلة الشكل العام")
        except Exception as e:
            print(f"   ⚠️ فشل تحميل معادلة الشكل العام: {e}")
            self.shape_equation = None

        # 4. نظام الخبير/المستكشف (يحتاج المعادلات المتكيفة)
        try:
            from core.expert_explorer_system import BaserahIntegratedExpertExplorer
            self.expert_explorer = BaserahIntegratedExpertExplorer("نظام_بصيرة_المتكامل", "ذكاء_اصطناعي")
            print("   ✅ تم تحميل نظام الخبير/المستكشف")
        except Exception as e:
            print(f"   ⚠️ فشل تحميل نظام الخبير/المستكشف: {e}")
            self.expert_explorer = None

        # 5. النواة التفكيرية ذات الثمان طبقات (آخر شيء)
        try:
            from core.complete_multi_layer_thinking_core import CompleteMultiLayerThinkingCore
            self.thinking_core = CompleteMultiLayerThinkingCore()
            print("   ✅ تم تحميل النواة التفكيرية ذات الثمان طبقات")
        except Exception as e:
            print(f"   ⚠️ فشل تحميل النواة التفكيرية: {e}")
            self.thinking_core = None

        # تقرير النتائج
        loaded_components = sum([
            self.mother_equation is not None,
            self.adaptive_equations is not None,
            self.shape_equation is not None,
            self.expert_explorer is not None,
            self.thinking_core is not None
        ])

        print(f"🎉 تم تحميل {loaded_components}/5 من مكونات النظام الأساسي!")
    
    def _initialize_new_components(self):
        """تهيئة المكونات الجديدة"""
        print("\n🚀 تهيئة المكونات الجديدة...")
        
        try:
            # 1. محرك التفاعل الذكي (استخدام الكلاس الصحيح)
            from محرك_التفاعل_الذكي_الثوري import RevolutionaryIntelligentInteractionEngine
            self.intelligent_interaction = RevolutionaryIntelligentInteractionEngine()
            print("   ✅ تم تحميل محرك التفاعل الذكي")
            
            # 2. قاعدة المعرفة الثورية
            from قاعدة_المعرفة_الثورية_الذكية import RevolutionaryKnowledgeBase
            self.knowledge_base = RevolutionaryKnowledgeBase()
            print("   ✅ تم تحميل قاعدة المعرفة الثورية")
            
            # 3. نظام توليد الإجابات الذكية
            from نظام_توليد_الإجابات_الذكية import IntelligentResponseGenerator
            self.response_generator = IntelligentResponseGenerator()
            print("   ✅ تم تحميل نظام توليد الإجابات الذكية")
            
            print("🎉 تم تحميل المكونات الجديدة بنجاح!")
            
        except ImportError as e:
            print(f"⚠️ خطأ في تحميل المكونات الجديدة: {e}")
    
    def process_user_input(self, user_input: str) -> Dict[str, Any]:
        """معالجة مدخلات المستخدم بالنظام المتكامل"""
        
        print(f"\n🧠 معالجة: {user_input}")
        
        result = {
            "input": user_input,
            "timestamp": datetime.now().isoformat(),
            "core_analysis": None,
            "thinking_layers": None,
            "expert_decision": None,
            "adaptive_response": None,
            "intelligent_response": None,
            "success": False
        }
        
        try:
            # 1. تحليل بالنظام الأساسي
            if self.thinking_core:
                result["thinking_layers"] = self.thinking_core.comprehensive_processing(user_input)
                print("   ✅ تم التحليل بالنواة التفكيرية")
            
            # 2. قرار الخبير/المستكشف
            if self.expert_explorer:
                problem_dict = {"input": user_input, "type": "user_query"}
                result["expert_decision"] = self.expert_explorer.analyze_situation(problem_dict)
                print("   ✅ تم اتخاذ قرار الخبير/المستكشف")
            
            # 3. استجابة المعادلات المتكيفة
            if self.adaptive_equations:
                # تحويل النص إلى بيانات رقمية للمعادلات
                import numpy as np
                input_array = np.array([len(user_input), hash(user_input) % 100, len(user_input.split())])
                result["adaptive_response"] = self.adaptive_equations.perform_adaptation()
                print("   ✅ تم التكيف بالمعادلات المتكيفة")
            
            # 4. الاستجابة الذكية الجديدة
            if self.response_generator:
                result["intelligent_response"] = self.response_generator.generate_intelligent_response(user_input)
                print("   ✅ تم توليد الاستجابة الذكية")
            
            result["success"] = True
            print("🎉 تمت المعالجة بنجاح!")
            
        except Exception as e:
            print(f"❌ خطأ في المعالجة: {e}")
            result["error"] = str(e)
        
        return result
    
    def get_system_status(self) -> Dict[str, Any]:
        """الحصول على حالة النظام"""
        
        return {
            "system_name": self.system_name,
            "creator": self.creator,
            "version": self.version,
            "creation_date": self.creation_date,
            "core_components": {
                "mother_equation": self.mother_equation is not None,
                "thinking_core": self.thinking_core is not None,
                "expert_explorer": self.expert_explorer is not None,
                "adaptive_equations": self.adaptive_equations is not None,
                "shape_equation": self.shape_equation is not None
            },
            "new_components": {
                "intelligent_interaction": self.intelligent_interaction is not None,
                "knowledge_base": self.knowledge_base is not None,
                "response_generator": hasattr(self, 'response_generator') and self.response_generator is not None
            },
            "integration_status": "متكامل" if all([
                self.mother_equation, self.thinking_core, self.expert_explorer,
                self.knowledge_base, hasattr(self, 'response_generator')
            ]) else "جزئي"
        }

def test_integrated_system():
    """اختبار النظام المتكامل"""
    print("🧪 بدء اختبار النظام المتكامل...")
    print("=" * 60)
    
    # إنشاء النظام
    system = IntegratedBaseraSystem()
    
    # عرض حالة النظام
    status = system.get_system_status()
    print(f"\n📊 حالة النظام:")
    print(f"   🧬 المكونات الأساسية: {sum(status['core_components'].values())}/5")
    print(f"   🚀 المكونات الجديدة: {sum(status['new_components'].values())}/3")
    print(f"   🔗 حالة التكامل: {status['integration_status']}")
    
    # اختبار المعالجة
    test_inputs = [
        "مرحباً، كيف حالك؟",
        "احسب لي 7 + 3",
        "ما هي النظريات الثورية الثلاث؟"
    ]
    
    for i, test_input in enumerate(test_inputs, 1):
        print(f"\n🧪 اختبار {i}: {test_input}")
        result = system.process_user_input(test_input)
        
        if result["success"]:
            print(f"   ✅ نجح - تم التحليل بـ {len([k for k, v in result.items() if v and k not in ['input', 'timestamp', 'success']])} مكون")
        else:
            print(f"   ❌ فشل: {result.get('error', 'خطأ غير معروف')}")
    
    print("\n🎉 انتهى اختبار النظام المتكامل!")
    return system

if __name__ == "__main__":
    test_integrated_system()
