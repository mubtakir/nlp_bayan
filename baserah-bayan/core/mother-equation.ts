/**
 * ═══════════════════════════════════════════════════════════════════════
 * المعادلة الأم - Mother Equation
 * ═══════════════════════════════════════════════════════════════════════
 */

export enum ObjectType {
  PHYSICAL = 'physical',
  ABSTRACT = 'abstract',
  COMPOSITE = 'composite',
  DYNAMIC = 'dynamic',
  STATIC = 'static',
  LINGUISTIC = 'linguistic',
  MATHEMATICAL = 'mathematical'
}

export class StaticProperties {
  mass: number;
  density: number;
  material: string;
  color: string;
  texture: string;
  customProperties: Record<string, any>;

  constructor(
    mass: number = 1.0,
    density: number = 1.0,
    material: string = 'unknown',
    color: string = 'unknown',
    texture: string = 'smooth'
  ) {
    this.mass = mass;
    this.density = density;
    this.material = material;
    this.color = color;
    this.texture = texture;
    this.customProperties = {};
  }

  addCustomProperty(key: string, value: any): void {
    this.customProperties[key] = value;
  }

  getCustomProperty(key: string): any {
    return this.customProperties[key];
  }

  toJSON(): object {
    return {
      mass: this.mass,
      density: this.density,
      material: this.material,
      color: this.color,
      texture: this.texture,
      customProperties: this.customProperties
    };
  }
}

export class DynamicProperties {
  position: number[];
  velocity: number[];
  acceleration: number[];
  rotation: number[];
  energy: number;
  temperature: number;
  timestamp: Date;
  customDynamic: Record<string, any>;

  constructor() {
    this.position = [0.0, 0.0, 0.0];
    this.velocity = [0.0, 0.0, 0.0];
    this.acceleration = [0.0, 0.0, 0.0];
    this.rotation = [0.0, 0.0, 0.0];
    this.energy = 0.0;
    this.temperature = 20.0;
    this.timestamp = new Date();
    this.customDynamic = {};
  }

  updatePosition(newPosition: number[]): void {
    this.position = newPosition;
    this.timestamp = new Date();
  }

  updateVelocity(newVelocity: number[]): void {
    this.velocity = newVelocity;
    this.timestamp = new Date();
  }

  updateAcceleration(newAcceleration: number[]): void {
    this.acceleration = newAcceleration;
    this.timestamp = new Date();
  }

  updateEnergy(newEnergy: number): void {
    this.energy = newEnergy;
    this.timestamp = new Date();
  }

  updateTemperature(newTemperature: number): void {
    this.temperature = newTemperature;
    this.timestamp = new Date();
  }

  addCustomDynamic(key: string, value: any): void {
    this.customDynamic[key] = value;
  }

  toJSON(): object {
    return {
      position: this.position,
      velocity: this.velocity,
      acceleration: this.acceleration,
      rotation: this.rotation,
      energy: this.energy,
      temperature: this.temperature,
      timestamp: this.timestamp.toISOString(),
      customDynamic: this.customDynamic
    };
  }
}

interface SigmoidTerm {
  coefficient: number;
  exponent: { real: number; imaginary: number };
}

interface LinearTerm {
  slope: number;
  intercept: number;
}

export class ShapeFunction {
  shapeType: string;
  dimensions: Record<string, number>;
  volume: number;
  surfaceArea: number;
  sigmoidTerms: SigmoidTerm[];
  linearTerms: LinearTerm[];

  constructor(shapeType: string = 'sphere') {
    this.shapeType = shapeType;
    this.dimensions = {};
    this.volume = 0.0;
    this.surfaceArea = 0.0;
    this.sigmoidTerms = [];
    this.linearTerms = [];
  }

  calculateVolume(): number {
    if (this.shapeType === 'sphere') {
      const radius = this.dimensions['radius'] || 1.0;
      this.volume = (4.0 / 3.0) * Math.PI * Math.pow(radius, 3);
    } else if (this.shapeType === 'cube') {
      const side = this.dimensions['side'] || 1.0;
      this.volume = Math.pow(side, 3);
    } else if (this.shapeType === 'cylinder') {
      const radius = this.dimensions['radius'] || 1.0;
      const height = this.dimensions['height'] || 1.0;
      this.volume = Math.PI * Math.pow(radius, 2) * height;
    }
    return this.volume;
  }

  calculateSurfaceArea(): number {
    if (this.shapeType === 'sphere') {
      const radius = this.dimensions['radius'] || 1.0;
      this.surfaceArea = 4.0 * Math.PI * Math.pow(radius, 2);
    } else if (this.shapeType === 'cube') {
      const side = this.dimensions['side'] || 1.0;
      this.surfaceArea = 6.0 * Math.pow(side, 2);
    } else if (this.shapeType === 'cylinder') {
      const radius = this.dimensions['radius'] || 1.0;
      const height = this.dimensions['height'] || 1.0;
      this.surfaceArea = 2.0 * Math.PI * radius * (radius + height);
    }
    return this.surfaceArea;
  }

  addSigmoidTerm(coefficient: number, exponent: { real: number; imaginary: number }): void {
    this.sigmoidTerms.push({ coefficient, exponent });
  }

  addLinearTerm(slope: number, intercept: number): void {
    this.linearTerms.push({ slope, intercept });
  }

  toJSON(): object {
    return {
      shapeType: this.shapeType,
      dimensions: this.dimensions,
      volume: this.volume,
      surfaceArea: this.surfaceArea,
      sigmoidTerms: this.sigmoidTerms,
      linearTerms: this.linearTerms
    };
  }
}

interface StateRecord {
  timestamp: string;
  position: number[];
  velocity: number[];
  energy: number;
  temperature: number;
}

export class MotherEquation {
  id: string;
  phi: StaticProperties;
  psi: DynamicProperties;
  gamma: ShapeFunction;
  objectType: ObjectType;
  name: string;
  creationTime: Date;
  history: StateRecord[];

  constructor(objectType: ObjectType, name: string, id?: string) {
    this.id = id || this.generateUUID();
    this.objectType = objectType;
    this.name = name;
    this.phi = new StaticProperties();
    this.psi = new DynamicProperties();
    this.gamma = new ShapeFunction();
    this.creationTime = new Date();
    this.history = [];
  }

  private generateUUID(): string {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
      const r = Math.random() * 16 | 0;
      const v = c === 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  }

  recordState(): void {
    const state: StateRecord = {
      timestamp: new Date().toISOString(),
      position: this.psi.position,
      velocity: this.psi.velocity,
      energy: this.psi.energy,
      temperature: this.psi.temperature
    };
    this.history.push(state);
  }

  getState(): object {
    return {
      id: this.id,
      name: this.name,
      objectType: this.objectType,
      phi: this.phi.toJSON(),
      psi: this.psi.toJSON(),
      gamma: this.gamma.toJSON(),
      creationTime: this.creationTime.toISOString(),
      historyLength: this.history.length
    };
  }

  getHistory(limit?: number): StateRecord[] {
    if (limit && limit > 0) {
      return this.history.slice(-limit);
    }
    return this.history;
  }

  toJSON(): string {
    return JSON.stringify(this.getState(), null, 2);
  }

  toString(): string {
    return `MotherEquation(id=${this.id}, name=${this.name}, type=${this.objectType})`;
  }
}
