import { SigmoidShapeEquation, ComplexExponent } from "./sigmoid-shape-equation";

export class SigmoidExamples {
  static createSmoothStep(): SigmoidShapeEquation {
    const shape = new SigmoidShapeEquation("SmoothStep");
    shape.addSigmoidTerm(1.0, 1.0, 5.0, 0.0);
    return shape;
  }

  static createBump(): SigmoidShapeEquation {
    const shape = new SigmoidShapeEquation("Bump");
    shape.addSigmoidTerm(1.0, 1.0, 5.0, -1.0);
    shape.addSigmoidTerm(-1.0, 1.0, 5.0, 1.0);
    return shape;
  }

  static createWave(): SigmoidShapeEquation {
    const shape = new SigmoidShapeEquation("Wave");
    for (let i = -5; i <= 5; i += 2) {
      shape.addSigmoidTerm(0.5, 1.0, 3.0, i);
    }
    return shape;
  }
}
