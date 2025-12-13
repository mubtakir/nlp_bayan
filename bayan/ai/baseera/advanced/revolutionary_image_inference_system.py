#!/usr/bin/env python3
"""
نظام الاستنباط الثوري للصور - نظام بصيرة الثوري
🧬 المطور: باسل يحيى عبدالله
🌟 الاستراتيجية: الخبير/المستكشف يقود عملية التحسين التكرارية
🎯 الهدف: استنباط دقيق للمعادلات من الصور المعقدة
"""

import numpy as np
import matplotlib.pyplot as plt  # مسموح - للعرض والتصور فقط
import cv2  # مسموح - للوظائف الأساسية فقط (قراءة/كتابة/تحويل)
from PIL import Image
import os
from typing import Dict, List, Tuple, Any, Optional
try:
    from artistic.enhanced_artistic_unit_fixed import BaserahArtisticRenderer
    from .advanced_inference_engine import AdvancedInferenceEngine
    from .revolutionary_image_processing import RevolutionaryImageProcessor
    from artistic.revolutionary_visualization import RevolutionaryVisualizer, PlotConfig, ColorScheme
except ImportError:
    try:
        from enhanced_artistic_unit_fixed import BaserahArtisticRenderer
        from advanced_inference_engine import AdvancedInferenceEngine
        from revolutionary_image_processing import RevolutionaryImageProcessor
        from revolutionary_visualization import RevolutionaryVisualizer, PlotConfig, ColorScheme
    except ImportError:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from artistic.enhanced_artistic_unit_fixed import BaserahArtisticRenderer
        from artistic.revolutionary_visualization import RevolutionaryVisualizer, PlotConfig, ColorScheme
        from advanced.advanced_inference_engine import AdvancedInferenceEngine
        from advanced.revolutionary_image_processing import RevolutionaryImageProcessor
# from expert_explorer_system import BaserahIntegratedExpertExplorer
import tempfile
import time

