import { EmotionDetector, Emotion } from "./emotion-detector";

export class EmpathySystem {
  detector: EmotionDetector;

  constructor() {
    this.detector = new EmotionDetector();
  }

  respondEmpathetically(text: string): string {
    const emotion = this.detector.detect(text);
    return `I understand you feel ${emotion}`;
  }
}
