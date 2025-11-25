import { CharacterAnimation, Keyframe } from "./character-animation";
import { GeneralShapeEquation } from "./general-shape-equation";

export class TextToAnimation {
  parseText(text: string): CharacterAnimation | null {
    const shape = new GeneralShapeEquation("TextShape");
    const animation = new CharacterAnimation(shape);
    return animation;
  }

  generateKeyframes(description: string): Keyframe[] {
    return [];
  }
}
