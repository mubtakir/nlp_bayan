"""
محرك التصور البصري لمعادلات GSE
GSE Visualization Engine

يوفر أدوات لرسم وتحليل معادلات الشكل المعممة (GSE) بصرياً.
مستوحى من sigmoid-drawing-engine.bn

المؤلف: باسل يحيى عبد الله
التاريخ: 2025-11-25
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from typing import List, Tuple, Optional, Dict
import os

from .gse import GSEModel, generalized_sigmoid


# ═══════════════════════════════════════════════════════════════
# الألوان الافتراضية
# ═══════════════════════════════════════════════════════════════

DEFAULT_COLORS = [
    "#ef4444",  # أحمر
    "#f59e0b",  # برتقالي
    "#10b981",  # أخضر
    "#3b82f6",  # أزرق
    "#8b5cf6",  # بنفسجي
    "#ec4899",  # وردي
    "#06b6d4",  # سماوي
    "#84cc16",  # ليموني
]

LINEAR_COLOR = "#94a3b8"      # رمادي للمكون الخطي
TOTAL_COLOR = "#000000"        # أسود للمعادلة الكاملة
GRID_COLOR = "#e2e8f0"         # رمادي فاتح للشبكة
AXES_COLOR = "#94a3b8"         # رمادي للمحاور


# ═══════════════════════════════════════════════════════════════
# إحصائيات الرسم
# ═══════════════════════════════════════════════════════════════

class DrawingStats:
    """إحصائيات محرك الرسم"""
    
    def __init__(self):
        self.shapes_drawn = 0
        self.components_visualized = 0
        self.points_plotted = 0
        self.last_draw_time = 0.0
    
    def reset(self):
        """إعادة تعيين الإحصائيات"""
        self.shapes_drawn = 0
        self.components_visualized = 0
        self.points_plotted = 0
        self.last_draw_time = 0.0
    
    def to_dict(self) -> Dict:
        """تحويل إلى قاموس"""
        avg_points = (self.points_plotted / self.shapes_drawn 
                     if self.shapes_drawn > 0 else 0)
        
        return {
            'shapes_drawn': self.shapes_drawn,
            'components_visualized': self.components_visualized,
            'points_plotted': self.points_plotted,
            'last_draw_time_ms': round(self.last_draw_time * 1000, 2),
            'avg_points_per_shape': int(avg_points)
        }


# إحصائيات عامة للمحرك
_global_stats = DrawingStats()


# ═══════════════════════════════════════════════════════════════
# دوال الرسم الأساسية
# ═══════════════════════════════════════════════════════════════

def plot_gse_model(
    model: GSEModel,
    x_range: Tuple[float, float] = (-10, 10),
    resolution: int = 500,
    title: str = "GSE Model",
    figsize: Tuple[int, int] = (10, 6),
    show_grid: bool = True,
    save_path: Optional[str] = None
) -> Figure:
    """
    رسم نموذج GSE.
    
    Args:
        model: نموذج GSE
        x_range: نطاق القيم (min, max)
        resolution: عدد النقاط
        title: عنوان الرسم
        figsize: حجم الشكل
        show_grid: عرض الشبكة
        save_path: مسار حفظ الصورة (اختياري)
    
    Returns:
        Figure object
    """
    import time
    start_time = time.time()
    
    # توليد النقاط
    x = np.linspace(x_range[0], x_range[1], resolution)
    y = model.evaluate(x)
    
    # إنشاء الرسم
    fig, ax = plt.subplots(figsize=figsize)
    
    # رسم المنحنى
    ax.plot(x, y, color=TOTAL_COLOR, linewidth=2, label='Total')
    
    # المحاور والشبكة
    ax.axhline(y=0, color=AXES_COLOR, linestyle='-', linewidth=0.8)
    ax.axvline(x=0, color=AXES_COLOR, linestyle='-', linewidth=0.8)
    
    if show_grid:
        ax.grid(True, color=GRID_COLOR, linestyle='-', linewidth=0.5, alpha=0.7)
    
    # العنوان والتسميات
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('f(x)', fontsize=12)
    ax.legend()
    
    # حفظ الصورة
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"✓ تم حفظ الصورة: {save_path}")
    
    # تحديث الإحصائيات
    _global_stats.shapes_drawn += 1
    _global_stats.points_plotted += resolution
    _global_stats.last_draw_time = time.time() - start_time
    
    return fig


def visualize_components(
    model: GSEModel,
    x_range: Tuple[float, float] = (-10, 10),
    resolution: int = 500,
    title: str = "GSE Components Visualization",
    figsize: Tuple[int, int] = (12, 8),
    save_path: Optional[str] = None
) -> Figure:
    """
    رسم كل مكون من مكونات GSE بلون منفصل.
    
    هذه الدالة مستوحاة من visualizeTerms() في sigmoid-drawing-engine.bn
    
    Args:
        model: نموذج GSE
        x_range: نطاق القيم
        resolution: عدد النقاط
        title: عنوان الرسم
        figsize: حجم الشكل
        save_path: مسار حفظ الصورة
    
    Returns:
        Figure object
    """
    import time
    start_time = time.time()
    
    x = np.linspace(x_range[0], x_range[1], resolution)
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # 1. رسم المكون الخطي
    if model.beta != 0 or model.gamma != 0:
        y_linear = model.beta * x + model.gamma
        ax.plot(x, y_linear, color=LINEAR_COLOR, linewidth=1.5, 
                linestyle='--', label=f'Linear: {model.beta:.2f}x + {model.gamma:.2f}',
                alpha=0.7)
    
    # 2. رسم كل مكون sigmoid بلون مختلف
    for i, comp in enumerate(model.components):
        # حساب sigmoid واحد
        y_comp = comp['alpha'] * generalized_sigmoid(
            x, comp['n'], comp['k'], comp['x0']
        )
        
        color = DEFAULT_COLORS[i % len(DEFAULT_COLORS)]
        label = f"S{i+1}: α={comp['alpha']:.2f}, n={comp['n']}, k={comp['k']:.2f}"
        
        ax.plot(x, y_comp, color=color, linewidth=1.5, 
                label=label, alpha=0.8)
    
    # 3. رسم المعادلة الكاملة
    y_total = model.evaluate(x)
    ax.plot(x, y_total, color=TOTAL_COLOR, linewidth=2.5, 
            label='Total (Sum)', linestyle='-')
    
    # المحاور والشبكة
    ax.axhline(y=0, color=AXES_COLOR, linestyle='-', linewidth=0.8)
    ax.axvline(x=0, color=AXES_COLOR, linestyle='-', linewidth=0.8)
    ax.grid(True, color=GRID_COLOR, linestyle='-', linewidth=0.5, alpha=0.7)
    
    # العنوان والتسميات
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('f(x)', fontsize=12)
    ax.legend(loc='best', fontsize=9)
    
    # معلومات إضافية
    info_text = f"Components: {len(model.components)} sigmoids + linear"
    ax.text(0.02, 0.98, info_text, transform=ax.transAxes,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    # حفظ الصورة
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"✓ تم حفظ الصورة: {save_path}")
    
    # تحديث الإحصائيات
    _global_stats.shapes_drawn += 1
    _global_stats.components_visualized += len(model.components) + 1  # +1 للخطي
    _global_stats.points_plotted += resolution * (len(model.components) + 2)
    _global_stats.last_draw_time = time.time() - start_time
    
    return fig


def plot_parametric(
    x_model: GSEModel,
    y_model: GSEModel,
    t_range: Tuple[float, float] = (0, 2*np.pi),
    resolution: int = 500,
    title: str = "Parametric Curve",
    figsize: Tuple[int, int] = (8, 8),
    save_path: Optional[str] = None
) -> Figure:
    """
    رسم منحنى بارامتري باستخدام نموذجي GSE.
    
    x = x_model(t)
    y = y_model(t)
    
    مستوحى من drawParametric() في sigmoid-drawing-engine.bn
    
    Args:
        x_model: نموذج GSE للإحداثي x
        y_model: نموذج GSE للإحداثي y
        t_range: نطاق المعامل t
        resolution: عدد النقاط
        title: عنوان الرسم
        figsize: حجم الشكل
        save_path: مسار حفظ الصورة
    
    Returns:
        Figure object
    """
    import time
    start_time = time.time()
    
    # توليد النقاط
    t = np.linspace(t_range[0], t_range[1], resolution)
    x = x_model.evaluate(t)
    y = y_model.evaluate(t)
    
    # إنشاء الرسم
    fig, ax = plt.subplots(figsize=figsize)
    
    # رسم المنحنى البارامتري
    ax.plot(x, y, color=DEFAULT_COLORS[0], linewidth=2)
    
    # نقطة البداية والنهاية
    ax.plot(x[0], y[0], 'go', markersize=10, label='Start')
    ax.plot(x[-1], y[-1], 'ro', markersize=10, label='End')
    
    # المحاور والشبكة
    ax.axhline(y=0, color=AXES_COLOR, linestyle='-', linewidth=0.8)
    ax.axvline(x=0, color=AXES_COLOR, linestyle='-', linewidth=0.8)
    ax.grid(True, color=GRID_COLOR, linestyle='-', linewidth=0.5, alpha=0.7)
    
    # العنوان والتسميات
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.legend()
    ax.set_aspect('equal', adjustable='box')
    
    # حفظ الصورة
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"✓ تم حفظ الصورة: {save_path}")
    
    # تحديث الإحصائيات
    _global_stats.shapes_drawn += 1
    _global_stats.points_plotted += resolution
    _global_stats.last_draw_time = time.time() - start_time
    
    return fig


def compare_models(
    models: List[Tuple[GSEModel, str]],
    x_range: Tuple[float, float] = (-10, 10),
    resolution: int = 500,
    title: str = "GSE Models Comparison",
    figsize: Tuple[int, int] = (12, 6),
    save_path: Optional[str] = None
) -> Figure:
    """
    مقارنة عدة نماذج GSE في رسم واحد.
    
    Args:
        models: قائمة من (model, label)
        x_range: نطاق القيم
        resolution: عدد النقاط
        title: عنوان الرسم
        figsize: حجم الشكل
        save_path: مسار حفظ الصورة
    
    Returns:
        Figure object
    """
    x = np.linspace(x_range[0], x_range[1], resolution)
    
    fig, ax = plt.subplots(figsize=figsize)
    
    for i, (model, label) in enumerate(models):
        y = model.evaluate(x)
        color = DEFAULT_COLORS[i % len(DEFAULT_COLORS)]
        ax.plot(x, y, color=color, linewidth=2, label=label)
    
    # المحاور والشبكة
    ax.axhline(y=0, color=AXES_COLOR, linestyle='-', linewidth=0.8)
    ax.axvline(x=0, color=AXES_COLOR, linestyle='-', linewidth=0.8)
    ax.grid(True, color=GRID_COLOR, linestyle='-', linewidth=0.5, alpha=0.7)
    
    # العنوان والتسميات
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('f(x)', fontsize=12)
    ax.legend()
    
    # حفظ الصورة
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"✓ تم حفظ الصورة: {save_path}")
    
    return fig


# ═══════════════════════════════════════════════════════════════
# دوال مساعدة
# ═══════════════════════════════════════════════════════════════

def get_stats() -> Dict:
    """
    الحصول على إحصائيات محرك الرسم.
    
    Returns:
        قاموس بالإحصائيات
    """
    return _global_stats.to_dict()


def reset_stats():
    """إعادة تعيين الإحصائيات"""
    _global_stats.reset()
    print("✓ تم إعادة تعيين إحصائيات محرك الرسم")


def show_plot():
    """عرض الرسوم البيانية"""
    plt.show()


def close_all():
    """إغلاق جميع الرسوم"""
    plt.close('all')
