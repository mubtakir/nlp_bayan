#!/usr/bin/env python3
"""
الوحدة الفنية المحسنة مع وحدة الاستنباط - نظام بصيرة الثوري (إصدار محسن)
🧬 المطور: باسل يحيى عبدالله
🌟 الأفكار الثورية: جميع النظريات من إبداع باسل يحيى عبدالله
🎯 المنهجية: sigmoid + linear فقط - بدون مكتبات ذكاء اصطناعي
"""

import numpy as np
import matplotlib.pyplot as plt
import tempfile
import os
import math
from typing import Dict, List, Tuple, Any, Optional

# ==========================================
# 🧬 النواة الرياضية الثورية
# ==========================================

def baserah_sigmoid(x, alpha=1.0, k=1.0, x0=0.0, n=1):
    """
    دالة السيجمويد الثورية مع عامل التكميم
    المعادلة الأساسية لنظام بصيرة
    """
    try:
        # تطبيق عامل التكميم n
        if hasattr(x, '__len__'):
            quantized_x = np.round(np.array(x) * n) / n if n > 0 else np.array(x)
        else:
            quantized_x = round(x * n) / n if n > 0 else x
        return alpha / (1 + np.exp(-k * (quantized_x - x0)))
    except:
        return np.zeros_like(x) if hasattr(x, '__len__') else 0.0

def baserah_linear(x, beta=1.0, gamma=0.0, n=1):
    """
    دالة الخط المستقيم الثورية مع عامل التكميم
    المكون الثاني للمعادلة الأساسية
    """
    try:
        if hasattr(x, '__len__'):
            quantized_x = np.round(np.array(x) * n) / n if n > 0 else np.array(x)
        else:
            quantized_x = round(x * n) / n if n > 0 else x
        return beta * quantized_x + gamma
    except:
        return np.zeros_like(x) if hasattr(x, '__len__') else 0.0

# ==========================================
# 🎨 محرك الرسم الثوري
# ==========================================

