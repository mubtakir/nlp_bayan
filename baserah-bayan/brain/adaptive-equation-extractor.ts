/**
 * مستخرج المعادلات التكيفية - Adaptive Equation Extractor
 */

import { AdaptiveRevolutionaryEquation, AdaptationType } from "./adaptive-equations-core";

export enum EquationType {
  SIGMOID = 'sigmoid',
  LINEAR = 'linear',
  POLYNOMIAL = 'polynomial',
  EXPONENTIAL = 'exponential',
  COMPOSITE = 'composite'
}

export class SigmoidParameters {
  alpha: number;
  k: number;
  x0: number;
  n: number;

  constructor(alpha: number = 1, k: number = 1, x0: number = 0, n: number = 1) {
    this.alpha = alpha;
    this.k = k;
    this.x0 = x0;
    this.n = n;
  }
}

export class LinearParameters {
  beta: number;
  gamma: number;

  constructor(beta: number = 0, gamma: number = 0) {
    this.beta = beta;
    this.gamma = gamma;
  }
}

export class ExtractedEquation {
  equationType: EquationType;
  sigmoidParams: SigmoidParameters[];
  linearParams: LinearParameters;
  accuracy: number;

  constructor(type: EquationType = EquationType.COMPOSITE) {
    this.equationType = type;
    this.sigmoidParams = [];
    this.linearParams = new LinearParameters();
    this.accuracy = 0;
  }
}

export class AdaptiveEquationExtractor {
  maxIterations: number;
  tolerance: number;
  learningRate: number;

  constructor() {
    this.maxIterations = 1000;
    this.tolerance = 0.001;
    this.learningRate = 0.01;
  }

  extractFromData(dataPoints: Array<{x: number; y: number}>): ExtractedEquation {
    const equation = new ExtractedEquation(EquationType.COMPOSITE);
    
    const numSigmoids = Math.min(5, Math.floor(dataPoints.length / 10));
    for (let i = 0; i < numSigmoids; i++) {
      const param = new SigmoidParameters(
        Math.random() * 2 - 1,
        Math.random() * 2,
        dataPoints[Math.floor(dataPoints.length * i / numSigmoids)].x,
        1
      );
      equation.sigmoidParams.push(param);
    }

    equation.linearParams = new LinearParameters(0, 0);
    equation.accuracy = this.calculateAccuracy(equation, dataPoints);

    return equation;
  }

  private calculateAccuracy(equation: ExtractedEquation, dataPoints: Array<{x: number; y: number}>): number {
    let totalError = 0;
    for (const point of dataPoints) {
      const predicted = this.evaluateEquation(equation, point.x);
      const error = predicted - point.y;
      totalError += error * error;
    }
    return 1 / (1 + totalError / dataPoints.length);
  }

  private evaluateEquation(equation: ExtractedEquation, x: number): number {
    let result = equation.linearParams.beta * x + equation.linearParams.gamma;
    
    for (const param of equation.sigmoidParams) {
      const sigmoid = param.alpha / Math.pow(1 + Math.exp(-param.k * (x - param.x0)), param.n);
      result += sigmoid;
    }

    return result;
  }

  optimizeEquation(equation: ExtractedEquation, dataPoints: Array<{x: number; y: number}>): ExtractedEquation {
    for (let iter = 0; iter < this.maxIterations; iter++) {
      const currentAccuracy = this.calculateAccuracy(equation, dataPoints);
      if (currentAccuracy > 1 - this.tolerance) {
        break;
      }
    }
    return equation;
  }
}
