/**
 * محرك الرسم بالسيغمويد - Sigmoid Drawing Engine
 */

import { SigmoidShapeEquation } from "./sigmoid-shape-equation";

export class SigmoidCanvasContext {
  canvas: HTMLCanvasElement | null;
  ctx: CanvasRenderingContext2D | null;
  width: number;
  height: number;
  scaleX: number;
  scaleY: number;
  offsetX: number;
  offsetY: number;

  constructor(canvasId: string, width: number = 800, height: number = 600) {
    this.canvas = document.getElementById(canvasId) as HTMLCanvasElement;
    this.ctx = this.canvas ? this.canvas.getContext('2d') : null;
    this.width = width;
    this.height = height;
    this.scaleX = 50;
    this.scaleY = 50;
    this.offsetX = width / 2;
    this.offsetY = height / 2;
  }

  setScale(scaleX: number, scaleY: number): void {
    this.scaleX = scaleX;
    this.scaleY = scaleY;
  }

  setOffset(offsetX: number, offsetY: number): void {
    this.offsetX = offsetX;
    this.offsetY = offsetY;
  }

  toCanvasX(x: number): number {
    return this.offsetX + x * this.scaleX;
  }

  toCanvasY(y: number): number {
    return this.offsetY - y * this.scaleY;
  }

  clear(): void {
    if (this.ctx) {
      this.ctx.clearRect(0, 0, this.width, this.height);
    }
  }
}

export class SigmoidDrawingEngine {
  canvasContext: SigmoidCanvasContext | null;
  currentEquation: SigmoidShapeEquation | null;
  drawingRange: [number, number];
  resolution: number;
  stats: Record<string, any>;

  constructor() {
    this.canvasContext = null;
    this.currentEquation = null;
    this.drawingRange = [-10, 10];
    this.resolution = 500;
    this.stats = {
      shapesDrawn: 0,
      pointsCalculated: 0,
      renderTime: 0
    };
  }

  initialize(canvasId: string, width: number = 800, height: number = 600): boolean {
    try {
      this.canvasContext = new SigmoidCanvasContext(canvasId, width, height);
      return this.canvasContext.ctx !== null;
    } catch (e) {
      return false;
    }
  }

  setEquation(equation: SigmoidShapeEquation): void {
    this.currentEquation = equation;
  }

  setRange(start: number, end: number): void {
    this.drawingRange = [start, end];
  }

  setResolution(resolution: number): void {
    this.resolution = Math.max(10, Math.min(10000, resolution));
  }

  draw(): void {
    if (!this.canvasContext || !this.canvasContext.ctx || !this.currentEquation) {
      return;
    }

    const startTime = performance.now();
    const ctx = this.canvasContext.ctx;
    const [start, end] = this.drawingRange;
    const step = (end - start) / this.resolution;

    ctx.beginPath();
    let firstPoint = true;

    for (let i = 0; i <= this.resolution; i++) {
      const x = start + i * step;
      const y = this.currentEquation.evaluate(x);
      const canvasX = this.canvasContext.toCanvasX(x);
      const canvasY = this.canvasContext.toCanvasY(y);

      if (firstPoint) {
        ctx.moveTo(canvasX, canvasY);
        firstPoint = false;
      } else {
        ctx.lineTo(canvasX, canvasY);
      }
    }

    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 2;
    ctx.stroke();

    this.stats.shapesDrawn++;
    this.stats.pointsCalculated += this.resolution + 1;
    this.stats.renderTime = performance.now() - startTime;
  }

  drawAxes(): void {
    if (!this.canvasContext || !this.canvasContext.ctx) return;

    const ctx = this.canvasContext.ctx;
    ctx.strokeStyle = '#cccccc';
    ctx.lineWidth = 1;

    ctx.beginPath();
    ctx.moveTo(0, this.canvasContext.offsetY);
    ctx.lineTo(this.canvasContext.width, this.canvasContext.offsetY);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(this.canvasContext.offsetX, 0);
    ctx.lineTo(this.canvasContext.offsetX, this.canvasContext.height);
    ctx.stroke();
  }

  clear(): void {
    if (this.canvasContext) {
      this.canvasContext.clear();
    }
  }

  getStats(): Record<string, any> {
    return { ...this.stats };
  }
}
