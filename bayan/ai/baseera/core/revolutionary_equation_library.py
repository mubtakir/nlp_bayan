#!/usr/bin/env python3
"""
مكتبة المعادلات الثورية المرجعية - نظام بصيرة الثوري
🧬 المطور: باسل يحيى عبدالله
🎯 الهدف: مكتبة شاملة من المعادلات الأساسية للاستنباط
🌟 الاستراتيجية: الحل الأخير عند فشل الطرق المعتادة
"""

import numpy as np
import json
import os
from typing import Dict, List, Tuple, Any, Optional
try:
    from artistic.enhanced_artistic_unit_fixed import BaserahArtisticRenderer
except ImportError:
    try:
        from enhanced_artistic_unit_fixed import BaserahArtisticRenderer
    except ImportError:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from artistic.enhanced_artistic_unit_fixed import BaserahArtisticRenderer

class RevolutionaryEquationLibrary:
    """
    مكتبة المعادلات الثورية المرجعية
    تحتوي على آلاف المعادلات الأساسية للأشكال المختلفة
    """
    
    def __init__(self):
        self.creator = "باسل يحيى عبدالله"
        self.methodology = "Revolutionary Reference Library Strategy"
        
        # المكتبة الرئيسية للمعادلات
        self.equation_library = {}
        
        # إعدادات المكتبة
        self.library_config = {
            'max_equations_per_shape': 200,  # مخفض لتجنب الحلقات اللانهائية
            'parameter_variations': 20,  # مخفض
            'resolution_points': 100,  # مخفض
            'accuracy_threshold': 0.5,  # مخفض لتجنب الحلقات اللانهائية
            'max_iterations_per_equation': 2,  # مخفض
            'max_search_time': 30  # حد أقصى للبحث (30 ثانية)
        }
        
        # إنشاء المكتبة
        self._initialize_library()
    
    def _initialize_library(self):
        """
        إنشاء المكتبة الشاملة للمعادلات
        """
        print("🧬 إنشاء مكتبة المعادلات الثورية...")
        
        # 1. معادلات الدوائر
        self.equation_library['circles'] = self._generate_circle_equations()
        
        # 2. معادلات القلوب
        self.equation_library['hearts'] = self._generate_heart_equations()
        
        # 3. معادلات الزهور
        self.equation_library['flowers'] = self._generate_flower_equations()
        
        # 4. معادلات الحلزونات
        self.equation_library['spirals'] = self._generate_spiral_equations()
        
        # 5. معادلات الموجات
        self.equation_library['waves'] = self._generate_wave_equations()
        
        # 6. معادلات الخطوط
        self.equation_library['lines'] = self._generate_line_equations()
        
        # 7. معادلات الأشكال المركبة
        self.equation_library['complex'] = self._generate_complex_equations()
        
        # 8. معادلات هندسية أساسية
        self.equation_library['geometric'] = self._generate_geometric_equations()
        
        total_equations = sum(len(equations) for equations in self.equation_library.values())
        print(f"✅ تم إنشاء {total_equations} معادلة في {len(self.equation_library)} فئة")
    
    def _generate_circle_equations(self) -> List[Dict]:
        """
        توليد معادلات الدوائر بتنويعات مختلفة
        """
        equations = []
        renderer = BaserahArtisticRenderer()
        
        # تنويعات الحجم
        sizes = np.linspace(0.5, 3.0, 20)
        
        # تنويعات الانحراف (ellipses)
        eccentricities = np.linspace(0.0, 0.8, 15)
        
        # تنويعات الدوران
        rotations = np.linspace(0, 2*np.pi, 12)
        
        for i, size in enumerate(sizes):
            for j, ecc in enumerate(eccentricities):
                for k, rot in enumerate(rotations):
                    # معاملات السيجمويد للدائرة
                    sigmoid_params = [
                        {
                            'alpha': size,
                            'k': 2.0,
                            'x0': np.pi/2 + rot,
                            'n': 1,
                            'component_type': 'x_component'
                        },
                        {
                            'alpha': size * (1 - ecc),  # تطبيق الانحراف
                            'k': 2.0,
                            'x0': rot,
                            'n': 1,
                            'component_type': 'y_component'
                        }
                    ]
                    
                    equation = {
                        'id': f'circle_{i}_{j}_{k}',
                        'shape_type': 'circle',
                        'parameters': {
                            'size': size,
                            'eccentricity': ecc,
                            'rotation': rot,
                            'sigmoid_components': sigmoid_params,
                            'linear_components': []
                        },
                        'properties': {
                            'closed': True,
                            'symmetric': True,
                            'complexity': 'simple'
                        }
                    }
                    
                    equations.append(equation)
                    
                    if len(equations) >= self.library_config['max_equations_per_shape']:
                        return equations
        
        return equations
    
    def _generate_heart_equations(self) -> List[Dict]:
        """
        توليد معادلات القلوب بتنويعات مختلفة
        """
        equations = []
        
        # تنويعات الحجم
        sizes = np.linspace(0.5, 2.5, 15)
        
        # تنويعات الشكل
        heart_styles = ['classic', 'rounded', 'pointed', 'wide', 'narrow']
        
        # تنويعات الدوران
        rotations = np.linspace(0, 2*np.pi, 8)
        
        for i, size in enumerate(sizes):
            for j, style in enumerate(heart_styles):
                for k, rot in enumerate(rotations):
                    # معاملات مخصصة لكل نمط قلب
                    if style == 'classic':
                        alpha_factor = 1.0
                        k_factor = 1.5
                    elif style == 'rounded':
                        alpha_factor = 1.2
                        k_factor = 1.0
                    elif style == 'pointed':
                        alpha_factor = 0.8
                        k_factor = 2.0
                    elif style == 'wide':
                        alpha_factor = 1.5
                        k_factor = 1.2
                    else:  # narrow
                        alpha_factor = 0.7
                        k_factor = 1.8
                    
                    sigmoid_params = [
                        {
                            'alpha': size * alpha_factor,
                            'k': k_factor,
                            'x0': np.pi/4 + rot,
                            'n': 1,
                            'component_type': 'heart_main'
                        },
                        {
                            'alpha': size * alpha_factor * 0.7,
                            'k': k_factor * 1.5,
                            'x0': 3*np.pi/4 + rot,
                            'n': 1,
                            'component_type': 'heart_secondary'
                        }
                    ]
                    
                    equation = {
                        'id': f'heart_{i}_{j}_{k}',
                        'shape_type': 'heart',
                        'parameters': {
                            'size': size,
                            'style': style,
                            'rotation': rot,
                            'sigmoid_components': sigmoid_params,
                            'linear_components': []
                        },
                        'properties': {
                            'closed': True,
                            'symmetric': True,
                            'complexity': 'medium'
                        }
                    }
                    
                    equations.append(equation)
                    
                    if len(equations) >= self.library_config['max_equations_per_shape']:
                        return equations
        
        return equations
    
    def _generate_flower_equations(self) -> List[Dict]:
        """
        توليد معادلات الزهور بتنويعات مختلفة
        """
        equations = []
        
        # تنويعات عدد البتلات
        petal_counts = range(3, 13)
        
        # تنويعات الحجم
        sizes = np.linspace(0.5, 2.0, 12)
        
        # تنويعات الشكل
        flower_styles = ['rose', 'daisy', 'tulip', 'lotus', 'sunflower']
        
        for i, petals in enumerate(petal_counts):
            for j, size in enumerate(sizes):
                for k, style in enumerate(flower_styles):
                    # معاملات مخصصة لكل نمط زهرة
                    if style == 'rose':
                        complexity_factor = 1.0
                        sharpness = 2.0
                    elif style == 'daisy':
                        complexity_factor = 0.8
                        sharpness = 3.0
                    elif style == 'tulip':
                        complexity_factor = 1.2
                        sharpness = 1.5
                    elif style == 'lotus':
                        complexity_factor = 1.5
                        sharpness = 1.0
                    else:  # sunflower
                        complexity_factor = 2.0
                        sharpness = 2.5
                    
                    sigmoid_params = []
                    
                    # مكونات البتلات
                    for petal in range(petals):
                        angle_offset = 2 * np.pi * petal / petals
                        
                        sigmoid_params.append({
                            'alpha': size * complexity_factor,
                            'k': sharpness,
                            'x0': angle_offset,
                            'n': 1,
                            'component_type': f'petal_{petal}'
                        })
                    
                    # مكون المركز
                    sigmoid_params.append({
                        'alpha': size * 0.3,
                        'k': 4.0,
                        'x0': 0,
                        'n': 1,
                        'component_type': 'center'
                    })
                    
                    equation = {
                        'id': f'flower_{i}_{j}_{k}',
                        'shape_type': 'flower',
                        'parameters': {
                            'petals': petals,
                            'size': size,
                            'style': style,
                            'sigmoid_components': sigmoid_params,
                            'linear_components': []
                        },
                        'properties': {
                            'closed': True,
                            'symmetric': True,
                            'complexity': 'high'
                        }
                    }
                    
                    equations.append(equation)
                    
                    if len(equations) >= self.library_config['max_equations_per_shape']:
                        return equations
        
        return equations
    
    def _generate_spiral_equations(self) -> List[Dict]:
        """
        توليد معادلات الحلزونات بتنويعات مختلفة
        """
        equations = []
        
        # تنويعات عدد اللفات
        turn_counts = np.linspace(1, 8, 15)
        
        # تنويعات الحجم
        sizes = np.linspace(0.3, 2.0, 10)
        
        # تنويعات النمط
        spiral_styles = ['fibonacci', 'archimedes', 'logarithmic', 'hyperbolic']
        
        for i, turns in enumerate(turn_counts):
            for j, size in enumerate(sizes):
                for k, style in enumerate(spiral_styles):
                    # معاملات مخصصة لكل نمط حلزون
                    if style == 'fibonacci':
                        growth_rate = 1.618  # النسبة الذهبية
                        tightness = 1.0
                    elif style == 'archimedes':
                        growth_rate = 1.0
                        tightness = 1.5
                    elif style == 'logarithmic':
                        growth_rate = 1.2
                        tightness = 0.8
                    else:  # hyperbolic
                        growth_rate = 0.8
                        tightness = 2.0
                    
                    sigmoid_params = [
                        {
                            'alpha': size,
                            'k': tightness,
                            'x0': np.pi/2,
                            'n': 1,
                            'component_type': 'spiral_x'
                        },
                        {
                            'alpha': size,
                            'k': tightness,
                            'x0': 0,
                            'n': 1,
                            'component_type': 'spiral_y'
                        }
                    ]
                    
                    linear_params = [
                        {
                            'beta': size * growth_rate / (2 * np.pi * turns),
                            'gamma': 0,
                            'n': 1,
                            'component_type': 'radial_growth'
                        }
                    ]
                    
                    equation = {
                        'id': f'spiral_{i}_{j}_{k}',
                        'shape_type': 'spiral',
                        'parameters': {
                            'turns': turns,
                            'size': size,
                            'style': style,
                            'growth_rate': growth_rate,
                            'sigmoid_components': sigmoid_params,
                            'linear_components': linear_params
                        },
                        'properties': {
                            'closed': False,
                            'symmetric': False,
                            'complexity': 'medium'
                        }
                    }
                    
                    equations.append(equation)
                    
                    if len(equations) >= self.library_config['max_equations_per_shape']:
                        return equations
        
        return equations

    def _generate_wave_equations(self) -> List[Dict]:
        """
        توليد معادلات الموجات بتنويعات مختلفة
        """
        equations = []

        # تنويعات التردد
        frequencies = np.linspace(0.5, 5.0, 20)

        # تنويعات السعة
        amplitudes = np.linspace(0.3, 2.0, 15)

        # تنويعات الطور
        phases = np.linspace(0, 2*np.pi, 8)

        # أنماط الموجات
        wave_types = ['sine', 'cosine', 'square', 'triangle']

        for i, freq in enumerate(frequencies):
            for j, amp in enumerate(amplitudes):
                for k, phase in enumerate(phases):
                    for l, wave_type in enumerate(wave_types):

                        if wave_type == 'sine':
                            k_factor = 2.0
                            n_factor = 1
                        elif wave_type == 'cosine':
                            k_factor = 2.0
                            n_factor = 1
                            phase += np.pi/2
                        elif wave_type == 'square':
                            k_factor = 10.0  # حاد للتقريب المربع
                            n_factor = 3
                        else:  # triangle
                            k_factor = 1.0
                            n_factor = 2

                        sigmoid_params = [
                            {
                                'alpha': amp,
                                'k': k_factor,
                                'x0': phase,
                                'n': n_factor,
                                'frequency': freq,
                                'component_type': f'wave_{wave_type}'
                            }
                        ]

                        equation = {
                            'id': f'wave_{i}_{j}_{k}_{l}',
                            'shape_type': 'wave',
                            'parameters': {
                                'frequency': freq,
                                'amplitude': amp,
                                'phase': phase,
                                'wave_type': wave_type,
                                'sigmoid_components': sigmoid_params,
                                'linear_components': []
                            },
                            'properties': {
                                'closed': False,
                                'symmetric': True,
                                'complexity': 'simple'
                            }
                        }

                        equations.append(equation)

                        if len(equations) >= self.library_config['max_equations_per_shape']:
                            return equations

        return equations

    def _generate_line_equations(self) -> List[Dict]:
        """
        توليد معادلات الخطوط بتنويعات مختلفة
        """
        equations = []

        # تنويعات الميل
        slopes = np.linspace(-3.0, 3.0, 25)

        # تنويعات التقاطع
        intercepts = np.linspace(-2.0, 2.0, 15)

        # أنماط الخطوط
        line_types = ['straight', 'curved']

        for i, slope in enumerate(slopes):
            for j, intercept in enumerate(intercepts):
                for k, line_type in enumerate(line_types):

                    if line_type == 'straight':
                        linear_params = [
                            {
                                'beta': slope,
                                'gamma': intercept,
                                'n': 1,
                                'component_type': 'straight_line'
                            }
                        ]
                        sigmoid_params = []

                    else:  # curved
                        # خط منحني باستخدام سيجمويد
                        sigmoid_params = [
                            {
                                'alpha': slope,
                                'k': 1.0,
                                'x0': 0,
                                'n': 1,
                                'component_type': 'curved_line'
                            }
                        ]
                        linear_params = [
                            {
                                'beta': 0,
                                'gamma': intercept,
                                'n': 1,
                                'component_type': 'offset'
                            }
                        ]

                    equation = {
                        'id': f'line_{i}_{j}_{k}',
                        'shape_type': 'line',
                        'parameters': {
                            'slope': slope,
                            'intercept': intercept,
                            'line_type': line_type,
                            'sigmoid_components': sigmoid_params,
                            'linear_components': linear_params
                        },
                        'properties': {
                            'closed': False,
                            'symmetric': False,
                            'complexity': 'simple'
                        }
                    }

                    equations.append(equation)

                    if len(equations) >= self.library_config['max_equations_per_shape']:
                        return equations

        return equations

    def _generate_complex_equations(self) -> List[Dict]:
        """
        توليد معادلات الأشكال المركبة
        """
        equations = []

        # دمج أشكال متعددة
        shape_combinations = [
            ['circle', 'line'],
            ['heart', 'circle'],
            ['flower', 'spiral'],
            ['wave', 'circle']
        ]

        for i, combination in enumerate(shape_combinations):
            for j in range(50):  # 50 تنويع لكل دمج
                # دمج معاملات من أشكال مختلفة
                sigmoid_params = []
                linear_params = []

                # إضافة مكونات أساسية
                sigmoid_params.append({
                    'alpha': 1.0,
                    'k': 2.0,
                    'x0': 0,
                    'n': 1,
                    'component_type': f'{combination[0]}_component'
                })

                linear_params.append({
                    'beta': 0.5,
                    'gamma': 0,
                    'n': 1,
                    'component_type': f'{combination[1]}_component'
                })

                equation = {
                    'id': f'complex_{i}_{j}',
                    'shape_type': 'complex',
                    'parameters': {
                        'combination': combination,
                        'sigmoid_components': sigmoid_params,
                        'linear_components': linear_params
                    },
                    'properties': {
                        'closed': False,
                        'symmetric': False,
                        'complexity': 'high'
                    }
                }

                equations.append(equation)

                if len(equations) >= self.library_config['max_equations_per_shape']:
                    return equations

        return equations

    def _generate_geometric_equations(self) -> List[Dict]:
        """
        توليد معادلات الأشكال الهندسية الأساسية
        """
        equations = []

        # مثلثات، مربعات، مضلعات
        polygon_sides = range(3, 9)
        sizes = np.linspace(0.5, 2.0, 10)

        for sides in polygon_sides:
            for size in sizes:
                # إنشاء مضلع منتظم
                sigmoid_params = []

                for vertex in range(min(sides, 4)):  # حد أقصى 4 رؤوس لتبسيط
                    angle = 2 * np.pi * vertex / sides

                    sigmoid_params.append({
                        'alpha': size,
                        'k': 5.0,  # حاد للزوايا
                        'x0': angle,
                        'n': 1,
                        'component_type': f'vertex_{vertex}'
                    })

                equation = {
                    'id': f'polygon_{sides}_{len(equations)}',
                    'shape_type': 'polygon',
                    'parameters': {
                        'sides': sides,
                        'size': size,
                        'sigmoid_components': sigmoid_params,
                        'linear_components': []
                    },
                    'properties': {
                        'closed': True,
                        'symmetric': True,
                        'complexity': 'medium'
                    }
                }

                equations.append(equation)

                if len(equations) >= self.library_config['max_equations_per_shape']:
                    return equations

        return equations

    def search_best_match(self, target_x: np.ndarray, target_y: np.ndarray,
                         shape_hint: str = None) -> Dict[str, Any]:
        """
        البحث عن أفضل معادلة مطابقة للبيانات المستهدفة
        الاستراتيجية: تجربة كل معادلة حتى العثور على تطابق مقبول
        """
        import time
        search_start_time = time.time()

        print(f"🔍 بدء البحث في مكتبة المعادلات...")
        print(f"📊 البيانات المستهدفة: {len(target_x)} نقطة")
        print(f"⏰ حد أقصى للبحث: {self.library_config['max_search_time']} ثانية")

        best_match = {
            'equation': None,
            'accuracy': 0.0,
            'shape_type': 'unknown',
            'parameters': {},
            'search_stats': {
                'equations_tested': 0,
                'categories_searched': 0,
                'best_category': None
            }
        }

        # تحديد فئات البحث
        search_categories = []
        if shape_hint and shape_hint in self.equation_library:
            # البحث في الفئة المحددة أولاً
            search_categories.append(shape_hint)
            # ثم باقي الفئات
            search_categories.extend([cat for cat in self.equation_library.keys() if cat != shape_hint])
        else:
            # البحث في جميع الفئات
            search_categories = list(self.equation_library.keys())

        print(f"🎯 فئات البحث: {search_categories}")

        for category in search_categories:
            # فحص الوقت المتبقي
            elapsed_time = time.time() - search_start_time
            if elapsed_time > self.library_config['max_search_time']:
                print(f"⏰ تم الوصول للحد الأقصى للوقت ({elapsed_time:.1f}s)")
                break

            print(f"\n📂 البحث في فئة: {category}")
            category_equations = self.equation_library[category]

            category_best_accuracy = 0.0
            equations_tested_in_category = 0

            for equation in category_equations:
                # فحص الوقت المتبقي
                elapsed_time = time.time() - search_start_time
                if elapsed_time > self.library_config['max_search_time']:
                    print(f"  ⏰ تم الوصول للحد الأقصى للوقت ({elapsed_time:.1f}s)")
                    break

                try:
                    # تطبيق المعادلة على البيانات
                    accuracy = self._test_equation_match(equation, target_x, target_y)
                    equations_tested_in_category += 1
                    best_match['search_stats']['equations_tested'] += 1

                    # تحديث أفضل نتيجة
                    if accuracy > best_match['accuracy']:
                        best_match['accuracy'] = accuracy
                        best_match['equation'] = equation
                        best_match['shape_type'] = equation['shape_type']
                        best_match['parameters'] = equation['parameters']
                        best_match['search_stats']['best_category'] = category

                        print(f"  🎯 تحسن! دقة: {accuracy:.3f} | معادلة: {equation['id']}")

                    if accuracy > category_best_accuracy:
                        category_best_accuracy = accuracy

                    # إذا وصلنا لدقة مقبولة، توقف
                    if accuracy >= self.library_config['accuracy_threshold']:
                        print(f"  ✅ وصلنا للدقة المطلوبة: {accuracy:.3f}")
                        break

                except Exception as e:
                    # تجاهل الأخطاء ومتابعة البحث
                    continue

            best_match['search_stats']['categories_searched'] += 1
            print(f"  📊 تم اختبار {equations_tested_in_category} معادلة | أفضل دقة: {category_best_accuracy:.3f}")

            # إذا وصلنا للدقة المطلوبة، توقف البحث
            if best_match['accuracy'] >= self.library_config['accuracy_threshold']:
                break

        print(f"\n🏆 نتائج البحث:")
        print(f"📊 أفضل دقة: {best_match['accuracy']:.3f}")
        print(f"🔍 معادلات مختبرة: {best_match['search_stats']['equations_tested']}")
        print(f"📂 فئات مبحوثة: {best_match['search_stats']['categories_searched']}")
        print(f"🎯 أفضل فئة: {best_match['search_stats']['best_category']}")

        return best_match

    def _test_equation_match(self, equation: Dict, target_x: np.ndarray, target_y: np.ndarray) -> float:
        """
        اختبار مدى تطابق معادلة مع البيانات المستهدفة
        """
        try:
            # توليد البيانات من المعادلة
            generated_x, generated_y = self._generate_data_from_equation(equation, len(target_x))

            # حساب دقة التطابق
            accuracy = self._calculate_match_accuracy(target_x, target_y, generated_x, generated_y)

            return accuracy

        except Exception as e:
            return 0.0

    def _generate_data_from_equation(self, equation: Dict, num_points: int) -> Tuple[np.ndarray, np.ndarray]:
        """
        توليد بيانات من معادلة محددة
        """
        renderer = BaserahArtisticRenderer()

        # إنشاء نقاط المعاينة
        t = np.linspace(0, 2*np.pi, num_points)

        shape_type = equation['shape_type']
        params = equation['parameters']

        try:
            if shape_type == 'circle':
                size = params.get('size', 1.0)
                x = renderer.sigmoid_wave_approximation(t, amplitude=size, frequency=1.0, phase=np.pi/2, steepness=2.0)
                y = renderer.sigmoid_wave_approximation(t, amplitude=size, frequency=1.0, phase=0.0, steepness=2.0)

            elif shape_type == 'heart':
                size = params.get('size', 1.0)
                style = params.get('style', 'classic')
                x, y = renderer.create_heart_shape(t, size, style)

            elif shape_type == 'flower':
                petals = params.get('petals', 5)
                size = params.get('size', 1.0)
                style = params.get('style', 'rose')
                x, y = renderer.create_flower_shape(t, petals, size, style)

            elif shape_type == 'spiral':
                turns = params.get('turns', 3)
                size = params.get('size', 1.0)
                style = params.get('style', 'fibonacci')
                x, y = renderer.create_spiral_shape(t, turns, size, style)

            elif shape_type == 'wave':
                amplitude = params.get('amplitude', 1.0)
                frequency = params.get('frequency', 1.0)
                x = t
                y = renderer.create_wave_pattern(x, amplitude, frequency, style='sine')

            elif shape_type == 'line':
                slope = params.get('slope', 1.0)
                intercept = params.get('intercept', 0.0)
                x = t
                y = slope * x + intercept

            else:
                # شكل افتراضي
                x = np.cos(t)
                y = np.sin(t)

            return np.array(x), np.array(y)

        except Exception as e:
            # في حالة الخطأ، إرجاع دائرة افتراضية
            x = np.cos(t)
            y = np.sin(t)
            return np.array(x), np.array(y)

    def _calculate_match_accuracy(self, target_x: np.ndarray, target_y: np.ndarray,
                                 generated_x: np.ndarray, generated_y: np.ndarray) -> float:
        """
        حساب دقة التطابق بين البيانات المستهدفة والمولدة
        """
        try:
            # تطبيع البيانات للمقارنة
            target_x_norm = self._normalize_data(target_x)
            target_y_norm = self._normalize_data(target_y)
            generated_x_norm = self._normalize_data(generated_x)
            generated_y_norm = self._normalize_data(generated_y)

            # حساب المسافة الإقليدية
            if len(target_x_norm) != len(generated_x_norm):
                # إعادة أخذ عينات للحصول على نفس الطول
                from scipy.interpolate import interp1d

                # إنشاء دوال الاستيفاء
                t_target = np.linspace(0, 1, len(target_x_norm))
                t_generated = np.linspace(0, 1, len(generated_x_norm))

                f_gen_x = interp1d(t_generated, generated_x_norm, kind='linear', fill_value='extrapolate')
                f_gen_y = interp1d(t_generated, generated_y_norm, kind='linear', fill_value='extrapolate')

                generated_x_resampled = f_gen_x(t_target)
                generated_y_resampled = f_gen_y(t_target)
            else:
                generated_x_resampled = generated_x_norm
                generated_y_resampled = generated_y_norm

            # حساب المسافة
            distance_x = np.mean((target_x_norm - generated_x_resampled) ** 2)
            distance_y = np.mean((target_y_norm - generated_y_resampled) ** 2)

            total_distance = np.sqrt(distance_x + distance_y)

            # تحويل المسافة إلى دقة (0-1)
            accuracy = max(0, 1 - total_distance)

            return accuracy

        except Exception as e:
            return 0.0

    def _normalize_data(self, data: np.ndarray) -> np.ndarray:
        """
        تطبيع البيانات للمقارنة
        """
        try:
            data_range = np.ptp(data)
            if data_range > 0:
                return (data - np.min(data)) / data_range
            else:
                return data - np.mean(data)
        except:
            return data

    def get_library_stats(self) -> Dict[str, Any]:
        """
        إحصائيات المكتبة
        """
        stats = {
            'total_equations': 0,
            'categories': {},
            'complexity_distribution': {'simple': 0, 'medium': 0, 'high': 0, 'very_high': 0}
        }

        for category, equations in self.equation_library.items():
            stats['categories'][category] = len(equations)
            stats['total_equations'] += len(equations)

            for equation in equations:
                complexity = equation['properties'].get('complexity', 'medium')
                if complexity in stats['complexity_distribution']:
                    stats['complexity_distribution'][complexity] += 1

        return stats
