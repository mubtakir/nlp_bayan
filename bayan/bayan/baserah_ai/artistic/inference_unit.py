"""
وحدة الاستنباط - Inference Unit
================================

تحويل الأشكال المرئية إلى معادلات رياضية.
شكل → معادلة

المؤلف: باسل يحيى عبدالله
"""

import numpy as np
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass, field
from scipy.optimize import curve_fit


@dataclass
class InferenceResult:
    """نتيجة الاستنباط"""
    # معاملات السيغمويد المستنبطة
    alpha: List[float] = field(default_factory=list)
    k: List[float] = field(default_factory=list)
    x0: List[float] = field(default_factory=list)
    n: List[int] = field(default_factory=list)
    
    # المعاملات الخطية
    beta: float = 0.0
    gamma: float = 0.0
    
    # جودة الاستنباط
    confidence: float = 0.0
    mse: float = float('inf')
    shape_type: str = "غير_معروف"
    
    # الميزات المستخرجة
    features: Dict[str, float] = field(default_factory=dict)
    
    def get_equation(self) -> str:
        """الحصول على معادلة النص"""
        parts = []
        for i in range(len(self.alpha)):
            parts.append(f"{self.alpha[i]:.2f}·σ_{self.n[i]}(x; {self.k[i]:.2f}, {self.x0[i]:.2f})")
        eq = " + ".join(parts) if parts else "0"
        if self.beta != 0:
            eq += f" + {self.beta:.2f}x"
        if self.gamma != 0:
            eq += f" + {self.gamma:.2f}"
        return f"f(x) = {eq}"


class InferenceUnit:
    """
    وحدة الاستنباط - تحويل الأشكال إلى معادلات
    
    تستخدم:
    - تحليل الميزات (الانحناء، التماثل، الدورية)
    - مطابقة المنحنيات
    - النظريات الثورية للتحسين
    """
    
    def __init__(self):
        self.known_patterns = {
            'دائرة': {'symmetry': 0.9, 'complexity': 0.1, 'periodicity': 0.8},
            'قلب': {'symmetry': 0.7, 'complexity': 0.5, 'periodicity': 0.3},
            'وردة': {'symmetry': 0.95, 'complexity': 0.6, 'periodicity': 0.9},
            'حلزون': {'symmetry': 0.2, 'complexity': 0.8, 'periodicity': 0.6},
            'موجة': {'symmetry': 0.5, 'complexity': 0.3, 'periodicity': 0.95}
        }
    
    def infer_from_points(self, x: np.ndarray, y: np.ndarray) -> InferenceResult:
        """
        استنباط المعادلة من نقاط الشكل
        """
        x = np.asarray(x, dtype=float)
        y = np.asarray(y, dtype=float)
        
        # استخراج الميزات
        features = self._extract_features(x, y)
        
        # تحديد نوع الشكل
        shape_type = self._classify_shape(features)
        
        # مطابقة المنحنى
        params = self._fit_curve(x, y)
        
        # حساب جودة المطابقة
        y_pred = self._evaluate(x, params)
        mse = np.mean((y - y_pred) ** 2)
        confidence = 1.0 / (1.0 + mse)
        
        return InferenceResult(
            alpha=params.get('alpha', [1.0]),
            k=params.get('k', [1.0]),
            x0=params.get('x0', [0.0]),
            n=params.get('n', [1]),
            beta=params.get('beta', 0.0),
            gamma=params.get('gamma', 0.0),
            confidence=confidence,
            mse=mse,
            shape_type=shape_type,
            features=features
        )
    
    def _extract_features(self, x: np.ndarray, y: np.ndarray) -> Dict[str, float]:
        """استخراج الميزات من البيانات"""
        features = {}
        
        # التماثل
        if len(y) > 1:
            y_rev = y[::-1]
            features['symmetry'] = 1.0 - np.mean(np.abs(y - y_rev)) / (np.ptp(y) + 1e-10)
        else:
            features['symmetry'] = 0.5
        
        # الدورية (باستخدام FFT)
        if len(y) > 10:
            fft = np.fft.fft(y)
            power = np.abs(fft[1:len(fft)//2]) ** 2
            if len(power) > 0 and np.sum(power) > 0:
                features['periodicity'] = np.max(power) / np.sum(power)
            else:
                features['periodicity'] = 0.0
        else:
            features['periodicity'] = 0.0
        
        # التعقيد (عدد نقاط الانعطاف)
        if len(y) > 2:
            dy = np.diff(y)
            sign_changes = np.sum(np.diff(np.sign(dy)) != 0)
            features['complexity'] = sign_changes / len(y)
        else:
            features['complexity'] = 0.0
        
        # التباين
        features['variance'] = np.var(y)
        
        return features
    
    def _classify_shape(self, features: Dict[str, float]) -> str:
        """تصنيف الشكل بناءً على الميزات"""
        best_match = "غير_معروف"
        best_score = 0.0
        
        for shape_name, pattern in self.known_patterns.items():
            score = 0.0
            for feat_name, pattern_value in pattern.items():
                if feat_name in features:
                    score += 1.0 - abs(features[feat_name] - pattern_value)
            score /= len(pattern)
            
            if score > best_score:
                best_score = score
                best_match = shape_name
        
        return best_match
    
    def _fit_curve(self, x: np.ndarray, y: np.ndarray) -> Dict[str, Any]:
        """مطابقة منحنى سيغمويد"""
        try:
            def sigmoid(x, alpha, k, x0):
                return alpha / (1 + np.exp(-k * (x - x0)))
            
            popt, _ = curve_fit(sigmoid, x, y, p0=[1, 1, 0], maxfev=1000)
            return {'alpha': [popt[0]], 'k': [popt[1]], 'x0': [popt[2]], 'n': [1]}
        except:
            return {'alpha': [1.0], 'k': [1.0], 'x0': [0.0], 'n': [1]}
    
    def _evaluate(self, x: np.ndarray, params: Dict) -> np.ndarray:
        """تقييم المعادلة"""
        y = np.zeros_like(x)
        for i in range(len(params.get('alpha', []))):
            alpha = params['alpha'][i]
            k = params['k'][i]
            x0 = params['x0'][i]
            y += alpha / (1 + np.exp(-k * (x - x0)))
        return y + params.get('beta', 0) * x + params.get('gamma', 0)

