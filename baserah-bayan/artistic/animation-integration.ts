import { SceneAnimator } from "./scene-animator";
import { PhysicsBasedAnimation } from "./physics-based-animation";

export class AnimationIntegration {
  sceneAnimator: SceneAnimator;
  physicsAnimation: PhysicsBasedAnimation;

  constructor() {
    this.sceneAnimator = new SceneAnimator();
    this.physicsAnimation = new PhysicsBasedAnimation();
  }

  update(deltaTime: number): void {
    this.sceneAnimator.update(deltaTime);
    this.physicsAnimation.update();
  }
}
