"""
Generalized Shape Equation (GSE) Model
======================================

A mathematical framework for function approximation using Modified Sigmoid Functions
and Linear Components.

Based on the research: "A Comprehensive Mathematical Model for Function Approximation
Using Modified Sigmoid Functions and Linear Components" by Bassel Yahya Abdullah.
"""

import numpy as np

def generalized_sigmoid(x, n, k, x0=0):
    """
    Generalized Sigmoid Function.
    
    Formula: σₙ(x; k, x₀) = 1 / (1 + e^(-k(x - x₀)^n))
    
    Args:
        x (array-like): Input values.
        n (int): Chopping coefficient (controls shape/symmetry).
        k (float): Sharpness coefficient.
        x0 (float): Midpoint/center of transition.
        
    Returns:
        array-like: Sigmoid values.
    """
    # Ensure x is a numpy array for element-wise operations
    x = np.array(x, dtype=np.float64)
    
    # Calculate exponent term: -k * (x - x0)^n
    # We use np.power for element-wise power
    # Note: For even n, (x-x0)^n is positive. For odd n, it preserves sign.
    term = x - x0
    
    # Handle potential overflow/underflow in exp
    # If k is very large, the exponent can be huge.
    # We can clip the exponent to a safe range to avoid RuntimeWarnings
    # but for mathematical precision in this model, we'll rely on numpy's handling
    # or use 128-bit floats if needed. For now, standard float64.
    
    exponent = -k * np.power(term, n)
    
    # Sigmoid formula
    return 1.0 / (1.0 + np.exp(exponent))


def linear_component(x, beta, gamma):
    """
    Linear Component for global trends.
    
    Formula: L(x; β, γ) = βx + γ
    
    Args:
        x (array-like): Input values.
        beta (float): Slope.
        gamma (float): Y-intercept.
        
    Returns:
        array-like: Linear values.
    """
    return beta * x + gamma


class GSEModel:
    """
    Generalized Shape Equation Model.
    
    Represents a function as a superposition of sigmoid components and a linear component.
    
    f̂(x) = Σ(αᵢ · σₙᵢ(x; kᵢ, x₀ᵢ)) + L(x; β, γ)
    """
    
    def __init__(self, beta=0.0, gamma=0.0):
        """
        Initialize GSE Model.
        
        Args:
            beta (float): Slope of linear component.
            gamma (float): Intercept of linear component.
        """
        self.beta = beta
        self.gamma = gamma
        self.components = [] # List of dicts: {'alpha': float, 'n': int, 'k': float, 'x0': float}
        
    def add_sigmoid(self, alpha, n, k, x0=0):
        """
        Add a generalized sigmoid component.
        
        Args:
            alpha (float): Weight/Amplitude.
            n (int): Chopping coefficient.
            k (float): Sharpness coefficient.
            x0 (float): Center position.
        """
        self.components.append({
            'alpha': alpha,
            'n': n,
            'k': k,
            'x0': x0
        })
        
    def evaluate(self, x):
        """
        Evaluate the model at given points.
        
        Args:
            x (array-like): Input values.
            
        Returns:
            array-like: Model output values.
        """
        x = np.array(x)
        
        # Start with linear component
        y = linear_component(x, self.beta, self.gamma)
        
        # Add sigmoid components
        for comp in self.components:
            sig = generalized_sigmoid(x, comp['n'], comp['k'], comp['x0'])
            y += comp['alpha'] * sig
            
        return y
        
    def clear_components(self):
        """Remove all sigmoid components."""
        self.components = []


def approximate_gate(x, a, b, n, k):
    """
    Create a gate function (rectangular pulse) using two sigmoids.
    
    G(x) ≈ σ(x; k, a) - σ(x; k, b)
    
    Args:
        x (array-like): Input values.
        a (float): Start of gate (rising edge).
        b (float): End of gate (falling edge).
        n (int): Chopping coefficient (usually odd for step-like behavior).
        k (float): Sharpness coefficient.
        
    Returns:
        array-like: Gate values (approx 1 between a and b, 0 otherwise).
    """
    entry = generalized_sigmoid(x, n, k, a)
    exit_val = generalized_sigmoid(x, n, k, b)
    return entry - exit_val
