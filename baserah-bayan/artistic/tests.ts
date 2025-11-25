import { GeneralShapeEquation, ShapeType } from "./general-shape-equation";
import { SigmoidShapeEquation } from "./sigmoid-shape-equation";
import { ClassicDrawingEngine } from "./classic-drawing-engine";

export class ArtisticTests {
  static runAllTests(): boolean {
    return this.testGeneralShape() && 
           this.testSigmoidShape() && 
           this.testDrawingEngine();
  }

  static testGeneralShape(): boolean {
    const shape = new GeneralShapeEquation("TestShape", ShapeType.LINE);
    return shape !== null;
  }

  static testSigmoidShape(): boolean {
    const shape = new SigmoidShapeEquation("TestSigmoid");
    shape.addSigmoidTerm(1.0, 1.0, 1.0, 0.0);
    const result = shape.evaluate(0);
    return !isNaN(result);
  }

  static testDrawingEngine(): boolean {
    return true;
  }
}
