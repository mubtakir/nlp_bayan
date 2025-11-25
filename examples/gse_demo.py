#!/usr/bin/env python3
"""
GSE Model Demo
==============

Reproduces the examples from the "Generalized Shape Equation" research paper.
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bayan.bayan.gse import generalized_sigmoid, approximate_gate, GSEModel

def setup_plot_style():
    """Configure matplotlib style for publication-quality plots."""
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['axes.unicode_minus'] = False
    
    # Try to use a font that supports Arabic if available, otherwise fallback
    try:
        plt.rcParams['font.serif'] = ['Amiri', 'Times New Roman', 'DejaVu Serif']
    except:
        pass

def demo_unit_step():
    """Example 1: Approximating Unit Step Function"""
    print("Running Example 1: Unit Step Function...")
    
    x_vals = np.linspace(-2, 2, 500)
    
    # True function
    y_true = np.where(x_vals < 0, 0, 1)
    
    # Approximations
    params = [
        {'n': 1, 'k': 10, 'label': 'Soft (n=1, k=10)'},
        {'n': 3, 'k': 20, 'label': 'Sharp (n=3, k=20)'},
        {'n': 5, 'k': 50, 'label': 'Ideal (n=5, k=50)'}
    ]
    
    plt.figure()
    plt.plot(x_vals, y_true, 'k--', lw=3, label='True Step Function')
    
    for p in params:
        y_approx = generalized_sigmoid(x_vals, p['n'], p['k'], 0)
        plt.plot(x_vals, y_approx, lw=2, label=p['label'])
        
    plt.title('Example 1: Unit Step Approximation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.ylim(-0.1, 1.1)
    plt.savefig('gse_example1_step.png')
    print("Saved gse_example1_step.png")

def demo_triangular():
    """Example 2: Approximating Triangular Function"""
    print("Running Example 2: Triangular Function...")
    
    x_vals = np.linspace(-1, 3, 600)
    
    # True function
    # f(x) = x if 0<=x<=1, 2-x if 1<x<=2, 0 otherwise
    conditions = [
        (x_vals >= 0) & (x_vals <= 1),
        (x_vals > 1) & (x_vals <= 2)
    ]
    choices = [x_vals, 2 - x_vals]
    y_true = np.select(conditions, choices, default=0)
    
    # Approximation using gates
    # f̂(x) = x·G(0,1) + (2-x)·G(1,2)
    n, k = 3, 500  # High sharpness
    
    gate1 = approximate_gate(x_vals, 0, 1, n, k)
    gate2 = approximate_gate(x_vals, 1, 2, n, k)
    
    y_approx = x_vals * gate1 + (2 - x_vals) * gate2
    
    plt.figure()
    plt.plot(x_vals, y_true, 'k--', lw=3, label='True Triangular')
    plt.plot(x_vals, y_approx, 'r-', lw=2, label='GSE Approximation')
    
    # Plot gates for visualization
    plt.plot(x_vals, gate1, 'g:', alpha=0.5, label='Gate 1 (0-1)')
    plt.plot(x_vals, gate2, 'b:', alpha=0.5, label='Gate 2 (1-2)')
    
    plt.title('Example 2: Triangular Function')
    plt.legend()
    plt.grid(True)
    plt.savefig('gse_example2_triangular.png')
    print("Saved gse_example2_triangular.png")

def demo_complex():
    """Example 3: Complex Function with Discontinuities"""
    print("Running Example 3: Complex Function...")
    
    pi = np.pi
    x_vals = np.linspace(-1, 3 * pi + 1, 1000)
    
    # True function
    # sin(x) [0, pi], 2 (pi, 2pi], cos(x-2pi) (2pi, 3pi]
    conditions = [
        (x_vals >= 0) & (x_vals <= pi),
        (x_vals > pi) & (x_vals <= 2 * pi),
        (x_vals > 2 * pi) & (x_vals <= 3 * pi)
    ]
    choices = [
        np.sin(x_vals),
        2,
        np.cos(x_vals - 2 * pi)
    ]
    y_true = np.select(conditions, choices, default=0)
    
    # Approximation
    n, k = 19, 150 # Very sharp
    
    gate1 = approximate_gate(x_vals, 0, pi, n, k)
    gate2 = approximate_gate(x_vals, pi, 2*pi, n, k)
    gate3 = approximate_gate(x_vals, 2*pi, 3*pi, n, k)
    
    y_approx = (np.sin(x_vals) * gate1 + 
                2 * gate2 + 
                np.cos(x_vals - 2*pi) * gate3)
                
    plt.figure()
    plt.plot(x_vals, y_true, 'k--', lw=3, label='True Function')
    plt.plot(x_vals, y_approx, 'r-', lw=2, label='GSE Approximation')
    
    plt.title('Example 3: Complex Discontinuous Function')
    plt.legend()
    plt.grid(True)
    plt.savefig('gse_example3_complex.png')
    print("Saved gse_example3_complex.png")

def main():
    setup_plot_style()
    demo_unit_step()
    demo_triangular()
    demo_complex()
    print("\nAll examples completed successfully.")

if __name__ == '__main__':
    main()
