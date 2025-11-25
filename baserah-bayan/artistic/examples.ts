import { GeneralShapeEquation, ShapeType, Color, StyleProperties, MathematicalTerm } from "./general-shape-equation";

export class ArtisticExamples {
  static createCircle(radius: number = 5): GeneralShapeEquation {
    const circle = new GeneralShapeEquation("Circle", ShapeType.CIRCLE);
    const xTerm = new MathematicalTerm("sine");
    xTerm.coefficients = [radius, 1, 0];
    const yTerm = new MathematicalTerm("cosine");
    yTerm.coefficients = [radius, 1, 0];
    circle.addTerm(xTerm);
    circle.addTerm(yTerm);
    circle.setParametric(true);
    circle.setClosed(true);
    return circle;
  }

  static createSineWave(amplitude: number = 1, frequency: number = 1): GeneralShapeEquation {
    const wave = new GeneralShapeEquation("SineWave", ShapeType.SINE_WAVE);
    const term = new MathematicalTerm("sine");
    term.coefficients = [amplitude, frequency, 0];
    wave.addTerm(term);
    return wave;
  }
}
