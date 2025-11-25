import { SigmoidShapeEquation, GeneralizedSigmoid, LinearComponent } from "./sigmoid-shape-equation";

export class SigmoidInferenceEngine {
  maxIterations: number;
  learningRate: number;
  tolerance: number;

  constructor() {
    this.maxIterations = 1000;
    this.learningRate = 0.01;
    this.tolerance = 0.001;
  }

  inferFromPoints(points: Array<{x: number; y: number}>, numTerms: number = 3): SigmoidShapeEquation {
    const equation = new SigmoidShapeEquation("InferredCurve");
    
    for (let i = 0; i < numTerms; i++) {
      const weight = Math.random() * 2 - 1;
      const scale = 1.0;
      const sharpness = 1.0;
      const midpoint = points[Math.floor(points.length / 2)].x;
      equation.addSigmoidTerm(weight, scale, sharpness, midpoint);
    }

    return equation;
  }

  calculateError(equation: SigmoidShapeEquation, points: Array<{x: number; y: number}>): number {
    let totalError = 0;
    for (const point of points) {
      const predicted = equation.evaluate(point.x);
      const error = predicted - point.y;
      totalError += error * error;
    }
    return totalError / points.length;
  }
}
