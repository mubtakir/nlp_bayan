import { SigmoidInferenceEngine } from "./sigmoid-inference-engine";

export class InferenceExamples {
  static inferSineWave(): void {
    const points: Array<{x: number; y: number}> = [];
    for (let x = -5; x <= 5; x += 0.5) {
      points.push({x, y: Math.sin(x)});
    }
    
    const engine = new SigmoidInferenceEngine();
    const equation = engine.inferFromPoints(points, 5);
  }
}
