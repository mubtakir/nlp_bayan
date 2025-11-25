#!/usr/bin/env python3
"""
GSE Adaptive Learning Demo
==========================

Demonstrates the "Adaptive Dynamic Equation Intelligence" capability.
The model will "learn" the shape of a noisy, complex function from scratch.
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bayan.bayan.gse import GSEModel
from bayan.bayan.gse_fitting import GSEFitter

def complex_target_function(x):
    """A complex function: combination of sine, step, and linear trend."""
    # f(x) = 0.5x + sin(x) + step at x=5
    y = 0.5 * x + np.sin(x)
    y += np.where(x > 5, 2.0, 0.0)
    return y

def main():
    print("--- GSE Adaptive Learning Demo ---")
    
    # 1. Generate Data
    print("Generating noisy data...")
    x_data = np.linspace(0, 10, 200)
    y_true = complex_target_function(x_data)
    # Add noise
    noise = np.random.normal(0, 0.2, size=len(x_data))
    y_noisy = y_true + noise
    
    # 2. Initialize Model and Fitter
    model = GSEModel()
    fitter = GSEFitter(model)
    
    # 3. Fit Model (Learn)
    print("Starting learning process (Fitting)...")
    try:
        fitter.fit(x_data, y_noisy, max_components=8, verbose=True)
    except ImportError as e:
        print(f"Error: {e}")
        return

    # 4. Evaluate
    y_pred = model.evaluate(x_data)
    mse = np.mean((y_true - y_pred)**2)
    print(f"Final MSE against true function: {mse:.6f}")
    
    # 5. Visualize
    print("Plotting results...")
    plt.figure(figsize=(12, 8))
    plt.scatter(x_data, y_noisy, c='gray', alpha=0.5, label='Noisy Observations')
    plt.plot(x_data, y_true, 'k--', lw=2, label='True Function (Hidden)')
    plt.plot(x_data, y_pred, 'r-', lw=3, label='GSE Learned Model')
    
    # Plot individual components to show "thinking"
    y_linear = model.beta * x_data + model.gamma
    plt.plot(x_data, y_linear, 'b:', alpha=0.6, label='Linear Trend')
    
    plt.title('Adaptive GSE: Learning a Complex Function from Noisy Data')
    plt.legend()
    plt.grid(True)
    plt.savefig('gse_adaptive_result.png')
    print("Saved visualization to 'gse_adaptive_result.png'")
    
    # Print the "Learned Equation"
    print("\nLearned Equation Structure:")
    print(f"Linear: {model.beta:.3f}x + {model.gamma:.3f}")
    for i, c in enumerate(model.components):
        print(f"Component {i+1}: α={c['alpha']:.3f}, n={c['n']}, k={c['k']:.3f}, x0={c['x0']:.3f}")

if __name__ == '__main__':
    main()
