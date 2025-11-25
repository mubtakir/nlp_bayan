import { GeneralShapeEquation } from "./general-shape-equation";

export interface Keyframe {
  time: number;
  position: {x: number; y: number};
  rotation: number;
  scale: {x: number; y: number};
}

export class CharacterAnimation {
  character: GeneralShapeEquation;
  keyframes: Keyframe[];
  currentTime: number;
  duration: number;

  constructor(character: GeneralShapeEquation) {
    this.character = character;
    this.keyframes = [];
    this.currentTime = 0;
    this.duration = 0;
  }

  addKeyframe(keyframe: Keyframe): void {
    this.keyframes.push(keyframe);
    this.keyframes.sort((a, b) => a.time - b.time);
    if (keyframe.time > this.duration) {
      this.duration = keyframe.time;
    }
  }

  interpolate(t: number): {position: {x: number; y: number}; rotation: number; scale: {x: number; y: number}} {
    if (this.keyframes.length === 0) {
      return {position: {x: 0, y: 0}, rotation: 0, scale: {x: 1, y: 1}};
    }

    if (this.keyframes.length === 1) {
      return {
        position: this.keyframes[0].position,
        rotation: this.keyframes[0].rotation,
        scale: this.keyframes[0].scale
      };
    }

    let k1 = this.keyframes[0];
    let k2 = this.keyframes[1];

    for (let i = 0; i < this.keyframes.length - 1; i++) {
      if (t >= this.keyframes[i].time && t <= this.keyframes[i + 1].time) {
        k1 = this.keyframes[i];
        k2 = this.keyframes[i + 1];
        break;
      }
    }

    const alpha = (t - k1.time) / (k2.time - k1.time);

    return {
      position: {
        x: k1.position.x + (k2.position.x - k1.position.x) * alpha,
        y: k1.position.y + (k2.position.y - k1.position.y) * alpha
      },
      rotation: k1.rotation + (k2.rotation - k1.rotation) * alpha,
      scale: {
        x: k1.scale.x + (k2.scale.x - k1.scale.x) * alpha,
        y: k1.scale.y + (k2.scale.y - k1.scale.y) * alpha
      }
    };
  }

  update(deltaTime: number): void {
    this.currentTime += deltaTime;
    if (this.currentTime > this.duration) {
      this.currentTime = 0;
    }
  }
}
