/**
 * معادلة الشكل بالسيغمويد - Sigmoid Shape Equation
 */

import { MotherEquation, ObjectType } from "../core/mother-equation";

export class ComplexExponent {
  real: number;
  imag: number;

  constructor(real: number = 1.0, imag: number = 0.0) {
    this.real = real;
    this.imag = imag;
  }

  magnitude(): number {
    return Math.sqrt(this.real * this.real + this.imag * this.imag);
  }

  phase(): number {
    return Math.atan2(this.imag, this.real);
  }

  toComplex(): { real: number; imag: number } {
    return { real: this.real, imag: this.imag };
  }
}

export class GeneralizedSigmoid {
  exponent: ComplexExponent;
  scale: number;
  sharpness: number;
  midpoint: number;

  constructor(scale: number = 1.0, sharpness: number = 1.0, midpoint: number = 0.0, exponent: ComplexExponent = new ComplexExponent(1.0, 0.0)) {
    this.exponent = exponent;
    this.scale = scale;
    this.sharpness = sharpness;
    this.midpoint = midpoint;
  }

  evaluate(x: number): number {
    try {
      const n = this.exponent.magnitude();
      const denominator = 1 + Math.pow(Math.abs(Math.exp(-this.sharpness * (x - this.midpoint))), n);
      return this.scale / denominator;
    } catch (e) {
      return this.scale * 0.5;
    }
  }

  derivative(x: number): number {
    const h = 0.0001;
    return (this.evaluate(x + h) - this.evaluate(x - h)) / (2 * h);
  }
}

export class LinearComponent {
  slope: number;
  intercept: number;

  constructor(slope: number = 0.0, intercept: number = 0.0) {
    this.slope = slope;
    this.intercept = intercept;
  }

  evaluate(x: number): number {
    return this.slope * x + this.intercept;
  }

  derivative(): number {
    return this.slope;
  }
}

export class SigmoidTerm {
  sigmoid: GeneralizedSigmoid;
  weight: number;

  constructor(weight: number = 1.0, scale: number = 1.0, sharpness: number = 1.0, midpoint: number = 0.0) {
    this.sigmoid = new GeneralizedSigmoid(scale, sharpness, midpoint);
    this.weight = weight;
  }

  evaluate(x: number): number {
    return this.weight * this.sigmoid.evaluate(x);
  }
}

export class SigmoidShapeEquation extends MotherEquation {
  sigmoidTerms: SigmoidTerm[];
  linearComponent: LinearComponent;
  name: string;

  constructor(name: string = "SigmoidShape") {
    super(ObjectType.MATHEMATICAL, name);
    this.name = name;
    this.sigmoidTerms = [];
    this.linearComponent = new LinearComponent();
  }

  addSigmoidTerm(weight: number, scale: number, sharpness: number, midpoint: number, exponent?: ComplexExponent): void {
    const term = new SigmoidTerm(weight, scale, sharpness, midpoint);
    if (exponent) {
      term.sigmoid.exponent = exponent;
    }
    this.sigmoidTerms.push(term);
  }

  setLinearComponent(slope: number, intercept: number): void {
    this.linearComponent = new LinearComponent(slope, intercept);
  }

  evaluate(x: number): number {
    let result = this.linearComponent.evaluate(x);
    for (const term of this.sigmoidTerms) {
      result += term.evaluate(x);
    }
    return result;
  }

  derivative(x: number): number {
    const h = 0.0001;
    return (this.evaluate(x + h) - this.evaluate(x - h)) / (2 * h);
  }

  getPoints(start: number, end: number, steps: number = 100): Array<{ x: number; y: number }> {
    const points: Array<{ x: number; y: number }> = [];
    const stepSize = (end - start) / steps;

    for (let i = 0; i <= steps; i++) {
      const x = start + i * stepSize;
      points.push({ x, y: this.evaluate(x) });
    }

    return points;
  }

  clone(): SigmoidShapeEquation {
    const shape = new SigmoidShapeEquation(this.name);
    shape.sigmoidTerms = this.sigmoidTerms.map(t => {
      const newTerm = new SigmoidTerm(t.weight, t.sigmoid.scale, t.sigmoid.sharpness, t.sigmoid.midpoint);
      newTerm.sigmoid.exponent = new ComplexExponent(t.sigmoid.exponent.real, t.sigmoid.exponent.imag);
      return newTerm;
    });
    shape.linearComponent = new LinearComponent(this.linearComponent.slope, this.linearComponent.intercept);
    return shape;
  }

  toJSON(): object {
    return {
      ...super.toJSON(),
      name: this.name,
      sigmoidTerms: this.sigmoidTerms.map(t => ({
        weight: t.weight,
        scale: t.sigmoid.scale,
        sharpness: t.sigmoid.sharpness,
        midpoint: t.sigmoid.midpoint,
        exponent: t.sigmoid.exponent.toComplex()
      })),
      linearComponent: {
        slope: this.linearComponent.slope,
        intercept: this.linearComponent.intercept
      }
    };
  }
}