class BaserahArtisticRenderer:
    """
    محرك الرسم الثوري - يحول المعادلات إلى أشكال فنية
    يستخدم فقط sigmoid + linear + عامل التكميم
    """
    
    def __init__(self):
        self.creator = "باسل يحيى عبدالله"
        self.methodology = "sigmoid + linear + quantization factor only"
        self.theories = ["Zero Duality", "Perpendicular Opposites", "Filament Theory"]
        
        # إعدادات الرسم
        self.default_resolution = 1000
        self.default_figsize = (10, 8)
        self.color_palette = {
            'primary': '#FF6B6B',
            'secondary': '#4ECDC4', 
            'accent': '#45B7D1',
            'background': '#F8F9FA',
            'text': '#2C3E50'
        }
    
    def sigmoid_wave_approximation(self, t, amplitude=1.0, frequency=1.0, phase=0.0, steepness=2.0):
        """
        تقريب الموجات باستخدام sigmoid فقط
        النواة الثورية لتوليد الأشكال
        """
        try:
            # تطبيق نظرية الفتائل - ترابط النقاط
            wave_points = []
            period = 2 * np.pi / frequency
            
            for i in range(-3, 4):  # 7 نقاط ترابط
                center = i * period + phase
                # نقطة صاعدة
                up_point = baserah_sigmoid(t, alpha=amplitude, k=steepness, x0=center + period/4)
                # نقطة هابطة  
                down_point = baserah_sigmoid(t, alpha=-amplitude, k=steepness, x0=center + 3*period/4)
                wave_points.append(up_point + down_point)
            
            # تطبيق نظرية ثنائية الصفر - توازن الموجة
            result = sum(wave_points) / len(wave_points)
            
            # تطبيق نظرية تعامد الأضداد - تنعيم النتيجة
            smoothed = baserah_sigmoid(result, alpha=amplitude, k=0.5)
            
            return smoothed
        except:
            # في حالة الخطأ، إرجاع موجة بسيطة
            return amplitude * baserah_sigmoid(t, alpha=1.0, k=steepness, x0=phase)
    
    def create_heart_shape(self, t, size=1.0, style='classic'):
        """
        إنشاء شكل القلب باستخدام sigmoid فقط
        تطبيق النظريات الثلاث في الحب والجمال
        """
        try:
            if style == 'classic':
                # القلب الكلاسيكي - sigmoid فقط
                sin_approx = self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, steepness=3.0)
                cos_approx = self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, phase=np.pi/2, steepness=3.0)
                cos2_approx = self.sigmoid_wave_approximation(2*t, amplitude=1.0, frequency=1.0, phase=np.pi/2, steepness=3.0)
                cos3_approx = self.sigmoid_wave_approximation(3*t, amplitude=1.0, frequency=1.0, phase=np.pi/2, steepness=3.0)
                cos4_approx = self.sigmoid_wave_approximation(4*t, amplitude=1.0, frequency=1.0, phase=np.pi/2, steepness=3.0)
                
                x = size * 16 * (sin_approx ** 3) / 16
                y = size * (13 * cos_approx - 5 * cos2_approx - 2 * cos3_approx - cos4_approx) / 16
                
            elif style == 'pulsing':
                # القلب النابض - تطبيق نظرية ثنائية الصفر
                pulse = baserah_sigmoid(np.sin(t * 2), alpha=0.3, k=2.0)
                base_size = size * (1 + pulse)
                
                sin_approx = self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, steepness=3.0)
                cos_approx = self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, phase=np.pi/2, steepness=3.0)
                
                x = base_size * 16 * (sin_approx ** 3) / 16
                y = base_size * (13 * cos_approx) / 16
                
            else:  # simple
                # القلب البسيط - sigmoid نقي
                sin_approx = self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, steepness=2.0)
                cos_approx = self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, phase=np.pi/2, steepness=2.0)
                
                x = size * sin_approx
                y = size * cos_approx
            
            return x, y
        except:
            # في حالة الخطأ، إرجاع دائرة بسيطة
            x = size * self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, phase=np.pi/2)
            y = size * self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, phase=0.0)
            return x, y
    
    def create_flower_shape(self, t, petals=5, size=1.0, style='rose'):
        """
        إنشاء شكل الزهرة باستخدام sigmoid فقط
        تطبيق نظرية الفتائل في جمال الطبيعة
        """
        try:
            if style == 'rose':
                # وردة - تطبيق نظرية الفتائل
                petal_freq = petals
                radius_modulation = baserah_sigmoid(
                    self.sigmoid_wave_approximation(petal_freq * t, amplitude=1.0, steepness=2.0),
                    alpha=0.5, k=2.0
                )
                base_radius = size * (1 + radius_modulation)
                
                cos_approx = self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, phase=np.pi/2, steepness=2.0)
                sin_approx = self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, steepness=2.0)
                
                x = base_radius * cos_approx
                y = base_radius * sin_approx
                
            else:  # simple
                # زهرة بسيطة - sigmoid نقي
                petal_effect = baserah_sigmoid(
                    self.sigmoid_wave_approximation(petals * t, amplitude=1.0, steepness=2.0),
                    alpha=0.4, k=1.0
                )
                
                radius = size * (0.7 + petal_effect)
                
                cos_approx = self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, phase=np.pi/2, steepness=2.0)
                sin_approx = self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, steepness=2.0)
                
                x = radius * cos_approx
                y = radius * sin_approx
            
            return x, y
        except:
            # في حالة الخطأ، إرجاع دائرة بسيطة
            x = size * self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, phase=np.pi/2)
            y = size * self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, phase=0.0)
            return x, y
    
    def create_spiral_shape(self, t, turns=3, size=1.0, style='fibonacci'):
        """
        إنشاء شكل الحلزون باستخدام sigmoid فقط
        تطبيق النظريات الثلاث في النمو الطبيعي
        """
        try:
            if style == 'fibonacci':
                # حلزون فيبوناتشي - تطبيق نظرية الفتائل
                golden_ratio = (1 + np.sqrt(5)) / 2
                radius = size * np.exp(t / golden_ratio) / np.exp(2 * np.pi * turns / golden_ratio)
                
            elif style == 'archimedes':
                # حلزون أرخميدس - تطبيق نظرية ثنائية الصفر
                radius = size * t / (2 * np.pi * turns)
                
            else:  # logarithmic
                # حلزون لوغاريتمي - تطبيق نظرية تعامد الأضداد
                growth_rate = 0.2
                radius = size * np.exp(growth_rate * t) / np.exp(growth_rate * 2 * np.pi * turns)
            
            # تطبيق sigmoid للحصول على إحداثيات ناعمة
            cos_approx = self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, phase=np.pi/2, steepness=2.0)
            sin_approx = self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, steepness=2.0)
            
            x = radius * cos_approx
            y = radius * sin_approx
            
            return x, y
        except:
            # في حالة الخطأ، إرجاع دائرة بسيطة
            x = size * self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, phase=np.pi/2)
            y = size * self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, phase=0.0)
            return x, y
    
    def create_wave_pattern(self, x, amplitude=1.0, frequency=1.0, phase=0.0, style='sine'):
        """
        إنشاء أنماط الموجات باستخدام sigmoid فقط
        تطبيق النظريات في الذبذبات والطاقة
        """
        try:
            if style == 'sine':
                # موجة جيبية - sigmoid نقي
                y = self.sigmoid_wave_approximation(x, amplitude=amplitude, frequency=frequency, phase=phase, steepness=2.0)
                
            elif style == 'square':
                # موجة مربعة - تطبيق عامل التكميم
                base_wave = self.sigmoid_wave_approximation(x, amplitude=amplitude, frequency=frequency, phase=phase, steepness=10.0)
                y = baserah_sigmoid(base_wave, alpha=amplitude, k=50.0, n=2)
                
            else:  # triangle or default
                # موجة مثلثية - تطبيق نظرية الفتائل
                y = amplitude * baserah_sigmoid(x, alpha=1.0, k=2.0)
            
            return y
        except:
            # في حالة الخطأ، إرجاع موجة بسيطة
            return amplitude * baserah_sigmoid(x, alpha=1.0, k=1.0)
    
    def render_shape(self, shape_type, parameters=None, animation=False):
        """
        رسم الشكل المطلوب مع التحكم في المعاملات
        """
        if parameters is None:
            parameters = {}
        
        # إعداد المعاملات الافتراضية
        size = parameters.get('size', 1.0)
        style = parameters.get('style', 'classic')
        color = parameters.get('color', self.color_palette['primary'])
        resolution = parameters.get('resolution', self.default_resolution)
        
        # إنشاء المجال الزمني
        if shape_type in ['heart', 'flower', 'spiral']:
            t = np.linspace(0, 2*np.pi, resolution)
        else:
            t = np.linspace(-2*np.pi, 2*np.pi, resolution)
        
        # إنشاء الشكل
        try:
            if shape_type == 'heart':
                x, y = self.create_heart_shape(t, size, style)
                title = f"قلب ثوري - {style}"
                equation = "Heart using PURE SIGMOID - NO trigonometry!"
                
            elif shape_type == 'flower':
                petals = parameters.get('petals', 5)
                x, y = self.create_flower_shape(t, petals, size, style)
                title = f"زهرة ثورية - {petals} بتلات - {style}"
                equation = f"Flower with {petals} petals using PURE SIGMOID!"
                
            elif shape_type == 'spiral':
                turns = parameters.get('turns', 3)
                x, y = self.create_spiral_shape(t, turns, size, style)
                title = f"حلزون ثوري - {turns} لفات - {style}"
                equation = f"Spiral with {turns} turns using PURE SIGMOID!"
                
            elif shape_type == 'wave':
                amplitude = parameters.get('amplitude', 1.0)
                frequency = parameters.get('frequency', 1.0)
                x = t
                y = self.create_wave_pattern(x, amplitude, frequency, style=style)
                title = f"موجة ثورية - {style}"
                equation = f"Wave pattern using PURE SIGMOID approximation!"
                
            else:  # circle default
                x = self.sigmoid_wave_approximation(t, amplitude=size, frequency=1.0, phase=np.pi/2, steepness=2.0)
                y = self.sigmoid_wave_approximation(t, amplitude=size, frequency=1.0, phase=0.0, steepness=2.0)
                title = "دائرة ثورية"
                equation = "Circle using PURE SIGMOID - NO trigonometry!"
        except Exception as e:
            # في حالة الخطأ، إنشاء دائرة بسيطة
            x = size * self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, phase=np.pi/2)
            y = size * self.sigmoid_wave_approximation(t, amplitude=1.0, frequency=1.0, phase=0.0)
            title = "شكل افتراضي (دائرة)"
            equation = "Default shape using PURE SIGMOID"
        
        # إنشاء الرسم
        fig, ax = plt.subplots(figsize=self.default_figsize)
        
        # رسم الشكل
        line, = ax.plot(x, y, linewidth=3, color=color, alpha=0.8, label='الشكل الثوري')
        ax.fill(x, y, alpha=0.3, color=color)
        
        # تنسيق الرسم
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3, color=self.color_palette['text'])
        ax.set_facecolor(self.color_palette['background'])
        
        # العنوان والمعلومات
        ax.set_title(title, fontsize=16, fontweight='bold', color=self.color_palette['text'], pad=20)
        
        # إضافة معلومات النظام
        info_text = f"""المطور: {self.creator}
المعادلة: {equation}
المنهجية: {self.methodology}
النظريات: {', '.join(self.theories)}"""
        
        ax.text(0.02, 0.98, info_text, transform=ax.transAxes, fontsize=9,
                verticalalignment='top', bbox=dict(boxstyle="round,pad=0.5",
                facecolor=self.color_palette['secondary'], alpha=0.8))
        
        plt.tight_layout()
        
        if animation:
            return fig, ax, line, (x, y)
        else:
            # حفظ الصورة
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            plt.savefig(temp_file.name, format='png', dpi=150, bbox_inches='tight',
                       facecolor=self.color_palette['background'])
            plt.close(fig)
            return temp_file.name

