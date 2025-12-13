#!/usr/bin/env python3
"""
النظام الثوري المحسن لاستنباط المعادلات من الصور
🧬 المطور: باسل يحيى عبدالله
🌟 الاستراتيجية المحسنة: الطرق المعتادة أولاً، ثم المكتبة المرجعية
🎯 الهدف: دقة عالية مضمونة باستخدام الحل الأخير
"""

import numpy as np
import os
from typing import Dict, List, Tuple, Any, Optional
import tempfile
import time
try:
    from .revolutionary_image_inference_system import RevolutionaryImageInferenceSystem
    from core.revolutionary_equation_library import RevolutionaryEquationLibrary
    from .revolutionary_image_processing import RevolutionaryImageProcessor
    from artistic.revolutionary_visualization import RevolutionaryVisualizer, PlotConfig, ColorScheme
    from artistic.enhanced_artistic_unit_fixed import BaserahArtisticRenderer
except ImportError:
    # Fallback for different execution contexts
    try:
        from revolutionary_image_inference_system import RevolutionaryImageInferenceSystem
        from revolutionary_equation_library import RevolutionaryEquationLibrary
        from revolutionary_image_processing import RevolutionaryImageProcessor
        from revolutionary_visualization import RevolutionaryVisualizer, PlotConfig, ColorScheme
        from enhanced_artistic_unit_fixed import BaserahArtisticRenderer
    except ImportError:
        # Last resort: try adding parent directory to path
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from core.revolutionary_equation_library import RevolutionaryEquationLibrary
        from artistic.revolutionary_visualization import RevolutionaryVisualizer, PlotConfig, ColorScheme
        from artistic.enhanced_artistic_unit_fixed import BaserahArtisticRenderer
        from advanced.revolutionary_image_inference_system import RevolutionaryImageInferenceSystem
        from advanced.revolutionary_image_processing import RevolutionaryImageProcessor

# استيراد sklearn مع معالجة الأخطاء
try:
    from sklearn.cluster import KMeans
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    print("⚠️ sklearn غير متوفر - سيتم استخدام استخراج ألوان مبسط")

