"""
GSE Adaptive Fitting Engine
===========================

Implements the "Adaptive Dynamic Equation Intelligence" algorithms for the GSE model.
This module allows the GSE model to "learn" its shape from data.

Algorithms:
1. Greedy Structural Build-up (Phase 1): Identifies key features and places sigmoid components.
2. Global Fine-Tuning (Phase 2): Optimizes all parameters simultaneously for high precision.
"""

import numpy as np
from .gse import GSEModel, generalized_sigmoid, linear_component

# Try to import scipy for optimization, fallback or error if not present
try:
    from scipy.optimize import minimize, least_squares
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False

class GSEFitter:
    """
    Adaptive fitting engine for GSE Models.
    """
    
    def __init__(self, model=None):
        """
        Initialize fitter.
        
        Args:
            model (GSEModel, optional): Existing model to fit. If None, creates a new one.
        """
        self.model = model if model is not None else GSEModel()
        
    def fit(self, x_data, y_data, max_components=10, epsilon=1e-4, verbose=False):
        """
        Fit the model to data using the two-stage adaptive strategy.
        
        Args:
            x_data (array-like): Input data.
            y_data (array-like): Target data.
            max_components (int): Maximum number of sigmoid components to add.
            epsilon (float): Convergence threshold for MSE.
            verbose (bool): Whether to print progress.
            
        Returns:
            GSEModel: The fitted model.
        """
        if not SCIPY_AVAILABLE:
            raise ImportError("scipy is required for GSE fitting. Please install it via 'pip install scipy'.")
            
        x_data = np.array(x_data)
        y_data = np.array(y_data)
        
        # --- Phase 1: Greedy Structural Build-up ---
        if verbose:
            print("--- Phase 1: Greedy Structural Build-up ---")
            
        # Initial linear fit (simple least squares for trend)
        self._fit_linear_trend(x_data, y_data)
        
        for i in range(max_components):
            # Calculate residual error
            y_pred = self.model.evaluate(x_data)
            residual = y_data - y_pred
            mse = np.mean(residual**2)
            
            if verbose:
                print(f"  Iter {i+1}: MSE = {mse:.6f}")
                
            if mse < epsilon:
                if verbose: print("  Converged.")
                break
                
            # Find point of maximum error
            max_err_idx = np.argmax(np.abs(residual))
            x_target = x_data[max_err_idx]
            err_val = residual[max_err_idx]
            
            # Add a "correction" sigmoid at this location
            # Heuristic: Sharp sigmoid (high k) to fix local error
            # Alpha is set to the error value to cancel it out immediately
            # n is set to an odd number (e.g., 3 or 5) for step-like correction
            self.model.add_sigmoid(alpha=err_val, n=3, k=10.0, x0=x_target)
            
        # Re-fit linear component after structural build-up
        y_pred_sigmoid = np.zeros_like(y_data)
        for comp in self.model.components:
            y_pred_sigmoid += comp['alpha'] * generalized_sigmoid(x_data, comp['n'], comp['k'], comp['x0'])
        
        residual_for_linear = y_data - y_pred_sigmoid
        self._fit_linear_trend(x_data, residual_for_linear)

        if verbose:
            print(f"--- Phase 1 Complete. Components: {len(self.model.components)} ---")

        # --- Phase 2: Global Fine-Tuning ---
        if verbose:
            print("--- Phase 2: Global Fine-Tuning ---")
            
        self._global_optimize(x_data, y_data)
        
        final_mse = np.mean((y_data - self.model.evaluate(x_data))**2)
        if verbose:
            print(f"--- Fitting Complete. Final MSE: {final_mse:.6f} ---")
            
        return self.model

    def _fit_linear_trend(self, x, y):
        """Fit linear component using least squares."""
        A = np.vstack([x, np.ones(len(x))]).T
        m, c = np.linalg.lstsq(A, y, rcond=None)[0]
        self.model.beta = m
        self.model.gamma = c

    def _global_optimize(self, x, y):
        """Optimize all parameters of the model simultaneously."""
        
        # Pack parameters into a single array
        # [beta, gamma, alpha1, n1, k1, x01, alpha2, n2, k2, x02, ...]
        params = [self.model.beta, self.model.gamma]
        for c in self.model.components:
            params.extend([c['alpha'], c['n'], c['k'], c['x0']])
            
        def objective(p):
            # Unpack and evaluate
            beta, gamma = p[0], p[1]
            y_est = beta * x + gamma
            
            idx = 2
            num_comps = len(self.model.components)
            for _ in range(num_comps):
                alpha, n, k, x0 = p[idx], p[idx+1], p[idx+2], p[idx+3]
                # Enforce constraints softly or via bounds if using minimize(bounds=...)
                # Here we just use the values
                y_est += alpha * generalized_sigmoid(x, n, k, x0)
                idx += 4
            
            return np.sum((y - y_est)**2)

        # Run optimization
        # L-BFGS-B is good for bound-constrained problems, but here we use BFGS for simplicity
        # or Nelder-Mead if gradients are tricky (though they are differentiable)
        res = minimize(objective, params, method='L-BFGS-B')
        
        if res.success:
            # Unpack optimized parameters back into model
            p = res.x
            self.model.beta = p[0]
            self.model.gamma = p[1]
            
            idx = 2
            for i in range(len(self.model.components)):
                self.model.components[i]['alpha'] = p[idx]
                self.model.components[i]['n'] = int(round(p[idx+1])) # n must be int
                self.model.components[i]['k'] = p[idx+2]
                self.model.components[i]['x0'] = p[idx+3]
                idx += 4
