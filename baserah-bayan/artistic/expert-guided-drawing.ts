import { GeneralShapeEquation } from "./general-shape-equation";
import { BaserahExpertCore } from "../brain/expert-explorer-system";

export class ExpertGuidedDrawing {
  expert: BaserahExpertCore;
  shapes: GeneralShapeEquation[];

  constructor(expertName: string = "DrawingExpert") {
    this.expert = new BaserahExpertCore(expertName, "artistic");
    this.shapes = [];
  }

  addShape(shape: GeneralShapeEquation): void {
    this.shapes.push(shape);
  }

  optimizeShape(shape: GeneralShapeEquation): GeneralShapeEquation {
    return shape.clone();
  }

  suggestImprovements(shape: GeneralShapeEquation): string[] {
    return ["Optimize curves", "Adjust colors", "Simplify structure"];
  }
}