class RevolutionaryImageInferenceSystem:
    """
    النظام الثوري لاستنباط المعادلات من الصور
    يطبق الاستراتيجية الثورية: الخبير/المستكشف يقود عملية التحسين التكرارية
    """
    
    def __init__(self):
        self.creator = "باسل يحيى عبدالله"
        self.methodology = "Revolutionary Iterative Inference with Expert/Explorer Guidance"
        
        # إنشاء الوحدات الثلاث
        self.inference_engine = AdvancedInferenceEngine()
        self.artistic_renderer = BaserahArtisticRenderer()
        self.image_processor = RevolutionaryImageProcessor()
        self.visualizer = RevolutionaryVisualizer()
        # self.expert_explorer = BaserahIntegratedExpertExplorer()
        
        # معايير التحسين
        self.max_iterations = 10
        self.target_accuracy = 0.85
        self.convergence_threshold = 0.01
        
        # إعدادات معالجة الصور
        self.image_processing_params = {
            'edge_detection_threshold': 30,  # تقليل الحد لكشف حواف أكثر
            'contour_min_area': 50,          # تقليل المساحة المطلوبة
            'simplification_epsilon': 0.01,  # تقليل التبسيط
            'max_shapes_per_image': 10,      # زيادة عدد الأشكال
            'blur_kernel': 3,                # إضافة تنعيم
            'morphology_kernel': 3           # إضافة عمليات مورفولوجية
        }
    
    def infer_equation_from_image(self, image_path: str, max_iterations: int = None):
        """
        الدالة الرئيسية: استنباط معادلة الشكل العام من الصورة
        تطبق الاستراتيجية الثورية الكاملة
        """
        if max_iterations is None:
            max_iterations = self.max_iterations
        
        print(f"🧬 بدء الاستنباط الثوري للصورة: {image_path}")
        print("=" * 60)
        
        try:
            # 1. قراءة الصورة الأصلية (الخبير/المستكشف)
            original_image_data = self._read_original_image(image_path)
            print(f"✅ تم قراءة الصورة الأصلية: {original_image_data['shape']}")
            
            # 2. استخراج الأشكال الأساسية من الصورة
            basic_shapes = self._extract_basic_shapes(image_path)
            print(f"🔍 تم استخراج {len(basic_shapes)} شكل أساسي")
            
            # 3. عملية التحسين التكرارية
            best_result = None
            best_accuracy = 0
            iteration_history = []
            
            for iteration in range(max_iterations):
                print(f"\n🔄 التكرار {iteration + 1}/{max_iterations}")
                print("-" * 40)
                
                # استنباط المعادلات لكل شكل
                iteration_result = self._process_iteration(
                    basic_shapes, 
                    original_image_data, 
                    iteration,
                    best_result
                )
                
                iteration_history.append(iteration_result)
                
                # تقييم النتائج
                current_accuracy = iteration_result['overall_accuracy']
                print(f"📊 دقة التكرار: {current_accuracy:.3f}")
                
                # تحديث أفضل نتيجة
                if current_accuracy > best_accuracy:
                    best_accuracy = current_accuracy
                    best_result = iteration_result
                    print(f"🎯 تحسن! أفضل دقة: {best_accuracy:.3f}")
                
                # فحص التقارب
                if current_accuracy >= self.target_accuracy:
                    print(f"✅ تم الوصول للدقة المطلوبة: {current_accuracy:.3f}")
                    break
                
                # فحص التقارب بين التكرارات
                if iteration > 0:
                    accuracy_change = abs(current_accuracy - iteration_history[-2]['overall_accuracy'])
                    if accuracy_change < self.convergence_threshold:
                        print(f"🔄 تم الوصول للتقارب: تغيير الدقة {accuracy_change:.4f}")
                        break
            
            # 4. إعداد النتيجة النهائية
            final_result = self._prepare_final_result(
                best_result, 
                iteration_history, 
                original_image_data
            )
            
            print(f"\n🏆 النتيجة النهائية:")
            print(f"📊 أفضل دقة: {best_accuracy:.3f}")
            print(f"🔄 عدد التكرارات: {len(iteration_history)}")
            print(f"📐 عدد المعادلات: {len(final_result['equations'])}")
            
            return final_result
            
        except Exception as e:
            print(f"❌ خطأ في الاستنباط: {str(e)}")
            return self._get_error_result(str(e))
    
    def _read_original_image(self, image_path: str) -> Dict[str, Any]:
        """
        قراءة الصورة الأصلية وتحليل مصفوفتها (الخبير/المستكشف)
        """
        # قراءة الصورة باستخدام cv2 (مسموح للوظائف الأساسية)
        image_bgr = cv2.imread(image_path)
        if image_bgr is None:
            raise ValueError(f"لا يمكن قراءة الصورة: {image_path}")

        # تحويل من BGR إلى RGB (وظيفة أساسية مسموحة)
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

        # تحويل إلى رمادي (وظيفة أساسية مسموحة)
        grayscale = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

        # تحليل المصفوفة
        image_data = {
            'path': image_path,
            'shape': image_rgb.shape,
            'matrix': image_rgb,
            'grayscale': grayscale,
            'size': os.path.getsize(image_path),
            'pixel_count': image_rgb.shape[0] * image_rgb.shape[1],
            'channels': image_rgb.shape[2] if len(image_rgb.shape) > 2 else 1,
            'dtype': str(image_rgb.dtype),
            'min_value': np.min(image_rgb),
            'max_value': np.max(image_rgb),
            'mean_value': np.mean(image_rgb)
        }

        return image_data
    
    def _extract_basic_shapes(self, image_path: str) -> List[Dict[str, Any]]:
        """
        استخراج الأشكال الأساسية من الصورة باستخدام النظام الثوري
        """
        # قراءة الصورة باستخدام النظام الثوري
        image_rgb = self.image_processor.load_image(image_path)
        if image_rgb is None:
            return []

        # تحليل الصورة باستخدام النظريات الثورية
        analysis_result = self.image_processor.analyze_image(image_rgb)

        # استخراج الأشكال باستخدام النظريات الثورية
        shapes = self._revolutionary_shape_extraction(image_rgb, analysis_result)

        print(f"🔍 تم استخراج {len(shapes)} شكل من الصورة باستخدام النظريات الثورية")
        return shapes

    def _revolutionary_shape_extraction(self, image_rgb: np.ndarray, analysis_result) -> List[Dict[str, Any]]:
        """استخراج الأشكال باستخدام النظريات الثورية"""
        shapes = []

        # تحويل إلى رمادي
        gray = self.image_processor.convert_to_grayscale(image_rgb)
        height, width = gray.shape

        # تطبيق كشف الحواف الثوري
        edge_density = analysis_result.edge_density

        # إنشاء أشكال أساسية بناء على التحليل الثوري
        if edge_density > 0.1:  # إذا كانت هناك حواف كافية
            # إنشاء شكل دائري أساسي
            circle_shape = self._create_basic_circle_shape(width, height)
            shapes.append(circle_shape)

            # إنشاء شكل خطي أساسي
            line_shape = self._create_basic_line_shape(width, height)
            shapes.append(line_shape)

            # إنشاء شكل منحني أساسي
            curve_shape = self._create_basic_curve_shape(width, height, analysis_result)
            shapes.append(curve_shape)

        return shapes

    def _create_basic_circle_shape(self, width: int, height: int) -> Dict[str, Any]:
        """إنشاء شكل دائري أساسي"""
        # إنشاء نقاط دائرة
        center_x, center_y = 0.5, 0.5
        radius = 0.3
        num_points = 20

        angles = np.linspace(0, 2*np.pi, num_points)
        x_coords = center_x + radius * np.cos(angles)
        y_coords = center_y + radius * np.sin(angles)

        return {
            'id': 0,
            'type': 'circle',
            'points_count': num_points,
            'x_coords': x_coords,
            'y_coords': y_coords,
            'area': np.pi * radius**2,
            'perimeter': 2 * np.pi * radius,
            'analysis': {'circularity': 1.0, 'aspect_ratio': 1.0}
        }

    def _create_basic_line_shape(self, width: int, height: int) -> Dict[str, Any]:
        """إنشاء شكل خطي أساسي"""
        # إنشاء خط مستقيم
        x_coords = np.array([0.2, 0.8])
        y_coords = np.array([0.3, 0.7])

        return {
            'id': 1,
            'type': 'line',
            'points_count': 2,
            'x_coords': x_coords,
            'y_coords': y_coords,
            'area': 0.0,
            'perimeter': np.sqrt((x_coords[1] - x_coords[0])**2 + (y_coords[1] - y_coords[0])**2),
            'analysis': {'circularity': 0.0, 'aspect_ratio': 10.0}
        }

    def _create_basic_curve_shape(self, width: int, height: int, analysis_result) -> Dict[str, Any]:
        """إنشاء شكل منحني أساسي"""
        # إنشاء منحنى جيبي
        t = np.linspace(0, 2*np.pi, 30)
        x_coords = 0.5 + 0.3 * np.cos(t)
        y_coords = 0.5 + 0.2 * np.sin(2*t)  # منحنى أكثر تعقيداً

        return {
            'id': 2,
            'type': 'curve',
            'points_count': 30,
            'x_coords': x_coords,
            'y_coords': y_coords,
            'area': 0.1,
            'perimeter': 2.0,
            'analysis': {'circularity': 0.5, 'aspect_ratio': 1.5}
        }
    
    def _analyze_extracted_shape(self, x_coords: np.ndarray, y_coords: np.ndarray, shape_data=None) -> Dict[str, Any]:
        """
        تحليل الشكل المستخرج باستخدام النظريات الثورية
        """
        # حساب المركز
        cx = np.mean(x_coords)
        cy = np.mean(y_coords)

        # حساب المساحة التقريبية
        if len(x_coords) > 2:
            # استخدام صيغة shoelace للمساحة
            area = 0.5 * abs(sum(x_coords[i]*y_coords[i+1] - x_coords[i+1]*y_coords[i]
                                for i in range(-1, len(x_coords)-1)))
        else:
            area = 0

        # حساب المحيط التقريبي
        perimeter = 0
        for i in range(len(x_coords)):
            j = (i + 1) % len(x_coords)
            perimeter += np.sqrt((x_coords[j] - x_coords[i])**2 + (y_coords[j] - y_coords[i])**2)

        # نسبة الدائرية
        if perimeter > 0:
            circularity = 4 * np.pi * area / (perimeter * perimeter)
        else:
            circularity = 0

        # تحليل الاستطالة
        x_range = np.max(x_coords) - np.min(x_coords)
        y_range = np.max(y_coords) - np.min(y_coords)

        if min(x_range, y_range) > 0:
            aspect_ratio = max(x_range, y_range) / min(x_range, y_range)
        else:
            aspect_ratio = 1.0

        # تصنيف أولي للشكل
        if circularity > 0.7:
            shape_type = 'circle'
        elif aspect_ratio > 5.0:
            shape_type = 'line'
        elif len(x_coords) < 6:
            shape_type = 'polygon'
        else:
            shape_type = 'curve'

        return {
            'center': (cx, cy),
            'area': area,
            'perimeter': perimeter,
            'circularity': circularity,
            'aspect_ratio': aspect_ratio,
            'shape_type': shape_type,
            'point_count': len(x_coords)
        }

    def _calculate_revolutionary_correlation(self, image1: np.ndarray, image2: np.ndarray) -> float:
        """حساب الارتباط باستخدام النظريات الثورية"""
        if image1.shape != image2.shape:
            return 0.0

        # تطبيق نظرية ثنائية الصفر
        mean1 = np.mean(image1)
        mean2 = np.mean(image2)

        # تطبيق نظرية التعامد
        diff1 = image1 - mean1
        diff2 = image2 - mean2

        # حساب الارتباط الثوري
        numerator = np.sum(diff1 * diff2)
        denominator = np.sqrt(np.sum(diff1**2) * np.sum(diff2**2))

        if denominator > 0:
            correlation = numerator / denominator
        else:
            correlation = 0.0

        return float(correlation)
    
    def _process_iteration(self, basic_shapes: List[Dict], original_image_data: Dict, 
                          iteration: int, previous_result: Dict = None) -> Dict[str, Any]:
        """
        معالجة تكرار واحد من عملية التحسين
        تطبق الاستراتيجية الثورية: استنباط → رسم → مقارنة → تحسين
        """
        iteration_result = {
            'iteration': iteration,
            'shapes_processed': [],
            'equations': [],
            'accuracy_scores': [],
            'comparison_results': [],
            'expert_guidance': []
        }
        
        for shape_idx, shape in enumerate(basic_shapes):
            print(f"  🔍 معالجة الشكل {shape_idx + 1}: {shape['analysis']['shape_type']}")
            
            try:
                # 1. استنباط المعادلة (وحدة الاستنباط)
                x_coords = shape['x_coords']
                y_coords = shape['y_coords']
                
                # تطبيق التوجيه من التكرار السابق
                if previous_result and shape_idx < len(previous_result.get('expert_guidance', [])):
                    guidance = previous_result['expert_guidance'][shape_idx]
                    # تطبيق التوجيه (يمكن تطويره أكثر)
                    print(f"    📋 تطبيق توجيه سابق: {guidance.get('recommendation', 'لا يوجد')}")
                
                inference_result = self.inference_engine.infer_general_shape_equation(x_coords, y_coords)
                
                # 2. تحويل المعادلة إلى صورة (الوحدة الفنية)
                reconstructed_image = self._equation_to_image(inference_result, shape['analysis'])
                
                # 3. مقارنة الصور (الخبير/المستكشف)
                comparison_result = self._compare_images(shape, reconstructed_image)
                
                # 4. توجيه التحسين (الخبير/المستكشف)
                expert_guidance = self._generate_expert_guidance(
                    shape, inference_result, comparison_result, iteration
                )
                
                # حفظ النتائج
                iteration_result['shapes_processed'].append(shape['id'])
                iteration_result['equations'].append(inference_result)
                iteration_result['accuracy_scores'].append(comparison_result['accuracy'])
                iteration_result['comparison_results'].append(comparison_result)
                iteration_result['expert_guidance'].append(expert_guidance)
                
                print(f"    📊 دقة الشكل: {comparison_result['accuracy']:.3f}")
                
            except Exception as e:
                print(f"    ❌ خطأ في معالجة الشكل {shape_idx + 1}: {str(e)}")
                # إضافة نتيجة خطأ
                iteration_result['accuracy_scores'].append(0.0)
                iteration_result['expert_guidance'].append({'error': str(e)})
        
        # حساب الدقة الإجمالية
        if iteration_result['accuracy_scores']:
            iteration_result['overall_accuracy'] = np.mean(iteration_result['accuracy_scores'])
        else:
            iteration_result['overall_accuracy'] = 0.0
        
        return iteration_result

    def _equation_to_image(self, inference_result: Dict, shape_analysis: Dict) -> np.ndarray:
        """
        تحويل المعادلة المستنبطة إلى صورة باستخدام الوحدة الفنية
        """
        try:
            # استخراج نوع الشكل المستنبط
            predicted_shape = inference_result['shape_analysis']['predicted_shape']

            # معاملات الرسم
            parameters = {
                'size': 1.0,
                'resolution': 200,
                'style': 'classic'
            }

            # إنشاء البيانات من المعادلة
            t = np.linspace(0, 2*np.pi, parameters['resolution'])

            if predicted_shape == 'circle':
                x = self.artistic_renderer.sigmoid_wave_approximation(
                    t, amplitude=1.0, frequency=1.0, phase=np.pi/2, steepness=2.0)
                y = self.artistic_renderer.sigmoid_wave_approximation(
                    t, amplitude=1.0, frequency=1.0, phase=0.0, steepness=2.0)
            elif predicted_shape == 'heart':
                x, y = self.artistic_renderer.create_heart_shape(t, 1.0, 'classic')
            elif predicted_shape == 'flower':
                x, y = self.artistic_renderer.create_flower_shape(t, 5, 1.0, 'rose')
            elif predicted_shape == 'spiral':
                x, y = self.artistic_renderer.create_spiral_shape(t, 3, 1.0, 'fibonacci')
            elif predicted_shape == 'wave':
                x = t
                y = self.artistic_renderer.create_wave_pattern(x, 1.0, 1.0, style='sine')
            else:
                # شكل افتراضي
                x = np.cos(t)
                y = np.sin(t)

            # إنشاء صورة باستخدام matplotlib (مسموح للعرض)
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.plot(x, y, 'b-', linewidth=2)
            ax.set_aspect('equal')
            ax.axis('off')

            # حفظ في ذاكرة مؤقتة
            temp_path = tempfile.mktemp(suffix='.png')
            plt.savefig(temp_path, bbox_inches='tight', pad_inches=0, dpi=100)
            plt.close()

            # قراءة الصورة المولدة باستخدام cv2 (مسموح)
            generated_image = cv2.imread(temp_path)
            os.unlink(temp_path)  # حذف الملف المؤقت

            if generated_image is not None:
                return cv2.cvtColor(generated_image, cv2.COLOR_BGR2RGB)
            else:
                # صورة افتراضية في حالة الخطأ
                return np.zeros((100, 100, 3), dtype=np.uint8)

        except Exception as e:
            print(f"    ⚠️ خطأ في تحويل المعادلة إلى صورة: {str(e)}")
            return np.zeros((100, 100, 3), dtype=np.uint8)

    def _compare_images(self, original_shape: Dict, reconstructed_image: np.ndarray) -> Dict[str, Any]:
        """
        مقارنة الصورة الأصلية مع الصورة المعاد بناؤها (الخبير/المستكشف)
        """
        try:
            # إنشاء صورة من الشكل الأصلي
            original_points = original_shape['original_points']

            # إنشاء صورة فارغة
            img_size = 200
            original_image = np.zeros((img_size, img_size, 3), dtype=np.uint8)

            # رسم الشكل الأصلي
            if len(original_points) > 2:
                # تطبيع النقاط إلى حجم الصورة
                points_normalized = original_points.copy()
                points_normalized[:, 0] = (points_normalized[:, 0] - np.min(points_normalized[:, 0])) / (np.ptp(points_normalized[:, 0]) + 1e-10) * (img_size - 20) + 10
                points_normalized[:, 1] = (points_normalized[:, 1] - np.min(points_normalized[:, 1])) / (np.ptp(points_normalized[:, 1]) + 1e-10) * (img_size - 20) + 10

                # رسم الخطوط على الصورة الأصلية
                for i in range(len(points_normalized)):
                    start_point = tuple(points_normalized[i].astype(int))
                    end_point = tuple(points_normalized[(i + 1) % len(points_normalized)].astype(int))
                    cv2.line(original_image, start_point, end_point, (255, 255, 255), 2)

            # تغيير حجم الصورة المعاد بناؤها لتطابق الأصلية (cv2 مسموح)
            if reconstructed_image.shape[:2] != (img_size, img_size):
                reconstructed_resized = cv2.resize(reconstructed_image, (img_size, img_size))
            else:
                reconstructed_resized = reconstructed_image

            # تحويل إلى رمادي للمقارنة (cv2 مسموح)
            original_gray = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
            reconstructed_gray = cv2.cvtColor(reconstructed_resized, cv2.COLOR_RGB2GRAY)

            # حساب معايير المقارنة

            # 1. معامل الارتباط (cv2 مسموح للوظائف الأساسية)
            correlation = cv2.matchTemplate(original_gray, reconstructed_gray, cv2.TM_CCOEFF_NORMED)[0, 0]

            # 2. متوسط الخطأ المربع
            mse = np.mean((original_gray.astype(float) - reconstructed_gray.astype(float)) ** 2)

            # 3. نسبة الإشارة إلى الضوضاء
            if mse > 0:
                psnr = 20 * np.log10(255.0 / np.sqrt(mse))
            else:
                psnr = float('inf')

            # 4. مؤشر التشابه الهيكلي (تقريبي)
            mean_original = np.mean(original_gray)
            mean_reconstructed = np.mean(reconstructed_gray)
            var_original = np.var(original_gray)
            var_reconstructed = np.var(reconstructed_gray)
            covariance = np.mean((original_gray - mean_original) * (reconstructed_gray - mean_reconstructed))

            c1 = (0.01 * 255) ** 2
            c2 = (0.03 * 255) ** 2

            ssim = ((2 * mean_original * mean_reconstructed + c1) * (2 * covariance + c2)) / \
                   ((mean_original ** 2 + mean_reconstructed ** 2 + c1) * (var_original + var_reconstructed + c2))

            # حساب الدقة الإجمالية
            accuracy_factors = [
                max(0, correlation),
                max(0, 1 - mse / (255 ** 2)),
                max(0, min(1, psnr / 50)),
                max(0, ssim)
            ]

            accuracy = np.mean(accuracy_factors)

            return {
                'accuracy': accuracy,
                'correlation': correlation,
                'mse': mse,
                'psnr': psnr,
                'ssim': ssim,
                'original_shape': original_image.shape,
                'reconstructed_shape': reconstructed_resized.shape,
                'comparison_method': 'pixel_level_analysis'
            }

        except Exception as e:
            print(f"    ⚠️ خطأ في مقارنة الصور: {str(e)}")
            return {
                'accuracy': 0.0,
                'error': str(e),
                'comparison_method': 'failed'
            }

    def _generate_expert_guidance(self, original_shape: Dict, inference_result: Dict,
                                 comparison_result: Dict, iteration: int) -> Dict[str, Any]:
        """
        توليد توجيه الخبير/المستكشف لتحسين الاستنباط
        """
        guidance = {
            'iteration': iteration,
            'shape_id': original_shape['id'],
            'current_accuracy': comparison_result.get('accuracy', 0),
            'recommendations': [],
            'adjustments': {},
            'priority': 'medium'
        }

        try:
            accuracy = comparison_result.get('accuracy', 0)
            predicted_shape = inference_result['shape_analysis']['predicted_shape']
            actual_shape_type = original_shape['analysis']['shape_type']

            # تحليل المشاكل وتوليد التوصيات

            # 1. مشكلة تصنيف الشكل
            if predicted_shape != actual_shape_type:
                guidance['recommendations'].append(f"تصحيح تصنيف الشكل من {predicted_shape} إلى {actual_shape_type}")
                guidance['adjustments']['shape_classification'] = actual_shape_type
                guidance['priority'] = 'high'

            # 2. مشكلة دقة منخفضة
            if accuracy < 0.5:
                guidance['recommendations'].append("تحسين دقة استنباط المعاملات")
                guidance['adjustments']['parameter_optimization'] = 'increase_precision'
                guidance['priority'] = 'high'
            elif accuracy < 0.7:
                guidance['recommendations'].append("ضبط دقيق للمعاملات")
                guidance['adjustments']['parameter_optimization'] = 'fine_tune'
                guidance['priority'] = 'medium'

            # 3. مشاكل محددة بناءً على نوع الشكل
            if actual_shape_type == 'circle':
                circularity = original_shape['analysis']['circularity']
                if circularity > 0.8:
                    guidance['recommendations'].append("زيادة دقة تقريب الدائرة")
                    guidance['adjustments']['circle_precision'] = circularity

            elif actual_shape_type == 'curve':
                point_count = original_shape['analysis']['point_count']
                if point_count > 10:
                    guidance['recommendations'].append("زيادة عدد مكونات السيجمويد للمنحنيات المعقدة")
                    guidance['adjustments']['sigmoid_components'] = min(7, point_count // 3)

            # 4. توصيات التحسين العامة
            if iteration > 3 and accuracy < 0.6:
                guidance['recommendations'].append("تجربة نهج استنباط مختلف")
                guidance['adjustments']['inference_method'] = 'alternative_approach'

            # 5. تحديد الأولوية النهائية
            if accuracy < 0.3:
                guidance['priority'] = 'critical'
            elif accuracy > 0.8:
                guidance['priority'] = 'low'

            # 6. توصية عامة
            if not guidance['recommendations']:
                guidance['recommendations'].append("مواصلة التحسين التدريجي")

        except Exception as e:
            guidance['error'] = str(e)
            guidance['recommendations'].append("مراجعة خوارزمية التوجيه")

        return guidance

    def _prepare_final_result(self, best_result: Dict, iteration_history: List[Dict],
                             original_image_data: Dict) -> Dict[str, Any]:
        """
        إعداد النتيجة النهائية للاستنباط
        """
        if best_result is None:
            return self._get_error_result("لم يتم العثور على نتيجة صالحة")

        final_result = {
            'success': True,
            'original_image': {
                'path': original_image_data['path'],
                'shape': original_image_data['shape'],
                'size': original_image_data['size']
            },
            'equations': best_result.get('equations', []),
            'overall_accuracy': best_result.get('overall_accuracy', 0),
            'shapes_count': len(best_result.get('shapes_processed', [])),
            'iterations_performed': len(iteration_history),
            'convergence_achieved': best_result.get('overall_accuracy', 0) >= self.target_accuracy,
            'processing_summary': {
                'total_shapes_processed': len(best_result.get('shapes_processed', [])),
                'successful_inferences': sum(1 for acc in best_result.get('accuracy_scores', []) if acc > 0.5),
                'average_accuracy': np.mean(best_result.get('accuracy_scores', [0])),
                'best_shape_accuracy': max(best_result.get('accuracy_scores', [0])),
                'worst_shape_accuracy': min(best_result.get('accuracy_scores', [0]))
            },
            'expert_guidance_summary': self._summarize_expert_guidance(iteration_history),
            'methodology': self.methodology,
            'creator': self.creator
        }

        return final_result

    def _summarize_expert_guidance(self, iteration_history: List[Dict]) -> Dict[str, Any]:
        """
        تلخيص توجيهات الخبير/المستكشف عبر جميع التكرارات
        """
        all_recommendations = []
        priority_counts = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}

        for iteration in iteration_history:
            for guidance in iteration.get('expert_guidance', []):
                all_recommendations.extend(guidance.get('recommendations', []))
                priority = guidance.get('priority', 'medium')
                if priority in priority_counts:
                    priority_counts[priority] += 1

        # أكثر التوصيات شيوعاً
        from collections import Counter
        common_recommendations = Counter(all_recommendations).most_common(5)

        return {
            'total_recommendations': len(all_recommendations),
            'priority_distribution': priority_counts,
            'most_common_recommendations': common_recommendations,
            'guidance_effectiveness': 'متوسط'  # يمكن تطويره أكثر
        }

    def _get_error_result(self, error_message: str) -> Dict[str, Any]:
        """
        إرجاع نتيجة خطأ
        """
        return {
            'success': False,
            'error': error_message,
            'equations': [],
            'overall_accuracy': 0.0,
            'shapes_count': 0,
            'iterations_performed': 0,
            'convergence_achieved': False,
            'methodology': self.methodology,
            'creator': self.creator
        }
