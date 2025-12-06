"""
📊 نظام التصور البصري للمعادلات اللغوية
Equation Visualizer - Visual representation of Linguistic Equations

يحول المعادلات اللغوية إلى:
- رسوم بيانية SVG
- خطوط زمنية
- شبكات سببية
"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
import html


@dataclass
class VisualNode:
    """عقدة في الرسم البياني"""
    id: str
    label: str
    node_type: str  # subject, verb, object, result
    x: float
    y: float
    color: str = "#3498db"
    

@dataclass
class VisualEdge:
    """رابط بين عقدتين"""
    source: str
    target: str
    label: str = ""
    color: str = "#2c3e50"


class EquationVisualizer:
    """
    مُصوِّر المعادلات اللغوية
    يحول المعادلات إلى رسوم SVG تفاعلية
    """
    
    # ألوان العناصر
    COLORS = {
        "subject": "#3498db",   # أزرق - الفاعل
        "verb": "#2ecc71",      # أخضر - الفعل
        "object": "#e74c3c",    # أحمر - المفعول به
        "result": "#9b59b6",    # بنفسجي - النتيجة
        "arrow": "#2c3e50",     # رمادي غامق - الأسهم
        "background": "#ecf0f1", # رمادي فاتح - الخلفية
    }
    
    def __init__(self, width: int = 900, height: int = 500):
        self.width = width
        self.height = height
    
    def visualize_equation(self, 
                          subject: str, 
                          verb: str, 
                          obj: str,
                          results: Optional[List[Dict]] = None) -> str:
        """
        تصور معادلة لغوية واحدة
        
        Args:
            subject: الفاعل
            verb: الفعل
            obj: المفعول به
            results: النتائج (اختياري)
        
        Returns:
            كود SVG
        """
        # تنظيف النص
        subject = html.escape(subject)
        verb = html.escape(verb)
        obj = html.escape(obj)
        
        # حساب المواقع
        center_y = self.height // 2
        spacing = self.width // 4
        
        svg_parts = [
            self._svg_header(),
            self._svg_defs(),
            
            # الفاعل (دائرة)
            self._create_circle(spacing, center_y, 60, self.COLORS["subject"], subject, "الفاعل"),
            
            # سهم 1
            self._create_arrow(spacing + 70, center_y, spacing * 2 - 60, center_y),
            
            # الفعل (مستطيل)
            self._create_rect(spacing * 2, center_y, 120, 60, self.COLORS["verb"], verb, "الحدث"),
            
            # سهم 2
            self._create_arrow(spacing * 2 + 70, center_y, spacing * 3 - 70, center_y),
            
            # المفعول به (دائرة)
            self._create_circle(spacing * 3, center_y, 60, self.COLORS["object"], obj, "المفعول به"),
        ]
        
        # إضافة النتائج إذا وجدت
        if results:
            svg_parts.append(self._create_results_section(results, spacing * 3, center_y + 100))
        
        # العنوان
        svg_parts.append(f'''
            <text x="{self.width // 2}" y="40" 
                  text-anchor="middle" 
                  class="title"
                  font-size="24" 
                  fill="#2c3e50"
                  font-family="Arial, sans-serif">
                المعادلة اللغوية
            </text>
        ''')
        
        # الصيغة الرياضية
        formula = f"{subject} + {verb} → {obj}"
        svg_parts.append(f'''
            <text x="{self.width // 2}" y="{self.height - 30}" 
                  text-anchor="middle"
                  font-size="18"
                  fill="#7f8c8d"
                  font-family="Arial, sans-serif">
                {formula}
            </text>
        ''')
        
        svg_parts.append("</svg>")
        return "\n".join(svg_parts)
    
    def _svg_header(self) -> str:
        return f'''<svg xmlns="http://www.w3.org/2000/svg" 
             width="{self.width}" height="{self.height}"
             viewBox="0 0 {self.width} {self.height}"
             style="background: {self.COLORS['background']}; direction: rtl;">'''
    
    def _svg_defs(self) -> str:
        return '''
        <defs>
            <marker id="arrowhead" markerWidth="10" markerHeight="7"
                    refX="9" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="#2c3e50"/>
            </marker>
            <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
                <feDropShadow dx="2" dy="2" stdDeviation="3" flood-opacity="0.3"/>
            </filter>
        </defs>'''

    def _create_circle(self, cx: float, cy: float, r: float,
                       color: str, text: str, label: str) -> str:
        return f'''
        <g class="node" transform="translate({cx}, {cy})">
            <circle r="{r}" fill="{color}" filter="url(#shadow)" opacity="0.9"/>
            <text y="5" text-anchor="middle" fill="white"
                  font-size="18" font-family="Arial, sans-serif" font-weight="bold">
                {text}
            </text>
            <text y="{r + 20}" text-anchor="middle" fill="#7f8c8d"
                  font-size="12" font-family="Arial, sans-serif">
                {label}
            </text>
        </g>'''

    def _create_rect(self, cx: float, cy: float, w: float, h: float,
                     color: str, text: str, label: str) -> str:
        return f'''
        <g class="node" transform="translate({cx}, {cy})">
            <rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}"
                  rx="10" fill="{color}" filter="url(#shadow)" opacity="0.9"/>
            <text y="5" text-anchor="middle" fill="white"
                  font-size="18" font-family="Arial, sans-serif" font-weight="bold">
                {text}
            </text>
            <text y="{h/2 + 20}" text-anchor="middle" fill="#7f8c8d"
                  font-size="12" font-family="Arial, sans-serif">
                {label}
            </text>
        </g>'''

    def _create_arrow(self, x1: float, y1: float, x2: float, y2: float) -> str:
        return f'''
        <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"
              stroke="{self.COLORS['arrow']}" stroke-width="3"
              marker-end="url(#arrowhead)"/>'''

    def _create_results_section(self, results: List[Dict], x: float, y: float) -> str:
        parts = [f'<g transform="translate({x}, {y})">']
        parts.append(f'''
            <text x="0" y="0" text-anchor="middle" fill="#9b59b6"
                  font-size="16" font-family="Arial, sans-serif" font-weight="bold">
                ↓ النتائج
            </text>
        ''')

        for i, result in enumerate(results[:3]):  # أول 3 نتائج
            entity = result.get("entity", "")
            change = result.get("change", "")
            parts.append(f'''
                <text x="0" y="{25 + i * 20}" text-anchor="middle" fill="#7f8c8d"
                      font-size="14" font-family="Arial, sans-serif">
                    {entity}: {change}
                </text>
            ''')

        parts.append("</g>")
        return "\n".join(parts)

    def visualize_timeline(self, events: List[Dict]) -> str:
        """
        تصور سلسلة أحداث كخط زمني

        Args:
            events: قائمة الأحداث [{subject, verb, object, time}]
        """
        svg_parts = [self._svg_header(), self._svg_defs()]

        # خط الزمن الرئيسي
        line_y = self.height // 2
        svg_parts.append(f'''
            <line x1="50" y1="{line_y}" x2="{self.width - 50}" y2="{line_y}"
                  stroke="#bdc3c7" stroke-width="4"/>
        ''')

        # الأحداث
        n = len(events)
        if n > 0:
            spacing = (self.width - 100) / n
            for i, event in enumerate(events):
                x = 50 + spacing * (i + 0.5)
                color = self.COLORS["verb"]

                # النقطة
                svg_parts.append(f'''
                    <circle cx="{x}" cy="{line_y}" r="15" fill="{color}"
                            filter="url(#shadow)"/>
                ''')

                # النص
                text = event.get("verb", f"حدث {i+1}")
                subject = event.get("subject", "")
                svg_parts.append(f'''
                    <text x="{x}" y="{line_y - 30}" text-anchor="middle"
                          fill="#2c3e50" font-size="14" font-family="Arial">
                        {html.escape(text)}
                    </text>
                    <text x="{x}" y="{line_y + 40}" text-anchor="middle"
                          fill="#7f8c8d" font-size="12" font-family="Arial">
                        {html.escape(subject)}
                    </text>
                ''')

        svg_parts.append("</svg>")
        return "\n".join(svg_parts)

    def save_to_file(self, svg_content: str, filename: str) -> str:
        """حفظ SVG في ملف HTML"""
        html_content = f'''<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <title>تصور المعادلة اللغوية</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
    </style>
</head>
<body>
    <div class="container">
        {svg_content}
    </div>
</body>
</html>'''

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

        return filename


# دالة مساعدة سريعة
def visualize(subject: str, verb: str, obj: str,
              results: List[Dict] = None, save_to: str = None) -> str:
    """
    تصور معادلة لغوية بسرعة

    مثال:
        svg = visualize("أحمد", "أكل", "تفاحة")
    """
    viz = EquationVisualizer()
    svg = viz.visualize_equation(subject, verb, obj, results)

    if save_to:
        viz.save_to_file(svg, save_to)

    return svg