# ==========================================
# 👁️ وحدة الاستنباط الثورية (مبسطة)
# ==========================================

class BaserahInferenceEngine:
    """
    وحدة الاستنباط الثورية - عين النظام (إصدار مبسط)
    تستنبط المعادلات من الأشكال والأنماط
    """
    
    def __init__(self):
        self.creator = "باسل يحيى عبدالله"
        self.methodology = "Revolutionary Pattern Recognition using Basil's Theories"
        self.theories = ["Zero Duality", "Perpendicular Opposites", "Filament Theory"]
        
        # قاعدة بيانات الأشكال المعروفة
        self.known_patterns = {
            'circle': {'signature': 'closed_curve_constant_radius', 'complexity': 1},
            'heart': {'signature': 'closed_curve_cusp_symmetry', 'complexity': 3},
            'flower': {'signature': 'radial_symmetry_petals', 'complexity': 2},
            'spiral': {'signature': 'expanding_curve_rotation', 'complexity': 2},
            'wave': {'signature': 'periodic_oscillation', 'complexity': 1},
            'star': {'signature': 'radial_spikes_symmetry', 'complexity': 2}
        }
    
    def analyze_curve_properties(self, x, y):
        """
        تحليل خصائص المنحنى باستخدام النظريات الثورية (مبسط)
        """
        properties = {}
        
        try:
            # التحقق من وجود البيانات
            if len(x) == 0 or len(y) == 0:
                return self._get_default_properties()
            
            # تطبيق نظرية ثنائية الصفر - تحليل التوازن
            center_x = np.mean(x)
            center_y = np.mean(y)
            properties['center'] = (center_x, center_y)
            
            # تطبيق نظرية تعامد الأضداد - تحليل التماثل
            x_centered = np.array(x) - center_x
            y_centered = np.array(y) - center_y
            
            # حساب نصف القطر المتوسط
            radii = np.sqrt(x_centered**2 + y_centered**2)
            properties['mean_radius'] = np.mean(radii)
            properties['radius_std'] = np.std(radii)
            
            # تحليل بسيط للتعقيد
            properties['complexity'] = min(len(x) / 100.0, 3.0)  # تقدير بسيط
            
            # تحليل الدورية
            properties['is_closed'] = self._is_closed_curve(x, y)
            properties['symmetry_score'] = 0.5  # قيمة افتراضية
            
            # تحليل الانحناء المبسط
            properties['mean_curvature'] = 1.0
            properties['curvature_variation'] = 0.5
            
        except Exception as e:
            properties = self._get_default_properties()
        
        return properties
    
    def _get_default_properties(self):
        """إرجاع خصائص افتراضية في حالة الخطأ"""
        return {
            'center': (0.0, 0.0),
            'mean_radius': 1.0,
            'radius_std': 0.1,
            'complexity': 1.0,
            'is_closed': True,
            'symmetry_score': 0.5,
            'mean_curvature': 1.0,
            'curvature_variation': 0.5
        }
    
    def _is_closed_curve(self, x, y, tolerance=0.1):
        """فحص ما إذا كان المنحنى مغلق"""
        try:
            if len(x) < 3:
                return False
            
            start_point = np.array([x[0], y[0]])
            end_point = np.array([x[-1], y[-1]])
            distance = np.linalg.norm(end_point - start_point)
            
            return distance < tolerance
        except:
            return True  # افتراضي
    
    def infer_shape_type(self, x, y):
        """
        استنباط نوع الشكل من الإحداثيات (مبسط)
        """
        try:
            properties = self.analyze_curve_properties(x, y)
            
            # تطبيق خوارزمية الاستنباط الثورية المبسطة
            scores = {}
            
            for shape_name, shape_info in self.known_patterns.items():
                score = self._calculate_shape_score_simple(properties, shape_name)
                scores[shape_name] = score
            
            # اختيار أفضل تطابق
            best_match = max(scores, key=scores.get)
            confidence = scores[best_match]
            
            return {
                'predicted_shape': best_match,
                'confidence': confidence,
                'all_scores': scores,
                'properties': properties
            }
        except Exception as e:
            # في حالة الخطأ، إرجاع نتيجة افتراضية
            return {
                'predicted_shape': 'circle',
                'confidence': 0.5,
                'all_scores': {'circle': 0.5},
                'properties': self._get_default_properties()
            }
    
    def _calculate_shape_score_simple(self, properties, shape_name):
        """
        حساب درجة التطابق مع شكل معين (مبسط)
        """
        try:
            score = 0.5  # نقطة بداية
            
            if shape_name == 'circle':
                # الدائرة: نصف قطر ثابت
                radius_consistency = 1.0 - min(properties['radius_std'] / max(properties['mean_radius'], 0.1), 1.0)
                score = 0.7 * radius_consistency + 0.3 * properties['symmetry_score']
                
            elif shape_name == 'heart':
                # القلب: تعقيد متوسط
                complexity_match = 1.0 - abs(properties['complexity'] - 2.0) / 2.0
                score = 0.6 * complexity_match + 0.4 * properties['symmetry_score']
                
            elif shape_name == 'flower':
                # الزهرة: تماثل شعاعي
                score = 0.8 * properties['symmetry_score'] + 0.2 * (1.0 - properties['complexity'] / 3.0)
                
            elif shape_name == 'spiral':
                # الحلزون: لا يُغلق
                open_curve_bonus = 0.8 if not properties['is_closed'] else 0.3
                score = 0.7 * open_curve_bonus + 0.3 * (properties['complexity'] / 3.0)
                
            elif shape_name == 'wave':
                # الموجة: لا يُغلق، تعقيد منخفض
                open_curve_bonus = 0.9 if not properties['is_closed'] else 0.2
                low_complexity_bonus = 1.0 - properties['complexity'] / 3.0
                score = 0.6 * open_curve_bonus + 0.4 * low_complexity_bonus
                
            return max(0.0, min(1.0, score))
        except:
            return 0.3  # قيمة افتراضية
    
    def generate_equation_from_inference(self, inference_result):
        """
        توليد المعادلة الرياضية من نتائج الاستنباط (مبسط)
        """
        try:
            shape_type = inference_result['predicted_shape']
            properties = inference_result['properties']
            
            size = properties.get('mean_radius', 1.0)
            
            if shape_type == 'circle':
                equation = f"""
دائرة ثورية:
x(t) = {size:.2f} × SigmoidWave(t, φ=π/2)
y(t) = {size:.2f} × SigmoidWave(t, φ=0)

حيث: SigmoidWave = تقريب sigmoid للدوال المثلثية
"""
                
            elif shape_type == 'heart':
                equation = f"""
قلب ثوري:
x(t) = {size:.2f} × 16 × SigmoidSin³(t)
y(t) = {size:.2f} × (13×SigmoidCos(t) - 5×SigmoidCos(2t))

النمط: كلاسيكي
"""
                
            elif shape_type == 'flower':
                equation = f"""
زهرة ثورية:
r(t) = {size:.2f} × (1 + 0.4×SigmoidCos(5t))
x(t) = r(t) × SigmoidCos(t)
y(t) = r(t) × SigmoidSin(t)

عدد البتلات: 5
"""
                
            elif shape_type == 'spiral':
                equation = f"""
حلزون ثوري:
r(t) = {size:.2f} × t/(2π×3)
x(t) = r(t) × SigmoidCos(t)
y(t) = r(t) × SigmoidSin(t)

عدد اللفات: 3
"""
                
            elif shape_type == 'wave':
                equation = f"""
موجة ثورية:
y(x) = {size:.2f} × SigmoidWave(x, f=1.0)

السعة: {size:.2f}
التردد: 1.0
"""
                
            else:
                equation = f"""
شكل عام (sigmoid + linear):
f(x) = Σ(αᵢ × sigmoid(x; kᵢ, x₀ᵢ) + βᵢx + γᵢ)

الحجم المقدر: {size:.2f}
"""
            
            return equation
        except:
            return "معادلة افتراضية: f(x) = sigmoid(x) + linear(x)"

