#!/usr/bin/env python3
"""
Bayan Benchmark Report Generator
توليد تقارير الأداء بصيغة HTML

Usage:
    python report_generator.py results/benchmark_results_20251125.json
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime


class ReportGenerator:
    def __init__(self, results_file):
        self.results_file = Path(results_file)
        self.data = self.load_results()
        
    def load_results(self):
        """تحميل نتائج البنشمارك"""
        with open(self.results_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def generate_html(self):
        """توليد تقرير HTML"""
        
        benchmarks = self.data.get('benchmarks', {})
        
        html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bayan Performance Report - تقرير أداء البيان</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .subtitle {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .metadata {{
            background: #f8f9fa;
            padding: 20px 40px;
            border-bottom: 2px solid #e9ecef;
        }}
        
        .metadata-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }}
        
        .metadata-item {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .metadata-label {{
            font-weight: bold;
            color: #495057;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .benchmark-section {{
            margin-bottom: 40px;
            border: 1px solid #e9ecef;
            border-radius: 10px;
            overflow: hidden;
        }}
        
        .benchmark-header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            font-size: 1.3em;
            font-weight: bold;
        }}
        
        .benchmark-stats {{
            padding: 20px;
            background: #f8f9fa;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
        }}
        
        .stat-card {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }}
        
        .stat-label {{
            font-size: 0.9em;
            color: #6c757d;
            margin-bottom: 5px;
        }}
        
        .stat-value {{
            font-size: 1.8em;
            font-weight: bold;
            color: #667eea;
        }}
        
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #6c757d;
            border-top: 2px solid #e9ecef;
        }}
        
        .badge {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 0.85em;
            font-weight: bold;
        }}
        
        .badge-success {{
            background: #28a745;
            color: white;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 تقرير أداء لغة البيان</h1>
            <p class="subtitle">Bayan Performance Benchmark Report</p>
        </header>
        
        <div class="metadata">
            <div class="metadata-grid">
                <div class="metadata-item">
                    <span class="metadata-label">📅 Date:</span>
                    <span>{self.data.get('timestamp', 'N/A')}</span>
                </div>
                <div class="metadata-item">
                    <span class="metadata-label">🔄 Iterations:</span>
                    <span>{self.data.get('iterations', 'N/A')}</span>
                </div>
                <div class="metadata-item">
                    <span class="metadata-label">🐍 Python:</span>
                    <span>{self.data.get('python_version', 'N/A').split()[0]}</span>
                </div>
                <div class="metadata-item">
                    <span class="metadata-label">📊 Benchmarks:</span>
                    <span>{len(benchmarks)}</span>
                </div>
            </div>
        </div>
        
        <div class="content">
"""
        
        # Add benchmark sections
        for name, stats in benchmarks.items():
            html += f"""
            <div class="benchmark-section">
                <div class="benchmark-header">
                    {name.replace('_', ' ').title()}
                    <span class="badge badge-success">✓ Complete</span>
                </div>
                <div class="benchmark-stats">
                    <div class="stats-grid">
                        <div class="stat-card">
                            <div class="stat-label">Minimum</div>
                            <div class="stat-value">{stats['min']:.3f}s</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-label">Maximum</div>
                            <div class="stat-value">{stats['max']:.3f}s</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-label">Mean</div>
                            <div class="stat-value">{stats['mean']:.3f}s</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-label">Median</div>
                            <div class="stat-value">{stats['median']:.3f}s</div>
                        </div>
                    </div>
                </div>
            </div>
"""
        
        html += """
        </div>
        
        <div class="footer">
            <p>Generated by Bayan Benchmark Suite</p>
            <p>لغة البيان - Bayan Programming Language</p>
        </div>
    </div>
</body>
</html>
"""
        
        return html
    
    def save_report(self):
        """حفظ التقرير"""
        output_file = self.results_file.parent / f"performance_report_{self.results_file.stem}.html"
        
        html = self.generate_html()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✓ Report generated: {output_file}")
        print(f"\nOpen in browser:")
        print(f"  file://{output_file.absolute()}")
        
        return output_file


def main():
    parser = argparse.ArgumentParser(
        description="Generate HTML report from benchmark results"
    )
    
    parser.add_argument(
        "results_file",
        help="Path to benchmark results JSON file"
    )
    
    args = parser.parse_args()
    
    if not Path(args.results_file).exists():
        print(f"Error: File not found: {args.results_file}")
        return 1
    
    generator = ReportGenerator(args.results_file)
    generator.save_report()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
