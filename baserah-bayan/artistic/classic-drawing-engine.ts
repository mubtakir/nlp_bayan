/**
 * محرك الرسم التقليدي - Classic Drawing Engine
 */

import { 
  GeneralShapeEquation, 
  ShapeType, 
  FillType, 
  LineStyle,
  Color,
  StyleProperties,
  MathematicalTerm
} from "./general-shape-equation";

export class Point2D {
  x: number;
  y: number;

  constructor(x: number = 0, y: number = 0) {
    this.x = x;
    this.y = y;
  }
}

export class CanvasContext {
  canvasId: string;
  width: number;
  height: number;
  context: any;

  constructor(canvasId: string, width: number = 800, height: number = 600) {
    this.canvasId = canvasId;
    this.width = width;
    this.height = height;
    this.context = null;
  }

  initialize(): boolean {
    try {
      if (typeof document !== 'undefined') {
        const canvas = document.getElementById(this.canvasId) as HTMLCanvasElement;
        if (canvas) {
          this.context = canvas.getContext('2d');
          canvas.width = this.width;
          canvas.height = this.height;
          return true;
        }
      }
      return false;
    } catch (e) {
      return false;
    }
  }

  clear(): void {
    if (this.context) {
      this.context.clearRect(0, 0, this.width, this.height);
    }
  }

  setBackground(color: Color): void {
    if (this.context) {
      this.context.fillStyle = color.toRGBA();
      this.context.fillRect(0, 0, this.width, this.height);
    }
  }
}

export class ClassicDrawingEngine {
  canvas: CanvasContext;
  originX: number;
  originY: number;
  scaleX: number;
  scaleY: number;

  constructor(canvasId: string, width: number = 800, height: number = 600) {
    this.canvas = new CanvasContext(canvasId, width, height);
    this.originX = width / 2;
    this.originY = height / 2;
    this.scaleX = 1;
    this.scaleY = -1;
  }

  initialize(): boolean {
    return this.canvas.initialize();
  }

  clear(): void {
    this.canvas.clear();
  }

  setBackground(color: Color): void {
    this.canvas.setBackground(color);
  }

  setOrigin(x: number, y: number): void {
    this.originX = x;
    this.originY = y;
  }

  setScale(scaleX: number, scaleY: number): void {
    this.scaleX = scaleX;
    this.scaleY = scaleY;
  }

  transformPoint(p: Point2D): Point2D {
    return new Point2D(
      this.originX + p.x * this.scaleX,
      this.originY + p.y * this.scaleY
    );
  }

  applyStyle(style: StyleProperties): void {
    if (!this.canvas.context) return;

    const ctx = this.canvas.context;
    ctx.strokeStyle = style.strokeColor.toRGBA();
    ctx.fillStyle = style.fillColor.toRGBA();
    ctx.lineWidth = style.lineWidth;
    ctx.globalAlpha = style.opacity;

    switch (style.lineStyle) {
      case LineStyle.DASHED:
        ctx.setLineDash([10, 5]);
        break;
      case LineStyle.DOTTED:
        ctx.setLineDash([2, 3]);
        break;
      case LineStyle.DASH_DOT:
        ctx.setLineDash([10, 5, 2, 5]);
        break;
      default:
        ctx.setLineDash([]);
    }
  }

  drawShape(shape: GeneralShapeEquation, start: number = -10, end: number = 10, steps: number = 100): void {
    if (!this.canvas.context) return;

    const ctx = this.canvas.context;
    this.applyStyle(shape.style);

    const points = shape.getPoints(start, end, steps);
    if (points.length === 0) return;

    ctx.beginPath();
    const firstPoint = this.transformPoint(new Point2D(points[0].x, points[0].y));
    ctx.moveTo(firstPoint.x, firstPoint.y);

    for (let i = 1; i < points.length; i++) {
      const p = this.transformPoint(new Point2D(points[i].x, points[i].y));
      ctx.lineTo(p.x, p.y);
    }

    if (shape.closed) {
      ctx.closePath();
    }

    ctx.stroke();

    if (shape.style.fillType !== FillType.NONE && shape.closed) {
      ctx.fill();
    }
  }

  drawLine(x1: number, y1: number, x2: number, y2: number, color: Color, lineWidth: number = 1): void {
    if (!this.canvas.context) return;

    const ctx = this.canvas.context;
    const p1 = this.transformPoint(new Point2D(x1, y1));
    const p2 = this.transformPoint(new Point2D(x2, y2));

    ctx.strokeStyle = color.toRGBA();
    ctx.lineWidth = lineWidth;
    ctx.beginPath();
    ctx.moveTo(p1.x, p1.y);
    ctx.lineTo(p2.x, p2.y);
    ctx.stroke();
  }

  drawCircle(cx: number, cy: number, radius: number, strokeColor: Color, fillColor?: Color, lineWidth: number = 1): void {
    if (!this.canvas.context) return;

    const ctx = this.canvas.context;
    const center = this.transformPoint(new Point2D(cx, cy));

    ctx.strokeStyle = strokeColor.toRGBA();
    ctx.lineWidth = lineWidth;
    ctx.beginPath();
    ctx.arc(center.x, center.y, radius * Math.abs(this.scaleX), 0, 2 * Math.PI);
    ctx.stroke();

    if (fillColor) {
      ctx.fillStyle = fillColor.toRGBA();
      ctx.fill();
    }
  }

  drawAxes(color: Color = new Color(128, 128, 128), lineWidth: number = 1): void {
    this.drawLine(-this.canvas.width, 0, this.canvas.width, 0, color, lineWidth);
    this.drawLine(0, -this.canvas.height, 0, this.canvas.height, color, lineWidth);
  }

  drawGrid(spacing: number = 1, color: Color = new Color(200, 200, 200), lineWidth: number = 0.5): void {
    const maxX = this.canvas.width / (2 * Math.abs(this.scaleX));
    const maxY = this.canvas.height / (2 * Math.abs(this.scaleY));

    for (let x = -maxX; x <= maxX; x += spacing) {
      this.drawLine(x, -maxY, x, maxY, color, lineWidth);
    }

    for (let y = -maxY; y <= maxY; y += spacing) {
      this.drawLine(-maxX, y, maxX, y, color, lineWidth);
    }
  }

  saveImage(): string | null {
    if (!this.canvas.context) return null;
    const canvas = document.getElementById(this.canvas.canvasId) as HTMLCanvasElement;
    return canvas ? canvas.toDataURL('image/png') : null;
  }
}
