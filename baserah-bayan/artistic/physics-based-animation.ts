import { GeneralShapeEquation } from "./general-shape-equation";

export interface PhysicsProperties {
  mass: number;
  velocity: {x: number; y: number};
  acceleration: {x: number; y: number};
  friction: number;
  gravity: number;
}

export class PhysicsBasedAnimation {
  shapes: Map<string, {shape: GeneralShapeEquation; physics: PhysicsProperties}>;
  time: number;
  deltaTime: number;

  constructor() {
    this.shapes = new Map();
    this.time = 0;
    this.deltaTime = 1/60;
  }

  addShape(id: string, shape: GeneralShapeEquation, physics: PhysicsProperties): void {
    this.shapes.set(id, {shape, physics});
  }

  update(): void {
    this.time += this.deltaTime;
    
    for (const [id, data] of this.shapes) {
      data.physics.velocity.y += data.physics.gravity * this.deltaTime;
      data.physics.velocity.x *= (1 - data.physics.friction);
      data.physics.velocity.y *= (1 - data.physics.friction);
    }
  }

  getShapePosition(id: string): {x: number; y: number} | null {
    const data = this.shapes.get(id);
    return data ? {x: 0, y: 0} : null;
  }
}
