#!/usr/bin/env python3
"""
Bayan Benchmark Runner
تشغيل جميع اختبارات الأداء لـ Bayan

Usage:
    python run_all_benchmarks.py
    python run_all_benchmarks.py --category logic
    python run_all_benchmarks.py --iterations 10
"""

import sys
import os
import subprocess
import time
import json
import argparse
from datetime import datetime
from pathlib import Path

# Add Bayan to path
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT))

from bayan.bayan.hybrid_interpreter import HybridInterpreter
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser


class BenchmarkRunner:
    def __init__(self, iterations=5):
        self.iterations = iterations
        self.results = {}
        self.benchmark_dir = SCRIPT_DIR
        
    def run_bayan_file(self, filepath):
        """تشغيل ملف Bayan وقياس الوقت"""
        print(f"\n{'='*60}")
        print(f"Running: {filepath.name}")
        print(f"{'='*60}")
        
        times = []
        
        for i in range(self.iterations):
            print(f"[Iteration {i+1}/{self.iterations}]", end=" ", flush=True)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                code = f.read()
            
            start = time.perf_counter()
            
            try:
                lexer = HybridLexer(code)
                tokens = lexer.tokenize()
                parser = HybridParser(tokens)
                ast = parser.parse()
                interpreter = HybridInterpreter()
                interpreter.interpret(ast)
                
                elapsed = time.perf_counter() - start
                times.append(elapsed)
                print(f"✓ {elapsed:.3f}s")
                
            except Exception as e:
                print(f"✗ Error: {str(e)}")
                return None
        
        if times:
            result = {
                "min": min(times),
                "max": max(times),
                "mean": sum(times) / len(times),
                "median": sorted(times)[len(times) // 2],
                "times": times
            }
            
            print(f"\nResults for {filepath.name}:")
            print(f"  Min:    {result['min']:.3f}s")
            print(f"  Max:    {result['max']:.3f}s")
            print(f"  Mean:   {result['mean']:.3f}s")
            print(f"  Median: {result['median']:.3f}s")
            
            return result
        
        return None
    
    def run_category(self, category):
        """تشغيل جميع benchmarks في فئة معينة"""
        bayan_dir = self.benchmark_dir / "bayan"
        
        category_files = {
            "logic": "logic_benchmarks.bayan",
            "oop": "oop_benchmarks.bayan",
            "data": "data_structures.bayan",
            "hybrid": "hybrid_benchmarks.bayan"
        }
        
        if category == "all":
            files_to_run = list(category_files.values())
        elif category in category_files:
            files_to_run = [category_files[category]]
        else:
            print(f"Unknown category: {category}")
            print(f"Available: {', '.join(category_files.keys())}, all")
            return
        
        for filename in files_to_run:
            filepath = bayan_dir / filename
            if filepath.exists():
                result = self.run_bayan_file(filepath)
                if result:
                    self.results[filename] = result
            else:
                print(f"File not found: {filepath}")
    
    def save_results(self):
        """حفظ النتائج إلى ملف JSON"""
        results_dir = self.benchmark_dir / "results"
        results_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = results_dir / f"benchmark_results_{timestamp}.json"
        
        output_data = {
            "timestamp": datetime.now().isoformat(),
            "iterations": self.iterations,
            "python_version": sys.version,
            "benchmarks": self.results
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n{'='*60}")
        print(f"Results saved to: {output_file}")
        print(f"{'='*60}")
        
        return output_file


def main():
    parser = argparse.ArgumentParser(
        description="Run Bayan benchmarks",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--category",
        choices=["logic", "oop", "data", "hybrid", "all"],
        default="all",
        help="Benchmark category to run (default: all)"
    )
    
    parser.add_argument(
        "--iterations",
        type=int,
        default=5,
        help="Number of iterations per benchmark (default: 5)"
    )
    
    args = parser.parse_args()
    
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║   Bayan Performance Benchmark Suite                      ║")
    print("║   مجموعة اختبارات الأداء للغة البيان                     ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    print()
    print(f"Category: {args.category}")
    print(f"Iterations: {args.iterations}")
    print()
    
    runner = BenchmarkRunner(iterations=args.iterations)
    runner.run_category(args.category)
    
    if runner.results:
        output_file = runner.save_results()
        
        print("\nTo generate HTML report, run:")
        print(f"  python report_generator.py {output_file}")
    else:
        print("\nNo benchmark results collected.")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
