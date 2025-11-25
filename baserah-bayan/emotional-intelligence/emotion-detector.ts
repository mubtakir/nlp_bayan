import { MotherEquation, ObjectType } from "../core/mother-equation";

export enum Emotion {
  HAPPY = 'happy',
  SAD = 'sad',
  ANGRY = 'angry',
  NEUTRAL = 'neutral'
}

export class EmotionDetector extends MotherEquation {
  constructor(name: string) {
    super(ObjectType.ABSTRACT, name);
  }
  
  detect(text: string): Emotion {
    if (text.includes('سعيد') || text.includes('رائع')) return Emotion.HAPPY;
    if (text.includes('حزين') || text.includes('سيء')) return Emotion.SAD;
    if (text.includes('غاضب')) return Emotion.ANGRY;
    return Emotion.NEUTRAL;
  }
}
