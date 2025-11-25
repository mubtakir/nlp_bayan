import { GeneralShapeEquation } from "./general-shape-equation";
import { CharacterAnimation } from "./character-animation";

export class SceneAnimator {
  animations: Map<string, CharacterAnimation>;
  currentTime: number;
  playing: boolean;

  constructor() {
    this.animations = new Map();
    this.currentTime = 0;
    this.playing = false;
  }

  addAnimation(id: string, animation: CharacterAnimation): void {
    this.animations.set(id, animation);
  }

  play(): void {
    this.playing = true;
  }

  pause(): void {
    this.playing = false;
  }

  stop(): void {
    this.playing = false;
    this.currentTime = 0;
  }

  update(deltaTime: number): void {
    if (!this.playing) return;

    this.currentTime += deltaTime;
    for (const [id, animation] of this.animations) {
      animation.update(deltaTime);
    }
  }
}
