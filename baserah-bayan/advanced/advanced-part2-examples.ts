import { EmotionalIntelligence, EmotionType } from "./emotional-intelligence";

export class AdvancedPart2Examples {
  static testEmotionalAI(): void {
    const ei = new EmotionalIntelligence();
    const emotion = ei.detectEmotion("I am happy!");
  }
}
