/**
 * معادلة الشكل العام - General Shape Equation
 */

import { MotherEquation, ObjectType } from "../core/mother-equation";

export enum ShapeType {
  LINE = 'line',
  CIRCLE = 'circle',
  ELLIPSE = 'ellipse',
  RECTANGLE = 'rectangle',
  POLYGON = 'polygon',
  BEZIER = 'bezier',
  SINE_WAVE = 'sine_wave',
  EXPONENTIAL = 'exponential',
  PARAMETRIC = 'parametric',
  COMPOSITE = 'composite'
}

export enum FillType {
  NONE = 'none',
  SOLID = 'solid',
  GRADIENT_LINEAR = 'gradient_linear',
  GRADIENT_RADIAL = 'gradient_radial',
  PATTERN = 'pattern'
}

export enum LineStyle {
  SOLID = 'solid',
  DASHED = 'dashed',
  DOTTED = 'dotted',
  DASH_DOT = 'dash_dot'
}

export class Color {
  r: number;
  g: number;
  b: number;
  a: number;

  constructor(r: number = 0, g: number = 0, b: number = 0, a: number = 1.0) {
    this.r = Math.max(0, Math.min(255, r));
    this.g = Math.max(0, Math.min(255, g));
    this.b = Math.max(0, Math.min(255, b));
    this.a = Math.max(0, Math.min(1, a));
  }

  toHex(): string {
    const rHex = Math.floor(this.r).toString(16).padStart(2, '0');
    const gHex = Math.floor(this.g).toString(16).padStart(2, '0');
    const bHex = Math.floor(this.b).toString(16).padStart(2, '0');
    return \`#\${rHex}\${gHex}\${bHex}\`;
  }

  toRGBA(): string {
    return \`rgba(\${Math.floor(this.r)}, \${Math.floor(this.g)}, \${Math.floor(this.b)}, \${this.a})\`;
  }

  clone(): Color {
    return new Color(this.r, this.g, this.b, this.a);
  }
}

export class StyleProperties {
  strokeColor: Color;
  fillColor: Color;
  lineWidth: number;
  lineStyle: LineStyle;
  fillType: FillType;
  opacity: number;

  constructor() {
    this.strokeColor = new Color(0, 0, 0, 1);
    this.fillColor = new Color(255, 255, 255, 0);
    this.lineWidth = 1;
    this.lineStyle = LineStyle.SOLID;
    this.fillType = FillType.NONE;
    this.opacity = 1.0;
  }

  clone(): StyleProperties {
    const style = new StyleProperties();
    style.strokeColor = this.strokeColor.clone();
    style.fillColor = this.fillColor.clone();
    style.lineWidth = this.lineWidth;
    style.lineStyle = this.lineStyle;
    style.fillType = this.fillType;
    style.opacity = this.opacity;
    return style;
  }
}

export class MathematicalTerm {
  termType: string;
  coefficients: number[];
  parameters: Record<string, any>;
  style: StyleProperties;

  constructor(termType: string = "linear") {
    this.termType = termType;
    this.coefficients = [];
    this.parameters = {};
    this.style = new StyleProperties();
  }

  evaluate(x: number): number {
    switch (this.termType) {
      case "linear":
        return (this.coefficients[0] || 0) * x + (this.coefficients[1] || 0);
      case "quadratic":
        return (this.coefficients[0] || 0) * x * x + 
               (this.coefficients[1] || 0) * x + 
               (this.coefficients[2] || 0);
      case "sine":
        return (this.coefficients[0] || 1) * Math.sin((this.coefficients[1] || 1) * x + (this.coefficients[2] || 0));
      case "cosine":
        return (this.coefficients[0] || 1) * Math.cos((this.coefficients[1] || 1) * x + (this.coefficients[2] || 0));
      case "exponential":
        return (this.coefficients[0] || 1) * Math.exp((this.coefficients[1] || 1) * x);
      default:
        return 0;
    }
  }

  clone(): MathematicalTerm {
    const term = new MathematicalTerm(this.termType);
    term.coefficients = [...this.coefficients];
    term.parameters = { ...this.parameters };
    term.style = this.style.clone();
    return term;
  }
}

export class GeneralShapeEquation extends MotherEquation {
  shapeType: ShapeType;
  mathematicalTerms: MathematicalTerm[];
  style: StyleProperties;
  closed: boolean;
  parametric: boolean;

  constructor(name: string, shapeType: ShapeType = ShapeType.LINE) {
    super(ObjectType.MATHEMATICAL, name);
    this.shapeType = shapeType;
    this.mathematicalTerms = [];
    this.style = new StyleProperties();
    this.closed = false;
    this.parametric = false;
  }

  addTerm(term: MathematicalTerm): void {
    this.mathematicalTerms.push(term);
  }

  evaluateAt(x: number): number {
    let result = 0;
    for (const term of this.mathematicalTerms) {
      result += term.evaluate(x);
    }
    return result;
  }

  evaluateParametric(t: number): { x: number; y: number } {
    if (this.mathematicalTerms.length < 2) {
      return { x: 0, y: 0 };
    }
    return {
      x: this.mathematicalTerms[0].evaluate(t),
      y: this.mathematicalTerms[1].evaluate(t)
    };
  }

  getPoints(start: number, end: number, steps: number = 100): Array<{ x: number; y: number }> {
    const points: Array<{ x: number; y: number }> = [];
    const stepSize = (end - start) / steps;

    for (let i = 0; i <= steps; i++) {
      const t = start + i * stepSize;
      if (this.parametric) {
        points.push(this.evaluateParametric(t));
      } else {
        points.push({ x: t, y: this.evaluateAt(t) });
      }
    }

    return points;
  }

  clone(): GeneralShapeEquation {
    const shape = new GeneralShapeEquation(this.name, this.shapeType);
    shape.mathematicalTerms = this.mathematicalTerms.map(t => t.clone());
    shape.style = this.style.clone();
    shape.closed = this.closed;
    shape.parametric = this.parametric;
    return shape;
  }
}
