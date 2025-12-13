#!/usr/bin/env python3
"""
نظام التصور الثوري - بديل لـ matplotlib
يستخدم النظريات الثلاث الثورية لإنشاء الرسوم البيانية بدون مكتبات تقليدية

🧬 المطور: باسل يحيى عبدالله
⚡ النظريات: ثنائية الصفر، تعامد الأضداد، الفتائل
🚫 بدون: matplotlib, seaborn, plotly
✅ يستخدم فقط: PIL, numpy, math
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import math
from typing import Dict, List, Tuple, Any, Optional, Union
import json
from dataclasses import dataclass
from enum import Enum
import os

class PlotType(Enum):
    """أنواع الرسوم البيانية"""
    LINE = "line"
    BAR = "bar"
    SCATTER = "scatter"
    HISTOGRAM = "histogram"
    PIE = "pie"
    HEATMAP = "heatmap"

class ColorScheme(Enum):
    """أنظمة الألوان الثورية"""
    ZERO_DUALITY = "zero_duality"
    PERPENDICULARITY = "perpendicularity"
    FILAMENT = "filament"
    REVOLUTIONARY = "revolutionary"

@dataclass
class PlotConfig:
    """إعدادات الرسم البياني"""
    width: int = 800
    height: int = 600
    background_color: Tuple[int, int, int] = (255, 255, 255)
    title: str = ""
    xlabel: str = ""
    ylabel: str = ""
    color_scheme: ColorScheme = ColorScheme.REVOLUTIONARY
    show_grid: bool = True
    show_legend: bool = True

class RevolutionaryVisualizer:
    """نظام التصور الثوري - بديل لـ matplotlib"""
    
    def __init__(self):
        self.name = "RevolutionaryVisualizer"
        
        # أنظمة الألوان الثورية
        self.color_schemes = {
            ColorScheme.ZERO_DUALITY: [
                (0, 100, 200),    # أزرق عميق
                (200, 100, 0),    # برتقالي
                (100, 200, 100),  # أخضر
                (200, 0, 100),    # أحمر-بنفسجي
                (100, 100, 200)   # أزرق فاتح
            ],
            ColorScheme.PERPENDICULARITY: [
                (200, 0, 0),      # أحمر
                (0, 200, 0),      # أخضر
                (0, 0, 200),      # أزرق
                (200, 200, 0),    # أصفر
                (200, 0, 200)     # بنفسجي
            ],
            ColorScheme.FILAMENT: [
                (150, 75, 0),     # بني
                (75, 150, 75),    # أخضر زيتوني
                (75, 75, 150),    # أزرق داكن
                (150, 150, 75),   # أصفر داكن
                (150, 75, 150)    # بنفسجي داكن
            ],
            ColorScheme.REVOLUTIONARY: [
                (255, 69, 0),     # أحمر برتقالي
                (50, 205, 50),    # أخضر ليموني
                (30, 144, 255),   # أزرق دودجر
                (255, 215, 0),    # ذهبي
                (138, 43, 226)    # بنفسجي أزرق
            ]
        }
        
        print("📊⚡ تم إنشاء نظام التصور الثوري")
        print("   🧬 النظريات الثلاث: نشطة")
        print("   🚫 بدون matplotlib أو مكتبات تصور تقليدية")
        print("   ✅ رسوم بيانية ثورية")
    
    def create_line_plot(self, x_data: List[float], y_data: List[float], 
                        config: PlotConfig = None) -> Image.Image:
        """إنشاء رسم بياني خطي"""
        if config is None:
            config = PlotConfig()
        
        # إنشاء الصورة
        image = Image.new('RGB', (config.width, config.height), config.background_color)
        draw = ImageDraw.Draw(image)
        
        # حساب منطقة الرسم
        margin = 80
        plot_x = margin
        plot_y = margin
        plot_width = config.width - 2 * margin
        plot_height = config.height - 2 * margin
        
        # رسم الشبكة
        if config.show_grid:
            self._draw_grid(draw, plot_x, plot_y, plot_width, plot_height)
        
        # رسم المحاور
        self._draw_axes(draw, plot_x, plot_y, plot_width, plot_height)
        
        # رسم البيانات
        if len(x_data) == len(y_data) and len(x_data) > 1:
            # تطبيع البيانات
            x_min, x_max = min(x_data), max(x_data)
            y_min, y_max = min(y_data), max(y_data)
            
            if x_max > x_min and y_max > y_min:
                # تحويل البيانات إلى إحداثيات الشاشة
                points = []
                for i in range(len(x_data)):
                    x_norm = (x_data[i] - x_min) / (x_max - x_min)
                    y_norm = (y_data[i] - y_min) / (y_max - y_min)
                    
                    screen_x = plot_x + x_norm * plot_width
                    screen_y = plot_y + plot_height - y_norm * plot_height
                    
                    points.append((screen_x, screen_y))
                
                # رسم الخط
                color = self.color_schemes[config.color_scheme][0]
                for i in range(len(points) - 1):
                    draw.line([points[i], points[i + 1]], fill=color, width=2)
                
                # رسم النقاط
                for point in points:
                    draw.ellipse([point[0] - 3, point[1] - 3, point[0] + 3, point[1] + 3], 
                               fill=color, outline=(0, 0, 0))
        
        # إضافة العناوين
        self._add_labels(draw, config, plot_x, plot_y, plot_width, plot_height)
        
        return image
    
    def create_bar_plot(self, categories: List[str], values: List[float], 
                       config: PlotConfig = None) -> Image.Image:
        """إنشاء رسم بياني بالأعمدة"""
        if config is None:
            config = PlotConfig()
        
        image = Image.new('RGB', (config.width, config.height), config.background_color)
        draw = ImageDraw.Draw(image)
        
        margin = 80
        plot_x = margin
        plot_y = margin
        plot_width = config.width - 2 * margin
        plot_height = config.height - 2 * margin
        
        # رسم الشبكة والمحاور
        if config.show_grid:
            self._draw_grid(draw, plot_x, plot_y, plot_width, plot_height)
        self._draw_axes(draw, plot_x, plot_y, plot_width, plot_height)
        
        if len(categories) == len(values) and len(categories) > 0:
            # حساب أبعاد الأعمدة
            bar_width = plot_width / len(categories) * 0.8
            bar_spacing = plot_width / len(categories) * 0.2
            
            # تطبيع القيم
            max_value = max(values) if values else 1
            min_value = min(values) if values else 0
            value_range = max_value - min_value if max_value > min_value else 1
            
            # رسم الأعمدة
            colors = self.color_schemes[config.color_scheme]
            for i, (category, value) in enumerate(zip(categories, values)):
                # حساب موقع وحجم العمود
                bar_x = plot_x + i * (bar_width + bar_spacing) + bar_spacing / 2
                normalized_value = (value - min_value) / value_range
                bar_height = normalized_value * plot_height
                bar_y = plot_y + plot_height - bar_height
                
                # اختيار اللون
                color = colors[i % len(colors)]
                
                # رسم العمود
                draw.rectangle([bar_x, bar_y, bar_x + bar_width, plot_y + plot_height], 
                             fill=color, outline=(0, 0, 0))
                
                # إضافة تسمية الفئة
                try:
                    font = ImageFont.load_default()
                    text_bbox = draw.textbbox((0, 0), category, font=font)
                    text_width = text_bbox[2] - text_bbox[0]
                    text_x = bar_x + bar_width / 2 - text_width / 2
                    text_y = plot_y + plot_height + 10
                    draw.text((text_x, text_y), category, fill=(0, 0, 0), font=font)
                except:
                    # في حالة عدم توفر الخط
                    pass
        
        # إضافة العناوين
        self._add_labels(draw, config, plot_x, plot_y, plot_width, plot_height)
        
        return image
    
    def create_scatter_plot(self, x_data: List[float], y_data: List[float], 
                           config: PlotConfig = None) -> Image.Image:
        """إنشاء رسم بياني نقطي"""
        if config is None:
            config = PlotConfig()
        
        image = Image.new('RGB', (config.width, config.height), config.background_color)
        draw = ImageDraw.Draw(image)
        
        margin = 80
        plot_x = margin
        plot_y = margin
        plot_width = config.width - 2 * margin
        plot_height = config.height - 2 * margin
        
        # رسم الشبكة والمحاور
        if config.show_grid:
            self._draw_grid(draw, plot_x, plot_y, plot_width, plot_height)
        self._draw_axes(draw, plot_x, plot_y, plot_width, plot_height)
        
        if len(x_data) == len(y_data) and len(x_data) > 0:
            # تطبيع البيانات
            x_min, x_max = min(x_data), max(x_data)
            y_min, y_max = min(y_data), max(y_data)
            
            if x_max > x_min and y_max > y_min:
                # رسم النقاط
                color = self.color_schemes[config.color_scheme][0]
                point_size = 4
                
                for i in range(len(x_data)):
                    x_norm = (x_data[i] - x_min) / (x_max - x_min)
                    y_norm = (y_data[i] - y_min) / (y_max - y_min)
                    
                    screen_x = plot_x + x_norm * plot_width
                    screen_y = plot_y + plot_height - y_norm * plot_height
                    
                    draw.ellipse([screen_x - point_size, screen_y - point_size, 
                                screen_x + point_size, screen_y + point_size], 
                               fill=color, outline=(0, 0, 0))
        
        # إضافة العناوين
        self._add_labels(draw, config, plot_x, plot_y, plot_width, plot_height)
        
        return image
    
    def create_pie_chart(self, labels: List[str], values: List[float], 
                        config: PlotConfig = None) -> Image.Image:
        """إنشاء رسم بياني دائري"""
        if config is None:
            config = PlotConfig()
        
        image = Image.new('RGB', (config.width, config.height), config.background_color)
        draw = ImageDraw.Draw(image)
        
        # حساب مركز ونصف قطر الدائرة
        center_x = config.width // 2
        center_y = config.height // 2
        radius = min(config.width, config.height) // 3
        
        if len(labels) == len(values) and len(values) > 0:
            total = sum(values)
            if total > 0:
                # رسم القطاعات
                colors = self.color_schemes[config.color_scheme]
                start_angle = 0
                
                for i, (label, value) in enumerate(zip(labels, values)):
                    # حساب زاوية القطاع
                    angle = (value / total) * 360
                    end_angle = start_angle + angle
                    
                    # اختيار اللون
                    color = colors[i % len(colors)]
                    
                    # رسم القطاع
                    bbox = [center_x - radius, center_y - radius, 
                           center_x + radius, center_y + radius]
                    draw.pieslice(bbox, start_angle, end_angle, fill=color, outline=(0, 0, 0))
                    
                    # إضافة التسمية
                    if angle > 10:  # فقط للقطاعات الكبيرة
                        label_angle = math.radians(start_angle + angle / 2)
                        label_x = center_x + (radius * 0.7) * math.cos(label_angle)
                        label_y = center_y + (radius * 0.7) * math.sin(label_angle)
                        
                        try:
                            font = ImageFont.load_default()
                            draw.text((label_x, label_y), f"{label}\n{value:.1f}%", 
                                    fill=(0, 0, 0), font=font, anchor="mm")
                        except:
                            pass
                    
                    start_angle = end_angle
        
        # إضافة العنوان
        if config.title:
            try:
                font = ImageFont.load_default()
                text_bbox = draw.textbbox((0, 0), config.title, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                title_x = config.width // 2 - text_width // 2
                draw.text((title_x, 20), config.title, fill=(0, 0, 0), font=font)
            except:
                pass
        
        return image
    
    def _draw_grid(self, draw: ImageDraw.Draw, x: int, y: int, width: int, height: int):
        """رسم الشبكة"""
        grid_color = (200, 200, 200)
        
        # خطوط عمودية
        for i in range(1, 10):
            grid_x = x + (width * i) // 10
            draw.line([(grid_x, y), (grid_x, y + height)], fill=grid_color, width=1)
        
        # خطوط أفقية
        for i in range(1, 10):
            grid_y = y + (height * i) // 10
            draw.line([(x, grid_y), (x + width, grid_y)], fill=grid_color, width=1)
    
    def _draw_axes(self, draw: ImageDraw.Draw, x: int, y: int, width: int, height: int):
        """رسم المحاور"""
        axis_color = (0, 0, 0)
        
        # المحور السيني (X)
        draw.line([(x, y + height), (x + width, y + height)], fill=axis_color, width=2)
        
        # المحور الصادي (Y)
        draw.line([(x, y), (x, y + height)], fill=axis_color, width=2)
    
    def _add_labels(self, draw: ImageDraw.Draw, config: PlotConfig, 
                   x: int, y: int, width: int, height: int):
        """إضافة التسميات والعناوين"""
        try:
            font = ImageFont.load_default()
            
            # العنوان الرئيسي
            if config.title:
                text_bbox = draw.textbbox((0, 0), config.title, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                title_x = config.width // 2 - text_width // 2
                draw.text((title_x, 20), config.title, fill=(0, 0, 0), font=font)
            
            # تسمية المحور السيني
            if config.xlabel:
                text_bbox = draw.textbbox((0, 0), config.xlabel, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                xlabel_x = x + width // 2 - text_width // 2
                xlabel_y = y + height + 40
                draw.text((xlabel_x, xlabel_y), config.xlabel, fill=(0, 0, 0), font=font)
            
            # تسمية المحور الصادي
            if config.ylabel:
                # رسم النص بشكل عمودي (تقريبي)
                ylabel_x = 20
                ylabel_y = y + height // 2
                draw.text((ylabel_x, ylabel_y), config.ylabel, fill=(0, 0, 0), font=font)
        
        except Exception as e:
            # في حالة عدم توفر الخط
            pass
    
    def save_plot(self, image: Image.Image, filename: str) -> bool:
        """حفظ الرسم البياني"""
        try:
            image.save(filename)
            return True
        except Exception as e:
            print(f"❌ خطأ في حفظ الرسم البياني: {e}")
            return False
    
    def create_heatmap(self, data: List[List[float]], 
                      config: PlotConfig = None) -> Image.Image:
        """إنشاء خريطة حرارية"""
        if config is None:
            config = PlotConfig()
        
        image = Image.new('RGB', (config.width, config.height), config.background_color)
        draw = ImageDraw.Draw(image)
        
        if not data or not data[0]:
            return image
        
        rows = len(data)
        cols = len(data[0])
        
        # حساب منطقة الرسم
        margin = 80
        plot_x = margin
        plot_y = margin
        plot_width = config.width - 2 * margin
        plot_height = config.height - 2 * margin
        
        # حساب حجم كل خلية
        cell_width = plot_width / cols
        cell_height = plot_height / rows
        
        # العثور على القيم الدنيا والعليا
        flat_data = [val for row in data for val in row]
        min_val = min(flat_data)
        max_val = max(flat_data)
        val_range = max_val - min_val if max_val > min_val else 1
        
        # رسم الخلايا
        for i in range(rows):
            for j in range(cols):
                # تطبيع القيمة
                normalized_val = (data[i][j] - min_val) / val_range
                
                # تحديد اللون بناء على القيمة
                intensity = int(255 * normalized_val)
                color = (intensity, 0, 255 - intensity)  # من الأزرق إلى الأحمر
                
                # رسم الخلية
                x1 = plot_x + j * cell_width
                y1 = plot_y + i * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height
                
                draw.rectangle([x1, y1, x2, y2], fill=color, outline=(255, 255, 255))
        
        # إضافة العناوين
        self._add_labels(draw, config, plot_x, plot_y, plot_width, plot_height)
        
        return image
    
    def create_histogram(self, data: List[float], bins: int = 10, 
                        config: PlotConfig = None) -> Image.Image:
        """إنشاء رسم بياني تكراري"""
        if config is None:
            config = PlotConfig()
        
        if not data:
            return Image.new('RGB', (config.width, config.height), config.background_color)
        
        # حساب التوزيع التكراري
        min_val = min(data)
        max_val = max(data)
        bin_width = (max_val - min_val) / bins if max_val > min_val else 1
        
        # إنشاء الفئات
        bin_counts = [0] * bins
        bin_centers = []
        
        for i in range(bins):
            bin_start = min_val + i * bin_width
            bin_end = bin_start + bin_width
            bin_centers.append((bin_start + bin_end) / 2)
            
            # عد القيم في هذه الفئة
            for value in data:
                if bin_start <= value < bin_end or (i == bins - 1 and value == bin_end):
                    bin_counts[i] += 1
        
        # إنشاء رسم بياني بالأعمدة
        categories = [f"{center:.2f}" for center in bin_centers]
        return self.create_bar_plot(categories, bin_counts, config)
    
    def apply_revolutionary_styling(self, image: Image.Image, 
                                   theory: str = "combined") -> Image.Image:
        """تطبيق التصميم الثوري على الرسم البياني"""
        # تحويل إلى numpy array للمعالجة
        img_array = np.array(image)
        
        if theory == "zero_duality":
            # تطبيق ثنائية الصفر - توازن الألوان
            img_array = self._apply_zero_duality_styling(img_array)
        elif theory == "perpendicularity":
            # تطبيق التعامد - تحسين التباين
            img_array = self._apply_perpendicularity_styling(img_array)
        elif theory == "filament":
            # تطبيق الفتائل - تحسين الترابط البصري
            img_array = self._apply_filament_styling(img_array)
        else:
            # تطبيق النظريات الثلاث
            img_array = self._apply_zero_duality_styling(img_array)
            img_array = self._apply_perpendicularity_styling(img_array)
            img_array = self._apply_filament_styling(img_array)
        
        # تحويل إلى PIL Image
        return Image.fromarray(img_array.astype(np.uint8))
    
    def _apply_zero_duality_styling(self, img_array: np.ndarray) -> np.ndarray:
        """تطبيق تصميم ثنائية الصفر"""
        # تحسين التوازن اللوني
        for channel in range(3):
            channel_data = img_array[:, :, channel]
            mean_val = np.mean(channel_data)
            
            # تطبيق معادلة ثنائية الصفر
            alpha = 1.1
            gamma = 2.5
            
            normalized = channel_data / 255.0
            enhanced = alpha * (1 / (1 + np.exp(-gamma * (normalized - 0.5))))
            img_array[:, :, channel] = np.clip(enhanced * 255, 0, 255)
        
        return img_array
    
    def _apply_perpendicularity_styling(self, img_array: np.ndarray) -> np.ndarray:
        """تطبيق تصميم التعامد"""
        # تحسين التباين
        for channel in range(3):
            channel_data = img_array[:, :, channel].astype(float)
            
            # تطبيق معادلة التعامد
            theta = 1.2
            phi = 1.3
            
            normalized = channel_data / 255.0
            enhanced = phi * np.sin(theta * np.pi * normalized)
            enhanced = np.abs(enhanced) * 255
            
            img_array[:, :, channel] = np.clip(enhanced, 0, 255)
        
        return img_array
    
    def _apply_filament_styling(self, img_array: np.ndarray) -> np.ndarray:
        """تطبيق تصميم الفتائل"""
        # تحسين الترابط البصري
        height, width = img_array.shape[:2]
        
        # تطبيق مرشح الفتائل
        lambda_param = 3.0
        mu = 0.5
        sigma = 1.5
        
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                for channel in range(3):
                    # حساب التباين المحلي
                    window = img_array[i-1:i+2, j-1:j+2, channel]
                    local_var = np.var(window) / (255.0 ** 2)
                    
                    # تطبيق معادلة الفتائل
                    enhancement = lambda_param * math.exp(-((local_var - mu) ** 2) / (2 * sigma ** 2))
                    
                    # تطبيق التحسين
                    original_val = img_array[i, j, channel]
                    enhanced_val = original_val * (1 + enhancement * 0.2)
                    img_array[i, j, channel] = np.clip(enhanced_val, 0, 255)
        
        return img_array