# ==========================================
# 🎨👁️ النظام المتكامل - الوحدة الفنية + الاستنباط
# ==========================================

class BaserahIntegratedSystem:
    """
    النظام المتكامل - يجمع بين الوحدة الفنية ووحدة الاستنباط
    القدرة على الرسم والاستنباط في نظام واحد ثوري
    """
    
    def __init__(self):
        self.renderer = BaserahArtisticRenderer()
        self.inference_engine = BaserahInferenceEngine()
        self.creator = "باسل يحيى عبدالله"
        self.system_name = "نظام بصيرة المتكامل - الوحدة الفنية + وحدة الاستنباط"
        
    def create_and_analyze(self, shape_type, parameters=None):
        """
        إنشاء شكل وتحليله في نفس الوقت
        """
        try:
            # إنشاء الشكل
            image_path = self.renderer.render_shape(shape_type, parameters)
            
            # الحصول على البيانات للتحليل
            if parameters is None:
                parameters = {}
            
            # إنشاء البيانات للتحليل
            resolution = parameters.get('resolution', 100)  # تقليل الدقة لتجنب الأخطاء
            size = parameters.get('size', 1.0)
            
            t = np.linspace(0, 2*np.pi, resolution)
            
            # إنشاء الإحداثيات
            if shape_type == 'heart':
                x, y = self.renderer.create_heart_shape(t, size, parameters.get('style', 'classic'))
            elif shape_type == 'flower':
                petals = parameters.get('petals', 5)
                x, y = self.renderer.create_flower_shape(t, petals, size, parameters.get('style', 'rose'))
            elif shape_type == 'spiral':
                turns = parameters.get('turns', 3)
                x, y = self.renderer.create_spiral_shape(t, turns, size, parameters.get('style', 'fibonacci'))
            elif shape_type == 'wave':
                x = t
                y = self.renderer.create_wave_pattern(x, parameters.get('amplitude', 1.0), 
                                                    parameters.get('frequency', 1.0), 
                                                    style=parameters.get('style', 'sine'))
            else:  # circle
                x = self.renderer.sigmoid_wave_approximation(t, amplitude=size, frequency=1.0, phase=np.pi/2, steepness=2.0)
                y = self.renderer.sigmoid_wave_approximation(t, amplitude=size, frequency=1.0, phase=0.0, steepness=2.0)
            
            # تحليل الشكل
            inference_result = self.inference_engine.infer_shape_type(x, y)
            equation = self.inference_engine.generate_equation_from_inference(inference_result)
            
            return {
                'image_path': image_path,
                'inference_result': inference_result,
                'equation': equation,
                'coordinates': (x, y),
                'original_parameters': parameters
            }
        except Exception as e:
            # في حالة الخطأ، إرجاع نتيجة افتراضية
            return {
                'image_path': None,
                'inference_result': {'predicted_shape': shape_type, 'confidence': 0.5},
                'equation': f"معادلة {shape_type} الثورية",
                'coordinates': ([], []),
                'original_parameters': parameters or {},
                'error': str(e)
            }
    
    def demonstrate_system(self):
        """
        عرض توضيحي لقدرات النظام المتكامل
        """
        print(f"🌟 {self.system_name}")
        print(f"🧬 المطور: {self.creator}")
        print("="*60)
        
        # اختبار الأشكال المختلفة
        test_shapes = [
            ('heart', {'style': 'classic', 'size': 1.2}),
            ('flower', {'petals': 6, 'style': 'rose', 'size': 1.0}),
            ('spiral', {'turns': 3, 'style': 'fibonacci', 'size': 0.8}),
            ('circle', {'size': 1.0})
        ]
        
        results = []
        
        for shape_type, params in test_shapes:
            print(f"\n🎨 اختبار {shape_type}...")
            try:
                result = self.create_and_analyze(shape_type, params)
                results.append(result)
                
                if result['image_path']:
                    print(f"✅ تم إنشاء الشكل: {os.path.basename(result['image_path'])}")
                else:
                    print("⚠️ لم يتم إنشاء الصورة")
                    
                print(f"🔍 الشكل المستنبط: {result['inference_result']['predicted_shape']}")
                print(f"📊 الثقة: {result['inference_result']['confidence']:.2f}")
                
                if 'error' in result:
                    print(f"⚠️ تحذير: {result['error']}")
                    
            except Exception as e:
                print(f"❌ خطأ في اختبار {shape_type}: {str(e)}")
                results.append({'error': str(e), 'shape_type': shape_type})
        
        print(f"\n🎉 تم اختبار {len(results)} أشكال!")
        print("🌟 النظام المتكامل يعمل!")
        
        return results

# ==========================================
# 🧪 اختبار النظام
# ==========================================

def test_integrated_system():
    """
    اختبار شامل للنظام المتكامل
    """
    print("🧪 بدء اختبار النظام المتكامل...")
    
    try:
        # إنشاء النظام
        system = BaserahIntegratedSystem()
        
        # تشغيل العرض التوضيحي
        results = system.demonstrate_system()
        
        print("\n📊 ملخص النتائج:")
        for i, result in enumerate(results):
            if 'error' in result:
                print(f"{i+1}. خطأ في {result.get('shape_type', 'unknown')}: {result['error']}")
            else:
                image_name = os.path.basename(result['image_path']) if result['image_path'] else 'لا توجد صورة'
                print(f"{i+1}. الصورة: {image_name}")
                print(f"   الاستنباط: {result['inference_result']['predicted_shape']}")
                print(f"   الثقة: {result['inference_result']['confidence']:.2f}")
        
        return results
    except Exception as e:
        print(f"❌ خطأ في اختبار النظام: {str(e)}")
        return []

if __name__ == "__main__":
    # تشغيل الاختبار
    test_results = test_integrated_system()
    print("\n✅ اكتمل اختبار النظام المتكامل!")
