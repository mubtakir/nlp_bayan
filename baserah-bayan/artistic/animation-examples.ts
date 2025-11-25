import { CharacterAnimation, Keyframe } from "./character-animation";
import { GeneralShapeEquation, ShapeType } from "./general-shape-equation";

export class AnimationExamples {
  static createBounce(): CharacterAnimation {
    const shape = new GeneralShapeEquation("Ball", ShapeType.CIRCLE);
    const animation = new CharacterAnimation(shape);
    
    animation.addKeyframe({time: 0, position: {x: 0, y: 10}, rotation: 0, scale: {x: 1, y: 1}});
    animation.addKeyframe({time: 1, position: {x: 0, y: 0}, rotation: 0, scale: {x: 1.2, y: 0.8}});
    animation.addKeyframe({time: 2, position: {x: 0, y: 10}, rotation: 0, scale: {x: 1, y: 1}});
    
    return animation;
  }
}