class EnhancedRevolutionaryInferenceSystem:
    """
    النظام الثوري المحسن مع المكتبة المرجعية
    يطبق الاستراتيجية المحسنة: الطرق المعتادة أولاً، ثم الحل الأخير
    """
    
    def __init__(self):
        self.creator = "باسل يحيى عبدالله"
        self.methodology = "Enhanced Revolutionary Strategy with Reference Library"
        
        # النظام الأساسي
        self.basic_system = RevolutionaryImageInferenceSystem()
        
        # المكتبة المرجعية
        self.equation_library = RevolutionaryEquationLibrary()
        
        # الوحدة الفنية
        self.artistic_renderer = BaserahArtisticRenderer()
        
        # إعدادات الاستراتيجية المحسنة
        self.enhanced_config = {
            'basic_method_threshold': 0.6,  # حد الدقة للطريقة الأساسية
            'library_search_threshold': 0.5,  # حد الدقة للبحث في المكتبة (مخفض لتجنب الحلقات اللانهائية)
            'max_library_search_time': 60,  # دقيقة واحدة كحد أقصى (مخفض)
            'max_segments_per_search': 10,  # حد أقصى لعدد الأجزاء المعالجة
            'segment_overlap': 0.1,  # تداخل بين أجزاء الصورة
            'min_segment_size': 20,  # حد أدنى لحجم الجزء
            'expert_guidance_weight': 0.3,  # وزن توجيه الخبير
            'background_removal_threshold': 0.1,  # حد تحسن إزالة الخلفية
            'max_background_attempts': 8,  # عدد ألوان الخلفية المختبرة
            'background_tolerance': 15  # تسامح لون الخلفية
        }

        # ألوان الخلفية المختبرة (بترتيب الأولوية)
        self.background_colors = [
            (255, 255, 255),  # أبيض
            (0, 0, 0),        # أسود
            (240, 240, 240),  # رمادي فاتح
            (128, 128, 128),  # رمادي متوسط
            (64, 64, 64),     # رمادي داكن
            (255, 255, 240),  # أبيض مصفر
            (248, 248, 255),  # أبيض مزرق
            (245, 245, 220)   # بيج فاتح
        ]
        
        print(f"🧬 تم إنشاء النظام الثوري المحسن")
        print(f"📚 المكتبة تحتوي على {self.equation_library.get_library_stats()['total_equations']} معادلة")
    
    def infer_equation_from_image_enhanced(self, image_path: str, max_iterations: int = 10):
        """
        الدالة الرئيسية المحسنة: استنباط معادلة الشكل العام من الصورة
        تطبق الاستراتيجية المحسنة الكاملة
        """
        print(f"🧬 بدء الاستنباط الثوري المحسن للصورة: {image_path}")
        print("=" * 70)
        
        start_time = time.time()
        
        try:
            # المرحلة 1: تجربة الطريقة الأساسية أولاً
            print("🎯 المرحلة 1: تطبيق الطريقة الأساسية")
            print("-" * 50)

            basic_result = self.basic_system.infer_equation_from_image(image_path, max_iterations)
            basic_accuracy = basic_result.get('overall_accuracy', 0.0)

            print(f"📊 نتيجة الطريقة الأساسية: {basic_accuracy:.3f}")

            # فحص إذا كانت الطريقة الأساسية كافية
            if basic_accuracy >= self.enhanced_config['basic_method_threshold']:
                print(f"✅ الطريقة الأساسية نجحت! دقة: {basic_accuracy:.3f}")
                basic_result['method_used'] = 'basic_revolutionary'
                basic_result['processing_time'] = time.time() - start_time
                return basic_result

            # المرحلة 1.5: تجربة الاستراتيجية المتقدمة لإزالة الألوان
            print(f"\n🎯 المرحلة 1.5: تجربة الاستراتيجية المتقدمة لإزالة الألوان")
            print("-" * 50)

            color_removal_result = self._apply_advanced_color_removal_strategy(image_path, max_iterations)
            color_removal_accuracy = color_removal_result.get('best_accuracy', 0.0)

            print(f"📊 نتيجة إزالة الألوان: {color_removal_accuracy:.3f}")

            # اختيار أفضل نتيجة من الطريقة الأساسية
            if color_removal_accuracy > basic_accuracy:
                print(f"🎯 تحسن مع إزالة الألوان! {color_removal_accuracy:.3f} > {basic_accuracy:.3f}")
                print(f"🌈 تم اختبار {len(color_removal_result.get('color_tests', []))} لون")
                print(f"🔍 تم اكتشاف {len(color_removal_result.get('combined_shapes', []))} شكل إجمالي")

                if color_removal_result.get('best_result'):
                    basic_result = color_removal_result['best_result']
                    basic_result['color_tests'] = color_removal_result.get('color_tests', [])
                    basic_result['combined_analysis'] = color_removal_result.get('combined_analysis', {})

                    if 'best_removed_color' in basic_result:
                        print(f"🎯 أفضل لون تم إزالته: RGB{basic_result['best_removed_color']}")

                basic_accuracy = color_removal_accuracy

            # فحص إذا كانت النتيجة المحسنة كافية
            if basic_accuracy >= self.enhanced_config['basic_method_threshold']:
                print(f"✅ الطريقة الأساسية المحسنة نجحت! دقة: {basic_accuracy:.3f}")
                basic_result['method_used'] = 'enhanced_basic_with_color_removal'
                basic_result['processing_time'] = time.time() - start_time
                return basic_result
            
            # المرحلة 2: تطبيق الحل الأخير - المكتبة المرجعية
            print(f"\n🎯 المرحلة 2: تطبيق الحل الأخير - المكتبة المرجعية")
            print(f"⚠️ الطريقة الأساسية لم تحقق الدقة المطلوبة ({basic_accuracy:.3f} < {self.enhanced_config['basic_method_threshold']})")
            print("-" * 50)

            library_result = self._apply_library_search_strategy(image_path, basic_result)

            # المرحلة 2.5: تجربة إزالة الخلفية مع المكتبة المرجعية
            print(f"\n🎯 المرحلة 2.5: تجربة إزالة الخلفية مع المكتبة المرجعية")
            print("-" * 50)

            library_bg_result = self._apply_library_with_background_removal(image_path)

            # اختيار أفضل نتيجة من المكتبة
            if library_bg_result.get('overall_accuracy', 0) > library_result.get('overall_accuracy', 0):
                print(f"🎯 تحسن مع إزالة الخلفية في المكتبة!")
                library_result = library_bg_result
            
            # دمج النتائج
            final_result = self._merge_results(basic_result, library_result)
            final_result['processing_time'] = time.time() - start_time
            
            print(f"\n🏆 النتيجة النهائية:")
            print(f"📊 الدقة النهائية: {final_result['overall_accuracy']:.3f}")
            print(f"🔧 الطريقة المستخدمة: {final_result['method_used']}")
            print(f"⏱️ وقت المعالجة الإجمالي: {final_result['processing_time']:.2f} ثانية")
            
            return final_result
            
        except Exception as e:
            print(f"❌ خطأ في الاستنباط المحسن: {str(e)}")
            return self._get_error_result(str(e))
    
    def _apply_library_search_strategy(self, image_path: str, basic_result: Dict) -> Dict[str, Any]:
        """
        تطبيق استراتيجية البحث في المكتبة المرجعية
        """
        print("🔍 بدء استراتيجية البحث في المكتبة المرجعية...")
        
        library_start_time = time.time()
        
        # استخراج أجزاء الصورة
        image_segments = self._extract_image_segments(image_path)

        # تحديد عدد الأجزاء المعالجة لتجنب الحلقات اللانهائية
        max_segments = min(len(image_segments), self.enhanced_config['max_segments_per_search'])
        image_segments = image_segments[:max_segments]

        print(f"📂 تم استخراج {len(image_segments)} جزء من الصورة (محدود بـ {max_segments})")

        # نتائج البحث لكل جزء
        segment_results = []
        total_equations_tested = 0

        for i, segment in enumerate(image_segments):
            print(f"\n🔍 معالجة الجزء {i+1}/{len(image_segments)}")

            # فحص الوقت المتبقي
            elapsed_time = time.time() - library_start_time
            if elapsed_time > self.enhanced_config['max_library_search_time']:
                print(f"⏰ تم الوصول للحد الأقصى للوقت ({elapsed_time:.1f}s)")
                break
            
            # البحث عن أفضل معادلة لهذا الجزء
            segment_result = self._search_segment_in_library(segment, i)
            segment_results.append(segment_result)
            
            total_equations_tested += segment_result.get('equations_tested', 0)
            
            print(f"  📊 أفضل دقة للجزء: {segment_result.get('accuracy', 0):.3f}")
        
        # دمج نتائج جميع الأجزاء
        library_result = self._combine_segment_results(segment_results)
        library_result['total_equations_tested'] = total_equations_tested
        library_result['search_time'] = time.time() - library_start_time
        library_result['segments_processed'] = len(segment_results)
        
        print(f"\n📊 ملخص البحث في المكتبة:")
        print(f"🔍 معادلات مختبرة: {total_equations_tested}")
        print(f"📂 أجزاء معالجة: {len(segment_results)}")
        print(f"⏱️ وقت البحث: {library_result['search_time']:.2f} ثانية")
        print(f"🎯 أفضل دقة: {library_result.get('overall_accuracy', 0):.3f}")
        
        return library_result
    
    def _extract_image_segments(self, image_path: str) -> List[Dict[str, Any]]:
        """
        استخراج أجزاء الصورة للمعالجة المنفصلة
        """
        # قراءة الصورة
        image = cv2.imread(image_path)
        if image is None:
            return []
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        height, width = gray.shape
        
        segments = []
        
        # تقسيم الصورة إلى شبكة
        grid_size = 3  # شبكة 3x3
        segment_height = height // grid_size
        segment_width = width // grid_size
        
        for row in range(grid_size):
            for col in range(grid_size):
                # حساب حدود الجزء
                y_start = row * segment_height
                y_end = min((row + 1) * segment_height, height)
                x_start = col * segment_width
                x_end = min((col + 1) * segment_width, width)
                
                # استخراج الجزء
                segment_image = gray[y_start:y_end, x_start:x_end]
                
                # فحص إذا كان الجزء يحتوي على محتوى
                if self._segment_has_content(segment_image):
                    # استخراج الكونتورات من الجزء
                    contours = self._extract_contours_from_segment(segment_image)
                    
                    if contours:
                        segment = {
                            'id': f'segment_{row}_{col}',
                            'position': (row, col),
                            'bounds': (y_start, y_end, x_start, x_end),
                            'image': segment_image,
                            'contours': contours,
                            'size': segment_image.shape
                        }
                        segments.append(segment)
        
        # إضافة الصورة الكاملة كجزء واحد
        full_contours = self._extract_contours_from_segment(gray)
        if full_contours:
            segments.append({
                'id': 'full_image',
                'position': (0, 0),
                'bounds': (0, height, 0, width),
                'image': gray,
                'contours': full_contours,
                'size': gray.shape
            })
        
        return segments
    
    def _segment_has_content(self, segment_image: np.ndarray) -> bool:
        """
        فحص إذا كان الجزء يحتوي على محتوى مفيد
        """
        # حساب التباين
        variance = np.var(segment_image)
        
        # حساب عدد البكسل غير الصفرية
        non_zero_pixels = np.count_nonzero(segment_image)
        total_pixels = segment_image.size
        
        # معايير وجود المحتوى
        has_variance = variance > 100  # تباين كافي
        has_content = (non_zero_pixels / total_pixels) > 0.1  # 10% على الأقل محتوى
        
        return has_variance and has_content
    
    def _extract_contours_from_segment(self, segment_image: np.ndarray) -> List[np.ndarray]:
        """
        استخراج الكونتورات من جزء الصورة
        """
        try:
            # تحسين الصورة
            blurred = cv2.GaussianBlur(segment_image, (3, 3), 0)
            
            # كشف الحواف
            edges = cv2.Canny(blurred, 30, 90)
            
            # العثور على الكونتورات
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # تصفية الكونتورات الصغيرة
            filtered_contours = []
            for contour in contours:
                area = cv2.contourArea(contour)
                if area > self.enhanced_config['min_segment_size']:
                    filtered_contours.append(contour)
            
            return filtered_contours
            
        except Exception as e:
            return []
    
    def _search_segment_in_library(self, segment: Dict, segment_index: int) -> Dict[str, Any]:
        """
        البحث عن أفضل معادلة لجزء محدد في المكتبة
        """
        # تحويل الكونتورات إلى نقاط x, y
        best_result = {
            'segment_id': segment['id'],
            'accuracy': 0.0,
            'equation': None,
            'equations_tested': 0
        }
        
        for contour in segment['contours']:
            # تحويل الكونتور إلى نقاط
            points = contour.reshape(-1, 2)
            if len(points) < 3:
                continue
            
            x_coords = points[:, 0].astype(float)
            y_coords = points[:, 1].astype(float)
            
            # تطبيع الإحداثيات
            x_range = np.ptp(x_coords)
            y_range = np.ptp(y_coords)
            
            if x_range > 0 and y_range > 0:
                x_normalized = (x_coords - np.min(x_coords)) / x_range
                y_normalized = (y_coords - np.min(y_coords)) / y_range
            else:
                continue
            
            # البحث في المكتبة
            library_match = self.equation_library.search_best_match(x_normalized, y_normalized)
            
            best_result['equations_tested'] += library_match['search_stats']['equations_tested']
            
            # تحديث أفضل نتيجة
            if library_match['accuracy'] > best_result['accuracy']:
                best_result['accuracy'] = library_match['accuracy']
                best_result['equation'] = library_match['equation']
                best_result['shape_type'] = library_match['shape_type']
                best_result['parameters'] = library_match['parameters']
            
            # إذا وصلنا لدقة عالية، توقف
            if library_match['accuracy'] >= self.enhanced_config['library_search_threshold']:
                break
        
        return best_result

    def _apply_background_removal_strategy(self, image_path: str, max_iterations: int) -> Dict[str, Any]:
        """
        تطبيق استراتيجية إزالة الخلفية لتحسين الاستنباط
        """
        print("🎨 بدء استراتيجية إزالة الخلفية...")

        best_result = {
            'overall_accuracy': 0.0,
            'method_used': 'background_removal_failed',
            'background_tests': []
        }

        original_image = cv2.imread(image_path)
        if original_image is None:
            return best_result

        # اختبار كل لون خلفية
        for i, bg_color in enumerate(self.background_colors[:self.enhanced_config['max_background_attempts']]):
            print(f"\n🎨 اختبار لون الخلفية {i+1}/{self.enhanced_config['max_background_attempts']}: RGB{bg_color}")

            try:
                # إزالة الخلفية
                processed_image_path = self._remove_background_color(image_path, bg_color, i)

                if processed_image_path:
                    # تطبيق النظام الأساسي على الصورة المعالجة
                    result = self.basic_system.infer_equation_from_image(processed_image_path, max_iterations)
                    accuracy = result.get('overall_accuracy', 0.0)

                    print(f"  📊 دقة مع إزالة الخلفية: {accuracy:.3f}")

                    # تسجيل النتيجة
                    test_result = {
                        'background_color': bg_color,
                        'accuracy': accuracy,
                        'processed_image': processed_image_path
                    }
                    best_result['background_tests'].append(test_result)

                    # تحديث أفضل نتيجة
                    if accuracy > best_result['overall_accuracy']:
                        best_result.update(result)
                        best_result['overall_accuracy'] = accuracy
                        best_result['method_used'] = 'background_removal_enhanced'
                        best_result['best_background_color'] = bg_color
                        best_result['best_processed_image'] = processed_image_path

                        print(f"  🎯 تحسن! أفضل دقة: {accuracy:.3f}")

                    # إذا وصلنا لدقة جيدة، توقف
                    if accuracy >= self.enhanced_config['basic_method_threshold']:
                        print(f"  ✅ وصلنا للدقة المطلوبة مع إزالة الخلفية!")
                        break

                    # تنظيف الملف المؤقت
                    try:
                        os.remove(processed_image_path)
                    except:
                        pass

            except Exception as e:
                print(f"  ❌ خطأ في معالجة لون الخلفية {bg_color}: {str(e)}")
                continue

        print(f"\n📊 ملخص إزالة الخلفية:")
        print(f"🎨 ألوان مختبرة: {len(best_result['background_tests'])}")
        print(f"🎯 أفضل دقة: {best_result['overall_accuracy']:.3f}")
        if 'best_background_color' in best_result:
            print(f"🌈 أفضل لون خلفية: RGB{best_result['best_background_color']}")

        return best_result

    def _remove_background_color(self, image_path: str, bg_color: tuple, index: int) -> str:
        """
        إزالة لون خلفية محدد من الصورة
        """
        try:
            # قراءة الصورة
            image = cv2.imread(image_path)
            if image is None:
                return None

            # تحويل إلى RGB
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # إنشاء قناع للخلفية
            tolerance = self.enhanced_config['background_tolerance']

            # حساب المسافة من لون الخلفية
            diff = np.abs(image_rgb.astype(np.float32) - np.array(bg_color).astype(np.float32))
            distance = np.sqrt(np.sum(diff**2, axis=2))

            # إنشاء القناع
            background_mask = distance <= tolerance

            # إزالة الخلفية (جعلها شفافة أو بيضاء)
            processed_image = image_rgb.copy()
            processed_image[background_mask] = [255, 255, 255]  # خلفية بيضاء

            # حفظ الصورة المعالجة
            temp_path = f"/tmp/bg_removed_{index}_{int(time.time())}.png"
            processed_image_bgr = cv2.cvtColor(processed_image, cv2.COLOR_RGB2BGR)
            cv2.imwrite(temp_path, processed_image_bgr)

            return temp_path

        except Exception as e:
            print(f"❌ خطأ في إزالة الخلفية: {str(e)}")
            return None

    def _extract_dominant_colors(self, image, num_colors=8):
        """
        استخراج الألوان الرئيسية من الصورة
        """
        try:
            # تصغير الصورة لتسريع المعالجة
            small_image = cv2.resize(image, (150, 150))

            # تحويل إلى RGB
            image_rgb = cv2.cvtColor(small_image, cv2.COLOR_BGR2RGB)

            # تحويل إلى مصفوفة ثنائية الأبعاد
            pixels = image_rgb.reshape(-1, 3)

            # استخدام K-means لاستخراج الألوان الرئيسية
            if SKLEARN_AVAILABLE:
                kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init=10)
                kmeans.fit(pixels)
                colors = kmeans.cluster_centers_.astype(int)
            else:
                # استخراج ألوان مبسط بدون sklearn
                colors = self._simple_color_extraction(pixels, num_colors)

            # تحويل إلى قائمة من tuples
            dominant_colors = [tuple(color) for color in colors]

            return dominant_colors

        except Exception as e:
            print(f"❌ خطأ في استخراج الألوان: {str(e)}")
            # إرجاع ألوان افتراضية
            return [(255, 255, 255), (0, 0, 0), (128, 128, 128)]

    def _simple_color_extraction(self, pixels, num_colors):
        """
        استخراج ألوان مبسط بدون sklearn
        """
        try:
            # تقسيم الألوان إلى مجموعات بسيطة
            unique_colors = []

            # أخذ عينة من البكسل لتسريع المعالجة
            sample_size = min(1000, len(pixels))
            sample_indices = np.random.choice(len(pixels), sample_size, replace=False)
            sample_pixels = pixels[sample_indices]

            # تجميع الألوان المتشابهة
            for pixel in sample_pixels:
                is_similar = False
                for existing_color in unique_colors:
                    if self._color_distance(pixel, existing_color) < 50:
                        is_similar = True
                        break

                if not is_similar:
                    unique_colors.append(tuple(pixel))

                # توقف عند الوصول للعدد المطلوب
                if len(unique_colors) >= num_colors:
                    break

            # إضافة ألوان افتراضية إذا لم نجد ما يكفي
            default_colors = [(255, 255, 255), (0, 0, 0), (128, 128, 128),
                            (192, 192, 192), (64, 64, 64)]

            for color in default_colors:
                if len(unique_colors) >= num_colors:
                    break
                if color not in unique_colors:
                    unique_colors.append(color)

            return unique_colors[:num_colors]

        except Exception as e:
            print(f"❌ خطأ في استخراج الألوان المبسط: {str(e)}")
            return [(255, 255, 255), (0, 0, 0), (128, 128, 128)]

    def _color_distance(self, color1, color2):
        """
        حساب المسافة بين لونين
        """
        return np.sqrt(sum((a - b) ** 2 for a, b in zip(color1, color2)))

    def _remove_specific_color(self, image_path: str, color: tuple, index: int) -> str:
        """
        إزالة لون محدد من الصورة
        """
        try:
            # قراءة الصورة
            image = cv2.imread(image_path)
            if image is None:
                return None

            # تحويل إلى RGB
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # إنشاء قناع للون المحدد
            tolerance = self.enhanced_config['background_tolerance']

            # حساب المسافة من اللون المحدد
            diff = np.abs(image_rgb.astype(np.float32) - np.array(color).astype(np.float32))
            distance = np.sqrt(np.sum(diff**2, axis=2))

            # إنشاء القناع
            color_mask = distance <= tolerance

            # إزالة اللون (جعله شفاف أو أبيض)
            processed_image = image_rgb.copy()
            processed_image[color_mask] = [255, 255, 255]  # استبدال بالأبيض

            # حفظ الصورة المعالجة
            temp_path = f"/tmp/color_removed_{index}_{int(time.time())}.png"
            processed_image_bgr = cv2.cvtColor(processed_image, cv2.COLOR_RGB2BGR)
            cv2.imwrite(temp_path, processed_image_bgr)

            return temp_path

        except Exception as e:
            print(f"❌ خطأ في إزالة اللون: {str(e)}")
            return None

    def _analyze_combined_shape_data(self, all_shapes, shape_frequency):
        """
        تحليل البيانات المجمعة من جميع عمليات إزالة الألوان
        """
        try:
            analysis = {
                'total_detections': len(all_shapes),
                'unique_shapes': len(shape_frequency),
                'most_common_shape': None,
                'confidence_scores': {},
                'layer_analysis': {},
                'recommended_shapes': []
            }

            if not all_shapes:
                return analysis

            # تحديد الشكل الأكثر تكراراً
            if shape_frequency:
                most_common = max(shape_frequency.items(), key=lambda x: x[1])
                analysis['most_common_shape'] = {
                    'type': most_common[0],
                    'frequency': most_common[1],
                    'confidence': most_common[1] / len(all_shapes)
                }

            # تحليل الثقة لكل شكل
            for shape_type, frequency in shape_frequency.items():
                confidence = frequency / len(all_shapes)
                analysis['confidence_scores'][shape_type] = confidence

            # تحليل الطبقات (أي الألوان التي كشفت عن أشكال أكثر)
            color_performance = {}
            for shape_info in all_shapes:
                color = tuple(shape_info['removed_color'])
                if color not in color_performance:
                    color_performance[color] = {
                        'shapes_found': 0,
                        'total_accuracy': 0.0,
                        'detections': []
                    }

                color_performance[color]['shapes_found'] += 1
                color_performance[color]['total_accuracy'] += shape_info['accuracy']
                color_performance[color]['detections'].append(shape_info)

            # حساب متوسط الأداء لكل لون
            for color, performance in color_performance.items():
                performance['average_accuracy'] = performance['total_accuracy'] / performance['shapes_found']
                analysis['layer_analysis'][str(color)] = performance

            # التوصية بالأشكال الأكثر موثوقية
            for shape_type, confidence in analysis['confidence_scores'].items():
                if confidence >= 0.3:  # ظهر في 30% أو أكثر من الاختبارات
                    analysis['recommended_shapes'].append({
                        'type': shape_type,
                        'confidence': confidence,
                        'recommendation': 'high' if confidence >= 0.6 else 'medium'
                    })

            return analysis

        except Exception as e:
            print(f"❌ خطأ في تحليل البيانات المجمعة: {str(e)}")
            return {'total_detections': 0, 'error': str(e)}

    def _apply_advanced_color_removal_strategy(self, image_path, max_iterations=3):
        """
        تطبيق الاستراتيجية المتقدمة: إزالة كل لون على حدة لكشف طبقات مختلفة من الأشكال
        """
        print("🎨 بدء الاستراتيجية المتقدمة: إزالة كل لون على حدة...")

        # قراءة الصورة الأصلية لاستخراج الألوان الموجودة
        image = cv2.imread(image_path)
        if image is None:
            return {'best_accuracy': 0.0, 'color_tests': [], 'combined_shapes': []}

        # استخراج الألوان الرئيسية من الصورة
        detected_colors = self._extract_dominant_colors(image)

        # إضافة الألوان الأساسية المعروفة
        all_colors_to_test = list(detected_colors) + [
            (255, 255, 255),  # أبيض
            (0, 0, 0),        # أسود
            (240, 240, 240),  # رمادي فاتح
            (128, 128, 128),  # رمادي متوسط
            (64, 64, 64),     # رمادي داكن
            (255, 255, 240),  # أصفر فاتح
            (248, 248, 255),  # أزرق فاتح
            (245, 245, 220),  # بيج
        ]

        # إزالة الألوان المكررة
        unique_colors = []
        for color in all_colors_to_test:
            is_duplicate = False
            for existing_color in unique_colors:
                if self._color_distance(color, existing_color) < 30:  # تسامح 30
                    is_duplicate = True
                    break
            if not is_duplicate:
                unique_colors.append(color)

        print(f"🌈 تم اكتشاف {len(detected_colors)} لون من الصورة")
        print(f"🎯 سيتم اختبار {len(unique_colors)} لون إجمالي")

        best_accuracy = 0.0
        best_result = None
        color_tests = []
        all_detected_shapes = []
        shape_frequency = {}

        for i, color in enumerate(unique_colors):
            print(f"\n🎨 إزالة اللون {i+1}/{len(unique_colors)}: RGB{color}")

            try:
                # إزالة اللون المحدد
                processed_image_path = self._remove_specific_color(image_path, color, i)

                if processed_image_path is None:
                    continue

                # تطبيق الطريقة الأساسية على الصورة المعالجة
                result = self.basic_system.infer_equation_from_image(
                    processed_image_path, max_iterations=max_iterations
                )

                accuracy = result.get('overall_accuracy', 0.0)
                shapes_found = result.get('equations', [])

                print(f"  📊 دقة مع إزالة اللون: {accuracy:.3f}")
                print(f"  🔍 أشكال مكتشفة: {len(shapes_found)}")

                # تسجيل الأشكال المكتشفة
                for shape in shapes_found:
                    shape_info = {
                        'equation': shape,
                        'removed_color': color,
                        'accuracy': accuracy,
                        'detection_method': f'color_removal_{i}'
                    }
                    all_detected_shapes.append(shape_info)

                    # إحصاء تكرار الأشكال
                    shape_key = str(shape.get('type', 'unknown'))
                    shape_frequency[shape_key] = shape_frequency.get(shape_key, 0) + 1

                color_tests.append({
                    'color': color,
                    'accuracy': accuracy,
                    'shapes_found': len(shapes_found),
                    'shapes': shapes_found,
                    'result': result
                })

                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    best_result = result
                    best_result['best_removed_color'] = color

                # تنظيف الملف المؤقت
                if os.path.exists(processed_image_path):
                    os.remove(processed_image_path)

            except Exception as e:
                print(f"  ❌ خطأ في إزالة اللون RGB{color}: {str(e)}")
                color_tests.append({
                    'color': color,
                    'accuracy': 0.0,
                    'shapes_found': 0,
                    'error': str(e)
                })

        # تحليل البيانات المجمعة
        combined_analysis = self._analyze_combined_shape_data(all_detected_shapes, shape_frequency)

        print(f"\n📊 ملخص إزالة الألوان:")
        print(f"🌈 ألوان مختبرة: {len(color_tests)}")
        print(f"🎯 أفضل دقة: {best_accuracy:.3f}")
        print(f"🔍 إجمالي الأشكال المكتشفة: {len(all_detected_shapes)}")
        print(f"📈 أنواع الأشكال: {len(shape_frequency)}")

        if combined_analysis.get('most_common_shape'):
            most_common = combined_analysis['most_common_shape']
            print(f"🏆 الشكل الأكثر تكراراً: {most_common['type']} (ثقة: {most_common['confidence']:.2f})")

        return {
            'best_accuracy': best_accuracy,
            'best_result': best_result,
            'color_tests': color_tests,
            'combined_shapes': all_detected_shapes,
            'shape_frequency': shape_frequency,
            'combined_analysis': combined_analysis,
            'improvement_achieved': best_accuracy > 0.0
        }

    def _enhance_image_contrast(self, image_path: str, index: int) -> str:
        """
        تحسين تباين الصورة لكشف أفضل للأشكال
        """
        try:
            image = cv2.imread(image_path)
            if image is None:
                return None

            # تحويل إلى LAB
            lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
            l, a, b = cv2.split(lab)

            # تطبيق CLAHE على قناة L
            clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
            l = clahe.apply(l)

            # دمج القنوات
            enhanced_lab = cv2.merge([l, a, b])
            enhanced_image = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

            # حفظ الصورة المحسنة
            temp_path = f"/tmp/enhanced_{index}_{int(time.time())}.png"
            cv2.imwrite(temp_path, enhanced_image)

            return temp_path

        except Exception as e:
            print(f"❌ خطأ في تحسين التباين: {str(e)}")
            return None

    def _combine_segment_results(self, segment_results: List[Dict]) -> Dict[str, Any]:
        """
        دمج نتائج جميع أجزاء الصورة
        """
        if not segment_results:
            return {
                'overall_accuracy': 0.0,
                'equations': [],
                'method_used': 'library_search_failed'
            }

        # جمع جميع المعادلات الناجحة
        successful_equations = []
        total_accuracy = 0.0

        for result in segment_results:
            if result.get('equation') and result.get('accuracy', 0) > 0.3:
                successful_equations.append({
                    'equation': result['equation'],
                    'accuracy': result['accuracy'],
                    'segment_id': result['segment_id'],
                    'shape_type': result.get('shape_type', 'unknown')
                })
                total_accuracy += result['accuracy']

        # حساب الدقة الإجمالية
        if successful_equations:
            overall_accuracy = total_accuracy / len(segment_results)
        else:
            overall_accuracy = 0.0

        return {
            'overall_accuracy': overall_accuracy,
            'equations': successful_equations,
            'method_used': 'library_search',
            'segments_with_equations': len(successful_equations),
            'total_segments': len(segment_results)
        }

    def _merge_results(self, basic_result: Dict, library_result: Dict) -> Dict[str, Any]:
        """
        دمج نتائج الطريقة الأساسية مع نتائج المكتبة
        """
        basic_accuracy = basic_result.get('overall_accuracy', 0.0)
        library_accuracy = library_result.get('overall_accuracy', 0.0)

        # اختيار أفضل نتيجة
        if library_accuracy > basic_accuracy:
            primary_result = library_result
            secondary_result = basic_result
            method_used = 'enhanced_library_search'
            final_accuracy = library_accuracy
        else:
            primary_result = basic_result
            secondary_result = library_result
            method_used = 'enhanced_basic_method'
            final_accuracy = basic_accuracy

        # دمج المعادلات
        merged_equations = []

        # إضافة معادلات من النتيجة الأساسية
        if 'equations' in primary_result:
            for eq in primary_result['equations']:
                merged_equations.append(eq)

        # إضافة معادلات إضافية من النتيجة الثانوية إذا كانت مفيدة
        if 'equations' in secondary_result:
            for eq in secondary_result['equations']:
                if isinstance(eq, dict) and eq.get('accuracy', 0) > 0.5:
                    merged_equations.append(eq)

        # إنشاء النتيجة المدمجة
        merged_result = {
            'success': final_accuracy > 0.3,
            'overall_accuracy': final_accuracy,
            'equations': merged_equations,
            'method_used': method_used,
            'basic_method_accuracy': basic_accuracy,
            'library_method_accuracy': library_accuracy,
            'improvement_achieved': library_accuracy > basic_accuracy,
            'improvement_factor': library_accuracy / basic_accuracy if basic_accuracy > 0 else float('inf'),
            'processing_summary': {
                'total_equations_found': len(merged_equations),
                'successful_equations': sum(1 for eq in merged_equations if isinstance(eq, dict) and eq.get('accuracy', 0) > 0.5),
                'method_comparison': {
                    'basic_method': basic_accuracy,
                    'library_method': library_accuracy,
                    'winner': 'library' if library_accuracy > basic_accuracy else 'basic'
                }
            }
        }

        # إضافة تفاصيل إضافية
        if 'search_time' in library_result:
            merged_result['library_search_time'] = library_result['search_time']

        if 'total_equations_tested' in library_result:
            merged_result['library_equations_tested'] = library_result['total_equations_tested']

        return merged_result

    def _get_error_result(self, error_message: str) -> Dict[str, Any]:
        """
        إرجاع نتيجة خطأ
        """
        return {
            'success': False,
            'error': error_message,
            'overall_accuracy': 0.0,
            'equations': [],
            'method_used': 'error',
            'methodology': self.methodology,
            'creator': self.creator
        }

    def get_system_stats(self) -> Dict[str, Any]:
        """
        إحصائيات النظام المحسن
        """
        library_stats = self.equation_library.get_library_stats()

        return {
            'system_type': 'Enhanced Revolutionary Inference System',
            'creator': self.creator,
            'methodology': self.methodology,
            'library_stats': library_stats,
            'configuration': self.enhanced_config,
            'capabilities': {
                'basic_revolutionary_method': True,
                'library_reference_search': True,
                'image_segmentation': True,
                'expert_guidance': True,
                'iterative_improvement': True
            }
        }

    def test_system_performance(self, test_images: List[str]) -> Dict[str, Any]:
        """
        اختبار أداء النظام المحسن
        """
        print("🧪 بدء اختبار أداء النظام المحسن")
        print("=" * 50)

        test_results = []
        total_start_time = time.time()

        for i, image_path in enumerate(test_images):
            print(f"\n🖼️ اختبار الصورة {i+1}/{len(test_images)}: {os.path.basename(image_path)}")

            try:
                result = self.infer_equation_from_image_enhanced(image_path)
                test_results.append({
                    'image_path': image_path,
                    'success': result['success'],
                    'accuracy': result['overall_accuracy'],
                    'method_used': result['method_used'],
                    'processing_time': result.get('processing_time', 0),
                    'equations_found': len(result.get('equations', []))
                })

                print(f"  ✅ نجح: {result['success']}")
                print(f"  📊 دقة: {result['overall_accuracy']:.3f}")
                print(f"  🔧 طريقة: {result['method_used']}")

            except Exception as e:
                test_results.append({
                    'image_path': image_path,
                    'success': False,
                    'accuracy': 0.0,
                    'method_used': 'error',
                    'processing_time': 0,
                    'equations_found': 0,
                    'error': str(e)
                })
                print(f"  ❌ فشل: {str(e)}")

        total_time = time.time() - total_start_time

        # تحليل النتائج
        successful_tests = sum(1 for r in test_results if r['success'])
        total_tests = len(test_results)
        success_rate = (successful_tests / total_tests) * 100 if total_tests > 0 else 0

        accuracies = [r['accuracy'] for r in test_results if r['success']]
        avg_accuracy = np.mean(accuracies) if accuracies else 0

        processing_times = [r['processing_time'] for r in test_results]
        avg_processing_time = np.mean(processing_times) if processing_times else 0

        # إحصائيات الطرق المستخدمة
        method_stats = {}
        for result in test_results:
            method = result['method_used']
            if method not in method_stats:
                method_stats[method] = 0
            method_stats[method] += 1

        performance_report = {
            'test_summary': {
                'total_tests': total_tests,
                'successful_tests': successful_tests,
                'success_rate': success_rate,
                'average_accuracy': avg_accuracy,
                'average_processing_time': avg_processing_time,
                'total_test_time': total_time
            },
            'method_distribution': method_stats,
            'detailed_results': test_results,
            'performance_grade': self._calculate_performance_grade(success_rate, avg_accuracy)
        }

        print(f"\n🏆 تقرير الأداء النهائي:")
        print(f"📊 معدل النجاح: {success_rate:.1f}%")
        print(f"🎯 متوسط الدقة: {avg_accuracy:.3f}")
        print(f"⏱️ متوسط وقت المعالجة: {avg_processing_time:.2f} ثانية")
        print(f"🏅 تقييم الأداء: {performance_report['performance_grade']}")

        return performance_report

    def _calculate_performance_grade(self, success_rate: float, avg_accuracy: float) -> str:
        """
        حساب تقييم الأداء
        """
        combined_score = (success_rate / 100) * 0.6 + avg_accuracy * 0.4

        if combined_score >= 0.9:
            return "ممتاز"
        elif combined_score >= 0.8:
            return "جيد جداً"
        elif combined_score >= 0.7:
            return "جيد"
        elif combined_score >= 0.6:
            return "مقبول"
        else:
            return "يحتاج تحسين"

    def _apply_library_with_background_removal(self, image_path: str) -> Dict[str, Any]:
        """
        تطبيق المكتبة المرجعية مع إزالة الخلفية
        """
        print("🎨📚 بدء البحث في المكتبة مع إزالة الخلفية...")

        best_result = {
            'overall_accuracy': 0.0,
            'method_used': 'library_with_background_removal',
            'background_library_tests': []
        }

        # اختبار أهم 4 ألوان خلفية فقط لتوفير الوقت
        priority_colors = self.background_colors[:4]

        for i, bg_color in enumerate(priority_colors):
            print(f"\n🎨 اختبار المكتبة مع لون خلفية {i+1}/4: RGB{bg_color}")

            try:
                # إزالة الخلفية
                processed_image_path = self._remove_background_color(image_path, bg_color, f"lib_{i}")

                if processed_image_path:
                    # تطبيق البحث في المكتبة على الصورة المعالجة
                    library_result = self._apply_library_search_strategy(processed_image_path, {})
                    accuracy = library_result.get('overall_accuracy', 0.0)

                    print(f"  📊 دقة المكتبة مع إزالة الخلفية: {accuracy:.3f}")

                    # تسجيل النتيجة
                    test_result = {
                        'background_color': bg_color,
                        'accuracy': accuracy,
                        'processed_image': processed_image_path
                    }
                    best_result['background_library_tests'].append(test_result)

                    # تحديث أفضل نتيجة
                    if accuracy > best_result['overall_accuracy']:
                        best_result.update(library_result)
                        best_result['overall_accuracy'] = accuracy
                        best_result['method_used'] = 'library_with_background_removal'
                        best_result['best_background_color'] = bg_color

                        print(f"  🎯 تحسن في المكتبة! أفضل دقة: {accuracy:.3f}")

                    # إذا وصلنا لدقة عالية، توقف
                    if accuracy >= self.enhanced_config['library_search_threshold']:
                        print(f"  ✅ وصلنا للدقة العالية مع المكتبة وإزالة الخلفية!")
                        break

                    # تنظيف الملف المؤقت
                    try:
                        os.remove(processed_image_path)
                    except:
                        pass

            except Exception as e:
                print(f"  ❌ خطأ في المكتبة مع لون الخلفية {bg_color}: {str(e)}")
                continue

        print(f"\n📊 ملخص المكتبة مع إزالة الخلفية:")
        print(f"🎨 ألوان مختبرة: {len(best_result['background_library_tests'])}")
        print(f"🎯 أفضل دقة: {best_result['overall_accuracy']:.3f}")
        if 'best_background_color' in best_result:
            print(f"🌈 أفضل لون خلفية: RGB{best_result['best_background_color']}")

        return best_result
